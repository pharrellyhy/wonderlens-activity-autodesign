# Shape Quest Property — Authoring Spec

> Category 5 (Collection/Tracking Exploration) · Property-bridge template · Parameterized by `{shape}`

## Premise

After a child photographs any object, the AI notices a prominent shape attribute (e.g., "round") and frames a quest: "Find 3 things that are round!" The child becomes a Shape Scout. Each find is evaluated against the criterion ("Is it round? — YES!"), creating a pass/fail game moment, and then the AI harvests a personal detail ("What does it remind you of?") to generate a character name. Once 3 quest items are collected, the child co-creates a short adventure story where all the shape-friends roll, bounce, or spin together. The quest criterion gives the collection PURPOSE; the detail harvesting gives each find PERSONALITY. Works for any detected shape: round, pointy, flat, long, curvy.

## Target

- **IB axis:** Form (primary) + Connection (secondary)
- **Primary rung:** T1 (ages 4–6)
- **Tier elasticity:** T0–T2 (±1)
- **Age tier:** child can listen to a multi-round quest, compare objects by shape, and invent short character names.

## Pedagogical rationale

Shape is one of the earliest categorization dimensions children can articulate verbally, but most T1 children still treat shape as *belonging to the object* ("the ball is a ball") rather than as an independent property that cuts across unlike things. This game decouples shape from category: a wheel, a coin, and a cookie are all round but serve completely different purposes. The quest criterion turns shape into a classifier the child practices ("Is it round? — YES!"). Comparing the finds side-by-side in the synthesis step surfaces **Form** as a property the world shares, and **Connection** as the surprising link between dissimilar things with the same shape.

## Selection trigger

Fires whenever the matcher finds a shape property on the photographed entity:

- `tier_0.appearance.shape` — most common path
- `tier_0.appearance.body_shape` — e.g., toy robot
- `tier_0.appearance.wing_shape` — e.g., butterfly
- `tier_1.appearance.hood_shape` — entity-specific shape features also qualify (e.g., raincoat)

The matched shape value is substituted into the `{shape}` template parameter at runtime. Because the trigger is a *property* rather than a specific entity, the game is entity-agnostic: the entity becomes an *exemplar* of the shape rather than the subject of the activity. This triggers the role pivot surfaced via `activity_signature.role_pivot_note`.

## Experience pillar & game style

- **Pillar:** Discovery
- **Game style:** `quest_collector` (criterion-driven collection + detail-harvest + story synthesis)
- **Mechanic:** `collect`
- **Observation angle:** `shape`
- **Entity role:** `exemplar` (parameterized — the entity becomes one example of the shape class)
