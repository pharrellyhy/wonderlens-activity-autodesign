# Matcher Runtime — Implementation Plan

**Date**: 2026-04-22
**Target repo**: `wonderlens-ai` (Python)
**Scope**: Build the interactive matcher that runs during multi-turn conversation, streams a live candidate ranking as context accumulates, and emits a final routing decision when the child takes a photo.
**Normative spec**: `program.md` §1.9 (autodesign repo). This plan implements that spec; it does not extend it.
**Companion doc**: `docs/matching_guideline.html` (autodesign repo) — read §01–§09 before implementing. The four worked traces in §05 are the golden test fixtures.

---

## Design decisions (locked)

| # | Decision | Chosen |
|---|---|---|
| 1 | When does matcher run? | **Every conversation turn** — incremental state, streamed candidate ranking |
| 2 | Does matcher own photo-prompt timing? | **No** — conversation layer decides when to ask for a photo |
| 3 | Target language/repo | **Python** in `wonderlens-ai` |
| 4 | Matching semantics (v0.1) | Pure exact-string overlap per §1.9; no embeddings / LLM fallback |
| 5 | Fixture data source | **Copied into `app/knowledge/`** (entities/, constellation/, games/); kept in sync with autodesign via a bootstrap script. No submodule. |
| 6 | State management (v0.1) | In-process dict keyed by `session_id`; no Redis |
| 7 | NER for conversation utterances | **Not** owned by matcher — upstream chat loop extracts signals, matcher consumes typed objects |
| 8 | Home for the matcher code | `app/modules/matcher/` (feature module in wonderlens-ai) |
| 9 | Home for the knowledge data | `app/knowledge/{entities,constellation,games}/` (structured knowledge layer) |

---

## What the matcher is (and isn't)

**Is**: a stateful service that maintains per-session ranked candidate games. Called on every conversation turn with new signals (child message, photo, property detector output). Returns the current top-k candidates + the most likely routing class (`mapped` / `bridged` / `property` / `none`).

**Isn't**: the conversation runtime, the vision recognizer, the property detector, a dialogue generator, or the photo-prompt decider. It is a ranker, not a planner.

---

## Where it fits in the conversation loop

```
┌─────────────────────────────────────────────────────────────────┐
│                       Conversation layer                        │
│                                                                 │
│   turn N:                                                       │
│     1. child sends utterance                                    │
│     2. upstream extractors produce structured signals           │
│        (entity mentions, topic mentions, photo, tier, …)        │
│     3. for each signal → MatcherService.update(session_id, sig) │
│     4. read Ranking back — top_pick, confidence, routing        │
│     5. use Ranking to pick next AI utterance                    │
│        (e.g., "should I ask for a photo now?" is chat's call)   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  MatcherService (this plan)                     │
│                                                                 │
│   in-memory: { session_id → SessionState }                      │
│   SessionState                                                  │
│     ├── accumulated signals                                     │
│     ├── tier, recent-game history                               │
│     ├── candidate ranking (top-k with scores + reasons)         │
│     └── routing class (mapped / bridged / property / none)      │
│                                                                 │
│   on startup: load entity YAMLs + constellation_map +           │
│     design §A.1 records from app/knowledge/games/catalog.yaml   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Contract with the conversation layer:**
- Conversation layer owns session lifetime (create, close).
- Conversation layer owns the decision to ask for a photo.
- Matcher emits a `Ranking` object on every `update()` call; conversation layer reads it as one input among many.
- Matcher is stateless w.r.t. the actual dialogue text — it never sees raw child strings, only structured signals.

---

## Repo layout

### Knowledge layer — `app/knowledge/`

Structured knowledge data that the matcher reads. **Copied from autodesign**, not submoduled. Kept in sync via a bootstrap script (see "Data sync strategy" below).

```
app/knowledge/
├── __init__.py
├── entities/
│   ├── _index.yaml                    # authoritative entity registry (mirrors autodesign)
│   ├── daily_objects/
│   │   ├── bath_toys.yaml             # rubber_duck, bath_toy, toy_boat, ...
│   │   ├── plush_toys.yaml            # teddy_bear, stuffed_bunny, ...
│   │   └── …
│   ├── animals/
│   ├── plants/
│   └── natural_phenomena/
├── constellation/
│   └── constellation_map.yaml         # mirror of autodesign's v0.3
└── games/
    └── catalog.yaml                   # compiled from autodesign designs/*.md §A.1 blocks
                                       # one record per game: id, title, category, pillar,
                                       # tier, entity_binding, bound_entity_id, a1_paths,
                                       # design_version, source_design_file
