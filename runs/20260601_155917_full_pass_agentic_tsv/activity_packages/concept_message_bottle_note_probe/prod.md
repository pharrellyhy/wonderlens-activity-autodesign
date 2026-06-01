## Message Bottle Note

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Message Bottle Note |
| Activity Category | cat3 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Responsibility |
| Related Concepts | kindness, message, care, expression |
| ATL Skills Focus | empathy, communication, fine-motor expression |
| Experience Pillar | Nurture |
| Game Style | care_station |

### B. Activity Overview

**1. Brief Description**

The child uses a photographed object or chosen inspiration to make a warm paper note. The AI tells a tiny story, helps the child choose a word or drawing, asks the child to write or draw with paper and pencil, and suggests placing the note for a parent or friend.

**2. Educational Purpose (KUD)**

- **K (Know):** A note can carry kindness through simple words, marks, or drawings.
- **U (Understand):** Caring can be shown by making something real and placing it where another person will find it.
- **D (Do):** Choose a recipient, choose words or a drawing, physically make the note, place it or plan its placement, and confirm completion without handwriting/OCR assessment.

**3. Design Highlight**

The photographed object is a story seed, not a writing-recognition task. The runtime must ask the child or caregiver what the note says or shows and must never claim to read handwriting from the photo.

**4. Typical Scenario**

The child photographs a toy, shell, flower, cup, or other small inspiration. The AI imagines it carrying a kind message, then the child draws a heart or writes a short note and places it on a pillow, desk, or in a school bag.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: Open from the child's photographed object or chosen inspiration and turn it into a warm "message bottle" story seed for a real paper note. Constraint: T1, 2-3 short sentences; no OCR, no handwriting claims, and do not require the AI to identify the photo beyond child/caregiver confirmation. Tone: tender and imaginative. Progress evidence: child confirms the inspiration object, names a recipient, or agrees to make a note. Branch behavior: if correct, reflect the named object/recipient and preview drawing or words; if wrong/off-topic, accept the idea and return to "one kind note for someone"; if help/silence, offer parent/friend and heart/smile choices, with a graceful exit after repeated silence. Frame/source guardrail: source frame is photographed-inspiration -> story -> physical note -> placement; screen shows inspiration card, paper/pencil checklist, and empty note tokens.

**Example AI line:** "Your photo can be our tiny message bottle. Who should this little kindness note sail to: a parent, a friend, or someone else?"

**Child responses:**

1. (Ideal) The child says "Mom," "friend," "Dad," "teacher," names the object, or agrees to write/draw.
2. (Unexpected) Child asks the AI to read the note, wants only to say kind words, or changes to a non-note game.
3. (No response) Child watches the inspiration card and materials checklist.

**AI follow-up:**

1. Save the recipient token and connect the object to a warm one-sentence story.
2. Clarify: "I cannot read handwriting here, but you can tell me what you draw or write."
3. [wait 2s] Offer "parent or friend?" and "heart or smile?" then allow a spoken-only plan if materials are not ready.

**Screen:** Shows the photo/chosen inspiration card, recipient token, and material chips: paper, pencil/crayon, place to leave note.

#### Step 2: Role And Rules

**Runtime AI instruction:** Goal: Set the physical-material rule: the child will choose a tiny message, draw/write it on paper, then place it for the recipient. Constraint: T1, 2-3 short sentences; require child/caregiver confirmation instead of visual/OCR verification; support drawing for pre-writers. Tone: caring and practical. Progress evidence: child has or confirms paper/pencil and chooses word/drawing mode. Branch behavior: if correct, move into message choice; if wrong/unsafe, pause for caregiver/material setup; if help/silence, offer drawing a heart as the smallest action and exit if materials are unavailable. Frame/source guardrail: do not reduce to verbal kindness only; screen stays on real-note checklist and placement map.

**Example AI line:** "Our rule is real and tiny: choose one kind word or drawing, put it on paper, then hide or place it where your person can find it."

**Child responses:**

1. (Ideal) The child confirms paper/pencil, says they will draw, or chooses a simple word.
2. (Unexpected) Child has no materials, asks the AI to send the message digitally, or wants the AI to judge handwriting.
3. (No response) Child does not confirm materials or message mode.

**AI follow-up:**

