## Current Topic Interview

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Current Topic Interview |
| Activity Category | cat1 |
| Recommended Tier | T2 |
| Core IB Key Concepts | Form and Causation |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | logical_reasoning (primary), observation, language expression |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

The child discusses an age-appropriate topic by giving an opinion and a reason.

**2. Educational Purpose (KUD)**

- **K (Know):** Children know the visible rule, role, or clue that starts this activity.
- **U (Understand):** Children understand that their action changes what happens next.
- **D (Do):** Children complete the repeated `deduce` action and explain or show one piece of evidence.

**3. Design Highlight**

Fresh full-rerun package generated from the workbook-derived source snapshot. Runtime wording uses behavior contracts plus example lines so the LLM can adapt while preserving the source sequence.

**4. Typical Scenario**

Older child and parent select an age-appropriate news, school, community, or nature topic.

### C. Interaction Flow

> Recommended Tier: T2

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open from the Current Topic Interview starter cue, name the child as current topic interview player, and preview the first opinion-and-reason interview turn.

**Example AI line:** "Current Topic Interview starts now. You are the current topic interview player; I will help one opinion-and-reason interview turn at a time."

**Child responses:**

1. (Ideal) The child accepts the current topic interview player role, notices the starter cue, or names something connected to the first opinion.
2. (Unexpected) Child asks for another game, starts the clue guess before the Current Topic Interview mission is framed, or follows an unrelated topic.
3. (No response) Child watches the Current Topic Interview title/trigger card without taking the current topic interview player role yet.

**AI follow-up:**

1. Name the current topic interview player role, connect it to the starter cue, and preview the first clue guess.
2. Acknowledge the request, return to the Current Topic Interview promise, and offer the smallest supported first action.
3. [wait 2s] Point to the Current Topic Interview role card and first token, then model one tiny in-frame response.

**Screen:** Shows title, child role, source trigger, and empty progress tokens.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain the rule as an action loop and name any required asset or honest fallback.

**Example AI line:** "Rule: I give one opinion-and-reason interview cue, you answer or try it, and we save one progress token each turn."

**Child responses:**

1. (Ideal) The child agrees to the clue guess loop for Current Topic Interview or asks for the easiest version.
2. (Unexpected) Child tries to skip the first opinion, ignore the required rule/asset, or count a different kind of response.
3. (No response) Child looks at the Current Topic Interview rule strip without confirming how to start the first turn.

**AI follow-up:**

1. Restate the Current Topic Interview loop as AI prompt, child clue guess, saved token, and show the first response slot.
2. Keep the rule tied to the first opinion, name the supported fallback, and offer one allowed first turn.
3. [wait 2s] Read the Current Topic Interview rule in one sentence and ask for yes, a point, or the first chance to make a clue-based guess.

**Screen:** Shows the rule strip, current round token, and asset/fallback chip. No prebuilt asset is required; show progress tokens and the active opinion-and-reason interview cue.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Start The Source Action:**

**Runtime AI instruction:** Preserve the workbook promise: The child discusses an age-appropriate topic by giving an opinion and a reason. Ask the child to use clues to infer in the first small turn.

**Example AI line:** "Let us start: The child discusses an age-appropriate topic by giving an opinion and a reason. Try the first opinion with a reason now."

**Child responses:**

1. (Ideal) The child uses the first opinion to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the first opinion, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the first opinion clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, reveal whether that clue fits, and set up the next evidence step.
2. Name the clue in the first opinion, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Point to one visible clue for the first opinion, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and opinion-and-reason interview cue. No prebuilt asset is required; show progress tokens and the active opinion-and-reason interview cue.

**Round 2 -- Repeat With A Variation:**

**Runtime AI instruction:** Keep the same source frame and ask for a second deduce turn with a small variation.

**Example AI line:** "Now try one more turn in the same game. What changes this time?"

**Child responses:**

1. (Ideal) The child uses the reason for the opinion to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the reason for the opinion, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the reason for the opinion clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, reveal whether that clue fits, and set up the next evidence step.
2. Name the clue in the reason for the opinion, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Point to one visible clue for the reason for the opinion, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and opinion-and-reason interview cue. No prebuilt asset is required; show progress tokens and the active opinion-and-reason interview cue.

**Round 3 -- Complete The Loop:**

**Runtime AI instruction:** Ask the child to recap, show, choose, or explain the result so the source action has closure.

**Example AI line:** "What should we remember from your opinion-and-reason interview turns?"

**Child responses:**

1. (Ideal) The child uses the polite follow-up thought to make or revise a plausible guess.
2. (Unexpected) Child guesses without using the polite follow-up thought, asks for the answer, or follows a detail that is not evidence yet.
3. (No response) Child studies the polite follow-up thought clue area without offering a maybe-guess.

**AI follow-up:**

1. Tie the guess to the visible clue, reveal whether that clue fits, and set up the next evidence step.
2. Name the clue in the polite follow-up thought, separate it from one distracting detail, and ask for one maybe-guess.
3. [wait 2s] Point to one visible clue for the polite follow-up thought, model a "maybe it is" guess, and invite a copy or new guess.

**Screen:** Shows the active round token, child response slot, and opinion-and-reason interview cue. No prebuilt asset is required; show progress tokens and the active opinion-and-reason interview cue.

#### Step 4: Magic Moment

**Runtime AI instruction:** Reveal the outcome caused by the child's saved turns and recap concrete choices.

**Example AI line:** "Your opinion-and-reason interview turns are saved: we started Current Topic Interview, practiced opinion-and-reason interview, and reached the finish."

**Child responses:**

1. (Ideal) The child notices how the polite follow-up thought changed the Current Topic Interview board or names a favorite saved turn.
2. (Unexpected) Child asks to restart before seeing the Current Topic Interview payoff or ignores how the saved clue guess turns connect.
3. (No response) Child watches the Current Topic Interview reveal without commenting on the saved turns.

**AI follow-up:**

1. Tie the reveal to the child's clue guess turns, name one concrete saved token, and invite a short reflection.
2. Hold the Current Topic Interview reveal, point to the saved turn that matters, and ask what changed because of it.
3. [wait 2s] Narrate one before/after change from the Current Topic Interview board, then offer two favorite-turn choices.

**Screen:** Shows a final board with saved turns, asset/fallback note when relevant, and source-specific payoff.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close with the two key concepts and one parent-reviewable recap.

**Example AI line:** "Today you practiced Form and Causation. You used your own answer to move the activity forward."

**Child responses:**

1. (Ideal) The child names a favorite Current Topic Interview moment, asks to play again, or watches the current topic interview recap badge.
2. (Unexpected) Child shifts topic before the recap names the clue guess skill or Form and Causation.
3. (No response) Child stays on the Current Topic Interview recap badge without responding.

**AI follow-up:**

1. Offer a next-time variation using the same deduce mechanic and the current topic interview frame.
2. Close Current Topic Interview first, name the practiced clue guess, and then offer one next-round seed.
3. [wait 2s] Read the Current Topic Interview badge in one sentence and end with one concrete next-time invitation.

**Screen:** Recap badge lists title, mechanic `deduce`, focal attribute `current_topic_interview`, and next-step hint.
