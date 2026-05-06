# Activity Tag Block and Progression Guide

**Version:** 0.1 - 2026-04-30
**Status:** Supplement reference
**Chinese version:** `docs/activity_tag_block_progression_guide_cn.md`
**Primary sources:** `activities/_schema/tag_block.schema.json`, `docs/activity_vocabulary.md`, `docs/progression_axes.md`, `docs/activity_tag_block_usage.md`, `docs/superpowers/specs/2026-04-24-progression-algorithm-design.md`

This guide is a consolidated map of the full activity tag block and the progression algorithm. It does not introduce new fields. It explains how the same `tag_block.yaml` is read by upstream matching, runtime rendering, downstream recap/dashboard surfaces, and the progression engine.

---

## 1. One Mental Model

A `tag_block.yaml` describes one activity package. The activity may be played many times by many children, but the tag block itself is the catalog-time declaration.

At runtime, the system creates session events from that declaration:

1. **Upstream matcher** reads tag blocks before the activity starts. It asks whether an activity can run for the photographed entity/tier and whether it is a coherent continuation of the conversation.
2. **Runtime activity layer** renders placeholders such as `{entity}`, `{color}`, or `{matched_color}` into child-facing and observer-facing copy.
3. **Progression engine** uses the activity's declared `progression.topic_axis` and `progression.difficulty_level`, plus observed child evidence, to update per-child axis state after the activity.
4. **Downstream surfaces** read the completed session event, not just the static tag block. Child recap summarizes what happened; parent growth path aggregates many activity events across a week or month.

The important split:

| Layer | Main question | Main fields |
|---|---|---|
| Upstream eligibility | Can this activity run for this photo and child tier? | `entity`, `entity_class`, `entity_binding`, `tier_range`, `matchability.*` |
| Upstream coherence | Should this activity follow this conversation? | `activity_signature.observation_angle`, `bridge_prerequisites`, `entity_role`, progression target |
| Runtime presentation | What should the child/observer see at activity start? | `activity_signature.focal_attribute`, `intro`, `preview_label`, `preview_prompt` |
| Progression | Which axis/rung did this activity exercise, and what changes after the session? | `progression.*`, evidence vector, axis state, progression event |
| Downstream child | What did the child do? | resolved `entity`, `activity_signature.*`, recap template output |
| Downstream parent | What pattern is emerging over time? | aggregated `progression.*`, `key_concepts`, `atl_skills`, `activity_signature.*`, `caregiver_role` |

---

## 2. Complete Tag Block Shape

This is the full current shape for migrated activity packages. Required fields are enforced by `activities/_schema/tag_block.schema.json`; some optional fields are included because current activities already use them.

```yaml
activity_id: color_scout_property
version: 1
source_entity_exemplar: ladybug
template_type: cat5
pillar: Discovery
game_style: field_experiment

entity: "{parameterized_by_matched_property}"
entity_class: []
entity_binding: parameterized
tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: "±1"

category: objects
attributes: []

key_concepts: [Form]
related_concepts: [variety, attention]
atl_skills: [observation, classification]
transdisciplinary_theme: How_We_Express_Ourselves
subject_tags: [science]

kud:
  know: ["the focal color appears on many kinds of things"]
  understand: ["color is a property we can use to group things"]
  do: ["find 3 things that share the focal color"]

progression:
  topic_axis: form
  difficulty_level: 2
  next_step_hint: "Next time, notice another attribute alongside color"
  reward_hook: "Earned the Color Scout badge"

caregiver_role: [scaffold, co-explorer]

activity_signature:
  observation_angle: color
  mechanic: collect
  entity_role: exemplar
  bridge_prerequisites:
    primary: [color]
    secondary: [pattern, visibility]
  focal_attribute: "{matched_color}"
  intro: "The child finds three {color} things using the photographed {entity} as a starting example."
  preview_label: "Find three {color} things!"
  preview_prompt: "You noticed the {color} of the {entity}. Let's go find more {color} things together."
  role_pivot_note: |
    The {entity} was our subject during the chat; now it becomes an
    example of {color}: we are going to find more {color} things.

matchability:
  entity_class_filter: []
  tier_support:
    T0: true
    T1: true
    T2: true
```

### 2.1 Required Top-Level Fields

