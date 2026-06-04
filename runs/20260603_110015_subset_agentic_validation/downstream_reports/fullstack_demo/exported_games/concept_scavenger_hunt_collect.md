---
category: category_5
entity_name: shared clue object
display_label: Shared Clue Object
tier: T1
ib_theme: How The World Works
play_rounds: 3
plain_description: Three real-world finds become evidence for one shared rule and
  one child-generated extra connection.
steps_summary:
- 'Goal: invite the child'
- 'Goal: explain the single'
- 'Goal: consume the first'
- 'Goal: synthesize all three'
- 'Goal: recap the child'
creative_slots:
  observation_angle: pattern
  collection_criterion: Things with shared visible clue
  collection_count: 3
  mission_metaphor: You are a Concept Scavenger Hunt Collect Explorer!
  role_title: Concept Scavenger Hunt Collect Explorer
  synthesis_type: naming_story
  stuck_hint: Look nearby for something with shared visible clue.
  naming_prompt: What would you name this find?
  detail_question_template: What do you notice about it?
  sorting_criterion: ''
step_instructions:
  hook:
    goal: 'Goal: invite the child into Scavenger Hunt from the trigger condition.
      Constraint: T1 max two short child-facing sentences; keep asset and capability
      claims honest. Tone: warm, specific, and playful. Progress evidence: child answer,
      child self-report, accepted photo_id, or quiet attention for the current beat.
      Branch behavior: ideal advances; unexpected validates then redirects to this
      beat; no response waits briefly, models one tiny answer, and keeps the child
      safe. Frame/source guardrail: preserve the source promise - Child finds and
      photographs three things that share a color, shape, or category, then names
      one extra shared connection. Example line: "Let us start Shared Clue Scavenger
      Hunt. I will keep the rule simple." Screen/state behavior: Use `intro_scene`;
      app-owned progress, choices, or camera slots are overlays and are not baked
      into the PNG.'
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
      guardrail: preserve the source promise - Child finds and photographs three things
      that share a color, shape, or category, then names one extra shared connection.
      Example line: "Here is the rule: one small answer at a time, and I will help
      if it feels tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned
      visual context with no buttons, labels, or progress dots baked in.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  rounds:
  - round_number: 1
    goal: 'Goal: consume the first photo_id and ask the child to name the visible
      shared clue. Constraint: T1 max two short child-facing sentences; keep asset
      and capability claims honest. Tone: warm, specific, and playful. Progress evidence:
      child answer, child self-report, accepted photo_id, or quiet attention for the
      current beat. Branch behavior: ideal advances; unexpected validates then redirects
      to this beat; no response waits briefly, models one tiny answer, and keeps the
      child safe. Frame/source guardrail: preserve the source promise - Child finds
      and photographs three things that share a color, shape, or category, then names
      one extra shared connection. Example line: "I see your first find. What part
      shares our clue?" Screen/state behavior: Use `round_1_scene`; app overlays the
      first captured photo slot separately.'
    scenario: First Matching Find
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: focused
    acceptable_themes:
    - it_is_round
    - same_color
    escalation_note: Source round 1 from the package runtime flow.
  - round_number: 2
    goal: 'Goal: compare the second photo to the first accepted find and keep the
      same clue active. Constraint: T1 max two short child-facing sentences; keep
      asset and capability claims honest. Tone: warm, specific, and playful. Progress
      evidence: child answer, child self-report, accepted photo_id, or quiet attention
      for the current beat. Branch behavior: ideal advances; unexpected validates
      then redirects to this beat; no response waits briefly, models one tiny answer,
      and keeps the child safe. Frame/source guardrail: preserve the source promise
      - Child finds and photographs three things that share a color, shape, or category,
      then names one extra shared connection. Example line: "Second find is here.
      Does it share the same clue or a different one?" Screen/state behavior: Use
      `round_2_scene`; app overlays two captured photo slots separately.'
    scenario: Second Matching Find
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: focused
    acceptable_themes:
    - same_shape
    - same_kind
    escalation_note: Source round 2 from the package runtime flow.
  - round_number: 3
    goal: 'Goal: accept the final matching photo only after child-visible or child-stated
      evidence. Constraint: T1 max two short child-facing sentences; keep asset and
      capability claims honest. Tone: warm, specific, and playful. Progress evidence:
      child answer, child self-report, accepted photo_id, or quiet attention for the
      current beat. Branch behavior: ideal advances; unexpected validates then redirects
      to this beat; no response waits briefly, models one tiny answer, and keeps the
      child safe. Frame/source guardrail: preserve the source promise - Child finds
      and photographs three things that share a color, shape, or category, then names
      one extra shared connection. Example line: "Final find check. Show me the clue
      that makes the trail complete." Screen/state behavior: Use `round_3_scene`;
      app overlays the final captured photo slot separately.'
    scenario: Third Matching Find
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: focused
    acceptable_themes:
    - yes_same_color
    escalation_note: Source round 3 from the package runtime flow.
  celebrate:
    goal: 'Goal: synthesize all three accepted finds into a shared rule and ask for
      one extra connection. Constraint: T1 max two short child-facing sentences; keep
      asset and capability claims honest. Tone: warm, specific, and playful. Progress
      evidence: child answer, child self-report, accepted photo_id, or quiet attention
      for the current beat. Branch behavior: ideal advances; unexpected validates
      then redirects to this beat; no response waits briefly, models one tiny answer,
      and keeps the child safe. Frame/source guardrail: preserve the source promise
      - Child finds and photographs three things that share a color, shape, or category,
      then names one extra shared connection. Do not end with generic completion;
      synthesize the collected evidence into a rule, summary, or story payoff. Example
      line: "Your three finds share the clue. What else do they have in common?" Screen/state
      behavior: Use `synthesis_scene`; app arranges captured photos as a web overlay.'
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
      - Child finds and photographs three things that share a color, shape, or category,
      then names one extra shared connection. Example line: "Today you practiced Form
      by using shared visible clue." Screen/state behavior: Use `closing_scene`; keep
      final state calm and free of baked badges, labels, buttons, or progress UI.'
    constraint: T1 max 2 sentences; keep child-facing wording concrete. Preserve ideal,
      unexpected, and no-response branch behavior.
    emotion_tag: warm
  early_exit:
    goal: Offer a gentle goodbye that validates whatever the child already tried.
    constraint: T1 max 2 sentences; no pressure to continue.
    emotion_tag: gentle
  synthesis:
    goal: 'Goal: synthesize all three accepted finds into a shared rule and ask for
      one extra connection. Constraint: T1 max two short child-facing sentences; keep
      asset and capability claims honest. Tone: warm, specific, and playful. Progress
      evidence: child answer, child self-report, accepted photo_id, or quiet attention
      for the current beat. Branch behavior: ideal advances; unexpected validates
      then redirects to this beat; no response waits briefly, models one tiny answer,
      and keeps the child safe. Frame/source guardrail: preserve the source promise
      - Child finds and photographs three things that share a color, shape, or category,
      then names one extra shared connection. Do not end with generic completion;
      synthesize the collected evidence into a rule, summary, or story payoff. Example
      line: "Your three finds share the clue. What else do they have in common?" Screen/state
      behavior: Use `synthesis_scene`; app arranges captured photos as a web overlay.'
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
  widget_label: 'Find 1: First Matching Find'
  animation_label: Progress update
