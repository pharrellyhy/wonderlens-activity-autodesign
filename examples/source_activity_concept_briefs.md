# Source Activity Concept Briefs

Source workbook: local concept workbook, `Sheet1`

Purpose: companion source context for the source-concept assignments in `assignments.md` Batch 4. These rows preserve source intent, normalize mechanics and asset policy, and provide direct English `prompt_en` values for assets when needed.

Language rule: source concepts may arrive in Chinese, but all normalized concept fields below are English so generated adaptation briefs and activity packages stay English-only.

## Selected Concept Rows

### source_scavenger_hunt

| Field | Value |
|---|---|
| source_row | 1 |
| activity_concept | Scavenger Hunt |
| normalized_description_en | Find several things that share a color, shape, or category. |
| normalized_notes_en | This is a reusable core format for properties and categories. For higher tiers, extend beyond collection by asking the child to name the collected items, tell a tiny story with them, or identify one additional shared feature. |
| assignment_type | match_pattern |
| input_mode_hint | parameterized |
| mechanic | collect |
| category | cat5 |
| asset_policy | no_assets |
| trigger_condition_en | Child photographs an object with a clear color, shape, or category feature. |
| adaptation_notes_en | Use runtime placeholders such as `{matched_color}`, `{matched_shape}`, or `{entity_class}`. Do not invent entity-specific facts. Step 3 repeated action must be find, photograph, and collect. |

### source_phoneme_hunt

| Field | Value |
|---|---|
| source_row | 2 |
| activity_concept | Phoneme Treasure Hunt |
| normalized_description_en | The AI introduces a target sound, then the child finds an object whose word starts with that sound. |
| normalized_notes_en | This is a sound-focused Scavenger Hunt variant. A letter card can support the task, but voice-only fallback must work. |
| assignment_type | match_pattern |
| input_mode_hint | parameterized |
| mechanic | collect |
| category | cat5 |
| asset_policy | optional_support |
| asset_requirements | phoneme_letter_card_01 |
| trigger_condition_en | Child enters language treasure-hunt mode or photographs an everyday object suitable for sound play. |
| adaptation_notes_en | Keep the activity playful rather than formal phonics assessment. The target sound becomes the collection criterion. |

### source_branching_story

| Field | Value |
|---|---|
| source_row | 3 |
| activity_concept | Branching Choice Story |
| normalized_description_en | The AI tells a story with choice points, and the child's choices decide what happens next. |
| normalized_notes_en | This may need authored story planning for high quality. For the current package workflow, keep it voice-led and disclose assumptions if story branching is generated dynamically. |
| assignment_type | activity_concept |
| input_mode_hint | concept_only |
| mechanic | narrate |
| category | cat1 |
| asset_policy | no_assets |
| trigger_condition_en | Child enters story mode or photographs a toy or object that can become a story character. |
| adaptation_notes_en | Do not require a complex visual branching UI. If the story uses a photographed object, treat it as a catalyst rather than a factual subject. |

### source_guess_in_10

| Field | Value |
|---|---|
| source_row | 18 |
| activity_concept | Guess in 10 |
| normalized_description_en | The AI gives clues one by one, and the child guesses an animal or object from the evidence. |
| normalized_notes_en | Clue difficulty should vary by tier. If the child cannot guess, the AI gives easier clues and reduces frustration. Optional pictures can support the reveal. |
| assignment_type | activity_concept |
| input_mode_hint | concept_only |
| mechanic | deduce |
| category | cat1 |
| asset_policy | optional_support |
| asset_requirements | guess_reference_cards_01 |
| trigger_condition_en | Child photographs an animal toy, animal picture, or enters guessing mode. |
| adaptation_notes_en | Step 3 must follow clue, child guess, AI confirmation or next clue. Pictures are support only; runtime copy must not claim a picture is displayed unless the asset is available. |

### source_animal_sound_imitation

| Field | Value |
|---|---|
| source_row | 13 |
| activity_concept | Animal Sound Imitation |
| normalized_description_en | The AI prompts a familiar animal, and the child imitates its sound or speaks in the animal role. |
| normalized_notes_en | Screen animal cards are optional. The activity should focus on voice, role play, and short low-pressure turns. |
| assignment_type | activity_concept |
| input_mode_hint | concept_only |
| mechanic | voice |
| category | cat1 |
| asset_policy | optional_support |
| asset_requirements | animal_sound_cards_01 |
| trigger_condition_en | Child photographs an animal toy, animal picture, or enters animal-sound mode. |
| adaptation_notes_en | Use common animals for younger children. The core child action is making a sound or speaking in role, not answering trivia. |

### source_tiny_curator

