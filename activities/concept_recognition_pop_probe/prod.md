# Recognition Pop Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Recognition Pop Challenge |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | observation, observation, language_expression |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The child quickly types or names the picture that matches a red apple target from fixed changing sets with blue car, strawberry, cherries, and basketball distractors.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Recognition Pop Challenge.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `compare` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the activity-specific role, repeated action, ideal/unexpected/no-response branches, and honest visual fallback behavior.

**4. Typical Scenario**

The child plays Recognition Pop Challenge with recognition_pop_challenge as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open by naming the activity and child role and name the child's role in this activity.

**Example AI line:** "I have a small mission for us: Recognition Pop Challenge. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the quick match spotter role, notices the starter cue, or names something connected to the first target picture.
2. (Unexpected) Child asks for another game, starts the comparison choice before the Recognition Pop Challenge mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Recognition Pop Challenge title and start cue without taking the quick match spotter role yet.

**AI follow-up:**

1. Name the quick match spotter role, connect it to the starter cue, and preview the first comparison choice.
2. Acknowledge the request, return to the Recognition Pop Challenge promise, and offer the smallest supported first action.
3. [wait 2s] Name the Recognition Pop Challenge role and the first picture, then gently model one tiny response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens. Optional support asset: `intro_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Here is how it works: I ask, you tell me your match, and we light up one spot for each turn."

**Child responses:**

1. (Ideal) The child agrees to the comparison choice loop for Recognition Pop Challenge or asks for the easiest version.
2. (Unexpected) Child tries to skip the first target picture, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Recognition Pop Challenge rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Recognition Pop Challenge flow as AI asks, child names a match, one spot lights up, and show the first response slot.
2. Keep the rule tied to the first target picture, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Recognition Pop Challenge rule in one sentence and ask for yes or one word about the visible options.

**Screen:** Shows the rule strip, current round token, and tap/select recognition cards. Use `recognition_challenge_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If card art is unavailable, use text labels and ask the child to tap or say the matching choice. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Red Apple Target With Blue Car Distractor:**

**Runtime AI instruction:** Preserve the asset promise: the target is a red apple and the first distractor is a blue car. Ask the child to type the matching red apple choice.

**Example AI line:** "The target is a red apple. Which choice matches it: red apple or blue car?"

**Child responses:**

1. (Ideal) The child compares the visible options for the first target picture and chooses or explains one.
2. (Unexpected) Child responds to only one side of the first target picture, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the first target picture options without choosing or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the first target picture, then ask for the matching picture name or a short description.
3. [wait 2s] Name one difference in the first target picture, model a choice, and invite one word or short description.

**Screen:** Shows the active round token, child response slot, and tap/select recognition cards. Use `recognition_challenge_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If card art is unavailable, use text labels and ask the child to tap or say the matching choice. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Red Apple Target With Strawberry And Cherries:**

**Runtime AI instruction:** Keep the asset promise: the target remains a red apple and the close distractors are strawberry and cherries. Invite the child to tell you their comparison in words.

**Example AI line:** "Now compare red apple with strawberry and cherries. Which one is the best match, and what looks different?"

**Child responses:**

1. (Ideal) The child compares the visible options for the new target among distractors and chooses or explains one.
2. (Unexpected) Child responds to only one side of the new target among distractors, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the new target among distractors options without choosing or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the new target among distractors, then ask for the matching picture name or a short description.
3. [wait 2s] Name one difference in the new target among distractors, model a choice, and invite one word or short description.

**Screen:** Shows the active round token, child response slot, and tap/select recognition cards. Use `recognition_challenge_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If card art is unavailable, use text labels and ask the child to tap or say the matching choice. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Red Apple Target With Basketball Distractor:**

**Runtime AI instruction:** Keep the asset promise: the target is a red apple and the final distractor is basketball. Ask for the red apple match plus one form clue.

**Example AI line:** "Last pop: red apple or basketball. Which matches the target, and what clue helped?"

**Child responses:**

1. (Ideal) The child compares the visible options for the final match rule and chooses or explains one.
2. (Unexpected) Child responds to only one side of the final match rule, changes the comparison rule, or talks about an option that is not visible.
3. (No response) Child looks between the final match rule options without choosing or naming a difference.

**AI follow-up:**

1. Name the comparison evidence, save the selected option, and keep the next comparison state clear.
2. Restate the two visible options and the comparison lens for the final match rule, then ask for the matching picture name or a short description.
3. [wait 2s] Name one difference in the final match rule, model a choice, and invite one word or short description.

**Screen:** Shows the active round token, child response slot, and tap/select recognition cards. Use `recognition_challenge_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If card art is unavailable, use text labels and ask the child to tap or say the matching choice. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your choices filled the activity board: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the final match rule changed the Recognition Pop Challenge board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Recognition Pop Challenge payoff or ignores how the saved comparison choice turns connect.
3. (No response) Child watches the Recognition Pop Challenge reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's comparison choice turns, name one concrete saved match, and invite a short reflection.
2. Hold the Recognition Pop Challenge reveal, name the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Recognition Pop Challenge board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Perspective. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Recognition Pop Challenge moment, asks to play again, or watches the whack a mole recognition recap badge.
2. (Unexpected) Child shifts topic before the recap names the comparison choice skill or Form and Perspective.
3. (No response) Child stays on the Recognition Pop Challenge recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same compare mechanic and the whack a mole recognition frame.
2. Close Recognition Pop Challenge first, name the practiced comparison choice, and then offer one next-round seed.
3. [wait 2s] Read the Recognition Pop Challenge badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `compare`, focal attribute `whack_a_mole_recognition`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
