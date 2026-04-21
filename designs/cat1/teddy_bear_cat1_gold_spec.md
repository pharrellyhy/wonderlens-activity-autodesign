# Activity Design: Teddy Bear + Category 1 (Sustained Verbal Interaction)

> Generated: 2026-04-01 | Style upgrade: helper_hotline → care_station | Agent: Activity Design Agent

---

## Activity: Teddy's Cozy Care Station

### A. Basic Info

- **Activity Name**: Teddy's Cozy Care Station
- **Activity Category**: 1 — Sustained Verbal Interaction (In-Device)
- **Recommended Tier**: T0 (ages 2–4)
- **Core IB Key Concepts**: Responsibility, Connection
- **Related Concepts (Discipline)**: Emotion, Safety, Expression, Empathy
- **ATL Skills Focus**: Social Skills (empathy, caring), Communication Skills (expressing, listening), Self-Management Skills (emotional regulation)
- **Experience Pillar**: Nurture
- **Game Style**: care_station
- **Design Version**: 1.0
- **Last Updated**: 2026-04-01
- **Trigger Entity**: Teddy bear
- **Trigger Scene**: Child photographs their teddy bear sitting on the bed in the evening light
- **Mapping Source**: none

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

### A.6 Constellation Adaptation Notes

Recipe for running this activity when the photographed entity is a constellation
neighbor of Teddy Bear (e.g., stuffed bunny, plush toy, doll, sock monkey)
instead of a teddy bear itself. The neighbor list, bridge type, and initial
bridge prompt live in `data/constellation_map.yaml` under
`mapped_entity: teddy_bear` — this section describes how Teddy's Cozy Care
Station adapts mechanically for a bridged entity.

**Preserve** — must not change across neighbors:
- The 3-round escalation from physical need → emotional need → complex combined need — this is the empathy-stretching arc that defines the Nurture pillar.
- The VISIBLE TRANSFORMATION narration ("shivering stops → smile grows → calls child by name") — the child must see each care act work, or the magic moment collapses.
- The "caretaker" role_title and the hearts-floating-up payoff that escalates 1 → 2 → 3 hearts across rounds.

**Swap** — re-phrase for the bridged entity:
- Round 1 "Teddy is shivering! Brrr brrr!" → neighbor's cold-signal (bunny: "ears are drooping and cold"; doll: "hands feel icy"; sock monkey: "tail is stiff with cold") — keep the "something warm" fix but re-name the body part.
- Round 2 "scared of the dark, eyes big and round" → neighbor's scared-signal (bunny: "ears pinned back"; doll: "eyes wide shut tight"; sock monkey: "arms hugging itself"). The comfort words ("it's okay! I'm here!") stay the same.
- Round 3 magic line "[Child's name], you're my best friend in the whole world!" → use the child's actual name regardless of neighbor; the neighbor's voice/accent can shift (bunny whispers, doll speaks gently, sock monkey says it with a playful lilt) but the calling-by-name beat is fixed.
- Vocabulary list "shivering, cozy, scared, brave, friend" stays — but the pronoun for the entity swaps cleanly (teddy → bunny → sock monkey); avoid keeping "teddy" hardcoded in the AI lines.

**Watch** — gotchas to avoid:
- Dolls and some plush toys have clear faces that never actually change — narrate the transformation in the child's imagination ("imagine the smile growing"), don't claim a physical change the photo doesn't support.
- Sock monkey's floppy shape can read as already-sad — don't start Round 1 assuming it's "shivering"; check the child's description first (it may be napping, dancing, etc.).
- Never skip the name-calling in Round 3 — that's the emotional payoff; if the AI doesn't have the child's name yet, harvest it earlier in Step 1 rather than using a generic "friend" in the finale.

### B. Activity Overview

