# Review Export

Use this reference when regenerating human review artifacts for a run.

## Purpose

Create derived reviewer artifacts from run/package source files:

- integrated asset bindings;
- one standalone HTML reviewer packet per integrated activity;
- `runs/<run_id>/review.html`;
- source comparison matrix when an intent audit exists.

Never hand-edit generated HTML as source of truth. Fix package, manifest, audit, asset, or generator inputs, then regenerate.

## Commands

Run the relevant commands from repo root:

```bash
python3 scripts/integrate_generated_assets.py runs/<run_id>
python3 scripts/integrate_generated_assets.py --validate runs/<run_id>
python3 scripts/export_activity_html.py runs/<run_id>
python3 scripts/export_activity_html.py --validate runs/<run_id>
python3 scripts/generate_run_review.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
```

If a source-intent audit exists or is in scope:

```bash
python3 scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml
python3 scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml --validate
```

## Dashboard Requirements

Follow `review_dashboard.md`. `review.html` must include, when present:

- activity cards and detail dialogs;
- runtime beat storyboard maps;
- source rows and source-promise-critical behavior;
- asset usage timelines;
- distinct `Asset dependencies`, `Display beats`, and `Image items`;
- standalone activity HTML export links;
- source comparison links;
- review criteria and scorecard results;
- blocked/resolved contract callouts;
- validation workflow commands.

## Manifest Updates

After export/generation:

- keep `outputs.review_dashboard` pointing to `runs/<run_id>/review.html`;
- keep `activity_exports/export_manifest.yaml` current when standalone packets exist;
- add check entries for commands run;
- record residual risks or reviewer notes in `review_notes.md` or `HANDOFF.md`.
