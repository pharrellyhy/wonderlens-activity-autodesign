# Runtime Conversion And Parity Implementation Plan

Date: 2026-05-26

Status: Planned

Refresh note: This plan was refreshed to match the current
`plan-goal-creator` workflow. The plan is the design source and should stay
code-light. The paired goal is the execution contract. File paths and commands
below are current evidence and validation targets; an executor must still
inspect the target repos before editing.

## Goal

Create a repeatable runtime conversion path that lets WonderLens activity
packages become executable in both:

- `/Users/pharrelly/codebase/gitlab/wonderlens-ai`
- `/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo`

The plan has three phases:

1. Build a deterministic package-to-runtime conversion layer, incorporating the
   existing `wonderlens-ai` runtime YAML generator plan.
2. Add consumer adapters so the same canonical runtime data can feed
   `wonderlens-ai` package loading and fullstack-demo markdown frontmatter.
3. Add runtime/UI extensions only for activities that cannot honestly fit the
   current Cat1/Cat5 demo primitives, then validate live response parity.

This is an umbrella plan. It should guide future implementation across repos,
but it does not itself change runtime behavior.

## Execution Boundary

This plan lives in `wonderlens-activity-autodesign` because that repo owns the
activity-package source material and cross-repo conversion requirements.
Implementation will mostly happen elsewhere:

| Repo | Expected ownership |
|---|---|
| `wonderlens-activity-autodesign` | Source packages, run-output fixtures, conversion contract documentation, optional exported fixture inputs. |
| `wonderlens-ai` | Canonical runtime YAML generator, validation, package adapter checks, optional parity harness. |
| `wonderlens-activity-fullstack-demo` | Baseline parser/runtime reference, generated frontmatter fixtures only when intentionally reviewed, later UI/runtime extensions if Phase 3 is authorized. |

Do not assume these paths are the only possible implementation locations. They
describe the current architecture and should be verified at execution time.

## Current Evidence

Autodesign activity packages currently contain five human/reviewer-facing files:

```text
activities/<activity_id>/
  spec.md
  prod.md
  tag_block.yaml
  recap.template.yaml
  dashboard.template.yaml
```

Run-local packages use the same shape under:

```text
runs/20260521_163621_workbook_review_packet_full/activity_packages/<activity_id>/
```

The curated `activities/*/prod.md` files are often strong enough as source
material. Examples such as `activities/time_machine_dinosaur/prod.md`,
`activities/fluffy_expedition_dandelion/prod.md`, and
`activities/concept_phoneme_hunt_collect/prod.md` contain concrete child-facing
beats, branch policies, and screen/fallback guidance.

The full run output is not ready to use directly as runtime prompt guidance.
The following generic phrases were present across run-local `prod.md` files:

| Phrase | Matching run packages |
|---|---:|
| `Open from the source trigger` | 40 |
| `I found a small mission` | 40 |
| `Rule: I prompt` | 40 |
| `source-intent cue` | 40 |
| `What is your first try` | 33 |
| `Your turns made the board light up` | 40 |
| `RESOLVED BLOCKER` | 32 |

Those phrases did not appear in fullstack-demo `backend/games/*.md`. They must
be rejected or rewritten before runtime export.

Fullstack-demo currently loads only top-level markdown files under
`backend/games/*.md` that start with YAML frontmatter. `backend/game_loader.py`
skips markdown without frontmatter, and `backend/game_parser.py` converts the
frontmatter into `EntityConfig` plus `InstructionRecipe`. The runtime overlay
uses only compact instruction fields:

- non-round steps: `goal`, `constraint`, `emotion_tag`;
- rounds: `round_number`, `goal`, `scenario`, `constraint`, `emotion_tag`,
  `acceptable_themes`, `escalation_note`;
- visual contract: `screen_frames` and optional `celebration_frame`.

`wonderlens-ai` already has a plan at:

```text
/Users/pharrelly/codebase/gitlab/wonderlens-ai/docs/plans/2026-05-15-activity-runtime-yaml-generator.md
```

That plan is not implemented yet. The expected files were not present when
checked:

