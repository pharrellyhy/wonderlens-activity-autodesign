# Review Notes

Run id: `20260510_152725_activity_concepts`

## Existing Package Enrichment Audit

Reviewer-agent pass added on 2026-05-11 for the seven older checked concept packages that were previously audited as no-op.

- Reviewer C: Gibbs (`019e14c5-502c-7903-9ca8-9e6827749fd4`)
  - Scope: `concept_scavenger_hunt_collect`, `concept_phoneme_hunt_collect`, `concept_branching_story_decide`, `concept_guess_in_10_deduce`.
  - Outcome: final package contract PASS for all four assigned packages.
  - Repairs: updated scorecard overall lines to record reviewer-agent evidence; tightened `concept_branching_story_decide` Step 3 follow-ups so each ideal branch names the specific consequence for the selected option.
  - Reviewer checks reported: file-count check PASS, scorecard placement PASS, tag/dashboard focal match PASS, placeholder/forbidden scan clean, full tag-block schema validation PASS, and scoped `git diff --check` PASS.
- Reviewer D: Aristotle (`019e14c5-8586-7433-a20c-6f1df5c6afa5`)
  - Scope: `concept_animal_sound_motion_voice`, `concept_tiny_curator_sort`, `concept_partial_reveal_deduce`.
  - Outcome: final package contract PASS for all three assigned packages.
  - Repairs: updated scorecard overall lines to record reviewer-agent evidence; no runtime/prod/tag/template content changes were needed.
  - Reviewer checks reported: file-count check PASS, scorecard placement PASS, tag/dashboard focal match PASS, targeted placeholder/forbidden scan clean, full tag-block schema validation PASS, and scoped `git diff --check` PASS.

Reviewed older package outcomes:

- `concept_scavenger_hunt_collect`: reviewer-agent PASS after quality review by Reviewer C.
- `concept_phoneme_hunt_collect`: reviewer-agent PASS after quality review by Reviewer C.
- `concept_branching_story_decide`: reviewer-agent PASS after quality edit by Reviewer C.
- `concept_guess_in_10_deduce`: reviewer-agent PASS after quality review by Reviewer C.
- `concept_animal_sound_motion_voice`: reviewer-agent PASS after quality review by Reviewer D.
- `concept_tiny_curator_sort`: reviewer-agent PASS after quality review by Reviewer D.
- `concept_partial_reveal_deduce`: reviewer-agent PASS after quality review by Reviewer D.

## Generated Package Review

Reviewer-agent pass added on 2026-05-11.

- Reviewer A: Dalton (`019e14a9-b67d-7430-95a3-840b60797764`)
  - Scope: `concept_word_echo_remember`, `concept_emotion_reader_care`, `concept_plant_parts_enumerate`, `concept_plant_state_compare`, `concept_color_mixing_collect`, `concept_constellation_star_count_enumerate`, `concept_career_decision_decide`, `concept_vegetable_sort_sort`.
  - Outcome: edited all eight packages; final package contract PASS after reviewer checks.
  - Repairs: replaced templated runtime dialogue with activity-specific hooks, rules, branch follow-ups, magic moments, and IB closings; made KUD language concrete in `prod.md` and `tag_block.yaml`; updated recap copy to reflect earned moments; fixed no-asset plant spec references; changed color mixing asset type to canonical `ui_overlay`; corrected constellation and vegetable asset-brief round references.
  - Reviewer checks reported: full tag-block schema validation PASS, placeholder/forbidden-text scan clean, `git diff --check` on assigned dirs PASS, and each assigned package has exactly five files.
- Reviewer B: Averroes (`019e14a9-e2b2-7200-8e82-cb0b42da8d16`)
  - Scope: `concept_how_many_guess_enumerate`, `concept_flashcards_enumerate`, `concept_trivia_game_remember`, `concept_would_you_rather_compare`, `concept_current_topic_interview_deduce`, `concept_little_poem_build`, `concept_travel_planner_predict`, `concept_quick_silly_decide`.
  - Outcome: edited all eight packages; final package contract PASS after reviewer checks.
  - Repairs: replaced generic KUD lines with activity-specific knowledge, understanding, and child actions; strengthened Step 3 branch follow-ups with concrete evidence, redirects, and mechanic-specific scaffolds; tightened T0 dialogue; fixed no-asset spec language; normalized asset brief rows; replaced non-vocabulary ATL token `communication` with `language_expression`; fixed YAML indentation.
  - Reviewer checks reported: full tag-block schema validation PASS, assigned package structural/template check PASS, targeted thin-marker/stale-token scan clean, and assigned-dir status stayed within scope.

Reviewed package outcomes:

- `concept_word_echo_remember`: reviewer-agent PASS after quality edits by Reviewer A.
- `concept_emotion_reader_care`: reviewer-agent PASS after quality edits by Reviewer A.
- `concept_plant_parts_enumerate`: reviewer-agent PASS after quality edits by Reviewer A.
- `concept_plant_state_compare`: reviewer-agent PASS after quality edits by Reviewer A.
- `concept_color_mixing_collect`: reviewer-agent PASS after quality edits by Reviewer A.
- `concept_constellation_star_count_enumerate`: reviewer-agent PASS after quality edits by Reviewer A.
- `concept_career_decision_decide`: reviewer-agent PASS after quality edits by Reviewer A.
- `concept_vegetable_sort_sort`: reviewer-agent PASS after quality edits by Reviewer A.
- `concept_how_many_guess_enumerate`: reviewer-agent PASS after quality edits by Reviewer B.
- `concept_flashcards_enumerate`: reviewer-agent PASS after quality edits by Reviewer B.
- `concept_trivia_game_remember`: reviewer-agent PASS after quality edits by Reviewer B.
- `concept_would_you_rather_compare`: reviewer-agent PASS after quality edits by Reviewer B.
- `concept_current_topic_interview_deduce`: reviewer-agent PASS after quality edits by Reviewer B.
- `concept_little_poem_build`: reviewer-agent PASS after quality edits by Reviewer B.
- `concept_travel_planner_predict`: reviewer-agent PASS after quality edits by Reviewer B.
- `concept_quick_silly_decide`: reviewer-agent PASS after quality edits by Reviewer B.

## Blocked Assignments

- `017`: Confirm runtime image generation support and safety review for child-facing generated assets.; Define coloring or recoloring UI behavior, selectable regions, state storage, and fallback behavior.
- `018`: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.
- `019`: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.
- `020`: Define UI state storage, progress memory, and resume/reset behavior.
- `021`: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.
- `022`: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `023`: Define coloring or recoloring UI behavior, selectable regions, state storage, and fallback behavior.; Define UI state storage, progress memory, and resume/reset behavior.
- `024`: Define UI state storage, progress memory, and resume/reset behavior.; Define before/after capture or parent confirmation; do not infer completion from one photo.
- `025`: Define UI state storage, progress memory, and resume/reset behavior.
- `026`: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.
- `027`: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.
- `028`: Define a supported Cat3 material workflow or convert the concept to a current Cat1/Cat5 scaffold without distorting the source promise.; Define caregiver/material setup, pacing, and no-assessment fallback for physical work.
- `029`: Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `030`: Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `031`: Define UI state storage, progress memory, and resume/reset behavior.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `032`: Confirm approved prebuilt asset library, display contract, and asset metadata availability.
- `033`: Define age-safe movement policy, caregiver gating, space checks, and prohibited movements.; Confirm approved prebuilt asset library, display contract, and asset metadata availability.
