# Generation Pass Details

Run: `20260529_172332_source_intent_pilot`

Branch: `feat/source-intent-pilot`

Final run report: `source_intent_pilot_validation.md`

This file records the end-to-end generation pass used for the source-intent
pilot, including how activity packages, runtime instructions, image assets,
review artifacts, and downstream validation reports were produced.

## Source Inputs

Primary source baseline:

```text
inputs/original_activity_concepts_2026-05-29.tsv
```

Normalized helper:

```text
inputs/source_activity_concepts.md
```

Run-local source snapshot:

```text
runs/20260529_172332_source_intent_pilot/source_snapshots/selected_source_rows.md
runs/20260529_172332_source_intent_pilot/source_snapshots/selected_source_rows.tsv
```

Selected rows:

| TSV row | Activity ID | Activity | Support result |
|---:|---|---|---|
| 2 | `concept_phoneme_hunt_collect` | Phoneme Treasure Hunt | degraded |
| 4 | `concept_guided_drawing_probe` | Guided Drawing | unsupported/gated |
| 20 | `concept_constellation_star_count_enumerate` | Constellation Star Count | supported |
| 15 | `concept_plant_parts_enumerate` | Plant Parts Explorer | unsupported/gated |
| 26 | `concept_career_decision_decide` | Career Decision | supported |
| 11 | `concept_partial_reveal_deduce` | Partial Reveal Guess | supported |
| 33 | `concept_would_you_rather_compare` | Would You Rather | supported |

## End-To-End Pass

1. Start from the source-intent pilot goal and plan.
   - `goals/2026-05-29-source-intent-pilot-validation-goal.md`
   - `docs/plans/2026-05-29-source-intent-pilot-validation.md`
2. Read the generation contracts.
   - `GOAL.md`
   - `run.md`
   - `program.md`
   - `templates.md`
   - `docs/activity_asset_generation_workflow.md`
   - `activities/README.md`
3. Record current repo state in `run_manifest.yaml`.
4. Select the seven workbook rows and write the source snapshot.
5. Write `assignment_snapshot.md` with one unchecked scoped assignment per selected row.
6. For each assignment, write an adaptation brief under `adaptation_briefs/`.
   - The original workbook row wins when it conflicts with normalized helper wording.
   - The adaptation brief records child role, device role, required child actions, non-negotiable source elements, allowed V1 adaptations, product capability flags, and asset dependency.
7. Generate one run-local package under `activity_packages/<activity_id>/`.
   - `spec.md`
   - `prod.md`
   - `tag_block.yaml`
   - `recap.template.yaml`
   - `dashboard.template.yaml`
   - `demo_support.yaml`
   - `asset_manifest.yaml`
8. Keep unsupported mechanics honest.
   - Guided Drawing stays `unsupported` because it requires Cat3 paper-and-pencil material workflow support.
   - Plant Parts Explorer stays `unsupported` because the downstream runtime does not yet support Cat5 enumerate/photo-part flow without mechanic drift.
9. Build image assets only after package validation, because package authoring writes manifests first and binary PNGs second.
10. Run independent review loops.
    - `source_intent_audits/`
    - `runtime_instruction_reviews/`
    - `visual_reference_reviews/`
11. Repair review findings.
    - Runtime branch behavior was made package-specific.
    - Phoneme Hunt was split into evidence and name-check runtime rounds.
    - Firefighter and constellation assets were repaired after visual QA.
12. Validate downstream conversion.
    - `downstream_reports/fullstack_import_review.yaml`
    - `downstream_reports/wonderlens_ai_runtime_review.yaml`
13. Write the final report and final-report review.
    - `source_intent_pilot_validation.md`
    - `final_report_review.yaml`

## Asset Build Mode

The run used:

```yaml
asset_build: generate_and_curate
```

That means:

- illustrative assets were generated as source PNGs;
- reference-bound assets were curated from accepted package-local sources;
- `scripts/build_activity_assets.py` built package-local runtime variants;
- `scripts/validate_asset_build_outputs.py` validated runtime paths, PNG sizes, and reference metadata.

## Asset Source Of Truth

For each package, the asset source of truth is:

```text
activity_packages/<activity_id>/asset_manifest.yaml
```

The deterministic work items generated from those manifests are:

