# Run Full-Pass Agentic Pipeline Goal

## Mode

Plan-backed.

Use this file as the Codex goal-mode execution contract for the actual
full-pass run.

## Objective

Execute the full-pass agentic activity generation pipeline for the current
workbook-derived activity set. Generate autodesign packages and PNG assets,
then validate that fullstack-demo and WonderLens AI can load and exercise those
packages directly without manual content improvement.

## Design Source

Source plan:

- `docs/plans/2026-06-01-run-full-pass-agentic-pipeline.md`

Pipeline contract:

- `docs/plans/2026-06-01-full-pass-agentic-pipeline.md`
- `GOAL.md`
- `run.md`
- `program.md`
- `docs/activity_asset_generation_workflow.md`
- `docs/full_pass_agentic_pipeline_explainer.md`

Consumer targets:

- Fullstack-demo required worktree:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game`
- Fullstack-demo credential source:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend`
- WonderLens AI repo:
  `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

The plan is authoritative for run procedure and validation detail. This goal is
authoritative for hard constraints, ordering, delegated-agent rules, credential
handling, completion, and final reporting.

## Hard Constraints

- Use `inputs/original_activity_concepts_2026-05-29.tsv` as the source-intent
  baseline unless the user explicitly provides a newer source.
- Treat `inputs/source_activity_concepts.md` as a normalized helper only. If it
  disagrees with the TSV on child role, sequence, required action,
  real/reference asset requirement, or background/context promise, the TSV
  wins unless a product decision is recorded.
- Set `asset_build=generate_and_curate` and `full_pass_pipeline=true`.
- Generate actual package-local PNG assets; `manifest_only` is not acceptable
  for this run.
- Generate illustrative source PNGs with the Codex built-in imagegen tool. Do
  not accept SVG/vector drawings, placeholder art, or non-imagegen scripts as
  generated illustrative assets.
- Use the repo-local style prompt and reference image in
  `docs/asset_style_reference/` as the active flat Nordic visual target.
- Keep package writing text-only and image generation image-only.
- Do not use fullstack-demo or WonderLens AI as content improvement steps.
- Do not rewrite activity intent to fit generated images, fullstack behavior,
  or WonderLens AI behavior.
- Do not accept packages with unresolved `intent_drift`.
- Do not compare fullstack-demo and WonderLens AI dialogue quality until
  runtime-facing `prod.md` files are free of raw `RESOLVED BLOCKER` or
  `RESOLVE BLOCKER` markers.
- Fullstack live validation must start from
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game`
  and the branch must be `feat/activity-text-game`.
- Fullstack live validation may source `.env` and the service-account JSON only
  from `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend`.
- Do not edit, print, copy into the repo, or commit `.env`, credential JSON
  files, tokens, or provider secrets.
- Do not leave servers running at completion.
- Do not commit downstream fullstack-demo or WonderLens AI changes unless the
  user explicitly expands scope.
- If image generation, hosted LLM, fullstack live API, WonderLens AI live API,
  or runtime-conversion calls hit provider rate limits, do not stop directly:
  log the sanitized throttle, wait a few minutes, retry with backoff, and only
  classify the condition as blocked after at least three retry attempts.
- Do not push unless explicitly asked.

## Required Scope

Produce a complete autodesign run with:

- run manifest and assignment/source snapshot;
- pre-package and post-package source-intent audit evidence;
- generated activity packages under `runs/<run_id>/activity_packages/`;
- package self-evaluation and independent package-review evidence;
- generated/curated PNG assets and asset validation reports;
- fullstack-style package-local scene bundles for every package:
  `activity_icon`, `intro_scene`, `rules_scene`, `round_1_scene`,
  `round_2_scene`, `round_3_scene`, `celebrate_scene`, and `closing_scene`,
  plus `synthesis_scene` for Cat5/synthesis flows;
- image QA and repair evidence;
- fullstack load/import evidence from the required worktree;
- fullstack converted `step_instructions` quality review;
- fullstack live dialogue QA using multiple child-input strategies;
- WonderLens AI runtime generation/load evidence;
- WonderLens AI dialogue QA using comparable child-input strategies;
- dialogue and image repair-loop evidence;
- final independent cross-artifact review;
- final run report and committed intended autodesign artifacts.

## Delegated Agent Rules

Use delegated agents whenever ownership is disjoint and evidence can be
reviewed independently. The master agent owns run setup, source scope,
credentials, server lifecycle, final acceptance, commits, and final user
reporting.

Required delegated roles:

