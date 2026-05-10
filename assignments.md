# Activity Design Assignments

> Each line is one assignment. The agent works through them top to bottom.
> Mark completed assignments with [x]. The agent skips completed ones.
>
> Current format: include `assignment_type=` on new rows.
> Entity package format: `- [ ] assignment_type=entity_activity, entity=<entity>, category=<cat1|cat5>, tier=TX, mechanic=mechanic, pillar=Pillar, style=game_style, mapping=entity_id, start=warm+cold, activity_id=optional_slug, scene=...`
> Concept format: `- [ ] assignment_type=activity_concept, activity_concept=<concept name>, concept_source=<file#concept_id>, description=<concept description>, mechanic=mechanic, category=<cat1|cat5|unknown>, asset_policy=<no_assets|optional_support|required_prebuilt|runtime_generated|blocked>, product_capabilities=optional_flags`
> Pattern format: `- [ ] assignment_type=match_pattern, activity_concept=<pattern name>, description=<runtime-match pattern>, mechanic=mechanic, category=<cat1|cat5>`
> Capability probe format: `- [ ] assignment_type=capability_probe, activity_concept=<concept name>, description=<product-dependent concept>, mechanic=mechanic, category=<hint>, asset_policy=<policy>, product_capabilities=required_flags`
> Required: either `entity + category` or `activity_concept + description/mechanic`. Recommended: `tier=`, `mechanic=`, and a concrete `scene=` when entity-grounded.
> Asset dependencies: use `asset_policy=` on the assignment row and put non-trivial asset details in a companion Activity Concept Brief / Asset Requirements table referenced by `asset_requirements=<source_or_asset_id>`.
> Source references: when `concept_source=` or `asset_requirements=` points to `file#id`, read that file before Phase 0 and use the matching concept / asset row as source context.
> Output language: source concept names may arrive in Chinese, but assignment `description=`, `trigger_condition=`, generated adaptation briefs, generated packages, asset briefs, and runtime files must be written in English.
> Mechanics are the primary action hint: `enumerate`, `compare`, `collect`, `sort`, `deduce`, `build`, `predict`, `decide`, `remember`, `imagine`, `care`, `motion_voice`.
> Game styles are optional secondary format hints: `mystery_lens`, `mystery_trail`, `inventor_workshop`, `mix_lab`, `voice_stage`, `ensemble_show`, `prediction_lab`, `field_experiment`, `time_traveler`, `quest_collector`, `care_station`, `rescue_team`.
> If `mechanic=` is provided but `style=` is omitted, the agent infers pillar/style from the mechanic, entity affordances, category, and program.md §1.6.
> Completed legacy rows may omit `assignment_type=` or contain retired style tokens; do not copy them for new assignments.

## Batch 1: Proof of Concept (10 activities)

### Category 1 — Sustained Verbal Interaction (In-Device)

- [x] toy dinosaur + category 1 (sustained verbal), tier=T0, scene=child photographs a toy T-Rex in the playroom
- [x] stuffed cat + category 1 (sustained verbal), tier=T0, scene=child photographs their stuffed cat on the bed
- [x] banana + category 1 (sustained verbal), tier=T1, scene=child photographs a banana on the kitchen table
- [x] toy fire truck + category 1 (sustained verbal), tier=T0, scene=child photographs a red toy fire truck on the living room floor
- [x] rubber duck + category 1 (sustained verbal), tier=T0, scene=child photographs a rubber duck in the bathtub

### Category 5 — Collection/Tracking Exploration (Out-of-Device)

- [x] dandelion + category 5 (collection/tracking), tier=T1, scene=child photographs a dandelion in the grass at the park
- [x] pinecone + category 5 (collection/tracking), tier=T1, scene=child photographs a pinecone under a tree in the yard
- [x] puddle + category 5 (collection/tracking), tier=T1, scene=child photographs a rain puddle on the sidewalk after rain
- [x] feather + category 5 (collection/tracking), tier=T1, scene=child photographs a feather found on the playground
- [x] autumn leaf + category 5 (collection/tracking), tier=T1, scene=child photographs a bright red leaf on the ground in the park

---

