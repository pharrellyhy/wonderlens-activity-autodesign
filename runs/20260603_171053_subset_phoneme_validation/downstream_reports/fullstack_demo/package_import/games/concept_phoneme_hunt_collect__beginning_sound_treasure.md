---
activity_type: concept_phoneme_hunt_collect__beginning_sound_treasure
activity_set: activity_text_game
source_export_id: concept_phoneme_hunt_collect
mechanic: collect
category: category_5
entity_name: beginning sound treasure
display_label: Beginning Sound Treasure
tier: T1
ib_theme: How We Express Ourselves
play_rounds: 3
plain_description: The AI introduces the target sound `/b/`, then invites the child
  to find one indoor treasure whose spoken word starts with that sound. The child
  shows or photographs the treasure and says its name so the AI can connect the object
  to the beginning sound.
steps_summary:
- 'Goal: open from language'
- 'Goal: model `/b/ /b/'
- 'Goal: let the child'
- 'Goal: turn the accepted'
- 'Goal: celebrate the child'
creative_slots:
  observation_angle: function
  collection_criterion: Things whose spoken names begin with the /b/ sound
  collection_count: 1
  mission_metaphor: You are a Concept Phoneme Hunt Collect Explorer!
  role_title: Concept Phoneme Hunt Collect Explorer
  synthesis_type: naming_story
  stuck_hint: Look nearby for something whose spoken name begins with /b/.
  naming_prompt: What would you name this find?
  detail_question_template: What do you notice about it?
  sorting_criterion: ''
step_instructions:
  hook:
    goal: 'Goal: open from language treasure-hunt mode with a warm, non-testing hook
      and introduce that the device is ready for one sound-treasure, not a worksheet
      answer. Constraint: T1, one or two short sentences; do not claim the image understands
      phonemes by itself. Tone: playful and inviting. Progress evidence: child says
      yes, looks ready, asks what sound, or stays with the screen. Branch behavior:
      if ready, move to the sound rule; if the child names a random object, admire
      the object and say the rule comes next; if silent, wait two seconds and model
      a tiny ready phrase. Frame/source guardrail: preserve the source frame that
      AI introduces `/b/` first, then the child finds one indoor treasure whose word
      starts with `/b/`; screen may show `intro_scene` only, with no baked letters,
      buttons, or progress UI.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: playful
  transition:
    goal: 'Goal: model `/b/ /b/ /b/` and define the one-object collection rule before
      any child search. Constraint: T1, two short sentences; use sound language, not
      formal phonics testing. Tone: clear, rhythmic, and playful. Progress evidence:
      child repeats `/b/`, names a possible B word, asks for help, or attends quietly.
      Branch behavior: if the child repeats or names a B word, confirm the sound and
      advance; if the child gives a non-B word, validate the try and contrast the
      first mouth sound; if silent, repeat `/b/` slowly and offer one example. Frame/source
      guardrail: the optional `b_sound_letter_cue` is a text-free backing only; runtime
      may overlay `/b/` or B separately, and if no overlay exists the AI must use
      voice-only fallback.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: sound
  rounds:
  - round_number: 1
    goal: 'Goal: let the child rehearse the target sound once and hear two example
      B words before moving into the room search. Constraint: T1, no more than two
      short sentences; do not ask the child to read the letter. Tone: focused and
      playful. Progress evidence: child says `/b/`, names one example B word, or accepts
      the model. Branch behavior: if the child gives a B example, connect it to the
      sound; if the child says a non-B example, contrast only the first sound; if
      no response, give a call-and-response model and proceed gently. Frame/source
      guardrail: this is sound preparation, not the final find; `round_1_scene` can
      show abstract listening/search imagery and optional example object sprites only
      as app-owned overlays, not baked into the scene background.'
    scenario: Practice The Sound Before Searching
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: listening
    acceptable_themes:
    - b
    - banana
    escalation_note: Source round 1 from the package runtime flow.
  - round_number: 2
    goal: 'Goal: send the child to find exactly one indoor object whose spoken name
      starts with `/b/`, then show or photograph it. Constraint: T1, two short sentences;
      include safe indoor searching and do not require the AI to infer the phoneme
      from pixels alone. Tone: adventurous but calm. Progress evidence: child returns
      with a photo_id, holds up an object, or says they cannot find one. Branch behavior:
      if a candidate appears, ask for or accept the object name; if the child cannot
      find one, offer nearby B examples such as book, bag, box, ball, or banana; if
      silent, wait and give a small search area hint. Frame/source guardrail: this
      is the required scavenger-hunt action; keep it to one treasure and keep camera
      UI separate from `round_2_scene`.'
    scenario: Find One Indoor Treasure
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: quest
    acceptable_themes:
    - book
    - ball
    escalation_note: Source round 2 from the package runtime flow.
  - round_number: 3
    goal: 'Goal: judge the child-provided object name against the `/b/` beginning
      sound and accept one matching treasure. Constraint: T1, two short sentences;
      do not use OCR, image-only phoneme inference, or harsh correction. Tone: precise,
      delighted, and low-pressure. Progress evidence: child says or enters a candidate
      name and, when available, has shown a photo_id. Branch behavior: if the name
      begins with `/b/`, accept it and prepare synthesis; if it does not, validate
      the search and invite one retry or voice-only example; if no name arrives, ask
      one naming prompt before judging. Frame/source guardrail: sound evidence comes
      from the child''s word, not from reading text in the photo; app overlays accepted
      photo/name evidence separately from `round_3_scene`.'
    scenario: Name And Accept The Match
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: delighted
    acceptable_themes:
    - book
    - ball
    - banana
    - box
    - bag
    escalation_note: Source round 3 from the package runtime flow.
  celebrate:
    goal: 'Goal: turn the accepted photo and object name into the shared beginning-sound
      rule, making the child''s evidence feel earned. Constraint: T1, two short sentences;
      no new required search task. Tone: proud wonder. Progress evidence: accepted
      B-word treasure with child-provided name. Branch behavior: if the child repeats
      the rule, celebrate it; if the child focuses only on the object, connect object
      plus sound; if silent, model the rule once. Frame/source guardrail: synthesize
      the source promise rather than ending with generic completion; `synthesis_scene`
      must not reveal extra target objects or duplicate picker sprites.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: proud
  closing:
    goal: 'Goal: celebrate the child first, then name Form and Connection as the ideas
      practiced through sound evidence. Constraint: T1, two short sentences; no fresh
      challenge. Tone: warm celebration. Progress evidence: completed one-treasure
      `/b/` hunt or honest fallback path. Branch behavior: if the child says goodbye
      or wants another sound, close and name the next-step idea; if the child asks
      to continue, offer a caregiver-safe future round without starting it; if no
      response, close softly. Frame/source guardrail: recap the exact source action:
      AI introduced `/b/`, child found one indoor treasure, child named it, and the
      AI connected word to beginning sound; use `celebrate_scene` briefly for the
      praise moment, then `closing_scene` for the calm close.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  early_exit:
    goal: Offer a gentle goodbye that validates whatever the child already tried.
    constraint: T1 max 2 sentences; no pressure to continue.
    emotion_tag: gentle
  synthesis:
    goal: 'Goal: turn the accepted photo and object name into the shared beginning-sound
      rule, making the child''s evidence feel earned. Constraint: T1, two short sentences;
      no new required search task. Tone: proud wonder. Progress evidence: accepted
      B-word treasure with child-provided name. Branch behavior: if the child repeats
      the rule, celebrate it; if the child focuses only on the object, connect object
      plus sound; if silent, model the rule once. Frame/source guardrail: synthesize
      the source promise rather than ending with generic completion; `synthesis_scene`
      must not reveal extra target objects or duplicate picker sprites.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: proud
