## The Garden Rescue Squad

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Garden Rescue Squad |
| Activity Category | Collection/Tracking Exploration (Out-of-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Responsibility, Connection |
| Related Concepts | Care, Interdependence, Empathy, Conservation |
| ATL Skills Focus | Social Skills (empathy, cooperation), Thinking Skills (creative thinking, transfer), Communication Skills (expressing) |
| Game Style | rescue_team |
| Design Version | 1.0 |
| Last Updated | 2026-04-21 |

### A.1 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/plants/generic_flowers.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_0.appearance.petals
  - tier_0.appearance.stem
  - tier_0.appearance.leaves
  - tier_0.state.droopy_or_fresh
  - tier_1.context.sun_and_water
  - tier_1.function.stem_support
  - tier_1.state.signs_of_needing_help
  - tier_1.state.fresh_healthy_look
  - tier_2.change.wilting_and_recovery
  - tier_2.context.garden_care_system
  - tier_2.context.neighbors_in_the_garden
  - tier_2.function.structural_support_for_petals
```

### A.2 Constellation Adaptation Notes

Recipe for running this activity when the photographed entity is a constellation
neighbor of Flower (e.g., other garden plants like tulip, rose, daisy, potted
houseplant, herb sprig) instead of a generic flower. The neighbor list, bridge
type, and initial bridge prompt will live in `data/constellation_map.yaml`
under `mapped_entity: flower` (Cat5 entry pending per that file's coverage
notes) — this section describes how The Garden Rescue Squad adapts mechanically
for a bridged entity.

**Preserve** — must not change across neighbors:
- The "Rescue Captain" role_title and the 3-more-finds mission (dry leaf + fallen twig + lonely pebble joining the seed plant) — the mutual-aid team needs all four to form.
- The MUTUAL AID synthesis in Step 4 where rescued items help EACH OTHER (leaf shades pebble, twig props petal, pebble anchors leaf) — this flip from one-way care to interdependence IS the Nurture-pillar magic moment.
- The signs-of-need diagnostic frame ("petals drooping", "edges curling", "fallen over") — observing distress and naming a care solution is the Responsibility key-concept landing.

**Swap** — re-phrase for the bridged entity:
- Transition bridge "Its petals are drooping down" → neighbor's distress-signal (tulip: "its tall stem is bending — too tired to stand"; rose: "one petal hanging, a thorn looks stuck"; potted plant: "the soil looks dry and cracked"; herb sprig: "leaves turning pale from too much sun").
- Round 4 finale "the twig props up a wilting PETAL" → neighbor's supportable part (tulip: "the twig props up the tall stem"; potted plant: "the pebble weighs down soil so it doesn't blow away"). The neighbor's specific body part replaces "petal" in the mutual-aid cross-references.
- Seed slot label "Flower — needs water" in the mission card → the neighbor's actual need (tulip: "Tulip — needs support"; dry potted plant: "Plant — needs water and shade"; rose with a bent stem: "Rose — needs gentle hands").
- Care solution menu in Round 1 (water / shade / hug) → broadened for indoor/container plants (potted: "water + better spot near window"); don't force outdoor-only solutions on a houseplant.

**Watch** — gotchas to avoid:
- Cactus and succulents don't want "water" as the default fix — if bridged, check the neighbor first; offering water to a droopy cactus is wrong-care; pivot to "less water, more light".
- If the seed plant is a potted houseplant (indoor, solo on a windowsill), the child may have no garden around them to find the 3 other rescues — pivot rescues to other indoor items (a droopy paper flower, a dusty vase, a wilted bouquet leaf).
- Never name the mutual aid pattern before Step 4 — if the child spots it in Round 2 ("the pebble could help the leaf!"), the AI praises but defers the reveal until all 4 are rescued; premature reveal drains the climax.

### B. Activity Overview

**① Brief Description**

The child photographs a flower and notices it looks a little droopy. The AI frames the child as a "Rescue Captain" leading a Garden Rescue Squad. The child explores the garden to find 3 more things that need help — a dry leaf, a fallen twig, a lonely pebble — and proposes care for each. At synthesis, the rescued items help EACH OTHER: the leaf shades the pebble, the twig props up a wilting petal, the pebble holds down the leaf in the wind.

**② Educational Purpose (KUD)**

- **K (Know):** Plants and garden things can show signs of needing help (drooping, drying, falling); water, shade, and support are ways to help living things; different items in a garden have different needs; things that receive help can also give help to others
- **U (Understand):** When we notice something needs help, we can take Responsibility by thinking of a solution; things that seem separate in a garden are actually Connected — they can support each other in surprising ways
- **D (Do):** Observe signs of need in natural objects; propose creative care solutions for garden items; explain how rescued items could help each other

**③ Design Highlight**

The mutual aid synthesis is the star mechanic. After the child rescues 3–4 items by proposing care, the AI flips the script: "Now your rescue team is complete — but guess what? They can help EACH OTHER!" The child discovers that the leaf they watered can shade the pebble, the twig they propped up can support a drooping petal, and the pebble can anchor the leaf in the wind. This transforms one-way caregiving into a web of interdependence.

**④ Typical Scenario**

A child in a garden photographs a droopy flower, then searches for 3 more nearby things that need help — proposing care for each — and discovers at the end that all the rescued items can help one another.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (tender, concerned) "Oh, look at this flower! Its petals are drooping down a little, like it is feeling tired. I think it might need some help. What do you think it needs?"

**Child responses:**

1. (Ideal) "It needs water!" / "It looks thirsty!"
2. (Unexpected) "It's pretty!" / "I like the color!"
3. (No response) Child looks at the flower quietly.

**AI follow-up:**

1. (warm, impressed) "Water — great idea! A little drink would perk those petals right up. You already know how to help! I bet other things in this garden need help too."
2. (warm, agreeing) "It IS pretty! Even pretty flowers get tired sometimes. See how the petals droop? Maybe it needs a little water or some shade. You could be its helper!"
3. (wait 2s) (gentle, coaxing) "See how its petals hang down? It looks a little sleepy. Maybe it needs water, or a friend nearby. What do you think would help?"

**Screen:** Flower photo centered with soft warm glow, drooping petals subtly highlighted, and tiny water droplet and sun icons floating nearby.


#### Step 2: Rule Introduction + Demo

**AI says:** (heroic, rallying) "You are now the Rescue Captain of the Garden Rescue Squad! Your mission has three parts. First, find three things nearby that need help. Second, tell me what each one needs. Third, we will see how they can help each other! Ready, captain?"

**Child responses:**

1. (Ideal) "Ready!" / "Let's rescue things!"
2. (Unexpected) "What kind of things need help?"
3. (No response) Child looks around the garden uncertainly.

**AI follow-up:**

1. (excited, encouraging) "Let's go, captain! Look around the garden — on the ground, near bushes, by the path. Find something that looks dry, fallen, or lonely. Take a photo when you spot it!"
2. (warm, helpful) "Great question! Look for things that are dry, fallen over, cracked, or all alone. Like a leaf that is curling up, or a stick that fell down. Anything that looks like it could use a friend!"
3. (wait 2s) (gentle, guiding) "Try looking near the ground first. See any dry leaves? Fallen sticks? A little stone all by itself? Take a photo of anything that looks like it needs help!"

**Screen:** Mission card with "Rescue Captain" badge (shield with leaf and heart), four collection slots (first filled with flower photo labeled "Flower — needs water"), three empty slots with red cross icons, and numbered checklist.


#### Step 3: Multi-Round Interaction

**Round 1:**

*(Child takes a photo of a dry, curled leaf on the ground)*

**AI says:** (concerned, caring) "Oh no, look at this leaf! It is all dry and curled up at the edges. It looks like it has been in the sun too long. What do you think it needs, captain?"

**Child responses:**

1. (Ideal) "Water!" / "It needs a drink!" / "Shade!"
2. (Unexpected) "It's crunchy!" / "I can step on it!"
3. (No response) Child looks at the leaf silently.

**AI follow-up:**

1. (warm, celebrating) "Yes! A little water would help it uncurl. *Imagine the leaf slowly opening up, getting softer and greener.* It is already feeling better thanks to you! Two more rescues to go, captain!"
2. (playful, redirecting) "It IS crunchy! That means it is really dry. Crunchy leaves are thirsty leaves! If we gave it some water, it might uncurl and get soft again. You just figured out what it needs! Two more to find!"
3. (wait 2s) (gentle, prompting) "Feel how dry it looks? When leaves curl up like that, they are thirsty. What if we gave it some water? *The leaf starts to uncurl a tiny bit.* It is getting better! Two more rescues to go!"

**Screen:** Leaf photo slides into second slot labeled "Leaf — needs water," with uncurling leaf animation. Counter: "1 of 3 rescued."

**Round 2 — "The Fallen Twig":** Child photographs a fallen twig; AI says it fell from its tree and looks like it wants to stand up again. Child proposes propping it up or leaning it against something. AI narrates the twig tilting upward proudly. Slot label: "Twig — needs support."

**Round 3 — "The Lonely Pebble":** Child photographs a pebble sitting alone on the path. AI notes it is far from the other pebbles and looks lonely. Child proposes moving it closer to friends. AI narrates the pebble wiggling happily next to its new neighbors. Includes stuck branch — AI suggests looking near the ground by bushes for dry leaves, on the path for lonely stones, or near dirt for fallen twigs.


#### Step 4: Celebration

**AI says:** (excited, building suspense) "Captain, your Garden Rescue Squad is complete! You helped the leaf, the twig, and the pebble. But guess what? Now THEY can help each other! Watch this — the leaf you watered is big and green now. It can give shade to the little pebble when the sun gets too hot! And the twig you propped up? It can lean over and hold up a droopy petal so it catches more sunlight! But here is the big question — how would the pebble help the leaf?"

**Child responses:**

1. (Ideal) "The pebble can hold the leaf down!" / "It can sit on the leaf so the wind does not blow it away!"
2. (Unexpected) "I don't know." / "The pebble is too small to help."

**AI follow-up:**

1. (amazed, celebrating) "YES! The pebble can sit on the leaf and hold it down when the wind blows! The leaf shades the pebble, the twig holds up the petal, and the pebble protects the leaf. They are ALL helping each other! That is what a real rescue team does, captain!"
2. (warm, scaffolding) "Think about it — the leaf is light, and the wind might blow it away. But the pebble is heavy! What if the pebble sat on the leaf to hold it down? See? Even the smallest member of the team can help! They are a real rescue team now!"

**AI says:** (proud, reflective) "Captain, look at what you did! You found four things that needed help. You gave each one exactly what it needed. And then something amazing happened — they started helping EACH OTHER. Which rescue was your favorite?"

**Child responses:**

1. (Ideal) "The pebble because it was lonely!" / "The leaf because it was so dry!"
2. (Unexpected) "I liked finding all of them!" / "Can I rescue more?"

**AI follow-up:**

1. (touched) "That one really needed you! And now it is part of a team. Every member of your rescue squad matters — even the smallest one can do something big for someone else."
2. (warm, celebrating) "You loved ALL of them — that is what makes you such a great captain! And yes, there are always more things that need help. You can be a Rescue Captain every time you go outside!"

**Screen:** All four photos in a circle with animated mutual aid arrows between them (leaf shades pebble, twig supports petal, pebble anchors leaf), glowing heart in center, golden star on favorite, and banner "Rescue Team — Helping Each Other!"


#### Step 5: Closing + IB Concepts

**AI says:** (proud, warm celebration) "You are an incredible Rescue Captain! You found things that needed help and gave each one care. That is Responsibility — when you notice something needs help and you do something about it. And then your rescue team helped each other — the leaf shaded the pebble, the twig propped up the petal, the pebble held down the leaf. That is Connection — everything in a garden is linked together, helping one another. You earned your Rescue Captain badge!"

**Screen:** "Rescue Captain" badge — green shield with golden heart and four item icons (flower, leaf, twig, pebble). "Responsibility" and "Connection" in artistic green and gold lettering with caring-hands and linked-chain icons. Four collection photos as insets around the badge.
