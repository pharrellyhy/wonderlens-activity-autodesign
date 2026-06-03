---
category: category_1
entity_name: dog-like target picture
display_label: Dog-Like Target Picture
tier: T1
ib_theme: How The World Works
play_rounds: 3
plain_description: The child compares changing pictures against a target rule; target
  and distractor sprites are separate from scene backgrounds.
steps_summary:
- 'Goal: invite the child'
- 'Goal: explain the single'
- 'Goal: introduce the target'
- 'Goal: celebrate the completed'
- 'Goal: recap the child'
creative_slots:
  game_mechanic: true_or_silly
  metaphor: A guided Concept Recognition Pop Probe activity.
  role_title: Concept Recognition Pop
  round_scenarios:
  - Learn The Target Rule
  - Compare One Distractor
  - Pop The Target Again
  escalation_axis: simple to more complex
  observation_detail: the target versus distractor recognition details
step_instructions:
  hook:
    goal: 'Goal: invite the child into Recognition Pop Challenge from the trigger
      condition. Constraint: T1 max two short child-facing sentences; keep asset and
      capability claims honest. Tone: warm, specific, and playful. Progress evidence:
      child answer, child self-report, target response, or quiet attention for the
      current beat. Branch behavior: ideal advances; unexpected validates then redirects
      to this beat; no response waits briefly, models one tiny answer, and keeps the
      child safe. Frame/source guardrail: preserve the source promise - After a source
      object such as dog, the device shows changing target and distractor pictures
      and the child responds only when the target appears. Example line: "Let us start
      Recognition Pop Challenge. I will keep the rule simple." Screen/state behavior:
      Use `intro_scene`; app-owned progress, choices, or camera slots are overlays
      and are not baked into the PNG.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  transition:
    goal: 'Goal: explain the single activity rule and name what evidence counts. Constraint:
      T1 max two short child-facing sentences; keep asset and capability claims honest.
      Tone: warm, specific, and playful. Progress evidence: child answer, child self-report,
      target response, or quiet attention for the current beat. Branch behavior: ideal
      advances; unexpected validates then redirects to this beat; no response waits
      briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail:
      preserve the source promise - After a source object such as dog, the device
      shows changing target and distractor pictures and the child responds only when
      the target appears. Example line: "Here is the rule: one small answer at a time,
      and I will help if it feels tricky." Screen/state behavior: Use `rules_scene`;
      show only source-aligned visual context with no buttons, labels, or progress
      dots baked in.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  rounds:
  - round_number: 1
    goal: 'Goal: introduce the target picture and the stay-quiet rule for distractors.
      Constraint: T1 max two short child-facing sentences; keep asset and capability
      claims honest. Tone: warm, specific, and playful. Progress evidence: child answer,
      child self-report, target response, or quiet attention for the current beat.
      Branch behavior: ideal advances; unexpected validates then redirects to this
      beat; no response waits briefly, models one tiny answer, and keeps the child
      safe. Frame/source guardrail: preserve the source promise - After a source object
      such as dog, the device shows changing target and distractor pictures and the
      child responds only when the target appears. Example line: "When the dog target
      appears, say dog. If another animal appears, stay quiet." Screen/state behavior:
      Use `round_1_scene` plus `dog_target`; background contains no duplicate animals.'
    scenario: Learn The Target Rule
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: focused
    acceptable_themes:
    - learn
    - the
    - target
    - rule
    escalation_note: Source round 1 from the package runtime flow.
  - round_number: 2
    goal: 'Goal: show one visually similar distractor and ask the child to stay quiet
      or say not dog. Constraint: T1 max two short child-facing sentences; keep asset
      and capability claims honest. Tone: warm, specific, and playful. Progress evidence:
      child answer, child self-report, target response, or quiet attention for the
      current beat. Branch behavior: ideal advances; unexpected validates then redirects
      to this beat; no response waits briefly, models one tiny answer, and keeps the
      child safe. Frame/source guardrail: preserve the source promise - After a source
      object such as dog, the device shows changing target and distractor pictures
      and the child responds only when the target appears. Example line: "This one
      is not the dog target. Quiet eyes ready." Screen/state behavior: Use `round_2_scene`
      plus one distractor sprite; background remains abstract.'
    scenario: Compare One Distractor
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: focused
    acceptable_themes:
    - compare
    - one
    - distractor
    escalation_note: Source round 2 from the package runtime flow.
  - round_number: 3
    goal: 'Goal: return the target and require the target response after contrast.
      Constraint: T1 max two short child-facing sentences; keep asset and capability
      claims honest. Tone: warm, specific, and playful. Progress evidence: child answer,
      child self-report, target response, or quiet attention for the current beat.
      Branch behavior: ideal advances; unexpected validates then redirects to this
      beat; no response waits briefly, models one tiny answer, and keeps the child
      safe. Frame/source guardrail: preserve the source promise - After a source object
      such as dog, the device shows changing target and distractor pictures and the
      child responds only when the target appears. Example line: "Target is back.
      Say dog!" Screen/state behavior: Use `round_3_scene` plus `dog_target`; app
      owns timing and tap state.'
    scenario: Pop The Target Again
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: focused
    acceptable_themes:
    - pop
    - the
    - target
    - again
    escalation_note: Source round 3 from the package runtime flow.
  celebrate:
    goal: 'Goal: celebrate the completed source-aligned sequence and name what the
      child caused. Constraint: T1 max two short child-facing sentences; keep asset
      and capability claims honest. Tone: warm, specific, and playful. Progress evidence:
      child answer, child self-report, target response, or quiet attention for the
      current beat. Branch behavior: ideal advances; unexpected validates then redirects
      to this beat; no response waits briefly, models one tiny answer, and keeps the
      child safe. Frame/source guardrail: preserve the source promise - After a source
      object such as dog, the device shows changing target and distractor pictures
      and the child responds only when the target appears. Example line: "You made
      the activity work by doing the steps in order." Screen/state behavior: Use `celebrate_scene`;
      if reference or object assets remain visible, they are separate runtime layers.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  closing:
    goal: 'Goal: recap the child action, source evidence, and key concept without
      adding a new task. Constraint: T1 max two short child-facing sentences; keep
      asset and capability claims honest. Tone: warm, specific, and playful. Progress
      evidence: child answer, child self-report, target response, or quiet attention
      for the current beat. Branch behavior: ideal advances; unexpected validates
      then redirects to this beat; no response waits briefly, models one tiny answer,
      and keeps the child safe. Frame/source guardrail: preserve the source promise
      - After a source object such as dog, the device shows changing target and distractor
      pictures and the child responds only when the target appears. Example line:
      "Today you practiced Form by using target versus distractor recognition." Screen/state
      behavior: Use `closing_scene`; keep final state calm and free of baked badges,
      labels, buttons, or progress UI.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  early_exit:
    goal: Offer a gentle goodbye that validates whatever the child already tried.
    constraint: T1 max 2 sentences; no pressure to continue.
    emotion_tag: gentle
