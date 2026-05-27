# Generate And Curate Asset Pipeline Implementation Plan

Date: 2026-05-28

Status: Planned

## Goal

Implement the real autodesign asset build pipeline for
`asset_build=generate_and_curate`.

The pipeline should work like the existing activity package generation workflow:
deterministic scripts prepare and validate work, while agents perform the
judgment-heavy pieces such as reference research, source verification, visual QA,
and bitmap generation. The output must be package-local runtime assets, not
review-only contact sheets.

## Current Context

The producer contract is already in place from
`docs/plans/2026-05-27-demo-package-contract-assets.md`.

Current behavior:

- full `GOAL.md` runs emit `demo_support.yaml` and `asset_manifest.yaml`;
- `asset_build` defaults to `manifest_only`;
- `asset_manifest.yaml` contains separate asset entries with nullable variant
  paths;
- `scripts/validate_demo_package_contract.py` validates demo support and asset
  manifest structure;
- older pilot asset tooling can make review contact-sheet bindings, but those
  are not final runtime assets.

Missing behavior:

- no implemented post-package asset phase actually creates runtime PNG files;
- package-local `assets/` directories are not populated;
- manifest variant `path` values remain null after package generation;
- reference-bound assets do not have an implemented source-verification and
  source-storage workflow;
- full `GOAL.md`, `run.md`, and `program.md` describe the mode but do not yet
  give agents an executable asset-build loop.

## Settled Decisions

- V1 implements `generate_and_curate`, not an illustrative-only or
  reference-only slice.
- The pipeline is agent-assisted, like activity package generation.
- The full `GOAL.md` run keeps `asset_build=manifest_only` as the default.
- When a run is invoked with `asset_build=generate_and_curate`, asset building
  runs after all selected packages validate.
- An asset-only rerun workflow must also exist for an existing
  `runs/<run_id>/activity_packages/` directory.
- The asset phase must actually generate bitmap images when the image generation
  tool is available.
- Final runtime assets are written back into each package:

```text
runs/<run_id>/activity_packages/<activity_id>/assets/
```

- Each package's `asset_manifest.yaml` is updated with relative variant `path`
  values pointing at package-local files.
- Run-level audit outputs are still written under:

```text
runs/<run_id>/generated_assets/
```

- Reference-bound assets store both final runtime assets and verified source
  material under package-local `assets/sources/` when the source license allows
  local storage. If a source cannot be stored or verified, it is not accepted for
  V1.
- Reference-bound candidate discovery may use agent-suggested leads and web
  search, but final accepted assets must come from approved originals, licensed
  or internal sources, official/verified URLs, or verified data/redraws.
- Do not use random generated approximations for constellations, artworks,
  maps, scientific diagrams, cultural artifacts, species, historical objects,
  named places, or famous structures.
- Contact sheets may remain review artifacts, but they must not be written as
  runtime variant paths.

## Visual Target For Illustrative Assets

Illustrative assets should use the `wonderlens_device_mint_soft_3d` style
already documented in `program.md` and the demo package contract.

The acceptable target resembles the inspected generated visual references under:

```text
/Users/pharrelly/.codex/generated_images/019e6796-207e-78b1-99ac-215bbe71abf1/
```

The round toy-scene references in that folder are appropriate as style
direction:

- soft 3D educational toy material;
- mint green, pale sage, warm porcelain, and gentle coral accents;
- clean centered subjects;
- gentle studio lighting;
- no text and no watermark;
- enough padding for a circular screen crop.

The UI mockup images in that folder are design references only. They should not
be emitted as runtime assets.

Runtime asset roles should stay distinct:

- `entity`, `activity_preview`, and `story_scene` may be scenic.
- `collection_correct`, `collection_distractor`, and `icon` should usually be
  one clear object per file, centered and inspectable at small size.
- `badge` should be simple and symbolic, with no rendered text unless the
  runtime separately supports text overlays.
- `ui_overlay` should be rare and must not bake interactive app UI into a
  static image unless the manifest explicitly requests it.

Round-device variants are the primary target. Keep all important detail inside
the central 70 to 75 percent circle. Horizontal debug variants are secondary
companions when requested by the manifest.

## Output Contract

Each package that builds assets should end with:

```text
runs/<run_id>/activity_packages/<activity_id>/
  asset_manifest.yaml
  assets/
    <asset_id>__<variant_id>.png
    sources/
      <asset_id>__source_original.<ext>
      <asset_id>__source_metadata.yaml
```

`asset_manifest.yaml` remains the source request and final package-local asset
contract. The asset phase should update only fields that reflect generated or
curated outputs:

