# E2E Subset Runtime Validation Report

Run: `runs/20260529_011012_e2e_subset_runtime_validation`  
Status: **Blocked**  
Completed at: `2026-05-29T01:39:26+08:00`

## Selected Packages

| Activity ID | Slice | Support | Notes |
|---|---|---|---|
| `e2e_shadow_story_seed` | Cat1 simple supported | `supported` | Package-local assets and runtime beats generated under `activity_packages/e2e_shadow_story_seed`. |
| `e2e_soft_shape_collect` | Cat5 simple collection supported | `supported` | Package-local assets and runtime beats generated under `activity_packages/e2e_soft_shape_collect`. |
| `e2e_b_sound_treasure_collect` | Cat5 runtime-judgment degraded | `degraded` | Package-local assets and runtime beats generated under `activity_packages/e2e_b_sound_treasure_collect`. |
| `e2e_rainbow_sort_board_unsupported` | Unsupported UI-heavy mechanic | `unsupported` | Package-local assets and runtime beats generated under `activity_packages/e2e_rainbow_sort_board_unsupported`. |
| `e2e_orion_number_reveal` | Reference-bound asset case | `supported` | Package-local assets and runtime beats generated under `activity_packages/e2e_orion_number_reveal`. |

## Autodesign Evidence

- Generated five fresh run-local packages with `demo_export=true` and `asset_build=generate_and_curate`.
- `asset_manifest.yaml` includes package-local runtime PNGs at `512x512`; Cat5 packages declare correct/distractor card roles and stable `collection_catalog_id` values.
- `e2e_orion_number_reveal` uses accepted NOIRLab Orion source metadata and a simplified seven-guide-star runtime card with no background star count drift.
- `review.html` validates, including `runtime_contract_quality`, branch follow-up, photo timing, asset output, scorecard, asset usage, and local link gates.

## Fullstack Demo Evidence

Import refreshed from current package files:

- Written: `e2e_shadow_story_seed__shadow_seed`, `e2e_soft_shape_collect__soft_shape`, `e2e_b_sound_treasure_collect__b_sound_object`, `e2e_orion_number_reveal__orion_constellation`.
- Skipped/gated: `e2e_rainbow_sort_board_unsupported` because `demo_support.status=unsupported` and `ui_template=none`.
- Live smoke: `/api/health` OK; `/api/entities` lists two Cat1 e2e supported packages, one Cat5 supported package, one Cat5 degraded package; unsupported rainbow package is absent.
- Browser-safe assets resolved through Vite: `/activity-assets/e2e_soft_shape_collect__soft_shape/round_shape__round_512.png` and `/activity-assets/e2e_orion_number_reveal__orion_constellation/orion_seven_star_card__round_512.png` returned `200 image/png`.
- `/api/start` returned sessions for Cat1, Cat5 supported, and Cat5 degraded imported filenames.

Fullstack follow-ups:

- The required aggregate backend check fails two exact-list fixture assertions in `tests/test_entity_registry.py` because fresh imported e2e IDs are legitimately present.
- Fresh imported packages still receive generic default `step_instructions`; fullstack does not convert rich `prod.md` Runtime AI instruction beats into fullstack-style step instructions. This affects behavior quality, especially the Orion number-first reveal.

## WonderLens AI Evidence

Deterministic package/runtime tests pass. Runtime conversion also passes:

- `runtime.yaml` generated for all five packages with `warnings=0`.
- Generated runtime data preserves one Step 3 runtime round per package with branch policy keys `hook`, `transition`, `round_1`, `celebrate`, and `closing`.
- Report path in downstream worktree: `.artifacts/e2e-subset-runtime/report.json`.

Blocking failure:

- Loading the converted packages with `WONDERLENS_ACTIVITY_PACKAGE_DIR=.artifacts/e2e-subset-runtime/activities` fails for all five packages.
- Owner: `wonderlens-ai`.
- Root cause: `ActivitySignature` forbids extra fields and does not accept autodesign-required `activity_signature.intro` from `tag_block.yaml`.
- Evidence: `load_activity_packages()` raises `ActivityPackageLoadError` with `activity_signature.intro Extra inputs are not permitted` for each generated package.
- Recommendation: update WonderLens AI package models or converter copy step to tolerate/mirror the current autodesign tag-block schema before live WS/package asset smoke can run.


