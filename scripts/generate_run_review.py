#!/usr/bin/env python3
"""Generate and validate a static human review dashboard for a run."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit(
        "PyYAML is required. Install pyyaml or run from the repo environment "
        "used for activity metadata validation."
    ) from exc


PACKAGE_FILES = [
    "spec.md",
    "prod.md",
    "tag_block.yaml",
    "recap.template.yaml",
    "dashboard.template.yaml",
]

RUBRIC_CRITERIA = [
    {
        "number": "1",
        "dimension": "V1 Technical Compliance",
        "pass": "No runtime beat depends on blocked V1 capabilities such as OCR, pose/expression detection, IMU sensing, before/after comparison, or unsupported non-speech audio detection.",
        "fail": "Fail when the package promises capability the current runtime cannot safely execute or verify.",
    },
    {
        "number": "2",
        "dimension": "Hook & Transition",
        "pass": "Step 1 opens from emotional resonance, grows naturally from the trigger, and bridges into the activity without feeling like a sudden quiz.",
        "fail": "Fail when the opening is a cold task assignment, knowledge test, or disconnected transition.",
    },
    {
        "number": "3",
        "dimension": "Edge Case Coverage",
        "pass": "Every dialogue step covers ideal, unexpected, and no-response branches with validating redirects, wait timing, and concrete scaffolds.",
        "fail": "Fail when branches are missing, generic, or leave a child stuck after silence or an unexpected answer.",
    },
    {
        "number": "4",
        "dimension": "IB Completeness",
        "pass": "Key Concepts, Related Concepts, KUD, ATL skills, and closing dialogue are specific and match what the child actually does.",
        "fail": "Fail when IB language is vague, missing, or forced onto an activity that does not support it.",
    },
    {
        "number": "5",
        "dimension": "Tier Appropriateness",
        "pass": "Language, response length, number of rounds, task complexity, and vocabulary fit the declared target tier.",
        "fail": "Fail when a T0/T1/T2 package asks for too much, uses over-complex language, or under-delivers for the target age.",
    },
    {
        "number": "6",
        "dimension": "Dialogue Specificity",
        "pass": "AI lines are concrete spoken dialogue with tone markers and branch-specific reactions, not abstract narration.",
        "fail": "Fail when the runtime would need to invent missing prompts, feedback, or child-facing wording.",
    },
    {
        "number": "7",
        "dimension": "Screen & UI Completeness",
        "pass": "Each step names what appears, persists, changes, and how progress or payoff is represented on screen.",
        "fail": "Fail when screen states are generic, missing, or disconnected from the dialogue.",
    },
    {
        "number": "8",
        "dimension": "Entity Mapping Alignment",
        "pass": "Mapping-informed designs use mapping concepts, themes, related concepts, tier language, anchor dimensions, and approved warm-start bridge logic. Non-mapping packages may be N/A.",
        "fail": "Fail when a mapping-informed package invents ungrounded facts or ignores required mapping anchors.",
    },
    {
        "number": "9",
        "dimension": "Game Feel",
        "pass": "The child experiences uncertainty, stakes, surprise, replay value, and an earned magic moment tied to repeated action.",
        "fail": "Fail when the activity is only a conversation or generic badge award without a game-like payoff.",
    },
    {
        "number": "10",
        "dimension": "Mechanic Fidelity + Scaffold Honesty",
        "pass": "Step 3's repeated child action matches the declared mechanic and source promise, while the pillar/style scaffold supports rather than distorts it.",
        "fail": "Fail when the scaffold hides a mechanic mismatch, unsupported capability, or diluted source promise.",
    },
]


@dataclass
class Link:
    label: str
    href: str
    exists: bool


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        for key, value in attrs:
            if key == "href" and value:
                self.hrefs.append(value)


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text()) or {}
    if not isinstance(data, dict):
        return {}
    return data


def normalize_text(value: Any) -> str:
    text = "" if value is None else str(value)
    replacements = {
        "\u2014": " - ",
        "\u2013": " - ",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u00a0": " ",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return re.sub(r"\s+", " ", text).strip()


def esc(value: Any) -> str:
    return html.escape(normalize_text(value), quote=True)


def multiline(value: Any) -> str:
    text = "" if value is None else str(value)
    text = text.replace("\u2014", " - ").replace("\u2013", " - ")
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    return html.escape(text.strip(), quote=True)


def parse_assignment(text: str) -> dict[str, str]:
    text = normalize_text(text)
    matches = list(re.finditer(r"([a-zA-Z_]+)=", text))
    parsed: dict[str, str] = {}
    for index, match in enumerate(matches):
        key = match.group(1)
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        raw = text[start:end]
        raw = raw[:-1] if raw.endswith(",") else raw
        parsed[key] = raw.strip(" ,")
    return parsed


def normalize_category(*values: Any) -> str:
    for value in values:
        text = normalize_text(value).lower()
        if not text:
            continue
        if "cat1" in text or "category_1" in text or text == "1":
            return "cat1"
        if "cat3" in text or "category_3" in text or "unsupported_cat3" in text or text == "3":
            return "cat3"
        if "cat5" in text or "category_5" in text or text == "5":
            return "cat5"
    return "unknown"


def compact_list(value: Any, limit: int = 5) -> list[str]:
    if isinstance(value, list):
        items = [normalize_text(item) for item in value if normalize_text(item)]
    elif isinstance(value, str):
        items = [normalize_text(part) for part in re.split(r"[,;]", value) if normalize_text(part)]
    else:
        items = []
    return items[:limit]


def read_text(path: Path) -> str:
    return path.read_text() if path.exists() else ""


def section(text: str, heading: str, level: int = 2) -> str:
    marks = "#" * level
    pattern = re.compile(
        rf"^{re.escape(marks)}\s+{re.escape(heading)}\s*$"
        rf"(?P<body>.*?)(?=^#{1,{level}}\s+|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body").strip() if match else ""


def subblock_after_bold(text: str, label: str) -> str:
    pattern = re.compile(
        rf"\*\*{re.escape(label)}\*\*\s*(?P<body>.*?)(?=\n\*\*\d+\.|\n### |\n#### |\Z)",
        re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        return ""
    body = match.group("body").strip()
    return re.sub(r"\n{2,}", "\n", body)


def bullets_from_markdown(text: str, limit: int = 5) -> list[str]:
    bullets: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped[2:].strip())
        if len(bullets) >= limit:
            break
    return bullets


def clean_markdown(value: str) -> str:
    value = re.sub(r"\*\*(.*?)\*\*", r"\1", value)
    value = re.sub(r"`([^`]+)`", r"\1", value)
    value = re.sub(r"\[(.*?)\]\((.*?)\)", r"\1", value)
    return normalize_text(value)


def field_block(text: str, label: str) -> str:
    pattern = re.compile(
        rf"\*\*{re.escape(label)}:\*\*\s*(?P<body>.*?)(?=\n\*\*[A-Z][^*]+:\*\*|\n\*\*Round |\n#### |\Z)",
        re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body").strip() if match else ""


def summarize_child_responses(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        match = re.match(r"\d+\.\s*\(([^)]+)\)\s*(.*)", stripped)
        if match:
            lines.append(f"{match.group(1)}: {match.group(2)}")
        if len(lines) >= 3:
            break
    return " | ".join(lines) if lines else clean_markdown(text)


def summarize_ai_followup(text: str) -> str:
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        match = re.match(r"\d+\.\s*(.*)", stripped)
        if match:
            lines.append(match.group(1))
        if len(lines) >= 2:
            break
    return " | ".join(clean_markdown(line) for line in lines) if lines else clean_markdown(text)


def beat_from_chunk(title: str, chunk: str) -> dict[str, str]:
    return {
        "title": clean_markdown(title),
        "ai": clean_markdown(field_block(chunk, "AI says")),
        "child": summarize_child_responses(field_block(chunk, "Child responses")),
        "followup": summarize_ai_followup(field_block(chunk, "AI follow-up")),
        "screen": clean_markdown(field_block(chunk, "Screen")),
    }


def runtime_beats(prod_text: str) -> list[dict[str, str]]:
    beats: list[dict[str, str]] = []
    step_matches = list(re.finditer(r"^####\s+(Step \d+:\s+.*?)\s*$", prod_text, re.MULTILINE))
    for step_index, step_match in enumerate(step_matches):
        step_title = step_match.group(1)
        start = step_match.end()
        end = step_matches[step_index + 1].start() if step_index + 1 < len(step_matches) else len(prod_text)
        step_chunk = prod_text[start:end].strip()
        round_matches = list(re.finditer(r"^\*\*(Round .*?):\*\*\s*$", step_chunk, re.MULTILINE))
        if round_matches:
            for round_index, round_match in enumerate(round_matches):
                round_start = round_match.end()
                round_end = round_matches[round_index + 1].start() if round_index + 1 < len(round_matches) else len(step_chunk)
                beats.append(beat_from_chunk(round_match.group(1), step_chunk[round_start:round_end]))
        else:
            beats.append(beat_from_chunk(step_title, step_chunk))
        if len(beats) >= 9:
            break
    return beats[:9]


def overall_scorecard(spec_text: str) -> str:
    match = re.search(r"\*\*Overall\*\*:\s*(.+)", spec_text)
    return normalize_text(match.group(1)) if match else ""


def scorecard_rows(spec_text: str) -> list[dict[str, str]]:
    body = section(spec_text, "Self-Evaluation Scorecard")
    rows: list[dict[str, str]] = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [clean_markdown(cell.strip()) for cell in stripped.strip("|").split("|")]
        if len(cells) < 4 or not cells[0].isdigit():
            continue
        rows.append(
            {
                "number": cells[0],
                "dimension": cells[1],
                "score": cells[2],
                "notes": cells[3],
            }
        )
    return rows


def package_links(repo_root: Path, activity_path: str) -> list[Link]:
    links: list[Link] = []
    for filename in PACKAGE_FILES:
        target = repo_root / activity_path / filename
        href = f"../../{activity_path}/{filename}"
        links.append(Link(filename, href, target.exists()))
    return links


def link_html(link: Link) -> str:
    if link.exists:
        return f'<a href="{esc(link.href)}">{esc(link.label)}</a>'
    return f'<span class="missing">{esc(link.label)} missing</span>'


def collect_asset_policy(entry: dict[str, Any], assignment_fields: dict[str, str], brief: dict[str, Any]) -> str:
    if assignment_fields.get("asset_policy"):
        return assignment_fields["asset_policy"]
    dependency = brief.get("adaptation_brief", {}).get("asset_dependency", {})
    if isinstance(dependency, dict) and dependency.get("policy"):
        return str(dependency["policy"])
    return "unknown"


def collect_package(repo_root: Path, run_dir: Path, entry: dict[str, Any], kind: str) -> dict[str, Any]:
    activity_path = normalize_text(entry.get("activity_path"))
    activity_id = normalize_text(entry.get("activity_id"))
    assignment_fields = parse_assignment(str(entry.get("assignment") or entry.get("source_assignment") or ""))
    package_dir = repo_root / activity_path
    tag = load_yaml(package_dir / "tag_block.yaml")
    spec_text = read_text(package_dir / "spec.md")
    prod_text = read_text(package_dir / "prod.md")
    brief_path = entry.get("adaptation_brief")
    brief = load_yaml(repo_root / str(brief_path)) if brief_path else {}
    signature = tag.get("activity_signature", {}) if isinstance(tag.get("activity_signature"), dict) else {}
    tier = tag.get("tier_range", {}).get("primary") if isinstance(tag.get("tier_range"), dict) else ""
    prod_title = ""
    for line in prod_text.splitlines():
        if line.startswith("## "):
            prod_title = line.strip("# ").strip()
            break
    detail_floor = section(spec_text, "Runtime Detail Floor Notes")
    package = {
        "kind": kind,
        "assignment_index": entry.get("assignment_index", ""),
        "activity_id": activity_id,
        "activity_name": prod_title or activity_id,
        "activity_path": activity_path,
        "status": normalize_text(entry.get("status") or "unknown"),
        "reviewer": normalize_text(entry.get("reviewer") or "unknown"),
        "category": normalize_category(
            assignment_fields.get("category"),
            tag.get("template_type"),
            tag.get("category"),
        ),
        "mechanic": normalize_text(signature.get("mechanic") or assignment_fields.get("mechanic") or "unknown"),
        "tier": normalize_text(tier or assignment_fields.get("tier") or "unknown"),
        "pillar": normalize_text(tag.get("pillar") or "unknown"),
        "game_style": normalize_text(tag.get("game_style") or "unknown"),
        "focal_attribute": normalize_text(signature.get("focal_attribute") or "unknown"),
        "observation_angle": normalize_text(signature.get("observation_angle") or "unknown"),
        "entity_role": normalize_text(signature.get("entity_role") or "unknown"),
        "asset_policy": collect_asset_policy(entry, assignment_fields, brief),
        "changed_files": compact_list(entry.get("changed_files"), limit=8),
        "key_concepts": compact_list(tag.get("key_concepts"), limit=4),
        "related_concepts": compact_list(tag.get("related_concepts"), limit=5),
        "atl_skills": compact_list(tag.get("atl_skills"), limit=5),
        "intro": normalize_text(signature.get("intro") or ""),
        "preview_label": normalize_text(signature.get("preview_label") or ""),
        "preview_prompt": normalize_text(signature.get("preview_prompt") or ""),
        "premise": section(spec_text, "Premise"),
        "selection_trigger": section(spec_text, "Selection Trigger"),
        "detail_notes": bullets_from_markdown(detail_floor, limit=5),
        "brief_description": subblock_after_bold(prod_text, "1. Brief Description"),
        "design_highlight": subblock_after_bold(prod_text, "3. Design Highlight"),
        "typical_scenario": subblock_after_bold(prod_text, "4. Typical Scenario"),
        "runtime_beats": runtime_beats(prod_text),
        "scorecard": overall_scorecard(spec_text),
        "scorecard_rows": scorecard_rows(spec_text),
        "review_reason": normalize_text(entry.get("reason") or ""),
        "links": package_links(repo_root, activity_path),
    }
    return package


REASON_RULES: list[dict[str, Any]] = [
    {
        "label": "Runtime image generation",
        "needles": ("runtime image generation", "requires_generated_image", "runtime_generated"),
        "meaning": "The concept needs the product to generate child-facing images during the session.",
        "why": "The package cannot promise runtime artwork until generation safety, latency, content policy, and fallback behavior are approved.",
    },
    {
        "label": "Coloring or recoloring UI",
        "needles": ("coloring", "recoloring", "requires_coloring_ui", "fillable"),
        "meaning": "The concept needs selectable regions, color application, or saved coloring state.",
        "why": "Runtime beats would otherwise assume UI controls and state behavior that do not exist in the current package contract.",
    },
    {
        "label": "Cat3 material workflow",
        "needles": ("cat3", "requires_materials", "material workflow", "paper", "pencil"),
        "meaning": "The child must use physical materials such as paper, blocks, craft objects, or handwriting.",
        "why": "The current run contract supports Cat1/Cat5 packages; material setup, caregiver involvement, timing, and completion evidence need a product decision first.",
    },
    {
        "label": "UI state or progress memory",
        "needles": ("requires_ui_state", "state storage", "progress memory", "resume/reset"),
        "meaning": "The activity needs persistent progress, resume/reset behavior, or interactive screen state.",
        "why": "Designing rounds before the state model is defined risks creating flows the runtime cannot store, resume, or verify.",
    },
    {
        "label": "Prebuilt asset display",
        "needles": ("requires_asset_display", "prebuilt asset", "asset library", "display contract"),
        "meaning": "The activity depends on approved cards, artworks, pose images, or other displayed assets.",
        "why": "The package needs known asset IDs, metadata, display rules, and fallbacks before it can claim what appears on screen.",
    },
    {
        "label": "Motion safety",
        "needles": ("requires_motion_safety", "movement policy", "space checks", "prohibited movements"),
        "meaning": "The child is asked to move their body or follow pose/action prompts.",
        "why": "Movement activities need age-safe constraints, caregiver gating, space checks, and prohibited movement rules before runtime dialogue is safe.",
    },
    {
        "label": "Before/after evidence",
        "needles": ("before_after_risk", "before/after", "parent confirmation", "infer completion"),
        "meaning": "The product would need to compare a finished physical result with an earlier state or receive confirmation.",
        "why": "Without an evidence policy, the activity could overclaim that it can assess drawings, builds, cleanup, or craft completion.",
    },
    {
        "label": "OCR or text handling",
        "needles": ("ocr_risk", "ocr", "text-aware", "reading level"),
        "meaning": "The activity may need to read child writing, letters, words, or text content.",
        "why": "Text recognition and reading-level behavior need explicit capability, privacy, and fallback decisions before runtime beats can rely on them.",
    },
    {
        "label": "Caregiver setup and pacing",
        "needles": ("caregiver", "setup", "pacing", "no-assessment"),
        "meaning": "The activity requires adult setup, material timing, or a no-assessment physical-work fallback.",
        "why": "The design needs clear caregiver responsibilities and pacing rules so the runtime does not leave the child waiting or judge unsupported work.",
    },
]

FALLBACK_REASON = {
    "label": "Product decision needed",
    "meaning": "The brief names an unresolved product or design dependency outside the current package contract.",
    "why": "The assignment may be previewed, but it cannot become a valid package until the missing decision is resolved.",
}


def reason_definitions(labels: list[str]) -> list[dict[str, str]]:
    definitions = {rule["label"]: rule for rule in REASON_RULES}
    definitions[FALLBACK_REASON["label"]] = FALLBACK_REASON
    return [definitions[label] for label in sorted(set(labels)) if label in definitions]


def classify_block_reason(brief: dict[str, Any], manifest_reason: str) -> list[str]:
    adaptation = brief.get("adaptation_brief", {}) if isinstance(brief.get("adaptation_brief"), dict) else {}
    decisions = " ".join(compact_list(adaptation.get("missing_product_decisions"), limit=20))
    flags = " ".join(compact_list(adaptation.get("product_capability_flags"), limit=20))
    scaffold = adaptation.get("scaffold_choice", {})
    scaffold_text = json.dumps(scaffold, sort_keys=True) if isinstance(scaffold, dict) else str(scaffold)
    haystack = normalize_text(f"{manifest_reason} {decisions} {flags} {scaffold_text}").lower()
    labels = [
        str(rule["label"])
        for rule in REASON_RULES
        if any(str(needle).lower() in haystack for needle in rule["needles"])
    ]
    return labels or [FALLBACK_REASON["label"]]


def run_href(path: str) -> str:
    path = normalize_text(path)
    return path.split("/", 2)[-1] if path.startswith("runs/") else path


def blocked_comments(preview_text: str) -> list[str]:
    comments: list[str] = []
    for line in preview_text.splitlines():
        match = re.search(r"BLOCKED ELEMENT:\s*(.+)", line)
        if match:
            comments.append(normalize_text(match.group(1)))
        if len(comments) >= 8:
            break
    return comments


def collect_blocked(repo_root: Path, entry: dict[str, Any]) -> dict[str, Any]:
    brief_path = normalize_text(entry.get("brief_path"))
    brief = load_yaml(repo_root / brief_path)
    adaptation = brief.get("adaptation_brief", {}) if isinstance(brief.get("adaptation_brief"), dict) else {}
    assignment_fields = parse_assignment(str(entry.get("assignment") or adaptation.get("source", {}).get("assignment_row") or ""))
    decisions = compact_list(adaptation.get("missing_product_decisions"), limit=6)
    flags = compact_list(adaptation.get("product_capability_flags"), limit=8)
    asset_dependency = adaptation.get("asset_dependency", {})
    asset_policy = ""
    if isinstance(asset_dependency, dict):
        asset_policy = normalize_text(asset_dependency.get("policy"))
    design_preview = normalize_text(
        entry.get("design_preview")
        or entry.get("design_preview_path")
        or entry.get("blocked_design")
        or adaptation.get("design_preview")
        or ""
    )
    preview_text = read_text(repo_root / design_preview) if design_preview else ""
    item = {
        "assignment_index": entry.get("assignment_index", ""),
        "activity_concept": normalize_text(adaptation.get("activity_concept") or assignment_fields.get("activity_concept") or "Unknown"),
        "activity_id": normalize_text(assignment_fields.get("activity_id") or ""),
        "status": normalize_text(entry.get("status") or adaptation.get("readiness") or "blocked"),
        "category": normalize_category(assignment_fields.get("category"), adaptation.get("category_decision")),
        "mechanic": normalize_text(adaptation.get("canonical_mechanic") or assignment_fields.get("mechanic") or "unknown"),
        "tier": normalize_text(assignment_fields.get("tier") or "unknown"),
        "asset_policy": asset_policy or normalize_text(assignment_fields.get("asset_policy") or "unknown"),
        "flags": flags,
        "core_promise": normalize_text(adaptation.get("core_promise") or assignment_fields.get("description") or ""),
        "trigger_condition": normalize_text(adaptation.get("trigger_condition") or assignment_fields.get("trigger_condition") or ""),
        "missing_decisions": decisions,
        "reason": normalize_text(entry.get("reason") or "; ".join(decisions)),
        "reason_types": classify_block_reason(brief, normalize_text(entry.get("reason"))),
        "brief_path": brief_path,
        "design_preview": design_preview,
        "preview_exists": bool(design_preview and (repo_root / design_preview).exists()),
        "preview_beats": runtime_beats(preview_text),
        "blocked_comments": blocked_comments(preview_text),
    }
    return item


def read_results(repo_root: Path) -> dict[str, dict[str, str]]:
    path = repo_root / "results.tsv"
    if not path.exists():
        return {}
    rows: dict[str, dict[str, str]] = {}
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        for row in reader:
            filename = row.get("filename", "")
            match = re.search(r"activities/([^/\t]+)", filename)
            if match:
                rows[match.group(1)] = row
    return rows


def css_token(value: Any) -> str:
    token = normalize_text(value).lower().replace("_", "-")
    token = re.sub(r"[^a-z0-9-]+", "-", token).strip("-")
    return token or "unknown"


def dom_id(prefix: str, value: Any, fallback: Any = "item") -> str:
    return f"{prefix}-{css_token(value) or css_token(fallback)}"


def badge(text: str, class_name: str = "", group: str = "default") -> str:
    classes = "badge" + (f" {class_name}" if class_name else "")
    group_attr = f' data-tag-group="{esc(group)}"'
    value_attr = f' data-tag-value="{esc(css_token(text))}"'
    return f'<span class="{classes}"{group_attr}{value_attr}>{esc(text)}</span>'


def group_badge(text: str, group: str, class_name: str = "") -> str:
    token = css_token(text)
    classes = f"badge badge-{group} badge-{group}-{token}"
    if class_name:
        classes += f" {class_name}"
    return f'<span class="{classes}">{esc(text)}</span>'


def value_list(items: list[str], empty: str = "None") -> str:
    if not items:
        return f'<span class="muted">{esc(empty)}</span>'
    return " ".join(group_badge(item, "metadata") for item in items)


def data_attrs(values: dict[str, Any]) -> str:
    return " ".join(f'data-{key}="{esc(value)}"' for key, value in values.items())


def package_tags(package: dict[str, Any]) -> str:
    tags = [
        group_badge(package["kind"], "kind"),
        group_badge(package["category"], "category"),
        group_badge(package["status"], "status"),
        group_badge(package["mechanic"], "mechanic"),
        group_badge(package["tier"], "tier"),
        group_badge(package["asset_policy"], "asset"),
        group_badge(package["reviewer"], "reviewer"),
    ]
    return "".join(tags)


def scorecard_table(rows: list[dict[str, str]]) -> str:
    if not rows:
        return '<p class="muted">No scorecard table found in spec.md.</p>'
    body = []
    for row in rows:
        body.append(
            "<tr>"
            f"<td>{esc(row['number'])}</td>"
            f"<td>{esc(row['dimension'])}</td>"
            f"<td>{group_badge(row['score'], 'status')}</td>"
            f"<td>{esc(row['notes'])}</td>"
            "</tr>"
        )
    return (
        '<div class="table-wrap scorecard-wrap"><table class="scorecard-table">'
        "<thead><tr><th>#</th><th>Dimension</th><th>Result</th><th>Why</th></tr></thead>"
        f"<tbody>{''.join(body)}</tbody></table></div>"
    )


def package_detail_content(
    package: dict[str, Any],
    link_bits: str,
    runtime: str,
    details: str,
    changed: str,
    scorecard: str,
) -> str:
    return f"""
