## Color Mixing Board

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Color Mixing Board |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | evidence_collection (primary), observation, language expression |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The child chooses or finds two colors, predicts what they make together, and compares against the mixed result.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `collect` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child notices two colors nearby or selects a color experiment mode.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Color Mixing Board starter cue, name the child as color mixing board player, and preview the first color-mixing prediction turn.

**Example AI line:** "Color Mixing Board starts now. You are the color mixing board player; I will help one color-mixing prediction turn at a time."

**Child responses:**

1. (Ideal) The child accepts the color mixing board player role, notices the starter cue, or names something connected to the first color pair.
2. (Unexpected) Child asks for another game, starts the matching-item hunt before the Color Mixing Board mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Color Mixing Board title/trigger card without taking the color mixing board player role yet.

**AI follow-up:**

1. Name the color mixing board player role, connect it to the starter cue, and preview the first matching-item hunt.
2. Acknowledge the request, return to the Color Mixing Board promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Color Mixing Board role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one color-mixing prediction cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the matching-item hunt loop for Color Mixing Board or asks for the easiest version.
2. (Unexpected) Child tries to skip the first color pair, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Color Mixing Board rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Color Mixing Board loop as AI prompt, child matching-item hunt, saved token, and show the first response slot.
2. Keep the rule tied to the first color pair, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Color Mixing Board rule in one sentence and ask for yes, a point, or the first chance to find or show one match.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `color_mixing_board_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the board is unavailable, explain the color result by voice and do not claim the screen is mixing colors.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child chooses or finds two colors, predicts what they make together, and compares against the mixed result. Ask the child to find or match in the first small turn.

**Example AI line:** "Let us start: The child chooses or finds two colors, predicts what they make together, and compares against the mixed result. Try the first color mix prediction now."

**Child responses:**

1. (Ideal) The child finds or names something that fits the first color pair and lets it become a collected token.
2. (Unexpected) Child offers something that does not match the first color pair, changes the hunt rule, or asks for credit without a find.
3. (No response) Child scans for the first color pair but does not name, point to, or show an item.

**AI follow-up:**

1. Name the matching evidence for the first color pair, add the token to the collection, and preview what changes next.
2. Keep the hunt rule visible, contrast one non-match with one allowed example, and ask for a safer match for the first color pair.
3. [wait 2s] Give one concrete example that would count for the first color pair, then ask the child to point, say, or show one.

**Screen:** Shows the active round token, child response slot, and color-mixing prediction cue. Use `color_mixing_board_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the board is unavailable, explain the color result by voice and do not claim the screen is mixing colors.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second collect turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child finds or names something that fits the mixed-color prediction check and lets it become a collected token.
2. (Unexpected) Child offers something that does not match the mixed-color prediction check, changes the hunt rule, or asks for credit without a find.
3. (No response) Child scans for the mixed-color prediction check but does not name, point to, or show an item.

**AI follow-up:**

1. Name the matching evidence for the mixed-color prediction check, add the token to the collection, and preview what changes next.
2. Keep the hunt rule visible, contrast one non-match with one allowed example, and ask for a safer match for the mixed-color prediction check.
3. [wait 2s] Give one concrete example that would count for the mixed-color prediction check, then ask the child to point, say, or show one.

**Screen:** Shows the active round token, child response slot, and color-mixing prediction cue. Use `color_mixing_board_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the board is unavailable, explain the color result by voice and do not claim the screen is mixing colors.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your color-mixing prediction turns?"

**Child responses:**

1. (Ideal) The child finds or names something that fits the name for the mixed result and lets it become a collected token.
2. (Unexpected) Child offers something that does not match the name for the mixed result, changes the hunt rule, or asks for credit without a find.
3. (No response) Child scans for the name for the mixed result but does not name, point to, or show an item.

**AI follow-up:**

1. Name the matching evidence for the name for the mixed result, add the token to the collection, and preview what changes next.
2. Keep the hunt rule visible, contrast one non-match with one allowed example, and ask for a safer match for the name for the mixed result.
3. [wait 2s] Give one concrete example that would count for the name for the mixed result, then ask the child to point, say, or show one.

**Screen:** Shows the active round token, child response slot, and color-mixing prediction cue. Use `color_mixing_board_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If the board is unavailable, explain the color result by voice and do not claim the screen is mixing colors.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your color-mixing prediction turns are saved: we started Color Mixing Board, practiced color-mixing prediction, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the name for the mixed result changed the Color Mixing Board board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Color Mixing Board payoff or ignores how the saved matching-item hunt turns connect.
3. (No response) Child watches the Color Mixing Board reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's matching-item hunt turns, name one concrete saved token, and invite a short reflection.
2. Hold the Color Mixing Board reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Color Mixing Board board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Connection. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Color Mixing Board moment, asks to play again, or watches the color mixing board recap badge.
2. (Unexpected) Child shifts topic before the recap names the matching-item hunt skill or Form and Connection.
3. (No response) Child stays on the Color Mixing Board recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same collect mechanic and the color mixing board frame.
2. Close Color Mixing Board first, name the practiced matching-item hunt, and then offer one next-round seed.
3. [wait 2s] Read the Color Mixing Board badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `collect`, focal attribute `color_mixing_board`, and next-step hint.
