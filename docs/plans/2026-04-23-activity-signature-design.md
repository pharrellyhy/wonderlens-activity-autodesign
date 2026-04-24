# Activity Signature — Design Spec

**Date:** 2026-04-23
**Status:** Approved design surface; implementation in progress
**Template 0 authority:** `docs/template_0_preview.html` §04 (tag block)
**Background brief:** `docs/plans/2026-04-23-progression-background-brief.md` (related systems overview)

---

## 1 · Context

### 1.1 The problem — conversation-to-activity coherence gap

Current activity selection (Tier A → B → P cascade) matches on **entity-level** signals:
- Tier A: exact entity gold standard
- Tier B: entity-to-gold-standard constellation
- Tier P: any detected visual property from the photo

None of these signals check whether the selected activity is **thematically coherent** with the conversation that just happened. Concrete example:

> Child photographs a red pen → 5-turn conversation about color → Tier P detects "round-ish" shape → activity picked: "find three round things". The pen shifts from *subject* to *exemplar of round*; the conversation's color focus is dropped without acknowledgement. Transition feels abrupt.

The activity was structurally eligible (Tier P matched on a valid property) but editorially wrong (wrong observation angle for the conversation). The tag block has no field that lets the matcher know which dimension of the entity the activity actually attends to.

### 1.2 Why the existing tag block isn't enough

Current tag block fields (§04, as of v0.3):
- `entity`, `category`, `attributes`
- `key_concepts`, `related_concepts`, `atl_skills`, `transdisciplinary_theme`
- `kud.know`, `kud.understand`, `kud.do`
- `progression.topic_axis`, `progression.difficulty_level`
- `caregiver_role`
- Matchability (v0.3): `entity_binding`, `entity_class`, `tier_range`

What's missing:
1. **What the activity attends to** — the attribute-level focus (color, shape, texture, function, origin, …). `topic_axis` is the IB axis (Form/Function/…); the sub-dimension inside Form is unspecified.
2. **What the child will do** — the mechanic (enumerate, collect, compare, voice, …). `game_style` hints at this but conflates it with pillar styling.
3. **How the photographed entity participates** — subject vs exemplar vs catalyst vs reference. Currently implicit; when it shifts (photo was the topic, activity uses photo as an example of a category), the runtime has no way to surface the pivot.
4. **What conversation themes the activity naturally extends** — no bridge signal for the upstream matcher to prefer coherent continuations.

### 1.3 Why now

Three triggers converged:
- **Progression runtime** (2026-04-21 plans) added per-axis state. Authors now ask "at what *angle* of Form is Mia at L2?" — the current schema can't distinguish Form/color L2 from Form/shape L2.
- **Parent dashboard** curiosity radial design wants to split axis-exposure by attribute angle (8 color sessions vs 2 shape sessions tells a different story than "10 Form sessions").
- **Matchability tags** (2026-04-20) answered "CAN this entity run this activity?" but left "SHOULD this activity follow this conversation?" unanswered.

---

## 2 · Scope

### In scope
- New `activity_signature` block in Template 0 §04 tag block with 8 required fields plus optional `role_pivot_note` (below)
- Closed vocabularies for `observation_angle`, `mechanic`, `entity_role`
- Per-game directory restructure (`activities/<game_id>/`) replacing flat `gold_standards/*.md` + `property_bridges/*.md` layout
- Game loader update (parses per-game dir)
- Matcher scoring bonus for `observation_angle` ↔ `conversation_signature.dominant_angle` match
- Conversation-module signature addition: `dominant_angle` output field
- Runtime write of `recap.latest.yaml` + `dashboard.latest.yaml` into the local game dir on session end (Option A — last-run cache)
- Child recap payload extension (reads new fields)
- Parent dashboard payload extension (angle-resolved radial + exploration matrix)
- Template 0 §04 preview HTML update (show the new block)
- Both repos (`wonderlens-ai` backend + `wonderlens-activity-fullstack-demo` prototype); shared vocabulary, same runtime behavior