<div class="dialog-grid">
  <section>
    <h4>Design</h4>
    <p>{esc(package['design_highlight'] or package['premise'] or 'Unknown')}</p>
    <p class="muted">{esc(package['typical_scenario'])}</p>
  </section>
  <section>
    <h4>Metadata</h4>
    <div class="meta-grid compact">
      <div><span>Activity ID</span><strong>{esc(package['activity_id'])}</strong></div>
      <div><span>Package</span><strong>{esc(package['kind'])}</strong></div>
      <div><span>Pillar</span><strong>{esc(package['pillar'])}</strong></div>
      <div><span>Style</span><strong>{esc(package['game_style'])}</strong></div>
      <div><span>Focal</span><strong>{esc(package['focal_attribute'])}</strong></div>
      <div><span>Results</span><strong>{esc(package.get('result_summary') or 'Not logged')}</strong></div>
      <div><span>Status</span><strong>{esc(package['status'])}</strong></div>
      <div><span>Reviewer</span><strong>{esc(package['reviewer'])}</strong></div>
    </div>
  </section>
  <section class="dialog-wide">
    <h4>Runtime Beats</h4>
    <ol class="beat-list">{runtime or '<li>Unknown</li>'}</ol>
  </section>
  <section>
    <h4>Learning Tags</h4>
    <p><span>Concepts</span>{value_list(package['key_concepts'])}</p>
    <p><span>Related</span>{value_list(package['related_concepts'])}</p>
    <p><span>ATL</span>{value_list(package['atl_skills'])}</p>
  </section>
  <section>
    <h4>Review Notes</h4>
    <p>{esc(package['review_reason'] or 'No run-specific review rationale recorded.')}</p>
    <ul>{details or '<li>No detail-floor bullets found.</li>'}</ul>
    <p>{esc(package['scorecard'] or 'No scorecard summary found.')}</p>
  </section>
  <section class="dialog-wide">
    <h4>Scorecard Results</h4>
    {scorecard}
  </section>
  <section class="dialog-wide">
    <h4>Files</h4>
    <div class="file-row inline-file-row"><div>{link_bits}</div><div class="changed-files">{changed}</div></div>
  </section>