```text
generated_assets/work_items/*.md
```

The selected illustrative source PNGs were stored in:

```text
generated_assets/inbox/<activity_id>/<asset_id>.png
```

The final runtime PNGs were stored in package-local paths:

```text
activity_packages/<activity_id>/assets/<asset_id>__round_512.png
```

Reference-bound source originals and metadata were stored in:

```text
activity_packages/concept_constellation_star_count_enumerate/assets/sources/
```

## Asset Image Generation Steps

### Illustrative Assets

Illustrative assets used `accuracy_mode: illustrative`,
`source_strategy: generated_illustrative`, and `transformation_policy:
generate_new`.

Steps:

1. Read `prompt_en` from each `asset_manifest.yaml`.
2. Keep the prompt tied to the activity mechanic and asset role.
3. Use Codex built-in image generation, one asset per generated image.
4. Do not generate contact sheets as runtime assets.
5. Copy the selected source PNG into `generated_assets/inbox/<activity_id>/<asset_id>.png`.
6. Inspect the image for:
   - square source image, at least 512x512;
   - no readable text, letters, numbers, labels, logos, watermarks, UI chrome, contact sheet, circular mask, border, or vignette;
   - subject inside the central circular safe area;
   - flat Nordic nursery style matching the current WonderLens asset contract.
7. Repair simple framing issues deterministically when possible.
8. Run the asset builder with `--mode generate_and_curate --force`.
9. Run asset validation and visual/reference QA.

### Reference-Bound Assets

Reference-bound assets used `accuracy_mode: reference_bound`,
`source_strategy: approved_internal_reference`, and `transformation_policy:
crop_resize_only`.

Steps:

1. Do not ask image generation to invent constellations.
2. Use an accepted package-local teaching chart source.
3. Store the accepted source original under `assets/sources/`.
4. Store metadata with accepted source type, license, source URI, storage permission, verification notes, SHA-256, and reviewer.
5. Build runtime variants by crop/resize only.
6. If visual QA finds extra star-like marks, repair the accepted internal chart deterministically and update metadata hashes.
7. Rebuild package-local runtime variants and re-run QA.

## Style Contract Used In Prompts

The prompt style came from `docs/activity_asset_generation_workflow.md` and the
latest fullstack style source:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/.worktrees/feat/activity-text-game/frontend/public/activity-assets/prompts/wonderlens-activity-style.md
```

Common style requirements:

- flat Nordic children's illustration;
- quiet white WonderLens prototype fit;
- broad flat color fills;
- sparse pencil texture;
- muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, and blush;
- square source art;
- important detail inside the central circular safe area;
- no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette.

## Asset Prompt Log

These are the actual package prompts or source requirements recorded in the
asset manifests and work items.

### `concept_phoneme_hunt_collect`

Target source path:

```text
generated_assets/inbox/concept_phoneme_hunt_collect/ball_b_sound_clue.png
```

Prompt:

```text
Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: A single friendly round ball object clue for a B-sound treasure hunt.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette.
```

Target source path:

```text
generated_assets/inbox/concept_phoneme_hunt_collect/banana_b_sound_clue.png
```

Prompt:

```text
Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: A single curved banana object clue for a B-sound treasure hunt.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette.
```

### `concept_career_decision_decide`

Target source path:

```text
generated_assets/inbox/concept_career_decision_decide/firefighter_role_card.png
```

Prompt:

```text
Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: One inclusive adult firefighter helper character with a simple safe tool, friendly and non-emergency, no flames or danger.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette.
```

Post-generation repair:

- Visual QA found the first runtime card overfilled the round safe area.
- The source image was deterministically reduced and centered on white before rebuilding:

```bash
magick generated_assets/inbox/concept_career_decision_decide/firefighter_role_card.png \
  -resize 900x900 \
  -background white \
  -gravity center \
  -extent 1254x1254 \
  generated_assets/inbox/concept_career_decision_decide/firefighter_role_card.tmp.png
mv generated_assets/inbox/concept_career_decision_decide/firefighter_role_card.tmp.png \
  generated_assets/inbox/concept_career_decision_decide/firefighter_role_card.png
