# WonderLens Activity Auto-Designer

Prompt, template, and activity-package repository for generating and maintaining WonderLens educational activities.

The current runtime format is the migrated `activities/<activity_id>/` package. Legacy `designs/` files remain as reference and compatibility material, but new activity generation should target `activities/`.

## How It Works

The agent reads the authoring contract, composes a Template 0 spine with a pillar overlay and Cat1/Cat5 category modifier, then writes a complete five-file activity package:

```text
activities/<activity_id>/
├── spec.md
├── prod.md
├── tag_block.yaml
├── recap.template.yaml
└── dashboard.template.yaml
```

Core files:

```text
program.md                         Agent instructions, migrated output contract, rubric
templates.md                       Template 0 reference, pillar overlays, Cat1/Cat5 modifiers
run.md                             Autonomous activity-package loop
activities/README.md               Five-file package rules and runtime invariants
activities/_schema/tag_block.schema.json
                                   Schema for tag_block.yaml
docs/activity_vocabulary.md        Closed enums for activity_signature fields
docs/game_styles.md                12 game styles under 6 experience pillars
entity_guidance.md                 Mapping schema and selection rules
conversation_bridge.md             Warm/cold bridge patterns
assignments.md                     Work queue
results.tsv                        Assignment and rubric log
```

## Activity Package Rules

- `spec.md` is for authors and reviewers. It owns exactly one `## Self-Evaluation Scorecard`.
- `prod.md` is runtime prompt guidance. It must not contain a scorecard.
- Every Step 3 round in `prod.md` must be fully expanded with AI dialogue, child response branches, AI follow-up branches, and screen state.
- Do not use condensed runtime placeholders such as "same structure," "AI gives a riddle," or one-line later-round summaries in migrated `prod.md` files.
- `tag_block.yaml` must validate against `activities/_schema/tag_block.schema.json`.
- `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` must equal `tag_block.yaml` `activity_signature.focal_attribute`.
- `recap.template.yaml`, `dashboard.template.yaml`, `tag_block.yaml`, `spec.md`, and `prod.md` must describe the same mechanic, pillar, game style, focal attribute, badge/reward, and next-step direction.

## Quick Start

1. Edit `assignments.md` with the activity requests to generate.
2. Start your coding agent from the repo root.
3. Ask it to run the package loop:

```text
Read program.md, templates.md, activities/README.md, activities/_schema/tag_block.schema.json, docs/activity_vocabulary.md, docs/game_styles.md, entity_guidance.md, conversation_bridge.md, run.md, and assignments.md. Then begin the autonomous activity package loop.
```

The loop creates one complete `activities/<activity_id>/` package per assignment, self-evaluates against the 10-dimension rubric, updates `results.tsv`, marks the assignment complete, and commits the package unless instructed otherwise.

## Working With `assignments.md`

`assignments.md` is the agent's queue. Each unchecked line (`- [ ]`) is one pending package request; checked lines (`- [x]`) are treated as complete and skipped. The loop processes the file from top to bottom.

Use this shape for new assignments:

```text
- [ ] entity + category 5 (collection/tracking), tier=T1, mechanic=collect, pillar=Adventure, style=quest_collector, mapping=optional_entity_id, start=warm+cold, activity_id=optional_slug, scene=child photographs ...
```

Required:

- Entity and category, such as `lion + category 1 (sustained verbal)`.

Recommended:

- `tier=` when the target tier is known.
- `mechanic=` as the primary child-action hint. Valid values are `enumerate`, `compare`, `collect`, `sort`, `deduce`, `voice`, `build`, `predict`, `narrate`, and `care`.
- `scene=` with concrete photo context.

Optional:

- `pillar=` and `style=` when you want to force a specific experience format.
- `mapping=` when the entity should be grounded in `data/mappings_dev20_0318/`; pair it with `start=warm+cold` for dual bridge handling.
- `activity_id=` when you need a specific package directory name.

