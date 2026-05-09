# Source Activity Concept Template

Use this file as the fillable input format for concept owners and curriculum authors.

Source concepts may start in any language, but every field used by generation must be normalized to English. The generator should use the `*_en` fields below and should not copy raw source-language prose into adaptation briefs or activity packages.

## How To Fill This Out

1. Create one concept section per activity idea under `Concept Rows`.
2. If the concept needs images, cards, line art, icons, overlays, or screen-displayed support, add one asset section under `Asset Requirements`.
3. Use stable lowercase IDs:
   - concept IDs: `source_<short_snake_case_name>`
   - asset IDs: `<short_snake_case_name>_01`
4. In `assignments.md`, reference these sections with:

```text
concept_source=examples/source_activity_concept_template.md#source_<short_snake_case_name>
asset_requirements=examples/source_activity_concept_template.md#<asset_id>
```

For a filled reference, see `examples/source_activity_concept_briefs.md`.

## Concept Rows

Copy this block once per activity concept.

### source_<short_snake_case_name>

| Field | Value |
|---|---|
| source_row | <optional source row number or source doc label> |
| source_original_name | <optional original concept name, any language; provenance only> |
| activity_concept | <English normalized concept name> |
| normalized_description_en | <1-2 sentences describing the child experience and core loop in English> |
| normalized_notes_en | <English notes about quality bar, constraints, difficulty, variants, or source intent> |
| assignment_type | <entity_activity|activity_concept|match_pattern|capability_probe> |
| input_mode_hint | <mapping_informed|parameterized|concept_only> |
| mechanic | <enumerate|compare|collect|sort|deduce|build|predict|decide|remember|imagine|care|motion_voice> |
| category | <cat1|cat5|unknown|unsupported_cat2|unsupported_cat3|unsupported_cat4|unsupported_cat6> |
| tier | <T0|T1|T2|unknown> |
| entity_scope | <specific entity, entity class, runtime placeholder, or mode-selected concept> |
| mapping | <optional entity_id from MAPPING_ROOT, or blank> |
| asset_policy | <no_assets|optional_support|required_prebuilt|runtime_generated|blocked> |
| asset_requirements | <comma-separated asset IDs, or blank> |
| product_capabilities | <comma-separated capability flags, or blank> |
| trigger_condition_en | <best moment to trigger this activity, in English> |
| adaptation_notes_en | <English notes for how to adapt this concept to the current workflow> |

## Asset Requirements

Copy this block once per asset or asset set.

### <asset_id>

| Field | Value |
|---|---|
| asset_id | <same as heading> |
| concept_ref | <source_<short_snake_case_name>> |
| asset_type | <reference_image|character_image|scene_background|line_art|card_set|icon|ui_overlay> |
| requiredness | <required|optional|fallback> |
| generation_timing | <pre_generated|runtime_generated|display_existing|none> |
| use_step | <exact use point, such as prod.step_2 or prod.step_3.round_1-3> |
| purpose_en | <why this asset exists in the activity loop> |
| prompt_en | <direct English image-generation prompt, required for generated assets> |
| source | <new_ai_generated_asset|existing_asset_library|approved_reference_set|future_runtime_image_generation|none> |
| display_behavior_en | <how runtime presents the asset> |
| fallback_behavior_en | <what the activity does if the asset is unavailable> |
| safety_constraints_en | <visual safety, privacy, realism, age-appropriateness, and text constraints> |

## Assignment Row Templates

Use one of these rows after the concept section is filled.

### Activity Concept

```text
- [ ] assignment_type=activity_concept, activity_concept=<English normalized concept name>, concept_source=examples/source_activity_concept_template.md#source_<short_snake_case_name>, description=<English normalized description>, mechanic=<mechanic>, category=<cat1|cat5|unknown>, tier=<T0|T1|T2>, asset_policy=<asset_policy>, asset_requirements=examples/source_activity_concept_template.md#<asset_id>, product_capabilities=<capability_flags>, activity_id=<concept_activity_id>, trigger_condition=<English trigger condition>
```

Omit `asset_requirements=` and `product_capabilities=` when they do not apply.

