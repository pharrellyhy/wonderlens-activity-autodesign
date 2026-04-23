# Mystery Trail Butterfly — Authoring Spec

> Category 5 (Collection/Tracking Exploration) · Bound to `butterfly` (insect class) · Mystery-trail with delayed pattern reveal

## Premise

After a child photographs a butterfly on a flower, the AI marvels at the wings and recruits the child as a "Butterfly World Detective." The AI gives riddle-clues one at a time — each describing something nearby (a flower, a leaf, a wet spot) without naming it — and the child searches, guesses, and photographs what they think matches. After 3 finds, the AI reveals the hidden connection: everything the child found is part of the butterfly's secret world — its food, shelter, and water. The big "aha!" is that the child has been mapping the butterfly's habitat all along without knowing it. That delayed reveal is the Mystery pillar's signature payoff.

## Target

- **IB axis:** Connection (primary, via habitat and interdependence) + Form (secondary, via observable clues)
- **Primary rung:** T1 (ages 4–6)
- **Tier elasticity:** T0–T2 (±1)
- **Age tier:** child can hold a riddle in working memory long enough to search, and can articulate what they found.

## Pedagogical rationale

A butterfly's wing patterns make it a natural observation target, but the deeper idea is that no creature exists in isolation — it lives inside a web of food, shelter, and water sources. This activity doesn't *tell* the child that, it *walks them through it* via three riddle-clues, then reframes the collection at the end ("Everything you found is your butterfly's secret world!"). The child assembles the habitat concept themselves, which is the IB learning-moment the Mystery pillar targets.

The delayed-reveal structure also models scientific inference: observations come first, the pattern emerges second. The riddle-voice ("I'm thinking of something nearby. It's bright and colorful, it has a sweet smell...") is sensory and concrete, keeping the inference accessible at T1. **Form** is the clue layer (bright petals, flat green leaves, wet ground); **Causation** (the original spec's second Key Concept) is the reveal layer (why the butterfly chose this park). We also surface **Connection** via the habitat web — pattern is a strong related concept here because wing patterns are what first drew the child's eye.

## Selection trigger

Fires when the matcher routes a photographed `butterfly` (or close constellation neighbor such as bee, moth, ladybug, or dragonfly) to this activity. Entity-bound — does **not** fire on property matches.

Drives off the insect `tier_guidance` attributes:

- `tier_0.appearance.wing_color`, `wing_shape`, `antennae`
- `tier_0.function.lands_on_flowers`
- `tier_1.appearance.wing_patterns`
- `tier_1.context.flower_visits`, `leafy_rests`, `puddle_visits`
- `tier_1.function.sipping_nectar`
- `tier_2.context.habitat_requirements`, `host_plants_for_eggs`

Constellation neighbors (bee, moth, ladybug, dragonfly) substitute via `data/constellation_map.yaml` under `mapped_entity: butterfly`; the riddle set swaps for the neighbor's food/shelter/water analogs per the `A.2 Constellation Adaptation Notes` in `prod.md`.

## Experience pillar & game style

- **Pillar:** Mystery
- **Game style:** `mystery_trail` (riddle-driven search with delayed pattern reveal)
- **Mechanic:** `collect`
- **Observation angle:** `pattern` (the butterfly's wing pattern is the entry hook; the habitat pattern is the hidden reveal)
- **Entity role:** `subject` (the butterfly IS the case to solve — no role pivot)
