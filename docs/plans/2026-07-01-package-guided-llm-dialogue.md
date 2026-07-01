# Package-Guided LLM Dialogue Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add package-owned dialogue policy for LLM-generated, emotional, child-friendly utterances while preserving deterministic response verification and exact fallback lines.

**Architecture:** Activity packages keep `dialogue_acts` as exact fallback semantics and add `speaker_dialogue_mode: package_guided_llm` plus `dialogue_policy`. WonderLens AI consumes those opaque policy fields to prompt the Speaker; future utterance tuning should mostly edit package YAML, not runtime code.

**Tech Stack:** Markdown/YAML activity packages, JSON Schema validation, WonderLens AI runtime generator.

---

### Task 1: Add Package Policy Fields

**Files:**
- Modify: `activities/concept_emotion_reader_care/tag_block.yaml`
- Modify: `activities/concept_partial_reveal_deduce/tag_block.yaml`
- Modify: `activities/concept_animal_sound_motion_voice/tag_block.yaml`
- Modify: `activities/concept_phoneme_hunt_collect/tag_block.yaml`

**Step 1: Write policy blocks**

For CAT1 response-verification packages, place:

```yaml
speaker_dialogue_mode: package_guided_llm
dialogue_policy:
  style: ...
  max_sentences: 2
  emotional_tone: ...
  acknowledge_child_response: ...
  forbidden_phrases: [...]
  act_guidance: ...
  examples: ...
```

For Letter Treasure Hunt, place the equivalent fields under `runtime_judgment_contract`.

**Step 2: Preserve exact fallbacks**

Keep `dialogue_acts` for all four packages. The runtime uses them as fallback and semantic targets, not as the primary utterance source in guided mode.

### Task 2: Validate Metadata

**Files:**
- Modify if needed: `activities/_schema/tag_block.schema.json`
- Modify if needed: `docs/activity_vocabulary.md`

**Step 1: Check schema behavior**

The schema currently allows additional properties, so new nested policy fields should validate without enum changes. If validation fails, add only the narrow schema allowance needed.

**Step 2: Run validation**

Run the project schema validation snippet from `AGENTS.md` against the four changed packages.

### Task 3: Align Consumer Runtime

**Files:**
- Source for copy into WonderLens AI: the four package `tag_block.yaml` files.

**Step 1: Copy package changes to WonderLens AI**

Mirror the four changed tag blocks into the AI repo package directory.

**Step 2: Regenerate AI runtime YAML**

Use WonderLens AI runtime generation checks for the four packages. Confirm `runtime.yaml` preserves `speaker_dialogue_mode`, `dialogue_policy`, and `dialogue_acts`.

### Task 4: QA Copy Criteria

Manual review each package policy against:
- utterance has a clear emotion
- acknowledgement is present when child input exists
- task instruction stays obvious
- no hidden answer leaks before final reveal
- wrong/off-topic does not praise
- no chatbot-style explanation
- no formula phrases such as `here is the rule`, `WonderLens will`, or `the correct answer is` before reveal

### Task 5: Docs and Commit

Update `HANDOFF.md` with problem, solution, edits, not changed, and verification. Commit with a conventional message.
