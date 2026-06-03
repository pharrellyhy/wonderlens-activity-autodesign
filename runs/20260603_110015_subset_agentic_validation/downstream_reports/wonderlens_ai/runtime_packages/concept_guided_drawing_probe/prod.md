## Step Card Drawing Guide

### Runtime Package

Recommended tier: `T1`.

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: invite the child into Guided Drawing from the trigger condition. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI guides the child to use paper and pencil to complete a simple drawing step by step, then celebrates the process.  Example line: "Let us start Step Card Drawing Guide. I will keep the rule simple." Screen/state behavior: Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.
**Example AI line:** [degraded T1 tone] "Let us start Step Card Drawing Guide. I will keep the rule simple."

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

**Runtime AI instruction:** Goal: explain the single activity rule and name what evidence counts. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI guides the child to use paper and pencil to complete a simple drawing step by step, then celebrates the process.  Example line: "Here is the rule: one small answer at a time, and I will help if it feels tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.
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

**Round 1 -- Draw The First Circle:**

**Runtime AI instruction:** Goal: show the first step card and ask the child to draw one big circle on paper. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI guides the child to use paper and pencil to complete a simple drawing step by step, then celebrates the process.  Example line: "First, draw one big circle. Say done when your circle is on the paper." Screen/state behavior: Use `round_1_scene` and `circle_step`; show only the first drawing action.
**Example AI line:** [focused] "First, draw one big circle. Say done when your circle is on the paper."

**Child responses:**

1. (Ideal) child says done or caregiver confirms.
2. (Unexpected) child asks if it must be perfect.
3. (No response) child keeps drawing silently.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_1_scene` and `circle_step`; show only the first drawing action.

**Round 2 -- Add Two Small Ears Or Petals:**

**Runtime AI instruction:** Goal: show the second step card and ask for two small side shapes. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI guides the child to use paper and pencil to complete a simple drawing step by step, then celebrates the process.  Example line: "Now add two small ears or petals, one on each side." Screen/state behavior: Use `round_2_scene` and `ears_step`; do not show a finished drawing yet.
**Example AI line:** [focused] "Now add two small ears or petals, one on each side."

**Child responses:**

1. (Ideal) child reports done or asks for more time.
2. (Unexpected) child adds many shapes or changes the object.
3. (No response) child stays focused on drawing.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_2_scene` and `ears_step`; do not show a finished drawing yet.

**Round 3 -- Finish With One Face Or Detail:**

**Runtime AI instruction:** Goal: show the final step card and ask for one simple finishing detail. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI guides the child to use paper and pencil to complete a simple drawing step by step, then celebrates the process.  Example line: "Last, add one happy face or tiny detail. Then tell me when your drawing is ready." Screen/state behavior: Use `round_3_scene` and `finish_step`; represent the finished simple drawing without assessment UI.
**Example AI line:** [focused] "Last, add one happy face or tiny detail. Then tell me when your drawing is ready."

**Child responses:**

1. (Ideal) child says ready or shows caregiver.
2. (Unexpected) child wants camera grading or asks if it is good.
3. (No response) child keeps drawing silently.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_3_scene` and `finish_step`; represent the finished simple drawing without assessment UI.

#### Step 4: Magic Moment

**Runtime AI instruction:** Goal: celebrate the completed source-aligned sequence and name what the child caused. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI guides the child to use paper and pencil to complete a simple drawing step by step, then celebrates the process.  Example line: "You made the activity work by doing the steps in order." Screen/state behavior: Use `celebrate_scene`; if reference or object assets remain visible, they are separate runtime layers.
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

**Runtime AI instruction:** Goal: recap the child action, source evidence, and key concept without adding a new task. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI guides the child to use paper and pencil to complete a simple drawing step by step, then celebrates the process.  Example line: "Today you practiced Form by using drawing step sequence." Screen/state behavior: Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
**Example AI line:** [degraded T1 tone] "Today you practiced Form by using drawing step sequence."

**Child responses:**

1. (Ideal) child says again, goodbye, or favorite part.
2. (Unexpected) child asks for a different topic.
3. (No response) child watches silently.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Validate the child's idea, restate the source rule, and offer one concrete next action.
3. [wait 2s] [gentle] Model the smallest valid response or action, then continue without pressure if the child remains quiet.

**Screen/state:** Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