1. Save "materials ready" and ask for one word/drawing.
2. Gate honestly: "We need paper and something to draw with. Ask a grown-up, or we can save this idea for later."
3. [wait 2s] Model "a heart is enough," then offer to stop with a saved idea if no response.

**Screen:** Checklist marks Inspiration, Recipient, Materials, Message, Placement. No camera/OCR success state is shown.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Warm Story From The Object:**

**Runtime AI instruction:** Goal: Tell a brief warm story inspired by the photographed/chosen object and ask what kind feeling the note should carry. Constraint: T1, 2-3 short sentences; use child-confirmed object name if available, otherwise say "your photo treasure." Tone: cozy and storybook-like. Progress evidence: child chooses a feeling such as love, thanks, miss you, good luck, or a smile. Branch behavior: if correct, turn the feeling into a note idea; if wrong/off-topic, gently return to what the object might want to say; if help/silence, offer two feelings and proceed with one child-approved choice. Frame/source guardrail: photographed inspiration must remain the story seed; screen shows object -> feeling -> note flow.

**Example AI line:** "Maybe this little photo treasure found a secret: kind words can travel. Should your note carry love, thanks, or a big smile?"

**Child responses:**

1. (Ideal) The child says "love," "thank you," "I miss you," "smile," or points to a feeling choice.
2. (Unexpected) Child gives an unkind message, asks for a long letter, or talks only about the object category.
3. (No response) Child does not pick a feeling.

**AI follow-up:**

1. Save the feeling token and suggest a matching word/drawing.
2. Redirect to kindness: "Let's make a note that helps someone feel cared for."
3. [wait 2s] Offer "love or thank you?" and accept a point/nod.

**Screen:** Inspiration card remains visible; feeling buttons/chips show Love, Thanks, Smile, Good Luck.

**Round 2 -- Choose Words Or Drawing:**

**Runtime AI instruction:** Goal: Help the child choose exactly what to put on paper: one short phrase, one name, or one drawing such as a heart, sun, flower, or smile. Constraint: T1, 2-3 short sentences; do not ask the AI to inspect handwriting; child may speak the content for confirmation. Tone: reassuring and low-pressure. Progress evidence: child says or chooses the note content. Branch behavior: if correct, repeat the chosen content and move to making; if wrong/too complex, shrink it to one word or one drawing; if help/silence, offer "heart + I love you" or "smile + thank you" and allow caregiver confirmation. Frame/source guardrail: this is physical note planning, not digital message composition; screen shows selected content slot.

**Example AI line:** "Your note can be tiny: a heart, a smile, or the words 'thank you.' What do you want your paper to say or show?"

**Child responses:**

1. (Ideal) The child chooses a word, phrase, drawing, or says they will make a heart.
2. (Unexpected) Child asks the AI to spell a long message, wants the AI to verify spelling, or chooses inappropriate content.
3. (No response) Child does not choose content.

**AI follow-up:**

1. Save the exact child-spoken content as the message token.
2. Simplify and safeguard: "Let's keep it kind and short. A heart or 'thank you' works."
3. [wait 2s] Model "heart plus your name," then ask for yes/no.

**Screen:** Message slot fills with child-confirmed words/drawing description; no handwriting recognition state appears.

**Round 3 -- Make The Paper Note:**

**Runtime AI instruction:** Goal: Invite the child to physically write or draw the chosen content on paper and confirm when they are done. Constraint: T1, 2-3 short sentences; wait supportively, use child/caregiver "done" confirmation, and never grade neatness or read the paper. Tone: patient and encouraging. Progress evidence: child says done, caregiver confirms, or child describes what they drew/wrote. Branch behavior: if correct, celebrate the making process; if wrong/no materials, switch to saved plan and ask a grown-up for later; if help/silence, give one tiny action and then graceful early exit after two unproductive turns. Frame/source guardrail: required child action is physical writing/drawing; screen shows making timer/checklist, not OCR capture.

**Example AI line:** "Now make the real note on paper. Draw your heart or words, and when you are ready, tell me 'done.'"

**Child responses:**

1. (Ideal) The child says "done," describes the drawing, or caregiver confirms the note is made.
2. (Unexpected) Child asks if the AI can see/read it, says they only imagined it, or cannot access materials.
3. (No response) Child may be busy drawing or not engaging.

**AI follow-up:**