### Out of scope (explicit deferrals)
- **LLM-based `dominant_angle` classification from raw conversation transcripts.** V1 derives dominant_angle via a simple keyword-matching heuristic. A proper LLM classifier is follow-up work.
- **Child recap UI / parent dashboard UI changes.** This plan updates the payloads; the React/iOS surfaces that consume them are separate plans.
- **Backfilling activity_signature for the full catalog.** V1 includes the schema + a migration pass for 5 seed activities; remaining backfills are mechanical follow-ups.
- **Cumulative session logs in the per-game dir.** `.latest.yaml` is last-run only; historical queries go through the DB.
- **Entity role-change detection heuristics beyond `entity_role` field reads.** The runtime surfaces the pivot via `role_pivot_note` when authored; it does not auto-detect pivots at runtime.
- **Vocabulary extension beyond the V1 closed sets.** If a game needs an angle/mechanic not in the enum, it's a spec conversation, not a code change.

### Explicitly deferred to a future iteration
- **New sibling of `activity_signature` for synthesis/output expectations** (what the child is expected to produce). Currently folded into `mechanic` + `kud.do`.
- **Multi-angle activities** (an activity that legitimately attends to color AND shape). V1 requires a single primary `observation_angle` per activity; compound activities get the dominant one.

---

## 3 · The new tag block fields

### 3.1 Schema (YAML)

```yaml
activity_signature:
  # ── Layer 1: editorial identity (fixed at authoring, read by upstream matcher) ──
  observation_angle: color          # required, enum — §3.2
  mechanic: collect                 # required, enum — §3.3
  entity_role: exemplar             # required, enum — §3.4
  bridge_prerequisites:             # required
    primary:   [color]              # 1-3 closed observation_angle values; strongest transition signal
    secondary: [pattern, visibility] # 0-3 values; enum values score, free-form descriptors document nuance

  # ── Layer 2: presentation (templated at authoring, rendered at session start) ──
  focal_attribute: red              # required; may be a {placeholder} for parameterized activities
  intro: "The child walks around to find three more things a {pet_type} needs — using the photographed {entity} as a starting point."  # required, one sentence, observer-facing — §3.5
  preview_label:  "Find three red things!"         # required, short (< 40 chars), child-facing
  preview_prompt: "You noticed the red..."         # required, single sentence, child-facing
  role_pivot_note: |                # optional, used when entity_role shifts from conversation's role
    The ladybug was our subject during the chat; now it becomes an
    EXAMPLE of red — we're going to find more reds like it.
```

All fields go under a single `activity_signature` key in the existing Template 0 §04 tag block. They do not replace any existing fields.

**Two-layer distinction:** Layer 1 fields are read by the upstream matcher to score candidate activities against the conversation signature — they never change per session. Layer 2 fields are author-written templates that the runtime renders at session start using concrete entity data from the photo. The matcher reads Layer 1 only. Downstream surfaces read rendered Layer 2 strings for display, and also store or render selected Layer 1 classifications (`observation_angle`, `mechanic`, `entity_role`) for recap and dashboard aggregation.

### 3.2 Observation angle — closed enum (10 values)

```yaml
observation_angle:
  # Visual/physical
  - color       # red, blue, green, … — surface color
  - shape       # round, pointy, flat, long, curvy
  - size        # tiny, small, big, huge; relative size
  - texture     # smooth, rough, fuzzy, shiny
  - material    # metal, wood, plastic, fabric, stone, glass
  - pattern     # stripes, spots, zigzag, checkered, plain

  # Functional/conceptual
  - function    # what it does, how it works, what it's for
  - origin      # where it came from, who made it, natural vs made
  - behavior    # how it moves, acts, interacts; lives/not-lives
  - state       # condition — worn/fresh, full/empty, alive/asleep
```

**Rationale:** 6 visual/physical + 4 functional/conceptual. The split is a reading aid for authors, not a classification. **Observation_angle is orthogonal to `topic_axis`** — all 7 IB Key Concepts can use all 10 angles. Picking an angle does NOT fix the axis; picking an axis does NOT fix the angle. Examples (same entity, angle = `color`):

