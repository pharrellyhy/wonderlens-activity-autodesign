# Dialogue Quality Recovery Implementation Plan

**Goal:** Make the four runtime-verified activity sessions produce short,
clear, state-accurate dialogue in prod-like live runs, with no internal labels,
no hidden-answer leakage, and no finalizer rewrites that distort package intent.

**Architecture:** Treat this as a boundary fix first and a package authoring pass
second. Runtime may normalize, verify, and route state, but it must not invent
new child-facing clues, expose internal scenario labels, or rewrite strict
package dialogue into a different task. Package files then provide concise
step-specific directions and accepted-answer metadata.

**Tech Stack:** WonderLens AI activity runtime, package `runtime.yaml` mirrors,
session JSONL logs, live activity websocket matrix checks, and producer package
metadata in this repository.

---

## Context

Latest prod logs reviewed:

- `181250+0800__ws_ws_9e3de1ea99da4eb2.jsonl`
- `181604+0800__ws_ws_6929667091464fab.jsonl`
- `182126+0800__ws_ws_708acf7fc04e4200.jsonl`
- `182419+0800__ws_ws_12c1515be7e04256.jsonl`

The logs show real improvement in rule-step brevity, but also prove that
package-only editing is not enough yet. Some bad dialogue is created after the
package text, inside generic runtime behavior.

## Non-Negotiable Done Criteria

The work is not done until a live activity websocket matrix run proves all of
these:

1. No child-facing output contains internal labels such as `Cue`, `Card Voice`,
   `partial reveal guess`, `scenario`, `round_scenario`, or package step IDs.
2. `concept_partial_reveal_deduce` never reveals or confirms the hidden answer
   before the final reveal.
3. Partial reveal wrong-final responses reveal the answer without saying or
   implying the child guessed correctly.
4. Emotion and animal verifier success bridges ask the next task directly,
   without repeating the previous retry text or exposing scenario labels.
5. Phoneme hunt uses one seed source for the target first letter and does not
   switch target letters mid-session.
6. Phoneme hunt visible object names are normalized to the object/entity noun,
   not adjective-heavy phrases such as `green ball`, `plastic cup`, or
   `Chinese Textbook`.
7. Capture-photo turns return `capture_photo` and the utterance asks for a
   photo, not a voice answer.
8. Speaker output, final text chunks, and TTS input have the same task meaning.
   TTS cleanup may remove recognized leading tone tags only.

## Phase 1: Runtime Boundary Fixes

### Task 1: Stop Hidden-Answer Grounding Rewrites

**Repo:** `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

**Files:**

- Modify: `app/modules/activity/dialogue_quality.py`
- Modify: `app/modules/activity/service.py`
- Test: nearest existing activity dialogue/finalizer tests, or add focused unit
  tests beside them.

**Problem from logs:** Partial reveal changed natural clue text into
`The partial reveal guess pounces...`. That came from generic grounding repair,
not from the package.

**Implementation:**

1. Add a guard so hidden-answer activities and hidden-answer rounds do not use
   generic entity grounding repair.
2. Keep hidden-answer masking in place.
3. Add a test where input `It listens with pointy ears. What do you think it
   is?` remains unchanged for partial reveal.

**Verification:**

```bash
pytest <focused-dialogue-quality-test> -q
```

### Task 2: Remove Generic Scenario-Label Success Bridges

**Repo:** `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

**Files:**

- Modify: `app/modules/activity/response_verification.py`
- Test: nearest response verification tests.

**Problem from logs:** Emotion success bridges said `Sleepy Shoulders Cue` and
`Brave Try Cue`.

**Implementation:**

1. For `speaker_dialogue_mode: strict_package`, do not build success directions
   from raw `next_scenario` labels.
2. Prefer package-authored `success_direction`.
3. If no package-authored success direction exists, synthesize from the next
   step child-facing goal, never from an internal scenario label.
4. Add tests that labels ending in `Cue`, `Card Voice`, or similar internal
   names do not appear in the response direction.

**Verification:**

```bash
pytest <focused-response-verification-test> -q
```

### Task 3: Make Partial Reveal Outcome-Aware

**Repo:** `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

**Files:**

- Modify: `app/modules/activity/response_verification.py`
- Modify: `app/modules/activity/service.py` only if the speaker needs explicit
  outcome context.
- Test: response verification and activity turn tests.

**Problem from logs:** The runtime said `You guessed it!` before final reveal
and later implied the child found the cat after a wrong final answer.

**Implementation:**

1. Distinguish pre-final guess acknowledgement from correct-answer
   confirmation.
2. Pass final answer outcome into the speaker direction when final verification
   matched false.
3. For wrong final answers, direct the speaker to reveal the answer neutrally.

**Verification:**

```bash
pytest <focused-partial-reveal-verification-test> -q
```

## Phase 2: Package Dialogue Contracts

### Task 4: Add Shared Good-Dialogue Rules for These Four Packages

**Repo:** `/Users/pharrelly/codebase/github/wonderlens-activity-autodesign`

**Files:**

- Modify: `docs/plans/2026-06-24-four-package-runtime-verification-authoring.md`
  or add a dedicated dialogue-quality note under `docs/plans/`.
- Modify package docs only if the rule belongs in durable authoring guidance.

**Rules:**

1. Rule step: explain only the rules, no extra invitation to play.
2. Round ask: one direct instruction or question, no extra teaching paragraph.
3. Retry: direct correction, no `would you like`, no broad chatbot-style help.
4. Success bridge: acknowledge briefly, then ask the next task.
5. Internal labels are never child-facing.
6. Binary choices are forbidden unless the activity explicitly requires them.
7. Hidden-answer games may say `maybe-guess`; they may not say `you guessed it`
   before the final answer is verified.

**Verification:**

```bash
git diff --check
```

## Phase 3: Package-Specific Edits

### Task 5: Emotion Reader

**Repos:**

- `/Users/pharrelly/codebase/github/wonderlens-activity-autodesign`
- `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

