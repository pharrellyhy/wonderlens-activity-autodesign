# WonderLens Game Style Taxonomy

Twelve interaction patterns for WonderLens activities, organized under six Experience Pillars. Each pillar defines a distinct emotional experience for the child. Use this reference when designing new activities: pick a pillar and style, then follow its structure.

---

## Experience Pillars Overview

| # | Pillar | Child feels... | Magic moment | Game element | Cognitive domain |
|---|--------|---------------|-------------|-------------|-----------------|
| 1 | **Mystery** | "I figured it out!" | Hidden truth revealed | Clues → deduction → aha! | Reasoning, spatial |
| 2 | **Creation** | "I made this!" | Invention unveiled | Open-ended building | Divergent thinking |
| 3 | **Performance** | "They loved it!" | Audience ovation | Express → react → encore | Empathy, communication |
| 4 | **Discovery** | "Was I right?!" | Prediction meets reality | Predict → commit → reveal → score | Scientific method |
| 5 | **Adventure** | "Look how far we went!" | Whole journey visible | Progress → choice → map | Narrative, temporal |
| 6 | **Nurture** | "I helped!" | Visible transformation | Need → solve → impact | Responsibility, empathy |

---

## Mystery

### `mystery_lens` — "I Spy meets 20 Questions in your own photo"

- **Category**: Cat 1 — Sustained Verbal Interaction (In-Device)
- **Child's role each round**: Deduces hidden details in their photo from AI's clues
- **What the AI does**: Secretly picks a DETAIL in the child's photo, gives clues one at a time
- **What the child does**: Observes photo closely and narrows down through deduction: "Is it the bow?" → "Warmer! It's softer than the bow..."
- **Game element**: Progressive clue revelation — can I spot it before the 3rd clue?
- **Magic moment**: Each "found it!" reveal
- **IB Key Concepts**: Form, Function
- **Lineage**: New
- **Example designs**: toy_robot_cat1_gold (Robot Inspector)

### `mystery_trail` — "Follow clue-riddles, discover the hidden pattern"

- **Category**: Cat 5 — Collection/Tracking Exploration (Out-of-Device)
- **Child's role each round**: Follows AI's riddle-clues to find and photograph items, then discovers the hidden connection
- **What the AI does**: Gives riddle-clues about things to find: "I'm rough, round, smaller than your hand..."
- **What the child does**: Searches, photographs guess; after 3-4 finds, AI reveals the HIDDEN CONNECTION: "Everything you found was shaped by water!"
- **Game element**: Riddle-driven search + pattern reveal at the end
- **Magic moment**: The pattern reveal — "WHOA, they're all connected!"
- **IB Key Concepts**: Form, Causation, Connection
- **Lineage**: New
- **Example designs**: butterfly_cat5_gold (The Butterfly World Detectives)

---

## Creation

### `inventor_workshop` — "What if we modified it?"

- **Category**: Cat 1 — Sustained Verbal Interaction (In-Device)
- **Child's role each round**: Imagines wild modifications to their photographed entity
- **What the AI does**: Asks "what if" questions: "What if your teddy had WHEELS?" Each round adds a wilder modification.
- **What the child does**: Invents and describes modifications; final round: AI describes "Super [Entity]" with ALL modifications combined
- **Game element**: Snowballing absurdity — each round adds to the creation
- **Magic moment**: The final "ta-da!" — all modifications combined into one glorious invention
- **IB Key Concepts**: Function, Change, Connection
- **Lineage**: New
- **Example designs**: rubber_duck_cat1_gold (Super Duck Workshop)

### `mix_lab` — "Collect ingredients, invent something new"

