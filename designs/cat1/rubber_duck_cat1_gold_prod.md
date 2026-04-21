## Super Duck Workshop

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Super Duck Workshop |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T0 (ages 2–4) |
| Core IB Key Concepts | Function, Change |
| Related Concepts | Creativity, Imagination, Discovery, Expression |
| ATL Skills Focus | Thinking Skills (creative, divergent), Communication Skills (expressing, listening), Self-Management Skills (focus, engagement) |
| Game Style | inventor_workshop |

### A.5 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/daily_objects/bath_toys.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_0.appearance.body_color
  - tier_0.senses.squeak_sound
  - tier_0.function.floats_on_water
  - tier_1.function.squeeze_and_squeak
  - tier_2.appearance.cartoon_styling
  - tier_2.change.imaginary_upgrades
  - tier_2.function.pretend_character_role
  - tier_2.senses.squeak_pitch_variation
```

### A.6 Constellation Adaptation Notes

Recipe for running this activity when the photographed entity is a constellation
neighbor of Rubber Duck (e.g., bath toy, toy boat, floating ring) instead of a
rubber duck itself. The neighbor list, bridge type, and initial bridge prompt
live in `data/constellation_map.yaml` under `mapped_entity: rubber_duck` — this
section describes how Super Duck Workshop adapts mechanically for a bridged
entity.

**Preserve** — must not change across neighbors:
- The "Builder" role_title and the 3-round stacking mechanic (physical mod → sensory mod → imaginative mod) — each round's modification STAYS for the finale reveal.
- The Super [X] finale where all three mods are stacked and narrated in one breathless line — this is the "I made this!" Creation-pillar magic moment.
- The onomatopoeia ritual (whoooosh, bzzzzz, quack) — toddlers feel the sounds in their mouths; never drop to flat description.

**Swap** — re-phrase for the bridged entity:
- Entity name everywhere (Super Duck → Super Boat, Super Ring, Super [bath toy]) and the closing badge label "Duck Builder" → "Boat Builder" / "Ring Builder" etc.
- Round 1 "What if duck had WINGS? Where would duck fly?" → a physical mod that suits the neighbor (toy boat: "What if boat had ROCKETS? Where would boat blast off?"; floating ring: "What if ring had SPRINGS? How high would ring bounce?"; generic bath toy: "What if [toy] had WHEELS? Where would [toy] roll?").
- Round 3 "Talk!" quack-becomes-talk → neighbor's equivalent (boat: "horn becomes music"; ring: "squeak becomes singing"; generic bath toy: its actual sound becoming full sentences). Keep the "give it voice" beat.
- Closing Function recap "Duck floats and quacks" → neighbor's baseline functions (boat: "boat floats and moves"; ring: "ring floats and spins"; bath toy: "toy floats and [its sound]").

**Watch** — gotchas to avoid:
- If the neighbor doesn't squeak (e.g., a toy boat with no squeaker), don't demand a squeeze-sound — the "squeak_pitch_variation" attribute doesn't transfer; lean on movement/buoyancy instead.
- Keep bath-time context even when the neighbor is primarily a pool toy (floating ring) — anchor in warm-water play; don't drift into "at the beach" unless the child's photo says so.
- Never truncate to 2 mods to save time — the 3-stack is what makes Super [X] feel earned; cut transition chatter before cutting a round.

### B. Activity Overview

**① Brief Description**

After the child photographs their rubber duck, the AI marvels at how cute and squeaky it is. The child becomes a "Duck Builder" — a tiny inventor in a magic workshop. Each round, the AI proposes a wild "what if" modification to the duck: wings, glowing, talking. The child imagines what happens with each change. In the grand finale, the AI combines ALL modifications into one glorious "Super Duck" — a flying, glowing, talking duck — and the child gets to hear the whole creation described in one breathless, delightful reveal.

**② Educational Purpose (KUD)**

- **K (Know)**: Learn the words "wings," "glow," "fly," "splash," and "quack." Learn that a rubber duck floats, squeaks, and is made for bath time.
- **U (Understand)**: Understand that things have a job — a duck floats and squeaks — that's Function. Understand that when we add or change something, it becomes different — that's Change.
- **D (Do)**: Practice imagining modifications to familiar objects. Practice expressing creative ideas with simple words and sounds. Practice building on ideas across multiple rounds.

**③ Design Highlight**

The "magic workshop" metaphor turns a bath toy into raw material for invention. The child doesn't just describe their duck — they MODIFY it, round by round, with escalating absurdity (physical wings → sensory glow → imaginative talking). The payoff — "Super Duck" with ALL powers combined — creates a genuine "I made this!" moment. Every round uses onomatopoeia (whoosh, bzzz, quack) that toddlers feel in their mouths and bodies.

**④ Typical Scenario**

Child photographs their yellow rubber duck in the bathroom. AI notices how cute and squeaky it looks. Child becomes a Duck Builder who adds wild modifications one at a time, building up to the ultimate Super Duck reveal.

### C. Interaction Flow

> Recommended Tier: T0 (ages 2–4)

#### Step 1: Transition Bridge

**AI says:** (delighted squeal) "Ohhh! A duck! Quack quack! So cute. Is duck splashy today?"

**Child responses:**

1. (Ideal) "Yeah! Splash splash!" / "Duck goes quack!" / "It's my duck!"
2. (Unexpected) "It's yellow!" / "Bath time!" / "Ducky!"
3. (No response) Child is silent or looking at the duck.

**AI follow-up:**

1. (joyful) "Splash splash! Fun duck! Want to make duck SUPER?"
2. (warm, playful) "Yellow ducky! So pretty. What if duck could do NEW things?"
3. (wait 2s) (soft, inviting) "Quack quack! Duck says hi. Want to play?"

**Screen:** Rubber duck photo centered with gentle blue water ripple animation and floating bubble particles.

#### Step 2: Rule Introduction + Demo

**AI says:** (excited whisper) "You are a Duck Builder! Magic workshop! I say 'what if.' You imagine! Like this — what if duck had a HAT? Ooh! Fancy duck! Your turn now!"

**Child responses:**

1. (Ideal) "Yeah!" / "Okay!" / "Duck hat!" / giggles
2. (Unexpected) "My duck!" / "Quack!" / repeats "hat"
3. (No response) Child is quiet, watching.

**AI follow-up:**

1. (thrilled) "Duck Builder ready! Here we go!"
2. (playful) "Quack! Duck says yes! Let's build!"
3. (wait 2s) (gentle, encouraging) "Easy! I ask. You say! Ready? First one!"

**Screen:** Duck photo on the left; "Magic Workshop" banner on the right with floating animated tools (wrench, sparkle wand, paintbrush) and a "Duck Builder" badge at the top.

#### Step 3: Multi-Round Interaction

**Round 1 — "Wings!":** (physical modification — simple, high-success)

**AI says:** (amazed) "What if duck had WINGS? Whoooosh! Where duck fly?"

**Child responses:**

1. (Ideal) "Up!" / "To the sky!" / "Fly high!" / makes whoosh sound
2. (Unexpected) "Quack!" / "Splash!" / "Duck swim!"
3. (No response) Child is silent or looking at screen.

**AI follow-up:**

1. (thrilled, zooming) "WHOOOOSH! Duck fly [child's answer]! Wings go flap flap flap! Flying duck! So cool!"
2. (validating, playful) "Quack quack! Duck says yes! And with wings — whoooosh! Duck fly UP! Flap flap! Where duck go?"
3. (wait 2s) (gentle prompt) "Wings! Flap flap! Duck fly UP! Wheee! To the clouds? Or to the moon?"

**Screen:** Duck photo with animated wings sprouting from its sides, flapping gently with motion lines showing upward flight.

**Round 2 — "Glow!":** Duck glows in the dark — bzzzzz! Child picks a color. AI celebrates a flying, glowing duck with both modifications visible on screen (wings + glow).

**Round 3 — "Talk!":** Duck can TALK, not just quack. Child says what duck would say. AI delights in the flying, glowing, talking duck — all three modifications now stacked.

#### Step 4: Celebration

**AI says:** (breathless, building excitement) "Ready? Your duck has... WINGS — whoooosh! AND glow — bzzzzz! AND talks — '[child's phrase]!' It's... SUPER DUCK! Flying, glowing, talking SUPER DUCK! You built it! QUACK QUACK WHOOOOSH!"

**Child responses:**

1. (Ideal) "Super Duck!" / "WHOOOOSH!" / giggles and cheers
2. (Unexpected) "Again!" / "More!" / "Quack quack!"
3. (No response) Child watches with wide eyes or smiles.

**AI follow-up:**

1. (pure celebration) "YOU made Super Duck! Best Duck Builder EVER! Super Duck goes whoooosh, bzzzzz, quack quack!"
2. (joyful) "Quack quack! Super Duck says THANK YOU! You are the best builder!"
3. (wait 2s) (warm, proud) "Look! Super Duck! You built it! Wings, glow, talk! WOW!"

**Screen:** Grand reveal — duck with ALL modifications (wings, glow, speech bubble) center-screen, "SUPER DUCK!" in bouncy rainbow letters, confetti burst and sparkle animations.

#### Step 5: Closing + IB Concepts

**AI says:** (warm, proud) "You are Duck Builder! You changed duck. Wings! Glow! Talk! That's Change! Duck floats and quacks — that's Function! You made duck do NEW things! Super Duck Builder!"

**Child responses:**

1. (Ideal) "Super Duck!" / "I'm Duck Builder!" / smiles and giggles
2. (Unexpected) "Bye duck!" / "More please!" / "Duck is my friend!"
3. (No response) Child is quiet or smiling.

**AI follow-up:**

1. (celebrating) "Best Duck Builder! Super Duck loves you! Quack quack whoooosh! Bye bye!"
2. (warm) "Duck says bye! Build again soon! Quack!"
3. (wait 2s) (gentle close) "Super Duck Builder! Great job! Quack quack! See you!"

**Screen:** "Duck Builder" badge with wrench-and-duck icon; "Change" with transformation arrow and "Function" with gear icon in playful lettering; Super Duck floating behind the badge with soft golden glow.
