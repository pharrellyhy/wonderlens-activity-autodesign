# Entity Bridging: Constellation, Property Bridge & Conversation-Only Fallback

## Problem

When a child photographs an entity NOT in the IB mind map (~21 mapped entities), the current system falls through to Tier C (template-generated game, 6-7/10 quality). This creates two problems:

1. **Quality cliff** — Tier C games feel generic compared to Tier A/B gold standards
2. **Missed connections** — Many unmapped entities are semantically close to mapped ones, but the system treats them as completely unknown

The upstream multi-turn conversation is an untapped opportunity. Before the game starts, the conversation can **naturally bridge** the child toward a mapped entity or a game-compatible property — turning an unknown entity into a known game path.

### Design Principle

**Discovery, not redirection.** The child's photographed entity is always honored. Bridges are additive connections ("your kitten is a cousin of a lion!"), never replacements ("let's look at something else"). If no natural bridge exists, we don't force one — we give the child a rich conversation ending instead of a bad game.

---

## Three Bridging Layers

```
Child photographs entity
    ↓
Entity in IB mind map?
    ├── YES → Normal flow (Tier A/B via Style Recommender)
    │
    └── NO → Layer 1: Entity Constellation match?
              ├── YES (score ≥ 0.7) → Bridge in conversation → Tier A/B game
              │
              └── NO → Layer 2: Property Bridge available?
                        ├── YES → Attribute-driven game
                        │
                        └── NO → Layer 3: Conversation-only mode
                                  (rich ending, no game)
```

---

## Layer 1: Entity Constellation Bridging

### Concept

Each mapped entity has a **constellation** — a cluster of semantically related unmapped entities that can naturally bridge to it in conversation.

### Constellation Table

| Mapped Entity | Constellation | Bridge Type | Bridge Prompt Pattern |
|---|---|---|---|
| lion | cat, kitten, tiger, leopard, stuffed lion | Same taxonomy | "Your [entity] is part of the cat family, just like a lion!" |
| teddy_bear | stuffed bunny, plush toy, doll, sock monkey | Same role | "Your [entity] is a cozy friend, just like a teddy bear!" |
| bicycle | toy car, scooter, skateboard, tricycle, wagon | Shared affordance | "Your [entity] has wheels, just like a bicycle!" |
| playground | swing, slide, seesaw, sandbox, climbing frame | Part-of | "That [entity] is part of a playground!" |
| banana | plantain, fruit bowl, mango, pear | Same domain | "Your [entity] is a fruit, just like a banana!" |
| sunflower | tulip, daisy, rose, wildflower | Same domain | "Your [entity] is a flower — like a sunflower's cousin!" |
| goldfish | pond fish, betta, turtle, frog | Shared habitat | "Your [entity] lives in water, just like a goldfish!" |
| piano | guitar, drum, xylophone, music box | Same domain | "Your [entity] makes music, just like a piano!" |
| crayons | colored pencils, markers, paintbrush, chalk | Same role | "Your [entity] is for making art, just like crayons!" |
| raincoat | umbrella, rain boots, jacket, poncho | Shared affordance | "Your [entity] keeps you dry, just like a raincoat!" |
| firefighter | police officer, doctor, nurse, mail carrier | Same domain | "Your [entity] is a helper, just like a firefighter!" |
| toothbrush_holder | soap dish, towel rack, cup holder | Companion | "Your [entity] lives in the bathroom, just like a toothbrush holder!" |
| stop_sign | traffic light, crosswalk sign, speed bump | Same domain | "Your [entity] tells people what to do, just like a stop sign!" |
| toy_robot | action figure, toy dinosaur, LEGO figure | Same role | "Your [entity] is a toy with cool parts, just like a robot!" |
| rubber_duck | bath toy, toy boat, floating ring | Companion | "Your [entity] loves bath time, just like a rubber duck!" |
| double_rainbow | sunset, clouds, rain puddle, prism | Same domain | "Your [entity] is made of light and color, just like a rainbow!" |
| eye | magnifying glass, glasses, mirror, camera | Shared affordance | "Your [entity] helps you see things, just like an eye!" |
| green_apple | orange, pear, strawberry, cherry | Same domain | "Your [entity] is a fruit, just like a green apple!" |
| city_library | bookstore, school, museum, post office | Same domain | "Your [entity] is a special building, just like a library!" |
| sandy_beach | lake shore, river bank, pool, water park | Shared habitat | "Your [entity] is near water, just like a sandy beach!" |

