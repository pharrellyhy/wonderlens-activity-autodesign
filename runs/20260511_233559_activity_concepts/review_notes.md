# Review Notes

Run id: `20260511_233559_activity_concepts`

## Existing Package Enrichment Audit

- Reviewer A (`019e17af-7861-7e22-8eab-9d43ef3f0a1f`): PASS
  - Scope: 12 checked concept packages: `concept_scavenger_hunt_collect`, `concept_phoneme_hunt_collect`, `concept_branching_story_decide`, `concept_guess_in_10_deduce`, `concept_animal_sound_motion_voice`, `concept_tiny_curator_sort`, `concept_partial_reveal_deduce`, `concept_word_echo_remember`, `concept_emotion_reader_care`, `concept_plant_parts_enumerate`, `concept_plant_state_compare`, `concept_color_mixing_collect`.
  - Repairs: `concept_word_echo_remember` T0 round count; optional-asset wording in `concept_word_echo_remember`, `concept_emotion_reader_care`, and `concept_color_mixing_collect`; YAML quoting repair in `concept_color_mixing_collect/recap.template.yaml` after parent validation found an invalid plain scalar.
  - Evidence commits: `290b1eb fix(activity): align concept audits`; final YAML repair pending in this run commit.
  - Evidence: Reviewer A audited 12 assigned concept packages against the current migrated package depth floor and package contracts. All 12 PASS after minimal repairs to `concept_word_echo_remember` T0 round count and optional-asset wording in `concept_word_echo_remember`, `concept_emotion_reader_care`, and `concept_color_mixing_collect`. Recheck confirmed five-file layout, tag schema validity, YAML parse, scorecard placement, no prod scorecards, dashboard focal alignment, asset reference coherence, expanded Step 3 rounds, and mechanic fidelity.

- Reviewer B (`019e17af-789f-7e43-a6f9-1dee48392003`): PASS
  - Scope: 11 checked concept packages: `concept_constellation_star_count_enumerate`, `concept_career_decision_decide`, `concept_vegetable_sort_sort`, `concept_how_many_guess_enumerate`, `concept_flashcards_enumerate`, `concept_trivia_game_remember`, `concept_would_you_rather_compare`, `concept_current_topic_interview_deduce`, `concept_little_poem_build`, `concept_travel_planner_predict`, `concept_quick_silly_decide`.
  - Repairs: `concept_little_poem_build` Step 4 poem reveal and screen-state specificity.
  - Evidence commit: `e35789a fix(activity): clarify poem reveal`.
  - Evidence: Reviewer B audited 11 assigned concept packages against the migrated package depth floor. All 11 PASS after one minimal package-local repair in `activities/concept_little_poem_build/`: Step 4 now includes a concrete four-line poem reveal and matching screen state, with the spec scorecard note updated. Checks confirmed exactly five files per package, schema-valid tag blocks, correct scorecard placement, no scorecard in prod, focal/mechanic alignment across tag/recap/dashboard, defined asset refs, expanded Step 3 rounds, concrete Step 1-5 runtime detail, and 10-dimension scorecard evidence.

Summary: 23 checked concept packages were audited, 4 were enriched, and 19 required no edits.

## Generated Package Reviews

Batch 5 fresh-rerun generation-ready rows reused the same stable `activity_id` packages after current-run reviewer audit and repairs. All 23 generated rows have independent PASS evidence from Reviewer A or Reviewer B before `results.tsv` logging and assignment checkoff. The generated package entries in `run_manifest.yaml` link each row to its current adaptation brief and package directory.

## Blocked Assignments

This run snapshot contains 34 blocked capability-probe rows: 17 original Batch 4 probes plus 17 duplicate Batch 5 fresh-rerun probes. Each row receives its own run-local blocked brief and constrained design preview. These previews are not valid runtime packages and keep the rows unchecked until the relevant product/design constraints are resolved.

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
- `041` concept_coloring_game_probe: Confirm runtime image generation support and safety review for child-facing generated assets.; Define coloring or recoloring UI behavior, selectable regions, state storage, and fallback behavior.; Define UI state storage, progress memory, and resume/reset behavior.
- `042` concept_guided_drawing_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.
- `043` concept_building_challenge_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.
- `044` concept_story_unlock_probe: Define UI state storage, progress memory, and resume/reset behavior.
- `045` concept_classic_music_movement_probe: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.
- `046` concept_childrens_yoga_probe: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `047` concept_emotion_color_outfit_probe: Define coloring or recoloring UI behavior, selectable regions, state storage, and fallback behavior.; Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `048` concept_toy_tidy_probe: Define UI state storage, progress memory, and resume/reset behavior.; Define before/after capture or parent confirmation; do not infer completion from one photo.
- `049` concept_time_sense_probe: Define UI state storage, progress memory, and resume/reset behavior.
- `050` concept_one_line_drawing_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `051` concept_message_bottle_note_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.; Define whether OCR or note reading is supported; otherwise avoid claiming to read child writing.
- `052` concept_award_certificate_probe: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.; Define before/after capture or parent confirmation; do not infer completion from one photo.
- `053` concept_recognition_pop_probe: Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `054` concept_word_build_guess_probe: Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `055` concept_art_critic_tournament_probe: Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `056` concept_color_famous_art_probe: Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `057` concept_body_movement_probe: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.

## Review Criteria

All generated, enriched, and audited packages are judged against `program.md` Phase 3's 10-dimension rubric: V1 Technical Compliance, Hook & Transition, Edge Case Coverage, IB Completeness, Tier Appropriateness, Dialogue Specificity, Screen & UI Completeness, Entity Mapping Alignment, Game Feel, and Mechanic Fidelity + Scaffold Honesty. Dimension 8 may be N/A when the package is not mapping-informed. Passing means every applicable dimension is PASS and the package also meets the migrated package depth floor: `spec.md` is decision-useful, `prod.md` is runnable without inventing beats, metadata files align, and reviewer uncertainty has been resolved.

This run uses the same 10-dimension validation as before. The per-package `spec.md` scorecard is parsed into `review.html` so each package detail dialog lists the result and the note explaining why.

## Residual Risks

- All 34 capability-probe rows remain blocked because the source rows still declare unresolved product capabilities such as runtime image generation, coloring UI, Cat3 material workflow, UI state, asset display, motion safety, before/after evidence, or OCR/text handling.
- The constrained previews are review artifacts only; they do not create valid `activities/` packages or `results.tsv` rows.
- Static package review does not prove runtime prompt execution or actual asset availability; it verifies file contracts, metadata/schema alignment, and design-depth requirements.

## Next Actions

- Product/design owners can resolve individual constraints, then rerun or promote the corresponding constrained preview through the normal five-file package gates.
- Use `review.html` to sort blocked probes by reason type and inspect each constrained preview's inline `BLOCKED ELEMENT` comments before deciding which constraints to resolve first.
