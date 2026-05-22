## Coloring Game

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Coloring Game |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Change |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | creative_thinking (primary), observation, language expression |
| Experience Pillar | Creation |
| Game Style | inventor_workshop |

### B. Activity Overview

**1. Brief Description**

The screen shows fillable line art; the child photographs real-world colors; the activity maps those colors to regions and honestly falls back if live recoloring is unavailable.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `build` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

A simple line-art picture waits for colors gathered from the child environment.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the source trigger and name the child's role in this activity.

**Example AI line:** "I found a small mission for us: Coloring Game. I will guide one step at a time."

**Child responses:**

1. (Ideal) The child accepts, asks what to do, or names a related object or idea.
2. (Unexpected) Child veers away from "Transition Bridge" in Coloring Game, skips the making action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Transition Bridge", watches the current screen, or needs a first tiny making model.

**AI follow-up:**

1. [specific] Confirm the role and preview the first action without turning it into a quiz.
2. [redirect] Validate briefly, keep the Coloring Game frame, and offer one safe choice that still completes "Transition Bridge".
3. [wait 2s] [gentle] Model one tiny making step for "Transition Bridge", then invite the child to copy or choose.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Runtime image generation: Approved minimum contract uses static or no-image fallback and does not claim unavailable runtime artwork.
> RESOLVED BLOCKER: Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child confirms the rule or asks for a smaller version.
2. (Unexpected) Child veers away from "Role And Rules" in Coloring Game, skips the making action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Role And Rules", watches the current screen, or needs a first tiny making model.

**AI follow-up:**

1. [specific] Offer the smallest safe version and keep the source play frame intact.
2. [redirect] Validate briefly, keep the Coloring Game frame, and offer one safe choice that still completes "Role And Rules".
3. [wait 2s] [gentle] Model one tiny making step for "Role And Rules", then invite the child to copy or choose.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `runtime_coloring_line_art_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Choose A Region:**

**Runtime AI instruction:** Show a line-art region before asking for a real-world color source.

**Example AI line:** "This big petal needs a color. Can you photograph or name something with the color you want?"

**Child responses:**

1. (Ideal) The child provides a color source.
2. (Unexpected) Child veers away from "Choose A Region" in Coloring Game, skips the making action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Choose A Region", watches the current screen, or needs a first tiny making model.

**AI follow-up:**

1. [specific] Record the intended color and region.
2. [redirect] Validate briefly, keep the Coloring Game frame, and offer one safe choice that still completes "Choose A Region".
3. [wait 2s] [gentle] Model one tiny making step for "Choose A Region", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `runtime_coloring_line_art_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package.
> RESOLVED BLOCKER: Runtime image generation: Approved minimum contract uses static or no-image fallback and does not claim unavailable runtime artwork.
> RESOLVED BLOCKER: Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 2 -- Apply Or Describe The Color:**

**Runtime AI instruction:** Fill the region only if coloring UI exists; otherwise describe the intended fill.

**Example AI line:** "Your object gave us red. I will put red on the petal if coloring is available."

**Child responses:**

1. (Ideal) The child confirms or adjusts.
2. (Unexpected) Child veers away from "Apply Or Describe The Color" in Coloring Game, skips the making action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Apply Or Describe The Color", watches the current screen, or needs a first tiny making model.

**AI follow-up:**

1. [specific] Use the no-coloring fallback honestly.
2. [redirect] Validate briefly, keep the Coloring Game frame, and offer one safe choice that still completes "Apply Or Describe The Color".
3. [wait 2s] [gentle] Model one tiny making step for "Apply Or Describe The Color", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `runtime_coloring_line_art_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package.
> RESOLVED BLOCKER: Runtime image generation: Approved minimum contract uses static or no-image fallback and does not claim unavailable runtime artwork.
> RESOLVED BLOCKER: Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 3 -- Reveal The Artwork:**

**Runtime AI instruction:** Show the evolving artwork or a static preview and recap the colors.

**Example AI line:** "Now your artwork has colors from real things you found."

**Child responses:**

1. (Ideal) The child reacts or names a favorite color.
2. (Unexpected) Child veers away from "Reveal The Artwork" in Coloring Game, skips the making action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Reveal The Artwork", watches the current screen, or needs a first tiny making model.

**AI follow-up:**

1. [specific] Celebrate color-from-photo co-creation.
2. [redirect] Validate briefly, keep the Coloring Game frame, and offer one safe choice that still completes "Reveal The Artwork".
3. [wait 2s] [gentle] Model one tiny making step for "Reveal The Artwork", then invite the child to copy or choose.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `runtime_coloring_line_art_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package.
> RESOLVED BLOCKER: Runtime image generation: Approved minimum contract uses static or no-image fallback and does not claim unavailable runtime artwork.
> RESOLVED BLOCKER: Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child reacts, names a favorite turn, or asks to revise one part.
2. (Unexpected) Child veers away from "Magic Moment" in Coloring Game, skips the making action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Magic Moment", watches the current screen, or needs a first tiny making model.

**AI follow-up:**

1. [specific] Tie the reveal directly to the child action and invite one short reflection.
2. [redirect] Validate briefly, keep the Coloring Game frame, and offer one safe choice that still completes "Magic Moment".
3. [wait 2s] [gentle] Model one tiny making step for "Magic Moment", then invite the child to copy or choose.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Change. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child says again, names a favorite part, or quietly watches the recap.
2. (Unexpected) Child veers away from "Closing + IB Concepts" in Coloring Game, skips the making action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Closing + IB Concepts", watches the current screen, or needs a first tiny making model.

**AI follow-up:**

1. [specific] Offer a next-time variation that keeps the same source mechanic.
2. [redirect] Validate briefly, keep the Coloring Game frame, and offer one safe choice that still completes "Closing + IB Concepts".
3. [wait 2s] [gentle] Model one tiny making step for "Closing + IB Concepts", then invite the child to copy or choose.

**Screen:** Recap badge lists title, mechanic `build`, focal attribute `coloring_game`, and next-step hint.