</div>"""


def package_card(package: dict[str, Any]) -> str:
    search = " ".join(
        normalize_text(package.get(key, ""))
        for key in [
            "kind",
            "activity_id",
            "activity_name",
            "category",
            "status",
            "mechanic",
            "tier",
            "pillar",
            "game_style",
            "focal_attribute",
            "asset_policy",
            "reviewer",
            "review_reason",
            "intro",
            "preview_label",
            "preview_prompt",
        ]
    )
    attrs = data_attrs(
        {
            "search": search.lower(),
            "kind": package["kind"],
            "category": package["category"],
            "status": package["status"],
            "mechanic": package["mechanic"],
            "tier": package["tier"],
            "asset": package["asset_policy"],
            "reviewer": package["reviewer"],
            "activity": package["activity_id"],
            "index": package["assignment_index"] or 9999,
        }
    )
    link_bits = " ".join(link_html(link) for link in package["links"])
    runtime = "".join(runtime_beat_html(beat) for beat in package["runtime_beats"])
    details = "".join(f"<li>{esc(note)}</li>" for note in package["detail_notes"])
    changed = value_list(package["changed_files"], empty="No files changed")
    scorecard = scorecard_table(package["scorecard_rows"])
    modal_id = dom_id("activity-detail", package["activity_id"], package["assignment_index"])
    tags = package_tags(package)
    detail = package_detail_content(package, link_bits, runtime, details, changed, scorecard)
    summary = package["intro"] or package["brief_description"] or package["premise"]
    return f"""
