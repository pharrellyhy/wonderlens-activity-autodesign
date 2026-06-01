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

**Runtime AI instruction:** Goal: tell the child they are the professional expert before any scenario question. Constraint: T1 max two sentences; role-first, not profession-matching. Tone: proud and invitational. Progress evidence: child accepts the role, says firefighter, or asks what to do. Branch behavior: if the child accepts, start the work problem; if they try to guess the job, restate that they are the expert; if quiet, model putting on the pretend helmet. Frame/source guardrail: preserve child-as-professional role play.

**Example AI line:** [proud] "Today you are the firefighter expert. Ready to help decide what our team should do?"

**Child responses:**
1. (Ideal) Child says "I am the firefighter", "ready", or asks what the team should do.
2. (Unexpected) Child tries to guess which profession is shown instead of taking the role.
3. (No response) Child watches the firefighter role card without answering.

**AI follow-up policy:**
1. (Ideal) [start] "Expert helmet on. You are the firefighter, so the next choice is yours."
2. (Unexpected) [repair] "This is not a job-guessing card; you are the firefighter expert today."
3. (No response) [model] "I will pretend you put on the firefighter helmet. Now you can make the expert choice."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show asset_id=firefighter_role_card as role support; if missing, keep voice-only role play honest.
#### Step 2: Present A Concrete Work Scenario

**Runtime AI instruction:** Goal: describe one simple firefighter scenario with two safe choices. Constraint: no scary detail; child chooses yes/no or A/B. Tone: calm and important. Progress evidence: child listens, points, or asks for choices again. Branch behavior: ask send-now versus wait, calm worry, and repeat the two choices after silence. Frame/source guardrail: child must make a work decision in role, not match profession to scenario.

**Example AI line:** [calm] "Our team sees smoke from a building. Should we send the fire truck now, yes or no?"

**Child responses:**
1. (Ideal) Child listens and says "send the truck", "yes", "wait", or asks to hear choices again.
2. (Unexpected) Child becomes worried by smoke or asks about scary emergency details.
3. (No response) Child gives no yes/no after the scenario.

**AI follow-up policy:**
1. (Ideal) [decision] "Good, you are choosing as the firefighter expert."
2. (Unexpected) [soothe] "This is pretend safety practice. We keep it calm and choose what helpers should do."
3. (No response) [choice] "Expert, choose one: send the truck now, or wait?"

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Keep role card visible with two simple choice slots in runtime state.
#### Step 3: Decide The Expert Action

**Round 1 -- Expert Action Decision:**

**Runtime AI instruction:** Goal: accept the child decision and explain why it helps. Constraint: one short explanation; do not punish wrong answers. Tone: respectful coach. Progress evidence: child chooses send now, wait, yes, or no. Branch behavior: explain why send-now is safer, repair wait without shame, and model send-now after silence. Frame/source guardrail: decision is made by the child as expert.

**Example AI line:** [coach] "What is your expert decision: send the truck now, or wait?"

**Child responses:**
1. (Ideal) Child chooses "send the truck now" or says yes to quick help.
2. (Unexpected) Child chooses wait, gives no reason, or says the grown-ups should decide instead.
3. (No response) Child stays quiet at the send/wait decision.

**AI follow-up policy:**
1. (Ideal) [explain] "Good expert call: quick trained help keeps people safer in our pretend scenario."
2. (Unexpected) [repair] "Waiting can let danger grow, so the safer expert choice is to send trained help now."
3. (No response) [model] "I will choose send the truck now for our pretend safety practice."

**Photo capture timing:** No photo capture.

**Screen/state:** Show a decision stamp state beside firefighter_role_card; no scoring meter.
#### Step 4: Give A Second Tiny Expert Choice

**Runtime AI instruction:** Goal: ask one more simple tool/action choice to keep the work role active. Constraint: binary choice, safe and short. Tone: focused and proud. Progress evidence: child chooses water, trained helpers, hose, or another safe action. Branch behavior: accept water/safe helper choices, correct oil gently, and scaffold with water after silence. Frame/source guardrail: keep child in professional role through the sequence.

**Example AI line:** [focused] "Expert choice two: for a small pretend fire, should helpers use water or oil?"

**Child responses:**
1. (Ideal) Child chooses water, hose, or trained helpers for the pretend fire.
2. (Unexpected) Child chooses oil, a toy sword, or another unsafe tool.
3. (No response) Child does not answer the water/oil choice.

**AI follow-up policy:**
1. (Ideal) [praise] "Water and trained helpers are safer practice choices for this pretend fire."
2. (Unexpected) [teach] "Oil can make fire worse, so firefighters use safer tools like water and hoses."
3. (No response) [scaffold] "I will choose water for the safe practice answer."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Role card remains visible; the safe choice is highlighted in runtime state.
#### Step 5: Close The Expert Shift

**Runtime AI instruction:** Goal: celebrate the child professional decision-making and recap the scenario choices. Constraint: max two sentences; avoid claiming real emergency competence. Tone: proud and safe. Progress evidence: child repeats firefighter, water, truck, or listens. Branch behavior: close with pretend expert pride, separate pretend practice from real emergencies, and save quietly if no reply. Frame/source guardrail: maintain professional agency without overclaiming.

**Example AI line:** [proud] "Firefighter expert shift complete: you made quick, safe pretend-work choices."

**Child responses:**
1. (Ideal) Child says firefighter, truck, water, or "I helped".
2. (Unexpected) Child asks whether they can fight a real fire.
3. (No response) Child gives no closing response.

**AI follow-up policy:**
1. (Ideal) [badge] "Expert shift saved: you chose quick help and a safer tool."
2. (Unexpected) [safety] "Real fires are for trained adults. You practiced pretend expert choices today."
3. (No response) [quiet close] "I will save your firefighter expert badge."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show role card with completed expert badge state.
