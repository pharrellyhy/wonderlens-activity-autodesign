# Image Quality Repair

Run: `20260601_155917_full_pass_agentic_tsv`
Repair owner: master after delegated image improver shutdown
Repair timestamp: `2026-06-01T18:22:23+0800`

## Summary

The prior independent image QA found 29 passing assets, 1 repair-needed asset,
and 1 product-decision asset. This repair resolves both non-pass items without
changing source activity intent.

## Repairs

### Art Critic Tournament

Initial issue:

- `artwork_tournament_set_01` included visible printed cartouche text and a
  white/gray source border.
- The tournament package had one artwork asset while the runtime beat asks for
  two approved artworks side by side.

Repair:

- Cropped the accepted Hokusai source-derived runtime PNG so the cartouche text
  and source border are no longer visible.
- Added `artwork_tournament_challenger_01` using the current run's accepted
  Van Gogh Cleveland Museum of Art public-domain source.
- Updated `asset_manifest.yaml`, `spec.md`, and `prod.md` so the runtime screen
  contract uses `artwork_tournament_set_01` plus
  `artwork_tournament_challenger_01` in `side_by_side_compare_area`.

### Recognition Pop Challenge

Initial issue:

- `recognition_challenge_cards_01` was a single composite image while the
  runtime beat says three cards appear and then pop one at a time.

Repair:

- Replaced the composite asset with three separate package assets:
  `recognition_target_dog_card`, `recognition_distractor_fox_card`, and
  `recognition_distractor_wolf_card`.
- Removed the stale composite runtime PNG and inbox source.
- Updated `asset_manifest.yaml`, `spec.md`, and `prod.md` so timing remains
  target-vs-distractor: say the target word on dog, stay quiet for fox/wolf.

## Validation

```bash
/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/build_activity_assets.py \
  runs/20260601_155917_full_pass_agentic_tsv --mode generate_and_curate
```

Result: `OK asset build: mode=generate_and_curate packages=40 assets=34 built=34 required_failures=0`

```bash
/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/validate_asset_build_outputs.py \
  runs/20260601_155917_full_pass_agentic_tsv
```

Result: `OK asset build outputs: runs/20260601_155917_full_pass_agentic_tsv`

```bash
/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/validate_demo_package_contract.py \
  runs/20260601_155917_full_pass_agentic_tsv/activity_packages
```

Result: `OK demo package contract: 40 package(s)`

## Residual Risk

- The original independent image QA report is preserved as historical evidence
  and still shows the pre-repair fail verdict. A new independent image QA pass
  is required before the image-quality gate can be considered passing.

