# Career Decision Role Play

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Career Decision Role Play |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | logical_reasoning, observation, language_expression |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The AI makes the child the firefighter in a smoke-alarm scene, then asks simple safety decisions.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Career Decision Role Play.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `decide` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the activity-specific role, repeated action, ideal/unexpected/no-response branches, and honest visual fallback behavior.

**4. Typical Scenario**

The child plays Career Decision Role Play with career_decision_role_play as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open by naming the activity and child role and name the child's role in this activity.

**Example AI line:** "I have a small mission for us: Career Decision Role Play. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the firefighter role-player role, notices the starter cue, or names something connected to the firefighter alarm decision.
2. (Unexpected) Child asks for another game, starts the choice before the Career Decision Role Play mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Career Decision Role Play title prompt without taking the firefighter role-player role yet.

**AI follow-up:**

1. Name the firefighter role-player role, connect it to the starter cue, and preview the first choice.
2. Acknowledge the request, return to the Career Decision Role Play promise, and offer the smallest supported first action.
3. [wait 2s] Name the Career Decision Role Play role and first marker, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress markers. Optional support asset: `intro_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I invite a turn, you make one safety choice, and one marker lights up for each turn."

**Child responses:**

1. (Ideal) The child agrees to the choice loop for Career Decision Role Play or asks for the easiest version.
2. (Unexpected) Child tries to skip the firefighter alarm decision, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Career Decision Role Play rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Career Decision Role Play loop as AI prompt, child choice, saved marker, and show the first response slot.
2. Keep the rule tied to the firefighter alarm decision, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Career Decision Role Play rule in one sentence and ask for yes or the first chance to make a choice.

**Screen:** Shows the rule strip, current round marker, and asset/fallback note. Use `career_portrait_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If art is unavailable, describe the helper role by voice and avoid claiming the screen shows a person. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Firefighter Smoke Alarm Decision:**

**Runtime AI instruction:** Assign the profession first and keep the child inside the role.

**Example AI line:** "Today you are the firefighter. A smoke alarm is ringing. Should your team send help now?"

**Child responses:**

1. (Ideal) The child answers as the firefighter and decides whether the team sends help for the alarm.
2. (Unexpected) Child drops the firefighter role, names another job, or talks about alarms without making the dispatch decision.
3. (No response) Child stays with the firefighter alarm scene without choosing what the team does.

**AI follow-up:**

1. Confirm the firefighter decision, name the safety reason, and keep the alarm scenario moving.
2. Put the child back in the firefighter role, restate the smoke alarm problem, and offer send help now or check first as bounded choices.
3. [wait 2s] Model "As the firefighter, I send help," then ask for send help or wait/check.

**Screen:** Shows the active round marker, child response slot, and activity cue. Use `career_portrait_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If art is unavailable, describe the helper role by voice and avoid claiming the screen shows a person. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Firefighter Tool Decision:**

**Runtime AI instruction:** Ask for a tool choice inside the same work scenario.

**Example AI line:** "Firefighter, which tool fits this fire scene: water hose or cooking oil?"

**Child responses:**

1. (Ideal) The child chooses the water hose over cooking oil for the fire scene.
2. (Unexpected) Child picks an unsafe tool, leaves the firefighter role, or asks for a tool unrelated to the fire scene.
3. (No response) Child looks between the water hose and cooking oil choices without picking a tool.

**AI follow-up:**

1. Confirm the tool choice, say why it fits a firefighter, and place the tool marker beside the scene.
2. Keep the child in role, name the unsafe tool plainly, and return to the two visible choices.
3. [wait 2s] Say "Firefighters use water for fire," then ask for hose or oil.

**Screen:** Shows the active round marker, child response slot, and activity cue. Use `career_portrait_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If art is unavailable, describe the helper role by voice and avoid claiming the screen shows a person. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Firefighter First Safe Action:**

**Runtime AI instruction:** Ask what the professional checks before acting.

**Example AI line:** "Should the firefighter check that people are safe outside, or run inside alone?"

**Child responses:**

1. (Ideal) The child chooses the safer first action: check that people are outside.
2. (Unexpected) Child chooses to run inside alone, ignores the safety check, or talks about being brave instead of making the first-action choice.
3. (No response) Child is unsure about the safety choice and has not picked outside check or run inside.

**AI follow-up:**

1. Affirm the safety-first action, show the people-safe marker, and close the firefighter scenario.
2. Validate wanting to help, then restate that firefighters work with teams and ask for the safe first action: check people are safe outside or run inside alone.
3. [wait 2s] Model "I check people are safe first," then ask: should the firefighter check people are safe outside, or run inside alone?

**Screen:** Shows the active round marker, child response slot, and activity cue. Use `career_portrait_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If art is unavailable, describe the helper role by voice and avoid claiming the screen shows a person. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your choices filled the activity board: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the first safe firefighter action changed the Career Decision Role Play board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Career Decision Role Play payoff or ignores how the saved choice turns connect.
3. (No response) Child watches the Career Decision Role Play reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's choice turns, name one concrete saved marker, and invite a short reflection.
2. Hold the Career Decision Role Play reveal, name the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Career Decision Role Play board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Responsibility. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Career Decision Role Play moment, asks to play again, or watches the career decision recap badge.
2. (Unexpected) Child shifts topic before the recap names the choice skill or Form and Responsibility.
3. (No response) Child stays on the Career Decision Role Play recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same decide mechanic and the career decision frame.
2. Close Career Decision Role Play first, name the practiced choice, and then offer one next-round seed.
3. [wait 2s] Read the Career Decision Role Play badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `decide`, focal attribute `career_decision`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
