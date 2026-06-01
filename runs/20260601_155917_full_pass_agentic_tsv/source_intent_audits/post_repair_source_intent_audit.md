# Post-Repair Source-Intent Audit

Run id: `20260601_155917_full_pass_agentic_tsv`

Source of truth: `inputs/original_activity_concepts_2026-05-29.tsv`

Helper only: `inputs/source_activity_concepts.md`

Package root: `runs/20260601_155917_full_pass_agentic_tsv/activity_packages`

Repair baseline: commit `553716a` (`fix(intent): repair drifted packages`)

Created: `2026-06-01T16:36:19+08:00`

This audit re-checks all 40 workbook/package rows after the source-intent text
repair. It compares the TSV source intent against run-local `spec.md`,
`prod.md`, `tag_block.yaml`, and `demo_support.yaml` evidence. It records
validation evidence only; it does not repair package content.

## Summary

| Verdict | Count |
|---|---:|
| aligned | 12 |
| minor_adaptation | 19 |
| intent_drift | 0 |
| needs_product_decision | 9 |
| total | 40 |

No `intent_drift` remains after the repair. Product-decision rows remain
`needs_product_decision` where source intent is preserved but runtime/demo
support, material workflow, asset rights, live recoloring, or state handling
needs explicit product acceptance.

## Repaired Package Before/After

| Row | Activity ID | Before | After | Post-repair evidence |
|---:|---|---|---|---|
| 16 | `concept_plant_state_compare` | intent_drift | minor_adaptation | Restores plant-state photo/discussion, visible state comparison, cautious change explanation, and simple water/light/gentle-care ideas. Minor adaptation remains because photo state judgment is degraded and `tag_block.yaml` does not explicitly carry the care-guidance promise. |
| 24 | `concept_message_bottle_note_probe` | intent_drift | needs_product_decision | Restores photographed or chosen inspiration, warm story seed, paper-and-pencil note creation, recipient, placement, and no-OCR confirmation. Runtime/material workflow support remains product-gated. |
| 28 | `concept_how_many_guess_enumerate` | intent_drift | minor_adaptation | Restores semantic feature counts such as dog legs, bicycle wheels, and flower petals instead of generic object piles. Minor adaptation remains because `tag_block.yaml` still has a stale visible-object-counting intro. |
| 31 | `concept_recognition_pop_probe` | intent_drift | needs_product_decision | Restores source target, similar distractors, mixed pop stream, say-target response, and quiet-on-distractor behavior. Timed target/distractor state is still unsupported by the current demo contract. |

## Remaining Intent Drift

None.

## Row Matrix

