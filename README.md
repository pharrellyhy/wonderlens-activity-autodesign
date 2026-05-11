# WonderLens Activity Auto-Designer

Prompt, template, and activity-package repository for generating and maintaining WonderLens educational activities.

The current runtime format is the migrated `activities/<activity_id>/` package. Legacy `designs/` files remain as reference and compatibility material, but new activity generation should target `activities/`.

Each autonomous `/goal` run also creates a provenance directory under `runs/<run_id>/`. The run directory records the assignment snapshot, adaptation briefs, blocked briefs, constrained blocked design previews, generated activity IDs, review notes, a static `review.html` dashboard, and a run manifest, so you can tell which run produced which packages without moving runtime files out of `activities/`.

## How It Works

The agent reads the authoring contract, runs a mechanic-first adaptation brief when the input is a concept-led assignment, carries any explicit asset dependency into the brief, composes a Template 0 spine with a mechanic adapter, Cat1/Cat5 category modifier, and pillar/style scaffold, then writes a complete five-file activity package:

```text
activities/<activity_id>/
├── spec.md
├── prod.md
├── tag_block.yaml
├── recap.template.yaml
└── dashboard.template.yaml
```

The same run writes provenance files separately:

```text
runs/<run_id>/
├── run_manifest.yaml
├── assignment_snapshot.md
├── generated_activity_ids.txt
├── adaptation_briefs/
├── blocked_briefs/
├── blocked_designs/
├── review_notes.md
└── review.html
```

Core files:

```text
GOAL.md                            Codex /goal objective and success criteria
program.md                         Agent instructions, adaptation brief, migrated output contract, rubric
templates.md                       Template 0 reference, mechanic adapters, pillar scaffolds, Cat1/Cat5 modifiers
run.md                             Autonomous activity-package loop
runs/README.md                     Run provenance directory contract
scripts/generate_run_review.py     Static run review dashboard generator and validator
activities/README.md               Five-file package rules and runtime invariants
activities/_schema/tag_block.schema.json
                                   Schema for tag_block.yaml
docs/activity_vocabulary.md        Closed enums for activity_signature fields
docs/game_styles.md                12 game styles under 6 experience pillars
entity_guidance.md                 Mapping schema and selection rules
conversation_bridge.md             Warm/cold bridge patterns
inputs/source_activity_concepts.md Active source concept rows referenced by assignments.md Batch 4
examples/                          Concrete input-source and input-mode examples
assignments.md                     Work queue
results.tsv                        Assignment and rubric log
```

## Activity Package Rules

- `spec.md` is for authors and reviewers. It owns exactly one `## Self-Evaluation Scorecard`.
- `prod.md` is runtime prompt guidance. It must not contain a scorecard.
- Every Step 3 round in `prod.md` must be fully expanded with AI dialogue, child response branches, AI follow-up branches, and screen state.
- Do not use condensed runtime placeholders such as "same structure," "AI gives a riddle," or one-line later-round summaries in migrated `prod.md` files.
- Every generated package must receive independent reviewer-agent PASS evidence before `results.tsv` logging or assignment checkoff; reviewer FAILs must be repaired and re-reviewed.
- If an activity uses pre-generated or displayed images, `spec.md` owns `## Asset Brief` with asset IDs, use timing, prompts/sources, display behavior, and fallback behavior. `prod.md` references asset IDs and fallback behavior only.
- `tag_block.yaml` must validate against `activities/_schema/tag_block.schema.json`.
- `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` must equal `tag_block.yaml` `activity_signature.focal_attribute`.
- `recap.template.yaml`, `dashboard.template.yaml`, `tag_block.yaml`, `spec.md`, and `prod.md` must describe the same mechanic, pillar, game style, focal attribute, badge/reward, and next-step direction.

## Quick Start

1. Edit `assignments.md` with the activity requests to generate.
2. Start your coding agent from the repo root.
3. Start the loop with the Codex `/goal` command:

```text
/goal Execute GOAL.md end to end using run.md. Initialize run provenance, audit/enrich existing checked activity packages against the current migrated package depth floor, using separate reviewer agents for package-quality review and repair evidence. Then process the run-start unchecked assignment snapshot exactly once in order. For each row, generate a five-file package that passes author self-check, independent reviewer-agent review, and package validation, or record a blocked brief plus a constrained blocked design preview and continue. In blocked previews, still design detailed runtime steps, but annotate each unsupported dependency inline with BLOCKED ELEMENT comments and keep the activity invalid until the blocker is resolved. Do not append results.tsv or mark a generated assignment complete until reviewer issues are repaired and re-reviewed. After final validation, generate and validate a self-contained light-theme review dashboard at runs/<run_id>/review.html with direct activity detail cards, sortable Cat1/Cat3/Cat5/status/mechanic controls, constrained blocked-preview links, and classified blocked-reason badges. Stop only on a hard workflow failure that makes later rows unsafe. Use GOAL.md success criteria as the completion contract and report generated, enriched, blocked, reviewer-agent coverage, review dashboard path, checks, and residual risks.
```

