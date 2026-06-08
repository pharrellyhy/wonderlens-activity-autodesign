# Image Generation Provider Setup

This repo supports Gemini as the first third-party provider for illustrative
runtime source PNGs. Use it when a collaborator cannot use Codex built-in
`imagegen`.

The provider reads `asset_manifest.yaml` files and writes source PNGs to:

```text
runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png
```

It does not edit package text, mechanics, `demo_support.yaml`,
`asset_manifest.yaml`, or package-local runtime variants. After provider
generation, run `scripts/build_activity_assets.py` to create package-local
runtime files.

## Dependencies

Install the image-generation dependencies in your active Python environment:

```bash
python3 -m pip install -r requirements-imagegen.txt
```

The file is intentionally separate because this repository has no root project
dependency manifest.

## Credentials

Use either Vertex AI credentials or a Gemini API key. Do not copy credentials
into this repository.

The local fullstack-demo backend is the reference setup:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend
```

Use it like this without printing any values:

```bash
FULLSTACK_BACKEND_ROOT="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend"
test -f "$FULLSTACK_BACKEND_ROOT/.env"
test -f "$FULLSTACK_BACKEND_ROOT/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
set -a
source "$FULLSTACK_BACKEND_ROOT/.env"
set +a
export GOOGLE_APPLICATION_CREDENTIALS="$FULLSTACK_BACKEND_ROOT/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
```

The provider uses Vertex AI when `GOOGLE_CLOUD_PROJECT` is set. If that is not
set, it uses `GEMINI_API_KEY`.

You can also pass explicit setup paths:

```bash
python3 scripts/generate_activity_asset_sources.py \
  --provider gemini \
  --model gemini-2.5-flash-image \
  --env-file "$FULLSTACK_BACKEND_ROOT/.env" \
  --google-credentials "$FULLSTACK_BACKEND_ROOT/.elaborate-baton-480304-r8-a8a39bcb34f1.json" \
  --run runs/<run_id> \
  --activity <activity_id> \
  --limit 1
```

The script records sanitized provider audit evidence under
`runs/<run_id>/generated_assets/provider_runs/`. Audit files may include auth
mode names such as `vertex` or `api_key`, model names, output paths, hashes,
and sanitized error classes. They must not include API keys, tokens, service
account JSON content, or request payloads containing secrets.

## Generate Illustrative Sources

For one activity:

```bash
python3 scripts/generate_activity_asset_sources.py \
  --provider gemini \
  --model gemini-2.5-flash-image \
  --run runs/<run_id> \
  --activity <activity_id>
```

For one asset:

```bash
python3 scripts/generate_activity_asset_sources.py \
  --provider gemini \
  --run runs/<run_id> \
  --activity <activity_id> \
  --asset <asset_id>
```

The provider selects only `accuracy_mode: illustrative` assets with
`source_strategy: generated_illustrative`. Reference-bound assets stay gated by
the source curation workflow in `docs/activity_asset_generation_workflow.md`.

## Build And Validate

After source PNGs exist in the inbox:

```bash
python3 scripts/build_activity_assets.py runs/<run_id> --mode generate_illustrative
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
```

Use `--mode generate_and_curate` when the same run also contains accepted
reference-bound source originals and metadata.

## Small Smoke

For a non-production smoke run, generate one illustrative source, build package
variants, and validate:

```bash
python3 scripts/generate_activity_asset_sources.py \
  --provider gemini \
  --model gemini-2.5-flash-image \
  --run <non-production-smoke-run> \
  --activity <smoke-activity-id> \
  --limit 1

python3 scripts/build_activity_assets.py <non-production-smoke-run> --mode generate_illustrative
python3 scripts/validate_asset_build_outputs.py <non-production-smoke-run>
```

If Gemini returns a quota or `RESOURCE_EXHAUSTED` error, record the sanitized
error class in the activity status and retry later with a smaller limit.
