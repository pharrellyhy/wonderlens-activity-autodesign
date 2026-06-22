# Guided Drawing

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Guided Drawing |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Change |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | creative_thinking, observation, language_expression |
| Experience Pillar | Creation |
| Game Style | inventor_workshop |

### B. Activity Overview

**1. Brief Description**

The AI guides the child to use paper and pencil to complete a simple drawing step by step.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Guided Drawing.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `build` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the activity-specific role, three paper drawing steps, final photo capture, ideal/unexpected/no-response branches, and honest visual fallback behavior. WonderLens AI does not verify drawing correctness in this minimal Cat1 adaptation.

**4. Typical Scenario**

The child draws on paper while WonderLens gives three short steps, then takes one final photo so the session has reviewable evidence.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open by naming the activity and child role and name the child's role in this activity.

**Example AI line:** "I have a small mission for us: Guided Drawing. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts the guided artist role, notices the starter cue, or names something connected to the first line or shape.
2. (Unexpected) Child asks for another game, starts the making step before the Guided Drawing mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Guided Drawing title prompt without taking the guided artist role yet.

**AI follow-up:**

1. Name the guided artist role, connect it to the starter cue, and preview the first making step.
2. Acknowledge the request, return to the Guided Drawing promise, and offer the smallest supported first action.
3. [wait 2s] Name the Guided Drawing role and first step, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress markers. Optional support asset: `intro_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop, require a done/not-yet confirmation after each drawing step, and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one drawing step, you try it, then you tell me yes or not yet before we move on."

**Child responses:**

1. (Ideal) The child agrees to the making step loop for Guided Drawing, repeats the done/not-yet rule, or asks for the easiest version.
2. (Unexpected) Child tries to skip the first line or shape, ignore the confirmation rule/asset, or count a different kind of response.
3. (No response) Child looks at the Guided Drawing rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Guided Drawing loop as AI prompt, child making step, child done/not-yet confirmation, saved step, and show the first response slot.
2. Keep the rule tied to the first line or shape, name the supported fallback, and offer one allowed first turn with yes/not-yet confirmation.
3. [wait 2s] Read the Guided Drawing rule in one sentence and ask for yes or not yet before starting the first making step.

**Screen:** Shows the rule strip, current round marker, and asset/fallback note. Use `guided_drawing_step_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If step art is unavailable, use voice-only step descriptions and still ask for a final photo. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Big Circle Starter:**

**Runtime AI instruction:** Preserve the workbook promise: guide the child to use paper and pencil to complete a simple drawing step by step. Ask only for step 1: draw one big circle, then ask the child to confirm yes/done or not yet before moving on.

**Example AI line:** "Let us start with one big circle. Draw one big circle on your paper. Are you done with this step? Say yes or not yet."

**Child responses:**

1. (Ideal) The child confirms the big circle step is done after trying it.
2. (Unexpected) Child says not yet, skips the big circle, changes the target, or asks the AI to complete the drawing for them.
3. (No response) Child stays with the big circle prompt without confirming whether the step is done.

**AI follow-up:**

1. Confirm the done signal, save the big circle step, and cue the next build step.
2. If not yet, wait and re-offer the same small step; if off-track, restate the one required big circle step and ask for yes or not yet.
3. [wait 2s] Model the smallest possible big circle step, then ask: "Are you done with this step, yes or not yet?"

**Screen:** Shows the active round marker, child response slot, and activity cue. Use `guided_drawing_step_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If step art is unavailable, use voice-only step descriptions and still ask for a final photo. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Ears Or Petals:**

**Runtime AI instruction:** Keep the same source frame and ask only for step 2: add two small ears or petals to the circle, then ask the child to confirm yes/done or not yet before moving on.

**Example AI line:** "Now add two small ears or petals to your circle. Are you done with this step? Say yes or not yet."

**Child responses:**

1. (Ideal) The child confirms the ears-or-petals step is done after trying it.
2. (Unexpected) Child says not yet, skips the ears or petals, changes the target, or asks the AI to complete the drawing for them.
3. (No response) Child stays with the ears-or-petals prompt without confirming whether the step is done.

**AI follow-up:**

1. Confirm the done signal, save the ears-or-petals step, and cue the final build step.
2. If not yet, wait and re-offer the same small step; if off-track, restate the two small ears or petals step and ask for yes or not yet.
3. [wait 2s] Model two tiny ears or petals, then ask: "Are you done with this step, yes or not yet?"

**Screen:** Shows the active round marker, child response slot, and activity cue. Use `guided_drawing_step_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If step art is unavailable, use voice-only step descriptions and still ask for a final photo. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Face Or Finishing Detail:**

**Runtime AI instruction:** Ask only for step 3: add one face/detail, then ask the child to confirm yes/done or not yet before the activity treats the drawing as finished.

**Example AI line:** "Last step: add one face or tiny detail. Are you done with this step? Say yes or not yet."

**Child responses:**

1. (Ideal) The child confirms the face-or-detail step is done after trying it.
2. (Unexpected) Child says not yet, skips the face/detail, changes the target, or asks the AI to complete the drawing for them.
3. (No response) Child stays with the face/detail prompt without confirming whether the step is done.

**AI follow-up:**

1. Confirm the done signal, save the finished detail, and cue the Guided Artist celebration.
2. If not yet, wait and re-offer the same small step; if off-track, restate the one face/detail step and ask for yes or not yet.
3. [wait 2s] Model one tiny face or detail, then ask: "Are you done with this step, yes or not yet?"

**Screen:** Shows the active round marker, child response slot, and activity cue. Use `guided_drawing_step_cards_01` in `round_device_screen` during prod.step_2; prod.step_3.round_1-3; fallback: If step art is unavailable, use voice-only step descriptions and still ask for a final photo. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Magic Moment

**Runtime AI instruction:** Ask the child to take one photo of the finished paper drawing, preserve the resulting `photo_id`, and celebrate the three saved drawing steps without judging drawing correctness.

**Example AI line:** "Now take one photo of your drawing. I will save the picture and celebrate your three steps."

**Child responses:**

1. (Ideal) The child takes a final photo, says the drawing is done, or names a favorite saved step.
2. (Unexpected) Child asks the AI to judge whether the drawing is correct, restarts before the photo, or changes the activity.
3. (No response) Child watches the final photo prompt without capturing yet.

**AI follow-up:**

1. Save the `photo_id`, name the three steps, and invite a short reflection.
2. Explain that WonderLens saves the photo but does not grade the drawing, then ask for one final capture.
3. [wait 2s] Model the action: "Point the camera at your paper," then ask for one photo or a done signal.

**Screen:** Shows the final photo capture prompt, saved step markers, and celebration badge. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Change. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Guided Drawing moment, asks to play again, or watches the guided drawing recap badge.
2. (Unexpected) Child shifts topic before the recap names the making step skill or Form and Change.
3. (No response) Child stays on the Guided Drawing recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same build mechanic and the guided drawing frame.
2. Close Guided Drawing first, name the practiced making step, and then offer one next-round seed.
3. [wait 2s] Read the Guided Drawing badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `build`, focal attribute `guided_drawing`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
