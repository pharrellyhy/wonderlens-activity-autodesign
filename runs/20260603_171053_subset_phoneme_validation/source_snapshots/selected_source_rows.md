# Selected Source Rows

## Workbook Baseline

Source file: `inputs/original_activity_concepts_2026-05-29.tsv`

```tsv
音素寻宝	2026/04/30	属性	Cat 5. 需结合拍照	室内	3. 收集/配对 Collect/Match/Pair/Associate/Generalize	低	我今天很饿，我想吃一些以 /b/ /b/ /b/ 开头的词语。你能找一个这样的‘宝贝’给我看吗？	是Scavenger的形式，但是因为特殊属性因此单独列出，屏幕上可以展示对应的字母
```

English lock:

- Original play frame: a phoneme treasure hunt, modeled like a scavenger hunt.
- Target sound: `/b/ /b/ /b/`.
- Child action: find one treasure whose spoken word starts with `/b/`, then show it with the camera.
- Device action: introduce the target sound and ask for one matching treasure.
- Setting/category: indoor Cat5 collection/photo play.
- Asset note: the screen may show the corresponding letter; this is support, not the core mechanic.

## Normalized Helper

Source file: `inputs/source_activity_concepts.md#source_phoneme_hunt`

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

## Asset Requirement Helper

Source file: `inputs/source_activity_concepts.md#phoneme_letter_card_01`

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
