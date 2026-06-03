# WonderLens Activity Auto-Design — program.md

Version: 1.35
Updated: 2026-06-03

Purpose: canonical authoring contract for WonderLens activity packages. This
file defines what a high-quality activity package must contain. `GOAL.md` and
`run.md` define how a run is executed. Scoped files under `goals/` define
subset/full-pass overrides. Historical change context lives in `HANDOFF.md` and
`docs/plans/`.

## How This Works

You are an **Activity Design Agent** for WonderLens, an AI-powered educational
camera for children ages 2-8. Your job is to design interactive activities from
an assignment row: an entity activity, activity concept, match pattern, or
capability probe.

Authoring responsibilities:

1. Run Phase 0 when the row is concept-led, underspecified, mapping-informed,
   asset-dependent, or product-capability-sensitive.
2. Preserve the source promise: original play frame, child role, device role,
   sequence, required child action, real/reference asset need, and
   background/context promise.
3. Compose scaffolding from `templates.md`: Template 0 spine, mechanic adapter,
   category modifier, then pillar/style overlay.
4. Write the migrated package files in Phase 2 format. Package writing is
   text-only; image generation happens only in explicit asset-build phases.
5. Self-evaluate with the 10-dimension rubric, repair failures, and require
   independent reviewer evidence before acceptance.
6. Keep output English-only, even when source rows contain Chinese or mixed
   language. Source snapshots may preserve original input text for provenance.

Operational details such as run manifests, assignment snapshots, enrichment
passes, full-pass delegated-agent orchestration, dashboard generation, and
commits live in `run.md` and scoped goal files.

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
| `demo_export` | Optional | Full `GOAL.md` generation runs default to `true`; set `false` only when the user explicitly disables direct demo export. |
| `asset_build` | Optional run/assignment override | `none`, `manifest_only`, `generate_illustrative`, `curate_reference`, or `generate_and_curate`. Default is `manifest_only` for ordinary scoped generation; larger/full production passes must set `generate_and_curate`. This controls post-package image building, not whether `asset_manifest.yaml` is emitted. |

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
| `asset_role` | Required for demo export | Runtime role: `entity`, `activity_preview`, `collection_correct`, `collection_distractor`, `badge`, `story_scene`, or `ui_overlay`. |
| `style_id` | Required for demo export | `wonderlens_device_mint_soft_3d` unless a future schema adds another approved style. |
| `screen_targets` | Required for demo export | Target display slots such as `round_device_screen`, `horizontal_debug_screen`, or `catalog_grid`, with aspect ratio, master size, and safe area. |
| `target_variants` | Required for demo export | Variant IDs, sizes, nullable file paths, and target screens, for example `round_512`, `icon_256`, `landscape_1280x720`. |
| `accuracy_mode` | Required for demo export | `illustrative` for ordinary generated art; `reference_bound` when real-world correctness matters. |
| `source_strategy` | Required for demo export | `generated_illustrative`, `curated_original`, `redraw_from_verified_data`, `licensed_reference`, or `approved_internal_reference`. |
| `transformation_policy` | Required for demo export | `generate_new`, `crop_resize_only`, `simplified_redraw`, `style_preserving_redraw`, or `no_derivative_generation`. |
| `reference_policy` / `sources` | Required for `reference_bound` assets | Approved source/provenance, allowed source type, license requirement, and verification requirement before generation is accepted. The asset builder also requires package-local accepted source metadata before producing runtime variants. |

Inline assignment rows may include `asset_policy=...`, but non-trivial assets should live in the companion asset table or YAML block. If an assignment includes `concept_source=file#concept_id` or `asset_requirements=file#asset_id`, load those referenced rows before Phase 0 and treat them as source / asset context. The activity generator should copy explicit asset requirements into Phase 0 in English; it should not generate image files directly unless a future product workflow explicitly adds an asset build stage. In full `GOAL.md` generation runs, treat `demo_export=true` by default unless the user explicitly disables it; request separate per-role runtime assets through `asset_manifest.yaml`, not one contact sheet as the runtime asset.

