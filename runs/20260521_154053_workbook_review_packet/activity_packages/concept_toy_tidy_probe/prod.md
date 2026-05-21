## Toy Tidy Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Toy Tidy Challenge |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | classification (grouping by a rule), logical reasoning (using evidence), organization (arranging by purpose) |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child starts from a toy area, accepts a short tidy-up mission, tidies for a limited time, and then confirms or shows the after state.

**2. Educational Purpose (KUD)**

- **K (Know):** Tidy-up can start with one small group such as wheels, blocks, soft toys, or books.
- **U (Understand):** Form helps sort what belongs together, and Connection links small actions to a cleaner space.
- **D (Do):** Accept a tidy mission, move one group during a short timer, confirm progress, and name one next place for leftovers.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. No displayed asset is required; progress is represented with simple in-session prompt and recap state.

**4. Typical Scenario**

Trigger: A parent starts tidy mode near visible toys or a toy area. The AI uses child/caregiver confirmation for progress and does not claim full-room before/after verification.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a toy tidy challenge mission. You are the Tidy Sort Captain. We will do one small tidy sprint, then check what changed. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. We will pick one toy group, tidy for a short timer, and celebrate effort."
2. [flexible] "I can make it smaller. One toy or one basket is enough."
3. [wait 2s] [gentle] "I will start with the easiest version."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Tidy Sort Captain rule: choose one toy group, tidy while I give simple tips, then tell me or show me what changed."

**Child responses:**

1. (Ideal) Child confirms the role or starts round one.
2. (Unexpected) Child needs materials, space, asset help, or a simpler choice.
3. (No response) Child listens without starting.

**AI follow-up:**

1. [encouraging] "Yes. That is our first saved step."
2. [scaffolded] "We can use the fallback: voice-only, self-report, caregiver help, or pause if setup is not safe."
3. [wait 2s] [modeling] "Try one small answer first."

**Screen:** Shows the role badge and first action card. No displayed asset is required; progress is represented with simple in-session prompt and recap state.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Tidy Mission:**

**AI says:** [round-1 guide] "Round 1: look at the toy area and pick one small group to tidy first: cars, blocks, soft toys, or books."

**Child responses:**

1. (Ideal) "Cars." / "Blocks."
2. (Unexpected) No toys nearby.
3. (No response) No response.

**AI follow-up:**

1. [specific] "Cars is a clear first group. Timer token 1 is ready."
2. [redirect] "We can use any safe visible objects or pause tidy mode."
3. [wait 2s] [gentle hint] "Pick one group: cars, blocks, soft toys."

**Screen:** A two-minute tidy timer appears when state is supported; fallback is a voice countdown. No before/after verification claim.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 2 -- Tidy During The Timer:**

**AI says:** [round-2 guide] "Round 2: start moving that group to its home. I will give two tiny tips while you work: put the same kind together, then check the floor for one more."

**Child responses:**

1. (Ideal) Child moves toys or says "Cars in the basket."
2. (Unexpected) Child mixes blocks and cars.
3. (No response) Child self-reports only.

**AI follow-up:**

1. [specific] "Cars in basket matches your mission. Effort token 2 is saved."
2. [redirect] "Mixed pile happens. Choose one car first, then one block later."
3. [wait 2s] [gentle hint] "Move one item or say one thing you moved."

**Screen:** Timer ring moves forward. Bin 1 fills by child/caregiver confirmation; state chip says self-reported if needed.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 3 -- Confirm The After State:**

**AI says:** [round-3 guide] "Round 3: timer done. Tell me or show me what changed. What toy group looks tidier now, and what is one next place for leftovers?"

**Child responses:**

1. (Ideal) "Cars are in the basket. Blocks go shelf."
2. (Unexpected) Room still messy.
3. (No response) No answer.

**AI follow-up:**

1. [specific] "Cars in basket is real progress. Blocks to shelf is the next tidy step."
2. [redirect] "We do not need perfect cleanup. We record one honest change and one next step."
3. [wait 2s] [gentle hint] "Say one thing that changed, or ask a grown-up to confirm."

**Screen:** Before/after area shows "child/caregiver confirmed" unless visual evidence is supported. Map shows completed group and next group, not a full-room cleanup claim.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your tidy sprint made: one toy group has a home, and one next group is ready. Which part did you work hardest on?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Toy Tidy Challenge: a cleanup map grouped by the child's sorting rule. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Form and Connection today. You used your own sort action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Tidy Sort Captain badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `toy_tidy`, asset/fallback note when relevant, and one next-step hint.
