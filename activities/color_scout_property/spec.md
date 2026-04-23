# Color Scout Property — Authoring Spec

> Category 5 (Collection/Tracking Exploration) · Property-bridge template · Parameterized by `{color}`

## Premise

After a child photographs any object, the AI notices a prominent color (e.g., "red") and frames a quest: "Find 3 red things!" The child becomes a Color Scout. For each find, the AI evaluates it against the quest criterion ("Is it red?") — a pass/fail game moment — and then harvests a personal detail ("What does it remind you of?") to generate a character name. Once 3 quest items are collected, the child co-creates a short adventure story starring the "Red Team." The quest criterion gives the collection PURPOSE; the detail harvesting gives each find PERSONALITY. Works for any detected color: red, blue, green, yellow, brown, orange, purple, pink, white, black.

## Target

- **IB axis:** Form (primary) + Connection (secondary)
- **Primary rung:** T1 (ages 4–6)
- **Tier elasticity:** T0–T2 (±1)
- **Age tier:** child is old enough to photograph, listen to a multi-round quest, and invent short character names.

## Pedagogical rationale

Color is the most perceptually accessible of all surface properties at T1, yet children rarely experience "color" as a dimension that cuts across dissimilar things. This game makes the abstract idea of a color *property* concrete: a fire truck, a strawberry, and a ladybug are all "red" even though they share nothing else. The quest criterion ("Is it red? — YES!") turns the property into a classifier the child practices. The detail-harvest ("What does it remind you of?") keeps the activity in the imaginative/expressive register, not a rote sort. Together they scaffold the IB Key Concepts of **Form** (what it looks like) and **Connection** (surprising links between unlike things).

## Selection trigger

Fires whenever the matcher finds a color property on the photographed entity:

- `tier_0.appearance.color` — most common path (raincoat, crayon, piano, library)
- `tier_0.appearance.body_color` — e.g., rubber duck, toy robot, goldfish, lion, bird
- `tier_0.appearance.wing_color` — e.g., butterfly

The matched color value is substituted into the `{color}` template parameter at runtime. Because the trigger is a *property* rather than a specific entity, the game is entity-agnostic: the entity becomes an *exemplar* of the color rather than the subject of the activity. This triggers the role pivot surfaced via `activity_signature.role_pivot_note`.

## Experience pillar & game style

- **Pillar:** Adventure
- **Game style:** `quest_collector` (criterion-driven collection + detail-harvest + story synthesis)
- **Mechanic:** `collect`
- **Observation angle:** `color`
- **Entity role:** `exemplar` (parameterized — the entity becomes one example of the color class)
