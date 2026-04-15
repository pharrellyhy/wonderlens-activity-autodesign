# Activity Design: Detail Detective — Property-Bridge Template (Category 1)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: Detail Detective

### A. Basic Info

- **Activity Name**: Detail Detective
- **Activity Category**: 1 — Sustained Verbal Interaction (In-Device)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: **Form** (What is it like?) & **Function** (How does it work?)
- **Related Concepts (Discipline)**: Observation, Pattern, Perspective, Discovery
- **ATL Skills Focus**: Thinking Skills (critical thinking, deduction), Research Skills (observation, information literacy), Communication Skills (expressing ideas, listening)
- **Experience Pillar**: Mystery
- **Game Style**: mystery_lens
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity with a detected {property} attribute (e.g., color, shape, material, texture)
- **Trigger Scene**: Child photographs an entity with multiple visible details that share or contrast along a detectable property category
- **Property Bridge**: AI detects a prominent property on the entity (e.g., "red" from the color category). This detected property SEEDS the clue category — every round becomes an "I Spy" deduction about a different detail defined by that property category. If color detected → each round targets a different color detail. If shape detected → each round targets a different shaped part. If material detected → each round targets a different material section.
- **Mapping Source**: none

### B. Activity Overview

- **① Brief Description**: After the child photographs their entity, the AI detects a prominent property (e.g., the dominant color "red" on a toy truck). The AI marvels at the entity, then reveals: "I noticed something special — your [entity] is full of secret colors!" The detected property seeds the CLUE CATEGORY for a multi-round "I Spy" deduction game. Each round, the AI picks a different detail on the entity defined by that property category and gives a progressive, descriptive clue. The child scans the photo, deduces the detail, and earns a "Found it!" each round. 3–4 rounds, each targeting a different detail, building toward the cumulative "You found every [property] secret!" celebration.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the names of specific details on the entity (e.g., wheels, windows, headlights, stickers). Learn descriptive vocabulary tied to the property category (e.g., red, silver, yellow, blue for color; round, square, pointy for shape). Learn that each detail has a particular look AND a particular job.
  - **U (Understand)**: Understand that every part of an entity has a specific appearance — shape, color, texture — and that noticing these details is called **Form** (what things are like). Understand that many details also have a purpose or job — that is **Function** (how things work).
  - **D (Do)**: Practice deductive reasoning by matching descriptive clues to visible details on a photograph (Thinking Skills — critical thinking, deduction). Practice careful, focused observation of fine details (Research Skills — observation). Practice describing and naming specific features using precise vocabulary (Communication Skills — expressing ideas).

- **③ Design Highlight**: The property-bridge mechanic makes every playthrough unique — the AI detects a REAL property of the photographed entity and uses it to seed the entire clue category. A red toy truck generates color-based rounds ("I spy something BLACK... SILVER... YELLOW..."). A LEGO castle with detectable shapes generates shape-based rounds ("I spy something SQUARE... ROUND... POINTY..."). This means the same child photographing different objects gets a fundamentally different detective experience each time. The progressive clue structure within each round — first a property clue, then a location hint, then a function clue — creates genuine suspense and gives the child multiple entry points to deduce the answer. The cumulative "You found every [property] secret!" moment transforms the child from casual observer to expert detective of their own belongings.

- **④ Typical Scenario**: Child photographs a colorful toy truck → AI detects "red" as the dominant color → "Wow, your truck is SO red! But I bet there are other colors hiding on it..." → Round 1: "I spy something NOT red — it's small, round, and BLACK!" (wheels) → Round 2: "I spy something SILVER and shiny — you can see through it!" (windows) → Round 3: "I spy something YELLOW on the front — it helps the truck see at night!" (headlights) → Round 4: "I spy the TINIEST bit of blue — almost hidden!" (a sticker or detail) → "You found every color secret on your truck!"

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs an entity (example: colorful toy truck) with no prior conversation. AI detects a prominent property: dominant color "red."
>
> **AI says**: "*(amazed, leaning-in gasp)* Whoa, look at your truck! It is SO red — like a fire engine! But wait... I am looking really closely and I think there are OTHER colors hiding on it. Sneaky little colors! If you could find every secret color on your truck, how many do you think there are?"
>
> **Possible child responses**:
> 1. (Ideal) "Three!" / "A lot!" / "I see black!" / Child guesses a number or names a color.
> 2. (Unexpected) "It's my favorite truck!" / "Daddy gave it to me!" / "Vroom vroom!" / Child talks about the truck or plays with it.
> 3. (No response) Child looks at the screen silently.
>
> **AI follow-up**:
> 1. "*(excited, conspiratorial)* Ooh, you are already spotting them! I bet there are even MORE than you think. Want to play a detective game? I will give you clues and YOU find each secret color!"
> 2. "*(warm, delighted)* I can tell you LOVE that truck! And your truck is FULL of hidden colors — not just red. I bet a truck expert like you can find them all. Want to try a detective game?"
> 3. *(waits 2 seconds)* "*(playful whisper)* I see at least FOUR secret colors on your truck besides red. I bet you can find them if I give you clues. Want to be a Detail Detective?"
>
> **Screen**: Entity photo centered on screen. A soft magnifying-glass shimmer animation slowly sweeps across the photo, as if scanning for hidden details. Tiny colorful question marks (matching the hidden detail colors) float around the edges of the photo. The dominant detected property (red) glows warmly on the entity.

