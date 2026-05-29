# Asset Work Item: e2e_orion_number_reveal/orion_seven_star_card

Mode: `generate_and_curate`
Package: `activity_packages/e2e_orion_number_reveal`
Role: `story_scene`
Requiredness: `required`
Accuracy mode: `reference_bound`
Source strategy: `licensed_reference`
Transformation policy: `simplified_redraw`

## Prompt Or Source Requirement

Create a simplified redraw from the verified Orion source data. Preserve the seven guide-star layout used for Orion, draw only those seven countable stars plus simple connecting guide lines, and do not add background stars, labels, numbers, text, or invented constellations.

## Declared Sources

- NSF NOIRLab Orion chart based on IAU and Sky & Telescope artwork: https://noirlab.edu/public/media/archives/images/large/ori.jpg (CC BY 4.0)

## Variants

- `round_512`: round_device_screen, 512x512

## Agent Instructions

Verify the source, store the accepted original in package-local `assets/sources/orion_seven_star_card__source_original.<ext>`, and only place a curated redraw in the inbox if the transformation policy requires one.

Do not use contact sheets as runtime assets. Do not use random approximations
for reference-bound assets. Keep important detail inside the central round-screen
safe area.