## Batch 2: Mapping-Informed Designs (17 activities)

> **Format**: `- [ ] entity + category, tier=TX, mapping=entity_id, start=warm+cold, scene=...`
> All Batch 2 designs use entity mapping data and produce dual warm/cold bridges.
> Read `entity_guidance.md` and `conversation_bridge.md` before starting.

### Category 1 — Sustained Verbal Interaction (In-Device)

- [x] goldfish + category 1 (sustained verbal), tier=T1, mapping=animals_goldfish, start=warm+cold, scene=child photographs their pet goldfish swimming in a glass bowl on the shelf
- [x] lion + category 1 (sustained verbal), tier=T0, mapping=animals_lion, start=warm+cold, scene=child photographs a toy lion on the playroom rug
- [x] crayons + category 1 (sustained verbal), tier=T0, mapping=arts_music_crayons, start=warm+cold, scene=child photographs a pile of crayons on the drawing table
- [x] piano + category 1 (sustained verbal), tier=T1, mapping=arts_music_piano, start=warm+cold, scene=child photographs the family piano in the living room
- [x] teddy bear + category 1 (sustained verbal), tier=T0, mapping=daily_objects_teddy_bear, start=warm+cold, scene=child photographs their teddy bear sitting on the bed
- [x] toothbrush holder + category 1 (sustained verbal), tier=T1, mapping=daily_objects_toothbrush_holder, start=warm+cold, scene=child photographs the toothbrush holder on the bathroom counter
- [x] eye + category 1 (sustained verbal), tier=T2, mapping=human_body_eye, start=warm+cold, scene=child photographs their own eye in a mirror
- [x] firefighter + category 1 (sustained verbal), tier=T1, mapping=people_roles_firefighter, start=warm+cold, scene=child photographs a firefighter figure or picture on the fridge
- [x] raincoat + category 1 (sustained verbal), tier=T0, mapping=clothing_accessories_raincoat, start=warm+cold, scene=child photographs their yellow raincoat hanging by the door

### Category 5 — Collection/Tracking Exploration (Out-of-Device)

- [x] city library + category 5 (collection/tracking), tier=T2, mapping=buildings_places_city_library, start=warm+cold, scene=child photographs the front of the city library building from across the street
- [x] playground + category 5 (collection/tracking), tier=T1, mapping=buildings_places_playground, start=warm+cold, scene=child photographs the slide at the neighborhood playground
- [x] green apple + category 5 (collection/tracking), tier=T1, mapping=food_green_apple, start=warm+cold, scene=child photographs a green apple found under a tree in the garden
- [x] double rainbow + category 5 (collection/tracking), tier=T1, mapping=natural_phenomena_double_rainbow, start=warm+cold, scene=child photographs a rainbow in the sky after a rain shower
- [x] sandy beach + category 5 (collection/tracking), tier=T1, mapping=nature_landscapes_sandy_beach, start=warm+cold, scene=child photographs the sandy shore at the beach
- [x] sunflower + category 5 (collection/tracking), tier=T1, mapping=plants_sunflower, start=warm+cold, scene=child photographs a tall sunflower in the garden
- [x] stop sign + category 5 (collection/tracking), tier=T1, mapping=signs_symbols_stop_sign, start=warm+cold, scene=child photographs a stop sign at the street corner during a walk
- [x] bicycle + category 5 (collection/tracking), tier=T1, mapping=vehicles_bicycle, start=warm+cold, scene=child photographs their bicycle parked in the driveway

---

## Batch 3: Category Swap — Same Entities, Opposite Mode (13 activities)

> **Goal**: Give Batch 2 entities a second activity in the opposite category.
> Dropped 4 entities with poor cross-category fit: teddy bear, toothbrush holder (Cat 1→5), double rainbow, sandy beach (Cat 5→1).
> All designs use entity mapping data, game styles, and dual warm/cold bridges.

### Cat 1 entities → Category 5 (Out-of-Device Collection)

