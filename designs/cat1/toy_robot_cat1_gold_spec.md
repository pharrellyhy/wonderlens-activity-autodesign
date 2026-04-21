# Activity Design: Toy Robot + Category 1 (Sustained Verbal Interaction)

> Generated: 2026-04-01 | Non-mapping design | Agent: Activity Design Agent

---

## Activity: Robot Inspector (机器人大侦探)

### A. Basic Info

- **Activity Name**: Robot Inspector (机器人大侦探)
- **Activity Category**: 1 — Sustained Verbal Interaction (In-Device)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: **Form** (What is it like?) & **Function** (How does it work?)
- **Related Concepts (Discipline)**: Structure, Discovery, Design, Observation
- **ATL Skills Focus**: Thinking Skills (critical thinking, deduction), Research Skills (observation, information literacy), Communication Skills (expressing ideas, listening)
- **Experience Pillar**: Mystery
- **Game Style**: mystery_lens
- **Design Version**: 1.0
- **Last Updated**: 2026-04-01
- **Trigger Entity**: Toy robot (a child's toy robot with buttons, joints, eyes, wheels, antenna, etc.)
- **Trigger Scene**: Child photographs their toy robot on the playroom floor
- **Mapping Source**: none

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

### A.6 Constellation Adaptation Notes

Recipe for running this activity when the photographed entity is a constellation
neighbor of Toy Robot (e.g., action figure, toy dinosaur, lego figure) instead
of a toy robot itself. The neighbor list, bridge type, and initial bridge
prompt live in `data/constellation_map.yaml` under `mapped_entity: toy_robot`
— this section describes how Robot Inspector adapts mechanically for a
bridged entity.

**Preserve** — must not change across neighbors:
- The "Chief Inspector" role_title and the progressive-clue deduction mechanic (shape → function → imaginative) — this clue-laddering is the Mystery pillar's engine.
- The 3–4 case structure where each round targets a DIFFERENT part, building the "my toy is full of discoverable details" reveal.
- The "first-clue solve" bonus framing — rewards careful looking and gives the game replay-value.

**Swap** — re-phrase for the bridged entity:
- Case 1 target "antenna (thin and pointy, catches signals)" → neighbor's signature protrusion (action figure: "weapon or accessory"; toy dinosaur: "spike or horn on the back"; lego figure: "hat or hair piece") with clue 1 re-written for that shape.
- Case 2 target "button (small, round, pushed with a finger)" → neighbor's equivalent small interactive feature (action figure: "a latch that clicks"; dinosaur: "a roar button or squeeze spot"; lego figure: "the stud on top of the head that connects to other bricks").
- Case 3 target "joint (hidden where two pieces connect, helps bend)" → neighbor's actual articulation points (action figure: "shoulder and knee joints that pose"; dinosaur: "jaw hinge"; lego figure: "the torso-twist between hips and chest").
- Case 4 target "eyes (two little glowing moons)" → neighbor's face feature (dinosaur: "tiny painted eyes plus nostrils"; lego figure: "printed stud-face"; action figure: "sculpted eyes and visor").

**Watch** — gotchas to avoid:
- If the neighbor has fewer distinct parts (a minimalist lego figure may have only head, body, legs), drop Round 4 rather than inventing parts that aren't there — Mystery dies when clues don't point at anything real.
- Don't keep "signal-catcher," "sensor-to-action loop," or other robot-specific Function language — re-derive each part's job from the neighbor's actual role (a dinosaur horn defends; a figure's weapon battles).
- Never give clues that require the child to touch the toy physically if the photographed subject is a tiny lego figure — "feel the bumpy joint" works for large robots but not for 4cm plastic minifigures; pivot to visual-only clues.

### B. Activity Overview

- **① Brief Description**: After the child photographs their toy robot, the AI marvels at all its cool parts — buttons, wheels, antenna, joints. The child becomes a "Chief Robot Inspector" who must figure out which secret part the AI is thinking of by listening to clues one at a time. Each round, the AI picks a different detail on the robot and gives progressive clues (shape, texture, function, then imaginative), and the child deduces which part it is. The fewer clues needed, the sharper the inspector!

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the names of robot parts — antenna, button, joint, wheel; learn that each part has a different shape (round, pointy, flat, bumpy); learn that each part has a job (antenna receives signals, wheels help move, buttons turn things on, joints help bend)
  - **U (Understand)**: Understand that every part of a robot has a specific shape, feel, and look — that is **Form** (what things are like). Understand that each part has a special job it does — that is **Function** (how things work).
  - **D (Do)**: Practice deductive reasoning by narrowing possibilities from clues (Thinking Skills — critical thinking, deduction). Practice careful observation of details in a photograph (Research Skills — observation). Practice describing and discussing object features using specific words (Communication Skills — expressing ideas).

