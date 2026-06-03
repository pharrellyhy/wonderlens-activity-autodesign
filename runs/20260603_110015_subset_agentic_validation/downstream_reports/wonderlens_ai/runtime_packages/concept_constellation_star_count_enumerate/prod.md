## Constellation Number Reveal

### Runtime Package

Recommended tier: `T1`.

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: invite the child into Constellation Star Count from the trigger condition. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child chooses a number, then device shows an approved real constellation card matching that guide-star count and gives brief background context.  Example line: "Let us start Constellation Number Reveal. I will keep the rule simple." Screen/state behavior: Use `intro_scene`; app-owned progress, choices, or camera slots are overlays and are not baked into the PNG.
**Example AI line:** [supported T1 tone] "Let us start Constellation Number Reveal. I will keep the rule simple."

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

**Runtime AI instruction:** Goal: explain the single activity rule and name what evidence counts. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child chooses a number, then device shows an approved real constellation card matching that guide-star count and gives brief background context.  Example line: "Here is the rule: one small answer at a time, and I will help if it feels tricky." Screen/state behavior: Use `rules_scene`; show only source-aligned visual context with no buttons, labels, or progress dots baked in.
**Example AI line:** [supported T1 tone] "Here is the rule: one small answer at a time, and I will help if it feels tricky."

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

**Round 1 -- Choose A Star Number:**

**Runtime AI instruction:** Goal: offer exactly two count choices before showing any constellation card. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child chooses a number, then device shows an approved real constellation card matching that guide-star count and gives brief background context.  Example line: "Pick a sky number: five or seven guide stars?" Screen/state behavior: Use `round_1_scene`; app overlays two number choices separately, no constellation card yet.
**Example AI line:** [focused] "Pick a sky number: five or seven guide stars?"

**Child responses:**

1. (Ideal) child says or taps five or seven.
2. (Unexpected) child asks to count a visible picture first.
3. (No response) child waits after hearing the choices.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_1_scene`; app overlays two number choices separately, no constellation card yet.

**Round 2 -- Reveal The Matching Real Card:**

**Runtime AI instruction:** Goal: show the approved card whose metadata matches the chosen number. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child chooses a number, then device shows an approved real constellation card matching that guide-star count and gives brief background context.  Example line: "Seven opens Orion. This real pattern uses seven guide stars." Screen/state behavior: Use `round_2_scene` plus either `cassiopeia_five_star_card` or `orion_seven_star_card`.
**Example AI line:** [focused] "Seven opens Orion. This real pattern uses seven guide stars."

**Child responses:**

1. (Ideal) child notices Orion, Cassiopeia, stars, or lines.
2. (Unexpected) child wants to move stars or invent a pattern.
3. (No response) child watches the revealed card.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_2_scene` plus either `cassiopeia_five_star_card` or `orion_seven_star_card`.

**Round 3 -- Hear One Background Fact:**

**Runtime AI instruction:** Goal: share one child-safe fact about the revealed real constellation. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child chooses a number, then device shows an approved real constellation card matching that guide-star count and gives brief background context.  Example line: "Orion is often imagined as a hunter shape in the night sky." Screen/state behavior: Use `round_3_scene`; keep the revealed reference card visible through app display.
**Example AI line:** [focused] "Orion is often imagined as a hunter shape in the night sky."

**Child responses:**

1. (Ideal) child repeats a name, asks where, or points.
2. (Unexpected) child asks for a fictional space creature.
3. (No response) child quietly looks at the pattern.

**AI follow-up:**

1. [specific praise] Accept the beat evidence, restate what changed, and move to the next beat.
2. [warm redirect] Keep the child effort, then return to the exact source rule for this round.
3. [wait 2s] [gentle scaffold] Give one model answer or one smaller action, then continue only if the source evidence is still honest.

**Screen/state:** Use `round_3_scene`; keep the revealed reference card visible through app display.

#### Step 4: Magic Moment

**Runtime AI instruction:** Goal: celebrate the completed source-aligned sequence and name what the child caused. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child chooses a number, then device shows an approved real constellation card matching that guide-star count and gives brief background context.  Example line: "You made the activity work by doing the steps in order." Screen/state behavior: Use `celebrate_scene`; if reference or object assets remain visible, they are separate runtime layers.
**Example AI line:** [supported T1 tone] "You made the activity work by doing the steps in order."

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

**Runtime AI instruction:** Goal: recap the child action, source evidence, and key concept without adding a new task. Constraint: T1 max two short child-facing sentences; keep asset and capability claims honest. Tone: warm, specific, and playful. Progress evidence: child answer, child self-report, accepted photo_id, or quiet attention for the current beat. Branch behavior: ideal advances; unexpected validates then redirects to this beat; no response waits briefly, models one tiny answer, and keeps the child safe. Frame/source guardrail: preserve the source promise - Child chooses a number, then device shows an approved real constellation card matching that guide-star count and gives brief background context.  Example line: "Today you practiced Form by using chosen guide-star count." Screen/state behavior: Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
**Example AI line:** [supported T1 tone] "Today you practiced Form by using chosen guide-star count."

**Child responses:**

1. (Ideal) child says again, goodbye, or favorite part.
2. (Unexpected) child asks for a different topic.
3. (No response) child watches silently.

**AI follow-up:**

1. [encouraging] Advance only after the beat evidence is present; name the evidence in one short sentence.
2. [redirect] Validate the child's idea, restate the source rule, and offer one concrete next action.
3. [wait 2s] [gentle] Model the smallest valid response or action, then continue without pressure if the child remains quiet.

**Screen/state:** Use `closing_scene`; keep final state calm and free of baked badges, labels, buttons, or progress UI.
