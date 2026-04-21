## The Pattern Trail

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | The Pattern Trail |
| Activity Category | 5 -- Collection/Tracking Exploration (Out-of-Device, Solo, Indoor/Outdoor) |
| Recommended Tier | T1 (ages 4-6) |
| Core IB Key Concepts | **Form** (What is it like?) & **Connection** (How is it connected to other things?) |
| Related Concepts (Discipline) | Pattern, Similarity, Observation, Discovery |
| ATL Skills Focus | Research Skills (observation, data collection), Thinking Skills (critical thinking, transfer), Communication Skills (expressing reasoning) |
| Experience Pillar | Mystery |
| Game Style | mystery_trail |
| Trigger Entity | Any entity with detected {pattern} attribute |
| Trigger Scene | Child photographs any object where AI detects a visual pattern (e.g., a striped shirt, spotted ladybug, ribbed leaf, wavy fence) |
| Mapping Source | property-bridge |
| IB Theme | How the World Works |
| Design Version | 1.0 |
| Last Updated | 2026-04-08 |
| Template Parameters | `{pattern}` -- detected visual pattern property (e.g., stripes, spots, zigzags, lines, waves, dots, ridges). Example: **stripes** |

### A.1 Entity Attributes Covered

This template is **parameterized** (not bound to one entity). It matches any entity whose `tier_guidance` contains at least one of the attribute paths below. The property value (e.g., `{pattern}`) is extracted from the matched entity's YAML at runtime and substituted for the template parameter. See `program.md` §1.9 "Matcher semantics" for the dual-overlap rule.

```yaml
entity_attributes_covered:
  - tier_0.appearance.pattern                # e.g., raincoat
  - tier_1.appearance.wing_patterns          # e.g., butterfly
  - tier_1.appearance.key_pattern            # e.g., piano
  - tier_1.appearance.scale_shimmer_pattern  # e.g., goldfish
```

### B. Activity Overview

- **① Brief Description**: After the child photographs any object, the AI notices a visual pattern -- for example, "stripes." The AI marvels at the pattern and recruits the child as a "Pattern Detective." The AI gives riddle-clues one at a time -- each describing something nearby with a DIFFERENT kind of visual pattern -- and the child searches, guesses, and photographs what they think matches. After 3 finds, the AI reveals the hidden connection: everything the child found has a pattern, and patterns are EVERYWHERE -- in nature, in clothes, in buildings. This template works for any detected visual pattern: stripes, spots, zigzags, waves, dots, ridges, checks, swirls, etc.

- **② Educational Purpose (KUD)**:
  - **K (Know)**: Learn the vocabulary "pattern," "stripes," "spots," "zigzag," and "lines." Learn that patterns are repeating visual arrangements found everywhere.
  - **U (Understand)**: Understand that the Form of things includes visual patterns -- repeating shapes, lines, or marks. Understand that Connection exists between very different things that share the quality of having a pattern.
  - **D (Do)**: Practice deductive reasoning from riddle-clues, search for and photograph matching items, and articulate the hidden connection between all finds.

- **③ Design Highlight**: The "Pattern Trail" transforms a pattern hunt into a mystery investigation. The key mechanism is riddle-driven search with a delayed pattern reveal: the child doesn't know that ALL their finds share the quality of having a pattern until the end. Each riddle-clue describes a DIFFERENT pattern type (spots, zigzags, parallel lines), so the child experiences variety and surprise. The magic moment -- "WHOA! Everything you found has a PATTERN!" -- reframes the entire activity retroactively.

- **④ Typical Scenario**: Child photographs a striped shirt --> AI notices stripes --> "Your shirt has STRIPES!" --> recruits the child as a Pattern Detective --> riddle-clue #1 (something with spots) --> child searches and photographs --> riddle-clue #2 (something with zigzags) --> child searches and photographs --> riddle-clue #3 (something with parallel lines) --> child searches and photographs --> AI reveals: "WHOA! Everything you found has a PATTERN -- patterns are EVERYWHERE!"

### C. Interaction Flow

> Recommended Tier: T1 (ages 4-6)

#### Step 1b: Transition Bridge -- Cold Start

**Context**: Child photographs any object where AI detects a visual pattern. Example: a striped shirt.

**AI says:** *(breathless, delighted)* "Ohhh -- look at your shirt! Do you see those LINES going side by side? Those are called STRIPES! They go this way and that way, marching together like a team. Your shirt has a PATTERN! Have you ever noticed stripes on other things too?"

