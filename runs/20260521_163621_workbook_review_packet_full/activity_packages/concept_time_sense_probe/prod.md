## Time Sense Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Time Sense Challenge |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Causation |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | prediction (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | prediction_lab |

### B. Activity Overview

**1. Brief Description**

The child predicts when a short amount of time has passed, then checks the result.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `predict` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child can sit safely and make a short estimate such as ten seconds or one minute.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Time Sense Challenge. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts, asks what to do, or names a related object or idea.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Confirm the role and preview the first action without turning it into a quiz.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child confirms the rule or asks for a smaller version.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Offer the smallest safe version and keep the source play frame intact.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child predicts when a short amount of time has passed, then checks the result.. Ask the child to predict or plan in the first small turn.

**Example AI line:** "Let us start: The child predicts when a short amount of time has passed, then checks the result. What is your first try?"

**Child responses:**

1. (Ideal) The child gives the first source-aligned action.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Confirm the action and name how it matches the source rule.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second predict turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child repeats the same mechanic with a variation.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Connect the variation back to the same play frame.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child recaps or reacts.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Summarize the child action and source-specific payoff.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child reacts, names a favorite turn, or asks to revise one part.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Tie the reveal directly to the child action and invite one short reflection.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Causation. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child says again, names a favorite part, or quietly watches the recap.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Offer a next-time variation that keeps the same source mechanic.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Recap badge lists title, mechanic `predict`, focal attribute `time_sense_challenge`, and next-step hint.
