## Plant State Compare

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Plant State Compare |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | observation (primary), observation, language expression |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The child compares a plant's visible state, such as sprouting, blooming, wilting, dried, healthy, or fruiting.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `compare` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

A plant photo shows a clear state, such as blooming, wilting, dried, or after watering.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Plant State Compare. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the plant state compare player role, notices the starter cue, or names something connected to the first visible plant state.
2. (Unexpected) Child asks for another game, starts the comparison choice before the Plant State Compare mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Plant State Compare title/trigger card without taking the plant state compare player role yet.

**AI follow-up:**

1. Name the plant state compare player role, connect it to the starter cue, and preview the first comparison choice.
2. Acknowledge the request, return to the Plant State Compare promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Plant State Compare role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the comparison choice loop for Plant State Compare or asks for the easiest version.
2. (Unexpected) Child tries to skip the first visible plant state, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Plant State Compare rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Plant State Compare loop as AI prompt, child comparison choice, saved token, and show the first response slot.
2. Keep the rule tied to the first visible plant state, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Plant State Compare rule in one sentence and ask for yes, a point, or the first chance to compare the visible options.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child compares a plant's visible state, such as sprouting, blooming, wilting, dried, healthy, or fruiting. Ask the child to compare and choose in the first small turn.

**Example AI line:** "Let us start: The child compares a plant's visible state, such as sprouting, blooming, wilting, dried, healthy, or fruiting. What is your first try?"

**Child responses:**

1. (Ideal) The child compares the visible options for the first visible plant state and chooses or explains one.
2. (Unexpected) Child responds to only one side of the first visible plant state, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the first visible plant state options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the first visible plant state, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the first visible plant state, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second compare turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child compares the visible options for the second state comparison and chooses or explains one.
2. (Unexpected) Child responds to only one side of the second state comparison, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the second state comparison options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the second state comparison, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the second state comparison, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child compares the visible options for the state clue explanation and chooses or explains one.
2. (Unexpected) Child responds to only one side of the state clue explanation, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the state clue explanation options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the state clue explanation, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the state clue explanation, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the state clue explanation changed the Plant State Compare board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Plant State Compare payoff or ignores how the saved comparison choice turns connect.
3. (No response) Child watches the Plant State Compare reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's comparison choice turns, name one concrete saved token, and invite a short reflection.
2. Hold the Plant State Compare reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Plant State Compare board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Perspective. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Plant State Compare moment, asks to play again, or watches the plant state compare recap badge.
2. (Unexpected) Child shifts topic before the recap names the comparison choice skill or Form and Perspective.
3. (No response) Child stays on the Plant State Compare recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same compare mechanic and the plant state compare frame.
2. Close Plant State Compare first, name the practiced comparison choice, and then offer one next-round seed.
3. [wait 2s] Read the Plant State Compare badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `compare`, focal attribute `plant_state_compare`, and next-step hint.
