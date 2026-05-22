## Would You Rather

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Would You Rather |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | observation (primary), observation, language expression |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The child chooses between two playful options and explains the preference or tradeoff.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `compare` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Conversation break, story reflection, or choice-making activity.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Would You Rather. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the would you rather player role, notices the starter cue, or names something connected to the first preference.
2. (Unexpected) Child asks for another game, starts the comparison choice before the Would You Rather mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Would You Rather title/trigger card without taking the would you rather player role yet.

**AI follow-up:**

1. Name the would you rather player role, connect it to the starter cue, and preview the first comparison choice.
2. Acknowledge the request, return to the Would You Rather promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Would You Rather role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the comparison choice loop for Would You Rather or asks for the easiest version.
2. (Unexpected) Child tries to skip the first preference, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Would You Rather rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Would You Rather loop as AI prompt, child comparison choice, saved token, and show the first response slot.
2. Keep the rule tied to the first preference, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Would You Rather rule in one sentence and ask for yes, a point, or the first chance to compare the visible options.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child chooses between two playful options and explains the preference or tradeoff. Ask the child to compare and choose in the first small turn.

**Example AI line:** "Let us start: The child chooses between two playful options and explains the preference or tradeoff. What is your first try?"

**Child responses:**

1. (Ideal) The child compares the visible options for the first preference and chooses or explains one.
2. (Unexpected) Child responds to only one side of the first preference, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the first preference options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the first preference, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the first preference, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second compare turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child compares the visible options for the tradeoff change and chooses or explains one.
2. (Unexpected) Child responds to only one side of the tradeoff change, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the tradeoff change options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the tradeoff change, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the tradeoff change, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child compares the visible options for the favorite reason and chooses or explains one.
2. (Unexpected) Child responds to only one side of the favorite reason, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the favorite reason options without choosing, pointing, or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the favorite reason, then ask for left/right or this/that.
3. [wait 2s] Name one difference in the favorite reason, model a choice, and invite one point or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the favorite reason changed the Would You Rather board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Would You Rather payoff or ignores how the saved comparison choice turns connect.
3. (No response) Child watches the Would You Rather reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's comparison choice turns, name one concrete saved token, and invite a short reflection.
2. Hold the Would You Rather reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Would You Rather board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Perspective. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Would You Rather moment, asks to play again, or watches the would you rather recap badge.
2. (Unexpected) Child shifts topic before the recap names the comparison choice skill or Form and Perspective.
3. (No response) Child stays on the Would You Rather recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same compare mechanic and the would you rather frame.
2. Close Would You Rather first, name the practiced comparison choice, and then offer one next-round seed.
3. [wait 2s] Read the Would You Rather badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `compare`, focal attribute `would_you_rather`, and next-step hint.
