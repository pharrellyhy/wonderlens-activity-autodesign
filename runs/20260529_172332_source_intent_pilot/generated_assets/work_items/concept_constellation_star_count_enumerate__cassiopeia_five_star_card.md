# Asset Work Item: concept_constellation_star_count_enumerate/cassiopeia_five_star_card

Mode: `generate_and_curate`
Package: `activity_packages/concept_constellation_star_count_enumerate`
Role: `story_scene`
Requiredness: `required`
Accuracy mode: `reference_bound`
Source strategy: `approved_internal_reference`
Transformation policy: `crop_resize_only`

## Prompt Or Source Requirement

Use the accepted package-local Cassiopeia teaching chart. Preserve exactly 5 prominent guide stars and approved guide-line shape. Do not add extra stars, text, labels, numbers, or fictional geometry.

## Declared Sources

- Approved internal Cassiopeia 5-guide-star teaching chart: internal://approved-constellation-reference/cassiopeia-5-guide-stars-v1 (Approved internal educational reference)

## Variants

- `round_512`: round_device_screen, 512x512

## Agent Instructions

Verify the source, store the accepted original in package-local `assets/sources/cassiopeia_five_star_card__source_original.<ext>`, and only place a curated redraw in the inbox if the transformation policy requires one.

Do not use contact sheets as runtime assets. Do not use random approximations
for reference-bound assets. Keep important detail inside the central round-screen
safe area.