**Child responses:**

1. (Ideal) "Yeah, on a zebra!" / "My socks have stripes!" / "There are stripes everywhere!"
2. (Unexpected) "I like my shirt!" / "It's blue and white." / "My mom picked it."
3. (No response) Child looks at the shirt or the screen quietly.

**AI follow-up:**

1. (excited, conspiratorial) "YES! Zebras have stripes, socks have stripes -- stripes are sneaky, they show up EVERYWHERE! But here's the thing -- stripes aren't the ONLY pattern out there. There are spots, zigzags, wavy lines... I bet there are MORE patterns hiding all around you RIGHT NOW. What if we could find them?"
2. (warm, curious) "It IS a great shirt! And those blue and white lines? That's a PATTERN called stripes! But here's a secret -- your shirt isn't the only thing with a pattern. There are spots, zigzags, all kinds of patterns hiding nearby. Want to find them?"
3. (wait 2s) (gentle, wondering) "See those lines on your shirt? They repeat -- over and over -- side by side. That's a pattern called stripes! And I bet there are MORE patterns hiding all around you. I have an idea -- want to be a detective and find them?"

**Screen:** Trigger photo centered with animated highlight lines tracing the detected pattern. "STRIPES" in bold, striped-textured letters. Pulsing magnifying glass icon with "?" in the corner.

#### Step 2: Rule Introduction + Demo

**AI says:** *(adventurous, detective tone)* "Alright -- you are now an official Pattern Detective! Here's your mission: I'm going to give you riddle-clues about things hiding nearby. Each one has a DIFFERENT kind of pattern! You search, you guess, and you take a photo. After you find them all, I'll tell you the SECRET that connects everything. Ready, Detective?"

**Child responses:**

1. (Ideal) "Ready!" / "Yes!" / "What's the first clue?"
2. (Uncertain) "What's a pattern?" / "Where do I look?"
3. (No response) Child looks around with curiosity.

**AI follow-up:**

1. (thrilled) "Here comes your first riddle-clue! Listen carefully, Detective..."
2. (encouraging) "A pattern is when something REPEATS -- like the stripes on your shirt, the same lines over and over! I'll give you riddle-clues and you just listen, look, and search. Here comes the first one..."
3. (wait 2s) (playful whisper) "Okay Detective, here's how it works -- I describe something with a pattern, you find it! Easy! Let's start with your very first riddle-clue..."

**Screen:** Detective-themed mission card with "Pattern Detective" badge, magnifying glass over pattern mosaic, 3 empty circle slots, trigger photo above with golden star, pulsing "CLUE #1" banner.

#### Step 3: Multi-Round Interaction

**Round 1 -- Riddle-Clue #1: Something with Spots (full detail)**

**AI says:** *(mysterious, slow riddle voice)* "Riddle-Clue number one! Listen closely, Detective... I'm thinking of something nearby. It's small and has SPOTS -- like tiny painted dots, scattered all over it. The dots might be dark on something light, or light on something dark. Can you find something with spots? Go look and take a photo!"

**Child responses:**

1. (Ideal) Child photographs something with spots/dots. "I found spots!" / "This has dots!"
2. (Unexpected) Child photographs something without a clear pattern. "Is it this?"
3. (No response / stuck) Child looks around but doesn't photograph.

**AI follow-up:**

1. (triumphant) "YES, Detective! Look at those SPOTS -- little dots sprinkled all over! Each dot is like a tiny circle, and they repeat across the whole thing. That's a pattern called SPOTS! Different from your stripes -- stripes are lines, but spots are DOTS! First clue -- SOLVED! Two more to go!"
2. (thoughtful, encouraging) "Ooh, interesting find! My riddle is about something with SPOTS -- tiny dots or circles repeated across it. Think of a ladybug's back, or a shirt with polka dots, or even a leaf with little bumps. Can you find something with dots on it?"
3. (wait 2s) (helpful whisper) "Detective hint! Spots are tiny dots or circles that repeat. Look at the ground -- do you see a stone with speckles? Or check your clothes -- any polka dots? Even a bumpy rock with different-colored flecks counts!"

**Screen:** Photo slides into first slot with spotted sparkles and "SOLVED!" animation. Spots icon appears. Counter: "Clue 1 of 3 -- SOLVED!" and "CLUE #2" pulses.