<article class="activity-card clickable-card" role="button" tabindex="0" aria-haspopup="dialog" aria-controls="detail-dialog" data-detail-template="{esc(modal_id)}" data-detail-title="{esc(package['activity_name'])}" {attrs}>
  <div class="card-top">
    <div>
      <div class="eyebrow">{esc(package['kind'])} activity</div>
      <h3>{esc(package['activity_name'])}</h3>
      <p class="activity-id">{esc(package['activity_id'])}</p>
    </div>
  </div>
  <div class="tag-row">{tags}</div>
  <p class="summary-copy">{esc(summary)}</p>
  <div class="inline-fields">
    <div><span>Preview label</span><strong>{esc(package['preview_label'] or 'Unknown')}</strong></div>
    <div><span>Runtime beats</span><strong>{esc(len(package['runtime_beats']))}</strong></div>
  </div>
  <div class="file-row">
    <div>{link_bits}</div>
    <button class="detail-button" type="button" data-open-detail>View details</button>
  </div>
  <template id="{esc(modal_id)}">{detail}</template>
</article>"""


def runtime_beat_html(beat: dict[str, str]) -> str:
    fields = [
        ("AI", beat.get("ai", "")),
        ("Child", beat.get("child", "")),
        ("Follow-up", beat.get("followup", "")),
        ("Screen", beat.get("screen", "")),
    ]
    field_html = "".join(
        f'<div class="beat-field"><span>{esc(label)}</span><p>{esc(value or "Unknown")}</p></div>'
        for label, value in fields
    )
    return f'<li><strong>{esc(beat.get("title", "Runtime beat"))}</strong>{field_html}</li>'


def blocked_tags(item: dict[str, Any]) -> str:
    tags = [
        group_badge(item["category"], "category"),
        group_badge(item["status"], "status"),
        group_badge(item["mechanic"], "mechanic"),
        group_badge(item["tier"], "tier"),
        group_badge(item["asset_policy"], "asset"),
    ]
    tags.extend(group_badge(reason, "reason", "blocked-reason-type") for reason in item["reason_types"])
    return "".join(tags)


def blocked_detail_content(
    item: dict[str, Any],
    decisions: str,
    flag_badges: str,
    preview_runtime: str,
    comments: str,
    brief_href: str,
    preview_link: str,
    design_status: str,
) -> str:
    return f"""
<div class="dialog-grid">
  <section>
    <h4>Why Blocked</h4>
    <p>{esc(design_status)}</p>
    <ul>{decisions or f'<li>{esc(item["reason"])}</li>'}</ul>
  </section>
  <section>
    <h4>Metadata</h4>
    <div class="meta-grid compact">
      <div><span>Concept</span><strong>{esc(item['activity_concept'])}</strong></div>
      <div><span>Activity ID</span><strong>{esc(item['activity_id'] or 'No package generated')}</strong></div>
      <div><span>Mechanic</span><strong>{esc(item['mechanic'])}</strong></div>
      <div><span>Tier</span><strong>{esc(item['tier'])}</strong></div>
      <div><span>Assets</span><strong>{esc(item['asset_policy'])}</strong></div>
      <div><span>Trigger</span><strong>{esc(item['trigger_condition'] or 'Unknown')}</strong></div>
    </div>
  </section>
  <section>
    <h4>Capability Flags</h4>
    <p>{flag_badges}</p>
  </section>
  <section>
    <h4>Blocked Elements</h4>
    <ul>{comments}</ul>
  </section>
  <section class="dialog-wide">
    <h4>Constrained Preview Beats</h4>
    <ol class="beat-list">{preview_runtime}</ol>
  </section>
  <section class="dialog-wide">
    <h4>Files</h4>
    <div class="file-row inline-file-row"><a href="{esc(brief_href)}">blocked brief</a>{preview_link}</div>
  </section>
