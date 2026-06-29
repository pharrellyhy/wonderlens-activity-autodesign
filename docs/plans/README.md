# Plan Status Index

> **Last checked:** 2026-06-24

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
| [2026-06-24-skip-intro-rules-only-packages.md](2026-06-24-skip-intro-rules-only-packages.md) | Active | Removes the separate intro step from four runtime-verified packages, keeps rules explanation-only, and preserves the first child action prompt in Round/Collect 1. |
| [2026-06-24-four-package-runtime-verification-authoring.md](2026-06-24-four-package-runtime-verification-authoring.md) | Active | Updates four packages for runtime verification without `activity_display_contract_v1.yaml`: seed-photo first-letter hunt, emotion cue matching, partial reveal answer hiding, and animal transcript verification. |
| [2026-06-23-activity-display-contract-v1.md](2026-06-23-activity-display-contract-v1.md) | Completed | Added producer-side `activity_display_contract_v1.yaml` schema/validator/tests, current-twelve and run-local backfill, docs updates, and English-only display effect fields. |
| [2026-06-08-gemini-asset-quality-candidates.md](2026-06-08-gemini-asset-quality-candidates.md) | Planned | Adds multi-candidate Gemini generation, style-reference prompting, explicit candidate acceptance, and reviewable visual QA evidence for illustrative assets. |
| [2026-06-08-team-readiness-and-gemini-assets.md](2026-06-08-team-readiness-and-gemini-assets.md) | Completed | Added collaborator onboarding, review-status template, Gemini source PNG provider, dependency setup, tests, docs links, and live smoke evidence. |
| [2026-06-05-entity-compatibility-axis-parameterization-contract.md](2026-06-05-entity-compatibility-axis-parameterization-contract.md) | Completed | Added explicit entity compatibility metadata, validator/schema enforcement, review-dashboard handoff verdicts, current-twelve reclassification, docs, fixtures, and focused verification. |
| [2026-06-05-entity-parameterized-package-authoring.md](2026-06-05-entity-parameterized-package-authoring.md) | Completed | Added producer-side parameterization metadata, authoring-agent mode decision docs, review-dashboard integrity verdicts, validator/schema coverage, current-twelve classification, and downstream WonderLens AI contract alignment. |
| [2026-06-01-run-full-pass-agentic-pipeline.md](2026-06-01-run-full-pass-agentic-pipeline.md) | Planned | Executes the current workbook full pass with `asset_build=generate_and_curate`, fullstack validation from the `feat/activity-text-game` worktree, WonderLens AI dialogue validation, image QA, repair loops, and final review. |
| [2026-06-01-full-pass-agentic-pipeline.md](2026-06-01-full-pass-agentic-pipeline.md) | Completed | Encoded the master/subagent full-pass generation workflow, source-intent and consumer/import gates, fullstack/WonderLens AI dialogue QA, image QA, repair loops, and final review contract before scaling generation. |
| [2026-05-29-source-intent-pilot-validation.md](2026-05-29-source-intent-pilot-validation.md) | Completed | Seven-row pilot passed source-intent, runtime-instruction, PNG asset, fullstack import, and WonderLens AI runtime validation; Guided Drawing and Plant Parts remain honestly gated. |
| [2026-05-28-e2e-subset-runtime-validation.md](2026-05-28-e2e-subset-runtime-validation.md) | Completed | Fresh subset/autodesign assets, fullstack import/play/gate behavior, fullstack runtime-beat conversion, and WonderLens AI runtime conversion/load/asset serving were validated; unsupported sorting remains correctly gated. |
| [2026-05-28-generate-and-curate-asset-pipeline.md](2026-05-28-generate-and-curate-asset-pipeline.md) | Completed | Implemented `generate_and_curate` asset build scripts, package-local runtime assets, source curation metadata, validation, dashboard visibility, fixture coverage, and bitmap smoke. |
| [2026-05-27-demo-package-contract-assets.md](2026-05-27-demo-package-contract-assets.md) | Completed | Added demo support metadata, runtime asset manifests, device asset style, unsupported mechanic gates, schemas, validator, and fixtures. |
| [2026-05-26-runtime-conversion-parity.md](2026-05-26-runtime-conversion-parity.md) | Planned | Refreshed for current plan-goal workflow; umbrella three-phase plan for canonical activity runtime conversion, fullstack export, and live parity validation. |
