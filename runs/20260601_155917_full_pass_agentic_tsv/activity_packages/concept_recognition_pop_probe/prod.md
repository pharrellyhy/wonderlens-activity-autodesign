## Recognition Pop Challenge

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | Recognition Pop Challenge |
| Activity Category | cat1 |
| Recommended Tier | T1 |
| Core IB Key Concepts | Form and Perspective |
| Related Concepts | target, distractor, similarity, attention |
| ATL Skills Focus | observation, inhibition, listening and speaking |
| Experience Pillar | Mystery |
| Game Style | mystery_lens |

### B. Activity Overview

**1. Brief Description**

After a source photo introduces a target animal such as a dog, the AI teaches similar animals such as fox and wolf. Then mixed cards appear one at a time: the child says the target word when the target appears and stays quiet or says nothing for distractors.

**2. Educational Purpose (KUD)**

- **K (Know):** Similar animals can share features, but the target has specific visible clues.
- **U (Understand):** Careful recognition means responding to the target and holding back for look-alikes.
- **D (Do):** Learn the target word, notice similar/different features, say the target word only on target cards, and stay quiet for distractors.

**3. Design Highlight**

This is target-vs-distractor timing behavior, not ordinary matching. The source photo target anchors the game, and every pop round requires speak-on-target or quiet-on-distractor behavior.

**4. Typical Scenario**

The child photographed a dog. The AI introduces dog, fox, and wolf with visible clues, then shows a timed stream of approved animal cards. When a dog card pops, the child says "dog"; when fox or wolf appears, the child stays quiet.

### C. Interaction Flow

> Recommended Tier: T1

#### Step 1: Transition Bridge

**Runtime AI instruction:** Goal: Open from the source photo target, such as dog, and name the child as a recognition-pop spotter who will say the target word only when the target appears. Constraint: T1, 2-3 short sentences; do not use ordinary left/right matching language; if source target is unavailable, use an approved target/distractor set and say it is a practice set. Tone: alert and playful. Progress evidence: child repeats or confirms the target word. Branch behavior: if correct, save target word and preview look-alikes; if wrong/off-topic, re-anchor to the source photo target; if help/silence, model the target word once and accept echo/point, with graceful exit after repeated silence. Frame/source guardrail: source frame is photo target -> similar animals -> mixed timed cards; screen shows source target card and empty pop tokens.

**Example AI line:** "Your photo target is dog. In this pop game, say 'dog' only when dog appears, and keep quiet for look-alikes."

**Child responses:**

1. (Ideal) The child says "dog," repeats the chosen target, points to the target, or agrees.
2. (Unexpected) Child says fox/wolf as the target, asks to pick any matching picture, or wants to tap all animals.
3. (No response) Child watches the target card without repeating.

**AI follow-up:**

1. Save the target word and move to similar-animal teaching.
2. Correct gently: "Fox and wolf are look-alikes today. Our target word is dog."
3. [wait 2s] Say the target word with the child once, then offer to do one slow practice pop.

**Screen:** Source target photo/card centered, target word chip visible, five empty pop tokens below.

#### Step 2: Role And Rules

**Runtime AI instruction:** Goal: Teach the target and similar distractors before the pop stream: dog is target; fox/wolf or approved similar animals are quiet cards. Constraint: T1, 2-3 short sentences; keep features visual and simple; no punitive whack imagery. Tone: focused coach. Progress evidence: child identifies target versus quiet cards or repeats "say dog, quiet for fox/wolf." Branch behavior: if correct, start Round 1; if wrong, contrast one visible feature and restate the timing rule; if help/silence, practice one target and one distractor slowly before proceeding or exiting. Frame/source guardrail: preserve target-vs-similar-animal timing; screen shows target and distractor cards with Say/Quiet labels.

**Example AI line:** "Dog is our say-it card. Fox and wolf are quiet cards, because they look similar but they are not the target."

**Child responses:**

1. (Ideal) The child says "dog means say," "fox quiet," or points to target/distractor cards.
2. (Unexpected) Child tries to match dog with fox, asks which is prettier, or says every animal name.
3. (No response) Child watches the rule cards.

**AI follow-up:**

1. Save "rule ready" and announce slow pops first.
2. Reframe: "This is not a matching choice. It is say target, quiet for distractor."
3. [wait 2s] Model: "Dog: say dog. Fox: quiet," then ask for a nod/echo.

**Screen:** Three cards appear: Dog Target with a small sound icon, Fox Quiet, Wolf Quiet. Asset `recognition_challenge_cards_01` is required for playable timing; unsupported fallback keeps the package gated instead of converting to matching.

