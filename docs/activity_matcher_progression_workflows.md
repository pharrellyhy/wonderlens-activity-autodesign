# Activity Matcher and Progression Workflows

**Version:** 0.1 - 2026-04-30
**Status:** Supplement reference
**Chinese version:** `docs/activity_matcher_progression_workflows_cn.md`
**Related guide:** `docs/activity_tag_block_progression_guide.md`

This document is diagram-first. It shows how the matcher uses the full tag block before an activity starts, and how the progression algorithm updates the next activity recommendation and parent growth path after an activity completes.

---

## 1. Activity Matcher Workflow

The matcher has two gates:

1. **Eligibility:** can this activity run for this photo, tier, and runtime context?
2. **Ranking:** among eligible activities, which one best follows the conversation and progression target?

```mermaid
flowchart TD
    Photo["Child photo + conversation context"] --> Detect["Detect entity, class chain, attributes, safety context"]
    Detect --> Signature["Build conversation_signature\nentity, dominant_angle, secondary_angles, child_tier"]
    Signature --> Target["Read progression target\naxis + rung preference"]
    Target --> Catalog["Load active activity catalog\ntag_block.yaml per activity"]

    Catalog --> Validate{"Valid tag block?"}
    Validate -->|no| DropInvalid["Exclude activity\nschema or required field issue"]
    Validate -->|yes| Tier{"Tier allowed?\ntier_range.span + matchability.tier_support"}

    Tier -->|no| DropTier["Exclude activity\ntier unsupported"]
    Tier -->|yes| Binding{"Binding rule passes?\nbound, parameterized, agnostic"}

    Binding -->|no| DropBinding["Exclude activity\nentity mismatch"]
    Binding -->|yes| ClassFilter{"entity_class_filter passes?\nempty means wide"}

    ClassFilter -->|no| DropClass["Exclude activity\nclass not allowed"]
    ClassFilter -->|yes| Properties{"Required properties resolve?\ncolor, shape, pattern, material, etc."}

    Properties -->|no| DropProperty["Exclude activity\nmissing runtime parameter"]
    Properties -->|yes| Safety{"Safety + availability pass?"}

    Safety -->|no| DropSafety["Exclude activity\nunsafe or unavailable"]
    Safety -->|yes| Eligible["Eligible candidate"]

    Eligible --> Score["Score candidate"]
    Score --> S1["Eligibility score\nbinding + class + tier fit"]
    Score --> S2["Conversation coherence\nobservation_angle + bridge_prerequisites"]
    Score --> S3["Progression fit\ntarget axis + rung"]
    Score --> S4["Freshness and product policy\navoid repetition, respect catalog constraints"]

    S1 --> Rank["Rank eligible candidates"]
    S2 --> Rank
    S3 --> Rank
    S4 --> Rank

    Rank --> Enough{"Coherent winner?"}
    Enough -->|yes| Render["Render preview fields\npreview_label, preview_prompt, intro"]
    Render --> Start["Start selected activity"]
    Enough -->|no| Fallback["Ask for another photo, continue conversation,\nor use safe fallback"]

    Start --> Session["Create session event seed\nselected activity_id, entity, tier, axis, rung, angle, mechanic"]
```

### 1.1 Eligibility Rules

An activity enters the candidate set only when all hard checks pass:

| Check | Fields used | Failure behavior |
|---|---|---|
| Tag block validity | schema-required fields | Exclude from catalog. |
| Tier support | `tier_range.span`, `matchability.tier_support` | Exclude for this child tier. |
| Binding fit | `entity_binding`, `entity`, `entity_class` | Exclude if the photo cannot support the declared binding. |
| Handoff compatibility | `entity_compatibility`, `parameterization.mode` when available | Exclude or flag if the package is source-bound, unsupported, or missing the mode required for arbitrary handoff. |
| Class allowlist | `matchability.entity_class_filter` | Exclude if non-empty filter does not intersect the detected entity class chain. |
| Property resolution | `activity_signature.focal_attribute`, legacy `entity_attributes_covered` where present | Exclude if required runtime value cannot be filled. |
| Safety/runtime availability | runtime safety and environment checks | Exclude or ask for another photo. |

### 1.2 Binding Examples

