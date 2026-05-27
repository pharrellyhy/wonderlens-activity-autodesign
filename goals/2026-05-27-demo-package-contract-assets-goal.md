# Demo Package Contract And Assets Goal

## Mode

Plan-backed.

## Objective

Implement the autodesign-side demo package contract so generated activity
packages can declare fullstack-demo support status, explicit entity bindings,
separate runtime asset requirements, device-compatible visual style, and
unsupported mechanic gates.

## Design Source

- Plan: `docs/plans/2026-05-27-demo-package-contract-assets.md`
- Consumer follow-up:
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/docs/plans/2026-05-27-autodesign-package-demo-import.md`

The linked plan is authoritative for design rationale and implementation
context. This goal is authoritative for constraints, required checks, and
completion. If they conflict, stop and document the conflict before changing
behavior.

## Hard Constraints

- Keep the existing five package files as the required canonical package
  contract.
- Add demo and asset data as optional package-local extension files, not as raw
  prose in `prod.md`.
- Do not make contact sheets the runtime asset format.
- Do not allow real-world factual/reference assets, such as constellations,
  artworks, maps, scientific diagrams, cultural artifacts, species, historical
  objects, or named places, to be represented by arbitrary generated images.
- Do not claim unsupported mechanics are playable.
- Do not implement fullstack demo code in this repo.
- Do not edit secrets, credentials, production data, or machine-local config.
- Do not perform unrelated refactors, broad formatting sweeps, or dependency
  upgrades.

## Required Scope

- Define and document `demo_support.yaml`.
- Define and document `asset_manifest.yaml`.
- Add schemas or equivalent validators for the new demo extension files.
- Update generation instructions so future demo-targeted packages request
  separate assets, not a single prebuilt contact sheet.
- Define the `wonderlens_device_mint_soft_3d` visual style, palette, sizes,
  variants, and round-screen safe-area rules.
- Define reference-bound asset rules for real-world factual assets, including
  source/provenance requirements and verification behavior.
- Add deterministic support classification for `supported`, `degraded`, and
  `unsupported` demo mechanics.
- Validate at least one Cat1 sample, one simple Cat5 sample, and one
  unsupported or degraded example.

## Execution Rules

- Work in `wonderlens-activity-autodesign`.
- Treat fullstack demo consumption as a separate goal that should execute after
  this contract is merged, or against a pinned fixture from this goal.
- Preserve tag-block enum compatibility unless a schema and vocabulary update
  is explicitly required and validated.
- Keep generated binary assets out of canonical packages unless the repo's
  current asset workflow explicitly supports committing them.
- Use conventional commits and do not push unless explicitly asked.

## Mandatory Ordering

1. Update the package contract and schema/validator design.
2. Update generation instructions.
3. Add or update sample fixtures.
4. Run validation.
5. Update plan and goal indexes to `Completed` or `Blocked` only after the
   implementation result is known.

## Preconditions

```bash
git status --short --branch
test -f activities/README.md
test -f program.md
test -f templates.md
test -f activities/_schema/tag_block.schema.json
```

If the working tree contains unrelated user changes, preserve them and stage
only the intended files for this goal.

## Success Criteria

- `demo_support.yaml` has a documented and validated shape.
- `asset_manifest.yaml` has a documented and validated shape.
- The asset contract defines separate runtime assets, roles, prompts, target
  variants, file path slots, fallback behavior, and round-screen safe areas.
- Reference-bound assets require approved sources or provenance and cannot pass
  validation as random generated approximations.
- The prototype-device visual style is expressed in generation instructions.
- Support gating distinguishes supported Cat1/Cat5, degraded Cat5 judgment,
  and unsupported UI-heavy mechanics.
- Existing five-file package validation and tag-block schema validation still
  pass.
- Sample packages or fixtures demonstrate the contract.

## Required Checks

Minimum final checks:

```bash
git diff --check
```

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

If a demo manifest validator or fixtures are added, run the focused validator
against those samples and include the exact command in the final response.

## Final Completion Gate

Do not mark achieved until:

- required scope is implemented or a real blocker is documented with evidence;
- success criteria are met;
- required checks pass;
- plan and goal indexes are updated as appropriate;
- intended changes are committed with a conventional commit message.

Final response must include changed files, checks run, sample coverage,
remaining risks, and commit hashes.

## Goal Invocation

```text
/goal Implement goals/2026-05-27-demo-package-contract-assets-goal.md. Stop only when its completion gate is satisfied or a blocker is documented.
```
