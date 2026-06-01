# Fullstack Validation

Run: `20260601_155917_full_pass_agentic_tsv`
Validator: master-controlled server lifecycle, pending delegated dialogue QA
Fullstack worktree: `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game`
Fullstack branch: `feat/activity-text-game`

## Verdict

Current verdict: **consumer gap**

The required fullstack branch is healthy for its existing loaded activity-text
games, but it does not currently expose a direct loader for the generated
autodesign package directories under this run.

## Preconditions Checked

- Worktree exists at the required path.
- Branch is `feat/activity-text-game`.
- Main backend credential files exist at
  `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend`.
- Live server was started from the required worktree backend.
- Runtime environment was sourced from the main backend directory only.
- Server was stopped after validation.

Port note: `127.0.0.1:8000` was already occupied locally, so validation used
`127.0.0.1:8001` without killing the existing process.

## Checks Run

```bash
uv run pytest \
  backend/tests/test_activity_text_game_api.py \
  backend/tests/test_activity_text_game_definitions.py \
  backend/tests/test_activity_text_game_cat3.py \
  backend/tests/test_activity_text_game_turns.py -q
```

Result: `17 passed in 2.05s`

```bash
uv run python scripts/run_activity_text_smoke.py --base-url http://127.0.0.1:8001
```

Result: `12 passed, 0 failed`

```bash
cd frontend
npm test -- tests/activityAssets.test.js tests/useActivityTextSession.test.jsx \
  tests/WonderLensDevice.test.jsx tests/ActivityGameApp.test.jsx
```

Result: `4 passed (4), 43 passed (43)`

```bash
cd frontend
npm run build
```

Result: `built in 1.12s` with Vite's existing chunk-size warning.

The smoke exercised the existing fullstack catalog:

- `activity_animal_sound_imitation`
- `activity_career_decision_role_play`
- `activity_constellation_star_count`
- `activity_emotion_reader`
- `activity_guided_drawing`
- `activity_partial_reveal_guess`
- `activity_phoneme_treasure_hunt`
- `activity_recognition_pop_challenge`
- `activity_story_challenge_unlock`
- `activity_travel_planner`
- `activity_vegetable_sort`
- `activity_word_echo_practice`

## Direct Package Load Finding

`backend/game_loader.py` loads only top-level `backend/games/*.md` files with
YAML frontmatter. It skips Markdown files without frontmatter and does not scan
autodesign package directories.

Searches in the fullstack worktree found no active
`scripts/import_autodesign_package.py` loader. The available conversion tools
are not direct package loaders:

- `scripts/generate_game_frontmatter.py` scaffolds frontmatter from a prod doc
  but leaves TODOs for `step_instructions`, catalogs, frames, and other fields.
- `scripts/convert_game.py` calls a hosted model to convert a prod doc into a
  loadable game file, but it operates on a single `*_prod.md` file, derives
  naming from the input filename, and validates only the generated game file
  shape. The CLI also hardcodes `backend/.env` inside the worktree, so this goal
  would need an explicit wrapper or code change to satisfy the main-backend-only
  credential rule.

Therefore the fullstack branch can validate its current converted games, but it
cannot yet prove that the 40 packages generated in this autodesign run load
directly without a conversion/import layer.

## Owner / Next Gate

Owner: fullstack consumer/importer.

Required follow-up before this run can pass the fullstack package gate:

1. Provide or implement a non-lossy autodesign package importer/converter that
   reads `activity_packages/<activity_id>/{prod.md,tag_block.yaml,demo_support.yaml,asset_manifest.yaml}`.
2. Preserve runtime-quality `step_instructions` comparable to
   `backend/games/fluffy_expedition_dandelion.md`.
3. Load the generated packages into the required worktree without manual content
   improvement.
4. Re-run live dialogue QA on the loaded package output using ideal, wrong,
   help/confusion, silence, premature done, and unsupported-request inputs.
