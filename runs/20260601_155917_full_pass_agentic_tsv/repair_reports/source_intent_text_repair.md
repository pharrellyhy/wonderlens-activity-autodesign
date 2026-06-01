# Source Intent Text Repair

Run id: `20260601_155917_full_pass_agentic_tsv`

Scope: four current-run packages marked `intent_drift` in `source_intent_audits/current_run_source_intent_audit.md`.

Source baseline: `inputs/original_activity_concepts_2026-05-29.tsv` rows 16, 24, 28, and 31. `inputs/source_activity_concepts.md` was used only as helper text where it preserved the TSV intent.

## Repairs

| Source row | Activity ID | Repair summary |
|---:|---|---|
| 16 | `concept_plant_state_compare` | Replaced generic comparison with photo/discussion-based plant leaf state comparison. Runtime now asks the child to notice green/yellow/damaged/blooming/wilting evidence, explains likely visible state changes cautiously, and gives simple plant-care guidance without hidden-health diagnosis. |
| 24 | `concept_message_bottle_note_probe` | Restored photographed-object inspiration, warm story seed, physical paper-and-pencil note creation, parent/friend placement, and child/caregiver confirmation. Runtime explicitly avoids OCR, handwriting-reading, and photo-quality claims. |
| 28 | `concept_how_many_guess_enumerate` | Replaced generic visible-object counting with semantic feature-count guessing: animal legs, object wheels/buttons, and petals. Cards are now framed as feature cards rather than unrelated count piles. |
| 31 | `concept_recognition_pop_probe` | Replaced ordinary matching with source-target recognition-pop timing: source target such as dog, similar animals such as fox/wolf, mixed timed cards, say target word on target, and stay quiet for distractors. |

## Files Changed

- `activity_packages/concept_plant_state_compare/spec.md`
- `activity_packages/concept_plant_state_compare/prod.md`
- `activity_packages/concept_plant_state_compare/demo_support.yaml`
- `activity_packages/concept_message_bottle_note_probe/spec.md`
- `activity_packages/concept_message_bottle_note_probe/prod.md`
- `activity_packages/concept_message_bottle_note_probe/demo_support.yaml`
- `activity_packages/concept_how_many_guess_enumerate/spec.md`
- `activity_packages/concept_how_many_guess_enumerate/prod.md`
- `activity_packages/concept_how_many_guess_enumerate/demo_support.yaml`
- `activity_packages/concept_how_many_guess_enumerate/asset_manifest.yaml`
- `activity_packages/concept_recognition_pop_probe/spec.md`
- `activity_packages/concept_recognition_pop_probe/prod.md`
- `activity_packages/concept_recognition_pop_probe/demo_support.yaml`
- `activity_packages/concept_recognition_pop_probe/asset_manifest.yaml`

## Product-Decision Gaps Not Fixed

- `concept_message_bottle_note_probe` remains marked unsupported for the current demo because real material workflow, physical placement, and note evidence handling need product/runtime support.
- `concept_recognition_pop_probe` remains marked unsupported for the current demo because target-vs-distractor timed card state is required; the repair intentionally does not convert it into ordinary dialogue matching.
- `concept_plant_state_compare` remains degraded for demo use because current runtime cannot reliably judge plant state from photos; runtime text uses visible clues and child/caregiver confirmation.

## Re-Audit Readiness

The repaired `prod.md` files now include runtime behavior contracts with goal/action, constraints, tone, progress evidence, branch behavior, frame/source guardrails, concrete example lines, and screen states for each runtime beat. These packages are ready for a fresh source-intent re-audit.
