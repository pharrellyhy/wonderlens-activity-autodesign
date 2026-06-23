# Activity Display Contract V1 Goal

## Mode

Plan-backed.

Use this file as the Codex goal-mode execution contract.

## Objective

Implement the producer-side `activity_display_contract_v1` package contract so
runtime-ready activity packages explicitly declare their app layout, displayed
asset, control mode, options, verification policy, and sound, lighting, and
haptic feedback profile.

## Design Source

Source plan:

- `docs/plans/2026-06-23-activity-display-contract-v1.md`

Consumer companion plan:

- `/Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-06-23-activity-display-runtime-verification.md`

The source plan is authoritative for design rationale, contract semantics,
current-twelve migration guidance, and risks. This goal is authoritative for
hard constraints, required checks, and completion. If the plan and goal
conflict, stop and document the conflict before changing behavior.

## Hard Constraints

- Keep the contract general for future packages; do not hard-code behavior to
  the current twelve activity IDs.
- Use only these app-facing layout IDs:
  - `single_image`
  - `two_image_options`
  - `two_direction_options`
  - `two_number_options`
  - `multi_option_carousel`
- Use English-only effect fields: `sound_effects`, `lighting_effects`, and
  `haptic_feedback`.
- Do not put display runtime metadata into `tag_block.yaml`.
- Do not claim unsupported layouts or mechanics are playable.
- Do not implement WonderLens AI runtime code in this repo.
- Do not edit secrets, local credentials, production data, or
  machine-specific config.
- Do not perform unrelated refactors, broad formatting sweeps, or dependency
  upgrades.

## Required Scope

- Define and document `activity_display_contract_v1.yaml`.
- Add schema or equivalent validation for the new contract file.
- Add a focused validator and tests for valid/invalid display contracts.
- Update generation/package docs so runtime-ready packages include the new
  contract.
- Backfill the current twelve concept packages with display-bound metadata.
- Ensure verification policies are bound to the displayed asset or displayed
  option.
- Keep effect profile fields English-only.

## Delegated Agent Rule

The user explicitly requested parallel delegated-agent work for this planning
and follow-up implementation area.

Use sub-agents only for independent exploration, implementation, verification,
or code review with disjoint ownership. Good delegation candidates include
schema/validator tests, current-package backfill audit, documentation review,
and independent validation. Keep contract semantics and final integration local
to the main agent unless ownership is clear.

## Execution Rules

- Work in `wonderlens-activity-autodesign`.
- Use a git worktree before implementation changes unless the change is
  doc-only and the current checkout is appropriate.
- Preserve existing package contracts and validators unless the source plan
  explicitly changes them.
- Use conventional commits and do not push unless explicitly asked.
- Stage only intended files for this goal.

## Mandatory Ordering

1. Add schema, validator, and focused fixtures.
2. Update package/generation documentation.
3. Backfill the current twelve packages.
4. Run focused validation.
5. Update plan/goal indexes and handoff notes only after the implementation
   result is known.

## Preconditions

```bash
git status --short --branch
test -f docs/activity_display_contract.md
test -f activities/README.md
test -f activities/_schema/tag_block.schema.json
test -f program.md
```

If unrelated user changes are present, preserve them and stage only the
intended goal changes.

## Success Criteria

- `activity_display_contract_v1.yaml` has a documented package-local shape.
- Producer validation rejects unknown layout IDs and missing verification data
  for verifiable frames.
- Current twelve concept packages have display-bound contract metadata.
- The phoneme hunt package declares photo verification against the displayed
  initial-sound target.
- Choice, number, sort, echo, semantic, self-report, and participation policies
  are represented where needed.
- Existing package metadata validation still passes.
- No Chinese effect terms remain in the authored contract or plan.

## Required Checks

Minimum final checks:

```bash
git diff --check
python3 scripts/validate_demo_package_contract.py activities
python3 -m unittest tests.test_demo_package_contract_validator -v
python3 -m unittest tests.test_activity_display_contract_validator -v
python3 scripts/validate_activity_display_contract.py activities
```

Also run this tag-block schema validation from `AGENTS.md`:

```bash
python3 -c "
import json, yaml, pathlib, sys
from jsonschema import Draft202012Validator
schema = json.loads(pathlib.Path('activities/_schema/tag_block.schema.json').read_text())
v = Draft202012Validator(schema)
ok = True
for p in sorted(pathlib.Path('activities').glob('*/tag_block.yaml')):
    errs = list(v.iter_errors(yaml.safe_load(p.read_text())))
    print(('OK  ' if not errs else 'FAIL'), p)
    for e in errs:
        ok = False
        print(f'  {list(e.absolute_path)}: {e.message}')
sys.exit(0 if ok else 1)
"
```

If run-local current-twelve packages are updated, validate that path too.

## Final Completion Gate

Do not mark achieved until:

- required scope is implemented or a real blocker is documented with evidence;
- success criteria are met;
- required checks pass or missing local dependencies are documented;
- plan and goal indexes are updated as appropriate;
- handoff notes are updated when project state changes;
- no secrets are included in artifacts;
- intended changes are committed with a conventional commit message.

Final response must include changed files, checks run, sample package coverage,
remaining risks, and commit hashes.

## Goal Invocation

```text
/goal Implement goals/2026-06-23-activity-display-contract-v1-goal.md. Use sub-agents for independent work with disjoint ownership. Stop only when its completion gate is satisfied or a blocker is documented.
```
