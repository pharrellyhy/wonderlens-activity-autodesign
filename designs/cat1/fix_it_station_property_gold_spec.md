# Activity Design: Fix-It Station — Property-Bridge Template (Category 1)

> Generated: 2026-04-08 | Property-bridge template

---

## Activity: [Entity]'s Fix-It Station

### A. Basic Info

- **Activity Name**: [Entity]'s Fix-It Station
- **Activity Category**: 1 — Sustained Verbal Interaction (In-Device)
- **Recommended Tier**: T1 (ages 4–6)
- **Core IB Key Concepts**: **Responsibility** (taking care), **Connection** (deepening relationship)
- **Related Concepts (Discipline)**: Emotion, Empathy, Causation, Change
- **ATL Skills Focus**: Social Skills (empathy, caring), Communication Skills (expressing, proposing solutions), Thinking Skills (problem-solving, creative thinking)
- **Experience Pillar**: Nurture
- **Game Style**: care_station
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any photographed entity (template written with worn stuffed animal)
- **Trigger Scene**: Child photographs a stuffed animal that looks a bit worn — faded color, a loose thread, a bit dusty. AI detects a "needs care" property and frames the child as a caretaker.
- **Property Bridge**: AI detects a worn/needs-care property (faded, dusty, scratched, torn, old-looking, droopy, sad-looking) on the entity. This property SEEDS the first need in the care station. If the entity does NOT look worn, AI playfully imagines a need: "Your shiny new robot looks great... but wait — I think it's feeling a little LONELY! Can you help?"
- **Mapping Source**: none

### B. Activity Overview

- **① Brief Description**: After the child photographs their entity, the AI detects a property that suggests the entity needs care (e.g., faded color, loose thread, dusty surface). The AI frames the child as a special fix-it caretaker. The detected property seeds the FIRST need, then needs escalate across three rounds: physical → emotional → complex (all three at once). Each time the child proposes a fix, the entity VISIBLY transforms — color brightens, threads mend, smiles appear — and the entity's gratitude deepens, until by the final round the entity calls the child by name and expresses deep personal trust. The magic moment is the visible transformation: you can SEE your help working.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the words "faded," "worn," "mend," "rest," and "care." Learn that when something looks worn, it might need attention. Learn that care involves noticing, proposing, and acting. Learn that both physical AND emotional needs exist.
  - **U (Understand)**: Understand that noticing what someone needs and doing something about it is **Responsibility**. Understand that when you care for someone over time, the bond between you deepens — that is **Connection**.
  - **D (Do)**: Practice observing specific properties and linking them to needs. Practice proposing creative solutions to escalating problems. Practice expressing empathy through words and actions.

- **③ Design Highlight**: The property-bridge mechanic makes every playthrough unique — the AI detects a REAL property of the photographed entity and uses it to seed the first need. A faded stuffed animal gets color care; a dusty toy gets a cleaning adventure; a scratched truck gets bodywork. This grounds the game in what the child can actually SEE. The escalation from physical needs (fix the fading) to emotional needs (the entity is tired) to complex needs (all three at once!) stretches the child's problem-solving and empathy naturally. The visible transformation — you can SEE the color returning, the smile growing — creates the "I helped!" payoff that defines the Nurture pillar.

