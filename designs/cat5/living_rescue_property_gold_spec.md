# Activity Design: Living Rescue + Category 5 (Collection/Tracking Exploration)

> Generated: 2026-04-08 | Property-bridge template | Agent: Activity Design Agent

---

## Activity: The Life Rescuer Squad

### A. Basic Info

- **Activity Name**: The Life Rescuer Squad
- **Activity Category**: 5 — Collection/Tracking Exploration (Out-of-Device, Solo, Outdoor)
- **Recommended Tier**: T1 (ages 4-6)
- **Core IB Key Concepts**: **Responsibility** (Taking care), **Connection** (Living things helping each other)
- **Related Concepts (Discipline)**: Care, Interdependence, Empathy, Conservation
- **ATL Skills Focus**: Social Skills (empathy, cooperation), Thinking Skills (creative thinking, transfer), Communication Skills (expressing ideas)
- **Experience Pillar**: Nurture
- **Game Style**: rescue_team
- **Design Version**: 1.0
- **Last Updated**: 2026-04-08
- **Trigger Entity**: Any entity where AI detects something alive or natural (plant, insect, animal, tree, flower, moss, etc.)
- **Trigger Scene**: Child photographs any living thing outdoors — a plant, a flower, a bug, a tree, a bird, moss on a rock, etc.
- **Mapping Source**: property-bridge
- **IB Theme**: Sharing the Planet

### B. Activity Overview

- **① Brief Description**: After photographing any living thing, the AI notices a sign of need — the plant looks thirsty, the flower is drooping, the tree has a broken branch, the bug looks lost. The AI frames the child as a "Life Rescuer" and challenges them to find 3 more living things nearby that need help. For each find, the AI identifies a "need" from the photo (drooping, dry, fallen, lonely, overgrown, tangled, dusty, wilting) — the child does NOT self-report the need. The child then proposes a care solution for each. At synthesis, the AI reveals how the rescued living things can help EACH OTHER — forming a mutual aid circle. The magic moment is discovering that the things you rescued can take care of one another.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Living things can show signs of needing help (drooping, drying, falling, being alone); water, shade, support, and companionship are ways to help living things; "alive" means it grows, needs water or food, and can change — plants, insects, and animals are alive, while rocks, plastic, and metal are not; things that receive help can also give help to others
  - **U (Understand)**: When we notice a living thing needs help, we can take Responsibility by thinking of a solution — care means noticing AND acting. Living things that seem separate are actually Connected — they can support each other in surprising ways, forming a web of mutual aid.
  - **D (Do)**: Observe signs of need in living things through photographs (Research — observation); propose creative care solutions (Thinking — creative thinking); explain how rescued living things could help each other (Communication — expressing ideas)

- **③ Design Highlight**: The AI-as-need-assessor mechanic is the first star. When the child photographs a living thing, the AI examines the photo and identifies the need — "I can see this plant's leaves are curling inward — that means it is thirsty!" The child does not self-report; the AI's visual assessment creates surprise and teaches observational vocabulary. The mutual aid synthesis is the second star. After the child rescues 3 living things by proposing care, the AI flips the script: "Now your rescue team is complete — but guess what? They can help EACH OTHER!" The child discovers that the watered plant can shade the bug, the propped-up flower can attract a bee to help the tree, and the tree's fallen leaves can feed the soil for the plant. This transforms one-way caregiving into a web of interdependence — the "I helped!" feeling deepens into "They help each other!"

- **④ Typical Scenario**: A child in a garden photographs a droopy plant, AI notices it looks thirsty, child becomes a Life Rescuer, finds 3 more living things that need help (a wilting flower, a lost bug, a dry patch of moss), AI identifies each need from the photo, child proposes care for each, and discovers at the end that all the rescued living things can help one another.

### C. Interaction Flow — Detailed Design [Target Tier: T1]

**Step 1b: Transition Bridge — Cold Start**

