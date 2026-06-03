## B-Sound Treasure Hunt

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | B-Sound Treasure Hunt |
| Activity Category | Cat5 Collection/Tracking Exploration |
| Recommended Tier | T1, ages 4-6 |
| Core IB Key Concepts | Form, Connection |
| Related Concepts | sound, beginning sound, word-object match, evidence |
| ATL Skills Focus | listening (isolating the first sound), language expression (naming the object), evidence collection (photo plus spoken name) |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The AI introduces the target sound `/b/`, then invites the child to find one indoor treasure whose spoken word starts with that sound. The child shows or photographs the treasure and says its name so the AI can connect the object to the beginning sound.

**2. Educational Purpose (KUD)**

- **K (Know):** `/b/` is a beginning sound; words like ball, banana, book, and box can begin with `/b/`; a photo needs a spoken or typed name for sound evidence.
- **U (Understand):** A word can match an object through its beginning sound; one shared sound can connect different treasures.
- **D (Do):** Listen for a target sound; find one matching object; explain the sound evidence using the object's name.

**3. Design Highlight**

The child is not quizzed on letters. The game keeps the scavenger-hunt feeling: hear a sound, search the room, show one treasure, and see the AI turn the child's photo and word into a simple sound rule.

**4. Typical Scenario**

A child starts language treasure-hunt mode indoors, hears `/b/`, and searches for one real object such as a ball, banana, book, box, or bag.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: open from language treasure-hunt mode with a warm, non-testing hook and introduce that the device is hungry for one sound-treasure, not a worksheet answer. Constraint: T1, one or two short sentences; do not claim the image understands phonemes by itself. Tone: playful and inviting. Progress evidence: child says yes, looks ready, asks what sound, or stays with the screen. Branch behavior: if ready, move to the sound rule; if the child names a random object, admire the object and say the rule comes next; if silent, wait two seconds and model a tiny ready phrase. Frame/source guardrail: preserve the source frame that AI introduces `/b/` first, then the child finds one indoor treasure whose word starts with `/b/`; screen may show `intro_scene` only, with no baked letters, buttons, or progress UI.

**Example AI line:** [playful hunger] "My sound basket is hungry today. It wants one special treasure."

**Child responses:**

1. (Ideal) "I want to play" or "What sound?"
2. (Unexpected) "Here is my cup" before hearing the rule.
3. (No response) Child watches the intro scene but does not speak.

**AI follow-up:**

1. [warm launch] "Good listening ears on. I will give you the sound."
2. [gentle redirect] "A cup is a real treasure. First, listen for today's sound."
3. [wait 2s] [soft model] "You can say, 'I'm ready.'"

**Screen:** `intro_scene` shows a quiet indoor search corner with an empty soft basket and listening spark shapes. The app may overlay a small activity title outside the PNG; the PNG itself has no text, letters, progress dots, buttons, or camera slot.

#### Step 2: Target Sound Rule

**Runtime AI instruction:** Goal: model `/b/ /b/ /b/` and define the one-object collection rule before any child search. Constraint: T1, two short sentences; use sound language, not formal phonics testing. Tone: clear, rhythmic, and playful. Progress evidence: child repeats `/b/`, names a possible B word, asks for help, or attends quietly. Branch behavior: if the child repeats or names a B word, confirm the sound and advance; if the child gives a non-B word, validate the try and contrast the first mouth sound; if silent, repeat `/b/` slowly and offer one example. Frame/source guardrail: the optional `b_sound_letter_cue` is a text-free backing only; runtime may overlay `/b/` or B separately, and if no overlay exists the AI must use voice-only fallback.

**Example AI line:** [sound play] "Today's sound is /b/ /b/ /b/. Ball starts with /b/."

**Child responses:**

1. (Ideal) Child says "/b/" or names "ball," "book," or "banana."
2. (Unexpected) Child says "cup" or another non-B word.
3. (No response) Child listens but does not repeat.

**AI follow-up:**

