# Shared Clue Scavenger Hunt -- Authoring Spec

> Category 5 (Collection/Tracking Exploration) . Parameterized match pattern . Mechanic: `collect`

## Premise

After a child photographs an object with a clear feature, the AI turns that feature into a "shared clue" mission. The child becomes a Shared Clue Scout and finds three more things that match the same clue: a color, shape, material, function, or simple category. Each find earns a photo slot. At the end, the child names one extra thing the finds have in common, so the collection becomes more than "three things" -- it becomes evidence for a rule the child can explain.

## Target

- **Primary tier:** T1 (ages 4-6)
- **Activity category:** Cat5, out-of-device collection/tracking
- **Mechanic:** `collect`
- **Parameterized trigger:** any photographed entity with a runtime-resolvable or child-confirmed shared feature
- **Entity role:** exemplar; the starting photo becomes the first example of a broader hunt
- **Progression axis:** Connection, level 2

## Adaptation Rationale

- **Input mode:** parameterized.
- **Core promise:** preserve the source Scavenger Hunt loop: find several things that share a feature, then generalize the shared rule.
- **Canonical mechanic:** `collect`; Step 3's repeated child action is find, photograph, and add an item that matches the shared clue.
- **Readiness:** ready_to_generate.
- **Trigger condition:** child photographs an object with a clear color, shape, or category feature.
- **Mapping use:** no entity mapping is required. The package uses runtime placeholders and does not claim entity-specific facts.
- **Asset dependency:** `no_assets`; no asset brief is needed.
- **Product capability flags:** none.
- **Scaffold fit:** strong. Adventure / `quest_collector` supports a purposeful hunt with a visible progress trail and a synthesis moment.
- **Assumptions:** runtime can suggest or confirm a broad clue such as `{shared_feature}`. Cross-photo similarity is handled conversationally and by independent photo reactions, not by computational before/after comparison.

## Selection Trigger

Start this activity when the matcher or conversation layer has one safe shared feature to use as the collection rule:

- `{matched_color}` such as red, blue, green, yellow, black, or white.
- `{matched_shape}` such as round, pointy, long, flat, or square.
- `{matched_material}` such as wood, metal, paper, plastic, cloth, or leaf-like.
- `{entity_class}` or simple category such as toy, plant, food, tool, or vehicle.

If runtime cannot infer a feature, the AI can ask the child to choose: "Should we hunt for the same color, same shape, or same kind of thing?"

## Experience Pillar & Game Style

- **Pillar:** Adventure
- **Game style:** `quest_collector`
- **Why this scaffold:** the child completes a purposeful quest, watches a three-slot trail fill up, and earns a badge by explaining the hidden connection among the finds.

## Self-Evaluation Scorecard

Evaluated against `prod.md`, `tag_block.yaml`, `program.md` Phase 3, and `templates.md` Adventure + Cat5 rules.

| # | Dimension | Score | Notes |
|---|-----------|-------|-------|
| 1 | V1 Technical Compliance | PASS | The activity uses independent photos plus dialogue. It does not require OCR, face/expression/pose detection, IMU sensing, non-speech audio detection, or before/after state comparison. |
| 2 | Hook & Transition | PASS | Step 1 opens with delight about the starting object and its shared clue, then pivots naturally into finding more examples. |
| 3 | Edge Case Coverage | PASS | Every dialogue step includes ideal, unexpected, and no-response branches with 2s waits; Step 3 includes stuck and not-a-match handling. |
| 4 | IB Completeness | PASS | Form and Connection are named, KUD is specific, related concepts and ATL skills are present, and the closing ties the child's collecting and rule naming to the concepts. |
| 5 | Tier Appropriateness | PASS | T1 children find three examples, answer short prompts, and name one extra commonality; spoken AI lines were tightened after review to use short, concrete sentences. |
| 6 | Dialogue Specificity | PASS | AI lines are spoken dialogue with tone markers; no runtime beat relies on abstract narrator instructions. |
| 7 | Screen & UI Completeness | PASS | Every step includes concrete screen states: shared-clue glow, mission card, three photo slots, clue meter, connection web, and badge. |
| 8 | Entity Mapping Alignment | N/A | Parameterized match-pattern package with no `mapping=` assignment and no entity-specific mapping claims. |
| 9 | Game Feel | PASS | The matching verdicts, 0-of-3 progress trail, and final "extra connection" reveal create uncertainty, stakes, and a replayable quest. |
| 10 | Mechanic Fidelity + Scaffold Honesty | PASS | `collect` is preserved in the Step 3 loop and tag block; Adventure / `quest_collector` frames the mission without changing the child action. |

**Overall**: ALL PASS -- one reviewer issue found and fixed: T1 spoken dialogue was shortened while preserving the collect loop.
