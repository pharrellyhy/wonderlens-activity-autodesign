## Shadow Story Seed

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Shadow Story Seed |
| Activity Category | 1 -- In-Device Verbal Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Perspective and Change |
| Related Concepts | shape, story detail, sequence |
| ATL Skills Focus | imagining, describing, turn-taking |
| Experience Pillar | Adventure |
| Game Style | time_traveler |

### B. Activity Overview

**1. Brief Description**

The child chooses one seed-like shadow and adds one story detail before hearing a tiny woven scene.

**2. Educational Purpose (KUD)**

- **K (Know):** Children can notice shadow shape as story prompt through a concrete activity frame.
- **U (Understand):** The activity keeps the child action, evidence source, and support status aligned.
- **D (Do):** The child performs the promised imagine action with one concrete response or evidence source.

**3. Design Highlight**

This package is part of a scoped E2E runtime validation subset. It is intentionally small so autodesign package quality, package-local assets, consumer import/conversion, and support gating can be verified without broadening into a full content batch.

**4. Typical Scenario**

The child follows the runtime prompt, the device uses only package-local assets declared by asset_id, and the consumer runtime either plays or gates the package according to demo_support.yaml.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Open The Shadow Seed

**Runtime AI instruction:** Goal: invite the child into a tiny story mission and show that one choice will grow the seed-shaped shadow into a scene. Constraint: T1 max two short sentences; ask for one choice only and do not require camera input. Tone: warm, curious, and storybook-small. Progress evidence: child looks, taps, says yes, or gives any first story signal. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: preserve the activity as child-led imagining from the package-local shadow_seed_scene, not a generic quiz about shadows.

**Example AI line:** [warm] "This little shadow seed can grow one tiny story. Which part should wake up first?"

**Child responses:**
1. (Ideal) Child chooses a part, says yes, or names a shape.
2. (Unexpected) Child asks to take a photo, count stars, or switch games.
3. (No response) Child watches the screen without speaking.

**AI follow-up policy:**
1. (Ideal) [curious] "Good seed choice. I will keep it tiny and you add one detail next."
2. (Unexpected) [validate then anchor] "That idea can wait. This round is only our shadow seed story."
3. (No response) [wait 2s] [gentle] "I can start with the small round bump; you can change it if you want."

**Photo capture timing:** No photo capture in this Cat1 package.

**Screen/state:** Show asset_id=shadow_seed_scene centered on the round screen with no labels; keep a small empty story-spark state until the child answers.

#### Step 2: Choose One Story Detail

**Runtime AI instruction:** Goal: ask for one concrete detail that can attach to the chosen shadow part. Constraint: T1 max two sentences; ask for one detail such as place, feeling, or tiny action. Tone: playful and patient. Progress evidence: child names or points to one detail, or accepts a modeled option. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: do not turn the shadow into a science explanation; keep the promised story-seed frame.

**Example AI line:** [playful] "Should this seed roll, hide, or whisper? Pick one tiny detail."

**Child responses:**
1. (Ideal) Child gives one story detail such as roll, hide, moon, sleepy, or fast.
2. (Unexpected) Child gives many unrelated facts or asks what the correct answer is.
3. (No response) Child remains quiet after the detail prompt.

**AI follow-up policy:**
1. (Ideal) [validate] "That detail fits. I will weave it into one tiny scene."
2. (Unexpected) [gentle boundary] "There is no correct answer. Choose just one story detail for the seed."
3. (No response) [wait 2s] [offer choice] "I can use 'hiding' or 'rolling'; tap or say one."

**Photo capture timing:** No photo capture; this step collects a verbal or tap detail.

**Screen/state:** Keep asset_id=shadow_seed_scene visible and add one subtle glow state after the child chooses; do not introduce new assets.

#### Step 3: Weave The Tiny Scene

**Round 1 -- Tiny Shadow Scene:**

**Runtime AI instruction:** Goal: react to the child detail and produce a three-beat micro-story from the seed choice. Constraint: T1 max three very short sentences; include the child detail exactly once and avoid extra plot complexity. Tone: wonder-filled but calm. Progress evidence: child hears the woven scene, repeats a word, smiles, or adds one more tiny response. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: preserve child authorship by building from the selected part and detail, not replacing them with a new story.

**Example AI line:** [wonder] "The shadow seed rolled under a moon dot, curled up, and saved its whisper for morning."

**Child responses:**
1. (Ideal) Child reacts, repeats a story word, or adds one small extra.
2. (Unexpected) Child rejects the story or requests a long adventure.
3. (No response) Child listens without adding a response.

**AI follow-up policy:**
1. (Ideal) [proud] "You grew that scene from one detail."
2. (Unexpected) [validate then limit] "We can change one tiny part, but this round stays small."
3. (No response) [soft close] "I will keep that tiny scene safe on the screen."

**Photo capture timing:** No photo capture; the runtime response is generated from the child's verbal/tap evidence.

**Screen/state:** Show a simple completed-story glow over asset_id=shadow_seed_scene, then hold the asset steady during the micro-story.

#### Step 4: Celebrate The Story Seed

**Runtime AI instruction:** Goal: celebrate the child's authorship and name the one detail that shaped the story. Constraint: one sentence plus optional short question; do not solicit a second full round. Tone: proud and warm. Progress evidence: child acknowledges the detail or listens to the recap. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: keep celebration tied to the shadow seed activity frame.

**Example AI line:** [proud] "Your one detail made the shadow seed feel alive."

**Child responses:**
1. (Ideal) Child names the detail or says they liked it.
2. (Unexpected) Child asks for a different activity.
3. (No response) Child stays quiet while the celebration plays.

**AI follow-up policy:**
1. (Ideal) [warm] "I will remember that tiny story detail."
2. (Unexpected) [kind boundary] "This story seed is closing now; another activity can come next."
3. (No response) [wait 2s] [gentle] "The seed story is complete."

**Photo capture timing:** No photo capture in the celebration.

**Screen/state:** Keep asset_id=shadow_seed_scene in a completed state with a small non-text sparkle effect.

#### Step 5: Close The Seed Round

**Runtime AI instruction:** Goal: close the Cat1 story round with a short recap of the choice and child detail. Constraint: max two short sentences; no new prompt or new asset. Tone: gentle closing tone. Progress evidence: child says goodbye, repeats the seed/detail, or gives no response. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: do not start another untracked round.

**Example AI line:** [gentle] "One shadow seed, one detail, one tiny story. Round complete."

**Child responses:**
1. (Ideal) Child says goodbye, seed, shadow, or the chosen detail.
2. (Unexpected) Child asks to keep playing.
3. (No response) Child is quiet at the end.

**AI follow-up policy:**
1. (Ideal) [close] "Story seed saved."
2. (Unexpected) [validate then close] "More stories can wait; this tiny one is finished."
3. (No response) [quiet close] "I will close the little story now."

**Photo capture timing:** No photo capture.

**Screen/state:** Fade asset_id=shadow_seed_scene to a saved-state thumbnail; no additional screen elements appear.
