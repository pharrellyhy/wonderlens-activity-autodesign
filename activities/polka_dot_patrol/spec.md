# Pattern Patrol - Authoring Spec

> Category 5 (Collection/Tracking Exploration) · Reusable property-target pattern catalog · First catalogs: `polka_dots`, `stripes`

## Premise

The child becomes a Pattern Patrol Officer. The runtime supplies a matched pattern property, such as `polka_dots` or `stripes`, and the child chooses three catalog cards that show that pattern. Each round asks the child to name the evidence they see: dots, spots, circles, lines, bands, or stripes. At synthesis, the child compares how the same pattern looks different across the selected cards, gives the cards playful names, and sends the pattern team on a tiny patrol parade.

The canonical package ID remains `polka_dot_patrol` because the original exemplar and first catalog set are polka dots. The machine-readable contract is broader: this is a reusable `property_target` pattern package with approved catalog sets.

## Target

- **IB axis:** Form (primary, via pattern as a property) + Connection (secondary, via the link between unrelated things that share a visual signature)
- **Primary rung:** T1 (ages 4-6)
- **Tier elasticity:** T0-T2 (+/-1)
- **Age tier:** child can look closely, choose matching catalog cards, and explain how one pattern differs across examples.

## Pedagogical Rationale

Pattern is an observable property that sits on an object rather than being the object itself. This activity makes the child zoom in on the pattern property: dots can be big circles or tiny speckles, and stripes can be thick bands or thin lines. The same-but-different comparison is the core move for **Form**, and connecting unrelated cards through one pattern builds **Connection**.

The patrol role keeps the activity playful while the catalog-card contract keeps the current demo honest. The demo does not claim to verify arbitrary camera photos. The child chooses from approved visible cards and explains the pattern evidence out loud.

## Selection Trigger

Use when the handoff includes an approved pattern property with a supported catalog set.

Supported initial `property_target` values:

- `polka_dots`
- `stripes`

Invalid when:

- no pattern property is supplied;
- the supplied pattern property has no approved catalog set;
- the runtime would need to judge arbitrary real-camera photos for pattern correctness.

## Experience Pillar & Game Style

- **Pillar:** Adventure
- **Game style:** `quest_collector`
- **Mechanic:** `collect`
- **Observation angle:** `pattern`
- **Entity role:** `exemplar`

## Demo Source Migration Notes

This conversion changes the demo runtime from open-world photo verification to supported catalog collection. The old polka-dot hunt remains the first catalog set and child-facing exemplar, but the package now also includes stripes to prove the `property_target` contract. If production camera-based pattern verification becomes available later, it can be added as a separate degraded or production-supported path; this package should not imply that current demo behavior can inspect arbitrary photos.

## Asset Brief

| asset_id | asset_type | requiredness | generation_timing | use_step | display_location | purpose | prompt_en/source | display_behavior | fallback_behavior | safety_constraints |
|---|---|---|---|---|---|---|---|---|---|---|
| `activity_icon` | icon | required | pre_generated | package preview | preview slot | Represent Pattern Patrol before play. | See `asset_manifest.yaml`. | Show centered Pattern Patrol icon. | Use text-only title if unavailable. | No text baked into image. |
| `intro_scene` | scene_background | required | pre_generated | Step 1 | round screen | Introduce the pattern clue. | See `asset_manifest.yaml`. | Show child noticing a pattern clue. | Use neutral pattern background. | No readable labels. |
| `rules_scene` | scene_background | required | pre_generated | Step 2 | round screen | Explain choosing three matching catalog cards. | See `asset_manifest.yaml`. | Show catalog-card selection motif without baked UI. | Explain rule by voice only. | No baked buttons or slots. |
| `round_1_scene` | scene_background | required | pre_generated | Step 3 Round 1 | round screen | Support first card choice. | See `asset_manifest.yaml`. | Show first patrol choice moment. | Continue with item cards only. | No readable labels. |
| `round_2_scene` | scene_background | required | pre_generated | Step 3 Round 2 | round screen | Support second card choice. | See `asset_manifest.yaml`. | Show comparison between two pattern examples. | Continue with item cards only. | No readable labels. |
| `round_3_scene` | scene_background | required | pre_generated | Step 3 Round 3 | round screen | Support final card choice. | See `asset_manifest.yaml`. | Show completing the three-card patrol set. | Continue with item cards only. | No readable labels. |
| `synthesis_scene` | scene_background | required | pre_generated | Step 4 synthesis | round screen | Support same/different comparison and parade payoff. | See `asset_manifest.yaml`. | Show a pattern parade with three selected cards. | Synthesize by voice only. | No baked app UI. |
| `celebrate_scene` | badge | required | pre_generated | Step 4 celebration | round screen | Celebrate Pattern Patrol completion. | See `asset_manifest.yaml`. | Show badge-style celebration art. | Use generic celebration treatment. | No readable badge text. |
| `closing_scene` | scene_background | required | pre_generated | Step 5 | round screen | Close with Form + Connection. | See `asset_manifest.yaml`. | Show pattern memories grouped together. | Close with spoken recap only. | No readable labels. |
| `polka_ladybug`, `polka_mushroom`, `polka_flower` | card_set | required | pre_generated | Step 3 | catalog grid | Correct choices for `polka_dots`. | See `asset_manifest.yaml`. | Show as selectable catalog item cards. | Remove the item and keep remaining approved cards. | One centered subject per file. |
| `stripe_sock`, `stripe_scarf`, `stripe_ball` | card_set | required | pre_generated | Step 3 | catalog grid | Correct choices for `stripes`. | See `asset_manifest.yaml`. | Show as selectable catalog item cards. | Remove the item and keep remaining approved cards. | One centered subject per file. |
| `plain_leaf`, `zigzag_block` | card_set | optional | pre_generated | Step 3 | catalog grid | Distractors for catalog collection. | See `asset_manifest.yaml`. | Show as optional non-target cards when the demo supports distractors. | Hide distractors if unavailable. | One centered subject per file. |