screen_frames:
- widget: photo_display
  widget_params:
    description: Source photo centered as the activity anchor
  animation: sparkle_highlight
  trigger: on_enter
  sfx_cue: wonder_chime
  widget_label: Source Photo
  animation_label: Sparkle highlight
- widget: character_display
  widget_params:
    description: Learn The Target Rule
  animation: scene_transition
  trigger: on_round_1
  sfx_cue: scene_woosh
  widget_label: 'Round 1: Learn The Target Rule'
  animation_label: Scene transition
- widget: character_display
  widget_params:
    description: Compare One Distractor
  animation: scene_transition
  trigger: on_round_2
  sfx_cue: scene_woosh
  widget_label: 'Round 2: Compare One Distractor'
  animation_label: Scene transition
- widget: character_display
  widget_params:
    description: Pop The Target Again
  animation: scene_transition
  trigger: on_round_3
  sfx_cue: scene_woosh
  widget_label: 'Round 3: Pop The Target Again'
  animation_label: Scene transition
celebration_frame:
  widget: badge_award
  widget_params:
    title: 'Goal: celebrate the completed'
  animation: badge_reveal
  trigger: on_correct
  sfx_cue: badge_awarded
  widget_label: Badge Earned
  animation_label: Badge reveal
pillar: Mystery
game_style: mystery_lens
ib_key_concept: Form
concepts_earned:
- Form
- Connection
keywords:
- dog-like target picture
- target versus distractor recognition
feature_keywords:
- target versus distractor recognition
photo_features:
- target versus distractor recognition
activity_type: concept_recognition_pop_probe
---

