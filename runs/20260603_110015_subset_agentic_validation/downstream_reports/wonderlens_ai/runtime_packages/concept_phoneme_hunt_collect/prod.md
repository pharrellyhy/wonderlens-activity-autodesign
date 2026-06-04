## B-Sound Treasure Hunt

### Runtime Package

Recommended tier: `T1`.

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: invite the child into Phoneme Treasure Hunt from the trigger condition. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "Let us start B-Sound Treasure Hunt. I will keep the rule simple." Screen/state behavior: Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.
**Example AI line:** [degraded T1 tone] "Let us start B-Sound Treasure Hunt. I will keep the rule simple."

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

**Runtime AI instruction:** Goal: explain the single activity rule and name what evidence counts. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "Here is the rule: one small answer at a time, and I will help if it feels tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.
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

**Round 1 -- Hear The Target Sound:**

**Runtime AI instruction:** Goal: model the /b/ sound and show object examples without baked letters. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "Listen: /b/ like ball. Can you say /b/ with me?" Screen/state behavior: Use `round_1_scene` and optional object sprites; app overlays any letter cue separately.
**Example AI line:** [focused] "Listen: /b/ like ball. Can you say /b/ with me?"

**Child responses:**

1. (Ideal) child repeats /b/ or names ball/book/banana.
2. (Unexpected) child says a non-B word or asks for the letter.
3. (No response) child listens silently.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_1_scene` and optional object sprites; app overlays any letter cue separately.

**Round 2 -- Capture One Treasure:**

**Runtime AI instruction:** Goal: ask for one real photo_id of an indoor object whose spoken name starts with /b/. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - AI introduces a target sound, then the child finds one indoor treasure whose word starts with that sound.  Example line: "Find one treasure that starts with /b/. Take its picture, then tell me its name." Screen/state behavior: Use `round_2_scene`; app camera slot is separate from the PNG.
**Example AI line:** [focused] "Find one treasure that starts with /b/. Take its picture, then tell me its name."

**Child responses:**

1. (Ideal) photo_id plus "ball", "book", "banana", "box", or similar.
2. (Unexpected) photo without name or non-B object name.
3. (No response) child searches without answering.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

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
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

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
**Example AI line:** [degraded T1 tone] "Today you practiced Form by using beginning sound evidence."

**Child responses:**

1. (Ideal) child says again, goodbye, or favorite part.
2. (Unexpected) child asks for a different topic.
3. (No response) child watches silently.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Validate the child's idea, restate the source rule, and offer one concrete next action.
3. [wait 2s] [gentle] Model the smallest valid response or action, then continue without pressure if the child remains quiet.

**Screen/state:** Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
