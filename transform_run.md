# Transform Execution Loop

## Setup

1. Read `transform.md` for all transformation rules
2. Read `docs/WonderLens_Game_Designs.md` for reference style calibration
3. If rerunning from scratch, reset `docs/WonderLens_Game_Designs_prod.md` to just the header before regenerating it
4. Treat `transform_assignments.md` as a progress tracker only; do not use checked boxes to skip regeneration of the final concatenated doc

## Per-Design Loop

For each design in `transform_assignments.md`, in file order:

### 1. Read Source
Read `designs/[entity]_cat[N]_spec.md` (engineering spec)

### 2. Apply Transformations
Apply all rules from `transform.md`:
- A: Basic Info bullet list → 7-row table including `Game Style` (drop trigger/mapping fields, strip Chinese, simplify category)
- B: Activity Overview — keep 4 sub-sections, light trim of KUD parentheticals
- C: Interaction Flow — drop Step 1a, use Step 1b as Step 1, keep Step 2, condense Step 3 (Round 1 full, rest as 1-line summaries), compress Step 4, keep Step 5. For cat5: merge 6 steps → 5 steps.
- D: Dialogue format — no blockquotes, simplified tone markers, 2-3 branches
- E: Screen descriptions — compress to 1 sentence each
- F: Strip scorecard entirely
- G: Use `## Activity Name` header (no "Activity:" prefix)

### 3. Self-Check
Before writing, verify:
- [ ] Basic Info is a 7-row table (Activity Name, Activity Category, Recommended Tier, Core IB Key Concepts, Related Concepts, ATL Skills Focus, Game Style)
- [ ] No Chinese text anywhere
- [ ] Single Step 1 (cold start only, no Step 1a/1b split)
- [ ] Step 3 has Round 1 in full, subsequent rounds as 1-line summaries
- [ ] All screen descriptions are 1 sentence
- [ ] No scorecard section
- [ ] No blockquotes in dialogue
- [ ] 5 steps total (not 6)
- [ ] Activity header is `## Name` (not `## Activity: Name`)

### 4. Write Individual Output
Write the transformed result to `designs/[entity]_cat[N]_prod.md`.

### 5. Mark Complete
Update the checkbox in `transform_assignments.md`: `- [ ]` → `- [x]`

## Final Regeneration

After all individual `designs/*_prod.md` files are ready, rebuild `docs/WonderLens_Game_Designs_prod.md` once in assignment order. Do not have multiple agents append to the same output file.

## Batch Processing

Multiple agents can transform separate source files in parallel, but only one ordered regeneration pass should write `docs/WonderLens_Game_Designs_prod.md`.
