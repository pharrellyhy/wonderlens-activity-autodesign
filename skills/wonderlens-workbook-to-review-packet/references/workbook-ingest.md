# Workbook Ingest

Use this reference when the user provides the original design workbook as the starting point.

## Purpose

Extract source design intent from the workbook before any generation, patch, or audit. The workbook is the human design source; generated packages must preserve its play frame unless product explicitly approves an adaptation.

## Steps

1. Confirm the workbook path exists and is an `.xlsx`, `.xls`, or `.csv`.
2. Inspect sheets and headers before assuming column meanings.
3. Identify the activity rows that are in scope. Preserve workbook row numbers or stable source IDs.
4. For each row, capture:
   - source title/name;
   - original source text;
   - intended child role;
   - original play frame;
   - interaction sequence;
   - required child actions;
   - story/role-play/challenge gates;
   - category/mechanic hints;
   - screen, asset, and product dependencies;
   - non-negotiable source elements;
   - allowed V1 adaptations or unresolved product decisions.
5. Normalize the design summary to English for repo artifacts, but retain enough original wording or row references for traceability.
6. Update or create the assignment/source snapshot expected by the current repo workflow. Prefer existing repo files and patterns such as `inputs/source_activity_concepts.md`, `assignments.md`, and run-local snapshots.
7. Do not mark source rows as generation-ready until unsupported product dependencies are either resolved by contract override or explicitly represented as blockers.
8. If `product_contract_override=minimum_unblock_allowed` is active or the user says the minimum acceptable versions are agreed, keep capability-probe rows in generation scope. Record their dependencies as resolved assumptions instead of product-decision blockers.

## Output Shape

Each normalized source concept should expose these fields, even if some values are unknown:

```yaml
source_row: <sheet and row or workbook id>
source_title: <original title>
activity_id: <proposed clean snake_case id>
original_play_frame: <what the child is pretending/doing>
child_role: <role child assumes>
interaction_sequence:
  - <ordered source beat>
required_child_actions:
  - <observable child action>
non_negotiable_elements:
  - <must preserve>
allowed_v1_adaptations:
  - <acceptable simplification>
product_dependencies:
  - <capability or decision>
minimum_unblock_status: <none|required|approved>
resolved_assumptions:
  - <minimum accepted behavior, fallback, or limit>
```

## Checks

- Every scoped workbook row maps to one source concept. It maps to a blocked/product-decision item only when no minimum acceptable version has been approved.
- Under `minimum_unblock_allowed`, capability-probe rows remain generation candidates and carry visible resolved assumptions.
- No generated artifact relies only on an inferred category when the workbook has a richer play frame.
- Source row IDs are stable enough for later `source_intent_audit.yaml` entries.
