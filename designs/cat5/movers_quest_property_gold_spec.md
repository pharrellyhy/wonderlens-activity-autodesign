# Activity Design: Movers Quest + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Movers Quest

### A. Basic Info

- **Activity Name**: The Movers Quest
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Indoor/Outdoor)
- **Recommended Tier**: T1 (ages 4-6)
- **Core IB Key Concepts**: **Form** (What is it like?) & **Connection** (How is it connected to other things?)
- **Related Concepts (Discipline)**: Structure, Movement, Design, Similarity
- **ATL Skills Focus**: Research Skills (observation, collecting and recording data), Thinking Skills (creative thinking — interpreting and imagining), Communication Skills (expressing — narrative co-creation)
- **Experience Pillar**: Adventure
- **Game Style**: quest_collector
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity with visible movement capability
- **Trigger Scene**: Child photographs any object where AI detects a visible movement feature — wheels (toy car, bicycle, stroller), legs (toy animal, chair), wings (bird, butterfly, toy plane), or rollable shape (ball, cylinder, log)
- **Mapping Source**: property-bridge
- **IB Theme**: How the World Works
- **Template Parameters**: `{movement_type}` — detected movement feature (e.g., wheels, legs, wings, rollable shape). Example value used throughout: **wheels** (toy car trigger).

### A.5 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{movement_type}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_0.function.moves             # generic action-toy path
  - tier_0.function.flies             # wing-driven entities (butterfly, bird)
  - tier_0.appearance.wheels_or_feet  # e.g., toy_robot
  - tier_1.function.wing_flapping     # e.g., butterfly
