# Emotion Color Outfit - Engineering Spec

## Metadata

- activity_id: `concept_emotion_color_outfit_probe`
- source_row: `17`
- source_concept: `source_emotion_color_outfit`
- assignment_type: `capability_probe`
- category: `cat1`
- mechanic: `care`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The child uses colors to represent feelings, then sees or imagines a character outfit matching that feeling.

## Selection Trigger

Child names a mood or chooses a color to represent a feeling.

## Source Intent Lock

The child uses colors to represent feelings, then sees or imagines a character outfit matching that feeling.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `care`.
- Preserve this source sequence: The child uses colors to represent feelings, then sees or imagines a character outfit matching that feeling.

## Resolved Product Contract Notes

- Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
- UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| emotion_color_character_01 | character_template | required | pre_generated_or_runtime_recolored | prod.step_2; prod.step_3.round_1-3 | center_card_area | Show a character whose outfit can reflect the child's chosen emotion color. | new_ai_generated_asset_or_future_avatar_renderer | If recoloring is unavailable, block at Phase 0 or run a voice-only emotion-color conversation without claiming the outfit changed. |

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `care` mechanic.

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
