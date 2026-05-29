## Constellation Star Count

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Constellation Star Count |
| Activity Category | 1 -- Reference-Bound In-Device Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | quantity, source fidelity, background information |
| ATL Skills Focus | choosing, observing, listening |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

The child chooses a number first, then sees a real approved constellation card matching that count and hears a short background fact.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The drift-prone part is locked: no visible star counting before choice, no fictional constellations, and no missing background information.

**4. Typical Scenario**

Child chooses 5 or 7, the device reveals Cassiopeia or Orion from approved package-local assets, and the AI shares one child-safe background note.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Choose A Star Count

**Runtime AI instruction:** Goal: ask the child to choose one number before any constellation appears. Constraint: T1 max two sentences; offer exactly 5 or 7 in this pilot. Tone: mysterious and warm. Progress evidence: child says, points, or taps 5 or 7. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: number choice must happen before reveal and must not become direct star counting.

**Example AI line:** [mysterious] "Pick a sky number: five or seven. Then I will open a real constellation card that matches your number."

**Child responses:**
1. (Ideal) Child completes Constellation Star Count / Step 1: Choose A Star Count with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 1: Choose A Star Count into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 1: Choose A Star Count before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 1: Choose A Star Count and move to the next preserved source step.
2. (Unexpected) [repair] For Step 1: Choose A Star Count, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 1: Choose A Star Count, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Closed sky-door state with no stars visible; do not show constellation assets yet.
#### Step 2: Reveal The Matching Real Constellation

**Runtime AI instruction:** Goal: reveal the approved constellation asset whose metadata matches the chosen count: 5 maps to cassiopeia_five_star_card and 7 maps to orion_seven_star_card. Constraint: max two sentences; do not add extra stars or ask the child to recount. Tone: wonder-filled and careful. Progress evidence: child notices the revealed pattern, says star, line, Orion, or Cassiopeia. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: preserve real/reference-bound assets and count metadata; no fictional constellations.

**Example AI line:** [wonder] "Your number opened a real constellation card. I will keep its star pattern just as the approved chart shows."

**Child responses:**
1. (Ideal) Child completes Constellation Star Count / Step 2: Reveal The Matching Real Constellation with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 2: Reveal The Matching Real Constellation into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 2: Reveal The Matching Real Constellation before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 2: Reveal The Matching Real Constellation and move to the next preserved source step.
2. (Unexpected) [repair] For Step 2: Reveal The Matching Real Constellation, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 2: Reveal The Matching Real Constellation, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Reveal the asset selected by count; no text labels, count markers, or background star clutter.
#### Step 3: Tell The Background Fact

**Round 1 -- Constellation Background Reveal:**

**Runtime AI instruction:** Goal: give one short background fact about the revealed real constellation and connect it to the visible card. Constraint: T1 max two short sentences; stable fact only. Tone: gentle teacher with wonder. Progress evidence: child listens, repeats the constellation name, asks where it is, or points to the pattern. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: do not replace background information with a counting challenge.

**Example AI line:** [gentle] "Constellations are star patterns people use to find shapes in the night sky. This card shows one approved pattern."

**Child responses:**
1. (Ideal) Child completes Constellation Star Count / Step 3: Tell The Background Fact with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 3: Tell The Background Fact into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 3: Tell The Background Fact before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 3: Tell The Background Fact and move to the next preserved source step.
2. (Unexpected) [repair] For Step 3: Tell The Background Fact, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 3: Tell The Background Fact, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture.

**Screen/state:** Keep the selected asset visible while the background fact is spoken.
#### Step 4: Celebrate The Number Door

**Runtime AI instruction:** Goal: celebrate the source sequence: choose a number, reveal a real matching card, hear background. Constraint: one or two short sentences; mention the number as opener, not a demand to count again. Tone: proud and wonder-filled. Progress evidence: child says the number, star, constellation, or listens. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: do not turn the celebration into star counting or random generation.

**Example AI line:** [proud] "Your number opened a real sky card, and we learned a little about it."

**Child responses:**
1. (Ideal) Child completes Constellation Star Count / Step 4: Celebrate The Number Door with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 4: Celebrate The Number Door into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 4: Celebrate The Number Door before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 4: Celebrate The Number Door and move to the next preserved source step.
2. (Unexpected) [repair] For Step 4: Celebrate The Number Door, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 4: Celebrate The Number Door, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Hold the revealed asset in completed state; no overlays.
#### Step 5: Close The Sky Door

**Runtime AI instruction:** Goal: recap the chosen number, matching real constellation reveal, and background fact. Constraint: max two sentences; no new constellation or direct counting prompt. Tone: gentle closing. Progress evidence: child says goodbye, number, or constellation. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: preserve approved reference/context flow through the ending.

**Example AI line:** [gentle] "Sky door closed: you chose a number, a real matching constellation appeared, and we learned one fact."

**Child responses:**
1. (Ideal) Child completes Constellation Star Count / Step 5: Close The Sky Door with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 5: Close The Sky Door into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 5: Close The Sky Door before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 5: Close The Sky Door and move to the next preserved source step.
2. (Unexpected) [repair] For Step 5: Close The Sky Door, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 5: Close The Sky Door, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Fade selected asset to saved thumbnail; no new assets appear.
