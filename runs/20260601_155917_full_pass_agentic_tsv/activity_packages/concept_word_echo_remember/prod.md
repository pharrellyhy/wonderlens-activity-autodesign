## Word Echo Practice

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Word Echo Practice |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | focus (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | memory_trail |

### B. Activity Overview

**1. Brief Description**

The AI says a simple word or phrase and the child repeats it back in a playful echo round.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `remember` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child enters language-practice mode, asks what an object is called, or photographs a familiar object whose name can be repeated safely.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Word Echo Practice. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the echo player role, notices the starter cue, or names something connected to the first echo word.
2. (Unexpected) Child asks for another game, starts the echo or recall before the Word Echo Practice mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Word Echo Practice title/trigger card without taking the echo player role yet.

**AI follow-up:**

1. Name the echo player role, connect it to the starter cue, and preview the first echo or recall.
2. Acknowledge the request, return to the Word Echo Practice promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Word Echo Practice role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the echo or recall loop for Word Echo Practice or asks for the easiest version.
2. (Unexpected) Child tries to skip the first echo word, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Word Echo Practice rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Word Echo Practice loop as AI prompt, child echo or recall, saved token, and show the first response slot.
2. Keep the rule tied to the first echo word, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Word Echo Practice rule in one sentence and ask for yes, a point, or the first chance to echo or recall the prompt.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `word_echo_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the activity voice-only and do not claim the screen is showing a word.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The AI says a simple word or phrase and the child repeats it back in a playful echo round. Ask the child to echo or recall in the first small turn.

**Example AI line:** "Let us start: The AI says a simple word or phrase and the child repeats it back in a playful echo round. What is your first try?"

**Child responses:**

1. (Ideal) The child repeats, remembers, or answers the first echo word prompt closely enough to keep the memory loop going.
2. (Unexpected) Child changes the first echo word word/fact, guesses randomly, or turns the echo into unrelated talk.
3. (No response) Child listens to the first echo word prompt without echoing, answering, or choosing a smaller repeat.

**AI follow-up:**

1. Repeat back the remembered part, mark the memory token, and cue the next echo or recall.
2. Slow the first echo word into smaller pieces, accept a partial recall, and ask for just the next word or sound.
3. [wait 2s] Say the first echo word prompt in two short beats, then invite the child to copy one beat.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `word_echo_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the activity voice-only and do not claim the screen is showing a word.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second remember turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child repeats, remembers, or answers the echo variation prompt closely enough to keep the memory loop going.
2. (Unexpected) Child changes the echo variation word/fact, guesses randomly, or turns the echo into unrelated talk.
3. (No response) Child listens to the echo variation prompt without echoing, answering, or choosing a smaller repeat.

**AI follow-up:**

1. Repeat back the remembered part, mark the memory token, and cue the next echo or recall.
2. Slow the echo variation into smaller pieces, accept a partial recall, and ask for just the next word or sound.
3. [wait 2s] Say the echo variation prompt in two short beats, then invite the child to copy one beat.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `word_echo_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the activity voice-only and do not claim the screen is showing a word.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child repeats, remembers, or answers the remembered echo pair prompt closely enough to keep the memory loop going.
2. (Unexpected) Child changes the remembered echo pair word/fact, guesses randomly, or turns the echo into unrelated talk.
3. (No response) Child listens to the remembered echo pair prompt without echoing, answering, or choosing a smaller repeat.

**AI follow-up:**

1. Repeat back the remembered part, mark the memory token, and cue the next echo or recall.
2. Slow the remembered echo pair into smaller pieces, accept a partial recall, and ask for just the next word or sound.
3. [wait 2s] Say the remembered echo pair prompt in two short beats, then invite the child to copy one beat.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `word_echo_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, run the activity voice-only and do not claim the screen is showing a word.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the remembered echo pair changed the Word Echo Practice board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Word Echo Practice payoff or ignores how the saved echo or recall turns connect.
3. (No response) Child watches the Word Echo Practice reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's echo or recall turns, name one concrete saved token, and invite a short reflection.
2. Hold the Word Echo Practice reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Word Echo Practice board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Connection. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Word Echo Practice moment, asks to play again, or watches the word echo practice recap badge.
2. (Unexpected) Child shifts topic before the recap names the echo or recall skill or Form and Connection.
3. (No response) Child stays on the Word Echo Practice recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same remember mechanic and the word echo practice frame.
2. Close Word Echo Practice first, name the practiced echo or recall, and then offer one next-round seed.
3. [wait 2s] Read the Word Echo Practice badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `remember`, focal attribute `word_echo_practice`, and next-step hint.
