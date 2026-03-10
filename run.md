# Run Instructions — Autonomous Design Loop

> This file tells the agent how to execute. Read this AFTER reading `program.md`.

## Setup (one-time, do this first)

1. Read `program.md` fully — this is your skill file containing all constraints, format, rubric, and seed exemplars.
2. Read `templates.md` fully — this contains the structural skeletons for each activity category.
3. Read `assignments.md` — this is your work queue.
3. Verify `designs/` directory exists. Create it if not.
4. Verify `results.tsv` exists. If not, create it with this header:

```
assignment	entity	category	tier	status	d1_tech	d2_hook	d3_transition	d4_edge	d5_ib	d6_tier	d7_dialogue	d8_screen	filename	timestamp
```

5. Confirm setup is complete, then say: "Setup complete. [N] assignments pending. Starting design loop."

## The Loop (repeat for every uncompleted assignment)

For each assignment in `assignments.md` that is marked `- [ ]` (not yet completed):

### Step 1: Parse the assignment

Extract: entity, category, tier, scene (if provided). If tier is not specified, infer it per program.md rules. If scene is not specified, invent one.

### Step 2: Load the category template

Read the matching template from `templates.md` (Template A for Category 1, Template B for Category 5). Use the step skeleton as scaffolding, brainstorm fresh creative variables for this entity using the Quick Entity Brainstorm Guide as inspiration.

### Step 3: Generate the activity design

Follow the EXACT output format from program.md Phase 2. Be thorough. Do not abbreviate. Every step needs full dialogue, 3 response branches, and screen descriptions.

### Step 4: Self-evaluate

Run through all 8 rubric dimensions from program.md Phase 3. If any dimension FAILS:
- Identify the specific issue
- Fix it in the design
- Re-evaluate
- Repeat until all 8 PASS

### Step 5: Save the design

Save the completed design to `designs/[entity]_[category_number].md`

Example filenames: `designs/toy_dinosaur_cat1.md`, `designs/dandelion_cat5.md`

### Step 6: Log the result

Append a row to `results.tsv`:

```
[full assignment text]\t[entity]\t[category]\t[tier]\t[PASS/FAIL]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[P/F]\t[filename]\t[ISO timestamp]
```

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
- **Quality over speed.** Take as many self-evaluation rounds as needed. A design that passes all 8 dimensions on the second try is better than a design that was rushed and would fail review.
