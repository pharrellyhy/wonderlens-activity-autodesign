# Generate And Curate Asset Pipeline Goal

## Mode

Plan-backed.

Use this file as the Codex goal-mode execution contract.

## Objective

Implement the real autodesign asset build pipeline for
`asset_build=generate_and_curate`: an agent-assisted post-package phase that
actually generates illustrative bitmap assets, curates reference-bound assets
from verified sources, writes final runtime files back into package-local
`assets/`, updates package `asset_manifest.yaml` variant paths, and records
run-level audit output.

## Design Source

Source plan:

- `docs/plans/2026-05-28-generate-and-curate-asset-pipeline.md`

Related context:

- `docs/plans/2026-05-27-demo-package-contract-assets.md`
- `GOAL.md`
- `run.md`
- `program.md`
- `README.md`

The plan is authoritative for design rationale, current evidence,
implementation areas, and risk context. This goal is authoritative for hard
constraints, required checks, credential handling, delegated-agent rules, and
completion. If the plan and goal conflict, stop and document the conflict before
changing behavior.

## Hard Constraints

- Implement `generate_and_curate` v1, not an illustrative-only or
  reference-only slice.
- Keep `asset_build=manifest_only` as the default.
- Run asset building only after package validation.
- Provide both full-run integration and an asset-only rerun workflow.
- Actually generate bitmap images with the Codex built-in imagegen tool when it
  is available. Do not accept SVG/vector drawings, placeholder art, or
  non-imagegen scripts as generated illustrative source art.
- Use the repo-local flat Nordic style prompt and reference image in
  `docs/asset_style_reference/` for generated illustrative assets.
- Write final runtime assets back into each package under
  `activity_packages/<activity_id>/assets/`.
- Write picker/selectable item/object runtime variants under package-local
  `activity_packages/<activity_id>/assets/items/`, separate from scene and
  background assets.
- Update package `asset_manifest.yaml` with package-relative variant paths.
- Store accepted reference-bound source originals and source metadata under
  package-local `assets/sources/` when source terms allow local storage.
- Do not create runtime contact sheets as a substitute for separate assets.
- Do not rewrite `prod.md` to fit generated images.
- Do not use random generated approximations for reference-bound assets.
- Do not accept unverified web-image thumbnails as sources.
- Do not implement consumer import in fullstack-demo or WonderLens AI here.
- Do not edit, print, copy, or commit `.env`, provider credentials, tokens, or
  machine-local secrets.
- Do not perform unrelated refactors, dependency upgrades, or broad formatting
  sweeps.

## Required Scope

Implement the asset pipeline across these areas:

- update `GOAL.md`, `run.md`, `program.md`, and `README.md` for the executable
  `generate_and_curate` workflow;
- add deterministic asset work-item preparation and output validation;
- add an asset-only rerun command/workflow for existing run directories;
- add package-local asset write-back and manifest path updates;
- add reference-bound source curation, source metadata, and source-original
  storage rules;
- add run-level audit files under `runs/<run_id>/generated_assets/`;
- update review dashboard output to show asset build status, generated paths,
  reference sources, and failures;
- add fixtures and tests for success, failure, path safety, idempotency, and
  reference-bound rejection.

## Delegated Agent Rule

The user explicitly requested delegated-agent rules for this goal.

Use sub-agents only for independent exploration, implementation, verification,
asset generation, reference-source research, visual QA, or code review with
disjoint ownership. Keep tightly coupled workflow contract edits, manifest
schema decisions, final integration, final validation, committing, and final
reporting local to the main agent.
Use at most three sub-agents in parallel; collect evidence and terminate or
kill each finished agent before spawning another.

Good delegation candidates:

- inspect current pilot asset scripts and propose the smallest reusable
  implementation path;
- build fixture matrices for illustrative, reference-bound, failed-source, and
  path-safety cases;
- research and verify reference-bound sources for smoke assets;
- generate illustrative bitmap assets from prepared work items using Codex
  built-in imagegen;
- visual QA for round-screen crop safety and reference fidelity;
- independent code review after implementation.

## Execution Rules

- Use a feature worktree/branch, for example
  `.worktrees/feat/generate-and-curate-asset-pipeline`.
- Start by confirming the current demo package contract validator and existing
  asset workflow tests pass.
- Prefer focused tests before or alongside implementation changes.
- Use existing repo patterns and scripts where practical.
- Keep generated bitmap smoke artifacts small and tied to fixtures or a tiny
  run; do not regenerate all 40 activities as part of this goal unless the user
  explicitly asks.
- If Codex built-in imagegen is unavailable, document the blocker and do not
  mark the goal complete.
- Update plan and goal indexes only after the goal is completed or genuinely
  blocked.
- Follow repo commit rules. Do not push unless explicitly asked.

## Mandatory Ordering