- **④ Typical Scenario**: Child photographs a worn stuffed animal → AI detects faded color and a loose thread → "Oh! Your friend looks like they've had LOTS of adventures — but I think they might need a little help. See how the color looks a bit faded? I think they need some care!" → child becomes the fix-it caretaker, solving escalating needs while watching the entity visibly recover and grow more grateful with each round.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs a worn stuffed animal with no prior conversation. AI detects properties: faded color, loose thread, a bit dusty.
>
> **AI says**: "*(soft gasp, noticing)* Oh! Look at your friend! They look like they've had SO many adventures — I can tell! See how the color looks a little faded here? And is that a tiny loose thread? I think your friend might need some help. They've been SO brave... but even brave adventurers need a fix-it station!"
>
> **Possible child responses**:
> 1. (Ideal) "Oh no!" / "My bunny needs help!" / "I can fix it!"
> 2. (Unexpected) "That's my favorite!" / "It's not broken!" / "I love it!"
> 3. (No response) Child looks at the screen silently.
>
> **AI follow-up**:
> 1. "*(warm, encouraging)* Yes! You can see it too! You have such good eyes. I bet YOU could be the perfect fix-it helper. Want to try?"
> 2. "*(gentle, validating)* Of COURSE you love them — and they love you! That's why all the color is a little faded — from all the hugs! But even the most loved friends need a little care sometimes. Want to help?"
> 3. *(waits 3 seconds)* "*(soft, inviting)* See how the color is a little lighter here? That means your friend has been loved A LOT. But they could use a little help. Can you be their fix-it helper?"
>
> **Screen**: Entity photo centered on screen with a warm workshop-style background — soft wooden bench illustration, tiny tools (paintbrush, needle, cloth) arranged around the edges. A gentle pulsing highlight circles the detected property (faded area) on the entity photo. A small heart-shaped "needs help" indicator glows softly in the corner.

**Step 2: Game Setup + Demo — "[Entity]'s Fix-It Station"**

> **AI says**: "*(excited, warm)* Welcome to the Fix-It Station! Here's how it works. I tell you what your friend needs. You tell me how to fix it! Like this — see this faded spot? Your friend says: 'My color is fading!' What should we do? Paint it! Swoosh! The color comes back! See? Easy! Ready for the real thing?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "I can fix it!" / "Let's go!"
> 2. (Unexpected) "What color?" / "I want to paint!" / child makes a sound
> 3. (No response) Child is quiet, watching.
>
> **AI follow-up**:
> 1. "*(cheery)* Swoosh! Look at that — color is already brighter! You're a natural! Now here comes the FIRST big fix..."
> 2. "*(playful)* Great question! Whatever color YOUR friend wants to be! Swoosh — beautiful! Now let's do the real fixing. Listen..."
> 3. *(waits 3 seconds)* "*(gentle, coaxing)* Swoosh! We painted it! So easy. Your friend already looks a little happier. Now they need MORE help. Listen..."
>
> **Screen**: Entity photo with a small faded area highlighted. When child responds (or after follow-up), a colorful paint-swoosh animation washes over the spot, brightening it. A tiny sparkle appears and a small smile icon pops up briefly. "[Entity]'s Fix-It Station" text appears at the top with a wrench-and-heart icon.

**Step 3: Core Loop (3 rounds)**

**Round 1 — "The color is fading!" (Physical need — property-seeded, high-success)**

> **AI says**: "*(storytelling, concerned voice)* Okay, fix-it helper — look closely! Your friend's color is fading. See? It used to be SO bright, but now it's getting pale. 'I used to be so colorful,' your friend says sadly. 'Can you bring my color back?' What should we do to fix the fading?"
>
> **Possible child responses**:
> 1. (Ideal) "Paint it!" / "Color it!" / "Use crayons!" / "Give it a bath!"
> 2. (Unexpected) "It looks fine!" / "I don't know!" / child describes the color
> 3. (No response) Child is quiet or looking at the entity.
>
> **AI follow-up**:
> 1. "*(delighted, narrating the transformation)* You're painting the color back! Look... swoooosh... the faded parts are filling in... brighter... brighter... and THERE! Your friend's color is coming back! 'Oh!' says your friend, 'I can feel it! I'm getting brighter! Thank you, fix-it helper!' Look — you can SEE the difference!"
> 2. "*(warm, guiding)* You're looking so carefully — that's what a good fix-it helper does! What if we tried painting the color back? We could use a magic paintbrush! Want to try saying 'paint it!'?"
> 3. *(waits 3 seconds)* "*(soft prompt)* Your friend's color is fading — they look so pale! What if we painted some color back? Say 'paint!' and watch what happens!"
>
> **Screen**: Entity photo with a visible "faded" filter applied — desaturated, soft. When child proposes a fix:
> - A paint-swoosh animation washes across the entity from left to right
> - Color gradually saturates — the faded look lifts and rich color returns
> - The entity's expression shifts from sad to a small, relieved smile
> - A speech bubble appears: "I'm getting brighter!"
> - A single floating star drifts upward with a sparkle trail
> - A small "Round 1" indicator with a green wrench-checkmark appears in the corner

