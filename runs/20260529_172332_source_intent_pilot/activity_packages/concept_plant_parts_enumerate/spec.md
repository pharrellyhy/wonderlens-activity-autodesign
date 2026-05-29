# Plant Parts Explorer Spec

## Premise

The child photographs different plant positions such as leaf, flower, or stem and hears simple function/background notes.

## Target

- Activity ID: `concept_plant_parts_enumerate`
- Template type: `cat5`
- Pillar / Game Style: Discovery / `field_experiment`
- Canonical mechanic: `enumerate`
- Demo support status: `unsupported`

## Adaptation Rationale

- **Core promise:** Child photographs different plant locations and receives interesting part-function background notes.
- **Readiness:** `blocked_until_product_decision`.
- **Canonical mechanic:** `enumerate` remains the primary child action; scaffold language is subordinate.
- **Product capability flags:** real_camera, device_round_screen.
- **Asset dependency:** 0 declared runtime asset(s) in asset_manifest.yaml.
- **Demo support:** `unsupported` / `ui_template: none` gates this package so consumers do not convert Cat5 enumerate into a misleading collect loop.
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

This package is structurally valid but intentionally not playable in the current downstream runtime templates. The source promise is photo-based enumeration of different plant parts plus part-function/background context; changing `mechanic: enumerate` to `collect` would be source-intent drift.

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
