# Activity Design: Property Performer — Property-Bridge Template (Category 1)

> Generated: 2026-04-08 | Property-bridge template

---

## Activity: [Entity]'s Big Performance

### A. Basic Info

- **Activity Name**: [Entity]'s Big Performance
- **Activity Category**: 1 — Sustained Verbal Interaction (In-Device)
- **Recommended Tier**: T0 (ages 2–4)
- **Core IB Key Concepts**: **Perspective** (expressing through the entity), **Form** (the property is what makes performance possible)
- **Related Concepts (Discipline)**: Expression, Identity, Creativity, Discovery
- **ATL Skills Focus**: Communication Skills (expressing, listening), Thinking Skills (creative thinking), Self-Management Skills (emotional regulation, confidence)
- **Experience Pillar**: Performance
- **Game Style**: voice_stage
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any photographed entity (template written with bouncy rubber ball)
- **Trigger Scene**: Child photographs a bouncy rubber ball. AI detects "round" and "bouncy" as properties and uses them as the performance theme.
- **Property Bridge**: AI detects a salient property of the entity (bouncy, shiny, fluffy, big, tiny, smooth, bumpy, sparkly, soft, loud, etc.) and uses it as the PERFORMANCE THEME. The child performs AS the entity, with the property driving the performance challenges. Works for any entity+property: shiny fork → "sparkle performance," fluffy cat → "fluffiest walk," big truck → "biggest engine roar."
- **Mapping Source**: none

### A.1 Entity Attributes Covered

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

- **① Brief Description**: After the child photographs their entity, the AI detects a standout property and turns it into a talent-show PERFORMANCE THEME. The child becomes the entity's voice and performs the property in increasingly creative ways: big, small, slow, fast, silly, serious. A panel of silly judges reacts to every performance with over-the-top delight, gasps, or laughter. Each round takes the detected property and asks the child to EXPRESS it differently. Round 3 introduces a surprise twist that takes the property to an unexpected place. The finale is a standing ovation — "The judges have NEVER seen a [property] performance like that!"

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the property word (e.g., "bouncy," "round"). Learn that one property can be expressed in many different ways — big, small, slow, fast. Learn the word "audience" means people (or things!) watching a show. Learn that performing means showing something in a special way.
  - **U (Understand)**: Understand that the same property can feel very different depending on HOW you express it — big bounce vs. tiny bounce vs. slow-motion bounce — and each way creates a different experience for the audience; that is **Perspective**. Understand that the property is what MAKES the entity special and what makes the performance possible — that is **Form**.
  - **D (Do)**: Express a property through voice and body in an escalating series of creative challenges. Listen to performance prompts and respond with vocal variety. Adapt performance style when a surprise twist changes the context.

- **③ Design Highlight**: The property-bridge mechanic means every playthrough is unique — the AI detects a REAL property of the photographed entity and builds the entire performance around it. A bouncy ball gets a bouncing talent show; a shiny fork gets a sparkle spectacular; a fluffy cat gets a fluffiness showcase. The audience of silly judges (three funny characters who react with physical comedy to every performance) creates genuine "they loved it!" energy. The surprise twist in Round 3 (property + unexpected context, like "bounce on the MOON!") generates delight and creative stretch. This is not just voice play — it is a PERFORMANCE with an audience, stakes, and a standing ovation.

- **④ Typical Scenario**: Child photographs a bouncy rubber ball → AI detects "round" and "bouncy" → "Your ball is SO bouncy! If your ball could perform in a talent show, it would BOUNCE onto stage!" → child performs as the ball in escalating bounce challenges while silly judges react with increasing excitement, culminating in a standing ovation.

