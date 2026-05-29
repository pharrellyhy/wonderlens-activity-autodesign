# Source Intent Pilot Validation

Run: `runs/20260529_172332_source_intent_pilot`

Status: Completed with non-blocking visual warning.

## Source Set

Source baseline:

- `inputs/original_activity_concepts_2026-05-29.tsv`
- `inputs/source_activity_concepts.md` as the normalized helper only
- Run snapshot: `source_snapshots/selected_source_rows.md` and `source_snapshots/selected_source_rows.tsv`

Selected pilot rows:

| TSV row | Activity ID | Source intent result | Runtime support |
|---:|---|---|---|
| 2 | `concept_phoneme_hunt_collect` | `minor_adaptation` | degraded Cat5 judgment |
| 4 | `concept_guided_drawing_probe` | `aligned` | unsupported/gated |
| 20 | `concept_constellation_star_count_enumerate` | `aligned` | supported |
| 15 | `concept_plant_parts_enumerate` | `aligned` | unsupported/gated |
| 26 | `concept_career_decision_decide` | `aligned` | supported |
| 11 | `concept_partial_reveal_deduce` | `aligned` | supported |
| 33 | `concept_would_you_rather_compare` | `minor_adaptation` | supported |

No package has unresolved `intent_drift` or `needs_product_decision`.

## Intent Fidelity

Independent source-intent audit files live in `source_intent_audits/`.

Summary:

- `aligned`: 5
- `minor_adaptation`: 2
- `intent_drift`: 0
- `needs_product_decision`: 0

The two minor adaptations are intentional V1 runtime honesty choices:

- `concept_phoneme_hunt_collect`: the package requires child name evidence because the demo cannot infer a /b/ initial sound from image pixels alone.
- `concept_would_you_rather_compare`: the runtime may ask for a tiny reason, while keeping the source's short binary-choice chain as the primary action.

The known constellation drift case is repaired in this pilot: the child chooses a number first, then the device reveals an approved matching constellation card and gives brief background context. It is not a direct count-the-stars quiz.

## Assets

Asset build mode: `generate_and_curate`.

Asset output evidence:

- `generated_assets/asset_outputs.yaml`
- `generated_assets/reference_sources.yaml`
- `generated_assets/qa_notes.yaml`
- Package-local PNGs under `activity_packages/*/assets/`

Built runtime PNGs:

| Activity ID | Asset IDs | Status |
|---|---|---|
| `concept_phoneme_hunt_collect` | `ball_b_sound_clue`, `banana_b_sound_clue` | generated, 512x512 |
| `concept_constellation_star_count_enumerate` | `cassiopeia_five_star_card`, `orion_seven_star_card` | reference-bound, 512x512 |
| `concept_career_decision_decide` | `firefighter_role_card` | generated, 512x512 |
| `concept_partial_reveal_deduce` | `rabbit_ears_reveal_card`, `tiger_tail_reveal_card`, `elephant_trunk_reveal_card` | generated, 512x512 |

Reference-bound constellation assets have accepted package-local source originals and metadata in:

- `activity_packages/concept_constellation_star_count_enumerate/assets/sources/cassiopeia_five_star_card__source_metadata.yaml`
- `activity_packages/concept_constellation_star_count_enumerate/assets/sources/orion_seven_star_card__source_metadata.yaml`

Visual/reference QA result: no blocking failures after repair. Remaining warning: `concept_partial_reveal_deduce` rabbit/elephant partial clues are readable, but important shapes sit close to the round-screen crop zone. This is a scale-up quality warning, not a pilot blocker.

## Runtime Instructions

Runtime instruction reviews live in `runtime_instruction_reviews/`.

All seven reviews have `verdict: pass` and `repair_required: false`.

Quality repairs made during the run:

- Replaced generic child-response examples and follow-ups with package-specific branch behavior.
- Split `concept_phoneme_hunt_collect` into explicit evidence and name-check runtime rounds so downstream import does not invent a generic Cat5 collection beat.
- Kept `concept_guided_drawing_probe` and `concept_plant_parts_enumerate` unsupported/gated instead of changing the mechanic to make them playable.

The fullstack conversion review checked generated `step_instructions` against the quality floor represented by `backend/games/fluffy_expedition_dandelion.md`: specific goal/action, constraint, tone, progress evidence, branch behavior, and source/frame guardrails.

## Downstream Results

Fullstack report:

- `downstream_reports/fullstack_import_review.yaml`
- Source commit used for import: `cc3d4271c8af956eb392b62e33bacbae5c042fe3`
- Import command exit status: 0
- Focused tests: `83 passed, 1 skipped`

Imported fullstack games:

- `concept_phoneme_hunt_collect__b_sound_treasure`
- `concept_constellation_star_count_enumerate__approved_constellation_count_card`
- `concept_career_decision_decide__firefighter_expert_role`
- `concept_partial_reveal_deduce__partial_animal_reveal_cards`
- `concept_would_you_rather_compare__silly_choice_prompt`

Skipped/gated in fullstack:

- `concept_guided_drawing_probe`
- `concept_plant_parts_enumerate`

WonderLens AI report:

- `downstream_reports/wonderlens_ai_runtime_review.yaml`
- Runtime generation exit status: 0
- Generated packages: 7
- Generator warnings: 0
- Focused tests: `45 passed`
- Generated destination loaded cleanly: 7 packages

WonderLens AI executable/gated behavior:

- Executable: career decision, constellation reveal, partial reveal, phoneme hunt, would-you-rather.
- Gated: guided drawing, plant parts.
- Phoneme hunt remains degraded, with runtime honesty about requiring photo plus name evidence.

## Checks

Autodesign:

- `/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/validate_demo_package_contract.py runs/20260529_172332_source_intent_pilot/activity_packages` -> pass, 7 packages.
- Run-local tag block schema validation -> pass, 7 files.
- `/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/build_activity_assets.py runs/20260529_172332_source_intent_pilot --mode generate_and_curate --force` -> pass, 8 assets built.
- `/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/validate_asset_build_outputs.py runs/20260529_172332_source_intent_pilot` -> pass.
- `/Users/pharrelly/.pyenv/versions/3.13.6/bin/python scripts/generate_run_review.py --validate runs/20260529_172332_source_intent_pilot` -> pass, `checked_links=116`.
- `ruby` YAML parse over `source_intent_audits/*.yaml` -> pass.
- `git diff --check` -> pass before the repair/report commit.

Downstream:

- Fullstack importer and focused tests -> pass; see `downstream_reports/fullstack_import_review.yaml`.
- WonderLens AI runtime generator, focused tests, and generated package load check -> pass; see `downstream_reports/wonderlens_ai_runtime_review.yaml`.

## Blockers And Risks

Blocking failures: none.

Non-blocking risks:

- `concept_guided_drawing_probe` needs a future Cat3 material-workflow runtime before it can be playable.
- `concept_plant_parts_enumerate` needs Cat5 enumerate/photo-part runtime support before it can be playable without mechanic drift.
- `concept_partial_reveal_deduce` should get safer source framing before a large asset run because two clue cards are close to the round crop edge.
- Downstream validation used focused test sets, not full repo test suites.
- Fullstack and WonderLens AI validation left transient untracked validation artifacts in their validation workspaces; no downstream commits were made.

## Recommendation

Proceed to a larger pilot/full-pass preparation with the current source-intent gates, but keep unsupported mechanics gated. The pilot proves the updated workflow can preserve source intent, generate PNG assets, and convert/load supported or degraded packages in both consumers. Before scaling all rows as playable, decide whether Cat3 material workflows and Cat5 enumerate/photo-part workflows should be implemented or remain blocked outputs.
