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

The child chooses a cleanup rule, groups or names matching objects, and turns a messy set into a small map of what belongs together and what still needs a home.

**2. Educational Purpose (KUD)**

- **K (Know):** A tidy group uses a visible or meaningful rule such as wheels, blocks, soft toys, or books.
- **U (Understand):** Form helps sort what belongs together, and Connection links the child's rule to a cleaner next step.
- **D (Do):** Choose a tidy rule, move or name matching objects, self-report progress, and name one next place for leftovers.

**3. Design Highlight**

This package is generated under `minimum_unblock_allowed`, so former blockers are visible but resolved. No displayed asset is required; progress is represented with simple in-session prompt and recap state.

**4. Typical Scenario**

Trigger: A parent starts tidy mode near cars, blocks, soft toys, books, or household objects. The AI uses child/caregiver confirmation for progress and does not claim full-room before/after verification.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**AI says:** [warm invitation] "I have a toy tidy challenge mission. You are the Tidy Sort Captain. We will do 3 small turns, and each one changes the ending. Ready?"

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
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.

#### Step 2: Role And Rules

**AI says:** [clear guide tone] "Tidy Sort Captain rule: pick one sorting rule such as soft things, wheels, or blocks. I only save what you choose, say, show, or self-report."

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

**Round 1 -- Choose a tidy rule:**

**AI says:** [round-1 guide] "Round 1: pick one sorting rule such as soft things, wheels, or blocks."

**Child responses:**

1. (Ideal) "Cars go together."
2. (Unexpected) No toys nearby
3. (No response) No response

**AI follow-up:**

1. [specific] "Cars together is a clear rule."
2. [redirect] "We can use any safe visible objects or pause tidy mode."
3. [wait 2s] [gentle hint] "Pick one group: cars, blocks, soft toys."

**Screen:** Three empty bin labels appear; no before/after verification claim.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 2 -- Sort the first group:**

**AI says:** [round-2 guide] "Round 2: move or name the first group and explain the rule."

**Child responses:**

1. (Ideal) "Cars in the basket."
2. (Unexpected) Child mixes blocks and cars
3. (No response) Child self-reports only

**AI follow-up:**

1. [specific] "Cars in basket matches your rule."
2. [redirect] "Mixed pile happens. Choose one car first."
3. [wait 2s] [gentle hint] "Show or say one item that belongs."

**Screen:** Bin 1 fills by child/caregiver confirmation; state chip says self-reported if needed.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
**Round 3 -- Finish and check:**

**AI says:** [round-3 guide] "Round 3: name what is left and where it belongs next."

**Child responses:**

1. (Ideal) "Blocks go shelf."
2. (Unexpected) Room still messy
3. (No response) No answer

**AI follow-up:**

1. [specific] "Blocks to shelf is the next tidy step."
2. [redirect] "We do not need perfect cleanup. We record one next step honestly."
3. [wait 2s] [gentle hint] "Say one thing left."

**Screen:** Map shows completed group and next group, not a full-room cleanup claim.

> RESOLVED BLOCKER: Approved minimum state contract: per-round choices persist during the session, with clear reset/resume behavior and a stateless fallback.
> RESOLVED BLOCKER: Approved minimum evidence policy: caregiver or child self-report is acceptable; the AI does not claim unsupported visual verification.
#### Step 4: Magic Moment

**AI says:** [reveal tone] "Here is what your turns made: a cleanup map grouped by the child's sorting rule. Which part feels most like yours?"

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