1. Save "paper note made" and avoid quality judgment.
2. Say: "I cannot read or grade it, but you can tell me what it says or shows."
3. [wait 4s] Say "take your time," then after another pause offer to save the idea and finish later.

**Screen:** Making state shows "Draw/write now" with a patient progress pulse and a "child/caregiver says done" confirmation button.

**Round 4 -- Place The Note:**

**Runtime AI instruction:** Goal: Help the child choose a real placement for the note, such as parent pillow, desk, lunch bag, school bag, or hand delivery to a friend. Constraint: T1, 2-3 short sentences; ask caregiver confirmation for placement safety/privacy; no claim that the AI tracks where it was placed. Tone: secret-helper excitement. Progress evidence: child chooses or confirms a placement. Branch behavior: if correct, save placement and prepare celebration; if wrong/unsafe, suggest a safer visible household spot with caregiver; if help/silence, offer pillow/desk/school bag choices and allow "give it by hand." Frame/source guardrail: the kindness action includes real placement, not just making the note; screen shows placement map/list.

**Example AI line:** "Where will your message bottle land: on a pillow, on a desk, or tucked safely in a school bag?"

**Child responses:**

1. (Ideal) The child chooses pillow, desk, school bag, hand delivery, or another safe place.
2. (Unexpected) Child chooses a private/unsafe spot, wants to hide it where it may be lost, or skips placement.
3. (No response) Child looks at placement choices without answering.

**AI follow-up:**

1. Save the placement token and ask for child/caregiver confirmation when placed or planned.
2. Redirect: "Let's choose a place your grown-up says is okay and your person can find."
3. [wait 2s] Offer two choices and accept a point or caregiver confirmation.

**Screen:** Placement choices appear; final token waits for "placed" or "planned" confirmation.

#### Step 4: Magic Moment

**Runtime AI instruction:** Goal: Celebrate the completed kindness chain: object inspiration, warm feeling, paper note, and real placement/plan. Constraint: T1, 2-3 short sentences; recap only child-confirmed content and do not infer written text from a photo. Tone: proud and gentle. Progress evidence: child confirms placed/planned note or repeats who it is for. Branch behavior: if correct, name the recipient and placement; if wrong/off-topic, recap the safe confirmed steps; if help/silence, close with "your idea is saved" rather than pushing more. Frame/source guardrail: payoff is physical care action; screen shows tokens Inspiration, Message, Made, Placed/Planned.

**Example AI line:** "Your tiny message traveled from a photo treasure to real paper. It is ready to make your person feel cared for."

**Child responses:**

1. (Ideal) The child says where it went, who will get it, or says "done."
2. (Unexpected) Child wants the AI to check spelling or read the note.
3. (No response) Child watches the completed kindness chain.

**AI follow-up:**

1. Celebrate the process and recipient without judging quality.
2. Repeat the no-OCR boundary: "You told me the message; that is our proof."
3. [wait 2s] Read the four tokens and move to closing.

**Screen:** Kindness chain board shows the inspiration card, child-confirmed message/drawing description, material confirmation, and placement.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Goal: Close by connecting Form to the note's form (word/drawing/place) and Responsibility to caring for someone else. Constraint: T1, 2 short sentences; include parent-reviewable recap based on child/caregiver confirmation. Tone: warm and complete. Progress evidence: child says goodbye, names recipient, or accepts badge. Branch behavior: if correct, echo recipient or placement; if wrong/off-topic, close the note activity first; if help/silence, end gracefully. Frame/source guardrail: closing must mention photographed inspiration, physical note, and placement/plan; screen shows no OCR or photo-grading claim.

**Example AI line:** "You used Form by making a real note, and Responsibility by choosing kindness for someone. Your note was inspired by your photo and placed or planned for your person."

**Child responses:**

1. (Ideal) The child names the recipient, says they placed it, or watches the badge.
2. (Unexpected) Child shifts topic before recap.
3. (No response) Child stays on the recap badge.

**AI follow-up:**

1. Offer next time: make another message bottle note from a new photo treasure.
2. Close the note activity first, then acknowledge the new topic.
3. [wait 2s] Read the badge and end.

**Screen:** Recap badge lists "Message Bottle Helper," mechanic `care`, focal attribute `message_bottle_note`, and next hint "photo treasure -> paper note -> kind place."
