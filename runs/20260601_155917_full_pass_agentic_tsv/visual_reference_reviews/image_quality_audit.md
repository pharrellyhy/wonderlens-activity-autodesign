# Image Quality Audit

Run: `20260601_155917_full_pass_agentic_tsv`
Audited after commits: `6eae5f4`, `0e517f1`
Role: independent image quality validator
Scope: built package-local runtime PNGs under `activity_packages/*/assets/*__round_512.png`

## Verdict

Overall verdict: **fail**

Counts:

| Verdict | Count |
| --- | ---: |
| pass | 29 |
| needs_repair | 1 |
| product_decision | 1 |
| total | 31 |

Evidence:

- `image_quality_contact_sheet.png` contains all 31 built PNGs in sorted path order.
- `identify` reported `512x512` for every built PNG.
- Alpha extraction reported `1,1` min/max for every built PNG, so the PNGs are fully opaque.
- All four reference-bound assets have accepted source metadata with `storage_allowed: true`.

## Non-Pass Assets

| Asset | Verdict | Reason | Recommendation |
| --- | --- | --- | --- |
| `concept_art_critic_tournament_probe/artwork_tournament_set_01` | needs_repair | Accepted public-domain source metadata exists, but the runtime PNG includes visible printed cartouche text and a white/gray artwork border. It also behaves like a single artwork while the manifest/prod beat asks for artwork pairs or tournament comparison support. | Rebuild from accepted reference material with crop/curation that removes readable cartouche text and border if allowed by the art-use policy; add or compose approved comparison artwork only if the product contract requires a visible pair. |
| `concept_recognition_pop_probe/recognition_challenge_cards_01` | product_decision | The image is visually clean and the dog plus two quiet animal silhouettes supports the target/distractor timing challenge. The open question is product intent: it is a one-file composite, while the style contract usually discourages combined multi-image source assets and prod says three cards appear. | Product should approve the single composite as the intended timing display, or request separate target and distractor card assets for dog, fox, and wolf. |

## Per-Asset Results

| # | Activity | Asset | Verdict | Reason |
| ---: | --- | --- | --- | --- |
| 1 | `concept_animal_sound_motion_voice` | `animal_sound_cards_01` | pass | Readable centered dog cue matches the animal imitation preview and flat Nordic style; no text or forbidden framing. |
| 2 | `concept_art_critic_tournament_probe` | `artwork_tournament_set_01` | needs_repair | Visible printed cartouche text and artwork border; source is accepted but the runtime image violates the no-text/no-border audit rule. |
| 3 | `concept_award_certificate_probe` | `award_inspiration_badges_01` | pass | Badge ideas are clear, centered, child-safe, and style-aligned; no text, labels, or logos. |
| 4 | `concept_body_movement_probe` | `body_movement_cards_01` | pass | Simple movement pose is readable and aligns with safe movement prompts. |
| 5 | `concept_building_challenge_probe` | `building_reference_cards_01` | pass | Block-build target is centered, simple, and matches the hands-on construction cue. |
| 6 | `concept_career_decision_decide` | `firefighter_role_card` | pass | Inclusive firefighter helper character is non-emergency, readable, and style-aligned. |
| 7 | `concept_childrens_yoga_probe` | `childrens_yoga_pose_cards_01` | pass | Calm seated pose matches age-safe yoga support and stays centered. |
| 8 | `concept_color_famous_art_probe` | `color_artwork_set_01` | pass | Accepted public-domain artwork source is used without visible labels or invented factual content. |
| 9 | `concept_color_mixing_collect` | `color_mixing_board_01` | pass | Two color spots visibly combine into a result spot, matching the prediction beat. |
| 10 | `concept_coloring_game_probe` | `runtime_coloring_line_art_01` | pass | Line-art plant and palette cue support the coloring beat and are readable. |
| 11 | `concept_constellation_star_count_enumerate` | `cassiopeia_five_star_card` | pass | Accepted internal reference preserves exactly five prominent guide stars and approved guide-line geometry. |
| 12 | `concept_constellation_star_count_enumerate` | `orion_seven_star_card` | pass | Accepted internal reference preserves exactly seven prominent guide stars and approved guide-line geometry. |
| 13 | `concept_emotion_color_outfit_probe` | `emotion_color_character_01` | pass | Character and color swatches support the emotion-color outfit beat while staying text-free. |
| 14 | `concept_emotion_reader_care` | `emotion_expression_cards_01` | pass | Facial expression cue is clear at runtime size and aligns with evidence-based emotion reading. |
| 15 | `concept_flashcards_enumerate` | `generic_flashcard_library_01` | pass | Picture-first apple flashcard is simple, readable, and intentionally framed as a card object. |
| 16 | `concept_guess_in_10_deduce` | `guess_reference_cards_01` | pass | Turtle reference picture is readable and suitable for optional clue support. |
| 17 | `concept_how_many_guess_enumerate` | `how_many_count_cards_01` | pass | Vehicle card provides a meaningful count-feature target with wheels visible. |
| 18 | `concept_one_line_drawing_probe` | `one_line_drawing_cards_01` | pass | Single-line snail target is centered, clean, and readable for a drawing prompt. |
| 19 | `concept_partial_reveal_deduce` | `elephant_trunk_reveal_card` | pass | Partial trunk and ear-edge clue matches the final reveal beat without showing the full animal. |
| 20 | `concept_partial_reveal_deduce` | `rabbit_ears_reveal_card` | pass | Rabbit ears and small head hint match the partial-reveal prompt. |
| 21 | `concept_partial_reveal_deduce` | `tiger_tail_reveal_card` | pass | Striped tail clue is the only animal evidence shown and supports the tiger deduction beat. |
| 22 | `concept_phoneme_hunt_collect` | `ball_b_sound_clue` | pass | Single ball object clue is centered, readable, and letter-free. |
| 23 | `concept_phoneme_hunt_collect` | `banana_b_sound_clue` | pass | Single banana object clue is centered, readable, and letter-free. |
| 24 | `concept_quick_silly_decide` | `quick_silly_countdown_01` | pass | Hourglass countdown cue is playful, text-free, and contains no numbers. |
| 25 | `concept_recognition_pop_probe` | `recognition_challenge_cards_01` | product_decision | Multiple animal silhouettes are acceptable for the timing concept only if product approves the one-file composite display. |
| 26 | `concept_story_unlock_probe` | `story_unlock_cards_01` | pass | Locked story door/token cue matches the unlock beat and remains text-free. |
| 27 | `concept_travel_planner_predict` | `travel_planning_cards_01` | pass | Suitcase, map, and travel items support pretend trip planning choices without labels or logos. |
| 28 | `concept_trivia_game_remember` | `trivia_reward_board_01` | pass | Reward board/progress cue is readable and text-free. |
| 29 | `concept_vegetable_sort_sort` | `vegetable_sort_cards_01` | pass | Vegetable card content supports sorting and uses an intentional card frame without text. |
| 30 | `concept_word_build_guess_probe` | `word_growth_ui_01` | pass | Blank tile growth surface supports word reveal without letters, numbers, or labels. |
| 31 | `concept_word_echo_remember` | `word_echo_cards_01` | pass | Banana picture cue is simple, readable, centered, and text-free. |

## Notes

- The `recognition_challenge_cards_01` multiple-animal composition is not treated as an image-quality failure by itself because the manifest asks for a target animal plus similar distractors and prod says three cards appear. It remains a product decision because the asset is a single composite rather than separate target/distractor runtime files.
- The Hokusai artwork source metadata is accepted; the failure is runtime presentation against this audit's no readable text and no border criteria.
