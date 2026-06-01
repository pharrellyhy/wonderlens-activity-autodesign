# Full Pass Agentic Pipeline Goal

## Mode

Plan-backed.

Use this file as the Codex goal-mode execution contract.

## Objective

Implement the full-pass agentic generation pipeline contract in autodesign so a
future larger/full activity pass can generate activity packages and all required
image assets, then validate that fullstack-demo loads and executes those
packages directly and that WonderLens AI generates/loads equivalent runtime
artifacts and exercises equivalent runtime dialogue without manual content
improvement.

This goal implements workflow documents, validation expectations, and any small
supporting templates/checks needed to make the contract executable. It does not
run the full activity generation pass.

## Design Source

Source plan:

- `docs/plans/2026-06-01-full-pass-agentic-pipeline.md`

Related context:

- `GOAL.md`
- `run.md`
- `program.md`
- `docs/activity_asset_generation_workflow.md`
- `docs/plans/2026-05-29-source-intent-pilot-validation.md`
- `docs/plans/2026-05-28-generate-and-curate-asset-pipeline.md`
- `inputs/original_activity_concepts_2026-05-29.tsv`
- `inputs/source_activity_concepts.md`
- `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo`
- `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

The plan is authoritative for design rationale, current evidence, agent roles,
validation strategy, and workflow detail. This goal is authoritative for hard
constraints, required scope, delegated-agent rules, credential handling,
required checks, and completion. If the plan and goal conflict, stop and
document the conflict before changing behavior.

## Hard Constraints

- Preserve `inputs/original_activity_concepts_2026-05-29.tsv` as the source
  intent baseline unless a newer committed workbook export is explicitly
  selected.
- Treat `inputs/source_activity_concepts.md` as a normalized helper. If it
  disagrees with the workbook row, the workbook row wins unless a product
  decision is recorded.
- Do not execute a larger/full activity generation pass in this goal.
- Do not regenerate all activity assets in this goal.
- Do not make fullstack-demo a content-improvement step. It is the direct
  loader/executor for autodesign packages.
- Do not make WonderLens AI a content-improvement step. It is a direct runtime
  consumer for autodesign packages.
- Do not hide activity drift by rewriting package prose to fit generated
  images, fullstack behavior, or WonderLens AI behavior.
- Keep unsupported/degraded mechanics honest; do not make them playable by
  changing the child action.
- Keep `asset_build=generate_and_curate` as the expected full-pass asset mode.
- Do not use generated approximations for reference-bound factual assets.
- Do not edit, print, copy, or commit `.env`, credential JSON files, tokens, or
  provider secrets.
- Do not leave backend/frontend servers running at completion.
- Do not push unless explicitly asked.

## Required Scope

Update the autodesign workflow so a future full pass has an explicit:

- master-orchestrated pipeline;
- source-intent auditor gate before and after package writing;
- text-only activity package writer role;
- image-only scene/object/item asset generation role;
- package/import contract validator role;
- live fullstack dialogue quality validator role;
- WonderLens AI dialogue quality validator role;
- marker-free runtime-facing `prod.md` precondition before fullstack-demo and
  WonderLens AI dialogue quality comparison;
- image quality validator role;
- dialogue quality improvement loop;
- WonderLens AI dialogue quality improvement loop;
- image quality improvement loop;
- final independent review gate.

Expected ownership areas:

- `GOAL.md`
- `run.md`
- `program.md`
- `docs/activity_asset_generation_workflow.md`
- supporting plan/goal docs or validation templates if needed
- README/status docs only when workflow behavior changes materially

Do not edit fullstack-demo or WonderLens AI in this goal unless the user
explicitly expands scope. If consumer runtime guardrails are required, document
the needed follow-up with evidence.

## Delegated Agent Rule

The user explicitly requested delegated/sub-agent rules for this pipeline.

During this goal execution, use delegated agents when they can work on disjoint
review or exploration tasks, such as:

- auditing current `GOAL.md`, `run.md`, and `program.md` for missing full-pass
  gates;
- inspecting fullstack importer/runtime expectations without editing
  fullstack;
- inspecting WonderLens AI runtime-generation/dialogue expectations without
  editing WonderLens AI;
- reviewing the image asset workflow against current fullstack style prompts;
- independently reviewing the final autodesign contract changes.

Keep all file edits, credentials, server lifecycle, blocking decisions, commits,
and final user reporting local to the main agent.

For the future full pass, encode these delegated roles in the workflow:

- source-intent auditor;
- activity package writer, text only;
- scene/object/item asset generator, image only;
- package/import contract validator;
- live dialogue quality validator;
- WonderLens AI dialogue quality validator;
- image quality validator;
- dialogue quality improver;
- WonderLens AI dialogue quality improver;
- image quality improver;
- final independent reviewer.

Every delegated review must return concise evidence and a verdict. Do not
accept a generated package without independent source-intent auditor evidence.

## Execution Rules

- Work in an isolated autodesign feature worktree.
- Inspect current `GOAL.md`, `run.md`, `program.md`, and
  `docs/activity_asset_generation_workflow.md` before editing.
- Prefer strengthening existing workflow sections over adding a parallel
  workflow that future agents might miss.
- Keep edits focused on executable generation, validation, and repair
  contracts.
- If adding scripts or structured checklists, use existing repo patterns and
  add focused tests.
- Record fullstack and WonderLens AI as direct consumers and validation targets,
  not authoring fallbacks.
- Stop and document a conflict if current docs disagree on source ownership,
  fullstack/WonderLens AI ownership, asset build mode, or live credential
  handling.

## Mandatory Ordering

1. Confirm the isolated worktree starts clean.
2. Inspect current workflow documents and prior pilot/asset plans.
3. Update the autodesign workflow contract for master/subagent orchestration.
4. Add source-intent, consumer/import, live dialogue, image QA, and repair-loop
   gates where they belong in the workflow.
5. Add delegated/subagent rules explicitly.
6. Run required checks.
7. Update plan/goal indexes if the implementation scope changes their status.
8. Commit the intended autodesign changes.

## Live Provider Credential Rule

This goal should not require live provider calls unless the executor chooses to
smoke-test wording against fullstack or WonderLens AI. If a live fullstack smoke
is necessary, use a temp DB and source credentials from the authorized
fullstack main backend without printing values:

```bash
FULLSTACK_MAIN_BACKEND="/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend"
set -a
source "$FULLSTACK_MAIN_BACKEND/.env"
set +a
export GOOGLE_APPLICATION_CREDENTIALS="$FULLSTACK_MAIN_BACKEND/.elaborate-baton-480304-r8-a8a39bcb34f1.json"
export DB_PATH="/tmp/wl_activity_live_audit.sqlite3"
```

If the target port is busy, use a separate audit port and stop only the server
started for this goal. Never print or commit secret values.

If a WonderLens AI smoke is necessary, use that repo's documented local runtime
or test harness and source only the explicitly required credentials. Record the
command and sanitized output, not secret values.

## Preconditions

Autodesign files:

```bash
test -f GOAL.md
test -f run.md
test -f program.md
test -f docs/activity_asset_generation_workflow.md
test -f docs/plans/2026-06-01-full-pass-agentic-pipeline.md
test -f goals/2026-06-01-full-pass-agentic-pipeline-goal.md
test -f inputs/original_activity_concepts_2026-05-29.tsv
test -f inputs/source_activity_concepts.md
```

Fullstack reference path:

```bash
test -d /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
```

WonderLens AI reference path:

```bash
test -d /Users/pharrelly/codebase/gitlab/wonderlens-ai
```

## Success Criteria

- `GOAL.md`, `run.md`, and `program.md` define the full-pass master/subagent
  pipeline clearly enough for a fresh goal-mode run.
- The workflow requires source-intent auditor evidence before package
  acceptance.
- The workflow separates text package writing from image asset generation.
- The workflow requires package/import validation before live dialogue QA.
- The workflow requires live dialogue QA with multiple child-input strategies,
  not only static term checks.
- The workflow requires WonderLens AI dialogue QA and repair/escalation, not
  only WonderLens AI conversion/load validation.
- The workflow requires image QA for style, asset role, scene/dialogue
  alignment, crop safety, reference fidelity, and no-text/no-label constraints.
- The workflow includes dialogue and image repair loops with ownership rules.
- Fullstack-demo is documented as loader/executor, not content improver.
- WonderLens AI is documented as a runtime consumer, not content improver.
- Delegated/subagent rules are explicit and bounded.
- Any downstream fullstack or WonderLens AI runtime guardrail gaps discovered
  during inspection are recorded as follow-up scope instead of hidden in
  autodesign package prose.

## Required Checks

Always run:

```bash
git diff --check
rg -n "source-intent auditor|Source-intent auditor|dialogue quality|WonderLens AI dialogue|image quality|asset_build=generate_and_curate|fullstack|WonderLens AI" GOAL.md run.md program.md docs goals
```

If scripts, schemas, or tests are changed, run the nearest focused test or
validator before completion and record the command.

If a live fullstack or WonderLens AI smoke is run, save only sanitized
transcripts and stop any audit server before final reporting.

## Final Completion Gate

Before marking this goal complete:

- intended autodesign changes are committed;
- required checks pass;
- changed files are limited to the planned workflow/validation scope;
- the final report names any downstream fullstack or WonderLens AI follow-up
  risk;
- no servers started by this goal are still running;
- no secret files or generated credential artifacts are changed.

## Goal Invocation

Use:

```text
/goal Implement goals/2026-06-01-full-pass-agentic-pipeline-goal.md. Stop only when its completion gate is satisfied or a blocker is documented.
```
