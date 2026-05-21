# Color In Famous Art - Engineering Spec

## Metadata

- activity_id: `concept_color_famous_art_probe`
- source_row: `35`
- source_concept: `source_color_in_famous_art`
- assignment_type: `capability_probe`
- category: `cat1`
- mechanic: `enumerate`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The child photographs or names a real-world color, then sees several approved artworks where that color is dominant or important.

## Selection Trigger

Child photographs or names a clear color and the screen can show approved public-domain artwork with known color metadata.

## Source Intent Lock

Preserve the sequence: child captures or chooses a real-world color, the system shows several artworks dominated by that color, then the AI gives a simple child-safe background introduction. Do not reduce this to studying one artwork first.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `enumerate`.
- Preserve this source sequence: Preserve the sequence: child captures or chooses a real-world color, the system shows several artworks dominated by that color, then the AI gives a simple child-safe background introduction. Do not reduce this to studying one artwork first.

## Resolved Product Contract Notes

- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| color_artwork_set_01 | approved_artwork_set | required | pre_curated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Provide approved artworks with known dominant color metadata. | approved_public_domain_or_licensed_artwork_set | If the artwork set is unavailable, block at Phase 0 rather than referencing famous art that cannot be shown. |

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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | The source action and mechanic stay aligned. |

**Overall**: PASS - fresh full-run package preserves source intent with explicit runtime-generation and minimum-unblock assumptions.
