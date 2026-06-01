# WonderLens Activity Asset Generation Workflow

This document records the workflow used to create runtime image assets for
autodesign activity packages.

Latest style source reviewed on 2026-05-29:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game/frontend/public/activity-assets/prompts/wonderlens-activity-style.md
```

The schema value remains `style_id: wonderlens_device_mint_soft_3d` for
consumer compatibility. The current visual target for that style is the flat
Nordic nursery illustration style below, not the older soft-3D toy look.

## When Assets Are Generated

Package authoring does not create binary images. `GOAL.md` runs default to
`asset_build=manifest_only`, which emits `asset_manifest.yaml` with nullable
variant paths.

Larger/full production passes must set `asset_build=generate_and_curate` so
runtime PNGs are generated or curated before fullstack-demo and WonderLens AI
dialogue validation. The asset generator role is image-only: it reads the
accepted package manifest, approved reference material, and this style contract;
it must not rewrite activity mechanics, runtime AI instructions, source-intent
audits, or dialogue to make an image easier to accept.

Generate or curate image files only after packages pass package validation and
the run explicitly requests one of these modes:

- `generate_illustrative`: generate only `accuracy_mode: illustrative` assets.
- `curate_reference`: curate only `accuracy_mode: reference_bound` assets.
- `generate_and_curate`: do both.

## Source Of Truth

Use package files in this order:

1. `asset_manifest.yaml` is the machine-readable source request: asset IDs,
   roles, prompts/sources, accuracy mode, variants, nullable paths, and
   fallback behavior.
2. `spec.md` explains reviewer-facing `## Asset Brief` and
   `## Asset Usage Timeline` rationale.
3. `prod.md` references stable `asset_id` values, display locations, and
   fallback behavior. It should not contain raw image-generation prompts.

Do not rewrite activity mechanics or runtime prose to fit generated images.
Assets support the accepted activity design.

## Illustrative Asset Workflow

1. Read each illustrative asset entry in `asset_manifest.yaml`.
2. Combine the asset-specific `prompt_en` subject with the current WonderLens
   activity style in this document.
3. Use Codex built-in image generation to create one source image per asset.
   Do not create contact sheets for runtime assets. Prompts should combine the
   asset-specific subject, scene/object/item role, use beat, and the full style
   contract below so the output aligns with the dialogue and screen state.
4. Select the best output, then copy it from
   `/Users/pharrelly/.codex/generated_images/...` into:

```text
runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png
```

5. Visually inspect the PNG before running the builder:
   - image is square and at least 512x512;
   - no text, letters, numbers, logos, watermarks, UI labels, borders, masks,
     vignettes, black corners, or baked device chrome;
   - the style matches the flat Nordic nursery target;
   - item/object/character assets have one centered subject with generous clean
     white padding;
   - scene/background assets are full-bleed square images and keep important
     content inside the round lens-safe center.
6. Run the deterministic builder:

```bash
python3 scripts/build_activity_assets.py runs/<run_id> --mode generate_illustrative
```

Use `--mode generate_and_curate` when the same run also has reference-bound
assets.

The builder consumes the inbox PNGs, writes package-local runtime variants
under `runs/<run_id>/activity_packages/<activity_id>/assets/`, updates
package-relative paths in `asset_manifest.yaml`, and writes run audit files
under `runs/<run_id>/generated_assets/`.

## Reference-Bound Asset Workflow

Reference-bound assets include constellations, artworks, maps, scientific
diagrams, cultural artifacts, species, historical objects, named places, and
famous structures. Do not use random generated approximations for these.

1. Use `asset_manifest.yaml` `reference_policy` and `sources` to identify the
   required source type and transformation policy.
2. Accept only approved internal references, licensed assets, public-domain
   references, official sources, or verified educational/scientific sources.
3. Store the accepted original under the package:

```text
runs/<run_id>/activity_packages/<activity_id>/assets/sources/<asset_id>__source_original.<ext>
```

4. Store reviewer-approved metadata beside it:

```text
runs/<run_id>/activity_packages/<activity_id>/assets/sources/<asset_id>__source_metadata.yaml
```

Required metadata includes `source_type`, verified `license`,
`storage_allowed: true`, `verification_status: accepted`, matching `sha256`,
`verified_at`, and `reviewer_agent`.

5. If `transformation_policy` requires a curated redraw, place the reviewed
   redraw in:

```text
runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>__curated.png
```

