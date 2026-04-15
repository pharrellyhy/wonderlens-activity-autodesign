# Plan: Transform Batch 2 Designs into Production Format

> **Status**: Pending | **Created**: 2026-03-18

## Context

**Problem**: Our auto-generated activity designs in `designs/` are detailed engineering specs (~200 lines, 12 metadata fields, dual warm/cold bridges, every round fully detailed, self-evaluation scorecard). The 教研 team expects a concise production format (~65 lines per activity) matching the reference at `docs/WonderLens_Game_Designs.md`.

**What we're building**: A `transform.md` instruction file + execution loop that condenses 17 Batch 2 designs into the production format — all in English, outputting to `docs/WonderLens_Game_Designs_v2.md`.

**Scope**: Batch 2 only (17 mapping-informed designs). Batch 1 excluded (pre-mapping, repetitive concepts).

---

## Key Decisions

- **Language**: English (NOT Chinese translation)
- **Step 1**: Cold start only (Step 1b) — drop warm start entirely
- **Output**: New file `docs/WonderLens_Game_Designs_v2.md` — all 17 designs concatenated
- **Scorecard**: Strip entirely (QA data lives in `results.tsv`)

---

## Transformation Rules

### A. Basic Info: Bullet list → Table (7 rows after taxonomy pass)

| Keep (reformat to table) | Drop |
|--------------------------|------|
| Activity Name | Trigger Entity |
| Activity Category | Trigger Scene |
| Recommended Tier | Mapping Source |
| Core IB Key Concepts | IB Theme (with weight) |
| Related Concepts | Dimension Anchors |
| ATL Skills Focus | Conversation Anchor Dimensions |

Base table format:
```
| Field | Value |
|-------|-------|
| Activity Name | The Banana Taste Test Show |
| Activity Category | Sustained Verbal Interaction (In-Device) |
| Recommended Tier | T1 (ages 4–6) |
| Core IB Key Concepts | Perspective, Responsibility |
| Related Concepts | Nutrition, Wellbeing, Preferences, Discovery |
| ATL Skills Focus | Thinking Skills (critical, creative), Communication Skills (expressing, listening) |
```

Post-taxonomy output adds:
```
| Game Style | storytelling_chain |
```

### B. Activity Overview: Keep all 4 sub-sections, light trim

- ① Brief Description — keep as-is
- ② Educational Purpose (KUD) — keep K/U/D structure, trim skill-mapping parentheticals
- ③ Design Highlight — keep as-is
- ④ Typical Scenario — keep as-is

### C. Interaction Flow: Structural condensation

| Source | Target | Rule |
|--------|--------|------|
| Step 1a (warm) | **DROP** | Remove entirely |
| Step 1b (cold) | Step 1: Transition Bridge | Use cold start content, single version |
| Step 2 | Step 2: Rule Introduction + Demo | Keep full detail |
| Step 3 (all rounds) | Step 3: Multi-Round Interaction | **Round 1 in full** (3 branches), subsequent rounds as 1-line summaries |
| Step 4 | Step 4: Celebration | Keep, compress |
| Step 5 | Step 5: Closing + IB Concepts | Keep full detail |
| Step 6 (cat5 only) | Merge into Step 4+5 | Cat5 6-step → 5-step |

### D. Dialogue format changes

| Source | Target |
|--------|--------|
| `> **AI says**: "*(tone)* text"` | `**AI says:** (tone) "text"` |
| `> **Possible child responses**:` | `**Child responses:**` |
| 3 branches always | 2-3 branches (drop "No response" if Step 4/5 celebration) |
| `> **AI follow-up**:` | `**AI follow-up:**` |
| Blockquote style (`>`) | Regular markdown (no blockquotes) |

### E. Screen descriptions: Compress to 1 sentence

- Source: 3-5 sentences with animation specifics, interactive feedback, state changes
- Target: 1 sentence capturing the key visual concept
- Example: "Teddy bear photo with a yawning mouth overlay. Background dims gradually..." → "Teddy bear photo centered with sleepy night-sky background and gentle star animations."

### F. Scorecard: Strip entirely

Remove everything after the final step's `---` separator.

---

## Files to Create

### 1. `transform.md` (NEW)
Agent instruction file encoding all transformation rules above, with:
- The reference format as a style guide (point to `docs/WonderLens_Game_Designs.md`)
- Exact field mapping table
- Round condensation examples (full → summary)
- Screen description compression examples
- 2-3 before/after examples showing source → target

### 2. `transform_run.md` (NEW)
Execution loop for the transform agent:
1. Read `transform.md` (rules)
2. Read reference doc (style calibration)
3. For each design in `transform_assignments.md`:
   a. Read source from `designs/[name].md`
   b. Apply transformation rules
   c. Self-check: table format? single Step 1? condensed rounds? 1-sentence screens? no scorecard?
   d. Append to `docs/WonderLens_Game_Designs_v2.md`
   e. Mark complete

### 3. `transform_assignments.md` (NEW)
Checklist of 17 Batch 2 designs to transform:
```
- [ ] banana_cat1.md
- [ ] goldfish_cat1.md
- [ ] lion_cat1.md
- [ ] crayons_cat1.md
- [ ] piano_cat1.md
- [ ] teddy_bear_cat1.md
- [ ] toothbrush_holder_cat1.md
- [ ] eye_cat1.md
- [ ] firefighter_cat1.md
- [ ] raincoat_cat1.md
- [ ] city_library_cat5.md
- [ ] playground_cat5.md
- [ ] green_apple_cat5.md
- [ ] double_rainbow_cat5.md
- [ ] sandy_beach_cat5.md
- [ ] sunflower_cat5.md
- [ ] stop_sign_cat5.md
```

### 4. `docs/WonderLens_Game_Designs_v2.md` (NEW — output)
The concatenated production document. Header + 17 activity sections separated by `---`.

---

## Implementation Sequence

```
1. transform.md (NEW)              — rules + examples
2. transform_run.md (NEW)          — execution loop
3. transform_assignments.md (NEW)  — work queue
4. Run transform loop              — 17 designs → v2.md
5. Verify output quality
```

Steps 1-3 can be done in one pass. Step 4 should write each transformed design to its own `designs/*_v2.md` file first, then regenerate the concatenated doc in a single ordered pass to avoid output races.

---

## Verification

1. **Format check**: Every activity in v2.md has table Basic Info (7 rows including `Game Style`), single Step 1, condensed Step 3, 1-sentence screens, no scorecard
2. **Content preservation**: KUD, concepts, ATL skills, closing concept naming all preserved
3. **Line count**: Each activity should be ~60-80 lines (vs ~200 in source)
4. **Reference comparison**: First 2 transforms should be visually compared against the reference doc style

---

## Critical Files

- `docs/WonderLens_Game_Designs.md` — reference format to match
- `designs/*_cat*.md` — 17 Batch 2 source files
- `program.md` — source format spec (Phase 2)
- `results.tsv` — QA data (replaces stripped scorecard)