- **Category**: Cat 5 — Collection/Tracking Exploration (Out-of-Device)
- **Child's role each round**: Collects items, AI identifies a "superpower" per item, then child combines them into an invention
- **What the AI does**: Assigns a superpower per find (sticky, bouncy, smooth, shiny...) based on what child describes
- **What the child does**: Collects 3-4 items, then at synthesis: "Combine the bounciness of the ball with the stickiness of the pinecone — what would you invent?"
- **Game element**: Superpower discovery per find + creative combination
- **Magic moment**: The invention reveal — something that couldn't exist but SHOULD
- **IB Key Concepts**: Form, Function, Connection
- **Lineage**: New
- **Example designs**: rock_cat5_gold (Nature Inventor's Lab)

---

## Performance

### `voice_stage` — "Perform for your audience!"

- **Category**: Cat 1 — Sustained Verbal Interaction (In-Device)
- **Child's role each round**: Performs as the entity in escalating challenges with audience reactions
- **What the AI does**: Sets performance CHALLENGES and responds AS audience: "The judges almost fell off their chairs!"
- **What the child does**: Speaks, roars, sings, emotes in character; escalation with surprise twists: "Now do it WHISPERING!"
- **Game element**: Audience reaction mechanic — can I make the crowd react?
- **Magic moment**: Audience goes wild
- **IB Key Concepts**: Perspective, Form
- **Lineage**: Evolved from `voice_acting` — adds audience reaction mechanic, surprise twist challenges
- **Example designs**: lion_cat1_gold (The Lion's Big Show), crayons_cat1 (Color Feelings), raincoat_cat1 (Rainy Day Feelings), piano_cat1 (Secret Song Storyteller)

### `ensemble_show` — "Assemble your cast, put on a show"

- **Category**: Cat 5 — Collection/Tracking Exploration (Out-of-Device)
- **Child's role each round**: Collects items, gives each a sound/voice, then directs an ensemble performance
- **What the AI does**: Asks per find: "If this could make ONE sound, what would it be?" At synthesis, narrates a concert
- **What the child does**: Assigns sounds, then directs: items perform solo, then "All together now!"
- **Game element**: Cast assembly + ensemble performance
- **Magic moment**: "All together now!" — the full ensemble plays
- **IB Key Concepts**: Form, Connection, Perspective
- **Lineage**: New
- **Example designs**: bird_cat5_gold (The Nature Orchestra)

---

## Discovery

### `prediction_lab` — "Commit, reveal, score!"

- **Category**: Cat 1 — Sustained Verbal Interaction (In-Device)
- **Child's role each round**: Commits to predictions before dramatic reveals, with running score
- **What the AI does**: Describes scenario, child COMMITS to prediction BEFORE reveal; dramatic reveal + scoring: "*drumroll*... TEDDY WIGGLES HIS NOSE! Half point!"
- **What the child does**: Predicts outcomes; running score: "You're 2 for 3! Can you go perfect?"
- **Game element**: Commitment before reveal + scoring tally
- **Magic moment**: Each reveal — right or wrong, there's drama
- **IB Key Concepts**: Causation, Function
- **Lineage**: Evolved from `prediction_game` — adds commit-before-reveal, dramatic reveals, running score
- **Example designs**: goldfish_cat1_gold (Goldfish Scientist), eye_cat1 (The Secret Eye Detective)

### `field_experiment` — "Test a hypothesis outdoors"

- **Category**: Cat 5 — Collection/Tracking Exploration (Out-of-Device)
- **Child's role each round**: Predicts an answer, collects evidence, AI assesses each find from the photo and tallies results
- **What the AI does**: Proposes a visually-verifiable hypothesis: "Are most things at the playground made of metal or something else?" Child PREDICTS, then collects 4-5 items. After each photo, **AI identifies the relevant property from the image** and announces it — the child does NOT self-report.
- **What the child does**: Commits to a prediction before collecting; photographs items; reacts to AI's assessments. AI tallies: "Metal: 2, Not Metal: 3 — your hypothesis was SURPRISING!"
- **Game element**: Hypothesis → evidence collection → AI-assessed tally → real result
- **Magic moment**: The tally — real data, real result, genuine surprise
- **IB Key Concepts**: Form, Causation
- **Visual verification constraint**: Hypotheses MUST use properties the AI can reliably assess from a photo. **Allowed**: color, shape, material type (metal/wood/plastic), size (bigger/smaller than X), count, alive/not-alive, category membership. **Banned**: texture (rough/smooth), weight (heavy/light), temperature (warm/cold), sound, smell, flexibility. The AI is the property assessor — it announces what it sees in the photo, preserving the "Was I right?!" surprise.
- **Lineage**: Evolved from `comparison_chart` — adds pre-collection hypothesis, AI-as-assessor mechanic, data tallying
- **Example designs**: playground_cat5_gold (The Playground Material Detective)

---

## Adventure

### `time_traveler` — "Journey through time"

- **Category**: Cat 1 — Sustained Verbal Interaction (In-Device)
- **Child's role each round**: Takes entity through time periods with choice points that branch the journey
- **What the AI does**: Takes entity through TIME: "3 months ago, your banana was a tiny green flower..." Each round = different time jump
- **What the child does**: Imagines each era; choice points: "Banana arrives at the store — fruit bowl or smoothie machine?" → different paths; final: timeline assembled
- **Game element**: Time jumps + choice points that branch + timeline visualization
- **Magic moment**: Seeing the whole timeline assembled — "look how far we went!"
- **IB Key Concepts**: Change, Connection, Causation
- **Lineage**: Evolved from `storytelling_chain` — adds time-based progression, genuine choice points, timeline visualization
- **Example designs**: banana_cat1_gold (The Banana Time Machine)

### `quest_collector` — "Mission with a purpose"

- **Category**: Cat 5 — Collection/Tracking Exploration (Out-of-Device)
- **Child's role each round**: Collects items matching a quest criterion, harvests details for character naming, synthesizes into a quest story
- **What the AI does**: Gives QUEST with criterion: "Find 3 things that USED to be something else." Each find evaluated against criterion
- **What the child does**: Finds items, harvests details per find ("What does it remind you of?" → character name), then co-creates quest story with detail-driven character roles
- **Game element**: Quest criterion gives collection PURPOSE + detail-driven naming + narrative synthesis
- **Magic moment**: "Quest complete!" — mission accomplished, story told
- **IB Key Concepts**: Change, Form, Connection
- **Lineage**: Evolved from `naming_story` — adds quest criterion framing, mission progression tracking; preserves detail harvesting
- **Example designs**: dandelion_cat5_gold (Dandelion Quest), feather_cat5 (The Sky-Light Brigade), puddle_cat5 (The Puddle Portal), sandy_beach_cat5 (The Shore Detective Agency), autumn_leaf_cat5 (The Warm Color Treasure Hunt), pinecone_cat5 (The Spiral Code Breakers), crayons_cat5 (The Color Friends Adventure), double_rainbow_cat5 (The Rainbow Color Scout), raincoat_cat5 (The Rain Guard Patrol)

---

## Nurture

### `care_station` — "Help it get better"

- **Category**: Cat 1 — Sustained Verbal Interaction (In-Device)
- **Child's role each round**: Diagnoses needs and provides solutions, with visible transformation showing impact
- **What the AI does**: Presents escalating needs: "Your teddy is shivering!" Child proposes solutions; AI narrates VISIBLE TRANSFORMATION: "Teddy stops shivering... smiles... 'Warm!'"
- **What the child does**: Solves problems; escalation: physical → emotional → complex (scared AND cold AND lonely); relationship arc: by round 3, entity calls child by name
- **Game element**: Visible transformation + deepening relationship arc
- **Magic moment**: The transformation — you can SEE your help working
- **IB Key Concepts**: Responsibility, Function, Connection
- **Lineage**: Evolved from `helper_hotline` — adds visible transformation, relationship arc with deepening gratitude
- **Example designs**: teddy_bear_cat1_gold (Teddy's Care Station), firefighter_cat1 (Helper Hotline), toothbrush_holder_cat1 (The Bathroom Helper Game)

### `rescue_team` — "Find things that need help"

- **Category**: Cat 5 — Collection/Tracking Exploration (Out-of-Device)
- **Child's role each round**: Finds items with needs, proposes care for each, then synthesis: rescued items help EACH OTHER
- **What the AI does**: Identifies a "need" per find: "This leaf looks dry and curled — it needs water!" Child proposes care
- **What the child does**: Rescues 3-4 items; synthesis: "Your rescue team is complete! Now... how would the feather help the leaf?" — mutual aid
- **Game element**: Empathy-driven collection + mutual aid synthesis
- **Magic moment**: The rescued team helping EACH OTHER
- **IB Key Concepts**: Responsibility, Connection, Perspective
- **Lineage**: New
- **Example designs**: flower_cat5_gold (The Garden Rescue Squad)

---

## Style Lineage

| Old Style | → New Style | Pillar | What changed |
|-----------|------------|--------|-------------|
| `voice_acting` | `voice_stage` | Performance | Added audience reaction mechanic, surprise twist challenges |
| `storytelling_chain` | `time_traveler` | Adventure | Added time-based progression, genuine choice points, timeline visualization |
| `prediction_game` | `prediction_lab` | Discovery | Added commit-before-reveal, dramatic reveals, running score |
| `helper_hotline` | `care_station` | Nurture | Added visible transformation, relationship arc with deepening gratitude |
| `comparison_chart` | `field_experiment` | Discovery | Added pre-collection hypothesis, "was I right?" mechanic, data tallying |
| `naming_story` | `quest_collector` | Adventure | Added quest criterion framing, mission progression; preserved detail harvesting |
| — | `mystery_lens` | Mystery | Entirely new Cat1 style |
| — | `mystery_trail` | Mystery | Entirely new Cat5 style |
| — | `inventor_workshop` | Creation | Entirely new Cat1 style |
| — | `mix_lab` | Creation | Entirely new Cat5 style |
| — | `ensemble_show` | Performance | Entirely new Cat5 style |
| — | `rescue_team` | Nurture | Entirely new Cat5 style |

---

## Style Distribution

| Pillar | Style | Cat | Gold | Legacy | Designs (gold in **bold**) |
|--------|-------|-----|------|--------|---------------------------|
| Mystery | `mystery_lens` | 1 | 1 | 0 | **toy_robot** |
| Mystery | `mystery_trail` | 5 | 1 | 0 | **butterfly** |
| Creation | `inventor_workshop` | 1 | 1 | 0 | **rubber_duck** |
| Creation | `mix_lab` | 5 | 1 | 0 | **rock** |
| Performance | `voice_stage` | 1 | 1 | 3 | **lion**, crayons, raincoat, piano |
| Performance | `ensemble_show` | 5 | 1 | 0 | **bird** |
| Discovery | `prediction_lab` | 1 | 1 | 1 | **goldfish**, eye |
| Discovery | `field_experiment` | 5 | 1 | 4 | **playground**, city_library, sunflower, stop_sign, green_apple |
| Adventure | `time_traveler` | 1 | 1 | 0 | **banana** |
| Adventure | `quest_collector` | 5 | 1 | 8 | **dandelion**, feather, puddle, sandy_beach, autumn_leaf, pinecone, crayons, double_rainbow, raincoat |
| Nurture | `care_station` | 1 | 1 | 2 | **teddy_bear**, firefighter, toothbrush_holder |
| Nurture | `rescue_team` | 5 | 1 | 0 | **flower** |
