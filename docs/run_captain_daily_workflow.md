<!--
  Version: 1.1
  Updated: 2026-06-11
  Audience: Run Captain
  Companion files: docs/full_pass_agentic_parallel_workflow.html, docs/role_agent_prompting_guide.md
  Scoped goal files: goals/baseline-text-packages-goal.md (one-shot baseline),
    goals/text-reviewer-goal.md (re-runnable), goals/asset-curator-goal.md (re-runnable),
    goals/integration-owner-goal.md (re-runnable)
-->

# Run Captain Daily Workflow

The run captain owns the full-pass run from setup through final dashboard handoff.
This doc covers what to do in a normal work session, when to involve a coding
agent, what commands to run, what evidence to expect, and when to stop.

## Scoped Goal Files

The baseline is produced once. Per-activity text review, asset curation, and
integration validation are separate, re-runnable goal files. The goal files
own the detailed rules, file scopes, validators, and completion criteria. This
doc tells the captain when and in what order to invoke them.

| Phase | Goal file | Frequency |
|---|---|---|
| Baseline text packages | `goals/baseline-text-packages-goal.md` | Once per run |
| Text review | `goals/text-reviewer-goal.md` | Re-runnable per activity |
| Asset curation | `goals/asset-curator-goal.md` | Re-runnable per activity |
| Integration validation | `goals/integration-owner-goal.md` | Re-runnable per activity (after text+asset pass) |

## Prerequisites

- Repo is clean and synced with `origin/main`.
- The active assignment rows are present in `assignments.md`.
- You have reviewed the assignment scope and run flags.

## Session Workflow

Each daily session follows four phases.

---

### Phase 1: Start — Freeze the Run

**Goal:** Everyone knows the run ID, branch, assigned activities, and flags.

```bash
# Step 1a. Sync and create the run branch
git checkout main
git pull origin main
export RUN_ID=$(date +%Y%m%d_%H%M%S)_agentic_pass
git checkout -b run/${RUN_ID}

# Step 1b. Snapshot the assignment rows
mkdir -p runs/${RUN_ID}
cp assignments.md runs/${RUN_ID}/assignment_snapshot.md

# Step 1c. Record run flags
cat > runs/${RUN_ID}/run_flags.md << 'EOF'
# Run Flags — <RUN_ID>
- demo_export: true
- asset_build: manifest_only (baseline); generate_and_curate (asset phase)
- full_pass_pipeline: false (phased via scoped goal files)
- product_contract_override: none
- mapping_root: data/mappings_dev20_0318
EOF

# Step 1d. Distribute activities to contributors
```

---

### Phase 2: Agent — Produce the Baseline (Once)

**Goal:** A committed run directory with generated text-only packages, manifests,
review-status files, and dashboards exists before text and asset reviewers branch.

Start the coding agent from repo root:

```text
/goal Execute goals/baseline-text-packages-goal.md end to end.
```

The goal file owns the package contract, adaptation briefs, source-intent
audits, 10-dimension rubric, independent reviewer pass, review_status creation,
results logging, and dashboard generation. The captain does not repeat those
rules here.

**Expected outputs:**

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

Spot-check at least two packages before committing:

```bash
python3 scripts/validate_demo_package_contract.py runs/${RUN_ID}/activity_packages/<activity_id>
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

Contributors invoke the scoped goal files per activity:

```text
# Text reviewer
/goal Execute goals/text-reviewer-goal.md end to end with RUN_ID=<RUN_ID> ACTIVITY_ID=<activity_id>.

# Asset curator
/goal Execute goals/asset-curator-goal.md end to end with RUN_ID=<RUN_ID> ACTIVITY_ID=<activity_id>.
```

For each contributor PR:

1. Confirm the PR edits only the assigned package slice and role-owned files
   (see the File Ownership matrix in the parallel workflow HTML).
2. Confirm `review_status/<activity_id>.yaml` has been updated.
3. Run validators recorded in the goal file's Required Checks.
4. Merge text PRs before asset PRs when the asset list depends on final runtime
   steps.
5. If a PR edits files outside its role, ask for a split before merging.

---

### Phase 4: Close — Finalize the Run

**Goal:** Regenerate the review dashboard, update the manifest, and hand to the
integration owner.

```bash
# Regenerate the review dashboard
python3 scripts/generate_run_review.py runs/${RUN_ID}
python3 scripts/generate_run_review.py --validate runs/${RUN_ID}

# Handoff check: no raw markers in prod.md
rg -n "RESOLVED BLOCKER\|RESOLVE BLOCKER" runs/${RUN_ID}/activity_packages/*/prod.md

# Handoff check: every package has a review status file
ls runs/${RUN_ID}/review_status/

# Commit
git add runs/${RUN_ID}/review.html runs/${RUN_ID}/run_manifest.yaml
git commit -m "chore: finalize ${RUN_ID} — review dashboard and manifest"
git push origin run/${RUN_ID}
```

Handoff to integration owner:

1. Confirm text and asset review statuses are `pass` for each package.
2. Share the run branch and review dashboard path.
3. Integration owner invokes `goals/integration-owner-goal.md` per activity.

---

## Quick Reference: Review Status Files

Each package gets a status file copied from the template (see
`program.md` Phase 3 and the baseline goal file):

```bash
cp runs/_templates/review_status.yaml runs/${RUN_ID}/review_status/<activity_id>.yaml
```

Then edit `activity_id`, `run_id`, and `owners.run_captain`. Leave
`text_review` and `asset_review` as `pending`. Only the run captain creates the
initial file; contributors update their own lane.

## Stop Conditions

Stop and ask the PM or product owner when:

- Assignment scope is ambiguous.
- A contributor PR edits files outside its role.
- A validator fails for a reason outside the package-owner scope.
- Multiple contributors need to edit the same activity concurrently.
- Credentials for downstream consumer repos are required but unavailable.

## Example Session

A 6-activity batch:

```text
# Session start
git checkout main && git pull
export RUN_ID=20260611_093000_batch3
git checkout -b run/${RUN_ID}
mkdir -p runs/${RUN_ID}
cp assignments.md runs/${RUN_ID}/assignment_snapshot.md

# Run baseline once
/goal Execute goals/baseline-text-packages-goal.md end to end.

# Spot-check, commit, push, share branch with team.

# Contributors do their work:
#   Bob: /goal Execute goals/text-reviewer-goal.md end to end with RUN_ID=20260611_093000_batch3 ACTIVITY_ID=vegetable_sort.
#   Carol: /goal Execute goals/asset-curator-goal.md end to end with RUN_ID=20260611_093000_batch3 ACTIVITY_ID=vegetable_sort.
#   ...repeat per activity...

# Captain reviews PRs, merges text before assets.

# Finalize: regenerate dashboard, update manifest, hand off.
```
