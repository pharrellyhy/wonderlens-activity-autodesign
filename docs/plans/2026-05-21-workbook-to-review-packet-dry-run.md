# Workbook To Review Packet Dry Run

Date: 2026-05-21

Workbook: `/Users/pharrelly/Downloads/活动库内部初版.xlsx`

Dry-run status: no activity generation, audit regeneration, asset integration, HTML export, or PR work was executed. This dry run only inspected the workbook, confirmed the existing normalized source snapshot, selected the proposed execution scope, and created a run-specific goal file.

## Workbook Inspection

The workbook exists and contains one populated sheet:

| Sheet | Populated rows | Activity rows | Populated columns |
|---|---:|---:|---:|
| `Sheet1` | 41 | 40 | 9 |

The second sheet, `数据透视表`, is empty.

`Sheet1` headers:

| Column | Header |
|---:|---|
| 1 | 活动名称 |
| 2 | 添加时间 |
| 3 | 主体类型 |
| 4 | 形式(单选) |
| 5 | 场景 |
| 6 | 机制(Mechanic)(单选) |
| 7 | 对屏幕的依赖度（特指视觉展示，不包括拍照行为） |
| 8 | 活动简介/举例 |
| 9 | 备注 |

## Source Snapshot Decision

The repo already has `inputs/source_activity_concepts.md`, a normalized English source snapshot derived from this workbook. The dry workflow should reuse it as the initial execution source, then verify it against the workbook before a real run starts.

Post-dry-run hardening added explicit `source_intent_lock_en`, `minimum_unblock_status`, and `resolved_assumptions_en` fields for four rows with known drift risk:

- `source_story_challenge_unlock`: story beat, paused challenge gate, child challenge, unlocked next story beat;
- `source_coloring_game`: fillable line art, child photographs real colors, system maps colors into regions;
- `source_toy_tidy_challenge`: initial toy context, short tidy mission, tips during cleanup, after-state confirmation;
- `source_career_decision`: child assumes a profession first, then makes expert decisions inside work scenarios.

The normalized snapshot contains:

| Field | Count |
|---|---:|
| Source concepts | 40 |
| `activity_concept` rows | 18 |
| `match_pattern` rows | 5 |
| `capability_probe` rows | 17 |
| `cat1` rows | 28 |
| `cat5` rows | 7 |
| `unsupported_cat3` rows | 5 |
| `no_assets` rows | 12 |
| `optional_support` rows | 14 |
| `required_prebuilt` rows | 13 |
| `runtime_generated` rows | 1 |
| `concept_only` rows | 35 |
| `mapping_informed` rows | 2 |
| `parameterized` rows | 3 |

## Proposed Execution Mode

Use a fresh full workbook-to-review-packet run unless the user explicitly asks to patch an existing run.

Recommended defaults for the full run:

- run label: `workbook_review_packet`;
- assignment scope: all 40 `Sheet1` workbook activity rows;
- source snapshot: `inputs/source_activity_concepts.md`;
- product contract override: `minimum_unblock_allowed`, matching the current Batch 5 unblocked contract so every workbook row can produce a reviewable package with resolved blocker annotations instead of stopping at product-decision rows;
- required final artifacts: generated packages, full source-intent audit, source comparison matrix, review dashboard, integrated asset/storyboard artifacts when images exist, and standalone reviewer packets for integrated activities;
- dry-run stop point: `goals/2026-05-21-workbook-to-review-packet-goal.md`.

If product wants unresolved product-decision rows to remain blocked, change the goal file from `product_contract_override=minimum_unblock_allowed` to `product_contract_override=none` before execution. That would likely produce 23 generation-ready rows and 17 blocked/capability-probe rows instead of 40 generated packages.

## Source Row Mapping

`source_row` is the normalized source index in `inputs/source_activity_concepts.md`; Excel row is `source_row + 1`.

