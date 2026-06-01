# Goal Status Index

> **Last checked:** 2026-05-29

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
| [2026-05-29-source-intent-pilot-validation-goal.md](2026-05-29-source-intent-pilot-validation-goal.md) | Completed | Seven-row pilot passed source-intent, runtime-instruction, PNG asset, fullstack import, and WonderLens AI runtime validation; Guided Drawing and Plant Parts remain honestly gated. |
| [2026-05-28-e2e-subset-runtime-validation-goal.md](2026-05-28-e2e-subset-runtime-validation-goal.md) | Completed | Fresh subset/autodesign assets, fullstack import/play/gate behavior, fullstack runtime-beat conversion, and WonderLens AI runtime conversion/load/asset serving were validated; unsupported sorting remains correctly gated. |
| [2026-05-28-generate-and-curate-asset-pipeline-goal.md](2026-05-28-generate-and-curate-asset-pipeline-goal.md) | Completed | Added the runtime asset builder, output validator, dashboard integration, tests/fixtures, docs workflow updates, and real bitmap/reference smoke evidence. |
| [2026-05-27-demo-package-contract-assets-goal.md](2026-05-27-demo-package-contract-assets-goal.md) | Completed | Implemented demo support metadata, runtime asset manifest contract, device asset style, unsupported mechanic gates, schemas, validator, and fixtures. |
| [2026-05-26-runtime-conversion-parity-goal.md](2026-05-26-runtime-conversion-parity-goal.md) | Planned | Refreshed for current plan-goal workflow; executes the runtime conversion, consumer adapters, and parity validation plan. |
