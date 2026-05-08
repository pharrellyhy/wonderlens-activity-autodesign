# WonderLens Activity Auto-Designer

Prompt, template, and activity-package repository for generating and maintaining WonderLens educational activities.

The current runtime format is the migrated `activities/<activity_id>/` package. Legacy `designs/` files remain as reference and compatibility material, but new activity generation should target `activities/`.

## How It Works

The agent reads the authoring contract, runs a mechanic-first adaptation brief when the input is a concept-led assignment, composes a Template 0 spine with a mechanic adapter, Cat1/Cat5 category modifier, and pillar/style scaffold, then writes a complete five-file activity package:

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
GOAL.md                            Codex /goal objective and success criteria
program.md                         Agent instructions, adaptation brief, migrated output contract, rubric
templates.md                       Template 0 reference, mechanic adapters, pillar scaffolds, Cat1/Cat5 modifiers
run.md                             Autonomous activity-package loop
activities/README.md               Five-file package rules and runtime invariants
activities/_schema/tag_block.schema.json
                                   Schema for tag_block.yaml
docs/activity_vocabulary.md        Closed enums for activity_signature fields
docs/game_styles.md                12 game styles under 6 experience pillars
entity_guidance.md                 Mapping schema and selection rules
conversation_bridge.md             Warm/cold bridge patterns
examples/                          Concrete input-source and input-mode examples
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
3. Start the loop with the Codex `/goal` command:

```text
/goal Run the WonderLens autonomous activity generation loop from GOAL.md. Process unchecked assignments.md rows in order using run.md. Continue until all generation-ready assignments are completed or the first blocked/failing assignment needs a product/design decision. Use the success criteria in GOAL.md as the completion contract.
```

`GOAL.md` defines the run objective, success criteria, and completion contract. `run.md` defines the step-by-step execution loop.

For generation-ready assignments, the loop creates one complete `activities/<activity_id>/` package, self-evaluates against the 10-dimension rubric, updates `results.tsv`, marks the assignment complete, and commits the package unless instructed otherwise. Blocked concept-led assignments stop at the `adaptation_brief` and are not logged or marked complete.

## Input Data Sources

The generation loop now separates **activity intent** from **entity grounding**. A request can start from a photographed entity, an activity concept row, a reusable property/category pattern, or a mix of those sources.

Current entity mapping root:

```text
MAPPING_ROOT=data/mappings_dev20_0318
```

`mapping=` values are entity IDs, not paths. Resolve them by opening `MAPPING_ROOT/_index.yaml`, then loading the relative YAML file listed for that entity. If the mapping data moves, update `MAPPING_ROOT` in the current authoring docs and keep `_index.yaml` at the new root.

| Source | Typical fields | Required when | How the agent uses it |
|---|---|---|---|
| `assignments.md` queue | unchecked line with `assignment_type`, `entity`, `activity_concept`, `description`, `category`, `mechanic`, `tier`, `scene`, `mapping`, `product_capabilities` | Always. This is the execution queue the loop reads. | Normalizes the request, runs Phase 0 when needed, then either generates a package or stops with an adaptation brief. |
| Activity concept row | `assignment_type=activity_concept`, `activity_concept`, `description`, concept notes, desired mechanic, product assumptions | The starting point is a lightweight activity concept rather than a full entity package request. | Produces an `adaptation_brief` first. The brief decides whether the idea is `concept_only`, `parameterized`, or `mapping_informed`, and whether generation is ready, assumption-based, or blocked. |
| Entity mapping YAML | `mapping=<entity_id>` resolved through `MAPPING_ROOT/_index.yaml` | Required only for mapping-informed packages, entity-specific factual claims, warm/cold bridge grounding, mapping-grounded Key Concepts, or matcher-ready entity routing. | Grounds visible attributes, tier language, IB concepts, related concepts, bridge prerequisites, trigger fit, and matchability. |
| Runtime matcher placeholders | `{matched_color}`, `{matched_shape}`, `{entity_class}`, or similar placeholders | Activity concept is property/category driven but no specific photographed entity is supplied. | Supports `parameterized` briefs and packages that can be matched later across many entities without inventing entity-specific facts. |
| Product capability notes | `product_capabilities=...`, concept comments, or explicit UI/asset/material assumptions | The idea depends on assets, UI state, materials, motion safety, OCR, pose detection, or before/after state. | Sets `product_capability_flags`; unsupported dependencies should produce `readiness=blocked_until_product_decision` instead of a forced package. |

Use these assignment types in new rows:

| Assignment type | Use when | Typical input mode |
|---|---|---|
| `entity_activity` | A specific photographed entity or entity class should become an activity package. | `mapping_informed` when `mapping=` is supplied |
| `activity_concept` | A PM, curriculum, or design concept describes the desired child experience before entity grounding is final. | `parameterized` or `concept_only` |
| `match_pattern` | The activity is a reusable property/category pattern that runtime matching can fill later. | `parameterized` |
| `capability_probe` | The row tests whether a product-dependent concept can be generated under current capabilities. | `concept_only`, often blocked |