For the current workbook-derived concept batch, `inputs/original_activity_concepts_2026-05-29.tsv` is the committed source-intent baseline. Use `inputs/source_activity_concepts.md` only as a normalized helper. If the TSV and helper disagree about the child's role, interaction sequence, required child action, real/reference asset requirement, or background/context content, the TSV controls unless product approval for the adaptation is recorded.

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
  source_promise_alignment:
    original_play_frame: "<the source design's actual play frame, paraphrased in English>"
    child_role: "<who the child is or what role the child takes first>"
    interaction_sequence: ["<ordered source beat>", "<ordered source beat>"]
    required_child_actions: ["<must-preserve child action>"]
    non_negotiable_elements: ["<source element that cannot be removed without approval>"]
    allowed_v1_adaptations: ["<safe simplification that preserves the promise>"]
    product_dependencies: ["<asset/UI/runtime capability that must be approved or called out>"]
    alignment_status: <aligned|minor_adaptation|needs_product_decision|intent_drift>
    alignment_note: "<why the generated frame preserves or changes the source promise>"
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
        asset_role: <entity|activity_preview|collection_correct|collection_distractor|badge|story_scene|ui_overlay>
        requiredness: <required|optional|fallback>
        generation_timing: <pre_generated|runtime_generated|display_existing|none>
        style_id: <wonderlens_device_mint_soft_3d|none>
        accuracy_mode: <illustrative|reference_bound>
        source_strategy: <generated_illustrative|curated_original|redraw_from_verified_data|licensed_reference|approved_internal_reference>
        transformation_policy: <generate_new|crop_resize_only|simplified_redraw|style_preserving_redraw|no_derivative_generation>
        use_step: "<where the asset appears, e.g. prod.step_2>"
        display_location: "<screen slot / region where the asset appears>"
        screen_targets: ["round_device_screen", "horizontal_debug_screen", "catalog_grid"]
        target_variants:
          - id: "<round_512|icon_256|badge_512|landscape_1280x720>"
            target: "<screen target>"
            size: "<WIDTHxHEIGHT>"
            path: null
        prompt_en: "<directly usable English image prompt, if generated>"
        source: "<existing source or approved library ref, if not generated>"
        reference_policy:
          source_required: <true|false>
          allowed_sources: [licensed_asset, public_domain_reference, approved_internal_reference, verified_source_url]
          verification_required: <true|false>
          verification_notes: "<what must remain correct before style is applied>"
        sources:
          - label: "<source/provenance label>"
            uri: "<approved source URL, asset-library URI, or internal reference URI>"
            license: "<license or approval status>"
        display_behavior: "<how screen uses it>"
        fallback_behavior: "<what happens if unavailable>"
    missing_asset_risk: <none|low|medium|high>

  demo_support:
    export_requested: <true|false>
    asset_build: <none|manifest_only|generate_illustrative|curate_reference|generate_and_curate>
    status: <supported|degraded|unsupported|not_requested>
    ui_template: <cat1_dialogue|cat5_collection|cat5_judgment|none>
    support_level: "<full, catalog_simulated_judgment, unsupported, or other concise level>"
    entity_bindings:
      - entity_id: "<bound demo entity or runtime placeholder>"
        display_label: "<child/reviewer label>"
        source_entity_exemplar: "<source exemplar>"
        default: true
    requires:
      generated_assets: <true|false>
      real_camera: <true|false>
      runtime_judgment: <true|false>
      device_round_screen: <true|false>
    unsupported_reasons: []
    degraded_reasons: []

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
- Required visual assets are dependencies, not narrative flavor. If the activity
  cannot work without an undefined asset, block or degrade honestly.
- `spec.md` owns `## Asset Brief` and `## Asset Usage Timeline`.
- `prod.md` references asset IDs, display behavior, and fallback behavior only;
  do not put raw image prompts in runtime guidance.
- Demo-targeted packages mirror the runtime contract in `asset_manifest.yaml`
  with separate assets, roles, accuracy modes, variants, nullable paths, source
  strategy, transformation policy, and fallback behavior.
- Use `style_id: wonderlens_device_mint_soft_3d` for compatibility. The active
  visual target and generation rules live in
  `docs/activity_asset_generation_workflow.md` and `docs/asset_style_reference/`.
- Illustrative assets must come from Codex built-in imagegen in explicit asset
  phases; do not accept SVG/vector placeholders, contact sheets, or script-made
  substitute art as generated illustrative assets.
- Picker/selectable item or object assets must be declared separately and built
  under package-local `assets/items/`.
- Reference-bound assets, including constellations, artworks, maps, diagrams,
  species, historical objects, named places, and famous structures, require
  approved provenance and verified source data. Random generated approximations
  fail the contract.
- Runtime PNG sizing, fullstack-style scene bundles, crop safety, no-text/no-UI
  constraints, image QA, and repair loops are governed by
  `docs/activity_asset_generation_workflow.md`, `run.md`, and scoped full-pass
  goal files.

### 0.4.1 Asset build runtime option

`asset_build` is a run-time option for a post-package phase. It is optional for
ordinary scoped runs and mandatory as `generate_and_curate` for larger/full
production passes. It never changes the activity mechanic or runtime dialogue
and must not rewrite package prose just to fit generated images.