> **Context**: Child photographs any living thing outdoors (e.g., a plant with drooping leaves) with no prior conversation.
>
> **AI says**: "*(tender, concerned tone)* Oh, look at this plant! I can see its leaves are drooping down and curling at the edges. That usually means it is feeling really thirsty — it needs a good drink of water! Poor little plant. I bet there are MORE living things around here that need help too. What do you think this plant needs most?"
>
> **Possible child responses**:
> 1. (Ideal) "Water!" / "It needs a drink!" / "Some shade!"
> 2. (Unexpected) "It's green!" / "I like plants!" / "Can I touch it?"
> 3. (No response) Child looks at the plant quietly.
>
> **AI follow-up**:
> 1. "*(warm, impressed)* Water — great idea! A big drink would perk those droopy leaves right up. You already know how to take care of living things! I bet other living things nearby need help too."
> 2. "*(warm, agreeing)* It IS green — that means it is alive and growing! But see how the leaves droop down? That is a sign it is thirsty. Living things tell us when they need help — we just have to look carefully! You could be its helper!"
> 3. *(wait 2s)* "*(gentle, coaxing)* See how its leaves hang down and curl? That is how plants say 'I am thirsty!' Maybe it needs a drink of water, or some shade from the hot sun. What do you think would help?"
>
> **Screen**: Plant photo centered with a soft warm glow. The drooping leaves are subtly highlighted with a gentle pulsing circle. A tiny water droplet icon and sun icon float nearby, suggesting possible needs.

**Step 2: Mission Briefing — Life Rescuer**

> **AI says**: "*(heroic, rallying tone)* You are now a Life Rescuer! Your mission: find three LIVING things nearby that need help. They could be plants, flowers, bugs, trees — anything that is ALIVE! For each one, take a photo and I will look at it closely to see what it needs. Then YOU tell me how to help it! At the end, we will see something amazing — your rescued things can help EACH OTHER! Ready, Life Rescuer?"
>
> **Possible child responses**:
> 1. (Ideal) "Ready!" / "Let's rescue things!" / "I can find them!"
> 2. (Unexpected) "What counts as alive?" / "Do rocks need help?"
> 3. (No response) Child looks around uncertainly.
>
> **AI follow-up**:
> 1. "*(excited, encouraging)* Let's go, Life Rescuer! Look around — on the ground, near bushes, by the path, up in the branches. Find something alive that looks like it could use some care. Take a photo when you spot it!"
> 2. "*(warm, helpful)* Great question! Alive means it GROWS — like plants, flowers, trees, bugs, and animals. They need water or food to live, and they can change over time. Rocks and plastic are NOT alive — they do not grow or need water. Look for something green, something crawling, something with petals!"
> 3. *(wait 2s)* "*(gentle, guiding)* Try looking near the ground first. See any plants with droopy leaves? A flower leaning over? A little bug all by itself? Even a patch of dry moss counts! Take a photo of anything alive that looks like it needs help!"
>
> **Screen**: A mission card appears with a "Life Rescuer" badge at the top — a shield with a green sprout and a tiny heart. Four collection slots in a row — the first slot filled with the initial photo and labeled with its need (e.g., "Plant — needs water"). Three empty slots glow softly, each marked with a green cross icon. A numbered checklist reads: 1) Find 3 living things that need help. 2) I will tell you what each one needs. 3) See how they help each other!

**Step 3: Multi-Round Exploration (3-4 rounds)**

> **Round 1 — First Rescue** (full detail):
>
> *(Child takes a photo of a living thing — e.g., a flower leaning sideways)*
>
> **AI says**: "*(examining closely, then concerned)* Oh! Let me look at this photo carefully... I can see a flower, and it is leaning way over to one side. Its stem looks thin and wobbly — like it cannot hold itself up anymore. I think it needs some SUPPORT! Something to lean against so it can stand tall again. What would you do to help it, Life Rescuer?"
>
> **Possible child responses**:
> 1. (Ideal) "Prop it up with a stick!" / "Put a rock next to it!" / "Tie it to something!"
> 2. (Unexpected) "It's pretty!" / "I want to pick it!"
> 3. (No response) Child looks at the flower silently.
>
> **AI follow-up**:
> 1. "*(warm, celebrating)* A stick to lean on — perfect! *Imagine the flower slowly straightening up, its petals lifting toward the sun.* It is already feeling stronger thanks to you! Two more rescues to go, Life Rescuer!"
> 2. "*(playful, redirecting)* It IS pretty — even pretty flowers need help sometimes! See how it leans over? Its stem is too thin to hold up alone. What if we gave it something to lean against — like a little stick? *The flower slowly straightens up.* You helped it stand! Two more to find!"
> 3. *(wait 2s)* "*(gentle, prompting)* See how it is leaning? Its stem cannot hold it up by itself. What if we put a little stick next to it for support? *The flower tilts upward, its petals catching the sun.* It is getting better! Two more rescues to go!"
>
> **Screen**: Flower photo slides into the second collection slot. The slot label updates to "Flower — needs support." A tiny animation shows a flower icon straightening up. Counter shows "1 of 3 rescued."

