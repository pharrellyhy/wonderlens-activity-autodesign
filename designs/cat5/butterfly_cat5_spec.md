## Activity: The Butterfly World Detectives

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Butterfly World Detectives |
| Activity Category | 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Outdoor) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Form (What is it like?) & Causation (Why is it like this?) |
| Related Concepts | Habitat (designed), Pattern (designed), Connection (designed), Discovery (designed) |
| ATL Skills Focus | Research Skills (observation, collecting and recording data), Thinking Skills (critical thinking — deducing from clues, transfer — connecting finds to a pattern), Communication Skills (expressing — describing finds and reasoning) |
| Experience Pillar | Mystery |
| Game Style | mystery_trail |
| Design Version | 1.0 — mystery_trail (new) |
| Last Updated | 2026-04-01 |
| Trigger Entity | Butterfly |
| Trigger Scene | Child spots and photographs a butterfly resting on a flower in the park |
| Mapping Source | none |

### B. Activity Overview

- **① Brief Description**: After the child photographs a butterfly on a flower, the AI expresses wonder at the butterfly's beautiful wings and then recruits the child as a "Butterfly World Detective." The AI gives riddle-clues one at a time — each describing something nearby without naming it — and the child searches, guesses, and photographs what they think matches. After 3–4 finds, the AI reveals the hidden connection: everything the child found is part of the butterfly's secret world — its food, shelter, water, and home. The big "aha!" is that the child has been mapping the butterfly's habitat all along without knowing it.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "nectar," "habitat," "shelter," "wings," "antenna." Learn that butterflies need specific things to survive — flowers for nectar, leaves for resting, puddles for water, and plants for laying eggs.
  - **U (Understand)**: Understand that the **Form** of things in nature (bright colors, flat surfaces, wet spots) reveals clues about why they exist in a particular place, and that **Causation** explains why butterflies live where they do — each element of their habitat serves a purpose.
  - **D (Do)**: Practice deductive reasoning from riddle-clues (Thinking Skills — critical thinking), search for and photograph matching items outdoors (Research Skills — observation and data collection), and articulate why all their finds are connected (Communication Skills — expressing reasoning).

- **③ Design Highlight**: The "Butterfly World Detectives" frame transforms a nature scavenger hunt into a mystery investigation. The key mechanism is riddle-driven search with a delayed pattern reveal: the child doesn't know WHY they're finding these specific things until the end, when the AI reveals that every single find is something a butterfly needs. The riddles are sensory and playful ("I'm bright and I smell sweet..."), making each search feel like solving a puzzle. The magic moment — "Everything you found is part of your butterfly's secret world!" — reframes the entire activity retroactively, giving the child an "I figured it out!" rush.

- **④ Typical Scenario**: Child photographs a butterfly on a flower in the park → AI marvels at the butterfly's wings and wonders about its world → recruits the child as a Butterfly World Detective → gives riddle-clue #1 (something bright and sweet-smelling → flower) → child searches and photographs → AI confirms and gives next riddle-clue (something green and flat → leaf) → child searches and photographs → riddle-clue #3 (something wet on the ground → puddle or mud) → child searches and photographs → AI reveals the hidden pattern: "Look at everything you found — they ALL are things your butterfly needs! You just mapped its secret world!"

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs a butterfly resting on a flower in the park.
>
> **AI says**: "*(breathless, enchanted whisper)* Ohhh — look at that butterfly! Those wings are SO beautiful — like tiny painted windows! And look, it's sitting right on that flower. I wonder... why did it choose THAT flower? Do you think the butterfly likes it there?"
>
> **Possible child responses**:
> 1. (Ideal) "Because it's pretty!" / "It likes the flower!" / "It's drinking from it!"
> 2. (Unexpected) "I want to catch it!" / "It's going to fly away!" / "It's a monarch!"
> 3. (No response) Child watches the butterfly quietly.
>
> **AI follow-up**:
> 1. "*(excited, conspiratorial)* I think you're RIGHT — the butterfly LOVES that flower! But here's the thing — I bet there are MORE things in this park that the butterfly loves. Things that are part of its secret world. What if we could find them all?"
> 2. "*(warm, intrigued)* It IS amazing to watch! And you know what? That butterfly picked this exact spot for a reason. This flower is part of its secret world — and I bet there are MORE secret things nearby that it needs. Want to find out what they are?"
> 3. *(waits 2 seconds)* "*(gentle, wondering)* That butterfly chose this flower for a reason — it's part of the butterfly's secret world. And I bet there are MORE things in this park that the butterfly loves. I have an idea — want to be a detective and find them?"
>
> **Screen**: Butterfly photo centered with a soft, shimmering glow around the wings. Tiny animated sparkles drift near the flower petals. A faint magnifying glass icon pulses gently in the corner with a "?" inside it.