| `asset_build` | Behavior |
|---|---|
| `none` | Skip asset generation/curation entirely. |
| `manifest_only` | Default. Emit and validate `asset_manifest.yaml` with nullable paths; create no binary image files. |
| `generate_illustrative` | Generate only illustrative assets from approved prompts and style/screen targets using Codex built-in imagegen. The deterministic builder consumes approved PNGs from `generated_assets/inbox/` and writes package-local runtime variants. Reference-bound assets remain unbuilt unless sources already exist. |
| `curate_reference` | Let an agent propose candidates, then use web/source search and provenance verification to accept only approved originals or verified data; store accepted source originals and reviewer-approved metadata under package-local `assets/sources/`; no random substitutes. |
| `generate_and_curate` | Run both illustrative generation and reference curation/build after all packages validate. |

Asset build outputs go into package-local `assets/` directories, and audit files go under `runs/<run_id>/generated_assets/` with `asset_outputs.yaml`, `reference_sources.yaml`, `qa_notes.yaml`, and delegated-agent work items. Missing generated files should degrade or gate demo playback according to `demo_support.yaml`; do not fake paths or claim unavailable assets are displayed.

### 0.4.2 Demo support classification

When `demo_export=true`, which is the default for full `GOAL.md` generation runs, classify demo readiness deterministically from category, mechanic, runtime beats, asset requirements, and product capability flags:

| Activity shape | `demo_support.status` | `ui_template` |
|---|---|---|
| Cat1 dialogue, riddle, voice acting, prediction, imagination, or simple enumeration that runs through speech plus screen state | `supported` | `cat1_dialogue` |
| Simple guided drawing or material build-step flow represented as text-guided child/caregiver self-report, with declared step-card assets/fallbacks, no visual assessment, and no photo-verification claim | `degraded` | `cat1_dialogue` |
| Cat5 simple visual collection such as fluffy, dots, color, shape, or another catalogable visible property | `supported` | `cat5_collection` |
| Cat5 requiring runtime judgment such as beginning sound, semantic category, or open-ended child naming | `degraded` | `cat5_judgment` |
| Drawing, coloring, physical building, sorting/grouping UI, tournament, certificate, complex Cat3, visual verification, final-photo validation, before/after comparison, or any unimplemented mechanic/UI dependency that cannot be represented by honest self-report | `unsupported` | `none` |

Supported and degraded demo packages must declare at least one `entity_bindings` entry and exactly one default binding. Unsupported packages may still include a binding for review context, but consumers must not show them as playable. A degraded package must explain the limitation, such as "catalog simulated judgment, not real camera validation." Do not hide an unsupported mechanic behind a Cat1 or Cat5 scaffold.

### 0.5 Readiness rules

- `ready_to_generate`: current Cat1/Cat3/Cat5 package workflow, V1 constraints, and existing schema can represent the idea safely.
- `generate_with_assumptions`: generation may proceed, but `spec.md` must include an `Adaptation Rationale` section summarizing the assumptions, asset dependency, and any weak scaffold fit.
- If the source play frame cannot be preserved without a product/design decision, set `readiness=blocked_until_product_decision` or `source_promise_alignment.alignment_status=needs_product_decision`.
- If category/mechanic labels are preserved but the child role, interaction sequence, story frame, or required child action changes materially, set `source_promise_alignment.alignment_status=intent_drift` and repair before finalization unless product explicitly approves the adaptation. For workbook-derived rows, compare against the workbook row first; for the current workbook batch, cite `inputs/original_activity_concepts_2026-05-29.tsv` evidence before normalized helper evidence.
- Source-derived, concept-led, workbook-derived, pilot-validation, and full-pass outputs require independent source-intent auditor evidence before package writing and again before acceptance. The pre-package audit locks the source promise for the writer; the post-package audit compares the original source row or run-local source snapshot against the generated package, blocked/degraded artifact, and downstream conversion/runtime evidence when available. Unresolved `intent_drift` prevents `results.tsv` logging, assignment checkoff, downstream acceptance, full-pass scale-up, and final completion.
- `blocked_until_product_decision`: write a blocked brief and a constrained design preview for this row, do not create a valid runtime package under `activities/`, append `results.tsv`, or mark the assignment complete, then continue to the next unchecked row. Use this for unsupported categories, required assets/UI state/material workflow/motion safety, OCR risk, pose risk, before/after state verification, or a mechanic that cannot be represented by current workflow without distorting the activity concept. The preview should be detailed enough to review the proposed activity, but every blocked assumption must be called out inline with `BLOCKED ELEMENT: <reason>` so the design can become valid only after those constraints are resolved.
- `minimum_unblock_allowed` override: if the run manifest records this product-contract override, dependencies that previously caused `blocked_until_product_decision` may generate as normal packages. The package still must show those dependencies in `spec.md` `## Resolved Product Contract Notes`, run provenance for affected beats, and `run_manifest.yaml` `resolved_blockers`. Runtime-facing `prod.md` may include review-only `RESOLVED BLOCKER` comments only when all target consumers ignore them safely. Dimension 1 passes because the product contract now authorizes the minimum behavior; the annotations remain for review and implementation traceability.
- Demo support status does not override package readiness. A package can be a valid five-file activity and still have `demo_support.status: unsupported` because the current fullstack demo lacks the needed UI/runtime primitive.

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