| Field | Required | How to use it |
|---|---:|---|
| `activity_id` | yes | Lowercase snake_case. Must match the package directory name. |
| `version` | yes | Integer package version. Bump when the package contract changes. |
| `template_type` | yes | `cat1` or `cat5`. Used by activity generation/runtime templates. |
| `pillar` | yes | Emotional/activity pillar: `Discovery`, `Performance`, `Mystery`, `Creation`, `Adventure`, `Connection`. |
| `game_style` | yes | Specific activity format, such as `field_experiment`, `voice_stage`, `mystery_trail`. |
| `entity` | yes | Bound entity name, or a placeholder for parameterized activities. |
| `entity_binding` | yes | `bound`, `parameterized`, or `agnostic`. Controls swap-ability. |
| `tier_range` | yes | Authoring tier intent and supported tier span. |
| `key_concepts` | yes | 1+ IB key concepts visible in the activity. |
| `progression` | yes | Primary progression axis/rung declaration for this activity. |
| `caregiver_role` | yes | Expected adult support roles. |
| `activity_signature` | yes | Conversation-to-activity coherence and presentation metadata. |
| `matchability` | yes | Extra top-level matcher eligibility filters. Sibling of `activity_signature`, not inside it. |

### 2.2 Optional But Common Fields

| Field | How to use it |
|---|---|
| `source_entity_exemplar` | Example entity used to author or illustrate a parameterized package. |
| `entity_class` | Ordered class chain. Empty only when runtime fills it for wide parameterized activities. |
| `category` | Runtime/entity category or legacy grouping. |
| `attributes` | Relevant entity attributes, often runtime-filled for parameterized activities. |
| `related_concepts` | Child-facing or curriculum-adjacent concept labels. |
| `atl_skills` | WonderLens thinking/learning tags such as `observation`, `classification`, `counting`, `logic`, `communication`. |
| `transdisciplinary_theme` | PYP theme token. |
| `subject_tags` | Curriculum domain tags when present, such as `math`, `science`, `language`. |
| `kud` | Authoring audit: what the child should know, understand, and do. |

---

## 3. Upstream Usage

Upstream selection has two layers: eligibility first, coherence second.

### 3.1 Eligibility: Can It Run?

Eligibility fields are top-level matcher inputs. They should be stable and machine-readable.

| Field | Usage | Example |
|---|---|---|
| `entity` | Nominal entity or placeholder. | `lion`, `{parameterized_by_matched_property}` |
| `entity_class` | Lets matcher roll up from specific to general when exact match misses. | `[lion, big_cat, mammal, animal]` |
| `entity_binding` | Declares how tightly the activity depends on a specific entity. | `bound`, `parameterized`, `agnostic` |
| `tier_range.primary` | Tier the activity was written for. | `T1` |
| `tier_range.span` | Tiers the activity can safely support. | `[T0, T1, T2]` |
| `tier_range.elasticity` | Human-readable stretch rule. | `"±1"`, `neighbor`, `strict`, `broad` |
| `matchability.entity_class_filter` | Additional class allowlist. Empty means wide. | `[]`, `[big_cat]`, `[insect, patterned_thing]` |
| `matchability.tier_support` | Boolean support matrix. Should agree with `tier_range.span`. | `{T0: true, T1: true, T2: true}` |

`matchability` is a top-level tag block section. It is not part of `activity_signature`.

An activity is **eligible** when all hard filters pass:

1. The tag block is valid and the activity is present in the active catalog.
2. The child's runtime tier is included in `tier_range.span`.
3. `matchability.tier_support[child_tier]` is `true`.
4. The photographed entity satisfies the binding rule for `entity_binding`.
5. The photographed entity is allowed by `matchability.entity_class_filter`; an empty filter means wide.
6. Required runtime properties can be resolved. For parameterized property activities, this means the photographed entity exposes the property the activity needs, such as color, shape, material, pattern, or quantity.
7. Safety and runtime availability checks pass.

Eligibility only means "this activity may be considered." It does not mean the activity should be selected. Ranking still uses conversation coherence, progression target, freshness, and other selector signals.

### 3.1.1 Binding-Specific Eligibility Rules

| Binding | Eligible when | Common `entity_class_filter` shape | Example |
|---|---|---|---|
| `bound` | The activity depends on a specific entity or narrow entity family. Prefer exact entity unless the script can safely render a broader class. | Narrow: `[big_cat]`, `[butterfly]`, `[ladybug]` | A lion voice activity can use `[big_cat]` only if the runtime keeps the copy coherent for the detected big cat. |
| `parameterized` | The entity is a slot and supplies the required property/value. Exact entity does not matter. | Wide `[]` for universal property hunts; restricted `[animal]`, `[plant]`, `[patterned_thing]` when the activity logic needs a class. | Color Scout can run on a red pen, red ladybug, or red toy if `{matched_color}` resolves. |
| `agnostic` | The entity is decorative or only anchors attention. Any safe observable thing can start the activity. | Usually `[]` or `[observable_thing]`; use a narrower filter only if the supposedly agnostic activity actually has a setting/entity constraint. | A "name three things you notice" warm-up can run on almost any photo. |

For legacy authoring that still includes `entity_attributes_covered`, use the overlap rule from `program.md`: `bound` activities require strict attribute resolution; `parameterized` activities use loose overlap, where any required property match can fill the runtime parameter.

