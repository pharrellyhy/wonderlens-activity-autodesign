## How Many Guess

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | How Many Guess |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form |
| Related Concepts | quantity, feature, evidence, comparison |
| ATL Skills Focus | counting, observation, reasoning from features |
| Experience Pillar | Discovery |
| Game Style | field_experiment |

### B. Activity Overview

**1. Brief Description**

The child guesses and checks meaningful feature counts: how many legs an animal has, how many wheels a vehicle has, how many petals a flower has, or how many buttons an object has. Cards may support the play, but the count target is the semantic feature, not a pile of unrelated icons.

**2. Educational Purpose (KUD)**

- **K (Know):** Animals and objects can have countable features such as legs, wings, wheels, petals, buttons, or points.
- **U (Understand):** Counting is more meaningful when the child knows what feature is being counted and why it belongs to that animal or object.
- **D (Do):** Hear the target animal/object, guess the feature count, count/check together, and compare the count with another example.

**3. Design Highlight**

This is a quantity-feature guessing game, not generic visible-object counting. The AI asks "How many legs does a dog have?" or "How many wheels does a bicycle have?" and then checks the feature evidence with the child.

**4. Typical Scenario**

The screen shows a clear animal/object feature card, or the AI uses a familiar voice-only prompt. The child guesses how many legs, wheels, petals, or buttons the target has, then counts together.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: Open the feature-count mission and make clear that the child will guess counts for meaningful animal/object features, not just count visible icons. Constraint: T1, 2-3 short sentences; keep numbers small and familiar; if no card is displayed, use voice-only examples and do not claim card visibility. Tone: curious quiz-host. Progress evidence: child names or accepts a feature such as legs, wheels, petals, or buttons. Branch behavior: if correct, save the feature and preview the first guess; if wrong/generic, redirect from "how many things on screen" to "how many parts/features"; if help/silence, offer two feature choices and allow a one-question mini game after repeated silence. Frame/source guardrail: source frame is semantic quantity-feature guessing; screen shows feature badge and either `how_many_count_cards_01` or a no-card voice fallback.

**Example AI line:** "Let's play How Many Guess with parts that belong to things. First feature: legs, wheels, petals, or buttons?"

**Child responses:**

1. (Ideal) The child says "legs," "wheels," "petals," "buttons," or agrees to guess.
2. (Unexpected) Child starts counting random objects in the room or asks to count all icons on the screen.
3. (No response) Child watches the feature badge/card without choosing.

**AI follow-up:**

1. Save the chosen feature and start the first target.
2. Reframe: "This time we count a part that belongs to one animal or object."
3. [wait 2s] Offer "legs or wheels?" then run one modeled example if needed.

**Screen:** Shows title, feature-count detective role, empty tokens, and either a semantic feature card set or a voice-only fallback chip.

#### Step 2: Role And Rules

**Runtime AI instruction:** Goal: Explain the loop: hear/see a target, guess how many of the named feature it has, then count/check the feature together. Constraint: T1, 2-3 short sentences; avoid generic pile-count prompts; cards must show or imply the animal/object with the feature target. Tone: clear and playful. Progress evidence: child repeats the rule, chooses "guess," or names the first target. Branch behavior: if correct, move to Round 1; if wrong, restate target-plus-feature; if help/silence, give a binary choice and graceful one-round exit. Frame/source guardrail: do not count card icons as the goal unless they are the meaningful feature itself; screen labels target and feature separately.

**Example AI line:** "Rule: I name the thing and the feature, you guess the number, then we check together. Dog plus legs, bike plus wheels, flower plus petals."

**Child responses:**

1. (Ideal) The child says yes, asks for an easy one, or names a target/feature.
2. (Unexpected) Child answers before hearing the feature, counts background decorations, or changes to naming objects.
3. (No response) Child looks at the rule strip.

**AI follow-up:**

1. Mark "rule ready" and introduce the first target.
2. Point back to the target-feature pair: "We need the thing and the part."
3. [wait 2s] Read one pair, "dog legs," and ask "guess two or four?"

**Screen:** Rule strip shows Target -> Feature -> Guess -> Check. `how_many_count_cards_01` appears only if available; fallback chip says "voice feature question."

#### Step 3: Multi-Round Core Loop

**Round 1 -- Animal Legs:**

**Runtime AI instruction:** Goal: Ask a meaningful animal-leg count question, such as how many legs a dog, cat, duck, spider, or bird has, and check by counting the legs/known body plan together. Constraint: T1, 2-3 short sentences; choose familiar animals and keep correction friendly; if a card is used, the child counts the animal's legs, not card icons. Tone: bright and investigative. Progress evidence: child guesses a number or participates in counting/checking. Branch behavior: if correct, save the count and explain the feature; if wrong, count together from one and let the child revise; if help/silence, offer two choices like two/four and model counting. Frame/source guardrail: target is animal legs as a semantic feature; screen shows animal card or voice fallback with leg markers.

**Example AI line:** "Dog question: how many legs does a dog usually have? Guess first, then we will check the paws together."

**Child responses:**

1. (Ideal) The child says "four," "two," "eight," or counts along.
2. (Unexpected) Child counts eyes, animals on the screen, or background shapes instead of legs.
3. (No response) Child looks at the animal card without guessing.

**AI follow-up:**

