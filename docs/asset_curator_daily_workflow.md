<!--
  Version: 1.0
  Updated: 2026-06-11
  Audience: Asset Curator
  Companion files: docs/full_pass_agentic_parallel_workflow.html, docs/role_agent_prompting_guide.md, docs/activity_asset_generation_workflow.md, docs/image_generation_provider_setup.md
-->

# Asset Curator Daily Workflow

The asset curator owns visual asset production: illustrative PNG generation,
reference-bound source curation, package-local asset outputs, and asset QA
evidence. This doc covers what to do in a normal work session, when to involve a
coding agent, what commands to run, what evidence to expect, and when to stop.

Read the [File Ownership matrix](full_pass_agentic_parallel_workflow.html#ownership)
to confirm which files belong to this role. Read
[docs/activity_asset_generation_workflow.md](activity_asset_generation_workflow.md)
for the WonderLens flat Nordic style contract. Read
[role_agent_prompting_guide.md](role_agent_prompting_guide.md) for the stock
asset curator prompt.

## Prerequisites

- The run captain has committed baseline packages. For packages that also need
  text review, the text reviewer should merge their PR before you start work.
- You have confirmed the asset requirements for each assigned package: which
  assets are `illustrative`, which are `reference_bound`, and which screen
  targets are needed.
- For illustrative assets: you have access to a Codex-enabled coding agent with
  built-in `imagegen`, or the Gemini provider is configured
  (see `docs/image_generation_provider_setup.md`).
- For reference-bound assets: approved source originals or verified source URLs
  are available before you start the build phase.
- Your local repo is synced with the latest run branch.

## File Scope

You may edit these files per assigned package:

- `runs/<run_id>/activity_packages/<activity_id>/asset_manifest.yaml`
- `runs/<run_id>/activity_packages/<activity_id>/assets/**`
- `runs/<run_id>/generated_assets/**`
- `runs/<run_id>/review_status/<activity_id>.yaml`

You may make narrow, clearly scoped corrections to:

- `spec.md` `## Asset Brief` and `## Asset Usage Timeline` (only to fix asset IDs or paths)

You must not edit:

- `prod.md` mechanics, dialogue, or branch behavior
- `spec.md` activity design rationale (except asset brief path corrections)
- `tag_block.yaml`, `demo_support.yaml`, `recap.template.yaml`, `dashboard.template.yaml`
- Downstream app repos
- Unrelated activity packages

## Key Concepts

### Illustrative assets

Generated art in the WonderLens flat Nordic children's illustration style.
- Style: broad flat color fills, sparse arc-eye/texture linework, restrained
  boho pastels (oatmeal beige, muted sage, dusty teal-blue, soft
  terracotta/salmon, warm brown, mustard/ochre, blush pink, pale leaf green,
  muted sky accents), generous negative space, square 512x512 source art.
- Scene assets: full-bleed square images that can be clipped by the round lens.
- Item/object/character assets: separate centered PNGs with clean white padding.
- No baked text, letters, numbers, UI chrome, masks, borders, logos, watermarks,
  contact sheets, or multi-card sheets.
- Round-screen variants keep important detail inside the central 70-75% circle
  and remain recognizable at 144 px.
- Source PNGs come from Codex built-in `imagegen` or the configured Gemini
  provider.

### Reference-bound assets

Real-world facts or identities that must be visually correct.
- Examples: constellations, artworks, maps, scientific diagrams, cultural
  artifacts, species, historical objects, named places, famous structures.
- Must include approved source/provenance, `source_strategy`,
  `transformation_policy`, and verification requirements.
- Random generated approximations fail the contract.
- Accepted source types: public-domain museum/archive, official/verified source
  URLs, licensed/internal asset libraries, verified educational/scientific
  sources, structured data that can be redrawn accurately.
- Store source originals under `assets/sources/<asset_id>__source_original.<ext>`
  and metadata under `assets/sources/<asset_id>__source_metadata.yaml`.

## Session Workflow

Each daily session follows five phases. Work activity by activity, not
directory-wide.

---

### Phase 1: Start — Set Up the Role Branch

```bash
# Step 1a. Sync and create your role branch
git fetch origin
git checkout run/<RUN_ID>
git pull
export ASSIGNED_IDS="activity_id_1 activity_id_2"
git checkout -b <your_name>/assets-$(echo ${ASSIGNED_IDS%% *} | head -c 20)

# Step 1b. Inspect asset requirements for assigned packages
for aid in ${ASSIGNED_IDS}; do
  echo "=== ${aid} ==="
  cat runs/${RUN_ID}/activity_packages/${aid}/asset_manifest.yaml
  echo "---"
  rg -A5 '## Asset Brief' runs/${RUN_ID}/activity_packages/${aid}/spec.md
  echo "---"
  rg -A3 '## Asset Usage Timeline' runs/${RUN_ID}/activity_packages/${aid}/spec.md
done

# Step 1c. Inventory what exists vs what is needed
for aid in ${ASSIGNED_IDS}; do
  echo "=== ${aid} ==="
  ls -R runs/${RUN_ID}/activity_packages/${aid}/assets/ 2>/dev/null || echo "(no assets yet)"
done
```

Before editing, classify each asset in the manifest:

- `accuracy_mode: illustrative` → needs Codex imagegen or Gemini source PNG generation
- `accuracy_mode: reference_bound` → needs approved source originals and metadata before build
- Check every `asset.role`: `entity`, `activity_preview`, `collection_correct`,
  `collection_distractor`, `badge`, `story_scene`, or `ui_overlay`
- Check `screen_targets`: at minimum `round_device_screen` with `aspect_ratio: "1:1"`

---

### Phase 2: Agent — Generate or Curate Sources

Start a coding agent per package:

```text
/goal Execute goals/asset-curator-goal.md end to end with RUN_ID=<run_id> ACTIVITY_ID=<activity_id>.
```

The goal file owns the WonderLens flat Nordic style contract (see
`docs/activity_asset_generation_workflow.md`), the allowed/forbidden file
lists, the deterministic builder and validator commands, the reference-bound
asset provenance rules, and the completion criteria. You do not need to
repeat these rules in the prompt.

### Phase 3: Source — Handle Reference-Bound Assets

Reference-bound assets cannot be faked. For each one:

1. Check the manifest's `reference_policy` and `sources` fields.
2. Confirm the source URL/URI resolves to the correct reference.
3. Verify the license allows storage and derivative transformation.
4. Download the source original and record metadata:

```bash
mkdir -p runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/assets/sources

# Download source original (example)
curl -L -o runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/assets/sources/<asset_id>__source_original.jpg "<approved_source_url>"

# Compute hash
sha256sum runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/assets/sources/<asset_id>__source_original.jpg
```

5. Write source metadata:

```yaml
# runs/<RUN_ID>/activity_packages/<ACTIVITY_ID>/assets/sources/<asset_id>__source_metadata.yaml
asset_id: <asset_id>
source_type: public_domain_museum
license: CC0
storage_allowed: true
verification_status: accepted
sha256: <computed_hash>
source_url: <approved_source_url>
verified_at: "<ISO 8601>"
reviewer_agent: <your_name>
notes: "<what is factually correct about this image>"
```

6. If no approved source exists, do not proceed. Mark `asset_review.status:
   blocked` and set `blocked_reason` with the missing-source detail.

---

### Phase 4: Build — Generate Runtime PNGs

```bash
# Step 4a. Confirm source PNGs are in place
# For illustrative assets:
ls runs/${RUN_ID}/generated_assets/inbox/${ACTIVITY_ID}/

# For reference-bound assets:
ls runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/assets/sources/

# Step 4b. Run the deterministic builder
python3 scripts/build_activity_assets.py runs/${RUN_ID} --mode generate_and_curate

# Step 4c. Validate build outputs
python3 scripts/validate_asset_build_outputs.py runs/${RUN_ID}

# Step 4d. Visual QA — open and inspect every generated PNG
# (Use your image viewer or the coding agent's view_image capability)
# Check:
# - Style matches the WonderLens flat Nordic contract
# - No baked text, UI, masks, contact sheets
# - Scene content matches the beat's child action
# - Round-screen variants keep detail inside the safe circle
# - Item/object assets are separate centered PNGs
# - Picker item count matches consumer-parity requirement (normally 4+8)
```

For larger/full production passes, also run:

```bash
python3 scripts/repair_full_pass_asset_bundle.py runs/${RUN_ID}
python3 scripts/validate_asset_granularity.py runs/${RUN_ID}
python3 scripts/validate_full_pass_asset_bundle.py runs/${RUN_ID}
```

Key image QA rules:

- Scene assets must visually explain the activity beat's child action, learning
  evidence, or source-specific screen state. Generic baskets, blank cards,
  blank boards, glows, empty rooms, and decorative placeholders fail.
- Story-scene assets must feel like coherent real-world scenes with plausible
  spaces, stable camera/framing, and concrete beat-to-beat changes.
- Sound/phoneme/word-hunt scenes must foreground listening, speaking, sound
  waves, or search motion — not default to treasure/basket metaphors.
- Picker/catalog activities need 4 correct items + 8 distractors unless the run
  goal records an approved smaller catalog.
- Scene backgrounds must not contain duplicate selectable objects that compete
  with picker sprites.
- No baked text, labels, UI controls, masks, borders, contact sheets, device
  chrome, or premature answer reveals.

If an image fails QA, record the root cause in a prompt note and regenerate with
an exact prompt that removes the failed placeholder subject.

---

### Phase 5: Submit — Open a PR

```bash
# Step 5a. Update review status
# Edit runs/<RUN_ID>/review_status/<ACTIVITY_ID>.yaml:
#   asset_review.status: pass (or needs_fix or blocked)
#   asset_review.reviewer: <your_name>
#   asset_review.provider_generation: (if applicable)
#   asset_review.generated_sources: [list of asset paths and hashes]
#   asset_review.reference_sources: [list of sourced references]
#   asset_review.findings: [1-2 sentence residual risk note]
#   next_owner: run_captain (or integration_owner)

# Step 5b. Run validators
python3 scripts/validate_asset_build_outputs.py runs/${RUN_ID}
git diff --check

# Step 5c. Create a manual prompt trace
mkdir -p runs/${RUN_ID}/manual_audits
cat > runs/${RUN_ID}/manual_audits/${ACTIVITY_ID}_prompt_trace.md << 'EOF'
# Prompt Trace — <ACTIVITY_ID>

| Step | Package Instruction | Imagegen Prompt | Status |
|---|---|---|---|
| ... | ... | ... | ... |
EOF

# Step 5d. Commit and push (ONLY asset files, no text or YAML outside scope)
git add runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/asset_manifest.yaml
git add runs/${RUN_ID}/activity_packages/${ACTIVITY_ID}/assets/
git add runs/${RUN_ID}/generated_assets/
git add runs/${RUN_ID}/review_status/${ACTIVITY_ID}.yaml
git add runs/${RUN_ID}/manual_audits/${ACTIVITY_ID}_prompt_trace.md
git commit -m "feat(assets): <ACTIVITY_ID> — asset build pass, [brief note]"
git push origin <your_name>/assets-<branch_suffix>

# Step 5e. Open a PR to the run branch
```

---

## Status File Rules

You own the `asset_review` block in `runs/<run_id>/review_status/<activity_id>.yaml`.
Update it for every package you work on, regardless of outcome.

Allowed statuses: `pending`, `pass`, `needs_fix`, `blocked`, `not_applicable`.

Every update must include:

- `reviewer` — your name
- `generated_sources` — list of asset IDs with paths, provider, and SHA256
- `reference_sources` — list of asset IDs with metadata paths and verification status
- `findings` — concrete residual risks in 1-2 sentences

For Gemini-generated sources:

```yaml
asset_review:
  provider_generation:
    status: pass
    provider: gemini
    model: gemini-2.5-flash-image
    audit_paths:
      - runs/<RUN_ID>/manual_audits/<ACTIVITY_ID>_prompt_trace.md
```

Do not edit `text_review`, `runtime_validation`, or `pm_review` blocks. Those
belong to other roles.

## Stop Conditions

Stop and ask the run captain when:

- A reference-bound asset has no approved source and the manifest claims it must
  exist.
- The image generation provider returns repeated quality or safety rejections
  after 3 retries.
- The activity's prod.md steps have changed since you started work and the asset
  manifest is now out of sync.
- A required screen target (e.g. `round_device_screen`) is missing from the
  manifest.
- Credentials for image generation or source access are unavailable.

If an asset is not buildable due to a product limitation (e.g. runtime image
generation is unsupported), mark it `blocked` and record the missing capability.

## Example Session

An asset curator session for 2 packages:

```text
# Session start
git fetch origin
git checkout run/20260611_093000_batch3
git pull
git checkout -b carol/assets-constellation-phoneme

# Inspect asset requirements
cat runs/20260611_093000_batch3/activity_packages/constellation_count/asset_manifest.yaml
# → 1 reference_bound (big_dipper_diagram), 1 illustrative (star_count_scene)

cat runs/20260611_093000_batch3/activity_packages/phoneme_hunt/asset_manifest.yaml
# → all illustrative: phoneme_intro_scene, phoneme_hunt_scene, phoneme_celebrate_scene

# Package 1: constellation_count
# Verify Big Dipper source is approved public-domain → download, write metadata
# Mark reference_bound asset as curated

# Package 2: phoneme_hunt
# Generate source PNGs with imagegen → place in inbox
# Run build, check visual QA
# Scene has placeholder basket → repair prompt, regenerate

# Both packages: run builder, validate, update status, commit, push, open PR
```