- widget: progress_tracker
  widget_params:
    filled: 2
    total: 3
  animation: card_slide_in
  trigger: on_round_2
  sfx_cue: photo_shutter_click
  widget_label: 'Find 2: Second Matching Find'
  animation_label: Progress update
- widget: progress_tracker
  widget_params:
    filled: 3
    total: 3
  animation: card_slide_in
  trigger: on_round_3
  sfx_cue: photo_shutter_click
  widget_label: 'Find 3: Third Matching Find'
  animation_label: Progress update
celebration_frame:
  widget: badge_award
  widget_params:
    title: 'Goal: synthesize all three'
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
- shared clue object
- shared visible clue
feature_keywords:
- shared visible clue
photo_features:
- shared visible clue
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
activity_type: concept_scavenger_hunt_collect
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

## Shared Clue Scavenger Hunt

### Runtime Package

Recommended tier: `T1`.

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: invite the child into Scavenger Hunt from the trigger condition. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child finds and photographs three things that share a color, shape, or category, then names one extra shared connection.  Example line: "Let us start Shared Clue Scavenger Hunt. I will keep the rule simple." Screen/state behavior: Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.
**Example AI line:** [warm] "Let us start Shared Clue Scavenger Hunt. I will keep the rule simple."

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

**Runtime AI instruction:** Goal: explain the single activity rule and name what evidence counts. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child finds and photographs three things that share a color, shape, or category, then names one extra shared connection.  Example line: "Here is the rule: one small answer at a time, and I will help if it feels tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.
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

