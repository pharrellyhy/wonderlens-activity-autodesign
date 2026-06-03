## Recognition Pop Challenge

### Runtime Package

Recommended tier: `T1`.

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: invite the child into Recognition Pop Challenge from the trigger condition. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "Let us start Recognition Pop Challenge. I will keep the rule simple." Screen/state behavior: Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.
**Example AI line:** [degraded T1 tone] "Let us start Recognition Pop Challenge. I will keep the rule simple."

**Child responses:**

1. (Ideal) child agrees or asks to play.
2. (Unexpected) child asks for a different game or gives an unrelated comment.
3. (No response) child looks at the screen or waits.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Validate the child's idea, restate the source rule, and offer one concrete next action.
3. [wait 2s] [gentle] Model the smallest valid response or action, then continue without pressure if the child remains quiet.

**Screen/state:** Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.

#### Step 2: Rule Introduction

**Runtime AI instruction:** Goal: explain the single activity rule and name what evidence counts. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "Here is the rule: one small answer at a time, and I will help if it feels tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.
**Example AI line:** [degraded T1 tone] "Here is the rule: one small answer at a time, and I will help if it feels tricky."

**Child responses:**

1. (Ideal) child repeats the rule or says ready.
2. (Unexpected) child asks what counts or proposes a different rule.
3. (No response) child hesitates before starting.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Validate the child's idea, restate the source rule, and offer one concrete next action.
3. [wait 2s] [gentle] Model the smallest valid response or action, then continue without pressure if the child remains quiet.

**Screen/state:** Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.

#### Step 3: Core Loop

**Round 1 -- Learn The Target Rule:**

**Runtime AI instruction:** Goal: introduce the target picture and the stay-quiet rule for distractors. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "When the dog target appears, say pop. If another animal appears, stay quiet." Screen/state behavior: Use `round_1_scene` plus `dog_target`; background contains no duplicate animals.
**Example AI line:** [focused] "When the dog target appears, say pop. If another animal appears, stay quiet."

**Child responses:**

1. (Ideal) child says pop for the target rule.
2. (Unexpected) child wants to pop every picture.
3. (No response) child watches the target sprite.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_1_scene` plus `dog_target`; background contains no duplicate animals.

**Round 2 -- Compare One Distractor:**

**Runtime AI instruction:** Goal: show one visually similar distractor and ask the child to stay quiet or say not dog. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "This one is not the dog target. Quiet eyes ready." Screen/state behavior: Use `round_2_scene` plus one distractor sprite; background remains abstract.
**Example AI line:** [focused] "This one is not the dog target. Quiet eyes ready."

**Child responses:**

1. (Ideal) child stays quiet or says not dog.
2. (Unexpected) child says pop for the distractor.
3. (No response) child watches without response.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_2_scene` plus one distractor sprite; background remains abstract.

**Round 3 -- Pop The Target Again:**

**Runtime AI instruction:** Goal: return the target and require the target response after contrast. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "Target is back. Now pop!" Screen/state behavior: Use `round_3_scene` plus `dog_target`; app owns timing and tap state.
**Example AI line:** [focused] "Target is back. Now pop!"

**Child responses:**

1. (Ideal) child says pop or taps once.
2. (Unexpected) child taps many times or names a distractor.
3. (No response) child misses the target turn.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_3_scene` plus `dog_target`; app owns timing and tap state.

#### Step 4: Magic Moment

**Runtime AI instruction:** Goal: celebrate the completed source-aligned sequence and name what the child caused. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "You made the activity work by doing the steps in order." Screen/state behavior: Use `celebrate_scene`; if reference or object assets remain visible, they are separate runtime layers.
**Example AI line:** [degraded T1 tone] "You made the activity work by doing the steps in order."

**Child responses:**

1. (Ideal) child reacts, repeats, or smiles.
2. (Unexpected) child asks to change the result or asks for another round.
3. (No response) child quietly watches the celebration.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Validate the child's idea, restate the source rule, and offer one concrete next action.
3. [wait 2s] [gentle] Model the smallest valid response or action, then continue without pressure if the child remains quiet.

**Screen/state:** Use `celebrate_scene`; if reference or object assets remain visible, they are separate runtime layers.

#### Step 5: Closing + Concepts

**Runtime AI instruction:** Goal: recap the child action, source evidence, and key concept without adding a new task. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - After a source object such as dog, the device shows changing target and distractor pictures and the child responds only when the target appears.  Example line: "Today you practiced Form by using target versus distractor recognition." Screen/state behavior: Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
**Example AI line:** [degraded T1 tone] "Today you practiced Form by using target versus distractor recognition."

**Child responses:**

1. (Ideal) child says again, goodbye, or favorite part.
2. (Unexpected) child asks for a different topic.
3. (No response) child watches silently.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Validate the child's idea, restate the source rule, and offer one concrete next action.
3. [wait 2s] [gentle] Model the smallest valid response or action, then continue without pressure if the child remains quiet.

**Screen/state:** Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
