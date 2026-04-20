# Entity Ontology

> Canonical class hierarchy for the `entity_class` tag in Template 0's tag block. Every entity appearing in an activity design must have a chain that resolves against this file.

**Version**: v0.1 · 2026-04-20 · Inaugural
**Upstream**: `docs/template_0_preview.html` §04

---

## Purpose

`entity_class` is an ordered list from specific to general (e.g. `[ladybug, beetle, insect, small_creature, living_thing, observable_thing]`). The upstream matcher uses this chain to roll up when exact-entity matches miss — "we have no ladybug activities but we have an `insect` activity tagged `parameterized`, so serve that one."

This file defines which class names are valid and how entities roll up.

---

## Top-level class

- `observable_thing` — the root. Used alone only by `entity_binding: agnostic` activities.

---

## Taxonomic hierarchy

```
observable_thing
├── natural_thing
│   ├── living_thing
│   │   ├── animal
│   │   │   ├── insect
│   │   │   │   ├── beetle
│   │   │   │   │   ├── ladybug
│   │   │   │   │   └── weevil
│   │   │   │   ├── bee
│   │   │   │   ├── ant
│   │   │   │   ├── caterpillar
│   │   │   │   └── butterfly
│   │   │   ├── arachnid
│   │   │   │   └── spider
│   │   │   ├── mollusk
│   │   │   │   ├── snail
│   │   │   │   └── slug
│   │   │   ├── bird
│   │   │   ├── mammal
│   │   │   └── fish
│   │   ├── plant
│   │   │   ├── flower
│   │   │   │   ├── sunflower
│   │   │   │   ├── daisy
│   │   │   │   └── rose
│   │   │   ├── tree
│   │   │   ├── fruit
│   │   │   │   ├── apple
│   │   │   │   └── banana
│   │   │   ├── vegetable
│   │   │   └── leaf
│   │   └── fungus
│   │       └── mushroom
│   └── non_living_natural_thing
│       ├── rock
│       ├── water
│       │   ├── puddle
│       │   └── stream
│       ├── weather_phenomenon
│       │   ├── cloud
│       │   └── rainbow
│       └── celestial
│           ├── sun
│           └── moon
└── human_made_thing
    ├── vehicle
    │   ├── car
    │   ├── bicycle
    │   ├── truck
    │   └── airplane
    ├── tool
    │   ├── scissors
    │   └── paintbrush
    ├── toy
    │   ├── doll
    │   ├── ball
    │   └── block
    ├── food
    │   ├── bread
    │   └── fruit_prepared
    ├── container
    │   ├── cup
    │   └── box
    ├── clothing
    └── instrument
```

---

## Abstract / cross-cutting classes

These aren't strict taxonomy — they tag *capability*. An entity can belong to multiple abstract classes in addition to its taxonomic chain.

| Abstract class | Member examples | Used for activities about |
|---|---|---|
| `small_creature` | ladybug, bee, ant, caterpillar, snail, slug, spider, small bird | Gentle observation, holding, attribute naming |
| `warning_colored_small_creature` | ladybug, bee, wasp, monarch caterpillar, poison-dart frog | Causation (why warning colors?), biology |
| `patterned_thing` | ladybug, zebra, giraffe, butterfly, polka-dot cup, striped fabric | Form, pattern recognition |
| `moving_thing` | any animal, vehicle, leaves in wind, flowing water | Change, motion, causation |
| `handheld_thing` | pencil, apple, cup, toy, small rock | Fine motor, close observation |
| `edible_thing` | fruit, vegetable, bread, prepared food | Sensory, food origin |

---

## Usage rules for activity authors

1. **Every activity with a specific nominal entity** declares an `entity_class` chain starting at the entity and rolling up to `observable_thing`.
2. **Abstract class memberships are additive** — an activity can target `entity_class: [ladybug, beetle, insect, small_creature, warning_colored_small_creature, living_thing, observable_thing]` to enable rollup on either axis.
3. **`entity_binding: agnostic` activities** use the minimal chain: `entity_class: [observable_thing]`.
4. **Adding a new entity**: if your activity uses an entity not in this file, add it to the ontology in the same PR as the activity. New entities never break existing chains.
5. **Never shrink the ontology** — renaming or removing a class is a breaking change (see Versioning).

---

## Example chains

| Nominal entity | Typical chain |
|---|---|
| ladybug | `[ladybug, beetle, insect, small_creature, warning_colored_small_creature, patterned_thing, living_thing, natural_thing, observable_thing]` |
| sunflower | `[sunflower, flower, plant, living_thing, natural_thing, observable_thing]` |
| apple | `[apple, fruit, plant, edible_thing, living_thing, natural_thing, observable_thing]` |
| car (toy) | `[car, vehicle, moving_thing, human_made_thing, observable_thing]` |
| cloud | `[cloud, weather_phenomenon, non_living_natural_thing, natural_thing, observable_thing]` |

---

## Versioning

- **v0.1** (2026-04-20) — Inaugural file. Covers the 7 running examples across Template 0 + surfaces docs (ladybug, sunflower, apple, ladybug variations) plus enough breadth to seed matcher development.

Append-only growth. Breaking changes bump to v1.0 and require coordinated migration of all tag blocks.