| Source row | Excel row | Source concept id | Activity concept | Assignment type | Category | Mechanic | Asset policy |
|---:|---:|---|---|---|---|---|---|
| 1 | 2 | `source_scavenger_hunt` | Scavenger Hunt | `match_pattern` | `cat5` | `collect` | `no_assets` |
| 2 | 3 | `source_phoneme_hunt` | Phoneme Treasure Hunt | `match_pattern` | `cat5` | `collect` | `optional_support` |
| 3 | 4 | `source_branching_story` | Branching Choice Story | `activity_concept` | `cat1` | `decide` | `no_assets` |
| 4 | 5 | `source_guided_drawing` | Guided Drawing | `capability_probe` | `unsupported_cat3` | `build` | `optional_support` |
| 5 | 6 | `source_word_echo_practice` | Word Echo Practice | `activity_concept` | `cat1` | `remember` | `optional_support` |
| 6 | 7 | `source_building_challenge` | Building Challenge | `capability_probe` | `unsupported_cat3` | `build` | `optional_support` |
| 7 | 8 | `source_story_challenge_unlock` | Story Challenge Unlock | `capability_probe` | `cat1` | `imagine` | `optional_support` |
| 8 | 9 | `source_coloring_game` | Coloring Game | `capability_probe` | `cat5` | `build` | `runtime_generated` |
| 9 | 10 | `source_classic_music_movement` | Classic Music And Movement | `capability_probe` | `cat1` | `motion_voice` | `no_assets` |
| 10 | 11 | `source_childrens_yoga` | Children's Yoga | `capability_probe` | `cat1` | `motion_voice` | `required_prebuilt` |
| 11 | 12 | `source_partial_reveal_guess` | Partial Reveal Guess | `activity_concept` | `cat1` | `deduce` | `required_prebuilt` |
| 12 | 13 | `source_emotion_reader` | Emotion Reader | `activity_concept` | `cat1` | `care` | `optional_support` |
| 13 | 14 | `source_animal_sound_imitation` | Animal Sound Imitation | `activity_concept` | `cat1` | `motion_voice` | `optional_support` |
| 14 | 15 | `source_tiny_curator` | Tiny Curator | `match_pattern` | `cat5` | `sort` | `no_assets` |
| 15 | 16 | `source_plant_parts_explorer` | Plant Parts Explorer | `match_pattern` | `cat5` | `enumerate` | `no_assets` |
| 16 | 17 | `source_plant_state_compare` | Plant State Compare | `match_pattern` | `cat5` | `compare` | `no_assets` |
| 17 | 18 | `source_emotion_color_outfit` | Emotion Color Outfit | `capability_probe` | `cat1` | `care` | `required_prebuilt` |
| 18 | 19 | `source_guess_in_10` | Guess in 10 | `activity_concept` | `cat1` | `deduce` | `optional_support` |
| 19 | 20 | `source_color_mixing_board` | Color Mixing Board | `activity_concept` | `cat1` | `collect` | `optional_support` |
| 20 | 21 | `source_constellation_star_count` | Constellation Star Count | `activity_concept` | `cat1` | `enumerate` | `required_prebuilt` |
| 21 | 22 | `source_toy_tidy_challenge` | Toy Tidy Challenge | `capability_probe` | `cat5` | `sort` | `no_assets` |
| 22 | 23 | `source_time_sense_challenge` | Time Sense Challenge | `capability_probe` | `cat1` | `predict` | `no_assets` |
| 23 | 24 | `source_one_line_drawing` | One-Line Drawing Challenge | `capability_probe` | `unsupported_cat3` | `build` | `required_prebuilt` |
| 24 | 25 | `source_message_bottle_note` | Message Bottle Note | `capability_probe` | `unsupported_cat3` | `care` | `no_assets` |
| 25 | 26 | `source_award_certificate` | Award Certificate | `capability_probe` | `unsupported_cat3` | `care` | `optional_support` |
| 26 | 27 | `source_career_decision` | Career Decision | `activity_concept` | `cat1` | `decide` | `optional_support` |
| 27 | 28 | `source_vegetable_sort` | Vegetable Sort | `activity_concept` | `cat1` | `sort` | `required_prebuilt` |
| 28 | 29 | `source_how_many_guess` | How Many Guess | `activity_concept` | `cat1` | `enumerate` | `required_prebuilt` |
| 29 | 30 | `source_flashcards` | Flashcards | `activity_concept` | `cat1` | `enumerate` | `required_prebuilt` |
| 30 | 31 | `source_trivia_game` | Trivia Game | `activity_concept` | `cat1` | `remember` | `optional_support` |
| 31 | 32 | `source_whack_a_mole_recognition` | Recognition Pop Challenge | `capability_probe` | `cat1` | `compare` | `required_prebuilt` |
| 32 | 33 | `source_word_build_guess` | Word Build Guess | `capability_probe` | `cat1` | `decide` | `required_prebuilt` |
| 33 | 34 | `source_would_you_rather` | Would You Rather | `activity_concept` | `cat1` | `compare` | `no_assets` |
| 34 | 35 | `source_art_critic_tournament` | Art Critic Tournament | `capability_probe` | `cat1` | `compare` | `required_prebuilt` |
| 35 | 36 | `source_color_in_famous_art` | Color In Famous Art | `capability_probe` | `cat1` | `enumerate` | `required_prebuilt` |
| 36 | 37 | `source_simple_body_movement` | Simple Body Movement Guide | `capability_probe` | `cat1` | `motion_voice` | `required_prebuilt` |
| 37 | 38 | `source_current_topic_interview` | Current Topic Interview | `activity_concept` | `cat1` | `deduce` | `no_assets` |
| 38 | 39 | `source_little_poem_generator` | Little Poem Generator | `activity_concept` | `cat1` | `build` | `no_assets` |
| 39 | 40 | `source_travel_planner` | Travel Planner | `activity_concept` | `cat1` | `predict` | `optional_support` |
| 40 | 41 | `source_quick_silly_questions` | Quick and Silly Questions | `activity_concept` | `cat1` | `decide` | `optional_support` |

## Goal File Created

Dry workflow output:

- `goals/2026-05-21-workbook-to-review-packet-goal.md`

This goal is ready for human review before execution. It should not be executed until the product-contract override and fresh-run-vs-existing-run choice are accepted.
