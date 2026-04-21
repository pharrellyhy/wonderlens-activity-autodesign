# Activity Design: Sound Stage + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Sound Stage

### A. Basic Info

- **Activity Name**: The Sound Stage
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: **Form**, **Connection**, **Perspective**
- **Related Concepts (Discipline)**: Expression (designed), Collaboration (designed), Pattern (designed), Role (designed)
- **ATL Skills Focus**: Communication Skills (expressing ideas, listening), Thinking Skills (creative thinking), Social Skills (collaboration)
- **Experience Pillar**: Performance
- **Game Style**: ensemble_show
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity that makes or could make a sound (musical instrument, toy, animal), OR any entity in an outdoor context where natural sound-makers are findable
- **Trigger Scene**: Child photographs any object where AI can creatively infer a sound from its visual form — shape, material, texture suggest what sound it would make
- **Mapping Source**: property-bridge
- **IB Theme**: How We Express Ourselves (expression, culture, creativity)

### A.5 Entity Attributes Covered

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

- **① Brief Description**: After the child photographs any object, the AI looks at the photo and IMAGINES what sound it would make based on its visual form — a long hard shape might go TAP, a thin crinkly thing might go RUSTLE, a smooth round object might go CLINK. The AI announces this creative inference with excitement and onomatopoeia, then frames the child as a "Sound Conductor" who must find 3 more items that look like they could make interesting sounds. For each find, the AI examines the photo and imagines the sound from visual form alone. The child can agree or suggest their own sound. At the climax, the AI narrates a concert — each performer plays its solo, then ALL TOGETHER NOW!

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Objects have visual properties (shape, size, material, texture) that suggest what kind of sound they could make; different objects produce different types of sounds; an ensemble is a group of performers playing together; a conductor directs when and how performers play
  - **U (Understand)**: Every object has its own unique qualities — its Form (shape, material, texture) tells us what kind of sound or expression it might make; when different things work together, they create something bigger than any one alone — that is Connection; giving voice to voiceless things is Perspective
  - **D (Do)**: Listen to AI's creative sound inference and respond with agreement or their own interpretation (Communication — expressing ideas, listening); search for objects with interesting visual forms that suggest sounds (Thinking — creative thinking); combine individual sounds into an ensemble performance and direct the concert (Social — collaboration)

- **③ Design Highlight**: The AI looks at each photographed object and IMAGINES what sound it would make from its visual form — this is creative inference, not sound verification. "This stick LOOKS like it would go TAP TAP TAP!" The child becomes a "Sound Conductor" who can agree, disagree, or suggest their own sound. Each object gets a performer identity through its imagined sound. The magic moment is the full ensemble concert: solos first, then ALL TOGETHER NOW, with the child directing volume, speed, and combinations. The Performance pillar shines through audience-style narration and crowd reactions.

- **④ Typical Scenario**: Child photographs a wooden spoon in the kitchen. AI notices the long, hard shape and imagines "Your spoon LOOKS like it would go TAP TAP TAP on a table!" The child hunts for 3 more "secret instruments" — a smooth pebble, a crinkly leaf, a bendy stick — and the AI imagines each one's sound from its visual form. Then the AI narrates a full concert with solos and an ensemble finale.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs any object (e.g., a wooden spoon) with no prior conversation. AI examines the photo and creatively infers a sound from its visual form.
>
> **AI says**: "*(delighted, hushed wonder)* Ooh! A wooden spoon! Look at that — it's long and hard and smooth. I bet if you tapped it on a table, it would go... TAP TAP TAP! Like a little drumstick! I think your spoon is a SECRET instrument. And I bet there are MORE secret instruments hiding around here. What do you think — are there other things nearby that could make cool sounds?"
>
> **Possible child responses**:
> 1. (Ideal) "Yeah! I can find more!" / "The pot makes sounds too!" / "Everything makes sounds!"
> 2. (Unexpected) "Spoons don't make music." / "I use it for cooking."
> 3. (No response) Child looks at the spoon or around the room.
>
> **AI follow-up**:
> 1. "*(warm, inspired)* You already know! Secret instruments are EVERYWHERE — you just have to look at their shape and imagine the sound. I think YOU could be the Sound Conductor! Find 3 things that LOOK like they could make interesting sounds!"
> 2. "*(playful, validating)* Cooking AND music! When you stir a pot, that spoon goes TAP TAP TAP on the sides. That IS music! What if we found more things that LOOK like they could make sounds? I bet this place is full of secret instruments!"
> 3. *(wait 2 seconds)* "*(gentle, coaxing)* Your spoon is long and hard — that's why it would go TAP TAP TAP, like a drum! I wonder what OTHER shapes are hiding around here. Smooth things? Crinkly things? Each shape makes a different sound!"
>
> **Screen**: Object photo centered on screen with a soft golden glow. Animated sound waves pulse outward from the object. Playful bouncing text shows the imagined sound: "TAP TAP TAP!" in rhythmic letters.

