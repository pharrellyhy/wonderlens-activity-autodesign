## Asset Pipeline Smoke

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Asset Pipeline Smoke |
| Activity Category | 5 -- Collection/Tracking Exploration (Out-of-Device, Solo) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | Form and Connection |
| Related Concepts | Texture, Pattern, Evidence, Source |
| ATL Skills Focus | Research Skills (observation, evidence collection), Communication Skills (describing), Thinking Skills (matching) |
| Experience Pillar | Discovery |
| Game Style | scavenger_hunt |

### B. Activity Overview

**1. Brief Description**

The child sees a soft generated `moss_token`, then uses the real camera to collect one nearby moss-like clue: something green, fuzzy, soft-looking, leafy, or bumpy. When the child captures and describes the real-world clue, the token is collected and the accurate `orion_card` opens as the reward.

**2. Educational Purpose (KUD)**

- **K (Know):** Real objects and screen tokens can share visible features such as color, texture, or pattern; reference cards should keep their source layout.
- **U (Understand):** Form helps us notice what something looks like. Connection helps us explain why a real-world find matches a guide token.
- **D (Do):** Look for a real matching clue, capture it, describe one visible detail, and notice one detail on the accurate Orion card.

**3. Design Highlight**

This smoke activity keeps the Cat5 loop intentionally small: one generated guide token, one real camera collection, and one reference-bound reward card. That lets importer tests verify the same package-local runtime assets while still exercising the out-of-device photo collection contract.

**4. Typical Scenario**

The child sees the moss token, points the camera at a patch of moss, a green plant, or a fuzzy green fabric nearby, then says "green" or "fuzzy." The system accepts the photo as the one smoke collection item and opens the Orion reward card.

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1: Moss Explorer Mission

**Runtime AI instruction:** Invite the child into a short real-world moss-clue hunt and explain that one camera capture will collect the token and open the star-card reward.

**Example AI line:** [warm] "Tiny explorer, this moss token is our guide. Find one real thing nearby that shares a clue with it."

**Child responses:**

1. (Ideal) Child agrees, looks around, or says they can find one.
2. (Unexpected) Child asks for the star card first, wants a different game, or says they do not know what to find.
3. (No response) Child stays quiet or only looks at the device.

**AI follow-up policy:**

1. (Ideal) [bright] "Great. Look for one green, fuzzy, leafy, or bumpy clue."
2. (Unexpected) [validate then focus] "The star card is exciting. First we need one real moss clue, then it opens."
3. (No response) [wait 2s] [model] "I'll help. We can look for something green or soft-looking."

**Photo capture timing:** No new photo is required before Step 1. The child should capture one real-world clue after Step 2.

**Screen/state:** Show the empty single-slot collection tray. Keep the round screen ready to display `moss_token`.

#### Step 2: Show The Moss Guide Token

**Runtime AI instruction:** Display `moss_token` as the guide image and ask the child to choose one clue to hunt for in the real world.

**Example AI line:** [curious] "Here is the moss token. Which clue should we hunt for: green, fuzzy, leafy, or bumpy?"

**Child responses:**

1. (Ideal) Child chooses a visible clue such as green, fuzzy, leafy, soft, round, or bumpy.
2. (Unexpected) Child names Orion, says a random object, or chooses a clue not visible on the token.
3. (No response) Child stays quiet after the token appears.

**AI follow-up policy:**

1. (Ideal) [validate] "Good clue. Now find one real thing that shows that clue."
2. (Unexpected) [validate then redirect] "That is a fun idea. For this token, choose a clue we can see: green, fuzzy, leafy, or bumpy."
3. (No response) [wait 2s] [scaffold] "Let's use green. Find one real green thing nearby and take its picture."

**Photo capture timing:** The camera capture should happen after this follow-up and before Step 3. The capture target is one real-world object or texture that shares the chosen moss-token clue.

**Screen/state:** Show `moss_token` centered in the round screen. Show one empty slot labeled "Real clue photo."

#### Step 3: Collect One Real Moss-Clue Photo

**Runtime AI instruction:** React to the captured photo and ask the child to name the matching clue. Accept one visible or child-confirmed match as the single Cat5 smoke collection.

**Example AI line:** [playful scout tone] "Your photo is in. What clue makes it match our moss token?"

**Child responses:**

1. (Ideal) Child says a matching clue, such as "green," "fuzzy," "leafy," "soft," or points to the matching part in the photo.
2. (Unexpected) Child says it does not match, wants to count an unrelated object, or asks to skip the photo.
3. (No response) Child waits while the photo is visible.

**AI follow-up policy:**

1. (Ideal) [celebrate] "Collected. Your real clue matches the moss token."
2. (Unexpected) [validate then repair] "It is okay if this one feels different. Show me any green, fuzzy, leafy, or bumpy part, or take one more photo."
3. (No response) [wait 2s] [offer choice] "I can help check. Is the matching clue green, fuzzy, leafy, or bumpy?"

**Photo capture timing:** The real-world collection photo has already been captured after Step 2 and before this Step 3 prompt. If the child needs a retry, the new capture happens after the unexpected follow-up and loops back to this Step 3 check.

**Screen/state:** Show the captured real-world photo in the collection slot beside the small `moss_token`. When accepted, stamp the slot "Collected" and move the token into a collected state.

#### Step 4: Open The Orion Reward Card

**Runtime AI instruction:** Reveal `orion_card` as the reward and ask one simple visual clue question without adding extra stars or unverified facts.

**Example AI line:** [wonder] "The accurate Orion card opened. Do you see a line of bright stars or a cluster of stars?"

**Child responses:**

1. (Ideal) Child names a visible pattern, such as line, cluster, stars, or points at the card.
2. (Unexpected) Child calls the card moss, asks to redraw it, or invents a pretend constellation.
3. (No response) Child looks silently at the card.

**AI follow-up policy:**

1. (Ideal) [validate] "Yes. We are looking at the real card pattern, so we keep those star positions the same."
2. (Unexpected) [validate then anchor] "Pretend stars are fun. This reward is the accurate Orion card, so we notice the stars already on it."
3. (No response) [wait 2s] [model] "I notice bright stars making a pattern. You can point to one bright part."

**Photo capture timing:** No new photo capture happens in Step 4. This step uses the already accepted collection photo and the package-local reference-bound card.

**Screen/state:** Keep the collected real-world photo as a small slot thumbnail. Show `orion_card` centered in the round screen.

#### Step 5: Close The Smoke Round

**Runtime AI instruction:** Recap the real photo collection, the generated moss guide token, and the source-faithful Orion card, then end cleanly.

**Example AI line:** [warm] "You collected one real clue for the moss token and opened the Orion card. One real-world find led to one star reward."

**Child responses:**

1. (Ideal) Child repeats moss, Orion, stars, green, fuzzy, or says goodbye.
2. (Unexpected) Child asks for more rounds or wants a different picture.
3. (No response) Child is quiet at the end.

**AI follow-up policy:**

1. (Ideal) [close] "Explorer round complete."
2. (Unexpected) [validate then boundary] "More rounds would be fun. This smoke round has one real photo and one reward card, so we stop here."
3. (No response) [wait 2s] [gentle close] "I'll save our tiny explorer win."

**Photo capture timing:** No new photo capture happens in Step 5.

**Screen/state:** Show a compact completion state with the accepted real-world photo thumbnail, collected `moss_token`, and `orion_card` thumbnail. No new assets appear.
