# Would You Rather Spec

## Premise

The child answers short playful Would You Rather questions and gives a tiny preference reason.

## Target

- Activity ID: `concept_would_you_rather_compare`
- Template type: `cat1`
- Pillar / Game Style: Performance / `choice_chain`
- Canonical mechanic: `compare`
- Demo support status: `supported`

## Adaptation Rationale

- **Core promise:** Child repeatedly compares two short playful options, chooses one, and gives a tiny reason.
- **Readiness:** `ready_for_demo`.
- **Canonical mechanic:** `compare` remains the primary child action; scaffold language is subordinate.
- **Product capability flags:** device_round_screen.
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