### 3.1.2 Eligibility Examples

#### Bound: narrow entity/family

```yaml
entity: lion
entity_binding: bound
entity_class: [big_cat, mammal, animal]
tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: "±1"
matchability:
  entity_class_filter: [big_cat]
  tier_support: {T0: true, T1: true, T2: true}
```

Eligible for: lion, and possibly other big-cat contexts if copy is safely parameterized.

Not eligible for: dog, beetle, toy car, or any photo whose class chain does not intersect `[big_cat]`.

#### Parameterized: wide property bridge

```yaml
entity: "{parameterized_by_matched_property}"
entity_binding: parameterized
entity_class: []
tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: "±1"
activity_signature:
  observation_angle: color
  focal_attribute: "{matched_color}"
matchability:
  entity_class_filter: []
  tier_support: {T0: true, T1: true, T2: true}
```

Eligible for: any safe photographed entity with a resolvable color value.

Not eligible for: a photo where no reliable color/property can be extracted, or a runtime context that forbids a movement/search activity.

#### Parameterized: restricted property bridge

```yaml
entity: "{parameterized_by_matched_property}"
entity_binding: parameterized
entity_class: []
activity_signature:
  observation_angle: pattern
  focal_attribute: "{matched_pattern}"
matchability:
  entity_class_filter: [patterned_thing]
  tier_support: {T0: true, T1: true, T2: true}
```

Eligible for: ladybug, striped shirt, spotted ball, or another entity whose class chain includes `patterned_thing` and whose pattern can be resolved.

Not eligible for: a plain object with no visible pattern, even if the child tier matches.

#### Agnostic: any safe observable thing

```yaml
entity: any
entity_class: [observable_thing]
entity_binding: agnostic
tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: broad
activity_signature:
  observation_angle: state
  focal_attribute: "{observed_detail}"
matchability:
  entity_class_filter: []
  tier_support: {T0: true, T1: true, T2: true}
```

Eligible for: almost any safe, recognizable photo, because the activity is about a general thinking move.

Not eligible for: unsafe/unclear photos, or activities that secretly rely on a specific entity property. If the script needs a color, shape, living thing, or animal, it is not truly agnostic.

### 3.2 Coherence: Should It Follow?

Coherence fields live mostly inside `activity_signature`. They help the selector rank eligible activities against the conversation signature.

| Field | Usage | Example |
|---|---|---|
| `activity_signature.observation_angle` | Primary attribute/dimension the activity attends to. | `color`, `quantity`, `emotion` |
| `activity_signature.bridge_prerequisites.primary` | 1-3 strong conversation angles that make this activity a natural next step. | `[color]`, `[behavior, function]` |
| `activity_signature.bridge_prerequisites.secondary` | Supporting angles or editorial descriptors. Enum values are preferred. | `[pattern, visibility]` |
| `activity_signature.entity_role` | How the photographed entity participates. | `subject`, `exemplar`, `catalyst`, `reference` |
| `activity_signature.role_pivot_note` | Explains a pivot when the photo stops being the direct subject. | "The pen becomes one example of red." |

Scoring pattern from the activity-signature design:

| Match | Selector effect |
|---|---|
| Candidate `observation_angle` equals conversation `dominant_angle` | Strong bonus |
| Candidate `observation_angle` appears in conversation `secondary_angles` | Smaller bonus |
| Candidate `bridge_prerequisites.primary` overlaps conversation angles | Continuity bonus |
| Candidate matches target axis/rung from progression state | Progression bonus |

Progression targeting is best-effort. The selector should prefer the target axis/rung when photo context and catalog coverage allow it, but hard eligibility still wins.

### 3.3 Where `conversation_signature` and `progression_target` Come From

The upstream selector receives two different runtime inputs before it scores activities:

| Runtime input | Owner | How it is produced | Used for |
|---|---|---|---|
| `conversation_signature` | Conversation/photo understanding layer | Built from the current photo, detected entity/properties, and recent chat turns. V1 uses keyword/attribute heuristics: count angle hits such as red/blue → `color`, round/square → `shape`, more/three → `quantity`; choose the top hit as `dominant_angle` and keep secondary hits as `secondary_angles`. | Conversation coherence scoring against `activity_signature.observation_angle` and `bridge_prerequisites`. |
| `progression_target` | Progression service | Read from the child's stored per-axis `axis_state` plus the latest `progression_event` / policy output. It usually contains the preferred next `target_axis` and `target_rung`; at L3 ceiling or persistent overload it may point to a sibling axis. | Progression bonus in activity ranking. |

Minimal runtime flow:

```text
photo + recent chat
  -> entity/properties + conversation_signature

child_id + stored axis_state + latest progression_event
  -> progression_target

conversation_signature + progression_target + active tag blocks
  -> activity selector
```

