## Robot Inspector

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Robot Inspector |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Form, Function |
| Related Concepts | Structure, Discovery, Design, Observation |
| ATL Skills Focus | Thinking Skills (critical thinking, deduction), Research Skills (observation, information literacy), Communication Skills (expressing, listening) |
| Game Style | mystery_lens |

### A.5 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/daily_objects/action_toys.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_1.appearance.antenna
  - tier_1.appearance.eyes
  - tier_1.appearance.button
  - tier_1.appearance.joint
  - tier_1.appearance.wheels_or_feet
  - tier_1.function.signal_catching
  - tier_1.function.watching_with_eyes
  - tier_1.function.push_to_start
  - tier_1.function.joint_bending
  - tier_1.senses.click_sound
  - tier_1.structure.limbs
  - tier_2.appearance.light_up_features
  - tier_2.function.sensor_to_action_loop
```

### B. Activity Overview

**① Brief Description**

After the child photographs their toy robot, the AI marvels at all its cool parts — buttons, wheels, antenna, joints. The child becomes a "Chief Robot Inspector" who must figure out which secret part the AI is thinking of by listening to clues one at a time. Each round, the AI picks a different detail on the robot and gives progressive clues (shape, texture, function, then imaginative), and the child deduces which part it is. The fewer clues needed, the sharper the inspector!

**② Educational Purpose (KUD)**

- **K (Know):** Learn the names of robot parts — antenna, button, joint, wheel. Learn that each part has a different shape (round, pointy, flat, bumpy). Learn that each part has a job (antenna receives signals, wheels help move, buttons turn things on, joints help bend).
- **U (Understand):** Every part of a robot has a specific shape, feel, and look — that is Form (what things are like). Each part has a special job it does — that is Function (how things work).
- **D (Do):** Practice deductive reasoning by narrowing possibilities from clues. Practice careful observation of details in a photograph. Practice describing and discussing object features using specific words.

**③ Design Highlight**

The "Chief Robot Inspector" metaphor transforms casual toy observation into a detective-style deduction game. The AI secretly picks a detail on the child's own robot photo and feeds progressive clues — visual, tactile, functional, then imaginative — creating genuine suspense. The child scans their photo closely, eliminating possibilities with each clue, building toward the "I got it!" moment. Each round targets a different robot part, so the child learns that even a familiar toy is full of discoverable details.

**④ Typical Scenario**

Child photographs their toy robot on the playroom floor. AI notices all the cool parts — wheels, buttons, antenna, eyes. Child becomes a Chief Robot Inspector who deduces which hidden part the AI is thinking of by listening to clues.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (amazed, delighted gasp) "Whoa, look at this robot! It has SO many cool parts — I see wheels, buttons, a pointy antenna... it looks ready for a mission! If your robot could talk, what do you think it would say?"

**Child responses:**

1. (Ideal) "Hello!" / "Beep boop!" / "Let's go on an adventure!"
2. (Unexpected) "It has red eyes!" / "My robot is blue!" / "I got it for my birthday!"
3. (No response) Child looks at the screen silently.

**AI follow-up:**

1. (warm, impressed) "Beep boop — I love that! Your robot sounds so friendly. I bet you know ALL its parts really well. Want to play a detective game about them?"
2. (enthusiastic) "Ooh, tell me more! Your robot sounds really special. Look at all those parts it has — buttons, wheels, everything! I bet you know your robot better than anyone. Want to test those skills?"
3. (wait 2s) (soft, conspiratorial whisper) "Your robot has a LOT of secret parts. I bet there are some you never even noticed! Want to be a detective and find them with me?"

**Screen:** Toy robot photo centered with gentle glowing pulse animation. Tiny gear-shaped sparkles around edges. Soft mechanical whirring ambient animation.


#### Step 2: Rule Introduction + Demo

**AI says:** (playful, mystery-voice) "Okay, here is how it works! I am going to think of ONE secret part on your robot. I will give you clues, one at a time. You listen, look at your robot, and guess which part I am thinking of! Watch — I will show you. My secret part is... something on your robot that is round. Hmm, could be a lot of things! Next clue — it helps your robot move. Can you guess? The WHEELS! See how that works? Now let's play for REAL. Can you figure it out before my third clue? Ready, Inspector?"

**Child responses:**

1. (Ideal) "Ready!" / "Yeah!" / "I can do it!"
2. (Unexpected) "I knew it was the wheels!" / "My robot has big wheels!"
3. (No response) Child is quiet, processing the rules.

**AI follow-up:**

1. (excited countdown) "Alright, Chief Inspector — your first case starts NOW! Listen to my clue very carefully..."
2. (delighted, impressed) "You knew it! You are already thinking like an inspector! But the REAL cases are going to be trickier. Here comes number one..."
3. (wait 2s) (encouraging, gentle) "It is easy — I give clues, you guess! Any guess is a good guess. Here comes the first one... listen carefully!"

**Screen:** Robot photo on left. Magnifying glass icon with "ROBOT INSPECTOR" in bold playful letters on right. Quick demo animation: glowing question mark over robot, clue bubbles appear, wheels flash with "FOUND IT!" stamp. "Case 1" badge glows below.


#### Step 3: Multi-Round Interaction

**Round 1 — "The Secret Part: Antenna"** (simple, visual — build confidence)

**AI says:** (mysterious narrator) "Case number one! I am thinking of a part on your robot. Here is your first clue... it is thin and pointy — like a tiny stick poking up! Look at your robot. Can you guess what it is?"

**Child responses:**

1. (Ideal) "The antenna!" / "That pointy thing on top!" / "The stick on its head!"
2. (Unexpected) "The arm!" / "A leg!" / "I don't know!"
3. (No response) Child looks at the photo but says nothing.

**AI follow-up:**

1. (thrilled, celebratory) "You GOT it on the FIRST clue! The antenna — yes! That thin pointy part sticking up from its head. You know what it does? It helps the robot pick up signals — like a tiny ear listening to the sky! AMAZING inspector work!"
2. (warm, encouraging) "Ooh, good guess — but not quite! Here is clue number two — it sticks UP from the very top of the robot's head. Like a flag pole! Now look again... what is up there?" If child gets it: "YES! The antenna! Right on top — you found it!" If still stuck, clue 3: "It helps the robot hear signals from far away, like a tiny ear! It is... the ANTENNA!"
3. (wait 2s) (helpful whisper) "Look at the very TIP TOP of your robot. Something thin is sticking up... do you see it? What could it be?"

**Screen:** Robot photo with soft pulsing glow around top area. When revealed, antenna gets bright spotlight and sparkle burst. "CASE 1" stamp with star. First-clue solves get "FIRST CLUE SOLVE!" bonus banner.

**Round 2 — "The Secret Part: Button"** (introduces function and texture): AI gives two clues — "small and round" then "you can PUSH it with your finger." Child deduces it's a button. AI celebrates: "Buttons are like tiny commands — press one and the robot listens!" If child guesses wrong round thing (eyes, wheels), AI redirects: "you can push it IN, like pressing a doorbell."

**Round 3 — "The Secret Part: Joint"** (tricky — hidden/less obvious): AI whispers "this one is sneaky — it is hidden where two pieces CONNECT... it helps your robot BEND." Child finds the joint. AI celebrates: "Without joints, your robot would be stiff like a stick!" If child names a limb instead, AI guides: "look WHERE the arm bends — see that little spot where two parts connect?"

**Round 4 (if engaged) — "The Secret Part: Eyes"** (imaginative): AI says "my secret part looks like two little glowing moons on the front of the robot. They LOOK like they are watching everything!" Child spots the eyes. AI: "On a real robot, they might be lights or cameras, but they LOOK like eyes watching the world!"


#### Step 4: Celebration

**AI says:** (building excitement, dramatic pause) "Chief Inspector... you did it. You inspected the antenna — that thin, pointy signal-catcher! You found the button — the little round commander! You cracked the case of the sneaky joint — the hidden bendy connector! And you spotted the eyes — those two glowing moon-watchers! Every single part of your robot — SOLVED! (big celebration) You are officially the CHIEF ROBOT INSPECTOR!"

**Child responses:**

1. (Ideal) "Yay!" / "I did it!" / "I'm the inspector!"
2. (Unexpected) "Can we do more?" / "My robot is so cool!"
3. (No response) Child smiles or looks at the screen.

**AI follow-up:**

1. (beaming with pride) "The BEST Robot Inspector I have ever seen! Your robot is lucky to have someone who knows ALL its secrets."
2. (delighted) "You want MORE cases? That means you are a TRUE inspector — always looking for clues! We can inspect again another time. But first, let me tell you something amazing about what you just did..."
3. (wait 2s) (warm whisper) "You know what? I think your robot is impressed too. You found every single one of its secrets. That is incredible."

**Screen:** Golden "CHIEF ROBOT INSPECTOR" badge with toy robot photo as portrait inside. Small icons of each solved part orbit — antenna, button, joint, eyes — each with checkmark. Confetti in metallic silver and blue. Gear-shaped sparkles spin outward.


#### Step 5: Closing + IB Concepts

**AI says:** (warm, reflective pride) "You know what you did today? You looked really closely at every part of your robot — the thin antenna, the round button, the hidden joint, the glowing eyes. You noticed what each part LOOKS like. That is called Form — understanding the shape and look of things. And you figured out what each part DOES — the antenna catches signals, the button gives commands, the joint lets it bend, the eyes seem to watch. That is called Function — how each part works! You did not just play with your robot today. You INSPECTED it. Chief Robot Inspector — that is you!"

**Child responses:**

1. (Ideal) "Form!" / "Function!" / "I'm an inspector!"
2. (Unexpected) "Can I show my robot to you again?" / "I want to play more!"
3. (No response) Child listens or looks at the screen.

**AI follow-up:**

1. (celebrating) "That is right — Form and Function! You earned your badge, Chief Robot Inspector. Next time you look at ANY toy, I bet you will notice all its hidden parts!"
2. (warm, laughing) "Your robot would love that! You are the best inspector it has ever had. See you next time, Chief Robot Inspector!"
3. (wait 2s) (gentle closing) "Great job today, Inspector. Your robot has a really smart friend. See you next time!"

**Screen:** Inspector badge centered. "Form" with magnifying glass icon and "Function" with gear icon in bold metallic silver lettering. Toy robot photo glows softly behind. "The End" ribbon in robot-metallic style scrolls across bottom.
