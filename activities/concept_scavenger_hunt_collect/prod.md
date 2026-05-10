## Shared Clue Scavenger Hunt

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Shared Clue Scavenger Hunt |
| Activity Category | 5 -- Collection/Tracking Exploration (Out-of-Device, Solo) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | Similarity, Classification, Evidence, Observation |
| ATL Skills Focus | Research Skills (observation, evidence collection), Thinking Skills (classification), Communication Skills (explaining a rule) |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The child starts with one photographed object and a shared clue such as `{shared_feature}`. They find and photograph three more things that match that clue, then name one extra thing the whole set has in common.

**2. Educational Purpose (KUD)**

- **K (Know):** Objects can share visible features such as color, shape, material, or category; a collection rule tells why things belong together; examples are pieces of evidence.
- **U (Understand):** Form helps us notice what things are like. Connection helps us explain why different things can belong in one group.
- **D (Do):** Find three matching examples, describe photo evidence, and explain one shared rule.

**3. Design Highlight**

The activity turns an ordinary scavenger hunt into a "shared clue" quest. Each photo gets a dramatic match check, a stable slot, and a visible connection line back to the starter object. The final magic moment asks the child to name a second connection, so the collection becomes an explained evidence web rather than a list of objects.

**4. Typical Scenario**

Child photographs a round blue ball; the AI chooses the clue "round," and the child hunts for three more round things nearby. If one find is only "maybe" round, it can sit beside the trail while the main three-slot progress stays intact.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Transition Bridge

**AI says:** [bright noticing tone] "Whoa, this `{starter_entity}` has a clue! The clue is `{shared_feature}`. It feels like a treasure map. What else has that clue?"

**Child responses:**

1. (Ideal) "I can find one!" / "That cup is round too!"
2. (Unexpected) "I like this one best." / "It is mine."
3. (No response) Child looks at the starter photo or around the room.

**AI follow-up:**

1. [excited scout tone] "Yes! Your clue eyes are awake. Let's find three matching things."
2. [warmly validating] "It is special. Special things start good missions. Let's find its shared clue."
3. [wait 2s] [gentle invitation] "Let's look together. Is it color, shape, or kind?"

**Screen:** The starter photo fills the center. A glowing outline highlights the runtime-selected clue area. A small compass appears with the label "Shared clue: `{shared_feature}`" and three empty photo slots underneath.

#### Step 2: Mission Briefing -- Shared Clue Scout

**AI says:** [adventurous guide tone] "You are the Shared Clue Scout. Find three things with `{shared_feature}`. Snap each matching thing. I will check the clue."

**Child responses:**

1. (Ideal) "Ready!" / "I know one!"
2. (Unexpected) "Can I pick a different clue?" / "What counts?"
3. (No response) Child hesitates before moving.

**AI follow-up:**

1. [cheering] "Mission starts now. Find your first match. Then take its picture."
2. [flexible and clear] "You can choose with me. Same color, shape, or kind? Pick one clue. Then we hunt for three."
3. [wait 2s] [helpful whisper] "Try the floor or shelf. Check a table or toy bin. A clue may hide nearby."

**Screen:** A mission card slides in: "Find 3 things with `{shared_feature}`." The starter photo sits at the left as "Example 0." Three empty numbered slots pulse softly. A trail line waits to connect the slots.

#### Step 3: Multi-Round Exploration

**Round 1 -- First Matching Find:**

**AI says:** [curious scout tone] "First photo is in. Let me check the shared clue. Does this one match `{shared_feature}`?"

**Child responses:**

1. (Ideal) "Yes, it matches!" / "It has the same shape!"
2. (Unexpected) "It is different." / "I just like it."
3. (No response) Child waits for the AI verdict.

**AI follow-up:**

1. [triumphant] "Scout verdict: MATCH! I can see the clue. Find 1 of 3. What should we call it?"
2. [kind redirect] "It is a cool find. This mission needs the shared clue. Does any part show `{shared_feature}`?"
3. [wait 2s] [soft thinking tone] "I am checking slowly. If you see it, point. Or say the matching part."

**Screen:** The first photo slides into slot 1. A green "MATCH" stamp appears if the clue fits; otherwise a yellow "Maybe" stamp appears with a loop arrow back to the hunt. The trail counter reads "1 of 3" when accepted.

**Round 2 -- Second Matching Find:**

