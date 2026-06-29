# Skip Intro Rules Only Packages Goal

Objective: remove the separate intro step from four runtime-verified activity packages, keep the rules step explanation-only, and reserve the first play invitation for Round/Collect 1.

Plan: `docs/plans/2026-06-24-skip-intro-rules-only-packages.md`

Completion criteria:
- The four package `prod.md` files begin with `Step 1: Rules`.
- The rules step does not ask the child to play, confirm readiness, or provide the first activity response.
- Round/Collect 1 remains the first place where the child is invited to act.
- `spec.md` asset `use_step` references match the renumbered flow.
- Targeted text scans and `git diff --check` pass.
