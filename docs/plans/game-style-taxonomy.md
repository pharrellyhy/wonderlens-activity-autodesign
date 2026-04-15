# Plan: Add Game Style Taxonomy to Activity Designs

## Context

**Problem**: The 17 Batch 2 designs (now in `designs/*_v2.md`) follow distinct interaction patterns, but there's no formal `game_style` field. Without it, we can't say "create a new activity for [entity] using [style]" and get a predictable structure. The 5 demo activities remain reference-only and are out of scope for this pass.

**What we're building**: A 6-style taxonomy added as a `Game Style` row in each v2 design's Basic Info table, plus a reference doc defining each style.

---

## Game Style Taxonomy (6 styles)

### Cat1 — In-Device Verbal (4 styles)

| Style | Child's role each round | Example prompt → response |
|-------|------------------------|--------------------------|
| `voice_acting` | Speaks/performs AS the object in a scenario | "Warm sun! Happy lion!" → child roars/says feeling |
| `storytelling_chain` | Adds what happens next in a narrative | "Chapter 2: banana hangs high..." → "It sees birds!" |
| `prediction_game` | Predicts what will happen given a cause | "Food flakes drop in water..." → "It swims up!" |
| `helper_hotline` | Decides what to do about a problem | "Kitchen full of smoke!" → "A mask!" |

### Cat5 — Out-of-Device Collection (2 styles)

| Style | Synthesis step | Example |
|-------|---------------|---------|
| `comparison_chart` | Collect → compare properties → chart/categorize | Playground: find equipment, name each one's "job" |
| `naming_story` | Collect → harvest entity-specific details per find → name as characters informed by those details → weave narrative FROM those details | Dandelion: find things, discover what each reminds you of, name characters, tell a detail-driven story |

---

## Design → Style Mapping

| Design | Style |
|--------|-------|
| lion_cat1 | `voice_acting` |
| crayons_cat1 | `voice_acting` |
| raincoat_cat1 | `voice_acting` |
| piano_cat1 | `voice_acting` |
| banana_cat1 | `storytelling_chain` |
| goldfish_cat1 | `prediction_game` |
| eye_cat1 | `prediction_game` |
| teddy_bear_cat1 | `helper_hotline` |
| firefighter_cat1 | `helper_hotline` |
| toothbrush_holder_cat1 | `helper_hotline` |
| playground_cat5 | `comparison_chart` |
| city_library_cat5 | `comparison_chart` |
| sunflower_cat5 | `comparison_chart` |
| stop_sign_cat5 | `comparison_chart` |
| green_apple_cat5 | `comparison_chart` |
| double_rainbow_cat5 | `naming_story` |
| sandy_beach_cat5 | `naming_story` |

---

## Implementation

### Step 1: Add `Game Style` row to each v2 design's Basic Info table

For each `designs/*_v2.md`, add a 7th row to the table:
```
| Game Style | voice_acting |
```

**Files**: all 17 `designs/*_v2.md` files

### Step 2: Update the concatenated doc

Regenerate `docs/WonderLens_Game_Designs_v2.md` from the updated individual files.

### Step 3: Create style reference doc (optional)

Write `docs/game_styles.md` documenting the 6 styles with:
- Name, category, description
- What the AI does each round
- What the child does each round
- Example designs

---

## Verification

1. All 17 v2 designs have a `Game Style` row in their Basic Info table
2. Every style in the mapping table appears at least once
3. `docs/WonderLens_Game_Designs_v2.md` matches individual files

---

## Critical Files

- `designs/*_v2.md` — 17 individual production designs (add Game Style row)
- `docs/WonderLens_Game_Designs_v2.md` — concatenated doc (regenerate)
- `docs/game_styles.md` — style reference (new, optional)
