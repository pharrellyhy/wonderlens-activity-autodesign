## Trivia Game

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Trivia Game |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | focus (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | memory_trail |

### B. Activity Overview

**1. Brief Description**

The child answers short memory or knowledge questions and receives a simple explanation.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `remember` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child has just explored a topic and can answer short fact or memory questions.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Trivia Game. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the trivia game player role, notices the starter cue, or names something connected to the first answer.
2. (Unexpected) Child asks for another game, starts the echo or recall before the Trivia Game mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Trivia Game title/trigger card without taking the trivia game player role yet.

**AI follow-up:**

1. Name the trivia game player role, connect it to the starter cue, and preview the first echo or recall.
2. Acknowledge the request, return to the Trivia Game promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Trivia Game role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the echo or recall loop for Trivia Game or asks for the easiest version.
2. (Unexpected) Child tries to skip the first answer, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Trivia Game rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Trivia Game loop as AI prompt, child echo or recall, saved token, and show the first response slot.
2. Keep the rule tied to the first answer, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Trivia Game rule in one sentence and ask for yes, a point, or the first chance to echo or recall the prompt.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `trivia_reward_board_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If stateful reward display is unavailable, use verbal encouragement only and do not claim stars are being added.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child answers short memory or knowledge questions and receives a simple explanation. Ask the child to echo or recall in the first small turn.

**Example AI line:** "Let us start: The child answers short memory or knowledge questions and receives a simple explanation. What is your first try?"

**Child responses:**

1. (Ideal) The child repeats, remembers, or answers the first answer prompt closely enough to keep the memory loop going.
2. (Unexpected) Child changes the first answer word/fact, guesses randomly, or turns the echo into unrelated talk.
3. (No response) Child listens to the first answer prompt without echoing, answering, or choosing a smaller repeat.

**AI follow-up:**

1. Repeat back the remembered part, mark the memory token, and cue the next echo or recall.
2. Slow the first answer into smaller pieces, accept a partial recall, and ask for just the next word or sound.
3. [wait 2s] Say the first answer prompt in two short beats, then invite the child to copy one beat.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `trivia_reward_board_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If stateful reward display is unavailable, use verbal encouragement only and do not claim stars are being added.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second remember turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child repeats, remembers, or answers the short explanation follow-up prompt closely enough to keep the memory loop going.
2. (Unexpected) Child changes the short explanation follow-up word/fact, guesses randomly, or turns the echo into unrelated talk.
3. (No response) Child listens to the short explanation follow-up prompt without echoing, answering, or choosing a smaller repeat.

**AI follow-up:**

1. Repeat back the remembered part, mark the memory token, and cue the next echo or recall.
2. Slow the short explanation follow-up into smaller pieces, accept a partial recall, and ask for just the next word or sound.
3. [wait 2s] Say the short explanation follow-up prompt in two short beats, then invite the child to copy one beat.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `trivia_reward_board_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If stateful reward display is unavailable, use verbal encouragement only and do not claim stars are being added.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child repeats, remembers, or answers the remembered fact prompt closely enough to keep the memory loop going.
2. (Unexpected) Child changes the remembered fact word/fact, guesses randomly, or turns the echo into unrelated talk.
3. (No response) Child listens to the remembered fact prompt without echoing, answering, or choosing a smaller repeat.

**AI follow-up:**

1. Repeat back the remembered part, mark the memory token, and cue the next echo or recall.
2. Slow the remembered fact into smaller pieces, accept a partial recall, and ask for just the next word or sound.
3. [wait 2s] Say the remembered fact prompt in two short beats, then invite the child to copy one beat.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `trivia_reward_board_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If stateful reward display is unavailable, use verbal encouragement only and do not claim stars are being added.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the remembered fact changed the Trivia Game board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Trivia Game payoff or ignores how the saved echo or recall turns connect.
3. (No response) Child watches the Trivia Game reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's echo or recall turns, name one concrete saved token, and invite a short reflection.
2. Hold the Trivia Game reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Trivia Game board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Connection. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Trivia Game moment, asks to play again, or watches the trivia game recap badge.
2. (Unexpected) Child shifts topic before the recap names the echo or recall skill or Form and Connection.
3. (No response) Child stays on the Trivia Game recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same remember mechanic and the trivia game frame.
2. Close Trivia Game first, name the practiced echo or recall, and then offer one next-round seed.
3. [wait 2s] Read the Trivia Game badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `remember`, focal attribute `trivia_game`, and next-step hint.
