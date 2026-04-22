## The Nature Orchestra

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Nature Orchestra |
| Activity Category | Collection/Tracking Exploration (Out-of-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Form, Connection, Perspective |
| Related Concepts | Expression, Collaboration, Pattern, Role |
| ATL Skills Focus | Communication Skills (expressing, listening), Thinking Skills (creative thinking), Social Skills (collaboration) |
| Game Style | ensemble_show |
| Design Version | 1.0 |
| Last Updated | 2026-04-21 |

### A.1 Entity Attributes Covered

Attribute IDs from `data/mappings_dev20_0318/animals/birds.yaml` `tier_guidance` that this activity exercises. Consumed by the upstream matcher to route photographed entities to this game.

```yaml
entity_attributes_covered:
  - tier_0.appearance.body_color
  - tier_0.senses.song_sound
  - tier_0.function.sits_on_branch
  - tier_1.context.branches_and_trees
  - tier_1.function.singing_to_communicate
  - tier_1.senses.song_variety
  - tier_2.context.shared_soundscape
  - tier_2.function.song_as_language
  - tier_2.senses.song_as_signal
```

### A.2 Constellation Adaptation Notes

Recipe for running this activity when the photographed entity is a constellation
neighbor of Bird (e.g., other vocal outdoor creatures like sparrow, robin,
pigeon, crow, duck) instead of a generic bird. The neighbor list, bridge type,
and initial bridge prompt will live in `data/constellation_map.yaml` under
`mapped_entity: bird` (Cat5 entry pending per that file's coverage notes) —
this section describes how The Nature Orchestra adapts mechanically for a
bridged entity.

**Preserve** — must not change across neighbors:
- The "Nature Conductor" role_title and the 4-performer assembly (lead singer + drummer + whisperer + bell-ringer) — the ensemble cast is the Performance pillar's stage.
- The ALL-TOGETHER-NOW finale where every performer plays at once under the child's direction ("LOUDER!") — this is the magic moment; solos without the unison climax collapse the game.
- The child-assigns-sound mechanic where the child (not AI) picks each found object's concert sound — ownership of the assigned sounds is what makes the child feel like the boss of the orchestra.

**Swap** — re-phrase for the bridged entity:
- Transition bridge "Listen — it is singing a little song!" → neighbor's signature sound (pigeon: "coo coo cooo, a soft rolling song"; crow: "CAW CAW, bold announcements"; duck: "quack quack, chatting to the water"; robin: "bright morning whistle"). Keep "what do you think it is singing about?"
- The photographed bird's role label "Lead Singer" → same label for all vocal neighbors (any bird-family neighbor is still the Lead Singer); the SOUND it makes in the concert scene changes (crow: "CAW CAW CAW", duck: "QUACK QUACK QUAAACK").
- Step 2 framing "a bird was singing by itself — let's give it a band" → "[neighbor] was making its [sound] all alone — let's find it some bandmates!"
- Step 5 Closing insight "different sounds work as a team" stays verbatim — the 3 found-objects (stick, leaf, pebble) don't change; only the lead singer's voice does.

**Watch** — gotchas to avoid:
- If the neighbor is a non-songbird (crow, duck, pigeon), don't romanticize the voice as "beautiful song" — reframe as "strong caller" or "chatty voice" so the child's real bird doesn't feel misrepresented.
- If the photographed bird is silent in the photo (common), describe an IMAGINED song the child can help invent; don't claim "listen, it IS singing!" when the child heard nothing.
- Never let the AI pick sounds for the stick, leaf, and pebble — the child's agency in naming those is what makes them own the orchestra; scaffold at most by offering a menu ("TAP or CRACK?") not a decision.

### B. Activity Overview

**① Brief Description**

The child photographs a bird singing on a branch and becomes the "Nature Conductor" — tasked with assembling a Nature Orchestra. The child searches for 3 more natural "performers" (a stick, a leaf, a pebble), photographs each one, and assigns a unique sound to it. At the climax, the AI narrates a concert where each performer plays its solo, then all together in a grand ensemble finale that the child gets to direct.

**② Educational Purpose (KUD)**

- **K (Know):** Birds use songs to communicate; different natural objects can produce different sounds (tapping, rustling, clinking); an orchestra is a group of performers playing together; a conductor directs when performers play
- **U (Understand):** Every object has its own unique qualities — its Form tells us what kind of sound or expression it might make; when different things work together, they create something bigger than any one alone — that is Connection
- **D (Do):** Assign creative sounds to found objects using onomatopoeia and imagination; listen to the AI's concert narration and respond with directing choices; combine individual sounds into an ensemble performance

**③ Design Highlight**

The child becomes a "conductor" who gives voice to voiceless things. Each natural object gets a personality through the sound the child assigns — a stick becomes "the drummer," a leaf becomes "the whisperer." The magic moment is the full ensemble concert, where every item performs its sound in sequence and then all together, with the child directing volume, speed, and combinations.

**④ Typical Scenario**

A child in the park photographs a bird singing on a branch, then hunts for 3 natural "performers" nearby — a stick, a leaf, and a pebble — assigns each a unique sound, and conducts a narrated Nature Orchestra concert.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (delighted, hushed wonder) "Oh! A bird! Listen — it is singing a little song up on that branch. It sounds so beautiful, like a tiny musician! What do you think it is singing about?"

**Child responses:**

1. (Ideal) "It's singing about the sun!" / "It's happy!"
2. (Unexpected) "I don't know." / "It's just chirping."
3. (No response) Child watches the bird quietly.

**AI follow-up:**

1. (warm, inspired) "A song about the sun! What a lovely idea. This bird is like a little performer on a stage. I wonder if we could find MORE performers to join it!"
2. (playful, validating) "Chirping IS singing! Every chirp is a tiny note. This bird is like a singer on a stage branch. What if it had a whole band to play with?"
3. (wait 2s) (gentle, coaxing) "That bird is singing all by itself up there. It sounds a bit lonely! What if we found it some friends to make music with?"

**Screen:** Bird photo centered with soft green glow, tiny animated musical notes drifting upward from the bird.


#### Step 2: Rule Introduction + Demo

**AI says:** (excited, rallying) "You are now a Nature Conductor! Your mission has three parts. First, find three things in nature that could be performers — like a stick, a leaf, or a rock. Second, take a photo of each one. Third, YOU give each one a special sound. Then we put on a Nature Concert! Ready, Conductor?"

**Child responses:**

1. (Ideal) "Ready!" / "Let's find performers!"
2. (Unexpected) "What's a conductor?" / "What sounds?"
3. (No response) Child looks around, uncertain where to start.

**AI follow-up:**

1. (pumped up) "Great! A conductor is the boss of the music. YOU tell the performers when to play. Now look around — find a stick, a leaf, or a rock. Take a photo when you spot one!"
2. (warm, explaining) "A conductor tells musicians when to play — loud, soft, fast, slow! And the sounds? YOU choose! A stick could go TAP TAP, a leaf could go RUSTLE RUSTLE. You decide! Now go find your first performer!"
3. (wait 2s) (encouraging) "Try looking on the ground near trees. A stick would be a great first performer! Or a leaf, or a little rock. Take a photo of whatever you find!"

**Screen:** Mission card with "Nature Conductor" badge (baton with musical notes), five performance slots (first filled with bird photo labeled "Lead Singer"), and numbered checklist.


#### Step 3: Multi-Round Interaction

**Round 1:**

*(Child takes a photo of a stick on the ground)*

**AI says:** (excited discovery) "Ooh, a stick! Great find, Conductor! Now here is the big question — if this stick could make ONE sound, what would it be? Show me! Say the sound!"

**Child responses:**

1. (Ideal) "TAP TAP TAP!" / "KNOCK KNOCK!" / "BOOM BOOM!"
2. (Unexpected) "I don't know what sound." / "Sticks don't make sounds."
3. (No response) Child is silent, thinking.

**AI follow-up:**

1. (thrilled, dramatic) "TAP TAP TAP! I love it! Stick is now the DRUMMER of the Nature Orchestra — TAP TAP TAP! What a beat! Two more performers to find, Conductor!"
2. (warm, scaffolding) "What if you tapped a stick on the ground? It would go TAP TAP! Or maybe CRACK! You pick the sound you like best. What do you think — TAP or CRACK?"
3. (wait 2s) (playful, modeling) "Hmm, a stick... I think it could go TAP TAP TAP, like a drum! Or maybe CLICK CLICK. Which one do you like? You choose!"

**Screen:** Stick photo slides into second performance slot with musical note burst; label shows child's assigned sound in bouncy letters; counter "1 of 3 performers found."

**Round 2 — "The Leaf Whisperer":** Child photographs a leaf; AI asks "If this leaf could make ONE sound, what would it be?" Child assigns a sound (RUSTLE, CRINKLE, SHHHH). AI names it the "Whisperer" of the orchestra. Includes scaffolding if child describes color instead of sound.

**Round 3 — "The Pebble Bell-Ringer":** Child photographs a pebble; AI asks for its concert sound. Child assigns a sound (CLINK, CLICK, BONK). AI names it the "Bell-Ringer" and announces cast complete. Includes stuck branch — AI suggests looking under trees for sticks, near paths for pebbles, on the ground for leaves.


#### Step 4: Celebration

**AI says:** (grand, theatrical) "Ladies and gentlemen, boys and girls — welcome to the Nature Orchestra Concert! Your conductor has assembled FOUR amazing performers. Let the show begin!"

(dramatic, building) "First up — the Lead Singer, Bird! *TWEET TWEET TWEEEEET!* The crowd goes wild!"

(building energy) "Next — the Drummer, Stick! *TAP TAP TAP!* What a beat! The audience is clapping along!"

(mysterious, soft) "Now, the Whisperer, Leaf, sneaks in... *RUSTLE RUSTLE RUSTLE...* Ohhh, so soft and beautiful!"

(bright, ringing) "And finally — the Bell-Ringer, Pebble! *CLINK CLINK CLINK!* The crowd is cheering!"

(huge, explosive energy) "And now, Conductor — ALL TOGETHER NOW! Bird sings TWEET TWEET, Stick drums TAP TAP, Leaf whispers RUSTLE RUSTLE, Pebble rings CLINK CLINK — ALL AT ONCE! The audience is ON THEIR FEET! BRAVO! BRAVOOO!"

**Child responses:**

1. (Ideal) Child cheers, laughs, claps, or shouts "AGAIN!" / "LOUDER!"
2. (Unexpected) "That was funny!" / "I want just the stick and pebble!"

**AI follow-up:**

1. (thrilled) "The conductor says LOUDER! TWEET TWEET! TAP TAP TAP! RUSTLE RUSTLE! CLINK CLINK CLINK! THE CROWD IS GOING CRAAAZY! Standing ovation! Encore, encore!"
2. (delighted) "Just stick and pebble — a duet! TAP TAP... CLINK CLINK... TAP CLINK TAP CLINK! Ohhh, what a cool combo! You are an amazing conductor — you know exactly what sounds good together!"

**AI says:** (warm, reflective) "Wow, Conductor! You built a whole orchestra from nature. Four performers, four different sounds, one amazing concert. Which performer was your favorite? Who made the best sound?"

**Child responses:**

1. (Ideal) "The stick because TAP TAP is so cool!" / "The bird because it sings for real!"
2. (Unexpected) "All of them!" / "I want to find more!"

**AI follow-up:**

1. (impressed) "Great pick! Every performer had its own special sound. That is what makes an orchestra so amazing — everyone is different, but together they make something beautiful!"
2. (delighted) "ALL of them! That is what a conductor would say — every performer matters! Together they made something none of them could make alone!"

**Screen:** Four performer photos in orchestra semicircle stage layout; each glows and sound text pulses during its solo; during "ALL TOGETHER NOW" all glow with confetti, stars, and animated crowd cheering at the bottom. Golden star on child's favorite. Banner: "4 performers, 1 amazing concert!"


#### Step 5: Closing + IB Concepts

**AI says:** (proud, warm celebration) "You are an incredible Nature Conductor! You looked at each thing you found and imagined what sound it could make — you discovered its Form, its own special voice. Then you put them all together and created something beautiful — that is Connection, when different things work as a team. And YOU gave each one a voice — that is Perspective, seeing the world through different eyes and ears. You earned your Nature Conductor badge! Bravo, Conductor!"

**Screen:** "Nature Conductor" badge — golden baton with four tiny icons (bird, stick, leaf, pebble) orbiting it. "Form," "Connection," and "Perspective" in artistic green, gold, and sky-blue lettering with musical note, chain-link, and ear icons. Four collection photos as insets in orchestra arc. Gentle confetti falling.
