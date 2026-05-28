## Soft Shape Collect

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Soft Shape Collect |
| Activity Category | 5 -- Collection/Tracking Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | round, corner, long, photo evidence |
| ATL Skills Focus | observing, describing, matching |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The child uses guide cards to choose a shape clue, then captures a real-world photo as the collection evidence.

**2. Educational Purpose (KUD)**

- **K (Know):** Children can notice soft or round visible shape through a concrete activity frame.
- **U (Understand):** The activity keeps the child action, evidence source, and support status aligned.
- **D (Do):** The child performs the promised collect action with one concrete response or evidence source.

**3. Design Highlight**

This package is part of a scoped E2E runtime validation subset. It is intentionally small so autodesign package quality, package-local assets, consumer import/conversion, and support gating can be verified without broadening into a full content batch.

**4. Typical Scenario**

The child follows the runtime prompt, the device uses only package-local assets declared by asset_id, and the consumer runtime either plays or gates the package according to demo_support.yaml.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Start The Shape Quest

**Runtime AI instruction:** Goal: invite the child to use guide cards to choose a real-world shape clue. Constraint: T1 max two sentences; explain that the card guides the hunt but the real photo is the evidence. Tone: bright quest-leader warmth. Progress evidence: child agrees, looks at the guide cards, or asks what to find. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: preserve Cat5 collection: guide assets are not the collected item; the later photo_id is required.

**Example AI line:** [bright] "These shape cards are our map. Pick one clue, then we will find it for real."

**Child responses:**
1. (Ideal) Child agrees or asks to see the cards.
2. (Unexpected) Child wants to collect the screen card itself.
3. (No response) Child watches silently.

**AI follow-up policy:**
1. (Ideal) [ready] "Good. I will show the choices now."
2. (Unexpected) [anchor] "The card only guides us; the collection needs a real photo."
3. (No response) [wait 2s] [model] "I will start with the round card so we know what to hunt."

**Photo capture timing:** No photo before Step 2.

**Screen/state:** Show an empty collection tray and prepare asset_ids round_shape, corner_shape, and long_shape for the guide row.

#### Step 2: Choose A Guide Card

**Runtime AI instruction:** Goal: show the three package-local selectable cards and ask which visible shape clue to hunt. Constraint: T1 one direct question; do not imply the card itself completes collection. Tone: curious and focused. Progress evidence: child chooses round_shape, corner_shape, long_shape, or names round/corner/long. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: preserve the source play frame of guide-before-capture and real-world collection after choice.

**Example AI line:** [curious] "Choose a guide: round, corner, or long. Which clue should your real photo match?"

**Child responses:**
1. (Ideal) Child chooses one guide card or says a shape clue.
2. (Unexpected) Child names an unrelated color or asks to skip the camera.
3. (No response) Child does not choose a guide.

**AI follow-up policy:**
1. (Ideal) [confirm] "Great. Now find a real thing with that clue and take its picture."
2. (Unexpected) [redirect] "Colors are interesting, but this quest needs a shape clue from these cards."
3. (No response) [wait 2s] [scaffold] "Let's choose round_shape. Find one real round thing."

**Photo capture timing:** The real camera capture happens after this guide choice and before Step 3.

**Screen/state:** Display selectable asset_ids round_shape, corner_shape, and long_shape. Highlight the chosen asset_id and keep an empty photo slot beside it.

#### Step 3: Collect The Real Shape Photo

**Round 1 -- Real Shape Photo:**

**Runtime AI instruction:** Goal: react to the captured photo_id and ask the child to name the shape evidence that matches the selected guide. Constraint: T1 max two sentences; require child-visible or child-stated evidence before accepting. Tone: playful field scout. Progress evidence: child captures a real photo_id and names or points to the matching shape clue. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: do not accept the guide card alone; preserve real camera capture and photo_id handoff semantics.

**Example AI line:** [playful] "Your real photo is in. What shape clue makes it match the guide?"

**Child responses:**
1. (Ideal) Child says round, corner, long, soft, edge, or points to the matching part in the captured photo.
2. (Unexpected) Child says the photo does not match or asks to use the screen card as the answer.
3. (No response) Child waits while the captured photo is shown.

**AI follow-up policy:**
1. (Ideal) [celebrate] "Collected. The real photo gives us the shape evidence."
2. (Unexpected) [repair] "The card cannot count as the find. Show the matching part in your photo or take one retry photo."
3. (No response) [wait 2s] [choice] "Does your photo match round, corner, or long?"

**Photo capture timing:** Consumes the photo captured after Step 2; any retry loops back through the same real photo_id handoff.

**Screen/state:** Show the captured photo_id in the collection slot next to the chosen guide asset_id; mark the slot collected only after evidence is named.

#### Step 4: Celebrate The Shape Match

**Runtime AI instruction:** Goal: celebrate the successful guide-card-to-real-photo connection. Constraint: one or two short sentences; mention the chosen guide and the real photo evidence. Tone: proud and concrete. Progress evidence: child hears or repeats the matching shape clue. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: celebrate the real collected photo, not a synthetic card match.

**Example AI line:** [proud] "You used a guide card, then proved it with a real photo."

**Child responses:**
1. (Ideal) Child repeats the shape clue or says yes.
2. (Unexpected) Child asks for a different card after collection.
3. (No response) Child is quiet after acceptance.

**AI follow-up policy:**
1. (Ideal) [warm] "That is real shape evidence."
2. (Unexpected) [boundary] "A new card would be another round; this one is collected."
3. (No response) [gentle] "I will save this shape match."

**Photo capture timing:** No new photo after acceptance.

**Screen/state:** Persist the photo_id thumbnail and chosen guide asset_id in a completed tray state.

#### Step 5: Close The Shape Quest

**Runtime AI instruction:** Goal: recap the selected card, real photo capture, and named shape evidence. Constraint: max two short sentences; do not introduce new cards or camera tasks. Tone: warm closing. Progress evidence: child says the shape clue or listens quietly. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: close with the Cat5 guide-plus-photo contract intact.

**Example AI line:** [warm] "Shape quest complete: guide card first, real photo evidence second."

**Child responses:**
1. (Ideal) Child names the collected clue.
2. (Unexpected) Child wants a second hunt.
3. (No response) Child gives no closing response.

**AI follow-up policy:**
1. (Ideal) [close] "Saved with the real photo."
2. (Unexpected) [validate then close] "Another hunt can come later. This validation round is done."
3. (No response) [quiet close] "I will close the shape tray."

**Photo capture timing:** No new photo in closing.

**Screen/state:** Show completed tray with chosen guide asset_id and captured photo_id thumbnail; then end.
