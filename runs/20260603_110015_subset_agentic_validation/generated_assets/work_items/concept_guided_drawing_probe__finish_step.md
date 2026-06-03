# Asset Work Item: concept_guided_drawing_probe/finish_step

Mode: `generate_and_curate`
Package: `activity_packages/concept_guided_drawing_probe`
Role: `story_scene`
Requiredness: `required`
Accuracy mode: `illustrative`
Source strategy: `generated_illustrative`
Transformation policy: `generate_new`

## Prompt Or Source Requirement

Flat Nordic children illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye and texture linework, restrained boho pastels, generous negative space, square 512x512 source art, no readable text, no letters or numbers, no logos, no watermark, no masks, no borders, and no baked UI chrome. Subject: paper with the simple finished drawing and one small face detail. One visual unit only. Keep important detail inside the central safe area. For scenes, no selectable target objects that compete with separate sprites.

## Declared Sources

- None declared

## Variants

- `round_512`: round_device_screen, 512x512

## Agent Instructions

Generate exactly one 512x512 source PNG into `generated_assets/inbox/concept_guided_drawing_probe/finish_step.png` using the prompt and device style. The source PNG must contain one visual unit for this asset role only; split scenes, objects, items, characters, icons, badges, and distractors into separate asset IDs instead of combining multiple cards or a contact sheet in one runtime image. If the image tool returns a larger square, downsample the accepted source to 512x512 before running this builder. Existing accepted sources may be any supported square size: 512x512; runtime variants are resized from the accepted source according to the manifest.

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
