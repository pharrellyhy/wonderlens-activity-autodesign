## Time Sense Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Time Sense Challenge |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Causation and Change |
| Related Concepts | evidence, choice, progress, reflection |
| ATL Skills Focus | prediction (commit before reveal), logical reasoning (using evidence), focus (listening and turn-taking) |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child locks a short time prediction before the reveal, compares early/late/close feedback, then tries a better estimate using the first result.

**2. Educational Purpose (KUD)**

- **K (Know):** A time guess is strongest when the child commits before the reveal and compares early, late, or close.
- **U (Understand):** Causation connects the child's waiting strategy to the result, and Change supports a better second estimate.
- **D (Do):** Lock a short prediction, reveal the timer result, adjust strategy, and compare the two guesses without shame.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. No displayed asset is required; progress is represented with simple in-session prompt and recap state.

**4. Typical Scenario**

Trigger: A child can sit safely for a ten-second challenge. The AI gives a clear start signal, records the child's stop guess, reveals the elapsed result, and keeps the second estimate low-pressure.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a time sense challenge mission. You are the Time Guesser. We will do 3 small turns, and each one changes the ending. Ready?"

**Child responses:**

1. (Ideal) "Ready." / starts the setup.
2. (Unexpected) "What do I do?" / wants a different theme.
3. (No response) Child looks at the prompt or waits.

**AI follow-up:**

1. [focused] "Great. I will show the first safe step and wait for you."
2. [flexible] "I can make it smaller. You can answer with one word, a point, a movement, or a spoken choice."
3. [wait 2s] [gentle] "I will start with the easiest version."

**Screen:** Shows title, setup cue, safety/fallback chip, and 3 empty progress slots.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Time Guesser rule: predict when ten seconds have passed. I only save what you choose, say, show, or self-report."

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

**Round 1 -- Make a short guess:**

**AI says:** [round-1 guide] "Round 1: predict when ten seconds have passed."

**Child responses:**

1. (Ideal) "I will say stop."
2. (Unexpected) Wants a long timer
3. (No response) No response

**AI follow-up:**

1. [specific] "Good. Your guess is locked before the timer."
2. [redirect] "Let us keep it short: ten seconds is safer for this game."
3. [wait 2s] [gentle hint] "Say ready, then guess stop."

**Screen:** Timer state shows hidden count and a locked guess badge.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 2 -- Check the result:**

**AI says:** [round-2 guide] "Round 2: compare the guess with the timer result."

**Child responses:**

1. (Ideal) "I was early."
2. (Unexpected) Argues the timer is wrong
3. (No response) No response

**AI follow-up:**

1. [specific] "Early is useful evidence."
2. [redirect] "The timer is our check. We use it to improve the next guess."
3. [wait 2s] [gentle hint] "Was it early, late, or close?"

**Screen:** Reveal shows early/late/close without ranking or shame.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
**Round 3 -- Try a better estimate:**

**AI says:** [round-3 guide] "Round 3: use the first result to make a second prediction."

**Child responses:**

1. (Ideal) "I will wait longer."
2. (Unexpected) Randomly shouts stop
3. (No response) No response

**AI follow-up:**

1. [specific] "Waiting longer uses your evidence."
2. [redirect] "Try one calm breath before stop."
3. [wait 2s] [gentle hint] "Take one breath, then guess."

**Screen:** Second result appears beside first; strategy note is saved.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: two time predictions and one better-estimate strategy. Which part feels most like yours?"

**Child responses:**

1. (Ideal) Child reacts or names a favorite part.
2. (Unexpected) Child wants to revise, stop, or change theme.
3. (No response) Child watches the reveal.

**AI follow-up:**

1. [proud recap] "You made that happen by doing each turn in order."
2. [honest repair] "We can revise only if the product state allows it; otherwise I save this version as your report."
3. [wait 2s] [soft recap] "I will point to each saved turn so the result makes sense."

**Screen:** Shows the specific payoff for Time Sense Challenge: two time predictions and one better-estimate strategy. Resolved contract chips remain visible for reviewer traceability.

#### Step 5: Closing + IB Concepts

**AI says:** [warm close] "You practiced Causation and Change today. You used your own predict action to make the result."

**Child responses:**

1. (Ideal) "Again!" / names a favorite part.
2. (Unexpected) "That was hard." / wants another theme.
3. (No response) Child watches the recap badge.

**AI follow-up:**

1. [next-step invitation] "Next time we can keep the rule and change the theme."
2. [validating] "Hard still counts. You finished a real mission."
3. [wait 2s] [gentle goodbye] "Your Time Guesser badge is saved."

**Screen:** Recap badge shows the 3-turn trail, focal attribute `time_sense`, asset/fallback note when relevant, and one next-step hint.
