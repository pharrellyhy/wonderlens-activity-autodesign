# Text Reviewer Goal

## Mode

Re-runnable. Accepts `RUN_ID` and `ACTIVITY_ID` as parameters.

Use this file as the Codex goal-mode execution contract for reviewing and
repairing the text/YAML quality of a single generated activity package. Run it
once per assigned activity, as many times as needed until the text review
passes.

## Objective

Review `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>` against the 10-dimension
rubric in `program.md` Phase 3. Verify package alignment across all text/YAML
files. Repair concrete failures. Update the per-activity review status file.
Do NOT edit assets, generate images, or touch downstream consumer repos.

## Parameters

Replace these before each run:

```text
RUN_ID=<run_id>                # e.g. 20260611_093000_batch3
ACTIVITY_ID=<activity_id>      # e.g. vegetable_sort
```

## Source Documents

- `program.md` — Phase 3 rubric (Dimensions 1-10) and Phase 2 package contract.
- `templates.md` — mechanic adapters, pillar overlays, category modifiers.
- `activities/README.md` — file roles, runtime invariants, asset brief requirements.
- `docs/activity_vocabulary.md` — closed enums for `activity_signature` fields.
- `docs/full_pass_agentic_parallel_workflow.html` — file ownership matrix.
- `docs/text_reviewer_daily_workflow.md` — detailed session workflow.

## Allowed Files

- `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/spec.md`
- `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/prod.md`
- `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/tag_block.yaml`
- `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/demo_support.yaml`
- `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/recap.template.yaml`
- `runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/dashboard.template.yaml`
- `runs/<RUN_ID>/review_status/<ACTIVITY_ID>.yaml`

## Forbidden Files

- `asset_manifest.yaml`, `assets/**`, `generated_assets/**`
- Downstream app repos
- Unrelated activity packages
- Canonical rules (`GOAL.md`, `program.md`, `run.md`, `templates.md`)

## Hard Constraints

- Do not change the activity mechanic, pillar, or game style unless the current
  selection is provably wrong and the fix is recorded in `spec.md`
  `## Adaptation Rationale`.
- Preserve child-facing tone and age-appropriate interaction.
- Do not regenerate the whole package; patch only the specific failures found.
- Do not edit asset files.
- If the activity needs new visual assets, record a note and set
  `next_owner: asset_curator`; do not mark the text review as failed solely
  for missing assets.

## Required Checks

```bash
ACTIVITY_ID="<activity_id>"
RUN_ID="<run_id>"

# Package contract
python3 scripts/validate_demo_package_contract.py \
  runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}

# Scorecard placement
rg -c '## Self-Evaluation Scorecard' \
  runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/spec.md
rg -c '## Self-Evaluation Scorecard' \
  runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/prod.md

# Focal attribute alignment
ruby -e 'require "yaml"; d="runs/'${RUN_ID}'/activity_packages/'${ACTIVITY_ID}'";
t=YAML.load_file(File.join(d,"tag_block.yaml"));
dash=YAML.load_file(File.join(d,"dashboard.template.yaml"));
ok=t.dig("activity_signature","focal_attribute")==
   dash.dig("dashboard_fragment","session","focal_attribute");
puts(ok ? "OK focal_attribute" : "FAIL focal_attribute")'

# Runtime completeness (no condensed placeholders)
rg -n 'Same structure|AI gives riddle|later rounds follow|Condensed later' \
  runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/prod.md

git diff --check
```

## Required Scope

- Read all 6 package text/YAML files.
- Evaluate against `program.md` Phase 3 Dimensions 1-10.
- Verify package alignment: `tag_block.yaml`, `recap.template.yaml`,
  `dashboard.template.yaml`, `spec.md`, and `prod.md` describe the same
  mechanic, pillar, game style, focal attribute, badge, and next-step direction.
- Verify `demo_support.yaml` honestly classifies the activity as supported,
  degraded, or unsupported, with concrete reasons.
- Repair concrete failures (thin Step 3 rounds, boilerplate edge branches,
  missing parameterization, mismatched focal_attribute, stale demo_support).
- Update `review_status/<ACTIVITY_ID>.yaml` `text_review` block with status,
  reviewer name, evidence, findings, and next_owner.
- Run required checks.

## Completion Gate

The goal is complete when:

- All 10 rubric dimensions pass or honest `needs_fix`/`not_applicable` notes
  are recorded.
- Package alignment is confirmed across all text/YAML files.
- `demo_support.yaml` status matches the actual package content.
- `review_status/<ACTIVITY_ID>.yaml` `text_review.status` is `pass` or
  `needs_fix` with a concrete repair scope recorded.
- Required checks pass.
- Intended text/YAML changes are committed.

## Goal Invocation

```text
/goal Execute goals/text-reviewer-goal.md end to end with RUN_ID=<run_id> ACTIVITY_ID=<activity_id>.
```
