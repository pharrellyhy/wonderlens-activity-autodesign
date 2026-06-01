# Product Decision Queue

Run: `20260601_155917_full_pass_agentic_tsv`

Source: `source_intent_audits/current_run_source_intent_audit.md`

These items are not accepted as source-intent drift repairs. They are package or
runtime capability decisions that need either explicit product approval or a
downstream follow-up classification before the full pass can be accepted.

| Row | Activity ID | Decision Needed |
|---:|---|---|
| 4 | `concept_guided_drawing_probe` | Approve Cat3 paper-and-pencil material workflow, final-work confirmation, and no-assessment language for runtime/demo use. |
| 8 | `concept_coloring_game_probe` | Decide whether static/verbal coloring fallback is acceptable when TSV asks for automatic recoloring from photographed colors. |
| 9 | `concept_classic_music_movement_probe` | Decide music/audio rights and trigger policy for freeze-dance/floor-is-lava style play. |
| 15 | `concept_plant_parts_enumerate` | Decide whether downstream templates can support source-faithful plant-part photo exploration and part-function explanation. |
| 17 | `concept_emotion_color_outfit_probe` | Decide whether static/verbal outfit-color fallback is acceptable when TSV asks for character outfit recoloring. |
| 23 | `concept_one_line_drawing_probe` | Approve Cat3 material workflow for one-line drawing from screen reference plus final-work confirmation. |
| 32 | `concept_word_build_guess_probe` | Decide whether clue-answer simplification is acceptable or require true object-bound letter guessing. |

## Handling Rule

- Do not silently downgrade these activities to make downstream validation pass.
- If product accepts a fallback, record the decision and rerun source-intent and
  dialogue validation with that decision as context.
- If product does not accept a fallback, route the item to package text repair,
  downstream runtime work, or blocked status with evidence.