`GOAL.md` defines the run objective, success criteria, and completion contract. `run.md` defines the step-by-step execution loop.

For generation-ready assignments, the loop creates one complete `activities/<activity_id>/` package, self-evaluates against the 10-dimension rubric, gets independent reviewer-agent PASS evidence, updates `results.tsv`, marks the assignment complete, and records the package in `runs/<run_id>/run_manifest.yaml`. Blocked concept-led assignments write a blocked brief under `runs/<run_id>/blocked_briefs/` and a constrained design preview under `runs/<run_id>/blocked_designs/`. These previews still show detailed proposed runtime steps with inline `BLOCKED ELEMENT` comments, but they are not logged, packaged, or marked complete until the constraints are resolved. They no longer halt the rest of the batch.

## Run Provenance

Use `runs/<run_id>/` to distinguish one autonomous generation session from another.

- `run_id` format is `YYYYMMDD_HHMMSS_<short_label>`, using local operator time, for example `20260509_113000_activity_concepts`.
- `assignment_snapshot.md` preserves the unchecked assignment rows at run start.
- `adaptation_briefs/` stores Phase 0 briefs for generated concept-led or underspecified assignments.
- `blocked_briefs/` stores briefs for assignments that reach `readiness=blocked_until_product_decision`.
- `blocked_designs/` stores constrained design previews for blocked assignments; these are human-review artifacts, not valid runtime packages.
- `generated_activity_ids.txt` lists packages created by that run in completion order.
- `review_notes.md` stores independent reviewer-agent coverage, repair notes, and residual risks for generated and enriched packages.
- `review.html` is the static human review dashboard generated by `scripts/generate_run_review.py`; it includes activity detail cards with concrete runtime beats, sortable/filterable package and blocked-assignment views, constrained preview links, reviewer coverage, checks, classified blocked reasons, and a reason guide explaining what each blocker means.
- `run_manifest.yaml` is the run-level index linking assignment rows, generated `activities/<activity_id>/` packages, blocked briefs, constrained design previews, results logging, checks, and timestamps.

Runtime packages are never nested inside `runs/`; the run layer is provenance only. See `runs/README.md` for the manifest template and update rules.

## Input Data Sources

The generation loop now separates **activity intent**, **asset dependency**, and **entity grounding**. A request can start from a photographed entity, an activity concept brief, a reusable property/category pattern, explicit visual assets, or a mix of those sources.

Current entity mapping root:

```text
MAPPING_ROOT=data/mappings_dev20_0318
```

`mapping=` values are entity IDs, not paths. Resolve them by opening `MAPPING_ROOT/_index.yaml`, then loading the relative YAML file listed for that entity. If the mapping data moves, update `MAPPING_ROOT` in the current authoring docs and keep `_index.yaml` at the new root.

| Source | Typical fields | Required when | How the agent uses it |
|---|---|---|---|
| `assignments.md` queue | unchecked line with `assignment_type`, `entity`, `activity_concept`, `concept_source`, `description`, `category`, `mechanic`, `tier`, `scene`, `mapping`, `asset_policy`, `asset_requirements`, `product_capabilities` | Always. This is the execution queue the loop reads. | Normalizes the request, loads referenced concept/asset rows when present, runs Phase 0 when needed, then either generates a package or records a blocked brief plus constrained design preview and continues. |
| Activity Concept Brief | concept row plus optional companion asset requirement rows | The starting point is a source/curriculum/design concept rather than a full entity package request. This is the preferred source for concept-led work. | Produces an English `adaptation_brief` first. The brief decides input mode, readiness, trigger fit, asset dependency, mapping use, and scaffold fit. |
| Asset Requirements table | `asset_id`, `concept_ref`, `asset_type`, `requiredness`, `generation_timing`, `use_step`, `purpose`, `prompt_en`, `source`, `display_behavior`, `fallback_behavior`, `safety_constraints` | The idea mentions or requires AI-generated images, screen-displayed reference images, line art, cards, icons, overlays, or visual supports. | Avoids asset inference from prose. Phase 0 copies the rows into `asset_dependency`; `spec.md` records an `## Asset Brief`; `prod.md` references stable asset IDs. |
| Entity mapping YAML | `mapping=<entity_id>` resolved through `MAPPING_ROOT/_index.yaml` | Required only for mapping-informed packages, entity-specific factual claims, warm/cold bridge grounding, mapping-grounded Key Concepts, or matcher-ready entity routing. | Grounds visible attributes, tier language, IB concepts, related concepts, bridge prerequisites, trigger fit, and matchability. |
| Runtime matcher placeholders | `{matched_color}`, `{matched_shape}`, `{entity_class}`, or similar placeholders | Activity concept is property/category driven but no specific photographed entity is supplied. | Supports `parameterized` briefs and packages that can be matched later across many entities without inventing entity-specific facts. |
| Product capability notes | `product_capabilities=...`, concept comments, or explicit UI/material/runtime-generation assumptions | The idea depends on UI state, runtime image generation, materials, motion safety, OCR, pose detection, or before/after state. | Sets `product_capability_flags`; unsupported dependencies should produce `readiness=blocked_until_product_decision`, a blocked brief, and a constrained design preview instead of a forced package. |