Both inputs can be missing. If `conversation_signature` is null, the selector skips conversation-angle bonuses. If `progression_target` is null, the selector skips progression bonuses and falls back to eligibility, coherence, freshness, and product policy.

### 3.4 Upstream Example

Child photographs a red pen. The conversation signature says:

```yaml
conversation_signature:
  entity: pen
  dominant_angle: color
  secondary_angles: [shape, function]
  child_tier: T1
progression_target:
  axis: form
  rung: 2
```

`color_scout_property` is a strong match:

```yaml
entity_binding: parameterized
matchability:
  entity_class_filter: []
  tier_support: {T0: true, T1: true, T2: true}
activity_signature:
  observation_angle: color
  bridge_prerequisites:
    primary: [color]
  entity_role: exemplar
progression:
  topic_axis: form
  difficulty_level: 2
```

Why it works:

- Eligibility passes because the activity is parameterized and wide.
- Conversation coherence passes because the dominant angle is `color`.
- Progression fit passes because the target axis/rung is `form` L2.
- Entity role is `exemplar`: the pen is not the whole subject; it becomes one example of red.

---

## 4. Runtime Presentation Usage

Runtime presentation fields are author-written templates. They are rendered when concrete photo/session values are known.

| Field | Runtime use |
|---|---|
| `activity_signature.focal_attribute` | The concrete attribute or placeholder under attention, such as `{matched_color}`, `lion_voice`, `more_less`. |
| `activity_signature.intro` | Observer-facing one-sentence description used in previews, logs, recap payloads, and parent timeline cards. |
| `activity_signature.preview_label` | Short activity card or button label. |
| `activity_signature.preview_prompt` | Conversation-to-activity transition line. |
| `activity_signature.role_pivot_note` | Runtime/editorial note for explaining subject-to-exemplar/catalyst/reference pivots. |

Example before rendering:

```yaml
preview_label: "Find three {color} things!"
preview_prompt: "You noticed the {color} of the {entity}. Let's go find more {color} things together."
```

Example after rendering:

```yaml
preview_label: "Find three red things!"
preview_prompt: "You noticed the red of the pen. Let's go find more red things together."
```

Runtime should not infer a factual attribute that was not observed or safely reported. For photo-limited attributes, prefer child-confirmed phrasing or avoid the claim.

---

## 5. Progression Declaration In The Tag Block

The `progression` block says which one axis/rung this activity formally exercises.

```yaml
progression:
  topic_axis: form
  difficulty_level: 2
  next_step_hint: "Next time, notice another attribute alongside color"
  reward_hook: "Earned the Color Scout badge"
```

| Field | Meaning |
|---|---|
| `topic_axis` | Exactly one of the 7 axes: `form`, `function`, `causation`, `change`, `connection`, `perspective`, `responsibility`. |
| `difficulty_level` | Current rung, integer `1`, `2`, or `3`. Do not write `L1`/`L2`/`L3` in the tag block. |
| `next_step_hint` | Suggested next direction. It is not a guarantee that the next selected activity will match it. |
| `reward_hook` | Optional reward/badge copy or achievement label. |

`progression.topic_axis` and `activity_signature.observation_angle` are orthogonal:

```yaml
activity_signature:
  observation_angle: quantity
progression:
  topic_axis: form
```

This means the child practiced Form through quantity evidence. It does not create a separate `form/quantity` level. The child still has one Form state; the parent dashboard can split evidence by angle.

Common combinations:

| Observation angle | Possible axis | Example |
|---|---|---|
| `quantity` | `form` | Count how many objects or parts there are. |
| `quantity` | `causation` | Ask why one group has more. |
| `emotion` | `perspective` | Infer how different characters might feel. |
| `function` | `responsibility` | Notice what care an object or living thing needs. |
| `pattern` | `connection` | Find shared patterns across different things. |

---

## 6. Progression Algorithm

The progression algorithm is not just the static `progression` block. It is the runtime policy that updates per-child state after observing how the child handled the activity.

The approved V1 model from `docs/superpowers/specs/2026-04-24-progression-algorithm-design.md` is:

1. Convert each round into an evidence vector.
2. Update per-child, per-axis, per-rung score state.
3. Apply hard pedagogical guardrails.
4. Use an explainable action policy.
5. Emit the same external action types already used by runtime systems.

### 6.1 Evidence Vector

Each round should produce richer evidence than pass/fail.

```yaml
evidence:
  correctness: 0.85
  correctness_confidence: 0.72
  spontaneity: 0.40
  latency_bucket: long_wait
  latency_confidence: 1.0
  hint_level: multiple_choice
  hint_confidence: 1.0
  language_depth: name
  language_depth_confidence: 0.68
  on_topic_persistence: 0.90
  prompt_repetition: false
  off_topic: false
  affect_energy: hesitant
```