- source-intent auditor;
- activity package writer, text only;
- scene/object/item asset generator, image only;
- fullstack dialogue validator;
- image quality validator;
- fullstack dialogue quality improver;
- image quality improver;
- WonderLens AI dialogue validator;
- WonderLens AI dialogue quality improver;
- final independent reviewer.

Rules:

- Run at most three delegated/sub-agents in parallel. When a delegated agent
  finishes, collect its evidence and terminate or kill that finished agent
  before spawning a replacement.
- Validators must return concise evidence, file paths, transcript paths when
  applicable, and a verdict.
- Validators must not repair their own findings.
- Improvers must start from a concrete validator failure and rerun the failed
  validator after repair.
- No delegated agent may edit `.env`, credential JSON files, or shared files
  outside its assigned artifact path.
- No package may be accepted without independent source-intent auditor evidence.
- No final run may pass without final independent reviewer PASS evidence.

## Mandatory Ordering

1. Confirm autodesign starts clean or create a clean isolated worktree.
2. Inspect `GOAL.md`, `run.md`, `program.md`,
   `docs/activity_asset_generation_workflow.md`, and the source TSV.
3. Confirm the fullstack target worktree exists and is on
   `feat/activity-text-game`.
4. Confirm the fullstack main backend credential files exist without printing
   them.
5. Confirm WonderLens AI exists and is ready for runtime generation/load
   validation.
6. Start a fresh autodesign run with `asset_build=generate_and_curate` and
   `full_pass_pipeline=true`.
7. Run pre-package source-intent audits from the TSV source rows.
8. Generate text-only packages.
9. Validate package contracts and runtime AI instruction quality.
10. Run post-package source-intent audits.
11. Generate or curate PNG assets and validate asset outputs.
12. Validate full-pass asset bundle completeness with
    `scripts/validate_full_pass_asset_bundle.py`, then run image QA and repair
    image-owned failures.
13. Verify all runtime-facing `prod.md` files are marker-free.
14. Load packages into fullstack-demo from the required worktree and validate
    converted `step_instructions`.
15. Start the fullstack server from the required worktree and run live dialogue
    QA.
16. Generate/load WonderLens AI runtime artifacts and run WonderLens AI
    dialogue QA.
17. Route each failure to package text repair, image repair, fullstack follow-up,
    WonderLens AI follow-up, or product decision.
18. Re-run failed validators after repairs.
19. Run final independent review.
20. Run required checks.
21. Commit intended autodesign artifacts.
22. Stop servers started by this goal and report results.

## Fullstack Server Startup

Use exactly this worktree and branch for fullstack validation:

```bash
FULLSTACK_WORKTREE="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game"
FULLSTACK_MAIN="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo"
FULLSTACK_MAIN_BACKEND="$FULLSTACK_MAIN/backend"

test -d "$FULLSTACK_WORKTREE"
test "$(git -C "$FULLSTACK_WORKTREE" branch --show-current)" = "feat/activity-text-game"
test -f "$FULLSTACK_MAIN_BACKEND/.env"
test -f "$FULLSTACK_MAIN_BACKEND/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
```

Start the backend from the worktree backend, sourcing secrets only from the
main backend directory:

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

Start the frontend from the same worktree only when browser verification is
needed:

```bash
cd "$FULLSTACK_WORKTREE/frontend"
npm install
npm run dev -- --host 127.0.0.1 --port 5173
```

Back up mutable fullstack loading surfaces before loading generated packages:

```bash
FULLSTACK_BACKUP="/tmp/wl_full_pass_${RUN_ID}/fullstack_backup"
mkdir -p "$FULLSTACK_BACKUP"
rsync -a "$FULLSTACK_WORKTREE/backend/games/" "$FULLSTACK_BACKUP/backend_games/"
rsync -a "$FULLSTACK_WORKTREE/frontend/public/activity-assets/" "$FULLSTACK_BACKUP/activity_assets/"
```

Record the exact load/import or structural conversion command used. If the
branch cannot load autodesign packages without improving or rewriting content,
classify that as a fullstack consumer gap instead of masking it in package
prose.

## WonderLens AI Startup

Use:

```bash
WONDERLENS_AI_ROOT="/Users/pharrelly/codebase/gitlab/wonderlens-ai"
cd "$WONDERLENS_AI_ROOT"
test "$(git branch --show-current)" = "main"
test -f .env
test -f .elaborate-baton-480304-r8-a8a39bcb34f1.json
```

When a live WonderLens AI smoke is needed:

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

## API Rate-Limit Rule

