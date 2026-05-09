# Input Mode Examples

This file gives one concrete Phase 0 example for each `adaptation_brief.input_mode`.

## 1. `mapping_informed`

Use when the activity concept or assignment is tied to a specific mapped entity.

Assignment row:

```text
- [ ] assignment_type=entity_activity, entity=lion, category=cat1, tier=T0, mechanic=voice, pillar=Performance, style=voice_stage, mapping=animals_lion, start=warm+cold, scene=child photographs a toy lion on the playroom rug
```

Expected brief:

```yaml
adaptation_brief:
  input_mode: mapping_informed
  core_promise: "Child speaks as a lion and explores what lion body features and sounds communicate."
  canonical_mechanic: voice
  mechanic_confidence: high

  category_decision: cat1
  readiness: ready_to_generate

  trigger_condition: "Photo is recognized as lion or lion-like toy, with visible face/body features."
  entity_role: subject
  observation_angle: behavior
  focal_attribute: "roar / lion voice"

  mapping_use:
    required: true
    available: true
    value_if_available: ["attributes", "tier language", "bridge prerequisites", "IB concepts", "matchability"]
    missing_mapping_risk: high

  product_capability_flags: []

  asset_dependency:
    policy: no_assets
    assets: []
    missing_asset_risk: none

  scaffold_choice:
    pillar: Performance
    game_style: voice_stage
    scaffold_fit: strong

  assumptions:
    - "A toy lion photo may use the lion mapping as the conceptual subject when the child is pretending."
```

Why this mode fits:

- `mapping=animals_lion` exists in `MAPPING_ROOT/_index.yaml`.
- The package can use lion-specific mapped attributes such as `tier_0.senses.sound` and `tier_1.appearance.mane_look`.
- Warm/cold bridge handling can be grounded in the mapped entity.

## 2. `parameterized`

Use when the activity concept is about a reusable property or category and runtime can fill the specific entity/attribute.

Assignment row:

```text
- [ ] assignment_type=match_pattern, activity_concept=Same-Color Collection, description=Child photographs an object with a clear color, then finds and photographs three things with the same color, mechanic=collect, category=cat5
```

Expected brief:

```yaml
adaptation_brief:
  input_mode: parameterized
  core_promise: "Child turns one visible color into a collection mission."
  canonical_mechanic: collect
  mechanic_confidence: high

  category_decision: cat5
  readiness: ready_to_generate

  trigger_condition: "Runtime matcher identifies a clear dominant color on the photographed entity."
  entity_role: exemplar
  observation_angle: color
  focal_attribute: "{matched_color}"

  mapping_use:
    required: false
    available: false
    value_if_available: ["attributes", "matchability"]
    missing_mapping_risk: low

  product_capability_flags: []

  asset_dependency:
    policy: no_assets
    assets: []
    missing_asset_risk: none

  scaffold_choice:
    pillar: Adventure
    game_style: quest_collector
    scaffold_fit: strong

  assumptions:
    - "Runtime can provide a stable color placeholder before the activity starts."
```

Why this mode fits:

- The activity concept does not need a specific mapped entity.
- The activity can stay honest with placeholders such as `{matched_color}`.
- The repeated child action is clearly `collect`: find/photo more items.

## 3. `concept_only`

Use when the activity concept describes a broad mechanic or product concept without a usable entity or runtime match condition yet.

Assignment row:

```text
- [ ] assignment_type=activity_concept, activity_concept=Branching Choice Story, description=Each round, the child chooses what happens next and the AI weaves those choices into one continuous story, mechanic=narrate, category=cat1
```

Expected brief:

