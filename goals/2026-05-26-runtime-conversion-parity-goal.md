# Runtime Conversion And Parity Goal

## Mode

Plan-backed.

## Objective

Implement the runtime conversion and parity plan so WonderLens activity packages
can be converted into executable runtime data for both `wonderlens-ai` and the
fullstack demo without feeding raw package markdown directly into prompts.

The implementation must deliver:

- a deterministic package-to-runtime converter;
- canonical runtime YAML that validates in `wonderlens-ai`;
- a fullstack-demo markdown/frontmatter exporter that targets the existing
  parser shape without changing fullstack runtime code in Phase 1 or Phase 2;
- deterministic schema, golden fixture, quality-gate, and adapter tests;
- live server/API parity validation after deterministic checks pass, when local
  credentials are available;
- honest `requires_runtime_extension` output for unsupported Cat3 or UI-heavy
  mechanics.

## Design Source

Authoritative implementation context:

- `docs/plans/2026-05-26-runtime-conversion-parity.md`

Existing plan to incorporate, not duplicate:

- `/Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-05-15-activity-runtime-yaml-generator.md`

Consumer repos:

- `/Users/pharrelly/codebase/gitlab/wonderlens-ai`
- `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo`

If this goal and the source plan conflict, stop and document the conflict
before changing behavior. The plan is authoritative for design rationale and
implementation context. This goal is authoritative for constraints, required
checks, credential handling, and completion.

## Hard Constraints

- Do not rerun full activity generation as part of this goal.
- Do not feed raw `prod.md` bodies directly into runtime prompts.
- Do not use an LLM in the v1 converter request path or deterministic tests.
- Do not change fullstack-demo runtime code in Phase 1 or Phase 2; emit the
  existing `backend/games/*.md` frontmatter shape instead.
- Do not mark Cat3, coloring, sorting, word reveal, tournament, or other
  unsupported UI-heavy activities executable unless matching runtime/UI support
  is actually implemented and tested.
- Do not silently map unsupported mechanics into unrelated fullstack mechanics.
- Do not claim unavailable assets are visible; emit explicit fallbacks.
- Do not edit, print, copy, or commit `.env`, credential JSON files, provider
  tokens, API keys, or production data.
- Do not include unrelated user changes in commits.

## Required Scope

Phase 1:

- Update or implement the `wonderlens-ai` runtime YAML generator from the
  existing 2026-05-15 plan.
- Add deterministic parsing for package metadata, step instructions, branch
  policy, asset/fallback guidance, and Cat1/Cat5 support boundaries.
- Add leakage rejection and quality warnings.
- Add `requires_runtime_extension` classification.
- Add golden fixtures for representative easy, judgment-heavy, adapted, and
  unsupported activities.

Phase 2:

- Add a consumer adapter for `wonderlens-ai` `runtime.yaml`.
- Add a fullstack-demo exporter that emits parseable markdown frontmatter for
  current Cat1/Cat5 primitives.
- Validate generated fullstack files through the existing parser.
- Keep generated demo activities either in a reviewed branch or a temporary
  export directory until the user chooses what to commit to fullstack-demo.

Phase 3:

- Do not implement broad UI extensions unless explicitly continuing into this
  phase.
- If continuing, scope extensions activity-by-activity and add focused widget,
  state, and browser checks.

Parity:

- Add or run an E2E parity harness after deterministic tests pass.
- Compare fullstack-demo and `wonderlens-ai` response quality on equivalent
  activity instructions and fixed turn sequences.
- Treat live parity as release validation, not as a replacement for
  deterministic tests.

## Mandatory Ordering

1. Implement deterministic converter and schema/golden tests first.
2. Add consumer adapters only after canonical runtime output validates.
3. Run fullstack parser checks before any live server comparison.
4. Run live E2E parity only after deterministic checks pass.
5. Do not start Phase 3 runtime/UI extension work until Phase 1 and Phase 2
   have a clear pass/fail report.

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

If either `.env` or credential JSON is unavailable, skip live parity, mark it
blocked with the missing prerequisite, and still complete deterministic checks.

## Preconditions

Confirm the key repos and source plan exist:

```bash
test -d /Users/pharrelly/codebase/gitlab/wonderlens-ai
test -d /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
test -f /Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-05-15-activity-runtime-yaml-generator.md
test -d /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities
test -d /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/runs/20260521_163621_workbook_review_packet_full/activity_packages
```

Check worktree state in every repo before editing:

```bash
git -C /Users/pharrelly/codebase/github/wonderlens-activity-autodesign status --short
git -C /Users/pharrelly/codebase/gitlab/wonderlens-ai status --short
git -C /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo status --short
```

## Success Criteria

- Canonical runtime YAML validates with `wonderlens-ai` `ActivityRuntime`.
- Generated packages load through `load_activity_package(...)`.
- Executable Cat1/Cat5 packages adapt through `game_definition_from_package(...)`.
- Fullstack-demo exports parse through `backend.game_parser.parse_game_file`.
- Golden fixtures cover `time_machine_dinosaur`,
  `fluffy_expedition_dandelion`, `concept_phoneme_hunt_collect`, at least one
  adapted mechanic, and one unsupported/hard mechanic.
- Quality gates reject known generic leakage strings and `RESOLVED BLOCKER`.
- Branch policies are preserved structurally or compacted into tested runtime
  constraints without dropping unexpected/no-response behavior.
- Asset claims have supported bindings or explicit no-display fallbacks.
- Unsupported Cat3/UI-heavy activities produce explicit
  `requires_runtime_extension` reasons.
- E2E parity report exists for the representative activity set, or live parity
  is explicitly blocked by missing credentials/provider availability.

## Required Checks

Autodesign doc/checkpoint:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git diff --check
```

`wonderlens-ai` deterministic checks:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run pytest tests/unit/activity/test_runtime_generator.py -v
uv run ruff check app/modules/activity/packages/runtime_generator.py scripts/generate_activity_runtime.py tests/unit/activity/test_runtime_generator.py
uv run ty check app/modules/activity/packages
```

Representative converter checks:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities --activity time_machine_dinosaur --check
uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities --activity fluffy_expedition_dandelion --check
uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities --activity concept_phoneme_hunt_collect --check
```

Fullstack parser check:

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
payloads, and response artifact paths when they are run.

## Final Completion Gate

Do not mark complete until:

- Phase 1 and Phase 2 deterministic tests pass;
- generated runtime/export artifacts are stable and reviewable;
- all unsupported mechanics are reported honestly;
- live parity is run and summarized, or blocked by a documented credential or
  provider prerequisite;
- no secrets or unrelated changes are staged;
- intended changes in each touched repo are committed with conventional commit
  messages;
- the final response lists changed files, checks run, parity status, generated
  fixture/activity coverage, residual risks, and commit hashes.

## Goal Invocation

```text
/goal Implement goals/2026-05-26-runtime-conversion-parity-goal.md. Stop only when its completion gate is satisfied or a blocker is documented.
```
