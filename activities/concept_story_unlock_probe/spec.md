# Story Challenge Unlock - Engineering Spec

## Metadata

- activity_id: `concept_story_unlock_probe`
- source_row: `7`
- source_concept: `source_story_challenge_unlock`
- assignment_type: `capability_probe`
- category: `cat1`
- mechanic: `imagine`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The AI tells a fixed story, pauses at challenge gates, and unlocks the next story beat only after the child completes each quick challenge.

## Selection Trigger

Child reaches a story pause point and can complete a quick challenge to continue.

## Source Intent Lock

Preserve the sequence: story beat, paused gate, small child challenge such as finding a color, making an animal sound, or echoing a word, then unlocked next story beat. Do not generate standalone challenges without story narration.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `imagine`.
- Preserve this source sequence: Preserve the sequence: story beat, paused gate, small child challenge such as finding a color, making an animal sound, or echoing a word, then unlocked next story beat. Do not generate standalone challenges without story narration.

## Resolved Product Contract Notes

- UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| story_unlock_cards_01 | story_card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Show a simple locked story door, token, or next-scene card during a story challenge. | new_ai_generated_asset | If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked. |

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `imagine` mechanic.

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
