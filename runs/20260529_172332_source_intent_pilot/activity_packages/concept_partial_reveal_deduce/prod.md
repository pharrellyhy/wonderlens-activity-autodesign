## Partial Reveal Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Partial Reveal Guess |
| Activity Category | 1 -- Visual Deduction Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Causation |
| Related Concepts | visible part, whole animal, evidence |
| ATL Skills Focus | observing, inferring, explaining |
| Experience Pillar | Mystery |
| Game Style | clue_detective |

### B. Activity Overview

**1. Brief Description**

The child sees one distinctive animal part at a time and guesses the whole animal using visible evidence.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The required screen dependency stays explicit: the card is the clue, and voice fallback must admit when no image is visible.

**4. Typical Scenario**

Child solves rabbit ears, tiger tail, and elephant trunk cards, explaining the evidence rather than hearing generic riddles.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Invite Evidence Guessing

**Runtime AI instruction:** Goal: frame the game as looking at one visible animal part and guessing the whole animal from evidence. Constraint: T1 max two sentences; no voice-only clues before the first card appears. Tone: curious mystery guide. Progress evidence: child agrees, asks to see the part, or points to the screen. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: visible partial asset is required for the main flow.

**Example AI line:** [curious] "I will show only one animal part. Look closely, then guess the whole animal."

**Child responses:**
1. (Ideal) Child completes Partial Reveal Guess / Step 1: Invite Evidence Guessing with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 1: Invite Evidence Guessing into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 1: Invite Evidence Guessing before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 1: Invite Evidence Guessing and move to the next preserved source step.
2. (Unexpected) [repair] For Step 1: Invite Evidence Guessing, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 1: Invite Evidence Guessing, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Closed mystery card state; no animal answer visible yet.
#### Step 2: Show The First Part

**Runtime AI instruction:** Goal: display rabbit_ears_reveal_card and ask what whole animal it might be. Constraint: do not show or say the answer before the child guesses. Tone: playful detective. Progress evidence: child says rabbit, bunny, ears, or gives evidence. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: child deduces from visible evidence, not generic riddles.

**Example AI line:** [detective] "Look at these long soft ears. What animal could be hiding?"

**Child responses:**
1. (Ideal) Child completes Partial Reveal Guess / Step 2: Show The First Part with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 2: Show The First Part into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 2: Show The First Part before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 2: Show The First Part and move to the next preserved source step.
2. (Unexpected) [repair] For Step 2: Show The First Part, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 2: Show The First Part, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show asset_id=rabbit_ears_reveal_card full screen inside the round safe area.
#### Step 3: Try A Different Part

**Round 1 -- Second Partial Clue:**

**Runtime AI instruction:** Goal: display tiger_tail_reveal_card and ask for a new whole-animal guess using visible stripes and tail shape. Constraint: one guess plus one evidence detail. Tone: excited detective. Progress evidence: child says tiger, striped tail, cat, or points to stripes. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: maintain partial reveal image flow across multiple rounds.

**Example AI line:** [excited] "Now I see a striped tail curling in. Which animal might own this part?"

**Child responses:**
1. (Ideal) Child completes Partial Reveal Guess / Step 3: Try A Different Part with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 3: Try A Different Part into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 3: Try A Different Part before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 3: Try A Different Part and move to the next preserved source step.
2. (Unexpected) [repair] For Step 3: Try A Different Part, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 3: Try A Different Part, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture.

**Screen/state:** Replace first card with asset_id=tiger_tail_reveal_card; keep a small solved rabbit badge.
#### Step 4: Final Part Challenge

**Runtime AI instruction:** Goal: display elephant_trunk_reveal_card and let the child use shape evidence for the final guess. Constraint: T1 max two sentences; no full animal reveal before answer. Tone: gentle suspense. Progress evidence: child says elephant, trunk, long nose, or points. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: do not replace this with generic animal trivia.

**Example AI line:** [suspense] "Last mystery part: a long trunk shape. What whole animal could it be?"

**Child responses:**
1. (Ideal) Child completes Partial Reveal Guess / Step 4: Final Part Challenge with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 4: Final Part Challenge into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 4: Final Part Challenge before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 4: Final Part Challenge and move to the next preserved source step.
2. (Unexpected) [repair] For Step 4: Final Part Challenge, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 4: Final Part Challenge, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show asset_id=elephant_trunk_reveal_card; three-card progress shows two solved badges.
#### Step 5: Close The Evidence Gallery

**Runtime AI instruction:** Goal: recap each visible part and the whole animal guessed from it. Constraint: max two sentences; no new card. Tone: proud and observant. Progress evidence: child names one animal or clue. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: keep the visible evidence source central to the ending.

**Example AI line:** [proud] "You solved animals from parts: ears, stripes, and trunk. That is evidence guessing."

**Child responses:**
1. (Ideal) Child completes Partial Reveal Guess / Step 5: Close The Evidence Gallery with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 5: Close The Evidence Gallery into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 5: Close The Evidence Gallery before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 5: Close The Evidence Gallery and move to the next preserved source step.
2. (Unexpected) [repair] For Step 5: Close The Evidence Gallery, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 5: Close The Evidence Gallery, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show three solved thumbnails using the same asset_ids; no new generated image.
