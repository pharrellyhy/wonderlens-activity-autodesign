## B-Sound Treasure Collect

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | B-Sound Treasure Collect |
| Activity Category | 5 -- Collection/Tracking Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Function |
| Related Concepts | initial sound, spoken evidence, photo_id |
| ATL Skills Focus | listening, describing, evidence |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The child uses B-sound cards as clues, captures a real object, and says the object name for runtime judgment.

**2. Educational Purpose (KUD)**

- **K (Know):** Children can notice name begins with B sound through a concrete activity frame.
- **U (Understand):** The activity keeps the child action, evidence source, and support status aligned.
- **D (Do):** The child performs the promised collect action with one concrete response or evidence source.

**3. Design Highlight**

This package is part of a scoped E2E runtime validation subset. It is intentionally small so autodesign package quality, package-local assets, consumer import/conversion, and support gating can be verified without broadening into a full content batch.

**4. Typical Scenario**

The child follows the runtime prompt, the device uses only package-local assets declared by asset_id, and the consumer runtime either plays or gates the package according to demo_support.yaml.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Start The B-Sound Quest

**Runtime AI instruction:** Goal: frame the mission as collecting a real object whose spoken name starts like B. Constraint: T1 max two sentences; explain that the demo is degraded unless the child supplies name evidence. Tone: adventurous but precise. Progress evidence: child agrees, repeats B, or asks for examples. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: do not claim image-only judgment can hear letters; preserve spoken/name evidence requirement.

**Example AI line:** [adventurous] "We are hunting B-sound treasure. Your photo helps, and your object name proves it."

**Child responses:**
1. (Ideal) Child says B, agrees, or asks to see examples.
2. (Unexpected) Child wants the camera alone to decide the sound.
3. (No response) Child watches without answering.

**AI follow-up policy:**
1. (Ideal) [ready] "I will show B clues now."
2. (Unexpected) [explain] "A photo cannot hear a starting sound, so I need the object's name too."
3. (No response) [wait 2s] [model] "Ball starts like B. Let's look for one real B-name."

**Photo capture timing:** No photo before the clue cards appear.

**Screen/state:** Show empty treasure tray with degraded badge text in metadata only; prepare asset_ids ball, book, banana, and cup.

#### Step 2: Choose A B Clue

**Runtime AI instruction:** Goal: show B-sound clue cards and one non-B distractor so the child understands the criterion before capture. Constraint: one direct choice; avoid letters printed on screen because runtime assets contain no text. Tone: curious treasure-guide. Progress evidence: child chooses ball, book, banana, or names a B-sound object. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: cards guide the hunt and do not replace real capture or spoken object-name evidence.

**Example AI line:** [curious] "Ball, book, and banana are B treasures. Which kind should we look for nearby?"

**Child responses:**
1. (Ideal) Child chooses a B card or names a B object.
2. (Unexpected) Child chooses cup or another non-B item as the target.
3. (No response) Child does not choose.

**AI follow-up policy:**
1. (Ideal) [confirm] "Good. Now capture a real object and say its name."
2. (Unexpected) [teach] "Cup is our not-B clue. Choose ball, book, banana, or another B name."
3. (No response) [wait 2s] [scaffold] "Let's try ball. Find a real ball or another B thing."

**Photo capture timing:** Real camera capture happens after this clue choice and before Step 3.

**Screen/state:** Display asset_ids ball, book, banana, and cup as selectable visual clues; highlight the selected B-sound clue and keep a real photo slot empty.

#### Step 3: Judge The Captured Treasure

**Round 1 -- B-Sound Evidence Check:**

**Runtime AI instruction:** Goal: consume the captured photo_id and ask for the object name so runtime can judge B-sound evidence. Constraint: T1 max two sentences; do not accept until the child says or enters an object name. Tone: focused and encouraging. Progress evidence: child provides a real photo_id plus a spoken/name clue such as ball, book, banana, box, or bag. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: preserve degraded honesty: image data alone cannot decide the initial sound.

**Example AI line:** [focused] "Your photo is ready. What is the object called? I will listen for the B start."

**Child responses:**
1. (Ideal) Child names a B-starting object or clearly corrects the object name.
2. (Unexpected) Child says only 'this one' or gives a non-B name.
3. (No response) Child stays quiet after the photo appears.

**AI follow-up policy:**
1. (Ideal) [celebrate] "That name starts like B, so it counts as treasure."
2. (Unexpected) [repair] "I need the object name. If it is not a B name, choose a different treasure or say another name."
3. (No response) [wait 2s] [choice] "Is it ball, book, banana, or another B thing?"

**Photo capture timing:** Consumes the real photo captured after Step 2; the runtime stores photo_id and pairs it with child name evidence.

**Screen/state:** Show captured photo_id beside selected clue asset_id; keep the treasure uncollected until a B-name is supplied.

#### Step 4: Celebrate The B Evidence

**Runtime AI instruction:** Goal: celebrate the accepted B-sound evidence while naming the degraded support limit. Constraint: one or two short sentences; acknowledge the photo and the name evidence together. Tone: proud and transparent. Progress evidence: child hears that both photo_id and object name were used. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: do not imply the photo alone proved the sound.

**Example AI line:** [proud] "Collected: your real photo plus the name gave us the B-sound evidence."

**Child responses:**
1. (Ideal) Child repeats the B object name.
2. (Unexpected) Child asks why the picture was not enough.
3. (No response) Child is quiet after acceptance.

**AI follow-up policy:**
1. (Ideal) [warm] "That B-name is saved with the photo."
2. (Unexpected) [explain] "Pictures show shape and color, but the name tells us the starting sound."
3. (No response) [gentle] "I will save this B treasure."

**Photo capture timing:** No new photo in celebration.

**Screen/state:** Mark the selected B clue as collected and persist the captured photo_id thumbnail.

#### Step 5: Close The B-Sound Quest

**Runtime AI instruction:** Goal: recap the selected card, real photo, and name-based B-sound judgment. Constraint: max two sentences; no second capture. Tone: warm closing. Progress evidence: child says the object name, B, or listens silently. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: close with degraded support reasoning visible for reviewers.

**Example AI line:** [warm] "B-sound quest complete: clue card, real photo, and object name all stayed together."

**Child responses:**
1. (Ideal) Child repeats the object or B sound.
2. (Unexpected) Child asks to test a non-B item.
3. (No response) Child gives no closing response.

**AI follow-up policy:**
1. (Ideal) [close] "Treasure saved."
2. (Unexpected) [boundary] "A non-B test would be another round. This validation quest is done."
3. (No response) [quiet close] "I will close the treasure tray."

**Photo capture timing:** No new photo.

**Screen/state:** Show completed tray with selected B asset_id and photo_id thumbnail; end the session.