- `app/modules/activity/packages/runtime_generator.py`
- `scripts/generate_activity_runtime.py`

The `wonderlens-ai` package loader currently requires `runtime.yaml` and
validates it through `ActivityRuntime`. `game_definition_from_package(...)`
adapts only executable `cat1` and `cat5` packages.

## Settled Decisions

- Do not rerun full activity generation just to make activities executable.
  Reuse the current packages as source material.
- Do not feed raw `prod.md` prose directly into fullstack-demo prompts.
  Convert it into a compact machine runtime contract.
- Do not use an LLM in the v1 converter. Use deterministic parsing,
  quality gates, and optional curated overrides. An LLM may be used later for
  offline review suggestions, never as an unreviewed request-path dependency.
- Treat the existing `wonderlens-ai` runtime YAML generator plan as the Phase 1
  baseline, but expand it into a canonical runtime contract that can also drive
  fullstack-demo exports.
- Keep fullstack-demo runtime code unchanged in Phase 1 and Phase 2. Export
  markdown frontmatter in the shape it already parses.
- Add fullstack runtime/UI changes only in Phase 3 for activities that cannot
  be made playable with existing primitives.
- Run live server/API parity checks as release validation, not as the first
  deterministic test gate.

## Non-Goals

- No request-path runtime generation from `prod.md`.
- No broad rewrite of fullstack-demo architecture.
- No Java or mobile-client contract changes in Phase 1 or Phase 2.
- No claim that unsupported mechanics are playable when they require new UI.
- No automatic activity approval based only on converter success.
- No secret, `.env`, credential JSON, provider-token, or production-data edits.

## Canonical Runtime Contract

The converter should produce a canonical runtime object that can be serialized
as `runtime.yaml` and then adapted for consumers.

Required common fields:

```yaml
activity_id: concept_phoneme_hunt_collect
template_type: cat5
category: category_5
entity_name: sound_object
display_label: B-Sound Treasure Hunt
tier: T1
play_rounds: 3
plain_description: Find three nearby objects whose names start with /b/.
creative_slots: {}
step_instructions: {}
screen_frames: []
runtime_support:
  executable: true
  requires_runtime_extension: false
  extension_reasons: []
  quality_warnings: []
```

Recommended runtime fields:

- `ib_theme`, `ib_key_concept`, `concepts_earned`;
- `keywords`, `feature_keywords`, `photo_features`;
- `collection_catalog` for Cat5;
- `asset_bindings` with asset IDs, display timing, widget target, and fallback;
- `branch_policy` for ideal, unexpected, and no-response behavior;
- `judgment_policy` for Cat5 validation or sound/form matching;
- `mechanic_mapping` showing source mechanic, consumer mechanic, and whether
  the mapping is exact, adapted, or unsupported.

The contract must keep entity binding explicit. An exported activity must state
which entity or source object triggers it, how the child sees that entity, and
which activity package owns the runtime.

## Step Instruction Conversion

The hardest and most important conversion is `step_instructions`.

Input sources:

- `tag_block.yaml` for activity ID, category, tier, source entity, focal
  attribute, mechanic, pillar, game style, and matchability metadata.
- `prod.md` for child-facing flow, branch policy, screen notes, and fallback
  behavior.
- `spec.md` for reviewer intent and design rationale when `prod.md` is too
  compressed.
- `integrated_assets/asset_bindings.yaml` and generated asset manifests when
  converting run-local activities.
- Curated override YAML for fields that cannot be safely inferred.

Extraction rules:

- Step 1 becomes `hook`.
- Step 2 becomes `transition` or `mission`.
- Step 3 rounds become `rounds`.
- Step 4 becomes `celebrate` or Cat5 `synthesis`.
- Step 5 becomes `closing`.
- Early-exit guidance should be synthesized when missing, but must stay
  generic and low-pressure.

For each step, preserve:

- what the AI must accomplish;
- what child action counts as progress;
- what to do for unexpected/off-rule responses;
- what to do for no response;
- screen state or honest no-screen fallback;
- tier-specific length/tone constraints.