#### Step 3: Multi-Round Core Loop

**Round 1 -- Slow Target Pop:**

**Runtime AI instruction:** Goal: Show or announce a slow target card and prompt the child to say the target word when the target appears. Constraint: T1, 1-2 short sentences during the pop; timing should be slow enough for preschool response; if timed UI is unavailable, mark unsupported rather than changing to matching. Tone: excited whisper. Progress evidence: child says target word, echoes it, or points and vocalizes. Branch behavior: if correct, award a pop token; if wrong/distractor word, restate target and replay one slow target; if help/silence, model "dog" and allow echo, then proceed or early-exit after repeated silence. Frame/source guardrail: child action is speak target on target card only; screen shows one target card, not multiple-choice matching.

**Example AI line:** "Pop! Dog is here. Say 'dog'!"

**Child responses:**

1. (Ideal) The child says "dog" or the current target word.
2. (Unexpected) Child says "fox," taps randomly, or waits for choices.
3. (No response) Child sees the target pop but does not speak.

**AI follow-up:**

1. Fill token 1 and say the target was caught by voice.
2. Replay slowly: "This one is dog, our say-it card."
3. [wait 2s] Model the word once and accept an echo; if still silent, move to a quiet-card practice.

**Screen:** One target animal card pops in the center; token 1 fills only for target-word response or supported echo.

**Round 2 -- Slow Distractor Quiet:**

**Runtime AI instruction:** Goal: Show or announce a similar distractor such as fox or wolf and coach the child to stay quiet or say nothing. Constraint: T1, 1-2 short sentences; praise quiet control without shaming accidental speech. Tone: suspenseful and kind. Progress evidence: child stays quiet, says "quiet," shakes head, or withholds the target word. Branch behavior: if correct, award a quiet token; if child says target on distractor, explain the visible difference and practice quiet once; if help/silence, count silence as acceptable progress when the distractor is showing. Frame/source guardrail: distractor response is no target word, not choosing which animal it is; screen shows a single distractor card with quiet state.

**Example AI line:** "Pop... fox! It looks a little like dog, but fox is a quiet card."

**Child responses:**

1. (Ideal) The child stays quiet, says "quiet," or does not say the target word.
2. (Unexpected) Child says "dog," tries to match fox with dog, or names all animals.
3. (No response) Child remains silent while the distractor is shown.

**AI follow-up:**

1. Fill a quiet token and celebrate careful waiting.
2. Say: "Good try. The pointy face/tail tells us this is fox, so we save our dog word."
3. [wait 2s] Treat silence as correct for distractor, then move on.

**Screen:** One fox/wolf distractor card appears; "quiet success" token can fill without speech.

**Round 3 -- Mixed Target After Distractor:**

**Runtime AI instruction:** Goal: Present a distractor then a target, requiring the child to stay quiet first and then say the target word when it appears. Constraint: T1, 2 short cue sentences max; keep timing slow and do not overload with more than two pops. Tone: playful attention coach. Progress evidence: child withholds target word on distractor and says target on target, or succeeds with one of the two responses after coaching. Branch behavior: if correct, save a combo token; if wrong, isolate the missed part and replay one pop; if help/silence, model the sequence once and allow a partial token. Frame/source guardrail: target-vs-distractor timing remains central; screen streams one card at a time with previous card fading out.

**Example AI line:** "First pop is wolf: quiet... next pop is dog: say 'dog'!"

**Child responses:**

1. (Ideal) The child stays quiet for wolf/fox and says "dog" for dog.
2. (Unexpected) Child says dog for both cards, names wolf, or asks to choose from two visible cards.
3. (No response) Child remains quiet for both pops.

**AI follow-up:**

1. Fill combo token and name the two-part skill.
2. Replay the missed contrast: "Quiet for wolf. Say dog for dog."
3. [wait 2s] Accept quiet as correct on the distractor, then model the target word for the target card.

**Screen:** Card stream shows one distractor then one target; token 3 records "quiet + say."

**Round 4 -- Look-Alike Challenge:**

**Runtime AI instruction:** Goal: Use a more similar approved distractor or target variant and ask the child to respond only when the target appears, reinforcing visible differences. Constraint: T1, 2 short sentences; do not introduce dog breeds unless approved assets support them; keep distractors child-safe and non-scary. Tone: focused and encouraging. Progress evidence: child responds to target or successfully waits for distractor. Branch behavior: if correct, save advanced token; if wrong, name one visible clue and slow down; if help/silence, give the clue before the pop and accept a smaller response. Frame/source guardrail: this remains a timing pop game from source target to similar animals, not a compare quiz.