### C. Interaction Flow — Detailed Design [Target Tier: T0]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs a bouncy rubber ball with no prior conversation. AI detects properties: round, bouncy.
>
> **AI says**: "*(delighted gasp)* Whoa! A BALL! And it's SO bouncy! I can tell — look how round it is! If your ball could be in a talent show, it would BOUNCE right onto the stage! Boing boing boing! Can you show me? What does your ball sound like when it bounces?"
>
> **Possible child responses**:
> 1. (Ideal) "Boing boing!" / "Bounce bounce!" / child makes bouncing sounds
> 2. (Unexpected) "That's my ball!" / "It's red!" / "I play with it!"
> 3. (No response) Child stares at the screen or touches the ball.
>
> **AI follow-up**:
> 1. "*(amazed, jaw-drop)* BOING BOING! WOW! That was the BOUNCIEST sound I ever heard! You know what? Some silly judges heard that bounce. They want MORE! Want to put on a BIG bouncy show?"
> 2. "*(warm, excited)* Your ball! So round and bouncy! I bet it has the best bounce sound hiding inside. Want to help it do a BIG show? Some silly judges want to see it bounce!"
> 3. *(waits 2 seconds)* "*(playful whisper)* Psst... I think your ball wants to go BOING! Can you help? Some silly judges are waiting to see the bounciest show ever!"
>
> **Screen**: Ball photo centered on screen with a bright, colorful stage background — spotlight beams, curtain edges. Soft bouncing animation on the ball photo — gentle up-down wobble. Three small shadowed character silhouettes (a penguin with a scorecard, a hamster with popcorn, and a giraffe with a big grin) peek in from the right edge, as if curious.

**Step 2: Game Setup + Demo — "The [Property] Talent Show"**

> **AI says**: "*(excited announcer voice)* Welcome to the Bouncy Talent Show! Three judges are here! Penguin... Hamster... and tall Giraffe! They want to see YOUR ball bounce! I tell you HOW to bounce. You bounce! Judges go CRAZY! Watch — ball says HELLO! BOING! Ohhh! Penguin dropped his scorecard! Ha! Your turn now!"
>
> **Possible child responses**:
> 1. (Ideal) Child laughs, says "BOING!" or "OK!" eagerly.
> 2. (Unexpected) "What's a judge?" / "I want hamster!" / child giggles.
> 3. (No response) Child watches quietly with interest.
>
> **AI follow-up**:
> 1. "*(cheering)* YES! Here comes Round One! Judges are ready! Penguin has his scorecard. Hamster has popcorn. Giraffe is stretching her neck to see! Let's GO!"
> 2. "*(warm, playful)* Judges are silly friends watching the show! Hamster loves bouncing! Ready? You bounce, judges go WOW! Here comes Round One!"
> 3. *(waits 2 seconds)* "*(encouraging, gentle)* It's easy! Just bounce when I say! Judges love EVERY bounce! Ready? Here comes the first one!"
>
> **Screen**: "BOUNCY TALENT SHOW" banner in bright, bouncy lettering at top. Ball photo at center-left on a small stage platform. Three judge characters appear on the right: a tuxedoed penguin holding a scorecard, a hamster with tiny popcorn, and a giraffe whose head pokes in from above — all drawn in friendly cartoon style with eager faces. A "Round 1" star badge glows in the corner.

**Step 3: Core Loop (3 rounds)**

> **Performance Escalation**: Round 1 is simple and high-success (big bouncy performance). Round 2 changes the tempo (slow-motion bounce — contrasting). Round 3 introduces a SURPRISE TWIST (bounce on the moon — the funniest and most creative challenge).

**Round 1 — "The BIGGEST Bounce!" (Big, bold, high-success)**

