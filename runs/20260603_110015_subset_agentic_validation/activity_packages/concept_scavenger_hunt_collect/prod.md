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