- variant `path`;
- optional variant metadata such as byte count, mime type, sha256, generated
  timestamp, or source reference ID if the schema is extended;
- source/provenance entries when reference curation accepts a source;
- readiness/fallback notes only where the existing schema or plan extension
  supports them.

Do not rewrite `prod.md` to fit generated images. `prod.md` may reference asset
IDs and fallback behavior; `asset_manifest.yaml` owns file paths and visual
source details.

Run-level audit output should include:

```text
runs/<run_id>/generated_assets/
  asset_outputs.yaml
  reference_sources.yaml
  qa_notes.yaml
  work_items/
    <activity_id>__<asset_id>.md
```

Recommended audit fields:

- `run_id`;
- `asset_build_mode`;
- `activity_id`;
- `asset_id`;
- `role`;
- `accuracy_mode`;
- `requiredness`;
- `source_strategy`;
- `transformation_policy`;
- output status: `generated`, `curated`, `blocked`, `missing_source`,
  `qa_failed`, or `skipped_fallback`;
- package-local output paths;
- source metadata path for reference-bound assets;
- prompt hash or source hash;
- QA notes and reviewer/agent status.

No generated artifact should require absolute local paths to be useful. Absolute
paths may appear only in transient local notes that are not package contracts.

## Agent-Assisted Workflow

The implementation should add a repeatable workflow with two entry points.

### Integrated `GOAL.md` Path

When a full run is invoked with `asset_build=generate_and_curate`:

1. Generate and validate all requested packages first.
2. Validate `demo_support.yaml` and `asset_manifest.yaml`.
3. Prepare asset work items from each package manifest.
4. Dispatch or instruct delegated agents for independent asset groups.
5. Build illustrative assets with image generation.
6. Curate reference-bound assets through verified source research and accepted
   transformations.
7. Write package-local runtime assets and source files.
8. Update package `asset_manifest.yaml` paths.
9. Run contract and output validation.
10. Regenerate `review.html` so reviewers can inspect asset status and paths.

### Asset-Only Rerun Path

Provide a separate command/workflow that takes an existing run directory:

```bash
python3 scripts/<asset_build_entrypoint>.py runs/<run_id> --mode generate_and_curate
```

The implementation may choose the final script name. The behavior must support:

- idempotent reruns;
- rebuilding only missing or failed assets where practical;
- preserving accepted source metadata;
- refusing to overwrite reviewed outputs unless a force flag is explicit;
- revalidating package manifests after updates.

## Illustrative Generation Rules

For `accuracy_mode: illustrative` assets:

- Use the manifest `prompt_en` as the source requirement.
- Add the shared `wonderlens_device_mint_soft_3d` style prompt and screen-target
  constraints.
- Generate the master asset at a large square size when possible, then derive
  declared variants.
- Do not generate text, watermarks, brand marks, copyrighted characters,
  photoreal child faces, unsafe props, or dense UI.
- Prefer separate subject assets over multi-object scenes unless the role is
  `story_scene` or `activity_preview`.
- Generate only declared assets. Do not invent extra collection items to make a
  package look fuller.
- Record the exact prompt used and enough metadata for a reviewer to reproduce
  the intent.

If image generation fails, keep variant paths null and record a clear failure in
`asset_outputs.yaml` and `qa_notes.yaml`. Do not fabricate placeholder paths.

## Reference-Bound Curation Rules

For `accuracy_mode: reference_bound` assets:

1. Read the manifest's `reference_policy`, `sources`, `source_strategy`, and
   `transformation_policy`.
2. If approved sources are already present and verifiable, use them.
3. If sources are missing and the asset build mode allows curation, an agent may
   propose candidate leads and search for official, public-domain, licensed,
   approved internal, educational, scientific, or otherwise verified sources.
4. Accept only sources that satisfy the manifest policy and can be documented in
   `reference_sources.yaml`.
5. Store the accepted source original and source metadata under
   `assets/sources/` when the license allows local storage.
6. Produce the runtime variant using the declared transformation policy:
   `crop_resize_only`, `simplified_redraw`, `style_preserving_redraw`, or
   `no_derivative_generation`.
7. QA the final asset against the source-specific correctness requirement.

Examples:

- A constellation must preserve the real star layout and relative pattern.
- A named public-domain artwork should generally use the original or a
  crop/resize, not a toy-style reinterpretation.
- A scientific diagram should redraw from verified data only when the result
  remains faithful.
- A species or cultural artifact must not be replaced with a generic cute
  object.