### Preferred Concept Source

Ask concept owners / curriculum authors to provide concept-led ideas as two linked tables. This is better than a prose-only document because asset needs become explicit dependencies instead of things the generator must detect.

Source concept names and comments may arrive in Chinese, but generated artifacts must be English-only. Normalize assignment `description=`, `trigger_condition=`, adaptation brief fields, package files, asset brief rows, and runtime dialogue to English before generation.

Use `examples/source_activity_concept_template.md` as the blank fillable template. Filled source concept files should follow the same field names so assignment rows can reference `concept_source=file#source_id` and `asset_requirements=file#asset_id` directly.

Concept table:

| Field | Example |
|---|---|
| `assignment_type` | `activity_concept` |
| `activity_concept` | `Animal Shadow Guess` |
| `description` | `Screen shows an animal silhouette. The child uses clues to guess the animal and explain the evidence.` |
| `mechanic` | `deduce` |
| `category` | `cat1` |
| `trigger_condition` | `Child photographs an animal toy, an animal picture, or enters animal theme mode.` |
| `entity_scope` | `animal_class` |
| `asset_policy` | `required_prebuilt` |
| `asset_requirements` | `shadow_card_set_01` |
| `product_capabilities` | `requires_asset_display` |

Asset requirements table:

| Field | Example |
|---|---|
| `asset_id` | `shadow_card_set_01` |
| `concept_ref` | `Animal Shadow Guess` |
| `asset_type` | `card_set` |
| `requiredness` | `required` |
| `generation_timing` | `pre_generated` |
| `use_step` | `prod.step_2`, `prod.step_3.round_1-3` |
| `purpose` | `Give the child visible animal silhouette evidence to inspect.` |
| `prompt_en` | `Create a set of animal silhouette cards for children ages 4-6. Use a plain white background, clear black silhouettes, recognizable animal outlines, no text, and a non-scary style.` |
| `source` | `new_ai_generated_asset` |
| `display_behavior` | `Show one silhouette card full screen each round while the AI gives one voice clue.` |
| `fallback_behavior` | `If cards are unavailable, switch to a voice-only animal riddle and do not claim the screen is showing a picture.` |
| `safety_constraints` | `No scary mood, no real child photos, and no text in the image.` |

`asset_policy` values:

| Value | Meaning | Generation behavior |
|---|---|---|
| `no_assets` | Activity does not need visual assets beyond normal camera/photo UI. | Proceed without `## Asset Brief`. |
| `optional_support` | Visuals improve the activity but are not required. | Proceed only with explicit fallback behavior. |
| `required_prebuilt` | Activity depends on assets that can be generated or sourced before runtime. | Proceed with assumptions only if every asset row is complete; otherwise block. |
| `runtime_generated` | Activity depends on image generation during the session. | Block unless product support is explicitly declared. |
| `blocked` | Source or design owner knows the idea needs unresolved asset/product work. | Write a blocked brief and constrained design preview; keep it out of valid packages until resolved. |

The activity package loop does **not** generate image files. It writes directly usable English prompts into `spec.md` `## Asset Brief` so a separate asset pipeline can create or approve visuals later.

Use these assignment types in new rows:

| Assignment type | Use when | Typical input mode |
|---|---|---|
| `entity_activity` | A specific photographed entity or entity class should become an activity package. | `mapping_informed` when `mapping=` is supplied |
| `activity_concept` | A source, curriculum, or design concept describes the desired child experience before entity grounding is final. | `parameterized` or `concept_only` |
| `match_pattern` | The activity is a reusable property/category pattern that runtime matching can fill later. | `parameterized` |
| `capability_probe` | The row tests whether a product-dependent concept can be generated under current capabilities. | `concept_only`, often blocked |

