# Partial Reveal Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Partial Reveal Guess |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Causation |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | logical_reasoning, observation, language_expression |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The screen reveals one distinctive part at a time while the child makes clue-based guesses. Runtime responses must not name or confirm the hidden answer before the final answer is verified.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Partial Reveal Guess.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `deduce` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the activity-specific role, repeated action, ideal/unexpected/no-response branches, and honest visual fallback behavior.

**4. Typical Scenario**

The child plays Partial Reveal Guess with partial_reveal_guess as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Rules

**Runtime AI instruction:** Explain only the Partial Reveal Guess rule and name any required asset or honest fallback. Do not ask the child to make the first guess here; the first action prompt belongs to Round 1.

**Example AI line:** "Rule: I share a clue, you make one guess, and we light up one step of the mystery for each turn."

**Child responses:**

1. (Ideal) The child understands that each guess must use the visible clue and that the answer stays hidden until the final reveal.
2. (Unexpected) Child tries to skip the first visible clue, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Partial Reveal Guess rule strip without responding.

**AI follow-up:**

1. Restate the Partial Reveal Guess loop as visible clue, clue-based guess, and one mystery step lit up.
2. Keep the rule tied to the first visible clue, name the supported fallback, and do not count any response yet.
3. [wait 2s] Read the Partial Reveal Guess rule in one sentence, then continue to Round 1.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `partial_reveal_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Multi-Round Core Loop

**Round 1 -- First Visible Clue:**

**Runtime AI instruction:** Preserve the asset promise: show only the first visible clue. Ask for a maybe-guess from that clue, and do not name, confirm, or switch the hidden answer.

**Example AI line:** "First clue: look at the visible part. What could this hidden animal be?"

**Child responses:**

1. (Ideal) The child uses the first visible clue to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the first visible clue, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the first visible clue clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, save the maybe-guess, and set up the next evidence step without confirming the answer.
2. Name the clue in the first visible clue, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Name one visible clue from the first visible clue, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `partial_reveal_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Second Visible Clue:**

**Runtime AI instruction:** Keep the asset promise: show only the second visible clue. Ask whether the guess changes or gets stronger without naming or confirming the hidden answer.

**Example AI line:** "Now there is one more clue. Does that change your guess, or make it feel stronger?"

**Child responses:**

1. (Ideal) The child uses the second revealed clue to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the second revealed clue, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the second revealed clue clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, save the maybe-guess, and set up the next evidence step without confirming the answer.
2. Name the clue in the second revealed clue, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Name one visible clue from the second revealed clue, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `partial_reveal_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Final Reveal Guess:**

**Runtime AI instruction:** Keep the asset promise, show the final reveal card, and ask for the final answer plus one clue reason without saying the answer first.

**Example AI line:** "The final reveal card is ready. What is your final answer, and which clue helped most?"

**Child responses:**

1. (Ideal) The child uses the final whole-object guess to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the final whole-object guess, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the final whole-object guess clue area without offering a maybe-guess.

**AI follow-up:**

1. Verify the final answer from the child's response, tie it to the visible clue, and then advance to the reveal.
2. Name the clue in the final whole-object guess, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Name one visible clue from the final whole-object guess, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `partial_reveal_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your choices filled the activity board: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the final whole-object guess changed the Partial Reveal Guess board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Partial Reveal Guess payoff or ignores how the saved clue guess turns connect.
3. (No response) Child watches the Partial Reveal Guess reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's clue guess turns, name one concrete saved turn, and invite a short reflection.
2. Hold the Partial Reveal Guess reveal, name the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Partial Reveal Guess board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Closing + IB Concepts

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

**Screen:** Recap badge lists title, mechanic `deduce`, focal attribute `partial_reveal_guess`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