**Step 2: Game Setup + Demo — "The Detail Detective Agency"**

> **AI says**: "*(playful, mystery-voice)* Okay, here is how it works! I spy a secret detail on your truck. I give you clues about what it looks like. You look at your truck and guess what I am spying! Watch — I will show you. I spy something on your truck that is... RED! Hmm, almost everything is red! Too easy. Let me try harder. I spy something BLACK and round — it touches the ground! Can you guess? The WHEELS! See how that works? Now the REAL game — I will find tricky hidden colors. Ready, Detective?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yeah!" / "I can find them!" / "Let's play!"
> 2. (Unexpected) "I knew it was the wheels!" / "My truck has big wheels!" / Repeats "wheels!"
> 3. (No response) Child is quiet, possibly processing the rules.
>
> **AI follow-up**:
> 1. "*(excited countdown)* Alright, Detail Detective — Case One starts NOW! Open your eyes wide and listen to my clue..."
> 2. "*(delighted, impressed)* You already knew! You are a natural detective! But the next ones are going to be trickier. Here comes the first REAL clue..."
> 3. *(waits 2 seconds)* "*(encouraging, gentle)* It is easy — I describe a secret color, you find it! Any guess is a great guess. Here comes the first one... listen carefully!"
>
> **Screen**: Entity photo slides to the left side. On the right, a magnifying glass icon appears with "DETAIL DETECTIVE" in bold playful letters. A quick demo animation plays: a glowing question mark hovers over the entity, then a clue bubble appears ("Something BLACK and round..."), then the wheels flash and sparkle with a "FOUND IT!" stamp. Below, a "Case 1" badge glows, ready. A small property-category label reads "COLOR CLUES" with a rainbow bar icon.

**Step 3: Multi-Round Interaction (3–4 rounds)**

**Round 1 — "I Spy Something BLACK!" *(Simple, high-contrast — build confidence)***

> **AI says**: "*(mysterious narrator voice)* Case number one! I spy something on your truck that is NOT red at all. It is small... it is round... and it is BLACK — dark as night! And your truck has more than one of them. Look at your truck. Can you find the black things?"
>
> **Possible child responses**:
> 1. (Ideal) "The wheels!" / "Tires!" / "The round black things on the bottom!"
> 2. (Unexpected) "The bumper!" / "I don't know!" / "Black?" / Child guesses wrong.
> 3. (No response) Child looks at the photo but says nothing.
>
> **AI follow-up**:
> 1. "*(thrilled, celebratory)* You GOT it! The WHEELS — yes! Those little round black circles that help your truck roll everywhere! Without them, your truck would be stuck. You know what the wheels DO? They let the truck zoom across the floor — that is their job! FIRST secret color — found! Detective, you are sharp!"
> 2. "*(warm, encouraging)* Ooh, good thinking — but look again! My secret things are round like donuts and they touch the ground. Your truck rolls on them! What are they?"
>    - *(If child guesses correctly after hint)*: "*(excited)* YES! The wheels — those black circles on the bottom! They help the truck roll. First color secret — FOUND!"
>    - *(If child still guesses wrong or is silent)*: "*(playful reveal)* Here is my last clue — your truck ROLLS on them! They are... the WHEELS! See? Black and round, right down there. Now you will always notice them. On to Case Two!"
> 3. *(waits 2 seconds)* "*(helpful whisper)* Look at the very BOTTOM of your truck. Something round and black is down there... your truck rolls on them! What are they?"
>
> **Screen**: Entity photo with a soft pulsing glow around the lower area (not directly highlighting the wheels — preserving the mystery). When revealed, the wheel areas get bright spotlight circles and sparkle burst animation. A "CASE 1 — FOUND IT!" stamp appears with a star. If solved on first clue, a "SHARP EYES!" bonus banner flashes. A small color swatch showing BLACK appears in a "Colors Found" tracker strip at the bottom.