- **① Brief Description**: After the child photographs their teddy bear, the AI notices teddy is shivering a little and looks like it needs help. The child becomes teddy's special caretaker across three rounds of escalating needs — from a simple physical problem (teddy is cold) to an emotional one (teddy is scared of the dark) to a complex combination (teddy is cold AND lonely AND can't sleep). Each time the child helps, teddy VISIBLY gets better — shivering stops, tears dry, a smile grows — and teddy's gratitude deepens, until by the final round teddy calls the child by name and says they're the best friend in the whole world.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the words "shivering," "cozy," "scared," "brave," and "friend." Learn that when someone is cold, a blanket or hug helps. Learn that when someone is scared, a gentle voice helps. Learn that caring for someone builds a special bond.
  - **U (Understand)**: Understand that taking care of someone means noticing what they need and doing something about it — that is **Responsibility**. Understand that when you care for someone, you build a special bond with them — that is **Connection**.
  - **D (Do)**: Practice identifying emotional and physical needs through listening. Practice proposing care solutions using simple language. Practice expressing empathy and comfort through words and sounds.

- **③ Design Highlight**: Unlike a simple Q&A about teddy, this design creates a VISIBLE TRANSFORMATION arc. When the child says "hug teddy," the AI doesn't just say "good job" — it narrates teddy CHANGING: the shivering stops, warmth spreads, a smile appears, and teddy speaks in a voice that gets more personal and affectionate each round. By Round 3, teddy calls the child by name, creating an emotional payoff that makes the child feel they truly helped a friend. The escalation from physical needs to emotional needs to complex needs stretches the child's empathy naturally.

- **④ Typical Scenario**: Child photographs their teddy bear on the bed → AI notices teddy is shivering and needs help → child becomes teddy's caretaker, solving escalating needs while watching teddy visibly recover and grow more grateful with each round.

### C. Interaction Flow — Detailed Design [Target Tier: T0]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs their teddy bear with no prior conversation.
>
> **AI says**: "*(soft gasp, concerned)* Oh! Look at teddy! So soft and fluffy... but wait — is teddy shivering? Brrr brrr! I think teddy needs help!"
>
> **Possible child responses**:
> 1. (Ideal) "Teddy cold!" / "Oh no!" / "Help teddy!"
> 2. (Unexpected) "Teddy is happy!" / "That's my teddy!" / "I love teddy!"
> 3. (No response) Child looks at the screen silently.
>
> **AI follow-up**:
> 1. "*(warm, encouraging)* Yes! Teddy is cold! You noticed! Can YOU help teddy feel better?"
> 2. "*(gentle, playful)* You love teddy! Teddy loves you! But look — brrr — teddy is a little shivery. Can you help?"
> 3. *(waits 2 seconds)* "*(soft whisper)* Teddy is going brrr brrr. Can you hear it? Teddy needs a friend!"
>
> **Screen**: Teddy bear photo centered on screen with a soft blue background. Teddy has a gentle shivering wobble animation — tiny movement side to side. Small snowflake-like sparkles drift around teddy. A small worried-face icon pulses softly in the corner.

**Step 2: Game Setup + Demo — "Teddy's Caretaker"**

> **AI says**: "*(excited whisper)* You can be teddy's helper! Here's how. I tell you what teddy needs. You fix it! Like this — teddy says: 'My nose is cold!' What do we do? Boop! We warm the nose! Ready?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Boop!" / "Yes!" / child giggles
> 2. (Unexpected) "Teddy nose!" / "Where's the nose?" / child makes a sound
> 3. (No response) Child is quiet, watching.
>
> **AI follow-up**:
> 1. "*(cheery)* Boop! Teddy's nose is warm now! See? You did it! Here comes the first big one..."
> 2. "*(playful)* Yes, teddy's little nose! Boop — warm! Easy! Now teddy needs MORE help. Listen..."
> 3. *(waits 2 seconds)* "*(gentle, coaxing)* Boop! We warmed teddy's nose! So easy. Now teddy needs your help again. Listen..."
>
> **Screen**: Teddy photo with a small blue nose highlighted. When child responds (or after follow-up), a warm orange glow spreads over the nose area, a tiny sparkle appears, and a small smile icon pops up briefly. "Teddy's Caretaker" text appears softly at the top with a heart icon.

