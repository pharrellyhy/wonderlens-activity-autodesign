## Plant Parts Explorer

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Plant Parts Explorer |
| Activity Category | 5 -- Photo-Based Enumeration Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Function and Connection |
| Related Concepts | leaf, stem, flower |
| ATL Skills Focus | observing, photographing, describing |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child photographs different visible plant parts and hears a simple function or background note for each.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The source promise is preserved by keeping the child moving around the plant and by including function/context talk after the captures.

**4. Typical Scenario**

Child photographs one plant part, finds a different part, hears playful function notes, and closes with part badges.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Start The Plant Parts Mission

**Runtime AI instruction:** Goal: invite the child to explore different visible positions on one plant through photos. Constraint: T1 max two sentences; ask for one plant part at a time. Tone: curious field guide. Progress evidence: child points to a plant or agrees to photograph a part. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: preserve photo-based plant part exploration and function/background notes.

**Example AI line:** [curious] "Let us visit one plant like tiny scientists. First, can you show me one part, maybe a leaf or flower?"

**Child responses:**
1. (Ideal) Child completes Plant Parts Explorer / Step 1: Start The Plant Parts Mission with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 1: Start The Plant Parts Mission into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 1: Start The Plant Parts Mission before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 1: Start The Plant Parts Mission and move to the next preserved source step.
2. (Unexpected) [repair] For Step 1: Start The Plant Parts Mission, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 1: Start The Plant Parts Mission, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Live photo slot and two empty part badges; no prebuilt asset is required.
#### Step 2: Capture The First Visible Part

**Round 1 -- First Plant Part:**

**Runtime AI instruction:** Goal: ask for a photo of a visible plant part and name it if the child can. Constraint: do not require species identification; use visible evidence only. Tone: encouraging. Progress evidence: photo_id of leaf, flower, stem, seed, fruit, or another visible part. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: each captured part should get a playful function/background note.

**Example AI line:** [encouraging] "Show me the first plant part. Is it a leaf, flower, or stem?"

**Child responses:**
1. (Ideal) Child completes Plant Parts Explorer / Step 2: Capture The First Visible Part with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 2: Capture The First Visible Part into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 2: Capture The First Visible Part before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 2: Capture The First Visible Part and move to the next preserved source step.
2. (Unexpected) [repair] For Step 2: Capture The First Visible Part, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 2: Capture The First Visible Part, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** Real camera capture happens here.

**Screen/state:** Show captured photo_id in first badge and a short function note beside it.
#### Step 3: Find A Different Plant Part

**Round 1 -- Second Plant Part:**

**Runtime AI instruction:** Goal: guide the child to photograph a different part from another location on the same plant. Constraint: ask for contrast with the previous part; no generic counting. Tone: exploratory. Progress evidence: second photo_id shows another part or child names a different part. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: repeated action is explore different plant positions and hear part-function context.

**Example AI line:** [exploratory] "Now look somewhere different on the plant. Can you find a part that does a different job?"

**Child responses:**
1. (Ideal) Child completes Plant Parts Explorer / Step 3: Find A Different Plant Part with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 3: Find A Different Plant Part into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 3: Find A Different Plant Part before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 3: Find A Different Plant Part and move to the next preserved source step.
2. (Unexpected) [repair] For Step 3: Find A Different Plant Part, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 3: Find A Different Plant Part, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** Second camera capture happens here.

**Screen/state:** Fill the second part badge and keep the first photo visible for comparison.
#### Step 4: Add One Fun Function Fact

**Runtime AI instruction:** Goal: tell a brief interesting function or background note about the parts the child captured. Constraint: child-safe, visible-evidence based, no species-specific claims unless known. Tone: playful science guide. Progress evidence: child repeats a part name, points, asks why, or listens. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: required background/context information must not be skipped.

**Example AI line:** [playful] "Leaves, stems, and flowers are like plant helpers, each doing a different job."

**Child responses:**
1. (Ideal) Child completes Plant Parts Explorer / Step 4: Add One Fun Function Fact with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 4: Add One Fun Function Fact into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 4: Add One Fun Function Fact before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 4: Add One Fun Function Fact and move to the next preserved source step.
2. (Unexpected) [repair] For Step 4: Add One Fun Function Fact, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 4: Add One Fun Function Fact, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show two captured photo thumbnails with simple part-job badges.
#### Step 5: Close The Plant Part Explorer

**Runtime AI instruction:** Goal: recap the captured plant positions and their simple functions. Constraint: max two sentences; no new capture. Tone: warm and proud. Progress evidence: child says leaf, flower, stem, or listens. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: close as plant-part exploration, not generic plant naming/counting.

**Example AI line:** [warm] "You explored different plant parts and learned that parts can do different jobs."

**Child responses:**
1. (Ideal) Child completes Plant Parts Explorer / Step 5: Close The Plant Part Explorer with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 5: Close The Plant Part Explorer into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 5: Close The Plant Part Explorer before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 5: Close The Plant Part Explorer and move to the next preserved source step.
2. (Unexpected) [repair] For Step 5: Close The Plant Part Explorer, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 5: Close The Plant Part Explorer, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Completed part badges with photo_id thumbnails and no generated assets.
