# Career Decision Role Play - Engineering Spec

## Metadata

- activity_id: `concept_career_decision_decide`
- source_row: `26`
- source_concept: `source_career_decision`
- assignment_type: `activity_concept`
- category: `cat1`
- mechanic: `decide`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The AI first assigns the child a profession, then places the child inside a concrete work scenario where they make expert decisions.

## Selection Trigger

Child sees a professional role, tool, uniform, vehicle, or story character connected to work.

## Source Intent Lock

Preserve the sequence: assign the child a profession, place them inside a concrete work scenario, ask a simple expert decision, then respond to the decision. Do not turn this into choosing which profession matches a scenario.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `decide`.
- Preserve this source sequence: Preserve the sequence: assign the child a profession, place them inside a concrete work scenario, ask a simple expert decision, then respond to the decision. Do not turn this into choosing which profession matches a scenario.

## Resolved Product Contract Notes

- Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

## Asset Usage Timeline

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_or_source | fallback_behavior |
|---|---|---|---|---|---|---|---|---|
| career_portrait_cards_01 | card_set | optional | pre_generated | prod.step_2; prod.step_3.round_1-3 | center_card_area | Provide inclusive helper-role visuals for scenario decisions. | new_ai_generated_asset | If cards are unavailable, describe the helper role by voice and avoid claiming the screen shows a person. |

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `decide` mechanic.

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
