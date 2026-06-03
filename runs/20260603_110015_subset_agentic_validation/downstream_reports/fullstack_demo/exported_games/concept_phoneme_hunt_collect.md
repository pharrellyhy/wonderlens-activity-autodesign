---
category: category_5
entity_name: beginning sound treasure
display_label: Beginning Sound Treasure
tier: T1
ib_theme: How We Express Ourselves
play_rounds: 3
plain_description: The target sound becomes the collection criterion; visual objects
  support but do not replace spoken or typed name evidence.
steps_summary:
- 'Goal: invite the child'
- 'Goal: explain the single'
- 'Goal: model the /b/'
- 'Goal: synthesize the visual'
- 'Goal: recap the child'
creative_slots:
  observation_angle: function
  collection_criterion: Things with beginning sound evidence
  collection_count: 3
  mission_metaphor: You are a Concept Phoneme Hunt Collect Explorer!
  role_title: Concept Phoneme Hunt Collect Explorer
  synthesis_type: naming_story
  stuck_hint: Look nearby for something with beginning sound evidence.
  naming_prompt: What would you name this find?
  detail_question_template: What do you notice about it?
  sorting_criterion: ''
step_instructions:
  hook:
    goal: 'Goal: invite the child into Phoneme Treasure Hunt from the trigger condition.
      Constraint: T1 max two short child-facing sentences; keep asset and capability
      claims honest. Tone: warm, specific, and playful. Progress evidence: child answer,
      child self-report, accepted photo_id, or quiet attention for the current beat.
      Branch behavior: ideal advances; unexpected validates then redirects to this
      beat; no response waits briefly, models one tiny answer, and keeps the child
      safe. Frame/source guardrail: preserve the source promise - AI introduces a
      target sound, then the child finds one indoor treasure whose word starts with
      that sound. Example line: "Let us start B-Sound Treasure Hunt. I will keep the
      rule simple." Screen/state behavior: Use `intro_scene`; app-owned progress,
      choices, or camera slots are overlays and are not baked into the PNG.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  transition:
    goal: 'Goal: explain the single activity rule and name what evidence counts. Constraint:
      T1 max two short child-facing sentences; keep asset and capability claims honest.
      Tone: warm, specific, and playful. Progress evidence: child answer, child self-report,
      accepted photo_id, or quiet attention for the current beat. Branch behavior:
      ideal advances; unexpected validates then redirects to this beat; no response
      waits briefly, models one tiny answer, and keeps the child safe. Frame/source
      guardrail: preserve the source promise - AI introduces a target sound, then
      the child finds one indoor treasure whose word starts with that sound. Example
      line: "Here is the rule: one small answer at a time, and I will help if it feels
      tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned
      visual context with no buttons, labels, or progress dots baked in.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  rounds:
  - round_number: 1
    goal: 'Goal: model the /b/ sound and show object examples without baked letters.
      Constraint: T1 max two short child-facing sentences; keep asset and capability
      claims honest. Tone: warm, specific, and playful. Progress evidence: child answer,
      child self-report, accepted photo_id, or quiet attention for the current beat.
      Branch behavior: ideal advances; unexpected validates then redirects to this
      beat; no response waits briefly, models one tiny answer, and keeps the child
      safe. Frame/source guardrail: preserve the source promise - AI introduces a
      target sound, then the child finds one indoor treasure whose word starts with
      that sound. Example line: "Listen: /b/ like ball. Can you say /b/ with me?"
      Screen/state behavior: Use `round_1_scene`, optional object sprites, and the
      text-free `b_sound_letter_cue` backing only if the app overlays the actual `/b/`
      or B cue separately.'
    scenario: Hear The Target Sound
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: focused
    acceptable_themes:
    - hear
    - the
    - target
    - sound
    escalation_note: Source round 1 from the package runtime flow.
  - round_number: 2
    goal: 'Goal: ask for one real photo_id of an indoor object whose spoken name starts
      with /b/. Constraint: T1 max two short child-facing sentences; keep asset and
      capability claims honest. Tone: warm, specific, and playful. Progress evidence:
      child answer, child self-report, accepted photo_id, or quiet attention for the
      current beat. Branch behavior: ideal advances; unexpected validates then redirects
      to this beat; no response waits briefly, models one tiny answer, and keeps the
      child safe. Frame/source guardrail: preserve the source promise - AI introduces
      a target sound, then the child finds one indoor treasure whose word starts with
      that sound. Example line: "Find one treasure that starts with /b/. Take its
      picture, then tell me its name." Screen/state behavior: Use `round_2_scene`;
      app camera slot is separate from the PNG.'
    scenario: Capture One Treasure
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: focused
    acceptable_themes:
    - ball
    - book
    - banana
    - box
    escalation_note: Source round 2 from the package runtime flow.
  - round_number: 3
    goal: 'Goal: judge the child-provided object name, not the image alone, and accept
      one B-sound treasure. Constraint: T1 max two short child-facing sentences; keep
      asset and capability claims honest. Tone: warm, specific, and playful. Progress
      evidence: child answer, child self-report, accepted photo_id, or quiet attention
      for the current beat. Branch behavior: ideal advances; unexpected validates
      then redirects to this beat; no response waits briefly, models one tiny answer,
      and keeps the child safe. Frame/source guardrail: preserve the source promise
      - AI introduces a target sound, then the child finds one indoor treasure whose
      word starts with that sound. Example line: "You said ball. Ball begins with
      /b/. Treasure found." Screen/state behavior: Use `round_3_scene`; app overlays
      accepted photo/name evidence separately.'
    scenario: Name Evidence Check
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: focused
    acceptable_themes:
    - name
    - evidence
    - check
    escalation_note: Source round 3 from the package runtime flow.
  celebrate:
    goal: 'Goal: synthesize the visual object and spoken name into a shared beginning-sound
      rule. Constraint: T1 max two short child-facing sentences; keep asset and capability
      claims honest. Tone: warm, specific, and playful. Progress evidence: child answer,
      child self-report, accepted photo_id, or quiet attention for the current beat.
      Branch behavior: ideal advances; unexpected validates then redirects to this
      beat; no response waits briefly, models one tiny answer, and keeps the child
      safe. Frame/source guardrail: preserve the source promise - AI introduces a
      target sound, then the child finds one indoor treasure whose word starts with
      that sound. Do not end with generic completion; synthesize the collected evidence
      into a rule, summary, or story payoff. Example line: "Your photo and word worked
      together: ball belongs because it begins with /b/." Screen/state behavior: Use
      `synthesis_scene`; app overlays the accepted photo separately.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: wonder
  closing:
    goal: 'Goal: recap the child action, source evidence, and key concept without
      adding a new task. Constraint: T1 max two short child-facing sentences; keep
      asset and capability claims honest. Tone: warm, specific, and playful. Progress
      evidence: child answer, child self-report, accepted photo_id, or quiet attention
      for the current beat. Branch behavior: ideal advances; unexpected validates
      then redirects to this beat; no response waits briefly, models one tiny answer,
      and keeps the child safe. Frame/source guardrail: preserve the source promise
      - AI introduces a target sound, then the child finds one indoor treasure whose
      word starts with that sound. Example line: "Today you practiced Form by using
      beginning sound evidence." Screen/state behavior: Use `closing_scene`; keep
      final state calm and free of baked badges, labels, buttons, or progress UI.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  early_exit:
    goal: Offer a gentle goodbye that validates whatever the child already tried.
    constraint: T1 max 2 sentences; no pressure to continue.
    emotion_tag: gentle
  synthesis:
    goal: 'Goal: synthesize the visual object and spoken name into a shared beginning-sound
      rule. Constraint: T1 max two short child-facing sentences; keep asset and capability
      claims honest. Tone: warm, specific, and playful. Progress evidence: child answer,
      child self-report, accepted photo_id, or quiet attention for the current beat.
      Branch behavior: ideal advances; unexpected validates then redirects to this
      beat; no response waits briefly, models one tiny answer, and keeps the child
      safe. Frame/source guardrail: preserve the source promise - AI introduces a
      target sound, then the child finds one indoor treasure whose word starts with
      that sound. Do not end with generic completion; synthesize the collected evidence
      into a rule, summary, or story payoff. Example line: "Your photo and word worked
      together: ball belongs because it begins with /b/." Screen/state behavior: Use
      `synthesis_scene`; app overlays the accepted photo separately.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: wonder
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
  widget_label: 'Find 1: Hear The Target Sound'
  animation_label: Progress update