6. Run:

```bash
python3 scripts/build_activity_assets.py runs/<run_id> --mode curate_reference
```

Use `--mode generate_and_curate` when illustrative assets are also present.

## Current Style Contract

Use case: `illustration-story`.

Visual target:

- flat Nordic children's illustration matching the quiet white WonderLens
  prototype;
- asymmetric simple silhouettes, large blocky body shapes, muted salmon and
  dusty blue characters, pale cheeks, arc eyes, sparse decorative strokes,
  thin colored-pencil linework, light paper grain inside subjects, airy nursery
  composition, and generous negative space;
- broad flat color fills with linework only for arc eyes, tiny facial marks,
  and sparse short texture dashes.

Palette:

- clean white or barely tinted white background;
- restrained boho pastels inside subjects: oatmeal beige, muted sage, dusty
  teal-blue, soft terracotta/salmon, warm brown, mustard/ochre, blush pink,
  pale leaf green, and muted sky accents;
- brighter yellow, coral, cyan, or lavender only as tiny accents.

Avoid:

- generic chibi/toy vocabulary, glossy eyes, dimensional modeling, bevels, hard
  shadows, deep perspective, heavy texture, cartoon clutter, thick outlines,
  raised seams, clothing construction lines, internal contour bands, dominant
  mint, dominant blue, dominant purple, black-heavy screens, neon pink, or neon
  cyan.

Composition:

- generate square source art;
- background scenes are full-bleed 512x512 images that can be clipped by the
  device's circular lens;
- item, object, and character assets are separate reusable PNGs with one
  centered subject per file, generous clean white padding, and no baked UI
  frame unless the frame itself is the intended object.

Hard constraints:

- no circular or oval image mask;
- no baked-in lens border, rim, vignette, black corners, transparent margin,
  colored border, readable text, letters, numbers, logos, watermark, UI labels,
  or combined multi-image source asset.

Final runtime outputs should include separate 512x512 PNG files for each beat,
item, object, or character asset unless `asset_manifest.yaml` explicitly
requests another size.

## Independent Image QA

After the builder writes package-local PNG variants, run an independent image
quality validator before consumer dialogue QA. The validator reads
`asset_manifest.yaml`, `prod.md` runtime beats, accepted reference metadata,
and the generated PNGs. It records concrete asset paths, verdicts, and repair
requests in `generated_assets/qa_notes.yaml` or `review_notes.md`.

The validator checks:

- style consistency with the current flat Nordic WonderLens target;
- one asset per file, with scene/object/item/character role matching the
  manifest;
- scene and object content aligns with the dialogue beat and screen state;
- object readability at runtime size;
- important content stays inside the round lens-safe center when relevant;
- no readable text, letters, numbers, logos, watermark, UI labels, contact
  sheets, masks, borders, or baked device chrome;
- reference-bound assets use accepted provenance and do not invent factual
  material;
- no image changes the activity mechanic, source play frame, or child action.

If QA fails, the image quality improver repairs only image-owned artifacts:
prompt specificity, regenerated illustrative PNGs, accepted reference source,
curated redraw, crop/resize, or built variants. It must not rewrite package
prose or source-intent evidence. Re-run the builder, asset output validator,
and image QA after repairs. Re-run dialogue QA when changed visuals affect
screen/dialogue claims.

## Validation

After any asset build, run:

```bash
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
```

For each package with demo extensions, also run:

```bash
python3 scripts/validate_demo_package_contract.py runs/<run_id>/activity_packages/<activity_id>
```

Then regenerate and validate the review dashboard:

```bash
python3 scripts/generate_run_review.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
```

If an input image or verified source is missing, leave the variant path null and
record the failure in `generated_assets/asset_outputs.yaml` or
`generated_assets/qa_notes.yaml`. Do not fabricate paths or mark unavailable
assets as displayed.

## Fullstack Demo Direct-Asset Workflow

When working directly in the fullstack demo repo rather than autodesign run
packages, follow the same style contract, generate one separate PNG per beat or
item, copy selected Codex imagegen outputs into:

```text
frontend/public/activity-assets/<activity_id>/
frontend/public/activity-assets/<activity_id>/items/
```

Then run the fullstack repo's asset screen builder:

```bash
python3 scripts/build_activity_screen_assets.py
```

Autodesign package runs should still use the package-local
`generated_assets/inbox/` plus `scripts/build_activity_assets.py` flow above.
