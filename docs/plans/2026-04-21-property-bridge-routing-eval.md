# Property-Bridge Routing Evaluation

> Created: 2026-04-21
> Owner: TBD
> **Status: Superseded on 2026-04-23** → see [`2026-04-23-matcher-verification-eval.md`](2026-04-23-matcher-verification-eval.md)
>
> The follow-up plan widens scope from Layer 2 (property-bridge) only to all three matching paths:
> Tier A strict-overlap lint + Layer 1 constellation routing + Layer 2 property-bridge routing.
> Content below is preserved for historical context; Part C of the new plan is the direct successor.

## Purpose

Measure whether the 18 property-bridge templates (12 Cat5 + 6 Cat1) actually serve unmapped entities well, before authoring a 19th. Specifically answer:

1. **Does Layer 2 routing hit the ~40% target** from `docs/plans/2026-04-08-entity-bridging.md` §Verification?
2. **Is any (Category × Pillar) cell starved** — i.e., unmapped entities that should reach that Pillar can't, because no template's `entity_attributes_covered` overlaps their attributes?
3. **Is Cat1 brittle** given its "6 templates, 1 per Pillar" density (vs Cat5's 12 across 6 Pillars, unevenly)?

Output decides whether to add templates, and *which*.

## Non-goals

- Judging template *quality* (D9 Game Feel, D10 Pillar Fidelity) — that's a separate pass per `docs/plans/2026-04-08-entity-bridging.md` §Verification.
- Layer 1 (constellation) tuning — already handled by the v0.3 tuning in commit `8234441`.
- Layer 3 ending design.
- Building a production matcher runtime — we build a throwaway simulator, not a service.

## Inputs already in place

| Artifact | Role in the eval |
|---|---|
| `data/constellation_map.yaml` | Layer 1 exclusion filter |
| `data/mappings_dev20_0318/` | Defines the 21 "mapped" set |
| 18 `*_property_gold_spec.md` under `designs/cat1/` + `designs/cat5/` | Source of `entity_attributes_covered` per template |
| `program.md §1.9` Matcher semantics (v1.5, 2026-04-21) | Loose-overlap rule for `entity_binding: parameterized` |

## Step 1 — Build the unmapped test set (N = 20)

**Goal**: 20 realistic photo targets that are NOT in the mapped-entity set and NOT in `constellation_map.yaml`. Split ~10 Cat1 (indoor, in-device) + ~10 Cat5 (outdoor, out-of-device).

**Seed candidates** (verify each against the exclusion set before including):

- **Cat1 (10)**: `cup`, `pencil`, `apple_watch`, `plush_octopus`, `shoelace`, `house_key`, `sock`, `coin`, `book`, `alarm_clock`
- **Cat5 (10)**: `dandelion_seed_head`, `acorn`, `pinecone`, `ladybug`, `snail`, `twig`, `stone`, `moss_patch`, `puddle`, `cloud`

**For each entity, manually list the visual attributes a vision model would plausibly return** — this is the ONLY manual input to the evaluation. Use the tier-path vocabulary from `program.md §1.9` / existing `entity_attributes_covered` fields so it's directly comparable:

```yaml
# Example — acorn
entity: acorn
category: 5
attributes:
  - tier_0.appearance.shape        # round-ish, oval
  - tier_0.appearance.size         # small-vs-hand
  - tier_0.appearance.color        # brown
  - tier_1.appearance.texture      # smooth cap, bumpy base
  - tier_1.classification.natural_or_made  # natural
  - tier_2.lifecycle.stage         # seed
```

Record these in `docs/evals/2026-04-21-property-bridge-routing/test_entities.yaml`.

**Guardrails**:
- Don't cheat — pick attributes that are visually verifiable from a single photo (`docs/plans/2026-04-08-entity-bridging.md:146-160`). No "weight", no "temperature".
- Don't list the full tier_guidance tree — list what vision would return with medium confidence, 3–6 attributes per entity.
- Two reviewers agree on the attribute stub for each entity. Divergence gets flagged as a data quality caveat in the final report.

## Step 2 — Extract template catalogs

Write `scripts/eval_routing/extract_template_attrs.py` (single-purpose, throwaway):

- Parse all 18 `*_property_gold_spec.md`
- Emit one row per template: `name, category, pillar, style, entity_attributes_covered[]`
- Output: `docs/evals/2026-04-21-property-bridge-routing/templates.yaml`

No need to handle the `bound` gold standards — they're Layer 0/Tier A and out of scope here.

## Step 3 — Implement the simulator (~50 LOC)

`scripts/eval_routing/route.py`:

```
for each test entity E:
  # Layer 1
  if E.name in constellation_map.entries:
      route = L1 → matched mapped entity's gold
      continue
  # Layer 2 — loose overlap, collect ALL matches (not just one)
  matches = [t for t in templates
             if t.category == E.category
             and any(a in E.attributes for a in t.entity_attributes_covered)]
  if matches:
      route = L2, matches = matches    # keep ALL, don't pick one
      continue
  # Layer 3
  route = L3_conversation_only
```

Key: **collect all Layer 2 matches**, don't simulate the ranker's single-winner pick. The coverage analysis (Step 4) needs the full set per entity to spot starved Pillars.

Output: `docs/evals/2026-04-21-property-bridge-routing/routing_results.yaml` — one record per entity, one row per matched template.

## Step 4 — Analyses

### 4a. Route distribution
Count L1 / L2 / L3 across the 20 entities. Compare to the `~40% L1 / ~40% L2 / ~20% L3` target in `docs/plans/2026-04-08-entity-bridging.md:376-377`. Large deviation on a sample of 20 is a hint, not proof — note the CI.

### 4b. (Category × Pillar) coverage heat map

| | Adventure | Discovery | Mystery | Creation | Performance | Nurture |
|---|---|---|---|---|---|---|
| Cat1 | n/N | n/N | n/N | n/N | n/N | n/N |
| Cat5 | n/N | n/N | n/N | n/N | n/N | n/N |

Each cell: how many of the N same-category entities could plausibly reach that Pillar via some L2 template. Cells at 0 = candidate gap.

### 4c. Cat1 brittleness check
For each of the 10 Cat1 test entities, how many distinct Pillars can it reach via L2?
- 0 Pillars → falls to L3 (bad)
- 1 Pillar → no choice, system can't vary replay
- ≥ 2 Pillars → healthy

Compare to the same distribution for Cat5. If Cat1 median is 0–1 and Cat5 median is ≥2, that's evidence the thin Cat1 pool is the problem.

### 4d. Starvation candidates
For each Pillar cell with consistent 0 matches, name the missing template hypothesis: *"Cat1 / Nurture is unreachable for entities exposing only `tier_0.appearance.color` — a color-driven care_station template would close the gap."* Only list gaps supported by ≥ 2 entities in the sample.

## Step 5 — Writeup

Single markdown file `docs/evals/2026-04-21-property-bridge-routing/REPORT.md`:

1. Test set (with attribute stubs)
2. Route distribution vs target
3. (Cat × Pillar) heat map
4. Cat1 brittleness finding
5. Ranked list of *evidence-backed* template proposals (Pillar, property hypothesis, entities that would benefit)
6. Caveats — small N, hand-stubbed attributes, no quality check

Decision output: 0, 1, or 2–3 new templates to author, each with a justification paragraph. **No template added without a starvation signal in this report.**

## Effort estimate

| Step | Time | Who |
|---|---|---|
| 1. Test set + attribute stubs (N=20, two-reviewer agreement) | ~2 hrs | 1 author, 1 reviewer |
| 2. Template extraction script | ~0.5 hr | 1 engineer |
| 3. Simulator script | ~1 hr | 1 engineer |
| 4. Analyses | ~1 hr | 1 engineer |
| 5. Report writeup | ~1 hr | 1 author |
| **Total** | **~5.5 hrs** | |

Throwaway code — simulator + extractor live under `scripts/eval_routing/` and don't need to meet production quality bars.

## Deliverables

| Path | Content |
|---|---|
| `docs/evals/2026-04-21-property-bridge-routing/test_entities.yaml` | 20 unmapped entities + attribute stubs |
| `docs/evals/2026-04-21-property-bridge-routing/templates.yaml` | 18 template catalog (extracted) |
| `docs/evals/2026-04-21-property-bridge-routing/routing_results.yaml` | Per-entity routing trace |
| `docs/evals/2026-04-21-property-bridge-routing/REPORT.md` | Findings + template recommendations |
| `scripts/eval_routing/extract_template_attrs.py` | Throwaway extractor |
| `scripts/eval_routing/route.py` | Throwaway simulator |

## Open questions

- **Test-set sourcing bias**: the seed candidates above are author-chosen. Is there a real photo-log we can sample from instead? (Ask product.) If yes, the hand-stubbed attribute step is reduced but not eliminated — real photos still need attribute annotation.
- **Attribute stub confidence**: do we need a third reviewer for entities where the two reviewers diverge, or is divergence itself useful signal (= vision would also struggle)?
- **Pillar preference**: the simulator treats all matched templates equally. In production the ranker has preferences (e.g., entity context may favor Discovery over Performance). Does the eval need to model that, or does "can this entity reach Pillar X at all" answer the coverage question well enough? Current plan: the latter — note the limitation in the report.

## Critical files

| File | Role |
|---|---|
| `docs/plans/2026-04-21-property-bridge-routing-eval.md` | This plan |
| `docs/plans/2026-04-08-entity-bridging.md` | Verification §; design source |
| `program.md` §1.9 Matcher semantics | Matcher rule (v1.5) |
| `data/constellation_map.yaml` | Layer 1 exclusion |
| `designs/cat1/*_property_gold_spec.md` + `designs/cat5/*_property_gold_spec.md` | Template attribute source |
