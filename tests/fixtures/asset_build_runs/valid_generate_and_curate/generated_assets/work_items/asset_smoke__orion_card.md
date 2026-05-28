# Asset Work Item: asset_smoke/orion_card

Mode: `generate_and_curate`
Package: `activity_packages/asset_smoke`
Role: `story_scene`
Requiredness: `required`
Accuracy mode: `reference_bound`
Source strategy: `curated_original`
Transformation policy: `crop_resize_only`

## Prompt Or Source Requirement

Preserve the approved Orion star layout exactly; add no extra stars.

## Declared Sources

- Approved internal Orion chart: internal://reference/astronomy/orion (approved_internal_reference)

## Variants

- `round_1024`: round_device_screen, 1024x1024

## Agent Instructions

Verify the source, store the accepted original in package-local `assets/sources/orion_card__source_original.<ext>`, and only place a curated redraw in the inbox if the transformation policy requires one.

Do not use contact sheets as runtime assets. Do not use random approximations
for reference-bound assets. Keep important detail inside the central round-screen
safe area.