## Asset Usage Timeline

| asset_id | timing | load/generate moment | first display | visible range | location | interaction/use | persistence/hide behavior | fallback |
|---|---|---|---|---|---|---|---|---|
| `activity_icon` | pre_generated | Before package selection. | preview | preview only | preview slot | Identifies Pattern Patrol. | Hidden once play starts. | Text-only package title. |
| `intro_scene` | pre_generated | Before Step 1. | Step 1 | Step 1 | round screen | Supports pattern-clue hook. | Replaced by rules scene. | Spoken hook plus neutral background. |
| `rules_scene` | pre_generated | Before Step 2. | Step 2 | Step 2 | round screen | Explains picking matching cards. | Replaced by round scene. | Spoken rule only. |
| `round_1_scene` | pre_generated | Before Step 3. | Step 3 Round 1 | Round 1 | round screen | Frames first catalog choice. | Replaced by Round 2 scene. | Item cards remain selectable. |
| `round_2_scene` | pre_generated | Before Step 3. | Step 3 Round 2 | Round 2 | round screen | Frames second catalog choice and comparison. | Replaced by Round 3 scene. | Item cards remain selectable. |
| `round_3_scene` | pre_generated | Before Step 3. | Step 3 Round 3 | Round 3 | round screen | Frames final catalog choice. | Replaced by synthesis scene. | Item cards remain selectable. |
| `synthesis_scene` | pre_generated | Before Step 4. | Step 4 | Step 4 synthesis | round screen | Supports three-card comparison and parade story. | Replaced by celebration scene. | Spoken synthesis only. |
| `celebrate_scene` | pre_generated | Before Step 4. | Step 4 celebration | Step 4 celebration | round screen | Awards Pattern Patrol. | Replaced by closing scene. | Generic celebration. |
| `closing_scene` | pre_generated | Before Step 5. | Step 5 | Step 5 | round screen | Closes with Form + Connection. | End of activity. | Spoken closing only. |
| catalog item cards | pre_generated | Before Step 3. | Step 3 Round 1 | Step 3 and synthesis | catalog grid / selected-card row | Child selects cards and explains pattern evidence. | Selected cards persist through synthesis. | Hide unavailable cards; do not start if fewer than three correct cards exist for target property. |

## Extensibility Notes

- Runtime slot `{target_pattern_property}` selects the supported pattern property.
- Runtime slot `{pattern_label}` renders child-facing wording such as `polka dots` or `stripes`.
- Runtime slot `{collection_catalog_id}` selects approved cards for that property.
- Add new pattern sets only when at least three correct catalog cards and honest child evidence prompts exist.
- Do not mark arbitrary camera-photo pattern judgment as supported until the product has a verified visual judgment path.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, and `templates.md` Adventure + Cat5 rules.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The demo uses approved catalog cards and child-stated evidence. It does not claim arbitrary camera-photo pattern verification, OCR, face/pose, IMU, or state-change detection. |
| 2 | Hook & Transition | PASS | Step 1 grows from a target pattern clue into a patrol mission without a sudden quiz. |
| 3 | Edge Case Coverage | PASS | Each step has ideal, unexpected, and no-response branches tied to catalog selection or pattern explanation. |
| 4 | IB Completeness | PASS | Form + Connection are named in metadata, KUD, synthesis, and closing. |
| 5 | Tier Appropriateness | PASS | T1 children choose concrete cards, use visible pattern words, and compare same/different features. |
| 6 | Dialogue Specificity | PASS | Dialogue names target pattern evidence, card selection behavior, comparison, naming, and parade payoff. |
| 7 | Screen & UI Completeness | PASS | The package defines scene assets, catalog cards, selected-card persistence, synthesis, badge, and fallback behavior. |
| 8 | Entity Mapping Alignment | N/A | This is a parameterized pattern-property package, not a mapping-informed entity package. |
| 9 | Game Feel | PASS | The patrol mission has visible progress, card choice, comparison, creative naming, and a final parade story. |
| 10 | Pillar Fidelity | PASS | Adventure/quest_collector remains honest: the child collects matching evidence and completes a playful patrol. |

**Overall**: ALL PASS.