```yaml
adaptation_brief:
  input_mode: concept_only
  core_promise: "Child co-authors a branching story by choosing what happens next."
  canonical_mechanic: narrate
  mechanic_confidence: high

  category_decision: cat1
  readiness: generate_with_assumptions

  trigger_condition: "Parent or child starts story mode, or a photographed object is used only as a story spark."
  entity_role: catalyst
  observation_angle: function
  focal_attribute: "story choice"

  mapping_use:
    required: false
    available: false
    value_if_available: ["tier language", "bridge prerequisites"]
    missing_mapping_risk: low

  product_capability_flags: []

  asset_dependency:
    policy: no_assets
    assets: []
    missing_asset_risk: none

  scaffold_choice:
    pillar: Creation
    game_style: inventor_workshop
    scaffold_fit: acceptable

  assumptions:
    - "The photographed entity, if any, is only a story spark and not a source of factual claims."
    - "The activity remains voice-led and does not require visual branching UI."
```

Why this mode fits:

- The idea is a mechanic-first activity concept, not an entity-grounded package request.
- Mapping is optional because no entity-specific fact is needed.
- The brief should preserve the assumption that the current Cat1 workflow can run the story through dialogue only.

## 4. `concept_only` blocked variant

Some concept-only assignments should stop at the brief.

Assignment row:

```text
- [ ] assignment_type=capability_probe, activity_concept=Guided Drawing, description=Child uses paper and pencil to draw something inspired by the photo, then AI continues from the offline work, mechanic=build, category=cat3, product_capabilities=requires_materials,before_after_risk
```

Expected brief result:

```yaml
readiness: blocked_until_product_decision
category_decision: unsupported_cat3
product_capability_flags:
  - requires_materials
  - before_after_risk
asset_dependency:
  policy: no_assets
  assets: []
  missing_asset_risk: none
```

Why it blocks:

- The current migrated package workflow supports Cat1/Cat5 generation, not a Cat3 material workflow.
- The activity depends on tracking an offline before/after drawing state.
- The agent should output the brief only and avoid forcing a production package.

## 5. `concept_only` with required visual assets

Use when the concept is not entity-grounded but does require prebuilt or generated visuals.

Assignment row:

```text
- [ ] assignment_type=activity_concept, activity_concept=Animal Picture Pair, description=Screen shows two animal pictures and the child names one similarity and one difference, mechanic=compare, category=cat1, asset_policy=required_prebuilt, asset_requirements=animal_pair_cards_01, product_capabilities=requires_asset_display
```

Expected brief excerpt:

```yaml
adaptation_brief:
  input_mode: concept_only
  core_promise: "Child compares animal pictures by naming same/different visible features."
  canonical_mechanic: compare
  mechanic_confidence: high

  category_decision: cat1
  readiness: generate_with_assumptions

  trigger_condition: "Parent or child starts animal picture compare mode, or a photographed animal toy acts as a topic spark."
  entity_role: reference
  observation_angle: pattern
  focal_attribute: "animal visual features"

  mapping_use:
    required: false
    available: false
    value_if_available: ["tier language", "matchability"]
    missing_mapping_risk: low

  product_capability_flags:
    - requires_assets
    - requires_asset_display

  asset_dependency:
    policy: required_prebuilt
    assets:
      - asset_id: animal_pair_cards_01
        asset_type: card_set
        requiredness: required
        generation_timing: pre_generated
        use_step: "prod.step_2 and prod.step_3"
        prompt_en: "Create animal picture-pair cards for children ages 4-6. Each pair should show two animals side by side with simple backgrounds, clear poses, visible features for comparison, and no text."
        source: "new_ai_generated_asset"
        display_behavior: "Each round displays two cards side by side while AI asks for one similarity or difference."
        fallback_behavior: "If cards are unavailable, switch to verbal comparison of two named animals and do not reference on-screen pictures."
    missing_asset_risk: medium
```

Why this mode fits:

- The activity depends on visual assets, but the concept is not tied to a specific mapped entity.
- The asset requirement is explicit, so the generator does not need to infer image needs from prose.
- `prod.md` can reference `asset_id=animal_pair_cards_01`; `spec.md` owns the image prompt.