### Match Pattern

```text
- [ ] assignment_type=match_pattern, activity_concept=<English normalized pattern name>, concept_source=examples/source_activity_concept_template.md#source_<short_snake_case_name>, description=<English reusable match pattern>, mechanic=<mechanic>, category=<cat5>, tier=<T0|T1|T2>, asset_policy=<asset_policy>, activity_id=<concept_activity_id>, trigger_condition=<English trigger condition>
```

### Capability Probe

```text
- [ ] assignment_type=capability_probe, activity_concept=<English normalized concept name>, concept_source=examples/source_activity_concept_template.md#source_<short_snake_case_name>, description=<English product-dependent concept>, mechanic=<mechanic>, category=<cat1|cat5|unknown|unsupported_cat3>, tier=<T0|T1|T2>, asset_policy=<asset_policy>, asset_requirements=examples/source_activity_concept_template.md#<asset_id>, product_capabilities=<required_capability_flags>, activity_id=<concept_activity_id>, trigger_condition=<English trigger condition>
```

## Allowed Values

### Assignment Type

| Value | Use when |
|---|---|
| `entity_activity` | A specific photographed entity or entity class should become an activity package. |
| `activity_concept` | The source concept describes the child experience before entity grounding is final. |
| `match_pattern` | The activity is a reusable property/category pattern that runtime matching can fill later. |
| `capability_probe` | The row tests whether a product-dependent concept can be generated under current capabilities. |

### Mechanic

| Value | Child action loop |
|---|---|
| `enumerate` | Notice, identify, count, or measure -> AI confirms/extends -> next attribute/part |
| `compare` | Inspect A/B -> child states same/different/preference/evidence -> AI names contrast |
| `collect` | Mission criterion -> child finds/matches/pairs/photos -> AI reacts -> set synthesis |
| `sort` | Rule or child-made rule -> group/rank/sequence items -> explain organizing logic |
| `deduce` | Clue/evidence -> child infers/guesses -> child justifies -> AI reveals or gives next clue |
| `build` | Material/idea prompt -> child creates/assembles/transforms/experiments -> AI adds/combines |
| `predict` | Commit guess/hypothesis/plan -> reveal/result/action -> tally or consequence |
| `decide` | Options appear -> child chooses/corrects -> AI applies consequence or explains correction |
| `remember` | Encode/show/hear -> delay or distract -> child recalls/repeats/retells -> AI confirms and extends |
| `imagine` | Story/pretend setup -> child adds choice/detail/roleplay/retell -> AI weaves or summarizes |
| `care` | Need or feeling appears -> child proposes help -> AI shows gratitude/impact |
| `motion_voice` | Motion/sound/role prompt -> child moves, imitates, or speaks in role -> AI reacts as audience/partner |

### Asset Policy

| Value | Meaning |
|---|---|
| `no_assets` | No visual assets beyond normal camera/photo UI. |
| `optional_support` | Visuals improve the activity but are not required; fallback is mandatory. |
| `required_prebuilt` | Activity depends on assets that can be generated or sourced before runtime. |
| `runtime_generated` | Activity depends on image generation during the session; usually blocks unless product support is declared. |
| `blocked` | Source owner already knows unresolved asset/product work must be decided first. |

### Product Capability Flags

Use comma-separated values when relevant:

```text
requires_assets,requires_asset_display,requires_generated_image,requires_coloring_ui,requires_ui_state,requires_materials,requires_motion_safety,ocr_risk,pose_risk,before_after_risk
```

## Readiness Checklist

Before adding the assignment row:

- `activity_concept`, `normalized_description_en`, `mechanic`, `category`, `asset_policy`, and `trigger_condition_en` are filled.
- Any non-`no_assets` concept has at least one asset section or a clear reason to block.
- Every generated asset has a direct English `prompt_en`.
- Every shown asset has `display_behavior_en` and `fallback_behavior_en`.
- `runtime_generated`, material workflow, motion safety, OCR, pose, and before/after state dependencies are declared in `product_capabilities`.
- The assignment row is English-only.
