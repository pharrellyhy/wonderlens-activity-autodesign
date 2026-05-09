# Activity Tag Block Usage Guide

> Supplement to `docs/plans/2026-04-23-activity-signature-design.md` and `docs/activity_vocabulary.md`. Use this when authoring or reviewing `activities/<activity_id>/tag_block.yaml`. For the complete tag block plus progression-algorithm map, see `docs/activity_tag_block_progression_guide.md`.

**Version:** 0.2 · 2026-05-09

---

## 1 · Why this guide exists

The tag block is now doing three jobs:

1. It lets the upstream matcher decide whether an activity can and should follow the current child moment.
2. It lets runtime compose the activity start, recap, and dashboard payloads.
3. It gives curriculum/product reviewers a stable way to audit what the activity teaches.

Those jobs should not be mentally mixed. A field can be stored in one YAML block but still have one clear primary consumer.

---

## 2 · Field Ownership At A Glance

| Group | Primary consumer | Fields |
|---|---|---|
| Catalog identity | Loader, sync scripts, reviewers | `activity_id`, `version`, `source_entity_exemplar`, `template_type`, `pillar`, `game_style` |
| Upstream eligibility | Matcher | `entity`, `entity_class`, `entity_binding`, `tier_range`, `matchability.entity_class_filter`, `matchability.tier_support` |
| Upstream coherence | Matcher, selector | `activity_signature.observation_angle`, `activity_signature.bridge_prerequisites.primary`, `activity_signature.bridge_prerequisites.secondary`, `activity_signature.entity_role`, `activity_signature.role_pivot_note` |
| Runtime presentation | Activity start, script agent, recap copy | `activity_signature.focal_attribute`, `activity_signature.intro`, `activity_signature.preview_label`, `activity_signature.preview_prompt`, `activity_signature.mechanic` |
| Parent dashboard | Parent dashboard, growth path, curriculum analytics | `key_concepts`, `atl_skills`, `transdisciplinary_theme`, `subject_tags` when present, `progression.*`, `activity_signature.observation_angle`, `activity_signature.mechanic`, `activity_signature.entity_role`, `caregiver_role` |
| Child recap | Recap renderer, child-facing recap template | `entity`, `pillar`, `related_concepts`, `atl_skills`, `activity_signature.observation_angle`, `activity_signature.mechanic`, `activity_signature.entity_role`, `activity_signature.focal_attribute`; game-specific recap copy lives in `recap.template.yaml` |
| Authoring audit | Reviewers, prompt authors | `attributes`, `kud.*`, `category`, `related_concepts`, `spec.md` rationale, `spec.md` `## Asset Brief` when assets are used |

Rule of thumb: if a field changes which activity is selected, it is upstream. If it changes what the parent sees over time, it is downstream. If it only explains author intent, keep it out of matching logic.

---

## 3 · Upstream Fields

These fields help the matcher answer two questions:

1. **Can this activity run for the detected entity and child tier?**
2. **Should this activity follow the conversation that just happened?**

### 3.1 Eligibility: can it run?

| Field | How to set it | Example | Notes |
|---|---|---|---|
| `entity` | Use the bound entity for gold-standard activities; use a placeholder for parameterized property activities. | `lion`, `{parameterized_by_matched_property}` | Runtime may replace the placeholder with the detected entity. |
| `entity_class` | Ordered class chain from specific to broad. Leave empty only when runtime fills it for wide parameterized activities. | `[lion, big_cat, mammal, animal]` | Used for rollup when exact entity match misses. |
| `entity_binding` | `bound` for exact-entity activities, `parameterized` for reusable entity/property activities, `agnostic` only when the entity truly does not matter. | `parameterized` | Do not mark an activity `agnostic` if the script names specific entity properties. |
| `tier_range.primary` | The age register the activity is written for. | `T1` | This is authoring intent, not the child's runtime tier. |
| `tier_range.span` | The supported neighboring tiers. | `[T0, T1, T2]` | Use narrow spans when language/task structure cannot safely stretch. |
| `tier_range.elasticity` | Human-readable rule for how far the activity can flex. | `±1`, `neighbor`, `strict` | Existing files use string values; keep the value understandable to reviewers. |
| `matchability.entity_class_filter` | List classes this activity accepts. Empty means wide. | `[]`, `[insect, patterned_thing]` | Use this to prevent an otherwise parameterized activity from matching nonsensical entities. |
| `matchability.tier_support` | Boolean support matrix for tiers. | `{T0: yes, T1: yes, T2: yes}` | Should agree with `tier_range.span`. |

