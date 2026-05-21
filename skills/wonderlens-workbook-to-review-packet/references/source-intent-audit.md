# Source-Intent Audit

Use this reference when comparing generated WonderLens activities to the original design workbook.

## Purpose

The audit is a judgment pass. The Python script renders and validates the matrix; it does not replace the agent's comparison of source intent to generated runtime behavior.

## Inputs

- Original workbook path.
- Workbook-derived source concepts or source row mapping.
- `runs/<run_id>/activity_packages/*` and/or canonical `activities/<activity_id>` packages.
- Existing `runs/<run_id>/source_comparison/source_intent_audit.yaml` when patching.
- Existing reviewer packets, storyboards, contact sheets, and `review.html` when available.

## Audit Fields

Create or update `runs/<run_id>/source_comparison/source_intent_audit.yaml` with one entry per scoped workbook row:

```yaml
- source_row: <sheet/row or stable id>
  activity_id: <generated id or blank>
  original_play_frame: <source design intent>
  generated_play_frame: <runtime behavior summary>
  preserved:
    - <source element preserved>
  drift:
    - <source element changed or missing>
  status: <aligned|minor_adaptation|intent_drift|needs_product_decision>
  severity: <none|low|medium|high>
  recommendation: <accept, patch, product review, or rerun>
  product_review_question: <question for product team, if any>
```

## Classification

- `aligned`: generated runtime preserves the workbook play frame, child role, sequence, and required child action.
- `minor_adaptation`: surface framing or implementation changed, but source intent and coverage remain intact.
- `intent_drift`: category/mechanic may be similar, but child role, sequence, story frame, or required child action materially changed.
- `needs_product_decision`: source requires unsupported or unresolved product capability, asset policy, safety decision, or evidence rule, and no accepted minimum version covers it.

When `product_contract_override=minimum_unblock_allowed` is active, do not use `needs_product_decision` for dependencies covered by the accepted minimum version. Instead, record the reduced behavior in `preserved`, `drift`, or the recommendation, then classify by whether source intent was preserved.

Use `intent_drift` for examples like:

- source asks the child to assume a profession and respond inside a work scenario, but generated activity asks the child to pick which profession matches a scenario;
- source asks the AI to tell a story with challenge gates that unlock the next story beat, but generated activity contains standalone challenges without story narration.

Examples of accepted minimum versions that can still be audit-aligned:

- Cat3 material activities can use caregiver/child confirmation and process celebration instead of AI judging final artwork quality.
- Movement activities can use safe verbal guidance and approved cards without motion detection.
- Cleanup or timer activities can use child/parent confirmation instead of visual verification.
- Coloring or avatar activities can use prebuilt/static assets or voice-only emotion-color discussion if live recoloring is unsupported.
- Story unlock can be voice-only if the AI still tells a story beat, pauses for a challenge, and narratively unlocks the next beat.

## Render And Validate

After the YAML audit is complete, run:

```bash
python3 scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml
python3 scripts/generate_source_comparison_review.py runs/<run_id> --workbook <source.xlsx> --intent-audit runs/<run_id>/source_comparison/source_intent_audit.yaml --validate
```

Record audit counts, commands, high-severity findings, and matrix path in `run_manifest.yaml`, `review_notes.md`, or `HANDOFF.md` as appropriate.
