# Plan: Redesign `naming_story` Game Style — Detail-Harvesting Into Story

## Context

The `naming_story` cat5 style currently says "collect → name as characters → weave narrative" but doesn't specify that **details harvested per entity should drive the narrative**. The Chinese reference Game 2 (石头花纹"故事创想家") shows the ideal: for each stone, the child interprets its visual pattern → names it from that interpretation → the story emerges organically from those detail-driven character identities.

Current naming_story designs either: don't name at all (double_rainbow, sandy_beach), name but story is generic (raincoat, crayons), or name but synthesis is actually classification/sorting (dandelion, autumn_leaf, pinecone).

**Goal**: Redesign the style definition + update all 9 naming_story designs so harvested details drive naming and story.

**Litmus test**: "If the child found different objects, would the story be different?" If yes → correct. If no → still generic.

---

## Phase 1: Update Style Definition

### File: `docs/game_styles.md` (lines 58-65)

Update `naming_story` entry:

```
### `naming_story`
- **Category**: Collection/Tracking Exploration (Out-of-Device)
- **Synthesis step**: Collect → harvest entity-specific details per find → name as characters informed by those details → weave narrative FROM those details
- **What the AI does**: Per find, asks 1-2 detail questions (what does it look/feel/remind you of?). Helps child name each find as a character whose name reflects the harvested detail. At synthesis, scaffolds a narrative where each character's role is constrained by the detail that birthed its name.
- **What the child does**: Per find: observes a specific detail, interprets it, names the find as a character. At synthesis: co-creates a story featuring those characters using their detail-driven identities.
- **Detail type varies by entity**: Visual/sensory (feather texture, stone pattern), functional (raincoat protection style), imaginative (puddle reflections, cloud shapes)
- **Tier-appropriate depth**:
  - T0: 1 detail question per find + 1 story prompt → AI narrates incorporating child's details
  - T1: 1-2 detail questions per find → child names story title → child co-creates 2-3 sentence narrative with AI scaffolding
```

Update Style Distribution table (line 78): naming_story count from 2 → 9, list all entities.

### File: `docs/plans/game-style-taxonomy.md` (line 27)

Update the naming_story row in the Cat5 table to match.

### File: `templates.md` (lines 329-335)

Update the `naming_story` sub-pattern:
- Add **Per-Find Detail Harvesting** requirement
- Add synthesis constraint: "Story must reference at least 2 character-specific details"
- Add examples of detail types (visual, functional, imaginative)

Update Quick Entity Brainstorm Guide (lines 354-358):
- Dandelion: change from CLASSIFICATION to NAMING + NARRATIVE
- Pinecone: change from PATTERN to NAMING + NARRATIVE
- Autumn leaf: change from CLASSIFICATION to NAMING + NARRATIVE
- Feather: already NAMING, add detail-harvesting note
- Puddle: already NARRATIVE, add per-find naming note

---

## Phase 2: Gold Standard Rewrites

### dandelion_cat5.md (T1 gold standard)

**Current problem**: Synthesis is sorting into Round Team vs Fluffy Team (comparison_chart behavior).

**Key changes**:
- Step 2: Mission shifts from "find round/fluffy things" to "find interesting things, we'll discover what each one reminds you of, name them, and make up a story"
- Step 3: Per find, replace binary "round or fluffy?" with open-ended "what does it remind you of?" → child names from their interpretation → AI connects name to narrative role
- Step 4: Replace sorting into teams with story co-creation: "Your characters are ready! What adventure do [Name 1], [Name 2], and [Name 3] have together?"
- KUD: Update D (Do) from classification/sorting to creative interpretation + narrative co-creation

### raincoat_cat5_prod.md + raincoat_cat5_spec.md (T0 gold standard)

**Current problem**: Story is generic "they all protect together" — not driven by per-find details.

**Key changes**:
- Step 3: Per find, add ONE detail question: "How does it protect? Is it big? Strong? Soft?" → naming informed by detail → AI gives character a trait: "Big Leafy the bunny blanket!"
- Step 4: AI narrates story using specific details: "Rain is coming! Raincoat goes swish-swish and covers YOU. Big Leafy spreads out and covers a tiny bunny. Roofie stands tall and keeps everyone underneath dry!"
- Each character's action in the story comes from their specific detail, not a generic "they protect"

> **Note**: User specified dandelion as T0 and raincoat as T1, but currently dandelion=T1 and raincoat=T0. Will confirm tier assignments during execution.

---

## Phase 3: Remaining 7 Designs

Each gets the same structural transformation. Ordered by proximity to correct pattern (easiest first):

| # | Design | File | Current Gap | Detail Type |
|---|--------|------|-------------|-------------|
| 1 | puddle | `designs/puddle_cat5.md` | Closest — has "what do portals whisper?" but no per-find naming | Imaginative: what world does each reflection show? |
| 2 | sandy_beach | `designs/sandy_beach_cat5_prod.md` | Has origin questions but no naming/story | Origin + texture: where from, what does it feel like? |
| 3 | feather | `designs/feather_cat5.md` | Has collective team naming but not per-entity | Sensory: texture, lightness, what it reminds you of |
| 4 | crayons | `designs/crayons_cat5_prod.md` + `_spec.md` | Names but thin story | Visual: what does the color remind you of? |
| 5 | double_rainbow | `designs/double_rainbow_cat5_prod.md` | Full rewrite needed — currently color sorting | Imaginative: what does each color remind you of? |
| 6 | autumn_leaf | `designs/autumn_leaf_cat5.md` | Full rewrite — currently color gradient sorting | Visual/imaginative: what does each warm thing look like? |
| 7 | pinecone | `designs/pinecone_cat5.md` | Full rewrite — currently pattern classification | Visual/imaginative: what does each pattern look like? |

**Per-design changes** (same for all):
1. Step 3: Replace classification/binary questions with detail-harvesting questions + naming
2. Step 4: Replace sorting/classification synthesis with storytelling synthesis
3. Sections B.1, B.3, B.4: Update to reflect naming_story structure
4. KUD B.2: Update D (Do) to include detail-driven naming + co-created narrative

---

## Verification

For each rewritten design, check:
- [ ] Step 3 asks at least one open-ended detail question per find (not binary yes/no)
- [ ] Naming flows from child's answer to the detail question
- [ ] Synthesis narrative references at least 2 character-specific details
- [ ] Synthesis is a narrative, NOT a sort/classify/pattern-find
- [ ] Tier-appropriate: T0=1 detail Q + AI narrates; T1=1-2 detail Qs + child co-creates
- [ ] Self-evaluation scorecard still passes all 8 dimensions
- [ ] Litmus test: "If child found different objects, would the story be different?" → Yes

### Files modified (complete list)

**Style definition (3 files)**:
- `docs/game_styles.md`
- `docs/plans/game-style-taxonomy.md`
- `templates.md`

**Gold standards (3 files)**:
- `designs/dandelion_cat5.md`
- `designs/raincoat_cat5_prod.md`
- `designs/raincoat_cat5_spec.md`

**Remaining designs (8 files)**:
- `designs/puddle_cat5.md`
- `designs/sandy_beach_cat5_prod.md`
- `designs/feather_cat5.md`
- `designs/crayons_cat5_prod.md`
- `designs/crayons_cat5_spec.md`
- `designs/double_rainbow_cat5_prod.md`
- `designs/autumn_leaf_cat5.md`
- `designs/pinecone_cat5.md`
