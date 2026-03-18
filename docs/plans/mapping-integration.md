# Plan: Integrate Entity Mappings into Activity Design System

> **Status**: In Progress | **Created**: 2026-03-18

## Context

**Problem**: The activity design agent brainstorms from scratch for every entity. This causes:
- Key Concept repetition (9/10 Batch 1 designs used Connection; all Cat 5 used Form+Connection)
- No connection to the preceding conversation phase (in the real app, a multi-turn conversation using tier_guidance happens BEFORE the activity)
- Tier-appropriate content is guessed, not grounded in entity-specific attributes

**What we're building**: A mapping-informed design workflow where the agent reads structured entity data (themes, concepts, tier attributes) and produces activities that feel like natural continuations of the conversation phase — with both "warm start" (post-conversation) and "cold start" (standalone) bridge versions.

**Source data**: 20 entity YAML files in `data/mappings_dev20_0318/`, each with theme weights, key concept relevance scores, and tier-specific dimension guidance.

---

## Files to Create

### 1. `entity_guidance.md` (NEW)

Teaches the agent how to read and use mapping YAML files:

- **§1 Schema reference**: Explain YAML structure (themes, key concepts, tier_guidance dimensions)
- **§2 Key Concept selection rules**:
  - MUST pick at least 1 concept from `primary_key_concepts` (relevance ≥ 0.8)
  - Second concept from primary or secondary
  - Anti-repetition: cannot default to Form+Connection without justification
- **§3 Theme alignment**: Activity's IB theme must come from the mapping's primary/secondary themes
- **§4 Related Concept sourcing**: At least 2 of 4 Related Concepts from `candidate_related_concepts`
- **§5 Tier guidance usage**: Pull vocabulary, facts, sensory details from tier-specific dimension attributes — don't invent them
- **§6 Dimension anchoring**: Select 2-3 "anchor dimensions" that supply the activity's core content
  - Cat 1: prefer engagement dimensions (emotions, imagination, narrative, reasoning) + 1 physical
  - Cat 5: prefer physical dimensions (appearance, structure, senses) + 1 engagement

### 2. `conversation_bridge.md` (NEW)

Defines conversation→activity transition logic and warm/cold start patterns:

- **§1 Conversation→Activity dimension mapping table**
- **§2 Warm Start bridge template** with 3-4 opener flavors
- **§3 Cold Start bridge** — current behavior preserved
- **§4 Dual-bridge requirement**: Every design includes Step 1a (warm) + Step 1b (cold); Steps 2+ shared

---

## Files to Modify

### 3. `program.md` — 4 targeted changes

| Change | Location | What |
|--------|----------|------|
| 3a | After §1.6 | Add §1.7 "Entity Mapping Data" — instructs agent to read entity YAML before designing |
| 3b | Phase 2 output format | Add `Mapping Source` and `Conversation Anchor Dimensions` to Basic Info; show Step 1a/1b dual format |
| 3c | Phase 3 rubric | Add **Dimension 9: Entity Mapping Alignment** |
| 3d | Appendix checklists | Add "Before Selecting Key Concepts" checklist |

### 4. `templates.md` — 3 changes

| Change | What |
|--------|------|
| 4a | Template A Step 1: add warm start variant pattern + source note |
| 4b | Template B Step 1: add warm start variant referencing physical dimensions |
| 4c | Both templates: add "Dimension Anchoring" section after Creative Variables table |

### 5. `run.md` — 5 changes

| Change | What |
|--------|------|
| 5a | Insert Step 1.5: Load entity mapping |
| 5b | Update Step 2: Incorporate mapping into template loading + dimension anchoring |
| 5c | Update Step 3: Require both Step 1a (warm) + Step 1b (cold) |
| 5d | Update Step 4: Self-evaluate against 9 dimensions (add D9) |
| 5e | Update results.tsv header: add `d9_mapping` column |

### 6. `assignments.md` — New Batch 2

Updated format with mapping= and start=warm+cold for remaining mapped entities.

---

## Implementation Sequence

```
1. entity_guidance.md (NEW)        — foundational, others reference it
2. conversation_bridge.md (NEW)    — defines warm/cold patterns
   ↓ (1 and 2 are independent of each other)
3. program.md (MODIFY)             — adds §1.7, format, D9, checklists
4. templates.md (MODIFY)           — adds warm start + dimension anchoring
   ↓ (3 and 4 are independent of each other)
5. run.md (MODIFY)                 — updated loop
6. assignments.md (MODIFY)         — Batch 2 work queue
   ↓ (5 and 6 are independent of each other)
7. Run Batch 2 design loop
```

---

## Verification

After implementation, verify by:
1. **Dry run 1 design manually**: Pick `banana + cat 1, mapping=food_banana` — check that the agent reads the YAML, selects concepts from mapping, grounds vocabulary in tier_1 attributes, produces both warm/cold bridges
2. **Concept diversity check**: After Batch 2, tally Key Concepts across all designs — should see 5+ distinct concepts (not just Form+Connection)
3. **Warm start quality**: Each warm bridge should reference a specific dimension topic from the mapping (not generic "we talked about it")
4. **Cold start regression**: Cold bridges should still pass Dimensions 1–8 unchanged; D9 adds mapping-specific checks only
5. **Mapping alignment (D9)**: Every design should PASS — concepts, themes, vocabulary traceable to mapping data
