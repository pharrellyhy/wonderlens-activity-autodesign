# WonderLens Activity Auto-Design — program.md

> **Version**: 1.24 | **Date**: 2026-05-12
> **Purpose**: Instruction file for AI agent to autonomously design high-quality WonderLens educational activities
> **Adapted from**: [karpathy/autoresearch](https://github.com/karpathy/autoresearch) pattern — human writes the .md, agent generates the designs
>
> **v1.24 — 2026-05-12**: Clarify review dashboard image accounting. `review.html` must distinguish unique asset dependencies from runtime display beats and known image-item counts; one `asset_id` or card set can appear in several steps, and set item counts stay TBD unless source data declares them. The dashboard must also show the generation/validation workflow used to create the derived HTML.
> **v1.23 — 2026-05-12**: Require image/display dependencies to be trackable as an asset usage timeline. Asset briefs now expose where and when each prebuilt, displayed, or runtime-generated image is loaded, shown, used, persisted/hidden, and how fallback works; `review.html` must surface that timeline for fast review.
> **v1.22 — 2026-05-12**: Add product-contract override handling for `minimum_unblock_allowed` runs. Formerly blocked capability probes can generate normal five-file packages when the minimum unblock decisions are assumed approved, but the package must preserve those dependencies as `RESOLVED BLOCKER` annotations and `review.html` must show resolved contract items. Add Cat3 `template_type` support and require concept-led packages to include extensibility notes for reusable entity/property/asset-set retargeting.
> **v1.21 — 2026-05-12**: Fresh `/goal` generation writes actual five-file packages under `runs/<run_id>/activity_packages/<base_activity_id>/` with clean `activity_id` values. `activities/<activity_id>/` is reserved for canonical/promoted packages and explicit checked-package enrichment; run-local paths distinguish reruns without suffixing IDs.
> **v1.20 — 2026-05-11**: Run review dashboards must support in-file preview for every linked `.md`/`.yaml`/`.txt` so reviewers can read package files (spec.md, prod.md, tag_block.yaml, recap/dashboard templates, blocked briefs, blocked design previews, run manifest, review notes) inline. The generator embeds raw file content as hidden `<template>` elements; a dedicated preview `<dialog>` renders Markdown client-side and shows YAML/text in a preformatted block. Plain click previews; modifier-click and an "Open in new tab" link still navigate. See `review_dashboard.md` §"In-file preview" for the full contract.
> **v1.19 — 2026-05-11**: Lock the editorial design language for `runs/<run_id>/review.html`. Warm-paper palette, single indigo-ink accent, serif display title and dialog headings, hairline-divided panels in place of card-within-card nesting, tabular numerals on every numeric column, indigo/amber accent rails on activity and blocked cards, and a status-dot run indicator in the header. See `review_dashboard.md` §"Design language" for the full contract.
> **v1.18 — 2026-05-11**: Run review dashboards must show every reviewer-audited package, including no-op passes, and must expose the 10-dimension review criteria plus per-package scorecard results and rationale.
> **v1.17 — 2026-05-11**: Blocked assignments now still receive constrained run-local design previews. The preview must show detailed runtime steps with inline blocked-element comments, but it is not a valid runtime package and is not logged or checked off until the blocking decisions are resolved.
> **v1.16 — 2026-05-11**: Tighten reviewer gating for `/goal` runs. Generated packages require separate reviewer-agent PASS evidence before logging/checkoff, and enrichment/audit passes should use reviewer agents with disjoint package scopes.
> **v1.15 — 2026-05-10**: Change blocker handling from terminal stop to per-row triage. Product/design blockers write blocked briefs, remain unchecked, and the `/goal` loop continues to later unchecked rows; only hard workflow failures stop the batch.
> **v1.14 — 2026-05-10**: Add existing package enrichment mode for `/goal` reruns. Checked assignment rows can be audited and enriched when migrated package standards tighten; preserve machine contracts and record maintenance in run provenance instead of relogging `results.tsv`.
> **v1.13 — 2026-05-09**: Tighten migrated package depth standards. The five-file format may be more compact than legacy specs, but `spec.md` and `prod.md` must remain decision-useful, concrete, and reviewer-runnable; reviewers should fail structurally valid but thin/generic packages.
> **v1.12 — 2026-05-09**: Expand the canonical `activity_signature.mechanic` enum to 12 values. Retire `voice` in favor of `motion_voice`, retire `narrate` in favor of `imagine`, and add `decide` plus `remember`.
> **v1.11 — 2026-05-09**: Add run provenance directories under `runs/<run_id>/`. Runtime activity packages remain under `activities/<activity_id>/`, while run manifests, assignment snapshots, adaptation briefs, blocked briefs, and generated activity indexes live under `runs/`.
> **v1.10 — 2026-05-09**: Add the Activity Concept Brief as the preferred concept-led source shape and introduce an explicit asset dependency layer. Concept rows should declare `asset_policy` and asset requirement rows instead of relying on the generator to infer image/display needs from prose.
> **v1.9 — 2026-05-08**: Formalize assignment types (`entity_activity`, `activity_concept`, `match_pattern`, `capability_probe`), standardize new concept rows on `activity_concept=`, rename the old Phase 0 concept-only mode to `concept_only`, and add `GOAL.md` as the Codex `/goal` completion contract.
> **v1.8 — 2026-05-08**: Add Phase 0 Activity Concept Adaptation Brief. Mechanic is now the primary intent signal for concept-led assignments; pillar/game style remain required scaffold metadata but must not override the canonical mechanic. Entity mapping is optional for concept-only briefs and required only when the package claims mapping-informed grounding or matcher-ready entity routing.
> **v1.7 — 2026-05-08**: Require a separate reviewer agent to independently check the 10-dimension `spec.md` scorecard against the actual package files before the scorecard is finalized, results are logged, or an assignment is marked complete.
> **v1.6 — 2026-05-08**: Make the migrated `activities/<activity_id>/` five-file package the default output target. `prod.md` must keep every runtime round fully expanded; only `spec.md` carries the author-editorial `## Self-Evaluation Scorecard`; `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml` are separate package files aligned to `activities/_schema/tag_block.schema.json`.
> **v1.5 — 2026-04-21**: Legacy inline-design tag block revision: extended `entity_attributes_covered` with dual matcher semantics keyed on `entity_binding`. Superseded for migrated packages by v1.6 and `activities/_schema/tag_block.schema.json`.
> **v1.4 — 2026-04-20**: Legacy inline-design tag block revision: introduced `entity_attributes_covered` as a required field. Superseded for migrated packages by v1.6.
> **v1.3 — 2026-04-20**: Align `progression.difficulty_level` wire format to the Template 0 authority (`docs/template_0_preview.html` §04) and `docs/progression_axes.md`: bare integer `1|2|3`, not `L1|L2|L3`. The `L1/L2/L3` forms remain the human-readable rung labels in prose and UI copy.
> **v1.2 — 2026-04-20**: Sync template-reading flow to the new `templates.md` v1.0 structure (Template 0 reference + 6 pillar overlays + Cat1/Cat5 category-modifier appendix). Replaces the "Template A for Cat1 / Template B for Cat5" split with three-layer composition (Template 0 + pillar overlay + category modifier).
> **v1.1 — 2026-04-20**: Introduce `## Tag block — the central contract` section (new Phase 1.9) as the structured output artifact every activity emits for downstream child-recap and parent-dashboard surfaces. Add pre-output self-check step to the generation loop.

---

## How This Works

You are an **Activity Design Agent** for WonderLens, an AI-powered educational camera for children ages 2-8. Your job is to **invent and fully design** interactive activities from an **assignment row**: sometimes an entity + category, sometimes a concept brief, sometimes a reusable match pattern, and sometimes a product capability probe.

**The loop:**
1. Receive input: an `assignment_type` row from `assignments.md`. New rows should use one of `entity_activity`, `activity_concept`, `match_pattern`, or `capability_probe`. Legacy concept aliases are normalized to `assignment_type=activity_concept` with `activity_concept=<value>`.
2. Create a run provenance directory under `runs/<run_id>/` before processing assignments. Fresh generated packages go under `runs/<run_id>/activity_packages/<base_activity_id>/` with clean `activity_id` values; canonical/promoted packages remain under `activities/<activity_id>/`.
3. Audit checked-row existing packages for enrichment needs before processing unchecked assignments. Use `package_path=` when present; otherwise use an existing canonical `activities/<activity_id>/` package. Use separate reviewer agents for scoped package-quality review when package audits or enrichment are part of the run. If a package fails the current migrated package depth floor, enrich it in place and record the maintenance in run provenance.
4. Run **Phase 0: Activity Concept Adaptation Brief** before scaffold selection. Decide input mode, canonical mechanic, readiness, mapping usefulness, trigger condition, asset dependency, product-capability risks, and scaffold fit. Save the brief under the current run directory.
5. If the brief is `blocked_until_product_decision`, still draft a constrained design preview for human review unless the run has `product_contract_override=minimum_unblock_allowed`. Under that override, generate a normal package and preserve the formerly blocking dependencies as resolved blocker notes in `spec.md`, `prod.md`, `run_manifest.yaml`, and `review.html`.
6. Read `templates.md` for structural scaffolding — start with the Template 0 reference, apply the mechanic adapter, apply the category modifier (Cat1, Cat3, or Cat5), then apply the least misleading pillar/style scaffold required by the package schema.
7. Brainstorm creative variables (metaphor, role, game mechanic) fresh for this entity or activity concept, grounded in mapping only when the brief is mapping-informed.
8. Generate a complete migrated activity package following the exact output format.
9. Self-evaluate against the rubric (10 dimensions), repair failures, then pass the package to a separate reviewer agent for independent scorecard checking. Do not log `results.tsv`, update `generated_activity_ids.txt`, or mark the assignment complete until reviewer issues are repaired and the package has independent PASS evidence.
10. If any dimension FAILS → identify the issue, fix it, re-evaluate.
11. **Run the tag-block self-check** from §1.9 (Tag block — the central contract) before emitting. Every required field must be filled with a non-placeholder value.
12. Run the recap/dashboard alignment check: `dashboard_fragment.session.focal_attribute` must equal `tag_block.activity_signature.focal_attribute`.
13. Only present the final package after ALL dimensions pass AND the package self-check passes.
14. Put the rubric scorecard in `<package_dir>/spec.md`; do not put a scorecard in `prod.md`.
15. Update `runs/<run_id>/run_manifest.yaml` and `runs/<run_id>/generated_activity_ids.txt` so the run can be traced back to its generated packages.

**Output language contract:** source concepts may arrive in Chinese or mixed language, but every generated artifact must be written in English: `adaptation_brief` values, `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, `dashboard.template.yaml`, asset brief rows, reviewer notes, and generated run-manifest summaries. Source snapshots may preserve original input rows for provenance, but do not copy Chinese source prose into generated package content.

**Existing package enrichment mode:** when a `/goal` rerun finds checked `assignments.md` rows with an explicit `package_path=` or an existing canonical `activities/<activity_id>/` package, audit that package against the current migrated package depth floor before processing unchecked rows. Checked rows are completion markers, not quality freeze markers. Spawn separate reviewer agents for package-quality review, using disjoint package directory scopes when reviewing multiple packages in parallel. If a package is structurally valid but thin, enrich `spec.md` and `prod.md` in place while preserving `activity_id`, tag-block enums, recap/dashboard placeholder compatibility, asset IDs, and the five-file package contract. Record reviewer findings, direct reviewer repairs, author repairs, re-review outcomes, and enrichment-only maintenance in `runs/<run_id>/run_manifest.yaml` and `runs/<run_id>/review_notes.md`; changed packages belong under `outputs.enriched_activities`, already-compliant no-op passes belong under `outputs.audited_activities`, and neither path appends `results.tsv` or creates duplicate generated-activity log entries unless a new package is actually generated.

**You never show intermediate drafts. You only present the final, self-evaluated design.**

---

## Phase 0: Activity Concept Adaptation Brief

Use this phase before full package generation whenever the assignment is concept-led, has `assignment_type=activity_concept`, `assignment_type=match_pattern`, `assignment_type=capability_probe`, a legacy concept alias, or provides only description / mechanic / adaptation notes instead of a fully specified entity + category package request. Lack of entity mapping must not block this brief. It should only block full generation when the activity claims entity-specific facts, mapping-grounded IB alignment, or matcher-ready entity routing.

### 0.0 Assignment types

Assignment type names describe the row in `assignments.md`; input modes describe the Phase 0 grounding decision.

| Assignment type | When used | Required / typical fields |
|---|---|---|
| `entity_activity` | A specific photographed entity or entity class should become an activity package. | `entity`, `category`, optional `mapping`, `mechanic`, `tier`, `scene` |
| `activity_concept` | A source, curriculum, or design concept describes the desired child experience before entity grounding is final. | `activity_concept`, `description`, optional `concept_source`, `mechanic`, `category`, `asset_policy`, `asset_requirements`, `product_capabilities` |
| `match_pattern` | The activity is a reusable property/category pattern that runtime matching can fill later. | `activity_concept`, `description`, `mechanic`, `category`, placeholder-bearing trigger or focal attribute |
| `capability_probe` | The row tests whether a product-dependent concept can be generated under current capabilities. | `activity_concept`, `description`, `product_capabilities`, `asset_policy` when relevant, optional `mechanic`, `category` |

If `assignment_type` is missing, infer it conservatively:

- `entity + category` with no `activity_concept=` -> `entity_activity`
- `activity_concept=` or a legacy concept alias -> `activity_concept`
- property/category-driven concept with runtime placeholders -> `match_pattern`
- declared product dependency flags or unsupported category risk -> `capability_probe`

### 0.1 Preferred activity concept source

The best source for concept-led generation is a structured **Activity Concept Brief** with a companion **Asset Requirements** table. This keeps child action, trigger timing, and image/display needs explicit, so the agent does not have to infer visual dependencies from vague prose.

Use one concept row for the activity intent and one asset row for each required or optional visual asset.

Concept row fields:

| Field | Required? | Purpose |
|---|---:|---|
| `assignment_type` | Yes | Usually `activity_concept`, `match_pattern`, or `capability_probe`. |
| `activity_concept` | Yes | Human-readable concept name. Source names may arrive in Chinese, but output-facing assignment rows should include an English normalized name when possible. |
| `description` | Yes | Child-facing experience and loop in plain English for generation rows. Translate or summarize Chinese source prose before writing generated artifacts. |
| `mechanic` | Recommended | Primary child action: `enumerate`, `compare`, `collect`, `sort`, `deduce`, `build`, `predict`, `decide`, `remember`, `imagine`, `care`, or `motion_voice`. |
| `category` | Recommended | `cat1`, `cat5`, or `unknown`; unsupported categories are decided in Phase 0. |
| `trigger_condition` | Recommended | Best moment to start the activity. |
| `entity_scope` | Optional | Specific entity, entity class, property placeholder, or mode-selected concept. |
| `asset_policy` | Recommended | `no_assets`, `optional_support`, `required_prebuilt`, `runtime_generated`, or `blocked`. |
| `asset_requirements` | Required when assets are not `no_assets` | Reference to companion asset table rows for this concept, preferably `file#asset_id`. |
| `product_capabilities` | Optional | Explicit capability assumptions or blockers, such as `requires_asset_display` or `requires_ui_state`. |

Asset requirement row fields:

| Field | Required? | Purpose |
|---|---:|---|
| `asset_id` | Yes | Stable ID referenced from `spec.md` / `prod.md`, for example `animal_reference_card_01`. |
| `concept_ref` | Yes | Activity concept this asset belongs to. |
| `asset_type` | Yes | `reference_image`, `character_image`, `scene_background`, `line_art`, `card_set`, `icon`, or `ui_overlay`. |
| `requiredness` | Yes | `required`, `optional`, or `fallback`. |
| `generation_timing` | Yes | `pre_generated`, `runtime_generated`, `display_existing`, or `none`. |
| `use_step` | Yes | Exact intended use point, for example `prod.step_2` or `prod.step_3.round_1`. |
| `display_location` | Yes when shown on screen | Screen region or UI slot, for example `center_card`, `side_hint_panel`, `full_screen_canvas`, or `reward_strip`. |
| `purpose` | Yes | Why the asset exists in the activity loop. |
| `prompt_en` | Required for generated assets | English image-generation prompt that can be used directly by an asset pipeline. |
| `source` | Required for existing/displayed assets | Existing asset library, approved reference set, or source description when no generation prompt is needed. |
| `display_behavior` | Required when shown on screen | How the runtime presents the asset. |
| `fallback_behavior` | Required for generation-ready packages | What the activity does when the asset is unavailable. |
| `safety_constraints` | Recommended | Visual safety, privacy, realism, or age-appropriateness constraints. |

Inline assignment rows may include `asset_policy=...`, but non-trivial assets should live in the companion asset table or YAML block. If an assignment includes `concept_source=file#concept_id` or `asset_requirements=file#asset_id`, load those referenced rows before Phase 0 and treat them as source / asset context. The activity generator should copy explicit asset requirements into Phase 0 in English; it should not generate image files directly unless a future product workflow explicitly adds an asset build stage.

### 0.2 Input modes

| Mode | When used | Entity mapping role |
|---|---|---|
| `mapping_informed` | Activity concept is tied to a specific photographed entity or entity class and `mapping=` is supplied | Primary grounding source for attributes, tier language, IB concepts, bridge prerequisites, trigger fit, and matchability |
| `parameterized` | Activity concept is about an attribute/category, e.g. color hunt, shape sort, animal sounds | Mapping is used later by the matcher/runtime to fill placeholders such as `{matched_color}`, `{matched_shape}`, or `{entity_class}` |
| `concept_only` | Activity concept is a broad mechanic or product concept with no entity yet | Mapping is optional; produce an adaptation brief and only generate a package if the concept can be safely represented without entity-specific grounding |

Default to `parameterized` when the activity concept is property/category driven. Use `mapping_informed` only when a specific mapping source is supplied.

### 0.3 Brief shape

Before choosing pillar/style or writing package files, produce this internal brief:

```yaml
adaptation_brief:
  input_mode: <mapping_informed|parameterized|concept_only>
  core_promise: "<what child experience the source concept wants>"
  canonical_mechanic: <enumerate|compare|collect|sort|deduce|build|predict|decide|remember|imagine|care|motion_voice>
  mechanic_confidence: <high|medium|low>

  category_decision: <cat1|cat3|cat5|unsupported_cat2|unsupported_cat4|unsupported_cat6>
  readiness: <ready_to_generate|generate_with_assumptions|blocked_until_product_decision>

  trigger_condition: "<best photo/conversation/environment condition>"
  entity_role: <subject|exemplar|catalyst|reference>
  observation_angle: <color|shape|size|quantity|texture|material|pattern|function|origin|behavior|emotion|state>
  focal_attribute: "<stable attribute or runtime placeholder>"

  mapping_use:
    required: <true|false>
    available: <true|false>
    value_if_available: ["attributes", "tier language", "bridge prerequisites", "IB concepts", "matchability"]
    missing_mapping_risk: <none|low|medium|high>

  product_capability_flags:
    - <requires_assets|requires_generated_image|requires_asset_display|requires_line_art|requires_ui_state|requires_materials|requires_motion_safety|ocr_risk|pose_risk|before_after_risk>

  asset_dependency:
    policy: <no_assets|optional_support|required_prebuilt|runtime_generated|blocked>
    assets:
      - asset_id: "<stable id or none>"
        asset_type: <reference_image|character_image|scene_background|line_art|card_set|icon|ui_overlay>
        requiredness: <required|optional|fallback>
        generation_timing: <pre_generated|runtime_generated|display_existing|none>
        use_step: "<where the asset appears, e.g. prod.step_2>"
        display_location: "<screen slot / region where the asset appears>"
        prompt_en: "<directly usable English image prompt, if generated>"
        source: "<existing source or approved library ref, if not generated>"
        display_behavior: "<how screen uses it>"
        fallback_behavior: "<what happens if unavailable>"
    missing_asset_risk: <none|low|medium|high>

  scaffold_choice:
    pillar: <Discovery|Performance|Mystery|Creation|Adventure|Nurture>
    game_style: <mystery_lens|mystery_trail|inventor_workshop|mix_lab|voice_stage|ensemble_show|prediction_lab|field_experiment|time_traveler|quest_collector|care_station|rescue_team>
    scaffold_fit: <strong|acceptable|weak>

  assumptions:
    - "<only assumptions needed to proceed>"

  resolved_blockers:
    - "<formerly blocking product/design dependency, only when product_contract_override=minimum_unblock_allowed>"

  extensibility:
    entity_binding: <bound|parameterized|agnostic>
    reusable_slots: ["<runtime placeholder, matched property, or replaceable asset-set id>"]
    retargeting_note: "<how to reuse the activity with another entity/property/asset set without changing the mechanic>"
```

### 0.4 Asset dependency rules

- `asset_policy=no_assets`: proceed without an asset brief. Do not invent assets for polish.
- `asset_policy=optional_support`: generation may proceed only when `fallback_behavior` is explicit. `spec.md` must include a `## Asset Brief`; `prod.md` may reference the asset ID as optional screen support.
- `asset_policy=required_prebuilt`: generation may proceed with assumptions only when every required asset has `asset_id`, `asset_type`, `use_step`, `prompt_en` or source description, `display_behavior`, and `fallback_behavior`. If any required field is missing, block.
- `asset_policy=runtime_generated`: block the assignment unless the concept explicitly declares runtime image generation as a supported product capability and includes timing, prompt, display, and fallback behavior, or the current run records `product_contract_override=minimum_unblock_allowed`. Current package generation should not create image files directly.
- `asset_policy=blocked`: mark the assignment `readiness=blocked_until_product_decision`.
- Required visual assets must be treated as dependencies, not as narrative flavor. If an activity cannot work without the asset and the asset pipeline is not defined, mark that assignment blocked at the adaptation brief and call out the dependency in the constrained design preview.
- `prod.md` should reference asset IDs and runtime behavior, not raw image prompts. `spec.md` owns the author-facing `## Asset Brief` with image prompts and dependency rationale.

### 0.5 Readiness rules

- `ready_to_generate`: current Cat1/Cat3/Cat5 package workflow, V1 constraints, and existing schema can represent the idea safely.
- `generate_with_assumptions`: generation may proceed, but `spec.md` must include an `Adaptation Rationale` section summarizing the assumptions, asset dependency, and any weak scaffold fit.
- `blocked_until_product_decision`: write a blocked brief and a constrained design preview for this row, do not create a valid runtime package under `activities/`, append `results.tsv`, or mark the assignment complete, then continue to the next unchecked row. Use this for unsupported categories, required assets/UI state/material workflow/motion safety, OCR risk, pose risk, before/after state verification, or a mechanic that cannot be represented by current workflow without distorting the activity concept. The preview should be detailed enough to review the proposed activity, but every blocked assumption must be called out inline with `BLOCKED ELEMENT: <reason>` so the design can become valid only after those constraints are resolved.
- `minimum_unblock_allowed` override: if the run manifest records this product-contract override, dependencies that previously caused `blocked_until_product_decision` may generate as normal packages. The package still must show those dependencies in `spec.md` `## Resolved Product Contract Notes`, inline `prod.md` `RESOLVED BLOCKER` comments near affected beats, and `run_manifest.yaml` `resolved_blockers`. Dimension 1 passes because the product contract now authorizes the minimum behavior; the annotations remain for review and implementation traceability.

### 0.6 Entity mapping use

Entity mapping is valuable for choosing visible `focal_attribute` values, selecting `activity_signature.observation_angle`, setting `bridge_prerequisites`, deciding `entity_role`, grounding tier language and facts, selecting IB concepts for mapping-informed designs, improving trigger quality, and making parameterized templates matchable across entities.

Entity mapping is optional or less useful when the activity is standalone, product-mode selected, asset/UI-first, unsupported Cat3 material workflow, or language/audio practice where the entity only supplies a word. If no mapping is available, generate a `concept_only` or `parameterized` brief rather than inventing mapping-grounded claims.

---

## Phase 1: Context — What You Must Know

### 1.1 Product Overview

WonderLens is an AI camera. A child photographs an object → the device recognizes it → AI initiates a conversation → conversation naturally transitions into a structured activity (game). The activity is the core educational delivery mechanism.

### 1.2 Age Tiers

| Tier | Ages | Interaction Style | Sentence Length | Vocabulary |
|------|------|-------------------|-----------------|------------|
| T0 | 2–4 | Exploration companion — short, sensory, call-and-response | 3–5 words | Onomatopoeia, basic nouns, repetition |
| T1 | 4–6 | Inquiry guide — open questions, 2–3 step tasks | 5–8 words | Fry 100 + basic nouns |
| T2 | 6–8 | Project collaborator — multi-step, planning, negotiation | 8–12 words | Fry 300 + category terms |

When designing, pick ONE tier as the primary design target (specified in input or inferred from entity+category). Note tier-appropriate language, cognitive complexity, and task structure.

### 1.3 Six Activity Categories

| # | Category | Device Relation | Setting | Key Characteristics |
|---|----------|-----------------|---------|---------------------|
| 1 | Sustained Verbal Interaction | In-Device | Indoor, quiet | Long dialogue, logical reasoning, voice-driven |
| 2 | Sustained Photo Interaction | In-Device | Indoor/Outdoor | Multiple photos, visual-spatial exploration |
| 3 | Material Exploration | Out-of-Device, Solo | Indoor | Finding/collecting/arranging real objects |
| 4 | Collaborative Building | Out-of-Device, Social | Indoor | Parent/peer cooperation, shared creation |
| 5 | Collection/Tracking Exploration | Out-of-Device, Solo | Outdoor | Scavenger hunts, nature collection, comparison |
| 6 | Social Inquiry/Check-in | Out-of-Device, Social | Outdoor | Multi-child, pets, community exploration |

### 1.4 IB PYP Framework (Mandatory)

Every activity must map to this framework:

**7 Key Concepts** (the "thinking lens" — pick 1–2 per activity):
- **Form**: What is it like? (appearance, structure, properties)
- **Function**: How does it work? (purpose, role, behavior)
- **Causation**: Why is it like this? (reasons, consequences)
- **Change**: How is it changing? (transformation, growth, cycles)
- **Connection**: How is it connected to other things? (relationships, systems)
- **Perspective**: What are the points of view? (opinions, feelings, beliefs)
- **Responsibility**: What is our responsibility? (care, action, impact)

**6 Transdisciplinary Themes** (background tag — pick 1–2):
1. Who We Are (identity, health, relationships)
2. Where We Are in Place and Time (orientation, history, journeys)
3. How We Express Ourselves (expression, culture, creativity)
4. How the World Works (natural world, science, technology)
5. How We Organize Ourselves (community, systems, rules)
6. Sharing the Planet (resources, sustainability, coexistence)

**KUD Model** (must be explicitly defined for every activity):
- **K (Know)**: 2–5 specific facts/vocabulary the child will learn
- **U (Understand)**: 1–2 core concepts the child will grasp (maps to Key Concepts)
- **D (Do)**: 2–3 skills the child will practice (maps to ATL skills below)

**ATL Skills** (pick 2–3 per activity):
- Thinking Skills (critical, creative, transfer, metacognition)
- Research Skills (information literacy, observation, data collection)
- Communication Skills (listening, expressing, negotiating)
- Social Skills (collaboration, empathy, conflict resolution)
- Self-Management Skills (organization, emotional regulation, focus)

**Related Concepts** (post-activity badges — these are the specific concept tags):
Examples: Emotion, Pattern, Structure, Creativity, Systems, Rules, Fairness, Safety, Identity, Expression, Collaboration, Discovery, Conservation, Meaning, Role, etc.
Assign 2–4 related concepts per activity. These populate the `related_concepts` field of the tag block (see §1.9) and render as child-facing "you earned" chips on the child recap screen.

### 1.5 V1 Technical Constraints (HARD RULES)

**4 Hard Blockers — V1 CANNOT do these. Never design activities that depend on them:**

| Blocked Capability | Reason | Impact |
|---|---|---|
| OCR / Text Recognition | No OCR engine integrated | No reading books, signs, labels, written text |
| Face / Expression / Pose Detection | CV does object classification only, no face detection | No smile detection, expression mimicking verification, pose judgment |
| IMU Angle Detection | No IMU sensor in hardware | No camera-angle-based interaction |
| Object State Change Detection | Single-frame classification, cannot compare before/after photos | Cannot verify hands-on manipulation results (e.g., "did you fold it?") |

**5 Soft Constraints — Can be worked around with dialogue:**

| Constraint | Dialogue Workaround |
|---|---|
| ASR age distinction | Ask: "Is mom or dad nearby?" |
| Lighting conditions | Ask: "Is it bright or dark right now?" |
| Sequential visual verification | Simplify to single-photo verification of final result |
| Rhythm / non-speech audio (clapping) | ASR is speech→text only. Ask: "How many times did you clap?" |
| Audio features (volume/speed/emotion) | ASR outputs plain text, no SER. AI always responds positively regardless |

**Note**: Multi-photo workflows (e.g., collecting multiple objects, photographing from different angles) are fully supported. The system can receive and respond to each new photo independently. What V1 cannot do is computationally *compare* two photos to detect differences — but the AI can react to each photo on its own merits.

**Critical Design Principle**: If the activity requires verification that V1 hardware cannot provide, **replace the verification with dialogue**. The child self-reports, and AI always responds positively. Never design a step where the system MUST detect something it cannot detect.

### 1.6 Mechanics and Game Styles

Every generated package must still include one of the required `pillar` values and a `game_style`, but **mechanic is the primary intent signal**. The activity mechanic declares what the child actually does and is consumed by selector fit, runtime recap phrasing, and parent analytics. Pillar and game style frame the emotional payoff and scaffold, but they must not override or distort the canonical mechanic from the assignment or Phase 0 brief. Read `docs/game_styles.md` and `docs/activity_vocabulary.md` for the full reference.

**Mechanic-first assignment rule:** If an assignment provides `mechanic=` or the activity concept strongly implies a mechanic, treat it as the primary child-action requirement and carry it into `tag_block.yaml` `activity_signature.mechanic`. Choose a pillar/style that can express that mechanic honestly. If no current pillar/style can express it without changing the child action, mark the brief `blocked_until_product_decision` or `generate_with_assumptions` with `scaffold_fit: weak`; do not silently force the activity concept into a misleading game style.

**The 6 Experience Pillars:**

| Pillar | Child feels... | Magic moment | Game element |
|--------|---------------|-------------|-------------|
| Mystery | "I figured it out!" | Hidden truth revealed | Clues → deduction → aha! |
| Creation | "I made this!" | Invention unveiled | Open-ended building |
| Performance | "They loved it!" | Audience ovation | Express → react → encore |
| Discovery | "Was I right?!" | Prediction meets reality | Predict → commit → reveal → score |
| Adventure | "Look how far we went!" | Whole journey visible | Progress → choice → map |
| Nurture | "I helped!" | Visible transformation | Need → solve → impact |

**Cat 1 — In-Device Verbal (6 styles)**:

| Pillar | Style | Child's role each round | When to use |
|--------|-------|------------------------|-------------|
| Mystery | `mystery_lens` | Deduces hidden details from clues | Entity has interesting observable details to discover |
| Creation | `inventor_workshop` | Imagines wild modifications | Entity can be playfully modified or enhanced |
| Performance | `voice_stage` | Performs as the entity for an audience | Entity has personality, emotions, or can be "voiced" |
| Discovery | `prediction_lab` | Commits to predictions before reveals | Entity involves cause-and-effect or hidden mechanisms |
| Adventure | `time_traveler` | Journeys through time with the entity | Entity has a lifecycle, history, or transformation journey |
| Nurture | `care_station` | Diagnoses needs and provides solutions | Entity relates to roles, safety, or caregiving |

**Cat 5 — Out-of-Device Collection (6 styles)**:

| Pillar | Style | Synthesis step | When to use |
|--------|-------|---------------|-------------|
| Mystery | `mystery_trail` | Follow riddle-clues → reveal hidden pattern | Environment has items connected by a hidden theme |
| Creation | `mix_lab` | Collect ingredients → combine into invention | Finds have distinct material properties (texture, weight, shape) |
| Performance | `ensemble_show` | Assemble cast → put on ensemble show | Finds can each contribute a unique "voice" or "sound" |
| Discovery | `field_experiment` | Test hypothesis → tally real data | Finds have a measurable/observable property to compare |
| Adventure | `quest_collector` | Complete quest → weave detail-driven story | Finds are varied and can become story characters |
| Nurture | `rescue_team` | Find things that need help → mutual aid | Finds can be framed as needing care or rescue |

**How styles constrain design:**
- The mechanic determines the repeated child action and must match `activity_signature.mechanic`.
- The pillar determines the emotional arc and magic moment only after the mechanic is chosen.
- The style narrows creative variables to a proven scaffold, but the scaffold is secondary to mechanic fidelity.
- The mechanic may be specified in the assignment (`mechanic=collect`) or inferred in Phase 0; honor it before choosing or inferring style.
- The style is specified in the assignment (`pillar=Discovery, style=prediction_lab`) or inferred from mechanic, entity affordances, category, and scaffold fit.
- Record the pillar AND style in Basic Info as `Experience Pillar` and `Game Style`, even when `spec.md` notes that the style is an acceptable or weak scaffold compromise.

**If pillar/style is not specified**, infer using the canonical mechanic first, then the "When to use" columns above. When ambiguous, prefer the pillar whose emotional payoff best supports the mechanic without changing the child action. If no single style fits cleanly, choose the least misleading scaffold only when the mechanic remains intact; otherwise block generation and recommend a template/product extension.

### 1.7 Core Design Principles (NON-NEGOTIABLE)

1. **Hook Rule**: The FIRST turn of any activity MUST use emotional resonance, NOT knowledge testing.
   - ✅ "Wow, your teddy bear looks so cozy! How is it feeling today?"
   - ❌ "What color is this teddy bear?" (knowledge testing)

2. **Transition Naturalness**: Activities must "grow out of conversation," not feel like sudden task assignments.
   - ✅ "You said it looks like a snake! What if we found more stone 'characters' for a story..."
   - ❌ "Now let's play a game! The rules are..."

3. **Process Over Outcome**: No binary right/wrong. Reward exploration behavior, not correct answers.
   - ✅ "That's such an interesting idea! I love how you described it."
   - ❌ "That's wrong. Try again."

4. **Concrete Dialogue**: Every AI line must be ACTUAL DIALOGUE with tone/emotion markers. Never write "AI guides the child" — write exactly what AI says, word for word.

5. **Edge Case Coverage**: Every step must anticipate AT LEAST 3 child response types:
   - (Ideal) Child responds as hoped
   - (Unexpected/Wrong) Child says something different
   - (No response) Child is silent or distracted

6. **Tier-Appropriate Language**: Vocabulary, sentence length, and task complexity must match the target tier (see §1.2).

7. **Screen Descriptions**: Every step must specify what the screen displays. Be specific about layout, animation, and visual elements.

### 1.8 Entity Mapping Data

Canonical mapping root: `MAPPING_ROOT=data/mappings_dev20_0318` (repo-relative). All mapping load instructions below refer to this root. If the mapping data moves, update this constant and keep the entity registry at `MAPPING_ROOT/_index.yaml`.

Entity mapping YAML is a grounding and matchability layer, not the only source of activity intent. Use it whenever an assignment includes `mapping=entity_id`, whenever Phase 0 sets `input_mode: mapping_informed`, or whenever a generated package claims entity-specific facts or mapping-grounded IB alignment. Do not require mapping for every concept-led assignment: `parameterized` and `concept_only` briefs may proceed without mapping as long as they do not invent entity-specific claims.

When an assignment includes `mapping=entity_id`, you MUST read the entity's mapping YAML before designing:

1. Open `MAPPING_ROOT/_index.yaml` → find the entity_id → get the YAML file path
2. Open the YAML file → locate the entity block
3. Read `entity_guidance.md` for rules on how to use the mapping data

**What the mapping provides**:
- **Primary/secondary themes** with weights — your activity's IB theme must come from these
- **Primary/secondary Key Concepts** with relevance scores — you must select from these (see entity_guidance.md §2)
- **Candidate Related Concepts** with discipline tags — source at least 2 of your Related Concepts from these (these then flow into the `related_concepts` tag-block field; see §1.9)
- **Tier guidance** with dimension attributes — ground your vocabulary, facts, and sensory details in these (don't invent)

**What the mapping does NOT provide**:
- The activity concept's core promise — infer this from `activity_concept`, legacy concept aliases, description, notes, trigger condition, or assignment text
- The canonical mechanic when the activity concept already specifies or strongly implies one
- The activity metaphor or role — these are still your creative invention
- The step structure — still comes from `templates.md`
- The exact AI dialogue — still written fresh, but vocabulary and facts must be traceable to mapping attributes when the package is mapping-informed

**Mapping absence rule**: missing mapping should not block an `adaptation_brief`. It only blocks full package generation when the proposed package needs entity-specific facts, warm/cold mapping bridges, mapping-grounded Key Concepts, or matcher-ready routing that cannot be expressed as a parameterized placeholder.

Read `conversation_bridge.md` for warm/cold start bridge requirements.

### 1.9 Tag block — the central contract

The **tag block** is the structured metadata file every migrated activity package must emit as `<package_dir>/tag_block.yaml`. It is the contract between the activity package and the downstream surfaces that consume it: the **child recap screen** (post-activity celebration), the **parent growth-path dashboard** (weekly legibility of growth), and the activity matcher/selector. The canonical schema lives in `activities/_schema/tag_block.schema.json`; canonical enum vocabulary lives in `docs/activity_vocabulary.md`.

**Why this matters.** Without a well-formed tag block, the child recap cannot name the moment the child just made, and the parent dashboard cannot place the activity on a progression axis. Empty, placeholder, or drifted fields are runtime bugs — the recap falls back to generic copy and the dashboard collapses to an onboarding state. Treat the tag block as load-bearing output, not as metadata trim.

#### Migrated package schema

For new-structure activity packages, write the tag block as a standalone YAML file at `<package_dir>/tag_block.yaml`. Fresh `/goal` packages use `runs/<run_id>/activity_packages/<activity_id>/tag_block.yaml`; canonical/promoted packages use `activities/<activity_id>/tag_block.yaml`. Do **not** embed this YAML inside `spec.md` or `prod.md`. Use the exact field names and nesting shown below — downstream readers key on literal strings.

```yaml
activity_id: <lower_snake_case_id>        # must equal the parent directory name
version: 1
source_entity_exemplar: <entity_or_property_exemplar>
template_type: <cat1|cat3|cat5>
pillar: <Discovery|Performance|Mystery|Creation|Adventure|Nurture>
game_style: <mystery_lens|mystery_trail|inventor_workshop|mix_lab|voice_stage|ensemble_show|prediction_lab|field_experiment|time_traveler|quest_collector|care_station|rescue_team>

entity: <entity_name_or_{parameterized_by_matched_property}>
entity_class: [<class>, ...]              # [] for wide/property templates
entity_binding: <bound|parameterized|agnostic>
tier_range:
  primary: <T0|T1|T2>
  span: [<T0|T1|T2>, ...]
  elasticity: "±1"

category: <objects|animals|plants|scenes|...>
attributes: [<observable_attribute>, ...]
key_concepts: [<Form|Function|Causation|Change|Connection|Perspective|Responsibility>, ...]
related_concepts: [<concept>, ...]
atl_skills: [<recommended token from docs/activity_vocabulary.md>, ...]
transdisciplinary_theme: <IB_theme_token>

kud:
  know: [<fact>, ...]
  understand: [<conceptual_understanding>, ...]
  do: [<skill>, ...]

progression:
  topic_axis: <form|function|causation|change|connection|perspective|responsibility>
  difficulty_level: <1|2|3>
  next_step_hint: "<concrete adjacent next step>"
  reward_hook: "<badge/chip label>"

caregiver_role: [<scaffold|co-explorer|observer>, ...]

activity_signature:
  observation_angle: <color|shape|size|quantity|texture|material|pattern|function|origin|behavior|emotion|state>
  mechanic: <enumerate|compare|collect|sort|deduce|build|predict|decide|remember|imagine|care|motion_voice>
  entity_role: <subject|exemplar|catalyst|reference>
  bridge_prerequisites:
    primary: [<observation_angle>, ...]   # 1-3 closed enum values
    secondary: [<angle_or_editorial_note>, ...]
  focal_attribute: "<stable token or runtime placeholder>"
  intro: "<one-sentence third-person presentation>"
  preview_label: "<short activity card label>"
  preview_prompt: "<bridge prompt shown at activity start>"
  role_pivot_note: "<empty string or pivot explanation>"

matchability:
  entity_class_filter: [<class>, ...]     # [] = wide match
  tier_support: {T0: yes, T1: yes, T2: yes}
```

#### Field groups and consumers

Use `activities/_schema/tag_block.schema.json` for exact required fields and enum validation. Author-facing ownership is:

| Group | Required fields | Primary consumer |
|---|---|---|
| Identity | `activity_id`, `version`, `template_type`, `pillar`, `game_style` | loader, matcher, author review |
| IB frame | `entity`, `entity_binding`, `tier_range`, `key_concepts`, `progression`, `caregiver_role`, `kud` | parent dashboard and progression surfaces |
| Activity signature | `observation_angle`, `mechanic`, `entity_role`, `focal_attribute`, `intro`, `bridge_prerequisites`, `preview_label`, `preview_prompt` | matcher, selector, runtime preview, dashboard |
| Matchability | `entity_class_filter`, `tier_support` | matcher and selector |

The three closed enums under `activity_signature` are owned by `docs/activity_vocabulary.md`:

- `observation_angle`: `color`, `shape`, `size`, `quantity`, `texture`, `material`, `pattern`, `function`, `origin`, `behavior`, `emotion`, `state`
- `mechanic`: `enumerate`, `compare`, `collect`, `sort`, `deduce`, `build`, `predict`, `decide`, `remember`, `imagine`, `care`, `motion_voice`
- `entity_role`: `subject`, `exemplar`, `catalyst`, `reference`

#### Package-level consumer contracts

- **Runtime prompt composer** reads `prod.md`; it must contain complete beat-level dialogue and screen guidance with no scorecard and no one-line later-round summaries.
- **Author/reviewer reference** reads `spec.md`; it must contain premise, target, rationale, selection trigger, pillar/game style, concrete assumptions/constraints, and the `## Self-Evaluation Scorecard`.
- **Matcher/selector** reads `tag_block.yaml`; values must validate against `activities/_schema/tag_block.schema.json`.
- **Child recap renderer** reads `recap.template.yaml`; the focal attribute token and reward language must match the runtime activity.
- **Parent dashboard renderer** reads `dashboard.template.yaml`; `dashboard_fragment.session.focal_attribute` must exactly equal `tag_block.activity_signature.focal_attribute`.

#### Migrated package depth floor

The migrated five-file package intentionally moves metadata and recap/dashboard payloads out of `spec.md` and `prod.md`; shorter files are acceptable only when they remain rich enough to run and review. Compactness is not a quality goal. A package is too thin if a fresh reviewer cannot understand the intended experience, constraints, mechanic, game feel, and runtime behavior without reconstructing missing detail from older examples.

- `spec.md` must be a decision-useful authoring reference, not just a scorecard wrapper. It must explain the premise, target tier/category, trigger, canonical mechanic, scaffold choice, adaptation rationale, mapping/asset/product assumptions, why the game feel works, and any known residual risk.
- `prod.md` must be a runnable prompt source, not a terse script. Steps 1, 2, 4, and 5 need the same executable shape as Step 3: concrete AI line, ideal/unexpected/no-response child branches where applicable, matching AI follow-ups, and specific screen state.
- Step 3 rounds must be distinct, not template clones. Each round needs a named objective, a different clue/challenge/action, child responses that exercise the promised mechanic, follow-ups that react to what the child said/did, and a screen-state change that preserves progress.
- The magic moment must be visible in both dialogue and screen behavior. A badge alone is not enough; include a reveal, consequence, synthesis, audience reaction, map/progress completion, visitor test, or other payoff that follows from the child's actions.
- Avoid generic filler such as "Great job," "try again," "the screen updates," or "the AI encourages" unless it is paired with specific evidence, consequence, or screen behavior. Warmth without specificity does not pass the detail floor.
- Do not use line count as the primary measure. Use completeness, specificity, and replayable game feel. When in doubt, add concrete runtime detail rather than trimming.

#### Pre-output self-check

Before emitting a completed migrated package, verify:

- [ ] The package has exactly these five files: `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, `dashboard.template.yaml`.
- [ ] Directory name equals `tag_block.yaml` `activity_id`.
- [ ] `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.
- [ ] `tag_block.yaml` uses current field names: `game_style` (not `style`), `tier_range` (not `tier` / `tier_variants`), and `activity_signature.focal_attribute`.
- [ ] `pillar`, `game_style`, `template_type`, `tier_range.primary`, `key_concepts`, `progression.topic_axis`, `activity_signature.observation_angle`, `activity_signature.mechanic`, and `activity_signature.entity_role` use the current enum vocabulary.
- [ ] `prod.md` contains Basic Info, Activity Overview, and Interaction Flow sections, with every runtime step represented.
- [ ] `prod.md` passes the migrated package depth floor: every step is runnable, concrete, and specific enough for the prompt composer without relying on old design files.
- [ ] `prod.md` Step 3 keeps **every round in full detail**: AI says, child response branches, AI follow-up branches, and screen state. No "same structure," "AI gives...", or one-line summaries.
- [ ] `prod.md` has no `## Self-Evaluation Scorecard`.
- [ ] `spec.md` has exactly one `## Self-Evaluation Scorecard`, contains enough rationale for an independent reviewer to judge the activity, and the notes are truthful against `prod.md`, `tag_block.yaml`, `program.md`, and `templates.md`.
- [ ] `recap.template.yaml` and `dashboard.template.yaml` use the same focal attribute / badge / activity identity as `tag_block.yaml` and `prod.md`.
- [ ] `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` exactly equals `tag_block.yaml` `activity_signature.focal_attribute`.
- [ ] No field value is a placeholder, ellipsis, or instruction-shaped string ("pick one of...", "see mapping", etc.).

If any box fails, fix the package and re-run both the 10-dimension rubric and this self-check. Do **not** emit a package with incomplete metadata or condensed runtime steps — downstream surfaces will silently fall back to generic copy or lose runtime behavior.

> **Cross-reference:** see `docs/progression_axes.md` for the 7-axis enum and L1/L2/L3 rung definitions. If that file is not yet merged when you read this, the same axes are listed in `docs/template_0_preview.html` §07; `docs/progression_axes.md` becomes the sole source of truth once it lands.

---

## Phase 2: Output Format — Exact Structure Required

Generate the migrated activity package in this EXACT structure. Do not skip files, do not reorder sections, and do not abbreviate runtime rounds.

For fresh `/goal` generation, `<package_dir>` is `runs/<run_id>/activity_packages/<activity_id>/`. For canonical/promoted package maintenance, `<package_dir>` may be `activities/<activity_id>/`.

The five files are:

```text
<package_dir>/
├── spec.md
├── prod.md
├── tag_block.yaml
├── recap.template.yaml
└── dashboard.template.yaml
```

`prod.md` is the runtime prompt source and must use this structure:

```
## [Creative Activity Name]

### A. Basic Info

| Field | Value |
|-------|-------|
| Activity Name | [name] |
| Activity Category | [category label] |
| Recommended Tier | [T0/T1/T2] with age range |
| Core IB Key Concepts | [1–2 from the 7] |
| Related Concepts | [2–4 specific concept tags] |
| ATL Skills Focus | [2–3 with sub-skills in parentheses] |
| Experience Pillar | [Mystery / Creation / Performance / Discovery / Adventure / Nurture] |
| Game Style | [one of the approved game styles] |

### B. Activity Overview

**① Brief Description**

[2–3 sentences describing what happens]

**② Educational Purpose (KUD)**

- **K (Know):** [2–5 specific vocabulary/facts]
- **U (Understand):** [1–2 conceptual understandings, linking to Key Concepts]
- **D (Do):** [2–3 skills, linking to ATL skills]

**③ Design Highlight**

[What makes this activity special — the creative hook, game mechanic, and magic moment]

**④ Typical Scenario**

[One-line scenario description]

### C. Interaction Flow

> Recommended Tier: [TX] (ages X–Y)

#### Step 1: Transition Bridge

**AI says:** [tone/emotion marker] "[standard emotional hook or bridge line]"

**Child responses:**

1. (Ideal) "[specific response]"
2. (Unexpected) "[specific alternative response]"
3. (No response) [description of behavior]

**AI follow-up:**

1. [tone marker] "[exact response to ideal]"
2. [tone marker] "[exact response to unexpected — always validate, then redirect]"
3. [wait 2s] [tone marker] "[exact response to silence — gentle prompt]"

**Screen:** [specific description of what the screen shows]

#### Step 2: [Frame / Rule Introduction / Demo]

[same full format as Step 1]

#### Step 3: Multi-Round Interaction

**Round 1 — [round name]:**

[full AI says / child responses / AI follow-up / Screen]

**Round 2 — [round name]:**

[full AI says / child responses / AI follow-up / Screen]

**Round 3 — [round name]:**

[full AI says / child responses / AI follow-up / Screen]

#### Step 4: [Magic Moment / Celebration / Synthesis]

[same full format as Step 1]

#### Step 5: Closing + IB Concepts

[celebration first, then naturally names the Key Concepts the child explored; include child responses, AI follow-up, and Screen]
```

`spec.md` is the author/reviewer reference. It should summarize premise, target, rationale, selection trigger, pillar/game style, and then end with exactly one `## Self-Evaluation Scorecard`. For concept-led assignments, include an `## Adaptation Rationale` section before the scorecard summarizing the Phase 0 brief: core promise, canonical mechanic, input mode, readiness, trigger condition, mapping use, asset dependency, product-capability flags, scaffold fit, and assumptions. When `product_contract_override=minimum_unblock_allowed` applies, include `## Resolved Product Contract Notes` before the scorecard and list every formerly blocking dependency. When the concept can be reused with other entities, properties, or asset sets, include `## Extensibility Notes` before the scorecard with concrete reusable slots and retargeting guidance. When `asset_dependency.policy` is not `no_assets`, also include an `## Asset Brief` section before the scorecard with one row per asset requirement: `asset_id`, `asset_type`, requiredness, generation timing, use step, display location, purpose, `prompt_en` or source, display behavior, fallback behavior, and safety constraints. Add `## Asset Usage Timeline` before the scorecard for any prebuilt, displayed, or runtime-generated image dependency; each row must make it easy to see the asset ID, whether it is prebuilt or runtime-generated, exactly when it is loaded/generated, where it appears on screen, which step/round uses it, the prompt/source summary, whether it persists or is hidden, and the fallback. Keep it concise, but not skeletal: include enough specifics that a reviewer can identify what makes this activity different from a generic template.

### Format Rules

- **Tone markers** are always in square brackets at the start of AI dialogue: `[excited discovery tone]`, `[mysterious whisper]`, `[warm celebration]`, etc.
- **Every runtime round must be fully expanded** in `prod.md`. Never write "same structure," "AI gives a riddle," "later rounds follow," or any one-line summary for a runtime round.
- **All runtime steps must be executable.** Do not reserve full detail only for Step 3; Steps 1, 2, 4, and 5 also need concrete dialogue branches, follow-ups, and screen states unless a branch is genuinely inapplicable.
- **Specificity beats brevity.** Distinguish rounds, screen states, and follow-ups with concrete clues, actions, labels, consequences, or child evidence. A compact migrated package still needs enough detail to match the older quality floor.
- **Round counts** may be specified as ranges in the authoring rationale, but the runtime flow must include the concrete number of rounds the activity actually plays.
- **Step count** varies by category: In-Device Verbal typically has 5 steps; Out-of-Device Collection may have 5–6 steps
- **Closing speech** must celebrate FIRST, then naturally name Key Concepts. Concepts feel like praise, not vocabulary lessons.
- **All AI dialogue is in English.** Use age-appropriate, warm, playful language.
- **Scorecard placement**: `spec.md` includes the scorecard; `prod.md` does not.
- **Asset placement**: `spec.md` may include asset prompts and dependency rationale in `## Asset Brief`; `spec.md` must include `## Asset Usage Timeline` for any prebuilt, displayed, or runtime-generated image dependency. `prod.md` references asset IDs, display location, and fallback behavior only. Review outputs must distinguish `Asset dependencies` from `Display beats` and `Image items`; do not treat one asset row or card set as one image when it is displayed across multiple steps. Do not generate or store image files as part of package generation unless a future asset pipeline explicitly requires it.
- **Resolved blocker placement**: product-contract override runs use `RESOLVED BLOCKER` comments in `prod.md` where the formerly unsupported behavior affects a runtime beat. These comments are review annotations and do not make the package invalid when the run manifest records the override.
- **Extensibility placement**: concept-led and parameterized packages should name reusable slots such as `{runtime_entity}`, `{shared_feature}`, `{matched_color}`, `{matched_shape}`, or approved asset-set IDs in `spec.md` `## Extensibility Notes`.
- **Package alignment**: `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml` must describe the same pillar, game style, focal attribute, badge, and next-step direction as `spec.md` and `prod.md`.

---

## Phase 3: Self-Evaluation Rubric

After generating the activity design, evaluate it against ALL 10 dimensions below. Each dimension is scored PASS or FAIL. If ANY dimension fails, identify the specific issue, fix the design, then re-evaluate. Repeat until all applicable dimensions pass.

Before finalizing the `## Self-Evaluation Scorecard`, spawn a separate reviewer agent to check the same 10 dimensions independently against the actual package files. This is a required acceptance gate for every generated package in a `/goal` run; if reviewer-agent tooling is unavailable, package finalization is a hard workflow failure, not a skippable residual risk. The reviewer must read `program.md` Phase 3 and the generated `<package_dir>` directly, plus `templates.md`, `activities/README.md`, `activities/_schema/tag_block.schema.json`, and `docs/activity_vocabulary.md`; for mapping-informed assignments, it must also read the relevant mapping source, `entity_guidance.md`, and `conversation_bridge.md`. Treat any reviewer FAIL or credible uncertainty as a required repair: fix the package, rerun the author self-evaluation, and request a fresh independent review before writing the final scorecard, logging `results.tsv`, or marking the assignment complete. Record reviewer-agent coverage, evidence, repairs, and re-review outcome in the current run's `review_notes.md`.

Reviewers must fail packages that are structurally valid but thin. Passing means the package meets the migrated package depth floor: `spec.md` carries enough authoring rationale to audit the design, and `prod.md` carries enough concrete dialogue and screen behavior to run the activity without inventing missing beats.

### Dimension 1: V1 Technical Compliance (PASS/FAIL)

Check every step for dependency on blocked capabilities:
- Does any step require OCR or text reading? → FAIL
- Does any step require face/expression/pose detection? → FAIL
- Does any step require IMU angle sensing? → FAIL
- Does any step require comparing before/after object state changes (e.g., "did you fold it?")? → FAIL
- Does any step require detecting non-speech audio (clapping, tapping)? → If yes, is it replaced with dialogue workaround? If not → FAIL
- Note: Multi-photo workflows (child takes several photos across steps) are ALLOWED. What's blocked is computational comparison between photos to detect differences.
- Exception: in a run with `product_contract_override=minimum_unblock_allowed`, a formerly blocked dependency may PASS only when the package records it as a resolved blocker in `spec.md`, `prod.md`, and `run_manifest.yaml`. If the dependency is used silently, Dimension 1 still FAILS.

### Dimension 2: Hook & Transition (PASS/FAIL)

- Does Step 1 (Transition Bridge) open with emotional resonance (not knowledge testing)? → Must be YES
- Does the activity grow naturally from the initial engagement, not feel like a sudden task assignment? → Must be YES
- Is there a clear conversational bridge from the initial photo/emotion to the activity structure? → Must be YES
- Could you remove the "step" labels and it would still feel like a flowing conversation? → Must be YES

### Dimension 3: Edge Case Coverage (PASS/FAIL)

- Does EVERY step with AI dialogue include at least 3 child response types (ideal, unexpected, no response)? → Must be YES
- Does every "unexpected" follow-up validate the child's response before redirecting? → Must be YES
- Does every "no response" follow-up include a specific wait time and a gentle prompt? → Must be YES
- For Out-of-Device activities: is there a "child can't find the required item" branch? → Must be YES if applicable

### Dimension 4: IB Completeness (PASS/FAIL)

- Are 1–2 Key Concepts explicitly named? → Must be YES
- Are 2–4 Related Concepts listed? → Must be YES
- Is KUD (Know/Understand/Do) fully defined with specifics, not vague statements? → Must be YES
- Are 2–3 ATL skills identified with sub-skills? → Must be YES
- Does the closing speech naturally name the Key Concepts? → Must be YES
- Do the Key Concepts actually match what the child did in the activity (not forced)? → Must be YES

### Dimension 5: Tier Appropriateness (PASS/FAIL)

For the target tier, check:
- **T0**: Sentences ≤5 words? Onomatopoeia used? Single-step instructions? Call-and-response model? Max 2 rounds?
- **T1**: Sentences 5–8 words? 2–3 step tasks? Open-ended questions? Concrete vocabulary?
- **T2**: Complex sentences OK? Multi-step planning? Negotiation/collaboration? Abstract reasoning?
- Does the vocabulary match the tier's level? → Must be YES
- Is the task complexity achievable for the target age? → Must be YES

### Dimension 6: Dialogue Specificity (PASS/FAIL)

- Is every AI line actual, concrete dialogue (not "AI guides the child to...")? → Must be YES
- Does every AI line include a tone/emotion marker? → Must be YES
- Are AI responses warm, playful, and child-appropriate? → Must be YES
- Is there zero use of abstract instructions like "AI encourages" or "AI provides feedback"? → Must be YES
- Do follow-ups react to the child's specific branch with evidence, consequence, or a targeted scaffold rather than generic praise? → Must be YES

### Dimension 7: Screen & UI Completeness (PASS/FAIL)

- Does every step include a "Screen" description? → Must be YES
- Are screen descriptions specific (not "screen shows relevant content")? → Must be YES
- Do screen elements match what's happening in the dialogue? → Must be YES
- Are animations/visual effects described concretely (not just "animation plays")? → Must be YES
- Does each screen description identify what persists, what changes, and how progress/payoff is represented? → Must be YES

### Dimension 8: Entity Mapping Alignment (PASS/FAIL) — mapping-informed designs only

Skip this dimension if the assignment has no `mapping=` parameter. For mapping-informed designs:

- Are 1–2 Key Concepts sourced from `primary_key_concepts` or `secondary_key_concepts` in the mapping? → Must be YES
- Does the chosen concept pair avoid the Form+Connection default without justification? → Must be YES (or justified)
- Is the IB theme drawn from the mapping's `primary_theme` or `secondary_themes`? → Must be YES
- Are at least 2 of 4 Related Concepts from `candidate_related_concepts`? → Must be YES
- Are vocabulary, facts, and sensory details traceable to `tier_guidance` dimension attributes for the target tier? → Must be YES
- Are 2–3 anchor dimensions identified and used to drive core activity content? → Must be YES
- Does the warm start bridge (Step 1a) reference a specific dimension topic from the mapping? → Must be YES
- Is the warm start bridge using one of the approved opener flavors from conversation_bridge.md §2? → Must be YES

### Dimension 9: Game Feel (PASS/FAIL)

Does the design feel like a GAME, not just a structured conversation?
- Does the child experience genuine uncertainty or stakes at least once? → Must be YES
- Is there a moment where the outcome is unknown before it's revealed? → Must be YES
- Does the design have a clear emotional climax ("magic moment")? → Must be YES
- Would a child want to play this again (replayability)? → Should be YES
- Is there at least one moment of surprise, drama, or delight beyond warm encouragement? → Must be YES
- Is the magic moment earned by the child's repeated action, not merely awarded as a generic badge? → Must be YES

### Dimension 10: Mechanic Fidelity + Scaffold Honesty (PASS/FAIL)

Does the design preserve the child action promised by the assignment or Phase 0 brief, while using pillar/style scaffolding honestly?
- Does the child's repeated action in `prod.md` match `tag_block.yaml` `activity_signature.mechanic` and the Phase 0 `canonical_mechanic` if present? → Must be YES
- Does the repeated action include the full source promise, such as evidence explanation, rule naming, consequence choice, or synthesis when the assignment asks for it? → Must be YES
- Does the selected pillar/style support the mechanic without distorting the activity concept or entity intent? → Must be YES
- If `scaffold_fit` is `weak` or `generate_with_assumptions`, does `spec.md` disclose the scaffold compromise and assumptions in `## Adaptation Rationale`? → Must be YES
- Does the package avoid forcing unsupported mechanics, product capabilities, or categories into a misleading current style? → Must be YES
- Does the design still deliver a clear emotional payoff / magic moment consistent with its chosen pillar? → Must be YES

### Rubric Scorecard (append at end of every `spec.md`)

```
## Self-Evaluation Scorecard

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS/FAIL | [brief note] |
| 2 | Hook & Transition | PASS/FAIL | [brief note] |
| 3 | Edge Case Coverage | PASS/FAIL | [brief note] |
| 4 | IB Completeness | PASS/FAIL | [brief note] |
| 5 | Tier Appropriateness | PASS/FAIL | [brief note] |
| 6 | Dialogue Specificity | PASS/FAIL | [brief note] |
| 7 | Screen & UI Completeness | PASS/FAIL | [brief note] |
| 8 | Entity Mapping Alignment | PASS/FAIL/N/A | [brief note — N/A if no mapping] |
| 9 | Game Feel | PASS/FAIL | [brief note] |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS/FAIL | [brief note] |

**Overall**: ALL PASS / [N] FAIL(s) — [fixed/presenting]
```

---

## Phase 4: Seed Exemplars — Quality Reference

Study these two exemplars carefully. They represent the quality floor. Your output must match or exceed this level of detail, creativity, and specificity.

### Exemplar 1: In-Device Sustained Verbal Interaction (T0)

**Entity**: Stuffed toy dog | **Category**: 1 (Sustained Verbal Interaction)

**Activity Name**: Mood Changer

**Concept**: Child becomes the stuffed dog's "emotional spokesperson." AI presents different scenarios, and the child voices what the dog would feel/say in each one. It's like casting a spell on the toy — the child becomes the toy's voice.

**Key Design Qualities to Learn From**:
- The metaphor ("magic game where you can hear the dog's inner voice") transforms a psychology exercise into play
- Each round targets a DIFFERENT emotion (happy → surprised → excited), creating variety
- AI MODELS the behavior first ("the dog might sigh 'ohh...' or say 'where's my ball?'") before asking the child
- The closing names the child as "Dog's Emotion Translator" — a role/title that celebrates the skill
- Screen responds dynamically to the narrative (sunshine animation when the scenario is "morning sun")
- Edge cases: when child says "woof woof!" (a non-emotional response), AI validates it AS emotional ("That's saying hello to the sun!") then extends with a richer example

**Interaction Pattern**: AI narrates scenario → child voices the emotion → AI validates + extends → next scenario. 3–5 rounds, escalating emotional complexity.

**IB Mapping**: Key Concept = Perspective. The closing line explicitly connects: "The same dog feels different things when different things happen — that's the magic of Perspective."

### Exemplar 2: Out-of-Device Collection Exploration (T1)

**Entity**: Patterned stone | **Category**: 5 (Collection/Tracking Exploration)

**Activity Name**: Story Creator

**Concept**: Child photographs a stone with interesting patterns → AI asks what the pattern looks like → child names it ("a snake!") → AI proposes finding more "stone actors" to form a "stone theater troupe" → child searches for and photographs 2 more stones → each stone gets a character name → child creates a mini-story with the troupe.

**Key Design Qualities to Learn From**:
- The metaphor escalates: pattern → character → troupe → story. Each step BUILDS on the previous
- The child has a ROLE: "Director." This gives ownership and agency
- Task is broken into 3 clear sub-tasks (find 2 actors, take group photo, announce the play name) — perfect for T1
- When child only takes a photo but doesn't name the stone, AI suggests a name ("Looks like 'Starry Stone'? Or do you have a better name?") — this is scaffolding, not correcting
- Screen shows collected stones as thumbnails on the side, building a visual collection
- The "no response" case for finding stones includes: "Look near the ground, at the flower bed edges — stone actors like to hide in corners" — a CONCRETE, actionable hint

**Interaction Pattern**: AI frames mission → child explores physically → photographs finds → AI reacts to each find → collection complete → child synthesizes (names the story) → AI celebrates and names concepts.

**IB Mapping**: Key Concepts = Form + Connection. "You discovered the beauty of each stone's Form, and used your imagination to create Connections between them as a story."

---

## Phase 5: How to Use This

### Mechanic-First Workflow

Before generating any design, ALWAYS:
1. Run Phase 0 when the assignment is concept-led, has `activity_concept=`, has a legacy concept alias, or lacks a fully specified entity + category request.
2. Read `templates.md` in the layered order: (a) the **Template 0 reference** for the 5-beat spine and universal creative variables, (b) the **Mechanic Adapter** matching `canonical_mechanic`, (c) the **category modifier** for Cat1, Cat3, or Cat5, and then (d) the least misleading pillar/style scaffold required by the package schema.
3. Use the composed scaffold (Template 0 spine + mechanic adapter + category modifier + optional pillar/style scaffold) — follow the beat sequence and keep the child action faithful to `activity_signature.mechanic`.
4. Use the **Quick Entity Brainstorm Guide** for inspiration, but invent FRESH creative variables.
5. Run the mechanic fidelity, scaffold honesty, and category-specific checks before running the full rubric (Dimensions 1–10, with D8 only for mapping-informed designs).
6. If your entity is not in the brainstorm guide, extrapolate using the pattern: identify the entity's most striking VISUAL FEATURE → choose the focal attribute / observation angle → build the activity loop from the canonical mechanic.

### Input Format

When the human gives you an assignment, it will look like:

```
Design an activity for: [entity] + [category number or name]
Optional: tier=[T0/T1/T2], mechanic=[mechanic], pillar=[pillar], style=[game_style], scene=[brief scenario]
```

For concept-led adaptation, it may look like:

```
Adapt activity concept: assignment_type=activity_concept, activity_concept=[activity name], description=[concept description], notes=[source / curriculum / design comments]
Optional: mechanic=[mechanic], category=[category hint], entity=[entity or entity class], mapping=[entity_id], product_capabilities=[declared capability flags]
```

Examples:
- `Design an activity for: butterfly + category 5 (collection/tracking), mechanic=deduce`
- `Design an activity for: toy car + category 1 (sustained verbal), tier=T0, mechanic=motion_voice, style=voice_stage`
- `Design an activity for: kitchen vegetables + category 3 (material exploration), tier=T1, scene=child photographs broccoli on kitchen counter`
- `Adapt activity concept: assignment_type=activity_concept, activity_concept=Scavenger Hunt, description=find X things with a shared color or shape, mechanic=collect`
- `Adapt activity concept: assignment_type=capability_probe, activity_concept=Coloring Game, description=child photographs colors and AI fills a line drawing, category=cat5`

If `mechanic=` is provided, honor it when setting `activity_signature.mechanic`. If `style=` is omitted, infer it per §1.6 rules from the canonical mechanic, entity affordances, category, and scaffold fit. If an activity concept requires unsupported product capabilities, output the adaptation brief and constrained design preview instead of forcing a valid package.

### If tier is not specified

Infer the most natural tier based on entity + category:
- Category 1 (verbal) with toys/stuffed animals → typically T0
- Category 5 (collection/outdoor) → typically T1
- Category 4/6 (social/collaborative) → typically T2
- If ambiguous, default to T1

### If scene is not specified

Invent a plausible, specific trigger scene. Don't be generic — include where the child is, what they're doing, and what they photograph. Example: "Child is in the park and photographs a ladybug on a leaf" not "child photographs an insect."

### Batch Mode

If the human gives multiple assignments at once, design each one fully before moving to the next. Do not abbreviate later designs because "they follow the same pattern."

### After Generating

Always end with:
1. A complete `<package_dir>/` package with five files.
2. The self-evaluation scorecard at the end of `spec.md` only.
3. A one-line summary: "Ready for curriculum review" or "N issues found and fixed during self-evaluation"

---

## Appendix: Quick-Reference Checklists

### Before Selecting Key Concepts (mapping-informed designs):
- [ ] Have I read the entity mapping YAML file?
- [ ] Am I picking at least 1 Key Concept from `primary_key_concepts` (relevance ≥ 0.8)?
- [ ] If I'm using Form+Connection, can I justify it from the mapping's reasoning fields?
- [ ] Have I checked what Key Concepts the previous designs in this batch used? (Aim for diversity)
- [ ] Does my chosen concept pair match what the child actually DOES in the activity?
- [ ] Is my IB theme drawn from the mapping's primary or secondary themes?
- [ ] Am I sourcing at least 2 Related Concepts from `candidate_related_concepts`?

### Before Writing Step 1, Ask Yourself:
- [ ] What's the creative METAPHOR that transforms this from "educational exercise" into "play"?
- [ ] What ROLE does the child take on? (translator, director, detective, scientist, architect...)
- [ ] How does the first line connect to the child's EMOTION, not their KNOWLEDGE?

### For Every Step, Verify:
- [ ] AI dialogue is concrete (actual words, not descriptions of behavior)
- [ ] Tone/emotion marker is present
- [ ] 3 child response branches exist (ideal / unexpected / silence)
- [ ] "Unexpected" branch validates before redirecting
- [ ] Screen description is specific
- [ ] No V1 hard-blocked capability is required

### For Closing, Verify:
- [ ] Celebrates FIRST, concepts SECOND
- [ ] Key Concepts are named naturally (feels like praise, not vocabulary)
- [ ] The concept connection is EARNED (matches what the child actually did)
- [ ] Screen shows concept words artistically

### V1 Red Flags (instant FAIL if present in any step):
- "Child reads the text on..."
- "AI detects the child's facial expression..."
- "Child tilts the camera to..."
- "AI compares the before and after photos to detect changes..."
- "AI detects clapping/tapping/stomping sounds..."
- "AI measures how loud the child speaks..."
- Note: "Child photographs another object and AI describes what it sees" is FINE — each photo is processed independently

---

*End of program.md — Activity Design Agent ready for assignments.*