For fullstack-demo v1, structured branch policy should be folded into compact
`goal`, `constraint`, `acceptable_themes`, and `escalation_note` fields because
that is what the current script overlay consumes. For `wonderlens-ai`, keep the
structured branch and judgment policy when the runtime model can carry it.

## Quality Gates

The converter must reject or warn on runtime-unsafe output.

Hard failures:

- missing `tag_block.yaml`;
- invalid tag block;
- missing required runtime fields after extraction and overrides;
- fullstack export that does not parse through `parse_game_file`;
- `wonderlens-ai` runtime YAML that fails `ActivityRuntime.model_validate`;
- Cat3 export marked executable without a Cat3 runtime;
- asset claim without an available asset binding or explicit no-display
  fallback;
- generated fullstack `creative_slots.game_mechanic` outside the current
  Pydantic literal set unless Phase 3 extends that schema.

Hard leakage failures:

- `Open from the source trigger`;
- `I found a small mission`;
- `Rule: I prompt`;
- `source-intent cue`;
- `current prompt`;
- `What is your first try`;
- `What did we make`;
- `Your turns made the board light up`;
- `RESOLVED BLOCKER`.

Warning conditions:

- fallback `step_instructions` are used because prose extraction was weak;
- `acceptable_themes` cannot be extracted for a round;
- Cat5 criterion requires runtime judgment that is not deterministic;
- source mechanic maps only approximately to a consumer mechanic;
- a visual asset is optional and no generated asset exists;
- activity requires a new widget but is exported in voice-only fallback mode.

## Mechanic Mapping

Mechanic mapping matters because it selects runtime prompts, state progression,
and widget behavior. Autodesign mechanics such as `decide`, `sort`, `build`,
`remember`, `deduce`, `compare`, `collect`, and `motion_voice` are not the same
as the current fullstack `Cat1CreativeSlots.game_mechanic` literals.

The converter must write an explicit mapping report:

```yaml
mechanic_mapping:
  source_mechanic: decide
  fullstack_game_mechanic: storytelling_chain
  mapping_status: adapted
  notes:
    - "Uses existing verbal story-chain primitive; no button/tournament UI."
```

If no honest mapping exists, the activity should export as
`requires_runtime_extension` rather than pretending to be playable.

## Phase 1: Canonical Runtime Converter

Phase 1 should incorporate and update the existing `wonderlens-ai` plan rather
than create a competing converter.

Current likely implementation home, based on the existing `wonderlens-ai`
plan and code layout:

```text
/Users/pharrelly/codebase/gitlab/wonderlens-ai/app/modules/activity/packages/runtime_generator.py
/Users/pharrelly/codebase/gitlab/wonderlens-ai/scripts/generate_activity_runtime.py
```

Phase 1 task areas:

- Implement deterministic package parsing and runtime YAML generation.
- Add a small override system with stable merge semantics.
- Add schema validation against `ActivityRuntime`.
- Add idempotent write/check behavior.
- Add source quality gates and leakage rejection.
- Add branch-policy extraction and compression.
- Add asset/fallback extraction.
- Add `requires_runtime_extension` classification.
- Generate reports that explain warnings, hard failures, and unsupported
  mechanics.
- Keep output stable and reviewable.

Representative fixtures:

- `time_machine_dinosaur`: Cat1 happy path aligned with fullstack demo.
- `fluffy_expedition_dandelion`: Cat5 collection happy path aligned with
  fullstack demo.
- `concept_phoneme_hunt_collect`: Cat5 judgment-heavy sound matching.
- `concept_branching_story_decide`: Cat1 adapted mechanic.
- `concept_coloring_game_probe`: unsupported/hard mechanic that should fail
  honestly or export only with an explicit fallback.

Phase 1 deterministic tests:

- Runtime YAML validates with `ActivityRuntime`.
- Generated package loads through `load_activity_package(...)`.
- Cat1/Cat5 packages adapt through `game_definition_from_package(...)`.
- Re-running the generator is byte-stable.
- `--check` fails when checked-in output diverges.
- Leakage strings fail conversion.
- Branch policy is preserved in structured runtime data or compacted warnings.
- Unsupported activities return `requires_runtime_extension` with reasons.

