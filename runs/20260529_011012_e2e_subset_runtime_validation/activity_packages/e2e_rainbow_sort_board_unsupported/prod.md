## Rainbow Sort Board

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Rainbow Sort Board |
| Activity Category | 5 -- Unsupported Persistent Board Preview |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | color lanes, grouping, persistent board |
| ATL Skills Focus | sorting, comparing, explaining |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child would sort several color tiles into persistent rainbow lanes, but the current demo must gate it.

**2. Educational Purpose (KUD)**

- **K (Know):** Children can notice color grouping into lanes through a concrete activity frame.
- **U (Understand):** The activity keeps the child action, evidence source, and support status aligned.
- **D (Do):** The child performs the promised sort action with one concrete response or evidence source.

**3. Design Highlight**

This package is part of a scoped E2E runtime validation subset. It is intentionally small so autodesign package quality, package-local assets, consumer import/conversion, and support gating can be verified without broadening into a full content batch.

**4. Typical Scenario**

The child follows the runtime prompt, the device uses only package-local assets declared by asset_id, and the consumer runtime either plays or gates the package according to demo_support.yaml.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Gate The Rainbow Board

**Runtime AI instruction:** Goal: tell the operator and child that this concept needs a persistent sorting board before runtime play. Constraint: short, clear, and non-playable; do not ask the child to pretend-sort verbally. Tone: honest and calm. Progress evidence: child or caregiver understands that the activity is not starting. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: preserve source promise by refusing to turn drag/drop sorting into a dialogue or camera substitute.

**Example AI line:** [calm] "This rainbow sorting board needs a real board screen before we can play it."

**Child responses:**
1. (Ideal) Child or caregiver accepts the gate.
2. (Unexpected) Child asks to sort by talking instead.
3. (No response) Child waits on the unsupported screen.

**AI follow-up policy:**
1. (Ideal) [brief] "We will save it for a board-ready version."
2. (Unexpected) [honest] "Talking would change the game. This one needs moving tiles."
3. (No response) [wait 2s] [gentle] "I will keep this one closed for now."

**Photo capture timing:** No photo capture; unsupported packages must not start a camera workaround.

**Screen/state:** Show unsupported gated state only; no playable cards, fake lanes, collection tray, or photo slot appear.

#### Step 2: Explain Missing Primitive

**Runtime AI instruction:** Goal: name the missing UI primitive for reviewers without presenting a child-play task. Constraint: one reviewer-facing sentence; avoid creating hidden gameplay. Tone: plain and transparent. Progress evidence: the system records unsupported_reasons and does not expose start controls. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: do not fake persistent rainbow lanes in Cat1/Cat5 templates.

**Example AI line:** [plain] "Missing primitive: persistent multi-tile drag/drop sorting lanes."

**Child responses:**
1. (Ideal) Caregiver or operator reviews the reason.
2. (Unexpected) Child asks to tap one color tile.
3. (No response) No child response is expected.

**AI follow-up policy:**
1. (Ideal) [plain] "Reason recorded."
2. (Unexpected) [boundary] "Tapping one tile would not be the sorting-board game."
3. (No response) [quiet] "The unsupported reason remains visible."

**Photo capture timing:** No photo capture.

**Screen/state:** Keep ui_template=none gated state; show support metadata outside the child play surface only.

#### Step 3: Preserve The Sorting Promise

**Round 1 -- Gated Sorting Promise:**

**Runtime AI instruction:** Goal: document that the required child action is grouping multiple items into lanes. Constraint: do not ask the child to provide an answer; this is blocked preview behavior. Tone: careful and precise. Progress evidence: reviewer can see mechanic=sort and support status unsupported. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: source promise requires persistent board state, not one-shot photo or verbal collection.

**Example AI line:** [careful] "The promised action is sorting several tiles into lanes, so this package stays gated."

**Child responses:**
1. (Ideal) Reviewer confirms sort is not playable in the current primitive.
2. (Unexpected) Someone suggests making a Cat5 photo hunt instead.
3. (No response) No interaction occurs.

**AI follow-up policy:**
1. (Ideal) [record] "Unsupported gating is correct."
2. (Unexpected) [reject drift] "A photo hunt would be a different activity, not this sorting board."
3. (No response) [record] "No gameplay started."

**Photo capture timing:** No photo capture.

**Screen/state:** No runtime board is rendered; package remains absent from playable selection.

#### Step 4: Recommend Follow-Up

**Runtime AI instruction:** Goal: assign the needed follow-up to product/UI support rather than autodesign content. Constraint: one short recommendation; no implementation inside this validation package. Tone: constructive and bounded. Progress evidence: follow-up owner is visible in final validation report. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: do not broaden this validation goal into implementing sorting UI.

**Example AI line:** [bounded] "Follow-up: add a persistent sorting-board primitive before this can run."

**Child responses:**
1. (Ideal) Reviewer accepts follow-up ownership.
2. (Unexpected) Reviewer asks to bypass the primitive.
3. (No response) No response occurs.

**AI follow-up policy:**
1. (Ideal) [record] "Follow-up recorded for product/UI."
2. (Unexpected) [boundary] "Bypassing the primitive would hide the product gap."
3. (No response) [quiet] "The recommendation stays in the report."

**Photo capture timing:** No photo capture.

**Screen/state:** Keep gated state with no assets and no start button.

#### Step 5: Close The Gated Preview

**Runtime AI instruction:** Goal: close without starting gameplay. Constraint: max one sentence; no new prompt. Tone: calm close. Progress evidence: unsupported state remains intact. Branch behavior: handle ideal, unexpected, and no response differently using the follow-up rows. Frame/source guardrail: never make unsupported mechanics playable to satisfy a demo.

**Example AI line:** [calm] "Rainbow sort board is saved as unsupported until the board exists."

**Child responses:**
1. (Ideal) Caregiver or reviewer moves on.
2. (Unexpected) Child asks to continue.
3. (No response) No response.

**AI follow-up policy:**
1. (Ideal) [close] "Closed as unsupported."
2. (Unexpected) [gentle boundary] "This one cannot continue yet."
3. (No response) [quiet close] "Unsupported preview closed."

**Photo capture timing:** No photo capture.

**Screen/state:** End on the same gated state; no playable session is created.
