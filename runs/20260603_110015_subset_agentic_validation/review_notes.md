# Review Notes - 20260603_110015_subset_agentic_validation

## Scope

Only the five rows under `## 2026-06-03 Subset Agentic Validation` were snapshotted and generated.

## Initial Package Review

- PASS: five run-local package directories created under `activity_packages/`.
- PASS: each package has the five canonical files plus `demo_support.yaml` and `asset_manifest.yaml`.
- PASS: `prod.md` files avoid raw blocker leakage markers.
- PASS: package writing is text-only; binary source images are in `generated_assets/inbox/` or package-local reference source directories for the post-package asset phase.

## Pending Gates

Asset builder, structural validators, consumer conversion, dialogue QA, image QA, final review, assignment/results updates, and commit remain pending.

## Image QA

Status: PASS after image-owned repairs.

Repairs made:

- Scavenger Hunt and Phoneme Hunt standard beat scenes were redrawn to avoid repeated generic imagery.
- Phoneme Hunt now includes a text-free optional `b_sound_letter_cue` backing; the runtime owns any `/b/` or B overlay.
- Constellation early scenes and activity icon were redrawn to avoid revealing a countable constellation before the child chooses a number.
- Guided Drawing intro/rules scenes were redrawn to show blank paper and pencil before the drawing steps.
- Recognition Pop scenes were redrawn as abstract backgrounds that do not duplicate target or distractor sprites.

Evidence: `generated_assets/image_qa_review.yaml`, `generated_assets/review_contact_sheets/`, rebuilt package-local PNGs including `b_sound_letter_cue__round_512.png`, and passing asset validators.