| topic_axis | Activity framing |
|---|---|
| Form | *"notice the RED spots on the ladybug"* |
| Function | *"what does the red DO? — it warns predators"* |
| Causation | *"why is it red, not green?"* |
| Change | *"does the red fade as the ladybug ages?"* |
| Connection | *"what OTHER things share this red warning?"* |
| Perspective | *"how does a bird see this red vs a human?"* |
| Responsibility | *"the red means 'don't eat me' — how should we respond to bugs with warning colors?"* |

A common confusion: earlier drafts of this spec implied visual angles "belong to" Form and functional angles "belong to" Function/Causation. That's wrong. The Cat Food → Pet Caretaker's Mission example uses `observation_angle: function` with `topic_axis: responsibility`; no axis owns any angle. The 4 conceptually-richer axes (Change, Connection, Perspective, Responsibility) are the **most angle-flexible** because they're interpretive stances on attributes rather than attribute types themselves.

**Closure discipline:** these 10 are authoritative. Adding an 11th requires a spec update + migration of existing games. If an activity's angle doesn't fit, pick the closest match and note the delta in `spec.md`.

### 3.3 Mechanic — closed enum (8 values)

```yaml
mechanic:
  - enumerate   # "name the parts", "list the attributes"
  - compare     # "which is bigger?", "how are these alike?"
  - collect     # "find three things that are [X]"
  - sort        # "put these into groups"
  - voice       # "what would the ladybug say?"
  - build       # "make something with this"
  - predict     # "what happens if…?"
  - narrate     # "tell me the story of this"
```

**Rationale:** each maps 1:1 to an established game_style family. `collect` is the Cat5 mission mechanic; `voice` maps to voice_stage/ensemble_show; `predict` to prediction_lab; etc. Authors already think in these buckets; the tag just makes it explicit.

### 3.4 Entity role — closed enum (4 values)

```yaml
entity_role:
  - subject       # the activity is ABOUT this entity specifically
  - exemplar      # this entity is one EXAMPLE of a broader category the activity explores
  - catalyst      # this entity sparked the question but the activity is elsewhere
  - reference     # this entity is source material for building/creating something new
```

**Rationale:** makes the pen→round-things pivot explicit. When `entity_role` in the activity differs from the conversation's role for this entity (usually `subject`), the runtime surfaces the pivot via `role_pivot_note`.

| Conversation role | Activity role | Example | Pivot surfaced? |
|---|---|---|---|
| subject | subject | Ladybug chat → ladybug voice-stage | no (continuity) |
| subject | exemplar | Ladybug chat → "find three red things" | yes — "ladybug becomes an example of red" |
| subject | catalyst | Ladybug chat → building a bug hotel | yes — "ladybug inspired us to build something new" |
| subject | reference | Ladybug chat → drawing a pattern using spots | yes — "using the ladybug's spots as our pattern guide" |

### 3.5 intro — one-sentence observer-facing description

A single sentence, third-person, describing what the child does. Serves parent-dashboard subtitles, pre-activity parent previews, debug logs, and author tooling — anywhere an **observer** (not the child) needs to understand what the activity is.

**Constraints:**
- One sentence, hard limit
- Third-person observer framing — *"The child walks around to find..."*, not *"You walk around..."* (that's preview_prompt's job) and not *"The activity tests..."* (too abstract)
- Rendered length target ≤ 120 chars; cap 160 for dashboard card fit
- Template-layer: authored with `{placeholders}`, rendered at session start
- Mentions the mechanic implicitly via verb — *"walks around to find"* → collect, *"gives the entity a voice"* → voice, *"makes up a story about"* → narrate
- Tier-agnostic — same intro for T0/T1/T2

**Example templates (authored) → rendered (at session start with cat food photo):**

| activity_id | Template | Rendered |
|---|---|---|
| color_scout_property | `"The child finds three {color} things using the {entity} as a starting example."` | *"The child finds three red things using the ladybug as a starting example."* |
| voice_stage_lion | `"The child gives the {entity} a voice and personality to match its presence."` | *"The child gives the lion a voice and personality to match its presence."* |
| pet_caretakers_mission | `"The child walks around to find three more things a {pet_type} needs — using the photographed {entity} as a starting point."` | *"The child walks around to find three more things a cat needs — using the photographed cat food as a starting point."* |

