# Demo-Ready Legacy Package Conversion Implementation Plan

> Execution note: implement this plan task-by-task with verification after each file group.

**Goal:** Convert `dream_whisperer_cat`, `mood_changer_dog`, `time_machine_dinosaur`, `polka_dot_patrol`, and `fluffy_expedition_dandelion` into demo-ready canonical packages with package-local visual assets.

**Architecture:** Treat this as existing-package maintenance under `activities/`, not fresh assignment queue generation. Add paired `demo_support.yaml` and `asset_manifest.yaml` files, bind freshly generated 512x512 PNG assets under each package's `assets/` directory, and update only package prose/templates needed to make the runtime contract honest.

**Tech Stack:** Markdown, YAML, freshly generated PNG assets, `scripts/validate_demo_package_contract.py`, ImageMagick `identify`, `sha256sum`/`shasum`, `git diff --check`.

**Asset Source Rule:** Do not reuse old image assets from sibling repos, fixture directories, prior runs, or existing demo/icon bundles. Every package-local PNG added by this plan must be freshly generated for this conversion.

---

### Task 1: Add Demo Extension Metadata For Three Cat1 Packages

**Files:**
- Create: `activities/dream_whisperer_cat/demo_support.yaml`
- Create: `activities/dream_whisperer_cat/asset_manifest.yaml`
- Create: `activities/mood_changer_dog/demo_support.yaml`
- Create: `activities/mood_changer_dog/asset_manifest.yaml`
- Create: `activities/time_machine_dinosaur/demo_support.yaml`
- Create: `activities/time_machine_dinosaur/asset_manifest.yaml`

**Steps:**
1. For `dream_whisperer_cat`, use `status: supported`, `ui_template: cat1_dialogue`, `entity_compatibility: agnostic`, and `parameterization.mode: entity_theme`.
2. For `mood_changer_dog`, use `status: supported`, `ui_template: cat1_dialogue`, `entity_compatibility: source_bound`, and `parameterization.mode: entity_theme`.
3. For `time_machine_dinosaur`, use `status: supported`, `ui_template: cat1_dialogue`, `entity_compatibility: source_bound`, and `parameterization.mode: entity_theme`.
4. In each manifest, declare the standard runnable scene bundle: `activity_icon`, `intro_scene`, `rules_scene`, `round_1_scene`, `round_2_scene`, `round_3_scene`, `celebrate_scene`, and `closing_scene`.
5. Use `style_id: wonderlens_device_mint_soft_3d`, `round_device_screen` 512x512/circle/safe-area target, generated illustrative prompts, and package-relative `assets/<asset_id>__round_512.png` paths.

**Validation:**
- Run `python3 scripts/validate_demo_package_contract.py activities/dream_whisperer_cat activities/mood_changer_dog activities/time_machine_dinosaur`.

### Task 2: Convert Polka Dot Patrol To Reusable Catalog Collection

**Files:**
- Modify: `activities/polka_dot_patrol/spec.md`
- Modify: `activities/polka_dot_patrol/prod.md`
- Modify: `activities/polka_dot_patrol/tag_block.yaml`
- Modify: `activities/polka_dot_patrol/recap.template.yaml`
- Modify: `activities/polka_dot_patrol/dashboard.template.yaml`
- Create: `activities/polka_dot_patrol/demo_support.yaml`
- Create: `activities/polka_dot_patrol/asset_manifest.yaml`

**Steps:**
1. Reframe the runtime contract as a reusable Pattern Patrol property target with approved catalog sets for `polka_dots` and `stripes`.
2. Keep `activity_id: polka_dot_patrol`; avoid a breaking package rename.
3. Use `entity_binding: parameterized`, `entity_compatibility: agnostic`, `parameterization.mode: property_target`, `status: supported`, and `ui_template: cat5_collection`.
4. Remove open-camera visual-verification claims. The child picks catalog items and explains the pattern evidence.
5. Add `## Asset Brief` and `## Asset Usage Timeline` to `spec.md`.
6. Add missing `activity_id` fields to recap/dashboard templates.
7. Declare pattern item assets as separate `collection_correct` / `collection_distractor` files under `assets/items/`.