4. **Concrete Runtime Speech Contract**: Older packages may use `AI says` with actual dialogue and tone/emotion markers. New packages may use `Runtime AI instruction` plus `Example AI line` when the live LLM should generate wording at runtime. The instruction must be strong enough to convert into downstream `step_instructions` or WonderLens AI equivalent runtime prompts: include the beat goal/action, tier or length constraint, emotion/tone, required child progress evidence, branch behavior, source/activity frame guardrail, safety/product limits, and source-promise alignment. The example line shows acceptable tone and wording but is not the only allowed runtime response. Never write vague summaries such as "AI guides the child."

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
- **Demo importer** reads optional `demo_support.yaml`; it must declare `supported`, `degraded`, or `unsupported`, a concrete UI template, explicit entity binding, product/runtime requirements, and limitation notes.
- **Asset pipeline / demo importer** reads optional `asset_manifest.yaml`; it must declare separate runtime assets, screen targets, prompt/source, variants, nullable file path slots, fallback behavior, and reference-bound provenance.

#### Migrated package depth floor

The migrated five-file package intentionally moves metadata and recap/dashboard payloads out of `spec.md` and `prod.md`; shorter files are acceptable only when they remain rich enough to run and review. Compactness is not a quality goal. A package is too thin if a fresh reviewer cannot understand the intended experience, constraints, mechanic, game feel, and runtime behavior without reconstructing missing detail from older examples.

- `spec.md` must be a decision-useful authoring reference, not just a scorecard wrapper. It must explain the premise, target tier/category, trigger, canonical mechanic, scaffold choice, adaptation rationale, mapping/asset/product assumptions, why the game feel works, and any known residual risk.
- `prod.md` must be a runnable prompt source, not a terse script. Steps 1, 2, 4, and 5 need the same executable shape as Step 3: exact AI dialogue or a runtime behavior contract with an example AI line, ideal/unexpected/no-response child branches where applicable, matching AI follow-ups or follow-up policy, and specific screen state.
- Step 3 rounds must be distinct, not template clones. Each round needs a named objective, a different clue/challenge/action, child responses that exercise the promised mechanic, follow-ups that react to what the child said/did, and a screen-state change that preserves progress.
- The magic moment must be visible in both dialogue and screen behavior. A badge alone is not enough; include a reveal, consequence, synthesis, audience reaction, map/progress completion, visitor test, or other payoff that follows from the child's actions.
- Avoid generic filler such as "Great job," "try again," "the screen updates," or "the AI encourages" unless it is paired with specific evidence, consequence, or screen behavior. Warmth without specificity does not pass the detail floor.
- Do not use line count as the primary measure. Use completeness, specificity, and replayable game feel. When in doubt, add concrete runtime detail rather than trimming.

#### Pre-output self-check

Before emitting a completed migrated package, verify:

- [ ] The package has the five required files: `spec.md`, `prod.md`, `tag_block.yaml`, `recap.template.yaml`, `dashboard.template.yaml`.
- [ ] Directory name equals `tag_block.yaml` `activity_id`.
- [ ] `tag_block.yaml` validates against `activities/_schema/tag_block.schema.json`.
- [ ] `tag_block.yaml` uses current field names: `game_style` (not `style`), `tier_range` (not `tier` / `tier_variants`), and `activity_signature.focal_attribute`.
- [ ] `pillar`, `game_style`, `template_type`, `tier_range.primary`, `key_concepts`, `progression.topic_axis`, `activity_signature.observation_angle`, `activity_signature.mechanic`, and `activity_signature.entity_role` use the current enum vocabulary.
- [ ] `prod.md` contains Basic Info, Activity Overview, and Interaction Flow sections, with every runtime step represented.
- [ ] `prod.md` passes the migrated package depth floor: every step is runnable, concrete, and specific enough for the prompt composer without relying on old design files.
- [ ] `prod.md` Step 3 keeps **every round in full detail**: either `AI says` exact dialogue or `Runtime AI instruction` plus `Example AI line`, child response branches, AI follow-up branches or policy, and screen state. No "same structure," "AI gives...", or one-line summaries.
- [ ] `prod.md` has no `## Self-Evaluation Scorecard`.
- [ ] `spec.md` has exactly one `## Self-Evaluation Scorecard`, contains enough rationale for an independent reviewer to judge the activity, and the notes are truthful against `prod.md`, `tag_block.yaml`, `program.md`, and `templates.md`.
- [ ] `recap.template.yaml` and `dashboard.template.yaml` use the same focal attribute / badge / activity identity as `tag_block.yaml` and `prod.md`.
- [ ] `dashboard.template.yaml` `dashboard_fragment.session.focal_attribute` exactly equals `tag_block.yaml` `activity_signature.focal_attribute`.
- [ ] No field value is a placeholder, ellipsis, or instruction-shaped string ("pick one of...", "see mapping", etc.).
- [ ] If `demo_support.yaml` is present, it validates against `activities/_schema/demo_support.schema.json` or the focused validator, and its status/template honestly match the current demo support gate.
- [ ] If `asset_manifest.yaml` is present, it validates against `activities/_schema/asset_manifest.schema.json` or the focused validator, uses separate runtime assets rather than contact sheets, and requires source/provenance for reference-bound assets.