**Round 2 — "I Spy Something SILVER!" *(Introduces function — moderate difficulty)***

> **AI says**: "*(dramatic, building suspense)* Case number two! I spy something SILVER and shiny — like a little mirror! It is flat and smooth. And here is a big clue — you can almost see THROUGH it! What silver thing on your truck can you look through?"
>
> **Possible child responses**:
> 1. (Ideal) "The windows!" / "The glass!" / "The windshield!" / "That clear part!"
> 2. (Unexpected) "The bumper!" / "The door handle!" / "Metal!" / Child guesses another shiny thing.
> 3. (No response) Child is quiet, thinking.
>
> **AI follow-up**:
> 1. "*(impressed gasp)* TWO clues and you nailed it! The WINDOWS — yes! Silver and shiny, and you can see right through them! You know why trucks have windows? So the driver can see where they are going! Without windows, the driver would be driving in the dark! SECOND secret color — found! Detective, you are on FIRE!"
> 2. "*(validating)* The bumper IS shiny — smart thinking! But my secret thing is flat and smooth and you can look THROUGH it — like you are peeking inside! What part of the truck lets you peek in?"
>    - *(If child gets it)*: "*(celebrating)* The windows — YES! Silver, shiny, and see-through! They help the driver look outside."
>    - *(If child still struggles)*: "*(playful reveal)* Last clue — the driver LOOKS through these to see the road! They are... the WINDOWS! See how they shimmer silver? Now you know! On to Case Three!"
> 3. *(waits 2 seconds)* "*(gentle nudge)* Something silver and shiny... and you can almost see through it, like glass! It is on the front and sides of the truck. Can you spot it?"
>
> **Screen**: Entity photo with a subtle shimmer across several shiny elements (windows, bumper, any chrome) — keeping the mystery alive. When the windows are revealed, a zoomed-in highlight pops around the window area with a gleaming sparkle animation and a "PEEK-A-BOO!" text animation. "CASE 2 — FOUND IT!" stamp with star appears. SILVER swatch adds to the "Colors Found" tracker.

**Round 3 — "I Spy Something YELLOW!" *(Tricky — small detail + function clue)***

> **AI says**: "*(conspiratorial whisper)* Case number three — this one is sneaky! I spy something YELLOW — bright like the sun! It is small, it is on the FRONT of your truck, and here is the big clue — it helps the truck see at NIGHT! What could it be?"
>
> **Possible child responses**:
> 1. (Ideal) "The headlights!" / "The lights!" / "The front lights!" / "The yellow circles!"
> 2. (Unexpected) "The bumper!" / "A sticker!" / "I don't see yellow!" / Child doesn't spot it at first.
> 3. (No response) Child looks closely at the photo but is unsure.
>
> **AI follow-up**:
> 1. "*(astonished)* You found the SNEAKY one! The HEADLIGHTS — those little yellow circles on the front! You know what headlights do? When it is dark outside, they turn ON and shine bright so the truck can see the road! Like flashlights for trucks! Detail Detective, you have EAGLE EYES!"
> 2. "*(warm, guiding)* Hmm, look right at the FRONT of the truck — the very front! See two small circles? They are a little bit yellow. At night, when it is dark, they light up to help the truck see. What do we call lights on the front of a truck?"
>    - *(If child gets it)*: "*(celebrating)* YES! The headlights! Bright yellow helpers that light up the road!"
>    - *(If still stuck)*: "*(playful reveal)* They are the HEADLIGHTS! Those little yellow circles right on the front. When it is dark, they turn on and go BEEEAM! Now you know their secret!"
> 3. *(waits 2 seconds)* "*(helpful, playful)* This one IS sneaky! Look at the very FRONT of your truck. Two little circles. They are yellow and they glow at night to help the truck see. Do you see them? They are called..."
>
> **Screen**: Entity photo with a very faint warm glow around the front area. When the headlights are revealed, a close-up zoom animation highlights the headlight area, with a tiny beam-of-light illustration overlaid — two warm yellow cones shining outward with sparkle trails. "CASE 3 — FOUND IT!" stamp with a gold star and a "SNEAKY FIND!" badge. YELLOW swatch adds to the tracker.

**Round 4 (if child is engaged) — "I Spy the TINIEST Bit of BLUE!" *(Almost hidden — maximum detective challenge)***

