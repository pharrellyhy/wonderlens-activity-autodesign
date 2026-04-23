# Voice Stage Lion — Authoring Spec

> Category 1 (Sustained Verbal Interaction) · Bound to `lion` (big_cat class) · Voice performance

## Premise

The child becomes a "Roar Star" who performs AS the lion in front of a silly audience of three jungle judges — a parrot, a monkey, and an elephant. Across three rounds, the AI sets a performance challenge (a happy greeting-roar, a sleepy lullaby-roar, and a surprise whisper-roar) and the audience reacts with over-the-top delight: the parrot falls off the branch, the monkey throws popcorn, the elephant trumpets. The surprise whisper-challenge in Round 3 adds genuine stakes ("Nobody thinks you can do it!"), and the finale is a standing ovation. The child leaves feeling "They LOVED it!" — a core Performance-pillar experience.

## Target

- **IB axis:** Connection (primary, via perspective-taking) + Form (secondary, via the lion's recognizable features)
- **Primary rung:** T1 (ages 4–6); elastic to T0 (2–4) with shorter prompts and simpler onomatopoeia
- **Tier elasticity:** T0–T2 (±1)
- **Age tier:** child is verbal enough to make sounds on cue and follow a 3-round call-and-response structure.

## Pedagogical rationale

Giving the lion a voice is a perspective-taking exercise: the child stops observing the lion from the outside and takes its point of view, producing sound AS the lion. Varying the roar across three contrasting emotional registers (happy → sleepy → whisper) makes it concrete that **the same creature expresses itself in many different ways depending on the situation** — a foundation for the IB Key Concept of perspective. The lion's distinctive **Form** (big mane, loud voice, strong body) is what anchors the activity to this specific entity; without the lion, you have no roar, no mane, no stage presence.

Audience reaction (the three judges) transforms voice play into a PERFORMANCE. The child doesn't just speak; they affect listeners. This shifts the learning from self-expression in isolation to communicative expression — closing the Communication Skills ATL loop.

## Selection trigger

Fires when the matcher routes a photographed `lion` (or close constellation neighbor such as toy lion, tiger, or stuffed lion) to this activity. Entity-bound — does **not** fire on property matches.

Drives off the big_cat `tier_guidance` attributes:

- `tier_0.appearance.covering` (mane)
- `tier_0.appearance.body_size`
- `tier_0.senses.sound`
- `tier_1.appearance.mane_look`
- `tier_1.function.communication_roar`

Constellation neighbors (cat, kitten, tiger, leopard, stuffed lion) can substitute via `data/constellation_map.yaml` under `mapped_entity: lion`; see `A.2 Constellation Adaptation Notes` in `prod.md` for preserve/swap/watch rules.

## Experience pillar & game style

- **Pillar:** Performance
- **Game style:** `voice_stage` (voice-driven, audience-reactive, 3-round escalation with surprise twist)
- **Mechanic:** `voice`
- **Observation angle:** `behavior` (how the lion sounds, how the voice varies)
- **Entity role:** `subject` (the lion IS the star — no role pivot)
