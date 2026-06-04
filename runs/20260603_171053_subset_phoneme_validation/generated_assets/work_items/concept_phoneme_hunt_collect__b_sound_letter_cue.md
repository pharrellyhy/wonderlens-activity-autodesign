# Asset Work Item: concept_phoneme_hunt_collect/b_sound_letter_cue

Mode: `generate_and_curate`
Package: `activity_packages/concept_phoneme_hunt_collect`
Role: `ui_overlay`
Requiredness: `optional`
Accuracy mode: `illustrative`
Source strategy: `generated_illustrative`
Transformation policy: `generate_new`

## Prompt Or Source Requirement

Use case: illustration-story. Asset type: text-free listening support tile. Primary request: one centered rounded listening tile for a runtime-owned target sound overlay; include a simple mouth-and-sound-wave pictogram so the image is not a blank placeholder. The generated image itself must contain no letters or words. Scene/backdrop: clean white. Style/medium: flat Nordic children's illustration matching docs/asset_style_reference/wonderlens-activity-style.md and style-reference-flat-nordic.png with restrained boho pastels and light paper grain. Composition/framing: one centered tile, generous padding, safe inside round crop. Constraints: no readable text, no letters, no numbers, no labels, no logos, no watermark, no app UI, no border, no progress dots, no basket, no treasure chest, no blank card, no blank board, no empty container.

## Style Reference Required For Imagegen

- Style prompt: `docs/asset_style_reference/wonderlens-activity-style.md`
- Reference image: `docs/asset_style_reference/style-reference-flat-nordic.png`
- Tool: Codex built-in imagegen

When generating an illustrative source PNG, combine the asset-specific prompt
above with the style prompt and use the reference image as the visual target.
Do not substitute SVG, vector, script-generated, or placeholder art.

## Declared Sources

- None declared

## Variants

- `round_512`: round_device_screen, 512x512

## Agent Instructions

Generate exactly one 512x512 source PNG into `generated_assets/inbox/concept_phoneme_hunt_collect/b_sound_letter_cue.png` using Codex built-in imagegen, the prompt below, `docs/asset_style_reference/wonderlens-activity-style.md`, and `docs/asset_style_reference/style-reference-flat-nordic.png`. The source PNG must contain one visual unit for this asset role only; split scenes, objects, items, characters, icons, badges, and distractors into separate asset IDs instead of combining multiple cards or a contact sheet in one runtime image. If the image tool returns a larger square, downsample the accepted source to 512x512 before running this builder. Existing accepted sources may be any supported square size: 512x512; runtime variants are resized from the accepted source according to the manifest.

## Prompt Trace Requirement

Record the exact final prompt text submitted to imagegen, or state that the
provider/tool did not expose an exact request payload. Keep secrets out of
trace files. For subset/full-pass runs, copy this evidence into the run-local
manual prompt trace for the activity.

Do not use contact sheets, multi-card sheets, labels, or baked UI chrome as
runtime assets. Do not use random approximations for reference-bound assets.
Keep important detail inside the central round-screen safe area.
Do not bake app-owned UI state into image files: no progress dots, round tokens,
response slots, rule strips, buttons, badges, chips, picker slots, device
chrome, or other runtime interface markers. The app/runtime overlays progress
and controls separately.
Full-pass scenes must be visually distinct by activity and grounded in the
source action for that exact beat. Do not reuse a generic cozy-room/blank-board
template across unrelated activities.
For guided drawing or other step-by-step build flows, each round scene must
show the drawing/building instruction for that step, such as the starting
shape, the added detail, then the finished simple form. Do not substitute
generic materials, locks, timers, cameras, or placeholder cards when the
runtime beat is supposed to tell the child what to do.
Hard source-intent visual QA: if the activity advances by selecting an
item/object, do not put duplicate selectable items/objects in background scenes
where they compete with picker sprites, target/distractor cards, or collection
items. If the activity builds evidence step by step or uses partial reveal, do
not show the final answer, full target, or solution before the source-aligned
reveal beat. Align this asset to its runtime beat step by step; violations are
hard repair findings, not polish notes.
