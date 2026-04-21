## The Property Predictor

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Property Predictor |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | Causation, Function |
| Related Concepts | Prediction, Discovery, Properties, Interaction |
| ATL Skills Focus | Thinking Skills (critical thinking, cause-and-effect), Communication Skills (expressing, listening), Research Skills (observation, data collection) |
| Experience Pillar | Discovery |
| Game Style | property_predictor |
| Design Version | 2.0 |
| Last Updated | 2026-04-08 |
| Property Bridge | AI detects physical properties; each experiment tests what that property DOES in a scenario |
| Example Entity | Rubber ball (properties: round, bouncy, small) |

### A.1 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{property}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  # Any one of these seeds a prediction experiment.
  - tier_0.appearance.shape             # predict rolling/stacking behavior
  - tier_0.appearance.size              # predict fit/weight-ish behavior
  - tier_0.senses.touch_feel            # predict bounce/drag behavior
  - tier_1.structure.stuffing_material  # predict float/sink behavior
```

### B. Activity Overview

**1. Brief Description**: After the child photographs a rubber ball, the AI marvels at its round, bouncy-looking shape and invites the child to become a "Ball Scientist" who runs prediction experiments. The AI detects the ball's key properties — round, bouncy, small — and generates scenarios: what happens when THIS property meets THAT situation? In each round, the child must COMMIT to a prediction BEFORE the AI reveals the answer. Reveals are dramatic and scored: full points for correct, half points for close. A running tally creates genuine stakes.

**2. Educational Purpose (KUD)**:
- **K (Know)**: (1) Round things roll because they have no flat side to stop them, (2) bouncy things bounce higher off hard surfaces than soft ones, (3) small light objects can float in water if the right material, (4) rubber squishes and springs back, (5) a ball's shape makes it roll in the direction it's pushed
- **U (Understand)**: (1) When an object's property meets a situation, something specific happens — the property CAUSES the reaction (Causation), (2) Each property has a specific job or behavior — roundness rolls, bounciness springs back, smallness fits (Function)
- **D (Do)**: (1) Commit to a prediction before seeing the outcome, (2) Describe what properties CAUSE using specific vocabulary, (3) Observe cause-and-effect patterns between properties and situations

**3. Design Highlight**: The AI detects specific properties and generates scenarios that TEST those properties. The child must COMMIT before the dramatic reveal. A running score creates genuine tension. Half-points reward close guesses. Each reveal is dramatized with suspense.

**4. Typical Scenario**: Child photographs a rubber ball. AI detects "round" and "bouncy" as key properties. Child becomes a Ball Scientist who commits to predictions about the ball in different scenarios (edge of table, pillow, water, tiny tunnel), then watches dramatic reveals with a running score.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**AI says:** (delighted gasp) "Ohhh WOW — look at that ball! It's SO round and smooth and it looks like it could BOUNCE right off the screen! I can tell just by looking — this ball has some serious bouncing power. Have you ever bounced this ball really, really high?"

**Child responses:**

1. (Ideal) "Yeah, it bounces super high!" / "It goes all the way up!" / "It bounces off the walls!"
2. (Unexpected) "It's my favorite ball!" / "It's red!" / "I play catch with it!"
3. (No response) Child watches the screen silently.

**AI follow-up:**

1. (warm, impressed) "Super high! I knew it — this ball is a bouncing CHAMPION. You know a lot about how this ball moves. Hey... want to test how much you REALLY know? Like a scientist?"
2. (enthusiastic) "{Child's answer} — that's so cool! This ball looks really special. Those smooth, round curves and that bouncy rubber... want to be a SCIENTIST and test what your ball can do?"
3. (wait 3s) (soft, wondering) "This ball is so perfectly round — like a little planet! I bet it does some really cool stuff when it rolls and bounces. Want to do science experiments with me to find out?"

**Screen:** Ball photo centered with gentle bouncing animation — photo subtly pulses up and down. Soft glow outlines the ball's round shape. Tiny sparkle effects on the surface.

#### Step 2: Rule Introduction + Demo

**AI says:** (playful, scientist voice) "Okay, here's how our Prediction Lab works! I'm going to describe something that's ABOUT to happen to your ball. But before I tell you what the ball does — YOU have to lock in your prediction! You say: 'I think the ball will...' and then we find out together! Full point if you're right, half point if you're close. Let me show you!"

(demo) "Ready? I put the ball on a bumpy gravel path. What will the ball do? I PREDICT... the ball will roll straight ahead! Locked in..."

(dramatic pause) "And the answer is... the ball rolls, but zig-zags all over the place because the bumps push it sideways! I said straight, but it zig-zagged! The round shape MAKES it roll, but the bumps change the direction. Half point for me! See how it works? YOUR turn, Scientist!"

**Child responses:**

1. (Ideal) "Ready!" / "Yeah!" / "Let's go!"
2. (Unexpected) "My ball does that!" / "What's a prediction?" / "I want a point!"
3. (No response) Child is quiet, possibly processing.

**AI follow-up:**

1. (excited countdown) "Okay, Ball Scientist — Experiment Number One! Listen carefully..."
2. (delighted) "You already know what your ball does? Then you're going to be AMAZING at this! A prediction is just a guess you lock in BEFORE you find out. Here comes Experiment Number One!"
3. (wait 3s) (encouraging) "It's easy — I describe what happens, you guess what the ball does. Any guess is great! Here comes the first one..."

**Screen:** Ball photo on left. On right, "PREDICTION LAB" clipboard with scoring circles and running score "Score: 0". Demo animation: ball on gravel zig-zagging, "1/2" sparkle. "Experiment 1" badge glows.

#### Step 3: Multi-Round Interaction

**Round 1 — "The Edge of the Table" (Experiment 1):**

**AI says:** (mysterious narrator) "Experiment Number One! Your ball is sitting right on the EDGE of a table. You give it one teeny tiny push. Lock in your prediction — does the ball STAY on the table or FALL off?"

**Child responses:**

1. (Ideal) "It falls off!" / "It rolls off the edge!" / "FALL!"
2. (Unexpected) "Don't push it!" / "It breaks!" / "It stays!"
3. (No response) Child is quiet or looking at their ball.

**AI follow-up:**

1. (confirming lock-in) "Prediction locked: falls off! Here we go... *drumroll*... the ball rolls to the edge and — WHOOPS — OFF IT GOES! Round things can't stop at edges because they have no flat side to catch them! The roundness CAUSES it to roll right over! FULL POINT! Score: 1 out of 1!"
2. (warm, helping lock in) "Prediction locked as 'stays on the table.' Here we go... *drumroll*... the ball rolls to the edge and — whoops — OFF it goes! Round things can't stop at edges — no flat side to catch them! Not quite your prediction, but now you know! Half point! Score: half out of 1!"
3. (wait 3s) (helpful) "Here's a clue — your ball is SO round, and the table has an edge. If you give a round thing a tiny push near an edge... does it stop? Or keep going? Lock in your guess!"

**Screen:** Table with ball on the edge. "LOCKED IN" stamp. Drumroll. Ball rolls off in slow-motion fall. Score circle fills gold or half-gold. Running score updates.

**Round 2 — "The Pillow Bounce" (Experiment 2):** Ball bounces super high on a hard kitchen floor. Now the child predicts what happens when the SAME ball bounces on a big soft fluffy pillow. AI reveals: barely bounces at all! Soft things ABSORB the bounce. The bounciness needs something HARD to push off of. Scored with running tally.

**Round 3 — "The Water Test" (Experiment 3):** Ball is dropped into a bowl of water. Child predicts float or sink. AI reveals: PLOP — it dips down then pops right back up! Rubber balls are light and have air inside. The air and lightness CAUSE it to float. Scored accordingly.

**Round 4 — "The Tiny Tunnel" (Experiment 4) — Surprise Round:** A cardboard tube (paper towel roll) is slightly smaller than the ball. Child predicts: does the ball squeeze through or get stuck? AI reveals: rubber squishes a little, but the ball is still too big — STUCK! Even though rubber is squishy, size matters. Half-points for knowing rubber squishes. Final tally revealed.

#### Step 4: Celebration

**AI says:** (building suspense) "Okay, Ball Scientist... the experiments are DONE! Time to count your score! You predicted what your ball does at an edge... on a pillow... in water... and at a tiny tunnel. And your final score is..."

(dramatic pause, drumroll)

"...{X} out of 4! {Score-specific reaction — perfect score gets 'FOUR OUT OF FOUR! PERFECT! You are a BALL GENIUS!' / near-perfect gets 'AMAZING — almost every one right!' / any score gets warm celebration of what they learned}"

**Child responses:**

1. (Ideal) "Yay!" / "I got {X}!" / "I'm a scientist!"
2. (Unexpected) "Can we do more?" / "I want to try again!"
3. (No response) Child smiles or looks pleased.

**AI follow-up:**

1. (beaming) "The BEST Ball Scientist! Your ball is lucky to have someone who understands it so well."
2. (delighted) "You want MORE experiments? That's exactly what real scientists say! We can run more another day. But first — let me tell you something amazing..."
3. (wait 3s) (warm whisper) "You know what? I think even your ball is impressed. That's what great scientists do."

**Screen:** Giant score "{X} / 4" in bold golden numbers. Mini-icons for each experiment (table edge, pillow, water bowl, cardboard tube) with score circles. "BALL SCIENTIST" title banner. Confetti explosion for perfect score; golden frame around ball photo for any score.

#### Step 5: Closing + IB Concepts

**AI says:** (warm, reflective) "You know what you did today? Every time I described something about to happen to your ball — the edge, the pillow, the water, the tunnel — you PREDICTED what your ball would do before I even told you! You figured out that properties CAUSE things to happen!"

"Round CAUSES the ball to roll off edges. Bouncy works differently on hard and soft — the surface CAUSES the bounce to change. Light and rubbery CAUSES the ball to float. And too-big CAUSES the ball to get stuck. That's called Causation — when a property CAUSES something to happen!"

"And you noticed something else — every property has a JOB. Roundness ROLLS. Bounciness BOUNCES. Lightness FLOATS. Every property has its own Function — what it DOES! You aren't just a scientist — you're a Ball Expert!"

**Child responses:**

1. (Ideal) "Causation!" / "I'm a scientist!" / "Function!"
2. (Unexpected) "Can I test my teddy next?" / "What about other things?"
3. (No response) Child listens or looks at the screen.

**AI follow-up:**

1. (celebrating) "That's right — Causation and Function! You earned your badge, Ball Scientist. Go test your ball for real — I bet it does exactly what you predicted!"
2. (warm, excited) "YES! You can be a Property Predictor for ANYTHING — a teddy, a shoe, a spoon! Every thing has properties that DO stuff. See you next time, Scientist!"
3. (wait 3s) (gentle closing) "Great job today, Scientist. You and your ball made an awesome team. See you next time!"

**Screen:** "BALL SCIENTIST" badge centered with ball photo portrait inside. "Causation" and "Function" in golden lettering with chain-link and gear icons. Four experiment icons as small trophies around the badge. Soft golden sparkle animations. "The End" ribbon.
