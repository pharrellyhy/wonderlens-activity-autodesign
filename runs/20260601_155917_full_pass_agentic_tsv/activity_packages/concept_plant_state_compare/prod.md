## Plant State Compare

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Plant State Compare |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, change, care, comparison |
| ATL Skills Focus | observation, language expression, reasoning from evidence |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The child photographs or discusses a plant with visible leaf/state evidence, compares states such as green, yellowing, damaged, blooming, or wilting, hears a simple state-change explanation, and chooses one gentle plant-care idea.

**2. Educational Purpose (KUD)**

- **K (Know):** Leaves and flowers can show visible states such as green, yellowing, damaged, blooming, or wilting.
- **U (Understand):** A visible plant state can give clues about change, but the AI should explain only likely, child-safe possibilities and avoid hidden health diagnosis.
- **D (Do):** Notice visible evidence, compare two states, explain what changed, and choose one simple care action such as checking light, water, or gentle leaf safety.

**3. Design Highlight**

The activity is a state-and-care comparison, not a generic compare game. Every turn starts from visible plant evidence and ends with a small explanation or care idea.

**4. Typical Scenario**

The child shows a houseplant or outdoor plant photo. The AI notices a green leaf, yellow leaf, damaged edge, bloom, or wilted stem, then helps the child compare what looks different and think of one gentle care step.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: Open from the child's plant photo or nearby plant and make the child a leaf-state detective who will compare visible plant states, not generic objects. Constraint: T1, 2-3 short sentences; do not diagnose hidden plant health or claim species-specific care unless supplied by mapping/caregiver. Tone: curious and gentle. Progress evidence: child names or points to one visible plant state such as green, yellow, damaged, blooming, or droopy. Branch behavior: if correct/engaged, mirror the exact visible clue and preview comparing; if wrong/off-topic, validate and bring attention back to a visible leaf/flower clue; if help/silence, offer two choices like green or yellow, and after two unproductive prompts allow a one-clue mini version. Frame/source guardrail: source frame is photo-based plant state-and-care comparison; screen keeps the plant photo/current state card visible with empty evidence tokens.

**Example AI line:** "I see a plant clue here. Are we looking at a green strong leaf, a yellow sleepy leaf, or a little damaged spot?"

**Child responses:**

1. (Ideal) The child says "yellow leaf," "green," "it is broken," points to a leaf, or confirms the plant photo.
2. (Unexpected) Child names a non-plant object, asks to compare toys, or says the plant is sick without visible evidence.
3. (No response) Child looks at the plant photo without naming or pointing to a state.

**AI follow-up:**

1. Save the named state as evidence token 1 and say the next job is to compare it with another visible state.
2. Reframe: "Let's only use what our eyes can see on the plant," then offer green/yellow/damaged as choices.
3. [wait 2s] Point/highlight one visible leaf area, model "I notice this leaf is yellow," and ask for "same or different?"

**Screen:** Shows the plant photo or "nearby plant" placeholder, a leaf-state detective badge, and three empty evidence tokens labeled Notice, Compare, Care.

#### Step 2: Role And Rules

**Runtime AI instruction:** Goal: Explain the loop: notice one plant state, compare it with another state, then pick one gentle care idea. Constraint: T1, 2-3 short sentences; keep care advice simple and conditional, such as "might need less/more water" or "ask a grown-up to check light." Tone: calm field-guide voice. Progress evidence: child agrees to compare or chooses a first visible state to start from. Branch behavior: if correct, start Round 1 with their state; if wrong/generic, restate that only visible plant clues count; if help/silence, give a yes/point option and after repeated silence run one narrated comparison then close gently. Frame/source guardrail: preserve photo/discussion plant frame; screen shows a rule strip with See, Compare, Care and never claims automatic plant diagnosis.

**Example AI line:** "Our rule is: see one plant clue, compare it with another clue, then choose one kind care idea. We only use what the leaf or flower shows us."

**Child responses:**

1. (Ideal) The child agrees, points to a leaf, or chooses "green," "yellow," "damaged," "flower," or "droopy."
2. (Unexpected) Child wants a generic before/after game, asks for exact plant species care, or gives invisible causes as facts.
3. (No response) Child watches the rule strip without confirming.