Eligibility means an activity may enter the selector's candidate set. It is not the same as being selected. An activity is eligible only when the tag block is valid, the child tier is allowed by both `tier_range.span` and `matchability.tier_support`, the photographed entity satisfies `entity_binding`, any `entity_class_filter` passes, required runtime properties can be resolved, and safety/runtime availability checks pass.

Binding examples:

| Binding | Typical `entity_class_filter` | Eligibility example |
|---|---|---|
| `bound` | Narrow: `[big_cat]`, `[butterfly]`, `[ladybug]` | A lion activity can enter only for lion/big-cat contexts where copy remains coherent. |
| `parameterized` | Wide `[]` for universal property hunts; restricted `[patterned_thing]`, `[animal]`, `[plant]` when needed | Color Scout can enter for any safe entity with a resolvable `{matched_color}`. |
| `agnostic` | Usually `[]` or `[observable_thing]` | A general "name three things you notice" warm-up can enter for almost any safe recognizable photo. |

### 3.2 Coherence: should it follow this conversation?

| Field | How to set it | Example | Notes |
|---|---|---|---|
| `activity_signature.observation_angle` | Pick the one primary attribute/dimension the activity attends to. | `color`, `quantity`, `emotion` | Closed enum; see `docs/activity_vocabulary.md`. Orthogonal to `progression.topic_axis`. |
| `activity_signature.bridge_prerequisites.primary` | 1-3 closed observation angles that make the activity a natural continuation. | `[color]`, `[behavior, function]` | Schema enforces the same 12-value enum as `observation_angle`. |
| `activity_signature.bridge_prerequisites.secondary` | 0-3 supporting angles or editorial descriptors. | `[pattern, visibility]`, `[sound, context]` | Prefer enum values; non-enum notes are allowed but not scored as structured angles. |
| `activity_signature.entity_role` | Say how the photographed entity participates in the activity. | `subject`, `exemplar`, `catalyst`, `reference` | Drives pivot handling and recap/dashboard phrasing. |
| `activity_signature.role_pivot_note` | Explain subject-to-exemplar/catalyst/reference shifts in one sentence. | "The ladybug becomes an example of red." | Empty or omit only when the role stays continuous. |

`observation_angle` and `progression.topic_axis` deliberately answer different questions:

```yaml
activity_signature:
  observation_angle: quantity   # what the child attends to
progression:
  topic_axis: change            # what conceptual lens the child practices
```

That example means: the child is attending to amount, but the learning move is noticing how amount changes.

---

## 4 · Runtime Presentation Fields

These fields shape what happens at activity start and what gets stored after the session.

| Field | How to set it | Example | Notes |
|---|---|---|---|
| `activity_signature.mechanic` | Pick the child's primary action. | `collect`, `compare`, `deduce`, `care` | This is not the same as `game_style`; many styles can share one mechanic. |
| `activity_signature.focal_attribute` | Concrete attribute value or placeholder rendered at runtime. | `red`, `{matched_color}`, `more_less` | Match the chosen `observation_angle`. |
| `activity_signature.intro` | One third-person sentence for observer-facing activity description. | "The child finds three {color} things using the photographed {entity} as a starting example." | Feeds previews, logs, recap/dashboard payloads. |
| `activity_signature.preview_label` | Short child-facing card/button label. | "Find three {color} things!" | Keep under about 40 characters after rendering. |
| `activity_signature.preview_prompt` | One sentence bridging from conversation to activity. | "You noticed the {color} of the {entity}. Let's go find more {color} things together." | Should acknowledge the prior conversation angle. |

Authoring check: if `observation_angle: quantity`, the `focal_attribute`, `intro`, and `preview_prompt` should not talk mainly about color or shape.

---

## 5 · Downstream Parent Fields

These fields are most important for parent-facing dashboards and curriculum analytics.