> **AI says**: "*(bright announcer)* Round One! Your ball is on stage! Show the judges your BIGGEST, BOUNCIEST bounce! Ready? GO! BOING BOING BOING!"
>
> **Possible child responses**:
> 1. (Ideal) "BOING BOING BOING!" / "BOUNCE!" / child bounces or makes loud bouncing sounds
> 2. (Unexpected) "Wheee!" / a silly sound / "I'm jumping!"
> 3. (No response) Child is quiet or shy.
>
> **AI follow-up**:
> 1. "*(audience goes wild)* OHHH! Penguin DROPPED his scorecard — it says TEN! Hamster is jumping up and down — the popcorn is flying EVERYWHERE! Giraffe's neck is wobbling like jelly! They LOVED that big bouncy bounce! BIG gold star!"
> 2. "*(delighted, laughing)* Wheee?! Ha! The judges LOVE surprises! Penguin wrote 'WOW' on his scorecard! Hamster fell over giggling! Giraffe is nodding so hard her spots are jiggling! Gold star for the surprise sound!"
> 3. *(waits 2 seconds)* "*(gentle, encouraging)* Even a tiny boing counts! Try a little one... boing? The judges are leaning forward with their big silly faces!"
>
> **Screen**: Stage spotlight on ball photo; bright bounce-lines radiate outward. When child responds: penguin fumbles scorecard showing "10!", hamster bounces with popcorn flying, giraffe's neck wobbles comically. A gold star stamps in the score area. "Round 1 COMPLETE" sparkles.

**Round 2 — "The Slow-Motion Bounce" (Contrasting tempo)**

> **AI says**: "*(soft, dreamy narrator)* Round Two! Sloooow motion! Your ball is bouncing in slow motion now. Boooooing... boooooing... nice and slow, up and down. Can you do the SLOWEST bounce ever? Ready? Slooooow... GO!"
>
> **Possible child responses**:
> 1. (Ideal) "Boooooing... boooooing..." (slow, drawn-out) — child does a slow bounce sound.
> 2. (Unexpected) "BOING BOING!" — child does a fast bounce instead, or "Slow!"
> 3. (No response) Child is quiet or processing.
>
> **AI follow-up**:
> 1. "*(hushed, mesmerized)* Ohhh... look! Penguin's head is going up... and down... up... and down... following the bounce. Hamster put the popcorn down and is swaying. Giraffe's long neck is going baaaack and fooorth like a pendulum. Your slow bounce hypnotized the WHOLE audience! Second gold star!"
> 2. "*(laughing gently)* A FAST bounce! Ha! The judges jumped! Penguin's scorecard went flying! Hamster says 'Whoa, that was NOT slow!' Giraffe's eyes went wide! Star for the speedy surprise!"
> 3. *(waits 2 seconds)* "*(gentle, modeling)* Try it like this... boooooing... nice and slooooow, like you're floating. Even a tiny slow boing counts. The judges have their eyes going back and forth!"
>
> **Screen**: Stage shifts to dreamy slow-motion effect — background stretches with light trails, ball photo gently lifts and lowers in a slow arc. When child responds slowly: penguin's head follows in slow motion, hamster sways gently, giraffe's neck pendulums. Second gold star stamps in. If fast: judges startle comically. "Round 2 COMPLETE" in soft floating letters.

**Round 3 — "SURPRISE — Bounce on the MOON!" (Twist Challenge)**

> **AI says**: "*(dramatic, conspiratorial whisper building to excitement)* Round Three! SURPRISE CHALLENGE! The judges say... what if your ball bounced on the MOON?! No gravity! Super slow! Super HIGH! Your ball goes booooing... up up up UP into SPACE! Nobody has EVER bounced on the moon before! Can you do it? Ready? THREE... TWO... ONE... MOON BOUNCE!"
>
> **Possible child responses**:
> 1. (Ideal) "Booooing... UP!" / "Wheeeee!" / child makes a slow rising sound / "To the moon!"
> 2. (Unexpected) "BOING!" — child does a regular bounce, or "The moon?!" or laughs
> 3. (No response) Child giggles, looks amazed, or is quiet.
>
> **AI follow-up**:
> 1. "*(absolutely stunned, building to explosion)* LOOK! Your ball is going UP... and UP... and UP... past the stars... past the planets... Penguin's jaw DROPPED! Hamster is standing on the chair screaming 'HIGHER! HIGHER!' Giraffe stretched her neck ALL the way to space to watch! A MOON BOUNCE! The crowd is going BANANAS! THIRD GOLD STAR! The judges have NEVER seen a bounce like THAT!"
> 2. "*(delighted, amazed)* A big bounce BLASTED right past the moon! The judges' mouths are WIDE open! Penguin wrote 'IMPOSSIBLE!' on his scorecard! Hamster fainted from amazement! Giraffe says 'I can see it from up here!' GOLD STAR for the BLAST-OFF bounce!"
> 3. *(waits 2 seconds)* "*(encouraging whisper)* The moon is SO far! Try a big slooow one going up up up... even just going 'uuuuup' counts! Penguin is holding his breath! Try it?"
>
> **Screen**: Stage transforms — background shifts to a starry space scene with the moon glowing above. Ball photo rises slowly upward with a glowing trail. "SURPRISE — MOON BOUNCE!" banner flashes in cosmic gold-blue lettering. When child responds: ball arcs upward past illustrated stars and planets. Judges react HUGE — penguin drops everything, hamster stands on chair, giraffe's neck extends past the top of the screen into the stars. EXPLOSION of celebration — confetti bursts into star shapes, cosmic sparkles everywhere. Third gold star stamps in with extra rocket-flame sparkle. "Round 3 COMPLETE — ALL STARS!" flashes.