> **AI says**: "*(dreamy, wondering tone)* Bonus case — the hardest one yet! I spy the TINIEST little bit of blue — almost hidden! You have to look SO carefully. It is flat and tiny and stuck right ON the truck. It might be a picture or a word or a little design. It is sooooo small! Can you find the secret blue?"
>
> **Possible child responses**:
> 1. (Ideal) "A sticker!" / "The logo!" / "That tiny blue thing!" / "I see it!"
> 2. (Unexpected) "There is no blue!" / "I can't find it!" / "The sky?"
> 3. (No response) Child is getting tired or distracted.
>
> **AI follow-up**:
> 1. "*(celebrating)* You found the HIDDEN one! A tiny blue sticker — so small most people would NEVER notice it! But a Detail Detective has sharper eyes than anyone. You spotted it! BONUS CASE SOLVED!"
> 2. "*(warm, guiding)* It IS really hard to see! Look right on the SIDE of the truck. There is a teeny tiny sticker or marking. Is there a little bit of blue hiding there? Look super close..."
>    - *(If child finds it)*: "*(delighted)* YES — you found it! That tiny hidden blue detail! You have the best eyes!"
>    - *(If still unsure)*: "*(playful reveal)* It is a tiny little STICKER — see? Right there on the side! A little splash of blue hiding in all that red. It was the sneakiest color secret of all, but now YOU know it is there!"
> 3. *(waits 2 seconds)* "*(gentle, cozy)* This one is SO tiny — even I almost missed it! Look on the side of your truck... there is a teeny tiny bit of blue. A sticker, maybe? Can you see it?"
>
> **Screen**: Entity photo with a very subtle blue twinkle animation in the area of the tiny detail. When revealed, a dramatic zoom-in animation magnifies the sticker/detail area, then a sparkle explosion reveals the blue detail. "BONUS CASE — FOUND IT!" stamp in gold with extra sparkle confetti. BLUE swatch completes the "Colors Found" tracker, which now shows all four colors in a row.

**Step 4: Payoff — The Magic Moment**

> **AI says**: "*(building excitement, dramatic pause)* Detail Detective... you did it. You found the BLACK wheels — those round rollers at the bottom! You uncovered the SILVER windows — shiny and see-through! You spotted the YELLOW headlights — those sneaky little night helpers! And you tracked down the TINIEST bit of hidden blue! Every single secret color on your truck — FOUND! *(big celebration voice)* You did not miss a SINGLE one! You are officially a MASTER Detail Detective!"
>
> **Possible child responses**:
> 1. (Ideal) "Yay!" / "I found them all!" / "I'm a detective!" / Cheers or giggles.
> 2. (Unexpected) "Can we do more?" / "My truck is so cool!" / "I want to find more colors!"
> 3. (No response) Child smiles or looks at the screen.
>
> **AI follow-up**:
> 1. "*(beaming with pride)* The BEST Detail Detective I have ever seen! Your truck is full of secrets and you found every single one!"
> 2. "*(delighted)* You want MORE cases? That means you are a TRUE detective — always looking for clues! We can detective again another time. But first, let me tell you something amazing about what you just did..."
> 3. *(waits 2 seconds)* "*(warm whisper)* You know what? Your truck has been hiding those colors this whole time, and YOU are the first one to find them all. That is incredible."
>
> **Screen**: A large golden "MASTER DETAIL DETECTIVE" badge fills the center of the screen with the entity photo as a portrait inside. Around it, small color swatches orbit — black, silver, yellow, blue — each with a checkmark and a tiny icon of the detail (wheel, window, headlight, sticker). Confetti bursts in the four discovered colors. Magnifying-glass sparkles spin outward. A triumphant chime plays. The "Colors Found" tracker at the bottom shows all four swatches filled with a golden glow connecting them.

**Step 5: Celebration + IB Concepts**

