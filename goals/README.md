# Goal Status Index

> **Last checked:** 2026-05-28

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
| [2026-05-28-generate-and-curate-asset-pipeline-goal.md](2026-05-28-generate-and-curate-asset-pipeline-goal.md) | Planned | Executes the agent-assisted `generate_and_curate` asset pipeline with package-local runtime assets, reference curation, bitmap smoke, and audit outputs. |
| [2026-05-27-demo-package-contract-assets-goal.md](2026-05-27-demo-package-contract-assets-goal.md) | Completed | Implemented demo support metadata, runtime asset manifest contract, device asset style, unsupported mechanic gates, schemas, validator, and fixtures. |
| [2026-05-26-runtime-conversion-parity-goal.md](2026-05-26-runtime-conversion-parity-goal.md) | Planned | Refreshed for current plan-goal workflow; executes the runtime conversion, consumer adapters, and parity validation plan. |