</div>"""


def blocked_card(item: dict[str, Any]) -> str:
    search = " ".join(
        normalize_text(item.get(key, ""))
        for key in [
            "activity_concept",
            "activity_id",
            "status",
            "category",
            "mechanic",
            "tier",
            "asset_policy",
            "reason",
            "core_promise",
            "trigger_condition",
        ]
    )
    search += " " + " ".join(item["reason_types"] + item["missing_decisions"] + item["flags"] + item["blocked_comments"])
    attrs = data_attrs(
        {
            "search": search.lower(),
            "category": item["category"],
            "status": item["status"],
            "mechanic": item["mechanic"],
            "reason": "|".join(item["reason_types"]),
            "activity": item["activity_concept"],
            "index": item["assignment_index"] or 9999,
        }
    )
    decisions = "".join(f"<li>{esc(decision)}</li>" for decision in item["missing_decisions"])
    flag_badges = value_list(item["flags"], empty="No capability flags")
    brief_href = run_href(item["brief_path"])
    preview_href = run_href(item["design_preview"])
    preview_link = (
        f'<a href="{esc(preview_href)}">blocked design preview</a>'
        if item["design_preview"] and item["preview_exists"]
        else '<span class="muted">No constrained design preview in this legacy run</span>'
    )
    if item["preview_exists"]:
        design_status = "Constrained design preview available; invalid until blockers are resolved."
    else:
        design_status = "No constrained design preview was recorded for this legacy run; future blocked assignments should include detailed steps with inline blocked-element comments."
    preview_runtime = "".join(runtime_beat_html(beat) for beat in item["preview_beats"])
    preview_runtime = preview_runtime or "<li>No constrained runtime beats were recorded.</li>"
    comments = "".join(f"<li>{esc(comment)}</li>" for comment in item["blocked_comments"])
    comments = comments or "<li>No inline BLOCKED ELEMENT comments were recorded.</li>"
    modal_id = dom_id("blocked-detail", item["activity_concept"], item["assignment_index"])
    tags = blocked_tags(item)
    detail = blocked_detail_content(item, decisions, flag_badges, preview_runtime, comments, brief_href, preview_link, design_status)
    return f"""
<article class="blocked-card clickable-card" role="button" tabindex="0" aria-haspopup="dialog" aria-controls="detail-dialog" data-detail-template="{esc(modal_id)}" data-detail-title="{esc(item['activity_concept'])}" {attrs}>
  <div class="card-top">
    <div>
      <div class="eyebrow">Blocked assignment {esc(item['assignment_index'])}</div>
      <h3>{esc(item['activity_concept'])}</h3>
      <p class="activity-id">{esc(item['activity_id'] or 'No package generated')}</p>
    </div>
  </div>
  <div class="tag-row">{tags}</div>
  <div class="blocked-design-status"><strong>Design status:</strong> {esc(design_status)}</div>
  <p class="summary-copy">{esc(item['core_promise'])}</p>
  <div class="inline-fields">
    <div><span>Missing decisions</span><strong>{esc(len(item['missing_decisions']))}</strong></div>
    <div><span>Preview beats</span><strong>{esc(len(item['preview_beats']))}</strong></div>
  </div>
  <div class="file-row"><a href="{esc(brief_href)}">blocked brief</a><button class="detail-button" type="button" data-open-detail>View details</button></div>
  <template id="{esc(modal_id)}">{detail}</template>
</article>"""


def reason_guide(reason_labels: list[str]) -> str:
    definitions = reason_definitions(reason_labels)
    if not definitions:
        return ""
    rows = []
    for item in definitions:
        rows.append(
            "<tr>"
            f"<td>{badge(item['label'], 'badge-reason')}</td>"
            f"<td>{esc(item['meaning'])}</td>"
            f"<td>{esc(item['why'])}</td>"
            "</tr>"
        )
    return f"""
  <section class="panel" id="blocking-reason-guide">
    <div class="panel-head"><h2>Blocking Reason Guide</h2></div>
    <div class="table-wrap"><table>
      <thead><tr><th>Reason</th><th>What it means</th><th>Why it blocks validity</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table></div>
  </section>
"""


def criteria_guide() -> str:
    rows = []
    for item in RUBRIC_CRITERIA:
        rows.append(
            "<tr>"
            f"<td>{esc(item['number'])}</td>"
            f"<td><strong>{esc(item['dimension'])}</strong></td>"
            f"<td>{esc(item['pass'])}</td>"
            f"<td>{esc(item['fail'])}</td>"
            "</tr>"
        )
    return f"""
  <section class="panel" id="review-criteria">
    <div class="panel-head"><h2>Review Criteria</h2></div>
    <div class="criteria-note">Packages are still judged with the `program.md` Phase 3 10-dimension rubric. A package passes only when every applicable dimension passes; Dimension 8 may be N/A for non-mapping packages. Any FAIL or credible reviewer uncertainty requires repair before logging or checkoff.</div>
    <div class="table-wrap"><table class="criteria-table">
      <thead><tr><th>#</th><th>Dimension</th><th>Pass Criteria</th><th>Why It Fails</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table></div>
  </section>
"""


def option_tags(values: list[str], all_label: str) -> str:
    options = [f'<option value="">{esc(all_label)}</option>']
    for value in sorted({normalize_text(v) for v in values if normalize_text(v)}):
        options.append(f'<option value="{esc(value)}">{esc(value)}</option>')
    return "\n".join(options)


def render_checks(checks: list[dict[str, Any]]) -> str:
    rows = []
    for check in checks:
        rows.append(
            "<tr>"
            f"<td>{esc(check.get('command', 'Unknown'))}</td>"
            f"<td>{badge(check.get('result', 'Unknown'), 'badge-status')}</td>"
            "</tr>"
        )
    return "\n".join(rows)


def reviewer_summary(review_notes: str) -> str:
    body = section(review_notes, "Generated Package Review") + "\n\n" + section(review_notes, "Existing Package Enrichment Audit")
    if not body.strip():
        return '<p class="muted">No reviewer summary found.</p>'
    cards = []
    current: list[str] = []
    for line in body.splitlines():
        if line.startswith("- Reviewer ") and current:
            cards.append("\n".join(current))
            current = [line]
        elif line.startswith("- Reviewer "):
            current = [line]
        elif current and (line.startswith("  - ") or not line.strip()):
            current.append(line)
    if current:
        cards.append("\n".join(current))
    if not cards:
        return f"<pre>{multiline(body[:4000])}</pre>"
    return "".join(f'<article class="reviewer-card"><pre>{multiline(card)}</pre></article>' for card in cards)


def residual_summary(review_notes: str) -> str:
    risk = section(review_notes, "Residual Risks") or section(review_notes, "Residual Risk")
    next_actions = section(review_notes, "Next Actions") or section(review_notes, "Next actions")
    if not risk and not next_actions:
        return '<p class="muted">No residual risk or next-action section found in review_notes.md.</p>'
    parts = []
    if risk:
        parts.append(f"<h4>Residual Risk</h4><pre>{multiline(risk)}</pre>")
    if next_actions:
        parts.append(f"<h4>Next Actions</h4><pre>{multiline(next_actions)}</pre>")
    return "\n".join(parts)


def build_html(repo_root: Path, run_dir: Path) -> str:
    manifest = load_yaml(run_dir / "run_manifest.yaml")
    if not manifest:
        raise SystemExit(f"Missing or unreadable manifest: {run_dir / 'run_manifest.yaml'}")
    outputs = manifest.get("outputs", {}) if isinstance(manifest.get("outputs"), dict) else {}
    generated = [collect_package(repo_root, run_dir, entry, "Generated") for entry in outputs.get("generated_activities", [])]
    enriched = [collect_package(repo_root, run_dir, entry, "Enriched") for entry in outputs.get("enriched_activities", [])]
    audited = [collect_package(repo_root, run_dir, entry, "Audited") for entry in outputs.get("audited_activities", [])]
    packages = generated + enriched + audited
    results_by_activity = read_results(repo_root)
    for package in packages:
        result = results_by_activity.get(package["activity_id"], {})
        if result:
            package["result_summary"] = f"{result.get('status', 'logged')} at {result.get('timestamp', 'unknown time')}"
        elif package["kind"] == "Enriched":
            package["result_summary"] = "Enrichment only"
        elif package["kind"] == "Audited":
            package["result_summary"] = "Audit pass, no package edits"
        else:
            package["result_summary"] = "Not logged"
    blocked = [collect_blocked(repo_root, entry) for entry in outputs.get("blocked_assignments", [])]
    review_notes = read_text(run_dir / "review_notes.md")
    summary = manifest.get("summary", {}) if isinstance(manifest.get("summary"), dict) else {}
    run_id = normalize_text(manifest.get("run_id") or run_dir.name)
    run_links = [
        ("run_manifest.yaml", "run_manifest.yaml"),
        ("review_notes.md", "review_notes.md"),
        ("assignment_snapshot.md", "assignment_snapshot.md"),
        ("generated_activity_ids.txt", "generated_activity_ids.txt"),
        ("results.tsv", "../../results.tsv"),
        ("assignments.md", "../../assignments.md"),
    ]
    package_categories = [p["category"] for p in packages]
    package_statuses = [p["status"] for p in packages]
    package_mechanics = [p["mechanic"] for p in packages]
    package_tiers = [p["tier"] for p in packages]
    package_assets = [p["asset_policy"] for p in packages]
    package_kinds = [p["kind"] for p in packages]
    blocked_categories = [b["category"] for b in blocked]
    blocked_mechanics = [b["mechanic"] for b in blocked]
    blocked_reasons = [reason for item in blocked for reason in item["reason_types"]]
    run_link_html = "".join(f'<a href="{esc(href)}">{esc(label)}</a>' for label, href in run_links)
    package_cards = "\n".join(package_card(package) for package in packages)
    blocked_cards = "\n".join(blocked_card(item) for item in blocked)
    reason_guide_html = reason_guide(blocked_reasons)
    criteria_guide_html = criteria_guide()
    checks = render_checks(manifest.get("checks", []))
    css = """