If verification fails, the asset remains unbuilt. Required reference-bound asset
failure should degrade or block demo readiness according to existing
`demo_support.yaml` rules rather than pretending the asset is available.

## Script And File Ownership Expectations

Likely implementation areas:

- `GOAL.md`: update the completion contract for `generate_and_curate`.
- `run.md`: add the concrete asset-build loop and asset-only rerun behavior.
- `program.md`: clarify generation prompts, curation acceptance, and package
  write-back rules.
- `README.md`: document how to run full and asset-only workflows.
- `activities/_schema/asset_manifest.schema.json`: extend only if required for
  output metadata while preserving existing valid manifests.
- `scripts/validate_demo_package_contract.py`: extend validation only when the
  schema or readiness rules require it.
- new asset build scripts under `scripts/`;
- new fixtures under `tests/fixtures/`;
- new tests under `tests/`.

Keep previous pilot scripts working unless a replacement is explicitly
documented. Review-only contact-sheet tooling should not be silently redefined
as runtime asset tooling.

## Validation And QA

Automated tests should cover:

- manifest parsing and work-item generation;
- illustrative asset path update behavior without requiring live image
  generation;
- reference-bound source acceptance and rejection;
- path safety: no absolute paths, no `..`, no writes outside the package;
- idempotent asset-only reruns;
- required asset failures leave null paths and produce clear audit status;
- successful package-local outputs validate with
  `scripts/validate_demo_package_contract.py`;
- review dashboard shows asset build mode, generated paths, reference sources,
  and failures.

Manual or goal-run smoke should cover actual bitmap generation:

- one illustrative asset;
- one reference-bound asset with an accepted source;
- one reference-bound asset that fails verification and remains honestly
  degraded or blocked.

For actual images, verify:

- PNG files exist and are non-empty;
- dimensions match declared variants;
- round variants are safe for circular crop;
- source originals and metadata exist for reference-bound accepted sources;
- package `asset_manifest.yaml` uses package-relative paths;
- fullstack-demo and WonderLens AI import paths can consume the package after
  their respective consumer goals land.

## Required Checks For Implementation

The implementation goal should run, or adapt with equivalent coverage:

```bash
python3 -m pytest tests/test_demo_package_contract_validator.py tests/test_integrated_asset_workflow.py tests/test_generate_run_review.py tests/test_generate_and_curate_asset_pipeline.py -q
python3 scripts/validate_demo_package_contract.py tests/fixtures/demo_package_contract/valid
python3 scripts/validate_asset_build_outputs.py tests/fixtures/asset_build_runs/valid_generate_and_curate
python3 scripts/generate_run_review.py tests/fixtures/asset_build_runs/valid_generate_and_curate
git diff --check
```

If the implementation chooses different script or fixture names, use equivalent
commands and document the substitutions in the final report.

## Non-Goals

- Do not make `generate_and_curate` the default asset mode.
- Do not generate assets during `manifest_only`.
- Do not create runtime contact sheets as a substitute for separate runtime
  assets.
- Do not add raw image prompts to `prod.md`.
- Do not implement full consumer import in fullstack-demo or WonderLens AI from
  this repo.
- Do not use random generated approximations for reference-bound assets.
- Do not accept unverified web-image thumbnails as sources.
- Do not add provider credentials, `.env` files, or machine-local secrets.

## Risks And Assumptions

- The actual image-generation tool is available to Codex goal execution. If it
  is unavailable, the implementation should still prepare work items and fail
  the final completion gate rather than claiming bitmap generation is complete.
- Some reference sources may be legal to cite but not store locally. V1 should
  reject those as accepted package-local sources unless the source terms allow
  storage.
- Image QA remains partly judgment-based. The pipeline should record agent QA
  notes and make failures visible instead of over-automating weak checks.
- Variant derivation may need a local image-processing dependency or system
  tool. Prefer the smallest deterministic approach that can validate dimensions
  and preserve crop safety.

## Completion Criteria

This plan is complete when:

- `asset_build=generate_and_curate` is executable in full `GOAL.md` runs;
- an asset-only rerun workflow exists for existing run directories;
- illustrative assets can be generated as package-local bitmap files;
- reference-bound assets can be curated from verified sources and store source
  originals plus source metadata in package-local `assets/sources/`;
- package `asset_manifest.yaml` files are updated with relative variant paths;
- failures leave paths null and produce honest audit/degraded/blocking status;
- run-level `generated_assets/` audit files are written;
- `review.html` exposes built asset status and failures;
- tests and validation cover success and failure paths;
- plan and goal indexes are updated after execution.
