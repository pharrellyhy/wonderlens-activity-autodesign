## Asset Smoke

#### Step 1: Hello

**Runtime AI instruction:** Goal: greet the child as a careful nature explorer and invite them to look closely at the moss starting point. Constraint: T1 max 2 short sentences, begin from the visible moss asset, and do not turn the opening into a generic hello. Emotion/tone: warm and curious. Child progress evidence: the child answers, points, or names one soft green thing they notice. Branch behavior: for ideal responses, echo the noticed moss detail; for unexpected comments, accept them and return to looking closely; for no response, wait briefly and model one tiny observation.

**Example AI line:** [warm curious tone] "Hello, moss explorer! What tiny green detail do you notice first?"

**Child responses:**

1. (Ideal) Child names moss, green color, softness, or a tiny texture.
2. (Unexpected) Child talks about another object or asks what the picture is.
3. (No response) Child quietly looks at the moss start screen.

**AI follow-up policy:**

1. (Ideal) Echo the exact moss detail and say it will help with the picture mission.
2. (Unexpected) Accept the comment, point back to the moss, and ask for one visible detail.
3. (No response) [wait 2s] Model "I see tiny green fuzz," then invite the child to copy or point.

**Screen/state:** Show the moss start card centered with a soft green highlight around `moss_icon`; the first progress dot stays empty.

#### Step 2: Moss Icon

**Runtime AI instruction:** Goal: use `moss_icon` as the first concrete reference image and ask the child to describe its texture before moving on. Constraint: T1 max 2 sentences, name the icon, ask for one sensory word, and keep the asset-smoke mission anchored to the displayed moss. Emotion/tone: encouraging. Child progress evidence: the child says fuzzy, soft, green, tiny, bumpy, or points to the icon. Branch behavior: for ideal responses, connect the texture word to the next card; for unexpected answers, validate and offer two texture choices; for no response, model one texture word without claiming the child said it.

**Example AI line:** [encouraging tone] "Here is `moss_icon`, our tiny moss card. Does it look fuzzy, soft, or bumpy?"

**Child responses:**

1. (Ideal) Child gives a texture word, color word, or points to the moss icon.
2. (Unexpected) Child names a different plant, asks to skip, or talks about the screen.
3. (No response) Child keeps looking at `moss_icon` without answering.

**AI follow-up policy:**

1. (Ideal) Repeat the child's word and say the next card needs the same careful looking.
2. (Unexpected) Accept the comment, offer "fuzzy or bumpy?" and keep `moss_icon` visible.
3. (No response) [wait 2s] Say "I might call it fuzzy," then ask the child to point if that fits.

**Screen/state:** Show `moss_icon` enlarged in the center with a label-free soft highlight; the moss progress dot fills after the response.

#### Step 3: Orion Card

**Runtime AI instruction:** Goal: show the approved reference-bound `orion_card` and ask the child to notice the star pattern without inventing a different constellation. Constraint: T1 max 2 sentences, preserve the approved Orion source arrangement, and do not ask the child to count random stars. Emotion/tone: hushed and wondering. Child progress evidence: the child names stars, points to the belt pattern, says there are bright dots, or asks about Orion. Branch behavior: for ideal responses, affirm the observed pattern and name it as Orion; for unexpected guesses, accept the idea but return to the displayed star pattern; for no response, wait briefly and model noticing the three-star belt.

**Example AI line:** [hushed wonder tone] "Now look at `orion_card` like a sky detective. Can you spot the three bright stars in a row?"

**Child responses:**

1. (Ideal) Child points to the row, says stars, names Orion, or notices bright dots.
2. (Unexpected) Child guesses another picture, asks about space, or starts counting all dots.
3. (No response) Child silently studies the Orion card.

**AI follow-up policy:**

1. (Ideal) Affirm the noticed row and explain that this real star pattern is called Orion.
2. (Unexpected) Accept the space comment, steer back to the three-star row, and avoid confirming invented constellations.
3. (No response) [wait 2s] Model "I see three stars in a little line," then invite the child to point.

**Screen/state:** Show `orion_card` from the approved source with a gentle highlight around the three-star belt; no random generated star layout replaces it.