Treat `429`, `RESOURCE_EXHAUSTED`, quota exceeded, `rate_limit`, and equivalent
provider throttles as retryable during image generation, hosted LLM calls,
fullstack live dialogue QA, WonderLens AI live dialogue QA, and runtime
conversion.

Do not stop the goal directly on the first rate-limit response. Record the
phase, activity ID or batch, command, timestamp, provider name if safe, and
sanitized error class. Wait at least 3 minutes before the first retry and use a
3/5/8-minute backoff for repeated throttles on the same request or batch. Retry
at least three times before declaring a blocker. Reduce concurrency or batch
size when safe. Do not print secrets, store secret-bearing request payloads, or
fabricate assets/transcripts/validation evidence to bypass throttling.

## Dialogue Quality Pass Gate

For both fullstack-demo and WonderLens AI, pass only when:

- source play frame, child role, device role, sequence, required child action,
  reference asset requirement, and background/context promise are preserved;
- converted runtime instructions remain comparable to the quality floor in
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/games/fluffy_expedition_dandelion.md`;
- each live beat has goal/action, tier or length constraint, emotion/tone,
  progress evidence, branch behavior, frame/source guardrail, screen/state
  expectation, and an example line;
- ideal, minimal, wrong, off-topic, help/confusion, silence, premature done,
  and unsupported-request inputs are covered for representative activities;
- repeated unproductive inputs force progress or graceful exit instead of
  looping forever;
- Cat5 synthesis preserves collected items and package-specific synthesis
  intent;
- no unsupported visual-inspection, hidden-state, screen-content, or sensing
  claims appear in transcripts;
- final recap names the correct concept and child action.

## Image Quality Pass Gate

Pass only when every accepted activity has:

- package-local 512x512 PNGs for all required manifest assets unless a larger
  variant is explicitly requested;
- 512x512 square illustrative source PNGs for subset and full-pass asset
  generation attempts, while final runtime variants stay manifest-driven;
- style alignment with `docs/activity_asset_generation_workflow.md`,
  `docs/asset_style_reference/wonderlens-activity-style.md`, and
  `docs/asset_style_reference/style-reference-flat-nordic.png`;
- Codex built-in imagegen provenance for generated illustrative source PNGs,
  with no SVG/vector/placeholder substitutes accepted as generated art;
- scene/dialogue alignment for each runtime beat;
- no baked app progress/control UI in PNGs; progress dots, round markers,
  response slots, rule strips, buttons, chips, picker slots, badges, and other
  runtime interface markers belong to the app;
- no cross-activity template reuse; unrelated activities cannot pass with the
  same cozy-room, blank-board, child-response, or child-on-rug scene structure;
- guided drawing/build-step scenes show the child action for that exact step
  rather than generic paper, pencil, lock, timer, camera, or placeholder cards;
- no duplicated selectable items/objects in background scenes when separate
  picker sprites, target/distractor cards, or collection items advance the
  activity;
- selectable item/object picker PNGs declared separately and built under
  package-local `assets/items/`, not mixed with beat-scene/background assets;
- no premature answer reveal in progressive evidence or partial-reveal flows;
  early beat images must preserve the source step sequence and reveal only what
  the current dialogue beat should show;
- duplicate picker objects or premature answer reveal are hard image-QA repair
  verdicts, not cosmetic notes;
- readable centered objects/items/characters/icons/badges/distractors at
  runtime size;
- no text, letters, numbers, labels, watermarks, contact sheets, multi-card
  sheets, borders, masks, or device chrome baked into generated assets;
- accepted source originals and metadata for reference-bound assets.

## Preconditions

Autodesign:

```bash
test -f GOAL.md
test -f run.md
test -f program.md
test -f docs/activity_asset_generation_workflow.md
test -f docs/asset_style_reference/wonderlens-activity-style.md
test -f docs/asset_style_reference/style-reference-flat-nordic.png
test -f docs/plans/2026-06-01-run-full-pass-agentic-pipeline.md
test -f goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md
test -f inputs/original_activity_concepts_2026-05-29.tsv
test -f inputs/source_activity_concepts.md
test -f scripts/build_activity_assets.py
test -f scripts/validate_asset_build_outputs.py
test -f scripts/validate_demo_package_contract.py
```

Fullstack:

```bash
FULLSTACK_WORKTREE="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game"
FULLSTACK_MAIN_BACKEND="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend"
test -d "$FULLSTACK_WORKTREE"
test "$(git -C "$FULLSTACK_WORKTREE" branch --show-current)" = "feat/activity-text-game"
test -f "$FULLSTACK_WORKTREE/backend/server.py"
test -f "$FULLSTACK_WORKTREE/frontend/package.json"
test -f "$FULLSTACK_MAIN_BACKEND/.env"
test -f "$FULLSTACK_MAIN_BACKEND/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
```

WonderLens AI:

```bash
WONDERLENS_AI_ROOT="/Users/pharrelly/codebase/gitlab/wonderlens-ai"
test -d "$WONDERLENS_AI_ROOT"
test -f "$WONDERLENS_AI_ROOT/scripts/generate_activity_runtime.py"
test -f "$WONDERLENS_AI_ROOT/app/main.py"
test -f "$WONDERLENS_AI_ROOT/.env"
test -f "$WONDERLENS_AI_ROOT/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
```

## Required Checks

Autodesign, replacing `<run_id>` with the generated run:

```bash
python3 scripts/validate_demo_package_contract.py runs/<run_id>/activity_packages
python3 scripts/build_activity_assets.py runs/<run_id> --mode generate_and_curate
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
python3 scripts/validate_asset_granularity.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
! rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md
git diff --check
```

Fullstack-demo from the required worktree after loading activities:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game
uv run pytest backend/tests/test_activity_text_game_api.py backend/tests/test_activity_text_game_definitions.py backend/tests/test_activity_text_game_cat3.py backend/tests/test_activity_text_game_turns.py -q
uv run python scripts/run_activity_text_smoke.py --base-url http://127.0.0.1:8000
cd frontend
npm test -- tests/activityAssets.test.js tests/useActivityTextSession.test.jsx tests/WonderLensDevice.test.jsx tests/ActivityGameApp.test.jsx
npm run build
```

