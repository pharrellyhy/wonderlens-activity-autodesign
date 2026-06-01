# Guided Drawing Spec

## Premise

The child would use paper and pencil while AI guides a simple drawing step by step, then photograph the finished work for celebration.

## Target

- Activity ID: `concept_guided_drawing_probe`
- Template type: `cat3`
- Pillar / Game Style: Creation / `maker_steps`
- Canonical mechanic: `build`
- Demo support status: `unsupported`

## Adaptation Rationale

- **Core promise:** AI guides paper-and-pencil drawing step by step, waits for process, and celebrates a final whole-work photo without quality grading.
- **Readiness:** `blocked_until_product_decision`.
- **Canonical mechanic:** `build` remains the primary child action; scaffold language is subordinate.
- **Product capability flags:** real_camera, device_round_screen.
- **Asset dependency:** 0 declared runtime asset(s) in asset_manifest.yaml.
- **Demo support:** Status and ui_template in demo_support.yaml control downstream behavior.
- **Assumptions:** Scoped to this pilot and subject to delegated source-intent, visual, fullstack, and WonderLens AI review.

## Selection Trigger

Run-local pilot selection from `inputs/original_activity_concepts_2026-05-29.tsv`. The original workbook row controls over normalized helper wording when they conflict.

## Asset Brief

| asset_id | asset_type | requiredness | generation timing | use step | display location | purpose | prompt/source | display behavior | fallback behavior | safety constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| none | none | none | no asset generation | no playable display | none | No runtime asset required. | No prompt/source. | No display. | No fallback. | No special constraint. |

## Asset Usage Timeline

| asset_id | source | load timing | display location | use | fallback |
|---|---|---|---|---|---|
| none | none | none | none | no runtime image dependency | no asset fallback needed |

## Unsupported Product Contract Notes

This package is structurally valid but intentionally not playable. Consumers should gate it instead of converting the source into a thinner Cat1 or Cat5 activity.

## Self-Evaluation Scorecard

| # | Dimension | Result | Why |
|---|---|---|---|
| 1 | V1 technical compliance | PASS | Support status and runtime requirements match demo_support.yaml. |
| 2 | Hook quality | PASS | Step 1 frames the source activity without a cold quiz. |
| 3 | Transition quality | PASS | Step 2 moves into the promised child action. |
| 4 | Edge-case handling | PASS | Every runtime beat has ideal, unexpected, and no-response branches. |
| 5 | IB alignment | PASS | Key concepts match what the child actually does. |
| 6 | Tier fit | PASS | Runtime constraints use short T1 language. |
| 7 | Dialogue/runtime contract | PASS | Runtime AI instructions include labels needed for downstream step_instructions. |
| 8 | Screen/state specificity | PASS | Screen states name assets, photo slots, or gated state. |
| 9 | Source integrity | PASS | Original sequence is preserved or unsupported capability is gated. |
| 10 | Mechanic fidelity | PASS | Step 3 child action matches the canonical mechanic and source promise. |
