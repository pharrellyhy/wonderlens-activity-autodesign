# Four Package Runtime Verification Authoring

Date: 2026-06-24

Status: Active

## Goal

Update the producer-authored package guidance and package files for four
activities so WonderLens AI can verify the child response from existing runtime
package metadata, without using `activity_display_contract_v1.yaml`.

Consumer companion work lives in:

```text
/Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-06-24-activity-response-verification-without-display-contract.md
```

## Scope

Target packages:

- `concept_phoneme_hunt_collect`
- `concept_emotion_reader_care`
- `concept_partial_reveal_deduce`
- `concept_animal_sound_motion_voice`

For these four packages, the runtime verification source is the existing
package shape: `prod.md`, `spec.md`, `tag_block.yaml`, `demo_support.yaml`,
`asset_manifest.yaml`, recap/dashboard templates, and WonderLens AI
`runtime.yaml` mirrors. Do not create or depend on
`activity_display_contract_v1.yaml` for this task.

## Required Authoring Changes

### Shared Dialogue Quality Rules

For these runtime-verified packages, child-facing dialogue must be a short
bridge to the next expected action, not a general chatbot response:

1. The rules step explains only the rule; it does not invite the first action.
2. Round asks use one direct instruction or question.
3. Retry directions are direct and state the current expected action.
4. Success directions briefly acknowledge the accepted response and ask the next
   task directly.
5. Internal labels such as `Cue`, `Card Voice`, package IDs, scenario IDs, and
   runtime field names are never child-facing.
6. Binary choices are used only when the activity intentionally accepts those
   exact alternatives.
7. Hidden-answer activities may acknowledge a `maybe-guess`, but must not say
   `you guessed it`, `correct`, or equivalent before the final answer outcome is
   known.

### First-Letter Hunt

`concept_phoneme_hunt_collect` should become a first-letter seed-photo hunt:

1. The first in-activity photo becomes the seed object.
2. Vision recognition normalizes the seed object name.
3. Runtime derives the first normalized English character.
4. Later photos must match that same first character.

Prefer keeping the existing activity ID for compatibility unless all consumer
selectors and fixtures are renamed in the same goal. Change child-facing prose
from phoneme/sound/B to first letter/starting letter.

### Emotion Reader

`concept_emotion_reader_care` must tie accepted responses to the active visible
cue. Generic caring language that ignores the displayed cue should not be enough
to advance.

### Partial Reveal

`concept_partial_reveal_deduce` must avoid child-visible answer leakage before
the final reveal. Internal answer metadata is allowed for final verification,
but early prompts, screen labels, examples, and branch text must use neutral
clue language.

### Animal Sound Imitation

`concept_animal_sound_motion_voice` must declare a verifiable transcript-based
response target per round. Do not claim acoustic classification; use accepted
tokens/role words derived from STT text unless WonderLens AI implements a real
audio classifier.

## Validation

Producer-side checks:

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

The `rg` command should return no package-local display-contract dependency for
these four packages.

## Risks

- The existing package name contains `phoneme`; broad renaming has selector and
  fixture blast radius. Prefer first-letter wording inside the package unless a
  coordinated rename is explicitly chosen.
- The runtime mirror in WonderLens AI must remain aligned with producer
  package text and metadata.
- Partial reveal can store the answer internally only if the child never sees
  it before the final reveal.
