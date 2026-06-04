# Asset Work Item: concept_constellation_star_count_enumerate/orion_seven_star_card

Mode: `generate_and_curate`
Package: `activity_packages/concept_constellation_star_count_enumerate`
Role: `story_scene`
Requiredness: `required`
Accuracy mode: `reference_bound`
Source strategy: `approved_internal_reference`
Transformation policy: `crop_resize_only`

## Prompt Or Source Requirement

Use the accepted package-local Orion teaching chart. Preserve exactly 7 prominent guide stars and approved guide-line shape. Do not add extra stars, text, labels, numbers, or fictional geometry.

## Declared Sources

- Approved internal Orion 7-guide-star teaching chart: internal://approved-constellation-reference/orion-7-guide-stars-v1 (Approved internal educational reference)

## Variants

- `round_512`: round_device_screen, 512x512

## Agent Instructions

Verify the source, store the accepted original in package-local `assets/sources/orion_seven_star_card__source_original.<ext>`, and only place a curated redraw in the inbox if the transformation policy requires one.

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
