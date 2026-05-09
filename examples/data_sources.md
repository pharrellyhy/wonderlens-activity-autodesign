# Data Source Examples

This file gives concrete examples for each input data source used by the current authoring workflow.

## 1. `assignments.md` Queue

Use this when the request is already close to a full package assignment.

```text
- [ ] assignment_type=entity_activity, entity=lion, category=cat1, tier=T0, mechanic=motion_voice, pillar=Performance, style=voice_stage, mapping=animals_lion, start=warm+cold, activity_id=voice_stage_lion_example, scene=child photographs a toy lion on the playroom rug
```

Expected handling:

- Source of execution truth: `assignments.md`
- Input mode: `mapping_informed`
- Mapping lookup: `mapping=animals_lion` -> `MAPPING_ROOT/_index.yaml` -> `animals/big_cats.yaml`
- Canonical mechanic: `motion_voice`
- Category decision: `cat1`
- Generation readiness: `ready_to_generate`

## 2. Activity Concept Row

Use this when a source, curriculum, or design owner provides an activity concept before a full entity package is specified.

Source row:

| Column | Example value |
|---|---|
| activity_concept | Color Hunt |
| description | Child photographs an object with a clear color, then finds three things with the same color. |
| mechanic | collect |
| category_hint | cat5 |
| asset_policy | no_assets |
| product_notes | No extra visual assets are needed; the activity only needs photo capture and color matching. |

Assignment row:

```text
- [ ] assignment_type=activity_concept, activity_concept=Color Hunt, description=Child photographs an object with a clear color, then finds three things with the same color, mechanic=collect, category=cat5, asset_policy=no_assets
```

Expected handling:

- Source of activity intent: activity concept row
- Input mode: `parameterized`
- Canonical mechanic: `collect`
- Focal attribute: `{matched_color}`
- Mapping required: `false`
- Asset dependency: `asset_policy=no_assets`
- Generation readiness: `ready_to_generate`

## 3. Activity Concept Brief with Asset Requirements

Use this when the concept asks for AI-generated images, prebuilt pictures, card sets, or screen-displayed visual supports.

Concept table row:

| Column | Example value |
|---|---|
| activity_concept | Animal Shadow Guess |
| description | Screen shows an animal silhouette. The child uses AI clues to guess the animal and explain the visible evidence. |
| mechanic | deduce |
| category_hint | cat1 |
| trigger_condition | Child photographs an animal toy, an animal picture, or enters animal theme mode. |
| entity_scope | animal_class |
| asset_policy | required_prebuilt |
| asset_requirements | shadow_card_set_01 |
| product_notes | Requires prebuilt animal silhouette display; runtime image generation is not needed. |

Asset requirements row:

| Column | Example value |
|---|---|
| asset_id | shadow_card_set_01 |
| concept_ref | Animal Shadow Guess |
| asset_type | card_set |
| requiredness | required |
| generation_timing | pre_generated |
| use_step | prod.step_2; prod.step_3.round_1-3 |
| purpose | Give the child visible animal outline evidence to inspect. |
| prompt_en | Create a set of animal silhouette cards for children ages 4-6. Use a plain white background, clear black silhouettes, recognizable outlines for common animals such as a cat, bird, and fish, no text, and a non-scary style. |
| source | new_ai_generated_asset |
| display_behavior | Show one silhouette card full screen each round while the AI gives one voice clue. |
| fallback_behavior | If cards are unavailable, switch to a voice-only animal riddle and do not claim the screen is showing a picture. |
| safety_constraints | No real child photos, no attack scenes, and no text in the image. |

Assignment row:

```text
- [ ] assignment_type=activity_concept, activity_concept=Animal Shadow Guess, description=Screen shows an animal silhouette and the child uses AI clues to guess the animal and explain the evidence, mechanic=deduce, category=cat1, asset_policy=required_prebuilt, asset_requirements=shadow_card_set_01, product_capabilities=requires_asset_display
```

Expected handling:

- Source of activity intent: Activity Concept Brief
- Source of asset dependency: Asset Requirements table
- Input mode: `concept_only` or `parameterized`, depending on whether runtime animal class matching is supplied
- Canonical mechanic: `deduce`
- Product capability flags: `requires_assets`, `requires_asset_display`
- Asset dependency: `required_prebuilt`, with a required `card_set`
- Generation readiness: `generate_with_assumptions` if asset display is supported and fallback is explicit; otherwise `blocked_until_product_decision`
- Package behavior: `spec.md` includes `## Asset Brief`; `prod.md` references `asset_id=shadow_card_set_01` and the fallback, not the raw prompt.

## 4. Entity Mapping YAML

Use this when the package must make entity-specific claims or use mapped IB / tier guidance.

Assignment row:

```text
- [ ] double rainbow + category 5 (collection/tracking), tier=T1, mechanic=deduce, pillar=Mystery, style=mystery_trail, mapping=natural_phenomena_double_rainbow, start=warm+cold, scene=child photographs a double rainbow after rain
```

Mapping resolution:

```yaml
# MAPPING_ROOT/_index.yaml
natural_phenomena_double_rainbow: natural_phenomena/rainbows.yaml
```

Concrete mapped values available from `MAPPING_ROOT/natural_phenomena/rainbows.yaml`:

```yaml
primary_theme:
  theme_id: how_world_works
primary_key_concepts:
  - causation
  - form
  - change
example_attributes:
  - tier_0.appearance.colors: many bright colors
  - tier_0.appearance.brightness: one bright, one faint
  - tier_1.appearance.second_arc_faintness: A lighter second bow, like a whisper of colors
  - tier_1.appearance.color_order_swap: Outer rainbow can have colors in reverse order
```

Expected handling:

- Input mode: `mapping_informed`
- Mapping required: `true`
- Entity role: `subject`
- Observation angle: `pattern` or `state`
- Missing mapping risk: `high`, because the package uses specific rainbow facts.

## 5. Runtime Matcher Placeholders

Use this when the activity should match many future entities rather than one mapped entity.

Assignment row:

```text
- [ ] assignment_type=match_pattern, activity_concept=Shape Sort, description=Child photographs an object with a clear shape, then groups nearby objects by same shape and different shape, mechanic=sort, category=cat5
```

Expected placeholder values:

```yaml
focal_attribute: "{matched_shape}"
trigger_condition: "runtime matcher identifies a clear dominant shape in the photographed entity"
entity_role: exemplar
mapping_use:
  required: false
  available: false
  value_if_available: ["attributes", "matchability"]
```

Expected handling:

- Input mode: `parameterized`
- Mapping required: `false`
- Do not claim specific facts about the photographed entity.
- Use placeholders such as `{matched_shape}` and `{entity_class}` until runtime fills them.

## 6. Product Capability Notes

Use this when the activity concept depends on product support outside the current package workflow.

Assignment row:

```text
- [ ] assignment_type=capability_probe, activity_concept=Coloring Game, description=Child photographs an object, AI generates line art, and the child colors it on screen, mechanic=build, category=cat5, asset_policy=runtime_generated, asset_requirements=line_art_from_photo, product_capabilities=requires_generated_image,requires_line_art,requires_ui_state
```

Expected handling:

- Input mode: `concept_only`
- Canonical mechanic: `build`
- Product capability flags: `requires_assets`, `requires_generated_image`, `requires_line_art`, `requires_ui_state`
- Asset dependency: `runtime_generated`, required `line_art`
- Category decision: `unsupported_cat3` or `unsupported_cat4`, depending on final product framing
- Generation readiness: `blocked_until_product_decision`
- Output only the adaptation brief. Do not create package files, append `results.tsv`, or mark the assignment complete.
