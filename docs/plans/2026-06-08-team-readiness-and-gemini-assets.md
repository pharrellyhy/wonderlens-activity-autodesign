# Team Readiness And Gemini Asset Provider Plan

Date: 2026-06-08

Status: Completed

## Goal

Prepare `wonderlens-activity-autodesign` for a small multi-person full-pass dry
run before sharing the repo with collaborators. The readiness work must make the
parallel workflow self-onboarding, add machine-readable review status templates,
and provide a non-Codex image generation path so asset curators who cannot use
Codex built-in `imagegen` can still generate package-local source PNGs.

The first supported third-party image provider should be Gemini, using the
credential and model pattern already proven in:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend
```

## Current Evidence

Autodesign already has the core full-pass and asset pipeline pieces:

- `docs/full_pass_agentic_parallel_workflow.html` explains the human parallel
  workflow, role split, branch model, file ownership, status model, and PM
  review criteria.
- `docs/activity_asset_generation_workflow.md` defines the current asset style,
  source-of-truth order, illustrative workflow, reference-bound workflow, and
  expected package-local asset paths.
- `scripts/build_activity_assets.py` is the deterministic builder. It consumes
  PNGs from `runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png`
  and writes package-local runtime variants under `assets/` or `assets/items/`.
- `scripts/validate_asset_build_outputs.py`,
  `scripts/validate_asset_granularity.py`, and
  `scripts/validate_full_pass_asset_bundle.py` already validate built asset
  outputs.
- `scripts/validate_demo_package_contract.py` validates `demo_support.yaml` and
  `asset_manifest.yaml` contracts.
- The repo has no root `package.json`, `pyproject.toml`, `Makefile`, or
  dependency manifest, so any provider setup must make Python dependency
  requirements explicit.

The fullstack-demo backend reference has the target Gemini pattern:

- `backend/config.yaml` sets `imagen_model: "gemini-2.5-flash-image"`.
- `backend/config.py` loads secrets from `.env` and app config from
  `config.yaml`.
- `backend/image_gen.py` uses the Google GenAI SDK and picks auth mode from
  config: Vertex AI when `GOOGLE_CLOUD_PROJECT` is present, otherwise API key
  via `GEMINI_API_KEY`.
- `backend/image_gen.py` calls `client.models.generate_content` with an image
  model and `types.GenerateContentConfig(response_modalities=["IMAGE"],
  image_config=types.ImageConfig(aspect_ratio=...))`.
- The backend directory contains local secret files `.env` and
  `.elaborate-baton-480304-r8-a8a39bcb34f1.json`. These are setup references
  only and must not be read, printed, copied into autodesign, or committed.

Current Gemini docs support image generation through the Google GenAI SDK using
image models such as `gemini-2.5-flash-image` and newer variants. This plan
keeps the model configurable while defaulting the local workflow to the
fullstack-demo model.

## Problem Statement

The current full-pass asset workflow is not shareable as-is because it assumes
Codex built-in `imagegen` for illustrative asset generation. Only the repo owner
currently has access to that tool. Other collaborators can review prompts,
source metadata, manifests, and visual quality, but they cannot produce the PNGs
needed by the deterministic builder unless the repo supports a third-party
provider path.

Without a readiness pass, new contributors may also edit the wrong files,
create branch conflicts, invent incompatible status fields, commit secrets by
mistake, or produce assets outside the expected inbox/package layout.

## Settled Decisions

- Do a readiness pass before asking collaborators to run or review a full
  production pass.
- Keep the existing parallel workflow HTML as the role/workflow overview.
- Add a text onboarding document for quick repo setup and role-specific
  contributor steps.
- Add one machine-readable per-activity review-status template instead of a
  single shared global tracker.
- Add Gemini as the first non-Codex illustrative image provider.
- Use `gemini-2.5-flash-image` as the default model because the referenced
  fullstack backend already uses it.
- Keep model and provider configurable so future providers or newer Gemini image
  models can be added without changing package manifests.
- Do not copy or store fullstack-demo credentials in this repo. Read them only
  from explicit user-provided paths or already exported environment variables.
- The provider script writes source PNGs only to the builder inbox. The existing
  deterministic builder remains responsible for package-local runtime variants.
- Reference-bound assets remain source-governed. Gemini may create a curated
  redraw only after accepted source originals and metadata exist; it must not
  invent random replacements for constellations, artworks, maps, diagrams, or
  other factual/reference-bound assets.

## Proposed Files

Likely implementation files:

```text
docs/team_onboarding.md
docs/image_generation_provider_setup.md
runs/_templates/review_status.yaml
requirements-imagegen.txt
scripts/generate_activity_asset_sources.py
tests/test_generate_activity_asset_sources.py
```

Likely updates:

```text
README.md
docs/full_pass_agentic_parallel_workflow.html
docs/activity_asset_generation_workflow.md
.gitignore
```

`.gitignore` should ensure local env files and service-account JSONs cannot be
accidentally committed. If a matching ignore rule is already present when this
goal executes, preserve it and avoid churn.

## Gemini Provider Contract

Add a provider script that reads run-local package manifests and writes source
images for illustrative assets into the existing builder inbox:

```text
runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png
```

Recommended CLI shape:

```bash
python3 scripts/generate_activity_asset_sources.py \
  --provider gemini \
  --model gemini-2.5-flash-image \
  --run runs/<run_id> \
  --activity <activity_id>
