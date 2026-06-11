# Role Agent Prompting Guide

Use this guide with `docs/full_pass_agentic_parallel_workflow.html` when several
people run coding agents against the same full-pass run branch.

Root `GOAL.md`, `run.md`, and `program.md` remain the canonical generation
contract. This file lists the scoped goal-file invocations for each role and the
role-specific operational rules.

## Core Rule

Every agent session uses a scoped goal file. Role-specific rules (file scope,
validators, completion criteria) live in the goal file, not in the prompt.

```text
/goal Execute goals/<goal-file>.md end to end with RUN_ID=<run_id> ACTIVITY_ID=<activity_id>.
```

Avoid prompts such as "fix whatever fails" or "make the activity pass." Those
prompts erase ownership boundaries and make review evidence hard to trust.

## Branch Rules

- Branch from the latest run integration branch, such as
  `run/202606xx-agentic-pass`.
- Use one contributor branch per role slice, such as
  `alice/text-activities-01-05` or `bob/assets-activity-vegetable-sort`.
- Do not let two agents edit the same package or manifest at the same time.
- Sync before PR with `git fetch origin`, rebase onto the run branch, then run
  `git diff --check`.
- The run captain merges text PRs before asset PRs when asset lists depend on
  final runtime steps.

## Run Captain

Use this when creating the baseline. The baseline goal runs once per run.

```text
/goal Execute goals/baseline-text-packages-goal.md end to end.
```

The goal file generates text-only packages for the active assignment queue,
creates review_status files, runs the 10-dimension rubric and independent
reviewer pass, logs results, and generates the review dashboard. After the
baseline is committed, the captain delegates per-activity work via the role goal
files below.

## Text Reviewer

Use this when reviewing and repairing one activity package. Re-runnable per
activity.

```text
/goal Execute goals/text-reviewer-goal.md end to end with RUN_ID=<run_id> ACTIVITY_ID=<activity_id>.
```

The goal file owns the rubric (program.md Phase 3), the allowed/forbidden file
lists, the required validators, the review_status update rules, and the
completion gate. The text reviewer must not edit asset files or downstream repos.

## Asset Curator

Use this when generating or curating assets for one activity package.
Re-runnable per activity. Run only after the text reviewer's PR is merged for
that activity.

```text
/goal Execute goals/asset-curator-goal.md end to end with RUN_ID=<run_id> ACTIVITY_ID=<activity_id>.
```

The goal file owns the style contract (docs/activity_asset_generation_workflow.md),
the file scope, the builder and validator commands, the reference-bound asset
provenance rules, the image QA rules, and the completion gate. The asset curator
must not edit package text, mechanics, or downstream repos.

## Integration Owner

Use this when validating one activity package in downstream consumers. Re-runnable
per activity. Run only after text review and asset curation both pass.

```text
/goal Execute goals/integration-owner-goal.md end to end with RUN_ID=<run_id> ACTIVITY_ID=<activity_id>.
```

The goal file owns the downstream consumer targets, the dialogue QA strategies,
the failure-classification rules, the required checks, and the completion gate.
The integration owner must not edit package text, assets, or metadata. Failures
are routed to the owning role, not silently fixed.

## Status Rules

Each activity should have:

```text
runs/<run_id>/review_status/<activity_id>.yaml
```

The baseline goal creates the initial file from `runs/_templates/review_status.yaml`.
Each role updates only its own lane:

| Lane | Role owner |
|---|---|
| `text_review` | Text Reviewer |
| `asset_review` | Asset Curator |
| `contract_validation` | Run Captain |
| `runtime_validation` | Integration Owner |
| `pm_review` | Integration Owner (after runtime evidence) |

Allowed statuses: `pending`, `pass`, `needs_fix`, `blocked`, `not_applicable`.

Every update must record the reviewer name, evidence paths, findings, and
`next_owner`.

## Stop Conditions

Ask the run captain before continuing when:

- A prompt would touch secrets, credentials, or machine-specific configuration.
- A reference-bound asset lacks an approved source.
- An activity needs an unsupported mechanic or UI capability.
- Multiple contributors need to edit the same file.
- A validator fails for a reason outside the role scope.
- Downstream consumer behavior contradicts the package contract.
- A goal-file precheck fails (missing docs, missing run directory, unresolved
  review_status dependency).