- **③ Design Highlight**: The "Chief Robot Inspector" metaphor transforms casual toy observation into a detective-style deduction game. The AI secretly picks a detail on the child's own robot photo and feeds progressive clues — visual, tactile, functional, then imaginative — creating genuine suspense. The child scans their photo closely, eliminating possibilities with each clue, building toward the "I got it!" moment. Each round targets a different robot part, so the child learns that even a familiar toy is full of discoverable details.

- **④ Typical Scenario**: Child photographs their toy robot on the playroom floor. AI notices all the cool parts — wheels, buttons, antenna, eyes. Child becomes a Chief Robot Inspector who deduces which hidden part the AI is thinking of by listening to clues.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs their toy robot with no prior conversation.
>
> **AI says**: "*(amazed, delighted gasp)* Whoa, look at this robot! It has SO many cool parts — I see wheels, buttons, a pointy antenna... it looks ready for a mission! If your robot could talk, what do you think it would say?"
>
> **Possible child responses**:
> 1. (Ideal) "Hello!" / "Beep boop!" / "Let's go on an adventure!" / Child imagines robot speech.
> 2. (Unexpected) "It has red eyes!" / "My robot is blue!" / "I got it for my birthday!" / Child describes the robot or shares a memory.
> 3. (No response) Child looks at the screen silently.
>
> **AI follow-up**:
> 1. "*(warm, impressed)* Beep boop — I love that! Your robot sounds so friendly. I bet you know ALL its parts really well. Want to play a detective game about them?"
> 2. "*(enthusiastic)* Ooh, tell me more! Your robot sounds really special. Look at all those parts it has — buttons, wheels, everything! I bet you know your robot better than anyone. Want to test those skills?"
> 3. *(waits 2 seconds)* "*(soft, conspiratorial whisper)* Your robot has a LOT of secret parts. I bet there are some you never even noticed! Want to be a detective and find them with me?"
>
> **Screen**: Toy robot photo centered on screen. Gentle glowing pulse animation radiates outward from the robot. Tiny gear-shaped sparkles float around the edges of the photo. Soft mechanical whirring ambient animation in the background.

**Step 2: Game Setup + Demo — "The Robot Inspector Academy"**

> **AI says**: "*(playful, mystery-voice)* Okay, here is how it works! I am going to think of ONE secret part on your robot. I will give you clues, one at a time. You listen, look at your robot, and guess which part I am thinking of! Watch — I will show you. My secret part is... something on your robot that is round. Hmm, could be a lot of things! Next clue — it helps your robot move. Can you guess? The WHEELS! See how that works? Now let's play for REAL. Can you figure it out before my third clue? Ready, Inspector?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yeah!" / "I can do it!" / "Let's play!"
> 2. (Unexpected) "I knew it was the wheels!" / "My robot has big wheels!" / Repeats "wheels!"
> 3. (No response) Child is quiet, possibly processing the rules.
>
> **AI follow-up**:
> 1. "*(excited countdown)* Alright, Chief Inspector — your first case starts NOW! Listen to my clue very carefully..."
> 2. "*(delighted, impressed)* You knew it! You are already thinking like an inspector! But the REAL cases are going to be trickier. Here comes number one..."
> 3. *(waits 2 seconds)* "*(encouraging, gentle)* It is easy — I give clues, you guess! Any guess is a good guess. Here comes the first one... listen carefully!"
>
> **Screen**: Robot photo slides to the left side. On the right, a magnifying glass icon appears with "ROBOT INSPECTOR" in bold playful letters. A quick demo animation plays: a glowing question mark hovers over the robot, then a clue bubble appears ("Something round..."), then another ("Helps it move..."), then the wheels flash and sparkle with a "FOUND IT!" stamp. Below, a "Case 1" badge glows, ready.

**Step 3: Multi-Round Interaction (3–4 rounds)**

**Round 1 — "The Secret Part: Antenna"** *(Simple, visual clue — build confidence)*

