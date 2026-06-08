# Gemini Asset Quality Candidates Goal

## Mode

Plan-backed

## Objective

Implement a production-quality candidate workflow for Gemini-generated
illustrative activity assets. The workflow must generate multiple reviewable
candidates per selected asset, use the repo-local flat Nordic style reference
image in Gemini calls, support explicit candidate acceptance into the existing
builder inbox, and preserve sanitized evidence for image QA.

## Design Source

Authoritative implementation context:

```text
docs/plans/2026-06-08-gemini-asset-quality-candidates.md
```

The plan is authoritative for design rationale, artifact contracts, prompt
requirements, and risks. This goal is authoritative for hard constraints,
required checks, credential handling, and the final completion gate. If they
conflict, stop and document the conflict before changing behavior.

## Hard Constraints

- Do not read, print, copy, edit, or commit `.env`, service-account JSON files,
  API keys, tokens, provider secrets, or production credentials.
- Do not commit exploratory live-generated images from `tmp/` or other
  non-production smoke locations.
- Do not modify WonderLens AI or fullstack-demo code.
- Do not rewrite package mechanics, `prod.md`, or `spec.md` to make image
  generation easier.
- Do not make `scripts/build_activity_assets.py` responsible for provider calls
  or visual quality judgment.
- Do not fabricate reference-bound factual assets with random generated images.
- Keep accepted illustrative sources compatible with the existing builder inbox:
  `runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png`.
- Preserve unrelated local user changes and stage only intended files.

## Required Scope

- Extend the Gemini source generator with a multi-candidate review mode.
- Add explicit candidate acceptance into the existing builder inbox.
- Include the repo-local flat Nordic style reference image in Gemini requests
  when generating candidates.
- Record sanitized candidate metadata, provider audit evidence, acceptance
  evidence, hashes, and paths.
- Add focused tests for candidate path safety, review-only generation,
  acceptance, idempotency, skipped/gated asset types, and secret-safe audits.
- Update collaborator docs so teammates understand candidate generation,
  curation, acceptance, and builder handoff.
- Run a live Gemini smoke with at least two candidates for one non-production
  real illustrative activity asset.

## Execution Rules

- Work from the autodesign repo root:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-autodesign
```

- Use a feature worktree under `.worktrees/` for implementation.
- Inspect current `scripts/generate_activity_asset_sources.py`,
  `scripts/build_activity_assets.py`, asset workflow docs, and tests before
  editing.
- Keep generated candidates run-local under `generated_assets/candidates/`.
- Only explicit acceptance may copy a candidate into `generated_assets/inbox/`.
- Fail with setup guidance when style references or credentials are missing.
- Keep all provider and candidate audit logs sanitized.
- Do not push unless explicitly asked after the goal run.

## Live Provider Credential Rule

Use the same local Gemini credential reference as the merged readiness workflow.
For local smoke execution, use this pattern without printing values:

```bash
FULLSTACK_BACKEND_ROOT="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend"
test -f "$FULLSTACK_BACKEND_ROOT/.env"
test -f "$FULLSTACK_BACKEND_ROOT/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
set -a
source "$FULLSTACK_BACKEND_ROOT/.env"
set +a
export GOOGLE_APPLICATION_CREDENTIALS="$FULLSTACK_BACKEND_ROOT/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
```

If those files are absent or the provider rejects the credentials, do not mark
the goal complete. Record a blocked result with the sanitized error class and
next setup step. Never include secret values or request payloads in logs,
commits, screenshots, or final reports.

## Preconditions

```bash
git status --short --branch
test -f scripts/generate_activity_asset_sources.py
test -f scripts/build_activity_assets.py
test -f scripts/validate_asset_build_outputs.py
test -f docs/asset_style_reference/style-reference-flat-nordic.png
test -f docs/asset_style_reference/wonderlens-activity-style.md
test -f docs/image_generation_provider_setup.md
test -d /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend
```

## Success Criteria

- The CLI can generate multiple Gemini candidates for one illustrative asset
  without writing to the builder inbox in review-only mode.
- Candidate metadata records provider, model, prompt source, dimensions, hashes,
  sanitized paths, and candidate statuses.
- The CLI can accept one safe run-local candidate into the existing builder
  inbox and record acceptance evidence.
- Candidate and acceptance paths reject traversal, absolute paths, unsafe IDs,
  and paths outside the run directory.
- Gemini candidate generation uses the text style contract and flat Nordic
  reference image.
- Existing builder and validator behavior remains compatible.
- Docs explain candidate generation, review, acceptance, and builder handoff.
- A live smoke generates at least two candidates, accepts one, builds it, and
  validates it without leaking credentials.

## Required Checks

Minimum static checks:

```bash
git diff --check
python3 -m unittest tests.test_generate_activity_asset_sources
python3 -m unittest tests.test_generate_and_curate_asset_pipeline
python3 scripts/generate_activity_asset_sources.py --help
```

Minimum live smoke, after sourcing credentials with the rule above:

```bash
python3 scripts/generate_activity_asset_sources.py \
  --provider gemini \
  --model gemini-2.5-flash-image \
  --run <non-production-smoke-run> \
  --activity <smoke-activity-id> \
  --asset <smoke-asset-id> \
  --candidates 2 \
  --review-only

python3 scripts/generate_activity_asset_sources.py \
  --run <non-production-smoke-run> \
  --activity <smoke-activity-id> \
  --asset <smoke-asset-id> \
  --accept-candidate <accepted-candidate-id-or-path>

python3 scripts/build_activity_assets.py <non-production-smoke-run> --mode generate_illustrative
python3 scripts/validate_asset_build_outputs.py <non-production-smoke-run>
```

If implementation chooses different CLI flag names, update docs and final
report with the exact commands that were run.

## Final Completion Gate

The goal is complete only when candidate generation, candidate acceptance,
style-reference prompting, docs, tests, static checks, and live Gemini smoke all
pass; no secrets or exploratory generated assets are staged; and the plan/goal
indexes reflect the completed state. If live Gemini cannot be run with the
referenced credentials, mark the goal blocked instead of claiming readiness.

## Goal Invocation

```text
/goal Implement goals/2026-06-08-gemini-asset-quality-candidates-goal.md. Stop only when its completion gate is satisfied or a blocker is documented.
```
