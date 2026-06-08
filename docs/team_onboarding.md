# Team Onboarding

This guide is for collaborators joining a small parallel full-pass run. It
assumes the run captain has already created or selected a shared integration
branch and a run directory under `runs/<run_id>/`.

Start with the visual workflow guide:

```text
docs/full_pass_agentic_parallel_workflow.html
```

Use this page for the exact files, commands, and status handoff.

## Roles

| Role | Owns | Does not own |
|---|---|---|
| Run captain | baseline run branch, canonical goal/program/run loop, merge order, final readiness call | Role-specific edits without owner review |
| Text package reviewer | `spec.md`, `prod.md`, package contract notes, source-intent findings | Runtime app code, generated PNG files |
| Image/source reviewer | `asset_manifest.yaml` review, source provenance, generated source PNG QA, package-local source metadata | Activity mechanics or runtime dialogue rewrites |
| Integration owner | final merge branch, generated dashboard, fullstack/WonderLens AI validation evidence, PM handoff | Silent package or asset rewrites without routing findings to owners |

For a three-person pass, one person can be both run captain and integration
owner, one person can own text review, and one person can own image/source plus
Gemini provider generation. For a two-person pass, combine run
captain/integration with text review, and keep image/source review separate.

Use one branch per role and activity slice:

```bash
git switch <run-integration-branch>
git pull --ff-only
git switch -c <role>/<run-id>-<activity-or-slice>
```

Keep edits scoped to your role. If a finding belongs to another role, update
the activity review status and hand it back instead of fixing unrelated files.

## Status Files

Each activity should have one machine-readable status file:

```text
runs/<run_id>/review_status/<activity_id>.yaml
```

Copy the template from:

```text
runs/_templates/review_status.yaml
```

Use only these status values unless the run captain updates the template:
`pending`, `pass`, `needs_fix`, `blocked`, `not_applicable`.

Update the status file when you start review, finish review, find a blocker, or
handoff to another owner. One status file per activity keeps parallel edits
from colliding in one shared tracker.

## Text Package Reviewer Checklist

1. Confirm the package files exist: `spec.md`, `prod.md`, `tag_block.yaml`,
   `recap.template.yaml`, and `dashboard.template.yaml`.
2. If present, verify `demo_support.yaml` and `asset_manifest.yaml` describe
   the same activity flow and entity binding as `prod.md`.
3. Check `prod.md` runtime steps for concrete AI instructions, ideal and
   unexpected response handling, no-response handling, and screen state.
4. Check reference-bound activities do not rely on random generated images.
5. Record the result in `review_status/<activity_id>.yaml`.

Focused validation:

```bash
python3 scripts/validate_demo_package_contract.py runs/<run_id>/activity_packages/<activity_id>
```

## Image/Source Reviewer Checklist

1. Read `docs/activity_asset_generation_workflow.md` before generating or
   accepting any image.
2. For illustrative assets, generate one 512x512 source PNG per asset ID into:

```text
runs/<run_id>/generated_assets/inbox/<activity_id>/<asset_id>.png
```

3. For reference-bound assets, accept only verified source originals and write
   package-local source metadata under:

```text
runs/<run_id>/activity_packages/<activity_id>/assets/sources/
```

4. Run the deterministic builder after source images are in place:

```bash
python3 scripts/build_activity_assets.py runs/<run_id> --mode generate_and_curate
python3 scripts/validate_asset_build_outputs.py runs/<run_id>
```

5. Update `review_status/<activity_id>.yaml` with generated/curated asset
   evidence and any visual QA findings.

## Gemini Provider Users

Teammates who cannot use Codex built-in `imagegen` should use Gemini for
illustrative source PNGs. Install the provider dependencies and configure
credentials with:

```text
docs/image_generation_provider_setup.md
```

The provider writes only source PNGs into the builder inbox. The deterministic
builder remains the only step that writes package-local runtime variants and
updates `asset_manifest.yaml` variant paths.

## Integration Owner Handoff

Before merging role branches back into the run integration branch:

1. Pull the latest integration branch and merge or rebase the role branch.
2. Run the narrowest validators for the touched packages and assets.
3. Confirm `review_status/<activity_id>.yaml` reflects the real state.
4. Generate or refresh the run dashboard if the run requires one.
5. Record any downstream fullstack-demo or WonderLens AI validation result in
   the status file and hand unresolved failures back to the owning role.

Do not commit `.env`, service-account JSON files, generated provider request
payloads with secrets, or machine-local absolute paths.