**Round 2 — "Your friend is tired!" (Emotional need — deeper)**

> **AI says**: "*(hushed, caring)* The color is back — beautiful! But wait... look at your friend's eyes. They look so tired. All those adventures wore them out. 'I'm so tired,' your friend whispers. 'I've been on so many adventures, but I never get to rest.' Your friend needs rest. How would YOU help them feel rested and comfy?"
>
> **Possible child responses**:
> 1. (Ideal) "Give them a bed!" / "Tuck them in!" / "Sing a song!" / "Let them sleep!"
> 2. (Unexpected) "I'm tired too!" / "Teddy sleeps with me!" / child yawns
> 3. (No response) Child is quiet, perhaps uncertain how to fix tiredness.
>
> **AI follow-up**:
> 1. "*(narrating transformation, gentle)* You're tucking them in... so gently. Look — your friend takes a deep breath... ahhhhh... the tired eyes start to soften... a peaceful look spreads across their face... and your friend murmurs: 'That's so nice. I haven't rested in so long. You always know what I need.' Look — a bigger smile this time! Your friend is feeling so much better because of YOU."
> 2. "*(warm, connecting)* You get tired too? That's how you KNOW what it feels like! What makes YOU feel rested? A cozy blanket? A soft pillow? Can you give that to your friend too?"
> 3. *(waits 3 seconds)* "*(gentle coaching)* When YOU feel really tired, what makes you feel better? A cozy spot? A soft blanket? Can you make your friend comfy? Try telling them what you'd do!"
>
> **Screen**: Background shifts to a soft, warm sunset tone. The entity's eyes have a gentle droopy tiredness animation. When child responds with a comfort solution:
> - A soft blanket-glow wraps gently around the entity
> - The tired eyes slowly relax into a peaceful, content expression
> - The entity's smile grows — noticeably bigger than Round 1
> - A speech bubble appears: "You always know what I need."
> - Two floating stars drift upward (one more than Round 1 — care deepening)
> - "Round 2" indicator with green wrench-checkmark

**Round 3 — "Fading AND tired AND missing you!" (Complex need — physical + emotional + relational)**

> **AI says**: "*(soft, caring concern)* Oh no, fix-it helper. Look. Your friend's color is starting to fade again... AND they still look tired... AND they whisper: 'When you go to school, I sit here all alone. I fade a little more every day because I miss you so much.' Your friend is faded AND tired AND lonely — all three at once! This is the BIGGEST fix yet. What's your plan?"
>
> **Possible child responses**:
> 1. (Ideal) "I'll take you with me!" / "I'll hug you every day!" / "I'll paint you AND tuck you in AND be your friend!" / combines solutions
> 2. (Unexpected) "I don't go to school!" / "Blanket!" / child solves only one need
> 3. (No response) Child seems overwhelmed by the complex need.
>
> **AI follow-up**:
> 1. "*(narrating the full transformation, deeply moved)* You're going to do ALL of that?! Watch... first — swoosh — the color floods back, brighter than EVER... then — ahhhh — the tiredness melts away, your friend looks rested and strong... and then — oh! — your friend's eyes light up and they whisper: '[Child's name]... you're not just a fix-it helper. You're my BEST friend. I'll never feel alone again because I know you'll always come back for me.' Look at that smile — the BIGGEST smile yet! Your friend is colorful, rested, and SO happy... all because of you."
> 2. "*(warm, building on partial solution)* A blanket — that helps with tired! Now your friend is cozy... but still fading, still missing you. Can you add something for the color AND the loneliness? What else could you do?"
> 3. *(waits 3 seconds)* "*(soft, scaffolding)* That's a LOT of things to fix! Let's start with one. Your friend's color is fading — can you say 'paint'? Then we'll help with tired and lonely too!"
>
> **Screen**: Entity photo with the faded filter returning, tired eyes, and a small tear drop visible. When child responds:
> - The transformation happens in STAGES:
>   - First: paint-swoosh animation — color floods back richer than ever (fading solved)
>   - Then: warm blanket-glow wraps around, tired expression relaxes into peace (tired solved)
>   - Finally: entity's whole posture lifts, eyes brighten, the biggest smile yet appears, a warm radiant glow surrounds them (lonely solved)
> - A speech bubble appears: "[Child's name], you're my best friend!"
> - THREE floating stars drift up in a cascade (deepening care arc — 1 in R1, 2 in R2, 3 in R3)
> - Golden workshop sparkles surround the screen
> - "Round 3" indicator with a gold star (not just checkmark — this was the hardest fix)

