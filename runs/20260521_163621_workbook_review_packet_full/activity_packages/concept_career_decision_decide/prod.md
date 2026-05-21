## Career Decision Role Play

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Career Decision Role Play |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | logical_reasoning (primary), observation, language expression |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The AI first assigns the child a profession, then places the child inside a concrete work scenario where they make expert decisions.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `decide` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

The child becomes the firefighter before the smoke-alarm scenario starts.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Career Decision Role Play. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts, asks what to do, or names a related object or idea.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Confirm the role and preview the first action without turning it into a quiz.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

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

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `career_portrait_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, describe the helper role by voice and avoid claiming the screen shows a person.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Become The Firefighter:**

**Runtime AI instruction:** Assign the profession first and keep the child inside the role.

**Example AI line:** "Today you are the firefighter. A smoke alarm is ringing. Should your team send help now?"

**Child responses:**

1. (Ideal) The child answers as the firefighter.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Confirm the expert response and keep the profession-first frame.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `career_portrait_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, describe the helper role by voice and avoid claiming the screen shows a person.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 2 -- Choose The Tool:**

**Runtime AI instruction:** Ask for a tool choice inside the same work scenario.

**Example AI line:** "Firefighter, which tool fits this fire scene: water hose or cooking oil?"

**Child responses:**

1. (Ideal) The child chooses a tool.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Explain why the safe tool fits the role.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `career_portrait_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, describe the helper role by voice and avoid claiming the screen shows a person.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 3 -- Choose The First Safe Action:**

**Runtime AI instruction:** Ask what the professional checks before acting.

**Example AI line:** "Should the firefighter check that people are safe outside, or run inside alone?"

**Child responses:**

1. (Ideal) The child chooses the safe first action.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Recap the expert decision path.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `career_portrait_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If cards are unavailable, describe the helper role by voice and avoid claiming the screen shows a person.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

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

**Example AI line:** "Today you practiced Form and Responsibility. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child says again, names a favorite part, or quietly watches the recap.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up:**

1. [specific] Offer a next-time variation that keeps the same source mechanic.
2. [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen:** Recap badge lists title, mechanic `decide`, focal attribute `career_decision`, and next-step hint.
