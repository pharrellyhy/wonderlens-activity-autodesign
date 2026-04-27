# Activity Vocabulary

> **Canonical source** for the three closed enums in Template 0 §04's `activity_signature` block. Any addition here MUST be reflected in both consumer repos' enum code; enum-drift tests compare against this doc. This file also records the recommended WonderLens `atl_skills` vocabulary used for thinking/learning-skill tagging.

**Version:** 1.3 · 2026-04-27

---

## observation_angle (12 values)

What attribute/dimension the activity centers on. **Orthogonal to `progression.topic_axis`** — all 7 IB Key Concepts can use all 12 angles. `observation_angle` names the attribute under attention; `topic_axis` names the conceptual lens. For example, `observation_angle: quantity` can support Form ("how many?"), Causation ("why more?"), or Change ("did the amount grow?"). See design spec §3.2 for the full explanation. This is a Layer 1 activity-signature field: the matcher reads it before activity start, and downstream surfaces aggregate it after the session.

| Token | Definition | Example games | Example focal_attribute |
|---|---|---|---|
| `color` | Surface color | Color Scout, Color Friends Adventure | red, blue, yellow |
| `shape` | Outline/form geometry | Shape Quest, Circle Spotter Challenge | round, pointy, long |
| `size` | Absolute or relative scale | Size Experiment | tiny, huge |
| `quantity` | Count or amount | Counting Hunt, More-or-Less Mission | three, more, fewer |
| `texture` | Surface feel | Texture Mix, Fluffy Expedition | fuzzy, smooth, rough |
| `material` | Substance composition | Material Lab, Nature vs Made | wood, metal, fabric |
| `pattern` | Repeating visual design | Pattern Trail, Polka Dot Patrol | spots, stripes, zigzag |
| `function` | What it does / how it works | Detail Detective, What-If Workshop | writes, carries, protects |
| `origin` | Where it came from | Time Shifter, Library Book's Journey | natural, man-made, local |
| `behavior` | How it moves/acts/interacts | Mood Changer, Dream Whisperer | roars, hides, flies |
| `emotion` | Perceived feeling, expression, or tone | Voice Stage, Feelings Detective | happy, worried, excited |
| `state` | Condition | Fix-It Station, Old vs New | worn, fresh, alive |

### Observation-angle scope notes

The V1 list is intentionally compact. It is a closed set for stable matcher behavior, not a complete ontology of everything a child can notice.

Usually covered elsewhere:
- `comparison` is usually a `mechanic`, because the child compares; the angle being compared is still `size`, `color`, `material`, etc.
- `sequence` and temporal order usually belong under `progression.topic_axis: change`; add an angle only if the activity truly centers on ordering itself.

Recognition/safety-limited candidates:
- Distance and direction are hard to infer reliably and can create unsafe movement prompts.
- Smell, taste, sound, and temperature are not photo-verifiable; taste is especially safety-sensitive.
- Touch can appear as `texture`, but the runtime should not claim photo certainty when the value requires child report.

## mechanic (10 values)

What the child actually does during the activity. This is intentionally coarser than `game_style`: multiple game styles can share one mechanic, and one game style can still carry pillar-specific flavor in `game_style`.

| Token | Definition | Example games |
|---|---|---|
| `enumerate` | Name parts or list attributes | Detail Detective, Mix Lab |
| `compare` | Contrast two+ items | Material Detective, comparison-chart games |
| `collect` | Find N things matching a criterion | Color Scout, Shape Quest, most property bridges |
| `sort` | Categorize into groups | Nature vs Made |
| `deduce` | Infer an answer from clues or evidence | Mystery Lens, Mystery Trail |
| `voice` | Give the entity a voice | Voice Stage Lion, Playground Voices |
| `build` | Make/invent something | What-If Workshop, Inventor Workshop |
| `predict` | "What happens next?" | Apple What Happens Next, Prediction Lab |
| `narrate` | Tell a story | Library Book's Journey, storytelling_chain games |
| `care` | Notice a need and propose help | Care Station, Rescue Team |

### Mechanic to game-style mapping

`mechanic` is the child's primary action. `game_style` remains the richer activity format and emotional payoff.

| Game style | Pillar | Recommended primary mechanic |
|---|---|---|
| mystery_lens | Mystery | `deduce` |
| mystery_trail | Mystery | `deduce` or `collect` depending on whether clue-solving or physical search is primary |
| inventor_workshop | Creation | `build` |
| mix_lab | Creation | `build` |
| voice_stage | Performance | `voice` |
| ensemble_show | Performance | `voice` |
| prediction_lab | Discovery | `predict` |
| field_experiment | Discovery | `predict` for hypothesis-led experiments; `collect` for simple property hunts |
| time_traveler | Adventure | `narrate` |
| quest_collector | Adventure | `collect` |
| care_station | Nurture | `care` |
| rescue_team | Nurture | `care` or `collect` depending on whether helping or finding is primary |

Imagination does not automatically mean `pillar: Creation` or `mechanic: build`. Mystery, Performance, Adventure, and Nurture can all use imagination. Use Creation only when the emotional payoff is "I made this" and the child invents/builds something.

## entity_role (4 values)

How the photographed entity participates in this activity.

| Token | Definition | Pivot from conversation? |
|---|---|---|
| `subject` | Activity is about this entity specifically | No pivot (continuity) |
| `exemplar` | Entity is one example of a broader category | Yes — surface via `role_pivot_note` |
| `catalyst` | Entity sparked the question; activity is elsewhere | Yes |
| `reference` | Entity is source material for creating something new | Yes |