**Validation:**
- Run `python3 scripts/validate_demo_package_contract.py activities/polka_dot_patrol`.
- Review `prod.md` for no remaining arbitrary-photo verification claims.

### Task 3: Generate And Bind Fresh Runtime PNG Assets

**Files:**
- Create PNGs under:
  - `activities/dream_whisperer_cat/assets/`
  - `activities/mood_changer_dog/assets/`
  - `activities/time_machine_dinosaur/assets/`
  - `activities/polka_dot_patrol/assets/`
  - `activities/polka_dot_patrol/assets/items/`
- Keep all four `asset_manifest.yaml` files schema-compatible with package-relative `path` values only.

**Steps:**
1. Generate one fresh separate 512x512 PNG per manifest asset using the WonderLens flat Nordic style.
2. Do not copy, crop, resize, or adapt existing assets from sibling repos, fixture packages, previous generated runs, or legacy frontend bundles.
3. Resize any larger generated source to 512x512 with ImageMagick.
4. Place scene assets under package-local `assets/`; place catalog item assets under `assets/items/`.
5. Use `identify` to confirm every asset is 512x512 PNG.
6. Compute `byte_count` and `sha256` for every variant as verification evidence only; do not write those fields into manifests because the canonical schema does not allow them.

**Validation:**
- Run `find activities/{dream_whisperer_cat,mood_changer_dog,time_machine_dinosaur,polka_dot_patrol}/assets -name '*.png' -print -exec identify -format '%w %h %m %b\n' {} \;`.
- Run `python3 scripts/validate_demo_package_contract.py activities/dream_whisperer_cat activities/mood_changer_dog activities/time_machine_dinosaur activities/polka_dot_patrol`.

### Task 4: Final Consistency And Commit

**Files:**
- Review all touched files.

**Steps:**
1. Run `git diff --check`.
2. Run targeted `rg` checks for stale unsupported wording in `polka_dot_patrol`.
3. Run final demo package validation across the four packages.
4. Inspect `git status --short` and stage only intended files.
5. Commit with `feat(activities): add demo-ready legacy assets`.

**Validation:**
- `git diff --check`
- `python3 scripts/validate_demo_package_contract.py activities/dream_whisperer_cat activities/mood_changer_dog activities/time_machine_dinosaur activities/polka_dot_patrol`

### Task 5: Convert Fluffy Expedition Dandelion To Catalog Collection

**Files:**
- Modify: `activities/fluffy_expedition_dandelion/spec.md`
- Modify: `activities/fluffy_expedition_dandelion/prod.md`
- Modify: `activities/fluffy_expedition_dandelion/tag_block.yaml`
- Modify: `activities/fluffy_expedition_dandelion/recap.template.yaml`
- Create: `activities/fluffy_expedition_dandelion/demo_support.yaml`
- Create: `activities/fluffy_expedition_dandelion/asset_manifest.yaml`
- Create PNGs under `activities/fluffy_expedition_dandelion/assets/` and `activities/fluffy_expedition_dandelion/assets/items/`

**Steps:**
1. Reframe the original tactile/photo collection as a supported Cat5 catalog collection for `fluffy_soft_texture`.
2. Use `entity_binding: parameterized`, `entity_compatibility: agnostic`, `parameterization.mode: property_target`, `status: supported`, and `ui_template: cat5_collection`.
3. Remove or neutralize claims that the runtime accepts arbitrary photos, verifies touch, or judges real-world softness.
4. Declare the standard scene bundle plus individual soft-texture catalog cards and texture distractors.
5. Generate fresh package-local PNGs only; do not reuse old image assets.

**Validation:**
- Run `python3 scripts/validate_demo_package_contract.py activities/fluffy_expedition_dandelion`.
- Run the full tag-block schema validation under the repo-root `.venv`.
- Run `find activities/fluffy_expedition_dandelion/assets -name '*.png' -print -exec identify -format '%w %h %m %b\n' {} \;`.