> **AI says**: "*(mysterious narrator voice)* Case number one! I am thinking of a part on your robot. Here is your first clue... it is thin and pointy — like a tiny stick poking up! Look at your robot. Can you guess what it is?"
>
> **Possible child responses**:
> 1. (Ideal) "The antenna!" / "That pointy thing on top!" / "The stick on its head!"
> 2. (Unexpected) "The arm!" / "A leg!" / "I don't know!" / Child guesses wrong.
> 3. (No response) Child looks at the photo but says nothing.
>
> **AI follow-up**:
> 1. "*(thrilled, celebratory)* You GOT it on the FIRST clue! The antenna — yes! That thin pointy part sticking up from its head. You know what it does? It helps the robot pick up signals — like a tiny ear listening to the sky! AMAZING inspector work!"
> 2. "*(warm, encouraging)* Ooh, good guess — but not quite! Here is clue number two — it sticks UP from the very top of the robot's head. Like a flag pole! Now look again... what is up there?"
>    - *(If child guesses correctly after clue 2)*: "*(excited)* YES! The antenna! Right on top — you found it! It picks up signals from far away. Two clues — that is great detective work!"
>    - *(If child still guesses wrong or is silent)*: "*(playful reveal)* Okay, here is my last clue — it helps the robot hear signals from far away, like a tiny ear! It is... the ANTENNA! See it up there? Thin, pointy, right on top! Now you will spot it forever. Next case!"
> 3. *(waits 2 seconds)* "*(helpful whisper)* Look at the very TIP TOP of your robot. Something thin is sticking up... do you see it? What could it be?"
>
> **Screen**: Robot photo with a soft pulsing glow around the top area (not directly highlighting the antenna — preserving the mystery). When revealed, the antenna area gets a bright spotlight circle and sparkle burst animation. A "CASE 1" stamp appears with a star. If solved on clue 1, a "FIRST CLUE SOLVE!" bonus banner flashes.

**Round 2 — "The Secret Part: Button"** *(More complex — introduces function and texture)*

> **AI says**: "*(dramatic, building suspense)* Case number two! My secret part is... something small and round. Lots of things are round, hmmm! Here is another clue — you can PUSH it with your finger. What am I thinking of?"
>
> **Possible child responses**:
> 1. (Ideal) "A button!" / "The button on its chest!" / "The power button!"
> 2. (Unexpected) "The eyes!" / "The wheels!" / "Its belly!" / Child guesses another round thing.
> 3. (No response) Child is quiet, thinking.
>
> **AI follow-up**:
> 1. "*(impressed gasp)* TWO clues and you nailed it! The button — yes! Small, round, and you push it to make something happen. Buttons are like tiny commands — press one and the robot listens! Inspector, you are on FIRE!"
> 2. "*(validating)* The eyes ARE round — smart thinking! But my secret part is not just round — you can push it IN, like pressing a doorbell. Boop! What on the robot can you press?"
>    - *(If child gets it)*: "*(celebrating)* The button — YES! You pushed through that tricky clue! Buttons tell the robot what to do."
>    - *(If child still struggles)*: "*(playful reveal)* Last clue — when you push it, the robot turns ON! It is... a BUTTON! Those little round circles you can press. Boop! On to case three!"
> 3. *(waits 2 seconds)* "*(gentle nudge)* Something small and round that you can push with your finger... boop! It is somewhere on the robot's body. Can you spot it?"
>
> **Screen**: Robot photo with a subtle shimmer across several round elements (buttons, eyes, wheels) — keeping the mystery alive. When the button is revealed, a zoomed-in highlight circle pops around the button area with a fun "BOOP!" text animation and a pressing-finger icon. "CASE 2" stamp with star appears.

**Round 3 — "The Secret Part: Joint"** *(Tricky — introduces hidden/less obvious parts)*