## Phase 2: Consumer Adapters

Phase 2 exposes the canonical runtime to both consumers.

### `wonderlens-ai` Adapter

The `wonderlens-ai` adapter writes or checks:

```text
activities/<activity_id>/runtime.yaml
```

It must preserve existing package files and satisfy:

- `ActivityRuntime.model_validate(...)`;
- `load_activity_package(...)`;
- `game_definition_from_package(...)` for executable Cat1/Cat5 packages;
- no WebSocket/API request-response schema changes unless separately planned.

### Fullstack-Demo Adapter

The fullstack adapter writes markdown with YAML frontmatter in the existing
shape:

```text
/Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend/games/<activity_id>.md
```

Phase 2 should avoid modifying fullstack-demo runtime code. The adapter should
emit:

- `activity_type`, `entity_name`, `category`, `display_label`, `tier`;
- `creative_slots` compatible with current Pydantic schemas;
- `step_instructions` compatible with `StepInstruction`;
- `screen_frames` compatible with `ScreenFrame`;
- `collection_catalog` for Cat5 where needed;
- optional `celebration_frame`;
- markdown body for reviewer context only.

The adapter should support writing to a temporary output directory for tests so
the fullstack demo repo can remain a baseline reference unless generated
activity files are intentionally reviewed and committed.

Phase 2 tests:

- Exported fullstack markdown parses through `parse_game_file`.
- Exported Cat1 and Cat5 activities load through `backend/game_loader.py` when
  copied into a test games directory.
- Fullstack export rejects unsupported `creative_slots.game_mechanic` values.
- Asset refs either map to supported screen frames or include no-display
  fallback language.
- Generated frontmatter contains no run-only review notes.

## Phase 3: Runtime And UI Extensions

Phase 3 is for activities that need more than current Cat1/Cat5 primitives.
Do not block Phase 1 or Phase 2 on these extensions.

Known hard activities:

- `concept_coloring_game_probe`: line art, color chips, region fill, or honest
  static/voice fallback.
- `concept_recognition_pop_probe`: choice grid, target/distractor state, and
  timing if kept as pop/recognition.
- `concept_word_build_guess_probe`: progressive letter/word reveal state.
- `concept_vegetable_sort_sort`: bucket/sorting interaction or voice-sort
  fallback.
- `concept_art_critic_tournament_probe`: approved art set, pairwise choice,
  bracket/progress state.
- `concept_emotion_color_outfit_probe`: avatar/outfit recolor or static
  emotion/color choice fallback.
- Cat3 set: guided drawing, one-line drawing, building challenge, award
  certificate, message bottle note.

Minimal UI direction:

- Prefer reusable `choice_grid`, `progress_tracker`, `word_reveal`,
  `sorting_buckets`, and `static_art_stage` primitives before building bespoke
  canvases.
- Keep screen widgets as prompt/memory surfaces when the child action can
  remain voice/text/photo based.
- Use self-report for physical activities and do not claim visual verification
  unless the runtime actually checks the photo.
- Mark Cat3 activities non-executable until the Cat3 runtime contract exists.

Phase 3 tests:

- Widget schema tests for any new screen primitive.
- State progression tests for choice, sort, reveal, and tournament flows.
- Visual fallback tests for missing assets.
- Playwright smoke only after UI code changes, with desktop/mobile checks.

## E2E Server Parity Validation

Live parity answers a different question from deterministic converter tests:
whether the ported `wonderlens-ai` runtime produces response quality comparable
to fullstack-demo for equivalent activity instructions.

Run parity only after deterministic Phase 1 and Phase 2 tests pass.

Recommended activities:

- `time_machine_dinosaur`;
- `fluffy_expedition_dandelion`;
- `concept_phoneme_hunt_collect`;
- one converted run-output activity after cleanup;
- one unsupported/hard activity to confirm honest failure or fallback.

Parity sequence:

- hook;
- transition/rules;
- round 1 normal child response;
- unexpected/off-rule child response;
- no-response/timeout branch if supported;
- celebration;
- closing.

Compare quality criteria, not exact wording:

- child-facing tone and age fit;
- follows activity-specific goal/constraint;
- respects tier length limits;
- preserves source role, sequence, and child action;
- does not hallucinate unsupported visuals/assets;
- handles Cat5 progress and collection counts honestly;
- preserves unexpected/no-response policy;
- returns equivalent screen/action directives where applicable.

This parity harness should live in a separate branch, probably in
`wonderlens-ai`, because that repo is the ported runtime under validation.
Fullstack-demo should remain the baseline reference unless fixture activity
files are intentionally added.

## Credential And Server Rules

Live server checks require local provider credentials. Do not print, copy, edit,
or commit secrets.

The deterministic converter and adapter tests must not require provider
credentials.

If live credentials or provider access are unavailable, record the parity check
as blocked and still complete deterministic validation.

## Validation Strategy

Validation is layered. Deterministic checks are mandatory before live provider
checks. Live provider parity is valuable but must not replace schema, parser,
golden fixture, and quality-gate tests.

Deterministic validation must prove:

- generated runtime data validates against the target model;
- generated artifacts are stable across runs;
- fullstack exports parse through the existing loader/parser;
- unsupported mechanics fail honestly;
- branch policy, judgment policy, and asset fallback behavior are not dropped.

Live parity validation must prove:

- `wonderlens-ai` response quality is comparable to the fullstack baseline for
  equivalent activity instructions;
- differences are judged by behavior and quality criteria, not exact wording;
- missing credentials or provider access are documented as a live-check blocker
  rather than hidden behind deterministic test success.

## Required Validation Commands

Autodesign documentation-only changes:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-autodesign
git diff --check
```

Phase 1 `wonderlens-ai` checks:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run pytest tests/unit/activity/test_runtime_generator.py -v
uv run ruff check app/modules/activity/packages/runtime_generator.py scripts/generate_activity_runtime.py tests/unit/activity/test_runtime_generator.py
uv run ty check app/modules/activity/packages
```

Phase 1/2 package validation examples:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities --activity time_machine_dinosaur --check
uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities --activity fluffy_expedition_dandelion --check
uv run python scripts/generate_activity_runtime.py --source /Users/pharrelly/codebase/github/wonderlens-activity-autodesign/activities --activity concept_phoneme_hunt_collect --check
```

Fullstack export checks:

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo
uv run python -m pytest tests -k "game_parser or game_loader" -v
uv run python - <<'PY'
from pathlib import Path
from backend.game_parser import parse_game_file
for path in sorted(Path("backend/games").glob("*.md")):
    if path.read_text(encoding="utf-8").startswith("---"):
        parse_game_file(path)
print("parsed fullstack game frontmatter")
PY
```

Live server commands should be verified against each repo's current README and
entrypoint before use. Current known commands are:

```bash
cd /Users/pharrelly/codebase/gitlab/wonderlens-ai
uv run uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload
```

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/backend
uv run uvicorn server:app --host 0.0.0.0 --port 8000 --reload
```

```bash
cd /Users/pharrelly/codebase/github/wonderlens-activity-fullstack-demo/frontend
npm run dev -- --port 5173
```

## Rollout

1. Land the converter and deterministic tests in `wonderlens-ai` or a shared
   package path agreed before implementation.
2. Generate runtime YAML for a small curated fixture set.
3. Add the fullstack markdown exporter and validate parser compatibility.
4. Run live server parity manually on 3-5 representative activities.
5. Only after parity, decide whether to commit generated fullstack demo
   activities or keep them as external export artifacts.
6. Plan Phase 3 UI/runtime extensions activity-by-activity.

## Open Risks

- Fullstack-demo and `wonderlens-ai` may diverge in prompt composition even with
  identical step instructions. E2E parity checks are needed to catch this.
- Some activity package prose is still too generic to extract high-quality
  runtime instructions without curated overrides.
- Fullstack-demo Cat1 mechanic literals are narrower than autodesign mechanics,
  so mechanic mapping must be explicit and test-covered.
- Cat5 runtime judgment quality depends on vision/LLM behavior and cannot be
  fully proven by schema tests.
- Cat3 remains a real runtime gap and should not be hidden behind conversion.
