# Review Notes

Run id: `20260521_154053_workbook_review_packet`

## Scope And Enrichment Audit

- Scope: all 40 Sheet1 rows from `/Users/pharrelly/Downloads/活动库内部初版.xlsx`, normalized through `inputs/source_activity_concepts.md`.
- Product contract override: `minimum_unblock_allowed`.
- Run provenance: seeded from `runs/20260512_172135_batch5_unblocked`, then repaired and revalidated under this run id against the workbook source-intent snapshot.
- Existing checked-package enrichment/audit: N/A for this scoped run because workbook rows are treated as a fresh review-packet scope and run-local packages remain under this run directory.

## Existing Package Enrichment Audit

- N/A. This run uses run-local packages only; no package was promoted into canonical `activities/`.

## Generated Package Review

- Reviewer Confucius (`019e1c6e-b836-7202-9c7c-18a02620cfe9`): PASS for `concept_scavenger_hunt_collect`, `concept_phoneme_hunt_collect`, `concept_branching_story_decide`, `concept_guess_in_10_deduce`, `concept_animal_sound_motion_voice`, `concept_tiny_curator_sort`, `concept_partial_reveal_deduce`, `concept_word_echo_remember`, `concept_emotion_reader_care`, and `concept_plant_parts_enumerate`.
  - Evidence: read-only final review checked five-file contract, tag schema, scorecard placement, 10 scorecard rows, asset sections/references, T0 dialogue length, focal alignment, and brief/tag mechanic alignment. Result: all PASS.
- Reviewer Hypatia (`019e1c6e-b883-7cb2-9976-17064ebc4e0d`): PASS for `concept_color_mixing_collect`, `concept_constellation_star_count_enumerate`, `concept_career_decision_decide`, `concept_how_many_guess_enumerate`, `concept_flashcards_enumerate`, `concept_trivia_game_remember`, `concept_would_you_rather_compare`, and `concept_current_topic_interview_deduce`; initially failed `concept_plant_state_compare` and `concept_vegetable_sort_sort`.
  - Evidence: failures were narrow cross-file inconsistencies: plant input mode / mapping scorecard wording, and vegetable recap observation angle.
- Reviewer Lovelace (`019e1c7e-df5b-7640-a114-312b37488abc`): PASS re-review for repaired `concept_plant_state_compare` and `concept_vegetable_sort_sort`.
  - Evidence: verified plant brief/spec `mapping_informed` alignment, mapping scorecard PASS, vegetable tag/recap/dashboard `function` angle alignment, five-file contract, schema validity, scorecard placement/count, focal equality, brief/tag alignment, tier metadata, and package depth.
- Reviewer Hilbert (`019e1c6e-b8cb-7800-9821-dbaf2e33a05a`): PASS for `concept_little_poem_build`, `concept_travel_planner_predict`, `concept_quick_silly_decide`, `concept_coloring_game_probe`, `concept_guided_drawing_probe`, `concept_building_challenge_probe`, `concept_story_unlock_probe`, `concept_classic_music_movement_probe`, `concept_childrens_yoga_probe`, and `concept_emotion_color_outfit_probe`.
  - Evidence: read-only final review checked five-file contract, tag schema, scorecard placement/count, brief/tag mechanic/focal/angle alignment, dashboard focal alignment, asset references/timelines, extensibility notes, resolved blocker coverage, and T0 dialogue constraints. Result: all PASS.
- Reviewer Planck (`019e1c6e-b917-7983-b3ab-0811daf4613e`): PASS for `concept_toy_tidy_probe`, `concept_time_sense_probe`, `concept_one_line_drawing_probe`, `concept_message_bottle_note_probe`, `concept_award_certificate_probe`, `concept_recognition_pop_probe`, `concept_word_build_guess_probe`, `concept_art_critic_tournament_probe`, `concept_color_famous_art_probe`, and `concept_body_movement_probe`.
  - Evidence: read-only final review checked five-file contract, tag schema, activity_id/focal alignment, scorecard placement and rows, resolved blocker visibility, asset timeline/fallback coherence, mechanic fidelity, package depth, and strict T0 dialogue length where applicable. Result: all PASS.

## Repairs Made After Reviewer Findings

- Repaired `concept_story_unlock_probe` so the runtime beats tell short story segments before each unlock challenge.
- Repaired `concept_career_decision_decide` so the child assumes a profession before facing the work scenario.
- Repaired `concept_toy_tidy_probe` so the mechanic is a physical tidy sprint with timer/tips/after-state confirmation instead of a verbal grouping map.
- Repaired `concept_coloring_game_probe` metadata and recap language so the minimum-contract fallback remains a photo-color-to-region plan without claiming unsupported recoloring.
- Tightened T0-supported dialogue to respect the `program.md` T0 sentence-length floor.
- Corrected stale scaffold references in specs after pillar/game-style repairs.
- Aligned optional asset and UI capability flags with voice-only or no-display fallback wording.
- Removed over-broad T0 routing support from T1 package metadata so richer T1 dialogue is not exposed to T0 routing.
- Added explicit fallback language where prod beats referenced optional or resolved visual assets.
- Aligned plant-state mapping-informed brief/spec wording and scorecard Dimension 8.
- Aligned vegetable sort observation angle across tag, dashboard, recap, and adaptation brief.

## Final Outcome

- Generated packages: 40.
- Enriched packages: 0.
- Audited no-op packages: 0.
- Blocked assignments: 0.
- Resolved blockers: present only as product-contract override annotations; they are visible in affected specs/prods and should be reviewed as resolved dependency callouts, not failures.
- Reviewer-agent coverage: all 40 seed packages have independent final PASS evidence; repaired rows were additionally checked by source-intent audit and regenerated reviewer exports.

## Residual Risks

- The run assumes `product_contract_override=minimum_unblock_allowed`; packages with resolved blocker annotations depend on product acceptance of the documented minimum policies and fallback behavior.
- Required prebuilt/display assets are specified as metadata and prompts/sources only. This run does not generate image files or verify an external asset pipeline.
- Run-local packages are not promoted to canonical `activities/` directories; consumers should use the run-local `package_path` values unless a later promotion step is requested.

## Next Actions

- No package-content repair is pending for this run.
- If these packages should become canonical, run an explicit promotion workflow from `runs/20260521_154053_workbook_review_packet/activity_packages/` into `activities/`.
