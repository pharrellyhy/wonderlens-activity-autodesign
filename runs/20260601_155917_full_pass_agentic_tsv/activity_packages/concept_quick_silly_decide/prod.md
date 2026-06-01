## Quick and Silly Questions

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Quick and Silly Questions |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | logical_reasoning (primary), observation, language expression |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

The child answers very short playful choice questions during a transition or warm-up.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `decide` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Light transition, waiting moment, or warm-up conversation.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Quick and Silly Questions. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the quick and silly questions player role, notices the starter cue, or names something connected to the first playful choice.
2. (Unexpected) Child asks for another game, starts the choice before the Quick and Silly Questions mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Quick and Silly Questions title/trigger card without taking the quick and silly questions player role yet.

**AI follow-up:**

1. Name the quick and silly questions player role, connect it to the starter cue, and preview the first choice.
2. Acknowledge the request, return to the Quick and Silly Questions promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Quick and Silly Questions role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the choice loop for Quick and Silly Questions or asks for the easiest version.
2. (Unexpected) Child tries to skip the first playful choice, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Quick and Silly Questions rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Quick and Silly Questions loop as AI prompt, child choice, saved token, and show the first response slot.
2. Keep the rule tied to the first playful choice, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Quick and Silly Questions rule in one sentence and ask for yes, a point, or the first chance to make a choice.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `quick_silly_countdown_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If countdown UI is unavailable, ask the quick questions by voice only and do not claim a timer is on screen.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child answers very short playful choice questions during a transition or warm-up. Ask the child to choose and respond in the first small turn.

**Example AI line:** "Let us start: The child answers very short playful choice questions during a transition or warm-up. What is your first try?"

**Child responses:**

1. (Ideal) The child makes the first playful choice choice and accepts the result of that decision.
2. (Unexpected) Child avoids the first playful choice choice, adds an unavailable option, or answers outside the offered decision frame.
3. (No response) Child looks at the first playful choice options without choosing one.

**AI follow-up:**

1. Confirm the chosen option, state the consequence for the first playful choice, and move the decision token forward.
2. Keep the decision frame, remove the unavailable option, and ask for one of the visible choices for the first playful choice.
3. [wait 2s] Read the visible choices for the first playful choice, model one choice sentence, and ask for a tap or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `quick_silly_countdown_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If countdown UI is unavailable, ask the quick questions by voice only and do not claim a timer is on screen.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second decide turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child makes the changed silly choice choice and accepts the result of that decision.
2. (Unexpected) Child avoids the changed silly choice choice, adds an unavailable option, or answers outside the offered decision frame.
3. (No response) Child looks at the changed silly choice options without choosing one.

**AI follow-up:**

1. Confirm the chosen option, state the consequence for the changed silly choice, and move the decision token forward.
2. Keep the decision frame, remove the unavailable option, and ask for one of the visible choices for the changed silly choice.
3. [wait 2s] Read the visible choices for the changed silly choice, model one choice sentence, and ask for a tap or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `quick_silly_countdown_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If countdown UI is unavailable, ask the quick questions by voice only and do not claim a timer is on screen.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child makes the favorite silly answer choice and accepts the result of that decision.
2. (Unexpected) Child avoids the favorite silly answer choice, adds an unavailable option, or answers outside the offered decision frame.
3. (No response) Child looks at the favorite silly answer options without choosing one.

**AI follow-up:**

1. Confirm the chosen option, state the consequence for the favorite silly answer, and move the decision token forward.
2. Keep the decision frame, remove the unavailable option, and ask for one of the visible choices for the favorite silly answer.
3. [wait 2s] Read the visible choices for the favorite silly answer, model one choice sentence, and ask for a tap or word.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `quick_silly_countdown_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If countdown UI is unavailable, ask the quick questions by voice only and do not claim a timer is on screen.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the favorite silly answer changed the Quick and Silly Questions board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Quick and Silly Questions payoff or ignores how the saved choice turns connect.
3. (No response) Child watches the Quick and Silly Questions reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's choice turns, name one concrete saved token, and invite a short reflection.
2. Hold the Quick and Silly Questions reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Quick and Silly Questions board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Responsibility. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Quick and Silly Questions moment, asks to play again, or watches the quick silly questions recap badge.
2. (Unexpected) Child shifts topic before the recap names the choice skill or Form and Responsibility.
3. (No response) Child stays on the Quick and Silly Questions recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same decide mechanic and the quick silly questions frame.
2. Close Quick and Silly Questions first, name the practiced choice, and then offer one next-round seed.
3. [wait 2s] Read the Quick and Silly Questions badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `decide`, focal attribute `quick_silly_questions`, and next-step hint.
