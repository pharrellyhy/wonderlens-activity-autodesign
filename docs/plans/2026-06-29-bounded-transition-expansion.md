# Bounded Transition Expansion

Status: Completed

## Problem

Emotion Reader now uses package-owned transition briefs with bounded runtime
Speaker generation, but the other reviewed packages still rely on exact scripts
or runtime hardcoded photo feedback. That keeps dialogue brittle and makes live
QA iteration mix package intent with runtime behavior.

## Scope

- Add bounded transition briefs to `concept_animal_sound_motion_voice`.
- Add bounded transition briefs to `concept_partial_reveal_deduce`, preserving
  the no-answer-leak rule before final reveal.
- Add explicit first-letter photo feedback transitions to
  `concept_phoneme_hunt_collect` while keeping CAT5 verification deterministic.
- Keep all changes package-local in this repo; no new display-layout contract.

## Validation

- Validate changed package metadata against the activity schema and demo package
  contract.
- Confirm WonderLens AI regenerates matching `runtime.yaml` files from these
  package definitions.
- Run the focused live matrix in WonderLens AI for the three packages.

## Result

- Added package-owned transition briefs for animal sound, partial reveal, and
  first-letter photo hunt.
- WonderLens AI regenerated matching runtime YAML and passed the focused schema,
  generator, unit, and corrected source-env live Activity WS checks.
