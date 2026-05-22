## Phoneme Treasure Hunt

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Phoneme Treasure Hunt |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | evidence_collection (primary), observation, language expression |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The AI introduces a target sound, then the child finds an object whose word starts with that sound.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `collect` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child enters language treasure-hunt mode or photographs an everyday object suitable for sound play.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Phoneme Treasure Hunt. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the sound treasure hunter role, notices the starter cue, or names something connected to the target sound and first object.
2. (Unexpected) Child asks for another game, starts the matching-item hunt before the Phoneme Treasure Hunt mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Phoneme Treasure Hunt title/trigger card without taking the sound treasure hunter role yet.

**AI follow-up:**

1. Name the sound treasure hunter role, connect it to the starter cue, and preview the first matching-item hunt.
2. Acknowledge the request, return to the Phoneme Treasure Hunt promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Phoneme Treasure Hunt role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the matching-item hunt loop for Phoneme Treasure Hunt or asks for the easiest version.
2. (Unexpected) Child tries to skip the target sound and first object, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Phoneme Treasure Hunt rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Phoneme Treasure Hunt loop as AI prompt, child matching-item hunt, saved token, and show the first response slot.
2. Keep the rule tied to the target sound and first object, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Phoneme Treasure Hunt rule in one sentence and ask for yes, a point, or the first chance to find or show one match.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `phoneme_letter_card_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the card is unavailable, the AI repeats the target sound by voice only and must not claim the screen is showing a letter.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The AI introduces a target sound, then the child finds an object whose word starts with that sound. Ask the child to find or match in the first small turn.

**Example AI line:** "Let us start: The AI introduces a target sound, then the child finds an object whose word starts with that sound. What is your first try?"

**Child responses:**

1. (Ideal) The child finds or names something that fits the target sound and first object and lets it become a collected token.
2. (Unexpected) Child offers something that does not match the target sound and first object, changes the hunt rule, or asks for credit without a find.
3. (No response) Child scans for the target sound and first object but does not name, point to, or show an item.

**AI follow-up:**

1. Name the matching evidence for the target sound and first object, add the token to the collection, and preview what changes next.
2. Keep the hunt rule visible, contrast one non-match with one allowed example, and ask for a safer match for the target sound and first object.
3. [wait 2s] Give one concrete example that would count for the target sound and first object, then ask the child to point, say, or show one.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `phoneme_letter_card_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the card is unavailable, the AI repeats the target sound by voice only and must not claim the screen is showing a letter.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second collect turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child finds or names something that fits the second object for the same sound and lets it become a collected token.
2. (Unexpected) Child offers something that does not match the second object for the same sound, changes the hunt rule, or asks for credit without a find.
3. (No response) Child scans for the second object for the same sound but does not name, point to, or show an item.

**AI follow-up:**

1. Name the matching evidence for the second object for the same sound, add the token to the collection, and preview what changes next.
2. Keep the hunt rule visible, contrast one non-match with one allowed example, and ask for a safer match for the second object for the same sound.
3. [wait 2s] Give one concrete example that would count for the second object for the same sound, then ask the child to point, say, or show one.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `phoneme_letter_card_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the card is unavailable, the AI repeats the target sound by voice only and must not claim the screen is showing a letter.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child finds or names something that fits the sound treasure recap and lets it become a collected token.
2. (Unexpected) Child offers something that does not match the sound treasure recap, changes the hunt rule, or asks for credit without a find.
3. (No response) Child scans for the sound treasure recap but does not name, point to, or show an item.

**AI follow-up:**

1. Name the matching evidence for the sound treasure recap, add the token to the collection, and preview what changes next.
2. Keep the hunt rule visible, contrast one non-match with one allowed example, and ask for a safer match for the sound treasure recap.
3. [wait 2s] Give one concrete example that would count for the sound treasure recap, then ask the child to point, say, or show one.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `phoneme_letter_card_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the card is unavailable, the AI repeats the target sound by voice only and must not claim the screen is showing a letter.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the sound treasure recap changed the Phoneme Treasure Hunt board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Phoneme Treasure Hunt payoff or ignores how the saved matching-item hunt turns connect.
3. (No response) Child watches the Phoneme Treasure Hunt reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's matching-item hunt turns, name one concrete saved token, and invite a short reflection.
2. Hold the Phoneme Treasure Hunt reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Phoneme Treasure Hunt board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Connection. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Phoneme Treasure Hunt moment, asks to play again, or watches the phoneme hunt recap badge.
2. (Unexpected) Child shifts topic before the recap names the matching-item hunt skill or Form and Connection.
3. (No response) Child stays on the Phoneme Treasure Hunt recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same collect mechanic and the phoneme hunt frame.
2. Close Phoneme Treasure Hunt first, name the practiced matching-item hunt, and then offer one next-round seed.
3. [wait 2s] Read the Phoneme Treasure Hunt badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `collect`, focal attribute `phoneme_hunt`, and next-step hint.
