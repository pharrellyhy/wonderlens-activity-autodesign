## Orion Number Reveal

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Orion Number Reveal |
| Activity Category | 1 -- Reference-Bound In-Device Verbal Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | quantity, source fidelity, background information |
| ATL Skills Focus | choosing, observing, listening |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

The child chooses a number before reveal, then sees a source-faithful Orion card and hears background information.

**2. Educational Purpose (KUD)**

- **K (Know):** Children can notice chosen number reveals the seven-star Orion card through a concrete activity frame.
- **U (Understand):** The activity keeps the child action, evidence source, and support status aligned.
- **D (Do):** The child performs the promised decide action with one concrete response or evidence source.

**3. Design Highlight**

This package is part of a scoped E2E runtime validation subset. It is intentionally small so autodesign package quality, package-local assets, consumer import/conversion, and support gating can be verified without broadening into a full content batch.

**4. Typical Scenario**

The child follows the runtime prompt, the device uses only package-local assets declared by asset_id, and the consumer runtime either plays or gates the package according to demo_support.yaml.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Choose A Number Before Reveal

**Runtime AI instruction:** Goal: ask the child to choose one number before any constellation image appears. Constraint: T1 max two sentences; offer simple choices like 3, 5, or 7 and do not show the Orion card yet. Tone: mysterious and warm. Progress evidence: child chooses a number, points, taps, or accepts the modeled number. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: preserve source intent: number choice comes before reveal and is not a count-the-image task.

**Example AI line:** [mysterious] "Pick a number for our sky door: three, five, or seven. Then I will reveal the real star picture."

**Child responses:**
1. (Ideal) Child chooses 3, 5, 7, or another number.
2. (Unexpected) Child asks to count stars already shown or asks for a pretend constellation.
3. (No response) Child waits before choosing.

**AI follow-up policy:**
1. (Ideal) [confirm] "Number chosen. Now the real Orion card can open."
2. (Unexpected) [anchor] "We choose first, then reveal. This card is real Orion, not pretend stars."
3. (No response) [wait 2s] [scaffold] "I can choose seven for the sky door if you want."

**Photo capture timing:** No photo capture in this Cat1 package.

**Screen/state:** Show a closed sky-door state with no stars visible; do not show asset_id=orion_seven_star_card until Step 2.

#### Step 2: Reveal The Real Orion Card

**Runtime AI instruction:** Goal: display the package-local reference-bound Orion asset after the number choice. Constraint: T1 max two sentences; reveal only asset_id=orion_seven_star_card and do not ask the child to count the stars. Tone: wonder-filled and careful. Progress evidence: child looks at the card, says star, Orion, line, or points to a visible guide star. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: preserve verified source layout; do not add random stars, background dots, labels, or invented constellation shapes.

**Example AI line:** [wonder] "Your number opened the real Orion card. These guide stars keep their true pattern."

**Child responses:**
1. (Ideal) Child notices the card, says Orion or star, or points to a line.
2. (Unexpected) Child starts counting every dot or asks to change the star positions.
3. (No response) Child quietly looks at the revealed card.

**AI follow-up policy:**
1. (Ideal) [validate] "Yes, we are noticing the real pattern that opened after your choice."
2. (Unexpected) [guardrail] "We are not counting a random picture. We keep this Orion card the way the source shows it."
3. (No response) [wait 2s] [model] "I notice a bright line and a wider shape around it."

**Photo capture timing:** No photo capture.

**Screen/state:** Reveal asset_id=orion_seven_star_card centered on the round screen; show exactly that source-faithful simplified card and no extra star background.

#### Step 3: Tell Orion Background

**Round 1 -- Orion Background Reveal:**

**Runtime AI instruction:** Goal: tell one short background fact after the reveal and connect it to the visible card. Constraint: T1 max two short sentences; include only stable background information and avoid mythology overload. Tone: gentle teacher with wonder. Progress evidence: child listens, repeats Orion, asks a question, or points to the star pattern. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: do not replace background information with a counting challenge; preserve the reveal-then-context flow.

**Example AI line:** [gentle] "Orion is a constellation, a star pattern people have used to find shapes in the night sky."

**Child responses:**
1. (Ideal) Child repeats Orion, star pattern, hunter, or asks where it is.
2. (Unexpected) Child asks for a different constellation or makes up a new star name.
3. (No response) Child listens without speaking.

**AI follow-up policy:**
1. (Ideal) [expand lightly] "Yes, people often call Orion the Hunter, and we can spot its bright pattern."
2. (Unexpected) [validate then anchor] "New constellations are fun, but this card is Orion, so we keep this background."
3. (No response) [wait 2s] [model] "I will remember: Orion is a real constellation pattern."

**Photo capture timing:** No photo capture.

**Screen/state:** Keep asset_id=orion_seven_star_card visible while the background fact is spoken; no count markers, labels, or added stars appear.

#### Step 4: Celebrate The Reveal

**Runtime AI instruction:** Goal: celebrate that the child chose first and then discovered a real constellation card. Constraint: one or two short sentences; mention the chosen number only as the opener, not as a star-count task. Tone: proud and wonder-filled. Progress evidence: child acknowledges the number, Orion, or real star pattern. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: do not convert the celebration into counting or random star generation.

**Example AI line:** [proud] "Your number opened Orion, and we kept the real star pattern safe."

**Child responses:**
1. (Ideal) Child says number, Orion, real, or star pattern.
2. (Unexpected) Child asks whether the card has the same number of stars as their choice.
3. (No response) Child watches quietly.

**AI follow-up policy:**
1. (Ideal) [warm] "That is the reveal we wanted: choice first, real card next."
2. (Unexpected) [clarify] "The number was the key that opened the card, not a promise to count matching stars."
3. (No response) [gentle] "I will keep the Orion reveal on screen for one more moment."

**Photo capture timing:** No photo capture.

**Screen/state:** Hold asset_id=orion_seven_star_card in a completed reveal state without overlays or text.

#### Step 5: Close The Sky Door

**Runtime AI instruction:** Goal: recap the number choice, real Orion reveal, and background fact. Constraint: max two short sentences; no new constellation or counting prompt. Tone: gentle closing. Progress evidence: child says goodbye, Orion, number, or listens quietly. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: close with source-faithful Orion context intact.

**Example AI line:** [gentle] "Sky door closed: you chose a number, Orion appeared, and we learned it is a real constellation."

**Child responses:**
1. (Ideal) Child repeats Orion, number, or constellation.
2. (Unexpected) Child asks for another sky card.
3. (No response) Child gives no closing response.

**AI follow-up policy:**
1. (Ideal) [close] "Orion reveal saved."
2. (Unexpected) [boundary] "Another sky card can be a later activity. This Orion reveal is complete."
3. (No response) [quiet close] "I will close the sky door."

**Photo capture timing:** No photo capture.

**Screen/state:** Fade asset_id=orion_seven_star_card to a small saved thumbnail; no new assets appear.
