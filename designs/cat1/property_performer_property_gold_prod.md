## [Entity]'s Big Performance

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | [Entity]'s Big Performance |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T0 (ages 2–4) |
| Core IB Key Concepts | Perspective, Form |
| Related Concepts | Expression, Identity, Creativity, Discovery |
| ATL Skills Focus | Communication Skills (expressing, listening), Thinking Skills (creative thinking), Self-Management Skills (emotional regulation, confidence) |
| Experience Pillar | Performance |
| Game Style | voice_stage |
| Property Bridge | AI detects a salient property (bouncy, shiny, fluffy, big, tiny, smooth, sparkly, soft, loud, etc.) and uses it as the PERFORMANCE THEME. Child performs AS the entity with the property driving challenges. |

### A.5 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{property}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  # Any one of these supplies the salient property that becomes the performance theme.
  - tier_0.appearance.shape         # "shape performance" (bouncy/round/pointy)
  - tier_0.appearance.size          # "size performance" (tiny/giant)
  - tier_0.senses.sound             # "sound performance"
  - tier_0.function.moves           # "motion performance"
  - tier_1.appearance.shine_level   # "sparkle performance"
```

### B. Activity Overview

**① Brief Description**

After the child photographs their entity, the AI detects a standout property and turns it into a talent-show PERFORMANCE THEME. The child becomes the entity's voice and performs the property in increasingly creative ways — big, slow, then a surprise twist. A panel of silly judges reacts with over-the-top delight. Round 3 introduces a surprise context shift. The finale is a standing ovation — "The judges have NEVER seen a [property] performance like that!"

**② Educational Purpose (KUD)**

- **K (Know)**: Learn the property word (e.g., "bouncy," "round"). Learn that one property can be expressed many ways — big, small, slow, fast. Learn the word "audience." Learn that performing means showing something in a special way.
- **U (Understand)**: The same property can feel very different depending on HOW you express it — that is Perspective. The property is what MAKES the entity special and what makes the performance possible — that is Form.
- **D (Do)**: Express a property through voice and body in escalating creative challenges. Listen to performance prompts and respond with vocal variety. Adapt when a surprise twist changes the context.

**③ Design Highlight**

The property-bridge mechanic means every playthrough is unique — the AI detects a REAL property and builds the entire performance around it. Bouncy ball → bouncing talent show. Shiny fork → sparkle spectacular. Fluffy cat → fluffiness showcase. The audience of silly judges creates genuine "they loved it!" energy. The surprise twist in Round 3 (property + unexpected context) generates delight and creative stretch.

**④ Typical Scenario**

Child photographs a bouncy rubber ball → AI detects "bouncy" → "Your ball is SO bouncy! If it could be in a talent show, it would BOUNCE onto stage!" → child performs in escalating bounce challenges while silly judges react, culminating in a standing ovation.

### C. Interaction Flow

> Recommended Tier: T0 (ages 2–4)

#### Step 1: Transition Bridge

**AI says:** (delighted gasp) "Whoa! A BALL! SO bouncy! Look how round! If your ball could be in a talent show, it would BOUNCE onto stage! Boing boing boing! Show me? What does your ball sound like when it bounces?"

**Child responses:**

1. (Ideal) "Boing boing!" / "Bounce bounce!" / child makes bouncing sounds
2. (Unexpected) "That's my ball!" / "It's red!" / "I play with it!"
3. (No response) Child stares at the screen or touches the ball.

**AI follow-up:**

1. (amazed) "BOING BOING! WOW! Bounciest sound EVER! Some silly judges heard that bounce. They want MORE! Want to put on a BIG bouncy show?"
2. (warm, excited) "Your ball! So round and bouncy! I bet it has the best bounce inside. Want to do a BIG show? Some silly judges want to see it!"
3. (wait 2s) (playful whisper) "Psst... I think your ball wants to go BOING! Can you help? Some silly judges are waiting!"

**Screen:** Ball photo centered with bright stage background — spotlight beams, curtain edges; gentle bounce animation on ball photo; three shadowed character silhouettes (penguin with scorecard, hamster with popcorn, giraffe with big grin) peek in from the right.

#### Step 2: Rule Introduction + Demo

**AI says:** (excited announcer) "Welcome to the Bouncy Talent Show! Three judges! Penguin... Hamster... and tall Giraffe! They want YOUR ball to bounce! I say HOW to bounce. You bounce! Judges go CRAZY! Watch — ball says HELLO! BOING! Ohhh! Penguin dropped his scorecard! Ha! Your turn!"

**Child responses:**

1. (Ideal) Child laughs, says "BOING!" or "OK!" eagerly.
2. (Unexpected) "What's a judge?" / "I want hamster!" / child giggles.
3. (No response) Child watches quietly with interest.

**AI follow-up:**

1. (cheering) "YES! Round One! Judges ready! Penguin has his scorecard. Hamster has popcorn. Giraffe is stretching to see! Let's GO!"
2. (warm, playful) "Judges are silly friends watching! Hamster loves bouncing! Ready? You bounce, judges go WOW! Round One!"
3. (wait 2s) (encouraging) "Easy! Just bounce when I say! Judges love EVERY bounce! Here comes the first one!"

**Screen:** "BOUNCY TALENT SHOW" banner in bouncy lettering; ball photo on small stage at center-left; three cartoon judge characters (tuxedoed penguin with scorecard, hamster with popcorn, giraffe poking in from above) on the right; "Round 1" star badge in corner.

#### Step 3: Multi-Round Interaction

**Round 1 — "The BIGGEST Bounce!"** (Big, bold, high-success)

**AI says:** (bright announcer) "Round One! Your ball is on stage! Show the judges your BIGGEST, BOUNCIEST bounce! Ready? GO! BOING BOING BOING!"

**Child responses:**

1. (Ideal) "BOING BOING BOING!" / "BOUNCE!" / child makes loud bouncing sounds
2. (Unexpected) "Wheee!" / a silly sound / "I'm jumping!"
3. (No response) Child is quiet or shy.

**AI follow-up:**

1. (audience goes wild) "OHHH! Penguin DROPPED his scorecard — it says TEN! Hamster is jumping up and down — popcorn flying EVERYWHERE! Giraffe's neck is wobbling like jelly! They LOVED it! BIG gold star!"
2. (delighted, laughing) "Wheee?! Ha! Judges LOVE surprises! Penguin wrote 'WOW' on his scorecard! Hamster fell over giggling! Gold star for the surprise sound!"
3. (wait 2s) (gentle) "Even a tiny boing counts! Try a little one... boing? The judges are leaning forward with big silly faces!"

**Screen:** Stage spotlight on ball photo with bright bounce-lines; penguin fumbles scorecard showing "10!", hamster bounces with popcorn flying, giraffe's neck wobbles; gold star stamps in score area.

**Round 2 — "The Slow-Motion Bounce":** Slooow motion! "Boooooing... boooooing..." Child does the slowest bounce ever. Penguin's head follows up and down, hamster sways, giraffe's neck pendulums. The whole audience is hypnotized. Second gold star.

**Round 3 — "SURPRISE — Bounce on the MOON!" (Twist Challenge):** SURPRISE — what if your ball bounced on the MOON?! No gravity! Super slow, super HIGH! "Nobody has EVER bounced on the moon!" Stage transforms to starry space scene. Child's moon bounce sends the ball past stars and planets. Judges ERUPT — penguin drops everything, hamster stands on chair screaming "HIGHER!", giraffe's neck stretches past the screen into space. Third gold star.

#### Step 4: Celebration

**AI says:** (announcer crescendo) "Three rounds! Three gold stars! ALL judges standing! Penguin's scorecard says 'PERFECT!' Hamster throwing popcorn like confetti! Giraffe clapping WAY up high! STANDING OVATION! The judges say: 'We have NEVER seen a bouncy performance like that!' You are the BOUNCE STAR!"

**Child responses:**

1. (Ideal) Child bounces or says "BOING!" triumphantly, giggles, claps, "Yay!"
2. (Unexpected) "Again! More!" / "Encore!" / "Moon again!"
3. (No response) Child beams or watches the celebration with delight.

**AI follow-up:**

1. (overjoyed) "The BEST Bounce Star EVER! Every judge says you win! Penguin wants your autograph!"
2. (thrilled) "ENCORE? Judges are SO happy! 'Come back anytime!' You can bounce for them again another day, Bounce Star!"
3. (wait 2s) (warm) "Look at that big smile! Penguin says 'That smile bounces right off the page!' You are a REAL Bounce Star!"

**Screen:** Full celebration — confetti in bouncy rainbow colors, penguin holds "PERFECT" scorecard with sparkles, hamster throws popcorn confetti, giraffe claps at top of screen; large golden "BOUNCE STAR" badge descends with ball photo framed inside, three gold stars underneath.

#### Step 5: Closing + IB Concepts

**AI says:** (warm, reflective) "Wow, Bounce Star. One bouncy ball, SO many bounces! Big bounce, slow bounce, MOON bounce — every one different! Same ball, same bounciness, but you made it feel different every time. That's Perspective! And the round shape, the bounciness — that's what makes your ball YOUR ball. That's Form! You are the Bounce Star of the Bouncy Talent Show!"

**Child responses:**

1. (Ideal) Child bounces one more time, says "Bye ball!" or "I'm a Bounce Star!"
2. (Unexpected) "What's perspective?" / "I want to be a hamster!"
3. (No response) Child watches the screen, content.

**AI follow-up:**

1. (warm, proud) "BOING! That's ball saying 'Thank you, Bounce Star!' Bye bye! Judges are waving!"
2. (warm, simple) "Perspective means same ball, different bounces — that's what YOU showed! Hamsters are fun too — maybe next time! Bye, Bounce Star!"
3. (wait 2s) (soft, closing) "Judges waving goodbye. Penguin says 'See you next show!' Bye bye, Bounce Star. BOING!"

**Screen:** Ball photo at center with "Perspective" (speech-bubble icon with multiple bounce styles) and "Form" (ball-silhouette icon) in bright playful lettering; "BOUNCE STAR" badge with three gold stars in the corner; three judges waving; warm spotlight glow fades to cheerful close.
