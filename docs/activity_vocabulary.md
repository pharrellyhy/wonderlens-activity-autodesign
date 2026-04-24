# Activity Vocabulary

> **Canonical source** for the three closed enums in Template 0 §04's `activity_signature` block. Any addition here MUST be reflected in both consumer repos' enum code; enum-drift tests compare against this doc.

**Version:** 1.0 · 2026-04-23

---

## observation_angle (10 values)

What attribute/dimension the activity centers on. **Orthogonal to `progression.topic_axis`** — all 7 IB Key Concepts can use all 10 angles (see design spec §3.2 for examples). This is a Layer 1 activity-signature field: the matcher reads it before activity start, and downstream surfaces aggregate it after the session.

| Token | Definition | Example games | Example focal_attribute |
|---|---|---|---|
| `color` | Surface color | Color Scout, Color Friends Adventure | red, blue, yellow |
| `shape` | Outline/form geometry | Shape Quest, Circle Spotter Challenge | round, pointy, long |
| `size` | Absolute or relative scale | Size Experiment | tiny, huge |
| `texture` | Surface feel | Texture Mix, Fluffy Expedition | fuzzy, smooth, rough |
| `material` | Substance composition | Material Lab, Nature vs Made | wood, metal, fabric |
| `pattern` | Repeating visual design | Pattern Trail, Polka Dot Patrol | spots, stripes, zigzag |
| `function` | What it does / how it works | Detail Detective, What-If Workshop | writes, carries, protects |
| `origin` | Where it came from | Time Shifter, Library Book's Journey | natural, man-made, local |
| `behavior` | How it moves/acts/interacts | Mood Changer, Dream Whisperer | roars, hides, flies |
| `state` | Condition | Fix-It Station, Old vs New | worn, fresh, alive |

## mechanic (8 values)

What the child actually does during the activity. This is intentionally coarser than `game_style`: multiple game styles can share one mechanic, and one game style can still carry pillar-specific flavor in `game_style`.

| Token | Definition | Example games |
|---|---|---|
| `enumerate` | Name parts or list attributes | Detail Detective, Mix Lab |
| `compare` | Contrast two+ items | Material Detective, comparison-chart games |
| `collect` | Find N things matching a criterion | Color Scout, Shape Quest, most property bridges |
| `sort` | Categorize into groups | Nature vs Made |
| `voice` | Give the entity a voice | Voice Stage Lion, Playground Voices |
| `build` | Make/invent something | What-If Workshop, Inventor Workshop |
| `predict` | "What happens next?" | Apple What Happens Next, Prediction Lab |
| `narrate` | Tell a story | Library Book's Journey, storytelling_chain games |

## entity_role (4 values)

How the photographed entity participates in this activity.

| Token | Definition | Pivot from conversation? |
|---|---|---|
| `subject` | Activity is about this entity specifically | No pivot (continuity) |
| `exemplar` | Entity is one example of a broader category | Yes — surface via `role_pivot_note` |
| `catalyst` | Entity sparked the question; activity is elsewhere | Yes |
| `reference` | Entity is source material for creating something new | Yes |

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

---

## Versioning

- Adding a value: bump minor (1.0 → 1.1); requires matching change in both consumer repos' enum code
- Removing a value: major bump (1.0 → 2.0); requires migration of all affected games
- Renaming: treat as remove + add

## Consumer mirrors

- `wonderlens-ai/app/modules/activity/activity_signature/vocabulary.py`
- `wonderlens-activity-fullstack-demo/backend/activity_signature/vocabulary.py`

Drift test compares parsed tables above against enum members; failure = CI block.