### Bridge Types Reference

| # | Bridge Type | Logic | Strength |
|---|---|---|---|
| 1 | Same taxonomy | Both in the same biological/categorical family | Very strong |
| 2 | Part-of / whole | One is a component of the other | Very strong |
| 3 | Same domain | Both in the same broad category | Strong |
| 4 | Shared affordance | Both DO the same thing (wheels, protection, music) | Strong |
| 5 | Same role | Both serve the same purpose in a child's life | Strong |
| 6 | Companion / co-occurrence | Often found together in real life | Moderate |
| 7 | Shared habitat | Both found in the same environment | Moderate |
| 8 | Sensory similarity | Feel/sound/look similar | Moderate |
| 9 | Cause-effect / process | One leads to or comes from the other | Moderate |
| 10 | Emotional / affective | Evoke similar feelings | Weak |
| 11 | Seasonal / temporal | Associated with the same time/season | Weak |
| 12 | Scale analogy | Similar size relationship to the child | Weak |
| 13 | Metaphorical | Imaginative resemblance | Weak |
| 14 | Contrast / opposite | Interesting because they're different | Weak |

Bridge types with strength "Weak" should only be used if no stronger bridge exists, and the conversation goes there naturally.

### Conversation Bridge Flow

```
Turn 1-3: Normal conversation about the child's entity
    ↓
Turn 4-5: AI draws a natural connection (IB: Connection concept)
  "Your kitten has such soft fur around its face — almost like a tiny mane!
   Did you know lions have HUGE manes? Your kitten is a baby cousin of a lion!"
    ↓
Turn 5-6: Check child's response
  ├── Child engages ("My kitten goes MEOW!")
  │     → Continue bridging: "I bet your kitten could ROAR if it tried!"
  │     → Game: use mapped entity's gold standard, adapted for child's entity
  │
  └── Child ignores / stays on original entity
        → Drop bridge gracefully, never retry
        → Fall through to Layer 2 or 3
```

### Bridge Rules

1. **One attempt only** — never retry a failed bridge in the same conversation
2. **Honor the original** — the bridge adds a connection, never dismisses the child's entity
3. **Category must match** — don't bridge a Cat1 entity to a Cat5 gold standard (context mismatch: indoor→outdoor)
4. **Minimum score 0.7** — don't force weak bridges
5. **The game references both** — "Since your kitten is a cousin of a lion, let's see if your kitten can perform like one!"

---

## Layer 2: Property Bridge

### Concept

When no entity constellation match exists, the system can bridge on a **detected visual attribute** of the photographed entity. Instead of matching entity-to-entity, it matches attribute-to-game-mechanic.

### How It Works

```
Child photographs "fork"
    ↓
Entity recognition: fork — NOT in mind map, no constellation match
    BUT: detected attributes: [shiny, metal, pointy, silver]
    ↓
Property Bridge: "metal" → field_experiment hypothesis
    "Your fork is made of METAL! I wonder — are most things
     in your kitchen metal, or something else?"
    ↓
Game: property-driven field_experiment (not entity-specific)
    Hypothesis: "Are most kitchen things metal or not-metal?"
    Mechanic: same as playground gold standard
    Quality: 7-8/10 (structured game with real mechanic)
```

### Bridgeable Properties

Only visually-verifiable properties are eligible (per field_experiment visual verification constraint):

