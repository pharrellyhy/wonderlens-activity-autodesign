# Message Bottle Note - Engineering Spec

## Metadata

- activity_id: `concept_message_bottle_note_probe`
- source_row: `24`
- source_concept: `source_message_bottle_note`
- assignment_type: `capability_probe`
- category: `cat3`
- mechanic: `care`
- generation_method: `fresh_full_rerun_from_source_snapshot`

## Premise

The child starts from a photographed object or chosen inspiration, hears a warm tiny story about it, chooses a word or drawing for a parent or friend, physically writes or draws a paper note with pencil, and places it somewhere kind such as a pillow, desk, or school bag.

## Selection Trigger

Parent starts a writing or kindness-note activity and the child has a photographed object or chosen inspiration plus paper and pencil or crayons.

## Source Intent Lock

Preserve the warm physical-note frame: start from the child's photographed object or chosen inspiration, tell a short warm story, invite the child to write or draw a kindness note for a parent or friend, and suggest a real placement such as pillow, desk, or school bag. Do not reduce this to only naming a recipient or saying kind words.

## Adaptation Rationale

The package preserves the original play frame, child role, required child action, and runtime sequence. Category and mechanic labels are metadata, not replacements for the workbook promise.

## Runtime Detail Floor Notes

- Use `Runtime AI instruction` plus `Example AI line` so runtime can adapt wording while preserving intent.
- Do not claim unsupported sensing, recoloring, pose detection, cleanup verification, OCR, or hidden state.
- Keep the repeated child action aligned to `care`: choose recipient, choose words or drawing, make the physical note, place or plan where to leave it, and confirm by child/caregiver report.
- Preserve this source sequence: photographed inspiration story, paper-and-pencil note creation, real placement for parent/friend, optional show/capture by confirmation only.

## Resolved Product Contract Notes

- Cat3 material workflow: Approved minimum contract uses caregiver setup, child self-report, and no-assessment physical-work language.
- Before/after evidence: Approved minimum evidence policy uses child or caregiver confirmation and never infers completion quality from photos.
- OCR or text handling: Approved minimum text policy asks the child to speak or choose text and does not verify handwriting or OCR correctness.

## Asset Usage Timeline

No prebuilt visual asset dependency. The activity depends on real-world paper/pencil materials and a photographed or chosen inspiration; the runtime must not claim OCR, handwriting recognition, or final-photo quality assessment.

## Extensibility Summary

Reusable by replacing the topic, scene, role, or approved asset set while preserving the source play frame and `care` mechanic.

## Extensibility Notes

- Replace `{runtime_entity}` only when the new trigger supports the same child action.
- Keep the same source sequence before changing category or mechanic labels.
- If an asset ID changes, preserve display timing, fallback wording, and safety constraints.

## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|---|---|---|
| 1 | V1 Technical Compliance | PASS | Fallbacks are explicit and unsupported capability is not overclaimed. |
| 2 | Hook & Transition | PASS | Opening uses the workbook trigger and play frame. |
| 3 | Edge Case Coverage | PASS | Ideal, unexpected, and no-response branches are present. |
| 4 | IB Completeness | PASS | KUD and concepts match the child action. |
| 5 | Tier Appropriateness | PASS | Prompts are short and scaffolded. |
| 6 | Dialogue Specificity | PASS | Runtime AI instructions include example lines. |
| 7 | Screen & UI Completeness | PASS | Each beat names screen, state, asset, or fallback. |
| 8 | Entity Mapping Alignment | N/A | Workbook-source concept run; not mapping-informed. |
| 9 | Game Feel | PASS | Progress tokens and payoff create game structure. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | The repaired package restores photographed inspiration, physical note creation, placement, and no-OCR confirmation. |

**Overall**: PASS - fresh full-run package preserves source intent with explicit runtime-generation and minimum-unblock assumptions.
