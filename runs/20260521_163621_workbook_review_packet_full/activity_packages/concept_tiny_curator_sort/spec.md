# Tiny Curator - Engineering Spec

## Metadata

- activity_id: `concept_tiny_curator_sort`
- source_row: `14`
- source_concept: `source_tiny_curator`
- assignment_type: `match_pattern`
- category: `cat5`
- mechanic: `sort`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The child finds three or four objects they think belong together, arranges them as a tiny exhibition, and explains their grouping rule.

## Selection Trigger

Child is at home or outdoors with several objects that can be grouped or compared.

## Source Intent Lock

The child finds three or four objects they think belong together, arranges them as a tiny exhibition, and explains their grouping rule.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `sort`.
- Preserve this source sequence: The child finds three or four objects they think belong together, arranges them as a tiny exhibition, and explains their grouping rule.

## Resolved Product Contract Notes

- None. No formerly blocking product dependency is required for the minimum package.

## Asset Usage Timeline

No asset dependency. The activity can run voice-only with ordinary runtime screen states.

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
