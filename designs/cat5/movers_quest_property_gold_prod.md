## Activity: The Movers Quest

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Movers Quest |
| Activity Category | 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Indoor/Outdoor) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | **Form** (What is it like?) & **Connection** (How is it connected to other things?) |
| Related Concepts (Discipline) | Structure, Movement, Design, Similarity |
| ATL Skills Focus | Research Skills (observation, collecting and recording data), Thinking Skills (creative thinking — interpreting and imagining), Communication Skills (expressing — narrative co-creation) |
| Experience Pillar | Adventure |
| Game Style | quest_collector |
| Trigger Entity | Any entity with visible movement capability |
| Trigger Scene | Child photographs any object where AI detects a visible movement feature — wheels (toy car, bicycle, stroller), legs (toy animal, chair), wings (bird, butterfly, toy plane), or rollable shape (ball, cylinder, log) |
| Mapping Source | property-bridge |
| IB Theme | How the World Works |
| Design Version | 1.0 |
| Last Updated | 2026-04-08 |
| Template Parameters | `{movement_type}` — detected movement feature (e.g., wheels, legs, wings, rollable shape). Example: **wheels** (toy car trigger) |

### B. Activity Overview

- **① Brief Description**: After the child photographs any object, the AI notices a visible movement feature — for example, wheels on a toy car. The AI marvels at the movement capability and frames a quest: "Find 3 things that can MOVE!" The child becomes a Motion Scout. For each find, the AI evaluates it against the quest criterion ("Can it move?") by examining the photo for movement-enabling features (wheels, legs, wings, round/rollable shape), creating a pass/fail game moment, and then harvests a personal detail ("If this could move anywhere, where would it GO?") to generate a character name and destination. Once 3 quest items are collected, the child co-creates a road trip story featuring all the movers going on a journey together. This template works for any entity with a visible movement feature.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "wheels," "legs," "wings," "roll," "slide," "swing," "spin." Learn that the shape of something often tells you how it moves — round things roll, flat things slide, things with wings fly.
  - **U (Understand)**: Understand that an object's **Form** — its shape and structure — determines how it can move (wheels roll, legs walk, wings fly). Understand that surprising **Connections** exist between very different things that share the ability to move.
  - **D (Do)**: Practice criterion-based observation (Research Skills — observation), invent character names and destinations from personal details (Thinking Skills — creative thinking), and co-create a narrative (Communication Skills — expressing).

- **③ Design Highlight**: The quest criterion — "Find 3 things that can MOVE!" — transforms aimless collecting into a purposeful movement hunt. Movement capability is visually verifiable: wheels, legs, wings, and rollable shapes are clearly identifiable from photos. The detail harvesting asks "Where would it GO?" — giving each mover a destination personality for the road trip story. Flexible evaluation allows partial credit for edge cases (tree sways, rock could be rolled).

- **④ Typical Scenario**: Child photographs a toy car --> AI notices wheels --> "Your car can ZOOM — it has wheels!" --> child becomes a Motion Scout --> searches for things that can move --> each find is evaluated and named --> at 3 of 3, "Quest complete!" triggers a co-created road trip story starring all the movers.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1b: Transition Bridge -- Cold Start

**Context**: Child photographs any object with visible movement capability (e.g., a toy car with wheels). AI detects movement feature (e.g., wheels).

**AI says**: *(breathless wonder)* "Ohhh — look at your toy car! And WOW — look at those WHEELS! Round and smooth — if you push it, it will ZOOM across the floor! Your car can MOVE! I bet there are TONS of things around here that can move too. Have you ever noticed how many things have wheels or legs or wings?"

**Possible child responses**:
1. (Ideal) "Yeah! My bike has wheels too!" / "Birds have wings!" / "I can run!"
2. (Unexpected) "It's a race car!" / "It's red!" / "Vroom vroom!"
3. (No response) Looks at the toy car or the screen silently.

**AI follow-up**:
1. *(delighted)* "Yes — bikes have wheels, birds have wings — moving things are EVERYWHERE! Your car zooms on its wheels. If it could drive ANYWHERE in the whole world, where would it go? To the beach? To a mountain? To the moon?"
2. *(warmly agreeing)* "VROOM VROOM is right! It IS a race car — and those wheels make it FAST! If your race car could zoom anywhere in the world, where would it go?"
3. *(waits 2s)* *(soft, inviting)* "See those round wheels? They make your car go ZOOM! If this car could drive anywhere, where would it go? To a castle? To the jungle? To a pizza shop?"

*(Child responds with a detail — e.g., "To the moon!")*