- widget: progress_tracker
  widget_params:
    filled: 2
    total: 3
  animation: card_slide_in
  trigger: on_round_2
  sfx_cue: photo_shutter_click
  widget_label: 'Find 2: Capture One Treasure'
  animation_label: Progress update
- widget: progress_tracker
  widget_params:
    filled: 3
    total: 3
  animation: card_slide_in
  trigger: on_round_3
  sfx_cue: photo_shutter_click
  widget_label: 'Find 3: Name Evidence Check'
  animation_label: Progress update
celebration_frame:
  widget: badge_award
  widget_params:
    title: 'Goal: synthesize the visual'
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
- beginning sound evidence
feature_keywords:
- beginning sound evidence
photo_features:
- beginning sound evidence
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
activity_type: concept_phoneme_hunt_collect
collection_catalog:
  correct:
  - id: green_apple
    label: Matching placeholder 1
    image: /icons/green_apple.png
  - id: dandelion
    label: Matching placeholder 2
    image: /icons/dandelion.png
  - id: ladybug
    label: Matching placeholder 3
    image: /icons/ladybug.png
  - id: smooth_pebble
    label: Matching placeholder 4
    image: /icons/smooth_pebble.png
  distractors:
  - id: straight_stick
    label: Distractor placeholder 1
    image: /icons/straight_stick.png
  - id: plain_leaf
    label: Distractor placeholder 2
    image: /icons/plain_leaf.png
  - id: hard_rock
    label: Distractor placeholder 3
    image: /icons/hard_rock.png
  - id: spiky_pinecone
    label: Distractor placeholder 4
    image: /icons/spiky_pinecone.png
  - id: dry_leaf
    label: Distractor placeholder 5
    image: /icons/dry_leaf.png
  - id: smooth_stone
    label: Distractor placeholder 6
    image: /icons/smooth_stone.png
  - id: bare_twig
    label: Distractor placeholder 7
    image: /icons/bare_twig.png
  - id: brown_dirt
    label: Distractor placeholder 8
    image: /icons/brown_dirt.png
