## Detail Detective

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Detail Detective |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Form, Function |
| Related Concepts | Observation, Pattern, Perspective, Discovery |
| ATL Skills Focus | Thinking Skills (critical thinking, deduction), Research Skills (observation, information literacy), Communication Skills (expressing ideas, listening) |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |
| Property Bridge | AI detects a prominent property on the entity (e.g., dominant color "red"). This detected property seeds the CLUE CATEGORY — every round targets a different detail defined by that property category. Color detected → rounds target different color details. Shape detected → rounds target different shaped parts. Material detected → rounds target different material sections. |

### A.5 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{property}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  # Any one of these seeds the mystery-clue category at runtime.
  - tier_0.appearance.color     # seeds "color" mystery
  - tier_0.appearance.shape     # seeds "shape" mystery
  - tier_0.appearance.pattern   # seeds "pattern" mystery
  - tier_0.senses.touch_feel    # seeds "texture/material" mystery
```

### B. Activity Overview

**① Brief Description**

After the child photographs their entity, the AI detects a prominent property (e.g., the dominant color "red" on a toy truck). The AI marvels at the entity, then reveals it is full of secret details within that property category. Each round, the AI picks a different detail on the entity defined by that category and gives progressive "I Spy" clues. The child scans the photo, deduces the detail, and earns a "Found it!" each round. 3–4 rounds, building toward the cumulative "You found every [property] secret!" celebration.

**② Educational Purpose (KUD)**

- **K (Know):** Learn the names of specific details on the entity (wheels, windows, headlights, stickers). Learn descriptive vocabulary tied to the property category (e.g., red, silver, yellow, blue for color). Learn that each detail has a particular look AND a particular job.
- **U (Understand):** Every part of an entity has a specific appearance — that is Form (what things are like). Many details also have a purpose or job — that is Function (how things work).
- **D (Do):** Practice deductive reasoning by matching descriptive clues to visible details. Practice careful, focused observation of fine details. Practice describing and naming features using precise vocabulary.

**③ Design Highlight**

The property-bridge mechanic makes every playthrough unique — the AI detects a REAL property and uses it to seed the entire clue category. A red truck generates color-based rounds ("I spy something BLACK... SILVER... YELLOW..."). A LEGO castle with shapes generates shape-based rounds. The progressive clue structure within each round — property clue, then location hint, then function clue — creates genuine suspense and gives the child multiple entry points. The cumulative "You found every [property] secret!" transforms the child from casual observer to expert detective.

**④ Typical Scenario**

Child photographs a colorful toy truck → AI detects "red" → "Your truck is SO red! But I bet there are other colors hiding on it..." → Round 1: "I spy something BLACK and round!" (wheels) → Round 2: "I spy something SILVER — you can see through it!" (windows) → Round 3: "I spy something YELLOW — it helps the truck see at night!" (headlights) → Round 4: "I spy the TINIEST bit of blue!" (sticker) → "You found every color secret!"

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (amazed, leaning-in gasp) "Whoa, look at your truck! It is SO red — like a fire engine! But wait... I think there are OTHER colors hiding on it. Sneaky little colors! If you could find every secret color on your truck, how many do you think there are?"

**Child responses:**

1. (Ideal) "Three!" / "A lot!" / "I see black!"
2. (Unexpected) "It's my favorite truck!" / "Daddy gave it to me!" / "Vroom vroom!"
3. (No response) Child looks at the screen silently.

**AI follow-up:**

1. (excited, conspiratorial) "Ooh, you are already spotting them! I bet there are even MORE than you think. Want to play a detective game? I give you clues and YOU find each secret color!"
2. (warm, delighted) "I can tell you LOVE that truck! And it is FULL of hidden colors — not just red. I bet a truck expert like you can find them all. Want to try a detective game?"
3. (wait 2s) (playful whisper) "I see at least FOUR secret colors on your truck besides red. I bet you can find them if I give you clues. Want to be a Detail Detective?"

**Screen:** Entity photo centered with magnifying-glass shimmer scanning across; tiny colorful question marks floating around edges; dominant property (red) glows warmly on entity.

#### Step 2: Rule Introduction + Demo

**AI says:** (playful, mystery-voice) "Okay, here is how it works! I spy a secret detail on your truck. I give you clues about what it looks like. You look and guess! Watch — I spy something BLACK and round — it touches the ground! Can you guess? The WHEELS! See how that works? Now the REAL game — I will find tricky hidden colors. Ready, Detective?"

**Child responses:**

1. (Ideal) "Ready!" / "Yeah!" / "I can find them!"
2. (Unexpected) "I knew it was the wheels!" / "My truck has big wheels!"
3. (No response) Child is quiet, processing the rules.

**AI follow-up:**

1. (excited countdown) "Alright, Detail Detective — Case One starts NOW! Open your eyes wide and listen..."
2. (delighted, impressed) "You already knew! You are a natural detective! But the next ones are trickier. Here comes the first REAL clue..."
3. (wait 2s) (encouraging, gentle) "It is easy — I describe a secret color, you find it! Any guess is a great guess. Here comes the first one..."

**Screen:** Entity photo on left. Magnifying glass icon with "DETAIL DETECTIVE" in bold playful letters on right. Quick demo animation: glowing question mark over entity, clue bubble, wheels flash with "FOUND IT!" stamp. "Case 1" badge glows below. "COLOR CLUES" label with rainbow bar icon.

#### Step 3: Multi-Round Interaction

**Round 1 — "I Spy Something BLACK!"** (simple, high-contrast — build confidence)

**AI says:** (mysterious narrator) "Case number one! I spy something on your truck that is NOT red at all. It is small... round... and BLACK — dark as night! Your truck has more than one of them. Can you find the black things?"

**Child responses:**

1. (Ideal) "The wheels!" / "Tires!" / "The round black things on the bottom!"
2. (Unexpected) "The bumper!" / "I don't know!" / "Black?"
3. (No response) Child looks at the photo but says nothing.

**AI follow-up:**

1. (thrilled, celebratory) "You GOT it! The WHEELS — those little round black circles that help your truck roll everywhere! You know what they DO? They let the truck zoom across the floor! FIRST secret color — found!"
2. (warm, encouraging) "Good thinking — but look again! My secret things are round like donuts and they touch the ground. Your truck rolls on them!" If child gets it: "YES! The wheels! First color secret — FOUND!" If still stuck: "Your truck ROLLS on them! They are... the WHEELS!"
3. (wait 2s) (helpful whisper) "Look at the very BOTTOM of your truck. Something round and black is down there... your truck rolls on them! What are they?"

**Screen:** Soft pulsing glow around lower area. When revealed, wheels get bright spotlight and sparkle burst. "CASE 1 — FOUND IT!" stamp with star. First-clue solves get "SHARP EYES!" banner. BLACK swatch appears in "Colors Found" tracker at bottom.

**Round 2 — "I Spy Something SILVER!"** (introduces function — moderate): AI gives clues — "silver and shiny, like a little mirror" then "you can almost see THROUGH it." Child deduces windows. AI celebrates: "So the driver can see where they are going! Without windows, the driver would be driving in the dark!" If child guesses another shiny thing (bumper, door handle), AI redirects: "flat and smooth and you can look THROUGH it — like peeking inside!"

**Round 3 — "I Spy Something YELLOW!"** (tricky — small detail + function): AI whispers "something YELLOW, bright like the sun, on the FRONT of your truck — it helps the truck see at NIGHT!" Child finds headlights. AI celebrates: "Like flashlights for trucks!" If child doesn't see yellow, AI guides: "Look right at the very front — two small circles. At night they light up!"

**Round 4 (if engaged) — "I Spy the TINIEST Bit of BLUE!"** (almost hidden — maximum challenge): AI says "the TINIEST little bit of blue — almost hidden! Flat and tiny, stuck right ON the truck." Child finds a sticker or marking. AI: "So small most people would NEVER notice it! But a Detail Detective has sharper eyes than anyone!"

#### Step 4: Celebration

**AI says:** (building excitement, dramatic pause) "Detail Detective... you did it. You found the BLACK wheels — those round rollers! You uncovered the SILVER windows — shiny and see-through! You spotted the YELLOW headlights — those sneaky night helpers! And you tracked down the TINIEST bit of hidden blue! Every single secret color on your truck — FOUND! (big celebration) You are officially a MASTER Detail Detective!"

**Child responses:**

1. (Ideal) "Yay!" / "I found them all!" / "I'm a detective!"
2. (Unexpected) "Can we do more?" / "My truck is so cool!"
3. (No response) Child smiles or looks at the screen.

**AI follow-up:**

1. (beaming with pride) "The BEST Detail Detective I have ever seen! Your truck is full of secrets and you found every single one!"
2. (delighted) "You want MORE cases? That means you are a TRUE detective — always looking for clues! We can detective again another time. But first, let me tell you something amazing..."
3. (wait 2s) (warm whisper) "Your truck has been hiding those colors this whole time, and YOU are the first one to find them all. That is incredible."

**Screen:** Golden "MASTER DETAIL DETECTIVE" badge with entity photo as portrait inside. Color swatches orbit — black, silver, yellow, blue — each with checkmark and tiny detail icon. Confetti in the four discovered colors. Magnifying-glass sparkles. "Colors Found" tracker shows all four swatches filled with golden glow.

#### Step 5: Closing + IB Concepts

**AI says:** (warm, reflective pride) "You looked REALLY closely at your truck — not just the big obvious red parts, but the tiny hidden details too. You noticed what each part LOOKS like — its color, its shape, where it hides. That is called Form — understanding what things look like. And you figured out what some parts DO — wheels help it roll, windows let the driver see, headlights shine at night. That is called Function — how each part works! You did not just look at your truck today. You DETECTED it. Master Detail Detective — that is you!"

**Child responses:**

1. (Ideal) "Form!" / "Function!" / "I'm a detective!"
2. (Unexpected) "Can I show you another toy?" / "I want to find more!"
3. (No response) Child listens or looks at the screen.

**AI follow-up:**

1. (celebrating) "That is right — Form and Function! You earned your badge, Master Detail Detective. Next time you look at ANYTHING, I bet you will notice colors and details nobody else sees!"
2. (warm, laughing) "Another toy? A detective is ALWAYS looking for the next case! See you next time, Master Detail Detective!"
3. (wait 2s) (gentle closing) "Great job today, Detective. You see things most people miss. That is a superpower. See you next time!"

**Screen:** Detective badge centered. "Form" with magnifying glass icon and "Function" with gear icon in bold metallic gold. Entity photo glows softly behind. Four color swatches as earned trophies below. "The End" ribbon in detective-badge style scrolls across bottom.
