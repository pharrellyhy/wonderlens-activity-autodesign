# Activity Design: Bird + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-01 | Non-mapping design | Agent: Activity Design Agent

---

## Activity: The Nature Orchestra (大自然交响乐)

### A. Basic Info

- **Activity Name**: The Nature Orchestra (大自然交响乐)
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Outdoor)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: **Form**, **Connection**, **Perspective**
- **Related Concepts (Discipline)**: Expression (designed), Collaboration (designed), Pattern (designed), Role (designed)
- **ATL Skills Focus**: Communication Skills (expressing ideas, listening), Thinking Skills (creative thinking), Social Skills (collaboration)
- **Experience Pillar**: Performance
- **Game Style**: ensemble_show
- **Design Version**: 1.0
- **Last Updated**: 2026-04-01
- **Trigger Entity**: Bird
- **Trigger Scene**: Child spots and photographs a bird singing on a branch in the park
- **Mapping Source**: none
- **IB Theme**: How We Express Ourselves (expression, culture, creativity)

### A.5 Entity Attributes Covered

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

### A.6 Constellation Adaptation Notes

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

- **① Brief Description**: The child photographs a bird singing on a branch and becomes the "Nature Conductor" — tasked with assembling a Nature Orchestra. The child searches for 3 more natural "performers" (a stick, a leaf, a pebble), photographs each one, and assigns a unique sound to it. At the climax, the AI narrates a concert where each performer plays its solo, then all together in a grand ensemble finale that the child gets to direct.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Birds use songs to communicate; different natural objects can produce different sounds (tapping, rustling, clinking); an orchestra is a group of performers playing together; a conductor directs when performers play
  - **U (Understand)**: Every object has its own unique qualities — its Form tells us what kind of sound or expression it might make; when different things work together, they create something bigger than any one alone — that is Connection
  - **D (Do)**: Assign creative sounds to found objects using onomatopoeia and imagination (Communication — expressing ideas); listen to the AI's concert narration and respond with directing choices (Communication — listening); combine individual sounds into an ensemble performance (Thinking — creative thinking)

- **③ Design Highlight**: The child becomes a "conductor" who gives voice to voiceless things. Each natural object gets a personality through the sound the child assigns — a stick becomes "the drummer," a leaf becomes "the rustler." The magic moment is the full ensemble concert, where every item performs its sound in sequence and then all together, with the child directing volume, speed, and combinations. The Performance pillar shines through audience-style narration: "Ladies and gentlemen, the Nature Orchestra!"

- **④ Typical Scenario**: A child in the park photographs a bird singing on a branch, then hunts for 3 natural "performers" nearby — a stick, a leaf, and a pebble — assigns each a unique sound, and conducts a narrated Nature Orchestra concert.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs a bird singing on a branch in the park with no prior conversation.
>
> **AI says**: "*(delighted, hushed wonder)* Oh! A bird! Listen — it is singing a little song up on that branch. It sounds so beautiful, like a tiny musician! What do you think it is singing about?"
>
> **Possible child responses**:
> 1. (Ideal) "It's singing about the sun!" / "It's happy!"
> 2. (Unexpected) "I don't know." / "It's just chirping."
> 3. (No response) Child watches the bird quietly.
>
> **AI follow-up**:
> 1. "*(warm, inspired)* A song about the sun! What a lovely idea. This bird is like a little performer on a stage. I wonder if we could find MORE performers to join it!"
> 2. "*(playful, validating)* Chirping IS singing! Every chirp is a tiny note. This bird is like a singer on a stage branch. What if it had a whole band to play with?"
> 3. *(wait 2 seconds)* "*(gentle, coaxing)* That bird is singing all by itself up there. It sounds a bit lonely! What if we found it some friends to make music with?"
>
> **Screen**: Bird photo centered on screen with soft green leaf-shaped glow around the branch. Tiny animated musical notes drift upward from the bird, fading gently as they rise.

**Step 2: Mission Briefing — Nature Conductor**