- [x] goldfish + category 5 (collection/tracking), tier=T1, style=comparison_chart, mapping=animals_goldfish, start=warm+cold, scene=child photographs a goldfish in a park pond or aquarium tank and goes on a hunt for other water creatures and shimmery things nearby
- [x] lion + category 5 (collection/tracking), tier=T0, style=comparison_chart, mapping=animals_lion, start=warm+cold, scene=child spots a toy lion in the yard and goes on a hunt for strong or brave-looking things nearby
- [x] crayons + category 5 (collection/tracking), tier=T0, style=naming_story, mapping=arts_music_crayons, start=warm+cold, scene=child brings crayons outside and searches for things that match each crayon color
- [x] piano + category 5 (collection/tracking), tier=T1, style=comparison_chart, mapping=arts_music_piano, start=warm+cold, scene=child hears the piano and goes outside to find things that make interesting sounds
- [x] eye + category 5 (collection/tracking), tier=T2, style=comparison_chart, mapping=human_body_eye, start=warm+cold, scene=child looks in a mirror at their eye then goes outside to find things with eye-like patterns or circles
- [x] firefighter + category 5 (collection/tracking), tier=T1, style=comparison_chart, mapping=people_roles_firefighter, start=warm+cold, scene=child photographs a firefighter figure then walks the neighborhood to find safety signs and helpers
- [x] raincoat + category 5 (collection/tracking), tier=T0, style=naming_story, mapping=clothing_accessories_raincoat, start=warm+cold, scene=child puts on their raincoat and goes outside to find things that protect from rain or weather

### Cat 5 entities → Category 1 (Sustained Verbal Interaction)

- [x] city library + category 1 (sustained verbal), tier=T2, style=storytelling_chain, mapping=buildings_places_city_library, start=warm+cold, scene=child photographs a library book at home and narrates its journey through the library system
- [x] playground + category 1 (sustained verbal), tier=T1, style=voice_acting, mapping=buildings_places_playground, start=warm+cold, scene=child photographs a playground from the window or a picture of one and voices what each piece of equipment feels
- [x] green apple + category 1 (sustained verbal), tier=T1, style=prediction_game, mapping=food_green_apple, start=warm+cold, scene=child photographs a green apple on the kitchen counter and predicts what happens as it grows and changes
- [x] sunflower + category 1 (sustained verbal), tier=T1, style=prediction_game, mapping=plants_sunflower, start=warm+cold, scene=child photographs a sunflower picture or seed packet and predicts what sun, rain, and bees cause
- [x] stop sign + category 1 (sustained verbal), tier=T1, style=helper_hotline, mapping=signs_symbols_stop_sign, start=warm+cold, scene=child photographs a stop sign picture on the fridge and helps solve traffic safety scenarios
- [x] bicycle + category 1 (sustained verbal), tier=T1, style=voice_acting, mapping=vehicles_bicycle, start=warm+cold, scene=child photographs their bicycle in the garage and voices what the bike feels on different adventures

---

## Batch 4: Source Activity Concepts

> Source workbook: local concept workbook, `Sheet1`.
> Companion concept and asset details: `examples/source_activity_concept_briefs.md`.
> Rows in "Generation-ready / assumption-ready" are intended to create packages. Rows in "Capability probes" are expected to write blocked briefs when current product capabilities cannot support them; the `/goal` loop should leave blocked rows unchecked and continue to later unchecked rows.
> All assignment row descriptions and trigger conditions in this batch are normalized to English even when the source concept name was Chinese.

### Generation-ready / assumption-ready concepts