---

## B-Sound Treasure Hunt

### Runtime Package

Recommended tier: `T1`.

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: invite the child into Phoneme Treasure Hunt from the trigger condition. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "Let us start B-Sound Treasure Hunt. I will keep the rule simple." Screen/state behavior: Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.
**Example AI line:** [warm] "Let us start B-Sound Treasure Hunt. I will keep the rule simple."

**Child responses:**

1. (Ideal) child agrees or asks to play.
2. (Unexpected) child asks for a different game or gives an unrelated comment.
3. (No response) child looks at the screen or waits.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Name beat evidence.
3. [wait 2s] [gentle] Model one tiny answer.

**Screen/state:** Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.

#### Step 2: Rule Introduction

**Runtime AI instruction:** Goal: explain the single activity rule and name what evidence counts. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "Here is the rule: one small answer at a time, and I will help if it feels tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.
**Example AI line:** [warm] "Here is the rule: one small answer at a time, and I will help if it feels tricky."

**Child responses:**

1. (Ideal) child repeats the rule or says ready.
2. (Unexpected) child asks what counts or proposes a different rule.
3. (No response) child hesitates before starting.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Name beat evidence.
3. [wait 2s] [gentle] Model one tiny answer.

**Screen/state:** Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.

#### Step 3: Core Loop

**Round 1 -- Hear The Target Sound:**