```

### B. Activity Overview

- **① Brief Description**: After the child photographs any object, the AI notices a visible movement feature — for example, wheels on a toy car. The AI marvels at the movement capability and frames a quest: "Find 3 things that can MOVE!" The child becomes a Motion Scout on a movers quest. For each find, the AI evaluates it against the quest criterion ("Can it move?") by examining the photo for movement-enabling features (wheels, legs, wings, round/rollable shape), creating a pass/fail game moment, and then harvests a personal detail ("If this could move anywhere, where would it GO?") to generate a character name and destination. Once 3 quest items are collected, the child co-creates a road trip story featuring all the movers going on a journey together. Movement capability is visible from form: wheels are round, legs stick out, wings spread, balls are round and rollable. This template works for any entity with a visible movement feature.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "wheels," "legs," "wings," "roll," "slide," "swing," "spin." Learn that many different things can move, and that the shape of something often tells you HOW it moves — round things roll, flat things slide, things with wings fly.
  - **U (Understand)**: Understand that an object's **Form** — its shape and structure — determines how it can move (wheels roll, legs walk, wings fly, round things bounce). Understand that surprising **Connections** exist between very different things that share the same ability to move, even though they move in different ways.
  - **D (Do)**: Practice criterion-based observation — searching for items that match a specific quest goal (Research Skills — observation), invent character names and destinations driven by personal detail responses (Thinking Skills — creative thinking), and co-create a narrative where each character's journey role reflects the child's imagination (Communication Skills — expressing).

- **③ Design Highlight**: The quest criterion — "Find 3 things that can MOVE!" — transforms aimless collecting into a purposeful movement hunt. Each find gets evaluated against the criterion, creating a game-like moment: "A bicycle — it HAS wheels — it can ROLL! Quest item #2!" The criterion is visually verifiable: wheels, legs, wings, and rollable shapes are all clearly identifiable from photos. The detail harvesting asks "Where would it GO?" — giving each mover a destination personality for the road trip story. The combination of quest evaluation (game feel) + detail harvesting (creative ownership) + mission progression ("2 of 3 collected!") makes the child feel "Look at our amazing motion team!" Flexible evaluation allows partial credit — a tree cannot move, but its leaves can blow.

- **④ Typical Scenario**: Child photographs a toy car → AI notices wheels → "Your car can ZOOM — it has wheels!" → child becomes a Motion Scout → searches for things that can move → each find is evaluated for movement capability and given a character name + destination → at 3 of 3, "Quest complete!" triggers a co-created road trip story starring all the movers.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs any object with visible movement capability (e.g., a toy car with wheels) with no prior conversation.
>
> **AI says**: "*(breathless wonder)* Ohhh — look at your toy car! And WOW — look at those WHEELS! Round and smooth — if you push it, it will ZOOM across the floor! Your car can MOVE! I bet there are TONS of things around here that can move too. Have you ever noticed how many things have wheels or legs or wings?"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah! My bike has wheels too!" / "Birds have wings!" / "I can run!"
> 2. (Unexpected) "It's a race car!" / "It's red!" / "Vroom vroom!"
> 3. (No response) Looks at the toy car or the screen silently.
>
> **AI follow-up**:
> 1. "*(delighted)* Yes — bikes have wheels, birds have wings — moving things are EVERYWHERE! Your car zooms on its wheels. If it could drive ANYWHERE in the whole world, where would it go? To the beach? To a mountain? To the moon?"
> 2. "*(warmly agreeing)* VROOM VROOM is right! It IS a race car — and those wheels make it FAST! All that speed comes from those round wheels. If your race car could zoom anywhere in the world, where would it go?"
> 3. *(waits 2 seconds)* "*(soft, inviting)* See those round wheels? They are what make your car go ZOOM! If this car could drive anywhere — anywhere at ALL — where would it go? To a castle? To the jungle? To a pizza shop?"
>
> *(Child responds with a detail — e.g., "To the moon!")*
>
> **AI says**: "*(thrilled)* To the MOON — I love that! Let's name your car 'Moon Zoomer'! And guess what — Moon Zoomer has wheels, so it can MOVE. I wonder... what ELSE around here can move?"
>
> **Screen**: Close-up of the toy car photo with a gentle motion-blur effect around the wheels. Tiny animated speed lines trail behind the car. A small name tag reading the character name (e.g., "Moon Zoomer") appears below the photo with a tiny wheel icon. A motion-quest compass icon appears in the bottom corner showing "Quest: 0 of 3."

**Step 2: Mission Briefing — The Movers Quest**

> **AI says**: "*(adventurous, explorer tone)* You are now an official Motion Scout! And I have a quest for you! Your mission: find 3 things around here that can MOVE! Things with wheels, legs, wings — or anything that rolls, slides, or swings! For each one, you will tell me where it would go if it could move ANYWHERE, and we will give it a quest name. Then — all your movers go on a big ROAD TRIP together! Ready, Scout? Find something that can move!"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yes, let's go!" / "I see something!"
> 2. (Uncertain) "What counts as moving?" / "Where should I look?"
> 3. (No response) Glances around the room or yard.
>
> **AI follow-up**:
> 1. "*(cheering)* Quest is ON! Find something that has wheels, legs, wings, or looks like it could roll or swing — then snap a photo! Go, Scout!"
> 2. "*(encouraging)* Great question! If it has wheels, it can roll. If it has legs, it can walk. If it has wings, it can fly. Even a ball can roll because it is ROUND! Look for anything that looks like it could go somewhere — then snap a photo!"
> 3. *(waits 2 seconds)* "*(gently)* Here is a scout tip — look for round things that could roll, things with legs that could walk, or things with wheels. Even a door can swing! Try looking near your toys, or outside at bikes, strollers, or animals!"
>
> **Screen**: A quest-themed mission card appears: a badge outline labeled "Motion Scout" with a wheel-and-wing silhouette. Below it, 3 empty circle-shaped slots (to be filled as the child collects quest items). The trigger photo sits above the slots with its character name tag and a golden speed-line checkmark. A quest scroll unfurls with the text: "Quest: Find 3 things that can MOVE!" A motion compass in the corner shows "0 of 3 collected."

**Step 3: Multi-Round Exploration (3 rounds)**

> **Round 1 — First Quest Find:**
>
> *(Child photographs something — e.g., a bicycle leaning against a wall)*
>
> **AI says**: "*(excited)* Quest find incoming! Ooh — let me see... Can it MOVE?"
>
> *(Brief dramatic pause — 1 second)*
>
> **AI says**: "*(triumphant)* YES! Look at those big round wheels — TWO of them! If you pedal, this thing ZOOMS down the street! It CAN move! Quest item number one! Now, Scout — if this bicycle could ride anywhere in the whole world, where would it GO?"
>
> **Possible child responses**:
> 1. (Ideal) "To the park!" / "To the beach!" / "To school, really fast!"
> 2. (Unexpected) "A bike." / "I don't know." (minimal description)
> 3. (No response) Just looks at the screen.
>
> **AI follow-up**:
> 1. "*(thrilled)* To the beach — YES! I can picture it pedaling along the sand! Let's call this quest character... Beach Rider! Welcome to the motion team, Beach Rider! One of 3 collected — two more to go, Scout!"
> 2. "*(looking closely)* A bike — yes! And if it could ride far far away, where would it go? To a mountain? A castle? A candy shop?" *(waits for child's destination, then names accordingly — e.g., "A candy shop? Then it is Candy Cruiser!")*
> 3. *(waits 2 seconds)* "*(enthusiastic)* Those big wheels could go ANYWHERE! Where would this bike ride to? A jungle? A volcano? A rainbow? It reminds me of a speedy explorer!"
>
> **Screen**: The new photo slides into the first empty quest slot with a burst of golden speed-lines. A "Can it move? YES!" stamp appears briefly in green. A name tag appears under the photo with the character name and a tiny wheel icon. The motion compass updates to "1 of 3 collected" with a satisfying click animation. A dotted road-trip trail begins extending from the trigger slot toward the next empty slot.

> **Round 2 — Second Quest Find:**
>
> *(Child photographs something — e.g., a ball on the grass)*
>
> **AI says**: "*(detective voice)* Quest report number two! I see your photo... can THIS one move?"
>
> *(Brief dramatic pause — 1 second)*
>
> **AI says**: "*(amazed)* Oh YES — look how ROUND it is! No wheels, no legs, no wings — but it does not NEED them! It is a perfect sphere — it can roll and bounce and fly through the air! It CAN move! Quest item number two! If this ball could bounce anywhere, where would it GO, Scout?"
>
> **Possible child responses**:
> 1. (Ideal) "To a soccer game!" / "Over a rainbow!" / "Into outer space!"
> 2. (Stretch) "It's just a ball." / "I don't know where."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(impressed)* Over a rainbow — amazing! Bouncing up up up over a rainbow! Let's call this one... Rainbow Bouncer! Two of 3 collected — just ONE more mover to go, Scout!"
> 2. "*(warmly)* It IS a ball — and balls are amazing movers! If it could bounce really far, would it go to a playground? A stadium? The top of a mountain?" *(waits for child's answer, then names accordingly — e.g., "The top of a mountain? Then it is Mountain Bouncer!")*
> 3. *(waits 2 seconds)* "*(curious)* This ball can bounce SO high! Where would it bounce to? A trampoline park? The clouds? A birthday party? It reminds ME of a bouncy explorer!"
>
> **Screen**: Second slot fills in with a burst of golden speed-lines. "Can it move? YES!" stamp appears in green. Name tag appears with character name. Motion compass updates to "2 of 3 collected." The road-trip trail extends further. A gentle bouncing animation ripples across the screen.

> **Round 3 — Third Quest Find (with stuck branch and edge cases):**
>
> **STUCK BRANCH** *(if child has been searching for more than a minute without finding something)*:
>
> **AI says**: "*(helpful whisper)* Scout tip! Things that can move are everywhere! Look for anything with wheels — a stroller, a skateboard, a wagon. Look for things with legs — a toy animal, a chair (it has legs!). Or look for anything round that could roll — a bottle, a crayon, even an orange!"
>
> **Possible child responses**:
> 1. (Ideal) "I see one!" / Child spots something with wheels, legs, or a rollable shape.
> 2. (Stuck) "I still can't find anything." / "There's nothing here."
> 3. (No response) Child keeps wandering.
>
> **AI follow-up**:
> 1. "*(encouraging)* Great spotting! Snap a photo, Scout — let's see if it can move!"
> 2. "*(reassuring)* That's okay! Here is a secret — even a DOOR can move! It swings open and closed. And a drawer slides! Look for anything that can go back and forth, up and down, or round and round!"
> 3. *(waits 2 seconds)* "*(gentle prompt)* Let's slow down and look right around you. Do you see anything with wheels? Anything round? Even a rocking chair rocks — that is moving! What do you see?"
>
> **DOESN'T MATCH BRANCH** *(child photographs something that cannot move — e.g., a tree)*:
>
> *(Child photographs something — e.g., a tree)*
>
> **AI says**: "*(curious pause)* Hmm, let me check... Can a tree move?"
>
> *(Brief pause)*
>
> **AI says**: "*(playfully)* Wellll... a tree STAYS in one spot — its roots hold it down! It cannot walk or roll. BUT — wait! Look at those branches and leaves. When the wind blows, they SWAY and wave and dance! That is a kind of moving! Half credit — the tree SWAYS! What do you think, Scout — does swaying count?"
>
> **Possible child responses**:
> 1. (Ideal) "Oh, let me find something with wheels!" / "Yeah, leaves blow!"
> 2. (Insists) "Trees can move!" / "I want to keep it!"
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(encouraging)* Yes — something with wheels or legs! Go find one, Scout!"
> 2. "*(warmly, accepting)* You know what? The tree's branches DO move in the wind — that counts! If this tree could walk anywhere on its roots, where would it go? Let's give it a quest name!" *(accepts the find — the child's agency matters more than strict criterion enforcement)*
> 3. *(waits 2 seconds)* "*(gently)* The tree does sway! But for our movers quest, let's try to find something that can really GO somewhere — something with wheels, legs, or a round shape. Look nearby for a bike, a toy, or even a ball!"
>
> **NORMAL ROUND 3** *(child photographs something that can move — e.g., a toy airplane)*:
>
> **AI says**: "*(building suspense)* FINAL quest find! Can this one move...?"
>
> *(Dramatic pause — 1.5 seconds)*
>
> **AI says**: "*(bursting with excitement)* YES! Look at those WINGS — spread wide and ready to FLY! If you throw it, it soars through the air! It CAN move — it can FLY! QUEST ITEM NUMBER THREE! Scout — if this airplane could fly anywhere, where would it go?"
>
> **Possible child responses**:
> 1. (Ideal) "To a volcano!" / "To Grandma's house!" / "Around the whole world!"
> 2. (Unexpected) "An airplane." / "It's blue."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(amazed)* Around the whole WORLD — YES! Flying over oceans and mountains and jungles! Let's call it... World Flyer! Three of 3 collected — QUEST COMPLETE!"
> 2. "*(looking closely)* An airplane — yes! And it has those amazing wings. If it could fly really far, where would it go? Over the mountains? To a tropical island? Around the whole planet?" *(waits for child's answer, names accordingly — e.g., "A tropical island? Then it is Island Glider!")*
> 3. *(waits 2 seconds)* "*(enthusiastic)* Look at those wings — ready to FLY! Where would it go? Over the ocean? To a castle in the clouds? It reminds ME of an explorer plane!"
>
> **Screen**: Final slot fills in with a BIG burst of golden speed-lines and sparkles. "Can it move? YES!" stamp appears. Name tag appears with character name. Motion compass hits "3 of 3 collected" and EXPLODES with a starburst animation. A large "QUEST COMPLETE!" banner drops from the top with confetti and motion trails. All four photos (trigger + 3 finds) light up with golden borders and character names. A "Road Trip!" banner starts pulsing.

**Step 4: Synthesis — The Road Trip (Magic Moment)**

> **AI says**: "*(proud and thrilled)* QUEST COMPLETE, Motion Scout! Look at your motion team! Moon Zoomer the car, [Name 1] the [item], [Name 2] the [item], and [Name 3] the [item] — they can ALL move! Now here comes the best part. Ready... set... GO! They ALL start moving at the same time! Moon Zoomer zooms on its wheels, [Name 1] [moves in its way], [Name 2] [moves in its way], and [Name 3] [moves in its way]! They are ALL heading to... where? Where does the motion team go on their big road trip?"
>
> **Possible child responses**:
> 1. (Ideal) "To the beach!" / "To a race track!" / "To a giant playground!" / Child starts narrating.
> 2. (Uncertain) "I don't know." / "They just go."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(narrating with wonder)* VROOOOM! BOUNCE! WHOOOOSH! The motion team is OFF! Moon Zoomer zooms ahead on its wheels — 'Follow me, team!' Then [Name 1] the [item] [moves] right behind — 'I am coming!' [Name 2] the [item] [moves] alongside and says, 'Look how fast we are going!' And [Name 3] the [item] [moves] past everyone — 'I can see [child's destination] from here!' They ALL arrive at [child's destination] together — the greatest road trip EVER! What do they do when they get there?"
> 2. "*(playfully)* They go — YES! Moon Zoomer leads the way — VROOM! Then [Name 1] [moves] right behind! 'Wait for me!' calls [Name 2]. And [Name 3] says, 'Let's race!' Where do they all end up?"
> 3. *(waits 2 seconds)* "*(gently, storytelling voice)* I'll start! Ready, set, GO! Moon Zoomer rolls on its wheels — ZOOM! Then [Name 1] the [item] starts [moving]! And [Name 2] and [Name 3] join the road trip too! They are ALL moving together — look how far they are going! Where do they end up?"
>
> **Screen**: All 4 photos displayed in a road-trip layout — photos arranged along a winding road trail that curves across the screen. Character name tags below each. Animated motion effects match each character's movement type (wheels spin, ball bounces, wings flap). Speech bubbles appear near characters when mentioned. A golden road-trip trail connects all characters from start to destination. Background shifts from starting point to adventure destination. A "What a road trip!" banner glows softly.

**Step 5: Discovery Celebration**

> **AI says**: "*(amazed and warm)* Wow, Scout! Moon Zoomer, [Name 1], [Name 2], and [Name 3] — they are all SO different! A car, a [item], a [item], and a [item]. But they all had one thing in common — they could ALL move! A car rolls on wheels, a [item] [moves its way], and a [item] [moves its way]. Why do you think so many different things can move?"
>
> **Possible child responses**:
> 1. (Ideal) "Because they have wheels!" / "Because they are round!" / "Because they have legs!" / Any creative reasoning.
> 2. (Unexpected) "I don't know."
> 3. (No response)
>
> **AI follow-up**:
> 1. "*(delighted)* That is such a smart thought! You are right — the SHAPE of something tells you how it moves! Wheels are round so they roll. Wings are flat and wide so they catch the air. Legs push off the ground. The way something LOOKS tells you how it GOES!"
> 2. "*(warmly)* It IS amazing! Here is a clue — look at the shapes. Moon Zoomer has round wheels that roll. [Name 1] has [feature] that [moves]. They are all shaped FOR moving! The shape is the secret!"
> 3. *(waits 2 seconds)* "*(sharing a secret)* Here is the cool part — the SHAPE tells you everything! Round things roll. Flat wings catch the wind. Legs push off the ground. Every mover has a shape that helps it go!"
>
> **Screen**: All four characters displayed in a circular formation. Gentle animated motion-lines connect them, showing their shared movement ability. Small movement-fact callouts appear near each character (e.g., "wheels roll!" near the car, "round = bounce!" near the ball, "wings catch air!" near the airplane). The road-trip trail shows the full journey path in the background.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(warm celebration)* Congratulations, Motion Scout! You completed the Movers Quest! You discovered **Form** — you noticed that the SHAPE of things tells you how they move! Round wheels roll, spread wings fly, and round balls bounce! And you found an incredible **Connection** — Moon Zoomer, [Name 1], [Name 2], and [Name 3] are all completely different, but they can ALL move! Different shapes, same superpower — MOVEMENT! You earned your Motion Quest Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to find more movers, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child watches the motion animation quietly.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you are outside, keep your motion eyes ON — who KNOWS how many movers are hiding in plain sight! Bikes, scooters, bugs, birds — movers are EVERYWHERE! See you on the next quest, Scout!"
> 2. "*(warm)* Your badge is saved! And remember — every time you see something with wheels, legs, or wings, that is another mover! Bye for now, Scout!"
> 3. *(waits 2 seconds)* "*(soft)* Your Motion Quest Badge is ready to roll. Bye for now, Scout!"
>
> **Screen**: A golden "Motion Quest Badge" appears — circular, with a wheel-and-wing silhouette at the center and the 4 photos as small insets around the edges, each with its character name. The words **"Form"** and **"Connection"** float up artistically — "Form" styled with shape outlines (wheel, wing, ball) and "Connection" with motion-trail lines linking the letters. A motion compass icon nestles between the concept words. A soft chime plays. Tiny animated wheels, wings, and bouncing dots drift across the screen and settle.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Each photo processed independently. No OCR, face detection, IMU, or state-change comparison. Movement capability is assessed by AI examining the photo for visible features (wheels, legs, wings, round shape) — not by detecting actual motion. |
| 2 | Hook & Transition | PASS | Opens with breathless wonder about the movement feature ("Look at those WHEELS!") — emotional resonance, not knowledge testing. Quest grows naturally from noticing one thing can move to wondering what else can move. No "let's play a game" break. |
| 3 | Edge Case Coverage | PASS | All steps have 3 response branches. Step 3 includes a concrete stuck branch (look for wheels, legs, round things, doors, drawers), a "doesn't match criterion" branch (tree — validates swaying, offers redirect OR accepts if child insists with flexible "half credit" evaluation), and silence branches throughout. "Unexpected" branches always validate first. |
| 4 | IB Completeness | PASS | KUD fully defined with 7 vocabulary words, 2 conceptual understandings, 3 skills. Form + Connection named as Key Concepts. 4 Related Concepts listed. 3 ATL skills with sub-skills. Closing speech names concepts naturally as praise — "Form" references shapes enabling movement, "Connection" references shared movement ability across different objects. Concepts match what the child actually DID. |
| 5 | Tier Appropriateness | PASS | T1: sentences 5-8 words, quest structure with clear criterion, concrete vocabulary (wheels, legs, wings, roll, slide, swing, spin), open-ended detail questions ("Where would it GO?"), 3-item quest achievable for ages 4-6, "Can it move?" is concrete enough for T1 comprehension. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. Zero instances of "AI guides" or "AI encourages." Quest evaluation moments are specific and dramatic ("Look at those big round wheels — TWO of them!"). Detail-harvesting and naming examples are concrete. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: motion-blur effect + speed lines, quest mission card with slots + motion compass, "Can it move? YES!" stamps, speed-line animations, "QUEST COMPLETE!" banner with confetti, road-trip trail layout, badge with shape outlines and motion-trail letters. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — trigger is any entity with visible movement capability, not a specific entity. |
| 9 | Game Feel | PASS | Quest criterion creates genuine stakes per find with dramatic pause before verdict. "Doesn't match" branch (tree) shows real uncertainty with flexible "half credit" evaluation. Mission progression (0/3 to 3/3) creates momentum. "QUEST COMPLETE!" is clear climax. Road trip story is earned reward. High replayability — different environments yield different movers. |
| 10 | Pillar Fidelity | PASS | Adventure pillar: child feels "Look at our amazing motion team!" Quest criterion gives collection PURPOSE and DIRECTION. Mission progression tracking (0/3 to 1/3 to 2/3 to 3/3 to QUEST COMPLETE!) creates visible progress. Road trip story is the journey-map synthesis. The magic moment is "Quest complete!" + the road trip narrative. Could NOT be re-labeled as Discovery (no hypothesis/tally), Creation (no invention), Mystery (no hidden pattern), Performance (no audience), or Nurture (no rescue). This is clearly Adventure. |

**Overall**: ALL PASS — property-bridge quest_collector template triggered by visible movement capability (wheels, legs, wings, rollable shape). Flexible criterion evaluation allows partial credit for edge cases (tree sways, rock could be rolled).