> **AI says**: "*(excited, rallying)* You are now a Nature Conductor! Your mission has three parts. First, find three things in nature that could be performers — like a stick, a leaf, or a rock. Second, take a photo of each one. Third, YOU give each one a special sound. Then we put on a Nature Concert! Ready, Conductor?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Let's find performers!"
> 2. (Unexpected) "What's a conductor?" / "What sounds?"
> 3. (No response) Child looks around, uncertain where to start.
>
> **AI follow-up**:
> 1. "*(pumped up)* Great! A conductor is the boss of the music. YOU tell the performers when to play. Now look around — find a stick, a leaf, or a rock. Take a photo when you spot one!"
> 2. "*(warm, explaining)* A conductor tells musicians when to play — loud, soft, fast, slow! And the sounds? YOU choose! A stick could go TAP TAP, a leaf could go RUSTLE RUSTLE. You decide! Now go find your first performer!"
> 3. *(wait 2 seconds)* "*(encouraging, pointing)* Try looking on the ground near trees. A stick would be a great first performer! Or a leaf, or a little rock. Take a photo of whatever you find!"
>
> **Screen**: A mission card appears with a "Nature Conductor" badge at the top — a small baton with musical notes swirling around it. Five performance slots are shown in a row — the first slot is filled with the bird photo labeled "Lead Singer." Three empty slots glow softly, each marked with a musical note icon. A numbered checklist reads: 1) Find 3 nature performers. 2) Photograph each one. 3) Give each one a sound!

**Step 3: Multi-Round Exploration (3–4 rounds)**

> **Round 1** (full detail):
>
> *(Child takes a photo of a stick on the ground)*
>
> **AI says**: "*(excited discovery)* Ooh, a stick! Great find, Conductor! Now here is the big question — if this stick could make ONE sound, what would it be? Show me! Say the sound!"
>
> **Possible child responses**:
> 1. (Ideal) "TAP TAP TAP!" / "KNOCK KNOCK!" / "BOOM BOOM!"
> 2. (Unexpected) "I don't know what sound." / "Sticks don't make sounds."
> 3. (No response) Child is silent, thinking.
>
> **AI follow-up**:
> 1. "*(thrilled, dramatic)* TAP TAP TAP! I love it! Stick is now the DRUMMER of the Nature Orchestra — TAP TAP TAP! What a beat! Two more performers to find, Conductor!"
> 2. "*(warm, scaffolding)* What if you tapped a stick on the ground? It would go TAP TAP! Or maybe CRACK! You pick the sound you like best. What do you think — TAP or CRACK?"
> 3. *(wait 2 seconds)* "*(playful, modeling)* Hmm, a stick... I think it could go TAP TAP TAP, like a drum! Or maybe CLICK CLICK. Which one do you like? You choose!"
>
> **Screen**: Stick photo slides into the second performance slot with a burst of musical notes. The label below changes to show the child's assigned sound in playful bouncing letters (e.g., "TAP TAP TAP!"). Counter shows "1 of 3 performers found."

> **Round 2** (full detail):
>
> *(Child takes a photo of a leaf on the ground or still on a bush)*
>
> **AI says**: "*(curious excitement)* A leaf! Ooh, leaves are sneaky sound-makers. If this leaf could make ONE sound for the concert, what would it be? Say it loud!"
>
> **Possible child responses**:
> 1. (Ideal) "RUSTLE RUSTLE!" / "CRINKLE CRINKLE!" / "SHHHH!"
> 2. (Unexpected) "Green!" / Child names the color or shape instead of a sound.
> 3. (No response) Child holds the leaf, thinking.
>
> **AI follow-up**:
> 1. "*(delighted, dramatic)* RUSTLE RUSTLE! Yes! Leaf is now the WHISPERER of the Nature Orchestra — RUSTLE RUSTLE RUSTLE! So soft and sneaky. One more performer to find!"
> 2. "*(warm, redirecting)* It IS green! A beautiful green leaf. And green leaves go... RUSTLE RUSTLE when the wind blows! Or maybe CRINKLE CRINKLE if you squish it. Pick a sound for your leaf performer!"
> 3. *(wait 2 seconds)* "*(gentle, encouraging)* Feel that leaf — it is thin and light. What if the wind blew it? It might go RUSTLE RUSTLE. Or SWOOSH! What sound do you want it to make in the concert?"
>
> **Screen**: Leaf photo slides into the third performance slot with a swirling leaf animation. The label below shows the assigned sound in wavy, airy letters (e.g., "RUSTLE RUSTLE!"). Counter shows "2 of 3 performers found."