WonderLens AI after runtime generation:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run python scripts/generate_activity_runtime.py --source <autodesign_run>/activity_packages --dest .artifacts/full-pass-agentic/activities --write --force --report-json .artifacts/full-pass-agentic/runtime-report.json
uv run pytest tests/unit/activity/test_activity_package_models.py tests/unit/activity/test_activity_package_loader.py tests/unit/activity/test_runtime_generator.py tests/unit/scripts/test_generate_activity_runtime.py -q
DIRECTIVE_PIPELINE_ENABLED=true uv run python tests/integration/live/test_activity_live_matrix.py --scenario all
```

If commands have moved, use the current equivalent command and record the
substitution and coverage delta.

## Final Completion Gate

Do not mark achieved until:

- generated run artifacts are present under `runs/<run_id>/`;
- source-intent, package-quality, image-quality, fullstack, WonderLens AI, and
  final-review evidence is recorded;
- every accepted package has no unresolved `intent_drift`;
- required assets validate or missing reference-bound assets are honestly
  blocked/degraded with product evidence;
- fullstack server validation used the required
  `feat/activity-text-game` worktree;
- fullstack and WonderLens AI dialogue QA pass or every failure has a recorded
  owner and explicit downstream/product decision;
- required checks pass or a blocker is documented;
- any API rate-limit blocker includes the sanitized retry log and resume point;
- no fullstack or WonderLens AI servers started by this goal remain running;
- no secret files or local credential artifacts are changed;
- intended autodesign artifacts are committed;
- downstream repo changes remain uncommitted unless the user explicitly
  expanded scope.

Final response must include:

- run path and run ID;
- source rows processed and package count;
- asset build status;
- source-intent verdict summary;
- fullstack branch/worktree used and server/check evidence;
- WonderLens AI runtime/check evidence;
- dialogue QA verdict summary;
- image QA verdict summary;
- repair-loop summary;
- final independent review verdict;
- checks run;
- remaining risks and commit hash.

## Goal Invocation

Use from the `wonderlens-activity-autodesign` repo or a clean autodesign
worktree:

```text
/goal Implement goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md. Execute the current workbook full pass from inputs/original_activity_concepts_2026-05-29.tsv with asset_build=generate_and_curate and full_pass_pipeline=true; generate illustrative assets with Codex built-in imagegen using docs/asset_style_reference/wonderlens-activity-style.md and docs/asset_style_reference/style-reference-flat-nordic.png; store picker item/object assets under package-local assets/items/; start fullstack validation only from /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game on branch feat/activity-text-game while sourcing live credentials only from /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend; use delegated agents for source intent, text package writing, image generation, fullstack dialogue QA, WonderLens AI dialogue QA, image QA, repair loops, and final independent review with at most three running in parallel and finished agents killed before replacements; if API rate limits occur, wait a few minutes and retry with backoff before declaring a blocker; stop only when the completion gate is satisfied or a blocker is documented.
```
