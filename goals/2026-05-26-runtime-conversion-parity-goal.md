# Runtime Conversion And Parity Goal

## Mode

Plan-backed.

## Objective

Implement the runtime conversion and parity plan so WonderLens activity
packages can become executable in both `wonderlens-ai` and the fullstack demo
through a deterministic conversion layer, not by placing raw package markdown
directly into runtime prompts.

## Design Source

- Plan: `docs/plans/2026-05-26-runtime-conversion-parity.md`
- Existing plan to incorporate:
  `/Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-05-15-activity-runtime-yaml-generator.md`
- Target repos:
  `/Users/pharrelly/codebase/gitlab/wonderlens-ai` and
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo`

The linked plan is authoritative for design rationale and implementation
context. This goal is authoritative for constraints, required checks,
credential handling, and completion. If the two conflict, stop and document the
conflict before changing behavior.

## Hard Constraints

- Do not rerun full activity generation for this goal.
- Do not use an LLM in the v1 converter path or deterministic tests.
- Do not feed raw `prod.md` bodies directly into fullstack-demo prompts.
- Do not change fullstack-demo runtime code in Phase 1 or Phase 2; export the
  existing `backend/games/*.md` frontmatter shape instead.
- Do not mark Cat3 or UI-heavy mechanics executable unless matching runtime/UI
  support is implemented and tested.
- Do not silently map unsupported mechanics into unrelated fullstack mechanics.
- Do not claim unavailable assets are visible; emit explicit fallbacks.
- Do not edit, print, copy, or commit `.env`, credential JSON files, provider
  tokens, API keys, or production data.

## Required Scope

- Implement or update the `wonderlens-ai` runtime YAML generator from the
  existing 2026-05-15 plan.
- Produce canonical runtime data that validates in `wonderlens-ai`.
- Add quality gates for generic leakage, weak `step_instructions`, missing
  branch policy, unsupported mechanics, and unsupported asset claims.
- Add a fullstack-demo exporter that emits parseable frontmatter for current
  Cat1/Cat5 primitives.
- Add deterministic schema, golden fixture, quality-gate, adapter, and parser
  checks.
- Run live server/API parity after deterministic checks pass, or document the
  credential/provider blocker.

## Execution Rules

- Work in the target repo that owns each change; check all repo worktrees
  before editing.
- Keep fullstack-demo as the baseline unless generated fixture files are
  intentionally reviewed and committed.
- Treat Phase 3 runtime/UI extensions as out of scope unless explicitly
  continued after Phase 1 and Phase 2 pass.
- Preserve unrelated user changes and commit only intended files.
- Use conventional commits in each touched repo.

## Mandatory Ordering

1. Implement deterministic converter and schema/golden tests first.
2. Add consumer adapters only after canonical runtime output validates.
3. Run fullstack parser checks before live server comparison.
4. Run live E2E parity only after deterministic checks pass.
5. Start Phase 3 only after Phase 1 and Phase 2 have a clear pass/fail report.

## Live Provider Credential Rule

Live API parity requires local credentials. Load them without printing secret
values.

For `wonderlens-ai`:

```bash
MAIN_REPO_ROOT="/Users/pharrelly/codebase/gitlab/wonderlens-ai"
set -a
source "$MAIN_REPO_ROOT/.env"
set +a
export GOOGLE_APPLICATION_CREDENTIALS="$(ls "$MAIN_REPO_ROOT"/.elaborate-baton-*.json | head -n 1)"
```

For fullstack-demo, verify the current backend env location before running:

```bash
DEMO_BACKEND_ROOT="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend"
set -a
source "$DEMO_BACKEND_ROOT/.env"
set +a
export GOOGLE_APPLICATION_CREDENTIALS="$(ls "$DEMO_BACKEND_ROOT"/.elaborate-baton-*.json | head -n 1)"
```

If either `.env` or credential JSON is unavailable, skip live parity, record the
missing prerequisite, and still complete deterministic validation.

## Preconditions

```bash
test -d /Users/pharrelly/codebase/gitlab/wonderlens-ai
test -d /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
test -f /Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-05-15-activity-runtime-yaml-generator.md
test -d /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities
test -d /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/runs/20260521_163621_workbook_review_packet_full/activity_packages
git -C /Users/pharrelly/codebase/github/wonderlens-activity-autodesign status --short
git -C /Users/pharrelly/codebase/gitlab/wonderlens-ai status --short
git -C /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo status --short
```

## Success Criteria

- Canonical runtime YAML validates with `wonderlens-ai` `ActivityRuntime`.
- Generated packages load through `load_activity_package(...)`.
- Executable Cat1/Cat5 packages adapt through `game_definition_from_package(...)`.
- Fullstack-demo exports parse through `backend.game_parser.parse_game_file`.
- Golden fixtures cover easy Cat1, easy Cat5, Cat5 runtime judgment, one
  adapted mechanic, and one unsupported/hard mechanic.
- Leakage strings and `RESOLVED BLOCKER` fail conversion.
- Branch policy and no-response/unexpected behavior are preserved or compacted
  into tested runtime constraints.
- Asset claims have supported bindings or explicit no-display fallbacks.
- Unsupported Cat3/UI-heavy activities report `requires_runtime_extension`.
- E2E parity report exists, or live parity is explicitly blocked by missing
  credentials/provider availability.

## Required Checks

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git diff --check
```

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run pytest tests/unit/activity/test_runtime_generator.py -v
uv run ruff check app/modules/activity/packages/runtime_generator.py scripts/generate_activity_runtime.py tests/unit/activity/test_runtime_generator.py
uv run ty check app/modules/activity/packages
```

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities --activity time_machine_dinosaur --check
uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities --activity fluffy_expedition_dandelion --check
uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities --activity concept_phoneme_hunt_collect --check
```

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
uv run python - <<'PY'
from pathlib import Path
from backend.game_parser import parse_game_file
for path in sorted(Path("backend/games").glob("*.md")):
    if path.read_text(encoding="utf-8").startswith("---"):
        parse_game_file(path)
print("parsed fullstack game frontmatter")
PY
```

Live parity commands must be documented with exact server URLs, request
payloads, response artifact paths, and result summary when run.

## Final Completion Gate

Do not mark complete until deterministic Phase 1 and Phase 2 checks pass,
unsupported mechanics are reported honestly, live parity is either run or
blocked with evidence, intended changes are committed in each touched repo, and
the final response lists changed files, checks, parity status, fixture/activity
coverage, residual risks, and commit hashes.

## Goal Invocation

```text
/goal Implement goals/2026-05-26-runtime-conversion-parity-goal.md. Stop only when its completion gate is satisfied or a blocker is documented.
```
