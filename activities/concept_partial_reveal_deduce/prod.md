# Mystery Clue Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Mystery Clue Guess |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Causation |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | logical_reasoning, observation, language_expression |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The screen reveals one distinctive part at a time while the child makes clue-based guesses. Runtime responses must not name or confirm the hidden answer before the final reveal.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Mystery Clue Guess.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `deduce` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the activity-specific role, repeated action, ideal/unexpected/no-response branches, and honest visual fallback behavior.

**4. Typical Scenario**

The child plays Mystery Clue Guess with mystery_clue_guess as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Rules

**Runtime AI instruction:** Say exactly: "Each clue gets a maybe-guess. The answer waits for the final reveal." Do not ask a question here.

**Example AI line:** "We'll look at one mystery clue at a time. Make a maybe-guess for each clue."

**Child responses:**

1. (Ideal) The child understands that each guess must use the visible clue and that the answer stays hidden until the final reveal.
2. (Unexpected) Child tries to skip the first visible clue, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Mystery Clue Guess rule strip without responding.

**AI follow-up:**

1. Restate the Mystery Clue Guess loop as visible clue, clue-based guess, and one mystery step lit up.
2. Keep the rule tied to the first visible clue, name the supported fallback, and do not count any response yet.
3. [wait 2s] Read the Mystery Clue Guess rule in one sentence, then continue to Round 1.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `partial_reveal_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Multi-Round Core Loop

**Round 1 -- First Visible Clue:**

**Runtime AI instruction:** Say exactly: "Pointy ears. What could it be?" Do not add clues, name the answer, or confirm the guess.

**Example AI line:** "First clue: pointy ears. What could it maybe be?"

**Child responses:**

1. (Ideal) The child uses the first visible clue to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the first visible clue, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the first visible clue clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, save the maybe-guess, and set up the next evidence step without confirming the answer.
2. Repeat the pointy-ears clue only, then ask for one maybe-guess without saying the answer.
3. [wait 2s] Repeat "pointy ears" only, model a maybe-guess format, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `partial_reveal_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Second Visible Clue:**

**Runtime AI instruction:** Say exactly: "Paws or feet. Keep your guess or change it?" Do not add clues, name the answer, or confirm the guess.

**Example AI line:** "Second clue: paws or feet. What is your maybe-guess now?"

**Child responses:**

1. (Ideal) The child uses the second revealed clue to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the second revealed clue, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the second revealed clue clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, save the maybe-guess, and set up the next evidence step without confirming the answer.
2. Repeat the paws-or-feet clue only, then ask for one maybe-guess without saying the answer.
3. [wait 2s] Repeat "paws or feet" only, model a maybe-guess format, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `partial_reveal_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Final Reveal Guess:**

**Runtime AI instruction:** Say exactly: "Pointy ears and paws or feet. What is your final guess?" Do not add clues or say the answer first.

**Example AI line:** "Final guess time. Use pointy ears and paws or feet. What could it be?"

**Child responses:**

1. (Ideal) The child uses the final whole-object guess to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the final whole-object guess, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the final whole-object guess clue area without offering a maybe-guess.

**AI follow-up:**

1. Save the final guess, tie it to one visible clue, and then advance to the reveal.
2. Repeat the pointy-ears and paws-or-feet clues only, then ask for one final guess without saying the answer.
3. [wait 2s] Repeat both clues only, model a maybe-guess format, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `partial_reveal_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Magic Moment

**Runtime AI instruction:** Say exactly: "The answer is cat. Here is the big reveal." Name only shown clues. Do not say the child found it.

**Example AI line:** "Reveal: it was a cat. The pointy ears and paws were the clues."

**Child responses:**

1. (Ideal) The child notices how the final whole-object guess changed the Mystery Clue Guess board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Mystery Clue Guess payoff or ignores how the saved clue guess turns connect.
3. (No response) Child watches the Mystery Clue Guess reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the visible clues and the child's guess turns, then invite a short reflection.
2. Hold the Mystery Clue Guess reveal, name the visible clues that matter, and ask what changed because of them.
3. [wait 2s] Narrate one before/after change from the Mystery Clue Guess board, then ask which clue helped most.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Closing + IB Concepts

**Runtime AI instruction:** Say exactly: "You looked at parts and made careful guesses about the whole cat."

**Example AI line:** "You looked at parts and made careful guesses about the whole cat."

**Child responses:**

1. (Ideal) The child names a favorite Mystery Clue Guess moment, asks to play again, or watches the mystery clue recap badge.
2. (Unexpected) Child shifts topic before the recap names the clue guess skill or Form and Causation.
3. (No response) Child stays on the Mystery Clue Guess recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same deduce mechanic and the mystery clue frame.
2. Close Mystery Clue Guess first, name the practiced clue guess, and then offer one next-round seed.
3. [wait 2s] Read the Mystery Clue Guess badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `deduce`, focal attribute `partial_reveal_guess`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
