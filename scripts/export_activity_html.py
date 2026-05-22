#!/usr/bin/env python3
"""Export integrated activity packages as self-contained static HTML pages."""

from __future__ import annotations

import argparse
import base64
import html
import mimetypes
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "PyYAML is required. Install pyyaml or run from the repo environment "
        "used for activity metadata validation."
    ) from exc

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_run_review as review  # noqa: E402


BASE_CSS = """
:root {
  color-scheme: light;
  --paper: #fbf7ef;
  --panel: #fffdf8;
  --ink: #243044;
  --muted: #667085;
  --line: #ded6c8;
  --accent: #4936a3;
  --accent-soft: #ece8ff;
  --asset: #08756f;
  --asset-soft: #e5f6f3;
  --warn: #9a5b00;
  --warn-soft: #fff2d4;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font: 15px/1.55 ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
.page {
  width: min(1180px, calc(100vw - 32px));
  margin: 0 auto;
  padding: 28px 0 48px;
}
.hero {
  border-bottom: 1px solid var(--line);
  padding: 10px 0 22px;
  margin-bottom: 22px;
}
.eyebrow, .label {
  color: var(--accent);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
}
h1, h2, h3 {
  margin: 0;
  font-family: ui-serif, "Iowan Old Style", "Hoefler Text", Charter, Georgia, serif;
  font-weight: 560;
}
h1 { font-size: clamp(30px, 4vw, 46px); line-height: 1.05; margin-top: 6px; }
h2 { font-size: 22px; margin-bottom: 14px; }
h3 { font-size: 18px; margin-bottom: 8px; }
.subline { color: var(--muted); margin: 10px 0 0; font-variant-numeric: tabular-nums; }
.layout {
  display: grid;
  grid-template-columns: minmax(280px, 44%) 1fr;
  gap: 18px;
  align-items: start;
}
.panel, .asset-panel, .summary-panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 18px;
  box-shadow: 0 1px 0 rgba(36, 48, 68, .04);
}
.asset-panel { margin: 0; }
.asset-panel img {
  display: block;
  width: 100%;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: white;
}
figcaption { color: var(--muted); font-size: 13px; margin-top: 10px; }
.panel { margin-top: 18px; }
.meta-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1px;
  border: 1px solid var(--line);
  background: var(--line);
  border-radius: 8px;
  overflow: hidden;
}
.meta-grid > div {
  background: var(--panel);
  padding: 10px 12px;
  min-width: 0;
}
.meta-grid span, .asset-contract span {
  display: block;
  color: var(--muted);
  font-size: 10px;
  font-weight: 700;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.meta-grid strong, code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 12px;
  overflow-wrap: anywhere;
}
.chip-row { display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 14px; }
.chip {
  display: inline-flex;
  border-radius: 5px;
  padding: 4px 7px;
  background: var(--accent-soft);
  color: var(--accent);
  font-size: 12px;
  font-weight: 700;
}
.chip.asset { background: var(--asset-soft); color: var(--asset); }
.chip.warn { background: var(--warn-soft); color: var(--warn); }
.asset-contract p {
  margin: 10px 0;
  padding-top: 10px;
  border-top: 1px solid var(--line);
}
.runtime-list, .scorecard-list {
  list-style: none;
  padding: 0;
  margin: 0;
}
.runtime-list li, .scorecard-list li {
  padding: 14px 0;
  border-top: 1px solid var(--line);
}
.runtime-list li:first-child, .scorecard-list li:first-child { border-top: 0; padding-top: 0; }
.beat-title {
  display: flex;
  gap: 10px;
  align-items: baseline;
}
.beat-title span {
  color: var(--accent);
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 12px;
  font-variant-numeric: tabular-nums;
}
.branch-table-wrap {
  overflow-x: auto;
  margin-top: 10px;
}
.branch-table {
  width: 100%;
  min-width: 640px;
  border-collapse: separate;
  border-spacing: 0;
  table-layout: fixed;
  font-size: 13px;
}
.branch-table th,
.branch-table td {
  border-top: 1px solid var(--line);
  padding: 9px 8px;
  text-align: left;
  vertical-align: top;
}
.branch-table th {
  color: var(--muted);
  font-size: 11px;
  letter-spacing: .06em;
  text-transform: uppercase;
}
.branch-table th:first-child,
.branch-table td:first-child { width: 124px; }
.branch-label {
  display: inline-flex;
  border-radius: 999px;
  padding: 2px 8px;
  background: var(--accent-soft);
  color: var(--accent);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .06em;
  text-transform: uppercase;
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}
th, td {
  border-top: 1px solid var(--line);
  padding: 9px 8px;
  text-align: left;
  vertical-align: top;
}
th { color: var(--muted); font-size: 11px; letter-spacing: .06em; text-transform: uppercase; }
details {
  border-top: 1px solid var(--line);
  padding: 12px 0;
}
summary { cursor: pointer; font-weight: 700; }
pre {
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  background: #f4efe5;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px;
  max-height: 460px;
  overflow: auto;
  font-size: 12px;
}
a { color: var(--accent); }
.path-list { display: grid; gap: 6px; margin-top: 12px; }
.path-list a { overflow-wrap: anywhere; }
.storyboard-block {
  display: grid;
  grid-template-columns: minmax(280px, 48%) 1fr;
  gap: 16px;
  align-items: start;
}
.storyboard-figure { margin: 0; }
.storyboard-figure img {
  display: block;
  width: 100%;
  border-radius: 8px;
  border: 1px solid var(--line);
  background: white;
}
.storyboard-note {
  color: var(--warn);
  background: var(--warn-soft);
  border: 1px solid #edd094;
  border-radius: 8px;
  padding: 10px 12px;
  margin: 0 0 14px;
}
.storyboard-caption-list {
  list-style: none;
  padding: 0;
  margin: 12px 0 0;
}
.storyboard-caption-list li {
  display: grid;
  grid-template-columns: 34px 1fr;
  gap: 10px;
  padding: 11px 0;
  border-top: 1px solid var(--line);
}
.storyboard-caption-list li:first-child { border-top: 0; }
.storyboard-panel-number {
  color: var(--accent);
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 12px;
  font-weight: 700;
}
.storyboard-caption-list strong { display: block; margin-bottom: 4px; }
.storyboard-caption-list p { margin: 0; }
.storyboard-source { display: block; color: var(--muted); font-size: 12px; margin-top: 5px; }
@media (max-width: 820px) {
  .layout, .meta-grid, .storyboard-block { grid-template-columns: 1fr; }
  .page { width: min(100vw - 20px, 1180px); }
}
"""


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return data if isinstance(data, dict) else {}


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=False))


