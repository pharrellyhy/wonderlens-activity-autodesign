# Vegetable Sort - Engineering Spec

## Metadata

- activity_id: `concept_vegetable_sort_sort`
- source_row: `27`
- source_concept: `source_vegetable_sort`
- assignment_type: `activity_concept`
- category: `cat1`
- mechanic: `sort`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The child uses tap/select vegetable cards to sort by a visible or meaningful rule.

## Selection Trigger

Screen can show vegetable cards that the child taps or names by group.

## Source Intent Lock

The child uses tap/select vegetable cards to sort by a visible or meaningful rule.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `sort`.
- Preserve this source sequence: The child uses tap/select vegetable cards to sort by a visible or meaningful rule.

## Resolved Product Contract Notes

- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| vegetable_sort_cards_01 | card_set | required | pre_generated | prod.step_2; prod.step_3.round_1-3 | round_device_screen | Provide vegetable cards that can be sorted by color, shape, edible part, or cooking use. | new_ai_generated_asset | If card art is unavailable, use text labels and ask the child to tap or say the matching group. |

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `sort` mechanic.

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
