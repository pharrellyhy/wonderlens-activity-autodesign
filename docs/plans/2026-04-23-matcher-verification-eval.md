# Matcher Verification Eval

> Created: 2026-04-23
> Owner: TBD
> Status: Planned
> Supersedes: [`2026-04-21-property-bridge-routing-eval.md`](2026-04-21-property-bridge-routing-eval.md) (scope widened from Layer 2 only to all three matching paths)

## Purpose

Verify the three matching paths that route a photographed entity to an activity, before trusting them in production and before authoring new templates to patch perceived gaps. Specifically:

- **Part A — Tier A strict-overlap lint** (bound gold standards): every ID in each gold's `entity_attributes_covered` resolves to a real `attribute:` entry in that entity's YAML `tier_guidance`. Static check; runs in seconds.
- **Part B — Layer 1 constellation routing**: unmapped entities that appear in `constellation_map.yaml` route to a same-category mapped gold, with bridge strength ≥ 0.7, and the prompt template substitutes correctly. ~40% of traffic in the target distribution.
- **Part C — Layer 2 property-bridge routing**: unmapped entities that miss Layer 1 reach a same-category property-bridge template via loose-overlap on `entity_attributes_covered`. ~40% of traffic. This is where the "do we need more templates?" question lives.

Output is a single report that decides which (if any) templates to author and which `entity_attributes_covered` lists need fixing.

## Non-goals

- Judging template or gold *quality* (D9 Game Feel, D10 Pillar Fidelity) — separate pass per `docs/plans/2026-04-08-entity-bridging.md` §Verification.
- **Style Recommender / Tier-A-vs-Tier-B preference** when an entity has both its own gold AND a constellation neighbor with a gold. Deferred — only ~21 mapped entities, mostly one gold each, low ROI on this cycle.
- Layer 3 (conversation-only) ending design.
- Building a production matcher runtime — this eval ships throwaway scripts under `scripts/eval_routing/`, not a service.

## Inputs already in place

| Artifact | Role in the eval |
|---|---|
| `data/constellation_map.yaml` | Part B source of truth; Part C exclusion filter |
| `data/mappings_dev20_0318/**/*.yaml` | Tier A strict-overlap target; defines the 21 "mapped" set |
| 12 `*_gold_spec.md` (bound) under `designs/cat1/` + `designs/cat5/` | Part A input |
| 18 `*_property_gold_spec.md` under `designs/cat1/` + `designs/cat5/` | Part C input |
| `program.md §1.9` Matcher semantics (v1.5) | Rules for strict vs loose overlap |

---

## Part A — Tier A strict-overlap lint (static)

**Goal**: for every bound gold design (entity_binding inferred as `bound`), confirm every ID in its `entity_attributes_covered` resolves under the entity's `tier_guidance`. A miss = authoring drift, not a matcher bug.

### A.1 Collect (entity, gold) pairs
Parse the 12 gold spec files (`*_gold_spec.md`, excluding `*property*`), extract:
- `Trigger Entity`
- `Category`
- `entity_attributes_covered` list from §A.1

### A.2 Resolve each ID against the entity YAML
For each pair, load `data/mappings_dev20_0318/**/<entity>.yaml`. Walk `tier_guidance.tier_{0,1,2}.{dimension}.{attribute}` and verify each listed dotted path resolves to an `attribute:` entry (not a branch, not missing).

### A.3 Emit a lint report
`docs/evals/2026-04-23-matcher-verification/lint_tierA.md`:

| Gold | Entity | IDs listed | Resolved | Missing | Status |
|---|---|---|---|---|---|