1. Confirm baseline validator and existing tests.
2. Implement deterministic work-item, validation, and manifest-update behavior.
3. Add integrated `GOAL.md`/`run.md`/`program.md` instructions.
4. Add asset-only rerun workflow.
5. Add review dashboard visibility.
6. Run automated checks.
7. Run a small real bitmap smoke with at least one illustrative asset and one
   reference-bound path.
8. Update indexes and commit only after checks and smoke are complete, or mark
   blocked with evidence.

## Live Provider Credential Rule

No repo secrets are required for this goal. Do not source `.env` or inspect
credential files.

The Codex built-in imagegen tool is the required generator for illustrative
bitmap generation. Web search may be used for reference-source discovery and
verification. Do not record secret values, private tokens, or machine-local
credential paths in package manifests or committed audit files.

## Preconditions

- Confirm the working tree is clean except intentional goal work.
- Confirm these files or their current equivalents exist:
  - `GOAL.md`
  - `run.md`
  - `program.md`
  - `README.md`
  - `activities/_schema/asset_manifest.schema.json`
  - `scripts/validate_demo_package_contract.py`
  - `scripts/generate_run_review.py`
  - `tests/test_demo_package_contract_validator.py`
  - `tests/test_integrated_asset_workflow.py`
- Run the baseline:

```bash
python3 -m pytest tests/test_demo_package_contract_validator.py tests/test_integrated_asset_workflow.py tests/test_generate_run_review.py -q
python3 scripts/validate_demo_package_contract.py tests/fixtures/demo_package_contract/valid
git diff --check
```

Stop on baseline failure and fix only what is required to restore the baseline.

## Success Criteria

- `asset_build=generate_and_curate` is documented and executable as a full
  `GOAL.md` post-package phase.
- An asset-only rerun workflow can fill assets for an existing run directory.
- Illustrative assets are generated as separate PNG runtime assets in the
  WonderLens flat Nordic activity style using `docs/asset_style_reference/`.
- Picker/selectable item and object assets are built under package-local
  `assets/items/`, not mixed with scene/background assets.
- Reference-bound assets require verified sources and accepted provenance before
  producing or accepting runtime variants.
- Accepted reference-bound assets store final runtime files plus source
  originals and source metadata in package-local directories.
- Package `asset_manifest.yaml` files use package-relative paths for built
  variants and leave failed variants null.
- Run-level `generated_assets/asset_outputs.yaml`,
  `reference_sources.yaml`, and `qa_notes.yaml` are produced.
- Required asset failures are visible and do not fake playable readiness.
- `review.html` shows asset build mode, built outputs, reference sources, and
  failures.
- Existing manifest-only behavior remains unchanged.

## Required Checks

Minimum final automated checks:

```bash
python3 -m pytest tests/test_demo_package_contract_validator.py tests/test_integrated_asset_workflow.py tests/test_generate_run_review.py tests/test_generate_and_curate_asset_pipeline.py -q
python3 scripts/validate_demo_package_contract.py tests/fixtures/demo_package_contract/valid
python3 scripts/validate_asset_build_outputs.py tests/fixtures/asset_build_runs/valid_generate_and_curate
python3 scripts/generate_run_review.py tests/fixtures/asset_build_runs/valid_generate_and_curate
git diff --check
```

The executor may substitute equivalent focused tests if file or script names
change, but coverage for validator compatibility, work-item generation, manifest
updates, source curation, path safety, review output, and diff hygiene is
required.

After automated checks pass, run a small real bitmap smoke:

- generate one illustrative PNG from a valid manifest work item;
- curate or verify one reference-bound source and produce or accept one runtime
  variant;
- verify package-local paths, source storage, dimensions, and contract
  validation;
- include smoke artifact paths and any image-generation limitations in the
  final report.

## Final Completion Gate

Do not mark achieved until:

- required scope is implemented or a real blocker is documented with evidence;
- success criteria are met;
- required automated checks pass;
- the small real bitmap smoke passes, or image generation/source access is
  documented as a real blocker;
- no secrets or unsafe absolute local paths are included in package contracts or
  committed audit files;
- `docs/plans/README.md` and `goals/README.md` mark this plan/goal `Completed`
  or `Blocked` as appropriate;
- intended changes are committed with conventional commit messages.

Final response must include files changed, checks run, bitmap smoke result or
blocker, remaining risks, and commit hashes.

## Goal Invocation

Use from the `wonderlens-activity-autodesign` repo or its implementation
worktree:

```text
/goal Implement goals/2026-05-28-generate-and-curate-asset-pipeline-goal.md. The user explicitly requests delegated-agent work for independent exploration, implementation, verification, asset generation, reference-source research, visual QA, and code review where ownership is disjoint. Stop only when its completion gate is satisfied or a blocker is documented.
```