```

Rationale: wonderlens-ai ships with its own copy. Runtime does not reach outside the repo to load knowledge. This makes the service self-contained, deterministic, and deployable without network access to autodesign. The tradeoff is sync discipline — we need a clear bootstrap story (below).

### Matcher module — `app/modules/matcher/`

Runtime domain logic. Stateless at the module level; per-session state held inside `MatcherService`.

```
app/modules/matcher/
├── __init__.py                        # public exports (MatcherService, Signal types, Ranking)
├── service.py                         # MatcherService — public API
├── state.py                           # SessionState + apply(signal) dispatch
├── ranker.py                          # §1.9 dual-semantics + scoring + Ranking
├── signals.py                         # UtteranceSignal, PhotoSignal, PropertyDetectionSignal, ...
├── loader.py                          # reads app/knowledge/** into in-memory Library
├── config.py                          # ranker weights, thresholds, defaults
├── models/
│   ├── __init__.py
│   ├── entity.py                      # Entity, TierGuidance, path-flattening
│   ├── game.py                        # Game, GameBinding enum
│   ├── constellation.py               # ConstellationEntry, ConstellationMap (indexed)
│   └── library.py                     # Library — aggregator holding all three
└── tests/
    ├── fixtures/                      # small curated fixtures for unit tests
    ├── test_loader.py
    ├── test_models.py
    ├── test_ranker.py
    ├── test_session.py
    ├── test_service.py
    └── test_golden_traces.py          # ports the 4 HTML guideline traces — uses real app/knowledge/ data
```

### Conversation pipeline bridge — `app/pipeline/`

```
app/pipeline/
└── matcher_bridge.py                  # adapter: chat-turn pipeline signals → matcher.Signal objects
                                       # called by whatever chat-turn handler lives elsewhere in pipeline/
```

### Bootstrap / sync — `scripts/`

```
scripts/
└── sync_knowledge_from_autodesign.py  # pulls latest autodesign, copies YAMLs to app/knowledge/,
                                       # compiles games/catalog.yaml from §A.1 blocks of design .md files