**Step 4: Payoff — The Magic Moment (Visible Transformation)**

> **AI says**: "*(soft, deeply warm)* Look at your friend now. Remember when they were faded and tired and lonely? Now look — the color is SO bright! They look rested and strong! And that smile... that's the smile of someone who knows they have the best friend in the whole world. Your friend whispers: '[Child's name]... you fixed everything. You brought my color back. You let me rest. And you made sure I'll never feel alone. I'm not just fixed — I'm BETTER than ever. Because of you.'"
>
> **Possible child responses**:
> 1. (Ideal) Child smiles, hugs their actual toy, says "I love you!" / "Yay!" / "All fixed!"
> 2. (Unexpected) "More!" / "Fix it again!" / "Another one!"
> 3. (No response) Child is quiet, looking at the screen with a soft expression.
>
> **AI follow-up**:
> 1. "*(beaming)* ALL FIXED! And your friend looks better than ever. That's what a great fix-it helper does!"
> 2. "*(playful, warm)* Your friend says 'Come fix me up again tomorrow!' The Fix-It Station is always open for you!"
> 3. "*(gentle, warm whisper)* Look at that big bright smile. That smile is all because of you."
>
> **Screen**: Full-screen warm golden workshop glow. Entity photo centered with vibrant, restored color — brighter than the original photo (the "better than ever" effect). The three-stage transformation replays as a quick montage:
> - Faded entity → colorful entity (Round 1 flash)
> - Tired entity → rested entity (Round 2 flash)
> - Lonely entity → happy, glowing entity (Round 3 flash)
> Then: A golden badge animation drops in reading "[Entity]'s Best Fix-It Helper" with a wrench-and-heart icon. Confetti in warm workshop colors (gold, copper, sky blue) rains down. Three stars arranged in a row below the badge — representing the three rounds of care.

**Step 5: Closing + IB Concepts**