Exact WonderLens AI conversion commands run from the WonderLens AI validation worktree. `AUTODESIGN_RUN` was set to the relative source path below to avoid recording a machine-local absolute path:

```bash
AUTODESIGN_RUN="../../../../../github/wonderlens-activity-autodesign/.worktrees/chore/e2e-subset-runtime-validation/runs/20260529_011012_e2e_subset_runtime_validation/activity_packages"
uv run python scripts/generate_activity_runtime.py --source "$AUTODESIGN_RUN" --dest .artifacts/e2e-subset-runtime/activities --write --force --report-json .artifacts/e2e-subset-runtime/report.json
uv run python scripts/generate_activity_runtime.py --source "$AUTODESIGN_RUN" --dest .artifacts/e2e-subset-runtime/activities --check --report-json .artifacts/e2e-subset-runtime/check-report.json
```

## Delegated Review

- Package QA: PASS after repair. Phase 0 readiness/alignment enums, `spec.md` asset/source detail, and Step 3 `Round 1` headings were re-reviewed.
- Visual/reference QA: PASS. All runtime PNGs are `512x512`; no text/logos/device chrome/contact sheets/masks; Orion has exactly seven prominent guide stars and accepted source metadata.
- Downstream sidecars: fullstack and WonderLens AI explorers provided current commands, path expectations, endpoint evidence, and known blockers before local execution.

## Checks

| Area | Command | Result |
|---|---|---|
| Autodesign | `python scripts/validate_demo_package_contract.py runs/20260529_011012_e2e_subset_runtime_validation/activity_packages` | PASS |
| Autodesign | `python scripts/build_activity_assets.py runs/20260529_011012_e2e_subset_runtime_validation --mode generate_and_curate --force` | PASS |
| Autodesign | `python scripts/validate_asset_build_outputs.py runs/20260529_011012_e2e_subset_runtime_validation` | PASS |
| Autodesign | `python scripts/generate_run_review.py --validate runs/20260529_011012_e2e_subset_runtime_validation` | PASS |
| Fullstack | `PYTHONDONTWRITEBYTECODE=1 uv run pytest tests/test_autodesign_importer.py tests/test_entity_registry.py tests/test_api.py -q -p no:cacheprovider` | FAIL: exact-list fixtures only |
| Fullstack | focused importer/API tests | PASS |
| Fullstack | `cd frontend && npm test -- --run` | PASS |
| WonderLens AI | package/runtime/loader/generator unit tests | PASS |
| WonderLens AI | asset manifest/API package tests | PASS |
| WonderLens AI | `AUTODESIGN_RUN=../../../../../github/wonderlens-activity-autodesign/.worktrees/chore/e2e-subset-runtime-validation/runs/20260529_011012_e2e_subset_runtime_validation/activity_packages; uv run python scripts/generate_activity_runtime.py --source "$AUTODESIGN_RUN" --dest .artifacts/e2e-subset-runtime/activities --write --force --report-json .artifacts/e2e-subset-runtime/report.json` and `uv run python scripts/generate_activity_runtime.py --source "$AUTODESIGN_RUN" --dest .artifacts/e2e-subset-runtime/activities --check --report-json .artifacts/e2e-subset-runtime/check-report.json` | PASS |
| WonderLens AI | `load_activity_packages()` with generated package root | FAIL: `activity_signature.intro` schema mismatch |

## Final Classification

This validation is **blocked**, not failed at autodesign. Autodesign generated the required package subset, assets, review dashboard, and runtime-ready instructions. The remaining blocker is a WonderLens AI schema compatibility issue after successful runtime conversion. Fullstack demo has import/play/gate evidence, but still needs a follow-up to convert rich Runtime AI instruction beats into `step_instructions` instead of defaults.