## Recognition Pop Challenge

### Runtime Package

Recommended tier: `T1`.

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: invite the child into Recognition Pop Challenge from the trigger condition. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, target response, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "Let us start Recognition Pop Challenge. I will keep the rule simple." Screen/state behavior: Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.
**Example AI line:** [warm] "Let us start Recognition Pop Challenge. I will keep the rule simple."

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

**Runtime AI instruction:** Goal: explain the single activity rule and name what evidence counts. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, target response, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "Here is the rule: one small answer at a time, and I will help if it feels tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.
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

**Round 1 -- Learn The Target Rule:**

**Runtime AI instruction:** Goal: introduce the target picture and the stay-quiet rule for distractors. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, target response, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "When the dog target appears, say dog. If another animal appears, stay quiet." Screen/state behavior: Use `round_1_scene` plus `dog_target`; background contains no duplicate animals.
**Example AI line:** [focused] "When the dog target appears, say dog. If another animal appears, stay quiet."

**Child responses:**

1. (Ideal) child says dog for the target rule.
2. (Unexpected) child wants to say dog for every picture.
3. (No response) child watches the target sprite.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [redirect] Name round evidence.
3. [wait 2s] [gentle] Model one small move.

**Screen/state:** Use `round_1_scene` plus `dog_target`; background contains no duplicate animals.

**Round 2 -- Compare One Distractor:**

**Runtime AI instruction:** Goal: show one visually similar distractor and ask the child to stay quiet or say not dog. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, target response, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "This one is not the dog target. Quiet eyes ready." Screen/state behavior: Use `round_2_scene` plus one distractor sprite; background remains abstract.
**Example AI line:** [focused] "This one is not the dog target. Quiet eyes ready."

**Child responses:**

1. (Ideal) child stays quiet or says not dog.
2. (Unexpected) child says dog for the distractor.
3. (No response) child watches without response.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [redirect] Name round evidence.
3. [wait 2s] [gentle] Model one small move.

**Screen/state:** Use `round_2_scene` plus one distractor sprite; background remains abstract.

**Round 3 -- Pop The Target Again:**

**Runtime AI instruction:** Goal: return the target and require the target response after contrast. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, target response, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "Target is back. Say dog!" Screen/state behavior: Use `round_3_scene` plus `dog_target`; app owns timing and tap state.
**Example AI line:** [focused] "Target is back. Say dog!"

**Child responses:**

1. (Ideal) child says dog once.
2. (Unexpected) child taps many times or names a distractor.
3. (No response) child misses the target turn.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [redirect] Name round evidence.
3. [wait 2s] [gentle] Model one small move.

**Screen/state:** Use `round_3_scene` plus `dog_target`; app owns timing and tap state.

#### Step 4: Magic Moment

**Runtime AI instruction:** Goal: celebrate the completed source-aligned sequence and name what the child caused. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, target response, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "You made the activity work by doing the steps in order." Screen/state behavior: Use `celebrate_scene`; if reference or object assets remain visible, they are separate runtime layers.
**Example AI line:** [warm] "You made the activity work by doing the steps in order."

**Child responses:**

1. (Ideal) child reacts, repeats, or smiles.
2. (Unexpected) child asks to change the result or asks for another round.
3. (No response) child quietly watches the celebration.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Name beat evidence.
3. [wait 2s] [gentle] Model one tiny answer.

**Screen/state:** Use `celebrate_scene`; if reference or object assets remain visible, they are separate runtime layers.

#### Step 5: Closing + Concepts

**Runtime AI instruction:** Goal: recap the child action, source evidence, and key concept without adding a new task. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, target response, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "Today you practiced Form by using target versus distractor recognition." Screen/state behavior: Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
**Example AI line:** [warm] "Today you practiced Form by using target versus distractor recognition."

**Child responses:**

1. (Ideal) child says again, goodbye, or favorite part.
2. (Unexpected) child asks for a different topic.
3. (No response) child watches silently.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Name beat evidence.
3. [wait 2s] [gentle] Model one tiny answer.

**Screen/state:** Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
