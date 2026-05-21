# Goal Planning

Use this reference before a full workbook-to-review-packet run or any multi-step patch/export workflow that should be resumable.

## Purpose

Create a concise goal-mode execution contract that makes the run inspectable and resumable. The goal file is not the detailed implementation plan; it points to the repo docs and records the specific workbook, target run, scope, outputs, and checks.

## Steps

1. If implementation details are not already written, create a detailed plan under `docs/plans/YYYY-MM-DD-<slug>.md`.
2. Use the `goal-file-creator` skill to create `goals/YYYY-MM-DD-<slug>-goal.md`.
3. Keep root `GOAL.md` as the generic run contract unless the user explicitly asks to update the global goal behavior.
4. Record precedence:
   - user request and supplied workbook path;
   - run-specific goal file;
   - detailed plan under `docs/plans/`;
   - current repo docs such as `program.md`, `run.md`, `review_dashboard.md`, and root `GOAL.md`.
5. Include the execution mode:
   - fresh full rerun from workbook;
   - existing run patch;
   - audit-only;
   - export-only.
6. Include concrete success criteria for:
   - source concept extraction;
   - generated or patched packages;
   - full-pass source-intent audit;
   - integrated assets and standalone HTML exports when in scope;
   - `review.html`;
   - manifest/review notes/handoff updates;
   - commits and PR if requested.

## Required Goal Fields

The goal must include:

- workbook path;
- target run label or target existing `runs/<run_id>`;
- activity scope;
- whether full rerun or patch is allowed;
- product-contract override status;
- source-intent audit requirement;
- export requirement;
- validation commands;
- hard constraints against hand-editing generated HTML as source of truth.

## Execution

If goal mode is available and the user requested end-to-end execution, start it from the run-specific goal file. If not, execute the goal file manually and state that goal mode was unavailable.
