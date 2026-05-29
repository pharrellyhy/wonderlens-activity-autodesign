# Source Intent Pilot Validation Goal

## Mode

Plan-backed.

Use this file as the Codex goal-mode execution contract.

## Objective

Run a fresh 3 to 5 activity pilot selected from the original source-design
inputs, with user-named rows taking priority when provided. Prove that
autodesign preserves source intent, generates runtime-ready AI instructions,
builds actual PNG assets with `asset_build=generate_and_curate`, and that both
fullstack-demo and WonderLens AI convert/load the packages cleanly.

## Design Source

Source plan:

- `docs/plans/2026-05-29-source-intent-pilot-validation.md`

Related context:

- `GOAL.md`
- `run.md`
- `program.md`
- `docs/activity_asset_generation_workflow.md`
- `inputs/original_activity_concepts_2026-05-29.tsv`
- `inputs/source_activity_concepts.md`
- `docs/plans/2026-05-28-e2e-subset-runtime-validation.md`
- `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/games/fluffy_expedition_dandelion.md`
- `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo`
- `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

The plan is authoritative for design rationale, pilot shape, and review
coverage. This goal is authoritative for hard constraints, required checks,
credential handling, delegated-agent rules, and completion. If the plan and
goal conflict, stop and document the conflict before changing behavior.

## Hard Constraints

- Select 3 to 5 pilot designs from
  `inputs/original_activity_concepts_2026-05-29.tsv`. If the user names
  specific designs, use those first; otherwise use the default high-risk
  candidate set in the source plan.
- Capture a stable source snapshot before generation, either by referencing
  exact committed source sections or by writing a run-local copy when the input
  comes from chat or another non-versioned form.
- Treat `inputs/source_activity_concepts.md` as a normalized helper for English
  fields, mechanics, asset requirements, and product-capability flags. If it
  disagrees with the original TSV row, the TSV row wins unless the final report
  records an explicit product-approved source change.
- Execute the scoped generation through `GOAL.md` / `run.md`; do not handwrite
  final packages outside the workflow.
- Set the run to `demo_export=true` and `asset_build=generate_and_curate`.
- Produce actual runtime PNG assets for required assets; `manifest_only` is not
  sufficient for this pilot.
- Do not accept arbitrary generated approximations for reference-bound assets.
- Do not rewrite package prose to fit generated images; assets support the
  activity design, not the other way around.
- Do not log `results.tsv`, mark assignments complete, or accept downstream
  imports while source-intent drift is unresolved.
- Do not accept thin `Runtime AI instruction` beats. They must be rich enough
  to convert into fullstack-demo and WonderLens AI step instructions.
- Compare converted fullstack `step_instructions` against the quality floor in
  `backend/games/fluffy_expedition_dandelion.md`.
- Do not make unsupported mechanics playable to make the pilot pass.
- Do not edit, print, copy, or commit `.env`, credential JSON files, tokens, or
  provider secrets.
- Do not leave backend/frontend servers running at completion.
- Do not push unless explicitly asked.

## Required Scope

The pilot should cover, across 3 to 5 designs:

- one factual or reference-bound asset case;
- one activity with required background/context information;
- one multi-step child-action sequence;
- one asset-dependent scene, character, or object case;
- one simpler control activity.

For each generated package, verify:

- source-intent preservation;
- package depth and mechanic fidelity;
- runtime AI instruction quality;
- generated PNG output and asset manifest paths;
- reference-bound source/provenance when applicable;
- fullstack import and converted `step_instructions`;
- WonderLens AI runtime generation/loading/conversion;
- support, degraded, or unsupported state honesty.

## Delegated Agent Rule

The user explicitly requested stronger subagent verification for source-intent
drift and checklist coverage.

Use sub-agents for independent source-intent audit, runtime-instruction quality
review, visual/reference QA, fullstack import verification, WonderLens AI
runtime verification, and final report review when ownership is disjoint. Keep
source-design normalization, product decisions, credentials, server lifecycle,
blocking judgments, commits, and final user reporting local to the main agent.

Every generated package must have independent source-intent auditor evidence
before it is accepted. Reviewer evidence must include a verdict of `aligned`,
`minor_adaptation`, `intent_drift`, or `needs_product_decision`.

## Execution Rules

- Start from clean synced `main` in autodesign, fullstack-demo, and WonderLens
  AI, or document unrelated local changes before proceeding.
- If the source-intent auditor gate is not explicit enough in `GOAL.md`,
  `run.md`, or `program.md`, strengthen those documents first and commit that
  contract change before running the pilot.
- Use a scoped validation section or scoped input file for the pilot designs.
- Preserve the original source design wording as reviewer evidence.
- Use `asset_build=generate_and_curate`; after package validation, generate or
  curate source images and run the asset builder/validator.
- For illustrative assets, create source PNGs under
  `runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png`.
- For reference-bound assets, store accepted originals and reviewer-approved
  metadata under package-local `assets/sources/`.
- Record all reviewer/subagent findings, repairs, and re-review outcomes in
  the run artifacts.
- Stop on failures that make later validation misleading. Record root cause and
  owning repo before broadening scope.
- Keep broad downstream fixes out of this pilot unless the user explicitly asks
  to implement them.

## Mandatory Ordering

1. Record current commit SHA and clean/dirty state for all three repos.
2. Confirm or add the explicit source-intent auditor gate in `GOAL.md`,
   `run.md`, and `program.md`.
3. Select 3 to 5 source designs from
   `inputs/original_activity_concepts_2026-05-29.tsv`, using user-named rows
   first and otherwise the plan's default high-risk candidate set.
4. Capture the selected source designs as stable pilot input.
5. Run scoped autodesign generation with `demo_export=true` and
   `asset_build=generate_and_curate`.
6. Build and validate package-local PNG assets.
7. Run independent source-intent, package-depth, runtime-instruction, and
   visual/reference reviews; repair and re-review failures.
8. Import the generated packages into fullstack-demo and inspect converted
   `step_instructions`.
9. Convert/load the generated packages in WonderLens AI and inspect runtime
   behavior.
10. Write `runs/<run_id>/source_intent_pilot_validation.md`.
11. Update plan/goal indexes to `Completed` or `Blocked`, then commit intended
    autodesign changes and artifacts.

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
path and record only that credentials were loaded. Never record secret values.

## Preconditions

Autodesign repo:

```bash
git status --short --branch
test -f GOAL.md
test -f run.md
test -f program.md
test -f docs/activity_asset_generation_workflow.md
test -f inputs/original_activity_concepts_2026-05-29.tsv
test -f inputs/source_activity_concepts.md
test -f scripts/build_activity_assets.py
test -f scripts/validate_asset_build_outputs.py
test -f scripts/validate_demo_package_contract.py
```

Fullstack demo repo:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
git status --short --branch
test -f scripts/import_autodesign_package.py
test -f backend/games/fluffy_expedition_dandelion.md
```