```

### `concept_partial_reveal_deduce`

Target source path:

```text
generated_assets/inbox/concept_partial_reveal_deduce/rabbit_ears_reveal_card.png
```

Prompt:

```text
Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: Partial-reveal animal guessing card showing only two long rabbit ears and a tiny top-of-head hint, not the full animal.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette.
```

Target source path:

```text
generated_assets/inbox/concept_partial_reveal_deduce/tiger_tail_reveal_card.png
```

Prompt:

```text
Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: Partial-reveal animal guessing card showing only an orange striped tiger tail curling into view, not the full animal.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette.
```

Target source path:

```text
generated_assets/inbox/concept_partial_reveal_deduce/elephant_trunk_reveal_card.png
```

Prompt:

```text
Use case: illustration-story. Asset type: WonderLens runtime activity asset. Primary request: Partial-reveal animal guessing card showing only a gentle elephant trunk and one soft ear edge, not the full animal.. Style: Flat Nordic children's illustration matching the quiet white WonderLens prototype; broad flat color fills, sparse pencil texture, muted sage, dusty teal-blue, soft terracotta, oatmeal, ochre, blush; square 512x512 source art with important detail inside central circular safe area; no readable text, letters, numbers, labels, logo, watermark, border, contact sheet, device frame, circular mask, or vignette.
```

Visual QA warning:

- Rabbit ears and elephant trunk clues are readable, but some important shapes sit close to the round crop edge.
- This was recorded as non-blocking for the pilot and should be tightened before a larger asset pass.

### `concept_constellation_star_count_enumerate`

Target source paths:

```text
activity_packages/concept_constellation_star_count_enumerate/assets/sources/cassiopeia_five_star_card__source_original.png
activity_packages/concept_constellation_star_count_enumerate/assets/sources/orion_seven_star_card__source_original.png
```

Cassiopeia source requirement:

```text
Use the accepted package-local Cassiopeia teaching chart. Preserve exactly 5 prominent guide stars and approved guide-line shape. Do not add extra stars, text, labels, numbers, or fictional geometry.
```

Orion source requirement:

```text
Use the accepted package-local Orion teaching chart. Preserve exactly 7 prominent guide stars and approved guide-line shape. Do not add extra stars, text, labels, numbers, or fictional geometry.
```

Reference metadata:

```text
activity_packages/concept_constellation_star_count_enumerate/assets/sources/cassiopeia_five_star_card__source_metadata.yaml
activity_packages/concept_constellation_star_count_enumerate/assets/sources/orion_seven_star_card__source_metadata.yaml
```

Post-QA deterministic repair:

- Visual QA found faint extra star-like marks in the first source charts.
- The accepted internal reference charts were re-rendered deterministically with exactly 5 and 7 guide stars.
- Metadata SHA-256 values were updated.

Cassiopeia repair command:

```bash
magick -size 512x512 canvas:'#526d92' \
  -stroke '#f3edd8' -strokewidth 5 -fill none \
  -draw 'line 96,285 176,197 line 176,197 256,277 line 256,277 336,192 line 336,192 421,260' \
  -stroke '#f3edd8' -strokewidth 5 -fill '#fff4c8' \
  -draw 'circle 96,285 108,285 circle 176,197 188,197 circle 256,277 268,277 circle 336,192 348,192 circle 421,260 433,260' \
  activity_packages/concept_constellation_star_count_enumerate/assets/sources/cassiopeia_five_star_card__source_original.png
```

Orion repair command:

```bash
magick -size 512x512 canvas:'#526d92' \
  -stroke '#f3edd8' -strokewidth 5 -fill none \
  -draw 'line 160,111 215,236 line 215,236 145,390 line 215,236 256,248 line 256,248 298,232 line 298,232 345,127 line 298,232 360,393' \
  -stroke '#f3edd8' -strokewidth 5 -fill '#fff4c8' \
  -draw 'circle 160,111 172,111 circle 215,236 227,236 circle 256,248 268,248 circle 298,232 310,232 circle 345,127 357,127 circle 145,390 157,390 circle 360,393 372,393' \
  activity_packages/concept_constellation_star_count_enumerate/assets/sources/orion_seven_star_card__source_original.png
```

## Asset Builder Commands

The build command used after inbox/source preparation:

```bash
/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/build_activity_assets.py \
  runs/20260529_172332_source_intent_pilot \
  --mode generate_and_curate \
  --force