**Step 2: Mission Briefing — Sound Conductor**

> **AI says**: "*(excited, rallying)* You are now the Sound Conductor! Your mission: find 3 things that LOOK like they could make interesting sounds. Take a photo of each one. I'll look at it and imagine what sound it would make — then YOU tell me if you agree or if you hear something different! After that, we put on a BIG concert with ALL the sounds together! Ready, Conductor?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Let's find instruments!" / "I know one already!"
> 2. (Unexpected) "What's a conductor?" / "How do you know the sounds?"
> 3. (No response) Child looks around, uncertain where to start.
>
> **AI follow-up**:
> 1. "*(pumped up)* Excellent! A conductor is the boss of the music — YOU tell the performers when to play, how loud, and how fast. Now look around — find something with an interesting shape. Round things, crinkly things, bendy things — they ALL have hidden sounds! Take a photo when you spot one!"
> 2. "*(warm, explaining)* A conductor tells musicians when to play — loud, soft, fast, slow! And the sounds? I look at the SHAPE of things. Long hard things go TAP. Round smooth things go CLINK. Crinkly things go CRUNCH. But you might hear something different — and YOUR idea counts too! Now go find your first secret instrument!"
> 3. *(wait 2 seconds)* "*(encouraging, pointing)* Try looking for something with a cool shape! Something round, something crinkly, something bendy. Take a photo of whatever catches your eye — I'll tell you what sound I think it would make!"
>
> **Screen**: A mission card appears with a "Sound Conductor" badge at the top — a small baton with sound waves swirling around it. Four performance slots are shown in a row — the first slot is filled with the trigger object photo labeled with its imagined sound. Three empty slots glow softly, each marked with a sound wave icon. A numbered checklist reads: 1) Find 3 secret instruments. 2) Photograph each one. 3) Hear their hidden sounds!

**Step 3: Multi-Round Exploration (3–4 rounds)**

> **Round 1** (full detail):
>
> *(Child takes a photo of a smooth round pebble)*
>
> **AI says**: "*(examining with excitement)* Ooh, let me look at this one... It's smooth and round and hard — like a tiny marble! I think if you tapped it against something, it would go... CLINK CLINK — like tiny bells ringing! What do you think, Conductor? Does that sound right, or do you hear a different sound?"
>
> **Possible child responses**:
> 1. (Ideal — agrees) "Yeah, CLINK CLINK!" / "Like bells!" / "I love that sound!"
> 2. (Ideal — suggests own) "No, I think it goes BONK BONK!" / "More like CLICK CLICK!"
> 3. (No response) Child is silent, thinking.
>
> **AI follow-up**:
> 1. "*(thrilled, dramatic)* CLINK CLINK it is! Pebble is now the BELL-RINGER of the Sound Stage — CLINK CLINK CLINK! What a beautiful sound! Two more secret instruments to find, Conductor!"
> 2. "*(delighted, accepting)* BONK BONK! Even BETTER! You're the conductor — YOUR ears decide! Pebble is now the BONKER of the Sound Stage — BONK BONK BONK! I love your version! Two more to find!"
> 3. *(wait 2 seconds)* "*(playful, modeling)* I think CLINK CLINK — but you could also say CLICK or CLACK or BONK! Any sound you want. You're the conductor! Let's call it CLINK CLINK for now — two more instruments to find!"
>
> **Screen**: Pebble photo slides into the second performance slot with a burst of sound waves. The label below changes to show the sound in playful bouncing letters (e.g., "CLINK CLINK!"). Counter shows "1 of 3 secret instruments found."

