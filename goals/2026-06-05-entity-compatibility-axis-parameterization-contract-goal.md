# Entity Compatibility Axis Parameterization Contract Goal

Mode: Plan-backed

## Objective

Implement
`docs/plans/2026-06-05-entity-compatibility-axis-parameterization-contract.md`
so producer-side activity packages separate broad entity compatibility from
runtime parameterization behavior, and reviewers can decide whether an activity
is handoff-safe without background knowledge.

## Design Source

- `docs/plans/2026-06-05-entity-compatibility-axis-parameterization-contract.md`
- `docs/plans/2026-06-05-entity-parameterized-package-authoring.md`
- `goals/2026-06-05-entity-parameterized-package-authoring-goal.md`
- `program.md`
- `activities/README.md`
- `activities/_schema/tag_block.schema.json`
- `activities/_schema/demo_support.schema.json`
- `docs/activity_vocabulary.md`
- `docs/activity_tag_block_usage.md`
- `docs/activity_tag_block_progression_guide.md`
- `docs/activity_matcher_progression_workflows.md`
- `docs/entity_ontology.md`
- `docs/activity_parameterization_matrix.yaml`
- `scripts/validate_demo_package_contract.py`
- `tests/test_demo_package_contract_validator.py`
- `tests/fixtures/demo_package_contract/`

## Hard Constraints

- Continue in the existing worktree:
  `/Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/entity-parameterized-package-authoring`.
- Do not create a new worktree unless the user explicitly redirects.
- Preserve the completed historical authoring plan and goal. Additive follow-up
  changes should reference them rather than rewriting their completion record.
- Keep the solution generic across activities. Do not hard-code behavior for
  one rewritten activity, phoneme hunt, or one source entity.
- Treat `entity_compatibility: agnostic` as a runtime handoff promise. It must
  include an explicit non-fixed `parameterization.mode`.
- Do not use prose-only extensibility notes as runtime authority.
- Do not edit secrets, local credentials, production data, or unrelated user
  changes.

## Execution Rules

- Use delegated agents/subagents for independent exploration, implementation,
  verification, and code review where file ownership is disjoint.
- Keep tightly coupled contract decisions in the main session.
- Give each subagent a bounded ownership slice and make clear that others may
  be editing nearby files.
- Review subagent output before integration.
- Auto-commit intended changes after validation passes, following the repo's
  conventional commit rules.

## Required Scope

- Add the `entity_compatibility` axis to the producer contract.
- Keep `parameterization.mode` as the deterministic runtime transform axis.
- Update authoring docs so agents infer compatibility and mode during authoring.
- Update schema and validator behavior so ambiguous `agnostic` packages fail.
- Update current fixtures and current-twelve metadata to declare both axes.
- Update `review.html` generation so the Extensibility Overview shows the
  compatibility/mode verdict, required context, dynamic fields, frozen fields,
  stale-text risk, and reviewer action.
- Update downstream contract docs for WonderLens AI runtime consumption.

## Mandatory Ordering

1. Read the design source files and current validator/schema behavior.
2. Define the compatibility-axis schema, validator rules, and vocabulary text.
3. Add tests and fixtures for valid and invalid combinations.
4. Implement docs, schema, validator, dashboard, and metadata updates.
5. Reclassify the current twelve runtime-ready activities.
6. Run focused checks and repair failures.
7. Use a delegated review pass before final completion.

## Success Criteria

- A fresh reviewer can answer "is this activity good for this photographed
  entity?" from `review.html` without reading the full generated paperwork.
- `entity_compatibility: agnostic` without a non-fixed
  `parameterization.mode` fails validation.
- Existing package metadata no longer relies on `entity_binding: agnostic` as
  the only proof of dynamic handoff support.
- Dynamic packages declare source fields, derived runtime fields, frozen fields,
  invalid/fallback behavior, evidence, confidence, and reviewer action.
- The current twelve rewritten activities are classified using the new contract.
- The implementation avoids one-activity special cases.

## Required Checks

```bash
git diff --check
python3 -m unittest tests.test_demo_package_contract_validator
python3 scripts/validate_demo_package_contract.py activities
python3 -m pytest tests/test_demo_package_contract_validator.py tests/test_generate_and_curate_asset_pipeline.py -q
```

If `activities/_schema/tag_block.schema.json` or any
`activities/*/tag_block.yaml` file changes, also run the tag-block schema
validation snippet from `AGENTS.md`.

## Final Completion Gate

Stop only when all required scope is implemented, intended changes are
validated, a delegated review pass has been considered, and the changes are
committed. If a blocker prevents completion, document the blocker with the
shortest useful reason and do not mark the goal complete.

## Goal Invocation

```text
/goal Implement goals/2026-06-05-entity-compatibility-axis-parameterization-contract-goal.md. The user explicitly requests delegated-agent work for independent exploration, implementation, verification, and code review where ownership is disjoint. Continue in the existing worktree and do not create a new one. Stop only when its completion gate is satisfied or a blocker is documented.
```