WonderLens AI repo:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
git status --short --branch
test -f scripts/generate_activity_runtime.py
```

## Success Criteria

- The pilot uses 3 to 5 designs from
  `inputs/original_activity_concepts_2026-05-29.tsv` and records a stable
  source snapshot.
- The run records `asset_build=generate_and_curate`.
- Required assets have package-local runtime PNG variants and asset validation
  passes.
- Reference-bound assets have verified source/provenance or are honestly
  blocked/degraded.
- Every package has independent source-intent auditor evidence.
- No package accepted as complete has unresolved `intent_drift`.
- Runtime AI instructions are rich enough to convert into quality downstream
  `step_instructions`.
- Fullstack-demo imports supported/degraded packages, gates unsupported
  packages, and produces step instructions that meet the quality floor.
- WonderLens AI converts/loads executable packages and preserves support,
  asset, and runtime-beat behavior.
- The final report clearly recommends whether to proceed to a larger/full pass.

## Required Checks

Autodesign checks, replacing `<run_id>` with the pilot run:

```bash
python3 scripts/validate_demo_package_contract.py runs/<run_id>/activity_packages
python3 scripts/build_activity_assets.py runs/<run_id> --mode generate_and_curate
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
git diff --check
```

Fullstack-demo deterministic checks after import:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
uv run python scripts/import_autodesign_package.py <package_dirs...> --source-commit <autodesign_commit>
PYTHONDONTWRITEBYTECODE=1 uv run pytest tests/test_autodesign_importer.py tests/test_entity_registry.py tests/test_api.py -q -p no:cacheprovider
```

WonderLens AI deterministic checks after runtime generation:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run python scripts/generate_activity_runtime.py --source <autodesign_run>/activity_packages --dest .artifacts/source-intent-pilot/activities --write --force --report-json .artifacts/source-intent-pilot/report.json
uv run pytest tests/unit/activity/test_activity_package_models.py tests/unit/activity/test_activity_package_loader.py tests/unit/activity/test_runtime_generator.py tests/unit/scripts/test_generate_activity_runtime.py -q
```

If repo commands have moved, use the current equivalent command and record the
substitution in the final report.

## Final Completion Gate

Do not mark achieved until:

- source-intent auditor, runtime-instruction, visual/reference, fullstack, and
  WonderLens AI evidence is recorded or explicitly blocked;
- every accepted package is free of unresolved `intent_drift`;
- generated PNG assets validate or missing required assets are honestly
  recorded as blockers/degraded behavior;
- downstream conversion/load checks pass or failures are assigned to an owning
  repo with evidence;
- the final report recommends whether to proceed to a larger/full pass;
- `docs/plans/README.md` and `goals/README.md` mark this plan/goal `Completed`
  or `Blocked`;
- intended autodesign artifacts are committed with conventional commit
  messages.

Final response must include selected activity IDs, run path, asset build status,
source-intent verdict summary, downstream report paths, checks run, delegated
review summary, remaining risks, and commit hashes.

## Goal Invocation

Use from the `wonderlens-activity-autodesign` repo or validation worktree:

```text
/goal Implement goals/2026-05-29-source-intent-pilot-validation-goal.md. Select 3 to 5 pilot source activity designs from inputs/original_activity_concepts_2026-05-29.tsv, using user-named rows first and otherwise the plan's default high-risk candidates; set asset_build=generate_and_curate so runtime PNGs are generated; and use delegated agents for independent source-intent, runtime-instruction, visual/reference, fullstack, WonderLens AI, and final-report verification where ownership is disjoint. Stop only when the completion gate is satisfied or a blocker is documented.
```
