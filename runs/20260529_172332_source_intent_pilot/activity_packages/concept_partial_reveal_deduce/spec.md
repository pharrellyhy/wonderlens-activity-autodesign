# Partial Reveal Guess Spec

## Premise

The screen shows a distinctive animal part and the child guesses the whole animal from visible evidence.

## Target

- Activity ID: `concept_partial_reveal_deduce`
- Template type: `cat1`
- Pillar / Game Style: Mystery / `clue_detective`
- Canonical mechanic: `deduce`
- Demo support status: `supported`

## Adaptation Rationale

- **Core promise:** Screen shows a distinctive part, child guesses the whole, and AI follows visible evidence.
- **Readiness:** `ready_for_demo`.
- **Canonical mechanic:** `deduce` remains the primary child action; scaffold language is subordinate.
- **Product capability flags:** generated_assets, device_round_screen.
- **Asset dependency:** 3 declared runtime asset(s) in asset_manifest.yaml.
- **Demo support:** Status and ui_template in demo_support.yaml control downstream behavior.
- **Assumptions:** Scoped to this pilot and subject to delegated source-intent, visual, fullstack, and WonderLens AI review.

## Selection Trigger

Run-local pilot selection from `inputs/original_activity_concepts_2026-05-29.tsv`. The original workbook row controls over normalized helper wording when they conflict.

## Asset Brief

| asset_id | asset_type | requiredness | generation timing | use step | display location | purpose | prompt/source | display behavior | fallback behavior | safety constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| `rabbit_ears_reveal_card` | story_scene | required | post-package asset_build=generate_and_curate | prod.md screen states | round device screen | rabbit ears partial reveal card | Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: Partial-reveal animal guessing card showing only two long rabbit ears and a tiny top-of-head hint, not the full animal.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette. | Show only when prod.md names this asset_id. | If rabbit_ears_reveal_card is unavailable, preserve support honesty and do not claim this asset is visible. | No text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path. |
| `tiger_tail_reveal_card` | story_scene | required | post-package asset_build=generate_and_curate | prod.md screen states | round device screen | tiger tail partial reveal card | Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: Partial-reveal animal guessing card showing only an orange striped tiger tail curling into view, not the full animal.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette. | Show only when prod.md names this asset_id. | If tiger_tail_reveal_card is unavailable, preserve support honesty and do not claim this asset is visible. | No text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path. |
| `elephant_trunk_reveal_card` | story_scene | required | post-package asset_build=generate_and_curate | prod.md screen states | round device screen | elephant trunk partial reveal card | Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: Partial-reveal animal guessing card showing only a gentle elephant trunk and one soft ear edge, not the full animal.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette. | Show only when prod.md names this asset_id. | If elephant_trunk_reveal_card is unavailable, preserve support honesty and do not claim this asset is visible. | No text, labels, logos, watermark, device chrome, circular mask, contact sheet, or unsafe path. |

## Asset Usage Timeline

| asset_id | source | load timing | display location | use | fallback |
|---|---|---|---|---|---|
| `rabbit_ears_reveal_card` | package-local runtime PNG | loaded before referenced beat | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |
| `tiger_tail_reveal_card` | package-local runtime PNG | loaded before referenced beat | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |
| `elephant_trunk_reveal_card` | package-local runtime PNG | loaded before referenced beat | round device screen | prod.md screen states name this asset_id | missing required asset gates or degrades playback |

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