1. Save the count token and say why the feature fits: "Four legs help a dog walk and run."
2. Redirect: "We are counting legs this time. Let's touch/count each leg together."
3. [wait 2s] Offer "two or four?" and count "one, two..." with the child.

**Screen:** Center card shows one animal with clear leg visibility or a no-card dog-leg prompt; token 1 fills with "animal legs."

**Round 2 -- Object Wheels Or Buttons:**

**Runtime AI instruction:** Goal: Ask an object-feature count, such as how many wheels a bicycle/car has or how many buttons a shirt/controller has, then check the feature. Constraint: T1, 2-3 short sentences; keep feature concrete and avoid counting all visible objects. Tone: upbeat and practical. Progress evidence: child gives a number, points to each feature, or revises after counting. Branch behavior: if correct, save the feature count and compare it to Round 1; if wrong, count the named feature together; if help/silence, offer a familiar object and two number choices. Frame/source guardrail: count the object's meaningful feature only; screen highlights wheels/buttons, not decorative extras.

**Example AI line:** "Bicycle question: how many wheels does a bicycle have? Make a guess before we count."

**Child responses:**

1. (Ideal) The child says "two," "four," points to wheels/buttons, or counts aloud.
2. (Unexpected) Child counts the whole bike/car/shirt, counts people, or says color names.
3. (No response) Child watches the object card.

**AI follow-up:**

1. Save the object-feature token and compare: "Two wheels is fewer than a dog's four legs."
2. Return to feature: "We count wheels, not the whole bike. One wheel, two wheels."
3. [wait 2s] Offer "two or four?" then model the check.

**Screen:** Center card or voice prompt shows the object; feature highlight chips mark wheels/buttons; token 2 fills.

**Round 3 -- Plant Petals Or Flower Parts:**

**Runtime AI instruction:** Goal: Ask a plant/object feature-count question such as how many petals a simple flower card shows, then check by counting visible petals one by one. Constraint: T1, 2-3 short sentences; if petal count is visually unclear, switch to a clearer feature like buttons or wheels. Tone: gentle and observant. Progress evidence: child guesses/counts the petals or chooses the clearer fallback feature. Branch behavior: if correct, save the count and recap the feature idea; if wrong, count each visible petal together; if help/silence, offer a smaller number choice and close after the check. Frame/source guardrail: feature count remains semantic; screen highlights petals or fallback feature and avoids generic icon piles.

**Example AI line:** "Flower question: how many petals can we count on this flower? Guess first, then we will tap each petal in order."

**Child responses:**

1. (Ideal) The child says a number, counts petals, or asks for help.
2. (Unexpected) Child counts flowers, colors, or background stars instead of petals.
3. (No response) Child watches the flower/feature card silently.

**AI follow-up:**

1. Save the final feature token and recap the target-feature pattern.
2. Redirect: "Only petals this time. We can count each petal slowly."
3. [wait 2s] Offer "three or five?" then count aloud and close.

**Screen:** Center card shows a simple flower or fallback feature; all three tokens appear as Legs, Wheels/Buttons, Petals.

#### Step 4: Magic Moment

**Runtime AI instruction:** Goal: Reveal that the child counted three different kinds of meaningful features and compare the counts. Constraint: T1, 2-3 short sentences; recap actual saved target-feature counts and do not introduce new generic counting. Tone: proud and discovery-focused. Progress evidence: child names a favorite count or notices which feature had more/fewer. Branch behavior: if correct, compare two saved counts; if wrong/off-topic, point to the saved feature tokens; if help/silence, narrate the board and proceed. Frame/source guardrail: payoff is quantity-feature reasoning, not visible-object total; screen shows target-feature-count board.

**Example AI line:** "You counted features: dog legs, bicycle wheels, and flower petals. Some things have more parts, and some have fewer."

**Child responses:**

1. (Ideal) The child names a count, says more/fewer, or points to a token.
2. (Unexpected) Child starts counting unrelated objects.
3. (No response) Child watches the completed board.

**AI follow-up:**

1. Compare two counts using the child's saved numbers.
2. Re-anchor: "Those are fun to count too, but our board is about parts that belong to one thing."
3. [wait 2s] Read the three target-feature pairs and move to closing.

**Screen:** Board lists each target, feature, and count; a "feature detective" badge appears.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Goal: Close with Form by naming how parts/features give animals and objects their form. Constraint: T1, 2 short sentences; include one parent-reviewable recap of feature counts practiced. Tone: warm and complete. Progress evidence: child says a count, asks to play again, or accepts badge. Branch behavior: if correct, echo the feature; if wrong/off-topic, close the feature-count mission first; if help/silence, end gracefully. Frame/source guardrail: closing must mention legs/wheels/petals/buttons or other semantic features, not generic counting cards.

**Example AI line:** "Today you practiced Form by counting parts that belong to things. You guessed and checked features like legs, wheels, and petals."

**Child responses:**

1. (Ideal) The child names a feature count, asks for another animal/object, or watches the badge.
2. (Unexpected) Child shifts topic before recap.
3. (No response) Child stays on the recap badge.

**AI follow-up:**

1. Offer next time: guess a new feature count for another animal or object.
2. Close the feature-count game first, then acknowledge the new topic.
3. [wait 2s] Read the badge and end.

**Screen:** Recap badge lists "Feature Count Guesser," mechanic `enumerate`, focal attribute `how_many_guess`, and next hint "Ask: how many parts does it have?"
