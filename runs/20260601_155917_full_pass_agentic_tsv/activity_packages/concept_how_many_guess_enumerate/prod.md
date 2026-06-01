## How Many Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | How Many Guess |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | counting (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child estimates how many objects are visible, then counts together with the AI.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `enumerate` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Screen can show a small set of objects or the camera sees countable items.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: How Many Guess. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the how many guess player role, notices the starter cue, or names something connected to the first estimate.
2. (Unexpected) Child asks for another game, starts the counting or naming step before the How Many Guess mission is framed, or follows an unrelated topic.
3. (No response) Child watches the How Many Guess title/trigger card without taking the how many guess player role yet.

**AI follow-up:**

1. Name the how many guess player role, connect it to the starter cue, and preview the first counting or naming step.
2. Acknowledge the request, return to the How Many Guess promise, and offer the smallest supported first action.
3. [wait 2s] Point to the How Many Guess role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the counting or naming step loop for How Many Guess or asks for the easiest version.
2. (Unexpected) Child tries to skip the first estimate, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the How Many Guess rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the How Many Guess loop as AI prompt, child counting or naming step, saved token, and show the first response slot.
2. Keep the rule tied to the first estimate, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the How Many Guess rule in one sentence and ask for yes, a point, or the first chance to count or name the target set.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `how_many_count_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use real photographed countable items or voice-only counting and do not claim a card is displayed.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child estimates how many objects are visible, then counts together with the AI. Ask the child to count or identify in the first small turn.

**Example AI line:** "Let us start: The child estimates how many objects are visible, then counts together with the AI. What is your first try?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the first estimate.
2. (Unexpected) Child guesses the first estimate without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the first estimate display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the first estimate, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the first estimate, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `how_many_count_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use real photographed countable items or voice-only counting and do not claim a card is displayed.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second enumerate turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the count-together check.
2. (Unexpected) Child guesses the count-together check without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the count-together check display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the count-together check, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the count-together check, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `how_many_count_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use real photographed countable items or voice-only counting and do not claim a card is displayed.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the guess-versus-count recap.
2. (Unexpected) Child guesses the guess-versus-count recap without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the guess-versus-count recap display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the guess-versus-count recap, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the guess-versus-count recap, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `how_many_count_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use real photographed countable items or voice-only counting and do not claim a card is displayed.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the guess-versus-count recap changed the How Many Guess board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the How Many Guess payoff or ignores how the saved counting or naming step turns connect.
3. (No response) Child watches the How Many Guess reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's counting or naming step turns, name one concrete saved token, and invite a short reflection.
2. Hold the How Many Guess reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the How Many Guess board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite How Many Guess moment, asks to play again, or watches the how many guess recap badge.
2. (Unexpected) Child shifts topic before the recap names the counting or naming step skill or Form.
3. (No response) Child stays on the How Many Guess recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same enumerate mechanic and the how many guess frame.
2. Close How Many Guess first, name the practiced counting or naming step, and then offer one next-round seed.
3. [wait 2s] Read the How Many Guess badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `enumerate`, focal attribute `how_many_guess`, and next-step hint.