> **Round 3** (full detail):
>
> *(Child takes a photo of a pebble or small rock)*
>
> **AI says**: "*(thrilled)* A pebble! Perfect — our last performer! If this pebble could make ONE sound in the concert, what would it be?"
>
> **Possible child responses**:
> 1. (Ideal) "CLINK CLINK!" / "CLICK CLICK!" / "BONK!"
> 2. (Unexpected) "It's heavy!" / Child describes the pebble instead of assigning a sound.
> 3. (No response) Child looks at the pebble quietly.
>
> **AI follow-up**:
> 1. "*(awed, celebrating)* CLINK CLINK! Pebble is now the BELL-RINGER of the Nature Orchestra — CLINK CLINK CLINK! Your cast is COMPLETE, Conductor! Time for the big show!"
> 2. "*(warm, building)* A heavy pebble! Heavy things make BIG sounds. Maybe THUD THUD? Or CLINK CLINK, like tiny bells? What sound do you want your pebble to make?"
> 3. *(wait 2 seconds)* "*(playful, modeling)* This pebble looks like it could go CLINK CLINK, like a little bell! Or CLICK CLICK, like a clock. Pick one — you are the conductor!"
>
> **Screen**: Pebble photo slides into the fourth performance slot with a sparkle burst. The label below shows the assigned sound in bold, bouncy letters (e.g., "CLINK CLINK!"). A "Cast Complete!" banner flashes across the screen. All four performer slots now filled: Bird (Lead Singer), Stick (sound), Leaf (sound), Pebble (sound).

> **Round 4 (optional)** (condensed):
>
> If the child is highly engaged and finds a fourth item (e.g., a flower, a pine cone, a seed pod), AI reacts with the same per-find pattern: excited reaction → "What sound would it make?" → child assigns sound → AI gives it a performer name. This is a bonus performer: "A fifth member! The orchestra grows!"

> **Stuck Branch** (if child cannot find a performer):
>
> **AI says**: "*(helpful, conspiratorial)* Nature performers like to hide! Try looking under a tree — sticks love to wait there. Or check near a flower bed for little rocks. Even a fallen leaf on the path would be a great singer!"
>
> **Screen**: A soft pulsing hint arrow appears pointing toward a tree or garden area. The text "Try: sticks under trees, pebbles near paths, leaves on the ground" appears in a small helpful bubble.

**Step 4: Synthesis — The Nature Orchestra Concert (Magic Moment)**

> **AI says**: "*(grand, theatrical announcer voice)* Ladies and gentlemen, boys and girls — welcome to the Nature Orchestra Concert! Your conductor has assembled FOUR amazing performers. Let the show begin!"
>
> *(brief pause)*
>
> "*(dramatic, building)* First up — the Lead Singer, Bird! *TWEET TWEET TWEEEEET!* The crowd goes wild!"
>
> *(brief pause)*
>
> "*(building energy)* Next — the Drummer, Stick! *TAP TAP TAP!* What a beat! The audience is clapping along!"
>
> *(brief pause)*
>
> "*(mysterious, soft)* Now, the Whisperer, Leaf, sneaks in... *RUSTLE RUSTLE RUSTLE...* Ohhh, so soft and beautiful!"
>
> *(brief pause)*
>
> "*(bright, ringing)* And finally — the Bell-Ringer, Pebble! *CLINK CLINK CLINK!* The crowd is cheering!"
>
> *(dramatic pause)*
>
> "*(huge, explosive energy)* And now, Conductor — ALL TOGETHER NOW! Bird sings TWEET TWEET, Stick drums TAP TAP, Leaf whispers RUSTLE RUSTLE, Pebble rings CLINK CLINK — ALL AT ONCE! The audience is ON THEIR FEET! BRAVO! BRAVOOO!"
>
> **Possible child responses**:
> 1. (Ideal) Child cheers, laughs, claps, or shouts "AGAIN!" / "LOUDER!"
> 2. (Unexpected) "That was funny!" / "I want just the stick and pebble!"
> 3. (No response) Child listens with a big smile.
>
> **AI follow-up**:
> 1. "*(thrilled, responding to direction)* The conductor says LOUDER! TWEET TWEET! TAP TAP TAP! RUSTLE RUSTLE! CLINK CLINK CLINK! THE CROWD IS GOING CRAAAZY! Standing ovation! Encore, encore!"
> 2. "*(delighted, following direction)* Just stick and pebble — a duet! TAP TAP... CLINK CLINK... TAP CLINK TAP CLINK! Ohhh, what a cool combo! You are an amazing conductor — you know exactly what sounds good together!"
> 3. *(wait 2 seconds)* "*(warm, celebrating)* I see that smile, Conductor! Your orchestra was AMAZING. The audience is throwing flowers! Should we do it one more time? You say when!"
>
> **Screen**: All four performer photos are displayed in a semicircle stage layout, like an orchestra on stage. As each performer is introduced, its photo glows and its sound text pulses and bounces in rhythm. During "ALL TOGETHER NOW," all four photos glow simultaneously with musical notes, stars, and confetti bursting across the screen. An animated crowd silhouette at the bottom of the screen cheers and waves. A large "BRAVO!" text flashes with golden sparkles.