**Runtime AI instruction:** Goal: model the /b/ sound and show object examples without baked letters. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "Listen: /b/ like ball. Can you say /b/ with me?" Screen/state behavior: Use `round_1_scene`, optional object sprites, and the text-free `b_sound_letter_cue` backing only if the app overlays the actual `/b/` or B cue separately.
**Example AI line:** [focused] "Listen: /b/ like ball. Can you say /b/ with me?"

**Child responses:**

1. (Ideal) child repeats /b/ or names ball/book/banana.
2. (Unexpected) child says a non-B word or asks for the letter.
3. (No response) child listens silently.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [redirect] Name round evidence.
3. [wait 2s] [gentle] Model one small move.

**Screen/state:** Use `round_1_scene`, optional object sprites, and the text-free `b_sound_letter_cue` backing only if the app overlays the actual `/b/` or B cue separately.

**Round 2 -- Capture One Treasure:**

**Runtime AI instruction:** Goal: ask for one real photo_id of an indoor object whose spoken name starts with /b/. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "Find one treasure that starts with /b/. Take its picture, then tell me its name." Screen/state behavior: Use `round_2_scene`; app camera slot is separate from the PNG.
**Example AI line:** [focused] "Find one treasure that starts with /b/. Take its picture, then tell me its name."

**Child responses:**

1. (Ideal) photo_id plus "ball", "book", "banana", "box", or similar.
2. (Unexpected) photo without name or non-B object name.
3. (No response) child searches without answering.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [redirect] Name round evidence.
3. [wait 2s] [gentle] Model one small move.

**Screen/state:** Use `round_2_scene`; app camera slot is separate from the PNG.

**Round 3 -- Name Evidence Check:**

**Runtime AI instruction:** Goal: judge the child-provided object name, not the image alone, and accept one B-sound treasure. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "You said ball. Ball begins with /b/. Treasure found." Screen/state behavior: Use `round_3_scene`; app overlays accepted photo/name evidence separately.
**Example AI line:** [focused] "You said ball. Ball begins with /b/. Treasure found."

**Child responses:**

1. (Ideal) child confirms the object name starts with /b/.
2. (Unexpected) child changes name or says a wrong sound.
3. (No response) child waits after photo capture.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [redirect] Name round evidence.
3. [wait 2s] [gentle] Model one small move.

**Screen/state:** Use `round_3_scene`; app overlays accepted photo/name evidence separately.

#### Step 4: Synthesis And Magic Moment

**Runtime AI instruction:** Goal: synthesize the visual object and spoken name into a shared beginning-sound rule. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound. Do not end with generic completion; synthesize the collected evidence into a rule, summary, or story payoff. Example line: "Your photo and word worked together: ball belongs because it begins with /b/." Screen/state behavior: Use `synthesis_scene`; app overlays the accepted photo separately.
**Example AI line:** [wonder] "Your photo and word worked together: ball belongs because it begins with /b/."

**Child responses:**

1. (Ideal) child names a shared rule, pattern, story link, or summary.
2. (Unexpected) child says the finds are different or chooses a favorite only.
3. (No response) child reviews the completed collection quietly.

**AI follow-up:**

1. [proud] Repeat the child's shared rule and connect it to all accepted finds.
2. [bridge] Agree that the finds differ, then ask for one same color, shape, place, sound, or kind.
3. [wait 2s] [model] Offer one source-safe synthesis such as "found today" only as a scaffold.

**Screen/state:** Use `synthesis_scene`; app overlays the accepted photo separately.

#### Step 5: Closing + Concepts

**Runtime AI instruction:** Goal: recap the child action, source evidence, and key concept without adding a new task. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "Today you practiced Form by using beginning sound evidence." Screen/state behavior: Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
**Example AI line:** [warm] "Today you practiced Form by using beginning sound evidence."

**Child responses:**

1. (Ideal) child says again, goodbye, or favorite part.
2. (Unexpected) child asks for a different topic.
3. (No response) child watches silently.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Name beat evidence.
3. [wait 2s] [gentle] Model one tiny answer.

**Screen/state:** Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
