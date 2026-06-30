# Activity Dialogue Source Guards Implementation Plan

**Goal:** Tighten four runtime-verified activity packages so their rule/intro steps clearly and warmly state what the activity will do, and their source guards keep runtime redirects grounded.

**Architecture:** Keep package changes local to the four activity packages. The package should describe source intent, allowed clue/asset sequence, and redirect boundaries; WonderLens AI runtime consumes those constraints separately.

**Tech Stack:** Markdown/YAML activity packages, tag-block schema validation, focused text scans.

---

## Scope

Activities:
- `concept_animal_sound_motion_voice`
- `concept_emotion_reader_care`
- `concept_partial_reveal_deduce`
- `concept_phoneme_hunt_collect`

Required behavior:
- Rules/intro copy should feel like a warm web-demo hook: clear, short, task-setting.
- Rules should not invite extra play beyond the actual first round/collect action.
- `idk` and off-topic handling should redirect to the current activity task.
- Package text should not encourage unrelated praise, story expansion, invented clues, or unsupported options.

Out of scope:
- No new layout contract.
- No asset regeneration.
- No broad rewrite of all packages.
- No WonderLens AI runtime code changes in this repo.

## Task 1: Rules/Intro Source Copy

**Files:**
- Modify: `activities/concept_animal_sound_motion_voice/prod.md`
- Modify: `activities/concept_emotion_reader_care/prod.md`
- Modify: `activities/concept_partial_reveal_deduce/prod.md`
- Modify: `activities/concept_phoneme_hunt_collect/prod.md`

**Steps:**
1. Update the rules/intro guidance so each package clearly states the loop:
   - Animal Sound: hear/see rabbit, cat, puppy; make one safe sound each round.
   - Emotion Reader: look at each picture and name the feeling.
   - Partial Reveal: use each visible clue to make a maybe-guess; answer waits for final reveal.
   - Phoneme Hunt: first photo chooses the starting letter; later photos find more names with that same first letter.
2. Keep the wording concise and child-facing.
3. Do not add exact-script-only constraints unless already present.

## Task 2: Tag-Block Source Guards

**Files:**
- Modify: `activities/concept_animal_sound_motion_voice/tag_block.yaml`
- Modify: `activities/concept_emotion_reader_care/tag_block.yaml`
- Modify: `activities/concept_partial_reveal_deduce/tag_block.yaml`
- Modify: `activities/concept_phoneme_hunt_collect/tag_block.yaml`

**Steps:**
1. Add or tighten package-local guidance for redirect behavior.
2. Preserve existing enums and schema-compatible structure.
3. Avoid reintroducing bounded dialogue contracts removed by the rollback.

## Task 3: Validation

Run:

```bash
git diff --check
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

If local Python lacks `yaml` or `jsonschema`, validate with the WonderLens AI Python environment and report that explicitly.
