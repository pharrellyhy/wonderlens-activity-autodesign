# Reference Curation Attempt

Run: `20260601_155917_full_pass_agentic_tsv`

Scope:

- `concept_art_critic_tournament_probe/artwork_tournament_set_01`
- `concept_color_famous_art_probe/color_artwork_set_01`

These assets are `accuracy_mode: reference_bound`, so they must use accepted
public-domain, licensed, or internal reference sources. They must not be
replaced with generated approximations.

## Attempted Sources

- Hokusai, `The Great Wave off Kanagawa`, Wikimedia Commons file page:
  `https://commons.wikimedia.org/wiki/File:The_Great_Wave_off_Kanagawa.jpg`
- Van Gogh, `Sunflowers`, Metropolitan Museum of Art object image via IIIF:
  `https://collectionapi.metmuseum.org/api/collection/v1/iiif/436524/2341734/main-image`

## Fetch Result

The shell fetch path timed out before a verified source original could be stored
inside the package.

Commands attempted:

```bash
curl --max-time 60 --fail --silent --show-error -L \
  -o /tmp/wl_reference_assets/great_wave.jpg \
  'https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg'

curl -4 --connect-timeout 10 --max-time 30 --fail --silent --show-error -L \
  -o /tmp/wl_reference_assets/great_wave.jpg \
  'https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg'
```

Observed sanitized failures:

- `curl: (28) Connection timed out after 60010 milliseconds`
- `curl: (28) SSL connection timeout`

## Successful Fallback Curation

After the Wikimedia/Met fetch path failed, the run used Cleveland Museum of Art
Open Access API/CDN sources that report `share_license_status: CC0`.

Accepted sources:

- `concept_art_critic_tournament_probe/artwork_tournament_set_01`
  - Source: Katsushika Hokusai, `South Wind, Clear Sky`, accession `1930.189`
  - Page: `https://clevelandart.org/art/1930.189`
  - Image: `https://openaccess-cdn.clevelandart.org/1930.189/1930.189_web.jpg`
  - Stored original:
    `activity_packages/concept_art_critic_tournament_probe/assets/sources/artwork_tournament_set_01__source_original.jpg`
- `concept_color_famous_art_probe/color_artwork_set_01`
  - Source: Vincent van Gogh, `The Large Plane Trees (Road Menders at Saint-Remy)`, accession `1947.209`
  - Page: `https://clevelandart.org/art/1947.209`
  - Image: `https://openaccess-cdn.clevelandart.org/1947.209/1947.209_web.jpg`
  - Stored original:
    `activity_packages/concept_color_famous_art_probe/assets/sources/color_artwork_set_01__source_original.jpg`

Package-local source metadata was written beside each original and includes
source URI, license, `storage_allowed: true`, `verification_status: accepted`,
SHA-256, and reviewer evidence.