1. [specific praise] "Yes. Your mouth popped the /b/ sound."
2. [kind contrast] "Cup starts with /k/. We need the pop-pop /b/ sound."
3. [wait 2s] [slow model] "Try just the first sound: /b/."

**Screen:** `rules_scene` shows a soft sound basket and simple listening shapes. If available, `b_sound_letter_cue` appears as a blank rounded cue backing while the app overlays the `/b/` cue separately; if the overlay is unavailable, the screen stays visual-only and the AI repeats the sound by voice.

#### Step 3: Multi-Round Interaction

**Round 1 -- Practice The Sound Before Searching:**

**Runtime AI instruction:** Goal: let the child rehearse the target sound once and hear two example B words before moving into the room search. Constraint: T1, no more than two short sentences; do not ask the child to read the letter. Tone: focused and playful. Progress evidence: child says `/b/`, names one example B word, or accepts the model. Branch behavior: if the child gives a B example, connect it to the sound; if the child says a non-B example, contrast only the first sound; if no response, give a call-and-response model and proceed gently. Frame/source guardrail: this is sound preparation, not the final find; `round_1_scene` can show abstract listening/search imagery and optional example object sprites only as app-owned overlays, not baked into the scene background.

**Example AI line:** [listening coach] "Say it with me: /b/. Ball and book both begin with /b/."

**Child responses:**

1. (Ideal) Child repeats "/b/" or says "banana."
2. (Unexpected) Child says "cup" because it is nearby.
3. (No response) Child looks around the room without speaking.

**AI follow-up:**

1. [bright confirmation] "Banana works. I heard the /b/ at the start."
2. [specific redirect] "Cup begins with /k/. Keep hunting for a /b/ beginning."
3. [wait 2s] [tiny scaffold] "I will start: /b/ like ball. Your turn if you want."

**Screen:** `round_1_scene` shows the blank cue backing and a small empty basket space. Any ball/book/banana examples appear only as separate item sprites or runtime overlays; the scene PNG itself avoids duplicate selectable objects and contains no letters or labels.

**Round 2 -- Find One Indoor Treasure:**

**Runtime AI instruction:** Goal: send the child to find exactly one indoor object whose spoken name starts with `/b/`, then show or photograph it. Constraint: T1, two short sentences; include safe indoor searching and do not require the AI to infer the phoneme from pixels alone. Tone: adventurous but calm. Progress evidence: child returns with a photo_id, holds up an object, or says they cannot find one. Branch behavior: if a candidate appears, ask for or accept the object name; if the child cannot find one, offer nearby B examples such as book, bag, box, ball, or banana; if silent, wait and give a small search area hint. Frame/source guardrail: this is the required scavenger-hunt action; keep it to one treasure and keep camera UI separate from `round_2_scene`.

**Example AI line:** [quest guide] "Find one treasure that starts with /b/. Take its picture, then tell me its name."

**Child responses:**

1. (Ideal) Child returns with photo_id and says "book" or "ball."
2. (Unexpected) Child says "I cannot find one" or brings a cup.
3. (No response) Child keeps searching and does not answer.

**AI follow-up:**

1. [evidence check] "I see your treasure. Now tell me its name."
2. [helpful clue] "Look for book, bag, box, ball, or banana. One is enough."
3. [wait 2s] [safe nudge] "Try looking on a table or shelf first."

**Screen:** `round_2_scene` shows an open indoor path and empty collection basket, leaving the app camera preview and capture slot outside the PNG. No selectable object sprites are baked into the scene background.

**Round 3 -- Name And Accept The Match:**

**Runtime AI instruction:** Goal: judge the child-provided object name against the `/b/` beginning sound and accept one matching treasure. Constraint: T1, two short sentences; do not use OCR, image-only phoneme inference, or harsh correction. Tone: precise, delighted, and low-pressure. Progress evidence: child says or enters a candidate name and, when available, has shown a photo_id. Branch behavior: if the name begins with `/b/`, accept it and prepare synthesis; if it does not, validate the search and invite one retry or voice-only example; if no name arrives, ask one naming prompt before judging. Frame/source guardrail: sound evidence comes from the child's word, not from reading text in the photo; app overlays accepted photo/name evidence separately from `round_3_scene`.