Prefer `mechanic=` over `style=` when you only know what the child should do. If `mechanic=` is present and `style=` is omitted, the agent infers pillar and game style from the mechanic, entity affordances, category, and `program.md` section 1.6. Older completed rows may contain retired style tokens such as `voice_acting`, `storytelling_chain`, `prediction_game`, `helper_hotline`, `comparison_chart`, or `naming_story`; keep them as legacy history, not templates for new rows.

To rerun an assignment, change its checkbox back to `- [ ]`. To add work, append a new unchecked line in the appropriate batch section or create a new batch heading.

## Project Structure

```text
.
├── README.md
├── program.md
├── templates.md
├── run.md
├── assignments.md
├── results.tsv
├── entity_guidance.md
├── conversation_bridge.md
├── activities/
│   ├── README.md
│   ├── _schema/
│   │   └── tag_block.schema.json
│   └── <activity_id>/
│       ├── spec.md
│       ├── prod.md
│       ├── tag_block.yaml
│       ├── recap.template.yaml
│       └── dashboard.template.yaml
├── designs/
│   ├── cat1/
│   └── cat5/
└── docs/
    ├── activity_vocabulary.md
    ├── game_styles.md
    └── plans/
```

## Mechanics and Game Styles

`activity_signature.mechanic` is the primary action signal for selector fit, runtime recap phrasing, and parent analytics. `game_style` remains required metadata, but it is a secondary package format chosen to express the mechanic under a pillar.

There are 12 game styles under 6 experience pillars:

| Pillar | Cat1 style | Cat5 style |
|---|---|---|
| Mystery | `mystery_lens` | `mystery_trail` |
| Creation | `inventor_workshop` | `mix_lab` |
| Performance | `voice_stage` | `ensemble_show` |
| Discovery | `prediction_lab` | `field_experiment` |
| Adventure | `time_traveler` | `quest_collector` |
| Nurture | `care_station` | `rescue_team` |

See `docs/game_styles.md` for definitions, migration notes, and coverage.

## Current Coverage

- Migrated runtime packages: 5 activities in `activities/`.
- Legacy/reference designs: existing Cat1 and Cat5 prod/spec files under `designs/`.
- Backend consumers may support both during migration, but new generation should use `activities/`.

## Validation

Run from the repo root.

```bash
git diff --check
```

Validate migrated tag blocks when `jsonschema` and `pyyaml` are installed:

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

Check focal-attribute alignment:

```bash
ruby -e 'require "yaml"; ok=true; Dir["activities/*/tag_block.yaml"].sort.each { |tag_path| dir=File.dirname(tag_path); dash=File.join(dir,"dashboard.template.yaml"); next unless File.exist?(dash); tag=YAML.load_file(tag_path); dashboard=YAML.load_file(dash); unless tag.dig("activity_signature","focal_attribute") == dashboard.dig("dashboard_fragment","session","focal_attribute"); ok=false; warn "FAIL #{dir}"; end }; puts(ok ? "OK focal_attribute equality" : "FAIL focal_attribute equality"); exit(ok ? 0 : 1)'
```

Check runtime completeness:

```bash
rg -n 'Same structure|AI gives riddle|later rounds follow|Only played if child is highly engaged|Condensed later' activities/*/prod.md
```

No output from the runtime completeness scan means no known condensed-round placeholder was found.

## Legacy Transform Workflow

`transform.md` and `transform_run.md` are retained only for the old `designs/*_spec.md` to `designs/*_prod.md` workflow and the aggregated legacy docs. Do not use them for migrated `activities/*/prod.md` files.

## Iterating

After review:

1. If generated packages miss structure, update `program.md`, `run.md`, or `activities/README.md`.
2. If activity mechanics feel weak, update the relevant pillar overlay in `templates.md`.
3. If metadata drifts, update `activities/_schema/tag_block.schema.json`, `docs/activity_vocabulary.md`, or the package self-checks.
4. Add new assignments to `assignments.md` and rerun the package loop.

## License

MIT
