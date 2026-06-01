## Flashcards

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Flashcards |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | counting (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child recognizes a picture card, names what they see, and answers one tiny follow-up.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `enumerate` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Parent selects a vocabulary, shape, color, animal, or object-recognition practice mode.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Flashcards starter cue, name the child as flashcards player, and preview the first picture-card naming turn.

**Example AI line:** "Flashcards starts now. You are the flashcards player; I will help one flashcard naming turn at a time."

**Child responses:**

1. (Ideal) The child accepts the flashcards player role, notices the starter cue, or names something connected to the picture-card name.
2. (Unexpected) Child asks for another game, starts the counting or naming step before the Flashcards mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Flashcards title/trigger card without taking the flashcards player role yet.

**AI follow-up:**

1. Name the flashcards player role, connect it to the starter cue, and preview the first counting or naming step.
2. Acknowledge the request, return to the Flashcards promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Flashcards role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one flashcard naming cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the counting or naming step loop for Flashcards or asks for the easiest version.
2. (Unexpected) Child tries to skip the picture-card name, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Flashcards rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Flashcards loop as AI prompt, child counting or naming step, saved token, and show the first response slot.
2. Keep the rule tied to the picture-card name, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Flashcards rule in one sentence and ask for yes, a point, or the first chance to count or name the target set.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `generic_flashcard_library_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a photographed object or voice-only recognition prompt and do not claim the screen shows a card.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child recognizes a picture card, names what they see, and answers one tiny follow-up. Ask the child to count or identify in the first small turn.

**Example AI line:** "Let us start: The child recognizes a picture card, names what they see, and answers one tiny follow-up. Name the first picture card now."

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the picture-card name.
2. (Unexpected) Child guesses the picture-card name without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the picture-card name display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the picture-card name, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the picture-card name, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and flashcard naming cue. Use `generic_flashcard_library_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a photographed object or voice-only recognition prompt and do not claim the screen shows a card.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second enumerate turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the one visible feature.
2. (Unexpected) Child guesses the one visible feature without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the one visible feature display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the one visible feature, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the one visible feature, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and flashcard naming cue. Use `generic_flashcard_library_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a photographed object or voice-only recognition prompt and do not claim the screen shows a card.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your flashcard naming turns?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the tiny follow-up answer.
2. (Unexpected) Child guesses the tiny follow-up answer without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the tiny follow-up answer display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the tiny follow-up answer, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the tiny follow-up answer, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and flashcard naming cue. Use `generic_flashcard_library_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, use a photographed object or voice-only recognition prompt and do not claim the screen shows a card.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your flashcard naming turns are saved: we started Flashcards, practiced flashcard naming, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the tiny follow-up answer changed the Flashcards board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Flashcards payoff or ignores how the saved counting or naming step turns connect.
3. (No response) Child watches the Flashcards reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's counting or naming step turns, name one concrete saved token, and invite a short reflection.
2. Hold the Flashcards reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Flashcards board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Flashcards moment, asks to play again, or watches the flashcards recap badge.
2. (Unexpected) Child shifts topic before the recap names the counting or naming step skill or Form.
3. (No response) Child stays on the Flashcards recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same enumerate mechanic and the flashcards frame.
2. Close Flashcards first, name the practiced counting or naming step, and then offer one next-round seed.
3. [wait 2s] Read the Flashcards badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `enumerate`, focal attribute `flashcards`, and next-step hint.