> **Round 2 — Second Rescue** (full detail):
>
> *(Child takes a photo of a living thing — e.g., a small bug on a dry patch of ground)*
>
> **AI says**: "*(examining the photo, then sympathetic)* Let me see... oh, I see a little bug! And look at the ground around it in the photo — it is all dry and cracked. This little bug is on hot, dry ground with no shade anywhere! I think it needs some SHADE — a cool, damp spot to rest. How would you help this little bug, Life Rescuer?"
>
> **Possible child responses**:
> 1. (Ideal) "Move it to the shade!" / "Put a leaf over it!" / "Take it near water!"
> 2. (Unexpected) "Eww, a bug!" / "It's tiny!" / "Can I keep it?"
> 3. (No response) Child watches the bug quietly.
>
> **AI follow-up**:
> 1. "*(delighted, encouraging)* A leaf for shade — that is so creative! *Imagine the little bug scurrying under a cool leaf, relaxing in the shade.* It is feeling SO much better! One more rescue to go!"
> 2. "*(warm, playful)* Tiny, yes — but even tiny things need help! This little bug is sitting on hot, dry ground. See how cracked the dirt looks in the photo? What if we found it a shady spot under a leaf? *The bug wiggles happily under a cool green leaf.* You helped! One more rescue!"
> 3. *(wait 2s)* "*(gentle, encouraging)* This little bug is on very dry, hot ground — see the cracks in the dirt? It needs a cool place. What if there was a leaf nearby to give it shade? *The bug finds a leaf and rests underneath.* There it goes! One more to find!"
>
> **Screen**: Bug photo slides into the third collection slot. The slot label updates to "Bug — needs shade." A tiny animation shows a bug icon moving under a leaf shape. Counter shows "2 of 3 rescued."

> **Round 3 — Third Rescue** (full detail):
>
> *(Child takes a photo of a living thing — e.g., a patch of dry moss on a rock, a lonely sapling, a tangled vine)*
>
> **AI says**: "*(examining carefully, then tender)* Let me look very closely at this photo... I can see [a patch of moss on this rock, and it looks brown and crumbly at the edges — that means it is drying out / a tiny tree all by itself with no other trees around — it looks a bit lonely / a vine all tangled up in a knot — it cannot spread its leaves to catch the sun]. I think it needs [a little mist of water to stay soft and green / a friend nearby to share the wind and rain with / to be gently untangled so its leaves can breathe]. What would you do to help, Life Rescuer?"
>
> **Possible child responses**:
> 1. (Ideal) "Spray it with water!" / "Plant something next to it!" / "Untangle it carefully!"
> 2. (Unexpected) "It looks weird!" / "I don't know what that is!"
> 3. (No response) Child looks at it curiously.
>
> **AI follow-up**:
> 1. "*(touched, warm)* [Water / A friend / Untangling] — what a kind idea! *Imagine [the moss turning soft and green again / a little flower growing beside the sapling / the vine slowly uncurling, its leaves stretching toward the light].* Your rescue team is COMPLETE, Life Rescuer!"
> 2. "*(warm, validating)* It might look [unusual/interesting], but it is ALIVE — and it needs help! From the photo I can see [specific visual cue]. [Care solution]. *[Micro-transformation narration].* You helped! Rescue team complete!"
> 3. *(wait 2s)* "*(gentle, revealing)* From what I see in the photo, this [living thing] needs [care]. *[Micro-transformation narration].* All three rescues done!"
>
> **Screen**: Photo slides into the fourth collection slot. The slot label updates with the appropriate need. Counter shows "3 of 3 rescued!" with a sparkle celebration burst.
>
> **Round 4 (optional)** (abbreviated — if child is especially engaged):
>
> If the child finds a fourth living thing (e.g., a bird with ruffled feathers, a worm on hot pavement, a wilting petal), AI identifies its need from the photo, child proposes care, and it joins as a bonus member. AI says: "*(amazed)* A bonus rescue! Your squad is even bigger now!"
>
> **Stuck Branch** (if child cannot find a living thing that needs help):
>
> **AI says**: "*(helpful, conspiratorial)* Living things that need help like to hide! Try looking close to the ground near bushes — dry leaves or thirsty moss love to be there. Check near paths for little bugs on hot ground. Even a flower leaning over in the wind counts! Remember — alive means it grows. Look for green things, crawling things, or things with petals!"
>
> **Screen**: A soft pulsing hint arrow appears pointing toward the ground near a bush. The text "Try: droopy flowers, dry moss, bugs on hot ground, lonely saplings" appears in a small bubble.

