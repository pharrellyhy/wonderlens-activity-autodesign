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

The AI introduces the beginning /b/ sound. The child takes a photo, WonderLens recognizes and normalizes the object name, and WonderLens accepts the find only when the normalized name begins with /b/.

**2. Educational Purpose (KUD)**

- **K (Know):** Words can share the same beginning sound.
- **U (Understand):** The photo is evidence, and the normalized object name is what proves the beginning sound.
- **D (Do):** The child collects three B-starting object names and explains the shared sound.

**3. Runtime Fidelity Notes**

WonderLens AI should preserve `photo_id`, run vision recognition, normalize the object label to a simple object name, then judge the beginning sound. If recognition returns a non-B name or cannot normalize the object, ask the child to try another photo.

**4. Typical Scenario**

A child photographs an object such as a ball, book, banana, or basket. WonderLens normalizes names such as "picture book" to "book" before judging the /b/ start.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Open Phoneme Treasure Hunt, name the child as a Sound Treasure Hunter, introduce letter B as the target beginning sound, and ask if they are ready to take a photo of a B object.

**Example AI line:** "Today our sound is B. Can you take a photo of something whose name starts with B?"

**Child responses:**

1. (Ideal) The child accepts the Sound Treasure Hunter role or names a possible B object.
2. (Unexpected) The child names a non-B object, wants a different game, or treats the picture alone as enough evidence.
3. (No response) The child watches the B treasure prompt without choosing yet.

**AI follow-up:**

1. Confirm the B sound mission and preview the first photo capture.
2. Acknowledge briefly, restate that the object name must begin with B, and offer ball or book as examples.
3. [wait 2s] Say "ball starts with B," then ask the child to take one B photo.

**Screen:** Shows the Phoneme Treasure Hunt title and three empty treasure markers. Optional support asset: `intro_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 2: Role And Rules

**Runtime AI instruction:** Explain that each turn saves one `photo_id`, uses vision to recognize and normalize the object name, then judges whether the normalized name begins with /b/.

**Example AI line:** "Rule: you take one photo, I name the object, and we save it when the name starts with B."

**Child responses:**

1. (Ideal) The child agrees to take a photo for the B sound check.
2. (Unexpected) The child takes a non-B photo, asks for credit without a photo, or wants to skip recognition.
3. (No response) The child looks at the B rule without starting the first turn.

**AI follow-up:**

1. Restate the photo-recognize-check loop and invite the first object.
2. Contrast one non-B example with one B example, and invite a safer B photo.
3. [wait 2s] Model "book begins with B" and ask for one photo of a B object.

**Screen:** Shows the B rule and empty collection markers. Optional support asset: `rules_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 3: Multi-Round Core Loop

**Round 1 -- First B Treasure:**

**Runtime AI instruction:** Ask for the first real camera photo, preserve `photo_id`, normalize the recognized object name, and accept only a beginning /b/ sound.

**Example AI line:** "Take one photo. I will name the object and check whether it starts with B."

**Child responses:**

1. (Ideal) The child takes a photo that vision normalizes to a B-starting object, such as ball or book.
2. (Unexpected) Vision returns a non-B object, no recognizable object, or an over-specific name that needs normalization before judging.
3. (No response) The child scans the objects but does not take a photo yet.

**AI follow-up:**

1. Name the normalized B-starting object, save it with the `photo_id`, and light the first marker.
2. Keep the B rule visible, explain the recognized name, and ask for another photo if it does not start with B.
3. [wait 2s] Give one B example, then ask the child to take one B photo.

**Screen:** Shows the first collection marker, B photo prompt, and simple B examples. Optional support asset: `round_1_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 2 -- Second B Treasure:**

**Runtime AI instruction:** Ask for a second real camera photo, compare the normalized object name to the first saved B word, and accept only a beginning /b/ sound.

**Example AI line:** "We saved one B word. What is another thing whose name starts with B?"

**Child responses:**

1. (Ideal) The child takes a second photo that vision normalizes to a B-starting object.
2. (Unexpected) Vision returns a non-B item, cannot recognize the object, or the child changes the rule away from beginning B.
3. (No response) The child watches the second marker without taking another photo yet.

**AI follow-up:**

1. Confirm the matching beginning sound, save the second normalized object name with `photo_id`, and compare it to the first B word.
2. Restate that the recognized name must start with B and ask for another photo, offering banana or basket as examples.
3. [wait 2s] Say "banana begins with B," then ask for one second B photo.

**Screen:** Shows two collection markers and the saved first B word when available. Optional support asset: `round_2_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

**Round 3 -- B Treasure Recap:**

**Runtime AI instruction:** Ask for the final real camera photo, normalize the object name, then prepare to recap all saved beginning-B words.

**Example AI line:** "One last B treasure. Take one more photo, and I will check the object name."

**Child responses:**

1. (Ideal) The child takes a final photo that vision normalizes to a B-starting object.
2. (Unexpected) Vision returns a non-B name, no recognizable object, or a name that cannot be normalized confidently.
3. (No response) The child watches the final marker without taking the final photo yet.

**AI follow-up:**

1. Save the final normalized B word with `photo_id`, name the shared beginning sound, and prepare the recap.
2. Explain the recognized name and guide one retry using a clear B example.
3. [wait 2s] Offer ball, book, banana, or basket and ask the child to take one final B photo.

**Screen:** Shows the full three-marker collection and the B recap area. Optional support asset: `round_3_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 4: Magic Moment

**Runtime AI instruction:** Recap the three saved object names, identify the shared /b/ beginning sound, and award Sound Treasure Hunter.

**Example AI line:** "You collected three B treasures. They connect because each name starts with B."

**Child responses:**

1. (Ideal) The child notices the shared B sound or names a favorite saved word.
2. (Unexpected) The child focuses only on the pictures and misses that the object names share a sound.
3. (No response) The child watches the B treasure reveal without commenting.

**AI follow-up:**

1. Repeat the child words and emphasize the shared beginning sound.
2. Point from picture to object name, then ask which saved name starts with B.
3. [wait 2s] Read the saved B words aloud and offer two favorite choices.

**Screen:** Shows the Sound Treasure Hunter badge and saved B words. Optional support asset: `celebrate_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Close by naming Form and Connection: the form is the beginning sound, and the connection is that the collected names start with B.

**Example AI line:** "Today you practiced Form and Connection by finding words that begin with B."

**Child responses:**

1. (Ideal) The child repeats a B word, asks to play again, or notices the shared sound.
2. (Unexpected) The child shifts topic before the recap names the B sound pattern.
3. (No response) The child stays on the recap badge without responding.

**AI follow-up:**

1. Offer a next-time sound hunt with a new beginning sound.
2. Close Phoneme Treasure Hunt first, then offer one new letter for later.
3. [wait 2s] Read the badge in one sentence and end with one warm next-time invitation.

**Screen:** Recap badge lists title, Form, Connection, and the saved B words. Optional support asset: `closing_scene`. If unavailable, continue with spoken guidance and do not claim the image is visible.
