# E2E Subset Runtime Validation Goal

## Mode

Plan-backed.

Use this file as the Codex goal-mode execution contract.

## Objective

Run a fresh 3 to 5 activity end-to-end validation subset across autodesign,
fullstack-demo, and WonderLens AI. Prove that autodesign can generate package
metadata and assets, fullstack-demo can import/play/gate the packages, and
WonderLens AI can convert/load/run matching runtime behavior.

## Design Source

Source plan:

- `docs/plans/2026-05-28-e2e-subset-runtime-validation.md`

Related context:

- `GOAL.md`
- `run.md`
- `README.md`
- `docs/plans/2026-05-28-generate-and-curate-asset-pipeline.md`
- `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/goals/2026-05-27-autodesign-package-demo-import-goal.md`
- `/Users/pharrelly/codebase/gitlab/wonderlens-ai/goals/2026-05-27-autodesign-demo-package-ingestion-goal.md`

The plan is authoritative for design rationale, current evidence, repo
boundaries, and risk context. This goal is authoritative for hard constraints,
required checks, credential handling, delegated-agent rules, and completion. If
the plan and goal conflict, stop and document the conflict before changing
behavior.

## Hard Constraints

- Use a fresh scoped autodesign run, not only old fixtures.
- Use `demo_export=true` and `asset_build=generate_and_curate`.
- Validate package-local assets, not contact sheets.
- Required assets must have at least one runtime variant with minimum edge
  `>=512px`.
- Reference-bound assets must use verified source metadata and must not be
  random generated approximations.
- Do not claim autodesign directly emits WonderLens AI `runtime.yaml`; verify
  `runtime.yaml` through the WonderLens AI converter.
- Do not make unsupported mechanics playable to make the demo pass.
- Do not implement broad downstream fixes inside this validation goal. Record
  substantial issues as blockers or follow-up goals with owning repo evidence.
- Do not edit, print, copy, or commit `.env`, credential JSON files, tokens, or
  provider secrets.
- Do not leave backend/frontend servers running at completion.
- Do not push unless explicitly asked.

## Required Scope

Produce and validate a subset covering:

- Cat1 simple supported activity;
- Cat5 simple collection supported activity;
- Cat5 runtime-judgment degraded or supported activity;
- unsupported UI-heavy mechanic;
- reference-bound asset case.

For the subset, verify:

- autodesign package files, demo support, asset manifest, generated assets, and
  review dashboard;
- fullstack-demo package import, asset copy, entity binding, selection gating,
  playable starts, and unsupported/degraded visibility;
- WonderLens AI runtime generation, package loading, support/asset readiness,
  exact-package runtime behavior, and asset serving;
- final result report under the autodesign run directory.

## Delegated Agent Rule

The user explicitly requested delegated-agent rules for this goal.

Use sub-agents only for independent exploration, verification, visual QA,
runtime behavior comparison, downstream import smoke, or code review with
disjoint ownership. Keep subset selection, credentials, server lifecycle,
cross-repo orchestration, blocker classification, final report, final checks,
committing, and final user reporting local to the main agent.

Good delegation candidates:

- review the autodesign generated packages against `program.md`, `GOAL.md`,
  demo support, asset manifest, and source-fidelity rules;
- inspect generated visual assets for round-screen quality and
  reference-bound correctness;
- run or review fullstack-demo import/play/gate results;
- run or review WonderLens AI runtime conversion and runtime-beat matching;
- independently review the final validation report for unsupported/degraded
  honesty and repo ownership of failures.

## Execution Rules

- Start from clean synced `main` in all three repos, or document any unrelated
  local changes before proceeding.
- Use validation branches/worktrees when generated imports or test artifacts
  would modify consumer repos.
- Prefer transient `.artifacts/` directories for downstream reports.
- Add scoped autodesign assignment rows only under a clearly labeled validation
  section and mark them complete only after reviewer evidence and local checks.
- Use existing repo commands and current AGENTS.md instructions in each repo.
- If a command name has moved, use the equivalent current command and record the
  substitution in the final report.
- Stop on failing checks that make later validation misleading. Record root
  cause before broadening scope.
- Keep final committed autodesign changes limited to intentional validation
  artifacts, status indexes, and the result report unless the user explicitly
  asks to commit downstream repo changes.

## Mandatory Ordering

1. Record current commit SHA and clean/dirty state for all three repos.
2. Create or identify the fresh autodesign subset assignments.
3. Run the scoped autodesign generation using `asset_build=generate_and_curate`.
4. Validate autodesign package/demo/asset outputs and run review dashboard.
5. Run independent package and visual/reference review, using delegated agents
   where ownership is disjoint.
6. Import the generated packages into fullstack-demo and verify play/gate
   behavior.
7. Convert/load the generated packages in WonderLens AI and verify
   `runtime.yaml`, support/readiness, asset serving, and runtime behavior.
8. Run live server/API/browser/WS smoke only after deterministic checks pass.
9. Write the final validation report and update plan/goal indexes to
   `Completed` or `Blocked`.
