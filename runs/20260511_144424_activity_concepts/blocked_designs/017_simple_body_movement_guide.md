# Constrained Blocked Design Preview: Simple Body Movement Guide

Run id: `20260511_144424_activity_concepts`
Assignment index: `017`
Activity id target: `concept_body_movement_probe`
Status: `blocked_until_product_decision`
Category decision: `cat1`
Canonical mechanic: `motion_voice`
Asset policy: `required_prebuilt`

This is a run-local constrained preview for human review. It is not a valid WonderLens runtime package, must not be copied to `activities/`, and must not be logged in `results.tsv` until the blocked decisions are resolved.

## Blocking Decisions

- Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.
- Confirm approved prebuilt asset library, display contract, and asset metadata availability.

Product capability flags: `requires_asset_display, requires_motion_safety`

## Asset / UI Dependency Snapshot

- `body_movement_cards_01`: Show simple safe movement prompts.

## Proposed Runtime Shape

#### Step 1: Open The Activity

**AI says:** "I have a special simple body movement guide mission ready. First, let's make sure this is the right kind of moment: Parent starts a short movement prompt and the child has enough space."

**Child responses:**
1. (Ready) Child says yes, chooses the theme, or confirms the setup.
2. (Unsure) Child asks what to do first.
3. (Not ready) Child or caregiver says the setup is missing.

**AI follow-up:**
1. Ready: "Good. I will keep each step small and you can tell me what you notice or choose."
2. Unsure: "We will do one tiny action at a time. I will say the next move, then wait."
3. Not ready: "Let's pause this mission until the setup is safe and ready."

**Screen:** Shows a simple title, readiness prompt, and the current activity theme.

> BLOCKED ELEMENT: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements. -- the runtime must know whether this setup can be supported before this screen becomes product behavior.

#### Step 2: Set Up The Play Space

**AI says:** "Here is the plan: The AI starts a short safe movement guide and asks for caregiver approval plus clear space."

**Child responses:**
1. (Confirms setup) Child says the materials, screen, space, or mode is ready.
2. (Needs help) Child asks for help finding materials, space, or the right screen.
3. (Wants a different theme) Child suggests another object, color, artwork, word, or movement.

**AI follow-up:**
1. Confirms setup: "I will start with the easiest version and we can build up."
2. Needs help: "Ask a grown-up to help set it up, or we can save this for later."
3. Different theme: "Good choice. I can adapt the mission, but the same product rules still apply."

**Screen:** Shows the setup target, any required card/art/line-art/state area, and a waiting state before Step 3.

> BLOCKED ELEMENT: Confirm approved prebuilt asset library, display contract, and asset metadata availability. -- this setup requires a product contract for assets, UI state, material flow, movement safety, OCR, or evidence handling before it can be valid.

#### Step 3: Core Play Loop

**Round 1: Tiny reach:**

**AI says:** "First challenge: Try a small reach, wave, or stretch within safe limits."

**Child responses:**
1. (Completes action) Child performs, chooses, says, photographs, taps, draws, builds, or explains the requested action.
2. (Partial attempt) Child gives an incomplete answer or says they are still working.
3. (Stuck) Child says they do not know what to do.

**AI follow-up:**
1. Completes action: "AI praises listening and offers a seated version."
2. Partial attempt: "You started the right kind of move. Add one more detail so I know what to do next."
3. Stuck: "Try the smallest version: point, choose, say one word, or ask a grown-up for setup help."

**Screen:** Updates the first progress slot, selected card, chosen region, timer state, artwork bracket, word space, movement symbol, or material step.

> BLOCKED ELEMENT: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements. -- the product must define how this child action is captured and what the screen is allowed to claim.

**Round 2: Slow balance or pause:**

**AI says:** "Second challenge: Try a still pose or one-foot-free alternative like toe tap."

**Child responses:**
1. (Completes action) Child performs the second action and gives a reason or confirmation.
2. (Changes mind) Child chooses a different option, material, color, pose, word, or target.
3. (Needs fallback) Child cannot use the planned UI, material, asset, or movement.

**AI follow-up:**
1. Completes action: "AI avoids claiming pose detection and prioritizes comfort."
2. Changes mind: "Changing your plan is allowed. I will use your new choice from here."
3. Needs fallback: "We can switch to a voice-only pretend version, but that is a fallback, not the full activity promise."

**Screen:** Updates the second progress slot and keeps earlier choices visible so the child can compare progress.

> BLOCKED ELEMENT: Confirm approved prebuilt asset library, display contract, and asset metadata availability. -- the runtime needs state, asset display, safety, or material-pacing support to preserve this round honestly.

**Round 3: Cool down:**

**AI says:** "Final challenge: Take a breath or gentle hand motion."

**Child responses:**
1. (Completes action) Child completes the final action and explains one choice.
2. (Self-reports result) Child describes what happened without the system verifying it.
3. (Stops early) Child wants to finish after two rounds.

**AI follow-up:**
1. Completes action: "AI closes the movement safely."
2. Self-reports result: "I will trust your report and describe it as something you told me, not something I measured."
3. Stops early: "We can close with the progress you already made."

**Screen:** Shows three progress marks, or shows the honest partial-progress state if the child stops early.

> BLOCKED ELEMENT: Confirm approved prebuilt asset library, display contract, and asset metadata availability. -- the product must define progress memory, verification limits, and fallback behavior before this becomes a valid runtime loop.

#### Step 4: Magic Moment

**AI says:** "Here is what your choices made: The child completes a three-move safety star sequence."

**Child responses:**
1. (Proud) Child reacts to the result or asks to see it again.
2. (Wants change) Child wants to revise one choice.
3. (Unsure) Child asks what changed.

**AI follow-up:**
1. Proud: "You made that happen by doing the steps in order."
2. Wants change: "A revision needs the product to know which state can be changed and what stays saved."
3. Unsure: "I will point to the three choices that built the result."

**Screen:** Reveals the payoff state: final artwork, gallery title, bracket winner, story unlock, progress map, word reveal, movement badge, or certificate read-aloud.

> BLOCKED ELEMENT: Confirm approved prebuilt asset library, display contract, and asset metadata availability. -- the payoff depends on unresolved rendering, state, evidence, asset, or safety behavior.

#### Step 5: Reflect And Close

**AI says:** "Before we finish, The child names which movement felt easiest and safest."

**Child responses:**
1. (Reflects) Child names a choice, clue, strategy, feeling, material, movement, or result.
2. (No answer) Child shrugs or says they do not know.
3. (Wants another round) Child asks to continue.

**AI follow-up:**
1. Reflects: "That is the part I will remember as your activity highlight."
2. No answer: "Then I will remember that you tried the mission step by step."
3. Wants another round: "Another round needs the product to reset or continue the saved state safely."

**Screen:** Shows a concise recap payload only if the product can honestly represent the completed activity state.

> BLOCKED ELEMENT: Confirm approved prebuilt asset library, display contract, and asset metadata availability. -- recap/dashboard output cannot claim completed unsupported work until the product decision is resolved.

## Promotion Requirements

This preview can become a valid package only after the product owner resolves the listed blocking decisions. Then rerun or promote it into the normal five-file `activities/<activity_id>/` package, remove or resolve the `BLOCKED ELEMENT` comments, run author self-evaluation, obtain reviewer-agent PASS evidence, validate package files, append `results.tsv`, and mark the assignment complete.