| Field | Value |
|---|---|
| source_row | 14 |
| activity_concept | Tiny Curator |
| normalized_description_en | The child finds three or four objects they think belong together, arranges them as a tiny exhibition, and explains their grouping rule. |
| normalized_notes_en | This is related to Scavenger Hunt, but the child defines the shared feature instead of the AI giving one in advance. |
| assignment_type | match_pattern |
| input_mode_hint | parameterized |
| mechanic | sort |
| category | cat5 |
| asset_policy | no_assets |
| trigger_condition_en | Child is at home or outdoors with several objects that can be grouped or compared. |
| adaptation_notes_en | Prioritize `sort`: child-made rule, grouping, and explanation. Do not make the AI impose one correct category before the child acts. |

### source_partial_reveal_guess

| Field | Value |
|---|---|
| source_row | 11 |
| activity_concept | Partial Reveal Guess |
| normalized_description_en | The screen shows one distinctive part of an animal or object, and the child guesses the whole thing from visible clues. |
| normalized_notes_en | This requires prebuilt images in a consistent style. Each session can use three to five challenges. The same animal may have multiple cards showing different parts. |
| assignment_type | activity_concept |
| input_mode_hint | concept_only |
| mechanic | deduce |
| category | cat1 |
| asset_policy | required_prebuilt |
| asset_requirements | partial_reveal_cards_01 |
| product_capabilities | requires_asset_display |
| trigger_condition_en | Child photographs an animal toy, animal picture, or enters partial-reveal guessing mode. |
| adaptation_notes_en | The generated package must include an Asset Brief. If display assets are unavailable, fall back to a voice-only partial-clue riddle and do not claim the screen is showing an image. |

### source_coloring_game

| Field | Value |
|---|---|
| source_row | 8 |
| activity_concept | Coloring Game |
| normalized_description_en | The screen shows line art with regions to color. The child chooses colors by photographing objects, and the system fills the regions to create a shareable artwork. |
| normalized_notes_en | Limit the number of captured colors. The line art should be interesting but simple. One color may fill multiple regions. |
| assignment_type | capability_probe |
| input_mode_hint | concept_only |
| mechanic | build |
| category | cat5 |
| asset_policy | runtime_generated |
| asset_requirements | runtime_coloring_line_art_01 |
| product_capabilities | requires_generated_image, requires_coloring_ui, requires_ui_state |
| trigger_condition_en | Child photographs an object with a clear color or enters coloring mode. |
| adaptation_notes_en | Block in the current workflow unless product support exists for runtime line-art generation, fillable-region UI, color state storage, and artwork export. |

### source_guided_drawing

| Field | Value |
|---|---|
| source_row | 4 |
| activity_concept | Guided Drawing |
| normalized_description_en | The AI guides the child to use paper and pencil to complete a simple drawing step by step. |
| normalized_notes_en | The source idea is a simple sketch workflow. The child photographs the finished work at the end, but quality is not evaluated; the value is in the process and celebration. |
| assignment_type | capability_probe |
| input_mode_hint | concept_only |
| mechanic | build |
| category | unsupported_cat3 |
| asset_policy | optional_support |
| asset_requirements | guided_drawing_step_cards_01 |
| product_capabilities | requires_materials, before_after_risk |
| trigger_condition_en | Child is indoors and photographs an object that could become a drawing theme. |
| adaptation_notes_en | Do not force this into the current Cat1/Cat5 package workflow. Output a Phase 0 brief and block unless product support for material workflows and final-work capture is declared. |

## Asset Requirements

### phoneme_letter_card_01

| Field | Value |
|---|---|
| asset_id | phoneme_letter_card_01 |
| concept_ref | source_phoneme_hunt |
| asset_type | card_set |
| requiredness | optional |
| generation_timing | pre_generated |
| use_step | prod.step_1; prod.step_3.round_1 |
| purpose_en | Give the child a visual reminder of the target sound and letter. |
| prompt_en | Create a simple child-friendly phonics card for the /b/ sound. Show uppercase B and lowercase b in large rounded letters, include one small friendly picture of a ball and one banana, use a clean light background, no extra words, suitable for children ages 4-6. |
| source | new_ai_generated_asset |
| display_behavior_en | Show the card at task start and briefly again if the child forgets the target sound. |
| fallback_behavior_en | If the card is unavailable, the AI repeats the target sound by voice only and must not claim the screen is showing a letter. |
| safety_constraints_en | No real child photos, no brands, no complex text, and no cluttered composition. |

### guess_reference_cards_01

