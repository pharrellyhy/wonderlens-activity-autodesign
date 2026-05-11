# Review Notes

Run id: `20260511_144424_activity_concepts`

## Existing Package Enrichment Audit

- Reviewer Carson (`019e15c8-8918-7072-b92d-6173a529072b`): PASS
  - Scope: 12 checked concept packages: `concept_scavenger_hunt_collect`, `concept_phoneme_hunt_collect`, `concept_branching_story_decide`, `concept_guess_in_10_deduce`, `concept_animal_sound_motion_voice`, `concept_tiny_curator_sort`, `concept_partial_reveal_deduce`, `concept_word_echo_remember`, `concept_emotion_reader_care`, `concept_plant_parts_enumerate`, `concept_plant_state_compare`, `concept_color_mixing_collect`.
  - Repairs: `concept_emotion_reader_care`, `concept_plant_state_compare`, and `concept_color_mixing_collect` were repaired so Step 3 repeatedly performs the declared `care`, `compare`, and `collect` mechanics.
  - Evidence commit: `61c56b9 fix(activities): align concept mechanics`.
  - Checks: five-file package contract, targeted tag-block schema validation, directory-name/activity-id match, scorecard placement, dashboard focal alignment, Step 1-5 presence, placeholder scan, asset reference coherence, and `git diff --check` on assigned directories all passed.
  - Residual risk: static package review only; runtime prompt execution and actual optional/prebuilt asset availability were not simulated.

- Reviewer Copernicus (`019e15c8-8964-73f2-8361-54645c0cac02`): PASS
  - Scope: 11 checked concept packages: `concept_constellation_star_count_enumerate`, `concept_career_decision_decide`, `concept_vegetable_sort_sort`, `concept_how_many_guess_enumerate`, `concept_flashcards_enumerate`, `concept_trivia_game_remember`, `concept_would_you_rather_compare`, `concept_current_topic_interview_deduce`, `concept_little_poem_build`, `concept_travel_planner_predict`, `concept_quick_silly_decide`.
  - Repairs: `concept_flashcards_enumerate`, `concept_current_topic_interview_deduce`, `concept_travel_planner_predict`, and `concept_quick_silly_decide` were repaired for T0 round-count compliance, prediction commit-before-reveal fidelity, deduce clue-to-conclusion fidelity, and synchronized spec/tag/recap wording.
  - Evidence commit: `593bef5 fix(activities): repair concept depth`.
  - Checks: assigned-package schema validation, focused package-depth/alignment script, exact five-file contract, scorecard placement, Step 1/2/4/5 labels, Step 3 round-count/detail checks, tag/dashboard/recap focal and mechanic alignment, and `git diff --check HEAD~1..HEAD` all passed.
  - Residual risk: no package-level residual risks found in the assigned scope.

Summary: 23 checked concept packages were audited, 7 were repaired, and 16 required no edits.

## Blocked Assignments

This run revisits the 17 still-unchecked capability probes and creates constrained blocked design previews under `runs/20260511_144424_activity_concepts/blocked_designs/`. These previews are not valid runtime packages and keep every row unchecked until the relevant product/design constraints are resolved.

- `001` concept_coloring_game_probe: Confirm runtime image generation support and safety review for child-facing generated assets.; Define coloring or recoloring UI behavior, selectable regions, state storage, and fallback behavior.; Define UI state storage, progress memory, and resume/reset behavior.
- `002` concept_guided_drawing_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.
- `003` concept_building_challenge_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.
- `004` concept_story_unlock_probe: Define UI state storage, progress memory, and resume/reset behavior.
- `005` concept_classic_music_movement_probe: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.
- `006` concept_childrens_yoga_probe: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `007` concept_emotion_color_outfit_probe: Define coloring or recoloring UI behavior, selectable regions, state storage, and fallback behavior.; Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `008` concept_toy_tidy_probe: Define UI state storage, progress memory, and resume/reset behavior.; Define before/after capture or parent confirmation; do not infer completion from one photo.
- `009` concept_time_sense_probe: Define UI state storage, progress memory, and resume/reset behavior.
- `010` concept_one_line_drawing_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `011` concept_message_bottle_note_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.; Define whether OCR or note reading is supported; otherwise avoid claiming to read child writing.
- `012` concept_award_certificate_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.
- `013` concept_recognition_pop_probe: Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `014` concept_word_build_guess_probe: Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `015` concept_art_critic_tournament_probe: Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `016` concept_color_famous_art_probe: Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `017` concept_body_movement_probe: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.

## Residual Risks

- All 17 unchecked capability probes remain blocked because the source rows still declare unresolved product capabilities such as runtime image generation, coloring UI, Cat3 material workflow, UI state, asset display, motion safety, before/after evidence, or OCR/text handling.
- The constrained previews are review artifacts only; they do not create valid `activities/` packages or `results.tsv` rows.
- Static package review does not prove runtime prompt execution or actual asset availability; it verifies file contracts, metadata/schema alignment, and design-depth requirements.

## Next Actions

- Product/design owners can resolve individual constraints, then rerun or promote the corresponding constrained preview through the normal five-file package gates.
- Use `review.html` to sort blocked probes by reason type and inspect each constrained preview's inline `BLOCKED ELEMENT` comments before deciding which constraints to resolve first.