**Surfaces that consume the rendered intro:**
- `session_state.rendered_intro` in the `/activity/select` + `/activity/start` responses
- `recap.latest.yaml` (included at session end)
- `dashboard.latest.yaml.session.intro` (feeds the parent dashboard timeline card)
- Debug logs: `[session-uuid] activity started: <rendered_intro>`
- Author-tooling game catalog: subtitle under `display_label`

**Back-compat:** if `activity_signature.intro` is absent, the loader falls back to `GameDefinition.plain_description`. Newly-authored games MUST include `intro`; legacy games keep working until migrated.

**Matcher impact (V1):** none. Intro is pure surfacing; matching uses Layer 1 fields only. Future V2 could use intro embeddings for semantic-similarity fallback when no structured match scores above threshold — noted as out-of-scope here.

### 3.6 focal_attribute

The specific attribute value parameterized into the activity. Flat string, usually drawn from the entity's `attributes` list or a property the vision pipeline detected. Bound/non-visual games may use an author-stable descriptor when the focal trait is not a literal detected property (for example `lion_voice`).

Example usage:
- Activity `observation_angle: color`, entity = ladybug → `focal_attribute: red`
- Activity `observation_angle: shape`, entity = ladybug → `focal_attribute: round_oval`
- Activity `observation_angle: pattern`, entity = ladybug → `focal_attribute: spots`

The runtime reads this into prompts: *"find three RED things"* not *"find three things that share a color with the ladybug"* (too abstract for T0/T1). Required field; no enum (too many legitimate values).

### 3.7 bridge_prerequisites

Lists conversation themes the activity naturally extends. Two tiers:
- `primary` — 1-3 closed `observation_angle` values; the strongest transition signal, scored against `dominant_angle` and `secondary_angles`
- `secondary` — 0-3 values; closed enum values may be scored later, while free-form descriptors are editorial notes only

```yaml
bridge_prerequisites:
  primary:   [color]
  secondary: [pattern, visibility]
```

`primary` MUST use the same vocabulary as `observation_angle` (the 10 values in §3.2). `secondary` SHOULD use that vocabulary when possible, but may include non-enum descriptors if they are editorially meaningful (e.g., `visibility` — a synthesis of color + pattern in the ladybug case). V1 matcher scoring ignores non-enum secondary values.

### 3.8 preview_label + preview_prompt

Short strings the upstream app can display during the conversation → activity transition.

- `preview_label` — button/card title, <40 chars. Example: *"Find three red things!"*
- `preview_prompt` — one-sentence AI bridge line. Example: *"You noticed the red of the ladybug. Let's go find more red things together."*

V1: both are author-written. Future: auto-generate from templates.

### 3.9 role_pivot_note

Optional. Used only when the activity's `entity_role` differs from the conversation's (most common transitions: subject → exemplar/catalyst/reference). One-sentence explanation the runtime can surface to make the pivot explicit.

---

## 4 · Per-game directory restructure

### 4.1 Current layout (source of today's pain)

```
wonderlens-activity-autodesign/
└── designs/                              # flat directory of .md files
    ├── banana_cat1.md
    ├── bicycle_cat5.md
    └── ...  (24 games, each a single markdown file)

wonderlens-ai/app/modules/activity/games/  # synced from autodesign
├── gold_standards/
│   └── *.md  (15 gold-standard games)
└── property_bridges/
    └── *.md  (14 property-bridge templates)
```

Problems:
- Related artifacts scattered across multiple files (spec vs prod content vs runtime data)
- No natural home for the new `activity_signature` YAML, recap template, dashboard template
- Adding matchability tags + activity signature keeps bolting fields onto the same `.md` frontmatter — scaling poorly
- Reviewers can't see "everything about this game" in one folder

### 4.2 New layout (proposed)

Autodesign (source of truth):

```
activities/
└── <game_id>/                             # e.g. color_scout_property, voice_stage_lion
    ├── spec.md                            # authoring design — why, for whom, pedagogy, IB mapping
    ├── prod.md                            # runtime content — dialogue templates, step instructions, creative slots
    ├── tag_block.yaml                     # Template 0 §04 tag block (entity, KCs, progression, matchability, activity_signature)
    ├── recap.template.yaml                # child recap payload shape — what this game CAN produce
    └── dashboard.template.yaml            # parent dashboard fragment shape
```

