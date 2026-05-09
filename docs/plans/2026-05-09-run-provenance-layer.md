# Run Provenance Layer

Date: 2026-05-09

## Goal

Make autonomous `/goal` activity generation traceable at the run level without changing the canonical runtime package layout.

The runtime package remains:

```text
activities/<activity_id>/
```

Each generation session also owns:

```text
runs/<run_id>/
```

This answers which run produced an activity, which assignment rows were pending at run start, which briefs blocked, and which generated packages were logged.

## Design Decisions

- Keep `activities/<activity_id>/` as the only runtime package location. Downstream consumers should not read runtime packages from `runs/`.
- Use `run_id=YYYYMMDD_HHMMSS_<short_label>` so run directories sort chronologically and remain readable.
- Snapshot unchecked `assignments.md` rows at run start. This avoids ambiguity when `assignments.md` is edited later.
- Store Phase 0 briefs under the run directory, not the activity package, because briefs are run/provenance artifacts and can also exist for blocked assignments.
- Store blocked briefs under `blocked_briefs/` and do not append `results.tsv` or mark the assignment complete when blocked.
- Keep `results.tsv` as the package-generation log for compatibility, and use `run_manifest.yaml` as the richer run index.

## Files

```text
runs/<run_id>/
├── run_manifest.yaml
├── assignment_snapshot.md
├── generated_activity_ids.txt
├── adaptation_briefs/
├── blocked_briefs/
└── review_notes.md
```

`run_manifest.yaml` links source files, assignment rows, generated package paths, blocked brief paths, result logging, checks, and timestamps.

## Workflow Changes

1. `run.md` creates `runs/<run_id>/` before processing the first assignment.
2. Phase 0 writes each generated or blocked adaptation brief into the run directory.
3. Generated packages still write exactly five files under `activities/<activity_id>/`.
4. After `results.tsv` logging, the loop appends the activity ID to `generated_activity_ids.txt` and updates `run_manifest.yaml`.
5. The final run report includes the run ID and manifest path.

## Risks

- `run_manifest.yaml` is not schema-validated yet.
- The run layer depends on the agent updating manifest counts and output lists accurately.
- Existing `results.tsv` does not include a `run_id` column. The manifest links back to results rows instead of changing the legacy log format in this pass.
