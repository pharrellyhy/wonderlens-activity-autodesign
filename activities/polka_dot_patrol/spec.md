# Polka Dot Patrol — Authoring Spec

> Category 5 (Collection/Tracking Exploration) · Property-bridge on pattern · Exemplified by `ladybug`

## Premise

After the child photographs a ladybug, the AI gasps at its beautiful polka-dotted shell and asks an imaginative question: do those tiny black dots look like buttons, or maybe little windows? The child becomes a "Polka-Dot Patrol Officer" and heads out on a detective adventure to find 3 more things nearby that have dots, spots, or circles — a spotted mushroom, a speckled pebble, a flower with circular markings. Each round the child describes the pattern they found. At synthesis, the child places all three finds side by side and examines how the "same" pattern is actually different every time: big blotchy spots on a mushroom, tiny speckles on a pebble, perfect round circles on a flower petal. The child gives each find a playful name ("Freckle Stone," "Polka Petal") and earns the Polka-Dot Patrol Officer badge.

## Target

- **IB axis:** Form (primary, via pattern as a property) + Connection (secondary, via the surprising link between unrelated spotted things)
- **Primary rung:** T1 (ages 4–6)
- **Tier elasticity:** T0–T2 (±1)
- **Age tier:** child can look closely, compare dot sizes, and verbalize how one pattern differs from another.

## Pedagogical rationale

Pattern is the most abstract of the observable properties — it isn't the object, it sits *on* the object — and T1 children usually see "spotted things" as a flat category. This game makes the child zoom in: yes, a ladybug and a flower both have dots, but the dots themselves behave differently. Big splotches, tiny speckles, and perfect circles are all "the pattern of dots" and also obviously different patterns. This concrete same-but-different comparison is exactly the cognitive move the IB Key Concept of **Form** is pointing at, and it builds into **Connection** when the child sees that unrelated items (bug, stone, petal) share a visual signature.

The creative-naming layer ("Freckle Stone," "Polka Petal") turns scientific observation into personal expression, keeping the activity in the imagination register rather than letting it collapse into a rote sort.

## Selection trigger

Fires whenever the matcher finds a pattern property — specifically dots, spots, or repeating round marks — on the photographed entity. The ladybug is the canonical exemplar, but the activity works for any entity whose detected pattern is dot-based.

Drives off a pattern trigger:

- primary bridge: `pattern` (the dot/spot/circle signature)
- secondary bridges: `color` (the dot's color vs the background), `shape` (the dot as shape)

Because the trigger is pattern-as-property, the entity functions as an *exemplar* of polka-dot pattern rather than the subject of the activity. The role pivot is surfaced via `activity_signature.role_pivot_note`.

## Experience pillar & game style

- **Pillar:** Discovery
- **Game style:** `quest_collector` (from the source gold standard — criterion-driven collection of 3 spotted things, with comparison-chart synthesis)
- **Mechanic:** `collect`
- **Observation angle:** `pattern`
- **Entity role:** `exemplar` (parameterized — the ladybug is one example of the polka-dot pattern class)