```

Credential setup should support either already exported environment variables or
explicit fullstack-backend references:

```bash
FULLSTACK_BACKEND_ROOT="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend"
set -a
source "$FULLSTACK_BACKEND_ROOT/.env"
set +a
export GOOGLE_APPLICATION_CREDENTIALS="$FULLSTACK_BACKEND_ROOT/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
```

The script should also support explicit paths:

```bash
python3 scripts/generate_activity_asset_sources.py \
  --provider gemini \
  --model gemini-2.5-flash-image \
  --env-file "$FULLSTACK_BACKEND_ROOT/.env" \
  --google-credentials "$FULLSTACK_BACKEND_ROOT/.elaborate-baton-480304-r8-a8a39bcb34f1.json" \
  --run runs/<run_id> \
  --activity <activity_id>
```

The script must never print secret values. It may print sanitized facts such as
which auth mode is active, which model is used, which assets were generated, and
where output files were written.

## Provider Behavior

For each selected `asset_manifest.yaml` illustrative asset:

- read `asset.id`, `role`, `label`, `accuracy_mode`, `source_strategy`,
  `prompt_en`, `variants`, and screen target information;
- skip non-illustrative assets unless an explicit curated-reference mode is
  implemented and the required source metadata is accepted;
- combine the asset prompt with `docs/activity_asset_generation_workflow.md`
  style requirements;
- request a square image suitable for 512x512 source use;
- save one PNG per asset in the builder inbox;
- inspect image dimensions and downsample to 512x512 if the provider returns a
  larger square output;
- record a sanitized provider audit file under `runs/<run_id>/generated_assets/`;
- optionally write or update the run-local prompt trace used by image QA.

The provider script should not edit `prod.md`, `spec.md`, `demo_support.yaml`,
`asset_manifest.yaml`, or package-local runtime variants. Those changes belong
to package review and deterministic build phases.

## Team Onboarding Contract

Add concise contributor-facing setup docs that explain:

- which page to read first:
  `docs/full_pass_agentic_parallel_workflow.html`;
- how to create a role branch from a run integration branch;
- how each role scopes file edits;
- how to update `runs/<run_id>/review_status/<activity_id>.yaml`;
- how to run focused validators;
- how to install image-generation dependencies;
- how to configure Gemini without copying credentials;
- how to run one provider smoke;
- how to open a PR or handoff note back to the run captain.

The onboarding doc should distinguish:

- collaborators who only review text/package quality;
- collaborators who curate sources and review images;
- collaborators who can run Gemini provider generation;
- the integration owner who runs WonderLens AI and fullstack-demo checks.

## Review Status Template

Add a template that can be copied to one file per activity:

```text
runs/<run_id>/review_status/<activity_id>.yaml
```

The template should include at least:

- `activity_id`;
- `owners`;
- `text_review`;
- `asset_review`;
- `contract_validation`;
- `runtime_validation`;
- `pm_review`;
- `final_verdict`;
- `blocked_reason`;
- `last_updated`.

Use stable status values such as `pending`, `pass`, `needs_fix`, `blocked`, and
`not_applicable`. Keep the first version hand-editable; a live dashboard can
consume the same shape later.

## Validation And Smoke Requirements

Static checks should cover:

- provider config parsing without reading real secrets;
- missing env file or missing credential path fails with a setup message;
- selected activity/asset filtering;
- generated output paths are under `generated_assets/inbox`;
- provider audit output excludes secret values;
- non-illustrative/reference-bound assets are skipped or gated unless the source
  workflow is satisfied;
- docs and templates contain no real secret strings.

Live smoke should be small and explicit. On a machine with the referenced
fullstack backend credentials, generate one non-production illustrative PNG into
a temporary run fixture or a deliberately scoped smoke run, then run the
deterministic builder and asset-output validator against that run. Do not use
Codex built-in `imagegen` as the live readiness proof.

## Non-Goals

- Do not run the full 40-activity production pass in this readiness goal.
- Do not modify WonderLens AI or fullstack-demo code.
- Do not implement a live dashboard yet.
- Do not require every collaborator to have downstream app access.
- Do not copy fullstack-demo `.env` or service-account JSON files into this
  repo.
- Do not commit generated production assets from smoke tests unless the smoke
  fixture is explicitly designed to be committed.
- Do not use Gemini to fabricate reference-bound factual assets without accepted
  source provenance.

## Risks And Mitigations

| Risk | Mitigation |
|---|---|
| Credentials leak through logs or commits | Sanitize logs, never print env values, add ignore rules, validate no secret filenames are staged. |
| Provider output style drifts from WonderLens assets | Reuse the existing asset style contract and require visual QA before build acceptance. |
| Gemini output dimensions differ from expected 512x512 | Normalize provider output before placing it in the builder inbox. |
| Teammates cannot install dependencies consistently | Add an explicit imagegen requirements file and setup doc. |
| Reference-bound assets become random generated approximations | Gate reference-bound assets until accepted source originals and metadata exist. |
| Status tracking creates merge conflicts | Use one review-status YAML per activity, not one shared global file. |

## Completion Definition

The readiness implementation is complete when a fresh collaborator can read the
onboarding docs, create a role branch, update a per-activity status file, install
image-generation dependencies, configure Gemini from the fullstack backend
credential pattern or equivalent environment variables, generate one illustrative
source PNG into the builder inbox, run the deterministic builder, and see
sanitized validation evidence without needing Codex built-in `imagegen`.