**Step 5: Discovery Celebration**

> **AI says**: "*(warm, reflective)* Wow, Conductor! You built a whole orchestra from nature. Four performers, four different sounds, one amazing concert. Which performer was your favorite? Who made the best sound?"
>
> **Possible child responses**:
> 1. (Ideal) "The stick because TAP TAP is so cool!" / "The bird because it sings for real!"
> 2. (Unexpected) "All of them!" / "I want to find more!"
> 3. (No response) Child points at one of the photos.
>
> **AI follow-up**:
> 1. "*(impressed, warm)* Great pick! Every performer had its own special sound. That is what makes an orchestra so amazing — everyone is different, but together they make something beautiful!"
> 2. "*(delighted)* ALL of them! That is what a conductor would say — every performer matters! Together they made something none of them could make alone!"
> 3. *(wait 2 seconds)* "*(gentle, affirming)* That one! Great choice. I think it had a really special sound too. Every single performer helped make the concert wonderful!"
>
> **Screen**: Collection photos displayed in the orchestra semicircle layout with a golden star appearing on the child's chosen favorite. Sound-wave lines connect all four performers to a central "Nature Orchestra" emblem. A banner reads: "4 performers, 1 amazing concert!"

**Step 6: Closing + IB Concepts**

> **AI says**: "*(proud, warm celebration)* You are an incredible Nature Conductor! You looked at each thing you found and imagined what sound it could make — you discovered its Form, its own special voice. Then you put them all together and created something beautiful — that is Connection, when different things work as a team. And YOU gave each one a voice — that is Perspective, seeing the world through different eyes and ears. You earned your Nature Conductor badge! Bravo, Conductor!"
>
> **Screen**: "Nature Conductor" badge — a golden baton with four tiny icons orbiting it (a bird, a stick, a leaf, a pebble). "Form," "Connection," and "Perspective" appear in artistic green, gold, and sky-blue lettering with a musical note icon, a chain-link icon, and an ear icon respectively. Four collection photos as small insets arranged around the badge in an orchestra arc. Confetti gently falls across the screen.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change comparison. Multi-photo workflow processes each find independently. Sound assignment uses verbal dialogue (ASR text), not audio detection. AI narrates the sounds — no requirement to detect actual clapping/tapping. |
| 2 | Hook & Transition | PASS | Step 1 opens with emotional wonder ("Oh! A bird! Listen — it is singing a little song"), not knowledge testing. The activity grows naturally from admiring the bird's singing to finding more performers. Removing step labels, it reads as a flowing conversation. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, no response). Stuck branch in Step 3 provides concrete location hints ("under a tree," "near a flower bed," "fallen leaf on the path"). Unexpected responses always validated before redirecting. |
| 4 | IB Completeness | PASS | Form + Connection + Perspective named as Key Concepts. KUD fully specified with concrete vocabulary and skills. 3 ATL skills with sub-skills. Closing naturally names concepts as praise tied to what child did. Concepts earned: Form (each object has unique sound qualities), Connection (ensemble teamwork), Perspective (giving voice to voiceless things). |
| 5 | Tier Appropriateness | PASS | T1: sentences 5–8 words, open-ended questions ("What sound would it make?"), concrete vocabulary (stick, leaf, pebble, tap, rustle, clink), 3-part mission, onomatopoeia encouraged. Manageable task complexity for ages 4–6. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. No abstract instructions like "AI guides the child." All sounds are written out as specific onomatopoeia. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with layout, animations, and visual elements. Stage layout, performer slots, sound text animations, confetti, crowd silhouette — all concretely described. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter specified. |
| 9 | Game Feel | PASS | Genuine uncertainty: what sounds will each object make? Magic moment: the full ensemble playing ALL TOGETHER NOW with crowd going wild. Surprise: child can direct the orchestra (louder, softer, duets). Replayable: different objects produce different orchestras every time. The concert narration creates real drama and delight. |
| 10 | Pillar Fidelity | PASS | Performance pillar delivers "They loved it!" feeling. Audience reaction mechanic throughout (crowd clapping, cheering, standing ovation, "BRAVO!"). Magic moment = audience ovation when all play together. Core loop = assemble cast + assign voices + put on show. Could not be re-labeled to another pillar — the conductor role, audience reactions, and concert format are distinctly Performance. |

**Overall**: ALL PASS — Ready for 教研 review