**AI says:** [playful detective tone] "Second scout photo! I need the same clue: `{shared_feature}`. Is it hiding here too?"

**Child responses:**

1. (Ideal) "Yes!" / "It is the same color."
2. (Unexpected) "It is bigger." / "This one is funny."
3. (No response) Child holds the device quietly.

**AI follow-up:**

1. [delighted] "Another match! Your trail is stronger. Find 2 of 3."
2. [validating then focusing] "Bigger is a good detail. Now check the mission clue. Does it share `{shared_feature}`?"
3. [wait 2s] [gentle clue tone] "Look from edge to edge. Same color? Same shape? Same kind? Name the matching part."

**Screen:** Slot 2 fills with the new photo. The trail line connects slot 1 to slot 2 with a dotted glow. A small "same clue?" magnifier bounces over both photos.

**Round 3 -- Final Matching Find:**

**AI says:** [building suspense] "Final scout photo! If it matches `{shared_feature}`, the trail is complete. Ready for the clue check?"

**Child responses:**

1. (Ideal) "Ready!" / "It matches!"
2. (Unexpected) "I cannot find one." / "Nothing matches."
3. (No response) Child keeps searching or looks unsure.

**AI follow-up:**

1. [celebration burst] "Clue check complete: MATCH! Find 3 of 3. Your trail is full."
2. [reassuring search coach] "That is okay. Shared clues can hide. Look for tiny matches. Try one spot, corner, or group."
3. [wait 2s] [calm guide tone] "Let's search one small place. Try the table, couch, or shoes. One matching clue is enough."

**Screen:** Slot 3 waits with a shimmering border. When accepted, all three slots light up in order, and the starter photo sends a glowing line to each find. The counter flips from "2 of 3" to "3 of 3."

**Round 3 helper branch -- Not a match yet:**

**AI says:** [friendly redirect tone] "This photo is interesting. I do not see our clue yet. It may fit another quest."

**Child responses:**

1. (Ideal) "I will find another." / "This has a little match."
2. (Unexpected) "I want this one." / "It should count."
3. (No response) Child looks disappointed.

**AI follow-up:**

1. [encouraging] "Good scout choice. Show me the matching part. If not, take one more photo."
2. [respectful and flexible] "You are the scout. We can count it. First, name the shared clue."
3. [wait 2s] [soft reset tone] "No problem. The quest is still open. Look for color, shape, or kind."

**Screen:** The photo rests beside the trail in a "maybe pile" with a yellow question mark. The three main slots stay stable so the child can continue without losing progress.

#### Step 4: Magic Moment -- Name the Hidden Connection

**AI says:** [wonder-filled reveal tone] "Quest complete, Shared Clue Scout! Look at all four photos. They all match `{shared_feature}`. Now find one more connection."

**Child responses:**

1. (Ideal) "They are all toys." / "They all roll." / "They are all on the floor."
2. (Unexpected) "This one is my favorite." / "They are different."
3. (No response) Child looks at the completed trail.

**AI follow-up:**

1. [impressed] "Yes! That is another connection. First clue: `{shared_feature}`. Extra connection: `{extra_connection}`. Strong scout thinking."
2. [validating and extending] "They are different, yes. Different things can share clues. Same color, shape, place, or kind?"
3. [wait 2s] [gentle multiple-choice tone] "I see one connection. You found them today. Do you see another one?"

**Screen:** The photos arrange into a web. The first connection label reads "`{shared_feature}`." A second blank ribbon appears, then fills with "`{extra_connection}`" or "found today" if the child needs help.

#### Step 5: Closing + IB Concepts

**AI says:** [warm celebration] "You did it, Shared Clue Scout. You used Form today. You noticed what things were like. You used Connection too. You found why they belong together."

**Child responses:**

1. (Ideal) "I want another clue!" / "I did it!"
2. (Unexpected) "Can I keep looking?" / "I found four."
3. (No response) Child watches the badge screen.

**AI follow-up:**

1. [proud guide tone] "Your clue eyes are strong. Next time, try two clues."
2. [delighted] "More finds make bigger evidence. Keep scouting after the badge shines."
3. [wait 2s] [soft goodbye tone] "Your Shared Clue badge is saved. You found a hidden rule."

**Screen:** A "Shared Clue Scout" badge appears with three photo insets. The words "Form" and "Connection" glow as two paths on a small map. A next-step card says, "Next: try two clues at once."