def read_text(path: Path) -> str:
    return path.read_text(errors="replace") if path.exists() else ""


def html_escape(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def norm(value: Any) -> str:
    return "" if value is None else " ".join(str(value).split())


def activity_slug(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "_", value).strip("_") or "activity"


def data_uri(path: Path) -> str:
    media_type = mimetypes.guess_type(path.name)[0] or "image/png"
    return f"data:{media_type};base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def render_static_image(asset_id: str, image_bytes: bytes) -> str:
    encoded = base64.b64encode(image_bytes).decode("ascii")
    return f'<img src="data:image/png;base64,{encoded}" alt="Contact sheet for {html_escape(asset_id)}">'


def run_manifest_entry_by_activity(run_manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    outputs = run_manifest.get("outputs", {})
    entries = outputs.get("generated_activities", []) if isinstance(outputs, dict) else []
    return {
        norm(entry.get("activity_id")): entry
        for entry in entries
        if isinstance(entry, dict) and entry.get("activity_id")
    }


def collect_activity_package(repo_root: Path, run_dir: Path, activity_entry: dict[str, Any]) -> dict[str, Any]:
    return review.collect_package(repo_root, run_dir, activity_entry, "generated")


def chip(text: Any, kind: str = "") -> str:
    extra = f" {kind}" if kind else ""
    return f'<span class="chip{extra}">{html_escape(text)}</span>'


def render_metadata(package: dict[str, Any], binding: dict[str, Any]) -> str:
    chips = "".join(
        [
            chip(package.get("mechanic"), "asset"),
            chip(package.get("category")),
            chip(package.get("tier")),
            chip(package.get("asset_policy"), "warn" if package.get("asset_policy") != "optional_support" else "asset"),
            chip(package.get("status")),
        ]
    )
    fields = {
        "Activity ID": binding.get("activity_id"),
        "Asset ID": binding.get("asset_id"),
        "Pillar": package.get("pillar"),
        "Game style": package.get("game_style"),
        "Reviewer": package.get("reviewer"),
        "Package": binding.get("package_path"),
    }
    items = "".join(
        f"<div><span>{html_escape(label)}</span><strong>{html_escape(value)}</strong></div>"
        for label, value in fields.items()
    )
    return f'<div class="chip-row">{chips}</div><div class="meta-grid">{items}</div>'


def render_asset_contract(binding: dict[str, Any]) -> str:
    rows = [
        ("Asset type", binding.get("asset_type")),
        ("Requiredness", binding.get("requiredness")),
        ("Generation timing", binding.get("generation_timing")),
        ("Use steps", binding.get("use_step")),
        ("Display location", binding.get("display_location")),
        ("Display behavior", binding.get("display_behavior")),
        ("Fallback contract", binding.get("fallback_behavior")),
        ("Safety constraints", binding.get("safety_constraints")),
    ]
    body = "".join(
        f'<p><span>{html_escape(label)}</span>{html_escape(value or "Not specified")}</p>'
        for label, value in rows
    )
    return f'<section class="asset-contract"><h2>Integrated Prebuilt Asset</h2>{body}</section>'


def render_overview(package: dict[str, Any]) -> str:
    paragraphs = [
        ("Brief Description", package.get("brief_description")),
        ("Design Highlight", package.get("design_highlight")),
        ("Typical Scenario", package.get("typical_scenario")),
        ("Scorecard Summary", package.get("scorecard")),
    ]
    body = "".join(
        f'<p><span class="label">{html_escape(label)}</span><br>{html_escape(value or "Not specified")}</p>'
        for label, value in paragraphs
    )
    return f'<section class="panel"><h2>Activity Overview</h2>{body}</section>'


def branch_html(beat: dict[str, Any]) -> str:
    branches = beat.get("branches") if isinstance(beat.get("branches"), list) else []
    if not branches:
        return (
            '<div class="branch-table-wrap"><table class="branch-table">'
            "<thead><tr><th>Branch</th><th>Child behavior</th><th>AI follow-up</th></tr></thead>"
            '<tbody><tr><td><span class="branch-label">Observed</span></td>'
            f'<td>{html_escape(beat.get("child") or "Unknown")}</td>'
            f'<td>{html_escape(beat.get("followup") or "Unknown")}</td></tr></tbody></table></div>'
        )
    rows = []
    for branch in branches:
        rows.append(
            "<tr>"
            f'<td><span class="branch-label">{html_escape(branch.get("label") or branch.get("token") or "Branch")}</span></td>'
            f'<td>{html_escape(branch.get("child") or "Unknown")}</td>'
            f'<td>{html_escape(branch.get("followup") or "Unknown")}</td>'
            "</tr>"
        )
    return (
        '<div class="branch-table-wrap"><table class="branch-table">'
        "<thead><tr><th>Branch</th><th>Child behavior</th><th>AI follow-up</th></tr></thead>"
        f'<tbody>{"".join(rows)}</tbody></table></div>'
    )


def render_runtime_flow(package: dict[str, Any]) -> str:
    items = []
    for index, beat in enumerate(package.get("runtime_beats", []), start=1):
        items.append(
            "<li>"
            f'<div class="beat-title"><span>{index:02d}</span><h3>{html_escape(beat.get("title") or "Runtime Beat")}</h3></div>'
            f'<p><span class="label">AI prompt</span><br>{html_escape(beat.get("ai") or "Unknown")}</p>'
            f"{branch_html(beat)}"
            f'<p><span class="label">Screen state</span><br>{html_escape(beat.get("screen") or "Unknown")}</p>'
            "</li>"
        )
    body = "".join(items) or "<li>No runtime beats parsed from prod.md.</li>"
    return f'<section class="panel"><h2>Runtime Flow</h2><ol class="runtime-list">{body}</ol></section>'


def render_scorecard(package: dict[str, Any]) -> str:
    rows = []
    for row in package.get("scorecard_rows", []):
        rows.append(
            "<tr>"
            f"<td>{html_escape(row.get('number'))}</td>"
            f"<td>{html_escape(row.get('dimension'))}</td>"
            f"<td>{html_escape(row.get('score'))}</td>"
            f"<td>{html_escape(row.get('notes'))}</td>"
            "</tr>"
        )
    body = "".join(rows) or '<tr><td colspan="4">No scorecard rows found.</td></tr>'
    return (
        '<section class="panel"><h2>Scorecard</h2>'
        '<table><thead><tr><th>#</th><th>Dimension</th><th>Result</th><th>Why</th></tr></thead>'
        f"<tbody>{body}</tbody></table></section>"
    )


def render_source_snapshot(title: str, text: str) -> str:
    return f"<details><summary>{html_escape(title)}</summary><pre>{html_escape(sanitize_snapshot(title, text))}</pre></details>"


def sanitize_snapshot(title: str, text: str) -> str:
    if not title.endswith(".meta.yaml"):
        return text
    return re.sub(
        r"(?m)^source_image:\s+/.*$",
        "source_image: '[existing local provenance path redacted in static export]'",
        text,
    )


def relative_link_from_export(binding_path: str) -> str:
    return f"../{binding_path}"


def storyboard_path(run_dir: Path, activity_id: str, filename: str) -> Path:
    for root in ("visual_storyboards_v2", "visual_storyboards"):
        candidate = run_dir / root / activity_id / filename
        if candidate.is_file():
            return candidate
    return run_dir / "__missing_storyboard_file__"


def storyboard_relative_path(run_dir: Path, activity_id: str, filename: str) -> str:
    path = storyboard_path(run_dir, activity_id, filename)
    return path.relative_to(run_dir).as_posix() if path.is_file() else ""


def storyboard_file_path(run_dir: Path, storyboard: dict[str, Any], field: str) -> Path:
    href = norm(storyboard.get(field))
    return run_dir / href if href else run_dir / "__missing_storyboard_file__"


def render_storyboard_captions(storyboard: dict[str, Any]) -> str:
    captions = storyboard.get("panel_captions", [])
    if not isinstance(captions, list) or not captions:
        return '<p class="subline">No panel captions were recorded.</p>'
    rows = []
    for item in captions:
        if not isinstance(item, dict):
            continue
        source = (
            f'<span class="storyboard-source">{html_escape(item.get("source"))}</span>'
            if item.get("source")
            else ""
        )
        rows.append(
            "<li>"
            f'<span class="storyboard-panel-number">{html_escape(item.get("number"))}</span>'
            "<div>"
            f"<strong>{html_escape(item.get('title') or 'Panel')}</strong>"
            f"<p>{html_escape(item.get('caption') or '')}</p>"
            f"{source}"
            "</div>"
            "</li>"
        )
    return f'<ol class="storyboard-caption-list">{"".join(rows)}</ol>' if rows else '<p class="subline">No panel captions were recorded.</p>'


def render_storyboard_section(run_dir: Path, package: dict[str, Any]) -> str:
    storyboard = package.get("storyboard") or {}
    if not storyboard:
        return ""
    image_path = storyboard_file_path(run_dir, storyboard, "image_href")
    prompt_path = storyboard_file_path(run_dir, storyboard, "prompt_href")
    meta_path = storyboard_file_path(run_dir, storyboard, "meta_href")
    image = (
        f'<img src="{data_uri(image_path)}" alt="Review-only mechanism storyboard for {html_escape(package.get("activity_name"))}">'
        if image_path.is_file()
        else '<p class="subline">Storyboard prompt ready; image not generated yet.</p>'
    )
    fields = {
        "Status": storyboard.get("status") or "Unknown",
        "Version": storyboard.get("version") or "Unknown",
        "Tool": storyboard.get("tool") or "Unknown",
        "Target model": storyboard.get("target_model") or "Unknown",
        "Actual model": storyboard.get("actual_model") or "Unknown",
        "Generated": storyboard.get("generated_at") or "Unknown",
    }
    meta = "".join(
        f"<div><span>{html_escape(label)}</span><strong>{html_escape(value)}</strong></div>"
        for label, value in fields.items()
    )
    links = []
    for label, path in [
        ("mechanism_grid.prompt.md", prompt_path),
        ("mechanism_grid.meta.yaml", meta_path),
        ("mechanism_grid.png", image_path),
    ]:
        if path.is_file():
            rel_path = path.relative_to(run_dir).as_posix()
            links.append(f'<a href="{html_escape(relative_link_from_export(rel_path))}">{html_escape(label)}: <code>{html_escape(rel_path)}</code></a>')
    snapshots = ""
    if prompt_path.is_file():
        snapshots += render_source_snapshot("mechanism_grid.prompt.md", read_text(prompt_path))
    if meta_path.is_file():
        snapshots += render_source_snapshot("mechanism_grid.meta.yaml", read_text(meta_path))
    return (
        '<section class="panel">'
        '<h2>Review-Only Mechanism Storyboard</h2>'
        '<p class="storyboard-note">This storyboard is a review artifact, not runtime UI. It explains the activity mechanism and should not be treated as a child-facing prebuilt asset.</p>'
        '<div class="storyboard-block">'
        f'<figure class="storyboard-figure">{image}</figure>'
        '<div>'
        f'<div class="meta-grid">{meta}</div>'
        f'{render_storyboard_captions(storyboard)}'
        f'<div class="path-list">{"".join(links)}</div>'
        '</div>'
        '</div>'
        f'{snapshots}'
        '</section>'
    )


def render_provenance_links(binding: dict[str, Any]) -> str:
    links = []
    for label, field in [
        ("spec.md", "spec_path"),
        ("prod.md", "prod_path"),
        ("asset.meta.yaml", "meta_path"),
        ("contact_sheet.prompt.md", "prompt_path"),
        ("contact_sheet.png", "image_path"),
    ]:
        href = relative_link_from_export(binding[field])
        links.append(f'<a href="{html_escape(href)}">{html_escape(label)}: <code>{html_escape(binding[field])}</code></a>')
    return '<div class="path-list">' + "".join(links) + "</div>"


def render_activity_html(run_dir: Path, binding: dict[str, Any], package: dict[str, Any]) -> str:
    image_uri = data_uri(run_dir / binding["image_path"])
    spec_text = read_text(run_dir / binding["spec_path"])
    prod_text = read_text(run_dir / binding["prod_path"])
    meta_text = read_text(run_dir / binding["meta_path"])
    prompt_text = read_text(run_dir / binding["prompt_path"])
    title = html_escape(package["activity_name"])
    activity_id = html_escape(binding["activity_id"])
    asset_id = html_escape(binding["asset_id"])
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} - Static Activity Export</title>
  <style>{BASE_CSS}</style>
</head>
<body>
  <main class="page">
    <header class="hero">
      <p class="eyebrow">WonderLens Static Activity Export</p>
      <h1>{title}</h1>
      <p class="subline">{activity_id} - integrated asset {asset_id}</p>
    </header>
    <section class="layout">
      <figure class="asset-panel">
        <img src="{image_uri}" alt="Contact sheet for {asset_id}">
        <figcaption>{asset_id} - {html_escape(binding.get("asset_type"))}</figcaption>
      </figure>
      <article class="summary-panel">
        {render_metadata(package, binding)}
        {render_asset_contract(binding)}
      </article>
    </section>
    {render_overview(package)}
    {render_storyboard_section(run_dir, package)}
    {render_runtime_flow(package)}
    {render_scorecard(package)}
    <section class="panel">
      <h2>File Provenance</h2>
      {render_provenance_links(binding)}
    </section>
    <section class="panel source-panel">
      <h2>Source Files</h2>
      {render_source_snapshot("spec.md", spec_text)}
      {render_source_snapshot("prod.md", prod_text)}
      {render_source_snapshot("asset.meta.yaml", meta_text)}
      {render_source_snapshot("contact_sheet.prompt.md", prompt_text)}
    </section>
  </main>
</body>
</html>
"""


def write_exports(run_dir: Path) -> dict[str, Any]:
    repo_root = run_dir.parents[1]
    binding_manifest = load_yaml(run_dir / "integrated_assets" / "asset_bindings.yaml")
    if not binding_manifest:
        raise SystemExit("Missing integrated_assets/asset_bindings.yaml. Run integrate_generated_assets.py first.")
    run_manifest = load_yaml(run_dir / "run_manifest.yaml")
    activities = run_manifest_entry_by_activity(run_manifest)
    export_dir = run_dir / "activity_exports"
    export_dir.mkdir(parents=True, exist_ok=True)
    entries = []
    binding_entries = [entry for entry in binding_manifest.get("entries", []) if isinstance(entry, dict)]
    activity_ids = [norm(entry.get("activity_id")) for entry in binding_entries]
    duplicate_activity_ids = {activity_id for activity_id in activity_ids if activity_ids.count(activity_id) > 1}
    for binding in binding_entries:
        if not isinstance(binding, dict):
            continue
        activity_id = norm(binding.get("activity_id"))
        asset_id = norm(binding.get("asset_id"))
        activity_entry = activities.get(activity_id)
        if not activity_entry:
            raise SystemExit(f"Activity missing from run_manifest.yaml: {activity_id}")
        package = collect_activity_package(repo_root, run_dir, activity_entry)
        html_text = render_activity_html(run_dir, binding, package)
        slug = activity_slug(activity_id)
        if activity_id in duplicate_activity_ids:
            slug = f"{slug}__{activity_slug(asset_id)}"
        html_path = export_dir / f"{slug}.html"
        html_path.write_text(html_text)
        entries.append(
            {
                "activity_id": activity_id,
                "activity_name": package.get("activity_name"),
                "asset_id": asset_id,
                "html_path": f"activity_exports/{html_path.name}",
                "package_path": binding.get("package_path"),
                "image_path": binding.get("image_path"),
                "embedded_image": True,
                "storyboard_image_path": storyboard_relative_path(run_dir, activity_id, "mechanism_grid.png"),
                "storyboard_meta_path": storyboard_relative_path(run_dir, activity_id, "mechanism_grid.meta.yaml"),
                "storyboard_prompt_path": storyboard_relative_path(run_dir, activity_id, "mechanism_grid.prompt.md"),
                "embedded_storyboard": bool(storyboard_relative_path(run_dir, activity_id, "mechanism_grid.png")),
                "status": "exported",
            }
        )
    manifest = {
        "run_id": run_dir.name,
        "artifact_kind": "integrated_activity_html_exports",
        "source_binding_manifest": "integrated_assets/asset_bindings.yaml",
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "export_count": len(entries),
        "entries": entries,
    }
    write_yaml(export_dir / "export_manifest.yaml", manifest)
    return manifest


def validate_exports(run_dir: Path, expected_count: int | None = None) -> list[str]:
    issues: list[str] = []
    binding_manifest = load_yaml(run_dir / "integrated_assets" / "asset_bindings.yaml")
    export_manifest = load_yaml(run_dir / "activity_exports" / "export_manifest.yaml")
    binding_entries = [entry for entry in binding_manifest.get("entries", []) if isinstance(entry, dict)]
    entries = export_manifest.get("entries", [])
    if not isinstance(entries, list):
        return ["export_manifest entries is not a list"]
    html_files = sorted((run_dir / "activity_exports").glob("*.html"))

    def pair_key(entry: dict[str, Any]) -> tuple[str, str]:
        return (norm(entry.get("activity_id")), norm(entry.get("asset_id")))

    binding_pair_list = [pair_key(entry) for entry in binding_entries]
    binding_pairs = set(binding_pair_list)
    duplicate_binding_pairs = sorted({pair for pair in binding_pair_list if binding_pair_list.count(pair) > 1})
    if duplicate_binding_pairs:
        issues.append(f"duplicate binding activity/asset pair entries: {duplicate_binding_pairs}")
    binding_by_pair = dict(zip(binding_pair_list, binding_entries))
    expected_total = expected_count if expected_count is not None else len(binding_entries)
    export_pair_list = [
        pair_key(entry)
        for entry in entries
        if isinstance(entry, dict)
    ]
    export_pairs = set(export_pair_list)
    duplicate_pairs = sorted({pair for pair in export_pair_list if export_pair_list.count(pair) > 1})
    if duplicate_pairs:
        issues.append(f"duplicate export activity/asset pair entries: {duplicate_pairs}")
    html_path_list = [
        norm(entry.get("html_path"))
        for entry in entries
        if isinstance(entry, dict)
    ]
    duplicate_html_paths = sorted({path for path in html_path_list if path and html_path_list.count(path) > 1})
    if duplicate_html_paths:
        issues.append(f"duplicate export HTML paths: {duplicate_html_paths}")
    if export_pairs != binding_pairs:
        missing = sorted(binding_pairs - export_pairs)
        extra = sorted(export_pairs - binding_pairs)
        issues.append(
            "export entries do not match binding activity/asset pairs"
            f"; missing={missing}; extra={extra}"
        )
    if export_manifest.get("export_count") != len(entries):
        issues.append("export_count does not match manifest entries")
    if len(entries) != expected_total:
        issues.append(f"expected {expected_total} export entries, found {len(entries)}")
    if len(html_files) != expected_total:
        issues.append(f"expected {expected_total} HTML files, found {len(html_files)}")
    for entry in entries:
        if not isinstance(entry, dict):
            issues.append("export entry is not a mapping")
            continue
        activity_id = norm(entry.get("activity_id"))
        asset_id = norm(entry.get("asset_id"))
        label = f"{activity_id}/{asset_id}"
        binding = binding_by_pair.get((activity_id, asset_id))
        if not activity_id or not asset_id:
            issues.append(f"{label}: missing activity_id or asset_id")
            continue
        if not binding:
            issues.append(f"{label}: missing matching binding")
            continue
        if norm(entry.get("image_path")) != norm(binding.get("image_path")):
            issues.append(f"{label}: image_path does not match binding")
        html_path = run_dir / norm(entry.get("html_path"))
        if not html_path.exists():
            issues.append(f"{label}: missing HTML at {entry.get('html_path')}")
            continue
        text = html_path.read_text(errors="replace")
        required = [
            "<!doctype html>",
            '<html lang="en">',
            activity_id,
            asset_id,
            "data:image/png;base64,",
            "Static Activity Export",
            "Integrated Prebuilt Asset",
            "Fallback",
            "Runtime Flow",
            "Scorecard",
            "Source Files",
        ]
        for token in required:
            if token not in text:
                issues.append(f"{label}: HTML missing {token}")
        expected_image = data_uri(run_dir / norm(binding.get("image_path")))
        if expected_image not in text:
            issues.append(f"{label}: embedded image does not match {binding.get('image_path')}")
        storyboard_image = storyboard_path(run_dir, activity_id, "mechanism_grid.png")
        if storyboard_image.is_file():
            expected_storyboard = data_uri(storyboard_image)
            if "Review-Only Mechanism Storyboard" not in text:
                issues.append(f"{label}: HTML missing Review-Only Mechanism Storyboard")
            if "review artifact, not runtime UI" not in text:
                issues.append(f"{label}: HTML missing storyboard review-only disclaimer")
            if expected_storyboard not in text:
                issues.append(f"{label}: storyboard image does not match {storyboard_image.relative_to(run_dir)}")
        if re.search(r'(?:src|href)=["\']https?://', text, re.I):
            issues.append(f"{label}: HTML references an external URL")
        if "cdn." in text.lower() or "@import" in text.lower():
            issues.append(f"{label}: HTML appears to reference external styling assets")
        if "{{" in text:
            issues.append(f"{label}: HTML contains unresolved placeholder braces")
        if "/Users/" in text:
            issues.append(f"{label}: HTML contains a local user path")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate", action="store_true", help="Validate existing HTML exports instead of regenerating.")
    parser.add_argument("run_dir", type=Path, help="Path to runs/<run_id>")
    args = parser.parse_args()
    run_dir = args.run_dir if args.run_dir.is_absolute() else Path.cwd() / args.run_dir
    if args.validate:
        issues = validate_exports(run_dir)
        if issues:
            print("FAIL activity HTML exports:", file=sys.stderr)
            for issue in issues:
                print(f"- {issue}", file=sys.stderr)
            raise SystemExit(1)
        print("PASS activity HTML exports: 12 files.")
        return
    manifest = write_exports(run_dir)
    issues = validate_exports(run_dir)
    if issues:
        print("FAIL activity HTML exports:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Exported {manifest['export_count']} activity HTML files.")
    print(f"Wrote {(run_dir / 'activity_exports' / 'export_manifest.yaml').relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