| Row | Activity ID | Verdict | Evidence summary |
|---:|---|---|---|
| 1 | `concept_scavenger_hunt_collect` | aligned | Preserves finding and photographing real objects with a shared color, shape, or category; no prebuilt screen asset required. |
| 2 | `concept_phoneme_hunt_collect` | minor_adaptation | Preserves /b/ treasure hunt, real-object photo capture, and spoken-name evidence; phoneme judgment remains a runtime assumption. |
| 3 | `concept_branching_story_decide` | aligned | Preserves story choice points where child decisions determine later story beats. |
| 4 | `concept_guided_drawing_probe` | needs_product_decision | Preserves paper-and-pencil guided drawing with final whole-work photo and no quality grade, gated on material workflow approval. |
| 5 | `concept_word_echo_remember` | aligned | Preserves listen-and-repeat word or phrase echo practice with voice-only fallback. |
| 6 | `concept_building_challenge_probe` | minor_adaptation | Preserves physical building and no-assessment celebration; completion evidence is child/caregiver confirmation. |
| 7 | `concept_story_unlock_probe` | minor_adaptation | Preserves fixed story gates unlocked by small challenges; visual unlock state is optional support. |
| 8 | `concept_coloring_game_probe` | needs_product_decision | Preserves photographed color-to-line-art intent, but live recoloring/static fallback needs product acceptance. |
| 9 | `concept_classic_music_movement_probe` | needs_product_decision | Preserves safe movement game framing, but music rights, audio policy, and trigger conditions remain unresolved. |
| 10 | `concept_childrens_yoga_probe` | minor_adaptation | Preserves child-safe pose imitation without camera grading; approved pose-card dependency remains. |
| 11 | `concept_partial_reveal_deduce` | aligned | Requires visible partial animal cards before guessing and keeps visual clue deduction as the main path. |
| 12 | `concept_emotion_reader_care` | minor_adaptation | Preserves feeling inference and caring response while simplifying context and avoiding real-person diagnosis. |
| 13 | `concept_animal_sound_motion_voice` | aligned | Preserves familiar animal sound or role-voice imitation. |
| 14 | `concept_tiny_curator_sort` | aligned | Preserves child-defined grouping, tiny exhibition arrangement, and explanation of the child's rule. |
| 15 | `concept_plant_parts_enumerate` | needs_product_decision | Restores photo-based plant-part exploration and function notes; downstream runtime/demo support remains gated. |
| 16 | `concept_plant_state_compare` | minor_adaptation | Repaired runtime text restores visible plant states, comparison, state-change explanation, and care guidance; demo photo judgment remains degraded. |
| 17 | `concept_emotion_color_outfit_probe` | needs_product_decision | Emotion-to-color choice remains, but live outfit recoloring or fallback acceptance needs product approval. |
| 18 | `concept_guess_in_10_deduce` | aligned | Preserves clue-by-clue guessing with easier hints. |
| 19 | `concept_color_mixing_collect` | minor_adaptation | Preserves color mixing and primary/secondary color talk, but allows choosing colors if photo collection is unavailable. |
| 20 | `concept_constellation_star_count_enumerate` | minor_adaptation | Preserves choose-number-before-reveal, reference-bound constellation cards, visible star-count practice, and background facts; narrowed to a two-card pilot subset. |
| 21 | `concept_toy_tidy_probe` | minor_adaptation | Preserves toy-area photo, timed tidy mission, organizing tips, and after confirmation while avoiding visual cleanup claims. |
| 22 | `concept_time_sense_probe` | aligned | Preserves elapsed-time prediction or sensing and check within the source time-limit frame. |
| 23 | `concept_one_line_drawing_probe` | needs_product_decision | Preserves physical one-line drawing from a reference, but material workflow and reference display require approval. |
| 24 | `concept_message_bottle_note_probe` | needs_product_decision | Repaired runtime text restores photographed inspiration, warm story, physical note creation, recipient, placement, and no-OCR confirmation; material/runtime support remains gated. |
| 25 | `concept_award_certificate_probe` | minor_adaptation | Preserves appreciation award design with paper/pencil and badge inspiration; photographed-object warm story trigger is weaker. |
| 26 | `concept_career_decision_decide` | minor_adaptation | Preserves role-first professional decision making; current package is a firefighter pilot subset. |
| 27 | `concept_vegetable_sort_sort` | minor_adaptation | Preserves vegetable sorting, but explicit vegetable taxonomy teaching is softened. |
| 28 | `concept_how_many_guess_enumerate` | minor_adaptation | Repaired runtime text restores semantic feature-count guessing; `tag_block.yaml` retains a stale visible-object-counting intro. |
| 29 | `concept_flashcards_enumerate` | aligned | Preserves reusable picture-card recognition, naming, and a tiny follow-up. |
| 30 | `concept_trivia_game_remember` | minor_adaptation | Preserves playful recall after content output, while topic binding and accumulated reward structure are implied rather than enforced. |
| 31 | `concept_recognition_pop_probe` | needs_product_decision | Repaired runtime text restores source target, similar distractors, one-card pop stream, say-target, and quiet-for-distractor behavior; timed card state remains unsupported. |
| 32 | `concept_word_build_guess_probe` | needs_product_decision | Generic word reveal is present, but object-tied letter guessing remains a product decision. |
| 33 | `concept_would_you_rather_compare` | aligned | Preserves short funny two-choice questions and tiny preference reasons. |
| 34 | `concept_art_critic_tournament_probe` | minor_adaptation | Preserves tournament preference flow; rights-cleared artwork source and state handling remain dependencies. |
| 35 | `concept_color_famous_art_probe` | aligned | Preserves child-provided color leading to approved artworks and simple background introduction. |
| 36 | `concept_body_movement_probe` | minor_adaptation | Preserves safe simple movement imitation with visual support and no detection/evaluation. |
| 37 | `concept_current_topic_interview_deduce` | minor_adaptation | Preserves opinion-and-reason interview, with social/current-topic background generalized. |
| 38 | `concept_little_poem_build` | minor_adaptation | Preserves poem co-creation, with runtime expected to bind to the child's object when available. |
| 39 | `concept_travel_planner_predict` | aligned | Preserves toy/character trip planning with packing, travel, and event/weather decisions. |
| 40 | `concept_quick_silly_decide` | minor_adaptation | Preserves quick silly binary choices; the 5-7 rapid-question countdown/drumbeat feel is under-specified. |

Full structured evidence is recorded in `post_repair_source_intent_audit.yaml`.