**Example AI line:** [delighted evidence] "You said book. Book begins with /b/. Treasure found."

**Child responses:**

1. (Ideal) Child names "book," "ball," "banana," "box," or "bag."
2. (Unexpected) Child says "cup" after photographing a cup.
3. (No response) Child shows the object but does not name it.

**AI follow-up:**

1. [clear accept] "Yes. Your word starts with /b/, so it goes in the basket."
2. [kind repair] "Cup is a good find, but it starts with /k/. Want to try book or bag?"
3. [wait 2s] [naming prompt] "Tell me the treasure's name first, then I can hear the sound."

**Screen:** `round_3_scene` shows a single soft acceptance glow and empty basket area. The app may overlay the accepted photo and name evidence; the PNG has no text, labels, progress markers, or picker slots.

#### Step 4: Synthesis And Magic Moment

**Runtime AI instruction:** Goal: turn the accepted photo and object name into the shared beginning-sound rule, making the child's evidence feel earned. Constraint: T1, two short sentences; no new required search task. Tone: proud wonder. Progress evidence: accepted B-word treasure with child-provided name. Branch behavior: if the child repeats the rule, celebrate it; if the child focuses only on the object, connect object plus sound; if silent, model the rule once. Frame/source guardrail: synthesize the source promise rather than ending with generic completion; `synthesis_scene` must not reveal extra target objects or duplicate picker sprites.

**Example AI line:** [proud wonder] "Your photo and word worked together. Book belongs because it begins with /b/."

**Child responses:**

1. (Ideal) Child says "It starts with /b/" or repeats the object name.
2. (Unexpected) Child says "I like my book" without naming the sound.
3. (No response) Child watches the synthesis screen.

**AI follow-up:**

1. [celebrating rule] "Exactly. You found the beginning-sound connection."
2. [bridge to evidence] "Yes, your book matters. Its first sound is /b/."
3. [wait 2s] [gentle model] "Our rule was: one treasure, one /b/ beginning."

**Screen:** `synthesis_scene` shows one abstract treasure shape joining a soft sound wave into the basket. The accepted photo remains an app overlay if available; the generated scene does not bake in the photo, letters, labels, or extra example objects.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Goal: celebrate the child first, then name Form and Connection as the ideas practiced through sound evidence. Constraint: T1, two short sentences; no fresh challenge. Tone: warm celebration. Progress evidence: completed one-treasure `/b/` hunt or honest fallback path. Branch behavior: if the child says goodbye or wants another sound, close and name the next-step idea; if the child asks to continue, offer a caregiver-safe future round without starting it; if no response, close softly. Frame/source guardrail: recap the exact source action: AI introduced `/b/`, child found one indoor treasure, child named it, and the AI connected word to beginning sound; use `celebrate_scene` briefly for the praise moment, then `closing_scene` for the calm close.

**Example AI line:** [warm celebration] "You were a Sound Treasure Finder. You used Form and Connection to match book with /b/."

**Child responses:**

1. (Ideal) Child says "again," "bye," or repeats the B word.
2. (Unexpected) Child asks for a different sound immediately.
3. (No response) Child stays quiet after the celebration.

**AI follow-up:**

1. [happy close] "Next time we can hunt a new sound."
2. [future bridge] "A new sound can be our next mission after a little break."
3. [wait 2s] [soft goodbye] "Thanks for showing me your /b/ treasure."

**Screen:** `celebrate_scene` appears first as a short sparkle around the completed sound basket. Then `closing_scene` shows the basket resting calmly with one abstract treasure glow. Any badge, recap chip, or next activity control is app-owned UI and is not baked into either image.
