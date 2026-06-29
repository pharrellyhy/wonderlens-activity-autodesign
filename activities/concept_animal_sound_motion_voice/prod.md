# Animal Sound Imitation

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Animal Sound Imitation |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Perspective |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | language_expression, observation, language_expression |
| Experience Pillar | Performance |
| Game Style | voice_stage |

### B. Activity Overview

**1. Brief Description**

The AI uses a fixed rabbit, cat meow, and puppy card sequence, and the child imitates each sound or speaks in that animal role.

**2. Educational Purpose (KUD)**

- **K (Know):** The child knows the visible rule or clue that starts Animal Sound Imitation.
- **U (Understand):** The child understands that each answer changes the next activity beat.
- **D (Do):** The child completes three short `motion_voice` turns and explains one piece of evidence.

**3. Runtime Fidelity Notes**

Runtime wording should adapt naturally, but it must preserve the fixed rabbit, cat, and puppy sequence, verify the transcript against the active animal target before advancing, and keep honest visual fallback behavior.

**4. Typical Scenario**

The child plays Animal Sound Imitation with animal_sound_imitation as the bound activity entity and package-local visual assets on the round WonderLens screen.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Rules

**Runtime AI instruction:** Say only that we will copy rabbit, cat, then puppy softly. Do not ask for a sound here.

**Example AI line:** "We'll copy three animal cards softly: rabbit, cat, then puppy."

**Child responses:**

1. (Ideal) The child understands that each animal turn must stay safe, small, and tied to the active animal.
2. (Unexpected) Child tries to skip the first animal voice, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Animal Sound Imitation rule without responding.

**AI follow-up:**

1. Restate the Animal Sound Imitation loop as active animal, small safe voice or movement, and saved turn.
2. Keep the rule tied to the first animal voice, name the supported fallback, and do not count any response yet.
3. [wait 2s] Say the Animal Sound Imitation rule in one sentence, then continue to Round 1.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `animal_sound_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Multi-Round Core Loop

**Round 1 -- Rabbit Card Voice:**

**Runtime AI instruction:** Ask directly for one tiny rabbit sniff or "I am a rabbit." Do not add scenario labels.

**Example AI line:** "Rabbit first. Make one tiny sniff, or say, 'I am a rabbit.'"

**Child responses:**

1. (Ideal) The child tries the first animal voice with safe volume, space, or body control.
2. (Unexpected) Child makes the first animal voice too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the first animal voice cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the first animal voice, save the performance turn, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the first animal voice.
3. [wait 2s] Demonstrate the smallest safe version of the first animal voice, then invite the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `animal_sound_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Cat Meow Voice Or Volume:**

**Runtime AI instruction:** Ask directly for one soft cat meow or "I am a cat." Do not add scenario labels.

**Example AI line:** "Cat next. Give one soft meow, or say, 'I am a cat.'"

**Child responses:**

1. (Ideal) The child tries the changed animal voice or volume with safe volume, space, or body control.
2. (Unexpected) Child makes the changed animal voice or volume too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the changed animal voice or volume cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the changed animal voice or volume, save the performance turn, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the changed animal voice or volume.
3. [wait 2s] Demonstrate the smallest safe version of the changed animal voice or volume, then invite the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `animal_sound_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Puppy Role Line:**

**Runtime AI instruction:** Ask directly for one friendly puppy woof or "I am a puppy." Do not add scenario labels.

**Example AI line:** "Puppy last. Give one friendly woof, or say, 'I am a puppy.'"

**Child responses:**

1. (Ideal) The child tries the favorite animal-role line with safe volume, space, or body control.
2. (Unexpected) Child makes the favorite animal-role line too rough/loud, switches to an unrelated performance, or proposes an unsafe movement.
3. (No response) Child watches the favorite animal-role line cue without moving, sounding, or choosing a smaller version.

**AI follow-up:**

1. Mirror the safe part of the favorite animal-role line, save the performance turn, and cue the next variation.
2. Name the safety boundary, shrink the action to a safer version, and invite one controlled try for the favorite animal-role line.
3. [wait 2s] Demonstrate the smallest safe version of the favorite animal-role line, then invite the child to copy just that part.

**Screen:** Shows the active round token, child response slot, and activity cue. Use `animal_sound_cards_01` in `round_device_screen` during prod.step_1; prod.step_2.round_1-3; fallback: If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Magic Moment

**Runtime AI instruction:** Recap only the three animal turns: rabbit sniff, cat meow, and puppy woof.

**Example AI line:** "I saved your rabbit sniff, cat meow, and puppy woof on the board."

**Child responses:**

1. (Ideal) The child notices how the favorite animal-role line changed the Animal Sound Imitation board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Animal Sound Imitation payoff or ignores how the saved safe sound or movement turns connect.
3. (No response) Child watches the Animal Sound Imitation reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's safe sound or movement turns, name one concrete saved turn, and invite a short reflection.
2. Hold the Animal Sound Imitation reveal, name the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Animal Sound Imitation board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Closing + IB Concepts

**Runtime AI instruction:** Close by saying the child used their voice three ways: rabbit, cat, and puppy.

**Example AI line:** "You used your voice three ways: rabbit, cat, and puppy."

**Child responses:**

1. (Ideal) The child names a favorite Animal Sound Imitation moment, asks to play again, or watches the animal sound imitation recap badge.
2. (Unexpected) Child shifts topic before the recap names the safe sound or movement skill or Form and Perspective.
3. (No response) Child stays on the Animal Sound Imitation recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same motion_voice mechanic and the animal sound imitation frame.
2. Close Animal Sound Imitation first, name the practiced safe sound or movement, and then offer one next-round seed.
3. [wait 2s] Read the Animal Sound Imitation badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `motion_voice`, focal attribute `animal_sound_imitation`, and next-step hint. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
