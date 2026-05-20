# Review Dashboard Contract

Use this file for `runs/<run_id>/review.html` requirements. `GOAL.md` should reference this contract instead of duplicating dashboard detail in the `/goal` command.

## Purpose

Create a self-contained HTML dashboard that lets a reviewer quickly scan a completed run, compare generated/enriched/audited packages, inspect blocked assignments, and open full activity details without downloading package files.

The dashboard is a derived review artifact. The source of truth remains `run_manifest.yaml`, `review_notes.md`, `results.tsv`, package files, adaptation briefs, blocked briefs, and constrained blocked design previews.

## Inputs

The generator reads:

- `runs/<run_id>/run_manifest.yaml`
- `runs/<run_id>/review_notes.md`
- `results.tsv`
- Package files referenced by `run_manifest.yaml` `activity_path`, including fresh run-local packages under `runs/<run_id>/activity_packages/<activity_id>/` and canonical/enriched packages under `activities/<activity_id>/`
- `<activity_path>/spec.md`
- `<activity_path>/prod.md`
- `<activity_path>/tag_block.yaml`
- `<activity_path>/recap.template.yaml`
- `<activity_path>/dashboard.template.yaml`
- `runs/<run_id>/blocked_briefs/*.yaml`
- `runs/<run_id>/blocked_designs/*.md` when present
- `run_manifest.yaml` generated-activity fields such as `resolved_blockers`, `resolved_blocker_types`, `extensibility_summary`, and `extensibility_notes` when a run used a product-contract override or reusable-entity review
- `spec.md` `## Asset Brief` and `## Asset Usage Timeline`, plus `run_manifest.yaml` `asset_usage` entries when present, for packages that use prebuilt, displayed, or runtime-generated images. Treat these rows as asset dependencies, not necessarily one image per row.

If a value cannot be derived from those inputs, show `Unknown` or omit the field instead of inventing content.

## Required Sections

- Run header: `run_id`, status, timestamps, pending/generated/enriched/blocked/failed counts, and links to `run_manifest.yaml`, `review_notes.md`, `assignment_snapshot.md`, `generated_activity_ids.txt`, and `results.tsv`.
- Sidebar navigation: a compact navigation column or collapsed top rail with links to the main review sections and high-signal run counts.
- Summary metrics: compact counters visible near the top of the first viewport.
- Review criteria: the `program.md` Phase 3 10-dimension rubric, including what passes and why a dimension fails.
- Blocking reason guide: badge label, what it means, why it blocks package validity, and the minimum policy or scope decision that would unblock it (the smallest acceptable resolution — often a "no verification" or fallback-only decision rather than full capability approval). This section must appear directly after Review Criteria when blocked assignments or resolved blocker annotations exist.
- Resolved contract items: when a run assumes minimum-to-unblock decisions are allowed by the product contract, list the formerly blocking activity elements as resolved blocker annotations. These are review callouts, not run failures.
- Extensibility overview: for every generated, enriched, or audited package with reusable-entity potential, show whether the package is entity-specific, entity-agnostic, or parameterized; list reusable slots such as `{runtime_entity}`, `{shared_feature}`, `{matched_color}`, or asset-set IDs; and summarize how the activity can be extended by replacing the current entity, property, or approved asset set.
- Activity HTML exports: when `activity_exports/export_manifest.yaml` exists, show a visible section with one direct link per standalone reviewer packet.
- Activity cards: one concise card per generated, enriched, or audited no-op package. A checked package that passes audit without edits must still appear as a card with `PASS / no changes` or equivalent status.
- Blocked assignment cards: one concise card per blocked assignment.
- Reviewer coverage summary: reviewer names/IDs when available, package scope, PASS/FAIL/N/A evidence, repairs made, and unresolved concerns.
- Validation checks: commands and results from `run_manifest.yaml` `checks`.
- Residual risk / next actions: derived from `review_notes.md` and run notes.

## Card Behavior

