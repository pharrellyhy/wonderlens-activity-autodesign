## Guess in 10

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Guess in 10 |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Causation |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | logical_reasoning (primary), observation, language expression |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The AI gives clues one by one, and the child guesses an animal or object from the evidence.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `deduce` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child photographs an animal toy, animal picture, or enters guessing mode.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Guess in 10. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the guess in 10 player role, notices the starter cue, or names something connected to the first clue guess.
2. (Unexpected) Child asks for another game, starts the clue guess before the Guess in 10 mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Guess in 10 title/trigger card without taking the guess in 10 player role yet.

**AI follow-up:**

1. Name the guess in 10 player role, connect it to the starter cue, and preview the first clue guess.
2. Acknowledge the request, return to the Guess in 10 promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Guess in 10 role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the clue guess loop for Guess in 10 or asks for the easiest version.
2. (Unexpected) Child tries to skip the first clue guess, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Guess in 10 rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Guess in 10 loop as AI prompt, child clue guess, saved token, and show the first response slot.
2. Keep the rule tied to the first clue guess, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Guess in 10 rule in one sentence and ask for yes, a point, or the first chance to make a clue-based guess.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `guess_reference_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, the AI continues with voice clues and encouragement and must not claim the screen is showing a picture.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The AI gives clues one by one, and the child guesses an animal or object from the evidence. Ask the child to use clues to infer in the first small turn.

**Example AI line:** "Let us start: The AI gives clues one by one, and the child guesses an animal or object from the evidence. What is your first try?"

**Child responses:**

1. (Ideal) The child uses the first clue guess to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the first clue guess, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the first clue guess clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, reveal whether that clue fits, and set up the next evidence step.
2. Name the clue in the first clue guess, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Point to one visible clue for the first clue guess, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `guess_reference_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, the AI continues with voice clues and encouragement and must not claim the screen is showing a picture.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second deduce turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child uses the new clue revision to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the new clue revision, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the new clue revision clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, reveal whether that clue fits, and set up the next evidence step.
2. Name the clue in the new clue revision, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Point to one visible clue for the new clue revision, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `guess_reference_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, the AI continues with voice clues and encouragement and must not claim the screen is showing a picture.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child uses the final evidence guess to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the final evidence guess, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the final evidence guess clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, reveal whether that clue fits, and set up the next evidence step.
2. Name the clue in the final evidence guess, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Point to one visible clue for the final evidence guess, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `guess_reference_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, the AI continues with voice clues and encouragement and must not claim the screen is showing a picture.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the final evidence guess changed the Guess in 10 board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Guess in 10 payoff or ignores how the saved clue guess turns connect.
3. (No response) Child watches the Guess in 10 reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's clue guess turns, name one concrete saved token, and invite a short reflection.
2. Hold the Guess in 10 reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Guess in 10 board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Causation. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Guess in 10 moment, asks to play again, or watches the guess in 10 recap badge.
2. (Unexpected) Child shifts topic before the recap names the clue guess skill or Form and Causation.
3. (No response) Child stays on the Guess in 10 recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same deduce mechanic and the guess in 10 frame.
2. Close Guess in 10 first, name the practiced clue guess, and then offer one next-round seed.
3. [wait 2s] Read the Guess in 10 badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `deduce`, focal attribute `guess_in_10`, and next-step hint.
