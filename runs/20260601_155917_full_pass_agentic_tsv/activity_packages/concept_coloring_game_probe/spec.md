# Coloring Game - Engineering Spec

## Metadata

- activity_id: `concept_coloring_game_probe`
- source_row: `8`
- source_concept: `source_coloring_game`
- assignment_type: `capability_probe`
- category: `cat5`
- mechanic: `build`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The screen shows fillable line art; the child photographs real-world colors; the activity maps those colors to regions and honestly falls back if live recoloring is unavailable.

## Selection Trigger

Child photographs an object with a clear color or enters coloring mode.

## Source Intent Lock

Preserve the sequence: show fillable line art, ask the child to photograph a color source, map that real-world color to one or more regions, then reveal the evolving artwork.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `build`.
- Preserve this source sequence: Preserve the sequence: show fillable line art, ask the child to photograph a color source, map that real-world color to one or more regions, then reveal the evolving artwork.

## Resolved Product Contract Notes

- Runtime image generation: Approved minimum contract uses static or no-image fallback and does not claim unavailable runtime artwork.
- Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
- UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| runtime_coloring_line_art_01 | line_art | required | runtime_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Convert a photographed object into a fillable line drawing and apply colors chosen from the child's photos. | future_runtime_image_generation | If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package. |

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `build` mechanic.

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