**Step 4: Synthesis — The Magic Moment (Mutual Aid)**

> **AI says**: "*(excited, building suspense)* Life Rescuer, your rescue squad is complete! You helped the flower stand tall, gave the bug some shade, and [cared for the third living thing]. But guess what? Now THEY can help each other! Watch this — the flower you propped up is standing tall now, and its big petals can give SHADE to the little bug when the sun gets too hot! And the bug? It can crawl around and spread pollen to help MORE flowers grow! But here is the big question — how does [the third rescued thing] help the flower?"
>
> **Possible child responses**:
> 1. (Ideal) "The moss keeps the ground wet for the flower!" / "The tree blocks the wind!" / "The vine gives it something to climb!"
> 2. (Unexpected) "I don't know." / "They can't help each other." / Child names a different connection.
> 3. (No response) Child thinks quietly.
>
> **AI follow-up**:
> 1. "*(amazed, celebrating)* YES! [Specific mutual aid explanation]! The flower shades the bug, the bug spreads pollen for the flower, and [the third item] [helps the flower/bug]. They are ALL helping each other! That is what a real rescue team does — everyone helps everyone!"
> 2. "*(warm, scaffolding)* Think about it — [specific hint based on the third item's nature]. What if [specific mutual aid scenario]? *[Visual narration of the connection forming].* See? Even the [smallest/quietest/least obvious] member of the team can help! They are a real rescue team now!"
> 3. *(wait 2s)* "*(gentle, revealing)* Here is how it works — [specific mutual aid explanation with all three connections]. Now they are ALL helping each other. Your rescue team is the best, Life Rescuer!"
>
> **Screen**: All four photos displayed in a circle (initial item at top, then the three rescues). Animated arrows appear between them showing mutual aid connections — each arrow has a tiny icon showing the type of help (shade icon, pollen icon, moisture icon, wind-block icon). A glowing heart appears in the center of the circle. A banner reads: "Rescue Team — Helping Each Other!" Each item's "before" state (droopy, hot, dry, tangled) fades into a "better" state (tall, cool, moist, free).

**Step 5: Discovery Celebration**

> **AI says**: "*(proud, reflective)* Life Rescuer, look at what you did! You found living things that needed help. You gave each one exactly what it needed. And then something amazing happened — they started helping EACH OTHER. The flower shades the bug. The bug helps the flower. [The third connection]. Every living thing in your team gives something AND gets something! Which rescue was your favorite? Which one made you feel the best?"
>
> **Possible child responses**:
> 1. (Ideal) "The bug because it was so hot!" / "The flower because it was falling over!"
> 2. (Unexpected) "I liked finding all of them!" / "Can I rescue more?"
> 3. (No response) Child looks at the display thoughtfully.
>
> **AI follow-up**:
> 1. "*(touched)* That one really needed you! And now it is part of a team where everyone takes care of everyone else. Even the smallest living thing can do something big for someone else."
> 2. "*(warm, celebrating)* You loved ALL of them — that is what makes you such a great Life Rescuer! And yes, there are always more living things that need help. You can be a Life Rescuer every time you go outside!"
> 3. *(wait 2s)* "*(gentle)* They all needed your help, and you gave it. Point to the one that makes you smile the most. That is your star rescue!"
>
> **Screen**: Collection photos displayed with a golden star appearing on the child's chosen favorite. Animated green vines gently connect all four photos. A banner reads: "Living things rescued — the squad helps each other!"

**Step 6: Closing + IB Concepts**

