## Award Certificate

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Award Certificate |
| Activity Category | cat3 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | empathy (primary), observation, language expression |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The child designs a paper award for someone they appreciate, using warm AI story framing and badge ideas without judging the final drawing.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `care` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

A family story or photographed object inspires a handmade award such as Best Helper or Best Mom.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Award Certificate. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the award certificate player role, notices the starter cue, or names something connected to the person to appreciate.
2. (Unexpected) Child asks for another game, starts the kind response before the Award Certificate mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Award Certificate title/trigger card without taking the award certificate player role yet.

**AI follow-up:**

1. Name the award certificate player role, connect it to the starter cue, and preview the first kind response.
2. Acknowledge the request, return to the Award Certificate promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Award Certificate role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the kind response loop for Award Certificate or asks for the easiest version.
2. (Unexpected) Child tries to skip the person to appreciate, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Award Certificate rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Award Certificate loop as AI prompt, child kind response, saved token, and show the first response slot.
2. Keep the rule tied to the person to appreciate, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Award Certificate rule in one sentence and ask for yes, a point, or the first chance to choose a kind response.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `award_inspiration_badges_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If badge assets or certificate workflow are unavailable, block at Phase 0 or run a verbal appreciation activity without claiming a certificate is created.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Choose The Person:**

**Runtime AI instruction:** Ask who receives the award and why.

**Example AI line:** "Who should receive today's award: someone who helped, tried hard, or made you smile?"

**Child responses:**

1. (Ideal) The child notices the person to appreciate cue and suggests a fitting feeling, need, or kind action.
2. (Unexpected) Child judges the person/object, ignores the person to appreciate cue, or offers help that does not fit the need.
3. (No response) Child watches the person to appreciate cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness token, and show the calmer or helped state.
2. Reframe without judging, point to the cue for the person to appreciate, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for the person to appreciate, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `award_inspiration_badges_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If badge assets or certificate workflow are unavailable, block at Phase 0 or run a verbal appreciation activity without claiming a certificate is created.

**Round 2 -- Design The Badge:**

**Runtime AI instruction:** Guide a paper-and-pencil badge with one color and one kind phrase.

**Example AI line:** "Draw one big badge shape. What color should the award use?"

**Child responses:**

1. (Ideal) The child notices the award title or badge idea cue and suggests a fitting feeling, need, or kind action.
2. (Unexpected) Child judges the person/object, ignores the award title or badge idea cue, or offers help that does not fit the need.
3. (No response) Child watches the award title or badge idea cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness token, and show the calmer or helped state.
2. Reframe without judging, point to the cue for the award title or badge idea, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for the award title or badge idea, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `award_inspiration_badges_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If badge assets or certificate workflow are unavailable, block at Phase 0 or run a verbal appreciation activity without claiming a certificate is created.

**Round 3 -- Present The Award:**

**Runtime AI instruction:** Invite the child to show or describe the certificate.

**Example AI line:** "Can you tell me the award name, like Best Helper or Best Mom?"

**Child responses:**

1. (Ideal) The child notices the kind certificate message cue and suggests a fitting feeling, need, or kind action.
2. (Unexpected) Child judges the person/object, ignores the kind certificate message cue, or offers help that does not fit the need.
3. (No response) Child watches the kind certificate message cue without naming a feeling, need, or helpful action.

**AI follow-up:**

1. Connect the cue to the caring choice, save the kindness token, and show the calmer or helped state.
2. Reframe without judging, point to the cue for the kind certificate message, and offer two gentle help choices.
3. [wait 2s] Model one caring sentence for the kind certificate message, then ask the child to choose a feeling or help action.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `award_inspiration_badges_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If badge assets or certificate workflow are unavailable, block at Phase 0 or run a verbal appreciation activity without claiming a certificate is created.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the kind certificate message changed the Award Certificate board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Award Certificate payoff or ignores how the saved kind response turns connect.
3. (No response) Child watches the Award Certificate reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's kind response turns, name one concrete saved token, and invite a short reflection.
2. Hold the Award Certificate reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Award Certificate board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Responsibility. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Award Certificate moment, asks to play again, or watches the award certificate recap badge.
2. (Unexpected) Child shifts topic before the recap names the kind response skill or Form and Responsibility.
3. (No response) Child stays on the Award Certificate recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same care mechanic and the award certificate frame.
2. Close Award Certificate first, name the practiced kind response, and then offer one next-round seed.
3. [wait 2s] Read the Award Certificate badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `care`, focal attribute `award_certificate`, and next-step hint.
