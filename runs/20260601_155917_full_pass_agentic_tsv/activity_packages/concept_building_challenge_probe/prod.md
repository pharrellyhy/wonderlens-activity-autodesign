## Building Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Building Challenge |
| Activity Category | cat3 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Change |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | creative_thinking (primary), observation, language expression |
| Experience Pillar | Creation |
| Game Style | inventor_workshop |

### B. Activity Overview

**1. Brief Description**

The child uses blocks, bricks, or household materials to build a simple target.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `build` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Parent or child selects a hands-on build mode and has blocks, bricks, or recyclable materials available.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Building Challenge starter cue, name the child as building challenge player, and preview the first making step turn.

**Example AI line:** "Building Challenge starts now. You are the building challenge player; I will help one building step turn at a time."

**Child responses:**

1. (Ideal) The child accepts the building challenge player role, notices the starter cue, or names something connected to the first base piece or shape.
2. (Unexpected) Child asks for another game, starts the making step before the Building Challenge mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Building Challenge title/trigger card without taking the building challenge player role yet.

**AI follow-up:**

1. Name the building challenge player role, connect it to the starter cue, and preview the first making step.
2. Acknowledge the request, return to the Building Challenge promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Building Challenge role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one building step cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the making step loop for Building Challenge or asks for the easiest version.
2. (Unexpected) Child tries to skip the first base piece or shape, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Building Challenge rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Building Challenge loop as AI prompt, child making step, saved token, and show the first response slot.
2. Keep the rule tied to the first base piece or shape, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Building Challenge rule in one sentence and ask for yes, a point, or the first chance to add one making step.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `building_reference_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, describe the build target by voice; still block package generation unless material workflow support exists.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child uses blocks, bricks, or household materials to build a simple target. Ask the child to create or assemble in the first small turn.

**Example AI line:** "Let us start: The child uses blocks, bricks, or household materials to build a simple target. Try the first building step now."

**Child responses:**

1. (Ideal) The child adds the requested first base piece or shape piece, mark, word, or construction step.
2. (Unexpected) Child skips the first base piece or shape step, changes the target, or asks the AI to complete the making for them.
3. (No response) Child looks at the first base piece or shape prompt without adding a mark, piece, word, or choice.

**AI follow-up:**

1. Name what the child added, show how it changes the creation, and cue the next build step.
2. Keep the target small, restate the one required first base piece or shape step, and offer an easier mark, word, or piece.
3. [wait 2s] Model the smallest possible first base piece or shape addition, then invite the child to copy or choose one part.

**Screen:** Shows the active round token, child response slot, and building step cue. Use `building_reference_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, describe the build target by voice; still block package generation unless material workflow support exists.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second build turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child adds the requested stability or detail challenge piece, mark, word, or construction step.
2. (Unexpected) Child skips the stability or detail challenge step, changes the target, or asks the AI to complete the making for them.
3. (No response) Child looks at the stability or detail challenge prompt without adding a mark, piece, word, or choice.

**AI follow-up:**

1. Name what the child added, show how it changes the creation, and cue the next build step.
2. Keep the target small, restate the one required stability or detail challenge step, and offer an easier mark, word, or piece.
3. [wait 2s] Model the smallest possible stability or detail challenge addition, then invite the child to copy or choose one part.

**Screen:** Shows the active round token, child response slot, and building step cue. Use `building_reference_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, describe the build target by voice; still block package generation unless material workflow support exists.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your building step turns?"

**Child responses:**

1. (Ideal) The child adds the requested finished structure recap piece, mark, word, or construction step.
2. (Unexpected) Child skips the finished structure recap step, changes the target, or asks the AI to complete the making for them.
3. (No response) Child looks at the finished structure recap prompt without adding a mark, piece, word, or choice.

**AI follow-up:**

1. Name what the child added, show how it changes the creation, and cue the next build step.
2. Keep the target small, restate the one required finished structure recap step, and offer an easier mark, word, or piece.
3. [wait 2s] Model the smallest possible finished structure recap addition, then invite the child to copy or choose one part.

**Screen:** Shows the active round token, child response slot, and building step cue. Use `building_reference_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, describe the build target by voice; still block package generation unless material workflow support exists.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your building step turns are saved: we started Building Challenge, practiced building step, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the finished structure recap changed the Building Challenge board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Building Challenge payoff or ignores how the saved making step turns connect.
3. (No response) Child watches the Building Challenge reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's making step turns, name one concrete saved token, and invite a short reflection.
2. Hold the Building Challenge reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Building Challenge board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Change. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Building Challenge moment, asks to play again, or watches the building challenge recap badge.
2. (Unexpected) Child shifts topic before the recap names the making step skill or Form and Change.
3. (No response) Child stays on the Building Challenge recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same build mechanic and the building challenge frame.
2. Close Building Challenge first, name the practiced making step, and then offer one next-round seed.
3. [wait 2s] Read the Building Challenge badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `build`, focal attribute `building_challenge`, and next-step hint.
