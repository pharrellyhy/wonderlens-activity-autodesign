# Phoneme Treasure Hunt - Engineering Spec

## Metadata

- activity_id: `concept_phoneme_hunt_collect`
- source_row: `2`
- source_concept: `source_phoneme_hunt`
- assignment_type: `match_pattern`
- category: `cat5`
- mechanic: `collect`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The AI introduces a target sound, then the child finds an object whose word starts with that sound.

## Selection Trigger

Child enters language treasure-hunt mode or photographs an everyday object suitable for sound play.

## Source Intent Lock

The AI introduces a target sound, then the child finds an object whose word starts with that sound.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `collect`.
- Preserve this source sequence: The AI introduces a target sound, then the child finds an object whose word starts with that sound.

## Resolved Product Contract Notes

- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| phoneme_letter_card_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Give the child a visual reminder of the target sound and letter. | new_ai_generated_asset | If the card is unavailable, the AI repeats the target sound by voice only and must not claim the screen is showing a letter. |

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `collect` mechanic.

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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | The source action and mechanic stay aligned. |

**Overall**: PASS - fresh full-run package preserves source intent with explicit runtime-generation and minimum-unblock assumptions.