> **AI says**: "*(proud, warm celebration)* You are an incredible Life Rescuer! You noticed living things that needed help and you DID something about it. That is Responsibility — when you see something alive that needs care and you step up to help. And then your rescue team helped each other — the flower shaded the bug, the bug spread pollen for the flower, and [third connection]. That is Connection — every living thing is linked to other living things, giving help and getting help. You earned your Life Rescuer Badge!"
>
> **Possible child responses**:
> 1. (Engaged) Cheers, talks about wanting to rescue more, or asks about the badge.
> 2. (Quiet) Smiles or says nothing.
> 3. (No response) Child looks at the screen.
>
> **AI follow-up**:
> 1. "*(encouraging)* Next time you go outside, look for living things that need help! A droopy flower, a thirsty plant, a bug on hot ground — they are everywhere. And remember, when you help one, you help them ALL because they are all connected. See you on the next rescue, Life Rescuer!"
> 2. "*(warm)* Your badge is saved! You are a real Life Rescuer now. Bye for now, Rescuer!"
> 3. *(wait 2s)* "*(soft)* Your Life Rescuer Badge is glowing. Great rescue mission today!"
>
> **Screen**: "Life Rescuer Badge" — a green shield with a golden sprout in the center and four small icons around it representing the rescued living things. "Responsibility" in warm green lettering with a caring-hands icon and "Connection" in golden lettering with a linked-vine icon float artistically. Four collection photos as small insets around the badge border. Gentle leaf and petal animations float across the screen.

---

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | No OCR, face detection, IMU, or state-change comparison required. Multi-photo workflow processes each photo independently. AI identifies "needs" from visual cues in each photo (drooping stems, dry/cracked ground, curled leaves, isolation) — all reliably identifiable visually. AI describes imagined micro-transformations through dialogue, not visual comparison. "Alive" is visually verifiable — plants, insects, animals vs rocks, plastic, metal. |
| 2 | Hook & Transition | PASS | Step 1 opens with emotional concern ("I can see its leaves are drooping down and curling at the edges — it is feeling really thirsty!"), not knowledge testing. Activity grows naturally from noticing one living thing needs care to finding more. |
| 3 | Edge Case Coverage | PASS | Every step has 3 response branches (ideal, unexpected, no response). Stuck branch in Step 3 provides concrete location hints ("near bushes," "near paths," "close to the ground") and clarifies what "alive" means. Step 2 handles "what counts as alive?" explicitly. Step 4 synthesis has scaffolding for children who cannot imagine mutual aid. Wait times specified for all silence branches. |
| 4 | IB Completeness | PASS | Responsibility + Connection named as Key Concepts; 4 Related Concepts listed; KUD fully specified with specifics; 3 ATL skills with sub-skills; closing naturally names concepts as praise ("That is Responsibility... That is Connection"). Concepts are earned — child actively takes responsibility for care AND discovers connections between rescued living things. |
| 5 | Tier Appropriateness | PASS | T1: sentences 5-8 words in key prompts, open-ended questions ("What would you do to help?"), concrete vocabulary (droopy, dry, thirsty, shade, water, prop up, lonely, curling, cracked). 2-3 step mission tasks. AI identifies needs in simple language. |
| 6 | Dialogue Specificity | PASS | Every AI line is concrete dialogue with tone/emotion markers. No abstract instructions like "AI guides the child." All micro-transformations described in specific, imagined language. AI-as-assessor lines describe specific visual cues from the photo before announcing the need. |
| 7 | Screen & UI Completeness | PASS | Every step has specific screen descriptions with layout, animations, and visual elements. Synthesis screen describes mutual aid arrows, heart icon, before/after states. Badge design specified. |
| 8 | Entity Mapping Alignment | N/A | Property-bridge template — works for any entity where AI detects something alive. |
| 9 | Game Feel | PASS | Genuine stakes: each living thing's visible need creates urgency; AI-as-assessor creates surprise — child does not know what the AI will diagnose from the photo. The mutual aid synthesis is a surprise twist — the child does not expect rescued living things to help each other. Clear emotional climax when the circle of mutual aid is revealed. Replayable — different outdoor spaces yield different rescue teams with different mutual aid configurations. |
| 10 | Pillar Fidelity | PASS | Nurture pillar: child feels "I helped!" — visible need identified by AI, care proposed by child, micro-transformation narrated. Need-solve-impact loop drives Step 3. Magic moment = rescued team helping EACH OTHER (mutual aid synthesis), matching rescue_team's defined magic moment. Core loop is empathy-driven collection + care proposals, not generic Q&A. Could NOT be re-labeled to another pillar — the care/rescue framing and mutual aid synthesis are uniquely Nurture. |

**Overall**: ALL PASS — Ready for review
