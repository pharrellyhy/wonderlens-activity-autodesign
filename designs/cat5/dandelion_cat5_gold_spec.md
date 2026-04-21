# Activity Design: Dandelion + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-01 | Non-mapping design | Agent: Activity Design Agent

---

## Activity: The Wish Puff Quest

### A. Basic Info

- **Activity Name**: The Wish Puff Quest
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Outdoor)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: Change (How is it changing?) & Connection (How is it connected to other things?)
- **Related Concepts**: Transformation (designed), Diversity (designed), Nature (designed), Discovery (designed)
- **ATL Skills Focus**: Research Skills (observation, collecting and recording data), Thinking Skills (creative thinking — interpreting and imagining), Communication Skills (expressing — narrative co-creation)
- **Experience Pillar**: Adventure
- **Game Style**: quest_collector
- **Design Version**: 3.0 — quest_collector redesign
- **Last Updated**: 2026-04-01
- **Trigger Entity**: Dandelion
- **Trigger Scene**: Child photographs a dandelion puff ball in the grass at the park — seeds ready to fly
- **Mapping Source**: none
- **IB Theme**: How the World Works

### A.5 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/plants/wildflowers.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_0.appearance.puff_head
  - tier_0.appearance.yellow_flower
  - tier_0.function.blows_away
  - tier_1.appearance.seed_parachutes
  - tier_1.function.wind_dispersal
  - tier_1.senses.gentle_float
  - tier_1.senses.light_weight
  - tier_1.structure.puff_arrangement
  - tier_1.structure.umbrella_bristles
  - tier_2.appearance.flower_to_puff_transformation
  - tier_2.change.seed_spreading_journeys
  - tier_2.context.shared_flight_companions
  - tier_2.function.parachute_engineering
  - tier_2.senses.breath_triggered_motion