Main interpretation:

| Evidence field | Why it matters |
|---|---|
| `correctness` | Whether the response satisfied the current rung goal. |
| `spontaneity` | Whether the child answered independently. |
| `latency_bucket` | Separates healthy thinking time from overload or no attempt. |
| `hint_level` | Prevents over-promoting scaffolded correctness. |
| `language_depth` | Maps response depth to L1 name, L2 extend, or L3 reason. |
| `on_topic_persistence` | Protects engaged struggle from being treated as failure. |
| `prompt_repetition` / `off_topic` | Signals possible overload or misunderstanding. |
| `affect_energy` | Advisory only in V1; never sole promote/demote evidence. |

### 6.2 Evidence Reliability

The engine should trust runtime-owned facts before soft classifier guesses.

| Reliability tier | Examples | V1 usage |
|---|---|---|
| Hard telemetry | wait time, hint count, prompt count, support move emitted by runtime | Safe to use directly. |
| Structured interaction facts | selected option, completed count, tapped target | Safe with light validation. |
| Shallow language classification | correctness, off-topic, prompt repetition, language depth | Use with confidence and reason codes. |
| Affect/energy | tired, hesitant, frustrated, playful | Advisory only until validated. |

Low-confidence positive evidence can support `hold` or internal `promote_ready`; it should not independently emit `promote`. Low-confidence negative evidence can increase support need; it should not independently emit `demote`.

### 6.3 Axis State

Progression state is per child and per axis, not global.

```yaml
axis_state:
  axis: form
  current_rung: 2
  mastery:
    l1: 0.92
    l2: 0.71
    l3: 0.28
  engagement: 0.84
  support_needed: 0.31
  stability: 0.76
  novelty_readiness: 0.68
  recent_events:
    - hold
    - soft_reframe
    - promote_ready_internal
  policy_version: evidence_v1_default
```

| Score | High value implies |
|---|---|
| `mastery[rung]` | Child can handle this rung on this axis. |
| `engagement` | Child is participating and emotionally available. |
| `support_needed` | Child needs scaffolding; hold, soften, or demote only if persistent. |
| `stability` | Evidence is consistent enough to change rung with confidence. |
| `novelty_readiness` | Child may benefit from a new exemplar, higher rung, or sibling axis. |

### 6.4 Score Update Policy

V1 uses hand-authored weights. They are intentionally simple, inspectable, and replaceable. The goal is not to create a perfect learning model in V1; the goal is to make the runtime more nuanced than pass/fail while keeping every update explainable.

Example deltas:

| Evidence | Mastery | Engagement | Support needed | Novelty readiness |
|---|---:|---:|---:|---:|
| Clean correct, no hint | `+0.18` | `+0.06` | `-0.05` | `+0.08` |
| Spontaneous L+1 | `+0.20` current rung, `+0.10` next rung | `+0.08` | `-0.04` | `+0.30` |
| Correct after light hint | `+0.10` | `+0.04` | `+0.08` | `+0.02` |
| Correct after multiple choice | `+0.06` | `+0.03` | `+0.14` | `0.00` |
| Modeling needed | `+0.04` | `0.00` | `+0.20` | `-0.03` |
| Mixed but on-topic | `+0.04` | `+0.05` | `+0.08` | `0.00` |
| Off-topic | `-0.08` | `-0.12` | `+0.10` | `-0.04` |
| Repeats prompt | `-0.06` | `-0.04` | `+0.15` | `-0.03` |
| Long silence after correct | `0.00` | `-0.02` | `+0.10` | `0.00` |
| Silence no attempt | `-0.05` | `-0.10` | `+0.12` | `-0.04` |

Use bounded exponential smoothing:

```text
new_score = clamp(old_score * retention + evidence_delta, 0.0, 1.0)
```

Recommended V1 retention:

| Score | Retention |
|---|---:|
| `mastery` | `0.90` |
| `engagement` | `0.80` |
| `support_needed` | `0.85` |
| `novelty_readiness` | `0.75` |

`stability` is computed from recent score variance and outcome consistency rather than direct deltas.

### 6.5 External Actions

The external action enum stays small.

| Action | Meaning | Child-facing handling |
|---|---|---|
| `promote` | Next prompt/activity can ask for deeper thinking on the same axis. | Ask a richer question; do not over-celebrate level mechanics. |
| `hold` | Stay on the same rung with a new variation or exemplar. | Continue naturally. |
| `soft_reframe` | Slow down, hint, or ask a gentler version without lowering the rung. | Use supportive wording. |
| `demote` | Lower cognitive load after repeated reliable evidence of overload. | Never expose demotion language; use Dignity Reframe. |
| `sibling_jump` | Shift laterally to a related axis for novelty or relief. | Frame as a new direction, not a failure. |