If any box fails, fix the package and re-run both the 10-dimension rubric and this self-check. Do **not** emit a package with incomplete metadata or condensed runtime steps — downstream surfaces will silently fall back to generic copy or lose runtime behavior.

> **Cross-reference:** see `docs/progression_axes.md` for the 7-axis enum and L1/L2/L3 rung definitions. If that file is not yet merged when you read this, the same axes are listed in `docs/template_0_preview.html` §07; `docs/progression_axes.md` becomes the sole source of truth once it lands.

---

## Phase 2: Output Format — Exact Structure Required

Generate the migrated activity package with the five required files in this exact structure. Do not skip required files, do not reorder required sections, and do not abbreviate runtime rounds. Full `GOAL.md` generation runs request direct demo export by default; add optional demo extension files unless the user explicitly disables demo export.

For fresh `/goal` generation, `<package_dir>` is `runs/<run_id>/activity_packages/<activity_id>/`. For canonical/promoted package maintenance, `<package_dir>` may be `activities/<activity_id>/`.

The five required files are:

```text
<package_dir>/
├── spec.md
├── prod.md
├── tag_block.yaml
├── recap.template.yaml
└── dashboard.template.yaml
```

When `demo_export=true`, also add:

```text
<package_dir>/
├── demo_support.yaml
└── asset_manifest.yaml
```

