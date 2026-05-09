# Review Notes

Run id: `20260509_153004_activity_concepts`

Independent review notes, repair notes, and residual risks will be appended after each generated package passes author checks.

## 001 -- concept_scavenger_hunt_collect

- Initial independent review found one blocking issue: Dimension 5 Tier Appropriateness failed because several spoken T1 AI lines were too sentence-heavy.
- Repair: shortened spoken runtime dialogue in `prod.md` while preserving the Cat5 collect loop, edge branches, and screen states.
- Fresh independent review passed all 10 dimensions and package invariants.
- Residual risk: this is a parameterized activity; runtime must supply or ask the child to confirm `{shared_feature}`, `{starter_entity}`, and `{extra_connection}` placeholders.

## 002 -- concept_phoneme_hunt_collect

- Independent review passed all 10 dimensions and package invariants.
- Asset handling verified: `phoneme_letter_card_01` is optional, defined in `spec.md` `## Asset Brief`, referenced by ID in `prod.md`, and has a voice-only fallback.
- Scaffold compromise verified: phoneme matching is represented as `observation_angle: pattern` because the closed enum has no sound/phoneme angle; this is disclosed in `spec.md`.
- Residual risk: the package uses `/b/` as the concrete target sound because the companion asset prompt is specifically authored for B/b.

## 003 -- concept_branching_story_decide

- Initial independent review found two blocking issues: Dimension 9 Game Feel and Dimension 10 Mechanic Fidelity failed because choices were recorded without distinct consequences.
- Repair: revised Step 3 and Step 4 so the door changes the world/path, the helper changes the road, and the ending changes the payoff.
- Fresh independent review passed all 10 dimensions and package invariants.
- Residual risk: branching remains voice-led with simple path tokens; it does not implement a complex branching UI.

## 004 -- concept_guess_in_10_deduce

- Initial independent review found one blocking issue: Dimension 3 Edge Case Coverage failed because Round 1's unexpected follow-up did not validate uncertainty before redirecting.
- Repair: revised the Round 1 unexpected follow-up to validate that mystery clues can feel tricky before redirecting toward water-compatible guesses.
- Fresh independent review passed all 10 dimensions and package invariants.
- Asset handling verified: `guess_reference_cards_01` is optional, defined in `spec.md` `## Asset Brief`, referenced by ID in `prod.md`, and has a voice-only fallback.
- Residual risk: the runtime version uses three clue rounds rather than ten to keep the T1 package concise.
