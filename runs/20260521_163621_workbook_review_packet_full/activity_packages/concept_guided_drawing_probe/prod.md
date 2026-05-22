## Guided Drawing

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Guided Drawing |
| Activity Category | cat3 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Change |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | creative_thinking (primary), observation, language expression |
| Experience Pillar | Creation |
| Game Style | inventor_workshop |

### B. Activity Overview

**1. Brief Description**

The AI guides the child to use paper and pencil to complete a simple drawing step by step.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `build` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child is indoors and photographs an object that could become a drawing theme.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Guided Drawing. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the guided artist role, notices the starter cue, or names something connected to the first line or shape.
2. (Unexpected) Child asks for another game, starts the making step before the Guided Drawing mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Guided Drawing title/trigger card without taking the guided artist role yet.

**AI follow-up:**

1. Name the guided artist role, connect it to the starter cue, and preview the first making step.
2. Acknowledge the request, return to the Guided Drawing promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Guided Drawing role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the making step loop for Guided Drawing or asks for the easiest version.
2. (Unexpected) Child tries to skip the first line or shape, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Guided Drawing rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Guided Drawing loop as AI prompt, child making step, saved token, and show the first response slot.
2. Keep the rule tied to the first line or shape, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Guided Drawing rule in one sentence and ask for yes, a point, or the first chance to add one making step.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `guided_drawing_step_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If step cards are unavailable, use voice-only step descriptions; the Cat3 material workflow still requires product approval before package generation.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The AI guides the child to use paper and pencil to complete a simple drawing step by step. Ask the child to create or assemble in the first small turn.

**Example AI line:** "Let us start: The AI guides the child to use paper and pencil to complete a simple drawing step by step. What is your first try?"

**Child responses:**

1. (Ideal) The child adds the requested first line or shape piece, mark, word, or construction step.
2. (Unexpected) Child skips the first line or shape step, changes the target, or asks the AI to complete the making for them.
3. (No response) Child looks at the first line or shape prompt without adding a mark, piece, word, or choice.

**AI follow-up:**

1. Name what the child added, show how it changes the creation, and cue the next build step.
2. Keep the target small, restate the one required first line or shape step, and offer an easier mark, word, or piece.
3. [wait 2s] Model the smallest possible first line or shape addition, then invite the child to copy or choose one part.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `guided_drawing_step_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If step cards are unavailable, use voice-only step descriptions; the Cat3 material workflow still requires product approval before package generation.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second build turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child adds the requested second guided detail piece, mark, word, or construction step.
2. (Unexpected) Child skips the second guided detail step, changes the target, or asks the AI to complete the making for them.
3. (No response) Child looks at the second guided detail prompt without adding a mark, piece, word, or choice.

**AI follow-up:**

1. Name what the child added, show how it changes the creation, and cue the next build step.
2. Keep the target small, restate the one required second guided detail step, and offer an easier mark, word, or piece.
3. [wait 2s] Model the smallest possible second guided detail addition, then invite the child to copy or choose one part.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `guided_drawing_step_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If step cards are unavailable, use voice-only step descriptions; the Cat3 material workflow still requires product approval before package generation.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child adds the requested finished drawing recap piece, mark, word, or construction step.
2. (Unexpected) Child skips the finished drawing recap step, changes the target, or asks the AI to complete the making for them.
3. (No response) Child looks at the finished drawing recap prompt without adding a mark, piece, word, or choice.

**AI follow-up:**

1. Name what the child added, show how it changes the creation, and cue the next build step.
2. Keep the target small, restate the one required finished drawing recap step, and offer an easier mark, word, or piece.
3. [wait 2s] Model the smallest possible finished drawing recap addition, then invite the child to copy or choose one part.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `guided_drawing_step_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If step cards are unavailable, use voice-only step descriptions; the Cat3 material workflow still requires product approval before package generation.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the finished drawing recap changed the Guided Drawing board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Guided Drawing payoff or ignores how the saved making step turns connect.
3. (No response) Child watches the Guided Drawing reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's making step turns, name one concrete saved token, and invite a short reflection.
2. Hold the Guided Drawing reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Guided Drawing board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Change. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Guided Drawing moment, asks to play again, or watches the guided drawing recap badge.
2. (Unexpected) Child shifts topic before the recap names the making step skill or Form and Change.
3. (No response) Child stays on the Guided Drawing recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same build mechanic and the guided drawing frame.
2. Close Guided Drawing first, name the practiced making step, and then offer one next-round seed.
3. [wait 2s] Read the Guided Drawing badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `build`, focal attribute `guided_drawing`, and next-step hint.