- Cards are scan-first summaries, not full detail dumps.
- Each card must show the minimum useful preview: title, ID or concept name, package/block status, category, mechanic, tier, asset policy, one short promise/summary, and file links.
- Each card must be clickable and keyboard-openable.
- Opening a card must reveal all available activity details in a popup dialog or a dedicated detail page. The default implementation should use an accessible in-page dialog so the dashboard remains one self-contained HTML file.
- The detail view must include enough `spec.md`, `prod.md`, and `tag_block.yaml` information for review without opening package files:
  - Design intent, premise, scenario, focal attribute, pillar, game style, and reviewer status.
  - Runtime beats with a visual storyboard/timeline map before the extracted source rows. The map must show step/round title, AI prompt, expected child response branches as colored branch chips, AI follow-up behavior, and screen state when present.
  - Asset usage timeline when visual assets are present: asset ID, type, requiredness, prebuilt/runtime/display timing, exact use step or round, screen location, display/use behavior, persistence/hide behavior, prompt/source summary, and fallback behavior.
  - Asset usage metrics that distinguish `Asset dependencies` (unique asset IDs or asset sets), `Display beats` (runtime step/round appearances parsed from `use_step`), and `Image items` (known image count, or set/item-count TBD when a row represents a card set or asset set). Do not label a single asset row as a single image when it is displayed across multiple steps.
  - Learning tags, related concepts, ATL skills, and scorecard summary when present.
  - Parsed scorecard results for all 10 dimensions from `spec.md`, with the PASS/FAIL/N/A result and the note explaining why. Dimension 8 may be N/A when no mapping source is required.
  - Resolved blocker notes when the product contract allowed a formerly blocking dependency. These notes must be visible near the affected activity detail and tagged with the same reason colors as blocked markers.
  - Extensibility notes and reusable slots, including parameter placeholders and any explicit `## Extensibility Notes` from `spec.md`.
  - Changed files and package-file links.
- Blocked cards must open a detail view with missing product/design decisions, capability flags, a `Minimum To Unblock` section immediately below capability flags, blocked reason badges, blocked brief link, constrained design preview link when present, proposed preview beats, and inline `BLOCKED ELEMENT` comments when present.
- The blocked detail `Minimum To Unblock` section must deduplicate blocker groups across missing decisions and inline markers, then show the smallest policy or scope decision that would make each blocker valid. Use the same reason definitions as the Blocking Reason Guide so the card-level answer matches the run-level guide.
- Blocked cards must distinguish missing decisions from inline blocked markers. Missing decisions are unresolved product/design questions from the brief. Inline blocked markers are occurrences inside proposed runtime steps where that unresolved decision affects a beat. Show both counts when available, plus a unique blocker-type count, so one missing decision that appears in several beats is not mistaken for several separate decisions.
- Inline blocked markers must be classified into the same blocking reason groups used by the reason guide and rendered as colored chips with the marker text. The text remains authoritative; color is only a scan aid.
- Blocked detail views must include a blocked-preview scorecard using the 10 `program.md` dimensions. This scorecard is review evidence only. It may use `REVIEWABLE`, `BLOCKED`, and `N/A` statuses to show what can be inspected in the constrained preview and what prevents package validity. It must not be treated as a normal package PASS, and it must not allow `results.tsv` logging or assignment checkoff until blockers are resolved and a standard five-file package passes the normal rubric.
- Clicking normal links inside a card must navigate to the link, not open the detail dialog.
- The detail dialog must provide a visible close button, close on `Escape`, trap browser focus naturally through the native dialog behavior, and return focus to the opened card when closed.

## Sorting And Filtering

Provide search, filter, and sort controls when fields are available:

- Package type
- Cat1/Cat3/Cat5 category
- Status
- Mechanic
- Tier
- Reviewer coverage
- Asset dependency
- Asset dependency count / display beat count / asset usage timing
- Blocked reason

Filters must hide/show cards without changing source data. Sorting must preserve stable card dimensions and avoid layout jumps beyond normal reflow.

## Tag Color System

Use grouped tag colors so reviewers can distinguish metadata types quickly:

- Category tags: distinct category color, with Cat1/Cat3/Cat5 still readable in light theme.
- Status tags: success/blocked/warning/pass/fail semantics.
- Mechanic tags: neutral-purple or similar non-status color.
- Tier tags: subdued neutral/blue.
- Asset tags: teal for normal/no-assets, amber for required/blocked/runtime-generated.
- Asset usage tags: distinct timing chips for `pre_generated`, `runtime_generated`, and `display_existing`; the text remains authoritative.
- Reviewer tags: green for PASS/covered, amber for unresolved/N/A, red for FAIL.
- Blocked reason tags: amber family, distinct from category and mechanic tags.
- Inline blocked/resolved marker tags: reason-specific backgrounds so runtime image generation, coloring UI, Cat3 material workflow, UI state, prebuilt assets, motion safety, before/after evidence, OCR/text handling, caregiver setup, and generic product decisions can be skimmed separately.

Keep colors restrained and accessible. Tags must not rely on color alone; the text label remains authoritative.

## Asset Counting Rules

The dashboard must avoid the ambiguous label `Image uses`.

- `Asset dependencies` counts unique `asset_id` rows. A `card_set` or approved reference pack still counts as one dependency even if it contains many images.
- `Display beats` counts where the dependency appears in runtime. For example, `prod.step_2; prod.step_3.round_1-2` means one asset dependency and three display beats.
- `Image items` should show a known item count only when the source declares it. For `card_set`, `reference pack`, or other set-like rows without an explicit item count, show a set label such as `card set, count not declared`.
- The detail view should keep the raw `use_step` text visible so reviewers can verify the parsed display-beat count.

