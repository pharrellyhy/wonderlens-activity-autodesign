# Constellation Star Count Spec

## Premise

The child chooses between two numbers, then the device reveals a real approved constellation card matching that count and gives background information.

## Target

- Activity ID: `concept_constellation_star_count_enumerate`
- Template type: `cat1`
- Pillar / Game Style: Adventure / `time_traveler`
- Canonical mechanic: `enumerate`
- Demo support status: `supported`

## Adaptation Rationale

- **Core promise:** Child chooses between two counts, device reveals a real approved constellation matching the selected count, then gives background information.
- **Readiness:** `ready_for_demo`.
- **Canonical mechanic:** `enumerate` remains the primary child action; scaffold language is subordinate.
- **Product capability flags:** generated_assets, device_round_screen.
- **Asset dependency:** 2 declared runtime asset(s) in asset_manifest.yaml.
- **Demo support:** Status and ui_template in demo_support.yaml control downstream behavior.
- **Assumptions:** Scoped to this pilot and subject to delegated source-intent, visual, fullstack, and WonderLens AI review.

## Selection Trigger

Run-local pilot selection from `inputs/original_activity_concepts_2026-05-29.tsv`. The original workbook row controls over normalized helper wording when they conflict.

## Asset Brief

| asset_id | asset_type | requiredness | generation timing | use step | display location | purpose | prompt/source | display behavior | fallback behavior | safety constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| `cassiopeia_five_star_card` | story_scene | required | post-package asset_build=generate_and_curate | prod.md screen states | round device screen | Cassiopeia five-guide-star card | Reference-bound source: Approved internal Cassiopeia 5-guide-star teaching chart (internal://approved-constellation-reference/cassiopeia-5-guide-stars-v1, Approved internal educational reference). | Show only when prod.md names this asset_id. | If the accepted Cassiopeia source is unavailable, do not reveal or describe the constellation card. | No text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path. |
| `orion_seven_star_card` | story_scene | required | post-package asset_build=generate_and_curate | prod.md screen states | round device screen | Orion seven-guide-star card | Reference-bound source: Approved internal Orion 7-guide-star teaching chart (internal://approved-constellation-reference/orion-7-guide-stars-v1, Approved internal educational reference). | Show only when prod.md names this asset_id. | If the accepted Orion source is unavailable, do not reveal or describe the constellation card. | No text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path. |

## Asset Usage Timeline

| asset_id | source | load timing | display location | use | fallback |
|---|---|---|---|---|---|
| `cassiopeia_five_star_card` | package-local runtime PNG | loaded before referenced beat | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |
| `orion_seven_star_card` | package-local runtime PNG | loaded before referenced beat | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |

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