Use these Phase 0 input modes:

| Mode | Best input shape | Mapping requirement | Output behavior |
|---|---|---|---|
| `mapping_informed` | `entity + category + mapping=<entity_id>` or an activity concept tied to a specific photographed entity/entity class | Required | Full package may use concrete mapped attributes, tier language, IB concepts, and warm/cold bridges. |
| `parameterized` | Activity concept about a property or category, such as color hunt, shape sort, animal sounds, or find-three-things | Optional | Package or brief uses runtime placeholders and stays matcher-ready without claiming specific entity facts. |
| `concept_only` | Broad activity mechanic or product concept with no entity or match criterion yet | Optional | Usually produces an adaptation brief; full generation proceeds only if the current Cat1/Cat5 package workflow can represent the idea safely. |

Default to `parameterized` for activity concepts driven by properties, categories, or reusable match rules. Use `mapping_informed` only when a concrete mapping source is supplied. Lack of mapping should not block an adaptation brief, but it should block full generation when the package would otherwise need mapping-grounded facts or routing.

See `examples/data_sources.md` and `examples/input_modes.md` for concrete assignment rows and expected adaptation brief snippets.

## Working With `assignments.md`

`assignments.md` is the agent's queue. Each unchecked line (`- [ ]`) is one pending package request; checked lines (`- [x]`) are treated as complete and skipped. The loop processes the file from top to bottom.

Use this shape for new assignments:

```text
- [ ] entity + category 5 (collection/tracking), tier=T1, mechanic=collect, pillar=Adventure, style=quest_collector, mapping=optional_entity_id, start=warm+cold, activity_id=optional_slug, scene=child photographs ...
```

For concept-led activity ideas, use:

```text
- [ ] assignment_type=activity_concept, activity_concept=Scavenger Hunt, description=find X things with a shared color or shape, mechanic=collect, category=cat5
```

Required:

- Either `entity + category`, such as `lion + category 1 (sustained verbal)`, or `activity_concept + description/mechanic` for a concept-led assignment.
- `category=` when known. If it is unknown, Phase 0 must infer `cat1`, `cat5`, or an unsupported category decision before generation.

Recommended:

- `tier=` when the target tier is known.
- `mechanic=` as the primary child-action hint. Valid values are `enumerate`, `compare`, `collect`, `sort`, `deduce`, `voice`, `build`, `predict`, `narrate`, and `care`.
- `scene=` with concrete photo context.
- `assignment_type=` for new rows. Valid values are `entity_activity`, `activity_concept`, `match_pattern`, and `capability_probe`.
- `description=` for concept-led rows so the adaptation brief can preserve the intended child experience.

Optional:

- `pillar=` and `style=` when you want to force a specific experience format.
- `mapping=` when the entity should be grounded in `MAPPING_ROOT`; pair it with `start=warm+cold` for dual bridge handling.
- `activity_id=` when you need a specific package directory name.
- `product_capabilities=` when an idea depends on assets, UI state, material workflows, motion safety, OCR, pose detection, or before/after state.

Prefer `mechanic=` over `style=` when you only know what the child should do. If `mechanic=` is present and `style=` is omitted, the agent infers pillar and game style from the mechanic, entity affordances, category, and `program.md` section 1.6. Concept-led rows first produce an `adaptation_brief`; blocked ideas stop at the brief instead of forcing package generation. `pm_idea=` is a legacy alias for `activity_concept=` and should not be used in new rows. Older completed rows may contain retired style tokens such as `voice_acting`, `storytelling_chain`, `prediction_game`, `helper_hotline`, `comparison_chart`, or `naming_story`; keep them as legacy history, not templates for new rows.

To rerun an assignment, change its checkbox back to `- [ ]`. To add work, append a new unchecked line in the appropriate batch section or create a new batch heading.

## Project Structure

```text
.
├── README.md
├── GOAL.md
├── program.md
├── templates.md
├── run.md
├── assignments.md
├── results.tsv
├── entity_guidance.md
├── conversation_bridge.md
├── examples/
│   ├── README.md
│   ├── data_sources.md
│   └── input_modes.md
├── data/
│   └── mappings_dev20_0318/
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

## Mechanics, Adaptation Briefs, and Game Styles

`activity_signature.mechanic` is the primary action signal for selector fit, runtime recap phrasing, and parent analytics. `game_style` remains required metadata, but it is a secondary package format chosen to express the mechanic under a pillar.

When an assignment is concept-led rather than a full entity package request, `program.md` Phase 0 creates an `adaptation_brief` with input mode, canonical mechanic, readiness, trigger condition, mapping use, product capability flags, and scaffold fit. Entity mapping YAML is useful for grounding and matchability, but concept-only and parameterized briefs can proceed without mapping unless the package claims entity-specific facts or mapping-informed routing.

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
