# Source Intent Audit: `concept_phoneme_hunt_collect`

## Evidence

- Active assignment: `assignments.md:46`
- Goal scope and source lock: `goals/2026-06-03-subset-agentic-validation-goal.md:29-33`, `goals/2026-06-03-subset-agentic-validation-goal.md:63-65`
- Workbook baseline: `inputs/original_activity_concepts_2026-05-29.tsv:3`
- Normalized source: `inputs/source_activity_concepts.md:29-44`
- Letter card asset: `inputs/source_activity_concepts.md:740-755`
- Source-promise rules: `program.md:23-25`, `program.md:300-304`, `program.md:898-904`
- Cat5/collect scaffold: `templates.md:88-99`, `templates.md:301-308`, `program.md:942-945`

## Original Play Frame

AI is playfully hungry and wants words beginning with the target sound, exemplified as `/b/ /b/ /b/`; the child is asked to find one matching "treasure" and show it. The workbook row is singular: find one object/treasure whose word starts with the sound (`inputs/original_activity_concepts_2026-05-29.tsv:3`). The goal repeats this as "one indoor treasure" (`goals/2026-06-03-subset-agentic-validation-goal.md:63-65`).

## Child Role

The child is an indoor sound treasure hunter. They hear the target phoneme, search the room, choose one real object whose spoken name starts with that sound, and show/photograph it (`assignments.md:46`; `inputs/source_activity_concepts.md:35`, `inputs/source_activity_concepts.md:43-44`).

## Device Role / Action

The AI introduces the target sound, keeps the frame playful rather than test-like, prompts the hunt, optionally shows a matching letter card, reacts to the child's shown treasure, and uses voice-only fallback if the card is unavailable (`inputs/source_activity_concepts.md:36`, `inputs/source_activity_concepts.md:44`, `inputs/source_activity_concepts.md:750-754`).

## Interaction Sequence

1. AI gives a playful hunger/treasure hook and target sound.
2. Optional card cue appears for the target sound/letter.
3. Child searches indoors.
4. Child photographs or shows one matching treasure.
5. AI reacts gently, asks for the object name or first sound if needed, then celebrates the sound-treasure match.

## Required Child Actions

- Hear the target sound.
- Find one indoor real-world object.
- Show or photograph the object.
- Name or confirm the object if runtime judgment is ambiguous.
- No required letter reading, multi-object collection, formal assessment, or worksheet-style answer.

## Asset / Letter Cue Requirement

`phoneme_letter_card_01` is optional support, not a required gameplay dependency (`inputs/source_activity_concepts.md:41-42`, `inputs/source_activity_concepts.md:747`). It is a pre-generated card for `/b/`, used at task start and again if the child forgets (`inputs/source_activity_concepts.md:748-754`). If unavailable, AI must repeat the sound by voice and must not claim a letter is visible (`inputs/source_activity_concepts.md:754`).

## Allowed Adaptations

- Parameterize the target sound, provided the sound remains the collection criterion (`inputs/source_activity_concepts.md:38`, `inputs/source_activity_concepts.md:44`).
- Use a treasure/mission wrapper, as long as the child still finds one indoor object.
- Ask the child to say the object name before judging beginning sound.
- Mark demo support as degraded `cat5_judgment`, because beginning-sound validation is runtime judgment, not simple visual collection (`program.md:292-296`).
- If Cat5 synthesis scaffolding is required, use it only as a brief recap of the one found treasure and target sound; disclose any scaffold compromise.

## Hard Drift Risks

- Expanding to generic 3-4 item Cat5 collection because templates usually expect multiple photo rounds (`templates.md:302-306`) despite the source/goal requiring one treasure.
- Changing the criterion from beginning sound to color, shape, category, object sound, or semantic theme.
- Making the activity a formal phonics quiz or requiring the child to read the letter.
- Treating the optional letter card as mandatory, or claiming it is on screen when absent.
- Claiming fully supported camera validation for beginning sound instead of degraded runtime judgment (`program.md:293-296`).
- Replacing the real indoor hunt with generic picker placeholders or stock collection items.
- Ending with a generic badge instead of a payoff tied to the found treasure and target sound.

## Pre-Package Verdict

**PASS with constraints.** Source intent is clear enough to package: one indoor phoneme treasure hunt, collect mechanic, optional letter-card support, degraded beginning-sound judgment. Any package that inflates the activity into a multi-object generic scavenger hunt, requires the card, omits the child's real-world photo/show action, or hides the runtime-judgment limitation should fail source intent.
