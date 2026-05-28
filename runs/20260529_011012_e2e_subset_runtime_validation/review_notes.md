# Review Notes

## Summary

Status: Blocked after downstream validation. Autodesign package generation, package-local assets, review dashboard validation, package QA, and visual/reference QA passed. WonderLens AI runtime conversion passed, but package loading failed on a downstream schema mismatch for `activity_signature.intro`.

## Delegated Reviews

- Package QA: Parfit (`019e6f9f-852d-7702-a3db-9b325c11f523`) final re-review PASS. Evidence: `python3 scripts/validate_demo_package_contract.py runs/20260529_011012_e2e_subset_runtime_validation/activity_packages` returned `OK demo package contract: 5 package(s)`; reviewed adaptation briefs under `adaptation_briefs/` and package `spec.md`/`prod.md` files for Phase 0 enums, asset/source summaries, and Step 3 `Round 1` headings.
- Visual/reference QA: Curie (`019e6f9f-85c8-7142-a48e-7addf0814a90`) PASS. Evidence: inspected all package-local `assets/*__round_512.png`, PIL dimension/mode checks, Orion bright-star connected-component count, and source metadata at `activity_packages/e2e_orion_number_reveal/assets/sources/orion_seven_star_card__source_metadata.yaml`.
- Fullstack sidecar: Plato (`019e6f8f-5457-7d80-b71a-8d185ebca05b`) identified current import command, output paths, endpoint smoke shape, exact-list fixture brittleness, and the step-instruction conversion gap. Local execution confirmed import output under downstream `backend/games/e2e_*.md` and `frontend/public/activity-assets/e2e_*/`.
- WonderLens AI sidecar: Newton (`019e6f8f-54f3-7003-87fd-8190d6cdb45d`) identified converter/load commands, package asset route `/activity-assets/packages/<activity_id>/<relative_asset_path>`, exact-package WS handoff path, and likely schema/load blockers. Local execution wrote `.artifacts/e2e-subset-runtime/report.json` and reproduced `activity_signature.intro` load failure.

## Local Validation

See `run_manifest.yaml` `checks` and `e2e_subset_validation.md` for command results. `review.html` validation passed after repairs.

## Blockers

- `wonderlens-ai`: converted packages cannot load because `ActivitySignature` forbids current autodesign `activity_signature.intro`.
- `wonderlens-activity-fullstack-demo`: follow-up needed to convert rich `prod.md` Runtime AI instructions into generated `step_instructions`; current fresh imports use generic defaults.

- Final report review: Hilbert (`019e6fab-985f-7241-b788-13b668892251`) initially failed the report for stale `final_report: pending`, command placeholders, `blocked_count` ambiguity, and thin delegated evidence. These items were repaired before commit.