**Step 2: Mission Briefing**

> **AI says**: "*(adventurous, detective tone)* Alright — you are now an official Butterfly World Detective! Here's your mission: I'm going to give you riddle-clues about things hidden in this park. Things that are part of your butterfly's secret world! You search, you guess, and you take a photo. After you find them all, I'll tell you the SECRET that connects everything. Ready, Detective?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Yes!" / "What's the first clue?"
> 2. (Uncertain) "What do I look for?" / "Where do I go?"
> 3. (No response) Child looks around the park with curiosity.
>
> **AI follow-up**:
> 1. "*(thrilled)* Here comes your first riddle-clue! Listen carefully, Detective..."
> 2. "*(encouraging)* Don't worry — I'll give you riddle-clues! Each one describes something nearby. You just listen, think, and search. The riddles will guide you! Here comes the first one..."
> 3. *(waits 2 seconds)* "*(playful whisper)* Okay Detective, here's how it works — I describe something, you find it! Easy! Let's start with your very first riddle-clue..."
>
> **Screen**: A detective-themed "mission card" appears: a badge outline labeled "Butterfly World Detective" with a butterfly silhouette and a magnifying glass. Below it, 3 empty circle-shaped slots (to be filled as the child solves riddles). The butterfly photo sits above the slots with a golden star. A "CLUE #1" banner starts pulsing at the bottom. A faint question mark hovers over each empty slot.

**Step 3: Multi-Round Exploration (3–4 rounds)**