## Visual Design

- Default to a polished light theme.
- Use system fonts, high-contrast text, subtle borders, compact spacing, and predictable product-dashboard patterns.
- Use a fixed desktop sidebar for section navigation and run counts. It must remain visible while the page scrolls and must not clip beneath the header. Collapse it above the content on narrower screens instead of hiding the navigation.
- Keep the first viewport useful: header, summary metrics, and primary filters should be visible without excessive scrolling on typical desktop widths.
- Prefer dense but organized information over marketing-style presentation.
- Do not use external CSS, JavaScript, fonts, images, CDNs, or build tooling.
- Do not use dark theme by default, decorative gradient/orb backgrounds, card-within-card nesting, or visible instructional copy explaining how to use the dashboard.

### Design language

The generator implements an editorial product-dashboard aesthetic. Treat the following as the canonical visual identity; preserve it across regenerations.

- **Palette.** Warm paper background (a faint amber-tinted off-white), slate-ink text, single indigo accent (`oklch(40% 0.18 268)` family). Status colors stay restrained: mint green for PASS, soft amber for blocked/warning, muted red for fail, neutral grey for N/A. Reason chips keep their distinct hues. Never pure black or pure white. Tint neutrals toward the indigo/amber paper hue.
- **Typography.** Pair a display serif stack (`ui-serif`, `"Iowan Old Style"`, `"Hoefler Text"`, Charter, Georgia) with the system sans stack for body text and a system mono stack for IDs and file links. Use the serif for the run title (H1) and detail dialog titles; use small-caps uppercase with tracked letterspacing for H2/eyebrow/section labels; use `font-variant-numeric: tabular-nums` on every numeric display (metrics, counts, timestamps, scorecards).
- **Hierarchy.** Editorial H1 (fluid `clamp(28px, ..., 38px)`, weight ~540, negative tracking) → small uppercase H2 section labels with a 6px accent dot prefix → compact 16px serif card titles → small uppercase field labels with 10px tracked letterspacing.
- **Spacing rhythm.** Use varied spacing, not uniform padding. Larger gaps between major panels (~18px), tight gaps inside panels (~12-14px). Section panels round at 10px; chips and field cells round at 4-6px. Hairline separators (`color-mix` with line color) replace heavy borders inside dense regions.
- **No card-in-card.** Inside a panel, prefer hairline-divided grids (metrics, meta-grid, inline-fields), counter-numbered hairline lists (runtime beats use `01`, `02`, ... in mono), compact visual runtime maps, and bordered chips. Do not stack panels-within-panels or boxed cards-within-cards. The reviewer-coverage and runtime-beat sections must use hairline rows, not nested card boxes.
- **Card accent rails.** Activity cards carry a thin indigo accent rail along the left edge. Blocked cards carry an amber accent rail. The rail is decorative reinforcement of the badge — the badge text and color remain authoritative.
- **Run status indicator.** The header shows a small filled dot beside the run status: mint green for `completed`, amber for `completed_with_blockers`, red for `failed`, blue for `in_progress`. The status word remains the authoritative signal; the dot is a scan aid.
- **Header layout.** The header uses a two-column layout: title block on the left (a 96px accent rule above the eyebrow, the eyebrow `WonderLens · Activity Run Review`, the run-id H1, then a single summary line with status dot, started, completed), and a small bordered "Run ID" stamp on the right. The header sticks while the user scrolls and uses a subtle backdrop blur.
- **Interaction polish.** Hover transitions are snappy (~100-120ms). Interactive surfaces (cards, buttons, inputs, sidebar links) all show a clear accent border or a soft `box-shadow` focus ring (`0 0 0 3px` of a 18% accent mix) on `:focus-visible`. The detail dialog uses a backdrop blur, refined drop shadow, and serif title; it must respect `prefers-reduced-motion`.
- **Numbers as data.** Metric numerals, scorecard counts, timestamps, and run ids must use tabular numerals so columns align without jitter when filters/sorts re-flow them.

These choices are visual polish on top of the contract above. They must not remove any data, navigation, filter, modal behavior, or accessibility affordance the contract requires.

## Link Rules

- Run-local files use local relative links such as `run_manifest.yaml`, `activity_packages/<activity_id>/spec.md`, `blocked_briefs/017_coloring_game.yaml`, and `blocked_designs/017_coloring_game.md`.
- Canonical activity package files use relative links back to the repo root, such as `../../activities/<activity_id>/spec.md`.
- Links should degrade safely if a target is missing: keep the label visible and mark the target missing instead of hiding the row.

## In-file preview

