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

**Runtime AI instruction:** Goal: frame the AI as hungry for treasures whose spoken names start with /b/. Constraint: T1 max two short sentences; pronounce /b/ by voice and do not require reading. Tone: playful and hungry. Progress evidence: child repeats /b/, agrees, asks for examples, or looks toward nearby objects. Branch behavior: if the child repeats /b/ or says yes, start the hunt; if the child points without naming, explain that the spoken name matters; if quiet, model ball as a B-starting example. Frame/source guardrail: the target sound is the collection criterion and visual cards only support the search.

**Example AI line:** [playful] "I am hungry for /b/ /b/ /b/ treasures. Can you find one real thing whose name starts like /b/?"

**Child responses:**
1. (Ideal) Child says "/b/", "I can find one", or asks "like ball?"
2. (Unexpected) Child points at an object but gives no name, or asks to just count toys.
3. (No response) Child watches the empty treasure tray without repeating the sound.

**AI follow-up policy:**
1. (Ideal) [ready] "Yes, that bouncy /b/ is our treasure sound. Now choose a clue before we search."
2. (Unexpected) [clarify] "Pointing helps me see, but the object name tells the starting sound. Listen for /b/ first."
3. (No response) [wait 2s] [model] "Ball starts like /b/. Can you say /b/ with me or tap the ball clue?"

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Empty treasure tray plus optional asset_ids ball_b_sound_clue and banana_b_sound_clue; no text or letters are required.
#### Step 2: Pick A Sound Clue

**Runtime AI instruction:** Goal: show or name B-sound examples before the real search. Constraint: one direct choice; do not let clue cards replace the real treasure. Tone: curious treasure-guide. Progress evidence: child chooses ball, banana, or names another B-starting object. Branch behavior: accept a B clue, treat a non-B choice as a boundary example, and scaffold with ball when quiet. Frame/source guardrail: the child must still find and photograph a real object and supply name evidence.

**Example AI line:** [curious] "Ball and banana start like /b/. Which clue should help our hunt?"

**Child responses:**
1. (Ideal) Child chooses ball, banana, or says another B word such as book or bag.
2. (Unexpected) Child chooses a non-B object such as cup, or says the card itself is already the treasure.
3. (No response) Child does not choose from the visible clue assets.

**AI follow-up policy:**
1. (Ideal) [confirm] "Good B clue. Now find a real one nearby and we will use its name."
2. (Unexpected) [teach] "Cup does not start like /b/. Pick ball, banana, book, bag, or another B-name treasure."
3. (No response) [scaffold] "Let us use the ball clue. Look for a real ball or another thing whose name starts /b/."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show the optional clue assets and an empty real-photo slot.
#### Step 3: Capture And Name The Treasure

**Round 1 -- B-Sound Evidence Check:**

**Runtime AI instruction:** Goal: ask the child to photograph a real object and say or enter its name for B-sound judgment. Constraint: T1 max two sentences; do not accept image-only evidence. Tone: focused and encouraging. Progress evidence: child provides photo_id plus a name such as ball, banana, bag, book, or box. Branch behavior: accept only photo plus B-starting name, keep non-B or missing names uncollected, and offer named choices after silence. Frame/source guardrail: preserve Cat5 collection and degraded honesty: runtime cannot infer initial phoneme from photo alone.

**Example AI line:** [focused] "Show me the real treasure, then tell me its name. I will listen for the /b/ start."

**Child responses:**
1. (Ideal) Child captures a real object and says "ball", "book", "banana", "bag", or another B-starting name.
2. (Unexpected) Child says "this one", gives only a photo, or names a non-B object such as cup.
3. (No response) A photo_id appears but the child gives no object name.

**AI follow-up policy:**
1. (Ideal) [accept] "Photo plus name: ball starts like /b/, so this can enter the tray."
2. (Unexpected) [repair] "I still need the object name. If the name is cup, it is not a /b/ treasure yet."
3. (No response) [wait 2s] [choice] "Is your photo a ball, banana, book, bag, or another /b/ thing?"

**Photo capture timing:** Real camera capture happens in this beat and is paired with child name evidence.