| Property | Detection Method | Game Styles It Enables |
|---|---|---|
| **Color** | AI vision (red, blue, green, yellow...) | quest_collector, field_experiment |
| **Shape** | AI vision (round, pointy, flat, long, square) | quest_collector, mystery_trail |
| **Material type** | AI vision (metal, wood, plastic, fabric, stone) | field_experiment, mix_lab |
| **Size** | AI vision + context (big, small, tiny, huge) | field_experiment, quest_collector |
| **Alive / not-alive** | AI vision (plant, animal, object) | field_experiment, rescue_team |
| **Natural / man-made** | AI vision | field_experiment |
| **Pattern** | AI vision (stripes, spots, zigzags, lines) | mystery_trail |
| **Visible texture** | AI vision (rough-looking, smooth-looking, fuzzy, bumpy) | mix_lab |
| **Sound potential** | Inferred from visual form (stick=tap, leaf=rustle) | ensemble_show |
| **Shininess** | AI vision (reflective/glossy vs matte/rough) | field_experiment |
| **Movement capability** | AI vision (has wheels, legs, wings, can roll) | quest_collector |
| **Age/wear** | AI vision (rust, cracks, fading vs bright, clean) | field_experiment |

### Property-Bridge Game Templates (Cat5)

12 reusable game shells parameterized by detected properties, covering all 6 Cat5 styles:

| # | Template | Style | Pillar | Property Parameter | Files |
|---|---|---|---|---|---|
| 1 | **Shape Quest** | quest_collector | Adventure | round, pointy, flat, curvy | `shape_quest_property_gold_*` |
| 2 | **Color Scout** | quest_collector | Adventure | red, blue, green, yellow | `color_scout_property_gold_*` |
| 3 | **Movers Quest** | quest_collector | Adventure | wheels, legs, wings, rolls | `movers_quest_property_gold_*` |
| 4 | **Material Lab** | field_experiment | Discovery | metal, wood, plastic, natural | `material_lab_property_gold_*` |
| 5 | **Size Experiment** | field_experiment | Discovery | bigger/smaller than hand | `size_experiment_property_gold_*` |
| 6 | **Nature vs Made** | field_experiment | Discovery | natural, man-made | `nature_vs_made_property_gold_*` |
| 7 | **Shiny Experiment** | field_experiment | Discovery | shiny, dull/matte | `shiny_experiment_property_gold_*` |
| 8 | **Old vs New** | field_experiment | Discovery | worn/faded, bright/clean | `old_vs_new_property_gold_*` |
| 9 | **Pattern Trail** | mystery_trail | Mystery | stripes, spots, zigzags | `pattern_trail_property_gold_*` |
| 10 | **Texture Mix** | mix_lab | Creation | rough, smooth, fuzzy, bumpy | `texture_mix_property_gold_*` |
| 11 | **Sound Stage** | ensemble_show | Performance | inferred from visual form | `sound_stage_property_gold_*` |
| 12 | **Living Rescue** | rescue_team | Nurture | alive, plant, growing | `living_rescue_property_gold_*` |

**Style coverage**: All 6 Cat5 styles represented. A child could photograph the same entity 6 different times and get 6 genuinely different games.

### Property-Bridge Game Templates (Cat1) — Planned

Cat1 property-bridge works differently: the property **seeds the game mechanic** about the single photographed entity, rather than driving a collection criterion.

| # | Template | Style | Pillar | How property drives the game | Status |
|---|---|---|---|---|---|
| 13 | **Detail Detective** | mystery_lens | Mystery | AI picks a property-related detail: "I spy something [shape] on your [entity]!" | Planned |
| 14 | **What-If Workshop** | inventor_workshop | Creation | "Your [entity] is [property]. What if it was [OPPOSITE]?" | Planned |
| 15 | **Property Predictor** | prediction_lab | Discovery | "What happens if your [entity]'s [property] CHANGED?" | Planned |
| 16 | **Time Shifter** | time_traveler | Adventure | "Your [entity] is [property] NOW. What was it BEFORE?" | Planned |
| 17 | **Fix-It Station** | care_station | Nurture | "Your [entity] looks a little [worn]! Let's help!" | Planned |
| 18 | **Property Performer** | voice_stage | Performance | "Your [entity] is SO [property]! Perform like something [property]!" | Planned |

**Total**: 18 property-bridge templates (12 Cat5 complete + 6 Cat1 planned).

### Property Bridge in Conversation

The conversation naturally introduces the property:

```
Turn 1-3: Normal conversation about the child's fork
  "Wow, your fork is SO shiny! Feel how smooth and hard it is —
   that's because it's made of METAL!"
    ↓
Turn 4: Property introduction
  "I have a fun question — is EVERYTHING in your kitchen metal?
   Or are some things made of something different? Let's find out!"
    ↓
Game: Material Lab template with property=metal
```