Support does not equal failure. A correct answer after modeling or multiple choice usually means `hold` or `soft_reframe`, not `promote`.

### 6.6 Guardrails

The algorithm uses score state, but pedagogy guardrails remain hard constraints.

| Guardrail | Runtime effect |
|---|---|
| 6-10 second wait time | Do not classify no-response too early. |
| No demote after one silence | Silence alone cannot lower rung. |
| Soft-Reframe | Required for processing-time or hesitant-but-engaged states. |
| Dignity Reframe | Required surface for every `demote`. |
| Banned phrases | Unchanged agent-prompt constraint. |
| Two failed attempts | Demotion eligibility threshold, not automatic demotion. |
| Three same-axis successes | Promotion evidence, not automatic promotion. |
| Sibling-axis jump | Preserved at L3 ceiling or persistent L1 overload. |

### 6.7 Timing, Activity Coverage, and Axis Routing

This part answers three implementation and catalog-planning questions:

1. When does progression affect the next activity?
2. Does every axis/rung need a separately prepared activity?
3. Which axis should the system choose after a child goes beyond L3?

#### 6.7.1 When Progression Takes Effect

Progression has two time scales:

| Time scale | Happens during live activity? | What can change | What should not change |
|---|---|---|---|
| Turn-level adaptation | Yes | Wait time, hint, multiple choice, modeling, `soft_reframe`, Dignity Reframe wording | Do not suddenly replace the whole activity. |
| Activity/session outcome | After the activity finishes | Axis state, mastery scores, next recommended rung, next recommended axis | Do not rewrite the completed activity retroactively. |

The runtime may adapt inside the activity, but durable progression state should normally commit after the activity finishes. This keeps the live experience stable: the child should not feel the system swapping games mid-stream.

Example:

```text
Current activity: Form L1
Child response: names color quickly, then adds "red warns birds"
During activity: agent can ask one richer follow-up
After activity: Form state updates; selector recommends Form L2 or L3-ready content next
Next activity: chosen from catalog using updated Form state
```

`promote` is best understood as "the next activity should target a higher rung," not "interrupt the current activity and load a new L2 activity immediately." The exception is an activity that already contains authored elastic prompts for multiple rungs; then the agent may use a richer prompt within the same activity, while persisted rung state still updates at session end.

#### 6.7.2 Avoiding Activity Explosion

A naive catalog model would require `7 axes x 3 rungs = 21` separate activity types, multiplied by entities, pillars, and age tiers. That is too much content work.

The recommended catalog model is **activity families with elastic rung variants**, not one bespoke activity per cell.

| Catalog layer | What authors prepare | Example |
|---|---|---|
| Activity family | Reusable game mechanic and entity/pillar structure | "Color Scout" or "Part Detective" |
| Primary axis | The one axis this activity formally updates | `form` |
| Rung variant pack | L1/L2/L3 prompt patterns inside the same family | L1 name color; L2 name and locate features; L3 explain why feature exists |
| Runtime selector | Best available family/rung for the child's current axis state | Pick Form L2 if available; otherwise use elastic Form L1 with L2 micro-challenge |

For a Form activity, one family can cover three rungs:

| Rung | Prompt shape | Child evidence |
|---|---|---|
| Form L1 | "What color/shape/part do you notice?" | Names one attribute |
| Form L2 | "Where do you see two or three details?" | Names multiple attributes and locates them |
| Form L3 | "Why might it have that color, shape, or pattern?" | Explains purpose or reason |

Promotion does not require the team to author a separate L2 activity for every L1 activity. The selector should be availability-aware:

1. Prefer exact match: same axis, recommended rung, suitable tier, fresh entity/pillar.
2. If no exact match exists, use the same activity family with a higher-rung prompt variant.
3. If no higher-rung variant exists, hold the rung but add a richer micro-challenge.
4. If the axis is saturated or at ceiling, use sibling-axis routing.

Catalog coverage should grow toward a matrix of strong axis/rung families. V1 can start with fewer well-designed families as long as each has elastic prompt variants and the selector records when it had to fall back.

#### 6.7.3 What Happens Beyond L3

There is no L4 in the current model. When a child shows stable L3 evidence on an axis, preserve the L3 mastery and route the next activity laterally to a related sibling axis at L1 or L2.

The sibling jump is not a demotion. It means: "You have gone deep here; now let's connect that strength to a nearby way of thinking."

Recommended default sibling graph:

| Current axis at L3 | Primary sibling jump | Fallback sibling | Rationale |
|---|---|---|---|
| `form` | `connection` L1 | `function` L1 | From noticing attributes to grouping shared attributes or asking what parts do |
| `function` | `causation` L1 | `change` L1 | From how it works to why it behaves that way or what changes when a part changes |
| `causation` | `change` L1 | `function` L1 | From why something happens to how that cause unfolds over time |
| `change` | `causation` L1 | `responsibility` L1 | From transformation sequence to why it changed or what care it needs next |
| `connection` | `perspective` L1 | `form` L2 | From relationships between things to different viewpoints on those relationships |
| `perspective` | `responsibility` L1 | `connection` L1 | From seeing another viewpoint to deciding what helpful action follows |
| `responsibility` | `perspective` L1 | `connection` L1 | From care/action to who needs what, or how the child is connected to the system |

Treat the table as a default, not a prison. The final sibling choice should combine:

- conceptual adjacency from the table;
- the child's current mastery and engagement on candidate sibling axes;
- recent exposure, to avoid repetition;
- catalog availability;
- entity/pillar freshness;
- parent or educator policy constraints, if any.

At L3 ceiling, sibling routing should usually choose a related axis where the child has lower or less recent evidence. At L1 floor with repeated overload, sibling routing should instead choose an axis with higher predicted engagement or stronger recent success.

| Sibling-jump case | Goal | Selection bias |
|---|---|---|
| L3 ceiling | Preserve novelty and broaden thinking | Conceptually adjacent, less recently explored axis |
| L1 persistent overload | Restore confidence and engagement | Axis with higher engagement, lower support need, or stronger prior success |

Example L3 ceiling:

```text
Mia reaches Form L3 on ladybugs:
"Red warns birds not to eat it."

Next activity should not invent Form L4.
Recommended jump: Connection L1
"Can you find another small thing with warning colors or spots?"
```

Example L1 overload:

```text
Mia struggles with Causation L1 twice:
no answer, then repeats the prompt.

Next activity should not keep forcing Causation.
Recommended relief jump: Form L1 or Connection L1, depending on her stronger recent engagement.
```

The completed activity still updates only its declared primary axis. A sibling jump affects the next selection, not the axis credited for the activity that just ended.

### 6.8 Progression Event

Every progression action should emit a compact explainability event.

```yaml
progression_event:
  axis: form
  entry_rung: 2
  exit_rung: 2
  action: soft_reframe
  reason_codes:
    - long_silence_after_correct
    - adequate_engagement
    - demotion_blocked_single_silence
  evidence_confidence:
    correctness: 0.61
    language_depth: 0.58
    latency_bucket: 1.0
    hint_level: 1.0
  scores_before:
    mastery_current: 0.58
    engagement: 0.79
    support_needed: 0.37
  scores_after:
    mastery_current: 0.58
    engagement: 0.77
    support_needed: 0.46
  policy_version: evidence_v1_default
```

Reason codes make debugging possible and support parent-facing aggregation without exposing raw transcript details.

---

## 7. Downstream Usage

Downstream surfaces should read resolved session events and aggregate them carefully. They should not expose matcher-only declarations such as `entity_binding` or `matchability`.

### 7.1 Child Recap

Child recap is about what the child did, not how the catalog matched the activity.

| Field | Child recap use |
|---|---|
| resolved `entity` | Names the object or creature the child worked with. |
| `activity_signature.observation_angle` | Phrasing such as "you noticed red" or "you counted how many." |
| `activity_signature.mechanic` | Phrasing such as "you collected", "you compared", "you cared." |
| `activity_signature.entity_role` | Explains whether the photo stayed the subject or became a bridge. |
| `activity_signature.focal_attribute` | Child-friendly concrete value: `red`, `three`, `happy`. |
| `highlight_moment` | Representative moment from the session. |

Child recap should not show `progression.topic_axis` as a label. It can use the axis only as hidden context for generating a better one-sentence highlight.

### 7.2 Parent Growth Path

Parent view is a windowed aggregate. One completed activity appends one event; the growth path rolls many events into the selected period.

| Field | Per-activity meaning | Window aggregation | Parent effect |
|---|---|---|---|
| `progression.topic_axis` | Axis climbed by this activity. | Group events by axis. | LxT ladder row. |
| `progression.difficulty_level` | Rung attempted/reached. | Compute current rung per axis using progression policy. | Evidence under that axis; possible visible rung movement. |
| `progression.next_step_hint` | Suggested direction after the activity. | Recent viable hints become a suggestion pool. | "Try at home" or possible next direction copy. |
| `key_concepts` | Conceptual lenses touched. | Count exposure by concept. | Curiosity profile/framework chips. |
| `atl_skills` | Thinking/learning modes practiced. | Count practiced modes. | Thinking-skill trail. |
| `subject_tags` | Curriculum domains touched. | Count domain balance. | Subject balance and parent summaries. |
| `activity_signature.observation_angle` | Attribute/dimension attended to. | Split axis evidence by angle. | Color vs quantity vs emotion exposure. |
| `activity_signature.mechanic` | Child action pattern. | Cross-tab with angle. | Exploration matrix. |
| `activity_signature.entity_role` | How the photo participated. | Track subject/exemplar/catalyst/reference patterns. | Timeline explanation and pivot clarity. |
| `caregiver_role` | Adult support expected/used. | Count support mix. | Parent guidance and support gauges. |

