# Current Run Source-Intent Audit

Run id: `20260601_155917_full_pass_agentic_tsv`

Source of truth: `inputs/original_activity_concepts_2026-05-29.tsv`

Helper only: `inputs/source_activity_concepts.md`

Package root: `runs/20260601_155917_full_pass_agentic_tsv/activity_packages`

Created: `2026-06-01T16:11:10+08:00`

This audit compares each workbook row to the mapped run-local package files (`spec.md`, `prod.md`, and `tag_block.yaml`). It records evidence only; it does not repair package content.

## Summary

| Verdict | Count |
|---|---:|
| aligned | 12 |
| minor_adaptation | 17 |
| intent_drift | 4 |
| needs_product_decision | 7 |
| total | 40 |

## High-Risk Previous Drift Rows

| Row | Activity ID | Current verdict | Unresolved? | Evidence |
|---:|---|---|---|---|
| 15 | `concept_plant_parts_enumerate` | needs_product_decision | yes | Current package restores photo-based plant-part exploration and part-function notes, but is intentionally unsupported in downstream runtime templates. |
| 16 | `concept_plant_state_compare` | intent_drift | yes | Still omits the TSV-required state-change explanation and simple plant-care idea. |
| 20 | `concept_constellation_star_count_enumerate` | minor_adaptation | no | Prior drift is substantially repaired: choose number before reveal, show real/reference-bound card, give background fact. Remaining adaptation is a two-card pilot subset. |
| 24 | `concept_message_bottle_note_probe` | intent_drift | yes | Still weakens photographed-object warm story, physical note writing/drawing, placement, and final show/capture. |
| 28 | `concept_how_many_guess_enumerate` | intent_drift | yes | Still changes meaningful quantity-feature questions into generic visible object counting. |
| 31 | `concept_recognition_pop_probe` | intent_drift | yes | Still changes speak-target/stay-quiet timing into ordinary matching choices. |
| 32 | `concept_word_build_guess_probe` | needs_product_decision | yes | Letter guessing tied to the photographed or asked-about object may be replaced by generic clue answering without recorded product approval. |

## Row Matrix

| Row | Activity ID | Verdict | Evidence summary |
|---:|---|---|---|
| 1 | `concept_scavenger_hunt_collect` | aligned | Child collects real objects with a shared color, shape, or category; no required assets. |
| 2 | `concept_phoneme_hunt_collect` | minor_adaptation | Preserves /b/ treasure hunt and real-object photo; degraded spoken-name judgment remains an assumption. |
| 3 | `concept_branching_story_decide` | aligned | Preserves story choice points where child choices decide later story beats. |
| 4 | `concept_guided_drawing_probe` | needs_product_decision | Preserves paper drawing intent as a gate; material workflow and final-work capture need product approval. |
| 5 | `concept_word_echo_remember` | aligned | Preserves listen-and-echo word practice with voice-only fallback. |
| 6 | `concept_building_challenge_probe` | minor_adaptation | Preserves physical building but reduces evidence to child/caregiver confirmation. |
| 7 | `concept_story_unlock_probe` | minor_adaptation | Preserves story gate challenge sequence with visual unlock state as optional support. |
| 8 | `concept_coloring_game_probe` | needs_product_decision | Source promises automatic recoloring from photographed colors; static/verbal fallback needs approval. |
| 9 | `concept_classic_music_movement_probe` | needs_product_decision | Movement frame is present, but music rights/audio trigger policy remains unresolved. |
| 10 | `concept_childrens_yoga_probe` | minor_adaptation | Preserves safe pose imitation with approved pose-card dependency. |
| 11 | `concept_partial_reveal_deduce` | aligned | Requires visible partial animal cards before guessing; strong source guardrails. |
| 12 | `concept_emotion_reader_care` | minor_adaptation | Preserves feeling inference but simplifies scene/context and avoids real-person diagnosis. |
| 13 | `concept_animal_sound_motion_voice` | aligned | Preserves animal sound or role-voice imitation. |
| 14 | `concept_tiny_curator_sort` | aligned | Preserves child-defined grouping, arrangement, and explanation. |
| 15 | `concept_plant_parts_enumerate` | needs_product_decision | Restores plant-part photo sequence and function notes; downstream support is explicitly gated. |
| 16 | `concept_plant_state_compare` | intent_drift | Generic state comparison misses state-change explanation and care guidance. |
| 17 | `concept_emotion_color_outfit_probe` | needs_product_decision | Emotion-to-color choice remains, but live character outfit recoloring is fallback-dependent. |
| 18 | `concept_guess_in_10_deduce` | aligned | Preserves clue-by-clue guessing and easier hints. |
| 19 | `concept_color_mixing_collect` | minor_adaptation | Preserves color mixing but allows choosing colors instead of only photographing specified colors. |
| 20 | `concept_constellation_star_count_enumerate` | minor_adaptation | Repairs sequence and reference-bound assets; narrows to two pilot constellation cards. |
| 21 | `concept_toy_tidy_probe` | minor_adaptation | Preserves timed tidy mission and tips; after photo may reduce to confirmation fallback. |
| 22 | `concept_time_sense_probe` | aligned | Preserves elapsed-time prediction and check. |
| 23 | `concept_one_line_drawing_probe` | needs_product_decision | Physical drawing and reference display require material-workflow approval. |
| 24 | `concept_message_bottle_note_probe` | intent_drift | Generic kindness-message loop misses photographed warm story and physical placement flow. |
| 25 | `concept_award_certificate_probe` | minor_adaptation | Preserves appreciation award design; photographed-object story trigger is weaker. |
| 26 | `concept_career_decision_decide` | minor_adaptation | Strong role-first decision flow; current package is a firefighter pilot subset. |
| 27 | `concept_vegetable_sort_sort` | minor_adaptation | Sorting preserved; TSV's vegetable taxonomy teaching is weakened. |
| 28 | `concept_how_many_guess_enumerate` | intent_drift | Generic count-card loop misses meaningful feature counts such as animal legs. |
| 29 | `concept_flashcards_enumerate` | aligned | Preserves picture-card recognition and naming. |
| 30 | `concept_trivia_game_remember` | minor_adaptation | Playful recall preserved; prior topic content/output is implied rather than enforced. |
| 31 | `concept_recognition_pop_probe` | intent_drift | Matching choices replace target-pop speak/stay-quiet behavior. |
| 32 | `concept_word_build_guess_probe` | needs_product_decision | Needs approval for clue-answer simplification and weak object binding. |
| 33 | `concept_would_you_rather_compare` | aligned | Preserves funny two-choice voice-led play. |
| 34 | `concept_art_critic_tournament_probe` | minor_adaptation | Tournament preference flow preserved; rights-cleared artwork source remains a dependency. |
| 35 | `concept_color_famous_art_probe` | aligned | Preserves photographed/named color leading to approved artworks and background intro. |
| 36 | `concept_body_movement_probe` | minor_adaptation | Preserves simple safe movement imitation with card/display dependency. |
| 37 | `concept_current_topic_interview_deduce` | minor_adaptation | Opinion-and-reason interview preserved; social/current-topic background is generalized. |
| 38 | `concept_little_poem_build` | minor_adaptation | Poem co-creation preserved; runtime should bind to child's photographed/asked-about object when available. |
| 39 | `concept_travel_planner_predict` | aligned | Preserves toy/character trip planning and packing decisions. |
| 40 | `concept_quick_silly_decide` | minor_adaptation | Quick silly choices preserved; 5-7 rapid-question rhythm/countdown is under-specified. |

Full per-field evidence is recorded in `current_run_source_intent_audit.yaml`.