**Example AI line:** "This one has a foxy face, so quiet... now here comes dog: say 'dog'!"

**Child responses:**

1. (Ideal) The child waits for distractor and says target on the target pop.
2. (Unexpected) Child explains differences instead of responding, taps all cards, or says target for every animal.
3. (No response) Child stays quiet through the sequence.

**AI follow-up:**

1. Save the advanced attention token.
2. Acknowledge the explanation briefly, then return to "say only on dog."
3. [wait 2s] Provide one clue and replay a single target pop; exit if still no response.

**Screen:** One-card pop stream with visible clue highlight; token 4 fills for target/quiet control.

**Round 5 -- Final Pop Check:**

**Runtime AI instruction:** Goal: Run one final short mixed pop check and let the child finish by saying the target word only on target. Constraint: T1, maximum three pops; if the child is fatigued or repeatedly unproductive, close with the tokens already earned. Tone: upbeat and concise. Progress evidence: child completes one target response or one distractor quiet response. Branch behavior: if correct, complete the board; if wrong, recap target/quiet rule without another full retry unless child asks; if help/silence, count safe quiet on distractors and close gracefully. Frame/source guardrail: final check must preserve speak-target/stay-quiet behavior; screen shows final timed cards and completion badge.

**Example AI line:** "Last pop round: quiet for fox, say 'dog' for dog, quiet for wolf."

**Child responses:**

1. (Ideal) The child says target only on target and stays quiet for distractors.
2. (Unexpected) Child says every animal, asks for matching choices, or loses interest.
3. (No response) Child remains quiet for the whole sequence.

**AI follow-up:**

1. Complete the recognition-pop board and recap the skill.
2. Say: "The target word is only for dog. We can stop here and keep practicing next time."
3. [wait 2s] Close with partial success: "You practiced careful waiting."

**Screen:** Final stream completes; badge shows target word, quiet cards, and pop tokens.

#### Step 4: Magic Moment

**Runtime AI instruction:** Goal: Reveal the child's recognition-pop board by showing target catches and quiet waits, emphasizing attention to similar animal forms. Constraint: T1, 2-3 short sentences; do not convert results into a matching score. Tone: proud coach. Progress evidence: child names target, says quiet rule, or watches tokens. Branch behavior: if correct, recap their strongest target/quiet moment; if wrong/off-topic, recap the rule neutrally; if help/silence, read the board and finish. Frame/source guardrail: payoff must be target-vs-distractor timing from the source photo; screen shows target word and distractor quiet tokens.

**Example AI line:** "You caught the dog pops and saved your voice for the fox and wolf pops. That is careful recognition."

**Child responses:**

1. (Ideal) The child says target word, names quiet card, or points to tokens.
2. (Unexpected) Child wants to rank animals or match pairs.
3. (No response) Child watches the board.

**AI follow-up:**

1. Name one exact target/quiet success.
2. Re-anchor: "This game was not about favorites; it was about saying dog only for dog."
3. [wait 2s] Read the tokens and move to closing.

**Screen:** Board shows Source Target, Similar Quiet Cards, Target Catches, Quiet Waits.

#### Step 5: Closing + IB Concepts

**Runtime AI instruction:** Goal: Close with Form and Perspective by naming how the child noticed similar forms and used the target perspective to decide when to speak. Constraint: T1, 2 short sentences; include parent-reviewable recap of source target and distractors. Tone: warm and complete. Progress evidence: child repeats target, says goodbye, or accepts badge. Branch behavior: if correct, echo target word; if wrong/off-topic, close the pop challenge first; if help/silence, end gracefully. Frame/source guardrail: closing must mention source target, similar animals, and say-target/stay-quiet timing.

**Example AI line:** "You practiced Form by noticing dog, fox, and wolf shapes, and Perspective by remembering which one was the target. You said 'dog' for dog and stayed quiet for look-alikes."

**Child responses:**

1. (Ideal) The child says "dog," asks for another target, or watches the badge.
2. (Unexpected) Child shifts topic before recap.
3. (No response) Child stays on the recap badge.

**AI follow-up:**

1. Offer next time: use a new source photo target and new look-alikes.
2. Close Recognition Pop first, then acknowledge the new topic.
3. [wait 2s] Read the badge and end.

**Screen:** Recap badge lists "Recognition Pop Spotter," mechanic `compare`, focal attribute `whack_a_mole_recognition`, and next hint "say target, quiet for look-alikes."