If Monday is `topic_axis: form` L2 and Tuesday's photo triggers `topic_axis: connection` L1, the Form row remains in the window history and Connection gets its own event. The selector should prefer continuity when possible, but the dashboard must preserve the child's actual path.

---

## 8. Worked Examples

### 8.1 Color Scout From A Red Pen

Static tag block:

```yaml
entity_binding: parameterized
matchability:
  entity_class_filter: []
  tier_support: {T0: true, T1: true, T2: true}
activity_signature:
  observation_angle: color
  mechanic: collect
  entity_role: exemplar
  focal_attribute: "{matched_color}"
progression:
  topic_axis: form
  difficulty_level: 2
```

Runtime event:

```yaml
session_event:
  entity: pen
  rendered_focal_attribute: red
  axis: form
  rung: 2
  angle: color
  mechanic: collect
  entity_role: exemplar
  completed_count: 3
```

Progression effect:

- Updates the child's Form state, because `topic_axis: form`.
- Adds color evidence under Form, because `observation_angle: color`.
- If the child independently finds and explains multiple red items, the progression engine may mark Form L2 as strong or prepare a future Form L3 prompt.
- If the child needs multiple-choice support but stays engaged, the likely action is `hold` or `soft_reframe`, not immediate `promote`.

Parent effect:

- Adds one Form-row event to the selected window.
- Increases `color` exposure under Form.
- Adds `collect x color` to the exploration matrix.
- Adds `observation` / `classification` to the thinking-skill trail if those `atl_skills` are present.

### 8.2 Voice Stage From A Lion

Static tag block:

```yaml
entity: lion
entity_class: [big_cat, mammal, animal]
entity_binding: bound
matchability:
  entity_class_filter: [big_cat]
  tier_support: {T0: true, T1: true, T2: true}
activity_signature:
  observation_angle: behavior
  mechanic: voice
  entity_role: subject
  focal_attribute: lion_voice
progression:
  topic_axis: connection
  difficulty_level: 2
```

Interpretation:

- Eligibility is narrower than Color Scout because `entity_class_filter: [big_cat]`.
- The lion remains the `subject`; no pivot is needed.
- The child practices Connection through behavior/voice evidence.
- Parent dashboard can later say the child used expressive/communication skills without exposing matcher fields.

---

## 9. Authoring Checklist

Before accepting a `tag_block.yaml`:

- `activity_id` matches the directory name.
- `entity_binding`, `entity_class`, `tier_range`, and `matchability` make the eligibility boundary clear.
- `matchability.tier_support` agrees with `tier_range.span`.
- `activity_signature.observation_angle` is one closed enum value from `docs/activity_vocabulary.md`.
- `activity_signature.bridge_prerequisites.primary` uses 1-3 closed observation-angle values.
- `activity_signature.mechanic` describes what the child actually does, not just the game style.
- `activity_signature.entity_role` explains whether the photo is subject, exemplar, catalyst, or reference.
- `progression.topic_axis` is exactly one axis and is not treated as the same thing as `observation_angle`.
- `progression.difficulty_level` is an integer `1`, `2`, or `3`.
- `next_step_hint` is written as a suggestion, not a guarantee.
- `atl_skills`, `kud.do`, and `activity_signature.mechanic` are consistent.
- Parent-facing fields are stable enough to aggregate over time.
- Child-facing recap can be generated without exposing matcher-only fields.

---

## 10. Source Map

Use these source docs when a field needs deeper review:

| Need | Source |
|---|---|
| Activity matcher and progression workflow diagrams | `docs/activity_matcher_progression_workflows.md` |
| Schema-required fields and machine validation | `activities/_schema/tag_block.schema.json` |
| Closed `activity_signature` enums and `atl_skills` vocabulary | `docs/activity_vocabulary.md` |
| Field ownership and authoring examples | `docs/activity_tag_block_usage.md` |
| Activity signature design rationale | `docs/plans/2026-04-23-activity-signature-design.md` |
| 7-axis progression ladder and tag-block contract | `docs/progression_axes.md` |
| Evidence-based progression algorithm | `docs/superpowers/specs/2026-04-24-progression-algorithm-design.md` |
| Parent growth path read contract | `docs/parent_growth_path_preview.html` |
| Template 0 tag block preview | `docs/template_0_preview.html` |
