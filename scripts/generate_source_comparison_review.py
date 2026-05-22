#!/usr/bin/env python3
"""Generate a product-facing source-to-activity comparison page."""

from __future__ import annotations

import argparse
import base64
import html
import re
import sys
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "PyYAML is required. Install pyyaml or run from the repo environment "
        "used for activity metadata validation."
    ) from exc


DEFAULT_OUTPUT = "source_comparison/product_review_matrix.html"
XLSX_NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}

SOURCE_NAME = "活动名称"
SOURCE_FORM = "形式(单选)"
SOURCE_MECHANIC = "机制(Mechanic)(单选)"
SOURCE_SCREEN_DEPENDENCE = "对屏幕的依赖度（特指视觉展示，不包括拍照行为）"
SOURCE_DESCRIPTION = "活动简介/举例"
SOURCE_NOTES = "备注"

MECHANIC_MAP = {
    "识别/计数": "enumerate",
    "比较/对比": "compare",
    "收集/配对": "collect",
    "排序/整理": "sort",
    "推理/演绎": "deduce",
    "搭建/创意": "build",
    "预测/计划": "predict",
    "选择/决策": "decide",
    "记忆/回顾": "remember",
    "语言/叙事": "imagine",
    "关爱/共情": "care",
    "动作/声音": "motion_voice",
}

STATUS_ORDER = {
    "Missing generated": 0,
    "Category + mechanic changed": 1,
    "Category changed": 2,
    "Mechanic changed": 3,
    "Capability-dependent": 4,
    "Matches": 5,
}
INTENT_STATUSES = {"aligned", "minor_adaptation", "intent_drift", "needs_product_decision"}
INTENT_SEVERITIES = {"none", "low", "medium", "high"}


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def norm(value: Any) -> str:
    return " ".join(str(value or "").split())


def truncate(value: str, limit: int = 160) -> str:
    text = norm(value)
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "..."


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    return data if isinstance(data, dict) else {}


