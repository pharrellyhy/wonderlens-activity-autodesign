# Phoneme Treasure Hunt

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Phoneme Treasure Hunt |
| Activity Category | cat5 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form, Connection |
| Related Concepts | evidence, choice, sequence, reflection |
| ATL Skills Focus | evidence collection, observation, language expression |
| Experience Pillar | Adventure |
| Game Style | quest_collector |

### B. Activity Overview

**1. Brief Description**

The first photo sets the target starting character. WonderLens recognizes and normalizes that object name, then accepts later finds only when their recognized names start with the same first character.

**2. Educational Purpose (KUD)**

- **K (Know):** Words can share the same starting character.
- **U (Understand):** The photo is evidence, and the normalized object name is what proves the starting character.
- **D (Do):** The child collects three object names that start with the same character and explains the shared form.

**3. Runtime Fidelity Notes**

WonderLens AI should preserve `photo_id`, run vision recognition, normalize the object label to a simple object name, and use the first recognized in-activity photo to seed the target first character. Later photos advance only when their recognized names start with that saved character. If recognition cannot produce a usable name or the name starts with a different character, ask the child to try another photo.

**4. Typical Scenario**

A child first photographs an object such as a car. WonderLens normalizes the name to "car," saves C as the target, and then asks for more objects whose recognized names start with C.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Rules

**Runtime AI instruction:** Say only that the first photo sets a starting letter and later names must match it. Do not ask for a photo here.

**Example AI line:** "The first photo sets our starting letter. Then we find two more names that start the same way."

**Child responses:**

1. (Ideal) The child understands the first-letter rule or repeats that the first recognized name sets the starting letter.
2. (Unexpected) The child asks for credit without a photo, wants to skip recognition, or changes the rule away from same starting characters.
3. (No response) The child looks at the first-letter rule without responding.

**AI follow-up:**

1. Restate the photo-recognize-check loop as the rule for the upcoming rounds.
2. Explain that WonderLens needs a recognized object name before it can set the letter, without counting any response yet.
3. [wait 2s] Model "cup starts with C after I recognize cup" as a rule example, then continue to Round 1.

**Screen:** Shows the first-letter rule and empty collection markers. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Multi-Round Core Loop

**Round 1 -- Seed Letter Treasure:**

**Runtime AI instruction:** Ask for one clear photo so WonderLens can name the object and save its first letter. Say letter, not sound.

**Example AI line:** "Take one photo. I will name the object and save its first letter for our hunt."

**Child responses:**

1. (Ideal) The child takes a photo that vision recognizes as a clear object and the runtime stores that object's first starting character.
2. (Unexpected) Vision returns no recognizable object or an over-specific name that needs normalization before judging.
3. (No response) The child scans the objects but does not take a photo yet.

**AI follow-up:**

1. Name the normalized object, save its first character with the `photo_id`, and light the first marker.
2. Explain the recognized name and ask for another seed photo if the object cannot be recognized.
3. [wait 2s] Give one clear object example, then ask the child to take one seed photo.

**Screen:** Shows the first collection marker, seed photo prompt, and the saved first letter after recognition. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Same Letter Treasure:**

**Runtime AI instruction:** Ask for another photo of an object whose name starts with the saved letter. Say letter, not sound.

**Example AI line:** "We saved our first letter. What else can you photograph that starts the same way?"

**Child responses:**

1. (Ideal) The child takes a second photo whose recognized object name starts with the saved first character.
2. (Unexpected) Vision returns an item with a different first character, cannot recognize the object, or the child changes the same-letter rule.
3. (No response) The child watches the second marker without taking another photo yet.

**AI follow-up:**

1. Confirm the matching first character, save the second normalized object name with `photo_id`, and compare it to the seed word.
2. Restate that the recognized name must start with the saved character and ask for another photo.
3. [wait 2s] Repeat the saved character and ask for one second same-letter photo.

**Screen:** Shows two collection markers and the saved seed word/letter when available. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- Same Letter Recap:**

**Runtime AI instruction:** Ask for one final photo of an object whose name starts with the saved letter. Say letter, not sound.

**Example AI line:** "One last same-letter treasure. Take one more photo, and I will check the object name."

**Child responses:**

1. (Ideal) The child takes a final photo whose recognized object name starts with the saved first character.
2. (Unexpected) Vision returns a name with a different first character, no recognizable object, or a name that cannot be normalized confidently.
3. (No response) The child watches the final marker without taking the final photo yet.

**AI follow-up:**

1. Save the final normalized same-letter word with `photo_id`, name the shared starting character, and prepare the recap.
2. Explain the recognized name and guide one retry using the saved first character.
3. [wait 2s] Repeat the saved first character and ask the child to take one final same-letter photo.

**Screen:** Shows the full three-marker collection and the same-letter recap area. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Magic Moment

**Runtime AI instruction:** Recap the three object names and their shared starting letter. Say letter, not sound.

**Example AI line:** "You collected three letter treasures. They connect because each name starts the same way."

**Child responses:**

1. (Ideal) The child notices the shared starting character or names a favorite saved word.
2. (Unexpected) The child focuses only on the pictures and misses that the object names share the same first character.
3. (No response) The child watches the same-letter treasure reveal without commenting.

**AI follow-up:**

1. Repeat the child words and emphasize the shared starting character.
2. Point from picture to object name, then ask which saved name starts the same way.
3. [wait 2s] Read the saved words aloud and offer two favorite choices.

**Screen:** Shows the Letter Treasure Hunter badge and saved same-letter words. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Closing + IB Concepts

**Runtime AI instruction:** Close by naming the pattern: each collected object name starts with the same letter, not sound.

**Example AI line:** "Today you practiced Form and Connection by finding names that start the same way."

**Child responses:**

1. (Ideal) The child repeats a saved word, asks to play again, or notices the shared starting character.
2. (Unexpected) The child shifts topic before the recap names the same-letter pattern.
3. (No response) The child stays on the recap badge without responding.

**AI follow-up:**

1. Offer a next-time hunt seeded by a different first photo.
2. Close Phoneme Treasure Hunt first, then offer one new seed-letter round for later.
3. [wait 2s] Read the badge in one sentence and end with one warm next-time invitation.

**Screen:** Recap badge lists title, Form, Connection, and the saved same-letter words. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
