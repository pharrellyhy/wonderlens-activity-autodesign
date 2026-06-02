# Run Full-Pass Agentic Pipeline Plan

Date: 2026-06-01

Status: Planned

## Purpose

Run the full WonderLens activity generation pass using the agentic pipeline
already encoded in `GOAL.md`, `run.md`, `program.md`, and
`docs/plans/2026-06-01-full-pass-agentic-pipeline.md`.

This is an execution plan, not another contract-hardening pass. The run should
generate complete autodesign activity packages and PNG assets, then prove that
fullstack-demo and WonderLens AI can load and exercise those packages directly
without manual content improvement.

## Run Target

Source input:

- `inputs/original_activity_concepts_2026-05-29.tsv` is the current workbook
  source-intent baseline.
- `inputs/source_activity_concepts.md` is a normalized helper only.
- If the TSV and helper disagree on child role, interaction sequence, required
  child action, real/reference asset requirement, or background/context
  promise, the TSV wins unless a product decision is recorded.

Default scope:

- Process the current workbook-derived activity set unless the user supplies a
  narrower scope before invocation.
- Use `asset_build=generate_and_curate`.
- Use `full_pass_pipeline=true`.
- Write generated artifacts under a fresh `runs/<run_id>/` directory.

Consumer targets:

- Fullstack-demo worktree and branch:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game`
- Fullstack-demo credential source:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend`
- WonderLens AI repo:
  `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

## Required Fullstack Server Branch

Fullstack validation must start the demo server from the
`feat/activity-text-game` worktree, not from the fullstack main checkout:

```bash
FULLSTACK_WORKTREE="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game"
FULLSTACK_MAIN="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo"
FULLSTACK_MAIN_BACKEND="$FULLSTACK_MAIN/backend"

