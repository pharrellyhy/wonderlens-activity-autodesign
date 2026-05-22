## Story Challenge Unlock

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Story Challenge Unlock |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | imagination (primary), observation, language expression |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

The AI tells a fixed story, pauses at challenge gates, and unlocks the next story beat only after the child completes each quick challenge.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `imagine` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

A fox reaches story gates that open with a color find, an animal sound, and a French word echo.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Story Challenge Unlock. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts, asks what to do, or names a related object or idea.
2. (Unexpected) Child veers away from "Transition Bridge" in Story Challenge Unlock, skips the story challenge action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Transition Bridge", watches the current screen, or needs a first tiny story challenge model.

**AI follow-up:**

1. [specific] Confirm the role and preview the first action without turning it into a quiz.
2. [redirect] Validate briefly, keep the Story Challenge Unlock frame, and offer one safe choice that still completes "Transition Bridge".
3. [wait 2s] [gentle] Model one tiny story challenge step for "Transition Bridge", then invite the child to copy or choose.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child confirms the rule or asks for a smaller version.
2. (Unexpected) Child veers away from "Role And Rules" in Story Challenge Unlock, skips the story challenge action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Role And Rules", watches the current screen, or needs a first tiny story challenge model.

**AI follow-up:**

1. [specific] Offer the smallest safe version and keep the source play frame intact.
2. [redirect] Validate briefly, keep the Story Challenge Unlock frame, and offer one safe choice that still completes "Role And Rules".
3. [wait 2s] [gentle] Model one tiny story challenge step for "Role And Rules", then invite the child to copy or choose.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `story_unlock_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Unlock The Moon Door:**

**Runtime AI instruction:** Tell the story beat before the task, then pause for a color challenge.

**Example AI line:** "The fox reaches a moon door. Can you name or show silver, white, or blue so it opens?"

**Child responses:**

1. (Ideal) The child names or shows a color.
2. (Unexpected) Child veers away from "Unlock The Moon Door" in Story Challenge Unlock, skips the story challenge action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Unlock The Moon Door", watches the current screen, or needs a first tiny story challenge model.

**AI follow-up:**

1. [specific] Narrate the door opening and continue the story.
2. [redirect] Validate briefly, keep the Story Challenge Unlock frame, and offer one safe choice that still completes "Unlock The Moon Door".
3. [wait 2s] [gentle] Model one tiny story challenge step for "Unlock The Moon Door", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `story_unlock_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 2 -- Wake The Owl Bridge:**

**Runtime AI instruction:** Continue the story, then pause for a soft animal sound challenge.

**Example AI line:** "The fox finds a sleepy owl bridge. Can you make a quiet hoo-hoo?"

**Child responses:**

1. (Ideal) The child makes the sound or says hello owl.
2. (Unexpected) Child veers away from "Wake The Owl Bridge" in Story Challenge Unlock, skips the story challenge action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Wake The Owl Bridge", watches the current screen, or needs a first tiny story challenge model.

**AI follow-up:**

1. [specific] Narrate the bridge waking and continuing.
2. [redirect] Validate briefly, keep the Story Challenge Unlock frame, and offer one safe choice that still completes "Wake The Owl Bridge".
3. [wait 2s] [gentle] Model one tiny story challenge step for "Wake The Owl Bridge", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `story_unlock_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 3 -- Echo The Star Word:**

**Runtime AI instruction:** Continue to the final gate, then ask for one echo word.

**Example AI line:** "A star page asks for bonjour. Can you echo bonjour?"

**Child responses:**

1. (Ideal) The child repeats the word.
2. (Unexpected) Child veers away from "Echo The Star Word" in Story Challenge Unlock, skips the story challenge action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Echo The Star Word", watches the current screen, or needs a first tiny story challenge model.

**AI follow-up:**

1. [specific] Unlock the meadow and recap the story path.
2. [redirect] Validate briefly, keep the Story Challenge Unlock frame, and offer one safe choice that still completes "Echo The Star Word".
3. [wait 2s] [gentle] Model one tiny story challenge step for "Echo The Star Word", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `story_unlock_cards_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If unlock UI is unavailable, use voice-only story choices and do not claim a screen element has unlocked.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child reacts, names a favorite turn, or asks to revise one part.
2. (Unexpected) Child veers away from "Magic Moment" in Story Challenge Unlock, skips the story challenge action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Magic Moment", watches the current screen, or needs a first tiny story challenge model.

**AI follow-up:**

1. [specific] Tie the reveal directly to the child action and invite one short reflection.
2. [redirect] Validate briefly, keep the Story Challenge Unlock frame, and offer one safe choice that still completes "Magic Moment".
3. [wait 2s] [gentle] Model one tiny story challenge step for "Magic Moment", then invite the child to copy or choose.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Perspective. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child says again, names a favorite part, or quietly watches the recap.
2. (Unexpected) Child veers away from "Closing + IB Concepts" in Story Challenge Unlock, skips the story challenge action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Closing + IB Concepts", watches the current screen, or needs a first tiny story challenge model.

**AI follow-up:**

1. [specific] Offer a next-time variation that keeps the same source mechanic.
2. [redirect] Validate briefly, keep the Story Challenge Unlock frame, and offer one safe choice that still completes "Closing + IB Concepts".
3. [wait 2s] [gentle] Model one tiny story challenge step for "Closing + IB Concepts", then invite the child to copy or choose.

**Screen:** Recap badge lists title, mechanic `imagine`, focal attribute `story_challenge_unlock`, and next-step hint.