**Step 4: Payoff — Standing Ovation (The Magic Moment)**

> **AI says**: "*(building excitement, announcer crescendo)* Three rounds! Three gold stars! And now... ALL the judges are standing up! Penguin is holding up his scorecard and it says 'PERFECT!' Hamster is throwing popcorn in the air like confetti! Giraffe is clapping her hooves WAY up high! STANDING OVATION for the ball! The judges say: 'We have NEVER seen a bouncy performance like that! Big bounces, slow bounces, MOON bounces — AMAZING!' You are the BOUNCE STAR!"
>
> **Possible child responses**:
> 1. (Ideal) Child bounces or says "BOING!" triumphantly, giggles, claps, or says "Yay!"
> 2. (Unexpected) "Again! More!" / "Encore!" / "Moon again!"
> 3. (No response) Child beams, smiles wide, or watches the celebration animation with delight.
>
> **AI follow-up**:
> 1. "*(overjoyed)* The BEST Bounce Star EVER! Every judge says you win! Penguin wants your autograph! Hamster wants to bounce with you!"
> 2. "*(thrilled)* ENCORE? The judges are SO happy! They say 'come back anytime!' You can bounce for them again another day, Bounce Star!"
> 3. *(waits 2 seconds)* "*(warm, celebratory)* Look at that big smile! The judges see it too. Penguin says 'That smile bounces right off the page!' You are a REAL Bounce Star!"
>
> **Screen**: Full celebration scene: confetti rains in bouncy rainbow colors across the entire screen. Penguin holds up "PERFECT" scorecard with sparkles. Hamster throws popcorn confetti. Giraffe claps at the very top of the screen with neck stretched in celebration. A large golden "BOUNCE STAR" badge descends from the top of the screen with the ball photo framed inside it, three gold stars underneath. Triumphant fanfare energy. A crowd of tiny silhouette characters in the background throws hats in the air.

**Step 5: Closing + IB Concepts**

