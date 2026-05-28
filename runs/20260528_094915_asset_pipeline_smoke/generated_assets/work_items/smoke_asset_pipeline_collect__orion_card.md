# Asset Work Item: smoke_asset_pipeline_collect/orion_card

Mode: `generate_and_curate`
Package: `activity_packages/smoke_asset_pipeline_collect`
Role: `story_scene`
Requiredness: `required`
Accuracy mode: `reference_bound`
Source strategy: `licensed_reference`
Transformation policy: `crop_resize_only`

## Prompt Or Source Requirement

Preserve the accepted Orion source image layout when resizing. Do not add, remove, or stylize stars.

## Declared Sources

- NSF NOIRLab Orion chart, based on IAU and Sky & Telescope artwork: https://noirlab.edu/public/media/archives/images/large/ori.jpg (CC BY 4.0)

## Variants

- `round_1024`: round_device_screen, 1024x1024

## Agent Instructions

Verify the source, store the accepted original in package-local `assets/sources/orion_card__source_original.<ext>`, and only place a curated redraw in the inbox if the transformation policy requires one.

Do not use contact sheets as runtime assets. Do not use random approximations
for reference-bound assets. Keep important detail inside the central round-screen
safe area.
