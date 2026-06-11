<!--
  Version: 1.0
  Updated: 2026-06-11
  Audience: Text Reviewer
  Companion files: docs/full_pass_agentic_parallel_workflow.html, docs/role_agent_prompting_guide.md, run.md, program.md
-->

# Text Reviewer Daily Workflow

The text reviewer owns package text quality: runtime beats, dialogue specificity,
branch behavior, parameterization, demo support metadata, and package alignment.
This doc covers what to do in a normal work session, when to involve a coding
agent, what commands to run, what evidence to expect, and when to stop.

Read the [File Ownership matrix](full_pass_agentic_parallel_workflow.html#ownership)
to confirm which files belong to this role. Read
[program.md](../program.md) Phase 3 for the 10-dimension rubric and
[role_agent_prompting_guide.md](role_agent_prompting_guide.md) for the stock
text reviewer prompt.

## Prerequisites

- The run captain has committed the baseline packages to the run branch and
  shared the branch name and your activity assignments.
- You have confirmed the activity ID, mechanic, category, support level, and
  entity mode for each assigned package.
- Your local repo is synced with the run branch.

## File Scope

You may edit these files per assigned package:

- `runs/<run_id>/activity_packages/<activity_id>/spec.md`
- `runs/<run_id>/activity_packages/<activity_id>/prod.md`
- `runs/<run_id>/activity_packages/<activity_id>/tag_block.yaml`
- `runs/<run_id>/activity_packages/<activity_id>/demo_support.yaml`
- `runs/<run_id>/activity_packages/<activity_id>/recap.template.yaml`
- `runs/<run_id>/activity_packages/<activity_id>/dashboard.template.yaml`
- `runs/<run_id>/review_status/<activity_id>.yaml`

You must not edit:

- `asset_manifest.yaml`, `assets/`, or `generated_assets/`
- Downstream app repos
- Unrelated activity packages
- Canonical rules (`GOAL.md`, `program.md`, `run.md`, `templates.md`)

## Session Workflow

Each daily session follows five phases. Run them in order and work activity by
activity, not directory-wide.

---

### Phase 1: Start — Set Up the Role Branch

```bash
# Step 1a. Sync and create your role branch
git fetch origin
git checkout run/<RUN_ID>
git pull
export ASSIGNED_IDS="activity_id_1 activity_id_2 activity_id_3"
git checkout -b <your_name>/text-$(echo ${ASSIGNED_IDS%% *} | head -c 20)

# Step 1b. Confirm the assigned packages exist
for aid in ${ASSIGNED_IDS}; do
  echo "=== ${aid} ==="
  ls runs/${RUN_ID}/activity_packages/${aid}/
  cat runs/${RUN_ID}/review_status/${aid}.yaml | head -8
done

# Step 1c. Quick orientation — read tag_block.yaml and spec.md preamble
for aid in ${ASSIGNED_IDS}; do
  echo "=== ${aid} ==="
  head -30 runs/${RUN_ID}/activity_packages/${aid}/spec.md
  echo "---"
  head -20 runs/${RUN_ID}/activity_packages/${aid}/tag_block.yaml
done
```

Before editing, answer these questions for each package:

- What mechanic does the child actually perform in Step 3?
- Does `demo_support.yaml` honestly classify the activity (supported / degraded / unsupported)?
- Do the five YAML/md files agree on pillar, game style, focal attribute, badge, and next-step direction?
- Are there any thin runtime beats that need expansion?

---

### Phase 2: Agent — Review One Package at a Time

Start a coding agent per package with this prompt:

```text
You are the text reviewer for run <RUN_ID>.
Review only runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>.

Goal:
- Verify spec.md, prod.md, tag_block.yaml, demo_support.yaml,
  recap.template.yaml, and dashboard.template.yaml describe the same activity.
- Improve runtime beat quality, step instructions, parameterization,
  entity binding, demo support metadata, and package alignment as needed.
- Preserve child-facing tone and age-appropriate interaction.
- Do not change the activity mechanic, pillar, or game style unless the current
  selection is provably wrong and the fix is recorded in spec.md
  ## Adaptation Rationale.

Allowed files:
- runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/spec.md
- runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/prod.md
- runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/tag_block.yaml
- runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/demo_support.yaml
- runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/recap.template.yaml
- runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/dashboard.template.yaml
- runs/<RUN_ID>/review_status/<ACTIVITY_ID>.yaml

Forbidden files:
- assets/**
- generated_assets/**
- downstream app repos
- unrelated activity packages

Validation:
- python3 scripts/validate_demo_package_contract.py
  runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>
- git diff --check

Update review_status with pass/fail evidence, reviewer name, next_owner,
and remaining risks in 1-2 concrete sentences.
Stop if the activity needs new visual assets, unsupported UI capability,
or product decisions.
```

---

### Phase 3: Review — Read and Judge the Output

After the agent finishes, read the output yourself. Open these files for each
package and confirm:

**spec.md:**
- Premise and target are consistent with the mechanic and pillar.
- Exactly one `## Self-Evaluation Scorecard` exists.
- If visual assets are declared, `## Asset Brief` and `## Asset Usage Timeline` are present.
- `## Adaptation Rationale` names any scaffold compromises.

**prod.md:**
- No `## Self-Evaluation Scorecard` is present.
- Every live beat has concrete AI dialogue or a detailed `Runtime AI instruction` block.
- Every Step 3 round is fully expanded (no "same structure" or one-line summaries).
- Unexpected and no-response branches are beat-specific, not copied boilerplate.
- Cat5 synthesis beats are separate from collection rounds and celebration.
- Asset IDs are referenced but raw image prompts are absent.

**tag_block.yaml:**
- Mechanic, pillar, game style, focal attribute match what spec.md and prod.md describe.
- Validates against `activities/_schema/tag_block.schema.json`.

**demo_support.yaml:**
- Status honestly reflects what the current Cat1/Cat5 demo can play.
- If `supported`, a default entity binding and playable `ui_template` exist.
- If `unsupported`, concrete reasons are listed.
- `entity_compatibility` and `parameterization` are present and complete when applicable.

**recap.template.yaml and dashboard.template.yaml:**
- `dashboard.template.yaml` `focal_attribute` equals `tag_block.yaml` `activity_signature.focal_attribute`.
- Placeholders are consistent with the mechanic and entity binding.

**Package alignment (cross-file check):**
- All five YAML/md files describe the same mechanic, pillar, game style, focal
  attribute, badge/reward, and next-step direction.

```bash
# Automated alignment check
ruby -e 'require "yaml"; dir="runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>";
tag=YAML.load_file(File.join(dir,"tag_block.yaml"));
dashboard=YAML.load_file(File.join(dir,"dashboard.template.yaml"));
ok=tag.dig("activity_signature","focal_attribute")==
   dashboard.dig("dashboard_fragment","session","focal_attribute");
puts(ok ? "OK focal_attribute" : "FAIL focal_attribute")'

# Runtime completeness scan
rg -n 'Same structure|AI gives riddle|later rounds follow|Only played if child is highly engaged|Condensed later' runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/prod.md
```

---

### Phase 4: Repair — Fix What Failed

If anything failed the review, identify the specific file and line. Do not
regenerate the whole package. Do not edit asset files.

Common repairs and where to fix them:

| Problem | Fix in |
|---|---|
| Thin Step 3 round | `prod.md` — expand with full AI dialogue and branches |
| Boilerplate edge branches | `prod.md` — write beat-specific unexpected/no-response paths |
| Wrong demo_support claim | `demo_support.yaml` — correct status, ui_template, reasons |
| Mismatched focal_attribute | `tag_block.yaml` and `dashboard.template.yaml` |
| Missing parameterization | `demo_support.yaml` — add mode, validity, source/derived fields |
| Stale or wrong pillar/style | `spec.md` `## Adaptation Rationale` and `tag_block.yaml` |

After repairs, re-run the Phase 3 checks and re-score.

---

### Phase 5: Submit — Open a PR

```bash
# Step 5a. Update review status
# Edit runs/<RUN_ID>/review_status/<ACTIVITY_ID>.yaml:
#   text_review.status: pass (or needs_fix)
#   text_review.reviewer: <your_name>
#   text_review.evidence: [list of validation outputs]
#   text_review.findings: [1-2 sentence residual risk note]
#   next_owner: run_captain (or asset_curator if assets are needed)

# Step 5b. Run validators
python3 scripts/validate_demo_package_contract.py runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>
git diff --check

# Step 5c. Commit and push
git add runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/ runs/<RUN_ID>/review_status/<ACTIVITY_ID>.yaml
git commit -m "fix(text): <ACTIVITY_ID> — text review pass, [brief note]"
git push origin <your_name>/text-<branch_suffix>

# Step 5d. Open a PR to the run branch
# (Use the GitHub app or CLI)
```

If any activity needs `needs_fix` in text_review but you cannot repair it
yourself (e.g. it needs a new asset before the text can be completed), set
`next_owner: asset_curator` and describe what is needed.

---

## Status File Rules

You own the `text_review` block in `runs/<run_id>/review_status/<activity_id>.yaml`.
Update it for every package you review, regardless of outcome.

Allowed statuses: `pending`, `pass`, `needs_fix`, `blocked`, `not_applicable`.

Every update must include:

- `reviewer` — your name
- `evidence` — validation command outputs, file paths checked
- `findings` — concrete residual risks in 1-2 sentences

Do not edit `asset_review`, `runtime_validation`, or `pm_review` blocks. Those
belong to other roles.

## Stop Conditions

Stop and ask the run captain when:

- The package mechanic, pillar, or game style is clearly wrong but you are
  unsure what to replace it with.
- The activity depends on a product capability that the current Cat1/Cat5 demo
  does not support, and you cannot honestly mark it `unsupported`.
- The runtime beats need new visual assets to be playable, and those assets do
  not exist yet.
- Two reviewers are assigned the same package.
- A validator fails for a reason outside the text review scope (e.g. asset
  schema errors, downstream runtime failures).

If a package needs only text repairs, do not mark it blocked. Mark it
`needs_fix` and describe the repair scope.

## Example Session

A text reviewer session for 3 packages:

```text
# Session start
git fetch origin
git checkout run/20260611_093000_batch3
git pull
git checkout -b alice/text-vegetable-sort

# Quick orientation on assigned packages
for aid in vegetable_sort phoneme_hunt word_echo; do
  head -30 runs/20260611_093000_batch3/activity_packages/${aid}/spec.md
done

# Start agent for package 1: vegetable_sort
# [use Phase 2 prompt]
# Read agent output, review all 6 files, note 1 thin Step 3 round
# Repair in prod.md, re-validate, update review_status → pass

# Start agent for package 2: phoneme_hunt
# Package OK as-is → review_status → pass

# Package 3: word_echo — demo_support claims supported but uses
# unsupported judgment mechanic
# Repair demo_support.yaml → degraded, add degraded_reasons
# Update review_status → pass with residual risk note

# Validate, commit, push, open PR
```
