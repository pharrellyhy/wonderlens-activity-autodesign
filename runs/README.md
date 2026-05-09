# Runs

Run directories record provenance for each autonomous generation session. They do **not** replace canonical runtime packages under `activities/<activity_id>/`.

Use this layer to answer:

- Which `/goal` run produced this activity?
- Which assignments were pending at run start?
- Which assignments generated packages?
- Which assignments blocked at the adaptation brief?
- Where are the adaptation briefs and review notes for this run?

## Directory Shape

```text
runs/
└── <run_id>/
    ├── run_manifest.yaml
    ├── assignment_snapshot.md
    ├── generated_activity_ids.txt
    ├── adaptation_briefs/
    │   └── 001_<assignment_slug>.yaml
    ├── blocked_briefs/
    │   └── 002_<assignment_slug>.yaml
    └── review_notes.md
```

`run_id` format:

```text
YYYYMMDD_HHMMSS_<short_label>
```

Examples:

```text
20260509_113000_activity_concepts
20260509_150500_mapping_batch_04
```

Use local operator time for readability. Keep the timestamp in `run_manifest.yaml` as ISO 8601.

## File Roles

| File | Required? | Purpose |
|---|---:|---|
| `run_manifest.yaml` | Yes | Run-level index: inputs, status, generated packages, blocked briefs, checks, and timestamps. |
| `assignment_snapshot.md` | Yes | Copy of pending `assignments.md` rows at run start, preserving the source queue context. |
| `generated_activity_ids.txt` | Yes | One generated `activity_id` per line, in completion order. |
| `adaptation_briefs/` | Yes when Phase 0 runs | One YAML file per generated concept-led or underspecified assignment. |
| `blocked_briefs/` | Yes when blocked | One YAML file per blocked assignment. |
| `review_notes.md` | Recommended | Independent reviewer summary, repair notes, and residual risks. |

## Manifest Template

```yaml
run_id: 20260509_113000_activity_concepts
status: in_progress # in_progress|completed|blocked|failed
started_at: "2026-05-09T11:30:00+08:00"
completed_at:

source:
  goal_file: GOAL.md
  runbook: run.md
  assignments_file: assignments.md
  assignment_snapshot: runs/20260509_113000_activity_concepts/assignment_snapshot.md
  mapping_root: data/mappings_dev20_0318

summary:
  pending_at_start: 3
  generated_count: 0
  blocked_count: 0
  failed_count: 0

outputs:
  generated_activities: []
  blocked_assignments: []

checks:
  - command: git diff --check
    result:

notes:
  - "Canonical packages remain under activities/<activity_id>/."
```

Generated activity entry:

```yaml
- assignment_index: 1
  assignment: "assignment_type=activity_concept, activity_concept=..."
  activity_id: color_hunt_red
  activity_path: activities/color_hunt_red
  adaptation_brief: runs/<run_id>/adaptation_briefs/001_color_hunt.yaml # omit when no Phase 0 brief was produced
  results_tsv_row: true
  status: PASS
```

Blocked assignment entry:

```yaml
- assignment_index: 2
  assignment: "assignment_type=capability_probe, activity_concept=..."
  brief_path: runs/<run_id>/blocked_briefs/002_coloring_game.yaml
  reason: "runtime_generated image and coloring UI require product decision"
  status: blocked_until_product_decision
```

## Rules

- Create the run directory before processing the first assignment.
- Keep activity packages in `activities/<activity_id>/`; do not nest runtime packages under `runs/`.
- Record blocked assignments in `blocked_briefs/` even though they are not appended to `results.tsv`.
- Update `run_manifest.yaml` after each generated or blocked assignment.
- Commit `runs/<run_id>/` together with generated activity packages and queue/log updates for the run.
