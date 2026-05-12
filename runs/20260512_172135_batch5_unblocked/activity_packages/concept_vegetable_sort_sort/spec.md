# Vegetable Sort Stand -- Authoring Spec

> CAT1 concept package . Concept source: `source_vegetable_sort` . Mechanic: `sort`

## Premise

The child sorts vegetable cards or photographed vegetables by a visible or meaningful rule. The activity turns that source promise into a cat1 runtime package where the child becomes the Veggie Sorter. The repeated action is `sort`, and the payoff is visible progress tied to the child's own responses.

## Target

- **Primary tier:** T1
- **Activity category:** cat1
- **Mechanic:** `sort`
- **Entity role:** reference
- **Progression axis:** connection, level 2

## Adaptation Rationale

- **Input mode:** concept_only.
- **Core promise:** The child sorts vegetable cards or photographed vegetables by a visible or meaningful rule.
- **Canonical mechanic:** `sort`; Step 3's repeated child action preserves this mechanic.
- **Readiness:** generate_with_assumptions.
- **Trigger condition:** Screen can show vegetable cards or a child photographs several vegetables.
- **Mapping use:** no required mapping for this package; runtime parameters avoid entity-specific facts unless runtime supplies them.
- **Asset dependency:** Asset dependency: `vegetable_sort_cards_01` is required card_set support; fallback behavior is documented.
- **Product capability flags:** requires_asset_display.
- **Scaffold fit:** acceptable. Adventure / `quest_collector` supplies the emotional payoff while `sort` remains the child-action contract.
- **Assumptions:** Mapping can improve real-photo routing but is not mandatory.

## Selection Trigger

Start when Screen can show vegetable cards or a child photographs several vegetables. If the required visual support is unavailable, use the fallback behavior from the Asset Brief or keep the interaction voice-only.

## Experience Pillar & Game Style

- **Pillar:** Adventure
- **Game style:** `quest_collector`
- **Why this scaffold:** Sorting stays the repeated action. The AI can suggest rules, but the child names and applies the grouping evidence.

## Runtime Detail Floor Notes

- **Distinct round design:** Round 1 -- Pick a Rule, Round 2 -- Place Two Vegetables, and Round 3 -- Name the Group each ask for a different child contribution and update a different progress token.
- **Branch specificity:** Unexpected answers are validated, then redirected to the current objective without pretending the runtime can verify unsupported facts.
- **Earned magic moment:** The stand opens with labeled groups, showing that the child made an organizing rule.
- **Residual risk:** The package stays within the current Cat1/Cat5 and asset-display contract; any richer UI, material workflow, or stateful display beyond the documented fallback remains a product decision.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| vegetable_sort_cards_01 | card_set | required | pre_generated | prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4 | center_card_area | Provide vegetable cards that can be sorted by color, shape, edible part, or cooking use. | Create a set of clear vegetable picture cards for children ages 4-7. Include carrot, broccoli, tomato, potato, corn, cucumber, pumpkin, and peas. Use one vegetable per card, plain light background, realistic but friendly illustration, no text, no brands, and clear color and shape. | Show a small set of cards and ask the child to choose a grouping rule. | If cards are unavailable, use photographed vegetables or a voice-only sorting prompt and do not claim cards are shown. | No choking imagery, no knives, no cooking hazards, and no brand packaging. |

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | display_behavior | fallback_behavior |
|---|---|---|---|---|---|---|---|---|---|
| vegetable_sort_cards_01 | card_set | required | pre_generated | prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4 | center_card_area | Provide vegetable cards that can be sorted by color, shape, edible part, or cooking use. | new_ai_generated_asset | Show a small set of cards and ask the child to choose a grouping rule. Persist or hide behavior: keep visible only through prod.step_1; prod.step_2; prod.step_3.round_1-3; prod.step_4, then summarize or hide at Step 4 according to the payoff. | If cards are unavailable, use photographed vegetables or a voice-only sorting prompt and do not claim cards are shown. |

## Extensibility Notes

- Reusable slots: `{runtime_topic}`, `vegetable_sort_cards_01`, `vegetable_sort_rule`, and `{runtime_tier}`.
- Retarget by changing the approved topic, scenario, entity, or asset set while preserving the `sort` mechanic.
- Retargeting guardrail: the repeated Step 3 child action must remain the same; only the surface theme changes.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, `templates.md`, and the Phase 0 adaptation brief.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The package uses voice dialogue, simple screen state, and documented asset fallback behavior; it does not require unsupported sensing or material verification. |
| 2 | Hook & Transition | PASS | Step 1 bridges from the trigger into a playful role without testing the child. |
| 3 | Edge Case Coverage | PASS | Each step includes ideal, unexpected, and no-response handling with concrete redirects. |
| 4 | IB Completeness | PASS | Key Concepts, related concepts, KUD, ATL skills, recap, and dashboard fragments align. |
| 5 | Tier Appropriateness | PASS | Language and task load match T1 expectations. |
| 6 | Dialogue Specificity | PASS | Runtime lines include concrete prompts, child branches, and follow-ups instead of abstract encouragement. |
| 7 | Screen & UI Completeness | PASS | Screen states identify visible progress, token changes, and fallback behavior where assets are optional or required. |
| 8 | Entity Mapping Alignment | N/A | This is a concept-led package with no required mapping source and no entity-specific claims. |
| 9 | Game Feel | PASS | The loop has escalating rounds and a visible payoff earned from the child's repeated action. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | Step 3, tag metadata, and adaptation rationale preserve `sort` while disclosing scaffold assumptions. |

**Overall**: ALL PASS -- author self-check after repair. Final independent reviewer evidence is tracked in `runs/20260512_172135_batch5_unblocked/review_notes.md`.