| Binding | Eligible example | Common `entity_class_filter` |
|---|---|---|
| `bound` | `voice_stage_lion` for lion/big-cat contexts. | Narrow: `[big_cat]`, `[butterfly]`, `[ladybug]`. |
| `parameterized` | `color_scout_property` for any safe entity with a resolvable color. | Wide `[]` for universal property hunts; restricted `[patterned_thing]` for pattern-specific activities. |
| `agnostic` | General noticing warm-up where the photo only anchors attention. | Usually `[]` or `[observable_thing]`. |

### 1.3 Ranking Is Separate From Eligibility

Eligibility says the activity may run. Ranking chooses the best activity among eligible candidates.

```mermaid
flowchart LR
    Eligible["Eligible candidates"] --> Coherence["Conversation coherence\nangle + bridge"]
    Eligible --> Progression["Progression preference\naxis + rung"]
    Eligible --> Freshness["Freshness\nentity, pillar, game style"]
    Eligible --> Policy["Product constraints\nsafety, coverage, availability"]

    Coherence --> Rank["Rank"]
    Progression --> Rank
    Freshness --> Rank
    Policy --> Rank

    Rank --> Winner["Selected activity"]
    Rank --> NoWinner["No coherent candidate\nfallback path"]
```

---

## 2. Progression Workflow

Progression starts with the activity's declared axis/rung, but it updates state from observed child evidence. It affects the next activity as a recommendation, not a guarantee.

```mermaid
flowchart TD
    Start["Activity starts\nselected activity_id + entity + tier"] --> Declared["Read declared progression\ntopic_axis + difficulty_level"]
    Declared --> Prompt["Agent prompts at declared or runtime-adjusted rung"]
    Prompt --> Response["Child response, silence, or action"]
    Response --> Evidence["Build evidence vector\ncorrectness, latency, hint_level, language_depth,\non_topic_persistence, confidence"]

    Evidence --> Reliability["Apply evidence reliability rules\nhard telemetry > structured facts > language classifier > affect"]
    Reliability --> Scores["Update per-child per-axis scores\nmastery, engagement, support_needed, stability, novelty_readiness"]
    Scores --> Guardrails["Apply pedagogy guardrails\nwait time, no single-silence demote,\nsoft reframe, dignity surface"]
    Guardrails --> Policy["Map state to external action"]

    Policy --> Promote["promote\nnext prompt/activity can go deeper"]
    Policy --> Hold["hold\nsame rung, new variation"]
    Policy --> Soft["soft_reframe\nslower or gentler wording"]
    Policy --> Demote["demote\nlower cognitive load with dignity wording"]
    Policy --> Sibling["sibling_jump\nlateral axis for novelty or relief"]

    Promote --> LiveAdapt["Optional in-activity adaptation\nricher follow-up if authored"]
    Hold --> LiveAdapt
    Soft --> LiveAdapt
    Demote --> LiveAdapt
    Sibling --> LiveAdapt

    LiveAdapt --> Complete["Activity completes"]
    Complete --> Event["Emit progression_event\naxis, entry_rung, exit_rung, action,\nreason_codes, scores_before, scores_after"]
    Event --> AxisState["Persist axis_state\none state per child per axis"]

    AxisState --> NextPref["Compute next preference\ntarget_axis, target_rung,\nsibling candidate if needed"]
    NextPref --> Selector["Next activity selector\nuses preference as bonus, not hard filter"]
    Selector --> CatalogFit{"Eligible matching activity exists?"}
    CatalogFit -->|yes| NextActivity["Prefer matching activity\nsame axis/rung or elastic variant"]
    CatalogFit -->|no| BestCoherent["Choose best coherent eligible activity\nrecord fallback reason"]

    Event --> ParentEvent["Append parent-safe session event\naxis, rung, action reason codes,\nangle, mechanic, entity_role"]
    ParentEvent --> Window["Aggregate over parent view window\nweek or month"]
    Window --> Dashboard["Update growth path\nLxT ladder, angle split,\nexploration matrix, Try at home suggestions"]
```

### 2.1 What Changes During The Activity

During the live activity, the runtime may adapt the prompt, hint, wait time, multiple-choice support, or wording. It should not suddenly swap the whole activity.

