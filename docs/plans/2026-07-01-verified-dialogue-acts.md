# Verified Package Dialogue Acts Implementation Plan

> **Implementation note:** Execute this plan task-by-task with tests and package
> validation before committing.

**Goal:** Extend package-owned dialogue acts from Emotion Reader to Partial
Reveal, Animal Sound, and Letter Treasure Hunt.

**Architecture:** Each package owns child-facing dialogue act copy under
`response_verification.dialogue_acts` or the package-local runtime judgment
contract. WonderLens AI consumes the generated runtime YAML and selects those
acts deterministically after verification, keeping LLM/Speaker out of critical
correctness paths.

---

## Scope

Modify package dialogue-act metadata only:

- `activities/concept_partial_reveal_deduce/tag_block.yaml`
- `activities/concept_animal_sound_motion_voice/tag_block.yaml`
- `activities/concept_phoneme_hunt_collect/tag_block.yaml`

Do not change schemas unless validation proves a missing closed vocabulary.

## Dialogue Quality Bar

- Speak directly to the child with warm, natural wording.
- Avoid meta phrases such as `here is the rule`, `runtime`, and
  `WonderLens will`.
- Keep each turn to one action or one transition.
- Avoid repetitive formula across rounds.
- Do not expose hidden answers before the package says they are visible.
- Preserve package intent: partial reveal guesses from visible clues only,
  animal sound verifies the active animal, and Letter Treasure Hunt uses first
  starting characters, not sounds.

## Tasks

### Task 1: Partial Reveal Dialogue Acts

Add package-owned acts for:

- `rule_intro`
- `round_prompt`
- `pre_final_advance`
- `wrong_retry`
- `off_topic_redirect`
- `answer_request_redirect`
- `idk_support`
- `final_reveal`
- `wrong_final_reveal`
- `celebrate`
- `closing`

Keep pre-final acts answer-safe. Final reveal may name `cat`.

Validation:

```bash
python3 -c "...tag-block schema validation snippet from AGENTS.md..."
```

### Task 2: Animal Sound Dialogue Acts

Add package-owned acts for:

- `rule_intro`
- `round_prompt`
- `correct_advance`
- `similar_advance`
- `wrong_retry`
- `off_topic_redirect`
- `idk_support`
- `celebrate`
- `closing`

Use rabbit, cat, and puppy only. Keep prompts small and safe.

Validation: run the same tag-block schema check.

### Task 3: Letter Treasure Hunt Dialogue Acts

Add package-owned acts to the runtime judgment contract or mirrored
verification metadata consumed by WonderLens AI:

- `rule_intro`
- `round_prompt`
- `correct_advance`
- `mismatch_retry`
- `unrecognized_retry`
- `no_photo_retry`
- `idk_support`
- `off_topic_redirect`
- `celebrate`
- `closing`

Use safe placeholders populated by WonderLens AI: `{recognized_name}`,
`{target_letter}`, `{actual_letter}`, and `{saved_names}`. Every retry/pass
during collection should keep the next app state as `capture_photo`.

Validation: run the same tag-block schema check and confirm no stale
phoneme/sound wording appears in the package.

### Task 4: Mirror And Verify Downstream

Mirror the three package files into WonderLens AI, regenerate runtime YAML, and
run the focused runtime/package tests from the downstream plan.

## Acceptance Criteria

- The three packages define package-owned dialogue acts.
- Existing Emotion Reader dialogue acts are unchanged.
- Rules and bridge text remain child-facing and non-formulaic.
- Hidden answer and first-letter constraints are explicit in package metadata.
- Autodesign tag-block schema validation passes.
