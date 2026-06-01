# Recognition Pop Challenge - Engineering Spec

## Metadata

- activity_id: `concept_recognition_pop_probe`
- source_row: `31`
- source_concept: `source_whack_a_mole_recognition`
- assignment_type: `capability_probe`
- category: `cat1`
- mechanic: `compare`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

After a source photo introduces a target animal such as a dog, the AI teaches visually similar animals such as fox and wolf, then runs a timing challenge where mixed target/distractor cards appear and the child says the target word only when the target appears.

## Selection Trigger

Product has a recognition-pop surface that can show a source target, teach similar approved animal cards, and then present timed target/distractor cards.

## Source Intent Lock

Preserve the recognition-pop frame: after a source object such as dog, introduce visually similar approved targets/distractors, then show changing real/approved pictures where the child responds only when the target appears and stays quiet for non-targets. Do not reduce this to ordinary left/right matching without the target-vs-distractor timing rule.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `compare`: identify the target animal, notice similar-animal differences, then practice say-target/stay-quiet timing.
- Preserve this source sequence: source photo target, similar animal teaching, mixed card stream, target word only on target, quiet/no word for distractors.

## Resolved Product Contract Notes

- UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| recognition_target_dog_card | target_animal_card | required | pre_generated | prod.step_2; prod.step_3.round_1; prod.step_3.round_3-5 | center_pop_area | Provide a separate dog target card for the timing challenge where the child speaks only on target cards. | new_ai_generated_asset | If target/distractor timing is unavailable, keep the package unsupported rather than converting to ordinary matching choices. |
| recognition_distractor_fox_card | distractor_animal_card | required | pre_generated | prod.step_2; prod.step_3.round_2-5 | center_pop_area | Provide a separate fox quiet card for the timing challenge where the child stays quiet for distractors. | new_ai_generated_asset | If target/distractor timing is unavailable, keep the package unsupported rather than converting to ordinary matching choices. |
| recognition_distractor_wolf_card | distractor_animal_card | required | pre_generated | prod.step_2; prod.step_3.round_2-5 | center_pop_area | Provide a separate wolf quiet card for the timing challenge where the child stays quiet for distractors. | new_ai_generated_asset | If target/distractor timing is unavailable, keep the package unsupported rather than converting to ordinary matching choices. |

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `compare` mechanic.

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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | The repaired package restores source-photo target, similar-animal teaching, and say-target/stay-quiet timing. |

**Overall**: PASS - fresh full-run package preserves source intent with explicit runtime-generation and minimum-unblock assumptions.