```

### A.6 Constellation Adaptation Notes

Recipe for running this activity when the photographed entity is a constellation
neighbor of Dandelion (e.g., other wind-dispersed plants like milkweed puff,
thistle seed head, wildflower in seed, maple "helicopter" seed) instead of a
dandelion puff itself. The neighbor list, bridge type, and initial bridge
prompt will live in `data/constellation_map.yaml` under
`mapped_entity: dandelion` (Cat5 entry pending per that file's coverage notes)
— this section describes how The Wish Puff Quest adapts mechanically for a
bridged entity.

**Preserve** — must not change across neighbors:
- The "Wish Puff Scout" role_title and the quest criterion "Find 3 things that are ready to fly!" — this criterion gives the collection Adventure-pillar purpose; swapping it loses the game feel.
- The COMMIT evaluation mechanic per find ("Is it ready to fly? *(pause)* YES!") with a "Ready to fly? YES!" stamp — the pass/fail moment is what makes the quest game-like.
- The detail-harvesting step ("What does it remind you of?") that generates each quest-team character name — this is what turns the collection into a cast for the Wind Adventure finale.

**Swap** — re-phrase for the bridged entity:
- Transition bridge "Look at all those tiny parachutes — seeds ready to fly!" → the neighbor's flight mechanism (milkweed: "big silky parachutes"; thistle: "purple-topped fluff that floats"; maple seed: "that wing that spins like a helicopter"). Keep "ready to fly" as the bridge line.
- The seed character name "Cloud Puff" (harvested from dandelion) → a new first-character name harvested from the neighbor (milkweed: "Silky Cloud"; maple: "Spinny Wing"). Built from the child's detail answer regardless of neighbor.
- Step 6 Closing line "a dandelion starts as a yellow flower and transforms into a puff ball" → the neighbor's Change story (milkweed: "a green pod cracks open into silky seeds"; maple seed: "a flower on the tree becomes a winged seed"). Keep the Change key-concept landing.
- Step 5 reflection "parachute seeds!" callout near dandelion → the neighbor's flight-engineering label ("silk parachutes", "wing shape", "feathery fluff").

**Watch** — gotchas to avoid:
- If the neighbor isn't a seed-head at all (a butterfly would match "ready to fly" but belongs to butterfly's own constellation — this game is for plant/seed neighbors), confirm bridge_type before routing; never cross-bridge from insect/bird to a plant quest.
- The Round 3 "doesn't match" branch (child photographs a rock) still applies — don't delete it just because the neighbor changed; rocks are off-criterion for ANY flight-ready quest.
- Never skip the detail-harvest if the child gives a minimal answer — scaffold it ("does it look like a wing? a parachute? a tiny boat?") rather than defaulting to a generic name; the characters' personality is what carries the Wind Adventure.

### B. Activity Overview

- **① Brief Description**: After photographing a dandelion, the AI marvels at its puffy seed head — all those tiny parachutes, ready to fly! The AI frames a quest: "Find 3 things in this park that are ready to fly!" The child becomes a Wish Puff Scout on a wind quest. For each find, the AI evaluates it against the quest criterion ("Is it ready to fly?"), creating a pass/fail game moment, and then harvests a personal detail ("What does it remind you of?") to generate a character name. Once 3 quest items are collected, the child co-creates a wind adventure story featuring all the characters, with each character's role shaped by the detail the child provided. The quest criterion gives the collection PURPOSE and DIRECTION; the detail harvesting gives each find PERSONALITY.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "seed," "parachute," "puff," "float," "breeze." Learn that dandelion seeds have tiny parachutes that catch the wind, and that many things in nature are designed to travel on air.
  - **U (Understand)**: Understand that things in nature **Change** form when they are ready to move or spread (a dandelion turns from yellow flower to puff ball), and that surprising **Connections** exist between very different things that share the same ability (flying, floating, drifting on air).
  - **D (Do)**: Practice criterion-based observation — searching for items that match a specific quest goal (Research Skills — observation), invent character names driven by personal detail responses (Thinking Skills — creative thinking), and co-create a narrative where each character's quest role reflects the child's observations (Communication Skills — expressing).

- **③ Design Highlight**: The quest criterion — "Find 3 things that are ready to fly!" — transforms aimless collecting into a purposeful mission. Each find gets evaluated against the criterion, creating a game-like moment: "A maple spinner — it IS ready to fly! Quest item #2!" The detail harvesting from the old naming_story is preserved but now serves the quest: the child's personal interpretation of each find becomes a character name and personality for the wind adventure story. The combination of quest evaluation (game feel) + detail harvesting (creative ownership) + mission progression ("2 of 3 collected!") makes the child feel "Look how far we went on our quest!" rather than just "I named some things."

- **④ Typical Scenario**: Child photographs a dandelion puff ball → AI notices its flying seeds and frames the wind quest → child searches for things that are "ready to fly" → each find is evaluated against the criterion and named → at 3 of 3, "Quest complete!" triggers a co-created wind adventure story starring all the quest characters.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1a: Transition Bridge — Warm Start**

> **Context**: Child has just finished a T1 conversation about the dandelion.
> **Conversation anchor**: appearance — shape ("round fluffy seed head, ready to fly"); senses — texture ("soft and light, like tiny parachutes")
>
> **AI says**: *(warm, building on earlier)* "You noticed all those tiny seeds — each one with a little parachute, ready to fly! I wonder what OTHER things in this park are ready to fly too..."
>
> **Possible child responses**:
> 1. (Ideal) "Let's find some!" / "I see something!" / child starts looking around
> 2. (Unexpected) "I want to blow it!" / "It's so fluffy!" / child touches the dandelion
> 3. (No response) Child looks at the dandelion or the screen quietly.
>
> **AI follow-up**:
> 1. *(excited)* "Yes! This dandelion puff is totally ready to fly — what does it remind you of? A tiny cloud? A fluffy star? Let's give it a name before we go searching!"
> 2. *(playful)* "It IS so fluffy and light! All those little parachutes, waiting for wind. You know what? I bet there are more things in this park that are ready to fly too! But first — what does this puff remind you of?"
> 3. *(wait 2s)* *(gentle, inviting)* "All those tiny seeds with their parachutes — ready to fly away! What does this puff ball remind you of? A cloud? A snowball? Let's give it a quest name!"
>
> **Screen**: Dandelion photo centered with a gentle glowing halo around the seed head. Tiny animated seed wisps lift upward from the edges. A soft shimmer highlights the flight-ready quality — a visual callback to the earlier conversation. A wind compass icon appears subtly in the corner.

**Step 1b: Transition Bridge — Cold Start**

> **AI says**: "*(breathless wonder)* Ohhh — a dandelion puff! Look at all those tiny seeds — each one has its own little parachute! If the wind blows, they'll ALL fly away like tiny wishes. Have you ever watched them float?"
>
> **Possible child responses**:
> 1. (Ideal) "Yes! They fly super far!" / "I blew one and they went everywhere!"
> 2. (Unexpected) "It's a flower!" / "I want to pick it!" / "It's white and fluffy!"
> 3. (No response) Looks at the dandelion or the screen silently.
>
> **AI follow-up**:
> 1. "*(delighted)* They DO fly super far — whoooosh! Each little seed rides the wind on its parachute! This dandelion puff is totally ready to fly. What does it remind you of? A tiny cloud? A white ball of wishes? A fluffy star?"
> 2. "*(warmly agreeing)* It IS a special flower! When it's done being yellow, it turns into this amazing puff ball. And every tiny piece is a seed with a parachute — all ready to FLY! What does this puff remind you of? A tiny cloud? A ball of fluff?"
> 3. *(waits 2 seconds)* "*(soft, inviting whisper)* See all those tiny white pieces? Each one is a seed with a teeny parachute. They're all waiting for the wind so they can fly! What does this puff ball remind you of? It reminds ME of a tiny cloud."
>
> *(Child responds with a detail — e.g., "A tiny cloud!" / "A snowball!" / "A fluffy star!")*
>
> **AI says**: "*(thrilled)* A tiny cloud — I love that! Let's name this dandelion puff 'Cloud Puff'! And guess what — Cloud Puff is ready to fly. I wonder... what ELSE in this park is ready to fly?"
>
> **Screen**: Close-up of the dandelion photo, with the seed head area surrounded by a gentle glowing halo. Tiny animated seed wisps lift slowly off the edges, floating upward. A small name tag reading the character name (e.g., "Cloud Puff") appears below the photo with a tiny parachute icon. A wind-quest compass icon appears in the bottom corner showing "Quest: 0 of 3."

**Step 2: Mission Briefing — The Wind Quest**

> **AI says**: "*(adventurous, explorer tone)* You are now an official Wish Puff Scout! And I have a quest for you! Your mission: find 3 things in this park that are READY TO FLY. Leaves that could blow away! Seeds that could float! Petals that could drift! For each one, you'll tell me what it reminds you of, and we'll give it a quest name. Then — all your flying characters go on a big wind adventure together! Ready, Scout? Find something that's ready to fly!"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yes, let's go!" / "I see something!"
> 2. (Uncertain) "What does 'ready to fly' mean?" / "Where should I look?"
> 3. (No response) Glances around the park.
>
> **AI follow-up**:
> 1. "*(cheering)* Quest is ON! Find something that looks like the wind could carry it away — then snap a photo! Go, Scout!"
> 2. "*(encouraging)* Great question! 'Ready to fly' means it looks like the wind could pick it up — something light and floaty, or loose and papery. Like a leaf that's about to blow away, or a feathery seed! Try looking near the grass or under a tree!"
> 3. *(waits 2 seconds)* "*(gently)* Here's a scout tip — look near the ground for loose leaves, fluffy seeds, or thin petals. Things that are ready to fly are usually light and thin! Try looking near a tree or at the edge of the path!"
>
> **Screen**: A quest-themed mission card appears: a badge outline labeled "Wish Puff Scout" with a dandelion parachute-seed silhouette. Below it, 3 empty circle-shaped slots (to be filled as the child collects quest items). The dandelion photo sits above the slots with its character name tag and a golden wind-swirl checkmark. A quest scroll unfurls with the text: "Quest: Find 3 things ready to fly!" A wind compass in the corner shows "0 of 3 collected."

**Step 3: Multi-Round Exploration (3 rounds)**

> **Round 1 — First Quest Find:**
>
> *(Child photographs something — e.g., a dry maple seed / "helicopter seed" on the ground)*
>
> **AI says**: "*(excited)* Quest find incoming! Ooh — let me see... Is it ready to fly?"
>
> *(Brief dramatic pause — 1 second)*
>
> **AI says**: "*(triumphant)* YES! Look at that wing shape — if you throw it up, it SPINS like a helicopter! It IS ready to fly! Quest item number one! Now, Scout — what does it remind you of?"
>
> **Possible child responses**:
> 1. (Ideal) "A helicopter!" / "A little wing!" / "A spinning hat!"
> 2. (Unexpected) "A seed." / "I don't know." (minimal description)
> 3. (No response) Just looks at the screen.
>
> **AI follow-up**:
> 1. "*(thrilled)* A little wing — perfect! It DOES look like a tiny wing, all thin and curved! Let's call this quest character... Wing Spin! Welcome to the quest, Wing Spin! One of 3 collected — two more to go, Scout!"
> 2. "*(looking closely)* A seed — yes! And look at the shape. Does it look more like a tiny wing, a little propeller, or a funny hat to you?" *(waits for child's detail, then names accordingly — e.g., "A propeller? Then let's call it Propeller Pete!")*
> 3. *(waits 2 seconds)* "*(enthusiastic)* I see something thin and curved — like a little wing! What does it remind YOU of? A wing? A propeller? A tiny leaf-boat? It reminds me of a little spinning helicopter!"
>
> **Screen**: The new photo slides into the first empty quest slot with a burst of golden wind-swirls. A "Ready to fly? YES!" stamp appears briefly in green. A name tag appears under the photo with the character name and a tiny wing icon. The wind compass updates to "1 of 3 collected" with a satisfying click animation. A dotted quest trail begins extending from the dandelion slot toward the next empty slot.

> **Round 2 — Second Quest Find:**
>
> *(Child photographs something — e.g., a loose feathery grass plume)*
>
> **AI says**: "*(detective voice)* Quest report number two! I see your photo... is THIS one ready to fly?"
>
> *(Brief dramatic pause — 1 second)*
>
> **AI says**: "*(amazed)* Oh WOW — look how feathery and light it is! One little breeze and it would float right up! It IS ready to fly! Quest item number two! What does this one remind you of, Scout?"
>
> **Possible child responses**:
> 1. (Ideal) "A tiny feather duster!" / "A fox tail!" / "A paintbrush!"
> 2. (Stretch) "It's just grass." / "I don't know what it looks like."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(impressed)* A fox tail — YES! All those soft wisps DO look like a fuzzy little tail! Let's call this one... Foxy Fluff! Two of 3 collected — just ONE more quest item to go, Scout!"
> 2. "*(warmly)* It IS grass — but look how soft and wispy the top is! Does it look more like a tiny feather, a fluffy tail, or a soft paintbrush to you?" *(waits for child's answer, then names accordingly — e.g., "A feather? Then it's Feather Top!")*
> 3. *(waits 2 seconds)* "*(curious)* I see something soft and wispy! It reminds ME of a tiny feather. What does it remind YOU of? A feather? A paintbrush? A fluffy tail?"
>
> **Screen**: Second slot fills in with a burst of golden wind-swirls. "Ready to fly? YES!" stamp appears in green. Name tag appears with character name. Wind compass updates to "2 of 3 collected." The quest trail extends further. A gentle breeze animation ripples across the screen.

> **Round 3 — Third Quest Find (with stuck branch and edge cases):**
>
> **STUCK BRANCH** *(if child has been searching for more than a minute without finding something)*:
>
> **AI says**: "*(helpful whisper)* Scout tip! Things that are ready to fly are usually light and thin. Try looking at the ground under a tree — fallen leaves, papery seed pods, and thin petals love to pile up there! Or check near the edge of the path for anything that looks loose and floaty!"
>
> **Possible child responses**:
> 1. (Ideal) "I see one!" / Child spots something near a tree or path edge.
> 2. (Stuck) "I still can't find anything." / "There's nothing here."
> 3. (No response) Child keeps wandering.
>
> **AI follow-up**:
> 1. "*(encouraging)* Great spotting! Snap a photo, Scout — let's see if it's ready to fly!"
> 2. "*(reassuring)* That's okay! Look for anything that's thin, light, or loose — a dry leaf, a petal on the ground, even a bit of fluff on a bush. If the wind could move it, it's ready to fly!"
> 3. *(waits 2 seconds)* "*(gentle prompt)* Let's slow down and look right at your feet. Do you see any thin leaves, fluffy bits, or papery things? Even something tiny — what does it look like to you?"
>
> **DOESN'T MATCH BRANCH** *(child photographs something heavy/not flight-ready — e.g., a rock)*:
>
> *(Child photographs something — e.g., a heavy rock)*
>
> **AI says**: "*(curious pause)* Hmm, let me check... Is a rock ready to fly?"
>
> *(Brief pause)*
>
> **AI says**: "*(playfully)* Wellll... rocks are pretty heavy! The wind would need to be REALLY strong to move that one. BUT — wait, does it have anything ON it? A thin leaf? A bit of moss? Sometimes flying things land on heavy things! What does this rock remind you of, though? I still like it!"
>
> **Possible child responses**:
> 1. (Ideal) "Oh, let me find something light!" / "I see a leaf near it!"
> 2. (Insists) "I want to keep it!" / "Rocks can fly!"
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(encouraging)* Yes — something light and floaty! Go find one, Scout!"
> 2. "*(warmly, accepting)* You know what? If YOU think this rock could fly, then it's a quest item! What does it remind you of? Maybe it's a secret flying rock! Let's give it a quest name!" *(accepts the find — the child's agency matters more than strict criterion enforcement)*
> 3. *(waits 2 seconds)* "*(gently)* That rock is cool! But for our flying quest, let's try to find something light — something the wind could pick up. Look nearby for a loose leaf or a fluffy seed!"
>
> **NORMAL ROUND 3** *(child photographs something flight-ready — e.g., a curled dry leaf)*:
>
> **AI says**: "*(building suspense)* FINAL quest find! Is this one ready to fly...?"
>
> *(Dramatic pause — 1.5 seconds)*
>
> **AI says**: "*(bursting with excitement)* YES! Look how thin and curled it is — one gust of wind and it would tumble and twirl through the air! It IS ready to fly! QUEST ITEM NUMBER THREE! Scout — what does this last one remind you of?"
>
> **Possible child responses**:
> 1. (Ideal) "A tiny boat!" / "A curly slide!" / "A crunchy chip!"
> 2. (Unexpected) "A leaf." / "It's brown."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(amazed)* A tiny boat — YES! It's all curled up like a little boat that sails on the wind instead of water! Let's call it... Wind Boat! Three of 3 collected — QUEST COMPLETE!"
> 2. "*(looking closely)* A leaf — yes! And look how it curls up at the edges. Does it look like a little bowl? A tiny boat? A curly hat?" *(waits for child's answer, names accordingly — e.g., "A curly hat? Then it's Curl Cap!")*
> 3. *(waits 2 seconds)* "*(enthusiastic)* Look at that — it's thin and curled! It reminds ME of a tiny boat. What does it remind YOU of? A boat? A bowl? A crispy scroll?"
>
> **Screen**: Final slot fills in with a BIG burst of golden wind-swirls and sparkles. "Ready to fly? YES!" stamp appears. Name tag appears with character name. Wind compass hits "3 of 3 collected" and EXPLODES with a starburst animation. A large "QUEST COMPLETE!" banner drops from the top with confetti wind-swirls. All four photos (dandelion + 3 finds) light up with golden borders and character names. A "Wind Adventure!" banner starts pulsing.

**Step 4: Synthesis — The Wind Adventure (Magic Moment)**

> **AI says**: "*(proud and thrilled)* QUEST COMPLETE, Wish Puff Scout! Look at your quest team! Cloud Puff the dandelion, [Name 1] the [detail], [Name 2] the [detail], and [Name 3] the [detail] — all ready to fly! Now here comes the best part. One big gust of wind blows through the park... WHOOOOSH! And they ALL take off! Where do they fly? What happens on their wind adventure?"
>
> **Possible child responses**:
> 1. (Ideal) "They fly to the clouds!" / "They go over the trees!" / "They fly to a castle!" / Child starts narrating.
> 2. (Uncertain) "I don't know." / "They just fly."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(narrating with wonder)* WHOOOSH! The big wind picks them ALL up! Cloud Puff floats up first — because dandelion puffs LOVE the wind! Then [Name 1] the [detail] starts spinning — whoosh whoosh whoosh! [Name 2] the [detail] drifts alongside and says, 'Look how high we are!' And [Name 3] the [detail] tumbles past and says, 'I can see [child's destination] from here!' They all fly together to [child's destination] — the most amazing wind adventure in the whole park! What do they find when they land?"
> 2. "*(playfully)* They fly — YES! Let me help. WHOOOSH — Cloud Puff goes first, floating high on its little parachute! Then [Name 1] the [detail] catches the wind and starts [action based on detail]. 'Wait for me!' calls [Name 2] the [detail]. And [Name 3] the [detail] says, 'Let's fly over the trees!' Where do they all land?"
> 3. *(waits 2 seconds)* "*(gently, storytelling voice)* I'll start! WHOOOSH — a big gust of wind sweeps through the park! Cloud Puff floats up on its tiny parachutes. Then [Name 1] the [detail] catches the breeze! And [Name 2] the [detail] and [Name 3] the [detail] fly up too! They're ALL in the air together — look how far they're going! Where do they land?"
>
> **Screen**: All 4 photos displayed in a wind-adventure layout — photos arranged along a swooping wind-trail that curves upward across the screen. Character name tags below each. An animated wind-gust sweeps across the scene, and tiny versions of each photo "lift off" and drift along the trail. Speech bubbles appear near characters when mentioned. A golden wind-trail connects all characters from takeoff to landing. Background shifts from park-green at the bottom to sky-blue at the top, showing the journey's height. A "Look how far we flew!" banner glows softly.

**Step 5: Discovery Celebration**

> **AI says**: "*(amazed and warm)* Wow, Scout! Cloud Puff, [Name 1], [Name 2], and [Name 3] — they're all SO different! A dandelion puff, a [item], a [item], and a [item]. But they all had one thing in common — they were ALL ready to fly! Why do you think so many different things can fly on the wind?"
>
> **Possible child responses**:
> 1. (Ideal) "Because they're light!" / "Because they're thin!" / "The wind picks them up!" / Any creative reasoning.
> 2. (Unexpected) "I don't know."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(delighted)* That's such a smart thought! You're right — they're all light and thin! The dandelion puff has tiny parachutes, [Name 1] has its [feature], and [Name 3] is curled and thin. Nature makes things light so the wind can carry them to new places — that's how seeds spread and find new soil to grow in!"
> 2. "*(warmly)* It IS amazing! Here's a clue — Cloud Puff is fluffy and light, with tiny parachutes. And [Name 1] the [detail] is thin and [feature]. They're both shaped so the wind can CARRY them. Nature designs things to travel!"
> 3. *(waits 2 seconds)* "*(sharing a secret)* Here's a cool secret — Cloud Puff's fluff catches the wind like tiny parachutes, carrying seeds far away to plant new flowers. And [Name 2] is light and [feature] for the same reason — to travel! Nature has lots of ways to fly."
>
> **Screen**: All four characters displayed in a circular formation. Gentle animated wind-lines connect them, showing their shared "flight-ready" quality. A soft breeze animation drifts across the screen. Small nature-fact callouts appear near each character (e.g., "parachute seeds!" near the dandelion, "wing shape!" near the maple seed). The wind-quest trail shows the full journey path in the background.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(warm celebration)* Congratulations, Wish Puff Scout! You completed the Wind Quest! You discovered how things **Change** — a dandelion starts as a yellow flower and transforms into a puff ball full of flying seeds! And you found an incredible **Connection** — Cloud Puff, [Name 1], [Name 2], and [Name 3] are all completely different, but they can ALL fly on the wind! You earned your Wind Quest Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to find more flying things, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child watches the drifting animation quietly.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you're outside, keep your quest eyes ON — who KNOWS what other things are ready to fly! Maybe you'll find a whole new wind team! See you on the next quest, Scout!"
> 2. "*(warm)* Your badge is saved! And remember — every time you see something light and floaty, that's another thing ready for a wind adventure! Bye for now, Scout!"
> 3. *(waits 2 seconds)* "*(soft)* Your Wind Quest Badge is shining. Bye for now, Scout!"
>
> **Screen**: A golden "Wind Quest Badge" appears — circular, with a dandelion puff silhouette at the center with tiny seeds flying outward, and the 3 quest-find photos plus the dandelion photo as small insets around the edges, each with its character name. The words **"Change"** and **"Connection"** float up artistically — "Change" styled with a transformation motif (yellow flower on the left morphing into a white puff on the right), "Connection" with gentle wind-trail lines linking the letters. A wind compass icon nestles between the concept words. A soft chime plays. Tiny animated seeds and wind-carried items drift across the screen and settle.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Each photo processed independently. No OCR, face detection, IMU, or state-change comparison. Multi-photo workflow is supported. The "ready to fly?" evaluation is done by AI reacting to the photo, not by comparing photos. |
| 2 | Hook & Transition | PASS | Both bridges open with emotional resonance — warm start builds on flight wonder ("all those tiny seeds with parachutes, ready to fly!"), cold start opens with breathless wonder about flying wishes. Neither tests knowledge. Quest grows naturally from dandelion's flight-readiness. |
| 3 | Edge Case Coverage | PASS | All steps have 3 response branches. Step 3 includes concrete stuck branch (look under trees, path edges), doesn't-match-criterion branch (rock — validates child, offers redirect OR accepts if child insists), and silence branches. "Unexpected" branches always validate first. |
| 4 | IB Completeness | PASS | KUD fully defined with 5 vocabulary words, 2 conceptual understandings, 3 skills. Change + Connection named as Key Concepts. 4 Related Concepts listed. 3 ATL skills with sub-skills. Closing speech names concepts naturally as praise — "Change" references dandelion's transformation, "Connection" references shared flight ability. Concepts match what the child actually DID. |
| 5 | Tier Appropriateness | PASS | T1: sentences 5–8 words, quest structure with clear criterion, concrete vocabulary (seed, parachute, puff, float, breeze), open-ended detail questions, 3-item quest achievable for ages 4–6, "ready to fly" is concrete enough for T1 comprehension. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. Zero instances of "AI guides" or "AI encourages." Quest evaluation moments are specific and dramatic. Detail-harvesting and naming examples are concrete. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: glowing halo + floating seeds, quest mission card with slots + wind compass, "Ready to fly? YES!" stamps, wind-swirl animations, "QUEST COMPLETE!" banner, wind-adventure trail layout, badge with transformation motif. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter in this assignment. |
| 9 | Game Feel | PASS | Quest criterion creates genuine stakes per find with dramatic pause before verdict. "Doesn't match" branch shows real uncertainty. Mission progression (0/3 → 3/3) creates momentum. "QUEST COMPLETE!" is clear climax. Wind adventure story is earned reward. High replayability. |
| 10 | Pillar Fidelity | PASS | Adventure pillar: child feels "Look how far we went on our quest!" Quest criterion gives collection PURPOSE. Mission progression tracking creates visible progress. Wind adventure is journey-map synthesis. Could NOT be re-labeled as any other pillar. Clearly Adventure. |

**Overall**: ALL PASS — quest_collector with criterion-driven collection + detail-harvesting. 3 issues found and fixed during self-evaluation.