screen_frames:
- widget: photo_display
  widget_params:
    description: Source photo centered as the activity anchor
  animation: sparkle_highlight
  trigger: on_enter
  sfx_cue: wonder_chime
  widget_label: Source Photo
  animation_label: Sparkle highlight
- widget: progress_tracker
  widget_params:
    filled: 1
    total: 3
  animation: card_slide_in
  trigger: on_round_1
  sfx_cue: photo_shutter_click
  widget_label: 'Find 1: Practice The Sound Before Searching'
  animation_label: Progress update
- widget: progress_tracker
  widget_params:
    filled: 2
    total: 3
  animation: card_slide_in
  trigger: on_round_2
  sfx_cue: photo_shutter_click
  widget_label: 'Find 2: Find One Indoor Treasure'
  animation_label: Progress update
- widget: progress_tracker
  widget_params:
    filled: 3
    total: 3
  animation: card_slide_in
  trigger: on_round_3
  sfx_cue: photo_shutter_click
  widget_label: 'Find 3: Name And Accept The Match'
  animation_label: Progress update
celebration_frame:
  widget: badge_award
  widget_params:
    title: 'Goal: turn the accepted'
  animation: badge_reveal
  trigger: on_correct
  sfx_cue: badge_awarded
  widget_label: Badge Earned
  animation_label: Badge reveal
pillar: Adventure
game_style: quest_collector
ib_key_concept: Form
concepts_earned:
- Form
- Connection
keywords:
- beginning sound treasure
- beginning_b_sound
- spoken_word
feature_keywords:
- beginning_b_sound
- spoken_word
photo_features:
- beginning_b_sound
- spoken_word
story_scaffold:
  premise: Each collected find becomes part of one shared discovery story.
  harvest_per_round: character_detail
  harvest_question_strategy: Ask one concrete detail question for each find, then
    reuse the child's own words.
  synthesis_goal: Connect the collected finds into a short child-led story.
  story_themes:
  - The finds meet and solve a small problem together
  synthesis_format: collaborative_story
