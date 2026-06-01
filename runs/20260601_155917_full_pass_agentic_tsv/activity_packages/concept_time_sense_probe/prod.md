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

**Runtime AI instruction:** Open from the Time Sense Challenge starter cue, name the child as time sense challenge player, and preview the first time prediction turn.

**Example AI line:** "Time Sense Challenge starts now. You are the time sense challenge player; I will help one time prediction turn at a time."

**Child responses:**

1. (Ideal) The child accepts the time sense challenge player role, notices the starter cue, or names something connected to the first time guess.
2. (Unexpected) Child asks for another game, starts the plan or prediction before the Time Sense Challenge mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Time Sense Challenge title/trigger card without taking the time sense challenge player role yet.

**AI follow-up:**

1. Name the time sense challenge player role, connect it to the starter cue, and preview the first plan or prediction.
2. Acknowledge the request, return to the Time Sense Challenge promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Time Sense Challenge role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one time prediction cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the plan or prediction loop for Time Sense Challenge or asks for the easiest version.
2. (Unexpected) Child tries to skip the first time guess, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Time Sense Challenge rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Time Sense Challenge loop as AI prompt, child plan or prediction, saved token, and show the first response slot.
2. Keep the rule tied to the first time guess, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Time Sense Challenge rule in one sentence and ask for yes, a point, or the first chance to make a plan or prediction.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the active time prediction cue.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child predicts when a short amount of time has passed, then checks the result. Ask the child to predict or plan in the first small turn.

**Example AI line:** "Let us start: The child predicts when a short amount of time has passed, then checks the result. Try the first time prediction now."

**Child responses:**

1. (Ideal) The child makes a plan or prediction for the first time guess and accepts that it can be checked or imagined next.
2. (Unexpected) Child treats the first time guess as a fixed answer, jumps past the check, or proposes a plan outside the pretend setup.
3. (No response) Child looks at the first time guess choices without making a prediction or plan.

**AI follow-up:**

1. Record the prediction, say what would make it true, and show how the next step will check or play it out.
2. Keep the pretend setup, narrow the first time guess to two possible outcomes, and ask which one might happen.
3. [wait 2s] Model "I think this will happen because.." for the first time guess, then ask for one guess or choice.

**Screen:** Shows the active round token, child response slot, and time prediction cue. No prebuilt asset is required; show progress tokens and the active time prediction cue.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second predict turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child makes a plan or prediction for the timer check and accepts that it can be checked or imagined next.
2. (Unexpected) Child treats the timer check as a fixed answer, jumps past the check, or proposes a plan outside the pretend setup.
3. (No response) Child looks at the timer check choices without making a prediction or plan.

**AI follow-up:**

1. Record the prediction, say what would make it true, and show how the next step will check or play it out.
2. Keep the pretend setup, narrow the timer check to two possible outcomes, and ask which one might happen.
3. [wait 2s] Model "I think this will happen because.." for the timer check, then ask for one guess or choice.

**Screen:** Shows the active round token, child response slot, and time prediction cue. No prebuilt asset is required; show progress tokens and the active time prediction cue.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your time prediction turns?"

**Child responses:**

1. (Ideal) The child makes a plan or prediction for the new prediction strategy and accepts that it can be checked or imagined next.
2. (Unexpected) Child treats the new prediction strategy as a fixed answer, jumps past the check, or proposes a plan outside the pretend setup.
3. (No response) Child looks at the new prediction strategy choices without making a prediction or plan.

**AI follow-up:**

1. Record the prediction, say what would make it true, and show how the next step will check or play it out.
2. Keep the pretend setup, narrow the new prediction strategy to two possible outcomes, and ask which one might happen.
3. [wait 2s] Model "I think this will happen because.." for the new prediction strategy, then ask for one guess or choice.

**Screen:** Shows the active round token, child response slot, and time prediction cue. No prebuilt asset is required; show progress tokens and the active time prediction cue.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your time prediction turns are saved: we started Time Sense Challenge, practiced time prediction, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the new prediction strategy changed the Time Sense Challenge board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Time Sense Challenge payoff or ignores how the saved plan or prediction turns connect.
3. (No response) Child watches the Time Sense Challenge reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's plan or prediction turns, name one concrete saved token, and invite a short reflection.
2. Hold the Time Sense Challenge reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Time Sense Challenge board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Causation. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Time Sense Challenge moment, asks to play again, or watches the time sense challenge recap badge.
2. (Unexpected) Child shifts topic before the recap names the plan or prediction skill or Form and Causation.
3. (No response) Child stays on the Time Sense Challenge recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same predict mechanic and the time sense challenge frame.
2. Close Time Sense Challenge first, name the practiced plan or prediction, and then offer one next-round seed.
3. [wait 2s] Read the Time Sense Challenge badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `predict`, focal attribute `time_sense_challenge`, and next-step hint.
