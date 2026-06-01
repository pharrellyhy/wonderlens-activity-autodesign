## Word Build Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Word Build Guess |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | logical_reasoning (primary), observation, language expression |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

The child chooses letters or answers clues to reveal a word step by step.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `decide` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Product has a text-aware word puzzle mode with parent approval for reading level.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Word Build Guess starter cue, name the child as word build guess player, and preview the first letter or clue choice turn.

**Example AI line:** "Word Build Guess starts now. You are the word build guess player; I will help one word-reveal choice turn at a time."

**Child responses:**

1. (Ideal) The child accepts the word build guess player role, notices the starter cue, or names something connected to the first clue or letter.
2. (Unexpected) Child asks for another game, starts the choice before the Word Build Guess mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Word Build Guess title/trigger card without taking the word build guess player role yet.

**AI follow-up:**

1. Name the word build guess player role, connect it to the starter cue, and preview the first choice.
2. Acknowledge the request, return to the Word Build Guess promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Word Build Guess role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one word-reveal choice cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the choice loop for Word Build Guess or asks for the easiest version.
2. (Unexpected) Child tries to skip the first clue or letter, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Word Build Guess rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Word Build Guess loop as AI prompt, child choice, saved token, and show the first response slot.
2. Keep the rule tied to the first clue or letter, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Word Build Guess rule in one sentence and ask for yes, a point, or the first chance to make a choice.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `word_growth_ui_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If word state is unsupported, block at Phase 0 or run a voice-only clue riddle with no letter UI claims.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child chooses letters or answers clues to reveal a word step by step. Ask the child to choose and respond in the first small turn.

**Example AI line:** "Let us start: The child chooses letters or answers clues to reveal a word step by step. Try the first letter or clue choice now."

**Child responses:**

1. (Ideal) The child makes the first clue or letter choice and accepts the result of that decision.
2. (Unexpected) Child avoids the first clue or letter choice, adds an unavailable option, or answers outside the offered decision frame.
3. (No response) Child looks at the first clue or letter options without choosing one.

**AI follow-up:**

1. Confirm the chosen option, state the consequence for the first clue or letter, and move the decision token forward.
2. Keep the decision frame, remove the unavailable option, and ask for one of the visible choices for the first clue or letter.
3. [wait 2s] Read the visible choices for the first clue or letter, model one choice sentence, and ask for a tap or word.

**Screen:** Shows the active round token, child response slot, and word-reveal choice cue. Use `word_growth_ui_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If word state is unsupported, block at Phase 0 or run a voice-only clue riddle with no letter UI claims.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second decide turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child makes the next letter or clue choice and accepts the result of that decision.
2. (Unexpected) Child avoids the next letter or clue choice, adds an unavailable option, or answers outside the offered decision frame.
3. (No response) Child looks at the next letter or clue options without choosing one.

**AI follow-up:**

1. Confirm the chosen option, state the consequence for the next letter or clue, and move the decision token forward.
2. Keep the decision frame, remove the unavailable option, and ask for one of the visible choices for the next letter or clue.
3. [wait 2s] Read the visible choices for the next letter or clue, model one choice sentence, and ask for a tap or word.

**Screen:** Shows the active round token, child response slot, and word-reveal choice cue. Use `word_growth_ui_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If word state is unsupported, block at Phase 0 or run a voice-only clue riddle with no letter UI claims.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your word-reveal choice turns?"

**Child responses:**

1. (Ideal) The child makes the final word reveal choice and accepts the result of that decision.
2. (Unexpected) Child avoids the final word reveal choice, adds an unavailable option, or answers outside the offered decision frame.
3. (No response) Child looks at the final word reveal options without choosing one.

**AI follow-up:**

1. Confirm the chosen option, state the consequence for the final word reveal, and move the decision token forward.
2. Keep the decision frame, remove the unavailable option, and ask for one of the visible choices for the final word reveal.
3. [wait 2s] Read the visible choices for the final word reveal, model one choice sentence, and ask for a tap or word.

**Screen:** Shows the active round token, child response slot, and word-reveal choice cue. Use `word_growth_ui_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If word state is unsupported, block at Phase 0 or run a voice-only clue riddle with no letter UI claims.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your word-reveal choice turns are saved: we started Word Build Guess, practiced word-reveal choice, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the final word reveal changed the Word Build Guess board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Word Build Guess payoff or ignores how the saved choice turns connect.
3. (No response) Child watches the Word Build Guess reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's choice turns, name one concrete saved token, and invite a short reflection.
2. Hold the Word Build Guess reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Word Build Guess board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Responsibility. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Word Build Guess moment, asks to play again, or watches the word build guess recap badge.
2. (Unexpected) Child shifts topic before the recap names the choice skill or Form and Responsibility.
3. (No response) Child stays on the Word Build Guess recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same decide mechanic and the word build guess frame.
2. Close Word Build Guess first, name the practiced choice, and then offer one next-round seed.
3. [wait 2s] Read the Word Build Guess badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `decide`, focal attribute `word_build_guess`, and next-step hint.
