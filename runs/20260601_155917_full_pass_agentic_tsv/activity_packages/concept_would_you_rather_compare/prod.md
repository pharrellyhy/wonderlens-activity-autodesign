## Would You Rather

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Would You Rather |
| Activity Category | 1 -- Voice-Led Comparison Exploration |
| Recommended Tier | T1 |
| Core IB Key Concepts | Perspective and Responsibility |
| Related Concepts | preference, tradeoff, short question |
| ATL Skills Focus | choosing, explaining, listening |
| Experience Pillar | Performance |
| Game Style | choice_chain |

### B. Activity Overview

**1. Brief Description**

The child chooses between short playful options and gives a tiny reason.

**2. Educational Purpose (KUD)**

- **K (Know):** Children notice the focal idea through one concrete child action.
- **U (Understand):** The activity keeps the original child role, device role, sequence, evidence source, and context promise connected.
- **D (Do):** The child responds with the promised choice, observation, capture, explanation, or material action.

**3. Design Highlight**

The source is intentionally simple; the stricter audit should not overfit only asset-heavy packages.

**4. Typical Scenario**

Child answers three short silly comparison prompts, explains tiny reasons, and closes with a favorite choice.

### C. Interaction Flow

Recommended Tier: T1

#### Step 1: Open The Silly Choice Round

**Runtime AI instruction:** Goal: introduce short, playful two-choice questions. Constraint: T1 max two sentences; no long setup. Tone: funny and safe. Progress evidence: child chooses, laughs, asks for choices, or listens. Branch behavior: start when the child agrees, simplify if they ask for rules, and model a tiny reason after silence. Frame/source guardrail: repeated action is compare two options, choose one, and give a tiny reason.

**Example AI line:** [funny] "Ready for a tiny Would You Rather? Pick one silly choice, then tell me why."

**Child responses:**
1. (Ideal) Child says yes, laughs, or asks for the first silly pair.
2. (Unexpected) Child asks for many rules or wants a long story instead.
3. (No response) Child waits at the empty two-choice state.

**AI follow-up policy:**
1. (Ideal) [start] "Great. I will give two short choices; you pick one and say a tiny why."
2. (Unexpected) [simple] "Only A or B, then a tiny reason like because it is funny."
3. (No response) [model] "I can show you: I choose the silly one because it makes me laugh."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** No required image; show simple two-choice runtime state.
#### Step 2: Ask The First Pair

**Runtime AI instruction:** Goal: ask one short silly pair and invite a reason. Constraint: options must be age-safe, non-shaming, and brief. Tone: playful. Progress evidence: child chooses ketchup toothbrush or chocolate-milk hair and gives any tiny reason. Branch behavior: accept either option with a reason, allow pass/neither without pressure, and repeat the two choices after silence. Frame/source guardrail: do not make questions long.

**Example AI line:** [playful] "Would you rather brush your teeth with ketchup, or wash your hair with chocolate milk?"

**Child responses:**
1. (Ideal) Child chooses ketchup toothbrush or chocolate-milk hair and says a reason such as sticky, silly, or sweet.
2. (Unexpected) Child says neither, invents an unsafe option, or gives a very long off-topic answer.
3. (No response) Child does not choose after hearing the first pair.

**AI follow-up policy:**
1. (Ideal) [respond] "That reason makes your choice clear: sticky teeth or chocolate hair would be very silly."
2. (Unexpected) [reframe] "You can say pass, or pick the less silly one. I will keep the choices safe and short."
3. (No response) [choice] "Ketchup toothbrush, or chocolate-milk hair? You can say because it is funnier."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show two abstract choice slots in runtime state; no asset dependency.
#### Step 3: Ask A Movement Pair

**Round 1 -- Movement Choice:**

**Runtime AI instruction:** Goal: ask another short pair with a different comparison dimension and scaffold a tiny reason. Constraint: one sentence question plus one optional why prompt. Tone: energetic. Progress evidence: child chooses hop everywhere or tiptoe everywhere and gives or accepts a tiny reason. Branch behavior: accept hop/tiptoe plus reason, keep movement pretend if unsafe, and model tiptoe after silence. Frame/source guardrail: keep funny compare/choose loop, not trivia.

**Example AI line:** [energetic] "Would you rather hop everywhere today, or tiptoe everywhere today?"

**Child responses:**
1. (Ideal) Child chooses hop everywhere or tiptoe everywhere and says because it is fast, sneaky, funny, or easier.
2. (Unexpected) Child tries an unsafe real movement or answers with unrelated trivia.
3. (No response) Child does not choose hop or tiptoe.

**AI follow-up policy:**
1. (Ideal) [curious] "Your reason shows the tradeoff: bouncy hopping or quiet tiptoeing."
2. (Unexpected) [safety] "Let us keep it pretend and safe. Choose hop or tiptoe with a tiny why."
3. (No response) [model] "I choose tiptoe because it feels sneaky and quiet."

**Photo capture timing:** No photo capture.

**Screen/state:** Update round counter to choice 2 of 3, preserve the two spoken options in runtime state, and keep the no-asset voice-led layout stable.
#### Step 4: Ask A Tiny Imagination Pair

**Runtime AI instruction:** Goal: ask a final short imaginative pair and invite one tiny reason. Constraint: avoid scary, gross, or humiliating options. Tone: whimsical. Progress evidence: child chooses pocket clouds or squeaky shoes and names a tradeoff. Branch behavior: reflect cozy/noisy reasons, soften scary options, and model pocket clouds after silence. Frame/source guardrail: no long or adult-style dilemmas.

**Example AI line:** [whimsical] "Would you rather have a pocket full of clouds, or shoes that squeak with every step?"

**Child responses:**
1. (Ideal) Child chooses pocket clouds or squeaky shoes and says because soft, funny, noisy, or useful.
2. (Unexpected) Child asks for a scary, gross, or mean option.
3. (No response) Child does not choose the final pair.

**AI follow-up policy:**
1. (Ideal) [reflect] "You compared cozy clouds with noisy shoes; that is a real choice."
2. (Unexpected) [soften] "We keep these choices silly and kind. Pick clouds or squeaky shoes."
3. (No response) [model] "I choose pocket clouds because they sound soft."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show final choice counter with the two spoken options tracked in runtime metadata; no image or generated asset is claimed.
#### Step 5: Close The Choice Chain

**Runtime AI instruction:** Goal: recap that the child compared options, chose, and gave reasons. Constraint: max two sentences; no new pair. Tone: warm and amused. Progress evidence: child repeats favorite choice or listens. Branch behavior: save the favorite choice, defer more questions to later, and close quietly if no reply. Frame/source guardrail: preserve short classic Would You Rather format.

**Example AI line:** [warm] "You made three silly choices and told your reasons. Choice chain complete."

**Child responses:**
1. (Ideal) Child names a favorite choice, such as clouds, squeaky shoes, hop, tiptoe, ketchup, or chocolate milk.
2. (Unexpected) Child asks for many more pairs immediately or changes to a quiz.
3. (No response) Child gives no closing response.

**AI follow-up policy:**
1. (Ideal) [save] "Favorite choice saved with your tiny reason."
2. (Unexpected) [boundary] "More silly pairs can be another round. This choice chain is complete."
3. (No response) [quiet close] "I will save your three silly choices."

**Photo capture timing:** No photo capture in this beat.

**Screen/state:** Show completed choice chain with three saved choices and a favorite-choice slot; no image or generated asset is claimed.
