# Subset Agentic Validation

Run: `20260603_110015_subset_agentic_validation`

## Scope

Exactly five scoped assignments from `assignments.md` were generated as run-local
activity packages under `activity_packages/`.

## Result

Verdict: PASS

- Generated 5 packages with `spec.md`, `prod.md`, `tag_block.yaml`, recap/dashboard
  templates, `demo_support.yaml`, and `asset_manifest.yaml`.
- Built 56 package-local runtime PNG assets, including the optional text-free
  phoneme cue backing.
- Preserved source promises for Scavenger Hunt, Phoneme Treasure Hunt,
  Constellation Star Count, Guided Drawing, and Recognition Pop Challenge.
- Verified deterministic WonderLens AI runtime export and fullstack-demo markdown
  export without downstream content rewrites.

## Checks

- `python scripts/validate_demo_package_contract.py runs/20260603_110015_subset_agentic_validation/activity_packages`
- `python scripts/build_activity_assets.py runs/20260603_110015_subset_agentic_validation --mode generate_and_curate --force`
- `python scripts/validate_asset_build_outputs.py runs/20260603_110015_subset_agentic_validation`
- `python scripts/validate_asset_granularity.py runs/20260603_110015_subset_agentic_validation --report-yaml runs/20260603_110015_subset_agentic_validation/generated_assets/asset_granularity_report.yaml`
- `python scripts/validate_full_pass_asset_bundle.py runs/20260603_110015_subset_agentic_validation --report-yaml runs/20260603_110015_subset_agentic_validation/generated_assets/full_pass_asset_bundle_report.yaml`
- run-local `tag_block.yaml` schema validation: 5 OK
- blocker/raw-label/source-fidelity grep checks: no unexpected matches
- `python scripts/generate_run_review.py --validate runs/20260603_110015_subset_agentic_validation`
- WonderLens AI `scripts/generate_activity_runtime.py --write --force`: 5 OK, warnings=0
- WonderLens AI `scripts/generate_activity_runtime.py --check`: 5 OK, warnings=0
- WonderLens AI focused tests: 65 passed
- fullstack-demo parser: 5 exported games parsed, expected round/synthesis shape
- fullstack-demo focused tests: 25 passed

## Artifacts

- Review dashboard: `review.html`
- Image QA: `generated_assets/image_qa_review.yaml`
- WonderLens AI QA: `downstream_reports/wonderlens_ai/dialogue_runtime_qa.md`
- fullstack-demo QA: `downstream_reports/fullstack_demo/dialogue_runtime_qa.md`