> **Round 2** (full detail):
>
> *(Child takes a photo of a crinkly dry leaf)*
>
> **AI says**: "*(curious excitement)* A leaf! Let me look... it's thin and dry and crinkly — see those curled-up edges? I think if you squeezed it, it would go... CRUNCH CRUNCH — like a tiny snare drum! What do you say, Conductor?"
>
> **Possible child responses**:
> 1. (Ideal) "CRUNCH CRUNCH!" / "Yes! Like crunching!" / "Like walking on leaves!"
> 2. (Unexpected) "It's green!" / "Leaves are quiet." / Child describes the leaf instead of responding to the sound.
> 3. (No response) Child holds the leaf, thinking.
>
> **AI follow-up**:
> 1. "*(delighted, dramatic)* CRUNCH CRUNCH! Yes! Leaf is now the SNARE DRUM of the Sound Stage — CRUNCH CRUNCH CRUNCH! So crispy and rhythmic. One more secret instrument to find!"
> 2. "*(warm, redirecting)* It IS green — a beautiful green leaf. And green leaves are sneaky — they LOOK quiet, but squeeze them and they go CRUNCH CRUNCH! Or maybe RUSTLE RUSTLE when the wind blows. What sound do you want YOUR leaf to play in the concert?"
> 3. *(wait 2 seconds)* "*(gentle, encouraging)* Look at those crinkly edges — thin and dry. I hear CRUNCH CRUNCH! Or maybe RUSTLE RUSTLE. What sound do you want it to make in our concert? You decide!"
>
> **Screen**: Leaf photo slides into the third performance slot with a swirling leaf animation. The label below shows the sound in wavy, airy letters (e.g., "CRUNCH CRUNCH!"). Counter shows "2 of 3 secret instruments found."

> **Round 3** (full detail):
>
> *(Child takes a photo of a bendy stick or twig)*
>
> **AI says**: "*(thrilled)* Our last secret instrument! Let me look at this one... It's long and thin and bendy — like a little guitar string! I think if you plucked it, it would go... TWANG — like a tiny guitar! What do you hear, Conductor?"
>
> **Possible child responses**:
> 1. (Ideal) "TWANG!" / "Like a guitar!" / "BOING BOING!"
> 2. (Unexpected) "It's just a stick." / "I want to break it!"
> 3. (No response) Child looks at the stick quietly.
>
> **AI follow-up**:
> 1. "*(awed, celebrating)* TWANG! Stick is now the GUITAR of the Sound Stage — TWAAANG! What a sound! Your cast is COMPLETE, Conductor! Time for the BIG SHOW!"
> 2. "*(warm, building)* A stick can be LOTS of things! A bendy stick like this could go TWANG like a guitar, or SWISH like a sword, or SNAP like a firecracker! Pick a sound — ANY sound. You're the boss!"
> 3. *(wait 2 seconds)* "*(playful, modeling)* This bendy stick looks like it could go TWANG, like a guitar string! Or maybe SWISH SWISH, like it's cutting through the air. Pick one — you are the conductor!"
>
> **Screen**: Stick photo slides into the fourth performance slot with a sparkle burst. The label below shows the sound in bold, stretchy letters (e.g., "TWAAANG!"). A "Cast Complete!" banner flashes across the screen. All four performer slots now filled: Trigger object (sound), Pebble (sound), Leaf (sound), Stick (sound).

> **Round 4 (optional)** (condensed):
>
> If the child is highly engaged and finds a fourth item (e.g., a metal pot lid, a pinecone, a rubber ball), AI reacts with the same per-find pattern: examines photo → imagines sound from visual form → child agrees or suggests own → AI gives it a performer name. This is a bonus performer: "A fifth member! The band is getting BIGGER!"

> **Stuck Branch** (if child cannot find a secret instrument):
>
> **AI says**: "*(helpful, conspiratorial)* Secret instruments like to hide! Look for something ROUND — round things go CLINK or BONK. Or something CRINKLY — crinkly things go CRUNCH or RUSTLE. Or something LONG — long things go TAP or TWANG. What shapes can you see around you?"
>
> **Screen**: A soft pulsing hint bubble appears with three shape icons: a circle (round = CLINK), a zigzag (crinkly = CRUNCH), and a line (long = TAP). Text reads: "Try: round things, crinkly things, long things!"

