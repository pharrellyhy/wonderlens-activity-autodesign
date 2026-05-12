# Plant Parts Field Scout -- Authoring Spec

> CAT5 concept package . Concept source: `source_plant_parts_explorer` . Mechanic: `enumerate`

## Premise

The child looks at a plant and identifies visible parts such as leaf, stem, flower, fruit, seed, or root. The activity turns that source promise into a cat5 runtime package where the child becomes the Plant Parts Scout. The repeated action is `enumerate`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T1
- **Activity category:** cat5
- **Mechanic:** `enumerate`
- **Entity role:** subject
- **Progression axis:** form, level 2

## Adaptation Rationale

- **Input mode:** mapping_informed.
- **Core promise:** The child looks at a plant and identifies visible parts such as leaf, stem, flower, fruit, seed, or root.
- **Canonical mechanic:** `enumerate`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Uploaded or live photo clearly shows a plant with at least two visible parts.
- **Mapping use:** no required mapping for this package; runtime parameters avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** Asset dependency: `no_assets`; no asset brief is needed.
- **Product capability flags:** none.
- **Scaffold fit:** acceptable. Discovery / `field_experiment` supplies the emotional payoff while `enumerate` remains the child-action contract.
- **Assumptions:** Use mapping to ground visible parts and tier language when available. If mapping is absent, avoid species-specific facts.

## Selection Trigger

Start when an uploaded or live photo clearly shows a plant with at least two visible parts. If the plant photo is too blurry or only the pot is visible, ask for a clearer plant view or switch to a voice-only "name any plant parts you know" fallback without claiming screen evidence.

## Experience Pillar & Game Style

- **Pillar:** Discovery
- **Game style:** `field_experiment`
- **Why this scaffold:** The activity uses only visible plant evidence. The surprise-part check and not-visible chips create uncertainty without inventing hidden plant facts.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Leaf Evidence Hunt, Round 2 -- Stem Path Hunt, and Round 3 -- Surprise Part Check each ask for a different child contribution and update a different evidence token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The plant map opens after the child records visible evidence and any honest not-visible chips, so uncertainty comes from inspecting the actual photo.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Extensibility Notes

- Reusable slots: `{runtime_plant}`, `{visible_plant_part}`, `{part_count}`, `{leaf_stem_flower_seed}`.
- Retarget to any safe plant photo with at least two visible parts; never claim hidden roots, seeds, or plant health unless visible or child-reported.
- Retargeting guardrail: preserve enumerate/identify; do not turn the activity into plant care diagnosis.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The package uses voice dialogue, simple screen state, and no-asset visible-part fallback behavior; it does not require unsupported sensing or material verification. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a playful role without testing the child. |
| 3 | Edge Case Coverage | PASS | Each step includes ideal, unexpected, and no-response handling with concrete redirects. |
| 4 | IB Completeness | PASS | Key Concepts, related concepts, KUD, ATL skills, recap, and dashboard fragments align. |
| 5 | Tier Appropriateness | PASS | Language and task load match T1 expectations. |
| 6 | Dialogue Specificity | PASS | Runtime lines include concrete prompts, child branches, and follow-ups instead of abstract encouragement. |
| 7 | Screen & UI Completeness | PASS | Screen states identify visible progress, token changes, and fallback behavior where assets are optional or required. |
| 8 | Entity Mapping Alignment | N/A | This is a concept-led package with no required mapping source and no entity-specific claims. |
| 9 | Game Feel | PASS | The surprise-part check, visible/not-visible chips, and evidence-map reveal create stakes tied to the child's inspection. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `enumerate` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
