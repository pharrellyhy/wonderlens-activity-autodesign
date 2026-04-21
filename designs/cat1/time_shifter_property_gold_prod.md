## The Time Shifter

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Time Shifter |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | Change, Causation |
| Related Concepts | Journey, Growth, Systems, Discovery |
| ATL Skills Focus | Thinking Skills (creative, transfer), Communication Skills (expressing, listening), Research Skills (observation) |
| Game Style | time_shifter |
| Design Version | 2.0 |
| Last Updated | 2026-04-08 |
| Property Bridge | AI detects a current property that changes over time; each time jump explores how that property was different |
| Example Entity | Yellow banana (property = yellow/color) |

### A.5 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{property}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  # Any one of these supplies a property that changes over time (the time-jump engine).
  - tier_2.change.waterproof_coating_wear      # e.g., raincoat (condition over time)
  - tier_2.change.full_metamorphosis           # e.g., butterfly (form over time)
  - tier_2.change.brown_spots_sugar_change     # e.g., banana (color over time)
  - tier_2.change.color_shift_with_age_health  # e.g., goldfish (color over time)
  - tier_2.change.fur_matting_over_time        # e.g., plush_toys (texture over time)
```

### B. Activity Overview

**1. Brief Description**: The child becomes a "Time Shifter" who uses the photographed entity's detected property as a portal through time. The AI notices a specific property RIGHT NOW and reveals it has not always been the same. Together, they shift through time — visiting the entity at different moments to discover how the property looked, felt, and behaved differently. At a critical moment, the child makes a choice that branches the entity's future. The magic moment is seeing the whole timeline assembled — the property transforming at every stop.

**2. Educational Purpose (KUD)**:
- **K (Know)**: (1) Bananas start as small green flowers on a tropical plant, (2) green bananas slowly turn yellow as they ripen, (3) bananas travel across oceans on ships before reaching stores, (4) overripe bananas turn brown with dark spots, (5) the color tells you its stage of ripeness
- **U (Understand)**: (1) Properties change over time — what something looks like NOW is just one moment in a long timeline (Change), (2) Each property change happens for a reason — sunshine makes it grow, ripening makes it change color, your choice determines its future (Causation)
- **D (Do)**: (1) Sequence property changes across a timeline, (2) Make and justify a choice about what happens next, (3) Describe how a property looked different at distinct points in time

**3. Design Highlight**: The AI detects a SINGLE CURRENT PROPERTY and uses it as the through-line for every time jump. A genuine branching choice point creates real stakes. The magic moment is seeing the property's transformation assembled into a connected timeline — one observable quality tracked through time.

**4. Typical Scenario**: Child photographs a yellow banana. AI detects "yellow" as the key property. AI launches a time-shifting adventure focused on COLOR — traveling backward to when it was different (green flower, green bunch, greenish-yellow on a ship) and forward to when it will change again (brown spots, compost). Child makes a choice that branches the color future; the timeline shows color transforming at every stop.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**AI says:** (amazed, whispering) "Whoa... look at THIS banana! It is SO yellow — bright, sunny yellow, like a little banana sunshine sitting right there. But here's a wild secret... your banana was NOT always yellow. A long time ago, this exact banana was a TOTALLY different color! What color do you think your banana was before it turned yellow?"

**Child responses:**

1. (Ideal) "Green!" / "It was green!" / "White?" / "Brown?"
2. (Unexpected) "It was always yellow!" / "I don't know!" / "I want to eat it!"
3. (No response) Child is silent or looking at the screen.

**AI follow-up:**

1. (excited) "YES! Your banana used to be a completely different color! It has been changing color its whole life. What if we could SHIFT through time and SEE every color it's ever been? I know a way..."
2. (playful, warm) "You know what's amazing? This banana has actually CHANGED colors — like magic! It wasn't born yellow. What if we could travel through time and watch the color change happen?"
3. (wait 3s) (gentle) "I'll tell you a secret — your banana used to be bright GREEN! Way up on a tall plant in a hot jungle. Want to go back in time and see it?"

**Screen:** Banana photo centered with golden glow. "YELLOW" floats above in playful lettering. Faint clock hands spin. Color spectrum strip at the bottom hints at greens and browns on either side of the yellow center.

#### Step 2: Rule Introduction + Demo

**AI says:** (conspiratorial excitement) "Okay, here's how it works — your banana's color is like a TIME PORTAL! We're going to SHIFT through time and visit your banana at different moments. At each stop, the color is DIFFERENT. You tell me what you see and imagine! Ready for the first shift? Here we go... *SHIIIIIFT!* We just landed THREE MONTHS AGO! Your banana isn't yellow yet. It isn't even a banana yet! It's a teeny tiny GREEN flower, smaller than your pinky finger, growing on a BIG tall plant in a hot, rainy jungle. Green green green — like a little emerald. What do you think this tiny green flower smells like in all that warm rain?"

**Child responses:**

1. (Ideal) "It smells like flowers!" / "Like rain!" / "Sweet!"
2. (Unexpected) "That's not a banana!" / "I don't like green!" / "Flowers are pink!"
3. (No response) Child is quiet.

**AI follow-up:**

1. (delighted) "Ooh, {child's answer}! I bet it smells just like that — warm and fresh and alive! And this tiny green flower is going to grow and grow, and its color is going to start changing. Let's shift to the next time stop and watch..."
2. (warm, validating) "You're right, it doesn't LOOK like a banana yet! But this is where your banana's color story begins — everything starts GREEN. Let's shift forward and watch the color change happen!"
3. (wait 3s) (encouraging) "I think it might smell warm and sweet — like rain on leaves! This tiny green flower is the very beginning of your banana's color story. Let's shift forward and see..."

**Screen:** Banana photo shrinks to top-right with "NOW: YELLOW" label. Main area shows illustrated jungle with tiny green flower highlighted. Rain drops animated. TIME SHIFT dial shows "3 MONTHS AGO." COLOR TIMELINE begins at bottom: bright green bar with flower icon as first stop.

#### Step 3: Multi-Round Interaction

**Round 1 — "Six Weeks Ago: The Green Gang":**

**AI says:** (whooshing) "*SHIIIIIFT!* SIX WEEKS AGO! The flower is gone — now there's a whole BUNCH of green bananas hanging together like fat green fingers! Your banana is one of them — chubby, stubby, and SO green. Not a speck of yellow anywhere! What do you think they're waiting for?"

**Child responses:**

1. (Ideal) "To turn yellow!" / "To get picked!" / "To grow bigger!"
2. (Unexpected) "Bananas don't wait!" / "I like green bananas!" / "They look like fingers!"
3. (No response) Child is quiet.

**AI follow-up:**

1. (laughing) "Yes — {child's answer}! The sunshine is what starts changing their color. Every day, a teensy bit more yellow sneaks in. But right now — pure green! Let's shift forward and see when the yellow starts..."
2. (playful) "They DO look like fingers! That's why a bunch is called a 'hand'! And right now, every finger is green — but the sunshine is starting to work its magic on the color..."
3. (wait 3s) (prompting) "I think they're waiting to change color! Every day, the sunshine makes them a tiny bit less green. Let's shift forward and watch..."

**Screen:** Green banana bunch on a plant, one banana glows. TIME SHIFT dial: "6 WEEKS AGO." COLOR TIMELINE extends: green flower -> green bunch, connected by bright green bar.

**Round 2 — "Two Weeks Ago: The Color Change Ship":** Banana is on a huge cargo ship crossing the ocean. The cool dark room is where the magic happens — green slowly turning greenish-yellow. The child guesses how much yellow the banana has. AI reveals the cool temperature CAUSES the color change. COLOR TIMELINE extends: green -> green -> greenish-yellow.

**Round 3 — "Right Now: The Big Choice" (CHOICE POINT):** The banana is BRIGHT YELLOW — the color the child photographed. But the color is not done changing. The child faces a genuine choice: does the banana go to the **fruit bowl** (yellow turns golden-brown with sweet spots over days) or the **freezer** (skin turns dark brown-black but inside stays creamy yellow for banana bread)? Two illustrated option buttons appear. The child's choice determines the next color stop.

**Round 4 — "Far Future: The Color Lives On":** On the fruit bowl path, the brown spotty banana becomes compost and GREEN sprouts push up — color has come full circle from green to green. On the freezer path, the dark frozen banana is mashed and baked into GOLDEN BROWN banana bread — a final warm color transformation. Both paths celebrate how the property continues changing.

#### Step 4: Celebration

**AI says:** (grand, awestruck) "Time Shifter... are you ready? Look at what we built together! *ding ding ding!* Your banana's ENTIRE color story — from the very first green all the way to {green again / golden bread}! Let's see the whole timeline..."

(dramatic pause — 2 seconds)

(proud narration) "It started as a teeny tiny GREEN flower in a hot jungle... then it was a chubby GREEN bunch hanging in the sunshine... then it sailed across the ocean, slowly turning GREENISH-YELLOW... then it arrived in YOUR kitchen, bright YELLOW — that's what you photographed!... then YOU chose — {fruit bowl / freezer}... and it became {golden-brown with spots / dark outside, golden bread}! ONE banana. SO many colors. Every color change happened for a REASON!"

**Child responses:**

1. (Ideal) "Wow!" / "So many colors!" / "We went through all the colors!"
2. (Unexpected) "Can we do it again?" / "What about a different banana?"
3. (No response) Child watches the screen with wide eyes.

**AI follow-up:**

1. (beaming) "SO many colors in one little banana! You shifted through time and watched every single change. YOU saw the whole color story!"
2. (excited) "You want to see MORE color stories? That's what great Time Shifters do! But first — look at this incredible timeline you built!"
3. (wait 3s) (warm) "Pretty incredible, right? All those colors, all those changes, all in one banana. That's YOUR color timeline!"

**Screen:** Full COLOR TIMELINE stretching left to right with five stops: (1) green flower/jungle — "3 MONTHS AGO," (2) green banana bunch — "6 WEEKS AGO," (3) ship/greenish-yellow — "2 WEEKS AGO," (4) kitchen/bright yellow with "YOU ARE HERE" and child's photo — "TODAY," (5) future scene with chosen color — "FUTURE." Glowing gradient line connects all stops shifting from green through yellow to brown/golden. "THE COLOR TIMELINE" header with each letter a different color. Confetti in green, yellow, and brown.

#### Step 5: Closing + IB Concepts

**AI says:** (warm, reflective) "You are officially a Time Shifter! You took ONE little property — the color yellow — and followed it through time. And you saw something incredible: this banana CHANGED color at every single stop. Green... green... yellowish... yellow... {brown-spotted / dark-then-golden}. That's the power of Change — nothing stays the same color forever, and every color is part of the story!"

"And you know what else? Every color change happened for a REASON. The sunshine made the flower grow green. The cool ship air made the green turn yellow. {The warm kitchen made the yellow get spots. / The freezer made the skin go dark.} YOUR choice decided which color came next! That's called Causation — when one thing MAKES another thing change. Pretty amazing for one banana and one incredible Time Shifter!"

**Child responses:**

1. (Ideal) "Yeah!" / "I'm a Time Shifter!" / "Change is cool!"
2. (Unexpected) "What about other things?" / "Can I shift a different color?"
3. (No response) Child looks at the screen.

**AI follow-up:**

1. (warm closing) "The best Time Shifter I've ever met! Next time you see something — a leaf, a puddle, even your shoes — you can wonder: what color WAS it before? What color will it be NEXT? See you next time, Time Shifter!"
2. (encouraging) "Great idea! Everything around you has a color that changes over time. You can be a Time Shifter for ANYTHING. See you on the next shift!"
3. (wait 3s) (gentle closing) "Every single thing around you has properties that change over time. You helped this banana tell its color story. See you next time, Time Shifter!"

**Screen:** "TIME SHIFTER" badge centered with colorful dial shape shifting through green-yellow-brown. "Change" and "Causation" in large hand-drawn lettering. "Change" has green-to-yellow-to-brown gradient animation. "Causation" has illustrated arrows: sunshine -> green growth, cool air -> yellow shift, choice -> future color. Miniaturized color timeline at bottom. Confetti in green, yellow, and brown. Warm chime.