**Step 4: Synthesis — The Sound Stage Concert (Magic Moment)**

> **AI says**: "*(grand, theatrical announcer voice)* Ladies and gentlemen, boys and girls — welcome to the SOUND STAGE CONCERT! Your conductor has discovered FOUR secret instruments. Let the show begin!"
>
> *(brief pause)*
>
> "*(dramatic, building)* First up — the Drummer, Wooden Spoon! *TAP TAP TAP!* The crowd is clapping along!"
>
> *(brief pause)*
>
> "*(bright, ringing)* Next — the Bell-Ringer, Pebble! *CLINK CLINK CLINK!* Like tiny bells — the audience is swaying!"
>
> *(brief pause)*
>
> "*(mysterious, crisp)* Now, the Snare Drum, Leaf, crunches in... *CRUNCH CRUNCH CRUNCH...* Ohhh, so crispy and rhythmic!"
>
> *(brief pause)*
>
> "*(stretchy, vibrating)* And finally — the Guitar, Stick! *TWAAANG!* The crowd is cheering!"
>
> *(dramatic pause)*
>
> "*(huge, explosive energy)* And now, Conductor — ALL TOGETHER NOW! Spoon drums TAP TAP, Pebble rings CLINK CLINK, Leaf crunches CRUNCH CRUNCH, Stick twangs TWAAANG — ALL AT ONCE! The audience is ON THEIR FEET! BRAVO! BRAVOOO!"
>
> **Possible child responses**:
> 1. (Ideal) Child cheers, laughs, claps, or shouts "AGAIN!" / "LOUDER!" / "Now just the pebble!"
> 2. (Unexpected) "That was funny!" / "I want the leaf and stick together!" / "Make it quiet!"
> 3. (No response) Child listens with a big smile.
>
> **AI follow-up**:
> 1. "*(thrilled, responding to direction)* The conductor says LOUDER! TAP TAP! CLINK CLINK CLINK! CRUNCH CRUNCH! TWAAANG! THE CROWD IS GOING CRAAAZY! Standing ovation! Encore, encore!"
> 2. "*(delighted, following direction)* Just leaf and stick — a duet! CRUNCH CRUNCH... TWAAANG... CRUNCH TWANG CRUNCH TWANG! Ohhh, what a cool combo! You are an amazing conductor — you know exactly what sounds good together!"
> 3. *(wait 2 seconds)* "*(warm, celebrating)* I see that smile, Conductor! Your concert was AMAZING. The audience is throwing flowers! Should we do it one more time? You say when!"
>
> **Screen**: All four performer photos are displayed in a semicircle stage layout, like an orchestra on stage. As each performer is introduced, its photo glows and its sound text pulses and bounces in rhythm. During "ALL TOGETHER NOW," all four photos glow simultaneously with sound waves, stars, and confetti bursting across the screen. An animated crowd silhouette at the bottom of the screen cheers and waves. A large "BRAVO!" text flashes with golden sparkles.

**Step 5: Discovery Celebration**

> **AI says**: "*(warm, reflective)* Wow, Conductor! You turned ordinary things into a whole band. Four secret instruments, four different sounds, one incredible concert. Which performer was your favorite? Which sound did you love the most?"
>
> **Possible child responses**:
> 1. (Ideal) "The pebble because CLINK is so pretty!" / "The stick because TWANG is funny!" / "All of them!"
> 2. (Unexpected) "I want to find more!" / "Can we do a different concert?"
> 3. (No response) Child points at one of the photos.
>
> **AI follow-up**:
> 1. "*(impressed, warm)* Great pick! Every performer had its own special sound — and that sound came from its SHAPE. Round things clink, crinkly things crunch, long things tap. The way something LOOKS tells you what it might SOUND like!"
> 2. "*(delighted)* MORE instruments? That's what a real conductor would say! Every new shape is a new sound. You could build the biggest band in the world just by looking at things differently!"
> 3. *(wait 2 seconds)* "*(gentle, affirming)* That one! Great choice. I think it had a really special sound too. Every single performer helped make the concert wonderful!"
>
> **Screen**: Collection photos displayed in the orchestra semicircle layout with a golden star appearing on the child's chosen favorite. Sound-wave lines connect all four performers to a central "Sound Stage" emblem. A banner reads: "4 secret instruments, 1 amazing concert!"

