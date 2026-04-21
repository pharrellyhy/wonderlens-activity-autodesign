## Goldfish Guess-What Lab

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Goldfish Guess-What Lab |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Causation, Function |
| Related Concepts | Habitat, Adaptation, Discovery, Prediction |
| ATL Skills Focus | Thinking Skills (critical thinking, cause-and-effect), Communication Skills (expressing, listening), Research Skills (observation, data collection) |
| Experience Pillar | Discovery |
| Game Style | prediction_lab |

### A.5 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/animals/pet_fish.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_1.appearance.fin_shape
  - tier_1.appearance.tail_style
  - tier_1.function.movement_style
  - tier_1.function.breathing_method
  - tier_1.function.defense_hiding
  - tier_1.structure.gills
  - tier_1.structure.mouth_position
  - tier_2.function.fin_control_steering_braking
  - tier_2.context.light_day_night_routine
  - tier_2.senses.lateral_line_water_vibration_sense
```

### B. Activity Overview

**① Brief Description**: After the child photographs their goldfish, the AI marvels at its gliding, shimmery movement and invites the child to become a "Goldfish Scientist" who runs prediction experiments. In each round, the AI describes something about to happen near the goldfish — and the child must COMMIT to a specific prediction before the AI reveals the answer. Reveals are dramatic and scored: full points for correct predictions, half points for close guesses. A running tally creates genuine stakes: "You're 2 for 3 — can you go perfect?"

**② Educational Purpose (KUD)**:
- **K (Know)**: A goldfish has a fan-shaped tail that pushes it through water; fins on the sides help it steer and balance; gills let it breathe underwater; goldfish dart away quickly when startled; goldfish swim upward toward food on the surface.
- **U (Understand)**: When something happens near a goldfish, the fish reacts in a specific way — a cause creates an effect. That is Causation. Each body part has a specific job — tail pushes, fins steer, gills breathe, mouth eats. That is Function.
- **D (Do)**: Practice committing to a prediction before seeing the outcome. Practice describing animal behavior using specific vocabulary. Practice observing cause-and-effect patterns in a living creature.

**③ Design Highlight**: The "prediction lab" mechanic transforms fish-watching into a scientific experiment with real stakes. The child must COMMIT ("I think the goldfish will...") before the AI reveals the dramatic answer. A running score creates genuine tension. Half-points reward close guesses, ensuring no child feels they "lost." Each reveal is dramatized with suspense, making the moment of truth thrilling whether the child is right or wrong.

**④ Typical Scenario**: Child photographs their pet goldfish in a bowl at home. AI notices how it glides and shimmers. Child becomes a Goldfish Scientist who commits to predictions about the goldfish's reactions, then watches dramatic reveals with a running score.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (delighted gasp) "Ohhh WOW — a goldfish! Look at it gliding in there, so smooth and sparkly! It is like a tiny golden submarine. I wonder... does your goldfish have a name?"

**Child responses:**

1. (Ideal) "Goldie!" / "Bubbles!" / "Yes, it's [name]!"
2. (Unexpected) "It's swimming!" / "It's orange!" / "I fed it!"
3. (No response) Child watches the screen silently.

**AI follow-up:**

1. (warm, impressed) "[Name] — what a perfect name! [Name] looks like a real adventurer in there, zooming and gliding. I bet you know a LOT about how [name] moves. Hey... want to test how much you know? Like a scientist?"
2. (enthusiastic) "Yes! Look at it go — swimming and gliding! Those little fins are working SO hard. You really watch your fish closely. Hey... want to be a scientist and TEST what your goldfish does?"
3. (wait 2s) (soft, wondering) "This goldfish is so pretty — those floaty fins waving like tiny flags! I bet it has lots of secrets. Want to do science experiments with me to find out?"

**Screen:** Goldfish photo centered with gentle blue water-ripple animation, tiny bubble animations floating upward, and soft golden shimmer outlining the fish.

#### Step 2: Rule Introduction + Demo

**AI says:** (playful, scientist voice) "Okay, here is how our lab works! I will tell you something that is ABOUT to happen near the goldfish. But before I tell you what the goldfish does — YOU have to lock in your prediction! You say: 'I think the goldfish will...' and then we find out! You get a point if you are right, and HALF a point if you are close. Let me show you!"

(demo) "Ready? Something is about to happen: a shadow passes over the bowl. What will the goldfish do? I PREDICT... the goldfish will hide behind the little castle! Let me lock that in..."

(dramatic pause) "And the answer is... the goldfish darts to the bottom and stays very still! Ohhh — I said hide behind the castle, but it stayed still at the bottom. That is close! Half point for me! See how it works? Now YOUR turn, Scientist. Ready?"

**Child responses:**

1. (Ideal) "Ready!" / "Yeah!" / "Let's go!"
2. (Unexpected) "My fish does that!" / "What's a prediction?" / "I want a point!"
3. (No response) Child is quiet, possibly processing.

**AI follow-up:**

1. (excited countdown) "Okay, Scientist — Experiment Number One! Listen carefully..."
2. (delighted) "You already know what your fish does? Then you are going to be AMAZING at this! A prediction is just a guess you lock in BEFORE you find out. Here comes Experiment Number One!"
3. (wait 2s) (encouraging, gentle) "It is easy — I say what happens, you guess what the goldfish does. Any guess is great! Here comes the first one..."

**Screen:** Goldfish photo on left; on the right, a "Prediction Lab" clipboard icon with scoring circles and running score display reading "Score: 0". Demo animation shows shadow passing, goldfish darting, and "½" appearing with a sparkle. "Experiment 1" badge glows below.

#### Step 3: Multi-Round Interaction

**Round 1 — "The Food Drop" (Experiment 1):**

**AI says:** (mysterious narrator) "Experiment Number One! Imagine... it is feeding time. You sprinkle tiny food flakes on top of the water. They float down slowly. BEFORE I tell you — lock in your prediction! What does the goldfish do?"

**Child responses:**

1. (Ideal) "I think the goldfish will swim up!" / "It eats the food!" / "It goes to the top!"
2. (Unexpected) "It's happy!" / "Yummy!" / "Bubble bubble!"
3. (No response) Child is quiet or looking at the fish bowl.

**AI follow-up:**

1. (confirming lock-in) "Prediction locked: swim up to the top! Okay, here we go... *drumroll*... and the answer is... the goldfish ZOOMS right up to the surface — swish goes that fan-shaped tail, pushing it up like a paddle! YES! You got it! The food CAUSES the fish to swim up — tail swishing all the way! FULL POINT! Score: 1 out of 1!"
2. (warm, helping lock in) "Ooh happy — so you predict the fish gets excited and wiggles? Locked in! Here we go... *drumroll*... the goldfish ZOOMS to the surface, tail swishing! Getting excited — yes! But it also zooms UP. Half point — you got the feeling right! Score: half out of 1!"
3. (wait 2s) (helpful) "Here is a clue — the food is floating at the TOP of the water. Where would the goldfish swim? Up or down? Lock in your guess!"

**Screen:** Bowl scene with food flakes drifting down. "LOCKED IN" stamp on clipboard, drumroll animation, goldfish zooms upward with tail-swish motion lines. Score circle fills gold or half-gold. Running score updates.

**Round 2 — "The Big Tap" (Experiment 2):** Someone bumps the table — THUMP! Child locks in prediction about the goldfish's reaction. AI reveals it darts away fast, side fins spread wide for a quick turn. The bump CAUSED the fish to flee. Scored with full or half point based on prediction accuracy.

**Round 3 — "The New Shiny Pebble" (Experiment 3):** A shiny blue pebble drops into the bowl. Child predicts the goldfish's reaction. AI reveals it swims down slowly and nibbles to investigate — that is how goldfish check if something is food. Scored accordingly, running tally updated.

**Round 4 — "The Calm Dark Room" (Experiment 4):** Nighttime, lights go off, total quiet. Child predicts what the goldfish does in darkness and silence. AI reveals it slows way down, tail barely moving, floating gently near the bottom — nothing CAUSING it to react. Surprise round scored; final tally revealed.

#### Step 4: Celebration

**AI says:** (building suspense) "Okay, Scientist... the experiments are DONE. Time to count your score! You ran four experiments. You predicted what the goldfish would do when food drops... when the table bumps... when a pebble appears... and when the lights go out. And your final score is..."

(dramatic pause, drumroll)

"...[X] out of 4! [Score-specific reaction — perfect score gets 'FOUR OUT OF FOUR! PERFECT! You are a goldfish GENIUS!' / near-perfect gets 'AMAZING — almost every one right!' / any score gets warm celebration of what they learned]"

**Child responses:**

1. (Ideal) "Yay!" / "I got [X]!" / "I'm a scientist!"
2. (Unexpected) "Can we do more?" / "I want to try again!"
3. (No response) Child smiles or looks pleased.

**AI follow-up:**

1. (beaming) "The BEST Goldfish Scientist! Your goldfish is lucky to have someone who understands it so well."
2. (delighted) "You want MORE experiments? That is exactly what real scientists say! We can run more another day. But first — let me tell you something amazing about what you just did..."
3. (wait 2s) (warm whisper) "You know what? I think your goldfish can tell you have been paying attention. That is what great scientists do."

**Screen:** Giant score display "[X] / 4" in bold golden numbers. Mini-icons for each experiment (food flakes, tapping hand, blue pebble, moon) with score circles beside them. "GOLDFISH SCIENTIST" title banner above. Confetti explosion for perfect score; golden frame around goldfish photo for any score.

#### Step 5: Closing + IB Concepts

**AI says:** (warm, reflective) "You know what you did today? Every time I told you something was about to happen — food drops, a bump, a pebble, the lights — you PREDICTED what the goldfish would do before I even told you. You figured out that causes make effects! Food CAUSES the fish to swim up. A bump CAUSES the fish to dart away. A new thing CAUSES the fish to investigate. And quiet CAUSES the fish to rest. That is called Causation — when one thing CAUSES another thing to happen!"

"And you noticed something else — the tail PUSHES, the side fins STEER, the mouth NIBBLES, the gills BREATHE. Every part has its own job! That is called Function — how each part works! You are not just a scientist — you are a goldfish expert!"

**Child responses:**

1. (Ideal) "Causation!" / "I'm a scientist!" / "Function!"
2. (Unexpected) "Can I feed my fish now?" / "Bye goldfish!"
3. (No response) Child listens or looks at the screen.

**AI follow-up:**

1. (celebrating) "That is right — Causation and Function! You earned your badge, Goldfish Scientist. Go say hi to your fish — I bet it knows you understand it now!"
2. (warm, laughing) "Go ahead — your goldfish is so lucky to have such a smart scientist! See you next time, Goldfish Scientist!"
3. (wait 2s) (gentle closing) "Great job today, Scientist. Your goldfish has a really smart friend. See you next time!"

**Screen:** "GOLDFISH SCIENTIST" badge centered with goldfish photo portrait inside. "Causation" and "Function" in golden lettering with chain-link and gear icons. Four experiment icons as small trophies around the badge. Soft golden sparkle animations and a gentle "The End" ribbon.
