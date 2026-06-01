# How Many Guess - Engineering Spec

## Metadata

- activity_id: `concept_how_many_guess_enumerate`
- source_row: `28`
- source_concept: `source_how_many_guess`
- assignment_type: `activity_concept`
- category: `cat1`
- mechanic: `enumerate`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The child answers meaningful quantity-feature questions, such as how many legs an animal has or how many wheels, petals, buttons, or points an object has, then checks the count with the AI.

## Selection Trigger

Screen can show an animal/object card with a semantic feature to count, or the child and AI can discuss a familiar animal/object feature by voice.

## Source Intent Lock

Preserve the quantity-attribute frame: ask how many of a meaningful feature an animal or object has, such as animal legs, wheels, petals, or buttons. Do not reduce this to estimating a pile of visible unrelated objects unless product explicitly approves the generic counting-card adaptation.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `enumerate`: hear the animal/object, identify the feature, guess the feature count, and check the semantic reason.
- Preserve this source sequence: ask a meaningful feature-count question, let child guess, count/check together, then compare the feature with another animal/object.

## Resolved Product Contract Notes

- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| how_many_count_cards_01 | semantic_feature_card_set | required | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Show animal/object cards whose count target is a meaningful feature such as legs, wheels, petals, or buttons. | new_ai_generated_asset | If cards are unavailable, ask familiar voice-only feature questions and do not claim a card is displayed. |

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `enumerate` mechanic.

## Extensibility Notes

- Replace `{runtime_entity}` only when the new trigger supports the same child action.
- Keep the same source sequence before changing category or mechanic labels.
- If an asset ID changes, preserve display timing, fallback wording, and safety constraints.

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|---|---|---|
| 1 | V1 Technical Compliance | PASS | Fallbacks are explicit and unsupported capability is not overclaimed. |
| 2 | Hook & Transition | PASS | Opening uses the workbook trigger and play frame. |
| 3 | Edge Case Coverage | PASS | Ideal, unexpected, and no-response branches are present. |
| 4 | IB Completeness | PASS | KUD and concepts match the child action. |
| 5 | Tier Appropriateness | PASS | Prompts are short and scaffolded. |
| 6 | Dialogue Specificity | PASS | Runtime AI instructions include example lines. |
| 7 | Screen & UI Completeness | PASS | Each beat names screen, state, asset, or fallback. |
| 8 | Entity Mapping Alignment | N/A | Workbook-source concept run; not mapping-informed. |
| 9 | Game Feel | PASS | Progress tokens and payoff create game structure. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | The repaired package restores semantic feature counts instead of generic visible-object counting. |

**Overall**: PASS - fresh full-run package preserves source intent with explicit runtime-generation and minimum-unblock assumptions.