def load_intent_audit(path: Path | None) -> dict[int, dict[str, Any]]:
    if not path:
        return {}
    data = load_yaml(path)
    entries = data.get("entries", [])
    by_row: dict[int, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        source_row = entry.get("source_row")
        if isinstance(source_row, int) or str(source_row).isdigit():
            by_row[int(source_row)] = entry
    return by_row


def col_to_index(col: str) -> int:
    index = 0
    for char in col:
        index = index * 26 + ord(char) - 64
    return index - 1


def read_source_workbook(path: Path) -> list[dict[str, Any]]:
    """Read the first worksheet in a minimal XLSX without third-party parsers."""
    with zipfile.ZipFile(path) as zf:
        shared_strings = []
        if "xl/sharedStrings.xml" in zf.namelist():
            shared_root = ET.fromstring(zf.read("xl/sharedStrings.xml"))
            for item in shared_root.findall("m:si", XLSX_NS):
                shared_strings.append("".join(t.text or "" for t in item.findall(".//m:t", XLSX_NS)))

        workbook_root = ET.fromstring(zf.read("xl/workbook.xml"))
        rels_root = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
        rel_targets = {rel.attrib["Id"]: rel.attrib["Target"] for rel in rels_root}
        sheet = workbook_root.find("m:sheets/m:sheet", XLSX_NS)
        if sheet is None:
            return []
        rel_id = sheet.attrib["{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"]
        sheet_path = "xl/" + rel_targets[rel_id].lstrip("/")
        sheet_root = ET.fromstring(zf.read(sheet_path))

        raw_rows: list[list[str]] = []
        for row in sheet_root.findall("m:sheetData/m:row", XLSX_NS):
            values: dict[int, str] = {}
            for cell in row.findall("m:c", XLSX_NS):
                ref = cell.attrib.get("r", "")
                match = re.match(r"([A-Z]+)(\d+)", ref)
                index = col_to_index(match.group(1)) if match else len(values)
                value_node = cell.find("m:v", XLSX_NS)
                inline_node = cell.find("m:is", XLSX_NS)
                cell_type = cell.attrib.get("t")
                value = ""
                if cell_type == "s" and value_node is not None:
                    value = shared_strings[int(value_node.text or "0")]
                elif cell_type == "inlineStr" and inline_node is not None:
                    value = "".join(t.text or "" for t in inline_node.findall(".//m:t", XLSX_NS))
                elif value_node is not None:
                    value = value_node.text or ""
                values[index] = value.strip()
            row_values = [values.get(i, "") for i in range(max(values.keys(), default=-1) + 1)]
            if any(row_values):
                raw_rows.append(row_values)

    if not raw_rows:
        return []
    headers = raw_rows[0]
    rows = []
    for source_row, values in enumerate(raw_rows[1:], 1):
        padded = (values + [""] * len(headers))[: len(headers)]
        rows.append({headers[i] or f"col{i + 1}": padded[i] for i in range(len(headers))} | {"source_row": source_row})
    return rows


def source_category(raw: str) -> str:
    if raw.startswith("Cat 1"):
        return "cat1"
    if raw.startswith("Cat 3"):
        return "cat3"
    if raw.startswith("Cat 5"):
        return "cat5"
    return ""


def source_mechanic(raw: str) -> str:
    for label, value in MECHANIC_MAP.items():
        if label in raw:
            return value
    return ""


def parse_source_markdown(repo_root: Path) -> dict[str, dict[str, Any]]:
    text = (repo_root / "inputs" / "source_activity_concepts.md").read_text()
    by_slug: dict[str, dict[str, Any]] = {}
    for match in re.finditer(r"^###\s+(source_[^\n]+)\n(.*?)(?=^###\s+source_|\Z)", text, re.S | re.M):
        slug = match.group(1)
        block = match.group(2)
        fields: dict[str, Any] = {"slug": slug}
        for line in block.splitlines():
            row_match = re.match(r"^\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|$", line)
            if not row_match:
                continue
            key = row_match.group(1).strip()
            value = row_match.group(2).strip()
            if key not in ("Field", "---"):
                fields[key] = value
        by_slug[slug] = fields
    return by_slug


def source_markdown_by_row(repo_root: Path) -> dict[int, dict[str, Any]]:
    by_row = {}
    for fields in parse_source_markdown(repo_root).values():
        if str(fields.get("source_row", "")).isdigit():
            by_row[int(fields["source_row"])] = fields
    return by_row


def adaptation_briefs_by_source(run_dir: Path) -> dict[str, dict[str, Any]]:
    briefs = {}
    for path in sorted((run_dir / "adaptation_briefs").glob("*.yaml")):
        data = load_yaml(path).get("adaptation_brief", {})
        if not isinstance(data, dict):
            continue
        source = data.get("source", {})
        concept_source = source.get("concept_source", "") if isinstance(source, dict) else ""
        slug = concept_source.split("#")[-1] if "#" in concept_source else ""
        if slug:
            briefs[slug] = dict(data, brief_path=path.relative_to(run_dir).as_posix())
    return briefs


def generated_entries_by_source(run_dir: Path) -> dict[str, dict[str, Any]]:
    manifest = load_yaml(run_dir / "run_manifest.yaml")
    outputs = manifest.get("outputs", {})
    entries = outputs.get("generated_activities", []) if isinstance(outputs, dict) else []
    by_source = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        assignment = norm(entry.get("assignment"))
        match = re.search(r"concept_source=inputs/source_activity_concepts\.md#([^,\s]+)", assignment)
        if match:
            by_source[match.group(1)] = entry
    return by_source


def exports_by_activity(run_dir: Path) -> dict[str, dict[str, Any]]:
    manifest = load_yaml(run_dir / "activity_exports" / "export_manifest.yaml")
    entries = manifest.get("entries", [])
    return {
        norm(entry.get("activity_id")): entry
        for entry in entries
        if isinstance(entry, dict) and norm(entry.get("activity_id"))
    }


def storyboards_by_activity(run_dir: Path) -> dict[str, dict[str, Any]]:
    manifest = load_yaml(run_dir / "visual_storyboards" / "storyboard_manifest.yaml")
    entries = manifest.get("entries", [])
    by_activity: dict[str, dict[str, Any]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        activity_id = norm(entry.get("activity_id"))
        if activity_id:
            by_activity[activity_id] = entry
    return by_activity


def package_title(run_dir: Path, entry: dict[str, Any]) -> str:
    package_path = norm(entry.get("activity_path"))
    package_dir = Path(package_path)
    if not package_dir.is_absolute():
        package_dir = run_dir.parent.parent / package_dir if package_path.startswith("runs/") else run_dir / package_dir
    prod = package_dir / "prod.md"
    if prod.exists():
        match = re.search(r"^##\s+(.+)$", prod.read_text(), re.M)
        if match:
            return match.group(1).strip()
    return norm(entry.get("activity_id")) or "Unknown"


def package_brief(run_dir: Path, entry: dict[str, Any], fallback: str) -> str:
    package_path = norm(entry.get("activity_path"))
    package_dir = Path(package_path)
    if not package_dir.is_absolute():
        package_dir = run_dir.parent.parent / package_dir if package_path.startswith("runs/") else run_dir / package_path
    prod = package_dir / "prod.md"
    if not prod.exists():
        return fallback
    text = prod.read_text()
    match = re.search(r"\*\*1\. Brief Description\*\*\s*(.*?)(?=\n\*\*|\n###|\Z)", text, re.S)
    return truncate(match.group(1), 190) if match else fallback


def data_uri(path: Path) -> str:
    if not path.is_file():
        return ""
    return f"data:image/png;base64,{base64.b64encode(path.read_bytes()).decode('ascii')}"


def rel_link(from_dir: Path, target: str) -> str:
    return "../" + target if target else ""


def classify_row(source_cat: str, source_mech: str, generated_cat: str, generated_mech: str, brief: dict[str, Any], generated: bool) -> str:
    if not generated:
        return "Missing generated"
    capability_dependent = (
        norm(brief.get("assignment_type")) == "capability_probe"
        or norm(brief.get("readiness")).startswith("resolved_from_blocked")
    )
    if capability_dependent:
        return "Capability-dependent"
    category_changed = bool(source_cat and generated_cat and source_cat != generated_cat)
    mechanic_changed = bool(source_mech and generated_mech and source_mech != generated_mech)
    if category_changed and mechanic_changed:
        return "Category + mechanic changed"
    if category_changed:
        return "Category changed"
    if mechanic_changed:
        return "Mechanic changed"
    return "Matches"


def review_question(status: str, source_cat: str, source_mech: str, generated_cat: str, generated_mech: str) -> str:
    if status == "Matches":
        return "Confirm this generated package is an acceptable representation of the source idea."
    if status == "Mechanic changed":
        return f"Approve mechanic realignment from {source_mech} to {generated_mech}?"
    if status == "Category changed":
        return f"Approve category change from {source_cat} to {generated_cat}?"
    if status == "Category + mechanic changed":
        return "Approve both the category and mechanic realignment?"
    if status == "Capability-dependent":
        return "Confirm product support, or keep this as a concept/probe until runtime capability is approved."
    return "Generate or map a package for this source row."


def change_note(status: str, source_cat: str, source_mech: str, generated_cat: str, generated_mech: str) -> str:
    if status == "Matches":
        return "Category and mechanic preserved."
    if status == "Mechanic changed":
        return f"Mechanic changed from {source_mech} to {generated_mech}; source intent is preserved through the generated loop."
    if status == "Category changed":
        return f"Category changed from {source_cat} to {generated_cat}; review whether this runtime framing is acceptable."
    if status == "Category + mechanic changed":
        return f"Category {source_cat}->{generated_cat}; mechanic {source_mech}->{generated_mech}."
    if status == "Capability-dependent":
        return "The generated artifact is a product-decision/probe package, not a fully approved runtime implementation."
    return "No generated package found for this source row."


def intent_key(value: str) -> str:
    return norm(value) or "not_audited"


def intent_label(value: str) -> str:
    labels = {
        "aligned": "Aligned",
        "minor_adaptation": "Minor adaptation",
        "intent_drift": "Intent drift",
        "needs_product_decision": "Needs product decision",
        "not_audited": "Not audited",
    }
    return labels.get(intent_key(value), norm(value) or "Not audited")


def build_report(repo_root: Path, run_dir: Path, workbook_path: Path, intent_audit_path: Path | None = None) -> dict[str, Any]:
    workbook_rows = read_source_workbook(workbook_path)
    source_rows = source_markdown_by_row(repo_root)
    generated_by_source = generated_entries_by_source(run_dir)
    briefs = adaptation_briefs_by_source(run_dir)
    exports = exports_by_activity(run_dir)
    storyboards = storyboards_by_activity(run_dir)
    intent_audit = load_intent_audit(intent_audit_path)

    rows = []
    for workbook_row in workbook_rows:
        source_row_number = int(workbook_row["source_row"])
        source = source_rows.get(source_row_number, {})
        slug = norm(source.get("slug"))
        generated_entry = generated_by_source.get(slug, {})
        brief = briefs.get(slug, {})
        activity_id = norm(generated_entry.get("activity_id"))
        export = exports.get(activity_id, {})
        storyboard = storyboards.get(activity_id, {})
        audit_entry = intent_audit.get(source_row_number, {})

        original_category = source_category(norm(workbook_row.get(SOURCE_FORM)))
        original_mechanic = source_mechanic(norm(workbook_row.get(SOURCE_MECHANIC)))
        generated_category = norm(brief.get("category_decision"))
        generated_mechanic = norm(brief.get("canonical_mechanic"))
        status = classify_row(original_category, original_mechanic, generated_category, generated_mechanic, brief, bool(generated_entry))
        generated_name = package_title(run_dir, generated_entry) if generated_entry else ""
        generated_loop = package_brief(run_dir, generated_entry, norm(brief.get("core_promise"))) if generated_entry else ""

        image_path = norm(export.get("image_path"))
        storyboard_path = norm(export.get("storyboard_image_path") or storyboard.get("image_href"))
        row = {
            "source_row": source_row_number,
            "original_name": norm(workbook_row.get(SOURCE_NAME)),
            "original_intent": norm(workbook_row.get(SOURCE_DESCRIPTION)),
            "original_notes": norm(workbook_row.get(SOURCE_NOTES)),
            "original_category": original_category,
            "original_category_raw": norm(workbook_row.get(SOURCE_FORM)),
            "original_mechanic": original_mechanic,
            "original_mechanic_raw": norm(workbook_row.get(SOURCE_MECHANIC)),
            "screen_dependency": norm(workbook_row.get(SOURCE_SCREEN_DEPENDENCE)),
            "normalized_name": norm(source.get("activity_concept")),
            "generated_name": generated_name,
            "activity_id": activity_id,
            "generated_category": generated_category,
            "generated_mechanic": generated_mechanic,
            "assignment_type": norm(brief.get("assignment_type")),
            "readiness": norm(brief.get("readiness")),
            "product_capability_flags": brief.get("product_capability_flags") or [],
            "status": status,
            "status_key": status.lower().replace(" + ", "-").replace(" ", "-"),
            "what_changed": change_note(status, original_category, original_mechanic, generated_category, generated_mechanic),
            "review_question": review_question(status, original_category, original_mechanic, generated_category, generated_mechanic),
            "generated_loop": generated_loop,
            "reviewer_packet": norm(export.get("html_path")),
            "reviewer_packet_link": rel_link(run_dir / "source_comparison", norm(export.get("html_path"))),
            "package_path": norm(generated_entry.get("activity_path")),
            "brief_path": norm(brief.get("brief_path")),
            "contact_sheet_path": image_path,
            "storyboard_path": storyboard_path,
            "contact_sheet_data_uri": data_uri(run_dir / image_path) if image_path else "",
            "storyboard_data_uri": data_uri(run_dir / storyboard_path) if storyboard_path else "",
            "intent_status": intent_key(audit_entry.get("status", "")),
            "intent_severity": norm(audit_entry.get("severity")),
            "original_play_frame": norm(audit_entry.get("original_play_frame")),
            "generated_play_frame": norm(audit_entry.get("generated_play_frame")),
            "intent_preserved": audit_entry.get("preserved") if isinstance(audit_entry.get("preserved"), list) else [],
            "intent_drift_notes": audit_entry.get("drift") if isinstance(audit_entry.get("drift"), list) else [],
            "intent_recommendation": norm(audit_entry.get("recommendation")),
            "intent_review_question": norm(audit_entry.get("product_review_question")),
            "intent_audit_activity_id": norm(audit_entry.get("activity_id")),
            "intent_audit_present": bool(audit_entry),
        }
        rows.append(row)

    intent_review_statuses = {"intent_drift", "needs_product_decision"}
    summary = {
        "source_rows": len(rows),
        "covered_rows": sum(1 for row in rows if row["activity_id"]),
        "missing_generated": sum(1 for row in rows if row["status"] == "Missing generated"),
        "matches": sum(1 for row in rows if row["status"] == "Matches"),
        "mechanic_changed": sum(1 for row in rows if row["status"] in ("Mechanic changed", "Category + mechanic changed")),
        "category_changed": sum(1 for row in rows if row["status"] in ("Category changed", "Category + mechanic changed")),
        "capability_dependent": sum(1 for row in rows if row["status"] == "Capability-dependent"),
        "intent_drift": sum(1 for row in rows if row["intent_status"] == "intent_drift"),
        "intent_needs_product_decision": sum(1 for row in rows if row["intent_status"] == "needs_product_decision"),
        "needs_review": sum(
            1
            for row in rows
            if row["status"] != "Matches" or row["intent_status"] in intent_review_statuses
        ),
    }
    return {
        "run_id": run_dir.name,
        "workbook_name": workbook_path.name,
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "summary": summary,
        "rows": rows,
        "visual_examples": select_visual_examples(rows),
        "intent_audit_provided": bool(intent_audit_path),
        "intent_audit_path": norm(intent_audit_path),
    }


def select_visual_examples(rows: list[dict[str, Any]], limit: int = 5) -> list[dict[str, Any]]:
    selected: list[dict[str, Any]] = []

    def add_first(predicate) -> None:
        if len(selected) >= limit:
            return
        for row in rows:
            if row in selected:
                continue
            if predicate(row):
                selected.append(row)
                return

    add_first(lambda row: row["status"] == "Matches" and row["contact_sheet_data_uri"] and row["storyboard_data_uri"])
    add_first(lambda row: row["status"] in ("Mechanic changed", "Category changed", "Category + mechanic changed") and (row["contact_sheet_data_uri"] or row["storyboard_data_uri"]))
    add_first(lambda row: row["status"] == "Capability-dependent" and row["storyboard_data_uri"])
    add_first(lambda row: row["original_category"] == "cat5" and row["storyboard_data_uri"])
    add_first(lambda row: row["reviewer_packet"] and (row["contact_sheet_data_uri"] or row["storyboard_data_uri"]))

    for row in rows:
        if len(selected) >= limit:
            break
        if row not in selected and (row["contact_sheet_data_uri"] or row["storyboard_data_uri"]):
            selected.append(row)
    return selected[:limit]


def status_badge(status: str) -> str:
    return f'<span class="status-badge status-{esc(status.lower().replace(" + ", "-").replace(" ", "-"))}">{esc(status)}</span>'


def intent_badge(status: str, severity: str = "") -> str:
    key = intent_key(status)
    classes = f"intent-badge intent-{esc(key)}"
    if severity:
        classes += f" severity-{esc(severity)}"
    return f'<span class="{classes}">{esc(intent_label(key))}</span>'


def metric(label: str, value: Any, tone: str = "") -> str:
    return f'<div class="metric {esc(tone)}"><span>{esc(label)}</span><strong>{esc(value)}</strong></div>'


def visual_card(row: dict[str, Any]) -> str:
    media = ""
    if row["contact_sheet_data_uri"]:
        media += (
            '<figure><img src="'
            + esc(row["contact_sheet_data_uri"])
            + '" alt="Prebuilt asset contact sheet for '
            + esc(row["generated_name"])
            + '"><figcaption>Prebuilt asset</figcaption></figure>'
        )
    if row["storyboard_data_uri"]:
        media += (
            '<figure><img src="'
            + esc(row["storyboard_data_uri"])
            + '" alt="Review-only mechanism storyboard for '
            + esc(row["generated_name"])
            + '"><figcaption>Review-only storyboard</figcaption></figure>'
        )
    packet = (
        f'<a class="inline-link" href="{esc(row["reviewer_packet_link"])}">Open reviewer packet</a>'
        if row["reviewer_packet_link"]
        else ""
    )
    return f"""
      <article class="visual-card">
        <div class="visual-copy">
          <p class="eyebrow">Row {esc(row["source_row"])} · {esc(row["original_name"])}</p>
          <h3>{esc(row["generated_name"] or row["normalized_name"])}</h3>
          <div>{status_badge(row["status"])}</div>
          <p>{esc(truncate(row["generated_loop"], 150))}</p>
          {packet}
        </div>
        <div class="visual-media">{media}</div>
      </article>
    """


def table_row(row: dict[str, Any]) -> str:
    packet = (
        f'<a href="{esc(row["reviewer_packet_link"])}">Packet</a>'
        if row["reviewer_packet_link"]
        else '<span class="muted">No packet</span>'
    )
    product_question = row["intent_review_question"] or row["review_question"]
    details = f"""
      <details>
        <summary>Details</summary>
        <div class="details-grid">
          <div><span>Original notes</span><p>{esc(row["original_notes"] or "None recorded.")}</p></div>
          <div><span>Source screen dependency</span><p>{esc(row["screen_dependency"] or "None recorded.")}</p></div>
          <div><span>Generated core loop</span><p>{esc(row["generated_loop"] or "Not generated.")}</p></div>
          <div><span>Original play frame</span><p>{esc(row["original_play_frame"] or "Not audited.")}</p></div>
          <div><span>Generated play frame</span><p>{esc(row["generated_play_frame"] or "Not audited.")}</p></div>
          <div><span>Intent drift notes</span><p>{esc("; ".join(row["intent_drift_notes"]) or "None recorded.")}</p></div>
          <div><span>Capability flags</span><p>{esc(", ".join(row["product_capability_flags"]) or "None")}</p></div>
          <div><span>Paths</span><p>{esc(row["package_path"] or "No package")}<br>{esc(row["brief_path"] or "No brief")}</p></div>
        </div>
      </details>
    """
    return f"""
      <tr data-status="{esc(row["status_key"])}" data-intent-status="{esc(row["intent_status"])}" data-review-needed="{str(row["status"] != "Matches" or row["intent_status"] in ("intent_drift", "needs_product_decision")).lower()}">
        <td class="row-number">{esc(row["source_row"])}</td>
        <td><strong>{esc(row["original_name"])}</strong><p>{esc(truncate(row["original_intent"], 130))}</p>{details}</td>
        <td><span>{esc(row["original_category"])}</span><code>{esc(row["original_mechanic"])}</code></td>
        <td><strong>{esc(row["generated_name"] or "Missing")}</strong><p class="activity-id">{esc(row["activity_id"] or "No activity ID")}</p></td>
        <td><span>{esc(row["generated_category"] or "N/A")}</span><code>{esc(row["generated_mechanic"] or "N/A")}</code></td>
        <td>{status_badge(row["status"])}<p>{esc(row["what_changed"])}</p></td>
        <td>{intent_badge(row["intent_status"], row["intent_severity"])}<p>{esc(row["intent_recommendation"] or "No source-intent audit note.")}</p></td>
        <td>{esc(product_question)}</td>
        <td>{packet}</td>
      </tr>
    """


def render_html(report: dict[str, Any]) -> str:
    summary = report["summary"]
    rows = report["rows"]
    visual_examples = report["visual_examples"]
    table_rows = "\n".join(table_row(row) for row in rows)
    visual_cards = "\n".join(visual_card(row) for row in visual_examples)
    css = """
:root {
  color-scheme: light;
  --paper: oklch(0.975 0.006 86);
  --surface: oklch(0.995 0.004 88);
  --surface-2: oklch(0.956 0.008 85);
  --ink: oklch(0.24 0.035 260);
  --muted: oklch(0.48 0.025 256);
  --line: oklch(0.88 0.012 83);
  --accent: oklch(0.48 0.145 248);
  --accent-soft: oklch(0.93 0.035 248);
  --green: oklch(0.45 0.105 153);
  --green-soft: oklch(0.93 0.035 153);
  --amber: oklch(0.62 0.12 72);
  --amber-soft: oklch(0.94 0.04 72);
  --red: oklch(0.54 0.14 30);
  --red-soft: oklch(0.94 0.035 30);
  --violet: oklch(0.50 0.12 300);
  --violet-soft: oklch(0.94 0.035 300);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
}
a { color: var(--accent); text-underline-offset: 3px; }
.page { width: min(1500px, calc(100vw - 32px)); margin: 0 auto; padding: 28px 0 48px; }
.hero { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(320px, .9fr); gap: 24px; align-items: end; padding-bottom: 22px; border-bottom: 1px solid var(--line); }
.eyebrow { margin: 0 0 7px; color: var(--accent); font-size: 11px; font-weight: 750; letter-spacing: .08em; text-transform: uppercase; }
h1 { margin: 0; max-width: 780px; font-size: 38px; line-height: 1.08; letter-spacing: 0; }
h2 { margin: 0; font-size: 20px; letter-spacing: 0; }
h3 { margin: 0; font-size: 16px; letter-spacing: 0; }
.intro { max-width: 74ch; margin: 12px 0 0; color: var(--muted); }
.metrics { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 8px; }
.metric { min-width: 0; padding: 13px 14px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); }
.metric span { display: block; color: var(--muted); font-size: 11px; font-weight: 700; text-transform: uppercase; }
.metric strong { display: block; margin-top: 4px; font-size: 22px; line-height: 1; font-variant-numeric: tabular-nums; }
.metric.warn { background: var(--amber-soft); }
.metric.good { background: var(--green-soft); }
.toolbar { position: sticky; top: 0; z-index: 3; display: flex; gap: 8px; align-items: center; flex-wrap: wrap; margin: 18px 0; padding: 10px; border: 1px solid var(--line); border-radius: 8px; background: color-mix(in oklch, var(--paper) 88%, transparent); backdrop-filter: blur(10px); }
button { border: 1px solid var(--line); border-radius: 7px; background: var(--surface); color: var(--ink); font: inherit; font-weight: 650; padding: 8px 11px; cursor: pointer; }
button:hover, button.active { border-color: var(--accent); background: var(--accent-soft); }
.count { margin-left: auto; color: var(--muted); font-variant-numeric: tabular-nums; }
.review-guide { display: grid; grid-template-columns: .92fr 1.08fr; gap: 12px; margin-top: 18px; }
.guide-panel { min-width: 0; padding: 13px 14px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); }
.guide-panel h2 { margin-bottom: 10px; }
.definition-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.definition-grid div { min-width: 0; }
.definition-grid dt { margin: 0 0 4px; color: var(--ink); font-weight: 760; }
.definition-grid dd { margin: 0; color: var(--muted); max-width: 42ch; }
.approval-list { margin: 0; padding-left: 18px; color: var(--muted); }
.approval-list li { margin: 0 0 7px; }
.approval-list li:last-child { margin-bottom: 0; }
.approval-list strong { color: var(--ink); }
.section { margin-top: 22px; }
.section-head { display: flex; align-items: baseline; justify-content: space-between; gap: 16px; margin-bottom: 10px; }
.section-head p { margin: 0; color: var(--muted); }
.visual-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.visual-card { display: grid; grid-template-columns: minmax(210px, .82fr) 1.18fr; gap: 14px; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); padding: 14px; }
.visual-copy { display: grid; align-content: start; gap: 9px; min-width: 0; }
.visual-copy p { margin: 0; color: var(--muted); }
.visual-media { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; align-items: start; }
.visual-media figure { margin: 0; min-width: 0; }
.visual-media img { display: block; width: 100%; aspect-ratio: 4 / 3; object-fit: contain; border: 1px solid var(--line); border-radius: 7px; background: var(--surface-2); }
.visual-media figcaption { margin-top: 5px; color: var(--muted); font-size: 12px; }
.inline-link { font-weight: 700; }
.table-wrap { overflow-x: auto; border: 1px solid var(--line); border-radius: 8px; background: var(--surface); }
table { width: 100%; border-collapse: collapse; min-width: 1240px; }
th, td { padding: 12px 13px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }
th { background: var(--surface-2); color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: .04em; }
td p { margin: 6px 0 0; color: var(--muted); max-width: 42ch; }
.row-number { color: var(--muted); font-variant-numeric: tabular-nums; }
code { display: inline-block; margin-top: 4px; padding: 2px 6px; border: 1px solid var(--line); border-radius: 5px; background: var(--surface-2); color: var(--ink); font-size: 12px; }
.activity-id { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 12px; overflow-wrap: anywhere; }
.status-badge { display: inline-flex; align-items: center; border-radius: 999px; padding: 4px 8px; font-size: 12px; font-weight: 760; white-space: nowrap; }
.status-matches { color: var(--green); background: var(--green-soft); }
.status-mechanic-changed, .status-category-changed, .status-category-mechanic-changed { color: var(--amber); background: var(--amber-soft); }
.status-capability-dependent { color: var(--violet); background: var(--violet-soft); }
.status-missing-generated { color: var(--red); background: var(--red-soft); }
.intent-badge { display: inline-flex; align-items: center; border-radius: 999px; padding: 4px 8px; font-size: 12px; font-weight: 760; white-space: nowrap; }
.intent-aligned { color: var(--green); background: var(--green-soft); }
.intent-minor_adaptation { color: var(--accent); background: var(--accent-soft); }
.intent-intent_drift { color: var(--red); background: var(--red-soft); }
.intent-needs_product_decision { color: var(--violet); background: var(--violet-soft); }
.intent-not_audited { color: var(--muted); background: var(--surface-2); }
details { margin-top: 8px; }
summary { color: var(--accent); cursor: pointer; font-weight: 700; }
.details-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-top: 10px; padding: 10px; border-radius: 7px; background: var(--surface-2); }
.details-grid span { display: block; color: var(--muted); font-size: 11px; font-weight: 750; text-transform: uppercase; }
.details-grid p { max-width: none; overflow-wrap: anywhere; }
.muted { color: var(--muted); }
tr.is-hidden { display: none; }
@media (max-width: 980px) {
  .hero, .visual-grid, .visual-card { grid-template-columns: 1fr; }
  .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .review-guide { grid-template-columns: 1fr; }
  .definition-grid { grid-template-columns: 1fr; }
}
"""
    js = """
const buttons = Array.from(document.querySelectorAll('[data-filter]'));
const rows = Array.from(document.querySelectorAll('tbody tr'));
const count = document.querySelector('[data-visible-count]');
function applyFilter(filter) {
  let visible = 0;
  rows.forEach((row) => {
    const status = row.dataset.status || '';
    const intentStatus = row.dataset.intentStatus || '';
    const reviewNeeded = row.dataset.reviewNeeded === 'true';
    const show = filter === 'all'
      || (filter === 'changed' && (status.includes('changed')))
      || (filter === 'capability' && status === 'capability-dependent')
      || (filter === 'intent-drift' && intentStatus === 'intent_drift')
      || (filter === 'intent-product' && intentStatus === 'needs_product_decision')
      || (filter === 'needs-review' && reviewNeeded)
      || status === filter;
    row.classList.toggle('is-hidden', !show);
    if (show) visible += 1;
  });
  buttons.forEach((button) => button.classList.toggle('active', button.dataset.filter === filter));
  if (count) count.textContent = `${visible} visible`;
}
buttons.forEach((button) => button.addEventListener('click', () => applyFilter(button.dataset.filter)));
applyFilter('all');
"""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Product Source Fidelity Review · {esc(report["run_id"])}</title>
  <style>{css}</style>
</head>
<body>
  <main class="page">
    <header class="hero">
      <div>
        <p class="eyebrow">Product Source Fidelity Review</p>
        <h1>Original activity concepts compared with generated WonderLens packages</h1>
        <p class="intro">One row per workbook activity. The table is intentionally compact: it highlights source coverage, category/mechanic changes, capability-dependent concepts, and direct links to reviewer packets when available.</p>
        <p class="intro">Source workbook: <strong>{esc(report["workbook_name"])}</strong>. Generated run: <strong>{esc(report["run_id"])}</strong>. Generated: {esc(report["created_at"])}.</p>
      </div>
      <div class="metrics">
        {metric("Source rows", summary["source_rows"])}
        {metric("Covered", summary["covered_rows"], "good")}
        {metric("Needs review", summary["needs_review"], "warn")}
        {metric("Capability-dependent", summary["capability_dependent"], "warn")}
        {metric("Intent drift", summary["intent_drift"], "warn")}
      </div>
    </header>

    <nav class="toolbar" aria-label="Comparison filters">
      <button type="button" data-filter="all">All</button>
      <button type="button" data-filter="matches">Matches</button>
      <button type="button" data-filter="changed">Changed</button>
      <button type="button" data-filter="capability">Capability-dependent</button>
      <button type="button" data-filter="intent-drift">Intent drift</button>
      <button type="button" data-filter="intent-product">Intent product decision</button>
      <button type="button" data-filter="needs-review">Needs review</button>
      <span class="count" data-visible-count></span>
    </nav>

    <section class="review-guide" aria-label="Review guidance">
      <section class="guide-panel" aria-labelledby="status-definitions-title">
        <h2 id="status-definitions-title">Status Definitions</h2>
        <dl class="definition-grid">
          <div>
            <dt>Needs review</dt>
            <dd>Needs review means rows where product should make an explicit approval decision before treating the generated package as accepted.</dd>
          </div>
          <div>
            <dt>Capability-dependent</dt>
            <dd>Capability-dependent means the generated packet depends on product support, permissions, materials, or runtime behavior that is not yet fully approved.</dd>
          </div>
          <div>
            <dt>Intent drift</dt>
            <dd>Intent drift means the source-intent audit found a meaningful mismatch between the original play frame and the generated activity flow.</dd>
          </div>
        </dl>
      </section>
      <section class="guide-panel" aria-labelledby="approval-checklist-title">
        <h2 id="approval-checklist-title">Approval Checklist</h2>
        <ul class="approval-list">
          <li><strong>Approve source-intent coverage:</strong> the generated loop preserves the workbook idea's core child action, role/frame, and learning interaction.</li>
          <li><strong>Approve category/mechanic changes:</strong> any changed category or mechanic is an accepted runtime realignment, not accidental drift.</li>
          <li><strong>Approve capability assumptions and minimum contracts:</strong> capability-dependent rows can ship as probes or need product support before runtime use.</li>
          <li><strong>Approve reviewer-packet readiness:</strong> the standalone packet gives enough runtime beats, branch handling, assets/storyboards, and fallback behavior for review.</li>
        </ul>
      </section>
    </section>

    <section class="section" aria-labelledby="visual-examples-title">
      <div class="section-head">
        <h2 id="visual-examples-title">Visual Examples</h2>
        <p>{esc(len(visual_examples))} representative examples, not every asset or storyboard</p>
      </div>
      <div class="visual-grid">{visual_cards}</div>
    </section>

    <section class="section" aria-labelledby="matrix-title">
      <div class="section-head">
        <h2 id="matrix-title">Review Matrix</h2>
        <p>Use changed and capability filters first.</p>
      </div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Row</th>
              <th>Original design</th>
              <th>Original cat/mechanic</th>
              <th>Generated package</th>
              <th>Generated cat/mechanic</th>
              <th>Fidelity status</th>
              <th>Intent alignment</th>
              <th>Approval needed</th>
              <th>Reviewer packet</th>
            </tr>
          </thead>
          <tbody>{table_rows}</tbody>
        </table>
      </div>
    </section>
  </main>
  <script>{js}</script>
</body>
</html>
"""


def validate_report(report: dict[str, Any]) -> list[str]:
    issues = []
    summary = report.get("summary", {})
    rows = report.get("rows", [])
    visual_examples = report.get("visual_examples", [])
    if summary.get("source_rows") != len(rows):
        issues.append("summary source row count does not match row list")
    if summary.get("source_rows") != summary.get("covered_rows"):
        issues.append("not all source rows are covered")
    if not visual_examples:
        issues.append("no visual examples selected")
    if len(visual_examples) > 5:
        issues.append("too many visual examples selected")
    if any("/Users/" in norm(row.get("reviewer_packet_link")) for row in rows):
        issues.append("local absolute path leaked into reviewer packet links")
    if summary.get("needs_review", 0) <= 0:
        issues.append("no review-needed rows classified")
    if report.get("intent_audit_provided"):
        missing_audit = [row for row in rows if not row.get("intent_audit_present")]
        if missing_audit:
            issues.append("intent audit does not cover every source row")
        for row in rows:
            if not row.get("intent_audit_present"):
                continue
            status = norm(row.get("intent_status"))
            severity = norm(row.get("intent_severity"))
            audit_activity_id = norm(row.get("intent_audit_activity_id"))
            activity_id = norm(row.get("activity_id"))
            if status not in INTENT_STATUSES:
                issues.append(f"invalid intent status for source row {row.get('source_row')}: {status}")
            if severity not in INTENT_SEVERITIES:
                issues.append(f"invalid intent severity for source row {row.get('source_row')}: {severity}")
            if audit_activity_id != activity_id:
                issues.append(
                    f"activity_id mismatch for source row {row.get('source_row')}: "
                    f"audit={audit_activity_id or 'missing'} generated={activity_id or 'missing'}"
                )
    return issues


def validate_html(html_text: str, report: dict[str, Any]) -> list[str]:
    issues = []
    required = [
        "Product Source Fidelity Review",
        "Visual Examples",
        "Review Matrix",
        'data-filter="changed"',
        'data-filter="capability"',
        "Reviewer packet",
        "Status Definitions",
        "Needs review means rows where product should make an explicit approval decision",
        "Capability-dependent means the generated packet depends on product support",
        "Intent drift means the source-intent audit found a meaningful mismatch",
        "Approval Checklist",
        "Approve source-intent coverage",
        "Approve category/mechanic changes",
        "Approve capability assumptions and minimum contracts",
        "Approve reviewer-packet readiness",
        "Approval needed",
    ]
    if report.get("intent_audit_provided"):
        required.extend(["Intent alignment", 'data-filter="intent-drift"'])
    for marker in required:
        if marker not in html_text:
            issues.append(f"HTML missing {marker}")
    if "/Users/" in html_text:
        issues.append("HTML leaks a local absolute path")
    if re.search(r'(?:src|href)=["\']https?://', html_text, re.I):
        issues.append("HTML references an external URL")
    if html_text.count("<tr data-status=") != report.get("summary", {}).get("source_rows"):
        issues.append("HTML row count does not match source row count")
    if "data:image/png;base64," not in html_text:
        issues.append("HTML does not embed visual example images")
    if "th { position: sticky" in html_text:
        issues.append("HTML uses sticky table headers that can overlap the first matrix rows")
    if report.get("intent_audit_provided"):
        for row in report.get("rows", []):
            if not row.get("intent_audit_present"):
                continue
            source_row = row.get("source_row")
            for label, key in (
                ("intent recommendation", "intent_recommendation"),
                ("intent review question", "intent_review_question"),
                ("original play frame", "original_play_frame"),
                ("generated play frame", "generated_play_frame"),
            ):
                value = norm(row.get(key))
                if value and esc(value) not in html_text:
                    issues.append(f"HTML missing {label} for source row {source_row}")
    return issues


def write_report(
    repo_root: Path,
    run_dir: Path,
    workbook_path: Path,
    output_rel: str = DEFAULT_OUTPUT,
    intent_audit_path: Path | None = None,
) -> Path:
    report = build_report(repo_root, run_dir, workbook_path, intent_audit_path=intent_audit_path)
    issues = validate_report(report)
    if issues:
        raise SystemExit("Source comparison validation failed before render:\n" + "\n".join(f"- {issue}" for issue in issues))
    html_text = "\n".join(line.rstrip() for line in render_html(report).splitlines()) + "\n"
    html_issues = validate_html(html_text, report)
    if html_issues:
        raise SystemExit("Source comparison HTML validation failed:\n" + "\n".join(f"- {issue}" for issue in html_issues))
    output_path = run_dir / output_rel
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html_text)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate product source comparison review page.")
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--workbook", type=Path, required=True)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--intent-audit", type=Path)
    parser.add_argument("--validate", action="store_true")
    args = parser.parse_args()

    repo_root = Path.cwd()
    if args.validate:
        report = build_report(repo_root, args.run_dir, args.workbook, intent_audit_path=args.intent_audit)
        issues = validate_report(report)
        output_path = args.run_dir / args.output
        if output_path.exists():
            issues.extend(validate_html(output_path.read_text(), report))
        else:
            issues.append(f"missing output HTML: {output_path}")
        if issues:
            print("FAIL source comparison review:")
            for issue in issues:
                print(f"- {issue}")
            raise SystemExit(1)
        print(
            f"PASS source comparison review: {report['summary']['source_rows']} source rows, "
            f"{report['summary']['covered_rows']} covered, {report['summary']['needs_review']} needing review, "
            f"{report['summary']['intent_drift']} intent drift."
        )
        return

    output_path = write_report(repo_root, args.run_dir, args.workbook, args.output, intent_audit_path=args.intent_audit)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
