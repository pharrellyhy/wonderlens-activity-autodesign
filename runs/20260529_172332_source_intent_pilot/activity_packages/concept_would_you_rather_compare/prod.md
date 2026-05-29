## Would You Rather

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Would You Rather |
| Activity Category | 1 -- Voice-Led Comparison Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Perspective and Responsibility |
| Related Concepts | preference, tradeoff, short question |
| ATL Skills Focus | choosing, explaining, listening |
| Experience Pillar | Performance |
| Game Style | choice_chain |

### B. Activity Overview

**1. Brief Description**

The child chooses between short playful options and gives a tiny reason.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The source is intentionally simple; the stricter audit should not overfit only asset-heavy packages.

**4. Typical Scenario**

Child answers three short silly comparison prompts, explains tiny reasons, and closes with a favorite choice.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Open The Silly Choice Round

**Runtime AI instruction:** Goal: introduce short, playful two-choice questions. Constraint: T1 max two sentences; no long setup. Tone: funny and safe. Progress evidence: child chooses, laughs, asks for choices, or listens. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: repeated action is compare two options and choose one.

**Example AI line:** [funny] "Ready for a tiny Would You Rather? Pick one silly choice, then tell me why."

**Child responses:**
1. (Ideal) Child completes Would You Rather / Step 1: Open The Silly Choice Round with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 1: Open The Silly Choice Round into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 1: Open The Silly Choice Round before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 1: Open The Silly Choice Round and move to the next preserved source step.
2. (Unexpected) [repair] For Step 1: Open The Silly Choice Round, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 1: Open The Silly Choice Round, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** No required image; show simple two-choice runtime state.
#### Step 2: Ask The First Pair

**Runtime AI instruction:** Goal: ask one short silly pair and invite a reason. Constraint: options must be age-safe, non-shaming, and brief. Tone: playful. Progress evidence: child chooses ketchup toothbrush or chocolate-milk hair and gives any reason. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: do not make questions long.

**Example AI line:** [playful] "Would you rather brush your teeth with ketchup, or wash your hair with chocolate milk?"

**Child responses:**
1. (Ideal) Child completes Would You Rather / Step 2: Ask The First Pair with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 2: Ask The First Pair into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 2: Ask The First Pair before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 2: Ask The First Pair and move to the next preserved source step.
2. (Unexpected) [repair] For Step 2: Ask The First Pair, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 2: Ask The First Pair, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show two abstract choice slots in runtime state; no asset dependency.
#### Step 3: Ask A Movement Pair

**Round 1 -- Movement Choice:**

**Runtime AI instruction:** Goal: ask another short pair with a different comparison dimension. Constraint: one sentence question plus one optional why prompt. Tone: energetic. Progress evidence: child chooses hop everywhere or tiptoe everywhere. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: keep funny compare/choose loop, not trivia.

**Example AI line:** [energetic] "Would you rather hop everywhere today, or tiptoe everywhere today?"

**Child responses:**
1. (Ideal) Child completes Would You Rather / Step 3: Ask A Movement Pair with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 3: Ask A Movement Pair into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 3: Ask A Movement Pair before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 3: Ask A Movement Pair and move to the next preserved source step.
2. (Unexpected) [repair] For Step 3: Ask A Movement Pair, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 3: Ask A Movement Pair, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture.

**Screen/state:** Update round counter to choice 2 of 3, preserve the two spoken options in runtime state, and keep the no-asset voice-led layout stable.
#### Step 4: Ask A Tiny Imagination Pair

**Runtime AI instruction:** Goal: ask a final short imaginative pair. Constraint: avoid scary, gross, or humiliating options. Tone: whimsical. Progress evidence: child chooses and names a tradeoff. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: no long or adult-style dilemmas.

**Example AI line:** [whimsical] "Would you rather have a pocket full of clouds, or shoes that squeak with every step?"

**Child responses:**
1. (Ideal) Child completes Would You Rather / Step 4: Ask A Tiny Imagination Pair with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 4: Ask A Tiny Imagination Pair into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 4: Ask A Tiny Imagination Pair before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 4: Ask A Tiny Imagination Pair and move to the next preserved source step.
2. (Unexpected) [repair] For Step 4: Ask A Tiny Imagination Pair, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 4: Ask A Tiny Imagination Pair, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show final choice counter with the two spoken options tracked in runtime metadata; no image or generated asset is claimed.
#### Step 5: Close The Choice Chain

**Runtime AI instruction:** Goal: recap that the child compared options, chose, and gave reasons. Constraint: max two sentences; no new pair. Tone: warm and amused. Progress evidence: child repeats favorite choice or listens. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: preserve short classic Would You Rather format.

**Example AI line:** [warm] "You made three silly choices and told your reasons. Choice chain complete."

**Child responses:**
1. (Ideal) Child completes Would You Rather / Step 5: Close The Choice Chain with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 5: Close The Choice Chain into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 5: Close The Choice Chain before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 5: Close The Choice Chain and move to the next preserved source step.
2. (Unexpected) [repair] For Step 5: Close The Choice Chain, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 5: Close The Choice Chain, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show completed choice chain with three saved choices and a favorite-choice slot; no image or generated asset is claimed.
