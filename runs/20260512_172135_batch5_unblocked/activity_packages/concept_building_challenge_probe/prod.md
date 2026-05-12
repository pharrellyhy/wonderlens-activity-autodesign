## Building Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Building Challenge |
| Activity Category | cat3 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Function and Change |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | creative thinking (making original choices), planning (sequencing steps), language expression (naming and explaining) |
| Experience Pillar | Creation |
| Game Style | inventor_workshop |

### B. Activity Overview

**1. Brief Description**

The child plans a safe build target, chooses available blocks or household materials, builds a base plus one useful feature, and explains what the structure can do.

**2. Educational Purpose (KUD)**

- **K (Know):** A simple build needs safe materials, a base, and one clear feature.
- **U (Understand):** Function helps each material do a job, and Change shows how a pile becomes a structure.
- **D (Do):** Choose materials, build one stable part, add a feature, and explain what the build can do.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `building_reference_cards_01` in `center_card_area`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

**4. Typical Scenario**

Trigger: A child has blocks, bricks, cups, or recycled materials within caregiver-approved reach. If materials are missing, the AI pauses or turns the build into a verbal plan instead of pretending a structure was verified.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a building challenge mission. You are the Build Planner. We will do 3 small turns, and each one changes the ending. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I will show the first safe step and wait for you."
2. [flexible] "I can make it smaller. You can answer with one word, a point, a movement, or a spoken choice."
3. [wait 2s] [gentle] "I will start with the easiest version."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Build Planner rule: choose blocks or household materials and make a stable base. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `building_reference_cards_01` in `center_card_area`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Choose the base:**

**AI says:** [round-1 guide] "Round 1: choose blocks or household materials and make a stable base."

**Child responses:**

1. (Ideal) "I used two blocks."
2. (Unexpected) No materials nearby
3. (No response) Child searches silently

**AI follow-up:**

1. [specific] "Two blocks can be the base. Slot one is saved."
2. [redirect] "Ask a grown-up for safe materials, or switch to a pretend build."
3. [wait 2s] [gentle hint] "Find one safe object or say pretend base."

**Screen:** If `building_reference_cards_01` is available, the reference card stays visible. Fallback: voice-only build cue with no card claim. Caregiver/material setup chip appears.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 2 -- Add a useful part:**

**AI says:** [round-2 guide] "Round 2: add one part that helps the build match the target."

**Child responses:**

1. (Ideal) "I made a roof."
2. (Unexpected) Build falls over
3. (No response) Child changes target

**AI follow-up:**

1. [specific] "A roof gives your build a job. Slot two is saved."
2. [redirect] "Falling is data. Make the base wider or call it a wobbly test."
3. [wait 2s] [gentle hint] "Choose one part: roof, bridge, wall, ramp."

**Screen:** Progress board shows base + added part, with self-report not visual verification.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 3 -- Show and explain:**

**AI says:** [round-3 guide] "Round 3: show the build and name what makes it stable or useful."

**Child responses:**

1. (Ideal) "It stands because it is wide."
2. (Unexpected) Child says AI should judge it
3. (No response) No answer

**AI follow-up:**

1. [specific] "Wide base is good evidence. I will record your explanation."
2. [redirect] "I cannot judge build quality from one photo. You tell me what works."
3. [wait 2s] [gentle hint] "Say: it stands because ___."

**Screen:** Finish slot shows child/caregiver confirmation and a no-assessment badge.

> RESOLVED BLOCKER: Approved minimum Cat3 contract: caregiver setup, material pacing, no-assessment fallback, and honest completion evidence are documented.
> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: a stable target build with base, useful part, and child explanation. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Building Challenge: a stable target build with base, useful part, and child explanation. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Function and Change today. You used your own build action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Build Planner badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `building_challenge`, asset/fallback note when relevant, and one next-step hint.
