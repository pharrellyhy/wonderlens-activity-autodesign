# Run Instructions — Autonomous Design Loop

> This file tells the agent how to execute. Read this AFTER reading `program.md`.

## Setup (one-time, do this first)

1. Read `program.md` fully — this is your skill file containing all constraints, format, rubric, and seed exemplars.
2. Read `templates.md` fully — this contains the structural skeletons for each activity category, including game style sub-patterns.
3. Read `docs/game_styles.md` — this is the game style taxonomy reference (6 styles with examples).
4. Read `entity_guidance.md` fully — this teaches you how to read and use entity mapping YAML files.
5. Read `conversation_bridge.md` fully — this defines warm/cold start bridge patterns.
6. Read `assignments.md` — this is your work queue.
7. Verify `designs/` directory exists. Create it if not.
8. Verify `results.tsv` exists and has the current header. If it is missing, create it with this header:

```
assignment	entity	category	tier	status	d1_tech	d2_hook	d3_transition	d4_edge	d5_ib	d6_tier	d7_dialogue	d8_screen	d9_mapping	filename	timestamp
```

9. Confirm setup is complete, then say: "Setup complete. [N] assignments pending. Starting design loop."

## The Loop (repeat for every uncompleted assignment)

For each assignment in `assignments.md` that is marked `- [ ]` (not yet completed):

### Step 1: Parse the assignment

Extract: entity, category, tier, style (if provided), scene (if provided), mapping (if provided), start type (if provided). If tier is not specified, infer it per program.md rules. If style is not specified, infer it per program.md §1.6 rules. If scene is not specified, invent one.

### Step 1.5: Load entity mapping (if `mapping=` is specified)

1. Read `data/mappings_dev20_0318/_index.yaml` → find the entity_id → get the YAML file path
2. Read the YAML file → locate the entity block matching the entity_id
3. Extract for the target tier:
   - `primary_theme` and `secondary_themes` (with weights)
   - `primary_key_concepts` and `secondary_key_concepts` (with relevance scores)
   - `candidate_related_concepts`
   - `tier_guidance.[target_tier].dimensions` — all available dimensions
4. Select 2–3 **anchor dimensions** per entity_guidance.md §6:
   - Cat 1: engagement-first (emotions/imagination/narrative/reasoning + 1 physical)
   - Cat 5: physical-first (appearance/structure/senses + 1 engagement)
5. Select Key Concepts per entity_guidance.md §2 (primary first, anti-repetition guard)
6. Select IB theme per entity_guidance.md §3 (from mapping themes)
7. Select Related Concepts per entity_guidance.md §4 (at least 2 from mapping)

If no `mapping=` parameter, skip this step entirely and proceed as before.

### Step 2: Load the category template + game style + dimension anchoring

Read the matching template from `templates.md` (Template A for Category 1, Template B for Category 5). Use the step skeleton as scaffolding. Also read the **Game Style Sub-Patterns** section for the assigned style — this constrains the game mechanic, scenario type, escalation axis, and synthesis type.

**If mapping-informed**: Use the Dimension Anchoring section in the template to connect your anchor dimensions to creative variables. Brainstorm creative variables that are grounded in the mapping data — metaphor and role are still your invention, but vocabulary, facts, and sensory details must trace to mapping attributes. The game style sub-pattern further constrains which creative variables are appropriate.

**If not mapping-informed**: Brainstorm fresh creative variables using the Quick Entity Brainstorm Guide as inspiration, constrained by the game style sub-pattern.

### Step 3: Generate the activity design

Follow the EXACT output format from program.md Phase 2. Be thorough. Do not abbreviate. Every step needs full dialogue, 3 response branches, and screen descriptions.

**If mapping-informed and `start=warm+cold`**: Generate BOTH Step 1a (warm start) and Step 1b (cold start) per conversation_bridge.md §4. Steps 2+ are shared and must work for both entry paths. Verify convergence: both bridges lead naturally into Step 2.

**If not mapping-informed**: Generate Step 1 as before (cold start only).

### Step 4: Self-evaluate

Run through all 9 rubric dimensions from program.md Phase 3. If any dimension FAILS:
- Identify the specific issue
- Fix it in the design
- Re-evaluate
- Repeat until all dimensions PASS

**Note**: Dimension 9 (Entity Mapping Alignment) only applies to mapping-informed designs. Score as N/A if no mapping.

### Step 5: Save the design

Save the completed design to `designs/[entity]_[category_number].md`

Example filenames: `designs/toy_dinosaur_cat1.md`, `designs/dandelion_cat5.md`

### Step 6: Log the result

Append a row to `results.tsv`:

```
[full assignment text]\t[entity]\t[category]\t[tier]\t[PASS/FAIL]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F/N]\t[filename]\t[ISO timestamp]
```

Column order: assignment, entity, category, tier, status, d1_tech, d2_hook, d3_transition, d4_edge, d5_ib, d6_tier, d7_dialogue, d8_screen, d9_mapping, filename, timestamp.

For d9_mapping: use P (pass), F (fail), or N (N/A — no mapping).

If you upgraded an older `results.tsv` that lacks `d9_mapping`, first add the column to the header and backfill `N` for earlier non-mapping rows before appending new results.

### Step 7: Mark assignment complete

In `assignments.md`, change `- [ ]` to `- [x]` for this assignment.

### Step 8: Commit

```bash
git add designs/ results.tsv assignments.md
git commit -m "Design: [entity] + cat[N] — ALL PASS"
```

### Step 9: Next assignment

Move to the next `- [ ]` assignment. If none remain, say: "All assignments complete. [N] designs generated. See results.tsv for summary."

## Important Rules

- **Never skip steps.** Every design must be complete before saving.
- **Never abbreviate later designs** because "they follow the same pattern." Each design is fully independent.
- **If you encounter an error** (e.g., can't write a file), report it and continue with the next assignment.
- **Commit after EVERY completed design**, not in batches. This is the ratchet — work is never lost.
- **Quality over speed.** Take as many self-evaluation rounds as needed. A design that passes all 9 dimensions on the second try is better than a design that was rushed and would fail review.