These extension files do not replace the five-required-file package contract. A package without them remains structurally valid, but it is not direct-demo-import ready. Under the standard full generation goal, missing extension files are a run failure unless demo export was explicitly disabled or the assignment only produced a blocked preview.

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
2. (Unexpected) "[specific off-track response likely in this exact beat]"
3. (No response) [specific silence/hesitation behavior tied to this beat's screen, role, or action]

**AI follow-up:**

1. [tone marker] "[exact response to ideal]"
2. [tone marker] "[exact response to unexpected - validate, then return to this beat's source action]"
3. [wait 2s] [tone marker] "[exact response to silence - model one tiny in-frame action]"

**Screen:** [specific description of what the screen shows]

For new runtime-LLM packages, a step or round may replace `AI says` with a behavior contract:

```markdown
**Runtime AI instruction:** Goal: [beat goal/action, source play frame, required content, and what must not be skipped]. Constraint: [tier/length and safety/product limits]. Tone: [emotion/tone]. Progress evidence: [what child progress looks like]. Branch behavior: [ideal, unexpected, and no-response policy]. Frame/source guardrail: [source role, sequence, asset, background/context, and screen-state guardrail].

**Example AI line:** [tone/emotion marker] "[one concrete acceptable line]"
```

Existing `AI says` exact-dialogue steps remain valid. Do not use a single fixed example line as the only runtime response when the product expects live LLM generation.

#### Step 2: [Frame / Rule Introduction / Demo]

[same full format as Step 1]

#### Step 3: Multi-Round Interaction

**Round 1 -- [round name]:**

[full AI says or Runtime AI instruction + Example AI line / child responses / AI follow-up or policy / Screen]

**Round 2 -- [round name]:**

[full AI says or Runtime AI instruction + Example AI line / child responses / AI follow-up or policy / Screen]

**Round 3 -- [round name]:**

[full AI says or Runtime AI instruction + Example AI line / child responses / AI follow-up or policy / Screen]

#### Step 4: [Magic Moment / Celebration / Synthesis]

[same full format as Step 1]

#### Step 5: Closing + IB Concepts

[celebration first, then naturally names the Key Concepts the child explored; include child responses, AI follow-up, and Screen]
```

`spec.md` is the author/reviewer reference. It should summarize premise, target, rationale, selection trigger, pillar/game style, and then end with exactly one `## Self-Evaluation Scorecard`. For concept-led assignments, include an `## Adaptation Rationale` section before the scorecard summarizing the Phase 0 brief: core promise, source-promise alignment, canonical mechanic, input mode, readiness, trigger condition, mapping use, asset dependency, product-capability flags, scaffold fit, and assumptions. When `product_contract_override=minimum_unblock_allowed` applies, include `## Resolved Product Contract Notes` before the scorecard and list every formerly blocking dependency. When the concept can be reused with other entities, properties, or asset sets, include `## Extensibility Notes` before the scorecard with concrete reusable slots and retargeting guidance. When `asset_dependency.policy` is not `no_assets`, also include an `## Asset Brief` section before the scorecard with one row per asset requirement: `asset_id`, `asset_type`, requiredness, generation timing, use step, display location, purpose, `prompt_en` or source, display behavior, fallback behavior, and safety constraints. Add `## Asset Usage Timeline` before the scorecard for any prebuilt, displayed, or runtime-generated image dependency; each row must make it easy to see the asset ID, whether it is prebuilt or runtime-generated, exactly when it is loaded/generated, where it appears on screen, which step/round uses it, the prompt/source summary, whether it persists or is hidden, and the fallback. For demo-targeted packages, mirror the consumer-facing asset contract in `asset_manifest.yaml`; `spec.md` may explain rationale, but `asset_manifest.yaml` owns separate runtime assets, role, style, variants, file path slots, fallbacks, and reference-bound source/provenance. Keep it concise, but not skeletal: include enough specifics that a reviewer can identify what makes this activity different from a generic template.

### Format Rules

- **Tone markers** are always in square brackets at the start of AI dialogue: `[excited discovery tone]`, `[mysterious whisper]`, `[warm celebration]`, etc.
- **Every runtime round must be fully expanded** in `prod.md`. Never write "same structure," "AI gives a riddle," "later rounds follow," or any one-line summary for a runtime round.
- **All runtime steps must be executable.** Do not reserve full detail only for Step 3; Steps 1, 2, 4, and 5 also need concrete dialogue branches, follow-ups, and screen states unless a branch is genuinely inapplicable.
- **Runtime behavior contracts** must pair `Runtime AI instruction` with `Example AI line`, and must preserve source-promise alignment. A behavior instruction is not acceptable if it omits the downstream `step_instructions` / WonderLens AI runtime essentials: goal/action, tier/length constraint, emotion/tone, child progress evidence, branch behavior, source/activity frame guardrail, concrete example line, and specific screen/state behavior. It is also not acceptable if it omits the story setup, profession role-play, physical challenge, photo collection, UI state, background/context promise, reference asset reveal, or other source element that makes the activity what it is.
- **Machine-convertible runtime instructions** are required for direct-consumer and full-pass packages. Every live activity beat must include one single-line label in this exact form: `**Runtime AI instruction:** Goal: ... Constraint: ... Tone: ... Progress evidence: ... Branch behavior: ... Frame/source guardrail: ...`. Use it for Step 1 hook, Step 2 mission/transition, every Step 3 round, Cat5 synthesis when present, celebration, closing, and early-exit behavior where applicable. `AI says` and `Example AI line` may remain as human-readable examples, but they are not sufficient by themselves for portable downstream loading.
- **Celebration is not a new gameplay beat.** Step 4 celebration/magic moment instructions must recap, reveal, synthesize, or award based on already-completed child actions. They must not ask a new required child decision, introduce a fresh binary choice, start another challenge, or move source-required gameplay out of Step 3. If the source promise needs one more choice, question, tool/action decision, photo, drawing step, or collection action, make it an explicit Step 3 round before celebration.
- **Parseable round and synthesis shape**: Step 3 round headings should use ASCII form `**Round N -- Short Scenario:**` so downstream importers can reliably extract round scenarios. Cat5 packages must distinguish collection rounds from synthesis and celebration; synthesis instructions must name the collection criterion, accepted evidence, how collected items are combined, and the required final story or summary format.
- **Branch policies must be beat- and round-specific.** Do not reuse boilerplate such as "Child gives an unrelated answer, unsafe action, or asks to change the task", "Validate the idea, restate the safe rule", or "Model a tiny answer" across activities. Do not keyword-substitute a generic row with the activity title, round title, or mechanic name. Unexpected and no-response branches must name what the child is likely to do in this exact beat and how the AI preserves the current mechanic, source frame, asset/fallback, and screen state.
- **Step 3 branch rows must not repeat across rounds.** If Round 1, Round 2, and Round 3 share the same unexpected/no-response child behavior or AI follow-up text, repair the package before review. Each round should reference the current clue, choice, challenge, asset state, prior consequence, or completion target.
- **Specificity beats brevity.** Distinguish rounds, screen states, and follow-ups with concrete clues, actions, labels, consequences, or child evidence. A compact migrated package still needs enough detail to match the older quality floor.
- **Round counts** may be specified as ranges in the authoring rationale, but the runtime flow must include the concrete number of rounds the activity actually plays.
- **Step count** varies by category: In-Device Verbal typically has 5 steps; Out-of-Device Collection may have 5–6 steps
- **Closing speech** must celebrate FIRST, then naturally name Key Concepts. Concepts feel like praise, not vocabulary lessons.
- **All AI dialogue is in English.** Use age-appropriate, warm, playful language.
- **Scorecard placement**: `spec.md` includes the scorecard; `prod.md` does not.
- **Asset placement**: `spec.md` may include asset prompts and dependency rationale in `## Asset Brief`; `spec.md` must include `## Asset Usage Timeline` for any prebuilt, displayed, or runtime-generated image dependency. For demo export, `asset_manifest.yaml` owns the machine-readable runtime asset contract: separate asset roles, style ID, screen targets, variants, nullable file paths, prompt/source, fallback behavior, and reference provenance. Illustrative prompts must use the WonderLens activity asset style from Phase 0.4 and the repo-local `docs/asset_style_reference/` files instead of pointing to an external prompt file. `prod.md` references asset IDs, display location, and fallback behavior only. Full-pass packages must include the standard fullstack-style scene bundle (`activity_icon`, `intro_scene`, `rules_scene`, `round_1_scene`, `round_2_scene`, `round_3_scene`, `celebrate_scene`, `closing_scene`, plus `synthesis_scene` when applicable) in addition to any object/item assets. Picker/selectable item or object assets must be declared separately and built under package-local `assets/items/`, not mixed with beat-scene/background assets. Review outputs must distinguish `Asset dependencies` from `Display beats` and `Image items`; do not treat one asset row or card set as one image when it is displayed across multiple steps. Do not generate or store image files as part of package authoring; only the explicit post-package asset build phase writes package-local runtime images. Contact sheets are review-only artifacts, not runtime asset manifests.
- **Resolved blocker placement**: product-contract override runs must preserve formerly blocked dependencies in `spec.md`, run provenance, and review/dashboard output. Use raw `RESOLVED BLOCKER` comments in `prod.md` only when every target consumer ignores them safely; WonderLens AI runtime generation currently treats such leakage markers as invalid, so direct WonderLens AI validation must either strip review-only markers before conversion or keep them out of runtime-facing `prod.md`. Before comparing or accepting fullstack-demo and WonderLens AI dialogue quality, run `! rg -n "RESOLVED BLOCKER|RESOLVE BLOCKER" runs/<run_id>/activity_packages/*/prod.md`; any match is a package-owned blocker unless the downstream converter is explicitly proven to strip or accept that marker.
- **Extensibility placement**: concept-led and parameterized packages should name reusable slots such as `{runtime_entity}`, `{shared_feature}`, `{matched_color}`, `{matched_shape}`, or approved asset-set IDs in `spec.md` `## Extensibility Notes`.
- **Package alignment**: `tag_block.yaml`, `recap.template.yaml`, and `dashboard.template.yaml` must describe the same pillar, game style, focal attribute, badge, and next-step direction as `spec.md` and `prod.md`.
- **Source-promise alignment**: the package must preserve the original play frame, child role, interaction sequence, and required child actions unless `spec.md` and run provenance explicitly record a product-approved adaptation.
- **Direct-consumer boundary**: fullstack-demo and WonderLens AI load/execute package content. They must not be used to improve, weaken, rewrite, or reinterpret the package to hide thin runtime AI instructions, source-intent drift, unsupported mechanics, or missing assets. Package-owned failures return to autodesign for repair; consumer-runtime failures are recorded as downstream follow-up unless explicitly in scope.

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
- Exception: in a run with `product_contract_override=minimum_unblock_allowed`, a formerly blocked dependency may PASS only when the package records it as a resolved blocker in `spec.md`, run provenance, and `run_manifest.yaml`. Runtime-facing `prod.md` markers are allowed only when target consumers ignore them safely. If the dependency is used silently, Dimension 1 still FAILS.
- For demo-targeted packages, does `demo_support.yaml` claim `supported` only when the current Cat1/Cat5 demo primitive can play it, and `degraded` only when the limitation is explicit? → Must be YES
- Does every unsupported demo mechanic/UI/runtime dependency use `demo_support.status: unsupported` instead of pretending it is playable? → Must be YES

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

- For exact-dialogue beats, is every `AI says` / follow-up line actual, concrete dialogue (not "AI guides the child to...")? → Must be YES
- For runtime-contract beats, does every `Runtime AI instruction` include goal/action, tier/length constraint, emotion/tone, child progress evidence, branch behavior, source/activity frame guardrail, safety/product constraints, specific screen/state behavior, and a concrete `Example AI line`? → Must be YES
- Does every exact AI line or example AI line include a tone/emotion marker? → Must be YES
- Are AI responses or runtime behavior constraints warm, playful, and child-appropriate? → Must be YES
- Is there zero use of abstract instructions like "AI encourages" or "AI provides feedback"? → Must be YES
- Do follow-ups react to the child's specific branch with evidence, consequence, or a targeted scaffold rather than generic praise? → Must be YES
- Are unexpected/no-response child branches and AI follow-up policies specific to this beat, not copied boilerplate across the package or run? → Must be YES

### Dimension 7: Screen & UI Completeness (PASS/FAIL)

- Does every step include a "Screen" description? → Must be YES
- Are screen descriptions specific (not "screen shows relevant content")? → Must be YES
- Do screen elements match what's happening in the dialogue? → Must be YES
- Are animations/visual effects described concretely (not just "animation plays")? → Must be YES
- Does each screen description identify what persists, what changes, and how progress/payoff is represented? → Must be YES
- If `asset_manifest.yaml` is present, do declared variants include the round-device screen target, safe-area rules, and fallback behavior for missing assets? → Must be YES
- For full-pass runs, does the package include the standard fullstack-style scene bundle and package-local 512x512 PNGs, not just item/card assets? → Must be YES
- For illustrative assets, do prompts and accepted outputs follow the WonderLens activity asset style and avoid baked-in masks, borders, text, labels, logos, contact sheets, and UI chrome? → Must be YES
- For generated illustrative assets in subset/full-pass runs, were source PNGs produced with Codex built-in imagegen rather than SVG/vector/placeholder substitutes? → Must be YES
- For item/object picker activities, do scene backgrounds avoid duplicate selectable objects that compete with picker sprites, target/distractor cards, or collection items? → Must be YES; otherwise hard REPAIR
- For item/object picker activities, are selectable item/object PNGs declared separately and built under `assets/items/` rather than mixed with scene/background assets? → Must be YES; otherwise hard REPAIR
- For evidence-building or partial-reveal activities, do images preserve the step-by-step reveal sequence and avoid showing the final answer too early? → Must be YES; otherwise hard REPAIR
- Do scene assets avoid baked app UI such as progress dots, round markers, response slots, rule strips, buttons, chips, picker slots, or badges? → Must be YES; otherwise hard REPAIR
- Are unrelated activities visually distinct rather than variants of the same generic template? → Must be YES; otherwise hard REPAIR
- For guided drawing/build-step activities, does each round image show the actual step the child should perform? → Must be YES; otherwise hard REPAIR
- For reference-bound assets, does the manifest include approved source/provenance and verification behavior before applying device style? → Must be YES

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
- Does the runtime flow preserve the source-promise alignment fields: original play frame, child role, interaction sequence, and required child actions? → Must be YES unless product-approved adaptation is recorded.
- Does the repeated action include the full source promise, such as evidence explanation, rule naming, consequence choice, or synthesis when the assignment asks for it? → Must be YES
- Does the selected pillar/style support the mechanic without distorting the activity concept or entity intent? → Must be YES
- If `scaffold_fit` is `weak` or `generate_with_assumptions`, does `spec.md` disclose the scaffold compromise and assumptions in `## Adaptation Rationale`? → Must be YES
- Does the package avoid forcing unsupported mechanics, product capabilities, or categories into a misleading current style? → Must be YES
- If the full activity is valid but not playable in the current demo, does `demo_support.yaml` mark it `unsupported` with concrete missing UI/runtime reasons? → Must be YES when demo export is requested
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

## Phase 4: Quality Reference

Use legacy designs and generated packages as examples only after reading the
current contracts above. Good packages share these qualities:

- The metaphor turns the source idea into play, not a worksheet.
- The child has a specific role tied to what they actually do.
- Each Step 3 round changes the objective, clue, action, evidence, or screen
  state.
- The AI models the expected behavior before asking young children to perform
  it.
- Edge branches validate the child first, then return to the current source
  action.
- Cat5 collection activities synthesize the set; they do not end at "you found
  three things."
- The magic moment follows from accumulated child action and is visible in
  dialogue plus screen behavior.
- IB concepts are named naturally in the closing because they match what the
  child just did.

Use `run.md` for execution steps, batch behavior, final reporting, and commit
rules.