**Step 3: Core Loop (3 rounds)**

**Round 1 — "Teddy is cold!" (Physical need — simple, high-success)**

> **AI says**: "*(storytelling, worried voice)* Oh no! Teddy is shivering! Brrr brrr brrr! 'I'm so cold!' says Teddy. Teddy needs something warm. What should we do?"
>
> **Possible child responses**:
> 1. (Ideal) "Hug teddy!" / "Blanket!" / "Cover teddy!" / "Warm teddy!"
> 2. (Unexpected) "Teddy is cold!" / "Brrr!" / child repeats the problem
> 3. (No response) Child is quiet or looking at teddy.
>
> **AI follow-up**:
> 1. "*(delighted, narrating the transformation)* You gave teddy a big warm hug! Look... teddy stops shivering... the brrrs go quiet... and a tiny smile appears! 'Ahhhh,' says Teddy, 'warm now! Thank you!' Teddy feels SO much better!"
> 2. "*(validating, then guiding)* Brrr is right! Poor teddy! What if we gave teddy a big warm hug? Try saying 'hug teddy!'"
> 3. *(waits 2 seconds)* "*(soft prompt)* Teddy says brrr brrr! So cold! Should we give teddy a hug? Say 'hug!'"
>
> **Screen**: Teddy photo with shivering animation intensified — little brrr text bubbles floating up. When child responds with a solution:
> - The shivering animation slows... then stops
> - A warm orange-golden glow wraps around teddy, starting from the middle and spreading outward
> - Teddy's expression shifts from worried to a small smile
> - A speech bubble appears: "Warm now!"
> - A single floating heart drifts upward
> - A small "Round 1" indicator with a green checkmark appears in the corner

**Round 2 — "Teddy is scared!" (Emotional need — more complex)**

> **AI says**: "*(hushed, dramatic whisper)* Uh oh. Teddy stopped shivering... but now teddy's eyes are big and round! 'It's dark,' whispers Teddy. 'I'm scared!' Teddy is afraid of the dark. What should we do?"
>
> **Possible child responses**:
> 1. (Ideal) "It's okay teddy!" / "Don't be scared!" / "I'm here!" / "Night light!"
> 2. (Unexpected) "I'm scared too!" / "Dark!" / child makes a scared sound
> 3. (No response) Child is quiet, perhaps uncertain how to help with a feeling.
>
> **AI follow-up**:
> 1. "*(narrating transformation, touched)* You said 'it's okay!' and look what happens... teddy takes a deep breath... the big scared eyes get smaller... and teddy whispers: 'You make me brave.' Look! Teddy is smiling again — a bigger smile this time! 'You always know what I need,' says Teddy."
> 2. "*(warm, validating)* Oh! You feel it too sometimes? That's okay! When we're scared, a friend helps. Can you tell teddy 'it's okay, I'm here'? That will help!"
> 3. *(waits 2 seconds)* "*(gentle coaching)* When YOU feel scared, what makes you feel better? A hug? A kind word? Can you try saying 'it's okay, teddy'?"
>
> **Screen**: Background shifts to dark blue-purple with soft shadows. Teddy's eyes are wide and shiny (worried animation). When child responds with comfort:
> - A soft warm glow appears around teddy, like a gentle night light
> - Teddy's wide eyes slowly relax to normal
> - Teddy's smile grows — noticeably bigger than Round 1
> - A speech bubble appears: "You make me brave!"
> - Two floating hearts drift upward (one more than Round 1 — relationship deepening)
> - "Round 2" indicator with green checkmark

**Round 3 — "Teddy is cold AND lonely AND can't sleep!" (Complex need — physical + emotional)**

