# Entity Parameterized Package Authoring Goal

## Mode

Plan-backed.

Use this file as the Codex goal-mode execution contract.

## Objective

Implement the producer-side package authoring contract for valid
entity-parameterized and entity-agnostic activities, including the current
twelve runtime-ready/generated activities.

Generated packages must explicitly declare whether a discovery handoff entity
is fixed, thematic, a runtime target, a property source, an initial-sound source,
a word target, an asset-catalog target, or invalid for the activity.

## Design Source

Source plan:

- `docs/plans/2026-06-05-entity-parameterized-package-authoring.md`

Related runtime-side plan:

- `/Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-06-05-activity-entity-parameterization-runtime.md`

The plan is authoritative for design rationale, current evidence,
implementation areas, and risk context. This goal is authoritative for hard
constraints, required checks, credential handling, and completion. If the plan
and goal conflict, stop and document the conflict before changing behavior.

## Hard Constraints

- Do not mark every package entity-agnostic by default.
- Do not claim dynamic entity targeting unless the package declares required
  slots, source fields, and derived runtime fields.
- Keep fixed authored content fixed unless the package is explicitly repaired to
  provide dynamic slots.
- Preserve the existing five-file package contract.
- Keep demo/asset extension files additive and compatible with current
  validators unless a schema migration is explicitly implemented and tested.
- Keep `entity_class_filter: []` as broad match metadata, not proof of dynamic
  entity validity.
- Treat authoring-agent or subagent mode inference as proposed evidence until
  the decision is written into package metadata and passes validator/reviewer
  integrity checks.
- Keep parameterization logic generic by declared mode and required fields. Do
  not hard-code package behavior by activity ID, current title, or one example
  activity.
- Do not implement WonderLens AI backend runtime code in this repo.
- Do not edit secrets, credentials, production data, or machine-local config.
- Do not perform unrelated refactors, broad formatting sweeps, or dependency
  upgrades.

## Required Scope

- Add a package parameterization declaration to the authoring contract.
- Update authoring/generation guidance so future demo/runtime-ready packages
  declare binding mode, required handoff inputs, dynamic target fields, authored
  constants, and invalid/fallback behavior.
- Add an authoring-agent/subagent parameterization decision step that emits the
  proposed mode, decision source, confidence, evidence, dynamic fields, frozen
  fields, required handoff fields, invalid/fallback behavior, and reviewer
  action.
- Update validators and schemas or equivalent checks for allowed modes and
  required fields.
- Add fixtures covering valid dynamic, valid thematic/fixed, and invalid
  dynamic claims.
- Classify the current twelve runtime-ready/generated activities.
- Migrate package examples or canonical package files where appropriate without
  pretending unsupported mechanics are playable.
- Document downstream WonderLens AI contract expectations.
- Update `review_dashboard.md` and `scripts/generate_run_review.py` so
  `runs/<run_id>/review.html` exposes a concise Extensibility Overview verdict
  with parameterization mode, integrity status, dynamic fields, frozen fields,
  required handoff, evidence, and reviewer action.

## Execution Rules

- Work in `wonderlens-activity-autodesign`.
- Use a feature worktree/branch for implementation, for example
  `.worktrees/feat/entity-parameterized-package-authoring`.
- Start by inspecting `program.md`, `activities/README.md`,
  `scripts/validate_demo_package_contract.py`,
  `activities/_schema/tag_block.schema.json`, and current package fixtures.
- Keep producer metadata generic by declared mode and fields, not activity ID.
- Coordinate field names with the WonderLens AI runtime plan. If the two repos'
  intended contracts conflict, stop and document the conflict before editing
  package behavior.
- Update `docs/plans/README.md` and `goals/README.md` only when the goal is
  completed or genuinely blocked.
- Follow repo commit rules. Do not push unless explicitly asked.

## Mandatory Ordering

1. Confirm current validator/tests baseline.
2. Define the parameterization contract and validator/schema behavior.
3. Update authoring instructions and examples.
4. Add the authoring-agent/subagent mode decision surface and review dashboard
   visibility.
5. Add fixtures and current-twelve classification coverage.
6. Migrate current package metadata where appropriate.
7. Run required checks before marking indexes completed or blocked.

## Live Provider Credential Rule

Live provider credentials are not required for this goal.

Do not source, inspect, print, edit, copy, or commit secrets. If an optional
consumer smoke is added, use only the relevant consumer repo's documented
credential pattern and do not expose secret values.

## Preconditions

```bash
git status --short --branch
test -f program.md
test -f activities/_schema/tag_block.schema.json
test -f scripts/validate_demo_package_contract.py
test -f goals/README.md
test -f docs/plans/README.md
```

If the working tree contains unrelated user changes, preserve them and stage
only intended goal work.

## Success Criteria

- Package authoring docs define allowed parameterization modes and required
  metadata.
- Validators reject unsupported mode values and dynamic claims that lack source
  fields, derived target slots, or required assets/provenance.
- Supported/degraded demo packages declare parameterization when entity binding
  matters.
- Fixed and thematic packages can honestly declare non-retargetable authored
  constants.
- Phoneme Treasure Hunt can declare `initial_sound_from_entity` without a
  conflicting hard-coded `/b/` target.
- The current twelve runtime-ready/generated activities are classified as
  dynamic, thematic, fixed, or unsupported until repaired.
- Downstream WonderLens AI expectations are documented with the matching runtime
  plan path.
- The generated review dashboard gives a new reviewer a scan-first verdict for
  parameterization integrity without requiring background knowledge or manual
  file archaeology.

## Required Checks

Minimum final checks:

```bash
git diff --check
python3 -m unittest tests.test_generate_run_review
python3 scripts/validate_demo_package_contract.py activities
python3 -m pytest tests/test_demo_package_contract_validator.py tests/test_generate_and_curate_asset_pipeline.py -q
```

If `activities/*/tag_block.yaml` or `activities/_schema/tag_block.schema.json`
changes, also run the tag-block schema validation snippet from `AGENTS.md`.

If available tests move, substitute equivalent focused tests that cover the
contract validator, fixtures, and any generation/asset-pipeline behavior touched
by the implementation.

## Final Completion Gate

Do not mark achieved until:

- required scope is implemented or a real blocker is documented with evidence;
- success criteria are met;
- required checks pass;
- no provider credentials or secrets are included in artifacts;
- `docs/plans/README.md` and `goals/README.md` mark this plan/goal `Completed`
  or `Blocked` as appropriate;
- intended changes are committed with conventional commit messages.

Final response must include changed files, checks run, remaining risks, and
commit hashes.

## Goal Invocation

Use from the `wonderlens-activity-autodesign` repo or implementation worktree:

```text
/goal Implement goals/2026-06-05-entity-parameterized-package-authoring-goal.md. Stop only when its completion gate is satisfied or a blocker is documented.
```
