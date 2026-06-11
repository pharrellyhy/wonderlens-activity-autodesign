<!--
  Version: 1.0
  Updated: 2026-06-11
  Audience: Run Captain
  Companion files: docs/full_pass_agentic_parallel_workflow.html, docs/role_agent_prompting_guide.md, GOAL.md, run.md
-->

# Run Captain Daily Workflow

The run captain owns the full-pass run from setup through final dashboard handoff.
This doc covers what to do in a normal work session, when to involve a coding
agent, what commands to run, what evidence to expect, and when to stop. Read
[full_pass_agentic_parallel_workflow.html](full_pass_agentic_parallel_workflow.html)
for the run-level pipeline overview and ownership matrix.

## Prerequisites

- Repo is clean and synced with `origin/main`.
- You have the scoped full-pass goal file (e.g.
  `goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md`).
- The active assignment rows you want are present in `assignments.md`.
- You have reviewed the assignment scope, asset mode, and run flags in the goal
  file.

## Session Workflow

Each daily session follows the same five phases. Run them in order and do not
skip evidence collection.

---

### Phase 1: Start — Freeze the Run

**Goal:** Everyone knows the run ID, branch, assigned activities, and flags.

```bash
# Step 1a. Sync and create the run branch
git checkout main
git pull origin main
export RUN_ID=$(date +%Y%m%d_%H%M%S)_agentic_pass
git checkout -b run/${RUN_ID}

# Step 1b. Write a frozen scope note (record the assignment rows being generated)
mkdir -p runs/${RUN_ID}
cp assignments.md runs/${RUN_ID}/assignment_snapshot.md

# Step 1c. Record run flags in a scoped notes file
cat > runs/${RUN_ID}/run_flags.md << 'EOF'
# Run Flags — <RUN_ID>

- demo_export: true
- asset_build: generate_and_curate
- full_pass_pipeline: true
- product_contract_override: none
- mapping_root: data/mappings_dev20_0318

## Assignment Scope
<!-- paste the unchecked rows from assignment_snapshot.md here -->
EOF

# Step 1d. Distribute assignments to contributors
```

The assignment scope and run flags are now locked. Share run ID, branch name,
and activity-to-owner plan with the team before proceeding.

---

### Phase 2: Agent — Run the Baseline

**Goal:** Produce a commit with generated packages, manifests, review-status
files, and initial reviewer evidence before text and asset reviewers branch.

Start the coding agent from repo root with this prompt:

```text
You are the run captain for run <RUN_ID>.
Work from the wonderlens-activity-autodesign repo root.
Execute the scoped full-pass goal:
/goal Execute goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md end to end.

Scope:
- Generate the baseline activity packages for the selected assignment set.
- Write run_manifest.yaml, generated_activity_ids.txt, review.html,
  and runs/<RUN_ID>/review_status/<activity_id>.yaml for every generated
  activity package.
- Keep asset_build and demo_export flags recorded in run_manifest.yaml.

Allowed files:
- runs/<RUN_ID>/**
- results.tsv only if the goal explicitly requires logging after reviewer PASS evidence.

Forbidden files:
- Downstream app repos.
- Unrelated canonical docs.
- Unassigned activity packages from older runs.

Validation:
- Run the validators required by the goal file: tag_block schema, demo contract,
  package self-evaluation, source-intent audit, independent reviewer pass.
- Run git diff --check.

Review status files:
- For each generated activity package, create
  runs/<RUN_ID>/review_status/<activity_id>.yaml by copying
  runs/_templates/review_status.yaml.
- Set owners.run_captain to your name.
- Set text_review.status to pending and asset_review.status to pending.

Commit only the intended baseline run output.
Stop if assignment scope, credentials, source files, or goal constraints are
ambiguous.
```

**Expected outputs after the agent finishes:**

```text
runs/<RUN_ID>/
├── run_manifest.yaml
├── assignment_snapshot.md
├── generated_activity_ids.txt
├── review_notes.md
├── review.html
├── activity_packages/<activity_id>/   (5 or 7 files each)
├── adaptation_briefs/
├── review_status/<activity_id>.yaml   (one per package)
└── ...
```

Spot-check at least two packages before committing. Verify:

- `tag_block.yaml` validates against the schema.
- `spec.md` has exactly one `## Self-Evaluation Scorecard`.
- `prod.md` has no scorecard and concrete Step 1-5 beats.
- `review_status/<activity_id>.yaml` exists and was copied from the template.

