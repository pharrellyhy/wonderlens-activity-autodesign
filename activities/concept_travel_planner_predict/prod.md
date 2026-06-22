# Travel Planner

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Travel Planner |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Causation |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | prediction, observation, language_expression |
| Experience Pillar | Discovery |
| Game Style | prediction_lab |

### B. Activity Overview

**1. Brief Description**

The child plans a pretend trip by choosing what to pack, how to travel, and what might happen.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Travel Planner.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `predict` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the activity-specific role, repeated action, ideal/unexpected/no-response branches, and honest visual fallback behavior.

**4. Typical Scenario**

The child plays Travel Planner with travel_planner as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open by naming the activity and child role and name the child's role in this activity.

**Example AI line:** "I have a small mission for us: Travel Planner. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the pretend trip planner role, notices the starter cue, or names something connected to the pack choice.
2. (Unexpected) Child asks for another game, starts the plan or prediction before the Travel Planner mission is framed, or follows an unrelated topic.
3. (No response) Child watches the opening Travel Planner moment without taking the pretend trip planner role yet.

**AI follow-up:**

1. Name the pretend trip planner role, connect it to the starter cue, and preview the first plan or prediction.
2. Acknowledge the request, return to the Travel Planner promise, and offer the smallest supported first action.
3. [wait 2s] Name the Travel Planner role and the first small plan, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens. Optional support asset: `intro_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I share a prompt, you try the activity, and we save one turn each time."

**Child responses:**

1. (Ideal) The child agrees to the plan or prediction loop for Travel Planner or asks for the easiest version.
2. (Unexpected) Child tries to skip the pack choice, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Travel Planner rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Travel Planner loop as AI prompt, child plan or prediction, saved turn, and show the first response slot.
2. Keep the rule tied to the pack choice, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Travel Planner rule in one sentence and ask for yes or the first chance to make a plan or prediction.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `travel_planning_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the planning conversation by voice only. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Sunny Place Packing Choice:**

**Runtime AI instruction:** Preserve the workbook promise: The child helps plan a pretend trip by choosing what to pack, how to travel, and what might happen. Ask the child to predict or plan in the first small turn.

**Example AI line:** "Let us start: The child helps plan a pretend trip by choosing what to pack, how to travel, and what might happen. What will you try first?"

**Child responses:**

1. (Ideal) The child makes a plan or prediction for the pack choice and accepts that it can be checked or imagined next.
2. (Unexpected) Child treats the pack choice as a fixed answer, jumps past the check, or proposes a plan outside the pretend setup.
3. (No response) Child looks at the pack choice choices without making a prediction or plan.

**AI follow-up:**

1. Record the prediction, say what would make it true, and show how the next step will check or play it out.
2. Keep the pretend setup, narrow the pack choice to two possible outcomes, and ask which one might happen.
3. [wait 2s] Model "I think this will happen because.." for the pack choice, then ask for one guess or choice.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `travel_planning_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the planning conversation by voice only. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Weather Change Plan:**

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

**Screen:** Shows the active round token, child response slot, and activity cue. Use `travel_planning_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the planning conversation by voice only. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Next Travel Event Prediction:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What changed after your turns, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child makes a plan or prediction for the what might happen on the trip and accepts that it can be checked or imagined next.
2. (Unexpected) Child treats the what might happen on the trip as a fixed answer, jumps past the check, or proposes a plan outside the pretend setup.
3. (No response) Child looks at the what might happen on the trip choices without making a prediction or plan.

**AI follow-up:**

1. Record the prediction, say what would make it true, and show how the next step will check or play it out.
2. Keep the pretend setup, narrow the what might happen on the trip to two possible outcomes, and ask which one might happen.
3. [wait 2s] Model "I think this will happen because.." for the what might happen on the trip, then ask for one guess or choice.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `travel_planning_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the planning conversation by voice only. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your choices filled the activity board: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the what might happen on the trip changed the Travel Planner board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Travel Planner payoff or ignores how the saved plan or prediction turns connect.
3. (No response) Child watches the Travel Planner reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's plan or prediction turns, name one concrete saved turn, and invite a short reflection.
2. Hold the Travel Planner reveal, name the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Travel Planner board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

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

**Screen:** Recap badge lists title, mechanic `predict`, focal attribute `travel_planner`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
