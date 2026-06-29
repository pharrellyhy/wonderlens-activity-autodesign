# Goal Status Index

> **Last checked:** 2026-06-24

## Status Definitions

- `Planned`: ready for future execution, not started.
- `Active`: currently being executed.
- `Completed`: completion gate passed and intended changes are committed.
- `Blocked`: execution could not complete; notes include the shortest useful reason.
- `Superseded`: replaced by a newer goal.

## Maintenance

Add new plan-backed goals to this index when they are created. When a goal run
completes successfully, mark it `Completed`. When execution stops at a real
blocker, mark it `Blocked` and include a brief reason.

This index starts with the plan-goal workflow added on 2026-05-26. Older goal
files remain under `goals/` and are not backfilled here.

## Index

| Goal | Status | Notes |
|---|---|---|
| [2026-06-24-skip-intro-rules-only-packages-goal.md](2026-06-24-skip-intro-rules-only-packages-goal.md) | Active | Removes separate intro hooks from four runtime-verified packages while keeping the first action prompt in Round/Collect 1. |
| [2026-06-24-four-package-runtime-verification-authoring-goal.md](2026-06-24-four-package-runtime-verification-authoring-goal.md) | Active | Plan-backed producer goal for four package verification updates without display-contract dependency. |
| [2026-06-23-activity-display-contract-v1-goal.md](2026-06-23-activity-display-contract-v1-goal.md) | Completed | Completion gate passed for producer-side display contract schema/validator/tests, current-twelve and run-local backfill, docs updates, and focused validation. |
| [2026-06-08-gemini-asset-quality-candidates-goal.md](2026-06-08-gemini-asset-quality-candidates-goal.md) | Planned | Implements multi-candidate Gemini generation, style-reference prompting, explicit candidate acceptance, and live smoke validation. |
| [2026-06-08-team-readiness-and-gemini-assets-goal.md](2026-06-08-team-readiness-and-gemini-assets-goal.md) | Completed | Completion gate passed for onboarding, review-status template, Gemini source provider, dependency setup, focused tests, static checks, and live smoke. |
| [2026-06-05-entity-compatibility-axis-parameterization-contract-goal.md](2026-06-05-entity-compatibility-axis-parameterization-contract-goal.md) | Completed | Completion gate passed for explicit entity compatibility, parameterization-mode enforcement, ambiguous agnostic package failures, review-dashboard verdicts, current-twelve reclassification, docs, fixtures, and focused checks. |
| [2026-06-05-entity-parameterized-package-authoring-goal.md](2026-06-05-entity-parameterized-package-authoring-goal.md) | Completed | Implemented producer-side package parameterization metadata, authoring-agent mode decision docs, review-dashboard integrity verdicts, validators, fixtures, current-twelve classification, and downstream runtime contract documentation. |
| [2026-06-01-run-full-pass-agentic-pipeline-goal.md](2026-06-01-run-full-pass-agentic-pipeline-goal.md) | Planned | Executes the current workbook full pass with `asset_build=generate_and_curate`, fullstack validation from the `feat/activity-text-game` worktree, WonderLens AI dialogue validation, image QA, repair loops, and final review. |
| [2026-06-01-full-pass-agentic-pipeline-goal.md](2026-06-01-full-pass-agentic-pipeline-goal.md) | Completed | Encoded the master/subagent full-pass generation workflow, source-intent and consumer/import gates, fullstack/WonderLens AI dialogue QA, image QA, repair loops, and final review contract before scaling generation. |
| [2026-05-29-source-intent-pilot-validation-goal.md](2026-05-29-source-intent-pilot-validation-goal.md) | Completed | Seven-row pilot passed source-intent, runtime-instruction, PNG asset, fullstack import, and WonderLens AI runtime validation; Guided Drawing and Plant Parts remain honestly gated. |
| [2026-05-28-e2e-subset-runtime-validation-goal.md](2026-05-28-e2e-subset-runtime-validation-goal.md) | Completed | Fresh subset/autodesign assets, fullstack import/play/gate behavior, fullstack runtime-beat conversion, and WonderLens AI runtime conversion/load/asset serving were validated; unsupported sorting remains correctly gated. |
| [2026-05-28-generate-and-curate-asset-pipeline-goal.md](2026-05-28-generate-and-curate-asset-pipeline-goal.md) | Completed | Added the runtime asset builder, output validator, dashboard integration, tests/fixtures, docs workflow updates, and real bitmap/reference smoke evidence. |
| [2026-05-27-demo-package-contract-assets-goal.md](2026-05-27-demo-package-contract-assets-goal.md) | Completed | Implemented demo support metadata, runtime asset manifest contract, device asset style, unsupported mechanic gates, schemas, validator, and fixtures. |
| [2026-05-26-runtime-conversion-parity-goal.md](2026-05-26-runtime-conversion-parity-goal.md) | Planned | Refreshed for current plan-goal workflow; executes the runtime conversion, consumer adapters, and parity validation plan. |