```

---

## Data sync strategy

**The problem**: autodesign is the source of truth for entity YAMLs, constellation_map, and game §A.1 blocks. wonderlens-ai holds its own copy under `app/knowledge/`. These must not drift.

**v0.1 approach (manual-with-discipline)**:
1. `scripts/sync_knowledge_from_autodesign.py` takes an autodesign commit SHA or tag as input.
2. It shallow-clones autodesign to a temp dir, copies:
   - `data/mappings_dev20_0318/` → `app/knowledge/entities/`
   - `data/constellation_map.yaml` → `app/knowledge/constellation/constellation_map.yaml`
3. It parses each `designs/cat{1,5}/*_gold_spec.md` file, extracts the §A.1 code fence, and emits `app/knowledge/games/catalog.yaml` with one record per game:
   ```yaml
   - game_id: teddy_bear_cat1_gold
     title: "Teddy's Cozy Care Station"
     category: 1
     pillar: Nurture
     tier: T0
     entity_binding: bound
     bound_entity_id: daily_objects_teddy_bear
     a1_paths:
       - tier_0.appearance.color
       - tier_0.senses.surface_feel
       - tier_1.function.comfort_hugging
       - tier_1.function.pretend_friend
       - tier_1.function.sleep_routine_helper
     design_version: "1.0"
     source_design_file: "designs/cat1/teddy_bear_cat1_gold_spec.md"
     source_commit: "5706515"
   ```
4. The script writes a `app/knowledge/_source.yaml` file recording the autodesign commit SHA that this snapshot was taken from — for provenance.
5. Sync is triggered by a human running the script and opening a PR with the diff. CI validates shape on review.

**v0.2 candidates** (not part of this plan, but worth flagging):
- Autodesign emits a versioned `knowledge.tar.gz` artifact on every main merge; wonderlens-ai CI pulls and diffs weekly.
- Autodesign becomes a published Python package (`wonderlens-autodesign`) and wonderlens-ai depends on it via pyproject.
- Either approach removes the manual sync but adds deployment coupling.

**Sync discipline for v0.1**:
- Autodesign PR descriptions that touch `data/` or `designs/` must include a reminder to run the sync script in wonderlens-ai.
- `app/knowledge/_source.yaml` makes it obvious which autodesign snapshot is in use.
- `test_golden_traces.py` will catch whole classes of drift (if autodesign renames an attribute path that the traces depend on, tests fail).

---

## Data model

### `Entity`

Loaded from `data/mappings_dev20_0318/<domain>/<file>.yaml`. One YAML file may hold multiple entities.

```python
@dataclass(frozen=True)
class Entity:
    entity_id: str                       # "daily_objects_rubber_duck"
    entity_name: str                     # "Rubber Duck"
    domain: str                          # "daily_objects"
    parent_category: str                 # "toys"
    subcategory: str                     # "bath_toys"
    source_file: Path                    # authoritative yaml path
    tier_guidance: dict                  # raw nested structure
    flattened_paths: frozenset[str]      # {"tier_0.appearance.body_color", ...}
```

Flattening rule: recursively walk `tier_guidance` keys; emit `tier_N.<dim>.<attr>` paths. The `value` and `topics` sub-keys are NOT flattened — they're leaves, not paths.

### `Game`

Loaded from `designs/cat{1,5}/*_gold_*.md`. Both spec and prod variants refer to the same logical game — load spec for authoritative §A.1; fall back to prod if spec is absent.

```python
@dataclass(frozen=True)
class Game:
    game_id: str                         # "teddy_bear_cat1_gold"
    title: str                           # "Teddy's Cozy Care Station"
    category: int                        # 1 or 5
    pillar: Pillar                       # Enum
    tier: Tier                           # Enum — Recommended Tier
    entity_binding: GameBinding          # bound | parameterized | agnostic
    bound_entity_id: str | None          # set iff bound
    a1_paths: frozenset[str]             # §A.1 entity_attributes_covered
    design_version: str                  # "1.0"
    source_file: Path
```

`entity_binding` is derived: if `game_id` contains `_property_gold_` → parameterized; else bound. `agnostic` is reserved for future legacy cases; unused in v0.1.

`bound_entity_id` is derived from the filename pattern `{entity}_{cat}_gold_*.md` for bound games.

### `ConstellationMap`

Loaded from `data/constellation_map.yaml`. One-shot read on startup; in-memory indexed for O(1) lookups.

```python
@dataclass(frozen=True)
class ConstellationEntry:
    mapped_entity: str                   # "teddy_bear"
    category: int
    pillar: Pillar | None                # null for legacy
    gold_standard: Path | None
    bridge_type: str                     # "same_role" | ...
    bridge_strength: str                 # "very_strong" | "strong" | "moderate" | "weak"
    bridge_prompt_pattern: str           # with "[entity]" placeholder
    constellation: frozenset[str]        # neighbor labels

class ConstellationMap:
    entries_by_mapped_entity: dict[str, ConstellationEntry]
    entries_by_neighbor: dict[str, ConstellationEntry]   # index: neighbor → entry
                                                          # (built from constellation lists)
```

Indexing: on load, iterate entries; for each, add the mapped_entity to `entries_by_mapped_entity`; for each neighbor in `constellation`, add the entry to `entries_by_neighbor[neighbor]`. A neighbor may appear in multiple entries; indexer stores a list then in `lookup()` picks the highest `bridge_strength`.

### `Signal` hierarchy

What the conversation layer passes in. All signals carry a timestamp.

```python
@dataclass(frozen=True)
class Signal:
    at: datetime

@dataclass(frozen=True)
class UtteranceSignal(Signal):
    """Child said something; upstream NER extracted hints."""
    entity_mentions: frozenset[str]      # raw labels — "my bunny", "truck", …
    topic_mentions: frozenset[str]       # topic-level hooks from entity YAML topics[]
    sentiment: Literal["positive", "neutral", "negative"] | None

@dataclass(frozen=True)
class PhotoSignal(Signal):
    """Child took a photo; recognizer returned a label."""
    recognizer_label: str
    confidence: float
    image_metadata: dict                 # exif, bbox, etc. — opaque to matcher

@dataclass(frozen=True)
class PropertyDetectionSignal(Signal):
    """Property detector ran (after PhotoSignal with unmapped label)."""
    properties: dict[str, PropertyDetectorResult]
    # {"color": {"value": "red", "confidence": 0.88}, ...}

@dataclass(frozen=True)
class TierSignal(Signal):
    """Tier hint — usually once per session."""
    tier: Tier

@dataclass(frozen=True)
class HistorySignal(Signal):
    """Games played today, for recency penalty in ranking."""
    recent_game_ids: tuple[str, ...]     # ordered, most recent first
```

Conversation layer is responsible for all NER / hint extraction. The matcher never parses free text.

---

## `SessionState` — what accumulates

```python
@dataclass
class SessionState:
    session_id: str
    created_at: datetime

    tier: Tier | None = None
    accumulated_entity_hints: Counter = field(default_factory=Counter)   # {label: n_mentions}
    accumulated_topic_hints: Counter = field(default_factory=Counter)
    recent_sentiment: list[str] = field(default_factory=list)

    photo: PhotoSignal | None = None
    properties: PropertyDetectionSignal | None = None
    recent_game_ids: tuple[str, ...] = ()

    # Cache (invalidated on any update)
    _last_ranking: Ranking | None = None
    _dirty: bool = True
```

On every `update(signal)`:
1. Mutate the relevant field on `SessionState`.
2. Set `_dirty = True`.
3. Re-rank synchronously (cheap — see §ranker).
4. Store result in `_last_ranking`, return it.

---

## Ranker — implementing §1.9 dual-semantics

The ranker is called on every update. Input: a `SessionState` + the full in-memory game library. Output: a `Ranking`.

### Pseudocode

```python
def rank(state: SessionState, library: Library) -> Ranking:
    # 1. Determine routing class from current state
    routing = decide_routing(state, library)
    # routing ∈ {"mapped", "bridged", "property", "none", "undetermined"}

    # 2. Build candidate set per routing class
    candidates = build_candidate_set(state, library, routing)

    # 3. Apply dual-semantics filter (§1.9)
    filtered = [c for c in candidates if dual_overlap_passes(c, state, library)]

    # 4. Score each surviving candidate
    scored = [(c, score(c, state)) for c in filtered]
    scored.sort(key=lambda x: x[1], reverse=True)

    # 5. Wrap into Ranking with top_pick + confidence
    return build_ranking(scored, routing)
```

### Routing-class decision tree

```
if state.photo is None:
    # Pre-photo: work from conversation hints only
    if any entity hint matches a mapped entity → tentative routing "mapped"
    elif any entity hint matches a constellation neighbor → tentative routing "bridged"
    else → "undetermined"   # pre-photo, weak signal
elif state.photo.recognizer_label in library.entities:
    routing = "mapped"
elif state.photo.recognizer_label in library.constellation.entries_by_neighbor:
    routing = "bridged"
elif state.properties and has_dominant_property(state.properties):
    routing = "property"
else:
    routing = "none"
```

"Undetermined" is pre-photo state with no entity hint strong enough to commit — the matcher still ranks candidates using conversation hints as soft signals, but confidence is low and conversation layer shouldn't commit to a game yet.

### Candidate-set builders per routing class

- **mapped**: entity = `library.entities[recognizer_label]`; candidate set = bound games whose `bound_entity_id == entity.entity_id` ∪ parameterized templates whose any §A.1 path ∈ entity.flattened_paths.
- **bridged**: lookup constellation entry for the neighbor label; proxy_entity = `library.entities[entry.mapped_entity]`; candidate set = same as mapped, but scored against proxy_entity with a `bridge_strength` boost.
- **property**: entity = None; candidate set = parameterized templates whose any §A.1 path suffix matches a dominant-property key from `state.properties`.
- **none**: empty candidate set → fallback signal to conversation layer.
- **undetermined**: same as "mapped" if any entity hint partially matches a known entity, but with heavy confidence discount.

### Dual-semantics filter

```python
def dual_overlap_passes(game: Game, state: SessionState, library: Library) -> bool:
    entity_paths = resolve_entity_paths(state, library)   # the flattened_paths of mapped or proxy entity
    if game.entity_binding == GameBinding.BOUND:
        return game.a1_paths <= entity_paths   # strict subset
    elif game.entity_binding == GameBinding.PARAMETERIZED:
        return bool(game.a1_paths & entity_paths)   # any one path in common
    else:
        return False   # agnostic reserved; not used in v0.1
```

### Score function

Weighted sum. Weights are tunable but shipped with sensible defaults.

```python
def score(game: Game, state: SessionState, entity: Entity | None = None) -> float:
    s = 0.0
    s += w_coverage * len(game.a1_paths & entity.flattened_paths) if entity else 0
    s += w_bound_bonus if game.entity_binding == BOUND else 0
    s += w_pillar_fit * pillar_affinity(state, game.pillar)
    s -= w_tier_mismatch * tier_distance(state.tier, game.tier)
    s += w_bridge_strength * strength_weight(bridge_strength) if routing == "bridged" else 0
    s -= w_recency * (1 if game.game_id in state.recent_game_ids else 0)
    s += w_entity_hint * entity_hint_boost(state, game)   # pre-photo only
    return s

DEFAULTS = {
    "w_coverage": 1.0,
    "w_bound_bonus": 3.0,
    "w_pillar_fit": 2.0,
    "w_tier_mismatch": 1.5,
    "w_bridge_strength": 1.0,
    "w_recency": 2.0,
    "w_entity_hint": 0.5,
}

STRENGTH_WEIGHT = {"very_strong": 1.0, "strong": 0.8, "moderate": 0.5, "weak": 0.3}
```

Weights live in `config.py` so they're tunable without code churn.

### `Ranking` output

```python
@dataclass(frozen=True)
class Candidate:
    game_id: str
    game_title: str
    score: float
    pillar: Pillar
    routing: str                        # which class pushed it in
    reason: str                         # one-line human-readable

@dataclass(frozen=True)
class Ranking:
    candidates: tuple[Candidate, ...]   # top-k, sorted by score desc
    top_pick: Candidate | None          # None if candidates is empty
    confidence: float                   # 0..1 — derived from score gap + routing class
    routing_class: str                  # "mapped" | "bridged" | "property" | "none" | "undetermined"
    entity_resolved: str | None         # mapped entity id if routing is mapped/bridged
    bridge_applied: str | None          # mapped_entity id if bridged
    diagnostics: dict                   # for logging — raw scores, filter drops, etc.
```

Conversation layer reads `top_pick`, `confidence`, `routing_class` to decide next move.

**Confidence heuristic**:
- routing == "mapped" and bound game top → 0.95
- routing == "bridged" with strong/very_strong strength → 0.85
- routing == "property" with dominant property confidence > 0.8 → 0.75
- routing == "undetermined" → 0.3 × max(score-normalized)
- routing == "none" → 0.0

Tune during integration.

---

## Public API

```python
class MatcherService:
    def __init__(self, knowledge_root: Path = Path("app/knowledge"), config: Config = DEFAULT_CONFIG):
        """Load all data on startup. Blocking. ~100ms for 60 games + 20 entities."""
        self.library = Library.load(knowledge_root)
        self.config = config
        self._sessions: dict[str, SessionState] = {}

    def create_session(self, child_tier: Tier, child_id: str) -> str:
        """Returns session_id. Idempotent on child_id for the day."""

    def update(self, session_id: str, signal: Signal) -> Ranking:
        """Feed one signal, get the updated ranking back. < 10ms."""

    def peek(self, session_id: str) -> Ranking:
        """Read current ranking without updating. For conversation-layer debug."""

    def close_session(self, session_id: str) -> None:
        """Free state. Idempotent."""

    def health(self) -> dict:
        """Liveness probe. Returns {libraries_loaded: bool, ...}."""
```

All methods are sync. If wonderlens-ai is async, wrap in `asyncio.to_thread()` at the chat-loop boundary — the matcher itself has no I/O after startup.

---

## Phased implementation plan

Six phases. Each is a single PR in wonderlens-ai.

### Phase 0 — Skeleton + knowledge bootstrap

- Create `app/modules/matcher/` package layout and `app/knowledge/{entities,constellation,games}/` directories.
- Add `scripts/sync_knowledge_from_autodesign.py` implementing the sync process (see "Data sync strategy").
- Run the sync script once against autodesign's current `main` HEAD, committing the initial snapshot. `app/knowledge/_source.yaml` records the commit SHA.
- Set up matcher package in `pyproject.toml`, ruff/mypy config, pytest discovery.
- CI: matrix runs `mypy --strict app/modules/matcher` + `pytest app/modules/matcher/`.
- **Acceptance**: `poetry run pytest app/modules/matcher/` passes on an empty test suite. `app/knowledge/entities/daily_objects/bath_toys.yaml` and `app/knowledge/games/catalog.yaml` exist and parse.

### Phase 1 — Loader + models

- Implement `Entity`, `Game`, `ConstellationEntry`, `ConstellationMap`, `Library` in `app/modules/matcher/models/`.
- `loader.py`:
  - Walk `app/knowledge/entities/**/*.yaml`, parse entities.
  - Parse `app/knowledge/constellation/constellation_map.yaml`.
  - Parse `app/knowledge/games/catalog.yaml` (flat list of game records — no markdown parsing in wonderlens-ai; §A.1 extraction happens in the sync script, not at runtime).
  - `entity_binding` is read directly from the catalog record (already derived by the sync script).
- **Acceptance**: loading the bundled knowledge yields 20 entities, 25 constellation entries, 60 games. Unit tests verify the derived `flattened_paths` for `rubber_duck` and `teddy_bear`. Load completes in under 300ms on cold start.

### Phase 2 — Signal types + `SessionState`

- Implement all `Signal` subclasses.
- `SessionState` with `apply(signal)` dispatch per signal type.
- Counter-based accumulation for entity/topic hints.
- **Acceptance**: passing a sequence of 4 signals (Utterance, Photo, PropertyDetection, History) produces expected `SessionState` fields; unit tests for each signal type.

### Phase 3 — Ranker + dual-semantics

- Implement `decide_routing`, `build_candidate_set`, `dual_overlap_passes`, `score`, `Ranking`.
- `config.py` with default weights.
- Routing class covered: `mapped`, `bridged`, `property`, `none`, `undetermined`.
- **Acceptance**: golden unit tests for each routing path — e.g. `rubber_duck` photo → ranking where `top_pick.game_id == "rubber_duck_cat1_gold"` with confidence > 0.9.

### Phase 4 — `MatcherService` public API

- Wrap ranker + state in `MatcherService`.
- Session lifecycle, thread-safe access to `self._sessions` via `threading.Lock` (keep simple; upgrade to async-safe later if needed).
- **Acceptance**: end-to-end test instantiates service, creates session, feeds a 5-signal conversation transcript, asserts final ranking matches guideline Trace 1 output.

### Phase 5 — Golden trace tests

- Port all four HTML guideline traces (`MAPPED`, `BRIDGED`, `PROPERTY`, `NO_MATCH`) as pytest cases in `test_golden_traces.py`.
- Each test: set up SessionState, feed exact signals, assert top_pick + routing_class + bridge_applied match the guideline.
- **Acceptance**: all four traces pass. If one fails, either the plan doc or the guideline is wrong — fix whichever is canonical.

### Phase 6 — Chat-loop integration stub

- Document how the conversation layer calls the matcher (sequence diagram + code example).
- Add `app/pipeline/matcher_bridge.py` that bridges the chat-turn pipeline's internal signal format to the matcher's `Signal` types.
- Provide a minimal fake chat loop in `examples/` for local manual testing.
- **Acceptance**: a developer can run `python -m examples.fake_chat` and walk through a 5-turn conversation, seeing the ranking update on each turn.

---

## Testing strategy

Three layers.

1. **Unit**: per-module. Loader, each signal type, ranker scoring, state transitions. Fast (< 1s suite).
2. **Golden traces**: the four HTML guideline traces as integration tests. If the guideline ships new traces, they land here too.
3. **Property tests** (optional v0.2): hypothesize random entity+game combos and assert dual-overlap invariants (e.g., a bound game always passes strict overlap against its bound entity).

**Fixture discipline**: golden trace tests use the real pinned autodesign data, not toy fixtures. Other unit tests use small curated fixtures under `tests/fixtures/`.

---

## Chat-loop integration contract

```python
# Pseudocode inside wonderlens-ai chat loop
matcher = MatcherService(knowledge_root=Path("app/knowledge"))

