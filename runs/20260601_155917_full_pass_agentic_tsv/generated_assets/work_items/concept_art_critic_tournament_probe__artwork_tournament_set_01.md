# Asset Work Item: concept_art_critic_tournament_probe/artwork_tournament_set_01

Mode: `generate_and_curate`
Package: `activity_packages/concept_art_critic_tournament_probe`
Role: `story_scene`
Requiredness: `required`
Accuracy mode: `reference_bound`
Source strategy: `curated_original`
Transformation policy: `crop_resize_only`

## Prompt Or Source Requirement

Use only approved public-domain, licensed, or internal reference artwork for this package. Do not invent or approximate the artwork set.

## Declared Sources

- Pending approved source set for artwork_tournament_set_01: pending://approved-reference-curation/artwork_tournament_set_01 (Pending approved public-domain, licensed, or internal reference curation)

## Variants

- `round_512`: round_device_screen, 512x512

## Agent Instructions

Verify the source, store the accepted original in package-local `assets/sources/artwork_tournament_set_01__source_original.<ext>`, and only place a curated redraw in the inbox if the transformation policy requires one.

Do not use contact sheets as runtime assets. Do not use random approximations
for reference-bound assets. Keep important detail inside the central round-screen
safe area.
