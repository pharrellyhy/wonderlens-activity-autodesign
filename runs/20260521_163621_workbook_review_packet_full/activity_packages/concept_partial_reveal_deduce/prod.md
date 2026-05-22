## Partial Reveal Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Partial Reveal Guess |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Causation |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | logical_reasoning (primary), observation, language expression |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The screen shows one distinctive part of an animal or object, and the child guesses the whole thing from visible clues.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `deduce` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child photographs an animal toy, animal picture, or enters partial-reveal guessing mode.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Partial Reveal Guess. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the picture clue detective role, notices the starter cue, or names something connected to the first visible clue.
2. (Unexpected) Child asks for another game, starts the clue guess before the Partial Reveal Guess mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Partial Reveal Guess title/trigger card without taking the picture clue detective role yet.

**AI follow-up:**

1. Name the picture clue detective role, connect it to the starter cue, and preview the first clue guess.
2. Acknowledge the request, return to the Partial Reveal Guess promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Partial Reveal Guess role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the clue guess loop for Partial Reveal Guess or asks for the easiest version.
2. (Unexpected) Child tries to skip the first visible clue, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Partial Reveal Guess rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Partial Reveal Guess loop as AI prompt, child clue guess, saved token, and show the first response slot.
2. Keep the rule tied to the first visible clue, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Partial Reveal Guess rule in one sentence and ask for yes, a point, or the first chance to make a clue-based guess.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `partial_reveal_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The screen shows one distinctive part of an animal or object, and the child guesses the whole thing from visible clues. Ask the child to use clues to infer in the first small turn.

**Example AI line:** "Let us start: The screen shows one distinctive part of an animal or object, and the child guesses the whole thing from visible clues. What is your first try?"

**Child responses:**

1. (Ideal) The child uses the first visible clue to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the first visible clue, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the first visible clue clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, reveal whether that clue fits, and set up the next evidence step.
2. Name the clue in the first visible clue, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Point to one visible clue for the first visible clue, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `partial_reveal_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second deduce turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child uses the second revealed clue to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the second revealed clue, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the second revealed clue clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, reveal whether that clue fits, and set up the next evidence step.
2. Name the clue in the second revealed clue, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Point to one visible clue for the second revealed clue, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `partial_reveal_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child uses the final whole-object guess to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the final whole-object guess, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the final whole-object guess clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, reveal whether that clue fits, and set up the next evidence step.
2. Name the clue in the final whole-object guess, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Point to one visible clue for the final whole-object guess, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `partial_reveal_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the final whole-object guess changed the Partial Reveal Guess board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Partial Reveal Guess payoff or ignores how the saved clue guess turns connect.
3. (No response) Child watches the Partial Reveal Guess reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's clue guess turns, name one concrete saved token, and invite a short reflection.
2. Hold the Partial Reveal Guess reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Partial Reveal Guess board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Causation. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Partial Reveal Guess moment, asks to play again, or watches the partial reveal guess recap badge.
2. (Unexpected) Child shifts topic before the recap names the clue guess skill or Form and Causation.
3. (No response) Child stays on the Partial Reveal Guess recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same deduce mechanic and the partial reveal guess frame.
2. Close Partial Reveal Guess first, name the practiced clue guess, and then offer one next-round seed.
3. [wait 2s] Read the Partial Reveal Guess badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `deduce`, focal attribute `partial_reveal_guess`, and next-step hint.