**Files:**

- Modify: `activities/concept_emotion_reader_care/prod.md`
- Modify: `activities/concept_emotion_reader_care/runtime.yaml`
- Modify WonderLens AI runtime mirror for the same package.

**Implementation:**

1. Add explicit `success_direction` per round.
2. Remove scenario labels from any child-facing direction.
3. Add accepted variants for likely correct STT text:
   - `sleeping`
   - `great try`
   - `good try`
   - `keep trying`
4. Keep retry text short and cue-specific.

**Live Gates:**

- Correct and similar answers advance.
- Wrong or off-topic answers stay.
- Success bridge asks the next visible cue directly.

### Task 6: Animal Sound Motion Voice

**Files:**

- Modify: `activities/concept_animal_sound_motion_voice/prod.md`
- Modify: `activities/concept_animal_sound_motion_voice/runtime.yaml`
- Modify WonderLens AI runtime mirror for the same package.

**Implementation:**

1. Replace binary retry phrasing with direct imitation prompts.
2. Keep accepted tokens transcript-based unless a real audio classifier is
   added.
3. Add conservative near-miss handling only when it does not advance unrelated
   answers.

**Live Gates:**

- Correct or similar animal sound/role response advances.
- Wrong answer stays with a direct retry.
- No long roleplay paragraph appears between rounds.

### Task 7: Partial Reveal Deduce

**Files:**

- Modify: `activities/concept_partial_reveal_deduce/prod.md`
- Modify: `activities/concept_partial_reveal_deduce/runtime.yaml`
- Modify WonderLens AI runtime mirror for the same package.

**Implementation:**

1. Tighten pre-final acknowledgement: `Good maybe-guess.`
2. Add explicit wrong-final response direction.
3. Keep each clue limited to the authored clue for that round.
4. Do not mention the correct answer until final reveal.

**Live Gates:**

- No answer leak before final.
- No `you guessed it` unless the answer is actually correct.
- Final reveal is neutral when the final guess was wrong.

### Task 8: Phoneme Hunt First-Letter Collect

**Files:**

- Modify: `activities/concept_phoneme_hunt_collect/prod.md`
- Modify: `activities/concept_phoneme_hunt_collect/runtime.yaml`
- Modify WonderLens AI runtime mirror for the same package.

**Implementation:**

1. Choose exactly one seed source:
   - Preferred: first in-activity photo sets the target first letter.
   - Alternative: source/handoff photo sets the target, and the package says so
     clearly from the start.
2. Normalize vision object names to a noun label before deriving the first
   letter.
3. Ensure failed and passed verification both return `capture_photo`, with
   different utterances.
4. Keep story synthesis separate from collection-photo turns.

**Live Gates:**

- The target letter does not change mid-session.
- Object labels are nouns.
- Capture-photo turns sound like photo tasks.

## Phase 4: Live Matrix and Log-Based Quality Review

### Task 9: Run Focused Live Matrix

**Repo:** `/Users/pharrelly/codebase/gitlab/wonderlens-ai`

**Implementation:**

Run one live session per activity against the target environment and save
session logs.

**Required Review:**

For every session, inspect:

- `speaker_output`
- final text chunks
- `tts_request`
- `stt_result`
- `response_verification_decision`
- server command/state frames

**Pass/Fail:**

If any non-negotiable done criterion fails, do not push. Classify the failure
as runtime, package, test harness, STT, TTS, or app-side state handling, then
fix the smallest responsible layer.

### Task 10: Push and Create MRs Only After Live Evidence

**Repos:**

- WonderLens AI MR for runtime and runtime package mirror changes.
- Autodesign MR for producer package/source documentation changes.

**MR Description Must Include:**

- The exact live session log filenames.
- A table mapping each prior issue to pass/fail evidence.
- Focused test commands and results.
- Any residual risk, especially around STT transcript quality.

## Current Risk Assessment

The highest risk is not the package wording itself. The highest risk is generic
runtime post-processing changing or contaminating good package wording. That is
why Phase 1 must happen before package dialogue tuning.

The second highest risk is treating one live success as proof. This plan
requires a four-activity live matrix and explicit log review before merge.
