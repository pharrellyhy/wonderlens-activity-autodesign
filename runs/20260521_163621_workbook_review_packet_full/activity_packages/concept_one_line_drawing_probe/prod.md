## One-Line Drawing Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | One-Line Drawing Challenge |
| Activity Category | cat3 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Change |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | creative_thinking (primary), observation, language expression |
| Experience Pillar | Creation |
| Game Style | inventor_workshop |

### B. Activity Overview

**1. Brief Description**

The child tries to draw a target without lifting the pencil or finger.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `build` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Child has paper or a drawing surface and chooses a drawing challenge.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: One-Line Drawing Challenge. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts, asks what to do, or names a related object or idea.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Confirm the role and preview the first action without turning it into a quiz.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child confirms the rule or asks for a smaller version.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Offer the smallest safe version and keep the source play frame intact.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `one_line_drawing_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards or drawing workflow are unavailable, block at Phase 0.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child tries to draw a target without lifting the pencil or finger.. Ask the child to create or assemble in the first small turn.

**Example AI line:** "Let us start: The child tries to draw a target without lifting the pencil or finger. What is your first try?"

**Child responses:**

1. (Ideal) The child gives the first source-aligned action.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Confirm the action and name how it matches the source rule.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `one_line_drawing_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards or drawing workflow are unavailable, block at Phase 0.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second build turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child repeats the same mechanic with a variation.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Connect the variation back to the same play frame.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `one_line_drawing_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards or drawing workflow are unavailable, block at Phase 0.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What did we make, find, choose, or learn from your turns?"

**Child responses:**

1. (Ideal) The child recaps or reacts.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Summarize the child action and source-specific payoff.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `one_line_drawing_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards or drawing workflow are unavailable, block at Phase 0.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child reacts, names a favorite turn, or asks to revise one part.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Tie the reveal directly to the child action and invite one short reflection.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Change. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child says again, names a favorite part, or quietly watches the recap.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Offer a next-time variation that keeps the same source mechanic.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Recap badge lists title, mechanic `build`, focal attribute `one_line_drawing`, and next-step hint.