**Round 1 -- First Matching Find:**

**Runtime AI instruction:** Goal: consume the first photo_id and ask the child to name the visible shared clue. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child finds and photographs three things that share a color, shape, or category, then names one extra shared connection.  Example line: "I see your first find. What part shares our clue?" Screen/state behavior: Use `round_1_scene`; app overlays the first captured photo slot separately.
**Example AI line:** [focused] "I see your first find. What part shares our clue?"

**Child responses:**

1. (Ideal) "It is round" or "same color".
2. (Unexpected) child says it is favorite or unrelated.
3. (No response) child watches the photo quietly.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [redirect] Name round evidence.
3. [wait 2s] [gentle] Model one small move.

**Screen/state:** Use `round_1_scene`; app overlays the first captured photo slot separately.

**Round 2 -- Second Matching Find:**

**Runtime AI instruction:** Goal: compare the second photo to the first accepted find and keep the same clue active. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child finds and photographs three things that share a color, shape, or category, then names one extra shared connection.  Example line: "Second find is here. Does it share the same clue or a different one?" Screen/state behavior: Use `round_2_scene`; app overlays two captured photo slots separately.
**Example AI line:** [focused] "Second find is here. Does it share the same clue or a different one?"

**Child responses:**

1. (Ideal) "same shape" or "same kind".
2. (Unexpected) child names a different detail such as bigger.
3. (No response) child holds device without answer.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [redirect] Name round evidence.
3. [wait 2s] [gentle] Model one small move.

**Screen/state:** Use `round_2_scene`; app overlays two captured photo slots separately.

**Round 3 -- Third Matching Find:**

**Runtime AI instruction:** Goal: accept the final matching photo only after child-visible or child-stated evidence. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child finds and photographs three things that share a color, shape, or category, then names one extra shared connection.  Example line: "Final find check. Show me the clue that makes the trail complete." Screen/state behavior: Use `round_3_scene`; app overlays the final captured photo slot separately.
**Example AI line:** [focused] "Final find check. Show me the clue that makes the trail complete."

**Child responses:**

1. (Ideal) "yes, same color" or points.
2. (Unexpected) child cannot find one or asks to count a maybe item.
3. (No response) child keeps searching silently.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [redirect] Name round evidence.
3. [wait 2s] [gentle] Model one small move.

**Screen/state:** Use `round_3_scene`; app overlays the final captured photo slot separately.

#### Step 4: Synthesis And Magic Moment

**Runtime AI instruction:** Goal: synthesize all three accepted finds into a shared rule and ask for one extra connection. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child finds and photographs three things that share a color, shape, or category, then names one extra shared connection. Do not end with generic completion; synthesize the collected evidence into a rule, summary, or story payoff. Example line: "Your three finds share the clue. What else do they have in common?" Screen/state behavior: Use `synthesis_scene`; app arranges captured photos as a web overlay.
**Example AI line:** [wonder] "Your three finds share the clue. What else do they have in common?"

**Child responses:**

1. (Ideal) child names a shared rule, pattern, story link, or summary.
2. (Unexpected) child says the finds are different or chooses a favorite only.
3. (No response) child reviews the completed collection quietly.

**AI follow-up:**

1. [proud] Repeat the child's shared rule and connect it to all accepted finds.
2. [bridge] Agree that the finds differ, then ask for one same color, shape, place, sound, or kind.
3. [wait 2s] [model] Offer one source-safe synthesis such as "found today" only as a scaffold.

**Screen/state:** Use `synthesis_scene`; app arranges captured photos as a web overlay.

#### Step 5: Closing + Concepts

**Runtime AI instruction:** Goal: recap the child action, source evidence, and key concept without adding a new task. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child finds and photographs three things that share a color, shape, or category, then names one extra shared connection.  Example line: "Today you practiced Form by using shared visible clue." Screen/state behavior: Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
**Example AI line:** [warm] "Today you practiced Form by using shared visible clue."

**Child responses:**

1. (Ideal) child says again, goodbye, or favorite part.
2. (Unexpected) child asks for a different topic.
3. (No response) child watches silently.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Name beat evidence.
3. [wait 2s] [gentle] Model one tiny answer.

**Screen/state:** Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