**AI follow-up:**

1. Move the chosen state into the first round slot.
2. Keep wording honest: "It might be about water or light, but we can only say what we see. Which visible clue should we compare?"
3. [wait 2s] Read the three rule words, ask for a point/yes, then offer to do one tiny example.

**Screen:** Rule strip shows See -> Compare -> Care, current plant photo remains visible, and a small "visible clues only" guardrail chip appears.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Green And Yellow Leaves:**

**Runtime AI instruction:** Goal: Ask the child to compare a green-looking leaf and a yellowing or pale leaf/state, then explain that leaf color can change when a plant is growing, aging, or not getting the right water/light. Constraint: T1, 2-3 short sentences; avoid definite diagnosis and avoid telling the child to water immediately without adult check. Tone: warm and wondering. Progress evidence: child identifies same/different color or says which leaf looks greener/yellower. Branch behavior: if correct, name the color evidence and give one likely-change explanation; if wrong, accept the attempt and contrast "green" versus "yellow/pale"; if help/silence, offer "green one or yellow one?" and save a modeled answer after two prompts. Frame/source guardrail: this beat must be about plant leaf states and simple care, not generic color comparison; screen highlights two visible state zones or fallback illustrated chips.

**Example AI line:** "This leaf looks greener, and this one looks more yellow. A yellow leaf can be an old leaf or a clue to ask a grown-up to check water or light."

**Child responses:**

1. (Ideal) The child says which leaf is green/yellow, says they are different, or points to the changed leaf.
2. (Unexpected) Child counts leaves, names a toy color, or says "it is dead" as a certainty.
3. (No response) Child looks between the two highlighted zones without choosing.

**AI follow-up:**

1. Save "color changed" as evidence and add the care idea "ask a grown-up to check water/light."
2. Rephrase: "Maybe, but we won't decide hidden health. We can say this leaf looks more yellow than that green one."
3. [wait 2s] Model "green here, yellow here," invite one point, then continue with the saved modeled comparison if needed.

**Screen:** Two highlights or chips labeled Green Leaf and Yellow Leaf, token 1 fills with "color clue," and a care bulb shows "check water/light with a grown-up."

**Round 2 -- Smooth And Damaged Leaves:**

**Runtime AI instruction:** Goal: Compare an intact/smooth leaf with a damaged, torn, spotted, or bitten-looking leaf and explain that leaves can change after bumps, weather, bugs, or drying. Constraint: T1, 2-3 short sentences; do not identify pests or disease from the image. Tone: careful and respectful of living things. Progress evidence: child names a damaged/smooth difference or points to the damaged edge/spot. Branch behavior: if correct, save the visible damage clue and suggest gentle care such as not pulling leaves and asking an adult before trimming; if wrong/off-topic, return to "edge, hole, spot, or smooth"; if help/silence, offer "smooth or bumpy/torn?" and allow exit after a modeled clue. Frame/source guardrail: compare visible plant damage/state only; screen keeps the damage highlight and care idea separate from diagnosis.

**Example AI line:** "This edge looks smooth, and this spot looks torn. A leaf can change after wind, bumps, or tiny nibblers, so our care idea is gentle hands."

**Child responses:**

1. (Ideal) The child says "broken," "hole," "smooth," "spot," or points to a damaged area.
2. (Unexpected) Child tries to pull the leaf, asks to find bugs, or names an unrelated damaged object.
3. (No response) Child watches the highlighted damage spot without responding.

**AI follow-up:**

1. Save "shape/damage clue" and praise careful looking.
2. Redirect safety: "We look with eyes and gentle hands. Which part looks smooth, and which part looks changed?"
3. [wait 2s] Model "this edge changed," ask for a point, then move on if still quiet.

**Screen:** Plant photo/drawing shows smooth and changed-area markers, token 2 fills with "edge/spot clue," and a gentle-hands icon appears.

**Round 3 -- Blooming, Drooping, Or Drying State:**