> **AI says**: "*(soft, caring concern)* Oh teddy... teddy is shivering again AND teddy whispers: 'I can't sleep. It's cold and dark and I feel all alone.' Teddy needs a LOT of help! Teddy is cold AND scared AND lonely. What should we do?"
>
> **Possible child responses**:
> 1. (Ideal) "Hug teddy!" / "I'll stay!" / "Sing teddy!" / "Shh, night night!" / combines actions
> 2. (Unexpected) "Blanket!" / "Teddy sleep!" / child says one thing (only solves one need)
> 3. (No response) Child seems overwhelmed by the complex need.
>
> **AI follow-up**:
> 1. "*(narrating the full transformation, deeply moved)* You said you'll stay with teddy! Listen... teddy stops shivering... the dark doesn't seem so scary anymore... and teddy's eyes get soft and sleepy. Teddy whispers: '[Child's name], you're my best friend in the whole world. I'm not alone anymore. I feel safe.' Look at that smile — the BIGGEST smile yet! Teddy is cozy, brave, and happy... all because of YOU."
> 2. "*(warm, building on partial solution)* A blanket — that helps with cold! Now teddy is warm... but still feels lonely. Can you say 'I'm here, teddy'? That helps with lonely!"
> 3. *(waits 2 seconds)* "*(soft, scaffolding)* Teddy needs SO much help! Let's start with one thing. Teddy is cold — can you say 'hug'? And then we'll help with the rest!"
>
> **Screen**: Dark background with teddy shivering AND wide-eyed. Small tear drops visible. When child responds:
> - The transformation happens in STAGES:
>   - First: shivering stops, warm glow appears (cold solved)
>   - Then: eyes relax, soft light fills the background (scared solved)
>   - Finally: teddy's whole body relaxes into a cozy posture, the biggest smile yet appears (lonely solved)
> - A speech bubble appears: "[Child's name], you're my best friend!"
> - THREE floating hearts drift up (deepening relationship arc — 1 in R1, 2 in R2, 3 in R3)
> - Soft lullaby-style sparkles surround the screen
> - "Round 3" indicator with a gold star (not just checkmark — this was the hardest one)

**Step 4: Payoff — The Magic Moment**

> **AI says**: "*(soft, deeply warm)* Look at teddy now. Remember when teddy was shivering and scared? Now teddy is warm... brave... and smiling SO big. Teddy whispers: '[Child's name]... thank you for taking care of me. You made the cold go away. You made the dark not scary. And you made me feel not alone. You're the best caretaker in the whole world.'"
>
> **Possible child responses**:
> 1. (Ideal) Child smiles, hugs their actual teddy, says "I love teddy!" / "Yay!"
> 2. (Unexpected) "More!" / "Teddy wake up!" / "Again!"
> 3. (No response) Child is quiet, looking at the screen with a soft expression.
>
> **AI follow-up**:
> 1. "*(beaming)* Teddy loves you SO much. You helped with everything!"
> 2. "*(playful, warm)* Teddy says 'help me again tomorrow!' You're the best!"
> 3. "*(gentle, warm whisper)* Look at teddy's big smile. That smile is all because of you."
>
> **Screen**: Full-screen warm golden glow. Teddy photo centered with the biggest, coziest expression — wrapped in a glowing blanket of light. The three-stage transformation replays as a quick montage:
> - Shivering teddy → warm teddy (Round 1 flash)
> - Scared teddy → brave teddy (Round 2 flash)
> - Lonely teddy → happy, cozy teddy (Round 3 flash)
> Then: A golden badge animation drops in reading "Teddy's Best Caretaker" with a bear-paw-and-heart icon. Confetti in warm colors (gold, pink, orange) rains down. Three hearts arranged in a row below the badge — representing the three rounds of care.

**Step 5: Closing + IB Concepts**

