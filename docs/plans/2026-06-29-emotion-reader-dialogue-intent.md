# Emotion Reader Dialogue Intent Plan

**Goal:** Restore Emotion Reader to an emotion-reading activity while keeping
runtime dialogue concise, natural, and free of hidden answer or cue-label leaks
before the child answers.

**Architecture:** The package owns the activity intent, hidden targets,
accepted answer variants, retry language, and micro-bridge directions. The
runtime owns bounded generation, leak guards, exact fallback lines, response
verification, and tests that prove package wording cannot drift into generic
chatbot behavior.

**Tech Stack:** WonderLens activity packages, WonderLens AI runtime generation,
response verification, Activity WS dialogue checker, and focused local live QA.

---

## Acceptance Criteria

1. Round prompts ask the child to infer the emotion in the image.
2. Pre-answer dialogue does not say hidden answers or labeled cues such as
   `worried hands`, `sleepy shoulders`, or `brave try`.
3. Correct or similar emotion answers advance.
4. Wrong or off-topic answers stay on the same round with a short retry prompt.
5. A success bridge may name the just-answered emotion, then asks the next
   emotion-reading question without leaking the next answer.
6. Lower tier support can use a binary choice when the child needs scaffolding.
7. Dialogue is generated inside a narrow contract when possible, with safe
   package fallbacks if the speaker output violates the contract.
8. The four-package dialogue checker catches Emotion Reader answer leaks and
   care/help-first prompt drift.

## Task 1: Add Failing Runtime Tests

**Repo:** `wonderlens-ai`

**Files:**

- Modify: `tests/unit/activity/test_runtime_generator.py`
- Modify: `tests/unit/activity/test_response_verification.py`
- Modify: `tests/unit/activity/test_package_response_matrix.py`
- Modify: `tests/unit/scripts/test_check_activity_ws_dialogue_quality.py`

**Steps:**

1. Add a runtime-generation test proving Emotion Reader round goals are
   emotion-inference prompts and do not include pre-answer hidden cue labels.
2. Add response-verification tests proving success directions do not leak the
   next round answer and retry directions do not reveal the current answer.
3. Add package matrix tests proving correct emotion-only answers advance while
   care/help-only answers no longer define the primary task.
4. Add checker tests proving session logs with pre-answer target leaks fail.
5. Run the focused tests and confirm they fail for the expected reasons.

## Task 2: Update Package Contract

**Repos:** `wonderlens-activity-autodesign`, `wonderlens-ai`

**Files:**

- Modify: `activities/concept_emotion_reader_care/prod.md`
- Modify: `activities/concept_emotion_reader_care/tag_block.yaml`

**Steps:**

1. Rewrite the rules line to explain only that each picture shows a feeling.
2. Rewrite round prompts to ask what feeling the child sees, without target
   words or labeled cue phrases.
3. Keep hidden targets and accepted variants in `response_verification`.
4. Rewrite success directions as compact bridges that can reveal only the
   just-matched emotion and ask the next neutral prompt.
5. Rewrite retry directions as neutral picture-clue prompts with no answer leak.

## Task 3: Implement Guarded Runtime Behavior

**Repo:** `wonderlens-ai`

**Files:**

- Modify: `app/modules/activity/agents/script_agent.py`
- Modify: `app/modules/activity/service.py`
- Modify: `scripts/check_activity_ws_dialogue_quality.py`
- Modify: `scripts/qa_activity_pipeline/axes.py`
- Modify: focused unit tests for runtime generation, response verification,
  service streaming, package matrix behavior, and session-log checking.

**Steps:**

1. Preserve package-defined hidden answer terms and forbidden pre-answer terms.
2. Allow bounded package generation for Emotion Reader where the package opts
   in, but fall back to safe package lines on leak or drift.
3. Keep exact package fallback support for streaming and non-streaming paths.
4. Make response verification choose package-authored bridge and retry
   directions before any generic runtime wording.
5. Preserve strict behavior for the other three targeted packages unless the
   checker or tests show a regression.

## Task 4: Regenerate And Validate

**Repos:** both

**Steps:**

1. Mirror the package into `wonderlens-ai`.
2. Regenerate `runtime.yaml` for `concept_emotion_reader_care`.
3. Run schema validation in autodesign.
4. Run `scripts/generate_activity_runtime.py --check` in AI.
5. Run focused unit/API tests and the dialogue checker tests.
6. Run a focused local Activity WS sweep for Emotion Reader correct, wrong, and
   off-topic paths.
7. Commit only the intended files in each repo after validation passes.