> **AI says**: "*(warm, reflective, proud)* You know what you did today? Every time your friend needed something — color, rest, a friend who won't forget — YOU figured out what to do. Noticing what someone needs and doing something about it... that's called Responsibility. And look at you two now — your friend trusts you completely, and you care about them SO much. That special bond? That's called Connection. You're not just a fix-it helper. You're the best friend anyone could ever have."
>
> **Possible child responses**:
> 1. (Ideal) "I'm the best fixer!" / "Bye, friend!" / child hugs their toy
> 2. (Unexpected) "What's responsibility?" / "I want to fix more things!" / any response
> 3. (No response) Child is quiet, perhaps hugging their toy.
>
> **AI follow-up**:
> 1. "*(soft, closing)* The best fixer AND the best friend! The Fix-It Station is closing for today. See you next time, fix-it helper!"
> 2. "*(warm)* Responsibility is when you notice someone needs help and you DO something! That's exactly what you did! You can fix more things next time!"
> 3. *(waits 3 seconds)* "*(gentle close)* Your friend is smiling at you. The Fix-It Station is closing... but that friendship? That stays open forever."
>
> **Screen**: "Responsibility" appears in warm copper lettering with a wrench-and-caring-hands icon. "Connection" appears in soft gold lettering with a heart-link icon. Both words float gently beside the entity photo, which shows the entity in a bright, restored, happy state. The "[Entity]'s Best Fix-It Helper" badge glows softly at the bottom. Gentle workshop sparkle animation fades as the screen transitions to a warm, cozy close.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, state comparison, or non-speech audio detection. The "property detection" is performed by AI vision on the initial photo (supported in V1). All subsequent "transformations" are AI-driven narration and pre-programmed screen animations, not camera-detected state changes. Dialogue-based verification throughout. |
| 2 | Hook & Transition | PASS | Step 1 opens with emotional resonance ("Oh! Look at your friend! They look like they've had SO many adventures") and specific property observation ("See how the color looks a little faded here?"), not knowledge testing. Activity grows naturally from noticing the property into the fix-it caretaking game. Remove step labels and it reads as flowing conversation. |
| 3 | Edge Case Coverage | PASS | Every step includes 3 response branches (ideal, unexpected, silence). All unexpected branches validate first ("Of COURSE you love them — and they love you!") then redirect. All silence branches wait 3 seconds then offer a gentle, specific prompt. Round 3 includes scaffolding for when child is overwhelmed by the complex triple need. Template includes guidance for entities that don't look worn (AI playfully imagines a need). |
| 4 | IB Completeness | PASS | Responsibility and Connection explicitly named in closing. KUD has specific vocabulary (faded, worn, mend, rest, care). 3 ATL skills with sub-skills. 4 Related Concepts. Closing celebrates first ("You're the best friend anyone could ever have!") then naturally names concepts. Concepts earned — child literally practiced responsibility (noticing needs, proposing fixes) and built connection (deepening relationship arc across three rounds). |
| 5 | Tier Appropriateness | PASS | T1: Sentences are slightly longer than T0 but remain concrete and action-oriented. Vocabulary includes "faded," "mend," "comfy" — age 4–6 appropriate. Multi-step problems in Round 3 stretch T1 capacity. 3 rounds. Instructions require proposing solutions (not just responding), appropriate for T1 cognitive development. Clear scaffolding for children who need help breaking down the complex Round 3 problem. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers in parentheses. Zero instances of "AI guides" or "AI encourages." Specific transformation narration: "the faded parts are filling in... brighter... brighter... and THERE!" Every response branch is written as speakable dialogue. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with layout (workshop background, entity centered), animations (paint-swoosh, blanket-glow, staged transformation), visual elements (faded filter, speech bubbles, floating stars, round indicators, badge, montage), and emotional progression visible on screen. The property highlight on the actual photo grounds the game in observable reality. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter in this template. |
| 9 | Game Feel | PASS | Genuine stakes: entity is suffering and the child's proposed solutions determine the transformation. Uncertainty: will my fix work? How will the entity respond? Emotional climax: Round 3 where entity calls child by name and says "you're my best friend — I'll never feel alone again." Replayability: different detected properties seed different first needs, making each playthrough unique. Surprise/delight: the visible transformation (color returning, tiredness lifting) creates delight beyond warm praise. The property-bridge means the game feels personal — "MY toy's color really IS faded!" |
| 10 | Pillar Fidelity | PASS | Nurture pillar delivered fully. Core loop: detected need → child proposes fix → VISIBLE TRANSFORMATION. Magic moment: entity fully restored "better than ever," calls child by name, expresses deep personal trust. Child feels "I fixed it!" with visible evidence (transformation montage in Step 4). Relationship arc deepens: Round 1 "Thank you, fix-it helper!" → Round 2 "You always know what I need" → Round 3 "[Name], you're my best friend." Need escalation: physical → emotional → complex. Cannot be re-labeled as any other pillar — the property-seeded transformation arc and gratitude deepening are uniquely Nurture. |

**Overall**: ALL PASS — 0 issues found during self-evaluation

Ready for 教研 review.