Consumer repos (wonderlens-ai, fullstack-demo) — synced read-only copy + runtime additions:

```
<repo>/activities/<game_id>/
    ├── spec.md                            # read-only mirror from autodesign
    ├── prod.md                            # read-only mirror
    ├── tag_block.yaml                     # read-only mirror
    ├── recap.template.yaml                # read-only mirror
    ├── dashboard.template.yaml            # read-only mirror
    ├── recap.latest.yaml                  # ◆ runtime-written on session end (Option A: overwrite)
    └── dashboard.latest.yaml              # ◆ runtime-written on session end (Option A: overwrite)
```

### 4.3 File responsibilities

| File | Hand-edited? | Purpose |
|---|---|---|
| `spec.md` | yes (autodesign only) | Authoring intent — why this game exists, what pedagogical theory it rests on, IB axis/rung/concept mapping, age-tier rationale. Prose. Reviewed by educators. |
| `prod.md` | yes (autodesign only) | Runtime content — dialogue templates (hook/rules/rounds/celebrate/closing), step_instructions, creative_slots, pillar-specific dialogue flavor. Reviewed by script authors. |
| `tag_block.yaml` | yes (autodesign only) | Structured metadata the matcher + downstream surfaces read. Reviewed by eng + authors. |
| `recap.template.yaml` | yes (autodesign only) | Shape + example of the child-recap payload this game produces. Reviewers see "what the child will be told." |
| `dashboard.template.yaml` | yes (autodesign only) | Shape + example of the parent-dashboard fragment. Reviewers see how this game contributes to the running dashboard. |
| `recap.latest.yaml` | **no** — runtime write | Last-run snapshot, written on session end. Committed when useful for review, annotated "auto-generated — do not hand-edit." |
| `dashboard.latest.yaml` | **no** — runtime write | Same. |

### 4.4 Sync discipline (autodesign ↔ consumer repos)

- Autodesign is **source of truth** for hand-edited files (`spec.md`, `prod.md`, `tag_block.yaml`, `*.template.yaml`)
- Consumer repos receive a read-only copy via a sync script (new in this plan) or manual `cp -r activities/ <consumer>/activities/`
- Changes to any of the 5 hand-edited files → PR on autodesign → merge → sync into consumers → PR on consumers
- `recap.latest.yaml` and `dashboard.latest.yaml` are **not** synced from autodesign; they're consumer-repo-local, written by that repo's runtime and committed only when a consumer PR intentionally includes last-run review artifacts

### 4.5 Runtime write semantics for `.latest.yaml` (Option A, decided)

On session end:
1. Runtime computes `SessionOutcome` + the child-recap payload + dashboard fragment
2. Writes `activities/<game_id>/recap.latest.yaml` and `activities/<game_id>/dashboard.latest.yaml`
3. Overwrites any existing content (no append, no history)
4. DB continues to hold the authoritative historical record (`activity_session_outcomes`)

Purpose of the file:
- Authoring debug aid — *"what did this game actually produce last time it ran?"*
- Git-diffable artifact for post-merge sanity checks — if a spec change unexpectedly alters the recap shape, the next `.latest.yaml` commit shows the diff
- Fast offline inspection without querying the DB

Why overwrite (not append):
- File stays bounded in size
- No concurrency issues (the writer is always "the session that just ended")
- Git history of the file IS the cumulative log — you can `git log` the file to see its evolution

Why commit these to git (not gitignore):
- Reviewer can compare spec.md changes against recap.latest.yaml changes in one PR
- Catches "I changed the prompts and didn't realize the recap copy now says X" regressions

**Decision to lock:** `.latest.yaml` files ARE committed to git. If authors find this noisy during rapid iteration, gitignoring them is a 1-line change; starting committed is the cautious default.

---

## 5 · Matcher behavior

### 5.1 Input: conversation_signature

New Pydantic model (in both repos):

```python
class ConversationSignature(BaseModel):
    dominant_angle: str | None = None        # one of observation_angle enum values
    secondary_angles: list[str] = []         # other angles touched in conversation
    turn_count: int = 0
    entity_role_implied: str = "subject"     # what role the conversation treated the entity as
```

