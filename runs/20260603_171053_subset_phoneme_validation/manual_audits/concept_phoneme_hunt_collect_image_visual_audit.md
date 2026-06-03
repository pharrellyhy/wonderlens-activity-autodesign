# concept_phoneme_hunt_collect Image Visual Audit

Run: `20260603_171053_subset_phoneme_validation`

Reviewed actual package PNGs under:

```text
runs/20260603_171053_subset_phoneme_validation/activity_packages/concept_phoneme_hunt_collect/assets/
runs/20260603_171053_subset_phoneme_validation/activity_packages/concept_phoneme_hunt_collect/assets/items/
```

Review method: built a temporary contact sheet from the package-local PNGs and
visually inspected the scene bundle and item sprites. This audit is based on the
actual images, not only `asset_manifest.yaml`, work items, or prompt text.

## Verdict

Fail image QA.

The images are technically generated PNGs and most item sprites are readable,
but the scene bundle does not make semantic sense for a phoneme treasure hunt.
Most scenes are placeholder visuals: basket, blank card, glow, or empty nursery
space. The child action and learning evidence are not visually legible.

The story-scene bundle also fails real-world coherence. It does not establish a
plausible activity world with stable camera/framing or concrete beat-to-beat
changes. The scenes read as isolated prompt symbols on soft backgrounds rather
than moments in one coherent child-facing activity.

## Scene Findings

| Asset | Visual finding | QA result |
| --- | --- | --- |
| `activity_icon__round_512.png` | Basket with small sound-wave marks. It reads as a container icon, not a phoneme hunt. | Fail: weak semantic fit |
| `b_sound_letter_cue__round_512.png` | Blank decorative card. It does not communicate `/b/`, beginning sound, listening, or speaking. | Fail: placeholder cue |
| `intro_scene__round_512.png` | Cozy room with basket and abstract sound lines. The scene gives no clear child action. | Fail: nonsensical scene |
| `rules_scene__round_512.png` | Child sitting beside basket and blank card. The blank card dominates but carries no runtime meaning in the PNG. | Fail: placeholder scene |
| `round_1_scene__round_512.png` | Basket plus blank card/sound marks. It does not show practicing the `/b/` sound. | Fail: placeholder scene |
| `round_2_scene__round_512.png` | Empty indoor path with basket. It does not show search evidence or a usable runtime state. | Fail: nonsensical scene |
| `round_3_scene__round_512.png` | Basket with glow. It does not show accepted sound evidence or child-provided item handling. | Fail: placeholder scene |
| `synthesis_scene__round_512.png` | Abstract shape entering basket. It does not make the beginning-sound synthesis visually clear. | Fail: weak semantic fit |
| `celebrate_scene__round_512.png` | Basket with sparkles/glow. This is generic celebration, not activity-specific payoff. | Fail: weak semantic fit |
| `closing_scene__round_512.png` | Basket in room with sound-wave marks. It repeats the same nonspecific motif. | Fail: repeated placeholder motif |

## Item Findings

The item sprites are mostly readable and correctly separated under
`assets/items/`, but the catalog is too small for the fullstack Cat5 contract.

Current catalog:

- Correct: `ball_object`, `banana_object`, `book_object`
- Distractors: `cup_object`, `sock_object`

Required for consumer parity unless explicitly waived by the run goal:

- 4 correct items
- 8 distractors

## Prompt Root Cause

The failure came from the image prompts. The manifest repeatedly requested
subjects such as `empty basket`, `sound basket`, `collection basket`, `blank cue
backing`, `acceptance glow`, and `abstract treasure shape`. Those subjects were
not tied to a visible child action or phoneme-learning evidence, so imagegen
correctly rendered a nice-looking but meaningless basket/card/glow motif.

This is not an imagegen quality problem first. It is an asset-brief problem:
the prompt optimized for avoiding target-object leakage and UI/text leakage,
but did not specify what real-world scene the child is in or what the scene
should communicate.

## Regeneration Direction

Regenerate the scene bundle from beat-specific visual subjects:

- `activity_icon`: child-friendly listening/search icon with mouth/sound-wave
  cue and small search path; no basket.
- `intro_scene`: establish one plausible room where the child can listen and
  search, with the same child/space language used by later scenes; no basket or
  blank card.
- `rules_scene`: show the child practicing the beginning sound in that same
  room, with mouth/sound-wave cues and a clear activity focus; no blank card as
  the main subject.
- `round_1_scene`: close but still real-world moment of the child listening and
  practicing `/b/`; no literal letters, no blank card.
- `round_2_scene`: same room/search area with the child looking for a real
  object and a sound-wave trail guiding the search; no basket.
- `round_3_scene`: same visual world after the child names a matching item,
  showing accepted sound evidence as an app-owned overlay area or concrete
  child reaction, not a basket/glow-only scene.
- `synthesis_scene`: same setting with multiple spoken-name sound waves
  converging into one beginning-sound pattern; no container.
- `celebrate_scene`: same child/world celebrating the sound discovery; no
  generic sparkle basket.
- `closing_scene`: calm finishing moment in the same setting; no repeated basket
  motif.

Regeneration prompts must explicitly ban: basket, treasure chest, blank card,
blank board, empty container, generic glow-only subject, and decorative empty
room unless the individual beat explicitly requires that subject.
