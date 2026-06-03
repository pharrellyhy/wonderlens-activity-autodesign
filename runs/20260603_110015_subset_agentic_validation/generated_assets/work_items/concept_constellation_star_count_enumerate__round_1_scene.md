# Asset Work Item: concept_constellation_star_count_enumerate/round_1_scene

Mode: `generate_and_curate`
Package: `activity_packages/concept_constellation_star_count_enumerate`
Role: `story_scene`
Requiredness: `required`
Accuracy mode: `illustrative`
Source strategy: `generated_illustrative`
Transformation policy: `generate_new`

## Prompt Or Source Requirement

Use case: illustration-story. Asset type: WonderLens full-pass runtime activity asset. Primary request: Round 1 scene for Constellation Number Reveal. Composition: full-bleed square beat scene, softly painterly nursery composition, no app UI; generate a 512x512 square source PNG; if the image tool returns a larger square, downsample it to 512x512 before asset build; keep important details inside the central round-lens safe area. Source beat context, for subject only: Use `round_1_scene` app overlays two number choices separately, no constellation card yet. Activity-specific direction: choose a visual motif unique to this activity's source promise and mechanic; avoid reusing the same blank-board, child-on-rug, response-slot, or cozy-room template across activities. Style: flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse arc-eye or tiny texture linework, light colored-pencil grain, restrained boho pastels, airy negative space, organic simple silhouettes. No readable text, letters, numbers, labels, logos, watermark, border, contact sheet, multi-card sheet, device frame, circular mask, vignette, black corners, glossy eyes, chibi toy look, hard shadows, or clutter. Do not draw progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, badges, or other app-owned interface state; the runtime overlays those separately.

## Declared Sources

- None declared

## Variants

- `round_512`: round_device_screen, 512x512

## Agent Instructions

Generate exactly one 512x512 source PNG into `generated_assets/inbox/concept_constellation_star_count_enumerate/round_1_scene.png` using the prompt and device style. The source PNG must contain one visual unit for this asset role only; split scenes, objects, items, characters, icons, badges, and distractors into separate asset IDs instead of combining multiple cards or a contact sheet in one runtime image. If the image tool returns a larger square, downsample the accepted source to 512x512 before running this builder. Existing accepted sources may be any supported square size: 512x512; runtime variants are resized from the accepted source according to the manifest.

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