| Field | How to set it | Example | Parent-facing use |
|---|---|---|---|
| `key_concepts` | 1-2 IB key concepts visible in the activity. | `[Form, Change]` | Curiosity profile and framework chips. |
| `progression.topic_axis` | Exactly one axis the activity climbs. | `form`, `responsibility` | Growth path ladder and next-step logic. |
| `progression.difficulty_level` | Current rung, 1-3. | `2` | Progression state and dashboard summaries. |
| `progression.next_step_hint` | Specific next activity direction. | "Next time, compare color and pattern together." | Parent-facing or internal recommendation copy. |
| `progression.reward_hook` | Badge/reward text for the axis/rung. | `connection_L2 badge` | Reward or achievement label. |
| `atl_skills` | 2-3 WonderLens thinking/learning tags. | `[counting, observation, classification]` | Parent can see practiced thinking modes. |
| `transdisciplinary_theme` | One PYP theme token. | `How_We_Express_Ourselves` | Parent framework chip. |
| `subject_tags` | Curriculum domain tags when present. | `[math, science]` | Filtering, subject balance, parent summaries. |
| `caregiver_role` | Cumulative support roles expected for the tier. | `[scaffold, co-explorer]` | Parent guidance and session framing. |
| `activity_signature.observation_angle` | Same value used by upstream. | `quantity` | Angle split in dashboard and session timeline. |
| `activity_signature.mechanic` | Same value used by runtime. | `compare` | Exploration matrix: mechanic x angle. |
| `activity_signature.entity_role` | Same value used by runtime. | `exemplar` | Explains whether the photographed item was the subject or a bridge. |

Keep parent fields stable. They are aggregated over time, so renaming values creates history drift.

### 5.1 From one activity to the growth path

A tag block describes one completed activity. The parent growth path does not show that tag block as a standalone record; it rolls many activity events into the selected window, usually week or month.

Each activity appends one event with its own axis, rung, angle, mechanic, entity role, concepts, and recap evidence. The dashboard then aggregates those events:

| Field | Per-activity meaning | Window aggregation | Growth path effect |
|---|---|---|---|
| `progression.topic_axis` | The one axis this activity climbed. | Group events by axis. | Creates or updates the axis row in the LxT ladder. |
| `progression.difficulty_level` | The rung attempted/reached in this activity. | Compute current rung per axis using progression policy, not blind last-write-wins. | Adds evidence under that axis and may move the visible rung. |
| `progression.next_step_hint` | Recommended direction after this activity. | Keep recent viable hints as a suggestion pool. | Feeds "Try at home" and possible next-step copy; does not reserve the next activity. |
| `key_concepts` | Conceptual lenses visible in the activity. | Count exposure by concept across the window. | Feeds curiosity profile and framework chips. |
| `atl_skills` | Thinking/learning modes practiced. | Count practiced modes across the window. | Feeds thinking-skill trail, such as counting, logic, classification, expression. |
| `subject_tags` | Curriculum domains touched. | Count domain balance across the window. | Feeds subject balance and parent summaries. |
| `activity_signature.observation_angle` | Attribute/dimension attended to in this activity. | Split axis evidence by angle. | Shows whether an axis was practiced through color, quantity, emotion, function, etc. |
| `activity_signature.mechanic` | Child action pattern in this activity. | Cross-tab with observation angle. | Feeds exploration matrix, such as compare x quantity or care x emotion. |
| `activity_signature.entity_role` | How the photographed item participated. | Track subject/exemplar/catalyst/reference patterns. | Explains why a photo became the main subject or a bridge to a broader activity. |
| `caregiver_role` | Adult support expected/used for the activity. | Count support mix over the window. | Feeds parent guidance and support gauges. |
| `highlight_moment` / recap output | Evidence from the completed session. | Select representative moments. | Feeds "In their words" and activity evidence under the ladder. |

One activity should not overwrite the growth path by itself. If a child spends Monday on `topic_axis: form` at L2, then Tuesday's photo triggers a coherent `topic_axis: connection` activity, the Form row remains part of the window history while Connection gets its own event. The next activity should prefer continuity when the photo and catalog allow it, but the aggregate view must preserve both the planned direction and the child's actual path.

### 5.2 Planned direction vs actual next activity

`progression.topic_axis`, `progression.difficulty_level`, and `progression.next_step_hint` describe the activity that just ran and the recommended direction for what could come next. They do not guarantee the next selected activity.

The next selection is constrained by the child's next photo, detected entity/properties, catalog coverage, tier support, safety rules, and conversation context. The selector should treat progression targets as a strong preference, not a hard requirement.

Expected runtime behavior:

| Situation | Selector behavior | Parent-facing interpretation |
|---|---|---|
| Eligible activity matches target axis/rung and photo context | Prefer it with progression bonus | "Next step followed." |
| Eligible activity matches axis but not exact rung | Prefer closest safe rung | "Continued the same area." |
| Photo context only supports a different axis/activity | Choose the best coherent eligible activity | "Followed the child's new curiosity." |
| No eligible activity is coherent or safe | Ask for another photo, use a generic fallback, or end gracefully | Do not imply a missed goal. |

Copy rule: parent-facing surfaces may say "suggested next step" or "possible next direction." They should not say "the next activity will be..." unless the runtime has already selected and reserved that activity.