test -d "$FULLSTACK_WORKTREE"
test "$(git -C "$FULLSTACK_WORKTREE" branch --show-current)" = "feat/activity-text-game"
test -f "$FULLSTACK_MAIN_BACKEND/.env"
test -f "$FULLSTACK_MAIN_BACKEND/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
```

When a live fullstack API smoke is required, start the backend from the
worktree backend while sourcing credentials from the fullstack main backend.
Do not copy, print, or commit the credential values:

```bash
RUN_ID="<run_id>"
cd "$FULLSTACK_WORKTREE/backend"
set -a
source "$FULLSTACK_MAIN_BACKEND/.env"
set +a
export GOOGLE_APPLICATION_CREDENTIALS="$FULLSTACK_MAIN_BACKEND/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
export DB_PATH="/tmp/wl_full_pass_fullstack_${RUN_ID}.sqlite3"
uv sync
uv run uvicorn server:app --host 127.0.0.1 --port 8000
```

If the frontend is needed for browser verification, start it from the same
worktree:

```bash
cd "$FULLSTACK_WORKTREE/frontend"
npm install
npm run dev -- --host 127.0.0.1 --port 5173
```

Use the canonical ports `8000` and `5173` unless they are occupied by a server
started for this run. Do not stop unrelated local services. If the canonical
ports cannot be used safely, record the blocker or the alternate port setup in
the validation report.

Before loading generated activities, back up any mutable fullstack target
directories to a local temp path:

```bash
FULLSTACK_BACKUP="/tmp/wl_full_pass_${RUN_ID}/fullstack_backup"
mkdir -p "$FULLSTACK_BACKUP"
rsync -a "$FULLSTACK_WORKTREE/backend/games/" "$FULLSTACK_BACKUP/backend_games/"
rsync -a "$FULLSTACK_WORKTREE/frontend/public/activity-assets/" "$FULLSTACK_BACKUP/activity_assets/"
```

The fullstack branch currently treats `backend/games/*.md` and
`frontend/public/activity-assets/` as the runtime loading surface. If its direct
autodesign-package importer is missing or has moved, use the current branch's
documented loader/converter only as a structural conversion step and audit the
converted `step_instructions` against the autodesign package. Do not accept a
conversion that improves, rewrites, or changes the activity intent.

## WonderLens AI Server

WonderLens AI validation should use the main checkout unless the user supplies
a separate branch:

```bash
WONDERLENS_AI_ROOT="/Users/pharrelly/codebase/gitlab/wonderlens-ai"
test -d "$WONDERLENS_AI_ROOT"
cd "$WONDERLENS_AI_ROOT"
test "$(git branch --show-current)" = "main"
test -f .env
test -f .elaborate-baton-480304-r8-a8a39bcb34f1.json
```

When a live WonderLens AI smoke is required:

```bash
cd "$WONDERLENS_AI_ROOT"
set -a
source .env
set +a
export GOOGLE_APPLICATION_CREDENTIALS="$WONDERLENS_AI_ROOT/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
export DIRECTIVE_PIPELINE_ENABLED=true
export DEBUG=true
uv sync --locked
uv run uvicorn app.main:app --host 127.0.0.1 --port 8765
```

Stop any server started by the run before completion.

## API Rate-Limit Handling

Rate limits are expected operational events during full-pass generation,
especially for image generation, live dialogue QA, and runtime conversion that
uses hosted providers. A rate-limit response must not stop the full pass
directly.

When any provider or local harness returns `429`, `RESOURCE_EXHAUSTED`, quota
exceeded, `rate_limit`, or equivalent throttling:

- record the phase, activity ID or batch, command, timestamp, provider name if
  safe, and sanitized error class;
- do not print or store secret-bearing request payloads or headers;
- wait a few minutes before retrying, using at least a 3-minute first pause and
  a 3/5/8-minute backoff for repeated throttles on the same request or batch;
- retry at least three times before classifying the condition as blocked;
- reduce concurrency or batch size when that lowers pressure without changing
  generation quality;
- continue only independent non-API work while waiting, and only when doing so
  does not violate the required validation order;
- never fabricate assets, transcripts, or validation evidence to bypass a rate
  limit.

If throttling persists after the retry window, record it as an external API
blocker with the retry log and resume point.

## Orchestration Model

The master agent owns run setup, artifact layout, server lifecycle, credentials,
final acceptance, commits, and user reporting. Delegated agents provide
evidence and repairs only within assigned ownership.

Required delegated roles:

| Role | Ownership | Pass output |
|---|---|---|
| Source-intent auditor | Workbook/source comparison only | `aligned`, `minor_adaptation`, `intent_drift`, or `needs_product_decision` per activity with evidence. |
| Activity package writer | Text package files only | `spec.md`, `prod.md`, metadata/templates, and `asset_manifest.yaml` with no image generation. |
| Scene/object/item asset generator | PNG source assets only | Source PNGs, accepted reference originals, and package-local variants generated from the manifest. |
| Fullstack dialogue validator | Fullstack import/load and live API only | Converted `step_instructions`, sanitized transcripts, and pass/fail criteria. |
| Image quality validator | Visual QA only | Style, role, crop, scene-dialogue alignment, reference fidelity, and no-text/no-label verdicts. |
| Fullstack dialogue improver | Package-owned text repair only | Repaired runtime instructions or downstream issue classification. |
| Image quality improver | Asset repair only | Regenerated/curated assets and updated asset reports. |
| WonderLens AI dialogue validator | WonderLens AI runtime only | Runtime generation/load report, transcripts, and pass/fail criteria. |
| WonderLens AI dialogue improver | Package-owned WonderLens-facing repair only | Package repair or WonderLens AI follow-up classification. |
| Final independent reviewer | Cross-artifact review | Final pass/fail report with unresolved risks. |

Delegated agents must not edit `.env`, credential JSON files, or shared files
outside their assigned artifact path. Validators must not repair their own
failures. Improvers must work from concrete failure reports and rerun the
failing validator after repair.

## Execution Phases

1. Prepare a clean autodesign worktree and record repo state.
2. Create a fresh run under `runs/<run_id>/` with `asset_build:
   generate_and_curate` and `full_pass_pipeline: true` in `run_manifest.yaml`.
3. Snapshot workbook rows and run the pre-package source-intent auditor.
4. Generate text-only packages from the source snapshots.
5. Run package validation, self-evaluation, and independent package review.
6. Run the post-package source-intent auditor before any downstream validation.
7. Generate or curate PNG assets using `scripts/build_activity_assets.py`.
8. Run image QA and repair image-owned failures.
9. Confirm runtime-facing `prod.md` files are marker-free:

   ```bash
   ! rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md
   ```

10. Load generated packages into fullstack-demo from the
    `feat/activity-text-game` worktree and validate converted
    `step_instructions`.
11. Start the fullstack server from the same worktree and run live dialogue QA
    with multiple input strategies.
12. Generate/load WonderLens AI runtime artifacts and run WonderLens AI
    dialogue QA with the same source-intent and unsupported-claim criteria.
13. Route failures to package text repair, image repair, fullstack follow-up,
    WonderLens AI follow-up, or product decision.
14. Re-run the failed validator after every repair.
15. Run final independent review and generate the run report.
16. Commit intended autodesign artifacts only after checks pass.

## Dialogue Quality Criteria

A fullstack or WonderLens AI dialogue pass requires:

- source play frame, child role, device role, sequence, required child action,
  reference asset requirement, and background/context promise are preserved;
- runtime instructions convert into quality `step_instructions` or WonderLens
  runtime prompts with goal/action, tier or length constraint, emotion/tone,
  progress evidence, branch behavior, frame/source guardrail, screen/state
  expectation, and an example line;
- no unsupported visual inspection, hidden-state, screen-content, or sensing
  claims;
- ideal, minimal, wrong, off-topic, help/confusion, silence, premature done,
  and unsupported-request inputs either progress, repair the branch, or exit
  gracefully;
- repeated unproductive inputs do not loop forever; the runtime should force
  progress or gracefully exit after the configured cap;
- Cat5 collection preserves collected items and synthesis quality;
- final recap names the correct concept and child action.

Package-owned dialogue failures block acceptance until repaired and rechecked.
Runtime-owned failures block full-pass acceptance unless the user explicitly
accepts a downstream follow-up instead.

## Image Quality Criteria

An image pass requires:

- generated PNGs follow `docs/activity_asset_generation_workflow.md` and the
  fullstack style reference at
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game/frontend/public/activity-assets/prompts/wonderlens-activity-style.md`;
- every package has the standard fullstack-style asset bundle:
  `activity_icon`, `intro_scene`, `rules_scene`, `round_1_scene`,
  `round_2_scene`, `round_3_scene`, `celebrate_scene`, and `closing_scene`,
  plus `synthesis_scene` for Cat5/synthesis flows;
- each declared scene, character, object, item, icon, badge, or distractor has
  one readable 512x512 asset unless a larger variant is explicitly requested;
- generated illustrative source PNGs are 512x512 square, while final runtime
  variants remain manifest-driven;
- scene assets match the dialogue beat and do not change the mechanic;
- scene PNGs do not contain app-owned progress/control UI such as progress
  dots, round markers, response slots, rule strips, buttons, chips, picker
  slots, badges, or other runtime interface markers;
- unrelated activity scene bundles are visually distinct and do not reuse the
  same cozy-room, blank-board, child-response, or child-on-rug template;
- guided drawing and other build-step scene bundles show the specific drawing
  or build instruction for each round;
- scene backgrounds do not duplicate selectable items/objects in a way that
  competes with picker sprites, target/distractor cards, or collection items;
- progressive evidence and partial-reveal images do not expose the final
  answer, full target, or solution before the source-aligned reveal beat;
- duplicate picker objects or premature answer reveal are hard image-QA repair
  verdicts because they change the source-intent step sequence;
- item/object/character assets are centered and crop-safe;
- no text, letters, numbers, labels, watermarks, contact sheets, multi-card
  sheets, borders, masks, or device chrome are baked into generated assets;
- reference-bound assets use accepted originals and metadata, not invented
  generated approximations.

## Required Checks

Autodesign checks:

```bash
python3 scripts/validate_demo_package_contract.py runs/<run_id>/activity_packages
python3 scripts/repair_full_pass_asset_bundle.py runs/<run_id>
python3 scripts/build_activity_assets.py runs/<run_id> --mode generate_and_curate
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
python3 scripts/validate_full_pass_asset_bundle.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
! rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md
git diff --check
```

Fullstack checks from the required worktree after loading activities:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game
uv run pytest backend/tests/test_activity_text_game_api.py backend/tests/test_activity_text_game_definitions.py backend/tests/test_activity_text_game_cat3.py backend/tests/test_activity_text_game_turns.py -q
uv run python scripts/run_activity_text_smoke.py --base-url http://127.0.0.1:8000
cd frontend
npm test -- tests/activityAssets.test.js tests/useActivityTextSession.test.jsx tests/WonderLensDevice.test.jsx tests/ActivityGameApp.test.jsx
npm run build
```

WonderLens AI checks after runtime generation:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run python scripts/generate_activity_runtime.py --source <autodesign_run>/activity_packages --dest .artifacts/full-pass-agentic/activities --write --force --report-json .artifacts/full-pass-agentic/runtime-report.json
uv run pytest tests/unit/activity/test_activity_package_models.py tests/unit/activity/test_activity_package_loader.py tests/unit/activity/test_runtime_generator.py tests/unit/scripts/test_generate_activity_runtime.py -q
DIRECTIVE_PIPELINE_ENABLED=true uv run python tests/integration/live/test_activity_live_matrix.py --scenario all
```

If repo commands have changed, use the current closest command, record the
substitution, and explain whether the validation coverage is equivalent.

## Success Criteria

- The run has package, source-intent, asset, downstream, dialogue, repair, and
  final-review evidence under `runs/<run_id>/`.
- Every accepted package is free of unresolved `intent_drift`.
- Every accepted package has package-local PNG assets or an honest
  blocked/degraded record for missing reference-bound sources.
- Fullstack-demo loads the packages from the `feat/activity-text-game`
  worktree and preserves converted `step_instructions` quality.
- WonderLens AI generates/loads runtime artifacts and preserves dialogue
  quality.
- Fullstack and WonderLens AI dialogue QA pass or every failure has an owner
  and an explicit product/downstream decision.
- No live server started by the run is still running.
- Intended autodesign artifacts are committed; downstream repo changes are not
  committed unless the user explicitly expands scope.

## Non-Goals

- Do not implement new fullstack-demo or WonderLens AI runtime features during
  this run unless the user explicitly expands scope.
- Do not use fullstack-demo or WonderLens AI as content improvers.
- Do not relax source intent to make packages easier to run.
- Do not accept generated approximations for factual/reference-bound assets.

## Goal Invocation

Use from the `wonderlens-activity-autodesign` repo or a clean autodesign
worktree:

```text
/goal Implement goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md. Execute the current workbook full pass from inputs/original_activity_concepts_2026-05-29.tsv with asset_build=generate_and_curate and full_pass_pipeline=true; start fullstack validation only from /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game on branch feat/activity-text-game while sourcing live credentials only from /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend; use delegated agents for source intent, text package writing, image generation, fullstack dialogue QA, WonderLens AI dialogue QA, image QA, repair loops, and final independent review; stop only when the completion gate is satisfied or a blocker is documented.
```