**Runtime AI instruction:** Goal: Help the child compare a flower/open/standing state with droopy, dry, or closed-looking evidence, then give one simple plant-care idea tied to the visible state. Constraint: T1, 2-3 short sentences; care idea must be cautious and adult-friendly, such as "check soil with a grown-up" or "move gently toward light if your family knows this plant likes it." Tone: encouraging and concrete. Progress evidence: child says what changed, chooses stronger/droopier, or repeats one care idea. Branch behavior: if correct, recap the state change and care idea; if wrong/generic, narrow to "open/closed, tall/droopy, wet/dry-looking"; if help/silence, offer two choices and then close with the evidence already collected. Frame/source guardrail: finish with state-change explanation plus care, not only a favorite choice; screen shows all evidence tokens and final care token.

**Example AI line:** "This flower looks open, but this stem looks droopy. That can be a clue to ask a grown-up to check the soil before giving water."

**Child responses:**

1. (Ideal) The child says "droopy," "flower open," "dry," "needs light/water maybe," or chooses a care step.
2. (Unexpected) Child says to pour lots of water, wants to pick the flower, or switches to naming colors only.
3. (No response) Child stays quiet on the final plant state.

**AI follow-up:**

1. Save "state change clue" and "care check" as the final token.
2. Keep care safe: "Maybe water, maybe light, so we ask a grown-up and check gently first."
3. [wait 2s] Offer "open or droopy?" then summarize the two prior clues if the child remains quiet.

**Screen:** Evidence board shows Color Clue, Edge/Spot Clue, State Change, and Care Check. No claim of automatic health detection is shown.

#### Step 4: Magic Moment

**Runtime AI instruction:** Goal: Reveal the child's plant detective board by linking each saved visible clue to one likely change and one gentle care idea. Constraint: T1, 2-3 short sentences; no new diagnosis, no species-specific promise. Tone: proud and thoughtful. Progress evidence: child recognizes a clue, repeats a care idea, or chooses a favorite state. Branch behavior: if correct, recap their exact clue; if wrong/off-topic, recap the visible evidence without correction pressure; if help/silence, read the board aloud and offer to finish. Frame/source guardrail: payoff must be state-and-care synthesis from the plant photo/discussion; screen shows saved evidence tokens, not generic progress.

**Example AI line:** "Your plant detective board says: color can change, edges can change, and droopy parts can be care clues. The kind care move is to check gently with a grown-up."

**Child responses:**

1. (Ideal) The child names favorite clue, repeats "check water/light," or points to a token.
2. (Unexpected) Child asks for exact plant diagnosis or wants to remove leaves.
3. (No response) Child watches the completed board.

**AI follow-up:**

1. Celebrate the specific clue and connect it to careful plant observation.
2. State the safe boundary: "We can notice clues, and a grown-up can decide exact care."
3. [wait 2s] Narrate the three tokens and proceed to closing.

**Screen:** Final detective board shows the original plant photo/fallback card, three evidence tokens, and one "gentle care check" badge.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Goal: Close by naming Form and Perspective through visible plant states and careful care choices. Constraint: T1, 2 short sentences; include one parent-reviewable recap of what the child compared. Tone: warm and complete. Progress evidence: child names one state, says goodbye, or accepts the badge. Branch behavior: if correct, echo their state; if wrong/off-topic, close with the evidence board; if help/silence, end gracefully without more demands. Frame/source guardrail: closing must mention plant state comparison and simple care guidance; screen shows recap badge with visible clues only.

**Example AI line:** "You practiced Form by seeing leaf states, and Perspective by thinking what the plant might need. Today you compared green/yellow/damaged clues and chose gentle care."

**Child responses:**

1. (Ideal) The child says a plant state, asks to check another plant, or watches the badge.
2. (Unexpected) Child shifts topic before the recap.
3. (No response) Child stays on the recap badge.

**AI follow-up:**

1. Offer next time: compare another plant leaf or flower state.
2. Close the plant activity first, then acknowledge the new topic.
3. [wait 2s] Read the badge and end.

**Screen:** Recap badge lists "Plant State Detective," mechanic `compare`, focal attribute `plant_state_compare`, and next hint "Find one green/yellow/damaged clue."
