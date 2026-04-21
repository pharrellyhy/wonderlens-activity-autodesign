## The Sound Stage

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Sound Stage |
| Activity Category | Collection/Tracking Exploration (Out-of-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Form, Connection, Perspective |
| Related Concepts | Expression, Collaboration, Pattern, Role |
| ATL Skills Focus | Communication Skills (expressing, listening), Thinking Skills (creative thinking), Social Skills (collaboration) |
| Game Style | ensemble_show |
| Trigger Entity | Any entity that makes or could make a sound, OR any outdoor context |
| Mapping Source | property-bridge |

### A.1 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{sound}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_0.senses.sound          # most common path (crayons, piano, bath_toys, libraries, etc.)
  - tier_0.senses.song_sound     # e.g., bird
  - tier_0.senses.silent_flight  # e.g., butterfly (absence-of-sound still qualifies)
  - tier_0.senses.squeak_sound   # e.g., rubber_duck
  - tier_0.senses.robot_sounds   # e.g., toy_robot
```

### B. Activity Overview

**① Brief Description**

After the child photographs any object, the AI looks at the photo and IMAGINES what sound it would make based on its visual form — a long hard shape might go TAP, a thin crinkly thing might go RUSTLE, a smooth round object might go CLINK. The AI announces this creative inference with excitement and onomatopoeia, then frames the child as a "Sound Conductor" who must find 3 more items that look like they could make interesting sounds. For each find, the AI examines the photo and imagines the sound from visual form. The child can agree or suggest their own sound. At the climax, the AI narrates a concert — each performer plays its solo, then ALL TOGETHER NOW!

**② Educational Purpose (KUD)**

- **K (Know):** Objects have visual properties (shape, size, material, texture) that suggest what kind of sound they could make; different objects produce different types of sounds; an ensemble is a group of performers playing together; a conductor directs when and how performers play
- **U (Understand):** Every object has its own unique qualities — its Form (shape, material, texture) tells us what kind of sound it might make; when different things work together, they create something bigger than any one alone — that is Connection; giving voice to voiceless things is Perspective
- **D (Do):** Listen to AI's creative sound inference and respond with agreement or their own interpretation; search for objects with interesting visual forms that suggest sounds; combine individual sounds into an ensemble performance and direct the concert

**③ Design Highlight**

The AI looks at each photographed object and IMAGINES what sound it would make from its visual form — creative inference, not sound verification. "This stick LOOKS like it would go TAP TAP TAP!" The child can agree or suggest their own sound. Each object gets a performer identity. The magic moment is the full ensemble concert: solos first, then ALL TOGETHER NOW, with the child directing volume, speed, and combinations.

**④ Typical Scenario**

Child photographs a wooden spoon. AI notices the long, hard shape and imagines "Your spoon LOOKS like it would go TAP TAP TAP!" The child hunts for 3 more "secret instruments" — a smooth pebble, a crinkly leaf, a bendy stick — and the AI imagines each one's sound from its visual form. Then the AI narrates a full concert with solos and an ensemble finale.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4–6)

#### Step 1: Transition Bridge

**AI says:** (delighted, hushed wonder) "Ooh! A wooden spoon! Look at that — it's long and hard and smooth. I bet if you tapped it on a table, it would go... TAP TAP TAP! Like a little drumstick! I think your spoon is a SECRET instrument. And I bet there are MORE secret instruments hiding around here. What do you think — are there other things nearby that could make cool sounds?"

**Child responses:**

1. (Ideal) "Yeah! I can find more!" / "The pot makes sounds too!" / "Everything makes sounds!"
2. (Unexpected) "Spoons don't make music." / "I use it for cooking."
3. (No response) Child looks at the spoon or around the room.

**AI follow-up:**

1. (warm, inspired) "You already know! Secret instruments are EVERYWHERE — you just have to look at their shape and imagine the sound. I think YOU could be the Sound Conductor! Find 3 things that LOOK like they could make interesting sounds!"
2. (playful, validating) "Cooking AND music! When you stir a pot, that spoon goes TAP TAP TAP on the sides. That IS music! What if we found more things that LOOK like they could make sounds?"
3. (wait 2s) (gentle, coaxing) "Your spoon is long and hard — that's why it would go TAP TAP TAP, like a drum! I wonder what OTHER shapes are hiding around here. Smooth things? Crinkly things? Each shape makes a different sound!"

**Screen:** Object photo centered with golden glow, animated sound waves pulsing outward, bouncing text showing imagined sound: "TAP TAP TAP!"


#### Step 2: Rule Introduction + Demo

**AI says:** (excited, rallying) "You are now the Sound Conductor! Your mission: find 3 things that LOOK like they could make interesting sounds. Take a photo of each one. I'll look at it and imagine what sound it would make — then YOU tell me if you agree or hear something different! After that, we put on a BIG concert! Ready, Conductor?"

**Child responses:**

1. (Ideal) "Ready!" / "Let's find instruments!" / "I know one already!"
2. (Unexpected) "What's a conductor?" / "How do you know the sounds?"
3. (No response) Child looks around, uncertain where to start.

**AI follow-up:**

1. (pumped up) "Excellent! A conductor is the boss of the music — YOU tell the performers when to play, how loud, and how fast. Now look around — find something with an interesting shape. Round things, crinkly things, bendy things — they ALL have hidden sounds!"
2. (warm, explaining) "A conductor tells musicians when to play! And the sounds? I look at the SHAPE. Long hard things go TAP. Round smooth things go CLINK. Crinkly things go CRUNCH. But YOUR idea counts too! Now go find your first secret instrument!"
3. (wait 2s) (encouraging) "Try looking for something with a cool shape! Something round, something crinkly, something bendy. Take a photo — I'll tell you what sound I think it would make!"

**Screen:** Mission card with "Sound Conductor" badge (baton with sound waves), four performance slots (first filled with trigger object photo and its sound), three empty slots with sound wave icons, and numbered checklist.


#### Step 3: Multi-Round Interaction

**Round 1:**

*(Child takes a photo of a smooth round pebble)*

**AI says:** (examining with excitement) "Ooh, let me look at this one... It's smooth and round and hard — like a tiny marble! I think if you tapped it, it would go... CLINK CLINK — like tiny bells! What do you think, Conductor? Does that sound right, or do you hear a different sound?"

**Child responses:**

1. (Ideal — agrees) "Yeah, CLINK CLINK!" / "Like bells!"
2. (Ideal — suggests own) "No, I think it goes BONK BONK!" / "More like CLICK CLICK!"
3. (No response) Child is silent, thinking.

**AI follow-up:**

1. (thrilled, dramatic) "CLINK CLINK it is! Pebble is now the BELL-RINGER of the Sound Stage — CLINK CLINK CLINK! Two more secret instruments to find, Conductor!"
2. (delighted, accepting) "BONK BONK! Even BETTER! You're the conductor — YOUR ears decide! Pebble is now the BONKER — BONK BONK BONK! Two more to find!"
3. (wait 2s) (playful) "I think CLINK CLINK — but you could also say CLICK or CLACK or BONK! Let's call it CLINK CLINK for now — two more instruments to find!"

**Screen:** Pebble photo in slot 2 with sound wave burst; label shows sound in bouncy letters; counter "1 of 3 secret instruments found."

**Round 2 — "The Snare Drum":** Child photographs a crinkly leaf. AI examines and imagines: "Thin and dry and crinkly — CRUNCH CRUNCH, like a tiny snare drum!" Child agrees or suggests own sound. AI names it the "Snare Drum." Includes redirect if child describes color instead of responding to sound.

**Round 3 — "The Guitar":** Child photographs a bendy stick. AI examines: "Long and thin and bendy — TWAAANG, like a tiny guitar!" Child agrees or offers alternative. AI names it the "Guitar" and announces cast complete. Includes stuck branch: "Look for something ROUND (CLINK), CRINKLY (CRUNCH), or LONG (TAP)!"


#### Step 4: Celebration

**AI says:** (grand, theatrical) "Ladies and gentlemen, boys and girls — welcome to the SOUND STAGE CONCERT! Your conductor has discovered FOUR secret instruments. Let the show begin!"

(dramatic, building) "First up — the Drummer, Wooden Spoon! *TAP TAP TAP!* The crowd is clapping along!"

(bright, ringing) "Next — the Bell-Ringer, Pebble! *CLINK CLINK CLINK!* Like tiny bells — the audience is swaying!"

(mysterious, crisp) "Now, the Snare Drum, Leaf, crunches in... *CRUNCH CRUNCH CRUNCH...* Ohhh, so crispy and rhythmic!"

(stretchy, vibrating) "And finally — the Guitar, Stick! *TWAAANG!* The crowd is cheering!"

(huge, explosive energy) "And now, Conductor — ALL TOGETHER NOW! Spoon drums TAP TAP, Pebble rings CLINK CLINK, Leaf crunches CRUNCH CRUNCH, Stick twangs TWAAANG — ALL AT ONCE! The audience is ON THEIR FEET! BRAVO! BRAVOOO!"

**Child responses:**

1. (Ideal) Child cheers, laughs, claps, or shouts "AGAIN!" / "LOUDER!"
2. (Unexpected) "That was funny!" / "I want just the pebble and stick!"

**AI follow-up:**

1. (thrilled) "The conductor says LOUDER! TAP TAP! CLINK CLINK! CRUNCH CRUNCH! TWAAANG! THE CROWD IS GOING CRAAAZY! Standing ovation! Encore, encore!"
2. (delighted) "Just pebble and stick — a duet! CLINK CLINK... TWAAANG... CLINK TWANG CLINK TWANG! Ohhh, what a cool combo! You know exactly what sounds good together!"

**AI says:** (warm, reflective) "Wow, Conductor! You turned ordinary things into a whole band. Four secret instruments, four different sounds, one incredible concert. Which performer was your favorite?"

**Child responses:**

1. (Ideal) "The pebble because CLINK is so pretty!" / "The stick because TWANG is funny!"
2. (Unexpected) "All of them!" / "I want to find more!"

**AI follow-up:**

1. (impressed) "Great pick! Every performer had its own special sound — and that sound came from its SHAPE. The way something LOOKS tells you what it might SOUND like!"
2. (delighted) "ALL of them! That's what a conductor would say — every performer matters! Together they made something none of them could make alone!"

**Screen:** Four performer photos in semicircle stage layout; each glows and sound text pulses during its solo; during "ALL TOGETHER NOW" all glow with sound waves, confetti, stars, and animated crowd cheering at the bottom. Golden star on child's favorite. Banner: "4 secret instruments, 1 amazing concert!"


#### Step 5: Closing + IB Concepts

**AI says:** (proud, warm celebration) "You are an incredible Sound Conductor! You looked at each thing and imagined what sound it could make just from the way it LOOKS — you discovered its Form, its own special voice. Then you put them all together and created something beautiful — that is Connection, when different things work as a team. And YOU gave voice to things that can't speak — that is Perspective, hearing the world in a brand new way. You earned your Sound Conductor badge! Bravo, Conductor!"

**Child responses:**

1. (Engaged) Cheers, talks about wanting to find more instruments, or hums the sounds.
2. (Quiet) Smiles or says nothing.
3. (No response) Child looks at the screen.

**AI follow-up:**

1. (encouraging) "Next time you see ANYTHING — a fork, a shoe, a pillow — try imagining its sound! Every shape is hiding a secret instrument inside. See you at the next concert, Conductor!"
2. (warm) "Your Sound Conductor badge is glowing! You'll never look at ordinary things the same way again. Bye for now, Conductor!"
3. (wait 2s) (soft) "Your badge is saved. The Sound Stage is always waiting for its conductor. Bravo!"

**Screen:** "Sound Conductor" badge — golden baton with four tiny icons (spoon, pebble, leaf, stick) orbiting it and sound waves radiating outward. "Form," "Connection," and "Perspective" in artistic green, gold, and sky-blue lettering with sound wave, chain-link, and ear icons. Four collection photos as insets in stage arc. Gentle confetti falling.