| Field | Value |
|---|---|
| asset_id | guess_reference_cards_01 |
| concept_ref | source_guess_in_10 |
| asset_type | card_set |
| requiredness | optional |
| generation_timing | pre_generated |
| use_step | prod.step_2; prod.step_3.round_1-3 |
| purpose_en | Provide optional reference pictures before or after a clue round to reduce frustration. |
| prompt_en | Create a set of friendly reference cards for common animals and household objects for a children's guessing game. Use one centered object per card, plain light background, clear recognizable shapes, soft colors, no text, no scary expressions. |
| source | new_ai_generated_asset |
| display_behavior_en | Show the matching card after the answer is revealed, or show a partial hint card if the child is stuck. |
| fallback_behavior_en | If cards are unavailable, the AI continues with voice clues and encouragement and must not claim the screen is showing a picture. |
| safety_constraints_en | No real child photos, friendly animal expressions, and no dangerous scenes. |

### animal_sound_cards_01

| Field | Value |
|---|---|
| asset_id | animal_sound_cards_01 |
| concept_ref | source_animal_sound_imitation |
| asset_type | card_set |
| requiredness | optional |
| generation_timing | pre_generated |
| use_step | prod.step_2; prod.step_3.round_1-3 |
| purpose_en | Help the child recognize the animal they are about to imitate. |
| prompt_en | Create a set of friendly animal picture cards for toddlers and preschoolers. Include common animals such as cat, dog, cow, duck, sheep, and lion. Use a plain bright background, simple expressive illustrations, one animal per card, no text, no scary poses. |
| source | new_ai_generated_asset |
| display_behavior_en | Show one animal card each round while the AI invites the child to imitate its sound. |
| fallback_behavior_en | If cards are unavailable, the AI describes the animal by voice and must not claim the screen is showing a picture. |
| safety_constraints_en | No real child photos, no attack or predation scenes, and friendly animal poses only. |

### partial_reveal_cards_01

| Field | Value |
|---|---|
| asset_id | partial_reveal_cards_01 |
| concept_ref | source_partial_reveal_guess |
| asset_type | card_set |
| requiredness | required |
| generation_timing | pre_generated |
| use_step | prod.step_2; prod.step_3.round_1-3 |
| purpose_en | Provide visible partial evidence so the child can infer the whole animal or object. |
| prompt_en | Create a set of partial-reveal animal guessing cards for children ages 4-6. Each card should show only one distinctive part of a common animal, such as a tiger tail, rabbit ears, elephant trunk, duck feet, or fish scales. Use a consistent soft illustration style, plain light background, no text, no scary details, and keep the cropped part large and easy to inspect. |
| source | new_ai_generated_asset |
| display_behavior_en | Show one partial-reveal card full screen each round. The child observes the part, guesses the whole, and explains the evidence. |
| fallback_behavior_en | If partial cards are unavailable, switch to a voice-only partial-clue riddle and do not claim the screen is showing a picture. |
| safety_constraints_en | No real child photos, no gore or scary details, no predation scenes, and clear inspectable cropped parts. |

### runtime_coloring_line_art_01

| Field | Value |
|---|---|
| asset_id | runtime_coloring_line_art_01 |
| concept_ref | source_coloring_game |
| asset_type | line_art |
| requiredness | required |
| generation_timing | runtime_generated |
| use_step | prod.step_2; prod.step_3.round_1-3 |
| purpose_en | Convert a photographed object into a fillable line drawing and apply colors chosen from the child's photos. |
| prompt_en | Generate a simple coloring-page line drawing based on the photographed object. Use clean black outlines, 3 to 5 large enclosed regions for coloring, no shading, no text, no background clutter, child-friendly proportions, and clear separation between regions. |
| source | future_runtime_image_generation |
| display_behavior_en | Show the line art at runtime and fill a selected region after each child color photo. |
| fallback_behavior_en | If runtime generation and coloring UI are unsupported, block at Phase 0 and do not generate an activity package. |
| safety_constraints_en | Do not generate real child portraits, copyrighted characters, or detailed dangerous objects. |

### guided_drawing_step_cards_01

| Field | Value |
|---|---|
| asset_id | guided_drawing_step_cards_01 |
| concept_ref | source_guided_drawing |
| asset_type | card_set |
| requiredness | optional |
| generation_timing | pre_generated |
| use_step | prod.step_2; prod.step_3.round_1-4 |
| purpose_en | Provide optional visual steps for a simple drawing task. |
| prompt_en | Create a set of step-by-step drawing cards for children ages 4-6. Show how to draw a simple friendly object in 4 clear steps using thick black sketch lines, large shapes, no text, minimal details, and a plain white background. |
| source | new_ai_generated_asset |
| display_behavior_en | Show one step card at a time while the AI leaves enough time for the child to draw on paper. |
| fallback_behavior_en | If step cards are unavailable, use voice-only step descriptions; the Cat3 material workflow still requires product approval before package generation. |
| safety_constraints_en | No real child photos, no fine-copying requirement, and only simple non-dangerous drawing themes. |
