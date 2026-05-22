## Award Certificate

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Award Certificate |
| Activity Category | cat3 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Responsibility |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | empathy (primary), observation, language expression |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The child designs a paper award for someone they appreciate, using warm AI story framing and badge ideas without judging the final drawing.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `care` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

A family story or photographed object inspires a handmade award such as Best Helper or Best Mom.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Award Certificate. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts, asks what to do, or names a related object or idea.
2. (Unexpected) Child veers away from "Transition Bridge" in Award Certificate, skips the care or appreciation action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Transition Bridge", watches the current screen, or needs a first tiny care or appreciation model.

**AI follow-up:**

1. [specific] Confirm the role and preview the first action without turning it into a quiz.
2. [redirect] Validate briefly, keep the Award Certificate frame, and offer one safe choice that still completes "Transition Bridge".
3. [wait 2s] [gentle] Model one tiny care or appreciation step for "Transition Bridge", then invite the child to copy or choose.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child confirms the rule or asks for a smaller version.
2. (Unexpected) Child veers away from "Role And Rules" in Award Certificate, skips the care or appreciation action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Role And Rules", watches the current screen, or needs a first tiny care or appreciation model.

**AI follow-up:**

1. [specific] Offer the smallest safe version and keep the source play frame intact.
2. [redirect] Validate briefly, keep the Award Certificate frame, and offer one safe choice that still completes "Role And Rules".
3. [wait 2s] [gentle] Model one tiny care or appreciation step for "Role And Rules", then invite the child to copy or choose.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `award_inspiration_badges_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If badge assets or certificate workflow are unavailable, block at Phase 0 or run a verbal appreciation activity without claiming a certificate is created.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Choose The Person:**

**Runtime AI instruction:** Ask who receives the award and why.

**Example AI line:** "Who should receive today's award: someone who helped, tried hard, or made you smile?"

**Child responses:**

1. (Ideal) The child names a person.
2. (Unexpected) Child veers away from "Choose The Person" in Award Certificate, skips the care or appreciation action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Choose The Person", watches the current screen, or needs a first tiny care or appreciation model.

**AI follow-up:**

1. [specific] Reflect the appreciation reason.
2. [redirect] Validate briefly, keep the Award Certificate frame, and offer one safe choice that still completes "Choose The Person".
3. [wait 2s] [gentle] Model one tiny care or appreciation step for "Choose The Person", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `award_inspiration_badges_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If badge assets or certificate workflow are unavailable, block at Phase 0 or run a verbal appreciation activity without claiming a certificate is created.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

**Round 2 -- Design The Badge:**

**Runtime AI instruction:** Guide a paper-and-pencil badge with one color and one kind phrase.

**Example AI line:** "Draw one big badge shape. What color should the award use?"

**Child responses:**

1. (Ideal) The child draws or names a color.
2. (Unexpected) Child veers away from "Design The Badge" in Award Certificate, skips the care or appreciation action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Design The Badge", watches the current screen, or needs a first tiny care or appreciation model.

**AI follow-up:**

1. [specific] Offer a short phrase the child can copy or say.
2. [redirect] Validate briefly, keep the Award Certificate frame, and offer one safe choice that still completes "Design The Badge".
3. [wait 2s] [gentle] Model one tiny care or appreciation step for "Design The Badge", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `award_inspiration_badges_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If badge assets or certificate workflow are unavailable, block at Phase 0 or run a verbal appreciation activity without claiming a certificate is created.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

**Round 3 -- Present The Award:**

**Runtime AI instruction:** Invite the child to show or describe the certificate.

**Example AI line:** "Can you tell me the award name, like Best Helper or Best Mom?"

**Child responses:**

1. (Ideal) The child presents or describes the award.
2. (Unexpected) Child veers away from "Present The Award" in Award Certificate, skips the care or appreciation action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Present The Award", watches the current screen, or needs a first tiny care or appreciation model.

**AI follow-up:**

1. [specific] Celebrate the caring intention, not drawing quality.
2. [redirect] Validate briefly, keep the Award Certificate frame, and offer one safe choice that still completes "Present The Award".
3. [wait 2s] [gentle] Model one tiny care or appreciation step for "Present The Award", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `award_inspiration_badges_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If badge assets or certificate workflow are unavailable, block at Phase 0 or run a verbal appreciation activity without claiming a certificate is created.
> RESOLVED BLOCKER: Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.
> RESOLVED BLOCKER: Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child reacts, names a favorite turn, or asks to revise one part.
2. (Unexpected) Child veers away from "Magic Moment" in Award Certificate, skips the care or appreciation action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Magic Moment", watches the current screen, or needs a first tiny care or appreciation model.

**AI follow-up:**

1. [specific] Tie the reveal directly to the child action and invite one short reflection.
2. [redirect] Validate briefly, keep the Award Certificate frame, and offer one safe choice that still completes "Magic Moment".
3. [wait 2s] [gentle] Model one tiny care or appreciation step for "Magic Moment", then invite the child to copy or choose.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Responsibility. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child says again, names a favorite part, or quietly watches the recap.
2. (Unexpected) Child veers away from "Closing + IB Concepts" in Award Certificate, skips the care or appreciation action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Closing + IB Concepts", watches the current screen, or needs a first tiny care or appreciation model.

**AI follow-up:**

1. [specific] Offer a next-time variation that keeps the same source mechanic.
2. [redirect] Validate briefly, keep the Award Certificate frame, and offer one safe choice that still completes "Closing + IB Concepts".
3. [wait 2s] [gentle] Model one tiny care or appreciation step for "Closing + IB Concepts", then invite the child to copy or choose.

**Screen:** Recap badge lists title, mechanic `care`, focal attribute `award_certificate`, and next-step hint.