**Round 2 -- Riddle-Clue #2: Something with Zigzags:** AI gives riddle about something that "goes back and forth, back and forth -- like a path that can't make up its mind!" Child searches for zigzag patterns -- cracks, serrated leaf edges, decorative fences. AI reveals zigzags are angles that repeat, different from stripes and spots.

**Round 3 -- Riddle-Clue #3: Something with Parallel Lines:** AI gives riddle about "straight LINES, all in a row -- marching together like soldiers!" Child searches for parallel lines -- wooden fence, stacked bricks, bench grooves, leaf veins. AI reveals lines are rows that repeat. Includes stuck branch with hints about sidewalk cracks, fabric weave, shoelaces.

#### Step 4: Celebration

**AI says:** *(slow, dramatic build-up)* "Okay, Pattern Detective -- look at everything you found. Something with spots... something with zigzags... something with lines in a row... And remember where we started -- your shirt with STRIPES! Now here's the SECRET I've been hiding... *(dramatic pause)* ...EVERYTHING you found has a PATTERN! Spots, zigzags, lines, stripes -- they're ALL patterns! Nature and people BOTH love making patterns! Stripes, spots, zigzags -- PATTERNS ARE EVERYWHERE!"

**Child responses:**

1. (Ideal) "Whoa!" / "Patterns ARE everywhere!" / "I found all the patterns!"
2. (Unexpected) "I knew it!" / "That's cool!" / "What other patterns are there?"

**AI follow-up:**

1. (celebrating) "You DID find them all! Spots are dots that repeat. Zigzags are angles that repeat. Lines are straight rows that repeat. Stripes are bands that repeat. They all REPEAT -- that's what makes them patterns! And you found them in totally different places -- on clothes, on the ground, on plants! Patterns connect EVERYTHING!"
2. (validating) "It IS cool! There are even MORE patterns -- spirals that swirl, waves that roll, checks that crisscross. Every time you look at something, ask: does it have a pattern? I bet the answer is YES!"

**Reflection prompt:**

**AI says:** *(amazed, reflective)* "Detective, look at your collection -- stripes, spots, zigzags, and lines. They look SO different from each other! But they ALL turned out to be patterns. Why do you think there are so many different KINDS of patterns?"

**AI follow-up:**

1. (delighted) "Exactly! Different patterns do different jobs! Stripes on a zebra help it hide. Spots on a ladybug warn predators. Zigzags on a snake help it blend in. Patterns aren't just pretty -- they're USEFUL!"
2. (warmly) "They ARE pretty! And patterns aren't just for looking at. Stripes help zebras hide, spots warn predators away, zigzags help snakes blend in. Pretty AND useful!"

**Screen:** Collection photos in a circle around trigger photo. Golden connection lines with labels: "SPOTS," "ZIGZAGS," "LINES." Trigger labeled "STRIPES." Shimmering "PATTERNS" word above in mixed-pattern-textured letters. Nature examples animate: zebra stripes, ladybug spots, snake zigzags.

#### Step 5: Closing + IB Concepts

**AI says:** *(warm, proud celebration)* "Congratulations, Pattern Detective! You did something incredible today. You looked closely at the **Form** of things -- the stripes, the spots, the zigzags, the lines -- and you recognized that they're all patterns. And you discovered the **Connection** -- that patterns link totally different things together! A shirt and a leaf and a sidewalk crack -- all connected by pattern! You earned your Pattern Detective Badge!"

**Child responses:**

1. (Engaged) Cheers, talks about patterns, wants to find more.
2. (Quiet) Smiles or says nothing.

**AI follow-up:**

1. (encouraging) "Next time you go outside, look at EVERYTHING around you -- clothes, leaves, buildings, bugs -- and ask: what's YOUR pattern? You'll see stripes, spots, and zigzags everywhere! Bye for now, Detective!"
2. (warm) "Your detective badge is saved! Patterns are hiding everywhere -- now YOU know how to spot them. Bye, Detective!"

**Screen:** Golden "Pattern Detective Badge" -- circular, magnifying glass over pattern mosaic center, 3 collection photos with pattern labels, trigger photo at top. "Form" in mixed-pattern-filled letters, "Connection" with golden thread-link weaving between letters. Pattern mosaic icon between concepts. Soft chime. Pattern fragments drift and settle on badge.