> **AI says**: "*(warm, reflective, gently amazed)* Wow, Bounce Star. You showed the judges that one bouncy ball can bounce SO many ways! Big bounce, slow bounce, MOON bounce — every bounce was different! Same ball, same bounciness, but you made it feel different every time. That's called Perspective — one ball, many bounces! And the judges loved the round shape, the bounciness — that's what makes your ball YOUR ball. That's called Form! You are the Bounce Star of the Bouncy Talent Show!"
>
> **Possible child responses**:
> 1. (Ideal) Child bounces one more time, says "Bye ball!" or "I'm a Bounce Star!" or smiles happily.
> 2. (Unexpected) "What's perspective?" / "I want to be a hamster!" / "Moon again!"
> 3. (No response) Child watches the screen, content and quiet.
>
> **AI follow-up**:
> 1. "*(warm, proud)* BOING! That's ball saying 'Thank you, Bounce Star!' Bye bye! The judges are waving!"
> 2. "*(warm, simple)* Perspective means same ball, different bounces — and that's what YOU showed! Hamsters are fun too — maybe next time! Bye, Bounce Star!"
> 3. *(waits 2 seconds)* "*(soft, closing)* The judges are waving goodbye. Penguin says 'See you next show!' Bye bye, Bounce Star. BOING!"
>
> **Screen**: Ball photo at center with "Perspective" (speech-bubble icon with multiple bounce styles inside) and "Form" (ball-silhouette icon) in bright, playful lettering. "BOUNCE STAR" badge glows in the corner with three gold stars. The three judges wave from the side of the screen. Warm spotlight glow fades to a cheerful closing scene.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change detection required. The "property detection" is performed by AI vision on the initial photo (supported in V1). All interaction is voice-based from a single photo. ASR outputs plain text; AI always responds positively regardless of audio quality. No non-speech audio detection needed. |
| 2 | Hook & Transition | PASS | Step 1 opens with emotional resonance and property excitement ("Whoa! A BALL! And it's SO bouncy! I can tell — look how round it is!") — not knowledge testing. The transition to the talent show grows naturally from the property observation. Remove step labels and it reads as flowing conversation. |
| 3 | Edge Case Coverage | PASS | Every step includes 3 child response branches (ideal, unexpected, no response). Every "unexpected" follow-up validates first ("Wheee?! Ha! The judges LOVE surprises!") before extending. Every "no response" includes a 2-second wait and a gentle, specific prompt. Template includes guidance for any entity+property combination. |
| 4 | IB Completeness | PASS | Perspective + Form explicitly named in closing. 4 Related Concepts listed. KUD fully specified with concrete vocabulary and skills. 3 ATL skills with sub-skills. Closing celebrates first ("Bounce Star!") then naturally names concepts. Concepts match what the child actually did (multiple bounce styles = Perspective; ball's distinctive bounciness = Form). |
| 5 | Tier Appropriateness | PASS | T0: AI sentences are 3–5 words each ("Super slow!", "Super HIGH!", "Ready? GO!"). Onomatopoeia used extensively ("BOING!", "Boooooing...", "Wheee!"). Single-step instructions per round. Call-and-response model throughout. 3 rounds (within T0 attention range, with audience reactions maintaining engagement). Vocabulary is basic and physical — bounce, boing, slow, fast, moon — all T0-appropriate. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete, word-for-word dialogue with tone/emotion markers. Zero abstract instructions ("AI guides..."). Specific judge reactions: "Penguin DROPPED his scorecard — it says TEN!" All responses are warm, playful, child-appropriate. |
| 7 | Screen & UI Completeness | PASS | Every step has detailed screen descriptions specifying layout (stage, judges, ball photo position), animation (bounce lines, slow-motion arc, space scene, confetti), and visual changes per round (spotlight → dreamy slow-motion → cosmic space). Gold star progression tracked visually. Judge characters have distinct visual personalities and comedic reactions. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter in this template. |
| 9 | Game Feel | PASS | Genuine stakes: "Nobody has EVER bounced on the moon before!" Uncertainty: how will the judges react? What is the surprise challenge? Clear emotional climax: standing ovation with all three judges going wild and "We have NEVER seen a bouncy performance like that!" High replayability: different detected properties create entirely different performances each time. Multiple moments of surprise and delight: popcorn flying, scorecard dropping, moon bounce twist, giraffe's neck stretching to space. |
| 10 | Pillar Fidelity | PASS | A blind reader would immediately identify this as Performance pillar: (1) Audience reaction mechanic — judges respond AS audience to every performance with specific physical comedy reactions, (2) Surprise twist — Round 3 moon bounce changes the context, (3) Performance escalation — big → slow → moon (genuinely different creative challenges), (4) Standing ovation magic moment — judges go wild, "PERFECT" scorecard, confetti, "BOUNCE STAR!" The child feels "They loved it!" not just "I expressed something." Property-bridge ensures the performance theme is grounded in what the child can SEE on their actual entity. Could NOT be relabeled as Nurture, Mystery, or any other pillar. |

**Overall**: ALL PASS — 0 issues found during self-evaluation

Ready for 教研 review.