```

The builder:

- validates package contracts before building;
- consumes illustrative source PNGs from `generated_assets/inbox/`;
- consumes accepted reference originals and metadata from package-local `assets/sources/`;
- writes `assets/<asset_id>__round_512.png`;
- updates package-relative variant paths in `asset_manifest.yaml`;
- writes `generated_assets/asset_outputs.yaml`;
- writes `generated_assets/reference_sources.yaml`;
- writes `generated_assets/qa_notes.yaml`.

Final builder result:

```text
OK asset build: mode=generate_and_curate packages=7 assets=8 built=8 required_failures=0
```

## Final Asset Outputs

| Activity ID | Runtime PNGs |
|---|---|
| `concept_phoneme_hunt_collect` | `assets/ball_b_sound_clue__round_512.png`, `assets/banana_b_sound_clue__round_512.png` |
| `concept_constellation_star_count_enumerate` | `assets/cassiopeia_five_star_card__round_512.png`, `assets/orion_seven_star_card__round_512.png` |
| `concept_career_decision_decide` | `assets/firefighter_role_card__round_512.png` |
| `concept_partial_reveal_deduce` | `assets/rabbit_ears_reveal_card__round_512.png`, `assets/tiger_tail_reveal_card__round_512.png`, `assets/elephant_trunk_reveal_card__round_512.png` |

Activities with no generated assets:

- `concept_guided_drawing_probe`
- `concept_plant_parts_enumerate`
- `concept_would_you_rather_compare`

## Validation Commands

Autodesign:

```bash
/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/validate_demo_package_contract.py \
  runs/20260529_172332_source_intent_pilot/activity_packages

/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/validate_asset_build_outputs.py \
  runs/20260529_172332_source_intent_pilot

/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/generate_run_review.py \
  runs/20260529_172332_source_intent_pilot

/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/generate_run_review.py \
  --validate runs/20260529_172332_source_intent_pilot

git diff --check
```

Fullstack:

```bash
uv run python scripts/import_autodesign_package.py <package_dirs...> --source-commit <autodesign_commit>
uv run pytest tests/test_autodesign_importer.py tests/test_entity_registry.py tests/test_api.py
```

WonderLens AI:

```bash
.venv/bin/python scripts/generate_activity_runtime.py \
  --source <autodesign_run>/activity_packages \
  --dest validation_artifacts/source_intent_pilot_runtime_20260529_172332/generated_activities \
  --write \
  --force \
  --report-json validation_artifacts/source_intent_pilot_runtime_20260529_172332/runtime_generation_report.json

.venv/bin/python -m pytest \
  tests/unit/activity/test_activity_package_models.py \
  tests/unit/activity/test_activity_package_loader.py \
  tests/unit/activity/test_runtime_generator.py \
  tests/unit/scripts/test_generate_activity_runtime.py \
  -v
```

## Review Gates

Acceptance required evidence from:

- source-intent audit: `source_intent_audits/*.yaml`;
- runtime instruction review: `runtime_instruction_reviews/*.yaml`;
- visual/reference QA: `visual_reference_reviews/*.yaml`;
- fullstack conversion: `downstream_reports/fullstack_import_review.yaml`;
- WonderLens AI conversion/load: `downstream_reports/wonderlens_ai_runtime_review.yaml`;
- final report review: `final_report_review.yaml`.

Final review outcome:

- no unresolved intent drift;
- no blocking visual asset failures;
- no missing required runtime PNGs;
- supported/degraded packages convert downstream;
- unsupported packages remain gated rather than falsely playable.

## Scale-Up Notes

For a larger/full pass:

1. Keep `inputs/original_activity_concepts_2026-05-29.tsv` as the source-intent baseline unless a newer workbook export is committed.
2. Keep `inputs/source_activity_concepts.md` as helper-only normalization.
3. Use `asset_build=generate_and_curate` only when the pass is expected to produce PNGs.
4. Generate one image per asset prompt, not contact sheets.
5. Treat reference-bound assets as source-curation work, not free image generation.
6. Preserve unsupported mechanics as blocked/gated packages until the product/runtime support exists.
7. Require downstream conversion reports before accepting the pass.
8. Fix or explicitly record any source-intent drift before marking the pass complete.