synthesis_format: collaborative_story
activity_type: concept_phoneme_hunt_collect__beginning_sound_treasure
collection_catalog:
  correct:
  - id: ball_object
    label: Ball
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/ball_object__round_512.png
  - id: banana_object
    label: Banana
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/banana_object__round_512.png
  - id: book_object
    label: Book
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/book_object__round_512.png
  - id: box_object
    label: Box
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/box_object__round_512.png
  distractors:
  - id: cup_object
    label: Cup
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/cup_object__round_512.png
  - id: sock_object
    label: Sock
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/sock_object__round_512.png
  - id: apple_object
    label: Apple
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/apple_object__round_512.png
  - id: car_object
    label: Car
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/car_object__round_512.png
  - id: hat_object
    label: Hat
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/hat_object__round_512.png
  - id: mug_object
    label: Mug
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/mug_object__round_512.png
  - id: shoe_object
    label: Shoe
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/shoe_object__round_512.png
  - id: spoon_object
    label: Spoon
    image: /activity-assets/concept_phoneme_hunt_collect__beginning_sound_treasure/spoon_object__round_512.png
---

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

**Runtime AI instruction:** Goal: open from language treasure-hunt mode with a warm, non-testing hook and introduce that the device is ready for one sound-treasure, not a worksheet answer. Constraint: T1, one or two short sentences; do not claim the image understands phonemes by itself. Tone: playful and inviting. Progress evidence: child says yes, looks ready, asks what sound, or stays with the screen. Branch behavior: if ready, move to the sound rule; if the child names a random object, admire the object and say the rule comes next; if silent, wait two seconds and model a tiny ready phrase. Frame/source guardrail: preserve the source frame that AI introduces `/b/` first, then the child finds one indoor treasure whose word starts with `/b/`; screen may show `intro_scene` only, with no baked letters, buttons, or progress UI.

**Example AI line:** [playful launch] "My listening lens is ready today. It wants one special sound treasure."

**Child responses:**

1. (Ideal) "I want to play" or "What sound?"
2. (Unexpected) "Here is my cup" before hearing the rule.
3. (No response) Child watches the intro scene but does not speak.

**AI follow-up:**

1. [warm launch] "Good listening ears on. I will give you the sound."
2. [gentle redirect] "A cup is a real treasure. First, listen for today's sound."
3. [wait 2s] [soft model] "You can say, 'I'm ready.'"

**Screen:** `intro_scene` shows the child in a plausible indoor search room listening to the device before the sound is named. The app may overlay a small activity title outside the PNG; the PNG itself has no text, letters, progress dots, buttons, or camera slot.

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

**Screen:** `rules_scene` shows the child practicing the beginning sound with mouth/speech cues and sound waves moving toward the device. If available, `b_sound_letter_cue` appears as a text-free listening tile while the app overlays the `/b/` cue separately; if the overlay is unavailable, the screen stays visual-only and the AI repeats the sound by voice.

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

**Screen:** `round_1_scene` shows the child rehearsing the target sound before searching. Any ball/book/banana/box examples appear only as separate item sprites or runtime overlays; the scene PNG itself avoids duplicate selectable objects and contains no letters or labels.

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

**Screen:** `round_2_scene` shows the child safely searching the room with a subtle sound-wave trail, leaving the app camera preview and capture slot outside the PNG. No selectable object sprites are baked into the scene background.

**Round 3 -- Name And Accept The Match:**

**Runtime AI instruction:** Goal: judge the child-provided object name against the `/b/` beginning sound and accept one matching treasure. Constraint: T1, two short sentences; do not use OCR, image-only phoneme inference, or harsh correction. Tone: precise, delighted, and low-pressure. Progress evidence: child says or enters a candidate name and, when available, has shown a photo_id. Branch behavior: if the name begins with `/b/`, accept it and prepare synthesis; if it does not, validate the search and invite one retry or voice-only example; if no name arrives, ask one naming prompt before judging. Frame/source guardrail: sound evidence comes from the child's word, not from reading text in the photo; app overlays accepted photo/name evidence separately from `round_3_scene`.

**Example AI line:** [delighted evidence] "You said book. Book begins with /b/. Treasure found."

**Child responses:**

1. (Ideal) Child names "book," "ball," "banana," "box," or "bag."
2. (Unexpected) Child says "cup" after photographing a cup.
3. (No response) Child shows the object but does not name it.

**AI follow-up:**

1. [clear accept] "Yes. Your word starts with /b/, so it counts for our sound hunt."
2. [kind repair] "Cup is a good find, but it starts with /k/. Want to try book or bag?"
3. [wait 2s] [naming prompt] "Tell me the treasure's name first, then I can hear the sound."

**Screen:** `round_3_scene` shows the child naming the found object toward the device, with a neutral evidence area where the app may overlay the accepted photo and name evidence; the PNG has no text, labels, progress markers, or picker slots.

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

**Screen:** `synthesis_scene` shows sound-wave evidence connecting the child's word to the beginning-sound pattern. The accepted photo remains an app overlay if available; the generated scene does not bake in the photo, letters, labels, or extra example objects.

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

**Screen:** `celebrate_scene` appears first as a short sound-wave celebration around the child and device. Then `closing_scene` shows the same room calming down with the sound-wave ribbon fading. Any badge, recap chip, or next activity control is app-owned UI and is not baked into either image.
