## Recognition Pop Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Recognition Pop Challenge |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | observation (noticing visible evidence), quantity comparison (same/different amount), language expression (naming and explaining) |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child compares a spoken target with visible cards, chooses the matching picture, explains one distractor, and completes a careful final match without punitive speed pressure.

**2. Educational Purpose (KUD)**

- **K (Know):** A target match uses visible evidence: same object, shape, color, or category cue.
- **U (Understand):** Form helps compare target and distractor details, and Perspective supports slowing down when a choice is uncertain.
- **D (Do):** Choose the matching picture, explain a distractor difference, make a careful final match, and review the evidence trail.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. Uses `recognition_challenge_cards_01` in `center_card_area`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

**4. Typical Scenario**

Trigger: The product can show a target card with simple distractors. The AI gives tap, point, or spoken-choice options and slows the game down if timing support is unavailable.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a recognition pop challenge mission. You are the Target Matcher. We will do 3 small turns, and each one changes the ending. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I will show the first safe step and wait for you."
2. [flexible] "I can make it smaller. You can answer with one word, a point, a movement, or a spoken choice."
3. [wait 2s] [gentle] "I will start with the easiest version."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Target Matcher rule: choose the picture that matches the spoken target. I only save what you choose, say, show, or self-report."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. Uses `recognition_challenge_cards_01` in `center_card_area`; fallback: Use the declared voice-only or self-report fallback and do not claim the missing asset, UI, or state is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Find the target:**

**AI says:** [round-1 guide] "Round 1: choose the picture that matches the spoken target."

**Child responses:**

1. (Ideal) "I tapped the apple."
2. (Unexpected) Taps a distractor
3. (No response) No response

**AI follow-up:**

1. [specific] "Apple matches the target. Slot one pops."
2. [redirect] "Close. Banana is food too, but the target is apple."
3. [wait 2s] [gentle hint] "Look for the apple shape/color."

**Screen:** Tap surface shows target + distractors and friendly pop feedback.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 2 -- Avoid the distractor:**

**AI says:** [round-2 guide] "Round 2: explain why a similar picture is not the target."

**Child responses:**

1. (Ideal) "Pear is not apple; different shape."
2. (Unexpected) Says all fruits count
3. (No response) No response

**AI follow-up:**

1. [specific] "Different shape is good comparison evidence."
2. [redirect] "Same category is true, but the target picture must match."
3. [wait 2s] [gentle hint] "Say same or different."

**Screen:** Distractor gets a gentle "not target" chip, no punitive whack imagery.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 3 -- Fast final match:**

**AI says:** [round-3 guide] "Round 3: make one quicker match with gentle pacing."

**Child responses:**

1. (Ideal) "There!"
2. (Unexpected) Rushed wrong tap
3. (No response) No response

**AI follow-up:**

1. [specific] "Quick and careful. Final match saved."
2. [redirect] "Speed is optional. Let us slow down and check the target."
3. [wait 2s] [gentle hint] "Find the one with the same outline."

**Screen:** Progress shows 3 friendly pops, not score pressure.

> RESOLVED BLOCKER: Approved minimum asset-display contract: listed asset IDs may be displayed with metadata and documented no-display fallback.
> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: three target matches with one distractor explanation. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Recognition Pop Challenge: three target matches with one distractor explanation. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Form and Perspective today. You used your own compare action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Target Matcher badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `recognition_pop`, asset/fallback note when relevant, and one next-step hint.