V1 derivation (simple heuristic):
- Count keyword hits in conversation history per angle vocabulary (e.g., "red" / "blue" / "green" → color; "round" / "square" / "long" → shape)
- `dominant_angle` = top keyword-hit angle with ≥3 mentions
- `secondary_angles` = other angles with ≥2 mentions
- `entity_role_implied` = "subject" unless the child's photo was never named as subject in dialogue (edge case, rare)

V2 (future): LLM-based classification from conversation transcript.

### 5.2 Game selector changes

`select_game()` gains parameters:
```python
def select_game(
    entity_name: str,
    detected_properties: list[str],
    age_tier: int,
    conversation_signature: ConversationSignature | None = None,   # ◆ NEW
    target_rung: Rung | None = None,                                # from progression plan
    target_axis: Axis | None = None,
    play_history: PlayHistory | None = None,
) -> GameSelectionResponse:
```

### 5.3 Scoring additions

Base tier scores (unchanged): Tier A = 10.0, Tier B = 8.0, Tier P = 7.0.

New bonuses (from this plan):
- `+1.5` if candidate's `activity_signature.observation_angle` == `conversation_signature.dominant_angle`
- `+0.75` if candidate's `observation_angle` appears in `conversation_signature.secondary_angles`
- `+0.5` if any of candidate's `bridge_prerequisites.primary` intersects with `dominant_angle` OR `secondary_angles`

Existing progression bonus (from 2026-04-21 backend plan): `+2.0` for rung match on target axis. This plan's bonuses are **additive**, not replacements.

**Pen → color scenario resolution:**
- Conversation signature: `dominant_angle = "color"`, secondary_angles = ["shape"]
- Candidates from Tier P: Color Scout (angle=color, score 7.0), Shape Quest (angle=shape, score 7.0)
- With bonuses: Color Scout → 7.0 + 1.5 angle match + 0.5 primary-bridge match = 9.0; Shape Quest → 7.0 + 0.75 secondary-angle match + 0.5 primary-bridge match = 8.25
- Color Scout wins. Coherent transition.

If Shape Quest were the only option, it still picks it (score 8.25 > min viable 3.0), but the runtime surfaces the pivot via `role_pivot_note` because the conversation treated the pen as the subject while the activity treats it as an exemplar.

### 5.4 When conversation_signature is null

Backwards-compatible: if the caller doesn't pass `conversation_signature` (e.g., game selection without prior conversation), the bonuses don't apply. Existing Tier A/B/P behavior is unchanged.

---

## 6 · Downstream surface changes

### 6.1 Child recap payload additions

Existing payload already reads `entity`, `tier`, `highlight_moment`, `caregiver_role`, `progression.difficulty_level`, `progression.next_step_hint`.

New fields the recap reads:
- `activity_signature.observation_angle` → drives copy ("noticed COLOR")
- `activity_signature.mechanic` → drives copy ("COLLECTED things")
- `activity_signature.entity_role` → drives pivot phrasing if exemplar/catalyst/reference
- `activity_signature.focal_attribute` → humanized for child vocabulary ("red")

Example composition (done by the recap renderer, not stored):
- observation_angle=color + mechanic=collect + entity_role=exemplar → *"You were a Color Scout today! We noticed RED. You collected 3 red things. The ladybug helped us spot red in our whole world."*

The template YAML (`recap.template.yaml`) per game specifies the skeleton; at runtime the renderer fills slots.

### 6.2 Parent dashboard payload additions

Existing payload: curiosity radial (7 axes), key_concepts_exposure, atl_skills_trail, session timeline.

New fields:
- **Curiosity radial angle split** — each axis now has `by_angle: {color: {sessions: N, rungs_reached: [...]}}` etc. Existing `current_rung_overall` per axis preserved for back-compat.
- **Exploration matrix** — 2D: mechanic × angle, values = session counts. Surfaces imbalance (e.g., "lots of collect, no voice").
- **Per-session fields** — `axis`, `angle`, `mechanic`, `entity_role` on each session in the timeline.

These are computed from `activity_session_outcomes` + the game's `tag_block.yaml`; no new persistence needed beyond adding the four activity-signature snapshot columns in §7 to `activity_session_outcomes` (both repos).