This feels natural because the property IS a genuine attribute of the child's entity — we're not redirecting away from it, we're exploring deeper.

---

## Layer 3: Conversation-Only Mode

### When It Triggers

- No entity constellation match (Layer 1 fails)
- No viable property bridge (Layer 2 fails — entity has no visually-distinctive property, or child is in a context where collection isn't possible)

### Design

The conversation ends with a satisfying IB-aligned closing instead of a forced game:

```
AI: "You discovered so many amazing things about your [entity] today!
     You noticed its [attribute 1] — that's Form, understanding what things
     look like! And you figured out [attribute 2] — that's Function,
     understanding what things do! You're a real [entity] expert now!"
```

**What the child gets:**
- Full multi-turn conversation (5-10 turns) — educationally complete
- IB concept celebration from the conversation itself
- A "Discovery Badge" — visual reward, no game required
- Gentle suggestion: "Next time, try photographing a [mapped entity near you] — I have an AMAZING game for that!"

### Conversation-Only Closing Pattern

```
Step 1: Celebrate what child discovered
  "You found out [specific things from conversation]. That's incredible!"

Step 2: Name IB concepts naturally
  "You looked closely at what [entity] is like — that's Form!
   You figured out how it works — that's Function!"

Step 3: Award Discovery Badge
  "You earned your [Entity] Expert Badge!"

Step 4 (optional): Gentle funnel
  "Know what? I have an amazing game about [related mapped entity].
   If you see one, photograph it and we'll play!"
```

The gentle funnel in Step 4 is important — it turns a "no game" moment into anticipation for the next session. The child isn't disappointed; they're excited about what's next.

---

## Integration with Style Recommender

The Entity Bridging system sits **upstream** of the Style Recommender:

```
Entity photographed
    ↓
IB mind map lookup
    ├── FOUND → Style Recommender (existing flow)
    │
    └── NOT FOUND → Entity Bridging System
                      ├── Layer 1 (Constellation) → Bridge → Style Recommender with mapped entity
                      ├── Layer 2 (Property) → Property-bridge template (bypasses Style Recommender)
                      └── Layer 3 (Conversation-only) → No game (bypasses Style Recommender)
```

### Changes to Style Recommender

The Style Recommender spec (`2026-04-01-style-recommender.md`) needs a small update:

1. **Three-Tier selection becomes Four-Tier**:
   - Tier A: Entity's own gold standard (10/10)
   - Tier B: Compatible gold standard adapted (8/10)
   - Tier B+: Constellation-bridged gold standard (8/10, via Layer 1)
   - Tier P: Property-bridge template game (7-8/10, via Layer 2)
   - ~~Tier C: Template generation (6-7/10)~~ → **Removed. No game instead.**

2. **Batch pre-computation** adds constellation data per entity

3. **Conversation-only fallback** replaces Tier C as the bottom of the funnel

### Changes to Existing Gold Standards

Each gold standard gets a small addition — **constellation adaptation notes** — describing how to adapt the game for constellation entities:

```yaml
# Added to each gold standard's Basic Info
constellation_notes:
  adaptable_entities: [kitten, cat, tiger, stuffed lion]
  swap_guidance: "Replace 'roar' with entity-appropriate sounds.
                  Keep talent show framing and judge characters.
                  Change habitat references from jungle to match entity."
```

This is a light annotation, not a redesign.

### New Files Needed

| File | Purpose | Status |
|---|---|---|
| `docs/plans/2026-04-08-entity-bridging.md` | This design doc | ✅ Done |
| `prompts/constellation_bridge.md` | Conversation agent bridging prompts | Planned |
| `constellation_map.yaml` | Entity constellation data (batch pre-computed) | Planned |
| Update: `conversation_bridge.md` | New §5: Entity Bridging Patterns | Planned |
| Update: `2026-04-01-style-recommender.md` | Cross-reference, remove Tier C | ✅ Done |

### Property-Bridge Templates — Status

**12 Cat5 templates** (all complete — spec + prod):

| # | Template | Style | Pillar | Property | Status |
|---|---|---|---|---|---|
| 1 | Shape Quest | quest_collector | Adventure | shape | ✅ `shape_quest_property_gold_*` |
| 2 | Color Scout | quest_collector | Adventure | color | ✅ `color_scout_property_gold_*` |
| 3 | Movers Quest | quest_collector | Adventure | movement | ✅ `movers_quest_property_gold_*` |
| 4 | Material Lab | field_experiment | Discovery | material | ✅ `material_lab_property_gold_*` |
| 5 | Size Experiment | field_experiment | Discovery | size | ✅ `size_experiment_property_gold_*` |
| 6 | Nature vs Made | field_experiment | Discovery | natural/man-made | ✅ `nature_vs_made_property_gold_*` |
| 7 | Shiny Experiment | field_experiment | Discovery | shininess | ✅ `shiny_experiment_property_gold_*` |
| 8 | Old vs New | field_experiment | Discovery | age/wear | ✅ `old_vs_new_property_gold_*` |
| 9 | Pattern Trail | mystery_trail | Mystery | pattern | ✅ `pattern_trail_property_gold_*` |
| 10 | Texture Mix | mix_lab | Creation | visible texture | ✅ `texture_mix_property_gold_*` |
| 11 | Sound Stage | ensemble_show | Performance | sound potential | ✅ `sound_stage_property_gold_*` |
| 12 | Living Rescue | rescue_team | Nurture | alive/not-alive | ✅ `living_rescue_property_gold_*` |

**6 Cat1 templates** (all complete — spec + prod):

| # | Template | Style | Pillar | How property seeds the game | Files |
|---|---|---|---|---|---|
| 13 | Detail Detective | mystery_lens | Mystery | "I spy something [property] on your [entity]!" | `detail_detective_property_gold_*` |
| 14 | What-If Workshop | inventor_workshop | Creation | "What if your [entity] was [opposite property]?" | `what_if_workshop_property_gold_*` |
| 15 | Property Predictor | prediction_lab | Discovery | "What happens if [property] changed?" | `property_predictor_property_gold_*` |
| 16 | Time Shifter | time_traveler | Adventure | "[Property] NOW → what was it BEFORE?" | `time_shifter_property_gold_*` |
| 17 | Fix-It Station | care_station | Nurture | "Looks [worn]! Let's help!" | `fix_it_station_property_gold_*` |
| 18 | Property Performer | voice_stage | Performance | "SO [property]! Perform like it!" | `property_performer_property_gold_*` |

**Total**: 18 property-bridge templates (12 Cat5 + 6 Cat1) — all complete.

---

## Verification

### Layer 1 (Constellation)
- Test 10 unmapped entities that HAVE constellation matches
- Verify bridge conversation feels natural (not forced)
- Verify adapted game still passes D9 (Game Feel) and D10 (Pillar Fidelity)
- Test failed bridges: does the system drop gracefully?

### Layer 2 (Property Bridge)
- Test 10 unmapped entities with detectable properties
- Verify property-bridge game feels coherent (not random)
- Compare quality: property-bridge game vs. old Tier C template → should be better
- Verify visual verification constraint holds (no banned properties used)

### Layer 3 (Conversation-only)
- Test 5 entities with NO bridge path
- Verify conversation ending feels complete (not abrupt)
- Verify Discovery Badge provides satisfying closure
- Test gentle funnel: does the suggestion of a mapped entity feel natural?

### End-to-End
- Run 20 random unmapped entities through the full pipeline
- Track: how many route to Layer 1 vs 2 vs 3?
- Target distribution: ~40% Layer 1, ~40% Layer 2, ~20% Layer 3
- Verify no entity gets a worse experience than the old Tier C

---

## Critical Files

| File | Role |
|---|---|
| `docs/plans/2026-04-08-entity-bridging.md` | This design doc |
| `docs/plans/2026-04-01-style-recommender.md` | Style Recommender — cross-reference |
| `conversation_bridge.md` | Bridge patterns — add §5 |
| `docs/game_styles.md` | Style taxonomy — reference |
| `templates.md` | Design templates — reference |
| `entity_guidance.md` | Entity mapping — reference |
| `data/mappings_dev20_0318/` | Entity mapping YAML files |
| `designs/cat1/`, `designs/cat5/` | Gold standards — add constellation notes |