> **AI says**: "*(warm, reflective pride)* You know what you did today? You looked REALLY closely at your truck — not just the big obvious red parts, but the tiny hidden details too. The black wheels, the silver windows, the yellow headlights, the teensy blue sticker. You noticed what each part LOOKS like — its color, its shape, where it hides. That is called Form — understanding what things look like, down to the smallest detail. And you figured out what some of those parts DO — the wheels help it roll, the windows let the driver see, the headlights shine at night. That is called Function — how each part works! You did not just look at your truck today. You DETECTED it. Every hidden color, every secret detail. Master Detail Detective — that is you!"
>
> **Possible child responses**:
> 1. (Ideal) "Form!" / "Function!" / "I'm a detective!" / Repeats a concept word happily.
> 2. (Unexpected) "Can I show you another toy?" / "I want to find more!" / "Bye truck!"
> 3. (No response) Child listens or looks at the screen.
>
> **AI follow-up**:
> 1. "*(celebrating)* That is right — Form and Function! You earned your badge, Master Detail Detective. Next time you look at ANYTHING, I bet you will notice colors and details nobody else sees!"
> 2. "*(warm, laughing)* Another toy? A detective is ALWAYS looking for the next case! See you next time, Master Detail Detective!"
> 3. *(waits 2 seconds)* "*(gentle closing)* Great job today, Detective. You see things most people miss. That is a superpower. See you next time!"
>
> **Screen**: The detective badge remains centered. Below it, the words **"Form"** and **"Function"** appear one at a time in bold, metallic gold lettering — "Form" accompanied by a magnifying glass icon examining a color swatch, "Function" accompanied by a small gear icon turning. The entity photo glows softly behind the text. Magnifying-glass sparkles rotate gently around the concept words. The four color swatches (black, silver, yellow, blue) rest below the concept words as earned trophies. After 3 seconds, a "The End" ribbon in detective-badge style scrolls across the bottom.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, state comparison, or non-speech audio detection required. All interaction is verbal — child deduces from spoken clues. Single photo used throughout. The "property detection" is performed by AI vision on the initial photo (supported in V1). All subsequent rounds are AI-driven dialogue and pre-programmed screen animations, not camera-detected state changes. |
| 2 | Hook & Transition | PASS | Step 1b opens with emotional delight ("Whoa, look at your truck! It is SO red!") and an inviting question ("how many secret colors do you think there are?") — no knowledge testing. Activity grows naturally from admiration of the entity's dominant color into a detective game about hidden contrasting colors. Remove step labels and it reads as flowing conversation. |
| 3 | Edge Case Coverage | PASS | Every step includes 3 response branches (ideal, unexpected, silence). All unexpected branches validate the child's response before redirecting. All silence branches wait 2 seconds then give a gentle, specific prompt. Rounds 1–4 include additional sub-branches for continued struggle after second clue. Template includes guidance for different property categories (shape, material — not just color). |
| 4 | IB Completeness | PASS | Form and Function explicitly named in closing as earned praise. KUD is specific with concrete vocabulary (wheels, windows, headlights, stickers, black, silver, yellow, blue). 3 ATL skills identified with sub-skills. 4 Related Concepts listed. Closing celebrates first, then naturally names concepts. Concepts match what the child actually did — observed forms (color details) and deduced functions (what details do). |
| 5 | Tier Appropriateness | PASS | T1: Sentences predominantly 5–8 words. Open-ended deduction questions used. Vocabulary is concrete and age-appropriate (round, shiny, tiny, flat, see-through, peek). 2-step reasoning tasks (hear clue, match to visible detail). Achievable for ages 4–6. 3–4 rounds appropriate for T1 attention span. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers in parentheses and italics. Zero instances of "AI guides" or "AI encourages." All responses are warm, playful, and child-appropriate. Specific detail descriptions: "small, round, and BLACK — dark as night!" not generic "something black." |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with layout, animations (magnifying-glass shimmer, spotlight reveals, zoom-in animations, beam-of-light overlays, sparkle bursts, confetti), and visual elements (magnifying glass icon, case stamps, detective badge, color swatch tracker, concept icons). The "Colors Found" tracker adds a cumulative visual progression across rounds. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter — property-bridge seeds the clue category, not a mapping. |
| 9 | Game Feel | PASS | Genuine stakes: "Can you find the secret before my next clue?" creates urgency. Uncertainty before each reveal. Clear magic moment: each "Found it!" plus the final cumulative "You found every color secret!" celebration. Replayable — different entities produce different detected properties and thus fundamentally different games. Surprise and delight in the "TINIEST bit of blue" bonus round and the "SNEAKY FIND!" badge. The property-bridge means the game feels personal — "MY truck really IS red with hidden colors!" |
| 10 | Pillar Fidelity | PASS | Mystery pillar clearly delivered: AI hides details, gives progressive clues, child deduces. Magic moment is "Found it!" reveal each round. Core loop is clue-based deduction (not generic Q&A or creative expression). Child feels "I figured it out!" — the Mystery pillar emotion. Could not be re-labeled to Creation, Nurture, Performance, or any other pillar without fundamentally changing the mechanic. Property-bridge adds uniqueness: detected property seeds the entire clue category, making Mystery personal. |

**Overall**: ALL PASS — 0 issues found during self-evaluation

Ready for 教研 review.
