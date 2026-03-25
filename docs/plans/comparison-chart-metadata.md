# Plan: Comparison_Chart Metadata Unification

## Context

The naming_story redesign is complete — all 9 entities now have prod+spec files with detail-harvesting (v2.0) and `Design Version` / `Last Updated` metadata. The 5 comparison_chart designs are working correctly and don't need a redesign. However, they lack the version metadata that naming_story files now have.

**Goal**: Add version metadata to all comparison_chart cat5 designs for consistency across the full cat5 design set.

**Decision**: comparison_chart designs stay as-is (no reclassification, no redesign). They pass their own litmus test: child's unique finds lead to different sorting outcomes.

---

## Step 1: Write this plan to `docs/plans/`

Save this plan as `docs/plans/comparison-chart-metadata.md` before executing.

## Step 2: Identify all comparison_chart files

Known comparison_chart designs (5 entities):
- playground
- city_library
- sunflower
- stop_sign
- green_apple

Need to check which have `_prod.md`, `_spec.md`, or both.

## Step 3: Add metadata to each file

Add after the `Game Style` line in each file:
- `Design Version`: `1.0` (original design, no redesign)
- `Last Updated`: date of their last substantive change (check git log per file)

Two formats:
- **TABLE** (`| Field | Value |`): add `| Design Version | 1.0 |` and `| Last Updated | YYYY-MM-DD |` rows
- **LIST** (`- **Field**:`): add `- **Design Version**: 1.0` and `- **Last Updated**: YYYY-MM-DD` items

## Step 4: Verify

- [ ] All comparison_chart prod files have metadata
- [ ] All comparison_chart spec files have metadata
- [ ] Format matches the file's existing Basic Info style (table vs list)
- [ ] `game_styles.md` Style Distribution counts are still accurate

---

## Files to modify

- `docs/plans/comparison-chart-metadata.md` (new — this plan)
- `designs/playground_cat5_prod.md` (+ spec if exists)
- `designs/city_library_cat5_prod.md` (+ spec if exists)
- `designs/sunflower_cat5_prod.md` (+ spec if exists)
- `designs/stop_sign_cat5_prod.md` (+ spec if exists)
- `designs/green_apple_cat5_prod.md` (+ spec if exists)