> **AI says**: "*(conspiratorial whisper)* Case number three — this one is sneaky! My secret part is hidden where two pieces CONNECT. You might not notice it at first! And here is your clue — it helps your robot BEND. What could it be?"
>
> **Possible child responses**:
> 1. (Ideal) "A joint!" / "The bendy part!" / "Where the arm bends!" / "The elbow!"
> 2. (Unexpected) "The arm!" / "The leg!" / "I don't see it!" / Child names a limb instead of the joint itself.
> 3. (No response) Child looks closely at the photo but is unsure.
>
> **AI follow-up**:
> 1. "*(astonished)* You found the SNEAKY one! The joint — that hidden bendy part where two pieces meet! Without joints, your robot would be stiff like a stick. Joints let it move and bend. Chief Inspector, you have EAGLE EYES!"
> 2. "*(warm, guiding)* The arm — YES, look at the arm! Now look WHERE the arm bends. See that little spot where two parts connect? THAT is the part I am thinking of. It is called a joint! Like YOUR elbow — see, bend your arm! Same idea!"
> 3. *(waits 2 seconds)* "*(helpful, playful)* This one IS sneaky! Look where the robot's arm meets its body, or where a leg can bend. There is a little hidden part there that lets it move. Do you see it? It is called a..."
>
> **Screen**: Robot photo with a very faint shimmer along the connection points of the robot's limbs. When the joint is revealed, a close-up zoom animation highlights the joint area, with a bending motion illustration overlaid — an arm bending back and forth with curved motion arrows. "CASE 3" stamp with a gold star and a "SNEAKY FIND!" badge.

**Round 4 (if child is engaged) — "The Secret Part: Eyes"** *(Imaginative — what it looks like vs. what it does)*

> **AI says**: "*(dreamy, wondering tone)* Bonus case! Last one — my secret part looks like two little glowing moons on the front of the robot. They do not really work like yours and mine... but they LOOK like they are watching everything! What are they?"
>
> **Possible child responses**:
> 1. (Ideal) "The eyes!" / "Robot eyes!" / "The lights on its face!"
> 2. (Unexpected) "The buttons!" / "Headlights!" / "Circles!"
> 3. (No response) Child is getting tired or distracted.
>
> **AI follow-up**:
> 1. "*(celebrating)* The EYES! Two little glowing moons — staring right at you! On a real robot, they might be lights or cameras, but they LOOK like eyes watching the world. You spotted them! BONUS CASE SOLVED!"
> 2. "*(warm, guiding)* Ooh, close — buttons and headlights are round too! But these are on the robot's FACE. They look like they are staring at you. What on a face stares and watches?"
>    - *(If child gets it)*: "*(delighted)* YES — the eyes! Two little glowing moons, right on its face!"
>    - *(If still unsure)*: "*(playful reveal)* They are the EYES! Those two round spots on the front that look like they are watching you. On a toy robot, they might be stickers or lights — but they look just like eyes!"
> 3. *(waits 2 seconds)* "*(gentle, cozy)* Two round things on the robot's face... they look like they can SEE you! What do we call those?"
>
> **Screen**: Robot photo with a soft mysterious glow emanating from the eye area. When revealed, the eyes get a playful "blink" animation — two sparkle bursts on the eye locations, then a cute winking animation overlaid. "BONUS CASE" stamp in gold with extra sparkle confetti.

**Step 4: Payoff — The Magic Moment**

> **AI says**: "*(building excitement, dramatic pause)* Chief Inspector... you did it. You inspected the antenna — that thin, pointy signal-catcher! You found the button — the little round commander! You cracked the case of the sneaky joint — the hidden bendy connector! And you spotted the eyes — those two glowing moon-watchers! Every single part of your robot — SOLVED! *(big celebration voice)* You are officially the CHIEF ROBOT INSPECTOR!"
>
> **Possible child responses**:
> 1. (Ideal) "Yay!" / "I did it!" / "I'm the inspector!" / Cheers or giggles.
> 2. (Unexpected) "Can we do more?" / "My robot is so cool!" / "I want another robot!"
> 3. (No response) Child smiles or looks at the screen.
>
> **AI follow-up**:
> 1. "*(beaming with pride)* The BEST Robot Inspector I have ever seen! Your robot is lucky to have someone who knows ALL its secrets."
> 2. "*(delighted)* You want MORE cases? That means you are a TRUE inspector — always looking for clues! We can inspect again another time. But first, let me tell you something amazing about what you just did..."
> 3. *(waits 2 seconds)* "*(warm whisper)* You know what? I think your robot is impressed too. You found every single one of its secrets. That is incredible."
>
> **Screen**: A large golden "CHIEF ROBOT INSPECTOR" badge fills the center of the screen with the toy robot photo as a portrait inside. Around it, small icons of each solved part orbit — antenna, button, joint, eyes — each with a checkmark. Confetti bursts in metallic silver and blue. Gear-shaped sparkles spin outward. A triumphant chime plays.