### 6.3 Template 0 §04 HTML preview update

Two additions to `docs/template_0_preview.html`:
1. New subsection showing the `activity_signature` block inline with the existing tag block YAML render
2. New entry in the §04 "fields read by downstream surfaces" table (lifecycle annotation) marking `observation_angle`, `mechanic`, `entity_role`, and `focal_attribute` as downstream-readable where applicable

CN mirror (`template_0_preview_cn.html`) gets parallel update. YAML tokens (`activity_signature`, `observation_angle`, enum values) stay English per house style.

---

## 7 · DB schema changes

Both repos add columns to `activity_session_outcomes`:

```sql
ALTER TABLE activity_session_outcomes
    ADD COLUMN observation_angle TEXT;     -- from activity_signature.observation_angle
ALTER TABLE activity_session_outcomes
    ADD COLUMN mechanic TEXT;              -- from activity_signature.mechanic
ALTER TABLE activity_session_outcomes
    ADD COLUMN entity_role TEXT;           -- from activity_signature.entity_role
ALTER TABLE activity_session_outcomes
    ADD COLUMN focal_attribute TEXT;       -- from activity_signature.focal_attribute
```

These are nullable; games without `activity_signature` (pre-migration) leave them NULL and the dashboard treats them as "angle-unspecified." Plan includes a backfill for the 5 most-played activities.

No new tables. The per-game `.latest.yaml` files are filesystem state, not DB.

---

## 8 · Migration strategy

### 8.1 Games to migrate in V1

V1 migrates **5 games** to the new per-game dir layout:
1. `color_scout_property` (Cat5, most-played property bridge)
2. `shape_quest_property` (Cat5, second-most-played)
3. `voice_stage_lion` (Cat1, canonical gold standard)
4. `mystery_trail_butterfly` (Cat5, gold standard, demonstrates Connection axis)
5. `polka_dot_patrol` (Cat5, gold standard, demonstrates pattern angle)

Remaining games migrate in follow-up PRs, one batch per PR. The loader supports both layouts during transition (§8.2); `activities/README.md` tracks the current count.

### 8.2 Dual-layout loader

The loader reads from **both** old-style and new-style paths during migration:

```python
def load_all_games() -> list[GameDefinition]:
    games = []
    # New layout
    for game_dir in sorted(p for p in (_BASE / "activities").glob("*/") if p.name != "_schema"):
        games.append(load_from_dir(game_dir))
    # Legacy layout (flat .md files)
    for subdir in ("gold_standards", "property_bridges"):
        for md_path in sorted((_BASE / subdir).glob("*.md")):
            games.append(parse_legacy_game_file(md_path))
    return games
```

When a game exists in both layouts, new-layout wins. Migration is complete when no legacy files remain; the legacy loader branch is removed in a follow-up.

### 8.3 Per-game migration recipe (authoring)

For each game to migrate:
1. Create `activities/<game_id>/` directory
2. Split old `<game_id>.md` content:
   - Frontmatter YAML → `tag_block.yaml` (add `activity_signature` block — hand-authored)
   - Prose sections (metaphor, round scenarios, rules, dialogue) → `prod.md`
   - Any "why this game exists" / "pedagogy" commentary → `spec.md` (or write from scratch if absent)
3. Hand-write `recap.template.yaml` using one reference session payload
4. Hand-write `dashboard.template.yaml` using the same reference session
5. Remove the legacy `<game_id>.md` file (the loader will pick up the new dir)

Per-game effort: ~30-60 min for an author familiar with the game. The 5 V1 migrations total ~3-4 hours of author time.

---

## 9 · Vocabulary storage

Closed enums live in a new canonical doc in the autodesign repo:

`docs/activity_vocabulary.md`:
- Section per enum (`observation_angle`, `mechanic`, `entity_role`)
- Each value has: canonical token, one-sentence definition, 2-3 example game mappings, example focal_attribute values
- Versioned header (v1.0 for this plan; bump on any addition)

Consumer repos import the vocabulary by:
- Runtime enums duplicated in `progression/models.py` or a new `activity_signature/vocabulary.py`
- Unit test verifies duplicated enum list matches the autodesign doc (parses doc, compares)
- Drift = test fails = CI block

