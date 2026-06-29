# Animal Sound Imitation - Engineering Spec

## Metadata

- activity_id: `concept_animal_sound_motion_voice`
- source_row: `13`
- source_concept: `source_animal_sound_imitation`
- assignment_type: `activity_concept`
- category: `cat1`
- mechanic: `motion_voice`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The AI prompts a familiar animal, and the child imitates its sound or speaks in the animal role.

## Selection Trigger

Child photographs an animal toy, animal picture, or enters animal-sound mode.

## Source Intent Lock

The AI prompts a familiar animal, and the child imitates its sound or speaks in the animal role.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `motion_voice`.
- Preserve this source sequence: The AI prompts a familiar animal, and the child imitates its sound or speaks in the animal role.

## Resolved Product Contract Notes

- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| animal_sound_cards_01 | card_set | optional | pre_generated | prod.step_1; prod.step_2.round_1-3 | center_card_area | Help the child recognize the animal they are about to imitate. | new_ai_generated_asset | If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture. |

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `motion_voice` mechanic.

## Extensibility Notes

- Replace `{runtime_entity}` only when the new trigger supports the same child action.
- Keep the same source sequence before changing category or mechanic labels.
- If an asset ID changes, preserve display timing, fallback wording, and safety constraints.

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|---|---|---|
| 1 | V1 Technical Compliance | PASS | Fallbacks are explicit and unsupported capability is not overclaimed. |
| 2 | Hook & Transition | PASS | Runtime start uses a rules-only setup; the first action prompt remains in Round 1. |
| 3 | Edge Case Coverage | PASS | Ideal, unexpected, and no-response branches are present. |
| 4 | IB Completeness | PASS | KUD and concepts match the child action. |
| 5 | Tier Appropriateness | PASS | Prompts are short and scaffolded. |
| 6 | Dialogue Specificity | PASS | Runtime AI instructions include example lines. |
| 7 | Screen & UI Completeness | PASS | Each beat names screen, state, asset, or fallback. |
| 8 | Entity Mapping Alignment | N/A | Workbook-source concept run; not mapping-informed. |
| 9 | Game Feel | PASS | Progress tokens and payoff create game structure. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | The source action and mechanic stay aligned. |

**Overall**: PASS - fresh full-run package preserves source intent with explicit runtime-generation and minimum-unblock assumptions.
