# Activity Design Assignments

This file is the active assignment queue for `/goal` runs. Historical batches,
completed smoke runs, and scoped validation rows live in
`docs/assignments_archive.md`.

## Queue Rules

- Keep only rows that should be processed by the next active generation run.
- Mark completed rows with `[x]`; the agent skips completed rows.
- Move completed or superseded batches to `docs/assignments_archive.md`.
- Put run-specific execution rules in `goals/*.md`, not in this queue.
- Use source files such as `inputs/source_activity_concepts.md` for long
  concept or asset details instead of expanding them here.

## Row Format

Each active row should be one line.

```text
assignment_type=activity_concept, activity_concept=<name>, concept_source=<file#id>, description=<English source promise>, mechanic=<mechanic>, category=<cat1|cat3|cat5|unknown>, tier=<T0|T1|T2>, asset_policy=<no_assets|optional_support|required_prebuilt|runtime_generated|blocked>, activity_id=<stable_slug>, trigger_condition=<English trigger>
```

Supported `assignment_type` values:

- `entity_activity`: entity-grounded activity using `entity=`, `category=`,
  and usually `mapping=`.
- `activity_concept`: concept-led activity using `activity_concept=`,
  `description=`, and `mechanic=`.
- `match_pattern`: reusable pattern activity, usually Cat5 or property-driven.
- `capability_probe`: product-dependent activity that may generate, degrade, or
  block depending on the current goal contract.

Recommended fields:

- `tier=`
- `mechanic=`
- `category=`
- `activity_id=`
- `concept_source=` when the source promise comes from another document
- `asset_requirements=` when asset details are non-trivial
- `product_capabilities=` when support depends on product/runtime behavior

## Active Queue

No active assignments are currently queued.
