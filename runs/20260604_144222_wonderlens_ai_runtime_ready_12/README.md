# WonderLens AI Runtime-Ready 12-Package Set

This run converts the 12 `activity_text_game` demo-aligned packages from the full workbook review packet into WonderLens AI runtime-ready source packages.

Source package run: `runs/20260521_163621_workbook_review_packet_full/activity_packages`
Fullstack demo game source: `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game/backend/games`
Fullstack UI assets source: `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game/frontend/public/activity-assets`

Each package contains:

- cleaned `prod.md` with WonderLens AI runtime beat headings and no generic converter leakage
- canonical `tag_block.yaml`, with `concept_phoneme_hunt_collect` patched to use `beginning_b_sound` for runtime judgment
- `demo_support.yaml` describing supported UI/runtime status, including minimal playable adaptations where needed
- `asset_manifest.yaml` with package-local PNG paths and WonderLens round-screen targets
- copied PNG assets under `assets/`, reusing the current fullstack demo UI artwork

WonderLens AI should generate `runtime.yaml` from these packages with:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
.venv/bin/python scripts/generate_activity_runtime.py \
  --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/.worktrees/feat/wonderlens-ai-runtime-ready/runs/20260604_144222_wonderlens_ai_runtime_ready_12/activity_packages \
  --dest validation_artifacts/wonderlens_ai_runtime_ready_12/generated_activities \
  --write --force \
  --report-json validation_artifacts/wonderlens_ai_runtime_ready_12/runtime_generation_report.json
```

Support status summary:

| Activity | UI status | Notes |
|---|---|---|
| `concept_animal_sound_motion_voice` | `supported` / `cat1_dialogue` | Runtime generation should be directly playable with Cat1 dialogue or Cat5 collection support. |
| `concept_career_decision_decide` | `supported` / `cat1_dialogue` | Runtime generation should be directly playable with Cat1 dialogue or Cat5 collection support. |
| `concept_constellation_star_count_enumerate` | `supported` / `cat1_dialogue` | Runtime generation should be directly playable with Cat1 dialogue or Cat5 collection support. |
| `concept_emotion_reader_care` | `supported` / `cat1_dialogue` | Runtime generation should be directly playable with Cat1 dialogue or Cat5 collection support. |
| `concept_guided_drawing_probe` | `supported` / `cat1_dialogue` | Minimal paper-photo adaptation: guide three paper drawing steps, capture a final photo, and do not verify drawing correctness. |
| `concept_partial_reveal_deduce` | `supported` / `cat1_dialogue` | Runtime generation should be directly playable with Cat1 dialogue or Cat5 collection support. |
| `concept_phoneme_hunt_collect` | `supported` / `cat5_judgment` | Use real camera capture, preserve photo_id, run vision recognition, normalize object names, and retry on non-B results. |
| `concept_recognition_pop_probe` | `supported` / `cat1_dialogue` | Minimal tap/select adaptation: choose matching cards without timed scoring or pop-grid state. |
| `concept_story_unlock_probe` | `supported` / `cat1_dialogue` | Runtime generation should be directly playable with Cat1 dialogue or Cat5 collection support. |
| `concept_travel_planner_predict` | `supported` / `cat1_dialogue` | Runtime generation should be directly playable with Cat1 dialogue or Cat5 collection support. |
| `concept_vegetable_sort_sort` | `supported` / `cat1_dialogue` | Minimal tap/select adaptation: group vegetable cards without drag/drop board state. |
| `concept_word_echo_remember` | `supported` / `cat1_dialogue` | Runtime generation should be directly playable with Cat1 dialogue or Cat5 collection support. |
