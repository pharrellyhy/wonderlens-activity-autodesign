## Career Decision

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Career Decision |
| Activity Category | 1 -- Role-Play Decision Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Function and Responsibility |
| Related Concepts | expert role, work scenario, safe choice |
| ATL Skills Focus | decision-making, explaining, role-play |
| Experience Pillar | Performance |
| Game Style | expert_choice |

### B. Activity Overview

**1. Brief Description**

The child is first placed in a professional role, then makes simple work decisions as that expert.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The child is never asked to match a profession to a scenario; the professional identity comes first and drives the choices.

**4. Typical Scenario**

Child becomes a firefighter expert, hears a safe pretend scenario, chooses actions, and receives a role-pride celebration.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Give The Child The Expert Role

**Runtime AI instruction:** Goal: tell the child they are the professional expert before any scenario question. Constraint: T1 max two sentences; role-first, not profession-matching. Tone: proud and invitational. Progress evidence: child accepts the role, says firefighter, or asks what to do. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: preserve child-as-professional role play.

**Example AI line:** [proud] "Today you are the firefighter expert. Ready to help decide what our team should do?"

**Child responses:**
1. (Ideal) Child completes Career Decision / Step 1: Give The Child The Expert Role with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 1: Give The Child The Expert Role into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 1: Give The Child The Expert Role before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 1: Give The Child The Expert Role and move to the next preserved source step.
2. (Unexpected) [repair] For Step 1: Give The Child The Expert Role, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 1: Give The Child The Expert Role, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show asset_id=firefighter_role_card as role support; if missing, keep voice-only role play honest.
#### Step 2: Present A Concrete Work Scenario

**Runtime AI instruction:** Goal: describe one simple firefighter scenario with two safe choices. Constraint: no scary detail; child chooses yes/no or A/B. Tone: calm and important. Progress evidence: child listens, points, or asks for choices again. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: child must make a work decision in role, not match profession to scenario.

**Example AI line:** [calm] "Our team sees smoke from a building. Should we send the fire truck now, yes or no?"

**Child responses:**
1. (Ideal) Child completes Career Decision / Step 2: Present A Concrete Work Scenario with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 2: Present A Concrete Work Scenario into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 2: Present A Concrete Work Scenario before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 2: Present A Concrete Work Scenario and move to the next preserved source step.
2. (Unexpected) [repair] For Step 2: Present A Concrete Work Scenario, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 2: Present A Concrete Work Scenario, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Keep role card visible with two simple choice slots in runtime state.
#### Step 3: Decide The Expert Action

**Round 1 -- Expert Action Decision:**

**Runtime AI instruction:** Goal: accept the child decision and explain why it helps. Constraint: one short explanation; do not punish wrong answers. Tone: respectful coach. Progress evidence: child chooses yes/no, water/oil, or another simple option. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: decision is made by the child as expert.

**Example AI line:** [coach] "What is your expert decision: send the truck now, or wait?"

**Child responses:**
1. (Ideal) Child completes Career Decision / Step 3: Decide The Expert Action with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 3: Decide The Expert Action into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 3: Decide The Expert Action before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 3: Decide The Expert Action and move to the next preserved source step.
2. (Unexpected) [repair] For Step 3: Decide The Expert Action, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 3: Decide The Expert Action, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture.

**Screen/state:** Show a decision stamp state beside firefighter_role_card; no scoring meter.
#### Step 4: Give A Second Tiny Expert Choice

**Runtime AI instruction:** Goal: ask one more simple tool/action choice to keep the work role active. Constraint: binary choice, safe and short. Tone: focused and proud. Progress evidence: child chooses water, hose, call for help, or another safe action. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: keep child in professional role through the sequence.

**Example AI line:** [focused] "Expert choice two: for a small pretend fire, should helpers use water or oil?"

**Child responses:**
1. (Ideal) Child completes Career Decision / Step 4: Give A Second Tiny Expert Choice with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 4: Give A Second Tiny Expert Choice into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 4: Give A Second Tiny Expert Choice before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 4: Give A Second Tiny Expert Choice and move to the next preserved source step.
2. (Unexpected) [repair] For Step 4: Give A Second Tiny Expert Choice, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 4: Give A Second Tiny Expert Choice, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Role card remains visible; the safe choice is highlighted in runtime state.
#### Step 5: Close The Expert Shift

**Runtime AI instruction:** Goal: celebrate the child professional decision-making and recap the scenario choices. Constraint: max two sentences; avoid claiming real emergency competence. Tone: proud and safe. Progress evidence: child repeats firefighter, water, truck, or listens. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: maintain professional agency without overclaiming.

**Example AI line:** [proud] "Firefighter expert shift complete: you made quick, safe pretend-work choices."

**Child responses:**
1. (Ideal) Child completes Career Decision / Step 5: Close The Expert Shift with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 5: Close The Expert Shift into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 5: Close The Expert Shift before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 5: Close The Expert Shift and move to the next preserved source step.
2. (Unexpected) [repair] For Step 5: Close The Expert Shift, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 5: Close The Expert Shift, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show role card with completed expert badge state.