**Step 5: Celebration + IB Concepts**

> **AI says**: "*(warm, reflective pride)* You know what you did today? You looked really closely at every part of your robot — the thin antenna, the round button, the hidden joint, the glowing eyes. You noticed what each part LOOKS like. That is called Form — understanding the shape and look of things. And you figured out what each part DOES — the antenna catches signals, the button gives commands, the joint lets it bend, the eyes seem to watch. That is called Function — how each part works! You did not just play with your robot today. You INSPECTED it. Chief Robot Inspector — that is you!"
>
> **Possible child responses**:
> 1. (Ideal) "Form!" / "Function!" / "I'm an inspector!" / Repeats a concept word happily.
> 2. (Unexpected) "Can I show my robot to you again?" / "Bye robot!" / "I want to play more!"
> 3. (No response) Child listens or looks at the screen.
>
> **AI follow-up**:
> 1. "*(celebrating)* That is right — Form and Function! You earned your badge, Chief Robot Inspector. Next time you look at ANY toy, I bet you will notice all its hidden parts!"
> 2. "*(warm, laughing)* Your robot would love that! You are the best inspector it has ever had. See you next time, Chief Robot Inspector!"
> 3. *(waits 2 seconds)* "*(gentle closing)* Great job today, Inspector. Your robot has a really smart friend. See you next time!"
>
> **Screen**: The inspector badge remains centered. Below it, the words **"Form"** and **"Function"** appear one at a time in bold, metallic silver lettering — "Form" accompanied by a magnifying glass icon examining a shape, "Function" accompanied by a small gear icon turning. The toy robot photo glows softly behind the text. Gear-shaped sparkles rotate gently around the concept words. After 3 seconds, a "The End" ribbon in robot-metallic style scrolls across the bottom.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, state comparison, or non-speech audio detection required. All interaction is verbal — child deduces from spoken clues. Single photo used throughout. |
| 2 | Hook & Transition | PASS | Step 1b opens with emotional delight ("Whoa, look at this robot!") and an imaginative question ("If your robot could talk, what would it say?") — no knowledge testing. Activity grows naturally from admiration of the robot's parts into a guessing game about them. |
| 3 | Edge Case Coverage | PASS | Every step includes 3 response branches (ideal, unexpected, silence). All unexpected branches validate the child's response before redirecting. All silence branches wait 2 seconds then give a gentle, specific prompt. Round 2 and 3 include additional sub-branches for continued struggle after clue 2. |
| 4 | IB Completeness | PASS | Form and Function explicitly named in closing as earned praise. KUD is specific with concrete vocabulary (antenna, button, joint, wheel, signals, commands, bend). 3 ATL skills identified with sub-skills. 4 Related Concepts listed. Closing celebrates first, then naturally names concepts. Concepts match what the child actually did — observed forms and deduced functions. |
| 5 | Tier Appropriateness | PASS | T1: Sentences predominantly 5–8 words. Open-ended deduction questions used. Vocabulary is concrete and age-appropriate (thin, pointy, round, push, bend, sticking up). 2-step reasoning tasks (hear clue, match to visual). Achievable for ages 4–6. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers in parentheses and italics. Zero instances of "AI guides" or "AI encourages." All responses are warm, playful, and child-appropriate. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with layout, animations (pulsing glows, spotlight reveals, bending motion overlays, blink animations, gear sparkles, confetti), and visual elements (magnifying glass, case stamps, inspector badge, concept icons). |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter — non-mapping design. |
| 9 | Game Feel | PASS | Genuine stakes: "Can you guess before my third clue?" creates urgency. Uncertainty before each reveal. Clear magic moment: each "Found it!" plus the final cumulative celebration. Replayable — different parts could be targeted, or child could play with a different toy. Surprise and delight in the "sneaky" joint case and the imaginative "glowing moons" eye case. |
| 10 | Pillar Fidelity | PASS | Mystery pillar clearly delivered: AI picks hidden details, gives progressive clues, child deduces. Magic moment is "Found it!" reveal. Core loop is clue-based deduction (not generic Q&A). Child feels "I figured it out!" — the Mystery pillar emotion. Could not be re-labeled to Creation, Performance, or any other pillar without fundamentally changing the mechanic. |

**Overall**: ALL PASS — 0 issues found during self-evaluation

Ready for 教研 review.