:root {
  color-scheme: light;
  --bg: oklch(98% 0.009 250);
  --panel: oklch(99.2% 0.005 250);
  --panel-soft: oklch(97.5% 0.007 250);
  --control: oklch(99% 0.004 250);
  --text: oklch(27% 0.035 255);
  --muted: oklch(52% 0.04 255);
  --line: oklch(90% 0.016 250);
  --line-strong: oklch(82% 0.024 250);
  --blue: oklch(47% 0.18 260);
  --blue-bg: oklch(95% 0.035 260);
  --blue-text: oklch(40% 0.15 260);
  --green-bg: oklch(95% 0.045 155);
  --green-text: oklch(39% 0.11 155);
  --amber-bg: oklch(96% 0.06 85);
  --amber-text: oklch(41% 0.1 78);
  --red-bg: oklch(94% 0.045 28);
  --red-text: oklch(42% 0.13 28);
  --purple-bg: oklch(95% 0.035 306);
  --purple-text: oklch(40% 0.12 306);
  --teal-bg: oklch(95% 0.035 190);
  --teal-text: oklch(36% 0.1 190);
  --neutral-tag-bg: oklch(94% 0.01 245);
  --neutral-tag-text: oklch(41% 0.035 245);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
}
a { color: var(--blue); text-decoration: none; }
a:hover { text-decoration: underline; }
header {
  background: var(--panel);
  border-bottom: 1px solid var(--line);
  position: sticky;
  top: 0;
  z-index: 10;
}
.header-inner { max-width: 1500px; margin: 0 auto; padding: 18px 24px 16px; }
.eyebrow {
  color: var(--muted);
  font-size: 11px;
  font-weight: 750;
  letter-spacing: .08em;
  text-transform: uppercase;
}
h1 { margin: 2px 0 8px; font-size: 30px; line-height: 1.15; letter-spacing: 0; }
h2 { margin: 0; font-size: 18px; letter-spacing: 0; }
h3 { margin: 2px 0 0; font-size: 18px; line-height: 1.22; letter-spacing: 0; }
h4 { margin: 0 0 6px; font-size: 13px; letter-spacing: 0; }
.summary-line { display: flex; flex-wrap: wrap; gap: 8px 18px; color: var(--muted); }
main { max-width: 1500px; margin: 0 auto; padding: 18px 24px 42px; }
.metrics { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 10px; }
.metric { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 11px 13px; min-height: 70px; }
.metric span { display: block; color: var(--muted); font-size: 12px; font-weight: 700; }
.metric strong { display: block; margin-top: 4px; font-size: 25px; line-height: 1; }
.panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  margin-top: 14px;
  overflow: hidden;
}
.panel-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 16px;
  border-bottom: 1px solid var(--line);
}
.controls {
  display: grid;
  grid-template-columns: minmax(260px, 1.4fr) repeat(6, minmax(120px, .7fr));
  gap: 9px;
  padding: 12px 16px;
  background: var(--panel-soft);
  border-bottom: 1px solid var(--line);
}
input, select {
  width: 100%;
  min-height: 36px;
  border: 1px solid var(--line-strong);
  border-radius: 6px;
  padding: 7px 9px;
  background: var(--control);
  color: var(--text);
  font: inherit;
}
.link-grid { display: flex; flex-wrap: wrap; gap: 8px; padding: 14px 16px; }
.link-grid a, .file-row a {
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 6px 9px;
  background: var(--control);
}
.activity-grid, .blocked-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  padding: 14px 16px 16px;
}
.activity-card, .blocked-card {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel);
  padding: 14px;
  min-height: 265px;
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.clickable-card {
  cursor: pointer;
  transition: border-color 160ms ease-out, box-shadow 160ms ease-out, transform 160ms ease-out;
}
.clickable-card:hover {
  border-color: var(--line-strong);
  box-shadow: 0 6px 20px oklch(40% 0.04 250 / 0.08);
  transform: translateY(-1px);
}
.clickable-card:focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
}
.card-top { display: flex; justify-content: space-between; gap: 14px; align-items: flex-start; }
.status-stack { display: flex; flex-direction: column; gap: 6px; align-items: flex-end; }
.activity-id { margin: 4px 0 0; color: var(--muted); font: 12px/1.4 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
.meta-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 8px;
}
.meta-grid.compact { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.meta-grid div, .inline-fields div {
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--panel-soft);
  padding: 8px;
  min-width: 0;
}
.meta-grid span, .inline-fields span, .details-grid span {
  display: block;
  color: var(--muted);
  font-size: 11px;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: .05em;
}
.meta-grid strong, .inline-fields strong { display: block; margin-top: 2px; overflow-wrap: anywhere; }
.inline-fields { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.summary-copy { margin: 0; color: var(--text); max-width: 74ch; }
details { border-top: 1px solid var(--line); padding-top: 10px; }
summary { cursor: pointer; font-weight: 750; color: var(--blue-text); }
.details-grid, .dialog-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px;
  margin-top: 10px;
}
.details-grid section, .dialog-grid section { min-width: 0; }
.dialog-wide { grid-column: 1 / -1; }
.details-grid p, .dialog-grid p { margin: 0 0 8px; }
ol, ul { margin: 0; padding-left: 20px; }
.beat-list { display: grid; gap: 10px; }
.beat-list li {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--panel-soft);
  padding: 10px;
}
.beat-list strong { display: block; margin-bottom: 8px; }
.beat-field {
  display: grid;
  grid-template-columns: 80px minmax(0, 1fr);
  gap: 8px;
  margin-top: 6px;
}
.beat-field p { margin: 0; }
.blocked-design-status {
  border: 1px solid var(--line);
  border-radius: 6px;
  background: var(--panel-soft);
  padding: 9px;
}
.badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 23px;
  min-width: 64px;
  padding: 2px 8px;
  border-radius: 999px;
  background: var(--panel-soft);
  border: 1px solid var(--line);
  color: var(--text);
  font-size: 12px;
  font-weight: 750;
  white-space: nowrap;
  margin: 0 4px 4px 0;
}
.tag-row, .reason-row { display: flex; flex-wrap: wrap; gap: 4px; }
.badge-kind { background: var(--neutral-tag-bg); color: var(--neutral-tag-text); border-color: transparent; }
.badge-kind-audited { background: var(--teal-bg); color: var(--teal-text); border-color: transparent; }
.badge-category, .badge-category-cat1 { background: var(--blue-bg); color: var(--blue-text); border-color: transparent; }
.badge-category-cat3 { background: var(--red-bg); color: var(--red-text); border-color: transparent; }
.badge-category-cat5 { background: var(--green-bg); color: var(--green-text); border-color: transparent; }
.badge-status, .badge-status-pass, .badge-status-enriched, .badge-status-pass-no-changes { background: var(--green-bg); color: var(--green-text); border-color: transparent; }
.badge-status-blocked-until-product-decision, .badge-blocked, .badge-reason { background: var(--amber-bg); color: var(--amber-text); border-color: transparent; }
.badge-status-fail, .badge-status-failed { background: var(--red-bg); color: var(--red-text); border-color: transparent; }
.badge-mechanic { background: var(--purple-bg); color: var(--purple-text); border-color: transparent; }
.badge-tier { background: var(--blue-bg); color: var(--blue-text); border-color: transparent; }
.badge-asset, .badge-asset-no-assets, .badge-asset-optional-support { background: var(--teal-bg); color: var(--teal-text); border-color: transparent; }
.badge-asset-required-prebuilt, .badge-asset-runtime-generated, .badge-asset-blocked { background: var(--amber-bg); color: var(--amber-text); border-color: transparent; }
.badge-reviewer { background: var(--green-bg); color: var(--green-text); border-color: transparent; }
.badge-reviewer-unknown, .badge-reviewer-n-a { background: var(--amber-bg); color: var(--amber-text); border-color: transparent; }
.badge-metadata { background: var(--neutral-tag-bg); color: var(--neutral-tag-text); border-color: transparent; }
.detail-button, .dialog-close {
  border: 1px solid var(--line-strong);
  border-radius: 6px;
  padding: 6px 9px;
  background: var(--control);
  color: var(--text);
  font: inherit;
  font-weight: 750;
  cursor: pointer;
}
.detail-button:hover, .dialog-close:hover { border-color: var(--blue); color: var(--blue-text); }
.file-row {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  align-items: flex-end;
  margin-top: auto;
  border-top: 1px solid var(--line);
  padding-top: 10px;
}
.inline-file-row { margin-top: 0; }
.changed-files { text-align: right; color: var(--muted); font-size: 12px; }
.missing { color: var(--red-text); background: var(--red-bg); border-radius: 4px; padding: 2px 6px; }
.muted { color: var(--muted); }
.hidden { display: none; }
.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; min-width: 840px; }
th, td { padding: 10px 12px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }
th { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .04em; background: var(--panel-soft); }
.criteria-note {
  padding: 12px 16px;
  border-bottom: 1px solid var(--line);
  color: var(--text);
}
.scorecard-wrap table { min-width: 760px; }
.scorecard-table td:first-child, .criteria-table td:first-child { width: 44px; color: var(--muted); font-weight: 750; }
pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  font: 12px/1.45 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
}
.reviewers { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; padding: 14px 16px; }
.reviewer-card { border: 1px solid var(--line); border-radius: 8px; background: var(--panel-soft); padding: 12px; }
.note-body { padding: 14px 16px; }
.detail-dialog {
  width: min(1080px, calc(100vw - 32px));
  max-height: min(860px, calc(100vh - 32px));
  border: 1px solid var(--line-strong);
  border-radius: 10px;
  padding: 0;
  background: var(--panel);
  color: var(--text);
  box-shadow: 0 18px 60px oklch(30% 0.04 250 / 0.18);
}
.detail-dialog::backdrop { background: oklch(30% 0.04 250 / 0.28); }
.dialog-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 16px;
  border-bottom: 1px solid var(--line);
  background: var(--panel-soft);
}
.dialog-head h2 { font-size: 18px; }
.dialog-body {
  padding: 16px;
  overflow: auto;
  max-height: calc(min(860px, calc(100vh - 32px)) - 62px);
}
@media (max-width: 1120px) {
  header { position: static; }
  .metrics { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .controls { grid-template-columns: 1fr 1fr 1fr; }
  .activity-grid, .blocked-grid, .reviewers { grid-template-columns: 1fr; }
}
@media (max-width: 700px) {
  main, .header-inner { padding-left: 14px; padding-right: 14px; }
  h1 { font-size: 23px; }
  .metrics, .controls, .meta-grid, .meta-grid.compact, .inline-fields, .details-grid, .dialog-grid { grid-template-columns: 1fr; }
  .dialog-wide { grid-column: auto; }
  .file-row { display: block; }
  .detail-button { margin-top: 8px; }
  .changed-files { text-align: left; margin-top: 8px; }
}
"""
    js = """
function normalize(value) {
  return (value || "").toString().toLowerCase();
}
function sortCards(containerId, selector, key) {
  const container = document.getElementById(containerId);
  const cards = Array.from(container.querySelectorAll(selector));
  const numeric = key === "index";
  cards.sort((a, b) => {
    const av = a.dataset[key] || "";
    const bv = b.dataset[key] || "";
    if (numeric) return Number(av) - Number(bv);
    return av.localeCompare(bv);
  });
  cards.forEach(card => container.appendChild(card));
}
function filterPackages() {
  const query = normalize(document.getElementById("package-search").value);
  const filters = {
    kind: document.getElementById("package-kind-filter").value,
    category: document.getElementById("package-category-filter").value,
    status: document.getElementById("package-status-filter").value,
    mechanic: document.getElementById("package-mechanic-filter").value,
    tier: document.getElementById("package-tier-filter").value,
    asset: document.getElementById("package-asset-filter").value
  };
  let visible = 0;
  document.querySelectorAll(".activity-card").forEach(card => {
    const matchesQuery = !query || normalize(card.dataset.search).includes(query);
    const matchesFilters = Object.entries(filters).every(([key, value]) => !value || card.dataset[key] === value);
    const show = matchesQuery && matchesFilters;
    card.classList.toggle("hidden", !show);
    if (show) visible += 1;
  });
  document.getElementById("package-count").textContent = `${visible} shown`;
}
function filterBlocked() {
  const query = normalize(document.getElementById("blocked-search").value);
  const filters = {
    category: document.getElementById("blocked-category-filter").value,
    mechanic: document.getElementById("blocked-mechanic-filter").value
  };
  const reason = document.getElementById("blocked-reason-filter").value;
  let visible = 0;
  document.querySelectorAll(".blocked-card").forEach(card => {
    const matchesQuery = !query || normalize(card.dataset.search).includes(query);
    const matchesReason = !reason || (card.dataset.reason || "").split("|").includes(reason);
    const matchesFilters = Object.entries(filters).every(([key, value]) => !value || card.dataset[key] === value);
    const show = matchesQuery && matchesReason && matchesFilters;
    card.classList.toggle("hidden", !show);
    if (show) visible += 1;
  });
  document.getElementById("blocked-count").textContent = `${visible} shown`;
}
let lastDetailTrigger = null;
const detailDialog = document.getElementById("detail-dialog");
const detailTitle = document.getElementById("detail-title");
const detailBody = document.getElementById("detail-body");
const detailClose = document.getElementById("detail-close");
function openDetail(card) {
  const template = document.getElementById(card.dataset.detailTemplate || "");
  if (!template || !detailDialog) return;
  lastDetailTrigger = card;
  detailTitle.textContent = card.dataset.detailTitle || "Activity details";
  detailBody.innerHTML = template.innerHTML;
  detailDialog.showModal();
}
function shouldSkipCardOpen(target) {
  return Boolean(target.closest("a, select, input, summary"));
}
document.querySelectorAll("[data-detail-template]").forEach(card => {
  card.addEventListener("click", event => {
    const target = event.target;
    if (target.closest("[data-open-detail]")) {
      event.preventDefault();
      openDetail(card);
      return;
    }
    if (shouldSkipCardOpen(target)) return;
    openDetail(card);
  });
  card.addEventListener("keydown", event => {
    if (event.key !== "Enter" && event.key !== " ") return;
    event.preventDefault();
    openDetail(card);
  });
});
if (detailClose) {
  detailClose.addEventListener("click", () => detailDialog.close());
}
if (detailDialog) {
  detailDialog.addEventListener("click", event => {
    if (event.target === detailDialog) detailDialog.close();
  });
  detailDialog.addEventListener("close", () => {
    detailBody.innerHTML = "";
    if (lastDetailTrigger) lastDetailTrigger.focus();
  });
}
document.querySelectorAll("[data-package-control]").forEach(el => el.addEventListener("input", filterPackages));
document.querySelectorAll("[data-blocked-control]").forEach(el => el.addEventListener("input", filterBlocked));
document.getElementById("package-sort").addEventListener("input", event => sortCards("activity-cards", ".activity-card", event.target.value));
document.getElementById("blocked-sort").addEventListener("input", event => sortCards("blocked-cards", ".blocked-card", event.target.value));
filterPackages();
filterBlocked();
"""
    metrics = [
        ("Pending at start", summary.get("pending_at_start", 0)),
        ("Generated", summary.get("generated_count", len(generated))),
        ("Enriched", summary.get("enriched_count", len(enriched))),
        ("Audited no-op", summary.get("enrichment_noop_count", len(audited))),
        ("Blocked", summary.get("blocked_count", len(blocked))),
        ("Review cards", len(packages)),
    ]
    metric_html = "".join(f'<div class="metric"><span>{esc(label)}</span><strong>{esc(value)}</strong></div>' for label, value in metrics)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>WonderLens Run Review - {esc(run_id)}</title>
<style>{css}</style>
</head>
<body>
<header>
  <div class="header-inner">
    <div class="eyebrow">WonderLens Activity Run Review</div>
    <h1>{esc(run_id)}</h1>
    <div class="summary-line">
      <span>Status: <strong>{esc(manifest.get('status', 'unknown'))}</strong></span>
      <span>Started: {esc(manifest.get('started_at', 'unknown'))}</span>
      <span>Completed: {esc(manifest.get('completed_at', 'unknown'))}</span>
    </div>
  </div>
</header>
<main>
  <section class="metrics">{metric_html}</section>

  <section class="panel">
    <div class="panel-head"><h2>Run Files</h2></div>
    <div class="link-grid">{run_link_html}</div>
  </section>

{criteria_guide_html}

  <section class="panel" id="activity-details">
    <div class="panel-head"><h2>Activity Details</h2><span class="muted" id="package-count"></span></div>
    <div class="controls">
      <input id="package-search" data-package-control type="search" placeholder="Search activity cards">
      <select id="package-kind-filter" data-package-control>{option_tags(package_kinds, 'All types')}</select>
      <select id="package-category-filter" data-package-control>{option_tags(package_categories, 'All categories')}</select>
      <select id="package-status-filter" data-package-control>{option_tags(package_statuses, 'All statuses')}</select>
      <select id="package-mechanic-filter" data-package-control>{option_tags(package_mechanics, 'All mechanics')}</select>
      <select id="package-tier-filter" data-package-control>{option_tags(package_tiers, 'All tiers')}</select>
      <select id="package-asset-filter" data-package-control>{option_tags(package_assets, 'All asset policies')}</select>
      <select id="package-sort">
        <option value="index">Sort by assignment</option>
        <option value="category">Sort by category</option>
        <option value="status">Sort by status</option>
        <option value="mechanic">Sort by mechanic</option>
        <option value="tier">Sort by tier</option>
        <option value="activity">Sort by activity id</option>
      </select>
    </div>
    <div class="activity-grid" id="activity-cards">{package_cards}</div>
  </section>

  <section class="panel" id="blocked-assignments">
    <div class="panel-head"><h2>Blocked Assignments</h2><span class="muted" id="blocked-count"></span></div>
    <div class="controls">
      <input id="blocked-search" data-blocked-control type="search" placeholder="Search blocked assignments">
      <select id="blocked-category-filter" data-blocked-control>{option_tags(blocked_categories, 'All categories')}</select>
      <select id="blocked-mechanic-filter" data-blocked-control>{option_tags(blocked_mechanics, 'All mechanics')}</select>
      <select id="blocked-reason-filter" data-blocked-control>{option_tags(blocked_reasons, 'All reason types')}</select>
      <select id="blocked-sort">
        <option value="index">Sort by assignment</option>
        <option value="category">Sort by category</option>
        <option value="mechanic">Sort by mechanic</option>
        <option value="activity">Sort by concept</option>
      </select>
    </div>
    <div class="blocked-grid" id="blocked-cards">{blocked_cards}</div>
  </section>

{reason_guide_html}

  <section class="panel">
    <div class="panel-head"><h2>Reviewer Coverage</h2></div>
    <div class="reviewers">{reviewer_summary(review_notes)}</div>
  </section>

  <section class="panel">
    <div class="panel-head"><h2>Validation Checks</h2></div>
    <div class="table-wrap"><table><thead><tr><th>Command</th><th>Result</th></tr></thead><tbody>{checks}</tbody></table></div>
  </section>

  <section class="panel">
    <div class="panel-head"><h2>Residual Risk And Next Actions</h2></div>
    <div class="note-body">{residual_summary(review_notes)}</div>
  </section>
</main>
<dialog class="detail-dialog" id="detail-dialog" aria-labelledby="detail-title">
  <div class="dialog-head">
    <h2 id="detail-title">Activity details</h2>
    <button class="dialog-close" id="detail-close" type="button">Close</button>
  </div>
  <div class="dialog-body" id="detail-body"></div>
</dialog>
<script>{js}</script>
</body>
</html>
"""


def validate(repo_root: Path, run_dir: Path) -> None:
    html_path = run_dir / "review.html"
    text = html_path.read_text()
    parser = LinkParser()
    parser.feed(text)
    html_parser = HTMLParser()
    html_parser.feed(text)
    manifest = load_yaml(run_dir / "run_manifest.yaml")
    outputs = manifest.get("outputs", {}) if isinstance(manifest.get("outputs"), dict) else {}
    expected_packages = (
        len(outputs.get("generated_activities", []))
        + len(outputs.get("enriched_activities", []))
        + len(outputs.get("audited_activities", []))
    )
    expected_blocked = len(outputs.get("blocked_assignments", []))
    package_entries = (
        outputs.get("generated_activities", [])
        + outputs.get("enriched_activities", [])
        + outputs.get("audited_activities", [])
    )
    scorecard_sets = [
        scorecard_rows(read_text(repo_root / normalize_text(entry.get("activity_path")) / "spec.md"))
        for entry in package_entries
    ]
    checks = {
        "has_html": "<html" in text,
        "has_style": "<style>" in text,
        "has_script": "<script>" in text,
        "has_run_id": normalize_text(manifest.get("run_id")) in text,
        "activity_card_count": text.count('class="activity-card') == expected_packages,
        "blocked_card_count": text.count('class="blocked-card') == expected_blocked,
        "category_filter": 'id="package-category-filter"' in text and "cat1" in text and "cat5" in text,
        "sort_controls": 'id="package-sort"' in text and "Sort by mechanic" in text,
        "blocked_reason_types": text.count("blocked-reason-type") >= expected_blocked,
        "detailed_runtime_beats": "beat-field" in text and "AI" in text and "Child" in text and "Screen" in text,
        "review_criteria": "Review Criteria" in text
        and "10-dimension rubric" in text
        and "Mechanic Fidelity + Scaffold Honesty" in text,
        "scorecard_results": expected_packages == 0
        or (
            text.count("Scorecard Results") >= expected_packages
            and "scorecard-table" in text
            and "Why" in text
        ),
        "package_scorecards_complete": expected_packages == 0
        or all(
            len(rows) == 10 and all(row["score"] in {"PASS", "FAIL", "N/A"} for row in rows)
            for rows in scorecard_sets
        ),
        "audited_noop_cards": len(outputs.get("audited_activities", [])) == 0
        or ("PASS / no changes" in text and "Audited" in text),
        "blocked_design_status": expected_blocked == 0
        or (
            "Constrained design preview available" in text
            or "No constrained design preview was recorded" in text
        ),
        "clickable_detail_cards": text.count("data-detail-template=") >= expected_packages + expected_blocked
        and "<dialog" in text
        and "showModal()" in text
        and "View details" in text,
        "grouped_tag_colors": "badge-mechanic" in text
        and "badge-asset" in text
        and "badge-category" in text
        and "badge-reviewer" in text,
        "reason_guide_descriptions": "Blocking Reason Guide" in text and "What it means" in text and "Why it blocks validity" in text,
        "no_external_assets": not re.search(r"<(?:script|link)[^>]+(?:src|href)=[\"']https?://", text),
    }
    missing_links: list[str] = []
    for href in parser.hrefs:
        if "://" in href or href.startswith("#"):
            continue
        target = (html_path.parent / href).resolve()
        try:
            target.relative_to(repo_root.resolve())
        except ValueError:
            missing_links.append(f"{href} (outside repo)")
            continue
        if not target.exists():
            missing_links.append(href)
    checks["local_links_resolve"] = not missing_links
    failed = [name for name, ok in checks.items() if not ok]
    for name, ok in checks.items():
        print(("PASS" if ok else "FAIL"), name)
    print(f"checked_links={len(parser.hrefs)}")
    if missing_links:
        print("missing_links=" + ", ".join(missing_links[:20]))
    if failed:
        raise SystemExit("FAIL review dashboard validation: " + ", ".join(failed))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_dir", type=Path, help="Path to runs/<run_id>")
    parser.add_argument("--validate", action="store_true", help="Validate an existing review.html")
    args = parser.parse_args()
    repo_root = Path.cwd()
    run_dir = args.run_dir
    if not run_dir.is_absolute():
        run_dir = repo_root / run_dir
    if args.validate:
        validate(repo_root, run_dir)
        return
    html_text = build_html(repo_root, run_dir)
    out = run_dir / "review.html"
    out.write_text(html_text)
    print(f"Wrote {out.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