Purpose: one place authors look up legal values; one place eng verifies against.

---

## 10 · Cross-references

- **Template 0 §04** ↔ this spec (§04 gains the `activity_signature` block in the preview HTML)
- **Matchability tags design** (`docs/plans/2026-04-20-matchability-tags-design.md`) — complementary. Matchability tags answer "can this entity run this activity?"; activity_signature answers "should this activity follow this conversation?"
- **Progression runtime plans** (`docs/plans/2026-04-21-progression-runtime-*.md`) — activity_signature enables angle-resolved progression (Form/color L2 vs Form/shape L2). Selector bonus (§5.3) stacks with progression's rung bonus.
- **Child recap preview** (`docs/child_recap_preview.html`) — §04 tag block contract gains activity-signature read fields
- **Parent dashboard preview** (`docs/parent_growth_path_preview.html`) — §03 curiosity radial design + §07 contract gain angle-resolved data
- **Background brief** (`docs/plans/2026-04-23-progression-background-brief.md`) — related system context

---

## 11 · Verification checklist

### 11.1 Schema
- [ ] `activity_vocabulary.md` published with 10 angles, 8 mechanics, 4 roles
- [ ] Template 0 §04 preview HTML renders the new block
- [ ] Template 0 §04 CN mirror updated
- [ ] Enum drift test passes in both repos

### 11.2 Per-game dir migration
- [ ] 5 V1 games have `activities/<game_id>/` dirs with all 5 required files
- [ ] Each `tag_block.yaml` validates against the schema (required fields present, enums legal)
- [ ] Legacy `.md` files removed for migrated games
- [ ] Loader test: given mixed new + legacy files, new-layout wins
- [ ] One game with `activity_signature` missing loads cleanly (backwards-compat)

### 11.3 Matcher
- [ ] Given conversation_signature.dominant_angle = "color", Color Scout outranks Shape Quest on a ladybug photo
- [ ] Given conversation_signature = null, existing Tier A/B/P behavior unchanged
- [ ] `role_pivot_note` surfaced in start-session dialogue when activity role ≠ conversation role

### 11.4 Runtime `.latest.yaml` writes
- [ ] Session end writes `recap.latest.yaml` with all required fields
- [ ] Session end writes `dashboard.latest.yaml` with angle + mechanic
- [ ] Second session on same game overwrites (doesn't append)
- [ ] Concurrent sessions on different games don't collide

### 11.5 Downstream surfaces
- [ ] Child recap payload includes `what_we_noticed`, `what_we_did`, `entity_role`
- [ ] Parent dashboard payload includes `by_angle` split on each axis + `exploration_matrix`
- [ ] Session timeline entries include `axis`, `angle`, `mechanic`

### 11.6 Cross-repo parity
- [ ] Vocabulary enum lists are byte-identical between autodesign doc + wonderlens-ai code + fullstack-demo code
- [ ] Shared test fixture `activity_signature_scenarios.json` passes in both repo test suites

---

## 12 · Implementation plan handoff

This spec is implemented by three repo-specific plans + a cross-repo overview:

- **Integration overview:** `docs/plans/2026-04-23-activity-signature-integration.md`
- **Authoring plan** (autodesign, 4 tasks): `docs/plans/2026-04-23-activity-signature-authoring.md`
- **Backend plan** (wonderlens-ai, 12 tasks): `wonderlens-ai/docs/plans/2026-04-23-activity-signature-backend.md`
- **Demo plan** (fullstack-demo, 5 tasks): `wonderlens-activity-fullstack-demo/docs/plans/2026-04-23-activity-signature-demo.md`

Total: 21 tasks. All TDD-shaped per repo conventions.

---

## Revnote

- **v0.1** (2026-04-23) — Inaugural design spec. Establishes layered `activity_signature` block with 3 closed vocabularies, per-game directory restructure, last-run cache (`recap.latest.yaml` / `dashboard.latest.yaml`) semantics, matcher scoring extension, and downstream surface payload changes. V1 migrates 5 seed games; remaining catalog migrations are follow-up PRs under the same spec.
