# Integration Owner Goal

## Mode

Re-runnable. Accepts `RUN_ID` and `ACTIVITY_ID` as parameters.

Use this file as the Codex goal-mode execution contract for validating a single
activity package in downstream consumer environments. Run it only after text
review and asset curation both pass for that activity.

## Objective

Load or convert `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>` in
fullstack-demo and WonderLens AI, compare runtime behavior against the package
contract, run dialogue QA, and route failures by owner. Do NOT edit package
text, assets, or metadata.

## Parameters

Replace these before each run:

```text
RUN_ID=<run_id>                # e.g. 20260611_093000_batch3
ACTIVITY_ID=<activity_id>      # e.g. vegetable_sort
```

## Source Documents

- `docs/full_pass_agentic_parallel_workflow.html` — dialogue QA strategies,
  failure classification, PM review handoff.
- `program.md` Phase 3 — runtime fidelity expectations.
- `docs/role_agent_prompting_guide.md` — stock integration owner prompt.
- `docs/run_captain_daily_workflow.md` — run branch and handoff context.

## Consumer Targets

- Fullstack-demo worktree:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game`
- Fullstack-demo credential source:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend`
- WonderLens AI repo:
  `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

## Allowed Files

- `runs/<RUN_ID>/review_status/<ACTIVITY_ID>.yaml`
- `runs/<RUN_ID>/downstream_reports/**`
- Downstream test logs or fixtures when the corresponding repo is part of the
  task.

## Forbidden Files

- Package text, YAML, and asset files in
  `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/`
- Canonical rules
- Unrelated activity packages

## Hard Constraints

- Do not edit package content to make downstream checks pass.
- Do not edit, print, copy into the repo, or commit `.env`, credential JSON
  files, tokens, or provider secrets.
- Do not leave servers running at completion.
- Fullstack validation must use the `feat/activity-text-game` worktree.
- Route failures to package, image, fullstack-demo, WonderLens AI, or product
  capability owners. Do not silently fix content across ownership boundaries.
- Retry transient provider throttles (`429`, `RESOURCE_EXHAUSTED`, rate limits)
  with a few-minute backoff before classifying as blocked.
- Do not push unless explicitly asked.

## Required Scope

1. Confirm text and asset review statuses are `pass` in
   `review_status/<ACTIVITY_ID>.yaml`.
2. Verify `prod.md` is free of raw `RESOLVED BLOCKER` markers.
3. Load or convert the package in fullstack-demo from the required worktree.
4. Confirm converted `step_instructions` preserve every machine-convertible
   `Runtime AI instruction`.
5. Start the fullstack server and run live dialogue QA with at least five
   child-input strategies:
   - expected_answer
   - wrong_unproductive_answer
   - help_confusion
   - silence_no_response
   - premature_done
6. Load or convert the package in WonderLens AI, generate runtime artifacts,
   and run comparable dialogue QA.
7. Write downstream evidence reports:
   - `runs/<RUN_ID>/downstream_reports/fullstack_demo/dialogue_qa_report.json`
   - `runs/<RUN_ID>/downstream_reports/wonderlens_ai/dialogue_qa_report.json`
8. Classify each failure by owner.
9. Update `review_status/<ACTIVITY_ID>.yaml` `runtime_validation` and
   `pm_review` blocks with evidence, verdict, and next_owner.
10. Stop any servers started by this goal.

## Required Checks

```bash
RUN_ID="<run_id>"
ACTIVITY_ID="<activity_id>"

# Marker-free precondition
! rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" \
  runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/prod.md

# Review status preconditions
grep 'pass' runs/${RUN_ID}/review_status/${ACTIVITY_ID}.yaml

git diff --check
```

## Dialogue Quality Pass Gate

Pass only when:

- Source play frame, child role, device role, sequence, required child action,
  and reference asset requirement are preserved.
- Converted runtime instructions remain comparable to the quality floor in
  `fluffy_expedition_dandelion.md`.
- Each live beat has goal/action, tier/length constraint, emotion/tone,
  progress evidence, branch behavior, frame guardrail, screen/state expectation,
  and an example line.
- All five child-input strategies return beat-specific responses, not generic
  fallbacks.
- Repeated unproductive inputs force progress or graceful exit.
- Cat5 synthesis preserves collected items and package-specific synthesis intent.
- No unsupported visual, hidden-state, or sensing claims appear in transcripts.
- Final recap names the correct concept and child action.

## Completion Gate

The goal is complete when:

- Downstream dialogue QA evidence exists for both consumers.
- Every failure has a classified owner.
- No servers started by this goal remain running.
- `review_status/<ACTIVITY_ID>.yaml` `runtime_validation` and `pm_review`
  blocks are updated.
- Intended evidence files are committed.

## Goal Invocation

```text
/goal Execute goals/integration-owner-goal.md end to end with RUN_ID=<run_id> ACTIVITY_ID=<activity_id>.
```