| Runtime signal | Allowed live effect |
|---|---|
| Long wait but engaged | `soft_reframe`, longer wait, gentler prompt. |
| Correct after support | Usually `hold`; vary exemplar or ask a similar prompt. |
| Spontaneous deeper answer | Optional richer follow-up if the activity has an authored variant. |
| Repeated overload | Lower cognitive load with dignity wording. |

### 2.2 What Changes After The Activity

Durable progression state normally commits after the activity ends.

| Output | Consumer | Use |
|---|---|---|
| `axis_state` | Progression engine and selector | Tracks current rung, mastery, engagement, support need, stability, novelty readiness. |
| `progression_event` | Analytics/debugging/parent-safe rollup | Explains why the action happened without exposing raw transcript. |
| `target_axis` / `target_rung` | Next activity selector | Adds a preference bonus to the next selection. |
| parent-safe session event | Parent dashboard | Feeds weekly/monthly aggregate views. |

### 2.3 Next Activity Routing

```mermaid
flowchart TD
    Pref["Progression preference\naxis + rung or sibling axis"] --> Photo["Next child photo + conversation"]
    Photo --> Candidates["Run matcher eligibility\nentity, tier, property, safety"]
    Candidates --> Exact{"Exact preferred axis/rung eligible?"}

    Exact -->|yes| UseExact["Select exact or near-exact match"]
    Exact -->|no| Elastic{"Same family with elastic rung variant?"}

    Elastic -->|yes| UseElastic["Use same family\nhigher-rung prompt variant or micro-challenge"]
    Elastic -->|no| SameAxis{"Any coherent same-axis option?"}

    SameAxis -->|yes| UseSameAxis["Hold axis/rung\nuse best coherent activity"]
    SameAxis -->|no| Sibling{"Sibling axis recommended or needed?"}

    Sibling -->|yes| UseSibling["Select sibling-axis activity\nnovelty or relief"]
    Sibling -->|no| ChildCuriosity["Follow child's new photo context\nbest coherent eligible activity"]

    UseExact --> Record["Record selection reason"]
    UseElastic --> Record
    UseSameAxis --> Record
    UseSibling --> Record
    ChildCuriosity --> Record
```

Progression preference is not a reservation. The next activity must still pass matcher eligibility and make sense for the child's actual next photo.

### 2.4 Parent Growth Path Impact

Parent-facing growth path is a windowed aggregate of completed activity events.

```mermaid
flowchart LR
    Session["Completed activity event"] --> Axis["progression.topic_axis\naxis row"]
    Session --> Rung["progression.difficulty_level\nrung evidence"]
    Session --> Hint["progression.next_step_hint\nsuggestion pool"]
    Session --> Angle["activity_signature.observation_angle\nangle split"]
    Session --> Mechanic["activity_signature.mechanic\nexploration matrix"]
    Session --> Role["activity_signature.entity_role\nsession timeline"]
    Session --> Skills["atl_skills + subject_tags\nthinking/domain distribution"]
    Session --> Support["caregiver_role\nsupport mix"]

    Axis --> Window["Selected parent window\nweek or month"]
    Rung --> Window
    Hint --> Window
    Angle --> Window
    Mechanic --> Window
    Role --> Window
    Skills --> Window
    Support --> Window

    Window --> Ladder["LxT ladder\ncurrent evidence per axis"]
    Window --> Curiosity["Curiosity profile\nconcept and angle distribution"]
    Window --> Matrix["Exploration matrix\nmechanic x angle"]
    Window --> TryHome["Try at home\nrecent viable hints"]
    Window --> Timeline["Session timeline\nrepresentative moments"]
    Window --> Gauges["Support gauges\ncaregiver role mix"]
```

One activity adds one event. It should not overwrite the growth path. If the next photo leads to a different axis, the parent dashboard should show both paths in the selected window.

---

## 3. Source Map

| Need | Source |
|---|---|
| Full field reference | `docs/activity_tag_block_progression_guide.md` |
| Activity-signature fields and scoring | `docs/plans/2026-04-23-activity-signature-design.md` |
| Progression algorithm | `docs/superpowers/specs/2026-04-24-progression-algorithm-design.md` |
| Progression axis contract | `docs/progression_axes.md` |
| Parent dashboard read contract | `docs/parent_growth_path_preview.html` |