Use these Phase 0 input modes:

| Mode | Best input shape | Mapping requirement | Output behavior |
|---|---|---|---|
| `mapping_informed` | `entity + category + mapping=<entity_id>` or an activity concept tied to a specific photographed entity/entity class | Required | Full package may use concrete mapped attributes, tier language, IB concepts, and warm/cold bridges. |
| `parameterized` | Activity concept about a property or category, such as color hunt, shape sort, animal sounds, or find-three-things | Optional | Package or brief uses runtime placeholders and stays matcher-ready without claiming specific entity facts. |
| `concept_only` | Broad activity mechanic or product concept with no entity or match criterion yet | Optional | Usually produces an adaptation brief; full generation proceeds only if the current Cat1/Cat5 package workflow can represent the idea safely. |

Default to `parameterized` for activity concepts driven by properties, categories, or reusable match rules. Use `mapping_informed` only when a concrete mapping source is supplied. Lack of mapping should not block an adaptation brief, but it should block full generation when the package would otherwise need mapping-grounded facts or routing.

See `examples/source_activity_concept_template.md` for the fillable template. See `examples/data_sources.md`, `examples/input_modes.md`, and `inputs/source_activity_concepts.md` for concrete assignment rows, selected source concepts, asset rows, and expected adaptation brief snippets.

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

For asset-dependent concepts, keep the assignment row compact and put the full asset details in the companion concept brief:

```text
- [ ] assignment_type=activity_concept, activity_concept=Animal Shadow Guess, description=Screen shows an animal silhouette and the child uses clues to guess the animal, mechanic=deduce, category=cat1, asset_policy=required_prebuilt, asset_requirements=shadow_card_set_01, product_capabilities=requires_asset_display
```

Required:

- Either `entity + category`, such as `lion + category 1 (sustained verbal)`, or `activity_concept + description/mechanic` for a concept-led assignment.
- `category=` when known. If it is unknown, Phase 0 must infer `cat1`, `cat5`, or an unsupported category decision before generation.

Recommended:

- `tier=` when the target tier is known.
- `mechanic=` as the primary child-action hint. Valid values are `enumerate`, `compare`, `collect`, `sort`, `deduce`, `build`, `predict`, `decide`, `remember`, `imagine`, `care`, and `motion_voice`.
- `scene=` with concrete photo context.
- `assignment_type=` for new rows. Valid values are `entity_activity`, `activity_concept`, `match_pattern`, and `capability_probe`.
- `description=` for concept-led rows so the adaptation brief can preserve the intended child experience.
- `asset_policy=` when the concept has any screen-displayed or AI-generated visual dependency. Use `no_assets`, `optional_support`, `required_prebuilt`, `runtime_generated`, or `blocked`.

Optional:

- `pillar=` and `style=` when you want to force a specific experience format.
- `mapping=` when the entity should be grounded in `MAPPING_ROOT`; pair it with `start=warm+cold` for dual bridge handling.
- `concept_source=file#concept_id` when the assignment should load a companion source concept brief before Phase 0.
- `activity_id=` when you need a specific package directory name.
- `asset_requirements=file#asset_id` when an assignment row points to a companion asset table/YAML block.
- `product_capabilities=` when an idea depends on asset display, runtime image generation, UI state, material workflows, motion safety, OCR, pose detection, or before/after state.

Prefer `mechanic=` over `style=` when you only know what the child should do. If `mechanic=` is present and `style=` is omitted, the agent infers pillar and game style from the mechanic, entity affordances, category, and `program.md` section 1.6. Concept-led rows first produce an `adaptation_brief`; blocked ideas also get a constrained design preview with inline blocked-element comments instead of forcing package generation, and the loop continues to later unchecked rows. Legacy concept aliases should not be used in new rows. Older completed rows may contain retired style tokens such as `voice_acting`, `storytelling_chain`, `prediction_game`, `helper_hotline`, `comparison_chart`, or `naming_story`; keep them as legacy history, not templates for new rows.

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
├── runs/
│   ├── README.md
│   └── <run_id>/
│       ├── run_manifest.yaml
│       ├── assignment_snapshot.md
│       ├── generated_activity_ids.txt
│       ├── adaptation_briefs/
│       ├── blocked_briefs/
│       ├── blocked_designs/
│       ├── review_notes.md
│       └── review.html
├── scripts/
│   └── generate_run_review.py
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
