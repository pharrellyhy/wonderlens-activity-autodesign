## Teddy's Cozy Care Station

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Teddy's Cozy Care Station |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T0 (ages 2–4) |
| Core IB Key Concepts | Responsibility, Connection |
| Related Concepts | Emotion, Safety, Expression, Empathy |
| ATL Skills Focus | Social Skills (empathy, caring), Communication Skills (expressing, listening), Self-Management Skills (emotional regulation) |
| Game Style | care_station |

### A.5 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/daily_objects/plush_toys.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_0.appearance.color
  - tier_0.senses.surface_feel
  - tier_1.function.comfort_hugging
  - tier_1.function.pretend_friend
  - tier_1.function.sleep_routine_helper
  - tier_1.senses.warmth_after_hug
  - tier_2.context.comfort_during_new_situations
  - tier_2.function.deep_pressure_comfort
  - tier_2.function.role_play_practice
```

### B. Activity Overview

**① Brief Description**

After the child photographs their teddy bear, the AI notices teddy is shivering and needs help. The child becomes teddy's special caretaker across three rounds of escalating needs — from a physical problem (teddy is cold) to an emotional one (teddy is scared of the dark) to a complex combination (cold AND lonely AND can't sleep). Each time the child helps, teddy VISIBLY gets better — shivering stops, tears dry, a smile grows — and teddy's gratitude deepens, until by the final round teddy calls the child by name.

**② Educational Purpose (KUD)**

- **K (Know)**: Learn the words "shivering," "cozy," "scared," "brave," and "friend." Learn that when someone is cold, a blanket or hug helps. Learn that when someone is scared, a gentle voice helps. Learn that caring for someone builds a special bond.
- **U (Understand)**: Understand that taking care of someone means noticing what they need and doing something about it — that is Responsibility. Understand that when you care for someone, you build a special bond with them — that is Connection.
- **D (Do)**: Practice identifying emotional and physical needs through listening. Practice proposing care solutions using simple language. Practice expressing empathy and comfort through words and sounds.

**③ Design Highlight**

This design creates a VISIBLE TRANSFORMATION arc. When the child says "hug teddy," the AI doesn't just say "good job" — it narrates teddy CHANGING: the shivering stops, warmth spreads, a smile appears, and teddy speaks in a voice that gets more personal and affectionate each round. By Round 3, teddy calls the child by name, creating an emotional payoff that makes the child feel they truly helped a friend. The escalation from physical needs to emotional needs to complex needs stretches the child's empathy naturally.

**④ Typical Scenario**

Child photographs their teddy bear on the bed → AI notices teddy is shivering and needs help → child becomes teddy's caretaker, solving escalating needs while watching teddy visibly recover and grow more grateful with each round.

### C. Interaction Flow

> Recommended Tier: T0 (ages 2–4)

#### Step 1: Transition Bridge

**AI says:** (soft gasp, concerned) "Oh! Look at teddy! So soft and fluffy... but wait — is teddy shivering? Brrr brrr! I think teddy needs help!"

**Child responses:**

1. (Ideal) "Teddy cold!" / "Oh no!" / "Help teddy!"
2. (Unexpected) "Teddy is happy!" / "That's my teddy!" / "I love teddy!"
3. (No response) Child looks at the screen silently.

**AI follow-up:**

1. (warm, encouraging) "Yes! Teddy is cold! You noticed! Can YOU help teddy feel better?"
2. (gentle, playful) "You love teddy! Teddy loves you! But look — brrr — teddy is a little shivery. Can you help?"
3. (wait 2s) (soft whisper) "Teddy is going brrr brrr. Can you hear it? Teddy needs a friend!"

**Screen:** Teddy bear photo centered with soft blue background, gentle shivering wobble animation, small snowflake sparkles, and a worried-face icon pulsing in the corner.

#### Step 2: Rule Introduction + Demo

**AI says:** (excited whisper) "You can be teddy's helper! Here's how. I tell you what teddy needs. You fix it! Like this — teddy says: 'My nose is cold!' What do we do? Boop! We warm the nose! Ready?"

**Child responses:**

1. (Ideal) "Ready!" / "Boop!" / "Yes!"
2. (Unexpected) "Teddy nose!" / "Where's the nose?"
3. (No response) Child is quiet, watching.

**AI follow-up:**

1. (cheery) "Boop! Teddy's nose is warm now! See? You did it! Here comes the first big one..."
2. (playful) "Yes, teddy's little nose! Boop — warm! Easy! Now teddy needs MORE help. Listen..."
3. (wait 2s) (gentle, coaxing) "Boop! We warmed teddy's nose! So easy. Now teddy needs your help again. Listen..."

**Screen:** Teddy photo with small blue nose highlighted; on response, warm orange glow spreads over nose, sparkle appears, and "Teddy's Caretaker" text with heart icon at top.

#### Step 3: Multi-Round Interaction

**Round 1 — "Teddy is cold!"** (Physical need — simple, high-success)

**AI says:** (storytelling, worried voice) "Oh no! Teddy is shivering! Brrr brrr brrr! 'I'm so cold!' says Teddy. Teddy needs something warm. What should we do?"

**Child responses:**

1. (Ideal) "Hug teddy!" / "Blanket!" / "Cover teddy!"
2. (Unexpected) "Teddy is cold!" / "Brrr!" / child repeats the problem
3. (No response) Child is quiet or looking at teddy.

**AI follow-up:**

1. (delighted, narrating transformation) "You gave teddy a big warm hug! Look... teddy stops shivering... the brrrs go quiet... and a tiny smile appears! 'Ahhhh,' says Teddy, 'warm now! Thank you!' Teddy feels SO much better!"
2. (validating, then guiding) "Brrr is right! Poor teddy! What if we gave teddy a big warm hug? Try saying 'hug teddy!'"
3. (wait 2s) (soft prompt) "Teddy says brrr brrr! So cold! Should we give teddy a hug? Say 'hug!'"

**Screen:** Teddy with shivering animation and brrr text bubbles; on response, shivering stops, warm golden glow wraps around teddy, smile appears, speech bubble says "Warm now!" and one floating heart drifts up.

**Round 2 — "Teddy is scared!":** Teddy's eyes are big and round — scared of the dark. Child comforts teddy with words like "it's okay!" or "I'm here!" AI narrates the transformation: eyes relax, soft light fills the background, teddy whispers "You make me brave" with a bigger smile. Two hearts float up — relationship deepening.

**Round 3 — "Teddy is cold AND lonely AND can't sleep!":** Teddy is shivering again, wide-eyed, and whispers "I feel all alone." Complex need requires multiple comforts. Child says "I'll stay!" or combines actions. AI narrates a three-stage transformation (cold solved → scared solved → lonely solved). Teddy calls child by name: "[Child's name], you're my best friend in the whole world!" Three hearts float up and a gold star appears.

#### Step 4: Celebration

**AI says:** (soft, deeply warm) "Look at teddy now. Remember when teddy was shivering and scared? Now teddy is warm... brave... and smiling SO big. Teddy whispers: '[Child's name]... thank you for taking care of me. You made the cold go away. You made the dark not scary. And you made me feel not alone. You're the best caretaker in the whole world.'"

**Child responses:**

1. (Ideal) Child smiles, hugs their actual teddy, says "I love teddy!" / "Yay!"
2. (Unexpected) "More!" / "Teddy wake up!" / "Again!"

**AI follow-up:**

1. (beaming) "Teddy loves you SO much. You helped with everything!"
2. (playful, warm) "Teddy says 'help me again tomorrow!' You're the best!"

**Screen:** Full-screen warm golden glow with teddy centered. Quick transformation montage (shivering → warm → scared → brave → lonely → happy). Golden badge "Teddy's Best Caretaker" with bear-paw-and-heart icon, warm confetti, three hearts in a row below the badge.

#### Step 5: Closing + IB Concepts

**AI says:** (warm, reflective, proud) "You know what you did today? Every time teddy needed something — warm, brave, not alone — YOU helped. Helping someone who needs you... that's called Responsibility. And now you and teddy have a special bond — teddy trusts you, and you care for teddy. That's called Connection. You're not just a helper. You're teddy's best friend!"

**Child responses:**

1. (Ideal) "I'm teddy's friend!" / "Bye teddy!" / child hugs their teddy bear
2. (Unexpected) "Teddy is my friend!" / any response
3. (No response) Child is quiet, perhaps hugging teddy.

**AI follow-up:**

1. (soft, closing) "Best friends! Night night, teddy. Night night, caretaker! See you next time!"
2. (warm) "Yes! Connection is when you care for someone and they care for you. Like you and teddy!"
3. (gentle close) "Teddy is smiling at you. Night night, teddy. Night night, best friend!"

**Screen:** "Responsibility" in warm gold with caring-hands icon, "Connection" in soft pink with heart-link icon, teddy in cozy sleeping pose with peaceful smile, "Teddy's Best Caretaker" badge glowing softly at bottom.
