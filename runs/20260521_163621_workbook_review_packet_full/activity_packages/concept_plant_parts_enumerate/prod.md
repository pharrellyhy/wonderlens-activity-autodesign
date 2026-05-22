## Plant Parts Explorer

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Plant Parts Explorer |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | counting (primary), observation, language expression |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child looks at a plant and identifies visible parts such as leaf, stem, flower, fruit, seed, or root.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `enumerate` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Uploaded or live photo clearly shows a plant with at least two visible parts.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Plant Parts Explorer. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the plant parts explorer player role, notices the starter cue, or names something connected to the first visible plant part.
2. (Unexpected) Child asks for another game, starts the counting or naming step before the Plant Parts Explorer mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Plant Parts Explorer title/trigger card without taking the plant parts explorer player role yet.

**AI follow-up:**

1. Name the plant parts explorer player role, connect it to the starter cue, and preview the first counting or naming step.
2. Acknowledge the request, return to the Plant Parts Explorer promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Plant Parts Explorer role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the counting or naming step loop for Plant Parts Explorer or asks for the easiest version.
2. (Unexpected) Child tries to skip the first visible plant part, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Plant Parts Explorer rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Plant Parts Explorer loop as AI prompt, child counting or naming step, saved token, and show the first response slot.
2. Keep the rule tied to the first visible plant part, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Plant Parts Explorer rule in one sentence and ask for yes, a point, or the first chance to count or name the target set.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child looks at a plant and identifies visible parts such as leaf, stem, flower, fruit, seed, or root. Ask the child to count or identify in the first small turn.

**Example AI line:** "Let us start: The child looks at a plant and identifies visible parts such as leaf, stem, flower, fruit, seed, or root. What is your first try?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the first visible plant part.
2. (Unexpected) Child guesses the first visible plant part without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the first visible plant part display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the first visible plant part, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the first visible plant part, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second enumerate turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the second plant part or location.
2. (Unexpected) Child guesses the second plant part or location without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the second plant part or location display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the second plant part or location, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the second plant part or location, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child counts, names, or checks the items required for the whole plant recap.
2. (Unexpected) Child guesses the whole plant recap without looking, counts unrelated items, or changes the target set.
3. (No response) Child looks at the whole plant recap display without saying a number, name, or first count.

**AI follow-up:**

1. Repeat the counted evidence, mark the number/name token, and show what set will be checked next.
2. Return attention to the target set for the whole plant recap, count one item aloud, and ask the child to continue.
3. [wait 2s] Point to the first item in the whole plant recap, say "one," and invite the child to say the next number or name.

**Screen:** Shows the active round token, child response slot, and source-intent cue. No prebuilt asset is required; show progress tokens and the current prompt.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the whole plant recap changed the Plant Parts Explorer board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Plant Parts Explorer payoff or ignores how the saved counting or naming step turns connect.
3. (No response) Child watches the Plant Parts Explorer reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's counting or naming step turns, name one concrete saved token, and invite a short reflection.
2. Hold the Plant Parts Explorer reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Plant Parts Explorer board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Plant Parts Explorer moment, asks to play again, or watches the plant parts explorer recap badge.
2. (Unexpected) Child shifts topic before the recap names the counting or naming step skill or Form.
3. (No response) Child stays on the Plant Parts Explorer recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same enumerate mechanic and the plant parts explorer frame.
2. Close Plant Parts Explorer first, name the practiced counting or naming step, and then offer one next-round seed.
3. [wait 2s] Read the Plant Parts Explorer badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `enumerate`, focal attribute `plant_parts_explorer`, and next-step hint.