**Screen/state:** Show captured photo_id beside the chosen clue; keep treasure uncollected until a B-starting name is supplied.
#### Step 4: Name-Check The Treasure

**Round 2 -- B-Sound Name Check:**

**Runtime AI instruction:** Goal: separate the spoken/name evidence check from the photo capture so the runtime has a second concrete Cat5 round instead of inventing a generic collection prompt. Constraint: T1 max two short sentences; ask for or confirm the object name and keep the tray uncollected until a B-starting name is present. Tone: careful and encouraging. Progress evidence: child says a B-starting object name, corrects the name, or confirms one offered choice. Branch behavior: accept clear B names, repair non-B or vague names, and offer ball/banana/book/bag choices after silence. Frame/source guardrail: this round is name evidence for the same captured object, not a second photo hunt.

**Example AI line:** [careful] "Now tell me the treasure name. Does the name start with /b/, like ball, banana, book, or bag?"

**Child responses:**
1. (Ideal) Child says a B-starting name such as ball, banana, book, bag, box, or bear for the captured object.
2. (Unexpected) Child says "this", gives a non-B name such as cup, or tries to take another photo instead of naming the current object.
3. (No response) Child stays quiet while the captured photo_id waits beside the clue.

**AI follow-up policy:**
1. (Ideal) [accept] "That name starts with /b/, so this same photo can become B treasure."
2. (Unexpected) [repair] "We are checking the name for this photo. If the name is not a /b/ word, the tray stays open."
3. (No response) [choice] "Is it ball, banana, book, bag, or another name that starts with /b/?"

**Photo capture timing:** No new photo; this round uses the photo_id captured in Step 3.

**Screen/state:** Keep the same captured photo_id visible, show a pending name-check badge, and do not mark the clue collected until the B-starting name is accepted.
#### Step 5: Celebrate The Sound Match

**Round 1 -- Sound Match Celebration:**

**Runtime AI instruction:** Goal: celebrate the accepted real object and the spoken/name evidence together. Constraint: one or two short sentences; mention both photo and name. Tone: proud and transparent. Progress evidence: child hears why the item counted. Branch behavior: celebrate a valid B name, explain photo-only limits if challenged, and refuse celebration if valid name evidence is missing. Frame/source guardrail: do not imply the screen card or photo alone proved the sound.

**Example AI line:** [proud] "Collected: your real photo and the name both helped us hear the /b/ treasure."

**Child responses:**
1. (Ideal) Child repeats the accepted B name or the /b/ sound.
2. (Unexpected) Child asks why the picture alone did not prove the sound, or tries to celebrate a non-B name.
3. (No response) Child is quiet after the accepted name appears.

**AI follow-up policy:**
1. (Ideal) [celebrate] "Yes, that name starts with /b/, and your real photo is saved with it."
2. (Unexpected) [explain] "The picture shows the object, but the name tells the first sound; non-B names stay outside the tray."
3. (No response) [gentle] "I will save this B treasure with its photo and name evidence."

**Photo capture timing:** No new photo.

**Screen/state:** Mark the selected clue as collected and persist the photo_id thumbnail.
#### Step 6: Close The Treasure Tray

**Runtime AI instruction:** Goal: recap the target sound, real object search, photo, and name evidence. Constraint: max two short sentences; no second capture. Tone: warm closing. Progress evidence: child repeats the sound, object, or listens. Branch behavior: close with the saved B object, redirect requests for other sounds to a later hunt, and quietly save if no reply. Frame/source guardrail: keep the source promise as phoneme treasure hunt, not generic object counting.

**Example AI line:** [warm] "Treasure tray closed: you hunted for /b/, showed a real thing, and named it."

**Child responses:**
1. (Ideal) Child says the saved object name, repeats /b/, or says "treasure".
2. (Unexpected) Child asks to test a non-B object or switch to a different sound immediately.
3. (No response) Child gives no closing response.

**AI follow-up policy:**
1. (Ideal) [close] "Your /b/ treasure is saved: real photo, real name, same starting sound."
2. (Unexpected) [boundary] "That can be a new sound hunt later. This tray is only for our /b/ treasure."
3. (No response) [quiet close] "I will close the /b/ treasure tray now."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Completed tray with selected clue asset_id and photo_id thumbnail.
