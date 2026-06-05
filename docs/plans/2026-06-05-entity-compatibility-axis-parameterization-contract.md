# Entity Compatibility Axis Parameterization Contract Plan

Date: 2026-06-05
Status: Completed
Owner repo: `wonderlens-activity-autodesign`
Current worktree: `.worktrees/feat/entity-parameterized-package-authoring`

Do not create a new worktree for this plan unless the user explicitly redirects.

## Background

`docs/plans/2026-06-05-entity-parameterized-package-authoring.md` and its
matching goal established producer-side package parameterization metadata,
authoring-agent mode decisions, review-dashboard visibility, and downstream
WonderLens AI alignment. That work is complete and should stay as historical
baseline.

The follow-up problem is semantic overloading: `entity_binding: agnostic` is too
broad for reviewers and consumers. It can mean "not tied to a source exemplar,"
"safe for arbitrary entity handoff," or "wide match because no better metadata
exists." Live runtime checks also showed that a package can resolve handoff
metadata correctly while still carrying stale authored constants in child-facing
text. A new reviewer needs one compact verdict that says whether the activity is
safe to run with the photographed entity, not a pile of disconnected paperwork.

This plan splits the contract into two axes:

- `entity_compatibility` describes whether arbitrary discovery handoff is safe.
- `parameterization.mode` describes the deterministic runtime transformation.

## Settled Contract

Use a small compatibility axis instead of adding one mode per activity:

- `source_bound`: safe only for the authored source entity or an explicit closed
  set. This is the normal home for `parameterization.mode: fixed`.
- `agnostic`: safe for arbitrary entity handoff within declared validity rules.
  This must include a non-fixed `parameterization.mode` and the fields needed to
  resolve the handoff.
- `unsupported`: not selectable from discovery handoff until repaired or
  re-authored.

Keep `parameterization.mode` focused on reusable runtime transforms:

- `entity_theme`
- `entity_target`
- `property_target`
- `initial_sound_from_entity`
- `word_from_entity`
- `asset_catalog_target`
- `unsupported_until_parameterized`

`fixed` remains valid for source-bound or non-handoff packages, but it must not
be used to justify `entity_compatibility: agnostic`.

Add a new mode only when the activity requires a different deterministic
resolution algorithm that cannot be expressed by source fields, derived runtime
fields, validity rules, frozen fields, or asset/catalog constraints.

## Reviewer-Facing Good Criteria

An activity is "good" for an arbitrary entity handoff only when a fresh reviewer
can confirm all of the following from `review.html` without background context:

- the package declares `entity_compatibility: agnostic`;
- the package declares a non-fixed `parameterization.mode`;
- required handoff fields and derived runtime fields are present;
- frozen authored constants are explicit and do not contradict the resolved
  entity, word, property, sound, or asset set;
- the review dashboard shows a parameterization-integrity verdict of pass;
- the first child-facing turns, capture instructions, and judgment policy use
  the resolved entity context instead of stale source constants;
- the activity mechanic remains generic, not hard-coded to one activity or one
  source entity.

Any `agnostic` package without an explicit non-fixed mode is incomplete. Any
wide-match package whose child-facing text still depends on a fixed source word,
letter, property, or object is not handoff-safe.

## Scope

1. Update producer-side authoring guidance.
   - Update `program.md`, `activities/README.md`, and related contract docs so
     authors use `entity_compatibility` plus `parameterization.mode`.
   - Keep legacy `entity_binding` readable for migration context, but stop using
     it as the only authority for runtime handoff readiness.

2. Update schema and validator behavior.
   - Extend `activities/_schema/tag_block.schema.json` and
     `activities/_schema/demo_support.schema.json` as needed.
   - Update `scripts/validate_demo_package_contract.py` so `agnostic` without a
     non-fixed parameterization mode fails.
   - Add fixture coverage under `tests/fixtures/demo_package_contract/`.
   - Keep enums synchronized with `docs/activity_vocabulary.md`.

3. Update authoring-agent mode decision workflow.
   - Add an explicit authoring/subagent step that infers
     `entity_compatibility` and `parameterization.mode` from the activity's
     entity binding and mechanics.
   - Require evidence for dynamic fields, frozen fields, required handoff
     fields, invalid/fallback behavior, and reviewer action.
   - Keep the rule generic across activities; do not special-case phoneme hunt
     or any other single activity.

4. Update review dashboard output.
   - Update `review_dashboard.md` and `scripts/generate_run_review.py`.
   - In `runs/<run_id>/review.html`, update the Extensibility Overview so a new
     reviewer can see compatibility, mode, required context, frozen constants,
     stale-text risk, and the final pass/conditional/fail verdict in one place.
   - Keep the dashboard concise: evidence should support the verdict, not bury
     it.

5. Reclassify the current twelve runtime-ready activities.
   - Re-export or patch generated package metadata so all twelve declare both
     axes.
   - Do not mark packages `agnostic` unless their runtime text and metadata are
     actually parameterized.
   - Treat stale source constants such as a fixed initial sound as a validation
     failure unless they are explicitly frozen and not used in dynamic handoff.

6. Document downstream handoff expectations.
   - Update the autodesign side of the WonderLens AI contract so the runtime can
     reject ambiguous packages instead of guessing.
   - Reference the runtime follow-up plan in the WonderLens AI worktree:
     `/Users/pharrelly/codebase/gitlab/wonderlens-ai/.worktrees/feat/activity-entity-parameterization-runtime/docs/plans/2026-06-05-activity-entity-compatibility-runtime-hardening.md`.

## Delegated-Agent Guidance

Use subagents for independent exploration, implementation, verification, and
review when ownership is disjoint. Good splits include schema/validator updates,
review-dashboard rendering, current-twelve classification, and downstream
contract review. Do not assign overlapping write ownership to multiple agents,
and keep tightly coupled decisions in the main session.

## Validation

For this plan/goal creation:

```bash
git diff --check
```

For the eventual implementation:

```bash
git diff --check
python3 -m unittest tests.test_demo_package_contract_validator
python3 scripts/validate_demo_package_contract.py activities
python3 -m pytest tests/test_demo_package_contract_validator.py tests/test_generate_and_curate_asset_pipeline.py -q
```

If `activities/_schema/tag_block.schema.json` or any
`activities/*/tag_block.yaml` file changes, also run the tag-block schema
validation snippet from `AGENTS.md`.

## Completion Gate

The implementation is complete only when the authoring docs, schemas,
validators, fixtures, current-twelve metadata, and generated review dashboard
all use the compatibility axis plus parameterization mode, and ambiguous
`agnostic` packages fail validation instead of passing as runtime-ready.
