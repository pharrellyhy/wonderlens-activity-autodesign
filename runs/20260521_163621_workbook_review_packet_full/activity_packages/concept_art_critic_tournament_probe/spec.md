# Art Critic Tournament - Engineering Spec

## Metadata

- activity_id: `concept_art_critic_tournament_probe`
- source_row: `34`
- source_concept: `source_art_critic_tournament`
- assignment_type: `capability_probe`
- category: `cat1`
- mechanic: `compare`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The child compares two approved artworks at a time, chooses a favorite, and keeps the winner moving until a final favorite wins.

## Selection Trigger

Product can show two approved artworks side by side and remember tournament progress.

## Source Intent Lock

The child compares two approved artworks at a time and chooses a favorite until one wins.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `compare`.
- Preserve this source sequence: The child compares two approved artworks at a time and chooses a favorite until one wins.

## Resolved Product Contract Notes

- UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| artwork_tournament_set_01 | approved_artwork_set | required | pre_curated | prod.step_2; prod.step_3.round_1-5 | center_card_area | Provide approved artwork pairs for comparison and tournament choice. | approved_public_domain_or_licensed_artwork_set | If the artwork set or tournament state is unavailable, block at Phase 0. |

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
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | The source action and mechanic stay aligned. |

**Overall**: PASS - fresh full-run package preserves source intent with explicit runtime-generation and minimum-unblock assumptions.
