# Data Source Examples

This file gives concrete examples for each input data source used by the current authoring workflow.

## 1. `assignments.md` Queue

Use this when the request is already close to a full package assignment.

```text
- [ ] assignment_type=entity_activity, entity=lion, category=cat1, tier=T0, mechanic=voice, pillar=Performance, style=voice_stage, mapping=animals_lion, start=warm+cold, activity_id=voice_stage_lion_example, scene=child photographs a toy lion on the playroom rug
```

Expected handling:

- Source of execution truth: `assignments.md`
- Input mode: `mapping_informed`
- Mapping lookup: `mapping=animals_lion` -> `MAPPING_ROOT/_index.yaml` -> `animals/big_cats.yaml`
- Canonical mechanic: `voice`
- Category decision: `cat1`
- Generation readiness: `ready_to_generate`

## 2. Activity Concept Row

Use this when PM, curriculum, or design provides an activity concept before a full entity package is specified.

Source row:

| Column | Example value |
|---|---|
| activity_concept | 颜色寻宝 |
| description | 孩子拍到一个有明显颜色的物体后，去找三个同色物品。 |
| mechanic | collect |
| category_hint | cat5 |
| product_notes | 不需要额外素材；只需要拍照和颜色匹配。 |

Assignment row:

```text
- [ ] assignment_type=activity_concept, activity_concept=颜色寻宝, description=孩子拍到一个有明显颜色的物体后，去找三个同色物品, mechanic=collect, category=cat5
```

Expected handling:

- Source of activity intent: activity concept row
- Input mode: `parameterized`
- Canonical mechanic: `collect`
- Focal attribute: `{matched_color}`
- Mapping required: `false`
- Generation readiness: `ready_to_generate`

## 3. Entity Mapping YAML

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

## 4. Runtime Matcher Placeholders

Use this when the activity should match many future entities rather than one mapped entity.

Assignment row:

```text
- [ ] assignment_type=match_pattern, activity_concept=形状分类, description=孩子拍到一个形状明显的物体后，把附近物品按相同形状和不同形状分组, mechanic=sort, category=cat5
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

## 5. Product Capability Notes

Use this when the activity concept depends on product support outside the current package workflow.

Assignment row:

```text
- [ ] assignment_type=capability_probe, activity_concept=涂色游戏, description=孩子拍一张物体照片，AI生成线稿并让孩子在屏幕上涂色, mechanic=build, category=cat5, product_capabilities=requires_assets,requires_ui_state
```

Expected handling:

- Input mode: `concept_only`
- Canonical mechanic: `build`
- Product capability flags: `requires_assets`, `requires_ui_state`
- Category decision: `unsupported_cat3` or `unsupported_cat4`, depending on final product framing
- Generation readiness: `blocked_until_product_decision`
- Output only the adaptation brief. Do not create package files, append `results.tsv`, or mark the assignment complete.
