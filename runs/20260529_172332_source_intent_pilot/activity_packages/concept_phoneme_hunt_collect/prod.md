## Phoneme Treasure Hunt

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Phoneme Treasure Hunt |
| Activity Category | 5 -- Sound-Based Collection/Tracking Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Function |
| Related Concepts | initial sound, spoken evidence, photo evidence |
| ATL Skills Focus | listening, describing, evidence |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The child hears /b/, finds and photographs a real object whose word starts with /b/, then gives the object name as evidence.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The sound stays the collection rule. Object cards support the hunt, but the child still has to find a real treasure and provide name evidence.

**4. Typical Scenario**

Child hears the hungry /b/ mission, chooses a clue, photographs a real object, names it, and celebrates only when the name starts with /b/.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Open The Hungry Sound Quest

**Runtime AI instruction:** Goal: frame the AI as hungry for treasures whose spoken names start with /b/. Constraint: T1 max two short sentences; pronounce /b/ by voice and do not require reading. Tone: playful and hungry. Progress evidence: child repeats /b/, agrees, asks for examples, or looks toward nearby objects. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: the target sound is the collection criterion and visual cards only support the search.

**Example AI line:** [playful] "I am hungry for /b/ /b/ /b/ treasures. Can you find one real thing whose name starts like /b/?"

**Child responses:**
1. (Ideal) Child completes Phoneme Treasure Hunt / Step 1: Open The Hungry Sound Quest with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 1: Open The Hungry Sound Quest into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 1: Open The Hungry Sound Quest before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 1: Open The Hungry Sound Quest and move to the next preserved source step.
2. (Unexpected) [repair] For Step 1: Open The Hungry Sound Quest, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 1: Open The Hungry Sound Quest, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Empty treasure tray plus optional asset_ids ball_b_sound_clue and banana_b_sound_clue; no text or letters are required.
#### Step 2: Pick A Sound Clue

**Runtime AI instruction:** Goal: show or name B-sound examples before the real search. Constraint: one direct choice; do not let clue cards replace the real treasure. Tone: curious treasure-guide. Progress evidence: child chooses ball, banana, or names another B-starting object. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: the child must still find and photograph a real object and supply name evidence.

**Example AI line:** [curious] "Ball and banana start like /b/. Which clue should help our hunt?"

**Child responses:**
1. (Ideal) Child completes Phoneme Treasure Hunt / Step 2: Pick A Sound Clue with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 2: Pick A Sound Clue into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 2: Pick A Sound Clue before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 2: Pick A Sound Clue and move to the next preserved source step.
2. (Unexpected) [repair] For Step 2: Pick A Sound Clue, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 2: Pick A Sound Clue, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show the optional clue assets and an empty real-photo slot.
#### Step 3: Capture And Name The Treasure

**Round 1 -- B-Sound Evidence Check:**

**Runtime AI instruction:** Goal: ask the child to photograph a real object and say or enter its name for B-sound judgment. Constraint: T1 max two sentences; do not accept image-only evidence. Tone: focused and encouraging. Progress evidence: child provides photo_id plus a name such as ball, banana, bag, book, or box. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: preserve Cat5 collection and degraded honesty: runtime cannot infer initial phoneme from photo alone.

**Example AI line:** [focused] "Show me the real treasure, then tell me its name. I will listen for the /b/ start."

**Child responses:**
1. (Ideal) Child completes Phoneme Treasure Hunt / Step 3: Capture And Name The Treasure with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 3: Capture And Name The Treasure into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 3: Capture And Name The Treasure before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 3: Capture And Name The Treasure and move to the next preserved source step.
2. (Unexpected) [repair] For Step 3: Capture And Name The Treasure, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 3: Capture And Name The Treasure, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** Real camera capture happens in this beat and is paired with child name evidence.

**Screen/state:** Show captured photo_id beside the chosen clue; keep treasure uncollected until a B-starting name is supplied.
#### Step 4: Celebrate The Sound Match

**Round 1 -- Sound Match Celebration:**

**Runtime AI instruction:** Goal: celebrate the accepted real object and the spoken/name evidence together. Constraint: one or two short sentences; mention both photo and name. Tone: proud and transparent. Progress evidence: child hears why the item counted. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: do not imply the screen card or photo alone proved the sound.

**Example AI line:** [proud] "Collected: your real photo and the name both helped us hear the /b/ treasure."

**Child responses:**
1. (Ideal) Child completes Phoneme Treasure Hunt / Step 4: Celebrate The Sound Match with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 4: Celebrate The Sound Match into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 4: Celebrate The Sound Match before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 4: Celebrate The Sound Match and move to the next preserved source step.
2. (Unexpected) [repair] For Step 4: Celebrate The Sound Match, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 4: Celebrate The Sound Match, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No new photo.

**Screen/state:** Mark the selected clue as collected and persist the photo_id thumbnail.
#### Step 5: Close The Treasure Tray

**Runtime AI instruction:** Goal: recap the target sound, real object search, photo, and name evidence. Constraint: max two short sentences; no second capture. Tone: warm closing. Progress evidence: child repeats the sound, object, or listens. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: keep the source promise as phoneme treasure hunt, not generic object counting.

**Example AI line:** [warm] "Treasure tray closed: you hunted for /b/, showed a real thing, and named it."

**Child responses:**
1. (Ideal) Child completes Phoneme Treasure Hunt / Step 5: Close The Treasure Tray with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 5: Close The Treasure Tray into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 5: Close The Treasure Tray before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 5: Close The Treasure Tray and move to the next preserved source step.
2. (Unexpected) [repair] For Step 5: Close The Treasure Tray, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 5: Close The Treasure Tray, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Completed tray with selected clue asset_id and photo_id thumbnail.