```bash
# Quick spot checks
python3 -c "
import json, yaml, pathlib
from jsonschema import Draft202012Validator
schema = json.loads(pathlib.Path('activities/_schema/tag_block.schema.json').read_text())
v = Draft202012Validator(schema)
for p in sorted(pathlib.Path('runs/${RUN_ID}/activity_packages').glob('*/tag_block.yaml')):
    errs = list(v.iter_errors(yaml.safe_load(p.read_text())))
    print(('OK' if not errs else 'FAIL'), p)
"

rg -c '## Self-Evaluation Scorecard' runs/${RUN_ID}/activity_packages/*/spec.md
rg -c '## Self-Evaluation Scorecard' runs/${RUN_ID}/activity_packages/*/prod.md
ls runs/${RUN_ID}/review_status/
```

Commit the baseline:

```bash
git add runs/${RUN_ID}/
git commit -m "Design: baseline ${RUN_ID} — activity packages, manifests, review status, dashboard"
git push -u origin run/${RUN_ID}
```

---

### Phase 3: Review — Manage Contributor PRs

**Goal:** Merge text and asset PRs with correct scope and ownership.

For each contributor PR:

1. Confirm the PR edits only the assigned package slice and role-owned files
   (see the File Ownership matrix in the parallel workflow HTML).
2. Confirm `review_status/<activity_id>.yaml` has been updated with evidence
   and a status.
3. Run the narrowest relevant validator:

```bash
# Text PR validation
python3 scripts/validate_demo_package_contract.py runs/${RUN_ID}/activity_packages/<activity_id>

# Asset PR validation
python3 scripts/validate_asset_build_outputs.py runs/${RUN_ID}
```

4. Merge text PRs before asset PRs when the asset list depends on final runtime
   steps.
5. If a PR edits files outside its role, ask for a split before merging.
6. Rebase the next PRs on the updated run branch.

---

### Phase 4: Close — Finalize the Run

**Goal:** Regenerate the review dashboard, update the manifest, and hand to the
integration owner.

```bash
# Step 4a. Regenerate the review dashboard
python3 scripts/generate_run_review.py runs/${RUN_ID}
python3 scripts/generate_run_review.py --validate runs/${RUN_ID}

# Step 4b. Update run_manifest.yaml final status
# (hand-edit to set completed_at, final status, and summary counts)

# Step 4c. Commit the final dashboard and manifest update
git add runs/${RUN_ID}/review.html runs/${RUN_ID}/run_manifest.yaml
git commit -m "chore: finalize ${RUN_ID} — review dashboard and manifest"
git push origin run/${RUN_ID}
```

Handoff to integration owner:

1. Confirm every package has a `review_status/<activity_id>.yaml` with
   text_review and asset_review statuses.
2. Confirm no `RESOLVED BLOCKER` markers remain in runtime-facing `prod.md`:
   ```bash
   rg -n "RESOLVED BLOCKER\|RESOLVE BLOCKER" runs/${RUN_ID}/activity_packages/*/prod.md
   ```
3. Share the run branch, review dashboard path, and a summary of remaining
   blocked or `needs_fix` items.

---

## Quick Reference: Review Status Files

Every generated package must get a status file copied from the template:

```bash
cp runs/_templates/review_status.yaml runs/${RUN_ID}/review_status/<activity_id>.yaml
```

Then edit these fields:

| Field | Set to |
|---|---|
| `activity_id` | The package activity ID |
| `run_id` | The current run ID |
| `owners.run_captain` | Your name |
| `text_review.status` | `pending` (text reviewer updates this later) |
| `asset_review.status` | `pending` (asset curator updates this later) |

Only the run captain creates the initial file. Contributors update their own
lane. Do not let two people edit the same status file from different branches
concurrently.

## Stop Conditions

Stop and ask the PM or product owner when:

- Assignment scope is ambiguous or the goal file's constraints are unclear.
- A contributor PR edits files outside its role.
- A validator fails for a reason that is not package, text, or asset owned.
- Multiple contributors need to edit the same activity concurrently.
- Credentials for downstream consumer repos are required but unavailable.
- A blocked activity depends on a product capability decision that has not been
  recorded.

## Example Session

A run captain session for a 6-activity batch:

```text
# Session start
git checkout main && git pull
export RUN_ID=20260611_093000_batch3
git checkout -b run/${RUN_ID}

# Snapshot assignments, record flags, assign activities
mkdir -p runs/${RUN_ID}
cp assignments.md runs/${RUN_ID}/assignment_snapshot.md
# Assign 3 activities to text reviewer A, 3 to text reviewer B,
# and matching assets to asset curator C.

# Start coding agent with the Phase 2 prompt. Wait ~20-45 min for baseline.
# Spot-check 2 packages, fix any schema or structure issues, commit baseline.
# Contributors branch from run/${RUN_ID}, do their work, open PRs.
# Review PRs: validate, confirm scope, merge text first, then assets.
# Regenerate review.html, update manifest, hand to integration owner.
```

Total session: roughly 1-2 hours of captain time across several days of parallel contributor work.
