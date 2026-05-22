## Travel Planner

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Travel Planner |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Causation |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | prediction (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | prediction_lab |

### B. Activity Overview

**1. Brief Description**

The child helps plan a pretend trip by choosing what to pack, how to travel, and what might happen.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `predict` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child asks about a place, weather, vehicle, animal habitat, or character journey.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Travel Planner. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the pretend trip planner role, notices the starter cue, or names something connected to the pack choice.
2. (Unexpected) Child asks for another game, starts the plan or prediction before the Travel Planner mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Travel Planner title/trigger card without taking the pretend trip planner role yet.

**AI follow-up:**

1. Name the pretend trip planner role, connect it to the starter cue, and preview the first plan or prediction.
2. Acknowledge the request, return to the Travel Planner promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Travel Planner role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the plan or prediction loop for Travel Planner or asks for the easiest version.
2. (Unexpected) Child tries to skip the pack choice, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Travel Planner rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Travel Planner loop as AI prompt, child plan or prediction, saved token, and show the first response slot.
2. Keep the rule tied to the pack choice, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Travel Planner rule in one sentence and ask for yes, a point, or the first chance to make a plan or prediction.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `travel_planning_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the planning conversation by voice only.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child helps plan a pretend trip by choosing what to pack, how to travel, and what might happen. Ask the child to predict or plan in the first small turn.

**Example AI line:** "Let us start: The child helps plan a pretend trip by choosing what to pack, how to travel, and what might happen. What is your first try?"

**Child responses:**

1. (Ideal) The child makes a plan or prediction for the pack choice and accepts that it can be checked or imagined next.
2. (Unexpected) Child treats the pack choice as a fixed answer, jumps past the check, or proposes a plan outside the pretend setup.
3. (No response) Child looks at the pack choice choices without making a prediction or plan.

**AI follow-up:**

1. Record the prediction, say what would make it true, and show how the next step will check or play it out.
2. Keep the pretend setup, narrow the pack choice to two possible outcomes, and ask which one might happen.
3. [wait 2s] Model "I think this will happen because.." for the pack choice, then ask for one guess or choice.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `travel_planning_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the planning conversation by voice only.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second predict turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child makes a plan or prediction for the transport or weather choice and accepts that it can be checked or imagined next.
2. (Unexpected) Child treats the transport or weather choice as a fixed answer, jumps past the check, or proposes a plan outside the pretend setup.
3. (No response) Child looks at the transport or weather choice choices without making a prediction or plan.

**AI follow-up:**

1. Record the prediction, say what would make it true, and show how the next step will check or play it out.
2. Keep the pretend setup, narrow the transport or weather choice to two possible outcomes, and ask which one might happen.
3. [wait 2s] Model "I think this will happen because.." for the transport or weather choice, then ask for one guess or choice.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `travel_planning_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the planning conversation by voice only.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child makes a plan or prediction for the what might happen on the trip and accepts that it can be checked or imagined next.
2. (Unexpected) Child treats the what might happen on the trip as a fixed answer, jumps past the check, or proposes a plan outside the pretend setup.
3. (No response) Child looks at the what might happen on the trip choices without making a prediction or plan.

**AI follow-up:**

1. Record the prediction, say what would make it true, and show how the next step will check or play it out.
2. Keep the pretend setup, narrow the what might happen on the trip to two possible outcomes, and ask which one might happen.
3. [wait 2s] Model "I think this will happen because.." for the what might happen on the trip, then ask for one guess or choice.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `travel_planning_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the planning conversation by voice only.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the what might happen on the trip changed the Travel Planner board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Travel Planner payoff or ignores how the saved plan or prediction turns connect.
3. (No response) Child watches the Travel Planner reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's plan or prediction turns, name one concrete saved token, and invite a short reflection.
2. Hold the Travel Planner reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Travel Planner board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Causation. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Travel Planner moment, asks to play again, or watches the travel planner recap badge.
2. (Unexpected) Child shifts topic before the recap names the plan or prediction skill or Form and Causation.
3. (No response) Child stays on the Travel Planner recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same predict mechanic and the travel planner frame.
2. Close Travel Planner first, name the practiced plan or prediction, and then offer one next-round seed.
3. [wait 2s] Read the Travel Planner badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `predict`, focal attribute `travel_planner`, and next-step hint.
