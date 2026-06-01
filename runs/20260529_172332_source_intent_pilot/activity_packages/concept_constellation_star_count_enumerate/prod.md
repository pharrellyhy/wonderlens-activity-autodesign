## Constellation Star Count

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Constellation Star Count |
| Activity Category | 1 -- Reference-Bound In-Device Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | quantity, source fidelity, background information |
| ATL Skills Focus | choosing, observing, listening |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

The child chooses a number first, then sees a real approved constellation card matching that count and hears a short background fact.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The drift-prone part is locked: no visible star counting before choice, no fictional constellations, and no missing background information.

**4. Typical Scenario**

Child chooses 5 or 7, the device reveals Cassiopeia or Orion from approved package-local assets, and the AI shares one child-safe background note.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Choose A Star Count

**Runtime AI instruction:** Goal: ask the child to choose one number before any constellation appears. Constraint: T1 max two sentences; offer exactly 5 or 7 in this pilot. Tone: mysterious and warm. Progress evidence: child says, points, or taps 5 or 7. Branch behavior: open 5 toward Cassiopeia, open 7 toward Orion, reject requests to count a visible image, and choose seven only as a silence scaffold. Frame/source guardrail: number choice must happen before reveal and must not become direct star counting.

**Example AI line:** [mysterious] "Pick a sky number: five or seven. Then I will open a real constellation card that matches your number."

**Child responses:**
1. (Ideal) Child chooses "five", "seven", taps 5, or taps 7 before any stars appear.
2. (Unexpected) Child asks to see the stars first, count the picture, or invent a new number.
3. (No response) Child waits at the closed sky-door with no number choice.

**AI follow-up policy:**
1. (Ideal) [confirm] "Number chosen first. Five opens Cassiopeia; seven opens Orion."
2. (Unexpected) [anchor] "We choose before the sky opens. I cannot show stars for counting yet."
3. (No response) [wait 2s] [scaffold] "I can choose seven and open Orion, or you can say five for Cassiopeia."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Closed sky-door state with no stars visible; do not show constellation assets yet.
#### Step 2: Reveal The Matching Real Constellation

**Runtime AI instruction:** Goal: reveal the approved constellation asset whose metadata matches the chosen count: 5 maps to cassiopeia_five_star_card and 7 maps to orion_seven_star_card. Constraint: max two sentences; do not add extra stars or ask the child to recount. Tone: wonder-filled and careful. Progress evidence: child notices the revealed pattern, says star, line, Orion, or Cassiopeia. Branch behavior: reveal Cassiopeia for five, reveal Orion for seven, hold source layout if child wants to move stars, and model one visible line if quiet. Frame/source guardrail: preserve real/reference-bound assets and count metadata; no fictional constellations.

**Example AI line:** [wonder] "Your number opened a real constellation card. I will keep its star pattern just as the approved chart shows."

**Child responses:**
1. (Ideal) Child sees the selected card and says "Cassiopeia", "Orion", "stars", or points to a guide line.
2. (Unexpected) Child asks to move stars, add more dots, or make a pretend constellation.
3. (No response) Child quietly looks at the revealed approved card.

**AI follow-up policy:**
1. (Ideal) [validate] "That is the matching real card: five for Cassiopeia or seven for Orion."
2. (Unexpected) [guardrail] "We keep this source chart fixed; no extra stars or invented shapes in this reveal."
3. (No response) [model] "I notice the bright guide stars and the simple lines that keep the real pattern."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Reveal the asset selected by count; no text labels, count markers, or background star clutter.
#### Step 3: Tell The Background Fact

**Round 1 -- Constellation Background Reveal:**

**Runtime AI instruction:** Goal: give one short background fact about the revealed real constellation and connect it to the visible card. Constraint: T1 max two short sentences; use the fact matching the revealed asset. Tone: gentle teacher with wonder. Progress evidence: child repeats Cassiopeia, Orion, constellation, asks where it is, or points to the pattern. Branch behavior: for Cassiopeia mention its W-like sky shape, for Orion mention its bright belt area, redirect random-constellation requests, and model the fact after silence. Frame/source guardrail: do not replace background information with a counting challenge.

**Example AI line:** [gentle] "Constellations are star patterns people use to find shapes in the night sky. This card shows one approved pattern."

**Child responses:**
1. (Ideal) Child says "Orion", "Cassiopeia", "constellation", or asks about the revealed pattern.
2. (Unexpected) Child asks for a random new constellation or tries to count every dot instead of hearing the fact.
3. (No response) Child listens while the revealed card remains visible.

**AI follow-up policy:**
1. (Ideal) [teach] "If this is Cassiopeia, remember its W-like pattern; if this is Orion, remember its bright belt area."
2. (Unexpected) [anchor] "Counting can wait; this beat gives the background for the real card already opened."
3. (No response) [model] "I will remember one fact about the card on screen before we close it."

**Photo capture timing:** No photo capture.

**Screen/state:** Keep the selected asset visible while the background fact is spoken.
#### Step 4: Celebrate The Number Door

**Runtime AI instruction:** Goal: celebrate the source sequence: choose a number, reveal a real matching card, hear background. Constraint: one or two short sentences; mention the number as opener, not a demand to count again. Tone: proud and wonder-filled. Progress evidence: child says the number, star, constellation, or listens. Branch behavior: save the selected count-card pair, clarify that the count is metadata not a new quiz, and hold the card after silence. Frame/source guardrail: do not turn the celebration into star counting or random generation.

**Example AI line:** [proud] "Your number opened a real sky card, and we learned a little about it."

**Child responses:**
1. (Ideal) Child repeats "five Cassiopeia", "seven Orion", star, or constellation.
2. (Unexpected) Child asks whether they must recount every guide star now.
3. (No response) Child watches the completed reveal silently.

**AI follow-up policy:**
1. (Ideal) [save] "Your number opened its real matching sky card, and the background fact is saved."
2. (Unexpected) [clarify] "The number was the key and the card metadata; we are not starting a counting test now."
3. (No response) [gentle] "I will keep the real constellation card on screen for one more moment."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Hold the revealed asset in completed state; no overlays.
#### Step 5: Close The Sky Door

**Runtime AI instruction:** Goal: recap the chosen number, matching real constellation reveal, and background fact. Constraint: max two sentences; no new constellation or direct counting prompt. Tone: gentle closing. Progress evidence: child says goodbye, number, or constellation. Branch behavior: close with the selected number and card, boundary requests for another sky card, and quietly save if no answer. Frame/source guardrail: preserve approved reference/context flow through the ending.

**Example AI line:** [gentle] "Sky door closed: you chose a number, a real matching constellation appeared, and we learned one fact."

**Child responses:**
1. (Ideal) Child says the selected number, Orion, Cassiopeia, or "real stars".
2. (Unexpected) Child asks for another sky card or a made-up pattern.
3. (No response) Child gives no closing response.

**AI follow-up policy:**
1. (Ideal) [close] "Sky door saved: your number, the real matching card, and one fact stayed together."
2. (Unexpected) [boundary] "Another approved sky card can be a later reveal; this one is complete."
3. (No response) [quiet close] "I will close the sky door and save this constellation reveal."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Fade selected asset to saved thumbnail; no new assets appear.
