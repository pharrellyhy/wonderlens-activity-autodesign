# Four Package Runtime Verification Authoring Goal

## Mode

Plan-backed.

## Objective

Update the producer-authored activity packages and docs for four runtime
verification behaviors that do not use `activity_display_contract_v1.yaml`.

## Design Source

Source plan:

- `docs/plans/2026-06-24-four-package-runtime-verification-authoring.md`

Consumer companion plan:

- `/Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-06-24-activity-response-verification-without-display-contract.md`

The source plan is authoritative for producer package authoring. The consumer
plan is authoritative for WonderLens AI runtime behavior. If they conflict,
stop and document the conflict before editing package behavior.

## Hard Constraints

- Do not create or depend on `activity_display_contract_v1.yaml` for the four
  target packages.
- Do not claim unsupported verification capability.
- Preserve package compatibility unless a rename is implemented end to end.
- Do not edit unrelated generated package prose.
- Do not edit secrets, credentials, production data, or machine-specific config.
- Do not perform unrelated refactors, formatting sweeps, or dependency
  upgrades.

## Required Scope

- `concept_phoneme_hunt_collect`: change package semantics from fixed B phoneme
  hunt to in-activity seed-photo first-letter hunt, or document any blocker.
- `concept_emotion_reader_care`: align response targets with active cue.
- `concept_partial_reveal_deduce`: remove child-visible answer leakage before
  final reveal and preserve final verification target.
- `concept_animal_sound_motion_voice`: declare transcript-verifiable targets per
  animal round.
- Keep WonderLens AI runtime mirrors aligned.
- Update plan/goal indexes and `HANDOFF.md` when package behavior changes.

## Delegated Agent Rule

The user explicitly requested parallel sub-agents with dedicated goals. Use
sub-agents only for independent package audits, implementation, verification,
or code review with disjoint ownership. Keep final package/runtime alignment
and commits local to the main executor.

## Execution Rules

- Work in `wonderlens-activity-autodesign`.
- Use the active worktree:
  `/Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/response-verification-packages`
- Use conventional commits and do not push unless explicitly asked.
- Stage only intended package/doc changes.

## Success Criteria

- The four packages express correct runtime-verification intent without display
  contract files.
- Producer package text and WonderLens AI runtime package mirrors agree on
  first-letter seed, emotion cue, partial reveal hidden answer, and animal
  transcript verification behavior.
- Existing demo package and tag-block validation still pass.

## Required Checks

```bash
python3 scripts/validate_demo_package_contract.py activities
python3 -m unittest tests.test_demo_package_contract_validator -v
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
rg -n "activity_display_contract_v1" activities/concept_phoneme_hunt_collect activities/concept_emotion_reader_care activities/concept_partial_reveal_deduce activities/concept_animal_sound_motion_voice
git diff --check
```

The `rg` command is expected to exit 1 with no matches for the target package
directories.

## Final Completion Gate

Do not mark achieved until intended package/docs changes are made or a blocker
is documented, required checks pass or missing dependencies are documented,
consumer runtime alignment is confirmed, indexes and handoff are updated, no
secrets are included, and intended changes are committed.

## Goal Invocation

```text
/goal Implement goals/2026-06-24-four-package-runtime-verification-authoring-goal.md. Coordinate with the WonderLens AI runtime goal and stop only when the completion gate is satisfied or a blocker is documented.
```
