# Emotion Reader

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Emotion Reader |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | empathy, observation, language_expression |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The child reads the feeling shown in each picture, then reflects on a caring response after the feeling is named.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Emotion Reader.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `care` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the picture sequence, hidden feeling targets, ideal/unexpected/no-response branches, honest visual fallback behavior, and transcript verification before advancing.

**4. Typical Scenario**

The child plays Emotion Reader with emotion_reader as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Rules

**Runtime AI instruction:** Say exactly: "Each picture shows a feeling. Read the feeling you see." Do not ask a question here.

**Example AI line:** "Each picture shows a feeling. Read the feeling you see."

**Child responses:**

1. (Ideal) The child understands that each answer should name the feeling shown in the picture.
2. (Unexpected) Child tries to skip the visible face or body clue, ignore the required rule/asset, or answer with unrelated help.
3. (No response) Child looks at the Emotion Reader rule without responding.

**AI follow-up:**

1. Restate the Emotion Reader loop as picture clue, feeling answer, and saved turn.
2. Keep the rule tied to the visible face or body clue, name the supported fallback, and do not count any response yet.
3. [wait 2s] Say the Emotion Reader rule in one sentence, then continue to Round 1.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `emotion_expression_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Multi-Round Core Loop

**Round 1 -- Picture 1:**

**Runtime AI instruction:** Ask what feeling the child sees in this picture. Do not name the target feeling or body clue before the child answers.

**Example AI line:** "What feeling do you see in this picture?"

**Child responses:**

1. (Ideal) The child names the target feeling or a close feeling and may add a caring response.
2. (Unexpected) Child judges the character, gives generic kindness without reading the feeling, or names a different picture's feeling.
3. (No response) Child watches the picture without naming a feeling.

**AI follow-up:**

1. Acknowledge the feeling the child named, save the turn, and ask the next picture without naming its answer.
2. Reframe without judging and ask the child to look again at the face and body for a feeling.
3. [wait 2s] Ask a short neutral feeling question again without naming the answer.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `emotion_expression_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. Do not ask the child to point, tap, or touch the screen. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Picture 2:**

**Runtime AI instruction:** Ask what feeling the child sees in this picture. Do not name the target feeling or body clue before the child answers.

**Example AI line:** "What feeling fits this picture?"

**Child responses:**

1. (Ideal) The child names the target feeling or a close feeling and may add a caring response.
2. (Unexpected) Child judges the character, gives generic kindness without reading the feeling, or names a different picture's feeling.
3. (No response) Child watches the picture without naming a feeling.

**AI follow-up:**

1. Acknowledge the feeling the child named, save the turn, and ask the next picture without naming its answer.
2. Reframe without judging and ask the child to look again at the face and body for a feeling.
3. [wait 2s] Ask a short neutral feeling question again without naming the answer.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `emotion_expression_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. Do not ask the child to point, tap, or touch the screen. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Picture 3:**

**Runtime AI instruction:** Ask what feeling the child sees in this picture. Do not name the target feeling or body clue before the child answers.

**Example AI line:** "What feeling do you read in this picture?"

**Child responses:**

1. (Ideal) The child names the target feeling or a close feeling and may add a caring response.
2. (Unexpected) Child judges the character, gives generic kindness without reading the feeling, or names a different picture's feeling.
3. (No response) Child watches the picture without naming a feeling.

**AI follow-up:**

1. Acknowledge the feeling the child named, save the turn, and move to the saved-feelings board.
2. Reframe without judging and ask the child to look again at the face and body for a feeling.
3. [wait 2s] Ask a short neutral feeling question again without naming the answer.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `emotion_expression_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If cards are unavailable, use a story description of a character's visible cues and avoid claiming the screen shows a face. Do not ask the child to point, tap, or touch the screen. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Magic Moment

**Runtime AI instruction:** Say exactly: "You read three feelings and chose caring words."

**Example AI line:** "You read each picture and saved a caring word."

**Child responses:**

1. (Ideal) The child notices how reading the feelings changed the Emotion Reader board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Emotion Reader payoff or ignores how the saved feeling turns connect.
3. (No response) Child watches the Emotion Reader reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's feeling-reading turns and invite a short reflection.
2. Hold the Emotion Reader reveal, name the reading skill, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Emotion Reader board, then ask which feeling was easiest to read.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Closing + IB Concepts

**Runtime AI instruction:** Say exactly: "You noticed feeling clues and chose caring help."

**Example AI line:** "You noticed clues and chose caring help. We can read a new feeling next time."

**Child responses:**

1. (Ideal) The child names a favorite Emotion Reader moment, asks to play again, or watches the emotion reader recap badge.
2. (Unexpected) Child shifts topic before the recap names the kind response skill or Form and Responsibility.
3. (No response) Child stays on the Emotion Reader recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same care mechanic and the emotion reader frame.
2. Close Emotion Reader first, name the practiced kind response, and then offer one next-round seed.
3. [wait 2s] Read the Emotion Reader badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `care`, focal attribute `emotion_reader`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