Any `Missing > 0` is a bug (either the gold's §A.1 is wrong or the entity YAML is out of date). Target: **zero misses**.

### A.4 Wire into pre-commit (optional, only if A.3 reveals misses)
If Part A finds real drift, consider adding `scripts/eval_routing/lint_tierA.py` to pre-commit on paths `designs/cat{1,5}/*_gold_spec.md` and `data/mappings_dev20_0318/**`. Decision deferred to the report.

**Effort**: ~1 hr (script + run + report).

---

## Part B — Layer 1 constellation routing

**Goal**: trace unmapped-but-constellation-listed entities end-to-end and verify the bridge rules from `docs/plans/2026-04-08-entity-bridging.md:109-117`.

### B.1 Build the Layer 1 test set (N = 10)
Pick 10 entities that appear in the `constellation` field of `data/constellation_map.yaml` — e.g., `kitten`, `tulip`, `toy_car`, `scooter`, `plush_bunny`, `mango`, `pond_fish`, `umbrella`, `toy_dinosaur`, `traffic_light`. Even split Cat1 / Cat5 where the constellation entry supports it.

For each, the "attribute stub" step from Part C is **not required** — Layer 1 matches on entity identity, not attributes. Only record `(name, expected_category)`.

### B.2 Route each entity
In the shared simulator (see Integration), Layer 1 rule:

```
for each candidate mapped entity M in constellation_map:
    if E.name in M.constellation and M.bridge_strength >= 0.7:
        if M.category != E.expected_category:
            flag  # cross-category bridge is a bug
        record (E → M, bridge_type, prompt_rendered)
```

Render the `bridge_prompt_pattern` with `[entity]` substituted, capture it.

### B.3 Assertions per entity
For each traced entity, verify:

| Check | Pass criterion |
|---|---|
| Category-same | `M.category == E.expected_category` |
| Bridge strength | ≥ 0.7 (or weak-type allowed only if no stronger exists) |
| Prompt substitution | rendered prompt has no `[entity]` leftover and reads natural |
| Adapted game route | `M`'s gold spec exists under `designs/cat{M.category}/` |
| One-attempt rule | (design-time only — can't test without runtime) noted as caveat |

### B.4 Output
`docs/evals/2026-04-23-matcher-verification/routing_L1.yaml` + a short findings section in the main report. Most-likely failure mode: weak bridges (score < 0.7) sneaking through, or cross-category entries in `constellation_map.yaml`.

**Effort**: ~2 hrs (test set selection, simulator extension, prompt render review).

---

## Part C — Layer 2 property-bridge routing

**Goal**: measure whether the 18 property-bridge templates actually serve unmapped entities well, before authoring a 19th. Specifically answer:

1. **Does Layer 2 routing hit the ~40% target** from `docs/plans/2026-04-08-entity-bridging.md` §Verification?
2. **Is any (Category × Pillar) cell starved** — i.e., unmapped entities that should reach that Pillar can't, because no template's `entity_attributes_covered` overlaps their attributes?
3. **Is Cat1 brittle** given its "6 templates, 1 per Pillar" density (vs Cat5's 12 across 6 Pillars, unevenly)?

### C.1 Build the Layer 2 test set (N = 20)

**Goal**: 20 realistic photo targets that are NOT in the mapped-entity set and NOT in `constellation_map.yaml`. Split ~10 Cat1 (indoor, in-device) + ~10 Cat5 (outdoor, out-of-device).

**Seed candidates** (verify each against the exclusion set before including):

- **Cat1 (10)**: `cup`, `pencil`, `apple_watch`, `plush_octopus`, `shoelace`, `house_key`, `sock`, `coin`, `book`, `alarm_clock`
- **Cat5 (10)**: `dandelion_seed_head`, `acorn`, `pinecone`, `ladybug`, `snail`, `twig`, `stone`, `moss_patch`, `puddle`, `cloud`

**For each entity, manually list the visual attributes a vision model would plausibly return** — this is the ONLY manual input to the evaluation. Use the tier-path vocabulary from `program.md §1.9`:

```yaml
# Example — acorn
entity: acorn
category: 5
layer_for: L2
attributes:
  - tier_0.appearance.shape
  - tier_0.appearance.size
  - tier_0.appearance.color
  - tier_1.appearance.texture
  - tier_1.classification.natural_or_made
  - tier_2.lifecycle.stage
```

**Guardrails**:
- Attributes must be visually verifiable from a single photo (`docs/plans/2026-04-08-entity-bridging.md:146-160`). No "weight", no "temperature".
- 3–6 attributes per entity — don't overstuff.
- Two reviewers agree on each stub. Divergence gets flagged as a data-quality caveat.

### C.2 Extract template catalog
`scripts/eval_routing/extract_template_attrs.py`:
- Parse all 18 `*_property_gold_spec.md`
- Emit: `name, category, pillar, style, entity_attributes_covered[]`
- Output: `docs/evals/2026-04-23-matcher-verification/templates.yaml`

### C.3 Route each entity (simulator continues from Part B)

```
# Layer 2 — loose overlap, collect ALL matches
matches = [t for t in templates
           if t.category == E.category
           and any(a in E.attributes for a in t.entity_attributes_covered)]
if matches:
    route = L2, matches = matches   # keep ALL, don't pick one
    continue
# Layer 3
route = L3_conversation_only
```

**Key**: collect all matches, don't simulate the ranker's single-winner pick. The coverage analysis needs the full set per entity to spot starved Pillars.

### C.4 Analyses

**C.4a — Route distribution**. Count L1 / L2 / L3 across the full 30-entity sample (10 from Part B + 20 from Part C). Compare to `~40% L1 / ~40% L2 / ~20% L3`. N=30 is small — note CI.

**C.4b — (Category × Pillar) coverage heat map**:

| | Adventure | Discovery | Mystery | Creation | Performance | Nurture |
|---|---|---|---|---|---|---|
| Cat1 | n/N | n/N | n/N | n/N | n/N | n/N |
| Cat5 | n/N | n/N | n/N | n/N | n/N | n/N |

Each cell: how many same-category entities can plausibly reach that Pillar via some L2 template. Cells at 0 = candidate gap.

**C.4c — Cat1 brittleness**. For each Cat1 entity in C.1, how many distinct Pillars can it reach via L2?
- 0 Pillars → falls to L3 (bad)
- 1 Pillar → no choice, system can't vary replay
- ≥ 2 Pillars → healthy

Compare Cat1 median to Cat5 median.

**C.4d — Starvation candidates**. For each Pillar cell with consistent 0 matches, name the missing template hypothesis. Only list gaps supported by ≥ 2 entities in the sample.

**Effort**: ~4.5 hrs (test set + attribute stubs ~2, extract script ~0.5, analyses ~1, writeup contribution ~1).

---

## Integration

Single shared simulator (`scripts/eval_routing/route.py`, ~80 LOC) runs Parts B and C:

- Part A is a standalone lint pass (no test entities) — `lint_tierA.py`
- Parts B and C share `test_entities.yaml` (30 rows, tagged `layer_for: L1 | L2`)
- Simulator walks each entity through L1 → L2 → L3 and records route, matches, bridge metadata

Shared output directory: `docs/evals/2026-04-23-matcher-verification/`.

## Unified writeup

Single markdown file `docs/evals/2026-04-23-matcher-verification/REPORT.md`:

1. **Part A findings**: lint pass/fail per gold, total drift count
2. **Part B findings**: constellation routing traces, assertion results, cross-category or weak-bridge issues
3. **Part C findings**: route distribution, (Cat × Pillar) heat map, Cat1 brittleness, starvation candidates
4. **Combined recommendations**:
   - Tier A drift fixes (authoring backlog)
   - Constellation map corrections (if any)
   - Ranked list of evidence-backed template proposals (Pillar, property hypothesis, entities that would benefit)
5. **Caveats**: small N, hand-stubbed attributes, no quality check, one-attempt rule not runtime-tested.

Decision output: 0, 1, or 2–3 new templates to author, each with a justification paragraph. **No template added without a starvation signal in this report.**

## Effort estimate

| Part | Time | Output |
|---|---|---|
| A — Tier A lint | ~1 hr | `lint_tierA.md` |
| B — Layer 1 constellation | ~2 hr | `routing_L1.yaml` + report section |
| C — Layer 2 property-bridge | ~4.5 hr | `routing_L2.yaml` + heat map + starvation list |
| Integration + REPORT.md | ~1 hr | `REPORT.md` |
| **Total** | **~8.5 hrs** | |

Throwaway code — scripts live under `scripts/eval_routing/` and don't need to meet production quality bars.

## Deliverables

| Path | Content | Part |
|---|---|---|
| `docs/evals/2026-04-23-matcher-verification/lint_tierA.md` | Strict-overlap lint report | A |
| `docs/evals/2026-04-23-matcher-verification/test_entities.yaml` | 30 entities (10 L1 + 20 L2) + attribute stubs where applicable | B, C |
| `docs/evals/2026-04-23-matcher-verification/templates.yaml` | 18 template catalog (extracted) | C |
| `docs/evals/2026-04-23-matcher-verification/routing_L1.yaml` | Per-entity L1 trace | B |
| `docs/evals/2026-04-23-matcher-verification/routing_L2.yaml` | Per-entity L2 trace (all matches) | C |
| `docs/evals/2026-04-23-matcher-verification/REPORT.md` | Unified findings + recommendations | A+B+C |
| `scripts/eval_routing/lint_tierA.py` | Throwaway lint | A |
| `scripts/eval_routing/extract_template_attrs.py` | Throwaway extractor | C |
| `scripts/eval_routing/route.py` | Throwaway simulator (L1 + L2) | B, C |

## Open questions

- **Test-set sourcing bias (Part C)**: seed candidates are author-chosen. Is there a real photo-log we can sample from? (Ask product.) Real photos still need attribute annotation but reduce selection bias.
- **Attribute stub confidence (Part C)**: if two reviewers diverge on an entity's attribute list, is that signal (= vision would also struggle) or noise?
- **Pillar preference (Part C)**: the simulator treats all matched templates equally. Does the eval need to model the ranker's preferences, or is "can this entity reach Pillar X at all" the right question? Current plan: the latter — note limitation in the report.
- **Part A CI hookup**: if zero drift is found, skip pre-commit. If drift is found, is a pre-commit lint worth the permissions friction, or better as a nightly CI check?
- **Deferred — Style Recommender**: when an entity has both its own gold AND a constellation-reachable gold, does the ranker pick correctly? Out of scope here; file separate plan if Part B surfaces mispicks.

## Critical files

| File | Role |
|---|---|
| `docs/plans/2026-04-23-matcher-verification-eval.md` | This plan |
| `docs/plans/2026-04-21-property-bridge-routing-eval.md` | Predecessor (Layer 2 only, superseded) |
| `docs/plans/2026-04-08-entity-bridging.md` | Verification §; design source |
| `program.md` §1.9 Matcher semantics | Matcher rule (v1.5) |
| `data/constellation_map.yaml` | Layer 1 source, Layer 2 exclusion |
| `data/mappings_dev20_0318/**/*.yaml` | Tier A strict-overlap target |
| `designs/cat{1,5}/*_gold_spec.md` (bound) | Part A input |
| `designs/cat{1,5}/*_property_gold_spec.md` (parameterized) | Part C input |
