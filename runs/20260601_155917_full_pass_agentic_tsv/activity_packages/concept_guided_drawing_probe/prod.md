## Guided Drawing Capability Gate

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Guided Drawing Capability Gate |
| Activity Category | Unsupported Cat3 -- Material Workflow Probe |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Change |
| Related Concepts | paper drawing, step sequence, process celebration |
| ATL Skills Focus | following steps, creating, reflecting |
| Experience Pillar | Creation |
| Game Style | maker_steps |

### B. Activity Overview

**1. Brief Description**

The original design is intentionally gated because it needs a paper-and-pencil material workflow and final photo celebration.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The package preserves the source by refusing a misleading playable conversion. Future implementation requirements stay explicit.

**4. Typical Scenario**

Operator reviews the gate; consumers must skip or show unsupported state until material workflow support exists.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Gate The Paper Drawing Workflow

**Runtime AI instruction:** Goal: explain that the source activity needs paper, pencil, timed drawing steps, and a final-work photo, so this pilot must gate it instead of pretending it is playable. Constraint: one clear gate message; do not invite the child to start unless product support exists. Tone: honest and warm. Progress evidence: reviewer sees unsupported state and required capabilities. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: preserve step-by-step material drawing, time allowance, final photo, no quality grading, and process celebration.

**Example AI line:** [honest] "This drawing idea needs paper steps and a final artwork photo, so I will not pretend it is ready yet."

**Child responses:**
1. (Ideal) Child completes Guided Drawing Capability Gate / Step 1: Gate The Paper Drawing Workflow with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 1: Gate The Paper Drawing Workflow into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 1: Gate The Paper Drawing Workflow before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 1: Gate The Paper Drawing Workflow and move to the next preserved source step.
2. (Unexpected) [repair] For Step 1: Gate The Paper Drawing Workflow, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 1: Gate The Paper Drawing Workflow, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** No playable runtime screen; consumer should gate with ui_template none.
#### Step 2: Preserve Required Product Capabilities

**Runtime AI instruction:** Goal: list the minimum capabilities needed for future support. Constraint: keep it as design contract, not child-facing play. Tone: precise. Progress evidence: material workflow, step timing, optional step cards, final photo, and no quality grading are recorded. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: do not make unsupported mechanics playable to pass the pilot.

**Example AI line:** [precise] "Future support needs step cards or voice steps, enough drawing time, final photo capture, and celebration without judging drawing quality."

**Child responses:**
1. (Ideal) Child completes Guided Drawing Capability Gate / Step 2: Preserve Required Product Capabilities with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 2: Preserve Required Product Capabilities into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 2: Preserve Required Product Capabilities before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 2: Preserve Required Product Capabilities and move to the next preserved source step.
2. (Unexpected) [repair] For Step 2: Preserve Required Product Capabilities, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 2: Preserve Required Product Capabilities, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** No screen assets are claimed because the package is unsupported.
#### Step 3: Block Runtime Launch

**Round 1 -- Unsupported Launch Gate:**

**Runtime AI instruction:** Goal: prevent downstream demos from launching this as a child activity. Constraint: ui_template must remain none and demo_support.status must remain unsupported. Tone: firm. Progress evidence: fullstack importer skips it and WonderLens AI preserves unsupported metadata. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: unsupported honesty is required source-intent preservation.

**Example AI line:** [firm] "Runtime launch is blocked for now; this is a product capability probe, not a playable game."

**Child responses:**
1. (Ideal) Child completes Guided Drawing Capability Gate / Step 3: Block Runtime Launch with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 3: Block Runtime Launch into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 3: Block Runtime Launch before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 3: Block Runtime Launch and move to the next preserved source step.
2. (Unexpected) [repair] For Step 3: Block Runtime Launch, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 3: Block Runtime Launch, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo because runtime launch is blocked.

**Screen/state:** Consumer gate only; no child play surface.
#### Step 4: Record Future Preview Shape

**Runtime AI instruction:** Goal: document the future child-facing shape without executing it. Constraint: summarize four drawing steps and final photo celebration only as a preview. Tone: warm design note. Progress evidence: reviewers can tell what support would need to implement. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: no per-step confirmation is required; leave enough time for drawing.

**Example AI line:** [warm] "Future version: draw one simple line, add a shape, add a tiny detail, then photograph the whole drawing for celebration."

**Child responses:**
1. (Ideal) Child completes Guided Drawing Capability Gate / Step 4: Record Future Preview Shape with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 4: Record Future Preview Shape into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 4: Record Future Preview Shape before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 4: Record Future Preview Shape and move to the next preserved source step.
2. (Unexpected) [repair] For Step 4: Record Future Preview Shape, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 4: Record Future Preview Shape, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Optional drawing step cards are documented in the source helper but not built for unsupported runtime.
#### Step 5: Close The Capability Probe

**Runtime AI instruction:** Goal: close with a clear product-decision outcome. Constraint: no child task, no asset claim, no result logging as playable. Tone: concise. Progress evidence: final report lists this as unsupported/gated. Branch behavior: handle ideal, unexpected, and no-response cases with the follow-up policies. Frame/source guardrail: blocking is the correct source-intent outcome until material workflow support exists.

**Example AI line:** [concise] "Guided Drawing remains gated: paper workflow support is required before play."

**Child responses:**
1. (Ideal) Child completes Guided Drawing Capability Gate / Step 5: Close The Capability Probe with the promised choice, capture, word, or observation.
2. (Unexpected) Child tries to change Step 5: Close The Capability Probe into a different game, skips the required evidence, or asks for a thinner shortcut.
3. (No response) Child pauses during Step 5: Close The Capability Probe before giving the required evidence, choice, or observation.

**AI follow-up policy:**
1. (Ideal) [confirm] Name the concrete evidence from Step 5: Close The Capability Probe and move to the next preserved source step.
2. (Unexpected) [repair] For Step 5: Close The Capability Probe, acknowledge the attempt, restore the original sequence, and offer one valid action that keeps the promise.
3. (No response) [scaffold] For Step 5: Close The Capability Probe, give one short example tied to the current screen state and invite the child to repeat or choose.

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Unsupported gate summary only: show the product-decision gate, unsupported status, and no launch button in the runtime metadata.