10. Commit intended autodesign validation artifacts and index updates.

## Live Provider Credential Rule

Live fullstack-demo and WonderLens AI smokes may require provider credentials.
Use this pattern only in the terminal session that starts the relevant backend:

```bash
MAIN_REPO_ROOT="<absolute repo root for the server being started>"
set -a
source "$MAIN_REPO_ROOT/.env"
set +a
export GOOGLE_APPLICATION_CREDENTIALS="$(ls "$MAIN_REPO_ROOT"/.elaborate-baton-*.json | head -n 1)"
```

If the repo uses a different documented credential file, use that documented
path and record only the fact that credentials were loaded, never the secret
values. Do not edit, print, copy, or commit `.env`, credential JSON files,
tokens, or provider secrets.

## Preconditions

Autodesign repo:

```bash
git status --short --branch
test -f GOAL.md
test -f run.md
test -f scripts/validate_demo_package_contract.py
test -f scripts/validate_asset_build_outputs.py
```

Fullstack demo repo:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
git status --short --branch
test -f scripts/import_autodesign_package.py
test -f frontend/package.json
```

WonderLens AI repo:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
git status --short --branch
test -f scripts/generate_activity_runtime.py
test -f app/modules/activity/packages/runtime_generator.py
```

## Success Criteria

- The subset contains the required Cat1, Cat5, degraded/judgment,
  unsupported, and reference-bound coverage.
- Autodesign generated packages pass demo package contract validation.
- Autodesign generated assets pass asset output validation and include
  high-resolution runtime variants.
- Autodesign `review.html` validates and links package-local assets.
- Fullstack-demo imports supported/degraded packages and gates unsupported
  packages according to `demo_support.yaml`.
- Fullstack-demo copied assets resolve through browser-safe URLs.
- WonderLens AI generates or validates `runtime.yaml` for executable packages.
- WonderLens AI rejects or gates unsupported and asset-blocked packages.
- Runtime behavior in both consumers is compared against the autodesign
  `prod.md` beats and differences are explained.
- Live smoke evidence is recorded, or missing credentials/provider blockers are
  documented clearly enough to reproduce.
- The final report assigns every failure to autodesign, fullstack-demo,
  WonderLens AI, credentials, or product-scope follow-up.

## Required Checks

Autodesign minimum checks, replacing `<run_id>` with the fresh run:

```bash
python3 scripts/validate_demo_package_contract.py runs/<run_id>/activity_packages
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
git diff --check
```

Fullstack-demo minimum deterministic checks after import:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
PYTHONDONTWRITEBYTECODE=1 uv run pytest tests/test_autodesign_importer.py tests/test_entity_registry.py tests/test_api.py -q -p no:cacheprovider
cd frontend && npm test -- --run
```

WonderLens AI minimum deterministic checks after runtime generation:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run pytest tests/unit/activity/test_activity_package_models.py tests/unit/activity/test_activity_package_loader.py tests/unit/activity/test_runtime_generator.py tests/unit/scripts/test_generate_activity_runtime.py -q
uv run pytest tests/unit/activity/test_activity_asset_manifest.py tests/api/test_activity_ws.py -k 'asset_manifest or package' -q
uv run python scripts/generate_activity_runtime.py --source <autodesign_run>/activity_packages --dest .artifacts/e2e-subset-runtime/activities --write --force --report-json .artifacts/e2e-subset-runtime/report.json
```

Live smoke checks must include at least one playable Cat1, one playable Cat5,
one gated unsupported package, and one asset/reference-bound inspection path.
Use the current repo-specific server commands and record ports, endpoints,
request IDs, screenshots, or trace files in the final report.

## Final Completion Gate

Do not mark achieved until:

- required scope is validated or a real blocker is documented with evidence;
- success criteria are met or each failure has an owning repo and follow-up
  recommendation;
- required deterministic checks pass unless blocked before the consumer stage;
- live smoke is completed or blocked by explicit credential/provider evidence;
- delegated-agent review evidence is recorded for at least autodesign package
  quality and one downstream consumer path;
- no live-provider credentials or unsafe absolute local paths are included in
  package contracts or committed audit files;
- `docs/plans/README.md` and `goals/README.md` mark this plan/goal `Completed`
  or `Blocked` as appropriate;
- intended autodesign artifacts are committed with conventional commit
  messages.

Final response must include selected activity IDs, run path, downstream report
paths, checks run, live smoke evidence or blocker, delegated-agent review
summary, remaining risks, and commit hashes.

## Goal Invocation

Use from the `wonderlens-activity-autodesign` repo or validation worktree:

```text
/goal Implement goals/2026-05-28-e2e-subset-runtime-validation-goal.md. The user explicitly requests delegated-agent work for independent package review, visual/reference QA, downstream import/runtime verification, live-smoke review, and final report review where ownership is disjoint. Stop only when its completion gate is satisfied or a blocker is documented.
```
