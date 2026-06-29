# Bounded Transition Guidance Plan

**Goal:** Give verified activities package-owned transition intent while keeping
the final child-facing line LLM-generated, concise, and leak-safe.

**Scope:** Start with `concept_emotion_reader_care`. The package should define
what each bridge is allowed to do; WonderLens AI should decide when each bridge
applies, ask the Speaker to write the line, and fall back only when generated
dialogue violates the package boundary.

## Acceptance Criteria

1. Rules explain only the activity rule and do not invite play again.
2. Round prompts ask the child to read the feeling in the current picture.
3. Pre-answer dialogue never names hidden answers or cue labels.
4. Correct or similar feeling answers advance.
5. Help-only, wrong, off-topic, or unknown answers stay on the same picture.
6. Success bridges feel like a short transition, not a fixed robotic line.
7. Retry bridges remain direct and supportive without revealing the answer.
8. Package metadata stays additive and schema-compatible for existing consumers.

## Package Changes

- Add `speaker_dialogue_mode: bounded_package` under
  `response_verification`.
- Add structured transition briefs under
  `response_verification.dialogue_contract.transitions`.
- Keep accepted feeling terms and hidden target labels verifier-only.
- Preserve safe fallback lines for runtime guard failures.
- Do not add a new layout contract or change display assets in this branch.

## Validation

- Run focused demo package validation for `concept_emotion_reader_care`.
- Run tag-block schema validation if the active Python environment has
  `pyyaml` and `jsonschema`.
- Mirror the updated package into `wonderlens-ai`.
- Regenerate and check `runtime.yaml` there.
- Use live Activity WS logs to confirm the output reads as natural transitions
  rather than exact scripted dialogue.
