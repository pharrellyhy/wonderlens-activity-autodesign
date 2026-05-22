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

1. (Ideal) The child accepts the coloring game player role, notices the starter cue, or names something connected to the first real-world color choice.
2. (Unexpected) Child asks for another game, starts the making step before the Coloring Game mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Coloring Game title/trigger card without taking the coloring game player role yet.

**AI follow-up:**

1. Name the coloring game player role, connect it to the starter cue, and preview the first making step.
2. Acknowledge the request, return to the Coloring Game promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Coloring Game role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.
> RESOLVED BLOCKER: Runtime image generation: Approved minimum contract uses static or no-image fallback and does not claim unavailable runtime artwork.
> RESOLVED BLOCKER: Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I prompt, you try the activity action, and we save one token for each turn."

**Child responses:**

1. (Ideal) The child agrees to the making step loop for Coloring Game or asks for the easiest version.
2. (Unexpected) Child tries to skip the first real-world color choice, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Coloring Game rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Coloring Game loop as AI prompt, child making step, saved token, and show the first response slot.
2. Keep the rule tied to the first real-world color choice, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Coloring Game rule in one sentence and ask for yes, a point, or the first chance to add one making step.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. Use `runtime_coloring_line_art_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Choose A Region:**

**Runtime AI instruction:** Show a line-art region before asking for a real-world color source.

**Example AI line:** "This big petal needs a color. Can you photograph or name something with the color you want?"

**Child responses:**

1. (Ideal) The child adds the requested first real-world color choice piece, mark, word, or construction step.
2. (Unexpected) Child skips the first real-world color choice step, changes the target, or asks the AI to complete the making for them.
3. (No response) Child looks at the first real-world color choice prompt without adding a mark, piece, word, or choice.

**AI follow-up:**

1. Name what the child added, show how it changes the creation, and cue the next build step.
2. Keep the target small, restate the one required first real-world color choice step, and offer an easier mark, word, or piece.
3. [wait 2s] Model the smallest possible first real-world color choice addition, then invite the child to copy or choose one part.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `runtime_coloring_line_art_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package.
> RESOLVED BLOCKER: Runtime image generation: Approved minimum contract uses static or no-image fallback and does not claim unavailable runtime artwork.
> RESOLVED BLOCKER: Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 2 -- Apply Or Describe The Color:**

**Runtime AI instruction:** Fill the region only if coloring UI exists; otherwise describe the intended fill.

**Example AI line:** "Your object gave us red. I will put red on the petal if coloring is available."

**Child responses:**

1. (Ideal) The child adds the requested region fill or honest fallback piece, mark, word, or construction step.
2. (Unexpected) Child skips the region fill or honest fallback step, changes the target, or asks the AI to complete the making for them.
3. (No response) Child looks at the region fill or honest fallback prompt without adding a mark, piece, word, or choice.

**AI follow-up:**

1. Name what the child added, show how it changes the creation, and cue the next build step.
2. Keep the target small, restate the one required region fill or honest fallback step, and offer an easier mark, word, or piece.
3. [wait 2s] Model the smallest possible region fill or honest fallback addition, then invite the child to copy or choose one part.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `runtime_coloring_line_art_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package.
> RESOLVED BLOCKER: Runtime image generation: Approved minimum contract uses static or no-image fallback and does not claim unavailable runtime artwork.
> RESOLVED BLOCKER: Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

**Round 3 -- Reveal The Artwork:**

**Runtime AI instruction:** Show the evolving artwork or a static preview and recap the colors.

**Example AI line:** "Now your artwork has colors from real things you found."

**Child responses:**

1. (Ideal) The child adds the requested finished coloring choice piece, mark, word, or construction step.
2. (Unexpected) Child skips the finished coloring choice step, changes the target, or asks the AI to complete the making for them.
3. (No response) Child looks at the finished coloring choice prompt without adding a mark, piece, word, or choice.

**AI follow-up:**

1. Name what the child added, show how it changes the creation, and cue the next build step.
2. Keep the target small, restate the one required finished coloring choice step, and offer an easier mark, word, or piece.
3. [wait 2s] Model the smallest possible finished coloring choice addition, then invite the child to copy or choose one part.

**Screen:** Shows the active round token, child response slot, and source-intent cue. Use `runtime_coloring_line_art_01` in `center_card_area` during prod.step_2; prod.step_3.round_1-3; fallback: If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package.
> RESOLVED BLOCKER: Runtime image generation: Approved minimum contract uses static or no-image fallback and does not claim unavailable runtime artwork.
> RESOLVED BLOCKER: Coloring or recoloring UI: Approved minimum contract may describe intended fills or use static preview when live recoloring is unavailable.
> RESOLVED BLOCKER: UI state or progress memory: Approved minimum state contract keeps per-round choices visible when supported and uses a stateless fallback when not.
> RESOLVED BLOCKER: Prebuilt asset display: Approved minimum asset-display contract uses declared asset IDs, display timing, and no-display fallback.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your turns made the board light up: first we started, then we tried, then we finished the mission."

**Child responses:**

1. (Ideal) The child notices how the finished coloring choice changed the Coloring Game board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Coloring Game payoff or ignores how the saved making step turns connect.
3. (No response) Child watches the Coloring Game reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's making step turns, name one concrete saved token, and invite a short reflection.
2. Hold the Coloring Game reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Coloring Game board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Change. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Coloring Game moment, asks to play again, or watches the coloring game recap badge.
2. (Unexpected) Child shifts topic before the recap names the making step skill or Form and Change.
3. (No response) Child stays on the Coloring Game recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same build mechanic and the coloring game frame.
2. Close Coloring Game first, name the practiced making step, and then offer one next-round seed.
3. [wait 2s] Read the Coloring Game badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `build`, focal attribute `coloring_game`, and next-step hint.