- [x] assignment_type=match_pattern, activity_concept=Scavenger Hunt, concept_source=examples/source_activity_concept_briefs.md#source_scavenger_hunt, description=Child finds and photographs three things that share a color, shape, or category, then names one extra thing they have in common, mechanic=collect, category=cat5, tier=T1, asset_policy=no_assets, activity_id=concept_scavenger_hunt_collect, trigger_condition=Child photographs an object with a clear color, shape, or category feature
- [x] assignment_type=match_pattern, activity_concept=Phoneme Treasure Hunt, concept_source=examples/source_activity_concept_briefs.md#source_phoneme_hunt, description=Child hears a target sound and finds one indoor treasure whose word starts with that sound, mechanic=collect, category=cat5, tier=T1, asset_policy=optional_support, asset_requirements=examples/source_activity_concept_briefs.md#phoneme_letter_card_01, activity_id=concept_phoneme_hunt_collect, trigger_condition=Child enters language treasure-hunt mode or photographs an everyday object suitable for sound play
- [x] assignment_type=activity_concept, activity_concept=Branching Choice Story, concept_source=examples/source_activity_concept_briefs.md#source_branching_story, description=AI tells a story with choice points; the child chooses between two next steps and the story continues from that choice, mechanic=decide, category=cat1, tier=T1, asset_policy=no_assets, activity_id=concept_branching_story_decide, trigger_condition=Child enters story mode or photographs a toy or object that can become a story character
- [x] assignment_type=activity_concept, activity_concept=Guess in 10, concept_source=examples/source_activity_concept_briefs.md#source_guess_in_10, description=AI gives step-by-step clues and the child uses evidence to guess an animal or object, with easier clues if the child gets stuck, mechanic=deduce, category=cat1, tier=T1, asset_policy=optional_support, asset_requirements=examples/source_activity_concept_briefs.md#guess_reference_cards_01, activity_id=concept_guess_in_10_deduce, trigger_condition=Child photographs an animal toy, animal picture, or enters guessing mode
- [x] assignment_type=activity_concept, activity_concept=Animal Sound Imitation, concept_source=examples/source_activity_concept_briefs.md#source_animal_sound_imitation, description=AI prompts a familiar animal and the child imitates its sound or speaks in that animal role, mechanic=motion_voice, category=cat1, tier=T0, asset_policy=optional_support, asset_requirements=examples/source_activity_concept_briefs.md#animal_sound_cards_01, activity_id=concept_animal_sound_motion_voice, trigger_condition=Child photographs an animal toy, animal picture, or enters animal-sound mode
- [x] assignment_type=match_pattern, activity_concept=Tiny Curator, concept_source=examples/source_activity_concept_briefs.md#source_tiny_curator, description=Child finds three or four objects that they think belong together, arranges a tiny exhibition, then explains their grouping rule, mechanic=sort, category=cat5, tier=T2, asset_policy=no_assets, activity_id=concept_tiny_curator_sort, trigger_condition=Child is at home or outdoors with several objects that can be grouped or compared
- [x] assignment_type=activity_concept, activity_concept=Partial Reveal Guess, concept_source=examples/source_activity_concept_briefs.md#source_partial_reveal_guess, description=Screen shows part of an animal or object; the child guesses the whole thing from visible clues and explains the evidence, mechanic=deduce, category=cat1, tier=T1, asset_policy=required_prebuilt, asset_requirements=examples/source_activity_concept_briefs.md#partial_reveal_cards_01, product_capabilities=requires_asset_display, activity_id=concept_partial_reveal_deduce, trigger_condition=Child photographs an animal toy, animal picture, or enters partial-reveal guessing mode

### Capability probes expected to block at Phase 0

- [ ] assignment_type=capability_probe, activity_concept=Coloring Game, concept_source=examples/source_activity_concept_briefs.md#source_coloring_game, description=Screen shows line art; the child chooses colors by taking photos and AI fills regions to create a shareable artwork, mechanic=build, category=cat5, tier=T1, asset_policy=runtime_generated, asset_requirements=examples/source_activity_concept_briefs.md#runtime_coloring_line_art_01, product_capabilities=requires_generated_image,requires_coloring_ui,requires_ui_state, activity_id=concept_coloring_game_probe, trigger_condition=Child photographs an object with a clear color or enters coloring mode
- [ ] assignment_type=capability_probe, activity_concept=Guided Drawing, concept_source=examples/source_activity_concept_briefs.md#source_guided_drawing, description=AI guides the child to use paper and pencil to complete a simple drawing step by step, then the child photographs the finished work, mechanic=build, category=cat3, tier=T1, asset_policy=optional_support, asset_requirements=examples/source_activity_concept_briefs.md#guided_drawing_step_cards_01, product_capabilities=requires_materials,before_after_risk, activity_id=concept_guided_drawing_probe, trigger_condition=Child is indoors and photographs an object that could become a drawing theme