**AI says**: *(thrilled)* "To the MOON — I love that! Let's name your car 'Moon Zoomer'! And guess what — Moon Zoomer has wheels, so it can MOVE. I wonder... what ELSE around here can move?"

**Screen**: Close-up of photo with motion-blur effect around the movement feature. Speed-line animation. Name tag with character name and wheel icon. Motion-quest compass showing "Quest: 0 of 3."

#### Step 2: Mission Briefing -- The Movers Quest

**AI says**: *(adventurous, explorer tone)* "You are now an official Motion Scout! And I have a quest for you! Your mission: find 3 things around here that can MOVE! Things with wheels, legs, wings — or anything that rolls, slides, or swings! For each one, you will tell me where it would go if it could move ANYWHERE, and we will give it a quest name. Then — all your movers go on a big ROAD TRIP together! Ready, Scout? Find something that can move!"

**Possible child responses**:
1. (Ideal) "Ready!" / "Yes, let's go!" / "I see something!"
2. (Uncertain) "What counts as moving?" / "Where should I look?"
3. (No response) Glances around.

**AI follow-up**:
1. *(cheering)* "Quest is ON! Find something that has wheels, legs, wings, or looks like it could roll or swing — then snap a photo! Go, Scout!"
2. *(encouraging)* "If it has wheels, it can roll. If it has legs, it can walk. If it has wings, it can fly. Even a ball can roll because it is ROUND! Look for anything that could go somewhere!"
3. *(waits 2s)* *(gently)* "Look for round things that could roll, things with legs, or things with wheels. Even a door can swing! Try looking near toys, bikes, or animals!"

**Screen**: Quest mission card with "Motion Scout" badge and wheel-and-wing silhouette. 3 empty slots. Trigger photo above with name tag and golden speed-line checkmark. Quest scroll: "Quest: Find 3 things that can MOVE!" Motion compass: "0 of 3 collected."

#### Step 3: Multi-Round Exploration (3 rounds)

**Round 1 -- First Quest Find:**

*(Child photographs something — e.g., a bicycle)*

**AI says**: *(excited)* "Quest find incoming! Ooh — let me see... Can it MOVE?"

*(Brief dramatic pause — 1 second)*

**AI says**: *(triumphant)* "YES! Look at those big round wheels — TWO of them! If you pedal, this thing ZOOMS down the street! It CAN move! Quest item number one! Now, Scout — if this bicycle could ride anywhere in the whole world, where would it GO?"

**Possible child responses**:
1. (Ideal) "To the park!" / "To the beach!" / "To school, really fast!"
2. (Unexpected) "A bike." / "I don't know."
3. (No response)

**AI follow-up**:
1. *(thrilled)* "To the beach — YES! Let's call this quest character... Beach Rider! Welcome to the motion team! One of 3 collected — two more to go, Scout!"
2. *(looking closely)* "A bike — yes! If it could ride far away, where would it go? A mountain? A castle? A candy shop?" *(names accordingly)*
3. *(waits 2s)* "Those big wheels could go ANYWHERE! Where would this bike ride to? A jungle? A volcano? A rainbow?"

**Screen**: Photo slides into first slot with golden speed-lines. "Can it move? YES!" stamp in green. Name tag with character name. Motion compass: "1 of 3 collected."

**Rounds 2-3**: Same structure. Round 2 uses detective voice ("Quest report number two!"). Round 3 builds to climax ("FINAL quest find!").

**Round 3 edge cases**:

- **STUCK BRANCH**: "Scout tip! Things that move are everywhere! Look for anything with wheels — a stroller, a skateboard. Things with legs — a toy animal, a chair! Or round things that roll — a bottle, a crayon, even an orange!"
- **DOESN'T MATCH BRANCH** (e.g., a tree): "Wellll... a tree stays in one spot — its roots hold it down! BUT — the branches and leaves SWAY in the wind! Half credit — the tree SWAYS! Does swaying count?" *(validates child, offers redirect or accepts if child insists)*

**Screen at quest complete**: All slots filled. "QUEST COMPLETE!" banner with confetti and motion trails. All 4 photos with golden borders and character names. "Road Trip!" banner pulsing.

#### Step 4: Synthesis -- The Road Trip (Magic Moment)

**AI says**: *(proud and thrilled)* "QUEST COMPLETE, Motion Scout! Look at your motion team! Moon Zoomer the car, [Name 1] the [item], [Name 2] the [item], and [Name 3] the [item] — they can ALL move! Now here comes the best part. Ready... set... GO! They ALL start moving at the same time! Where does the motion team go on their big road trip?"

