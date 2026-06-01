# Plan Status Index

> **Last checked:** 2026-06-01

## Status Definitions

- `Planned`: ready for future execution, not started.
- `Active`: currently being executed.
- `Completed`: completion gate passed and intended changes are committed.
- `Blocked`: execution could not complete; notes include the shortest useful reason.
- `Superseded`: replaced by a newer plan.

## Maintenance

Add new plan-backed implementation plans to this index when they are created.
When a linked goal run completes, update the plan status if the plan scope is
materially implemented. Keep notes concise and evidence-based.

This index starts with the plan-goal workflow added on 2026-05-26. Older
standalone plans remain under `docs/plans/` and are not backfilled here.

## Index

| Plan | Status | Notes |
|---|---|---|
| [2026-06-01-full-pass-agentic-pipeline.md](2026-06-01-full-pass-agentic-pipeline.md) | Completed | Encoded the master/subagent full-pass generation workflow, source-intent and consumer/import gates, fullstack/WonderLens AI dialogue QA, image QA, repair loops, and final review contract before scaling generation. |
| [2026-05-29-source-intent-pilot-validation.md](2026-05-29-source-intent-pilot-validation.md) | Completed | Seven-row pilot passed source-intent, runtime-instruction, PNG asset, fullstack import, and WonderLens AI runtime validation; Guided Drawing and Plant Parts remain honestly gated. |
| [2026-05-28-e2e-subset-runtime-validation.md](2026-05-28-e2e-subset-runtime-validation.md) | Completed | Fresh subset/autodesign assets, fullstack import/play/gate behavior, fullstack runtime-beat conversion, and WonderLens AI runtime conversion/load/asset serving were validated; unsupported sorting remains correctly gated. |
| [2026-05-28-generate-and-curate-asset-pipeline.md](2026-05-28-generate-and-curate-asset-pipeline.md) | Completed | Implemented `generate_and_curate` asset build scripts, package-local runtime assets, source curation metadata, validation, dashboard visibility, fixture coverage, and bitmap smoke. |
| [2026-05-27-demo-package-contract-assets.md](2026-05-27-demo-package-contract-assets.md) | Completed | Added demo support metadata, runtime asset manifests, device asset style, unsupported mechanic gates, schemas, validator, and fixtures. |
| [2026-05-26-runtime-conversion-parity.md](2026-05-26-runtime-conversion-parity.md) | Planned | Refreshed for current plan-goal workflow; umbrella three-phase plan for canonical activity runtime conversion, fullstack export, and live parity validation. |
