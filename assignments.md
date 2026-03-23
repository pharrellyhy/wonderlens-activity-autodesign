# Activity Design Assignments

> Each line is one assignment. The agent works through them top to bottom.
> Mark completed assignments with [x]. The agent skips completed ones.
>
> Format: `- [ ] entity + category (number/name), tier=TX, style=game_style, scene=optional`
> Game styles: `voice_acting`, `storytelling_chain`, `prediction_game`, `helper_hotline` (Cat 1) | `comparison_chart`, `naming_story` (Cat 5)
> If `style=` is omitted, the agent infers it per program.md §1.6.

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
