# Existing Run Patch

Use this reference when the user wants to audit or repair an existing run without a full rerun.

## Purpose

Patch the current run artifacts with the smallest safe changes. Do not regenerate all activities just to add audit coverage or review exports.

## Steps

1. Confirm the target `runs/<run_id>` exists.
2. Read:
   - `runs/<run_id>/run_manifest.yaml`;
   - `runs/<run_id>/review_notes.md`;
   - package files referenced by the manifest;
   - existing `activity_exports/`, `source_comparison/`, integrated assets, storyboard/contact-sheet artifacts when present.
3. Load the original workbook and source-row mapping.
4. Run a source-intent audit for every scoped workbook row.
5. Classify each row as `aligned`, `minor_adaptation`, `intent_drift`, or `needs_product_decision`.
6. If the existing run has `product_contract_override: minimum_unblock_allowed`, treat capability-probe dependencies covered by the accepted minimum version as resolved assumptions, not unresolved product-decision blockers.
7. For high-severity `intent_drift`, choose the smallest repair:
   - patch only the affected package and regenerate review artifacts; or
   - leave the row explicitly flagged for product review when a product decision is required.
8. Regenerate only affected derived artifacts: source comparison matrix, standalone packets, and/or `review.html`.
9. Update manifest/review notes/handoff with audit counts, commands, changed packages, and residual high-severity findings.

## Guardrails

- Do not perform a full generation rerun unless the user asks for it or patching cannot preserve source intent.
- Do not rewrite unrelated packages.
- Do not mark blocked rows complete.
- Do not append `results.tsv` for audit-only or export-only changes.
- Do not hand-edit generated HTML.

## Checks

Run the narrow validation for what changed:

```bash
python3 scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml --validate
python3 scripts/export_activity_html.py --validate runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
git diff --check
```
