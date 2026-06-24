# Skip Intro Rules Only Packages Plan

**Goal:** Update four runtime-verified packages so the authored flow starts with rules only and keeps the first child action prompt in Round/Collect 1.

**Scope:**
- `concept_phoneme_hunt_collect`
- `concept_emotion_reader_care`
- `concept_partial_reveal_deduce`
- `concept_animal_sound_motion_voice`

**Implementation:**
1. Remove each package's separate `Step 1: Transition Bridge`.
2. Make the new `Step 1: Rules` explain only the rule/mission and asset fallback.
3. Keep the first invitation or action request in Round/Collect 1.
4. Renumber later production steps and update `spec.md` asset `use_step` references.
5. Leave metadata and assets untouched unless runtime consumers require a separate contract update.

**Validation:**
- Confirm no package `prod.md` contains `Step 1: Transition Bridge`, intro-scene references, or rules-step first-action invitations.
- Confirm Round/Collect 1 still contains the first action prompt.
- Run `git diff --check`.