**Possible child responses**:
1. (Ideal) "To the beach!" / "To a race track!" / "To a giant playground!" / Child narrates.
2. (Uncertain) "I don't know." / "They just go."
3. (No response)

**AI follow-up**:
1. *(narrating with wonder)* "VROOOOM! BOUNCE! WHOOOOSH! The motion team is OFF! Moon Zoomer zooms ahead — 'Follow me, team!' Then [Name 1] [moves] right behind! [Name 2] calls out, 'Look how fast we are going!' And [Name 3] [moves] past everyone — 'I can see [destination] from here!' They ALL arrive together — the greatest road trip EVER! What do they do when they get there?"
2. *(playfully)* "They go — YES! Moon Zoomer leads the way — VROOM! Then [Name 1] catches up! 'Wait for me!' calls [Name 2]. And [Name 3] says, 'Let's race!' Where do they all end up?"
3. *(waits 2s)* *(storytelling voice)* "Ready, set, GO! Moon Zoomer rolls — ZOOM! Then [Name 1] starts [moving]! And [Name 2] and [Name 3] join in! They are ALL moving together — where do they end up?"

**Screen**: Team road-trip layout with photos along a winding road trail. Animated motion effects per character (wheels spin, ball bounces, wings flap). Speech bubbles near characters. Golden road-trip trail. "What a road trip!" banner.

#### Step 5: Discovery Celebration

**AI says**: *(amazed and warm)* "Wow, Scout! Moon Zoomer, [Name 1], [Name 2], and [Name 3] — they are all SO different! But they all had one thing in common — they could ALL move! Why do you think so many different things can move?"

**AI follow-up**:
1. *(delighted)* "The SHAPE tells you everything! Wheels are round so they roll. Wings are flat and wide so they catch the air. Legs push off the ground. The way something LOOKS tells you how it GOES!"
2. *(warmly)* "Round wheels roll. Flat wings catch wind. Legs push off the ground. They are all shaped FOR moving — the shape is the secret!"
3. *(waits 2s)* "The SHAPE is the secret! Round things roll, wings catch air, legs push the ground. Every mover has a shape that helps it go!"

**Screen**: Four characters in circular formation with motion-lines connecting them. Movement-fact callouts near each character. Road-trip trail in background.

#### Step 6: Closing + IB Concepts

**AI says**: *(warm celebration)* "Congratulations, Motion Scout! You completed the Movers Quest! You discovered **Form** — you noticed that the SHAPE of things tells you how they move! Round wheels roll, spread wings fly, and round balls bounce! And you found an incredible **Connection** — Moon Zoomer, [Name 1], [Name 2], and [Name 3] are all completely different, but they can ALL move! Different shapes, same superpower — MOVEMENT! You earned your Motion Quest Badge!"

**AI follow-up**:
1. *(encouraging)* "Next time you are outside, keep your motion eyes ON — who KNOWS how many movers are hiding in plain sight! See you on the next quest, Scout!"
2. *(warm)* "Your badge is saved! Every time you see something with wheels, legs, or wings, that is another mover! Bye for now, Scout!"
3. *(waits 2s)* *(soft)* "Your Motion Quest Badge is ready to roll. Bye for now, Scout!"

**Screen**: Golden "Motion Quest Badge" — circular, with wheel-and-wing silhouette at center and 4 photos as insets with character names. **"Form"** and **"Connection"** float up artistically. Motion compass between concept words. Soft chime. Animated wheels, wings, and bouncing dots settle.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Each photo processed independently. No OCR, face detection, IMU, or state-change comparison. |
| 2 | Hook & Transition | PASS | Opens with emotional wonder about movement feature, not knowledge testing. Quest grows naturally from detected attribute. |
| 3 | Edge Case Coverage | PASS | All steps have 3 response branches. Stuck branch, doesn't-match branch (tree — flexible half credit), and silence branches included. |
| 4 | IB Completeness | PASS | KUD defined. Form + Connection as Key Concepts. Closing names concepts as earned praise. |
| 5 | Tier Appropriateness | PASS | T1: short sentences, concrete vocabulary, achievable 3-item quest for ages 4-6. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. Zero "AI guides" placeholders. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with animations and visual elements. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — trigger is any entity with visible movement capability, not a specific entity. |
| 9 | Game Feel | PASS | Quest criterion creates stakes. Flexible evaluation with half credit adds nuance. Mission progression creates momentum. Road trip story is earned reward. |
| 10 | Pillar Fidelity | PASS | Adventure pillar: quest criterion gives collection PURPOSE, mission progression creates visible progress. Road trip is journey-map synthesis. |

**Overall**: ALL PASS — property-bridge quest_collector template parameterized by visible movement capability.
