# concept_phoneme_hunt_collect Image Visual Audit

Run: `20260603_171053_subset_phoneme_validation`

Reviewed actual rebuilt package PNGs under:

```text
runs/20260603_171053_subset_phoneme_validation/activity_packages/concept_phoneme_hunt_collect/assets/
runs/20260603_171053_subset_phoneme_validation/activity_packages/concept_phoneme_hunt_collect/assets/items/
```

Review artifact:

```text
runs/20260603_171053_subset_phoneme_validation/image_qa/source_contact_sheet.png
```

Review method: rebuilt all package-local PNGs from the repaired imagegen inbox,
created a contact sheet from the actual package PNGs, and visually inspected the
scene bundle plus item sprites. This audit is based on rendered images, not only
`asset_manifest.yaml`, work items, or prompt text.

## Verdict

PASS image QA after shared-stage scene repair.

The repaired scene bundle now communicates a coherent phoneme treasure hunt:
listen, practice the beginning sound, search the room, name the found object,
connect the spoken word to the sound rule, celebrate, and close. The old
basket/card/container motif has been removed from runtime scenes. The scenes now
use a repeated low-clutter playroom, a stable child, and a recognizable rounded
rectangular WonderLens device instead of an unexplained circle on the rug. The
scene PNGs keep app-owned UI, photo/name overlays, progress, and selectable item
sprites out of the backgrounds.

## Scene Findings

| Asset | Visual finding | QA result |
| --- | --- | --- |
| `activity_icon__round_512.png` | Child profile, sound cue, magnifier, and search path communicate listening plus search without revealing a target object. | PASS |
| `b_sound_letter_cue__round_512.png` | Unframed mouth-and-sound-wave pictogram; not a blank cue card and no readable mark. | PASS |
| `intro_scene__round_512.png` | Child listens beside a rounded rectangular WonderLens device before the sound is named. | PASS |
| `rules_scene__round_512.png` | Child practices the sound with mouth/speech cues and sound waves moving to the device. | PASS |
| `round_1_scene__round_512.png` | Child rehearses the sound with mouth/ear action; no baked B examples. | PASS |
| `round_2_scene__round_512.png` | Child actively searches the low-clutter room with the device in hand; no answer object or camera UI is baked in. | PASS |
| `round_3_scene__round_512.png` | Child speaks toward the device and points to unmarked open space reserved for runtime evidence overlay; no photo slot, panel, marked placeholder, or accepted object is baked in. | PASS |
| `synthesis_scene__round_512.png` | Sound-wave connection makes the spoken-name to beginning-sound rule visible without checkmarks, badges, letters, or item objects. | PASS |
| `celebrate_scene__round_512.png` | Celebration is tied to child/device sound-wave success, not generic container sparkle. | PASS |
| `closing_scene__round_512.png` | Calm finishing scene in the same low-clutter room with the device still visible and a fading sound ribbon. | PASS |

## Item Findings

The package now provides consumer-parity catalog coverage under `assets/items/`:

- Correct /b/ items: `ball_object`, `banana_object`, `book_object`, `box_object`
- Distractors: `cup_object`, `sock_object`, `apple_object`, `car_object`,
  `hat_object`, `mug_object`, `shoe_object`, `spoon_object`

All item sprites are centered, text-free, visually readable, and separated from
story-scene backgrounds.

## Repair Summary

- Rewrote scene prompts and runtime screen copy to foreground listening,
  speaking, sound waves, search motion, evidence areas, and a reusable
  shared-stage contract.
- Regenerated all story scenes with Codex built-in imagegen using the repeated
  low-clutter playroom and rounded rectangular WonderLens device prompts.
- Retained the already accepted item sprites and support assets.
- Downsampled accepted source PNGs to 512x512 before the asset build.
- Rebuilt package-local runtime PNGs with `scripts/build_activity_assets.py`.
- Refreshed WonderLens AI and fullstack-demo run-local evidence to reflect the
  4-correct/8-distractor catalog and one-treasure collection count.