Examples:
- A red pen that launches "find three red things" is `exemplar`: the pen is one example of red.
- A ladybug chat that opens general animal flashcards is `exemplar` if the framing is "ladybug is one animal; let's look at more animals," but `catalyst` if the ladybug only sparked a separate flashcard activity and no longer participates.
- A ladybug-specific fact activity is `subject`.

## bridge_prerequisites (open lists)

`bridge_prerequisites` is not a fourth enum, but it is part of the same `activity_signature` contract. It tells the matcher which conversation angles the activity naturally extends.

- `primary`: 1-3 closed `observation_angle` values. These are scored against `conversation_signature.dominant_angle` and `secondary_angles`.
- `secondary`: 0-3 values. Prefer closed `observation_angle` values when possible; non-enum descriptors are allowed as editorial notes and ignored by V1 matcher scoring.

Example:

```yaml
bridge_prerequisites:
  primary: [color]
  secondary: [pattern, visibility]
```

Here `color` and `pattern` are canonical enum values; `visibility` documents author intent but does not participate in V1 enum scoring.

Secondary uses beyond initial selection:
- If the child rejects a recommended activity, use compatible bridge prerequisites to swap to a nearby activity instead of a random one.
- If the child finishes with high engagement, use the completed activity's signature as context for the next bridge-compatible activity.
- If a future runtime prepares several activities in advance, bridge prerequisites can help assemble a coherent candidate set.

## atl_skills (recommended controlled vocabulary)

`atl_skills` remains the tag-block field for the child's practiced thinking/learning skills. Internally this keeps compatibility with existing Template 0 logic. Product copy can surface it as "Thinking & Learning Skills" or "孩子练习的思维方式" instead of using the IB term ATL.

Prefer these WonderLens tokens for new activities:

| Token | Parent-facing meaning | Use when the child... |
|---|---|---|
| `counting` | 数量感 / counting | Counts items or target finds |
| `quantity_comparison` | 比较多少 / quantity comparison | Decides more/less, same/different amount |
| `measurement` | 测量与大小判断 / measurement | Compares big/small, long/short, high/low |
| `spatial_reasoning` | 空间推理 / spatial reasoning | Uses position, direction, arrangement, or shape relations |
| `pattern_recognition` | 发现规律 / pattern recognition | Notices repeated forms, colors, rhythms, or visual patterns |
| `observation` | 细致观察 / observation | Looks closely and names evidence |
| `classification` | 分类 / classification | Sorts or groups by a rule |
| `logical_reasoning` | 逻辑推理 / logical reasoning | Uses if/then, evidence, or constraints |
| `causal_reasoning` | 因果推理 / causal reasoning | Explains why something happens |
| `prediction` | 预测 / prediction | Makes a guess before reveal or test |
| `evidence_collection` | 收集证据 / evidence collection | Gathers examples, photos, or observations to support a claim |
| `creative_thinking` | 创造性思考 / creative thinking | Generates new ideas or alternatives |
| `imagination` | 想象 / imagination | Pretends, personifies, or imagines impossible scenarios |
| `narrative_expression` | 叙事表达 / narrative expression | Builds a story sequence or character arc |
| `language_expression` | 语言表达 / language expression | Explains, describes, names, or voices ideas |
| `perspective_taking` | 换位思考 / perspective taking | Considers how another person, animal, or object might feel/see/act |
| `empathy` | 共情 / empathy | Notices needs or feelings and responds with care |
| `collaboration` | 合作 / collaboration | Works with caregiver, AI, or collected items as a team |
| `focus` | 专注 / focus | Sustains attention across rounds or a multi-step task |

Examples:

```yaml
# Find three red things
subject_tags: [math, science]
atl_skills: [counting, observation, classification]
activity_signature:
  observation_angle: color
  mechanic: collect
  entity_role: exemplar
  focal_attribute: red
  bridge_prerequisites:
    primary: [color]
    secondary: [pattern]

# Which group has more?
subject_tags: [math]
atl_skills: [counting, quantity_comparison, evidence_collection]
activity_signature:
  observation_angle: quantity
  mechanic: compare
  entity_role: catalyst
  focal_attribute: more_less
  bridge_prerequisites:
    primary: [quantity]
    secondary: [size]

# Sort by size
subject_tags: [math]
atl_skills: [measurement, classification, logical_reasoning]
activity_signature:
  observation_angle: size
  mechanic: sort
  entity_role: exemplar
  focal_attribute: relative_size
  bridge_prerequisites:
    primary: [size]
    secondary: [shape]
```

---

## Versioning

- Adding a value: bump minor (1.0 → 1.1); requires matching change in both consumer repos' enum code
- Removing a value: major bump (1.0 → 2.0); requires migration of all affected games
- Renaming: treat as remove + add
- Adding recommended `atl_skills` tokens or explanatory mappings: bump minor; schema enforcement remains a separate decision

## Consumer mirrors

- `wonderlens-ai/app/modules/activity/activity_signature/vocabulary.py`
- `wonderlens-activity-fullstack-demo/backend/activity_signature/vocabulary.py`

Drift test compares parsed tables above against enum members; failure = CI block.

## Revnote

- **v1.3 · 2026-04-27** — Adds `quantity` and `emotion` to the closed `observation_angle` enum.
- **v1.2 · 2026-04-27** — Review clarification pass: documents observation-angle scope boundaries, adds game-style-to-mechanic mapping, clarifies entity-role examples, expands bridge-prerequisite uses, and adds the recommended WonderLens `atl_skills` vocabulary.
- **v1.1 · 2026-04-27** — Adds `deduce` and `care` mechanics.
