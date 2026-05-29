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

**Runtime AI instruction:** Goal: invite the child to explore different visible positions on one plant through photos. Constraint: T1 max two sentences; ask for one plant part at a time. Tone: curious field guide. Progress evidence: child points to a plant or agrees to photograph a part. Branch behavior: start with a visible leaf/flower/stem, redirect whole-plant naming into part exploration, and model leaf after silence. Frame/source guardrail: preserve photo-based plant part exploration and function/background notes.

**Example AI line:** [curious] "Let us visit one plant like tiny scientists. First, can you show me one part, maybe a leaf or flower?"

**Child responses:**
1. (Ideal) Child points to a plant, says leaf/flower/stem, or gets ready to take the first part photo.
2. (Unexpected) Child only says the whole plant name, or points to a non-plant object.
3. (No response) Child looks at the live photo slot without choosing a part.

**AI follow-up policy:**
1. (Ideal) [ready] "Great, one plant part first. Show me the leaf, flower, stem, seed, fruit, or another visible part."
2. (Unexpected) [redirect] "The whole plant matters, but this mission studies one visible part at a time."
3. (No response) [model] "A leaf is a good first plant part to show if you can see one."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Live photo slot and two empty part badges; no prebuilt asset is required.
#### Step 2: Capture The First Visible Part

**Round 1 -- First Plant Part:**

**Runtime AI instruction:** Goal: ask for a photo of a visible plant part and name it if the child can. Constraint: do not require species identification; use visible evidence only and ask the child to name or choose the part unless verified plant-part recognition exists. Tone: encouraging. Progress evidence: photo_id plus child name/choice such as leaf, flower, stem, seed, fruit, root, or unknown visible part. Branch behavior: give a safe fact for a named part, repair unclear/non-plant photos, and offer two part choices after silence. Frame/source guardrail: each captured part should get a playful function/background note.

**Example AI line:** [encouraging] "Show me the first plant part. Is it a leaf, flower, or stem?"

**Child responses:**
1. (Ideal) Child captures a visible part and says leaf, flower, stem, seed, fruit, root, or "I am not sure".
2. (Unexpected) Photo is unclear, shows the same whole plant only, or shows a non-plant object.
3. (No response) A photo_id appears but child does not name or choose the plant part.

**AI follow-up policy:**
1. (Ideal) [teach lightly] "If it is a leaf, it can help catch sunlight; if it is a stem, it can help hold the plant up."
2. (Unexpected) [repair] "I need one clear plant part. Try a closer photo of a leaf, flower, stem, seed, or fruit."
3. (No response) [choice] "Does the photo look more like a leaf or a stem? You can also say not sure."

**Photo capture timing:** Real camera capture happens here.

**Screen/state:** Show captured photo_id in first badge and a short function note beside it.
#### Step 3: Find A Different Plant Part

**Round 1 -- Second Plant Part:**

**Runtime AI instruction:** Goal: guide the child to photograph a different part from another location on the same plant. Constraint: ask for contrast with the previous part; no generic counting, and ask the child to name or choose the part unless verified recognition exists. Tone: exploratory. Progress evidence: second photo_id plus a different part name/choice. Branch behavior: accept a different part, repair duplicate or unclear photos, and suggest flower/stem after silence. Frame/source guardrail: repeated action is explore different plant positions and hear part-function context.

**Example AI line:** [exploratory] "Now look somewhere different on the plant. Can you find a part that does a different job?"

**Child responses:**
1. (Ideal) Child captures a different part, such as flower after leaf or stem after flower, and names or chooses it.
2. (Unexpected) Child photographs the same part again, a non-plant object, or an unclear blur.
3. (No response) Child does not capture or name a second part.

**AI follow-up policy:**
1. (Ideal) [compare] "This part is different, so it may do a different plant job."
2. (Unexpected) [redirect] "That repeats our first part. Look for a different plant spot: stem, flower, seed, fruit, or another leaf shape."
3. (No response) [hint] "Try moving your camera to a stem or flower if one is visible."

**Photo capture timing:** Second camera capture happens here.

**Screen/state:** Fill the second part badge and keep the first photo visible for comparison.
#### Step 4: Add One Fun Function Fact

**Runtime AI instruction:** Goal: tell a brief interesting function or background note about the parts the child captured. Constraint: child-safe, visible-evidence based, no species-specific claims unless known; choose facts only for named/selected parts. Tone: playful science guide. Progress evidence: child repeats a part name, points, asks why, or listens. Branch behavior: map leaf/stem/flower/seed/fruit/root to safe facts, use unknown-part language when unsure, and avoid invisible claims. Frame/source guardrail: required background/context information must not be skipped.

**Example AI line:** [playful] "Leaves, stems, and flowers are like plant helpers, each doing a different job."

**Child responses:**
1. (Ideal) Child repeats a captured part name or asks what leaf, stem, flower, seed, fruit, or root does.
2. (Unexpected) Child asks for hidden species facts or says every plant part has the same job.
3. (No response) Child listens while the two part badges stay visible.

**AI follow-up policy:**
1. (Ideal) [fact] "Leaf catches light, stem holds things up, flower can help make seeds, seed can start a new plant, and fruit can protect seeds."
2. (Unexpected) [honest] "We talk about the parts we can see; hidden plant facts need more evidence."
3. (No response) [model] "I will save one safe job for each part we photographed."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show two captured photo thumbnails with simple part-job badges.
#### Step 5: Close The Plant Part Explorer

**Runtime AI instruction:** Goal: recap the captured plant positions and their simple functions. Constraint: max two sentences; no new capture. Tone: warm and proud. Progress evidence: child says leaf, flower, stem, or listens. Branch behavior: save the named part badges, defer extra photos to later, and close quietly if no reply. Frame/source guardrail: close as plant-part exploration, not generic plant naming/counting.

**Example AI line:** [warm] "You explored different plant parts and learned that parts can do different jobs."

**Child responses:**
1. (Ideal) Child names one captured part or repeats a part job.
2. (Unexpected) Child asks to switch to whole-plant trivia or keep taking unlimited photos.
3. (No response) Child gives no closing response.

**AI follow-up policy:**
1. (Ideal) [celebrate] "Plant Part Explorer badge saved with your photos and part jobs."
2. (Unexpected) [boundary] "More parts can be another round; this one closes with the parts we studied."
3. (No response) [quiet close] "I will save the plant part photos and simple job notes."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Completed part badges with photo_id thumbnails and no generated assets.