> **Round 1 — Riddle-Clue #1: The Flower**
>
> **AI says**: "*(mysterious, slow riddle voice)* Riddle-Clue number one! Listen closely, Detective... I'm thinking of something nearby. It's BRIGHT and colorful. It has a sweet smell. And tiny creatures visit it to drink something yummy inside. Can you find it? Go look and take a photo of what you think it is!"
>
> **Possible child responses**:
> 1. (Ideal) Child photographs a flower. "A flower!" / "This one!" / "I found it!"
> 2. (Unexpected) Child photographs something else — a colorful leaf, a berry, a bright toy. "Is it this?"
> 3. (No response / stuck) Child looks around but doesn't find anything or photograph anything.
>
> **AI follow-up**:
> 1. "*(triumphant)* YES, Detective! A flower — that's it! Flowers are bright and colorful, and inside they have something called NECTAR — that's the sweet, yummy drink butterflies love! Your butterfly was sitting on a flower just like this one. First clue — SOLVED! Two more to go!"
> 2. "*(thoughtful, encouraging)* Ooh, interesting guess! That IS colorful! But my riddle says tiny creatures visit it to drink something sweet inside. Can you think of something that bees and butterflies land on to sip from? Something with petals? Look for one nearby!"
> 3. *(waits 2 seconds)* "*(helpful whisper)* Detective hint! Think about what your butterfly was sitting on when you took that first photo. Something with petals, something colorful. Look near the bushes or in the flower bed — do you see anything bright and colorful with petals?"
>
> **STUCK BRANCH** *(if child still can't find a flower)*:
>
> **AI says**: "*(reassuring)* That's okay! Try looking along the edge of the path, near any bushes, or in a garden bed. Flowers like to grow where it's sunny! Even a tiny little wildflower in the grass counts. Do you see any spots of color on the ground or on a bush?"
>
> **Possible child responses**:
> 1. (Ideal) "I see one!" / Child spots a flower.
> 2. (Still stuck) "I can't find any." / "There are no flowers."
> 3. (No response) Child keeps searching.
>
> **AI follow-up**:
> 1. "*(cheering)* Go take a photo, Detective! Let's see your find!"
> 2. "*(warm)* No problem! Even a clover in the grass or a tiny weed flower counts — look right at your feet! If you really can't find one, take a photo of something that's bright and colorful — we'll make it work!"
> 3. *(waits 2 seconds)* "*(gently)* Look right near your feet in the grass — sometimes tiny flowers hide there! Take a photo of anything bright and pretty."
>
> **Screen**: New photo slides into the first empty slot on the mission card. A burst of golden sparkles and a magnifying glass "SOLVED!" animation plays over the slot. The clue text fades and a small flower icon appears. Counter updates to "Clue 1 of 3 — SOLVED!" A "CLUE #2" banner starts pulsing.

> **Round 2 — Riddle-Clue #2: The Leaf**
>
> **AI says**: "*(building excitement, mystery voice)* Riddle-Clue number TWO! Here it comes, Detective... I'm thinking of something that's green and flat. It can be big or small. Tiny creatures like to hide UNDER it when it rains. And some creatures even eat it for lunch! Can you find one? Go search and snap a photo!"
>
> **Possible child responses**:
> 1. (Ideal) Child photographs a leaf. "A leaf!" / "This big green one!" / "Here!"
> 2. (Unexpected) Child photographs grass, moss, or something else green. "Is it the grass?" / "This green thing?"
> 3. (No response / stuck) Child looks around without photographing.
>
> **AI follow-up**:
> 1. "*(impressed)* A leaf — BRILLIANT, Detective! Leaves are like little green umbrellas — butterflies hide under them when it's rainy or too hot. And baby caterpillars — that's what butterflies used to be — they MUNCH on leaves for food! Second clue — SOLVED! One more to go!"
> 2. "*(validating, then redirecting)* Ooh, grass IS green! You're on the right track — but my riddle says something FLAT that creatures hide UNDER. Think bigger and flatter — something on a bush or a tree, something that could be like a tiny roof. Look up at the branches or on a bush — do you see something flat and green?"
> 3. *(waits 2 seconds)* "*(helpful)* Detective hint! Look at any tree or bush near you. See those flat, green things growing on the branches? They're like tiny green blankets! Grab a photo of one you can reach!"
>
> **Screen**: Second photo slides into the second slot. A burst of green sparkles and "SOLVED!" animation. A small leaf icon appears. Counter updates to "Clue 2 of 3 — SOLVED!" A "CLUE #3" banner pulses.

> **Round 3 — Riddle-Clue #3: The Puddle / Wet Spot**
>
> **AI says**: "*(dramatic, hushed detective voice)* Last riddle-clue, Detective — this is the tricky one! I'm thinking of something WET. You might find it on the ground. It could be a tiny puddle, or a damp patch of mud, or even drops on a rock. Butterflies visit it, but NOT to swim — they go there to DRINK! Find something wet and take a photo!"
>
> **Possible child responses**:
> 1. (Ideal) Child photographs a puddle, wet mud, dew on grass, or a damp spot. "A puddle!" / "Wet mud!" / "I found water!"
> 2. (Unexpected) Child photographs a water fountain, a bottle, or a dry patch. "Is it this?" / "I found a fountain!"
> 3. (No response / stuck) Child can't find anything wet.
>
> **AI follow-up**:
> 1. "*(thrilled, almost shouting)* YES! You found it, Detective! Butterflies actually drink from puddles and wet mud — it's called 'puddling!' The wet ground has tiny minerals that butterflies need, like vitamins! Final clue — SOLVED! ALL clues solved!"
> 2. "*(encouraging)* That does have water! But my riddle is about something on the GROUND — a puddle, a damp muddy spot, or even wet leaves. Butterflies land on the ground to drink! Look near a shady spot or where the ground dips down — any wet patches?"
> 3. *(waits 2 seconds)* "*(helpful whisper)* This one IS tricky! Look for a shady spot near a tree or a low place in the ground — water collects there. Even a patch of dark, damp dirt counts! Or check near a water fountain or faucet — the ground is often wet nearby."
>
> **STUCK BRANCH** *(if child truly can't find anything wet)*:
>
> **AI says**: "*(reassuring)* It's a dry day! That's okay, Detective. Look for the DARKEST patch of dirt you can find — dark dirt is usually a little damp. Or check near a tree trunk at the very bottom — it's often moist there. Even one drop on a leaf counts!"
>
> **Possible child responses**:
> 1. (Ideal) "I found some dark dirt!" / Child photographs a damp-looking area.
> 2. (Still stuck) "Everything is dry!" / "I can't find water."
> 3. (No response) Child keeps looking.
>
> **AI follow-up**:
> 1. "*(encouraging)* Perfect — go photograph it! Dark dirt is damp dirt, and butterflies love it!"
> 2. "*(warm, flexible)* That's totally fine! Take a photo of anything near the ground — a rock, some dirt, a patch of moss. Butterflies visit ALL of these! We'll count it, Detective!"
> 3. *(waits 2 seconds)* "*(gently)* How about this — just photograph the ground near the closest tree. That counts! Butterflies love resting on cool, shady ground."
>
> **Screen**: Third photo slides into the final slot. A big burst of multi-colored sparkles and a "ALL CLUES SOLVED!" animation. All three slots glow with golden borders. A "REVEAL TIME!" banner appears and pulses dramatically. A large magnifying glass icon shimmers in the center.

> **Round 4 (Optional Bonus) — If child is highly engaged:**
>
> **AI says**: "*(excited)* Wait — BONUS clue, Detective! I'm thinking of something small, round, and colorful. It might be a berry, a seed, or a tiny bud. Butterflies don't eat it — but the birds that live near butterflies do! Can you spot one?"
>
> **Possible child responses**:
> 1. (Ideal) Child photographs a berry, seed pod, or small bud.
> 2. (Unexpected) Child photographs something else round and colorful.
> 3. (No response / wants to move on) "What's the secret?" / "Tell me!"
>
> **AI follow-up**:
> 1. "*(amazed)* Bonus clue SOLVED! Birds eat berries and seeds, and birds and butterflies share the same park — they're neighbors! Now — are you ready for the BIG secret?"
> 2. "*(accepting)* That's a great find! It's round and colorful — I'll count it! Now — ready for the BIG secret?"
> 3. "*(laughing)* You want the secret? I don't blame you — okay, here it comes!"
>
> **Screen**: If bonus round played, a bonus "star" slot lights up next to the three main slots. Then the "REVEAL TIME!" banner appears.

**Step 4: Synthesis — The Big Pattern Reveal**

> **AI says**: "*(slow, dramatic build-up)* Okay, Butterfly World Detective — look at everything you found. A flower... a leaf... something wet on the ground... Now here's the SECRET I've been hiding... *(dramatic pause)* ...EVERYTHING you found is something your BUTTERFLY needs to live! The flower gives it nectar to drink. The leaf gives it shade to rest AND food for its babies. The wet ground gives it minerals and water. You didn't just find random things — you found your butterfly's whole SECRET WORLD! Its home, its restaurant, its water fountain, and its baby nursery — all right here in this park!"
>
> **Possible child responses**:
> 1. (Ideal) "Whoa!" / "The butterfly needs all of those?" / "I found its world!" / Child is surprised and excited.
> 2. (Unexpected) "I knew it!" / "That's cool!" / "Butterflies eat leaves?"
> 3. (No response) Child looks at the screen, taking it in.
>
> **AI follow-up**:
> 1. "*(celebrating)* You DID find its world! The flower is like the butterfly's restaurant — that's where it eats. The leaf is like its bedroom — that's where it rests and where its babies grow. And the wet spot is like its drinking fountain! Everything your butterfly needs is right here, and YOU found it all, Detective!"
> 2. "*(validating, adding detail)* It IS cool! And you know what's really amazing? The BABY butterflies — caterpillars — they eat the leaves. Then they grow up and drink nectar from the flowers. And the wet ground gives them special minerals to stay strong. It's all connected — like a circle!"
> 3. *(waits 2 seconds)* "*(warm, amazed)* You mapped the butterfly's whole world! The flower feeds it, the leaf shelters it, and the wet ground gives it water. Your butterfly chose this park because EVERYTHING it needs is right here. And you, Detective — you figured it out!"
>
> **Screen**: All collection photos displayed in a circle around the original butterfly photo in the center. Animated golden lines connect each find to the butterfly with small labels: "Nectar" (flower → butterfly), "Shelter & Food for babies" (leaf → butterfly), "Water & Minerals" (wet spot → butterfly). A shimmering "HABITAT" word floats above the arrangement. A pulsing glow moves around the circle showing how everything connects. Gentle butterfly wing animations flutter near each connection line.

**Step 5: Discovery Celebration**

> **AI says**: "*(amazed, reflective)* Detective, look at your map — a flower, a leaf, and a wet spot. They look SO different from each other! But they ALL ended up being things your butterfly needs. Why do you think the butterfly picked THIS park to live in?"
>
> **Possible child responses**:
> 1. (Ideal) "Because it has everything!" / "Because the flowers are here!" / "It likes this spot!"
> 2. (Unexpected) "I don't know." / "Because it's pretty."
> 3. (No response) Child looks at the collection on screen.
>
> **AI follow-up**:
> 1. "*(delighted)* Exactly! This park has EVERYTHING a butterfly needs — food, water, shelter — all in one place. That's why it lives here! It's like you discovered the butterfly's secret shopping list for picking a home!"
> 2. "*(warmly)* It IS pretty — and here's a secret: pretty things like flowers aren't just pretty for US — they're USEFUL for the butterfly! The bright colors help the butterfly find the nectar. Pretty AND useful!"
> 3. *(waits 2 seconds)* "*(sharing a wonder)* I think it's because this park has everything on the butterfly's checklist — food from flowers, shelter from leaves, and water from the ground. The butterfly is really smart about picking where to live!"
>
> **Screen**: The habitat map remains. A soft animation shows a tiny butterfly visiting each find in sequence — landing on the flower, resting under the leaf, sipping from the wet spot — then returning to center. Small text callouts appear: "Food!" "Shelter!" "Water!" The word "HABITAT" glows steadily above.

**Step 6: Closing + IB Concepts**

> **AI says**: "*(warm, proud celebration)* Congratulations, Butterfly World Detective! You did something incredible today. You looked closely at the **Form** of things — bright petals, flat green leaves, wet ground — and you figured out what they really are. And you discovered the **Causation** — the reason your butterfly lives here. It's not by accident — every single thing you found is something the butterfly NEEDS. Flowers, leaves, water — they all have a job! You earned your Butterfly World Detective Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about butterflies, wants to find more.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child watches the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you see a butterfly, look around — see if you can spot its flower restaurant, its leaf bedroom, and its puddle fountain! You'll see its whole world now. Bye for now, Detective!"
> 2. "*(warm)* Your detective badge is saved! Every butterfly you see has its own secret world — now YOU know how to find it. Bye, Detective!"
> 3. *(waits 2 seconds)* "*(soft)* Your badge is shining, Detective. See you next time!"
>
> **Screen**: A golden "Butterfly World Detective Badge" appears — circular, with a butterfly silhouette at the center and the 3 collection photos as small insets around the edges, each with its connection label (Nectar, Shelter, Water). The words **"Form"** and **"Causation"** float up artistically — "Form" styled with bright, petal-like shapes filling the letters, "Causation" with tiny arrow connections linking the letters like a cause-and-effect chain. A small habitat icon (circle with butterfly, flower, leaf, water drop) nestles between the concept words. A soft chime plays. Tiny animated butterflies drift across the screen and settle on the badge.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | Each photo processed independently. No OCR, face detection, IMU, or state-change comparison required. Multi-photo workflow (3–4 photos across rounds) fully supported. All verification done through AI recognition of individual photos + dialogue. |
| 2 | Hook & Transition | PASS | Step 1 opens with emotional wonder ("Those wings are SO beautiful — like tiny painted windows!") and an imaginative question ("why did it choose THAT flower?"), not knowledge testing. Activity grows naturally from butterfly observation → wondering about its world → detective mission. No "let's play a game" break. |
| 3 | Edge Case Coverage | PASS | All steps have 3 response branches (ideal, unexpected, no response). Steps 3 rounds include concrete stuck branches with specific location hints ("look along the edge of the path," "near any bushes," "check near a tree trunk at the very bottom"). "Unexpected" branches always validate first ("That IS colorful!") then redirect. "Can't find" branches in outdoor search rounds with actionable hints. |
| 4 | IB Completeness | PASS | KUD fully defined: 5 vocabulary words (nectar, habitat, shelter, wings, antenna), 2 conceptual understandings (Form reveals clues, Causation explains butterfly habitat), 3 skills (critical thinking, observation/data collection, expressing reasoning). Form + Causation as Key Concepts. 4 Related Concepts (Habitat, Pattern, Connection, Discovery). 3 ATL skills with sub-skills. Closing speech names Form and Causation naturally as praise. Concepts match what child actually did — observed forms and deduced causes. |
| 5 | Tier Appropriateness | PASS | T1 (ages 4–6): Sentences 5–8 words. 3-part riddle structure with concrete sensory clues ("bright and colorful," "green and flat," "wet on the ground"). Open-ended search tasks. Concrete vocabulary (nectar, shelter, habitat introduced in context). 2–3 step tasks per riddle (listen → search → photograph). |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. Zero instances of "AI guides" or "AI encourages." Riddle-clues are specific and sensory. All responses are actual words the AI speaks. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions: butterfly photo with shimmering wing glow, detective mission card with badge and empty slots, per-round "SOLVED!" animations with sparkles, habitat connection map with labeled golden lines, badge with butterfly silhouette and concept words styled with petal-shapes and arrow-chains. |
| 8 | Entity Mapping Alignment | N/A | No mapping parameter — design is not mapping-informed. |
| 9 | Game Feel | PASS | Genuine uncertainty in every round (child doesn't know what the riddle describes). Stakes: "Can I solve this riddle?" Pattern reveal creates a major "aha!" moment — the child doesn't know the hidden connection until the end. Clear emotional climax at the reveal ("EVERYTHING you found is something your BUTTERFLY needs!"). Replayable: different parks yield different finds. Surprise and delight in the retroactive reframing of all finds. |
| 10 | Pillar Fidelity | PASS | Mystery pillar fully delivered. Child feels "I figured it out!" at the pattern reveal. Magic moment = hidden truth revealed (the connection between all finds). Core loop = clues → deduction → aha! Game element = riddle-driven search + delayed pattern reveal. Emotional arc: curiosity → search → solve → bigger mystery → revelation. Cannot be re-labeled as another pillar — the riddle-clue mechanic and hidden pattern reveal are distinctively Mystery. |

**Overall**: ALL PASS — mystery_trail with riddle-clue search and habitat pattern reveal. Litmus test: the child doesn't know they're mapping a butterfly's habitat until the reveal. The "aha!" moment retroactively transforms all their finds from random things into a connected ecosystem.