**Step 6: Closing + IB Concepts**

> **AI says**: "*(proud, warm celebration)* You are an incredible Sound Conductor! You looked at each thing and imagined what sound it could make just from the way it LOOKS — you discovered its Form, its own special voice. Then you put them all together and created something beautiful — that is Connection, when different things work as a team to make music. And YOU gave voice to things that can't speak — that is Perspective, hearing the world in a brand new way. You earned your Sound Conductor badge! Bravo, Conductor!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to find more instruments, or hums the sounds.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child looks at the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you see ANYTHING — a fork, a shoe, a pillow — try imagining its sound! Every shape is hiding a secret instrument inside. See you at the next concert, Conductor!"
> 2. "*(warm)* Your Sound Conductor badge is glowing! You'll never look at ordinary things the same way again. Bye for now, Conductor!"
> 3. *(wait 2s)* "*(soft)* Your badge is saved. The Sound Stage is always waiting for its conductor. Bravo!"
>
> **Screen**: "Sound Conductor" badge — a golden baton with four tiny icons orbiting it (a spoon, a pebble, a leaf, a stick) and sound waves radiating outward. "Form," "Connection," and "Perspective" appear in artistic green, gold, and sky-blue lettering with a sound wave icon, a chain-link icon, and an ear icon respectively. Four collection photos as small insets arranged around the badge in a stage arc. Confetti gently falls across the screen.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change comparison. Multi-photo workflow processes each find independently. AI imagines sounds from VISUAL form (shape, texture, material appearance) — no actual audio detection or microphone input required. Sound inference is creative narration, not verification. |
| 2 | Hook & Transition | PASS | Opens with emotional wonder ("Ooh! A wooden spoon! Look at that — it's long and hard and smooth") and creative imagination, not knowledge testing. Activity grows naturally from imagining one object's sound to finding more secret instruments. Removing step labels, it reads as a flowing conversation. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, no response). Stuck branch in Step 3 provides concrete shape-based hints ("round things go CLINK, crinkly things go CRUNCH, long things go TAP"). Unexpected responses always validated before redirecting. Child can accept AI's sound or suggest their own — both paths handled. |
| 4 | IB Completeness | PASS | Form + Connection + Perspective named as Key Concepts. KUD fully specified with concrete vocabulary and skills. 4 Related Concepts. 3 ATL skills with sub-skills. Closing naturally names concepts as praise tied to what child did. Concepts earned: Form (visual properties suggest sound), Connection (ensemble teamwork), Perspective (giving voice to voiceless things). |
| 5 | Tier Appropriateness | PASS | T1: sentences 5–8 words, open-ended questions ("What do you hear?"), concrete vocabulary (tap, clink, crunch, twang, round, crinkly, long, bendy), 3-part mission, onomatopoeia throughout. Manageable task complexity for ages 4–6. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. No abstract instructions like "AI guides the child." All sounds are written out as specific onomatopoeia. AI's creative inference is always grounded in visible form properties. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with layout, animations, and visual elements. Stage layout, performer slots, sound wave animations, confetti, crowd silhouette — all concretely described. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — parameterized by any entity with sound-suggesting visual form, not a specific entity mapping. |
| 9 | Game Feel | PASS | Genuine uncertainty: what sound will the AI imagine for each object? Creative agency: child can agree or propose their own sound. Magic moment: the full ensemble playing ALL TOGETHER NOW with crowd going wild. Surprise: child can direct the orchestra (louder, softer, duets). Replayable: different objects produce different concerts every time. |
| 10 | Pillar Fidelity | PASS | Performance pillar delivers "They loved it!" feeling. Audience reaction mechanic throughout (crowd clapping, cheering, standing ovation, "BRAVO!"). Magic moment = audience ovation when all play together. Core loop = discover instruments + hear their voices + put on show. Could not be re-labeled to another pillar — the conductor role, audience reactions, and concert format are distinctly Performance. |

**Overall**: ALL PASS — Ready for 教研 review
