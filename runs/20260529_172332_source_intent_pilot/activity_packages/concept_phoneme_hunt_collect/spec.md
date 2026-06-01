# Phoneme Treasure Hunt Spec

## Premise

The child hears a target sound, finds a real object whose name starts with that sound, photographs it, and supplies the name evidence.

## Target

- Activity ID: `concept_phoneme_hunt_collect`
- Template type: `cat5`
- Pillar / Game Style: Adventure / `quest_collector`
- Canonical mechanic: `collect`
- Demo support status: `degraded`

## Adaptation Rationale

- **Core promise:** Child uses B-sound support, captures one real object, and supplies the name so the target sound remains the collection criterion.
- **Readiness:** `degraded_demo`.
- **Canonical mechanic:** `collect` remains the primary child action; scaffold language is subordinate.
- **Product capability flags:** generated_assets, real_camera, runtime_judgment, device_round_screen.
- **Asset dependency:** 2 declared runtime asset(s) in asset_manifest.yaml.
- **Demo support:** Status and ui_template in demo_support.yaml control downstream behavior.
- **Assumptions:** Scoped to this pilot and subject to delegated source-intent, visual, fullstack, and WonderLens AI review.

## Selection Trigger

Run-local pilot selection from `inputs/original_activity_concepts_2026-05-29.tsv`. The original workbook row controls over normalized helper wording when they conflict.

## Asset Brief

| asset_id | asset_type | requiredness | generation timing | use step | display location | purpose | prompt/source | display behavior | fallback behavior | safety constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| `ball_b_sound_clue` | activity_preview | required | post-package asset_build=generate_and_curate | prod.md screen states | round device screen | ball B-sound visual clue | Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: A single friendly round ball object clue for a B-sound treasure hunt.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette. | Show only when prod.md names this asset_id. | If ball_b_sound_clue is unavailable, preserve support honesty and do not claim this asset is visible. | No text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path. |
| `banana_b_sound_clue` | activity_preview | required | post-package asset_build=generate_and_curate | prod.md screen states | round device screen | banana B-sound visual clue | Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: A single curved banana object clue for a B-sound treasure hunt.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette. | Show only when prod.md names this asset_id. | If banana_b_sound_clue is unavailable, preserve support honesty and do not claim this asset is visible. | No text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path. |

## Asset Usage Timeline

| asset_id | source | load timing | display location | use | fallback |
|---|---|---|---|---|---|
| `ball_b_sound_clue` | package-local runtime PNG | loaded before referenced beat | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |
| `banana_b_sound_clue` | package-local runtime PNG | loaded before referenced beat | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |

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