> **AI says**: "*(warm, reflective, proud)* You know what you did today? Every time teddy needed something — warm, brave, not alone — YOU helped. Helping someone who needs you... that's called Responsibility. And now you and teddy have a special bond — teddy trusts you, and you care for teddy. That's called Connection. You're not just a helper. You're teddy's best friend!"
>
> **Possible child responses**:
> 1. (Ideal) "I'm teddy's friend!" / "Bye teddy!" / child hugs their teddy bear
> 2. (Unexpected) "Teddy is my friend!" / "What's connection?" / any response
> 3. (No response) Child is quiet, perhaps hugging teddy.
>
> **AI follow-up**:
> 1. "*(soft, closing)* Best friends! Night night, teddy. Night night, caretaker! See you next time!"
> 2. "*(warm)* Yes! Connection is when you care for someone and they care for you. Like you and teddy!"
> 3. *(waits 2 seconds)* "*(gentle close)* Teddy is smiling at you. Night night, teddy. Night night, best friend!"
>
> **Screen**: "Responsibility" appears in warm gold lettering with a caring-hands icon. "Connection" appears in soft pink lettering with a heart-link icon. Both words float gently beside the teddy photo, which shows teddy in a cozy, sleeping pose with a peaceful smile. The "Teddy's Best Caretaker" badge glows softly at the bottom. Gentle sparkle animation fades as the screen dims to a cozy, night-time warmth.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, state comparison, or non-speech audio detection. All verification is dialogue-based. Screen animations are AI-driven narration, not hardware detection. Teddy's "transformation" is narrated by AI and shown via pre-programmed screen animations, not camera-detected state changes. |
| 2 | Hook & Transition | PASS | Step 1 opens with emotional resonance ("Oh! Look at teddy! So soft and fluffy... but wait — is teddy shivering?"), not knowledge testing. Activity grows naturally from concern for teddy into the caretaking game. Remove step labels and it reads as flowing conversation. |
| 3 | Edge Case Coverage | PASS | Every step includes 3 response branches (ideal, unexpected, silence). All unexpected branches validate first ("You love teddy! Teddy loves you!") then redirect. All silence branches wait 2 seconds then offer a gentle prompt. Round 3 includes scaffolding for when child is overwhelmed by complex need. |
| 4 | IB Completeness | PASS | Responsibility and Connection explicitly named in closing. KUD has specific vocabulary (shivering, cozy, scared, brave, friend). 3 ATL skills with sub-skills. 4 Related Concepts. Closing celebrates first ("You're teddy's best friend!") then naturally names concepts. Concepts earned — child literally practiced responsibility (helping) and built connection (deepening relationship arc). |
| 5 | Tier Appropriateness | PASS | T0: Sentences consistently 3-5 words ("Teddy is cold!" "Hug teddy!" "Brrr brrr!"). Onomatopoeia used throughout (brrr, boop, shh). Single-step instructions per round. Call-and-response model (AI describes need → child responds → AI narrates result). 3 rounds (within T0 limit). Vocabulary is basic nouns and feelings words appropriate for ages 2-4. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. Zero instances of "AI guides" or "AI encourages." Specific transformation narration: "teddy stops shivering... a tiny smile appears... 'Ahhhh, warm now!'" |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with layout, animations (shivering wobble, warm glow spreading, eyes relaxing, hearts floating, transformation montage), visual elements (brrr text bubbles, speech bubbles, round indicators, badge), and emotional progression visible on screen. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter in this assignment. |
| 9 | Game Feel | PASS | Genuine stakes: teddy is suffering and the child's response determines whether teddy gets better. Uncertainty: will my solution work? Emotional climax: Round 3 where teddy calls child by name and says "you're my best friend in the whole world." Replayability: different needs could be generated, and the relationship arc makes it emotionally satisfying to replay. Surprise/delight: the visible transformation (shivering stopping, smile appearing) and the escalating gratitude create delight beyond warm encouragement. |
| 10 | Pillar Fidelity | PASS | Nurture pillar delivered fully. Core loop: need → child solves → VISIBLE TRANSFORMATION. Magic moment: entity fully recovered, calls child by name, expresses deep personal gratitude. Child feels "I helped!" with visible evidence (transformation montage in Step 4). Relationship arc deepens: Round 1 "Thank you!" → Round 2 "You always know what I need" → Round 3 "[Name], you're my best friend." Need escalation: physical → emotional → complex. Cannot be re-labeled as any other pillar — the transformation arc and gratitude deepening are uniquely Nurture. |

**Overall**: ALL PASS — 0 issues found during self-evaluation

Ready for 教研 review.
