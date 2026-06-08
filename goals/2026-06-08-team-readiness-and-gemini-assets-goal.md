# Team Readiness And Gemini Assets Goal

## Mode

Plan-backed

## Objective

Make `wonderlens-activity-autodesign` ready to share with collaborators for a
small parallel full-pass dry run, including self-onboarding docs, per-activity
review status templates, and a Gemini image-generation provider path that does
not depend on Codex built-in `imagegen`.

## Design Source

Authoritative implementation context:

```text
docs/plans/2026-06-08-team-readiness-and-gemini-assets.md
```

The plan is authoritative for design rationale, file candidates, provider
contract, and rollout context. This goal is authoritative for hard constraints,
required checks, credential handling, and the final completion gate. If they
conflict, stop and document the conflict before changing behavior.

## Hard Constraints

- Do not read, print, copy, edit, or commit `.env`, service-account JSON files,
  API keys, tokens, or provider secrets.
- Do not copy fullstack-demo credentials into this repo.
- Do not use Codex built-in `imagegen` as the readiness proof for teammates.
- Keep package-local runtime variant generation in
  `scripts/build_activity_assets.py`; the Gemini provider may only write source
  PNGs into `runs/<run_id>/generated_assets/inbox/<activity_id>/`.
- Do not rewrite package text or mechanics to make image generation easier.
- Do not fabricate reference-bound factual assets with random generated images.
- Do not touch WonderLens AI or fullstack-demo implementation code.
- Preserve unrelated local user changes; stage only intended readiness work.

## Required Scope

- Add contributor onboarding documentation for the parallel workflow.
- Add image-generation provider setup documentation for Gemini.
- Add a per-activity `review_status.yaml` template under `runs/_templates/` or
  an equivalent template location documented for run authors.
- Add a Gemini provider script or adapter that reads run-local
  `asset_manifest.yaml` files and writes illustrative source PNGs to the
  existing builder inbox.
- Add explicit Python dependency setup for image generation because this repo
  has no root dependency manifest today.
- Update README and relevant workflow docs so collaborators can find the
  onboarding, provider setup, and status template.
- Add focused tests for provider config/path handling and secret-safe audit
  behavior.
- Run one live Gemini smoke in this workspace when the referenced fullstack
  backend credentials are present.

## Execution Rules

- Work from the autodesign repo root:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-autodesign
```

- Use a feature worktree or branch if implementation becomes more than a small
  docs-only patch.
- Inspect current scripts and tests before adding new provider code.
- Keep the Gemini implementation provider-agnostic enough that future providers
  can be added without changing `asset_manifest.yaml`.
- Default the Gemini model to `gemini-2.5-flash-image`, matching the referenced
  fullstack backend, but allow override by CLI or environment.
- Fail with setup guidance when credentials are missing; never log secret
  values.
- If dependencies are missing, document exact install commands instead of
  silently relying on the executor's local environment.
- Do not push unless explicitly asked after the goal run.

## Mandatory Ordering

1. Confirm worktree state and preserve unrelated local changes.
2. Inspect the current asset builder, validators, and fullstack backend Gemini
   pattern without reading secret files.
3. Add docs/templates before implementing provider code.
4. Add provider code and focused tests.
5. Run static/unit checks.
6. Run the live Gemini smoke only after static checks pass.
7. Update plan/goal indexes to `Completed` only after all completion gates pass.

## Live Provider Credential Rule

The Gemini setup reference is:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend
```

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
test -f scripts/build_activity_assets.py
test -f scripts/validate_asset_build_outputs.py
test -f docs/activity_asset_generation_workflow.md
test -f docs/full_pass_agentic_parallel_workflow.html
test -d /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend
```

## Success Criteria

- A new collaborator can find a concise onboarding doc from the README.
- The onboarding doc explains role branches, file ownership, review status
  updates, validation expectations, and handoff to the integration owner.
- A stable per-activity review-status template exists and is documented.
- Gemini provider setup is documented using the fullstack backend auth pattern
  while keeping secrets outside this repo.
- The provider script can select illustrative manifest assets, generate source
  PNGs with Gemini, write them to the builder inbox, and emit sanitized audit
  evidence.
- The deterministic asset builder still owns package-local runtime variants.
- Tests cover config/path handling, missing credential behavior, output path
  safety, and secret-safe audit output.
- A live Gemini smoke generates at least one non-production illustrative PNG,
  builds it through `scripts/build_activity_assets.py`, and validates the output.

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
  --limit 1

python3 scripts/build_activity_assets.py <non-production-smoke-run> --mode generate_illustrative
python3 scripts/validate_asset_build_outputs.py <non-production-smoke-run>
```

If implementation chooses a different smoke fixture path or CLI flag, update
the setup docs and final report with the exact command that was run.

## Final Completion Gate

The goal is complete only when the docs, template, provider path, tests, static
checks, and live Gemini smoke all pass, no secrets are staged or logged, and the
plan/goal indexes reflect the completed state. If live Gemini cannot be run
with the referenced backend credentials, mark the goal blocked instead of
claiming readiness.

## Goal Invocation

```text
/goal Implement goals/2026-06-08-team-readiness-and-gemini-assets-goal.md. Stop only when its completion gate is satisfied or a blocker is documented.
```