async def handle_turn(session_id: str, turn: ChatTurn) -> ChatReply:
    # 1. Extract signals from turn via upstream NER
    signals = await extractor.extract(turn)

    # 2. Update matcher per signal
    ranking = None
    for sig in signals:
        ranking = matcher.update(session_id, sig)

    # 3. Use ranking to shape reply
    if ranking.routing_class == "none":
        return await fallback_dialogue(turn)
    if ranking.confidence < 0.4:
        return await probe_for_more_signal(turn, ranking)   # ask a clarifying question
    if ranking.routing_class in {"mapped", "bridged", "property"} and ranking.confidence > 0.7:
        return await initiate_game(ranking.top_pick, ranking)

    # Otherwise — continue conversation, carry ranking along
    return await continue_conversation(turn, ranking)
```

Key point: the matcher emits a `Ranking`; chat loop decides what to do with it. Photo-prompt decisions, fallback routing, and game-initiation timing all live in chat logic.

---

## Acceptance criteria (end-to-end)

1. `MatcherService` loads the pinned autodesign commit's 20 entities + 25 constellation entries + 60 games in under 300ms on cold start.
2. `update()` round-trip latency < 10ms p99 on a warm service.
3. All four guideline traces reproduce exactly — same `top_pick`, `routing_class`, and `bridge_applied`.
4. Adding a new entity YAML upstream (via autodesign PR → run `scripts/sync_knowledge_from_autodesign.py` → commit the diff) does not require matcher code changes. Automated sync on autodesign merge is a v0.2 follow-up.
5. Weight defaults can be tuned in `config.py` without touching ranker logic.
6. `mypy --strict` passes for the matcher package.

---

## Out of scope (explicitly)

- Embedding-based recognizer-label or attribute-path fallback (known limitation per guideline §09).
- LLM fallback before the off-ramp.
- Cross-session learning / personalization.
- Hot-reload of autodesign data without restart.
- Property detector integration (assumed implemented upstream; matcher accepts `PropertyDetectionSignal`).
- Recognizer integration (same — upstream owns it).
- §A.2 Constellation Adaptation — the matcher picks the game; runtime adaptation happens in the chat/dialogue layer that reads §A.2 text from the design file.
- Matching guideline HTML update to reflect the live matcher — if/when implemented, re-run the golden traces and regenerate the preview doc's JSON fixtures.

---

## Open questions (flag before starting phase 1)

1. **Sync automation**: v0.1 ships with a manual-but-scripted sync (`scripts/sync_knowledge_from_autodesign.py`). The open question is when/how often to run it — on every autodesign `main` merge? Weekly? On-demand only? Proposed v0.2 path is a CI hook that opens a sync PR automatically. Confirm cadence before phase 0.
2. **Session persistence**: in-process dict dies on restart. For v0.1 that's acceptable (sessions are short). v0.2 should add Redis / PostgreSQL persistence. Plan needs the team to decide storage.
3. **Concurrent sessions**: how many simultaneous users? If > 1000 active sessions, in-process state may need sharding. Not a v0.1 concern but size the machine appropriately.
4. **Pillar affinity source**: the score function uses `pillar_affinity(state, game.pillar)` but the plan leaves the function stubbed. Proposed v0.1 impl: read `state.recent_sentiment` + accumulated topic hints' pillar-maps from entity YAML. But this may need a product-side signal (child's curiosity profile) that doesn't exist yet. Ship with `pillar_affinity = 1.0` uniform if no signal is available, tune later.
5. **Who extracts entity hints from child utterances?** This plan assumes upstream (wonderlens-ai's own chat layer). If that extractor already exists elsewhere in `app/pipeline/` or `app/llm/`, point `matcher_bridge.py` at it. If not, build it as a separate module — **not** inside `app/modules/matcher/`. Confirm ownership before phase 6.
6. **`app/knowledge/games/catalog.yaml` vs splitting per-category**: shipping all 60 games as a single YAML keeps the runtime simple (one file parse). Alternative: `app/knowledge/games/cat1.yaml` + `cat5.yaml` for easier diffing. Proposed v0.1: single catalog.yaml, revisit if the file gets unwieldy (> 3000 lines).

---

## File deliverables (summary)

### Matcher module — `app/modules/matcher/`
| File | Purpose | Approx. lines |
|---|---|---|
| `__init__.py` | Public exports (MatcherService, Signal types, Ranking) | 20 |
| `loader.py` | Load `app/knowledge/**` into in-memory Library | 150 |
| `models/__init__.py` | Module exports | 10 |
| `models/entity.py` | `Entity` + path flattening | 80 |
| `models/game.py` | `Game` + GameBinding enum | 60 |
| `models/constellation.py` | `ConstellationMap` + indexed lookups | 90 |
| `models/library.py` | `Library` aggregator | 40 |
| `signals.py` | Signal hierarchy (Utterance, Photo, PropertyDetection, Tier, History) | 80 |
| `state.py` | `SessionState` + `apply(signal)` dispatch | 120 |
| `ranker.py` | Routing decision + dual-semantics filter + scoring + `Ranking` | 250 |
| `service.py` | `MatcherService` public API | 120 |
| `config.py` | Weights + thresholds + defaults | 40 |
| `tests/` | Unit tests + golden trace tests | 400 |
| **Subtotal** | | **~1460** |

### Knowledge layer — `app/knowledge/`
| Path | Purpose | Notes |
|---|---|---|
| `entities/_index.yaml` | Entity registry (mirrors autodesign) | ~30 lines |
| `entities/**/*.yaml` | ~10 YAML files across domains | copied from autodesign `data/mappings_dev20_0318/` |
| `constellation/constellation_map.yaml` | Bridging graph | copied from autodesign |
| `games/catalog.yaml` | Compiled §A.1 records for all 60 games | ~1200 lines — generated by sync script |
| `_source.yaml` | Autodesign commit provenance | ~6 lines |

### Sync tooling
| File | Purpose | Approx. lines |
|---|---|---|
| `scripts/sync_knowledge_from_autodesign.py` | Pull autodesign data + compile games/catalog.yaml | 200 |

### Pipeline integration
| File | Purpose | Approx. lines |
|---|---|---|
| `app/pipeline/matcher_bridge.py` | Adapter between chat-turn pipeline and matcher | 80 |

### Examples
| File | Purpose | Approx. lines |
|---|---|---|
| `examples/fake_chat.py` | Manual integration harness for local dev | 80 |

**Total new code**: ~1820 lines (matcher + sync + bridge + example). Plus ~1250 lines of YAML copied/compiled into `app/knowledge/`.

---

## Reading order for the implementer

1. This plan.
2. `docs/matching_guideline.html` §01–§09 in the autodesign repo (the companion doc).
3. `program.md` §1.9 in the autodesign repo (normative matcher spec).
4. Five representative fixture files: `data/constellation_map.yaml`, `data/mappings_dev20_0318/daily_objects/bath_toys.yaml`, `data/mappings_dev20_0318/daily_objects/plush_toys.yaml`, `designs/cat1/rubber_duck_cat1_gold_spec.md`, `designs/cat1/detail_detective_property_gold_spec.md`.

---

## Revnote

- v0.1 · 2026-04-22 · Inaugural plan — six-phase implementation of an interactive, per-turn matcher in wonderlens-ai (Python). Matcher runtime lives at `app/modules/matcher/`; knowledge data (entity YAMLs, constellation map, compiled game catalog) lives at `app/knowledge/{entities,constellation,games}/` copied in from autodesign via `scripts/sync_knowledge_from_autodesign.py` — no submodule. String-match-only v0; embedding/LLM fallback deferred. Four guideline traces are the golden tests. Awaiting implementer sign-off before phase 0.