Reviewers must be able to read every linked `.md`, `.yaml`, and `.txt` file without leaving the dashboard. The generator embeds the raw content of each linked file as a hidden `<template>` element and opens it on click in an accessible in-page preview dialog.

- The generator embeds raw text content for every relative `.md`, `.yaml`, `.yml`, and `.txt` link inside the run directory or the repo. Files larger than ~240 KB are recorded with a "truncated" flag and the preview dialog shows a "Open file in new tab" affordance instead of inline content.
- Each previewable anchor carries a `data-preview-id` attribute pointing at its `<template>` element. The dialog renders Markdown for `.md` files and a preformatted code block for `.yaml`/`.txt`/`.tsv`.
- The Markdown renderer is dependency-free and inline (no external libraries). It supports headings, paragraphs, ordered/unordered lists, fenced code, inline code, bold/italic, blockquotes, and links.
- Click behaviour: a plain click opens the inline preview. `Cmd`/`Ctrl`/`Shift`/`Alt`/middle-click bypass the preview and navigate to the file directly. The dialog also exposes an "Open file in new tab" link so reviewers can escape to the raw file when they want it.
- Accessibility: the preview dialog uses the native `<dialog>` element, is opened with `showModal()`, closes on `Escape`, closes when the backdrop is clicked, and returns focus to the link that opened it. Markdown rendering inherits the dashboard's serif display stack for headings and the system sans stack for body text.
- The preview behaviour must not interfere with the existing activity-detail dialog, card-click navigation, or `data-detail-template` modal pattern.

## Generation And Validation

Generate and validate:

```bash
python3 scripts/integrate_generated_assets.py runs/<run_id>
python3 scripts/integrate_generated_assets.py --validate runs/<run_id>
python3 scripts/export_activity_html.py runs/<run_id>
python3 scripts/export_activity_html.py --validate runs/<run_id>
python3 scripts/generate_run_review.py runs/<run_id>
python3 scripts/generate_run_review.py --validate runs/<run_id>
```

These commands assume `python3` resolves to an environment with PyYAML available. If the local default `python3` does not have PyYAML, activate the repo/operator Python environment first; for example, this run was validated with `env PATH="$(pyenv root)/versions/3.13.6/bin:$PATH" python3 ...`.

Workflow:

1. Finish package generation, reviewer evidence, package checks, blocked briefs/previews, and manifest outputs first.
2. When generated prebuilt contact sheets are being accepted into the run, run `python3 scripts/integrate_generated_assets.py runs/<run_id>` and `python3 scripts/integrate_generated_assets.py --validate runs/<run_id>` to create and validate `integrated_assets/asset_bindings.yaml`.
3. When integrated activities need standalone reviewer packets, run `python3 scripts/export_activity_html.py runs/<run_id>` and `python3 scripts/export_activity_html.py --validate runs/<run_id>` to create one self-contained static HTML file per integrated activity under `activity_exports/`. Each packet embeds the integrated contact sheet and the review-only mechanism storyboard. The storyboard must be labeled as review context, not child-facing runtime UI.
4. Run `python3 scripts/generate_run_review.py runs/<run_id>` to generate the self-contained HTML from `run_manifest.yaml`, `review_notes.md`, `results.tsv`, packages, blocked briefs, blocked design previews, and run-local asset artifacts.
5. Run `python3 scripts/generate_run_review.py --validate runs/<run_id>` before reporting completion.
6. Keep generated HTML files as derived artifacts. Fix source run/package files or the generator, then regenerate; do not hand-edit `review.html` or `activity_exports/*.html` as source of truth.

After writing `review.html`:

1. Update `runs/<run_id>/run_manifest.yaml` `outputs.review_dashboard` to `runs/<run_id>/review.html`.
2. Add check entries for the integration, export, generation, and validation commands that were run.
3. Verify the file exists, is non-empty, has `<html`, `<style`, `<script>`, the run id, sidebar navigation, the review-dashboard workflow section, activity HTML export links when `activity_exports/export_manifest.yaml` exists, cards for generated/enriched/audited packages, blocked entries when present, review criteria, the blocking reason guide directly after review criteria when blocked or resolved blocker annotations exist, resolved contract items when applicable, extensibility overview when applicable, visual runtime beat maps plus extracted source rows, asset usage timelines when image/display dependencies exist, distinct `Asset dependencies`, `Display beats`, and `Image items` labels, 10-dimension package scorecard results, blocked-preview scorecards when blocked entries exist, clickable detail behavior, modal/detail content, per-blocked-card `Minimum To Unblock` sections below capability flags, grouped tag colors, inline blocked/resolved marker chips, clear missing-decision versus inline-marker counts, in-file preview templates plus a `<dialog id="preview-dialog">` and `data-preview-id` link wiring, and resolving local links.