---

## 6 · Child Recap Fields

The child recap should reflect what the child did, not expose framework classification.

| Field | How to set it | Child-facing use |
|---|---|---|
| `entity` | Runtime-resolved entity name. | Names the thing the child started from. |
| `pillar` | Emotional mode of the activity. | Frames the badge/identity indirectly. |
| `related_concepts` | Child-friendly concept chips. | "Pattern", "Camouflage", "Variety". |
| `atl_skills` | Thinking/learning skills, rewritten child-friendly. | "noticing", "counting", "sorting". |
| `activity_signature.observation_angle` | Attribute noticed. | "You noticed red", "You counted how many". |
| `activity_signature.mechanic` | Action performed. | "You collected", "You compared", "You cared". |
| `activity_signature.entity_role` | How the photo participated. | Lets recap explain pivots gently. |
| `activity_signature.focal_attribute` | Rendered attribute value. | "red", "three", "happy". |

Game-specific recap copy belongs in `recap.template.yaml`, not in extra tag-block fields.

---

## 7 · Authoring Audit Fields

These fields help humans and generation prompts review the design, but should not carry heavy runtime logic.

| Field | How to set it | Use |
|---|---|---|
| `attributes` | Observable properties invoked by the activity; may be runtime-filled for parameterized games. | Audit that prompts actually use the intended properties. |
| `category` | Activity/content category or runtime-filled object category. | Catalog review and filtering. |
| `related_concepts` | 2-4 child-friendly concepts. | Recap and authoring review. |
| `kud.know` | Facts or vocabulary. | Curriculum review. |
| `kud.understand` | 1-2 conceptual understandings. | Checks alignment with `key_concepts`. |
| `kud.do` | 2-3 child actions. | Checks alignment with `mechanic` and `atl_skills`. |

If a value only explains why the activity exists, it probably belongs in `spec.md`, not `tag_block.yaml`. Asset requirements follow this rule: prebuilt/generated image prompts, `asset_id` tables, display behavior, and fallback behavior live in `spec.md` `## Asset Brief` and `prod.md` screen guidance, not in `tag_block.yaml`, unless a future schema explicitly adds asset fields.

---

## 8 · Worked Mini Examples

### 8.1 Color collection

```yaml
key_concepts: [Form]
atl_skills: [counting, observation, classification]
subject_tags: [math, science]
progression:
  topic_axis: form
  difficulty_level: 2
activity_signature:
  observation_angle: color
  mechanic: collect
  entity_role: exemplar
  focal_attribute: red
  bridge_prerequisites:
    primary: [color]
    secondary: [pattern]
```

Interpretation: the child attends to color, practices Form, collects examples, and the photographed entity becomes one example of a broader color hunt.

### 8.2 Quantity comparison

```yaml
key_concepts: [Form, Causation]
atl_skills: [counting, quantity_comparison, evidence_collection]
subject_tags: [math]
progression:
  topic_axis: causation
  difficulty_level: 2
activity_signature:
  observation_angle: quantity
  mechanic: compare
  entity_role: catalyst
  focal_attribute: more_less
  bridge_prerequisites:
    primary: [quantity]
    secondary: [size]
```

Interpretation: the child attends to amount, but the conceptual lens is why one group has more or less. This demonstrates why `observation_angle` and `topic_axis` are orthogonal.

### 8.3 Feeling voice-stage

```yaml
key_concepts: [Perspective]
atl_skills: [language_expression, perspective_taking, empathy]
subject_tags: [language, social_emotional]
progression:
  topic_axis: perspective
  difficulty_level: 2
activity_signature:
  observation_angle: emotion
  mechanic: voice
  entity_role: subject
  focal_attribute: happy_sleepy_worried
  bridge_prerequisites:
    primary: [emotion, behavior]
    secondary: [sound]
```

Interpretation: the child attends to emotion and behavior, gives the entity a voice, and practices Perspective.

---

## 9 · Review Checklist

Before accepting a new `tag_block.yaml`, check:

- Upstream eligibility fields are enough for the matcher to say "can run."
- `activity_signature` fields are enough for the matcher to say "should follow."
- `observation_angle` and `progression.topic_axis` are both set and not treated as synonyms.
- `bridge_prerequisites.primary` uses only the 12 closed observation-angle values.
- `mechanic` describes the child's action, not the visual style of the game.
- Parent fields are stable and aggregatable.
- Child-facing strings live in `preview_*` or `recap.template.yaml`, not scattered across audit fields.
- `kud.do`, `atl_skills`, and `activity_signature.mechanic` agree with each other.
