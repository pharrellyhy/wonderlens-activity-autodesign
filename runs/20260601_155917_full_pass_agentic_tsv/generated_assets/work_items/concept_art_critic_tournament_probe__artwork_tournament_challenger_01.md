# Asset Work Item: concept_art_critic_tournament_probe/artwork_tournament_challenger_01

Mode: `generate_and_curate`
Package: `activity_packages/concept_art_critic_tournament_probe`
Role: `story_scene`
Requiredness: `required`
Accuracy mode: `reference_bound`
Source strategy: `curated_original`
Transformation policy: `crop_resize_only`

## Prompt Or Source Requirement

Use the accepted package-local Van Gogh public-domain reference artwork as the tournament challenger. Do not invent, redraw, or approximate the artwork.

## Declared Sources

- Vincent van Gogh, The Large Plane Trees (Road Menders at Saint-Remy): https://clevelandart.org/art/1947.209 (CC0 1.0 / Cleveland Museum of Art Open Access)

## Variants

- `round_512`: round_device_screen, 512x512

## Agent Instructions

Verify the source, store the accepted original in package-local `assets/sources/artwork_tournament_challenger_01__source_original.<ext>`, and only place a curated redraw in the inbox if the transformation policy requires one.

Do not use contact sheets as runtime assets. Do not use random approximations
for reference-bound assets. Keep important detail inside the central round-screen
safe area.
