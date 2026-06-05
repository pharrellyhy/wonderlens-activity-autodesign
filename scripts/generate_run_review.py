#!/usr/bin/env python3
"""Generate and validate a static human review dashboard for a run."""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
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

BRANCH_LABELS = [
    ("Ideal", "ideal"),
    ("Unexpected", "unexpected"),
    ("No response", "no-response"),
]

GENERIC_BRANCH_POLICY_PATTERNS = {
    "Unexpected child": "Child gives an unrelated answer, unsafe action, or asks to change the task.",
    "No response child": "Child stays quiet, waits, or looks at the screen.",
    "Unexpected AI follow-up": "[redirect] Validate the idea, restate the safe rule, and offer one easier choice.",
    "No response AI follow-up": "[wait 2s] [gentle] Model a tiny answer and invite one small try.",
}

RUNTIME_CONTRACT_CUE_GROUPS = {
    "goal/action": (
        "goal:",
        "ask",
        "build",
        "celebrate",
        "close",
        "explain",
        "frame",
        "guide",
        "invite",
        "react",
        "teach",
        "tell",
    ),
    "constraint": (
        "constraint:",
        "avoid",
        "do not",
        "limit",
        "max",
        "must",
        "sentence",
        "tier",
    ),
    "emotion/tone": (
        "emotion",
        "tone",
        "curious",
        "excited",
        "gentle",
        "mysterious",
        "playful",
        "proud",
        "warm",
        "wonder",
    ),
    "child progress evidence": (
        "child progress",
        "progress evidence",
        "child",
        "chooses",
        "captures",
        "describes",
        "evidence",
        "finds",
        "names",
        "photo",
        "points",
        "says",
        "tap",
    ),
    "branch behavior": (
        "branch",
        "ideal",
        "no response",
        "off-track",
        "silence",
        "unexpected",
    ),
    "activity/source frame": (
        "activity",
        "build from",
        "child role",
        "do not skip",
        "do not turn",
        "frame",
        "mission",
        "preserve",
        "promise",
        "role",
        "source",
        "story",
    ),
}

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

CONSUMER_DIALOGUE_QA_REPORTS = {
    "fullstack_demo": "fullstack-demo",
    "wonderlens_ai": "WonderLens AI",
}

REQUIRED_DIALOGUE_QA_STRATEGIES = {
    "expected_answer",
    "wrong_unproductive_answer",
    "help_confusion",
    "silence_no_response",
    "premature_done",
}
CONSUMER_DIALOGUE_QA_FILENAMES = ("dialogue_qa_report.json", "dialogue_runtime_qa.json")
DIALOGUE_QA_STRATEGY_ALIASES = {
    "wrong_or_unproductive_answer": "wrong_unproductive_answer",
    "help_or_confusion": "help_confusion",
}


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


def clip_text(value: Any, limit: int = 140) -> str:
    text = normalize_text(value)
    if len(text) <= limit:
        return text
    return text[: limit - 1].rstrip() + "..."


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


def unresolved_product_capability_entries(entries: list[dict[str, Any]]) -> list[str]:
    """Return generated entries whose product capability assumptions lost traceability."""

    gaps: list[str] = []
    for entry in entries:
        fields = parse_assignment(str(entry.get("assignment") or entry.get("source_assignment") or ""))
        if not fields.get("product_capabilities"):
            continue
        if entry.get("resolved_blockers"):
            continue
        gaps.append(normalize_text(entry.get("activity_id") or entry.get("base_activity_id") or "unknown"))
    return gaps


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


def placeholder_tokens(*values: Any) -> list[str]:
    tokens: set[str] = set()

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            for child in value.values():
                visit(child)
            return
        if isinstance(value, list):
            for child in value:
                visit(child)
            return
        text = normalize_text(value)
        for match in re.finditer(r"\{[a-zA-Z0-9_]+\}", text):
            tokens.add(match.group(0))

    for value in values:
        visit(value)
    return sorted(tokens)


def read_text(path: Path) -> str:
    return path.read_text() if path.exists() else ""


def strip_trailing_whitespace(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.splitlines()) + "\n"


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


def branch_token(label: str) -> str:
    normalized = normalize_text(label).lower().replace("-", " ")
    for known_label, token in BRANCH_LABELS:
        if normalized == known_label.lower().replace("-", " "):
            return token
    return re.sub(r"[^a-z0-9]+", "-", normalized).strip("-") or "observed"


def branch_label_for_token(token: str) -> str:
    for label, known_token in BRANCH_LABELS:
        if token == known_token:
            return label
    return token.replace("-", " ").title() if token else "Observed"


def field_block(text: str, label: str) -> str:
    pattern = re.compile(
        rf"\*\*{re.escape(label)}:\*\*\s*(?P<body>.*?)(?=\n\*\*[A-Z][^*]+:\*\*|\n\*\*Round |\n\*\*Helper branch |\n> RESOLVED BLOCKER|\n#### |\Z)",
        re.DOTALL,
    )
    match = pattern.search(text)
    return match.group("body").strip() if match else ""


def first_field_block(text: str, labels: tuple[str, ...]) -> str:
    for label in labels:
        value = field_block(text, label)
        if value:
            return value
    return ""


def summarize_child_responses(text: str) -> str:
    branches = child_response_branches(text)
    if branches:
        return " | ".join(f"{branch['label']}: {branch['child']}" for branch in branches)
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
    followups = ai_followup_branches(text)
    if followups:
        return " | ".join(f"{followup['label']}: {followup['followup']}" for followup in followups)
    lines = []
    for line in text.splitlines():
        stripped = line.strip()
        match = re.match(r"\d+\.\s*(.*)", stripped)
        if match:
            lines.append(match.group(1))
        if len(lines) >= 2:
            break
    return " | ".join(clean_markdown(line) for line in lines) if lines else clean_markdown(text)


def child_response_branches(text: str) -> list[dict[str, str]]:
    branches: list[dict[str, str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        match = re.match(r"\d+\.\s*\(([^)]+)\)\s*(.*)", stripped)
        if not match:
            continue
        token = branch_token(match.group(1))
        branches.append(
            {
                "label": branch_label_for_token(token),
                "token": token,
                "child": clean_markdown(match.group(2)),
            }
        )
    return branches


def ai_followup_branches(text: str) -> list[dict[str, str]]:
    followups: list[dict[str, str]] = []
    for line in text.splitlines():
        stripped = line.strip()
        match = re.match(r"\d+\.\s*(.*)", stripped)
        if not match:
            continue
        body = match.group(1).strip()
        label_match = re.match(r"\(([^)]+)\)\s*(.*)", body)
        if label_match:
            token = branch_token(label_match.group(1))
            body = label_match.group(2)
        elif len(followups) < len(BRANCH_LABELS):
            _, token = BRANCH_LABELS[len(followups)]
        else:
            token = f"follow-up-{len(followups) + 1}"
        followups.append(
            {
                "label": branch_label_for_token(token),
                "token": token,
                "followup": clean_markdown(body),
            }
        )
    return followups


def paired_branch_followups(child_text: str, followup_text: str) -> list[dict[str, str]]:
    child_by_token = {branch["token"]: branch for branch in child_response_branches(child_text)}
    followup_by_token = {followup["token"]: followup for followup in ai_followup_branches(followup_text)}
    tokens = [token for _, token in BRANCH_LABELS]
    tokens.extend(token for token in child_by_token if token not in tokens)
    tokens.extend(token for token in followup_by_token if token not in tokens)
    rows: list[dict[str, str]] = []
    for token in tokens:
        child = child_by_token.get(token, {})
        followup = followup_by_token.get(token, {})
        if not child and not followup:
            continue
        rows.append(
            {
                "label": child.get("label") or followup.get("label") or branch_label_for_token(token),
                "token": token,
                "child": child.get("child") or "",
                "followup": followup.get("followup") or "",
            }
        )
    return rows


def generic_branch_policy_findings(beats: list[dict[str, Any]]) -> list[str]:
    findings: list[str] = []
    seen_branch_policy: dict[tuple[str, str, str], list[str]] = {}
    for beat in beats:
        title = normalize_text(beat.get("title") or "Runtime beat")
        labels: list[str] = []
        templated_labels: list[str] = []
        for branch in beat.get("branches", []):
            token = branch_token(branch.get("token", "observed"))
            child = normalize_text(branch.get("child"))
            followup = normalize_text(branch.get("followup"))
            child_lower = child.lower()
            followup_lower = followup.lower()
            if token in {"unexpected", "no-response"}:
                if len(child) >= 48:
                    seen_branch_policy.setdefault((token, "child", child), []).append(title)
                if len(followup) >= 48:
                    seen_branch_policy.setdefault((token, "AI follow-up", followup), []).append(title)
            if followup_lower.startswith("[specific]") or "source rule" in followup_lower:
                templated_labels.append(f"{branch_label_for_token(token)} AI follow-up")
            if token == "unexpected":
                if child == normalize_text(GENERIC_BRANCH_POLICY_PATTERNS["Unexpected child"]):
                    labels.append("Unexpected child")
                if followup == normalize_text(GENERIC_BRANCH_POLICY_PATTERNS["Unexpected AI follow-up"]):
                    labels.append("Unexpected AI follow-up")
                if "veers away from" in child_lower and "skips the" in child_lower and "unsafe/out-of-scope" in child_lower:
                    templated_labels.append("Unexpected child")
                if (
                    "validate briefly, keep the" in followup_lower
                    and "offer one safe choice that still completes" in followup_lower
                ):
                    templated_labels.append("Unexpected AI follow-up")
            if token == "no-response":
                if child == normalize_text(GENERIC_BRANCH_POLICY_PATTERNS["No response child"]):
                    labels.append("No response child")
                if followup == normalize_text(GENERIC_BRANCH_POLICY_PATTERNS["No response AI follow-up"]):
                    labels.append("No response AI follow-up")
                if "pauses at" in child_lower and "needs a first tiny" in child_lower and "model" in child_lower:
                    templated_labels.append("No response child")
                if "model one tiny" in followup_lower and "invite the child to copy or choose" in followup_lower:
                    templated_labels.append("No response AI follow-up")
        if labels:
            findings.append(f"{title}: generic branch policy in {', '.join(labels)}")
        elif templated_labels:
            findings.append(f"{title}: keyword-substitution branch policy in {', '.join(templated_labels)}")
    repeated_labels: list[str] = []
    for (token, field, text), titles in seen_branch_policy.items():
        distinct_titles = sorted(set(titles))
        if len(distinct_titles) < 2:
            continue
        label = f"{branch_label_for_token(token)} {field}"
        repeated_labels.append(f"{label} across {len(distinct_titles)} beats")
    if repeated_labels:
        findings.append(f"Runtime beat set: repeated branch policy in {', '.join(sorted(repeated_labels))}")
    return findings


def runtime_contract_quality_findings(beats: list[dict[str, Any]]) -> list[str]:
    findings: list[str] = []
    for beat in beats:
        if beat.get("speech_mode") != "runtime_contract":
            continue
        title = normalize_text(beat.get("title") or "Runtime beat")
        instruction = normalize_text(beat.get("runtime_instruction"))
        instruction_lower = instruction.lower()
        example = normalize_text(beat.get("example_ai_line"))
        screen = normalize_text(beat.get("screen"))
        missing: list[str] = []
        if not example:
            missing.append("missing Example AI line")
        elif not re.match(r"^\[[^\]]+\]", example):
            missing.append("Example AI line lacks leading tone marker")

        missing_cues = [
            label
            for label, cues in RUNTIME_CONTRACT_CUE_GROUPS.items()
            if not any(cue in instruction_lower for cue in cues)
        ]
        if len(instruction) < 160:
            missing_cues.append("fullstack-style detail")
        if missing_cues:
            missing.append("missing runtime contract cues: " + ", ".join(dict.fromkeys(missing_cues)))

        branch_rows = beat.get("branches", [])
        branch_by_token = {
            branch.get("token"): branch
            for branch in branch_rows
            if normalize_text(branch.get("child")) or normalize_text(branch.get("followup"))
        }
        missing_branches = [
            branch_label_for_token(token)
            for _, token in BRANCH_LABELS
            if not normalize_text(branch_by_token.get(token, {}).get("child"))
            or not normalize_text(branch_by_token.get(token, {}).get("followup"))
        ]
        if missing_branches:
            missing.append("missing branch-specific child/follow-up rows: " + ", ".join(missing_branches))

        if not screen or len(screen) < 40 or screen.lower() in {"show the activity start.", "screen updates."}:
            missing.append("missing specific screen/state behavior")

        if runtime_beat_kind(title) == "payoff" and _celebration_instruction_asks_new_gameplay(instruction_lower):
            missing.append("celebration beat asks for new gameplay; move required child action to Step 3")

        if missing:
            findings.append(f"{title}: " + "; ".join(missing))
    return findings


def _celebration_instruction_asks_new_gameplay(instruction_lower: str) -> bool:
    future_preview_cues = (
        "without executing it",
        "as a preview",
        "future version:",
        "future child-facing shape",
    )
    if any(cue in instruction_lower for cue in future_preview_cues):
        return False

    gameplay_phrases = (
        "ask one more",
        "binary choice",
        "child chooses",
        "child photographs",
        "child takes a photo",
        "child draws",
        "child collects",
        "collection action",
        "drawing step",
        "one more simple tool",
        "progress evidence: child chooses",
        "tool/action choice",
    )
    if any(phrase in instruction_lower for phrase in gameplay_phrases):
        return True
    return bool(re.search(r"\bgoal:\s*ask\b", instruction_lower))


def normalize_dialogue_qa_strategy(value: Any) -> str:
    strategy = normalize_text(value)
    return DIALOGUE_QA_STRATEGY_ALIASES.get(strategy, strategy)


def dialogue_qa_report_path(run_dir: Path, report_dir: str) -> Path:
    base = run_dir / "downstream_reports" / report_dir
    for filename in CONSUMER_DIALOGUE_QA_FILENAMES:
        path = base / filename
        if path.exists():
            return path
    return base / CONSUMER_DIALOGUE_QA_FILENAMES[0]


def beat_from_chunk(title: str, chunk: str) -> dict[str, Any]:
    child_block = field_block(chunk, "Child responses")
    followup_block = first_field_block(chunk, ("AI follow-up", "AI follow-up policy"))
    ai_says = clean_markdown(field_block(chunk, "AI says"))
    runtime_instruction = clean_markdown(field_block(chunk, "Runtime AI instruction"))
    example_ai_line = clean_markdown(field_block(chunk, "Example AI line"))
    speech_mode = "runtime_contract" if runtime_instruction else "exact_dialogue"
    return {
        "title": clean_markdown(title),
        "speech_mode": speech_mode,
        "ai": ai_says or runtime_instruction,
        "runtime_instruction": runtime_instruction,
        "example_ai_line": example_ai_line,
        "child": summarize_child_responses(child_block),
        "followup": summarize_ai_followup(followup_block),
        "branches": paired_branch_followups(child_block, followup_block),
        "photo_timing": clean_markdown(field_block(chunk, "Photo capture timing")),
        "screen": clean_markdown(first_field_block(chunk, ("Screen", "Screen/state"))),
    }


def runtime_beats(prod_text: str) -> list[dict[str, Any]]:
    beats: list[dict[str, Any]] = []
    step_matches = list(re.finditer(r"^####\s+(Step \d+:\s+.*?)\s*$", prod_text, re.MULTILINE))
    for step_index, step_match in enumerate(step_matches):
        step_title = step_match.group(1)
        start = step_match.end()
        end = step_matches[step_index + 1].start() if step_index + 1 < len(step_matches) else len(prod_text)
        step_chunk = prod_text[start:end].strip()
        loop_matches = list(
            re.finditer(r"^\*\*((?:Round|Helper branch).*?):\*\*\s*$", step_chunk, re.MULTILINE)
        )
        if loop_matches:
            for loop_index, loop_match in enumerate(loop_matches):
                loop_start = loop_match.end()
                loop_end = loop_matches[loop_index + 1].start() if loop_index + 1 < len(loop_matches) else len(step_chunk)
                beats.append(beat_from_chunk(loop_match.group(1), step_chunk[loop_start:loop_end]))
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


def consumer_dialogue_qa_findings(run_dir: Path) -> list[str]:
    findings: list[str] = []
    for report_dir, label in CONSUMER_DIALOGUE_QA_REPORTS.items():
        report_path = dialogue_qa_report_path(run_dir, report_dir)
        if not report_path.exists():
            findings.append(f"{label}: missing {report_path.relative_to(run_dir)}")
            continue

        try:
            data = json.loads(report_path.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            findings.append(f"{label}: unreadable dialogue QA report ({exc})")
            continue

        if not isinstance(data, dict):
            findings.append(f"{label}: dialogue QA report must be a JSON object")
            continue

        status = normalize_text(data.get("status") or data.get("verdict")).lower()
        if status not in {"pass", "downstream_owned_failure"}:
            findings.append(f"{label}: status must be pass or downstream_owned_failure")

        raw_strategies = data.get("strategies")
        raw_legacy_strategies = data.get("strategies_exercised")
        if not isinstance(raw_strategies, list):
            if isinstance(raw_legacy_strategies, list):
                strategy_names = {normalize_dialogue_qa_strategy(item) for item in raw_legacy_strategies}
            else:
                findings.append(f"{label}: strategies must list dialogue QA cases")
                strategy_names = set()
        else:
            strategy_names = set()
            for item in raw_strategies:
                if isinstance(item, str):
                    strategy_names.add(normalize_dialogue_qa_strategy(item))
                    continue
                if isinstance(item, dict):
                    item_name = normalize_dialogue_qa_strategy(item.get("strategy") or item.get("name") or item.get("id"))
                    item_status = normalize_text(item.get("status")).lower()
                    if item_name:
                        strategy_names.add(item_name)
                    if item_name and item_status not in {"pass", "downstream_owned_failure"}:
                        findings.append(f"{label}: strategy {item_name} has invalid status {item_status or '<empty>'}")

        missing = sorted(REQUIRED_DIALOGUE_QA_STRATEGIES.difference(strategy_names))
        if missing:
            findings.append(f"{label}: missing dialogue QA strategies {', '.join(missing)}")

        if status == "downstream_owned_failure":
            failure_text = normalize_text(data.get("failure_summary") or data.get("downstream_follow_up"))
            if not failure_text:
                findings.append(f"{label}: downstream_owned_failure requires failure_summary or downstream_follow_up")

    return findings


def href_from_run_dir(run_dir: Path, target: Path) -> str:
    return Path(os.path.relpath(target, run_dir)).as_posix()


def package_links(repo_root: Path, run_dir: Path, activity_path: str) -> list[Link]:
    links: list[Link] = []
    for filename in PACKAGE_FILES:
        target = (repo_root / activity_path / filename).resolve()
        href = href_from_run_dir(run_dir.resolve(), target)
        links.append(Link(filename, href, target.exists()))
    return links


def active_storyboard_root_name(run_dir: Path, allow_prompt_only: bool = True) -> str:
    """Pick the storyboard root the dashboard should display.

    Prefer a root that has generated PNGs. This keeps prompt-only v2 experiments
    from overriding the generated v1 storyboards already used for review.
    """

    candidates = ("visual_storyboards_v2", "visual_storyboards")
    for candidate in candidates:
        root = run_dir / candidate
        if not root.exists():
            continue
        manifest = load_yaml(root / "storyboard_manifest.yaml")
        try:
            if int(manifest.get("generated_count") or 0) > 0:
                return candidate
        except (TypeError, ValueError):
            pass
        if any(root.glob("*/mechanism_grid.png")):
            return candidate
    if not allow_prompt_only:
        return ""
    for candidate in candidates:
        root = run_dir / candidate
        if root.exists() or (root / "storyboard_manifest.yaml").exists():
            return candidate
    return ""


def link_html(link: Link) -> str:
    if link.exists:
        pid = register_preview(link.href)
        data = f' data-preview-id="{esc(pid)}"' if pid else ""
        return f'<a href="{esc(link.href)}"{data}>{esc(link.label)}</a>'
    return f'<span class="missing">{esc(link.label)} missing</span>'


def markdown_table_blocks(body: str) -> list[list[list[str]]]:
    blocks: list[list[list[str]]] = []
    current: list[list[str]] = []
    for line in body.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [cell.strip() for cell in stripped.strip("|").split("|")]
            if cells and not all(re.fullmatch(r":?-{2,}:?", cell) for cell in cells):
                current.append(cells)
            continue
        if current:
            blocks.append(current)
            current = []
    if current:
        blocks.append(current)
    return blocks


def asset_key(key: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", normalize_text(key).lower()).strip("_")
    aliases = {
        "prompt_en_source": "prompt_or_source",
        "prompt_source": "prompt_or_source",
        "purpose_en": "purpose",
        "display_behavior_en": "display_behavior",
        "fallback_behavior_en": "fallback_behavior",
        "safety_constraints_en": "safety_constraints",
        "display_slot": "display_location",
        "screen_slot": "display_location",
        "screen_location": "display_location",
        "where_to_display": "display_location",
        "where_displayed": "display_location",
        "when_to_display": "use_step",
        "when_displayed": "use_step",
    }
    return aliases.get(normalized, normalized)


def normalize_asset_item(item: dict[str, Any]) -> dict[str, str]:
    fields = {asset_key(key): normalize_text(value) for key, value in item.items() if normalize_text(value)}
    prompt_or_source = (
        fields.get("prompt_or_source")
        or fields.get("prompt_en")
        or fields.get("source")
        or fields.get("prompt")
        or ""
    )
    return {
        "asset_id": fields.get("asset_id", ""),
        "asset_type": fields.get("asset_type", ""),
        "requiredness": fields.get("requiredness", ""),
        "generation_timing": fields.get("generation_timing", ""),
        "use_step": fields.get("use_step", ""),
        "display_location": fields.get("display_location", ""),
        "purpose": fields.get("purpose", ""),
        "prompt_or_source": prompt_or_source,
        "display_behavior": fields.get("display_behavior", ""),
        "fallback_behavior": fields.get("fallback_behavior", ""),
    }


def asset_dependency_count(assets: list[dict[str, str]]) -> int:
    ids = {asset.get("asset_id", "") for asset in assets if asset.get("asset_id")}
    return len(ids) if ids else len(assets)


def asset_display_count_for_token(token: str) -> tuple[int, bool]:
    round_ranges = [
        (int(match.group(1)), int(match.group(2)))
        for match in re.finditer(r"round[_\s-]*(\d+)\s*[-\u2013\u2014]\s*(\d+)", token, re.I)
    ]
    if round_ranges:
        return sum(abs(end - start) + 1 for start, end in round_ranges), False

    step_ranges = [
        (int(match.group(1)), int(match.group(2)))
        for match in re.finditer(r"step[_\s-]*(\d+)\s*[-\u2013\u2014]\s*(\d+)", token, re.I)
    ]
    if step_ranges:
        return sum(abs(end - start) + 1 for start, end in step_ranges), False

    round_refs = re.findall(r"round[_\s-]*\d+", token, re.I)
    if round_refs:
        return len(round_refs), False

    step_refs = re.findall(r"step[_\s-]*\d+", token, re.I)
    if step_refs:
        return len(step_refs), False

    return 1, True


def asset_display_beat_count(use_step: str) -> tuple[int, bool]:
    text = normalize_text(use_step)
    if not text:
        return 0, True
    total = 0
    has_unknown = False
    tokens = [token.strip() for token in re.split(r"\s*(?:;|,|\+|\band\b)\s*", text) if token.strip()]
    for token in tokens:
        count, unknown = asset_display_count_for_token(token)
        total += count
        has_unknown = has_unknown or unknown
    return total, has_unknown


def asset_display_summary(assets: list[dict[str, str]]) -> str:
    if not assets:
        return "0"
    total = 0
    has_unknown = False
    for asset in assets:
        count, unknown = asset_display_beat_count(asset.get("use_step", ""))
        total += count
        has_unknown = has_unknown or unknown
    if has_unknown and total:
        return f"{total}+"
    if has_unknown:
        return "Unknown"
    return str(total)


def asset_item_summary(assets: list[dict[str, str]]) -> str:
    if not assets:
        return "0"
    set_count = sum(1 for asset in assets if "set" in asset.get("asset_type", "").lower())
    individual_count = max(0, len(assets) - set_count)
    parts: list[str] = []
    if individual_count:
        parts.append(str(individual_count))
    if set_count == 1:
        parts.append("card set")
    elif set_count > 1:
        parts.append(f"{set_count} card sets")
    if set_count:
        parts.append("count not declared")
    return ", ".join(parts) if parts else str(len(assets))


def asset_usage_from_spec(spec_text: str) -> list[dict[str, str]]:
    body = section(spec_text, "Asset Usage Timeline") or section(spec_text, "Asset Brief")
    if not body:
        return []
    assets: list[dict[str, str]] = []
    for block in markdown_table_blocks(body):
        if not block:
            continue
        header = [asset_key(cell) for cell in block[0]]
        if "asset_id" in header and len(header) > 2:
            for row in block[1:]:
                fields = {header[index]: row[index] for index in range(min(len(header), len(row)))}
                asset = normalize_asset_item(fields)
                if asset["asset_id"]:
                    assets.append(asset)
            continue
        if all(len(row) == 2 for row in block):
            current: dict[str, str] = {}
            for key_cell, value in block:
                key = asset_key(key_cell)
                if key == "asset_id" and current.get("asset_id"):
                    assets.append(normalize_asset_item(current))
                    current = {}
                current[key] = value
            asset = normalize_asset_item(current)
            if asset["asset_id"]:
                assets.append(asset)
    return assets


def asset_usage_from_brief(brief: dict[str, Any]) -> list[dict[str, str]]:
    dependency = brief.get("adaptation_brief", {}).get("asset_dependency", {})
    if not isinstance(dependency, dict):
        return []
    assets = dependency.get("assets", [])
    if not isinstance(assets, list):
        return []
    return [
        asset
        for asset in (normalize_asset_item(item) for item in assets if isinstance(item, dict))
        if asset["asset_id"]
    ]


def asset_policy_from_spec(spec_text: str) -> str:
    """Derive an asset_policy enum value from spec.md when assignment/brief don't carry it.

    Mapping: no `## Asset Brief` → `no_assets`. With a brief, `requiredness: optional`
    → `optional_support`; `requiredness: required` plus a generated source →
    `runtime_generated`; otherwise `required_prebuilt`.
    """

    assets = asset_usage_from_spec(spec_text)
    if not assets:
        return "no_assets"
    first = assets[0]
    requiredness = first.get("requiredness", "").lower()
    source = first.get("prompt_or_source", "").lower()
    timing = first.get("generation_timing", "").lower()
    if requiredness == "optional":
        return "optional_support"
    if requiredness == "required":
        if "runtime_generated" in timing or any(token in source for token in ("runtime_generated", "new_ai_generated", "ai_generated")):
            return "runtime_generated"
        return "required_prebuilt"
    return "optional_support"


def collect_asset_policy(
    entry: dict[str, Any],
    assignment_fields: dict[str, str],
    brief: dict[str, Any],
    spec_text: str = "",
) -> str:
    if assignment_fields.get("asset_policy"):
        return assignment_fields["asset_policy"]
    dependency = brief.get("adaptation_brief", {}).get("asset_dependency", {})
    if isinstance(dependency, dict) and dependency.get("policy"):
        return str(dependency["policy"])
    if spec_text:
        return asset_policy_from_spec(spec_text)
    return "unknown"


def compact_field_list(value: Any, limit: int = 8) -> list[str]:
    if isinstance(value, dict):
        items = [normalize_text(key) for key in value if normalize_text(key)]
        return items[:limit]
    return compact_list(value, limit=limit)


def first_mapping(*values: Any) -> dict[str, Any]:
    for value in values:
        if isinstance(value, dict) and value:
            return value
    return {}


def collect_parameterization_decision(
    package_dir: Path,
    tag: dict[str, Any],
    entry: dict[str, Any],
) -> dict[str, Any]:
    """Return declared or proposed package parameterization metadata for review."""

    package_parameterization = load_yaml(package_dir / "parameterization.yaml")
    demo_support = load_yaml(package_dir / "demo_support.yaml")
    raw = first_mapping(
        entry.get("parameterization_decision"),
        entry.get("parameterization"),
        tag.get("parameterization"),
        package_parameterization.get("parameterization"),
        package_parameterization if package_parameterization.get("mode") else {},
        demo_support.get("parameterization"),
    )
    if not raw:
        return {}
    validity = raw.get("validity") if isinstance(raw.get("validity"), dict) else {}
    decision = {
        "mode": normalize_text(raw.get("mode") or raw.get("declared_mode") or raw.get("parameterization_mode")),
        "integrity_status": normalize_text(
            raw.get("integrity_status")
            or raw.get("validity_status")
            or raw.get("status")
            or validity.get("status")
        ),
        "decision_source": normalize_text(raw.get("decision_source") or raw.get("source")),
        "confidence": normalize_text(raw.get("confidence")),
        "reviewer_action": normalize_text(raw.get("reviewer_action") or raw.get("required_reviewer_action")),
        "required_handoff_fields": compact_field_list(
            raw.get("required_handoff_fields")
            or raw.get("required_handoff")
            or raw.get("requires")
            or validity.get("requires"),
            limit=10,
        ),
        "dynamic_fields": compact_field_list(
            raw.get("dynamic_fields")
            or raw.get("derived_runtime_fields")
            or raw.get("derived_fields"),
            limit=10,
        ),
        "frozen_fields": compact_field_list(
            raw.get("frozen_fields")
            or raw.get("authored_constants"),
            limit=10,
        ),
        "invalid_when": compact_list(
            raw.get("invalid_when")
            or validity.get("invalid_when"),
            limit=8,
        ),
        "evidence": compact_list(raw.get("evidence") or raw.get("debug_evidence"), limit=8),
    }
    return {key: value for key, value in decision.items() if value}


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
    resolved_blockers = compact_list(entry.get("resolved_blockers"), limit=20) or bullets_from_markdown(
        section(spec_text, "Resolved Product Contract Notes"),
        limit=20,
    )
    declared_resolved_types = compact_list(entry.get("resolved_blocker_types"), limit=20)
    inferred_resolved_types = [
        label
        for item in resolved_blockers
        for label in classify_reason_text_labels(item)
    ]
    extensibility_notes = compact_list(entry.get("extensibility_notes"), limit=10) or bullets_from_markdown(
        section(spec_text, "Extensibility Notes"),
        limit=10,
    )
    manifest_asset_usage: list[dict[str, str]] = []
    if isinstance(entry.get("asset_usage"), list):
        for item in entry["asset_usage"]:
            if isinstance(item, dict):
                asset = normalize_asset_item(item)
                if asset["asset_id"]:
                    manifest_asset_usage.append(asset)
    asset_usage = manifest_asset_usage or asset_usage_from_spec(spec_text) or asset_usage_from_brief(brief)
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
        "entity_binding": normalize_text(tag.get("entity_binding") or "unknown"),
        "parameter_slots": placeholder_tokens(tag, spec_text),
        "parameterization_decision": collect_parameterization_decision(package_dir, tag, entry),
        "asset_policy": collect_asset_policy(entry, assignment_fields, brief, spec_text),
        "asset_usage": asset_usage,
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
        "resolved_blockers": resolved_blockers,
        "resolved_blocker_types": sorted(set(declared_resolved_types + inferred_resolved_types)),
        "extensibility_notes": extensibility_notes,
        "extensibility_summary": normalize_text(
            entry.get("extensibility_summary")
            or section(spec_text, "Extensibility Summary")
            or ""
        ),
        "links": package_links(repo_root, run_dir, activity_path),
    }
    package["storyboard"] = mechanism_storyboard(run_dir, package)
    return package


def mechanism_storyboard(run_dir: Path, package: dict[str, Any]) -> dict[str, Any]:
    """Return run-local visual storyboard metadata for an activity when present."""

    activity_id = normalize_text(package.get("activity_id"))
    storyboard_root = ""
    storyboard_dir = Path()
    candidates = ("visual_storyboards_v2", "visual_storyboards")
    generated_candidates = [
        candidate
        for candidate in candidates
        if (run_dir / candidate / activity_id / "mechanism_grid.png").exists()
    ]
    prompt_candidates = [
        candidate
        for candidate in candidates
        if (
            (run_dir / candidate / activity_id).exists()
            or (run_dir / candidate / activity_id / "mechanism_grid.meta.yaml").exists()
            or (run_dir / candidate / activity_id / "mechanism_grid.prompt.md").exists()
        )
    ]
    for candidate in generated_candidates or prompt_candidates:
        candidate_dir = run_dir / candidate / activity_id
        storyboard_root = candidate
        storyboard_dir = candidate_dir
        break
    if not storyboard_root:
        return {}
    meta_path = storyboard_dir / "mechanism_grid.meta.yaml"
    prompt_path = storyboard_dir / "mechanism_grid.prompt.md"
    image_path = storyboard_dir / "mechanism_grid.png"
    meta = load_yaml(meta_path)
    panel_captions = meta.get("panel_captions", [])
    if not isinstance(panel_captions, list):
        panel_captions = []
    normalized_captions = []
    for index, item in enumerate(panel_captions[:6], start=1):
        if isinstance(item, dict):
            normalized_captions.append(
                {
                    "number": normalize_text(item.get("number") or index),
                    "title": normalize_text(item.get("title") or f"Panel {index}"),
                    "label": normalize_text(item.get("label") or ""),
                    "caption": normalize_text(item.get("caption") or item.get("visual") or ""),
                    "source": normalize_text(item.get("source") or ""),
                }
            )
        else:
            normalized_captions.append(
                {
                    "number": str(index),
                    "title": f"Panel {index}",
                    "label": "",
                    "caption": normalize_text(item),
                    "source": "",
                }
            )
    return {
        "status": normalize_text(meta.get("status") or ("generated" if image_path.exists() else "prompt_ready")),
        "version": normalize_text(meta.get("storyboard_version") or ("v2" if storyboard_root.endswith("_v2") else "v1")),
        "root": storyboard_root,
        "tool": normalize_text(meta.get("tool") or "Codex image generation"),
        "target_model": normalize_text(meta.get("target_model") or meta.get("model") or "gpt-image-2"),
        "actual_model": normalize_text(meta.get("actual_model") or "codex-configured image model"),
        "generated_at": normalize_text(meta.get("generated_at") or ""),
        "continuity_rules": normalize_text(meta.get("continuity_rules") or ""),
        "caption_policy": normalize_text(meta.get("caption_policy") or ""),
        "source_image": normalize_text(meta.get("source_image") or ""),
        "image_href": href_from_run_dir(run_dir.resolve(), image_path.resolve()) if image_path.exists() else "",
        "image_exists": image_path.exists(),
        "prompt_href": href_from_run_dir(run_dir.resolve(), prompt_path.resolve()) if prompt_path.exists() else "",
        "prompt_exists": prompt_path.exists(),
        "meta_href": href_from_run_dir(run_dir.resolve(), meta_path.resolve()) if meta_path.exists() else "",
        "meta_exists": meta_path.exists(),
        "panel_captions": normalized_captions,
    }


REASON_RULES: list[dict[str, Any]] = [
    {
        "label": "Runtime image generation",
        "needles": (
            "runtime image generation",
            "runtime image",
            "runtime-image",
            "requires_generated_image",
            "runtime_generated",
            "no-image fallback",
        ),
        "meaning": "The concept needs the product to generate child-facing images during the session.",
        "why": "The package cannot promise runtime artwork until generation safety, latency, content policy, and fallback behavior are approved.",
        "unblocks_when": "Product approves a runtime-image policy: latency cap, content-safety rules, and a declared fallback when generation fails or is unavailable. A simpler unblock is to declare no runtime generation and use only prebuilt assets.",
    },
    {
        "label": "Coloring or recoloring UI",
        "needles": ("coloring", "recoloring", "requires_coloring_ui", "fillable"),
        "meaning": "The concept needs selectable regions, color application, or saved coloring state.",
        "why": "Runtime beats would otherwise assume UI controls and state behavior that do not exist in the current package contract.",
        "unblocks_when": "Product approves a coloring UI contract (selectable regions, color input, persistence rules) or declares a no-coloring fallback such as verbal description of color choices with no on-screen fill.",
    },
    {
        "label": "Cat3 material workflow",
        "needles": ("cat3", "requires_materials", "material workflow", "paper", "pencil"),
        "meaning": "The child must use physical materials such as paper, blocks, craft objects, or handwriting.",
        "why": "The current run contract supports Cat1/Cat5 packages; material setup, caregiver involvement, timing, and completion evidence need a product decision first.",
        "unblocks_when": "Product extends the package contract to Cat3 (material list, caregiver setup script, timing, completion-evidence policy) or commits to a Cat1/Cat5 re-cast that does not require materials.",
    },
    {
        "label": "UI state or progress memory",
        "needles": (
            "requires_ui_state",
            "state storage",
            "progress memory",
            "state contract",
            "per-round choices persist",
            "stateless fallback",
            "resume/reset",
        ),
        "meaning": "The activity needs persistent progress, resume/reset behavior, or interactive screen state.",
        "why": "Designing rounds before the state model is defined risks creating flows the runtime cannot store, resume, or verify.",
        "unblocks_when": "Product declares the state model: what persists across rounds and sessions, resume/reset rules, and the stateless fallback used when storage is unavailable.",
    },
    {
        "label": "Prebuilt asset display",
        "needles": (
            "requires_asset_display",
            "prebuilt asset",
            "asset library",
            "asset-display contract",
            "display contract",
            "asset ids may be displayed",
        ),
        "meaning": "The activity depends on approved cards, artworks, pose images, or other displayed assets.",
        "why": "The package needs known asset IDs, metadata, display rules, and fallbacks before it can claim what appears on screen.",
        "unblocks_when": "Product approves the required asset IDs with metadata and display rules, and the package documents a voice-only or no-display fallback when an asset is missing.",
    },
    {
        "label": "Motion safety",
        "needles": (
            "requires_motion_safety",
            "movement policy",
            "motion policy",
            "space check",
            "low-risk movement",
            "prohibited motions",
            "prohibited movements",
        ),
        "meaning": "The child is asked to move their body or follow pose/action prompts.",
        "why": "Movement activities need age-safe constraints, caregiver gating, space checks, and prohibited movement rules before runtime dialogue is safe.",
        "unblocks_when": "Product approves an age-appropriate motion policy (allowed/prohibited movements, caregiver-present requirement, space-check prompt) or restricts the activity to low-risk gestures that match the existing safety contract.",
    },
    {
        "label": "Before/after evidence",
        "needles": (
            "before_after_risk",
            "before/after",
            "evidence policy",
            "parent confirmation",
            "self-report",
            "visual verification",
            "completion evidence",
            "infer completion",
        ),
        "meaning": "The product would need to compare a finished physical result with an earlier state or receive confirmation.",
        "why": "Without an evidence policy, the activity could overclaim that it can assess drawings, builds, cleanup, or craft completion.",
        "unblocks_when": "Product picks an evidence policy — caregiver confirmation, child self-report, or no completion verification at all (AI narrates progress without claiming evidence). Choosing 'no verification' is the smallest unblock.",
    },
    {
        "label": "OCR or text handling",
        "needles": ("ocr_risk", "ocr", "text-aware", "text policy", "speak text", "reading level"),
        "meaning": "The activity may need to read child writing, letters, words, or text content.",
        "why": "Text recognition and reading-level behavior need explicit capability, privacy, and fallback decisions before runtime beats can rely on them.",
        "unblocks_when": "Product picks a text-handling policy: approve OCR with privacy and reading-level rules, OR require the child to speak text aloud instead, OR declare no correctness verification of written text. The 'no verification' decision is the smallest unblock.",
    },
    {
        "label": "Caregiver setup and pacing",
        "needles": ("caregiver", "setup", "pacing", "no-assessment"),
        "meaning": "The activity requires adult setup, material timing, or a no-assessment physical-work fallback.",
        "why": "The design needs clear caregiver responsibilities and pacing rules so the runtime does not leave the child waiting or judge unsupported work.",
        "unblocks_when": "Product defines caregiver responsibilities (setup steps, timing cues, no-assessment fallback) and the package records them in a caregiver-facing pacing note.",
    },
]

FALLBACK_REASON = {
    "label": "Product decision needed",
    "meaning": "The brief names an unresolved product or design dependency outside the current package contract.",
    "why": "The assignment may be previewed, but it cannot become a valid package until the missing decision is resolved.",
    "unblocks_when": "Resolve the missing product or design decision, capture it in program.md / run.md / the relevant schema, and rerun the assignment so the brief and package can be validated against the updated contract.",
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


def classify_reason_text_labels(text: str) -> list[str]:
    primary_text = normalize_text(text).split("--", 1)[0]
    labels: list[str] = []
    for candidate in (primary_text, text):
        haystack = normalize_text(candidate).lower()
        for rule in REASON_RULES:
            if any(str(needle).lower() in haystack for needle in rule["needles"]):
                label = str(rule["label"])
                if label not in labels:
                    labels.append(label)
    return labels or [FALLBACK_REASON["label"]]


def classify_reason_text(text: str) -> str:
    return classify_reason_text_labels(text)[0]


def run_href(path: str) -> str:
    path = normalize_text(path)
    return path.split("/", 2)[-1] if path.startswith("runs/") else path


def blocked_comments(preview_text: str) -> list[dict[str, str]]:
    comments: list[dict[str, str]] = []
    for line in preview_text.splitlines():
        match = re.search(r"BLOCKED ELEMENT:\s*(.+)", line)
        if match:
            text = normalize_text(match.group(1))
            comments.append({"label": classify_reason_text(text), "text": text})
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
    blocked_comment_items = blocked_comments(preview_text)
    blocked_comment_types = sorted({item["label"] for item in blocked_comment_items})
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
        "blocked_comments": blocked_comment_items,
        "blocked_comment_types": blocked_comment_types,
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
            if filename:
                rows[filename] = row
            match = re.search(r"(?:activities|activity_packages)/([^/\t]+)", filename)
            if match:
                rows.setdefault(match.group(1), row)
    return rows


def css_token(value: Any) -> str:
    token = normalize_text(value).lower().replace("_", "-")
    token = re.sub(r"[^a-z0-9-]+", "-", token).strip("-")
    return token or "unknown"


def _status_dot_class(status: Any) -> str:
    token = css_token(status)
    if token in {"completed", "complete"}:
        return ""
    if token.startswith("completed-with-blockers") or "blocker" in token:
        return "status-blocked"
    if token in {"failed", "fail", "error"}:
        return "status-fail"
    if token in {"in-progress", "running", "started", "pending"}:
        return "status-progress"
    return "status-progress"


# In-file preview registry. Populated as link_html / file links are emitted; emitted
# as <template> elements at the end of the page so reviewers can read .md/.yaml
# files without leaving the dashboard. See review_dashboard.md §"In-file preview".
_PREVIEW_REGISTRY: dict[str, dict[str, str]] = {}
_PREVIEW_CTX: dict[str, Path] = {}
_PREVIEW_MAX_BYTES = 240_000
_PREVIEW_KINDS = {".md": "Markdown", ".yaml": "YAML", ".yml": "YAML", ".txt": "Text", ".tsv": "Text"}


def _preview_label(repo_root: Path, full_path: Path) -> str:
    try:
        return str(full_path.resolve().relative_to(repo_root.resolve()))
    except ValueError:
        return full_path.name


def register_preview(href: str) -> str | None:
    """Read the file at href (relative to the run dir), record its content, return preview id.

    Returns None when the file is missing, outside the repo, oversized, or in a
    non-previewable format. Existing entries are not re-read.
    """

    if not href or href.startswith("#") or "://" in href:
        return None
    repo_root = _PREVIEW_CTX.get("repo_root")
    run_dir = _PREVIEW_CTX.get("run_dir")
    if not repo_root or not run_dir:
        return None
    target = (run_dir / href).resolve()
    try:
        target.relative_to(repo_root.resolve())
    except ValueError:
        return None
    if not target.is_file():
        return None
    suffix = target.suffix.lower()
    if suffix not in _PREVIEW_KINDS:
        return None
    pid = "preview-" + css_token(href)
    if pid in _PREVIEW_REGISTRY:
        return pid
    try:
        size = target.stat().st_size
    except OSError:
        return None
    if size > _PREVIEW_MAX_BYTES:
        _PREVIEW_REGISTRY[pid] = {
            "id": pid,
            "label": _preview_label(repo_root, target),
            "href": href,
            "kind": _PREVIEW_KINDS[suffix],
            "content": "",
            "truncated": "true",
            "size": str(size),
        }
        return pid
    try:
        text = target.read_text(errors="replace")
    except OSError:
        return None
    _PREVIEW_REGISTRY[pid] = {
        "id": pid,
        "label": _preview_label(repo_root, target),
        "href": href,
        "kind": _PREVIEW_KINDS[suffix],
        "content": text,
        "truncated": "false",
        "size": str(size),
    }
    return pid


def preview_anchor(href: str, label: str, *, class_attr: str = "") -> str:
    """Render an anchor that opens the in-page preview when previewable; falls back to a plain link otherwise."""

    pid = register_preview(href)
    cls = f' class="{esc(class_attr)}"' if class_attr else ""
    data = f' data-preview-id="{esc(pid)}"' if pid else ""
    return f'<a href="{esc(href)}"{cls}{data}>{esc(label)}</a>'


def preview_templates_html() -> str:
    """Emit <template> elements with raw escaped file content for all registered previews."""

    if not _PREVIEW_REGISTRY:
        return ""
    parts: list[str] = ['<div id="file-previews" hidden aria-hidden="true">']
    for entry in _PREVIEW_REGISTRY.values():
        attrs = (
            f' data-label="{esc(entry["label"])}"'
            f' data-href="{esc(entry["href"])}"'
            f' data-kind="{esc(entry["kind"])}"'
            f' data-truncated="{esc(entry.get("truncated", "false"))}"'
            f' data-size="{esc(entry.get("size", "0"))}"'
        )
        parts.append(f'<template id="{esc(entry["id"])}"{attrs}>{multiline(entry["content"])}</template>')
    parts.append("</div>")
    return "\n".join(parts)


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


def reason_badge(label: str, class_name: str = "", suffix: str = "") -> str:
    token = css_token(label)
    classes = f"badge badge-reason badge-reason-{token}"
    if class_name:
        classes += f" {class_name}"
    return f'<span class="{classes}">{esc(label + suffix)}</span>'


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


def resolved_blocker_rows(package: dict[str, Any]) -> str:
    items = package.get("resolved_blockers", [])
    if not items:
        return '<p class="muted">No resolved product-contract blockers recorded for this package.</p>'
    rows = []
    for item in items:
        rows.append(
            '<li class="resolved-blocker-row">'
            f'{reason_badge(classify_reason_text(item), "resolved-blocker-chip")}'
            f'<span>{esc(item)}</span>'
            "</li>"
        )
    return f'<ul class="resolved-blocker-list">{"".join(rows)}</ul>'


def extensibility_rows(package: dict[str, Any]) -> str:
    slots = package.get("parameter_slots", [])
    notes = package.get("extensibility_notes", [])
    decision = package.get("parameterization_decision") or {}
    slot_html = value_list(slots, empty="No explicit parameter slots")
    note_html = "".join(f"<li>{esc(note)}</li>" for note in notes)
    if decision.get("evidence"):
        note_html += "".join(f"<li>Parameterization evidence: {esc(item)}</li>" for item in decision["evidence"])
    if decision.get("invalid_when"):
        note_html += "".join(f"<li>Invalid when: {esc(item)}</li>" for item in decision["invalid_when"])
    note_html = note_html or "<li>Package is primarily standalone; no extensibility note recorded.</li>"
    summary = package.get("extensibility_summary") or "Review how the activity can be reused by replacing entity, attribute, asset, or topic slots."
    parameterization_html = ""
    if decision:
        parameterization_html = (
            '<div class="inline-fields">'
            f"<div><span>Parameterization mode</span><strong>{esc(decision.get('mode') or 'not_declared')}</strong></div>"
            f"<div><span>Integrity</span><strong>{esc(decision.get('integrity_status') or 'not_declared')}</strong></div>"
            f"<div><span>Decision source</span><strong>{esc(decision.get('decision_source') or 'not_declared')}</strong></div>"
            f"<div><span>Confidence</span><strong>{esc(decision.get('confidence') or 'not_declared')}</strong></div>"
            f"<div><span>Reviewer action</span><strong>{esc(decision.get('reviewer_action') or 'not_declared')}</strong></div>"
            "</div>"
            f"<p><span>Dynamic fields</span>{value_list(decision.get('dynamic_fields', []), empty='No dynamic fields declared')}</p>"
            f"<p><span>Frozen fields</span>{value_list(decision.get('frozen_fields', []), empty='No frozen fields declared')}</p>"
            f"<p><span>Required handoff</span>{value_list(decision.get('required_handoff_fields', []), empty='No handoff fields declared')}</p>"
        )
    return (
        '<div class="extensibility-block">'
        f'<p>{esc(summary)}</p>'
        f"{parameterization_html}"
        f'<p><span>Reusable slots</span>{slot_html}</p>'
        f'<ul>{note_html}</ul>'
        "</div>"
    )


def asset_usage_table(package: dict[str, Any]) -> str:
    rows = []
    for asset in package.get("asset_usage", []):
        display_context = asset.get("display_location") or asset.get("display_behavior") or "Not specified"
        rows.append(
            "<tr>"
            f"<td><strong>{esc(asset.get('asset_id') or 'Unknown')}</strong><br><span class=\"muted\">{esc(asset.get('asset_type') or 'image/support')}</span></td>"
            f"<td>{group_badge(asset.get('generation_timing') or 'unknown', 'asset')}</td>"
            f"<td>{esc(asset.get('use_step') or 'Not specified')}</td>"
            f"<td>{esc(asset_display_summary([asset]))}</td>"
            f"<td>{esc(asset_item_summary([asset]))}</td>"
            f"<td>{esc(display_context)}</td>"
            f"<td>{esc(asset.get('purpose') or asset.get('display_behavior') or 'Not specified')}</td>"
            f"<td>{esc(clip_text(asset.get('prompt_or_source') or 'Not specified'))}</td>"
            f"<td>{esc(asset.get('fallback_behavior') or 'Not specified')}</td>"
            "</tr>"
        )
    if not rows:
        return '<p class="muted">No image, card, line-art, icon, overlay, or displayed reference asset recorded for this package.</p>'
    return (
        '<div class="table-wrap"><table class="asset-usage-table">'
        "<thead><tr><th>Asset</th><th>Timing</th><th>When</th><th>Display beats</th><th>Image items</th><th>Where</th><th>Use</th><th>Prompt/source</th><th>Fallback</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table></div>"
    )


def asset_metric_strip(package: dict[str, Any]) -> str:
    assets = package.get("asset_usage", [])
    return f"""<div class="inline-fields asset-metric-strip">
      <div><span>Asset dependencies</span><strong>{esc(asset_dependency_count(assets))}</strong></div>
      <div><span>Display beats</span><strong>{esc(asset_display_summary(assets))}</strong></div>
      <div><span>Image items</span><strong>{esc(asset_item_summary(assets))}</strong></div>
    </div>"""


def storyboard_panel_rows(storyboard: dict[str, Any]) -> str:
    captions = storyboard.get("panel_captions", [])
    if not captions:
        return '<p class="muted">No panel captions were recorded.</p>'
    rows = []
    for item in captions:
        source = f'<span class="storyboard-source">{esc(item.get("source"))}</span>' if item.get("source") else ""
        label = f'<code>{esc(item.get("label"))}</code>' if item.get("label") else ""
        rows.append(
            '<li class="storyboard-caption-row">'
            f'<span class="storyboard-panel-number">{esc(item.get("number"))}</span>'
            '<div>'
            f'<strong>{esc(item.get("title"))} {label}</strong>'
            f'<p>{esc(item.get("caption"))}</p>'
            f'{source}'
            '</div>'
            '</li>'
        )
    return f'<ol class="storyboard-caption-list">{"".join(rows)}</ol>'


def storyboard_detail(package: dict[str, Any]) -> str:
    storyboard = package.get("storyboard") or {}
    if not storyboard:
        return '<p class="muted">No review-only mechanism storyboard was generated for this package.</p>'
    image = (
        f'<a class="storyboard-image-link" href="{esc(storyboard["image_href"])}" target="_blank" rel="noopener">'
        f'<img src="{esc(storyboard["image_href"])}" alt="Mechanism storyboard grid for {esc(package["activity_name"])}" loading="lazy">'
        '</a>'
        if storyboard.get("image_exists")
        else '<div class="storyboard-placeholder">Prompt ready; image not generated yet.</div>'
    )
    links = []
    if storyboard.get("prompt_exists"):
        links.append(preview_anchor(storyboard["prompt_href"], "storyboard prompt"))
    if storyboard.get("meta_exists"):
        links.append(preview_anchor(storyboard["meta_href"], "storyboard metadata"))
    if storyboard.get("image_exists"):
        links.append(f'<a href="{esc(storyboard["image_href"])}" target="_blank" rel="noopener">storyboard image</a>')
    link_html = " ".join(links) if links else '<span class="muted">No storyboard files linked.</span>'
    provenance = (
        '<div class="inline-fields storyboard-meta">'
        f'<div><span>Status</span><strong>{esc(storyboard.get("status") or "Unknown")}</strong></div>'
        f'<div><span>Version</span><strong>{esc(storyboard.get("version") or "Unknown")}</strong></div>'
        f'<div><span>Tool</span><strong>{esc(storyboard.get("tool") or "Unknown")}</strong></div>'
        f'<div><span>Target model</span><strong>{esc(storyboard.get("target_model") or "Unknown")}</strong></div>'
        f'<div><span>Actual model</span><strong>{esc(storyboard.get("actual_model") or "Unknown")}</strong></div>'
        f'<div><span>Generated</span><strong>{esc(storyboard.get("generated_at") or "Unknown")}</strong></div>'
        f'<div><span>Files</span><strong>{link_html}</strong></div>'
        '</div>'
    )
    rule_note = ""
    if storyboard.get("continuity_rules") or storyboard.get("caption_policy"):
        rule_note = (
            '<p class="storyboard-rule-note">'
            f'{esc(storyboard.get("continuity_rules") or "")}'
            f' {esc(storyboard.get("caption_policy") or "")}'
            '</p>'
        )
    return (
        '<div class="storyboard-block">'
        f'<figure class="storyboard-figure">{image}</figure>'
        '<div class="storyboard-detail-copy">'
        f'{provenance}'
        f'{rule_note}'
        f'{storyboard_panel_rows(storyboard)}'
        '</div>'
        '</div>'
    )


def prebuilt_asset_pilot_entries(run_dir: Path) -> list[dict[str, Any]]:
    manifest_path = run_dir / "generated_assets_pilot" / "asset_manifest.yaml"
    manifest = load_yaml(manifest_path)
    raw_entries = manifest.get("entries", [])
    if not isinstance(raw_entries, list):
        return []
    entries: list[dict[str, Any]] = []
    for raw_entry in raw_entries:
        if not isinstance(raw_entry, dict):
            continue
        meta_href = run_href(str(raw_entry.get("meta_path") or ""))
        meta = load_yaml(run_dir / meta_href) if meta_href else {}
        image_href = run_href(str(raw_entry.get("image_path") or meta.get("image_path") or ""))
        prompt_href = run_href(str(raw_entry.get("prompt_path") or meta.get("prompt_path") or ""))
        image_path = run_dir / image_href if image_href else Path()
        prompt_path = run_dir / prompt_href if prompt_href else Path()
        meta_path = run_dir / meta_href if meta_href else Path()
        entry = {
            "activity_id": normalize_text(meta.get("activity_id") or raw_entry.get("activity_id")),
            "activity_name": normalize_text(meta.get("activity_name") or raw_entry.get("activity_name") or raw_entry.get("activity_id")),
            "mechanic": normalize_text(meta.get("mechanic") or raw_entry.get("mechanic") or "unknown"),
            "asset_id": normalize_text(meta.get("asset_id") or raw_entry.get("asset_id")),
            "asset_type": normalize_text(meta.get("asset_type") or raw_entry.get("asset_type") or "image"),
            "requiredness": normalize_text(meta.get("requiredness") or raw_entry.get("requiredness") or "unknown"),
            "generation_timing": normalize_text(meta.get("generation_timing") or raw_entry.get("generation_timing") or "unknown"),
            "status": normalize_text(meta.get("status") or raw_entry.get("status") or "unknown"),
            "tool": normalize_text(meta.get("tool") or "Codex built-in image generation"),
            "target_model": normalize_text(meta.get("target_model") or "gpt-image-2"),
            "actual_model": normalize_text(meta.get("actual_model") or "codex-configured image model"),
            "generated_at": normalize_text(meta.get("generated_at") or ""),
            "use_step": normalize_text(meta.get("use_step") or "Not specified"),
            "display_location": normalize_text(meta.get("display_location") or "Not specified"),
            "purpose": normalize_text(meta.get("purpose") or "Not specified"),
            "display_behavior": normalize_text(meta.get("display_behavior") or ""),
            "fallback_behavior": normalize_text(meta.get("fallback_behavior") or "Not specified"),
            "safety_constraints": normalize_text(meta.get("safety_constraints") or "Not specified"),
            "prompt_href": prompt_href,
            "prompt_exists": bool(prompt_href and prompt_path.exists()),
            "meta_href": meta_href,
            "meta_exists": bool(meta_href and meta_path.exists()),
            "image_href": image_href,
            "image_exists": bool(image_href and image_path.exists()),
        }
        if entry["activity_id"] and entry["asset_id"]:
            entries.append(entry)
    return entries


def prebuilt_asset_pilot_card(entry: dict[str, Any]) -> str:
    image = (
        f'<a class="asset-pilot-image-link" href="{esc(entry["image_href"])}" target="_blank" rel="noopener">'
        f'<img src="{esc(entry["image_href"])}" alt="Prebuilt asset contact sheet for {esc(entry["asset_id"])}" loading="lazy">'
        '</a>'
        if entry.get("image_exists")
        else '<div class="asset-pilot-placeholder">Prompt ready; contact sheet not generated yet.</div>'
    )
    links = []
    if entry.get("prompt_exists"):
        links.append(preview_anchor(entry["prompt_href"], "asset prompt"))
    if entry.get("meta_exists"):
        links.append(preview_anchor(entry["meta_href"], "asset metadata"))
    if entry.get("image_exists"):
        links.append(f'<a href="{esc(entry["image_href"])}" target="_blank" rel="noopener">contact sheet</a>')
    link_html = " ".join(links) if links else '<span class="muted">No asset files linked.</span>'
    tag_html = "".join(
        [
            group_badge(entry["mechanic"], "mechanic"),
            group_badge(entry["status"], "status"),
            group_badge(entry["generation_timing"], "asset"),
            group_badge(entry["requiredness"], "kind"),
        ]
    )
    return f"""
<article class="asset-pilot-card" data-mechanic="{esc(entry['mechanic'])}" data-status="{esc(entry['status'])}">
  <figure class="asset-pilot-figure">{image}</figure>
  <div class="asset-pilot-copy">
    <div class="eyebrow">Generated prebuilt asset</div>
    <h3>{esc(entry['asset_id'])}</h3>
    <p class="activity-id">{esc(entry['activity_id'])}</p>
    <div class="tag-row">{tag_html}</div>
    <div class="inline-fields asset-pilot-fields">
      <div><span>When to display</span><strong>{esc(entry['use_step'])}</strong></div>
      <div><span>Where</span><strong>{esc(entry['display_location'])}</strong></div>
    </div>
    <div class="asset-placement">
      <p><span>Purpose</span>{esc(entry['purpose'])}</p>
      <p><span>Behavior</span>{esc(entry['display_behavior'] or 'Use the generated card sheet as a review proxy for runtime asset slices.')}</p>
      <p><span>Fallback</span>{esc(entry['fallback_behavior'])}</p>
      <p><span>Consistency</span>One contact sheet keeps card frame, lighting, scale, and illustration style consistent within this activity. Different mechanics use different style directions so cross-activity scenes remain visually distinct.</p>
    </div>
    <div class="file-row inline-file-row"><div>{link_html}</div></div>
  </div>
</article>"""


def prebuilt_asset_pilot_section(entries: list[dict[str, Any]]) -> str:
    if not entries:
        return ""
    generated = sum(1 for entry in entries if entry.get("status") == "generated")
    mechanics = sorted({entry.get("mechanic", "unknown") for entry in entries})
    cards = "\n".join(prebuilt_asset_pilot_card(entry) for entry in entries)
    return f"""
  <section class="panel" id="generated-assets">
    <div class="panel-head"><h2>Generated Prebuilt Assets</h2><span class="muted">{esc(generated)} of {esc(len(entries))} contact sheets generated</span></div>
    <div class="criteria-note">Pilot contact sheets cover one declared prebuilt/display asset per mechanic: {esc(', '.join(mechanics))}. They are review aids for child-facing asset direction and do not change the activity package contract.</div>
    <div class="asset-pilot-grid">{cards}</div>
  </section>
"""


def runtime_asset_output_entries(run_dir: Path) -> list[dict[str, Any]]:
    manifest_path = run_dir / "generated_assets" / "asset_outputs.yaml"
    manifest = load_yaml(manifest_path)
    raw_entries = manifest.get("entries", [])
    if not isinstance(raw_entries, list):
        return []
    reference_sources = load_yaml(run_dir / "generated_assets" / "reference_sources.yaml")
    sources_by_key: dict[tuple[str, str], dict[str, Any]] = {}
    for source in reference_sources.get("entries", []) if isinstance(reference_sources.get("entries"), list) else []:
        if not isinstance(source, dict):
            continue
        key = (normalize_text(source.get("activity_id")), normalize_text(source.get("asset_id")))
        if key[0] and key[1]:
            sources_by_key[key] = source
    entries: list[dict[str, Any]] = []
    for raw_entry in raw_entries:
        if not isinstance(raw_entry, dict):
            continue
        activity_id = normalize_text(raw_entry.get("activity_id"))
        asset_id = normalize_text(raw_entry.get("asset_id"))
        if not activity_id or not asset_id:
            continue
        source = sources_by_key.get((activity_id, asset_id), {})
        output_variants = raw_entry.get("output_variants", [])
        if not isinstance(output_variants, list):
            output_variants = []
        variant_links = []
        for variant in output_variants:
            if not isinstance(variant, dict):
                continue
            package_path = normalize_text(raw_entry.get("package_path"))
            variant_path = normalize_text(variant.get("path"))
            href = f"{package_path}/{variant_path}" if package_path and variant_path else ""
            variant_links.append(
                {
                    "variant_id": normalize_text(variant.get("variant_id")),
                    "path": variant_path,
                    "href": href,
                    "size": normalize_text(variant.get("size")),
                    "exists": bool(href and (run_dir / href).exists()),
                }
            )
        source_metadata_path = normalize_text(source.get("source_metadata_path"))
        source_original_path = normalize_text(source.get("source_original_path"))
        package_path = normalize_text(raw_entry.get("package_path"))
        entries.append(
            {
                "activity_id": activity_id,
                "asset_id": asset_id,
                "role": normalize_text(raw_entry.get("role")),
                "accuracy_mode": normalize_text(raw_entry.get("accuracy_mode")),
                "requiredness": normalize_text(raw_entry.get("requiredness")),
                "source_strategy": normalize_text(raw_entry.get("source_strategy")),
                "transformation_policy": normalize_text(raw_entry.get("transformation_policy")),
                "status": normalize_text(raw_entry.get("status")),
                "package_path": package_path,
                "work_item_path": normalize_text(raw_entry.get("work_item_path")),
                "work_item_exists": bool(raw_entry.get("work_item_path") and (run_dir / normalize_text(raw_entry.get("work_item_path"))).exists()),
                "variants": variant_links,
                "source_label": normalize_text(source.get("source_label")),
                "source_uri": normalize_text(source.get("source_uri")),
                "license": normalize_text(source.get("license")),
                "source_metadata_href": f"{package_path}/{source_metadata_path}" if package_path and source_metadata_path else "",
                "source_original_href": f"{package_path}/{source_original_path}" if package_path and source_original_path else "",
                "qa_notes": compact_list(raw_entry.get("qa_notes"), limit=4),
            }
        )
    return entries


def requested_runtime_asset_mode(manifest: dict[str, Any]) -> str:
    source = manifest.get("source", {}) if isinstance(manifest.get("source"), dict) else {}
    mode = normalize_text(source.get("asset_build")).lower()
    if mode and mode not in {"none", "manifest_only"}:
        return mode
    return ""


def runtime_asset_output_card(entry: dict[str, Any]) -> str:
    variant_links = []
    for variant in entry.get("variants", []):
        if not isinstance(variant, dict):
            continue
        label = f"{variant.get('variant_id') or 'variant'} {variant.get('size') or ''}".strip()
        if variant.get("exists"):
            variant_links.append(
                f'<a href="{esc(variant["href"])}" target="_blank" rel="noopener">{esc(label)}: {esc(variant["path"])}</a>'
            )
        elif variant.get("path"):
            variant_links.append(f'<span class="missing">{esc(label)} missing at {esc(variant["path"])}</span>')
    if not variant_links:
        variant_links.append('<span class="muted">No runtime variant paths recorded.</span>')
    source_links = []
    if entry.get("source_label"):
        source_links.append(f'<span>{esc(entry["source_label"])}</span>')
    if entry.get("source_metadata_href"):
        source_links.append(preview_anchor(entry["source_metadata_href"], "source metadata"))
    if entry.get("source_original_href"):
        source_links.append(f'<a href="{esc(entry["source_original_href"])}" target="_blank" rel="noopener">source original</a>')
    if entry.get("work_item_path"):
        source_links.append(preview_anchor(entry["work_item_path"], "work item"))
    qa = "; ".join(entry.get("qa_notes") or [])
    return f"""
<article class="runtime-asset-card" data-status="{esc(entry['status'])}">
  <div class="asset-pilot-copy">
    <div class="eyebrow">Generated runtime asset</div>
    <h3>{esc(entry['asset_id'])}</h3>
    <p class="activity-id">{esc(entry['activity_id'])}</p>
    <div class="tag-row">
      {group_badge(entry['status'], 'status')}
      {group_badge(entry['accuracy_mode'], 'asset')}
      {group_badge(entry['requiredness'], 'kind')}
      {group_badge(entry['role'], 'metadata')}
    </div>
    <div class="inline-fields asset-pilot-fields">
      <div><span>Source strategy</span><strong>{esc(entry['source_strategy'])}</strong></div>
      <div><span>Transform</span><strong>{esc(entry['transformation_policy'])}</strong></div>
    </div>
    <div class="asset-placement">
      <p><span>Runtime variants</span>{'<br>'.join(variant_links)}</p>
      <p><span>Reference/source</span>{' '.join(source_links) if source_links else 'No reference source recorded.'}</p>
      <p><span>QA</span>{esc(qa or 'No QA note recorded.')}</p>
    </div>
  </div>
</article>"""


def runtime_asset_output_section(run_dir: Path, entries: list[dict[str, Any]], requested_mode: str = "") -> str:
    asset_outputs_path = run_dir / "generated_assets" / "asset_outputs.yaml"
    manifest = load_yaml(asset_outputs_path)
    mode = normalize_text(manifest.get("asset_build_mode") or requested_mode or "unknown")
    if not entries:
        if not requested_mode:
            return ""
        message = "Missing asset_outputs.yaml" if not asset_outputs_path.exists() else "No asset output entries recorded"
        return f"""
  <section class="panel" id="runtime-assets">
    <div class="panel-head"><h2>Generated Runtime Assets</h2><span class="muted">0 assets built</span></div>
    <div class="criteria-note">Asset build mode `{esc(mode)}` was requested, but {esc(message)}. Run `python3 scripts/build_activity_assets.py runs/{esc(run_dir.name)} --mode {esc(mode)}` and regenerate this dashboard.</div>
  </section>
"""
    built = sum(1 for entry in entries if entry.get("status") in {"generated", "curated"})
    cards = "\n".join(runtime_asset_output_card(entry) for entry in entries)
    return f"""
  <section class="panel" id="runtime-assets">
    <div class="panel-head"><h2>Generated Runtime Assets</h2><span class="muted">{esc(built)} of {esc(len(entries))} assets built</span></div>
    <div class="criteria-note">Asset build mode `{esc(mode)}` writes separate package-local runtime assets and source metadata. Contact sheets remain review-only artifacts.</div>
    <div class="asset-pilot-grid">{cards}</div>
  </section>
"""


def activity_export_card(entry: dict[str, Any]) -> str:
    activity_id = normalize_text(entry.get("activity_id"))
    activity_name = normalize_text(entry.get("activity_name") or activity_id)
    asset_id = normalize_text(entry.get("asset_id"))
    html_path = normalize_text(entry.get("html_path"))
    storyboard_path = normalize_text(entry.get("storyboard_image_path"))
    tag_html = "".join(
        [
            group_badge("review packet", "kind"),
            group_badge("embedded asset", "asset"),
            group_badge("storyboard", "metadata" if storyboard_path else "status"),
        ]
    )
    return f"""
<article class="activity-export-card">
  <div class="activity-export-copy">
    <div class="eyebrow">Standalone reviewer packet</div>
    <h3>{esc(activity_name)}</h3>
    <p class="activity-id">{esc(activity_id)}</p>
    <div class="tag-row">{tag_html}</div>
    <div class="inline-fields activity-export-fields">
      <div><span>Integrated asset</span><strong>{esc(asset_id or 'Unknown')}</strong></div>
      <div><span>Storyboard</span><strong>{esc(storyboard_path or 'Not embedded')}</strong></div>
    </div>
    <div class="file-row inline-file-row"><div><a href="{esc(html_path)}">{esc(html_path)}</a></div></div>
  </div>
</article>"""


def activity_export_section(entries: list[dict[str, Any]]) -> str:
    clean_entries = [entry for entry in entries if isinstance(entry, dict)]
    if not clean_entries:
        return ""
    cards = "\n".join(activity_export_card(entry) for entry in clean_entries)
    return f"""
  <section class="panel" id="activity-html-exports">
    <div class="panel-head"><h2>Activity HTML Exports</h2><span class="muted">{esc(len(clean_entries))} standalone reviewer packets</span></div>
    <div class="criteria-note">These standalone reviewer packets embed the integrated contact sheet and the review-only mechanism storyboard for each exported activity. Storyboards explain the interaction mechanism; they are not child-facing runtime UI.</div>
    <div class="activity-export-grid">{cards}</div>
  </section>
"""


def package_detail_content(
    package: dict[str, Any],
    link_bits: str,
    runtime_map: str,
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
    <h4>Mechanism Storyboard</h4>
    {storyboard_detail(package)}
  </section>
  <section class="dialog-wide">
    <h4>Runtime Beats</h4>
    {runtime_map}
    <div class="runtime-source-label">Extracted source detail</div>
    <ol class="beat-list">{runtime or '<li>Unknown</li>'}</ol>
  </section>
  <section class="dialog-wide">
    <h4>Asset Usage Timeline</h4>
    <p class="muted">Asset dependencies count unique asset IDs or asset sets. Display beats count runtime appearances from the use-step range, so `prod.step_2; prod.step_3.round_1-2` is one asset dependency but three display beats. Image items show card set, count not declared when the source does not declare the exact count.</p>
    {asset_metric_strip(package)}
    {asset_usage_table(package)}
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
    <h4>Resolved Blockers</h4>
    <p class="muted">These are product-contract dependencies that would previously block the activity. This run assumes the minimum unblock decisions are now allowed.</p>
    {resolved_blocker_rows(package)}
  </section>
  <section class="dialog-wide">
    <h4>Extensibility</h4>
    {extensibility_rows(package)}
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
            "asset_usage",
            "reviewer",
            "review_reason",
            "resolved_blocker_types",
            "resolved_blockers",
            "extensibility_summary",
            "extensibility_notes",
            "parameter_slots",
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
    runtime_map = runtime_beat_map(package["runtime_beats"])
    runtime = "".join(runtime_beat_html(beat) for beat in package["runtime_beats"])
    details = "".join(f"<li>{esc(note)}</li>" for note in package["detail_notes"])
    changed = value_list(package["changed_files"], empty="No files changed")
    scorecard = scorecard_table(package["scorecard_rows"])
    modal_id = dom_id("activity-detail", package["activity_id"], package["assignment_index"])
    tags = package_tags(package)
    detail = package_detail_content(package, link_bits, runtime_map, runtime, details, changed, scorecard)
    summary = package["intro"] or package["brief_description"] or package["premise"]
    storyboard_status = (package.get("storyboard") or {}).get("status") or "not generated"
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
    <div><span>Asset dependencies</span><strong>{esc(asset_dependency_count(package['asset_usage']))}</strong></div>
    <div><span>Display beats</span><strong>{esc(asset_display_summary(package['asset_usage']))}</strong></div>
    <div><span>Image items</span><strong>{esc(asset_item_summary(package['asset_usage']))}</strong></div>
    <div><span>Storyboard</span><strong>{esc(storyboard_status)}</strong></div>
    <div><span>Resolved blockers</span><strong>{esc(len(package['resolved_blockers']))}</strong></div>
    <div><span>Reusable slots</span><strong>{esc(len(package['parameter_slots']))}</strong></div>
  </div>
  <div class="file-row">
    <div>{link_bits}</div>
    <button class="detail-button" type="button" data-open-detail>View details</button>
  </div>
  <template id="{esc(modal_id)}">{detail}</template>
</article>"""


def runtime_beat_kind(title: str) -> str:
    value = normalize_text(title).lower()
    if "round" in value:
        return "round"
    if "step 1" in value or "warm" in value or "cold" in value:
        return "setup"
    if "step 2" in value or "bridge" in value or "invite" in value:
        return "prompt"
    if "step 4" in value or "magic" in value or "celebrat" in value:
        return "payoff"
    if "step 5" in value or "closing" in value or "wrap" in value:
        return "close"
    return "beat"


def runtime_branch_followups(beat: dict[str, Any]) -> str:
    branches = beat.get("branches") if isinstance(beat.get("branches"), list) else []
    if not branches:
        child = normalize_text(beat.get("child"))
        followup = normalize_text(beat.get("followup"))
        return f"""
<div class="branch-followup-table-wrap">
  <table class="branch-followup-table">
    <thead><tr><th>Branch</th><th>Child behavior</th><th>AI follow-up</th></tr></thead>
    <tbody><tr class="branch-followup-observed">
      <td><span class="branch-chip branch-chip-observed">Observed</span></td>
      <td>{esc(child or "Unknown")}</td>
      <td>{esc(followup or "Unknown")}</td>
    </tr></tbody>
  </table>
</div>"""
    rows = []
    for branch in branches:
        token = branch_token(branch.get("token", "observed"))
        label = branch.get("label") or branch_label_for_token(token)
        child = branch.get("child") or "Unknown"
        followup = branch.get("followup") or "Unknown"
        rows.append(
            f"""
    <tr class="branch-followup-{esc(token)}">
      <td><span class="branch-chip branch-chip-{esc(token)}">{esc(label)}</span></td>
      <td>{esc(child)}</td>
      <td>{esc(followup)}</td>
    </tr>"""
        )
    return (
        '<div class="branch-followup-table-wrap">'
        '<table class="branch-followup-table">'
        "<thead><tr><th>Branch</th><th>Child behavior</th><th>AI follow-up</th></tr></thead>"
        f'<tbody>{"".join(rows)}</tbody></table></div>'
    )


def runtime_photo_timing(beat: dict[str, Any]) -> str:
    timing = normalize_text(beat.get("photo_timing"))
    if not timing:
        return ""
    return f'<div class="photo-timing-strip"><span>Photo timing</span><p>{esc(timing)}</p></div>'


def runtime_beat_map(beats: list[dict[str, Any]]) -> str:
    if not beats:
        return '<p class="muted">No visual runtime map available.</p>'
    nodes = []
    for index, beat in enumerate(beats, start=1):
        title = beat.get("title") or "Runtime beat"
        kind = runtime_beat_kind(title)
        photo_timing = runtime_photo_timing(beat)
        is_contract = beat.get("speech_mode") == "runtime_contract"
        ai_label = "Runtime behavior contract" if is_contract else "AI prompt"
        followup_label = "Child branches and AI follow-up policy" if is_contract else "Child branches and AI follow-ups"
        screen_label = "Screen/state" if is_contract else "Screen"
        example_line = (
            f'\n      <div class="runtime-lane runtime-lane-example"><span>Example AI line</span><p>{esc(beat.get("example_ai_line") or "Unknown")}</p></div>'
            if is_contract
            else ""
        )
        nodes.append(
            f"""<li class="runtime-map-node runtime-map-node-{esc(kind)}">
  <div class="runtime-step-marker"><span>{index:02d}</span></div>
  <div class="runtime-step-body">
    <div class="runtime-map-head"><strong>{esc(title)}</strong><span>{esc(kind)}</span></div>
    <div class="runtime-lanes">
      <div class="runtime-lane runtime-lane-ai"><span>{esc(ai_label)}</span><p>{esc(beat.get("ai") or "Unknown")}</p></div>{example_line}
      <div class="runtime-lane runtime-lane-followup"><span>{esc(followup_label)}</span>{runtime_branch_followups(beat)}</div>
    </div>
{photo_timing}
    <div class="screen-strip"><span>{esc(screen_label)}</span><p>{esc(beat.get("screen") or "Unknown")}</p></div>
  </div>
</li>"""
        )
    return f'<ol class="runtime-map">{"".join(nodes)}</ol>'


def runtime_beat_html(beat: dict[str, Any]) -> str:
    if beat.get("speech_mode") == "runtime_contract":
        fields = [
            ("Runtime behavior contract", beat.get("runtime_instruction", "")),
            ("Example AI line", beat.get("example_ai_line", "")),
            ("Child", beat.get("child", "")),
            ("Follow-up policy", beat.get("followup", "")),
        ]
        screen_label = "Screen/state"
    else:
        fields = [
            ("AI", beat.get("ai", "")),
            ("Child", beat.get("child", "")),
            ("Follow-up", beat.get("followup", "")),
        ]
        screen_label = "Screen"
    if normalize_text(beat.get("photo_timing")):
        fields.append(("Photo timing", beat.get("photo_timing", "")))
    fields.append((screen_label, beat.get("screen", "")))
    field_html = "".join(
        f'<div class="beat-field"><span>{esc(label)}</span><p>{esc(value or "Unknown")}</p></div>'
        for label, value in fields
    )
    return f'<li><strong>{esc(beat.get("title", "Runtime beat"))}</strong>{field_html}</li>'


def blocked_comment_summary(comments: list[dict[str, str]]) -> str:
    if not comments:
        return '<span class="muted">No inline blocked markers recorded</span>'
    counts: dict[str, int] = {}
    for comment in comments:
        label = comment["label"]
        counts[label] = counts.get(label, 0) + 1
    return " ".join(
        reason_badge(label, "blocked-element-chip", suffix=f" x{count}")
        for label, count in sorted(counts.items())
    )


def blocked_comment_rows(comments: list[dict[str, str]]) -> str:
    if not comments:
        return '<li class="blocked-marker-row"><span class="muted">No inline BLOCKED ELEMENT comments were recorded.</span></li>'
    return "".join(
        '<li class="blocked-marker-row">'
        f'{reason_badge(comment["label"], "blocked-element-chip")}'
        f'<span>{esc(comment["text"])}</span>'
        "</li>"
        for comment in comments
    )


def minimum_unblock_rows(item: dict[str, Any]) -> str:
    labels = item.get("reason_types", []) + item.get("blocked_comment_types", [])
    definitions = reason_definitions(labels) or [FALLBACK_REASON]
    return "".join(
        '<li class="minimum-unblock-row">'
        f'{reason_badge(definition["label"], "minimum-unblock-chip")}'
        f'<p>{esc(definition.get("unblocks_when", FALLBACK_REASON["unblocks_when"]))}</p>'
        "</li>"
        for definition in definitions
    )


def blocked_preview_scorecard_rows(item: dict[str, Any]) -> list[dict[str, str]]:
    reason_types = item.get("reason_types", []) or [FALLBACK_REASON["label"]]
    blockers = ", ".join(reason_types)
    has_preview = bool(item.get("preview_exists") and item.get("preview_beats"))
    marker_count = len(item.get("blocked_comments", []))
    marker_type_count = len(item.get("blocked_comment_types", []))
    marker_note = f"{marker_count} inline blocked marker(s) across {marker_type_count} blocker type(s)."
    has_branches = any(
        normalize_text(beat.get("child")) and normalize_text(beat.get("followup"))
        for beat in item.get("preview_beats", [])
    )
    has_screen = any(normalize_text(beat.get("screen")) for beat in item.get("preview_beats", []))
    has_magic = any("magic moment" in normalize_text(beat.get("title")).lower() for beat in item.get("preview_beats", []))
    reviewable = "REVIEWABLE" if has_preview else "BLOCKED"
    return [
        {
            "number": "1",
            "dimension": "V1 Technical Compliance",
            "score": "BLOCKED",
            "notes": f"Blocked by unresolved {blockers}. The preview remains invalid until the product/design decision is resolved.",
        },
        {
            "number": "2",
            "dimension": "Hook & Transition",
            "score": reviewable,
            "notes": "The constrained preview can be inspected for opening flow." if has_preview else "No constrained preview was recorded.",
        },
        {
            "number": "3",
            "dimension": "Edge Case Coverage",
            "score": "REVIEWABLE" if has_branches else "BLOCKED",
            "notes": "Preview includes child branches and follow-up behavior, but final pass depends on resolved blockers." if has_branches else "Branch coverage cannot be judged without preview beats.",
        },
        {
            "number": "4",
            "dimension": "IB Completeness",
            "score": "BLOCKED",
            "notes": "No valid five-file package or final metadata should be produced until blockers are resolved.",
        },
        {
            "number": "5",
            "dimension": "Tier Appropriateness",
            "score": reviewable,
            "notes": f"Tier target is {item.get('tier') or 'unknown'}; final dialogue must be rechecked after blockers are resolved.",
        },
        {
            "number": "6",
            "dimension": "Dialogue Specificity",
            "score": reviewable,
            "notes": "Preview dialogue is available for human review, but blocked markers identify unsupported assumptions.",
        },
        {
            "number": "7",
            "dimension": "Screen & UI Completeness",
            "score": "REVIEWABLE" if has_screen else "BLOCKED",
            "notes": "Screen states are present for preview review." if has_screen else "Screen states are missing or unavailable in the preview.",
        },
        {
            "number": "8",
            "dimension": "Entity Mapping Alignment",
            "score": "N/A",
            "notes": "Blocked concept previews are treated as product-decision triage unless the brief explicitly requires mapping.",
        },
        {
            "number": "9",
            "dimension": "Game Feel",
            "score": "REVIEWABLE" if has_magic else reviewable,
            "notes": "Preview includes a magic-moment beat." if has_magic else "Preview can be reviewed for payoff, but the final package must re-score this after blockers are resolved.",
        },
        {
            "number": "10",
            "dimension": "Mechanic Fidelity + Scaffold Honesty",
            "score": "BLOCKED",
            "notes": f"{marker_note} The mechanic cannot be marked valid until these blocked elements are resolved or removed.",
        },
    ]


def blocked_tags(item: dict[str, Any]) -> str:
    tags = [
        group_badge(item["category"], "category"),
        group_badge(item["status"], "status"),
        group_badge(item["mechanic"], "mechanic"),
        group_badge(item["tier"], "tier"),
        group_badge(item["asset_policy"], "asset"),
    ]
    tags.extend(reason_badge(reason, "blocked-reason-type") for reason in item["reason_types"])
    return "".join(tags)


def blocked_detail_content(
    item: dict[str, Any],
    decisions: str,
    flag_badges: str,
    minimum_unblock: str,
    preview_runtime_map: str,
    preview_runtime: str,
    comments: str,
    marker_summary: str,
    scorecard: str,
    brief_href: str,
    preview_link: str,
    design_status: str,
) -> str:
    return f"""
<div class="dialog-grid">
  <section>
    <h4>Missing Product Decisions</h4>
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
    <h4>Minimum To Unblock</h4>
    <p class="muted">Smallest policy or scope decision needed before this preview can become a valid package.</p>
    <ul class="minimum-unblock-list">{minimum_unblock}</ul>
  </section>
  <section>
    <h4>Inline Blocked Markers</h4>
    <p class="muted">These are occurrences inside the preview steps, not separate missing decisions.</p>
    <div class="blocked-marker-summary">{marker_summary}</div>
    <ul class="blocked-marker-list">{comments}</ul>
  </section>
  <section class="dialog-wide">
    <h4>Constrained Preview Beats</h4>
    {preview_runtime_map}
    <div class="runtime-source-label">Extracted source detail</div>
    <ol class="beat-list">{preview_runtime}</ol>
  </section>
  <section class="dialog-wide">
    <h4>Blocked Preview Scorecard</h4>
    <p class="muted">This is review evidence only. It does not turn a blocked preview into a passing package.</p>
    {scorecard}
  </section>
  <section class="dialog-wide">
    <h4>Files</h4>
    <div class="file-row inline-file-row">{preview_anchor(brief_href, "blocked brief")}{preview_link}</div>
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
    comment_text = [comment["text"] for comment in item["blocked_comments"]]
    search += " " + " ".join(
        item["reason_types"]
        + item["blocked_comment_types"]
        + item["missing_decisions"]
        + item["flags"]
        + comment_text
    )
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
        preview_anchor(preview_href, "blocked design preview")
        if item["design_preview"] and item["preview_exists"]
        else '<span class="muted">No constrained design preview in this legacy run</span>'
    )
    if item["preview_exists"]:
        design_status = "Constrained design preview available; invalid until blockers are resolved."
    else:
        design_status = "No constrained design preview was recorded for this legacy run; future blocked assignments should include detailed steps with inline blocked-element comments."
    preview_runtime_map = runtime_beat_map(item["preview_beats"])
    preview_runtime = "".join(runtime_beat_html(beat) for beat in item["preview_beats"])
    preview_runtime = preview_runtime or "<li>No constrained runtime beats were recorded.</li>"
    comments = blocked_comment_rows(item["blocked_comments"])
    marker_summary = blocked_comment_summary(item["blocked_comments"])
    minimum_unblock = minimum_unblock_rows(item)
    scorecard = scorecard_table(blocked_preview_scorecard_rows(item))
    modal_id = dom_id("blocked-detail", item["activity_concept"], item["assignment_index"])
    tags = blocked_tags(item)
    detail = blocked_detail_content(
        item,
        decisions,
        flag_badges,
        minimum_unblock,
        preview_runtime_map,
        preview_runtime,
        comments,
        marker_summary,
        scorecard,
        brief_href,
        preview_link,
        design_status,
    )
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
    <div><span>Inline blocked markers</span><strong>{esc(len(item['blocked_comments']))}</strong></div>
    <div><span>Unique blocker types</span><strong>{esc(len(item['blocked_comment_types']))}</strong></div>
    <div><span>Preview beats</span><strong>{esc(len(item['preview_beats']))}</strong></div>
  </div>
  <div class="file-row">{preview_anchor(brief_href, "blocked brief")}<button class="detail-button" type="button" data-open-detail>View details</button></div>
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
            f"<td>{reason_badge(item['label'])}</td>"
            f"<td>{esc(item['meaning'])}</td>"
            f"<td>{esc(item['why'])}</td>"
            f"<td>{esc(item.get('unblocks_when', 'Resolve the missing product or design decision recorded in the brief.'))}</td>"
            "</tr>"
        )
    return f"""
  <section class="panel" id="blocking-reason-guide">
    <div class="panel-head"><h2>Blocking Reason Guide</h2></div>
    <div class="criteria-note">Each row also lists the minimum policy or scope decision that would make the blocker valid. Resolve any one of the listed options to unblock — full capability approval is not required, sometimes a "no verification" or fallback-only decision is enough.</div>
    <div class="table-wrap"><table class="reason-guide-table">
      <thead><tr><th>Reason</th><th>What it means</th><th>Why it blocks validity</th><th>Minimum to unblock</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table></div>
  </section>
"""


def resolved_contract_summary(packages: list[dict[str, Any]]) -> str:
    packages_with_items = [package for package in packages if package.get("resolved_blockers")]
    if not packages_with_items:
        return ""
    rows = []
    for package in packages_with_items:
        chips = " ".join(reason_badge(label, "resolved-blocker-chip") for label in package["resolved_blocker_types"])
        type_count = len(package["resolved_blocker_types"])
        note_count = len(package["resolved_blockers"])
        rows.append(
            "<tr>"
            f"<td>{esc(package['activity_name'])}<br><span class=\"muted\">{esc(package['activity_id'])}</span></td>"
            f"<td>{chips}</td>"
            f"<td>{esc(type_count)}</td>"
            f"<td>{esc(note_count)}</td>"
            "</tr>"
        )
    return f"""
  <section class="panel" id="resolved-contract-items">
    <div class="panel-head"><h2>Resolved Contract Items</h2></div>
    <div class="criteria-note">This run assumes the minimum unblock decisions are now part of the product contract. The activity detail dialogs still call out where those formerly blocking capabilities appear.</div>
    <div class="table-wrap"><table class="reason-guide-table">
      <thead><tr><th>Activity</th><th>Resolved blocker types</th><th>Type count</th><th>Resolved notes</th></tr></thead>
      <tbody>{''.join(rows)}</tbody>
    </table></div>
  </section>
"""


def extensibility_summary(packages: list[dict[str, Any]]) -> str:
    rows = []
    for package in packages:
        notes = package.get("extensibility_notes", [])
        slots = package.get("parameter_slots", [])
        decision = package.get("parameterization_decision") or {}
        if not notes and not slots and not decision:
            continue
        rows.append(
            "<tr>"
            f"<td>{esc(package['activity_name'])}<br><span class=\"muted\">{esc(package['activity_id'])}</span></td>"
            f"<td>{esc(package.get('entity_binding') or 'unknown')}</td>"
            f"<td>{esc(decision.get('mode') or 'not_declared')}</td>"
            f"<td>{esc(decision.get('integrity_status') or 'not_declared')}</td>"
            f"<td>{value_list(slots, empty='No explicit slots')}</td>"
            f"<td>{value_list(decision.get('dynamic_fields', []), empty='No dynamic fields declared')}</td>"
            f"<td>{value_list(decision.get('required_handoff_fields', []), empty='No handoff fields declared')}</td>"
            f"<td>{esc(notes[0] if notes else package.get('extensibility_summary') or 'Reusable by changing the concept context.')}</td>"
            "</tr>"
        )
    if not rows:
        return ""
    return f"""
  <section class="panel" id="extensibility-overview">
    <div class="panel-head"><h2>Extensibility Overview</h2></div>
    <div class="criteria-note">This section highlights whether an activity can be extended to other entities, topics, or matched properties by replacing slots such as {{runtime_entity}}, {{shared_feature}}, or asset-set IDs, and whether the parameterization decision has enough integrity evidence for runtime handoff.</div>
    <div class="table-wrap"><table class="reason-guide-table">
      <thead><tr><th>Activity</th><th>Binding</th><th>Parameterization mode</th><th>Integrity</th><th>Reusable slots</th><th>Dynamic fields</th><th>Required handoff</th><th>How to extend</th></tr></thead>
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


def dashboard_workflow(run_id: str) -> str:
    run_path = f"runs/{run_id}"
    return f"""<section class="panel" id="dashboard-workflow">
    <div class="panel-head"><h2>Review Dashboard Workflow</h2></div>
    <div class="criteria-note">This HTML file is generated once after package generation, reviewer evidence, manifest entries, blocked previews, and package checks are current. It is derived from run files and package files; it is not a source of truth.</div>
    <ol class="workflow-list">
      <li><strong>Collect run inputs</strong><span>Read `run_manifest.yaml`, `review_notes.md`, `results.tsv`, generated or enriched package files, blocked briefs, and blocked design previews.</span></li>
      <li><strong>Prepare mechanism storyboard prompts</strong><code>python3 scripts/generate_storyboard_prompts.py {esc(run_path)}</code></li>
      <li><strong>Generate review-only storyboard images</strong><span>Use Codex image generation with the prompt files under `visual_storyboards/&lt;activity_id&gt;/`, then copy each final PNG to `mechanism_grid.png` and rerun the prompt script to refresh metadata. Prompt-only storyboard experiments are ignored when generated v1 images are present.</span></li>
      <li><strong>Repair full-pass asset manifest bundle</strong><code>python3 scripts/repair_full_pass_asset_bundle.py {esc(run_path)}</code></li>
      <li><strong>Build runtime assets when requested</strong><code>python3 scripts/build_activity_assets.py {esc(run_path)} --mode generate_and_curate</code><span>Use agent-generated illustrative PNGs and verified reference originals as inputs; write scene assets into package-local `assets/` and picker item sprites into `assets/items/`.</span></li>
      <li><strong>Validate runtime asset outputs</strong><code>python3 scripts/validate_asset_build_outputs.py {esc(run_path)}</code></li>
      <li><strong>Validate full-pass asset bundle</strong><code>python3 scripts/validate_full_pass_asset_bundle.py {esc(run_path)}</code></li>
      <li><strong>Prepare prebuilt asset prompts</strong><code>python3 scripts/generate_asset_pilot_prompts.py {esc(run_path)}</code></li>
      <li><strong>Generate prebuilt contact sheets</strong><span>Use Codex image generation with `generated_assets_pilot/&lt;activity_id&gt;/&lt;asset_id&gt;/contact_sheet.prompt.md`, copy the selected PNG to `contact_sheet.png`, then rerun the prompt script so `asset.meta.yaml` and `asset_manifest.yaml` record status, timing, placement, fallback, and provenance.</span></li>
      <li><strong>Integrate generated assets</strong><code>python3 scripts/integrate_generated_assets.py {esc(run_path)}</code></li>
      <li><strong>Validate integrated assets</strong><code>python3 scripts/integrate_generated_assets.py --validate {esc(run_path)}</code></li>
      <li><strong>Export integrated activity HTMLs</strong><code>python3 scripts/export_activity_html.py {esc(run_path)}</code></li>
      <li><strong>Validate activity HTML exports</strong><code>python3 scripts/export_activity_html.py --validate {esc(run_path)}</code></li>
      <li><strong>Generate the dashboard</strong><code>python3 scripts/generate_run_review.py {esc(run_path)}</code></li>
      <li><strong>Validate the dashboard</strong><code>python3 scripts/generate_run_review.py --validate {esc(run_path)}</code></li>
      <li><strong>Record provenance</strong><span>Keep `outputs.review_dashboard` pointing to `{esc(run_path)}/review.html` and record the generation and validation checks in the run manifest.</span></li>
    </ol>
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


def reviewer_by_activity(review_notes: str) -> dict[str, str]:
    body = section(review_notes, "Generated Package Review") + "\n\n" + section(review_notes, "Existing Package Enrichment Audit")
    reviewers: dict[str, str] = {}
    for line in body.splitlines():
        if not line.startswith("- Reviewer "):
            continue
        match = re.match(r"- Reviewer\s+([^(`:]+)", line)
        if not match:
            continue
        reviewer = normalize_text(match.group(1))
        for activity_id in re.findall(r"`(concept_[^`]+)`", line):
            reviewers[activity_id] = reviewer
    return reviewers


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
    _PREVIEW_REGISTRY.clear()
    _PREVIEW_CTX["repo_root"] = repo_root
    _PREVIEW_CTX["run_dir"] = run_dir
    manifest = load_yaml(run_dir / "run_manifest.yaml")
    if not manifest:
        raise SystemExit(f"Missing or unreadable manifest: {run_dir / 'run_manifest.yaml'}")
    outputs = manifest.get("outputs", {}) if isinstance(manifest.get("outputs"), dict) else {}
    generated = [collect_package(repo_root, run_dir, entry, "Generated") for entry in outputs.get("generated_activities", [])]
    enriched = [collect_package(repo_root, run_dir, entry, "Enriched") for entry in outputs.get("enriched_activities", [])]
    audited = [collect_package(repo_root, run_dir, entry, "Audited") for entry in outputs.get("audited_activities", [])]
    packages = generated + enriched + audited
    review_notes = read_text(run_dir / "review_notes.md")
    reviewers = reviewer_by_activity(review_notes)
    for package in packages:
        reviewer = reviewers.get(package["activity_id"])
        if reviewer and css_token(package.get("reviewer")) in {"", "unknown", "n-a"}:
            package["reviewer"] = reviewer
    results_by_activity = read_results(repo_root)
    for package in packages:
        result = results_by_activity.get(package["activity_path"], {}) or results_by_activity.get(package["activity_id"], {})
        if result:
            package["result_summary"] = f"{result.get('status', 'logged')} at {result.get('timestamp', 'unknown time')}"
        elif package["kind"] == "Enriched":
            package["result_summary"] = "Enrichment only"
        elif package["kind"] == "Audited":
            package["result_summary"] = "Audit pass, no package edits"
        else:
            package["result_summary"] = "Not logged"
    blocked = [collect_blocked(repo_root, entry) for entry in outputs.get("blocked_assignments", [])]
    asset_pilot_entries = prebuilt_asset_pilot_entries(run_dir)
    runtime_asset_entries = runtime_asset_output_entries(run_dir)
    requested_runtime_mode = requested_runtime_asset_mode(manifest)
    export_manifest = load_yaml(run_dir / "activity_exports" / "export_manifest.yaml")
    export_entries = export_manifest.get("entries", []) if isinstance(export_manifest.get("entries"), list) else []
    summary = manifest.get("summary", {}) if isinstance(manifest.get("summary"), dict) else {}
    run_id = normalize_text(manifest.get("run_id") or run_dir.name)
    source = manifest.get("source", {}) if isinstance(manifest.get("source"), dict) else {}
    run_links = [
        ("run_manifest.yaml", "run_manifest.yaml"),
        ("review_notes.md", "review_notes.md"),
        ("assignment_snapshot.md", "assignment_snapshot.md"),
        ("generated_activity_ids.txt", "generated_activity_ids.txt"),
    ]
    if (run_dir / "results.tsv").exists():
        run_links.append(("results.tsv", "results.tsv"))
    elif source.get("results_file"):
        run_links.append(("results.tsv", f"../../{source['results_file']}"))
    if source.get("assignments_file"):
        run_links.append(("assignments.md", f"../../{source['assignments_file']}"))
    active_storyboard_root = active_storyboard_root_name(run_dir)
    if active_storyboard_root:
        label = "storyboard_manifest_v2.yaml" if active_storyboard_root.endswith("_v2") else "storyboard_manifest.yaml"
        run_links.insert(4, (label, f"{active_storyboard_root}/storyboard_manifest.yaml"))
    if (run_dir / "generated_assets" / "asset_outputs.yaml").exists():
        run_links.insert(5, ("asset_outputs.yaml", "generated_assets/asset_outputs.yaml"))
    if (run_dir / "generated_assets" / "reference_sources.yaml").exists():
        run_links.insert(6, ("reference_sources.yaml", "generated_assets/reference_sources.yaml"))
    if (run_dir / "generated_assets" / "qa_notes.yaml").exists():
        run_links.insert(7, ("qa_notes.yaml", "generated_assets/qa_notes.yaml"))
    if (run_dir / "generated_assets_pilot" / "asset_manifest.yaml").exists():
        run_links.insert(5, ("asset_manifest.yaml", "generated_assets_pilot/asset_manifest.yaml"))
    if (run_dir / "activity_exports" / "export_manifest.yaml").exists():
        run_links.insert(6, ("export_manifest.yaml", "activity_exports/export_manifest.yaml"))
    package_categories = [p["category"] for p in packages]
    package_statuses = [p["status"] for p in packages]
    package_mechanics = [p["mechanic"] for p in packages]
    package_tiers = [p["tier"] for p in packages]
    package_assets = [p["asset_policy"] for p in packages]
    package_kinds = [p["kind"] for p in packages]
    blocked_categories = [b["category"] for b in blocked]
    blocked_mechanics = [b["mechanic"] for b in blocked]
    blocked_reasons = [reason for item in blocked for reason in item["reason_types"]]
    resolved_reasons = [
        reason
        for package in packages
        for reason in package.get("resolved_blocker_types", [])
    ]
    run_link_html = "".join(preview_anchor(href, label) for label, href in run_links)
    package_cards = "\n".join(package_card(package) for package in packages)
    blocked_cards = "\n".join(blocked_card(item) for item in blocked)
    reason_guide_html = reason_guide(blocked_reasons + resolved_reasons).strip()
    resolved_contract_html = resolved_contract_summary(packages).strip()
    extensibility_html = extensibility_summary(packages).strip()
    asset_pilot_html = prebuilt_asset_pilot_section(asset_pilot_entries).strip()
    runtime_asset_html = runtime_asset_output_section(run_dir, runtime_asset_entries, requested_runtime_mode).strip()
    activity_export_html = activity_export_section(export_entries).strip()
    criteria_guide_html = criteria_guide().strip()
    manifest_checks = manifest.get("checks", [])
    checks = render_checks(manifest_checks)
    css = """
:root {
  color-scheme: light;
  --content-max: 1500px;
  --sidebar-width: 244px;
  --sidebar-top: 116px;
  /* Warm paper palette with a confident indigo-ink accent. */
  --bg: oklch(98.2% 0.006 85);
  --bg-grain: oklch(96.6% 0.011 85);
  --panel: oklch(99.4% 0.003 85);
  --panel-soft: oklch(97.1% 0.008 85);
  --panel-raised: oklch(99.7% 0.002 85);
  --control: oklch(99.5% 0.002 85);
  --text: oklch(21% 0.038 264);
  --text-soft: oklch(32% 0.04 264);
  --muted: oklch(48% 0.034 264);
  --line: oklch(89.5% 0.014 250);
  --line-strong: oklch(78% 0.022 250);
  --hairline: color-mix(in oklch, var(--line) 70%, transparent);
  --shadow-soft: 0 1px 0 oklch(100% 0 0 / 0.6), 0 8px 22px oklch(28% 0.06 264 / 0.06);
  --shadow-raised: 0 1px 0 oklch(100% 0 0 / 0.6), 0 14px 36px oklch(28% 0.06 264 / 0.08);
  --shadow-hover: 0 1px 0 oklch(100% 0 0 / 0.6), 0 18px 44px oklch(28% 0.06 264 / 0.14);
  --accent: oklch(40% 0.18 268);
  --accent-ink: oklch(28% 0.13 268);
  --accent-soft: oklch(95% 0.03 268);
  --accent-line: oklch(76% 0.07 268);
  --blue: var(--accent);
  --blue-bg: var(--accent-soft);
  --blue-text: var(--accent-ink);
  --green-bg: oklch(95% 0.04 158);
  --green-text: oklch(34% 0.11 158);
  --amber-bg: oklch(95.5% 0.058 85);
  --amber-text: oklch(38% 0.11 70);
  --red-bg: oklch(94.5% 0.045 28);
  --red-text: oklch(40% 0.14 28);
  --purple-bg: oklch(95% 0.032 306);
  --purple-text: oklch(38% 0.13 306);
  --teal-bg: oklch(95% 0.035 188);
  --teal-text: oklch(34% 0.1 188);
  --neutral-tag-bg: oklch(94.5% 0.008 245);
  --neutral-tag-text: oklch(38% 0.03 245);
  --display-stack: ui-serif, "Iowan Old Style", "Hoefler Text", Charter, "Source Serif Pro", Georgia, serif;
  --sans-stack: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", system-ui, sans-serif;
  --mono-stack: ui-monospace, "SF Mono", SFMono-Regular, Menlo, Consolas, monospace;
  --radius-sm: 4px;
  --radius: 6px;
  --radius-lg: 10px;
  --tnum: tabular-nums;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  background:
    radial-gradient(circle at 0% -10%, var(--bg-grain), transparent 38%),
    radial-gradient(circle at 100% 0%, var(--bg-grain), transparent 42%),
    var(--bg);
  color: var(--text);
  font: 14px/1.55 var(--sans-stack);
  font-feature-settings: "ss01", "cv11";
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent-ink); text-decoration: none; border-bottom: 1px solid color-mix(in oklch, var(--accent) 30%, transparent); transition: border-color 100ms ease, color 100ms ease; }
a:hover { text-decoration: none; border-bottom-color: var(--accent); color: var(--accent); }
header {
  background: linear-gradient(180deg, color-mix(in oklch, var(--panel) 92%, var(--accent-soft) 8%), var(--panel) 70%);
  border-bottom: 1px solid var(--line);
  position: sticky;
  top: 0;
  z-index: 20;
  backdrop-filter: saturate(140%) blur(8px);
}
.header-inner {
  max-width: var(--content-max);
  margin: 0 auto;
  padding: 22px 28px 18px;
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 16px;
  align-items: end;
}
.header-inner > .header-main { min-width: 0; }
.header-rule {
  height: 1px;
  background: linear-gradient(90deg, var(--accent), transparent 60%);
  margin-bottom: 16px;
  width: 96px;
}
.eyebrow {
  color: var(--accent);
  font-size: 10.5px;
  font-weight: 760;
  letter-spacing: .14em;
  text-transform: uppercase;
  font-feature-settings: "ss01";
}
.eyebrow.eyebrow-muted { color: var(--muted); }
h1 {
  margin: 6px 0 10px;
  font-family: var(--display-stack);
  font-size: clamp(28px, 2vw + 18px, 38px);
  line-height: 1.08;
  letter-spacing: -0.022em;
  font-weight: 540;
  color: var(--text);
}
h2 {
  margin: 0;
  font-size: 13px;
  font-weight: 760;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--text);
}
h3 { margin: 2px 0 0; font-size: 16px; line-height: 1.28; letter-spacing: -0.005em; font-weight: 640; }
h4 { margin: 0 0 8px; font-size: 11px; letter-spacing: .1em; text-transform: uppercase; font-weight: 720; color: var(--muted); }
.summary-line {
  display: flex;
  flex-wrap: wrap;
  gap: 6px 22px;
  color: var(--muted);
  font-size: 12.5px;
  font-variant-numeric: var(--tnum);
}
.summary-line strong { color: var(--text); font-weight: 640; }
.summary-line .status-strong {
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.summary-line .status-dot {
  width: 8px;
  height: 8px;
  border-radius: 999px;
  background: oklch(60% 0.16 145);
  box-shadow: 0 0 0 3px color-mix(in oklch, oklch(60% 0.16 145) 22%, transparent);
}
.summary-line .status-dot.status-blocked { background: oklch(64% 0.14 75); box-shadow: 0 0 0 3px color-mix(in oklch, oklch(64% 0.14 75) 22%, transparent); }
.summary-line .status-dot.status-fail { background: oklch(58% 0.18 28); box-shadow: 0 0 0 3px color-mix(in oklch, oklch(58% 0.18 28) 22%, transparent); }
.summary-line .status-dot.status-progress { background: oklch(62% 0.14 220); box-shadow: 0 0 0 3px color-mix(in oklch, oklch(62% 0.14 220) 22%, transparent); }
.header-stamp {
  align-self: end;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 8px 12px;
  background: var(--panel-raised);
  color: var(--muted);
  font-size: 11px;
  letter-spacing: .08em;
  text-transform: uppercase;
  font-weight: 720;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-variant-numeric: var(--tnum);
}
.header-stamp strong { color: var(--text); font-weight: 720; letter-spacing: 0; text-transform: none; font-size: 12px; }
main { max-width: var(--content-max); margin: 0 auto; padding: 22px 28px 56px; }
.review-layout {
  display: grid;
  grid-template-columns: var(--sidebar-width) minmax(0, 1fr);
  gap: 22px;
  align-items: start;
}
.review-content { grid-column: 2; min-width: 0; display: grid; gap: 18px; }
.sidebar {
  position: fixed;
  top: var(--sidebar-top);
  bottom: 24px;
  left: max(28px, calc((100vw - var(--content-max)) / 2 + 28px));
  width: var(--sidebar-width);
  overflow: auto;
  overscroll-behavior: contain;
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  background: var(--panel-raised);
  box-shadow: var(--shadow-soft);
  padding: 14px;
  z-index: 5;
}
.sidebar-title {
  margin: 0 4px 10px;
  font-size: 10px;
  font-weight: 760;
  letter-spacing: .16em;
  text-transform: uppercase;
  color: var(--muted);
}
.side-nav { display: grid; gap: 2px; }
.side-nav a {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 30px;
  border-radius: var(--radius-sm);
  padding: 6px 9px;
  color: var(--text-soft);
  font-weight: 600;
  font-size: 13px;
  letter-spacing: -0.002em;
  border-bottom: 1px solid transparent;
  position: relative;
}
.side-nav a::before {
  content: "";
  position: absolute;
  left: -1px;
  top: 6px;
  bottom: 6px;
  width: 2px;
  background: transparent;
  border-radius: 2px;
}
.side-nav a:hover {
  background: var(--accent-soft);
  color: var(--accent-ink);
  border-bottom-color: transparent;
}
.side-nav a:hover::before { background: var(--accent); }
.side-nav a:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.sidebar-counts {
  display: grid;
  gap: 4px;
  margin-top: 14px;
  padding-top: 14px;
  border-top: 1px solid var(--hairline);
}
.sidebar-counts div {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 10px;
  color: var(--muted);
  font-size: 11.5px;
  letter-spacing: .02em;
  padding: 2px 4px;
}
.sidebar-counts div span { text-transform: uppercase; letter-spacing: .1em; font-size: 10px; font-weight: 720; }
.sidebar-counts strong { color: var(--text); font-size: 14px; font-weight: 720; font-variant-numeric: var(--tnum); }
.metrics {
  display: grid;
  grid-template-columns: repeat(6, minmax(0, 1fr));
  gap: 0;
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  background: var(--panel);
  overflow: hidden;
  box-shadow: var(--shadow-soft);
}
.metric {
  padding: 16px 18px 18px;
  min-height: 88px;
  border-right: 1px solid var(--hairline);
  display: flex;
  flex-direction: column;
  gap: 8px;
  position: relative;
}
.metric:last-child { border-right: none; }
.metric::before {
  content: "";
  position: absolute;
  top: 16px;
  left: 0;
  width: 2px;
  height: 14px;
  background: transparent;
  border-radius: 2px;
}
.metric:first-child::before { background: var(--accent); }
.metric span {
  display: block;
  color: var(--muted);
  font-size: 10.5px;
  font-weight: 740;
  letter-spacing: .11em;
  text-transform: uppercase;
}
.metric strong {
  display: block;
  font-family: var(--display-stack);
  font-weight: 540;
  font-size: 30px;
  line-height: 1;
  letter-spacing: -0.018em;
  color: var(--text);
  font-variant-numeric: var(--tnum);
}
.panel {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  overflow: hidden;
  box-shadow: var(--shadow-soft);
}
.panel, .metrics { scroll-margin-top: 116px; }
.panel-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 14px 18px 12px;
  border-bottom: 1px solid var(--hairline);
  background: linear-gradient(180deg, var(--panel-raised), var(--panel));
}
.panel-head h2 { display: inline-flex; align-items: center; gap: 10px; }
.panel-head h2::before {
  content: "";
  width: 6px;
  height: 6px;
  border-radius: 999px;
  background: var(--accent);
  flex: none;
}
.panel-head .muted { font-variant-numeric: var(--tnum); }
.controls {
  display: grid;
  grid-template-columns: minmax(260px, 1.4fr) repeat(6, minmax(120px, .7fr));
  gap: 8px;
  padding: 12px 18px 14px;
  background: var(--panel-soft);
  border-bottom: 1px solid var(--hairline);
}
input, select {
  width: 100%;
  min-height: 34px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 6px 10px;
  background: var(--control);
  color: var(--text);
  font: inherit;
  font-size: 13px;
  transition: border-color 100ms ease, box-shadow 100ms ease;
}
input::placeholder { color: var(--muted); }
input:hover, select:hover { border-color: var(--line-strong); }
input:focus, select:focus {
  outline: none;
  border-color: var(--accent);
  box-shadow: 0 0 0 3px color-mix(in oklch, var(--accent) 18%, transparent);
}
.link-grid { display: flex; flex-wrap: wrap; gap: 6px; padding: 14px 18px; }
.link-grid a, .file-row a {
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 5px 10px;
  background: var(--control);
  font-size: 12.5px;
  font-weight: 600;
  font-family: var(--mono-stack);
  color: var(--text-soft);
  border-bottom: 1px solid var(--line);
}
.link-grid a:hover, .file-row a:hover {
  border-color: var(--accent);
  color: var(--accent-ink);
  background: color-mix(in oklch, var(--accent-soft) 55%, var(--control));
}
.activity-grid, .blocked-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  padding: 14px 18px 18px;
}
.activity-card, .blocked-card {
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  background: var(--panel-raised);
  padding: 16px 18px 14px;
  min-height: 268px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  box-shadow: var(--shadow-soft);
  position: relative;
  overflow: hidden;
}
.activity-card::before, .blocked-card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 3px;
  background: transparent;
  transition: background 100ms ease;
}
.activity-card::before { background: color-mix(in oklch, var(--accent) 60%, transparent); }
.blocked-card::before { background: oklch(70% 0.13 75); }
.clickable-card {
  cursor: pointer;
  transition: border-color 120ms ease, box-shadow 120ms ease, transform 120ms cubic-bezier(.2,.6,.2,1);
}
.clickable-card:hover {
  border-color: var(--accent-line);
  box-shadow: var(--shadow-hover);
  transform: translateY(-2px);
}
.clickable-card:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 3px;
}
.card-top { display: flex; justify-content: space-between; gap: 14px; align-items: flex-start; }
.card-top .eyebrow { color: var(--muted); }
.status-stack { display: flex; flex-direction: column; gap: 6px; align-items: flex-end; }
.activity-id {
  margin: 4px 0 0;
  color: var(--muted);
  font: 12px/1.4 var(--mono-stack);
  font-variant-numeric: var(--tnum);
}
.meta-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0;
  border: 1px solid var(--hairline);
  border-radius: var(--radius);
  overflow: hidden;
  background: var(--panel-soft);
}
.meta-grid.compact { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.meta-grid > div, .inline-fields > div {
  padding: 8px 10px;
  min-width: 0;
  border-right: 1px solid var(--hairline);
  border-bottom: 1px solid var(--hairline);
  background: var(--panel-soft);
}
.meta-grid > div:nth-child(3n), .meta-grid.compact > div:nth-child(2n), .inline-fields > div:nth-child(2n) { border-right: none; }
.meta-grid > div:nth-last-child(-n+3), .meta-grid.compact > div:nth-last-child(-n+2), .inline-fields > div:nth-last-child(-n+2) { border-bottom: none; }
.meta-grid span, .inline-fields span, .details-grid span {
  display: block;
  color: var(--muted);
  font-size: 10px;
  font-weight: 740;
  text-transform: uppercase;
  letter-spacing: .1em;
}
.meta-grid strong, .inline-fields strong {
  display: block;
  margin-top: 3px;
  overflow-wrap: anywhere;
  font-size: 13px;
  font-weight: 580;
  color: var(--text);
}
.inline-fields {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0;
  border: 1px solid var(--hairline);
  border-radius: var(--radius);
  overflow: hidden;
  background: var(--panel-soft);
}
.asset-metric-strip { grid-template-columns: repeat(3, minmax(0, 1fr)); margin: 10px 0 12px; }
.asset-metric-strip > div:nth-child(2n) { border-right: 1px solid var(--hairline); }
.asset-metric-strip > div:nth-child(3n) { border-right: none; }
.asset-metric-strip > div:nth-last-child(-n+3) { border-bottom: none; }
.asset-pilot-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px;
  padding: 14px 18px 18px;
}
.asset-pilot-card {
  min-width: 0;
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  background: var(--panel-raised);
  box-shadow: var(--shadow-soft);
  overflow: hidden;
  display: grid;
  grid-template-rows: auto 1fr;
}
.asset-pilot-figure {
  margin: 0;
  border-bottom: 1px solid var(--hairline);
  background: var(--panel-soft);
}
.asset-pilot-image-link {
  display: block;
  border: 0;
}
.asset-pilot-image-link:hover { border: 0; }
.asset-pilot-figure img {
  display: block;
  width: 100%;
  aspect-ratio: 1 / 1;
  object-fit: cover;
}
.asset-pilot-placeholder {
  display: grid;
  place-items: center;
  aspect-ratio: 1 / 1;
  min-height: 240px;
  padding: 20px;
  color: var(--muted);
  font-weight: 650;
  text-align: center;
}
.asset-pilot-copy {
  min-width: 0;
  padding: 15px 16px 14px;
  display: grid;
  gap: 10px;
}
.asset-pilot-fields { grid-template-columns: 1.15fr .85fr; }
.asset-pilot-fields > div:nth-child(2n) { border-right: none; }
.asset-pilot-fields > div:nth-last-child(-n+2) { border-bottom: none; }
.activity-export-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
  padding: 14px 18px 18px;
}
.activity-export-card {
  min-width: 0;
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  background: var(--panel-raised);
  box-shadow: var(--shadow-soft);
}
.activity-export-copy {
  min-width: 0;
  padding: 15px 16px 14px;
  display: grid;
  gap: 10px;
}
.activity-export-fields { grid-template-columns: 1fr; }
.activity-export-fields > div { border-right: none; }
.activity-export-fields > div:last-child { border-bottom: none; }
.asset-placement {
  display: grid;
  gap: 7px;
  color: var(--text-soft);
  font-size: 12.5px;
  line-height: 1.45;
}
.asset-placement p { margin: 0; }
.asset-placement span {
  display: block;
  margin-bottom: 2px;
  color: var(--muted);
  font-size: 10px;
  font-weight: 740;
  letter-spacing: .1em;
  text-transform: uppercase;
}
.storyboard-block {
  display: grid;
  grid-template-columns: minmax(280px, .92fr) minmax(0, 1fr);
  gap: 16px;
  align-items: start;
}
.storyboard-figure {
  margin: 0;
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  overflow: hidden;
  background: var(--panel-soft);
  box-shadow: var(--shadow-soft);
}
.storyboard-image-link {
  display: block;
  border: 0;
}
.storyboard-image-link:hover { border: 0; }
.storyboard-figure img {
  display: block;
  width: 100%;
  height: auto;
  aspect-ratio: 1 / 1;
  object-fit: cover;
}
.storyboard-placeholder {
  display: grid;
  place-items: center;
  min-height: 280px;
  padding: 20px;
  color: var(--muted);
  font-weight: 650;
  text-align: center;
}
.storyboard-detail-copy { min-width: 0; display: grid; gap: 12px; }
.storyboard-meta { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.storyboard-rule-note {
  margin: 0;
  padding: 10px 12px;
  border: 1px solid color-mix(in srgb, var(--accent) 18%, var(--hairline));
  border-radius: var(--radius);
  background: color-mix(in srgb, var(--accent-soft) 58%, white);
  color: var(--text-soft);
  font-size: 12.5px;
  line-height: 1.45;
}
.storyboard-caption-list {
  display: grid;
  gap: 0;
  padding: 0;
  margin: 0;
  list-style: none;
  border-top: 1px solid var(--hairline);
}
.storyboard-caption-row {
  display: grid;
  grid-template-columns: 34px minmax(0, 1fr);
  gap: 10px;
  padding: 10px 0;
  border-bottom: 1px solid var(--hairline);
}
.storyboard-panel-number {
  display: inline-grid;
  place-items: center;
  width: 28px;
  height: 24px;
  border-radius: var(--radius-sm);
  background: var(--accent-soft);
  color: var(--accent-ink);
  font: 11px/1 var(--mono-stack);
  font-variant-numeric: var(--tnum);
}
.storyboard-caption-row strong {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  align-items: center;
  color: var(--text);
  font-size: 13px;
  font-weight: 680;
}
.storyboard-caption-row code {
  padding: 2px 5px;
  border: 1px solid var(--hairline);
  border-radius: 5px;
  background: var(--panel-soft);
  color: var(--accent-ink);
  font: 10.5px/1.2 var(--mono-stack);
}
.storyboard-caption-row p {
  margin: 2px 0 0;
  color: var(--text-soft);
  font-size: 12.5px;
  line-height: 1.45;
}
.storyboard-source {
  display: block;
  margin-top: 3px;
  color: var(--muted);
  font: 10.5px/1.35 var(--mono-stack);
}
.summary-copy { margin: 0; color: var(--text-soft); max-width: 74ch; font-size: 13.5px; line-height: 1.5; }
details { border-top: 1px solid var(--hairline); padding-top: 10px; }
summary { cursor: pointer; font-weight: 700; color: var(--accent-ink); font-size: 12px; letter-spacing: .04em; text-transform: uppercase; }
.details-grid, .dialog-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px 18px;
  margin-top: 10px;
}
.details-grid section, .dialog-grid section { min-width: 0; }
.dialog-wide { grid-column: 1 / -1; }
.details-grid p, .dialog-grid p { margin: 0 0 8px; color: var(--text-soft); }
.details-grid section + section, .dialog-grid section + section { }
.dialog-grid section { padding-bottom: 4px; }
ol, ul { margin: 0; padding-left: 20px; }
.workflow-list {
  display: grid;
  gap: 0;
  padding: 0 18px 16px;
  list-style: none;
  counter-reset: workflow;
  border-top: 1px solid var(--hairline);
}
.workflow-list li {
  position: relative;
  counter-increment: workflow;
  padding: 14px 0 14px 38px;
  border-bottom: 1px solid var(--hairline);
  color: var(--text-soft);
}
.workflow-list li:last-child { border-bottom: none; }
.workflow-list li::before {
  content: counter(workflow, decimal-leading-zero);
  position: absolute;
  left: 0;
  top: 17px;
  font: 11px/1 var(--mono-stack);
  letter-spacing: .04em;
  color: var(--muted);
}
.workflow-list strong { display: block; margin-bottom: 5px; color: var(--text); font-size: 13px; }
.workflow-list span, .workflow-list code { display: block; font-size: 13px; line-height: 1.5; }
.workflow-list code {
  font-family: var(--mono-stack);
  color: var(--accent-ink);
  overflow-wrap: anywhere;
}
.runtime-map {
  display: grid;
  gap: 0;
  padding: 0;
  margin: 2px 0 14px;
  list-style: none;
  border-top: 1px solid var(--hairline);
}
.runtime-map-node {
  display: grid;
  grid-template-columns: 38px minmax(0, 1fr);
  gap: 12px;
  padding: 14px 0;
  border-bottom: 1px solid var(--hairline);
}
.runtime-step-marker {
  position: relative;
  display: grid;
  justify-items: center;
  align-content: start;
  min-height: 100%;
}
.runtime-step-marker::after {
  content: "";
  width: 1px;
  min-height: 100%;
  margin-top: 6px;
  background: var(--hairline);
}
.runtime-step-marker span {
  display: inline-grid;
  place-items: center;
  width: 30px;
  height: 24px;
  border-radius: var(--radius-sm);
  border: 1px solid color-mix(in oklch, var(--accent-line) 60%, var(--line));
  background: var(--panel-raised);
  color: var(--accent-ink);
  font: 11px/1 var(--mono-stack);
  font-variant-numeric: var(--tnum);
}
.runtime-step-body { min-width: 0; display: grid; gap: 9px; }
.runtime-map-head {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 10px;
}
.runtime-map-head strong {
  min-width: 0;
  color: var(--text);
  font-size: 13px;
  font-weight: 680;
}
.runtime-map-head span {
  flex: 0 0 auto;
  border-radius: var(--radius-sm);
  padding: 2px 7px;
  background: var(--neutral-tag-bg);
  color: var(--neutral-tag-text);
  font-size: 10px;
  font-weight: 760;
  letter-spacing: .1em;
  text-transform: uppercase;
}
.runtime-lanes {
  display: grid;
  grid-template-columns: minmax(220px, .85fr) minmax(0, 2.15fr);
  gap: 8px;
  align-items: start;
}
.runtime-lane,
.runtime-branches,
.screen-strip {
  min-width: 0;
  border: 1px solid var(--hairline);
  border-radius: var(--radius-sm);
  background: color-mix(in oklch, var(--panel-soft) 82%, var(--panel-raised));
  padding: 8px 10px;
}
.runtime-lane > span,
.runtime-branches > span,
.screen-strip > span {
  display: block;
  margin-bottom: 5px;
  color: var(--muted);
  font-size: 10px;
  font-weight: 760;
  letter-spacing: .11em;
  text-transform: uppercase;
}
.runtime-lane-followup { grid-column: 1 / -1; }
.runtime-lane p,
.screen-strip p {
  margin: 0;
  color: var(--text-soft);
  font-size: 12.5px;
  line-height: 1.45;
}
.branch-followup-table-wrap { overflow-x: auto; }
.branch-followup-table {
  width: 100%;
  min-width: 640px;
  border-collapse: separate;
  border-spacing: 0;
  table-layout: fixed;
  color: var(--text-soft);
}
.branch-followup-table th,
.branch-followup-table td {
  padding: 7px 8px;
  border-top: 1px solid color-mix(in oklch, var(--hairline) 72%, transparent);
  text-align: left;
  vertical-align: top;
}
.branch-followup-table th {
  color: var(--muted);
  font-size: 9.5px;
  font-weight: 780;
  letter-spacing: .11em;
  text-transform: uppercase;
}
.branch-followup-table th:first-child,
.branch-followup-table td:first-child { width: 126px; }
.branch-followup-table tbody tr:first-child td { border-top-color: var(--hairline); }
.branch-chip {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  padding: 2px 7px;
  font-size: 9.5px;
  font-weight: 780;
  letter-spacing: .08em;
  text-transform: uppercase;
}
.branch-chip-ideal { background: var(--green-bg); color: var(--green-text); }
.branch-chip-unexpected { background: var(--amber-bg); color: var(--amber-text); }
.branch-chip-no-response { background: var(--purple-bg); color: var(--purple-text); }
.branch-chip-observed { background: var(--accent-soft); color: var(--accent-ink); }
.branch-followup-table td {
  font-size: 12px;
  line-height: 1.42;
}
.branch-followup-ideal td { background: color-mix(in oklch, var(--green-bg) 72%, var(--panel-raised)); }
.branch-followup-unexpected td { background: color-mix(in oklch, var(--amber-bg) 72%, var(--panel-raised)); }
.branch-followup-no-response td { background: color-mix(in oklch, var(--purple-bg) 68%, var(--panel-raised)); }
.branch-followup-observed td { background: color-mix(in oklch, var(--accent-soft) 68%, var(--panel-raised)); }
.screen-strip {
  display: grid;
  grid-template-columns: 74px minmax(0, 1fr);
  gap: 10px;
  background: color-mix(in oklch, var(--teal-bg) 55%, var(--panel-raised));
}
.screen-strip > span { margin: 0; padding-top: 2px; color: var(--teal-text); }
.photo-timing-strip {
  display: grid;
  grid-template-columns: 118px minmax(0, 1fr);
  gap: 10px;
  min-width: 0;
  border: 1px solid color-mix(in oklch, var(--accent-line) 35%, var(--hairline));
  border-radius: var(--radius-sm);
  background: color-mix(in oklch, var(--accent-soft) 55%, var(--panel-raised));
  padding: 8px 10px;
}
.photo-timing-strip > span {
  margin: 0;
  padding-top: 2px;
  color: var(--accent-ink);
  font-size: 10px;
  font-weight: 760;
  letter-spacing: .11em;
  text-transform: uppercase;
}
.photo-timing-strip p {
  margin: 0;
  color: var(--text-soft);
  font-size: 12.5px;
  line-height: 1.45;
}
.runtime-source-label {
  margin: 2px 0 6px;
  color: var(--muted);
  font-size: 10px;
  font-weight: 760;
  letter-spacing: .12em;
  text-transform: uppercase;
}
.beat-list { display: grid; gap: 0; padding-left: 0; list-style: none; counter-reset: beat; border-top: 1px solid var(--hairline); }
.beat-list li {
  border-bottom: 1px solid var(--hairline);
  padding: 14px 0 14px 36px;
  position: relative;
  counter-increment: beat;
}
.beat-list li::before {
  content: counter(beat, decimal-leading-zero);
  position: absolute;
  top: 14px;
  left: 0;
  width: 28px;
  color: var(--muted);
  font: 11px/1 var(--mono-stack);
  letter-spacing: .04em;
}
.beat-list strong { display: block; margin-bottom: 8px; font-size: 13px; letter-spacing: -0.005em; color: var(--text); }
.beat-field {
  display: grid;
  grid-template-columns: 74px minmax(0, 1fr);
  gap: 10px;
  margin-top: 6px;
  font-size: 13px;
}
.beat-field > span {
  color: var(--muted);
  font-size: 10px;
  font-weight: 740;
  letter-spacing: .12em;
  text-transform: uppercase;
  padding-top: 3px;
}
.beat-field p { margin: 0; color: var(--text-soft); }
.blocked-design-status {
  border-left: 3px solid oklch(70% 0.13 75);
  border-radius: 0 var(--radius) var(--radius) 0;
  background: linear-gradient(90deg, oklch(97% 0.04 85), transparent 60%);
  padding: 10px 12px;
  color: var(--text-soft);
  font-size: 13px;
}
.badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 22px;
  padding: 1px 9px;
  border-radius: 999px;
  background: var(--panel-soft);
  border: 1px solid color-mix(in oklch, var(--line) 80%, transparent);
  color: var(--text);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: .02em;
  white-space: nowrap;
  margin: 0 4px 4px 0;
  font-variant-numeric: var(--tnum);
}
.tag-row, .reason-row { display: flex; flex-wrap: wrap; gap: 4px; }
.badge-kind { background: var(--neutral-tag-bg); color: var(--neutral-tag-text); border-color: transparent; }
.badge-kind-audited { background: var(--teal-bg); color: var(--teal-text); border-color: transparent; }
.badge-kind-enriched { background: var(--accent-soft); color: var(--accent-ink); border-color: transparent; }
.badge-category, .badge-category-cat1 { background: color-mix(in oklch, var(--accent-soft) 70%, var(--panel-soft)); color: var(--accent-ink); border-color: transparent; }
.badge-category-cat3 { background: var(--red-bg); color: var(--red-text); border-color: transparent; }
.badge-category-cat5 { background: var(--green-bg); color: var(--green-text); border-color: transparent; }
.badge-status, .badge-status-pass, .badge-status-enriched, .badge-status-pass-no-changes { background: var(--green-bg); color: var(--green-text); border-color: transparent; }
.badge-status-reviewable { background: var(--accent-soft); color: var(--accent-ink); border-color: transparent; }
.badge-status-n-a { background: var(--neutral-tag-bg); color: var(--neutral-tag-text); border-color: transparent; }
.badge-status-blocked, .badge-status-blocked-until-product-decision, .badge-blocked, .badge-reason { background: var(--amber-bg); color: var(--amber-text); border-color: transparent; }
.badge-status-fail, .badge-status-failed { background: var(--red-bg); color: var(--red-text); border-color: transparent; }
.badge-mechanic { background: var(--purple-bg); color: var(--purple-text); border-color: transparent; }
.badge-tier { background: color-mix(in oklch, var(--accent-soft) 60%, var(--panel-soft)); color: var(--accent-ink); border-color: transparent; }
.badge-asset, .badge-asset-no-assets, .badge-asset-optional-support { background: var(--teal-bg); color: var(--teal-text); border-color: transparent; }
.badge-asset-required-prebuilt, .badge-asset-runtime-generated, .badge-asset-blocked { background: var(--amber-bg); color: var(--amber-text); border-color: transparent; }
.badge-reviewer { background: var(--green-bg); color: var(--green-text); border-color: transparent; }
.badge-reviewer-unknown, .badge-reviewer-n-a { background: var(--amber-bg); color: var(--amber-text); border-color: transparent; }
.badge-metadata { background: var(--neutral-tag-bg); color: var(--neutral-tag-text); border-color: transparent; font-family: var(--mono-stack); font-size: 10.5px; padding: 1px 7px; }
.badge-reason-runtime-image-generation { background: oklch(95% 0.05 306); color: oklch(38% 0.13 306); border-color: transparent; }
.badge-reason-coloring-or-recoloring-ui { background: oklch(95% 0.052 338); color: oklch(39% 0.14 338); border-color: transparent; }
.badge-reason-cat3-material-workflow { background: oklch(96% 0.055 75); color: oklch(40% 0.105 75); border-color: transparent; }
.badge-reason-ui-state-or-progress-memory { background: oklch(95% 0.04 248); color: oklch(37% 0.13 248); border-color: transparent; }
.badge-reason-prebuilt-asset-display { background: oklch(95% 0.04 185); color: oklch(34% 0.1 185); border-color: transparent; }
.badge-reason-motion-safety { background: oklch(94% 0.052 28); color: oklch(40% 0.14 28); border-color: transparent; }
.badge-reason-before-after-evidence { background: oklch(95.5% 0.06 98); color: oklch(38% 0.105 98); border-color: transparent; }
.badge-reason-ocr-or-text-handling { background: oklch(95% 0.045 282); color: oklch(38% 0.13 282); border-color: transparent; }
.badge-reason-caregiver-setup-and-pacing { background: oklch(94.5% 0.025 230); color: oklch(36% 0.06 230); border-color: transparent; }
.badge-reason-product-decision-needed { background: oklch(95% 0.03 65); color: oklch(38% 0.095 65); border-color: transparent; }
.blocked-element-chip { margin-bottom: 0; }
.blocked-marker-summary { display: flex; flex-wrap: wrap; gap: 4px; margin: 4px 0 10px; }
.blocked-marker-list, .resolved-blocker-list { display: grid; gap: 0; padding-left: 0; list-style: none; border-top: 1px solid var(--hairline); }
.minimum-unblock-list { display: grid; gap: 0; padding-left: 0; list-style: none; margin: 8px 0 0; border-top: 1px solid var(--hairline); }
.minimum-unblock-row,
.blocked-marker-row,
.resolved-blocker-row {
  display: grid;
  grid-template-columns: max-content minmax(0, 1fr);
  gap: 10px;
  align-items: start;
  padding: 9px 4px;
  border-bottom: 1px solid var(--hairline);
}
.minimum-unblock-row p { margin: 0; color: var(--text-soft); }
.resolved-blocker-chip { box-shadow: inset 0 0 0 1px color-mix(in oklch, var(--green-text) 24%, transparent); }
.extensibility-block ul { margin-top: 8px; }
.extensibility-block p span { display: inline-block; margin-right: 8px; color: var(--muted); font-size: 10px; font-weight: 740; letter-spacing: .1em; text-transform: uppercase; }
.detail-button, .dialog-close {
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 6px 12px;
  background: var(--panel-raised);
  color: var(--text);
  font: inherit;
  font-weight: 640;
  font-size: 12px;
  letter-spacing: .02em;
  cursor: pointer;
  transition: all 100ms ease;
}
.detail-button { box-shadow: 0 1px 0 oklch(100% 0 0 / 0.7); }
.detail-button:hover, .dialog-close:hover {
  border-color: var(--accent);
  color: var(--accent-ink);
  background: var(--accent-soft);
}
.detail-button:focus-visible, .dialog-close:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
.file-row {
  display: flex;
  justify-content: space-between;
  gap: 10px;
  align-items: flex-end;
  margin-top: auto;
  border-top: 1px solid var(--hairline);
  padding-top: 12px;
}
.inline-file-row { margin-top: 0; }
.changed-files { text-align: right; color: var(--muted); font-size: 11.5px; font-family: var(--mono-stack); }
.missing { color: var(--red-text); background: var(--red-bg); border-radius: var(--radius-sm); padding: 2px 6px; }
.muted { color: var(--muted); }
.hidden { display: none; }
.table-wrap { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; min-width: 840px; font-variant-numeric: var(--tnum); }
th, td { padding: 12px 16px; border-bottom: 1px solid var(--hairline); text-align: left; vertical-align: top; }
th {
  color: var(--muted);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: .14em;
  font-weight: 720;
  background: var(--panel-soft);
  border-bottom-color: var(--line);
}
tbody tr:hover td { background: color-mix(in oklch, var(--panel-soft) 60%, var(--panel-raised)); }
tbody tr:last-child td { border-bottom: none; }
.criteria-note {
  padding: 14px 18px;
  border-bottom: 1px solid var(--hairline);
  color: var(--text-soft);
  font-size: 13.5px;
  line-height: 1.55;
  max-width: 86ch;
}
.scorecard-wrap table { min-width: 760px; }
.asset-usage-table { min-width: 1320px; }
.asset-usage-table td:first-child strong { display: block; font-family: var(--mono-stack); font-size: 11px; color: var(--text); }
.scorecard-table td:first-child, .criteria-table td:first-child {
  width: 38px;
  color: var(--muted);
  font: 600 11px/1 var(--mono-stack);
  letter-spacing: .04em;
  padding-top: 14px;
}
.criteria-table strong { font-weight: 640; color: var(--text); letter-spacing: -0.005em; }
pre {
  margin: 0;
  white-space: pre-wrap;
  word-break: break-word;
  font: 12.5px/1.55 var(--mono-stack);
  color: var(--text-soft);
}
.reviewers { display: grid; grid-template-columns: 1fr; gap: 0; padding: 0 18px 14px; }
.reviewer-card {
  border: none;
  border-top: 1px solid var(--hairline);
  border-radius: 0;
  background: transparent;
  padding: 14px 0;
}
.reviewer-card:first-child { border-top: none; padding-top: 14px; }
.note-body { padding: 14px 18px; color: var(--text-soft); }
.note-body h4 { margin-top: 8px; }
.note-body h4:first-child { margin-top: 0; }
.detail-dialog {
  width: min(1080px, calc(100vw - 32px));
  max-height: min(860px, calc(100vh - 32px));
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 0;
  background: var(--panel-raised);
  color: var(--text);
  box-shadow: 0 24px 80px oklch(20% 0.06 264 / 0.22);
  overflow: hidden;
}
.detail-dialog::backdrop {
  background: oklch(22% 0.06 264 / 0.32);
  backdrop-filter: blur(4px);
}
.dialog-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  padding: 16px 20px 14px;
  border-bottom: 1px solid var(--hairline);
  background: linear-gradient(180deg, var(--panel-raised), var(--panel));
}
.dialog-head h2 {
  font-family: var(--display-stack);
  font-size: 19px;
  font-weight: 540;
  letter-spacing: -0.012em;
  text-transform: none;
  color: var(--text);
}
.dialog-head h2::before { display: none; }
.dialog-body {
  padding: 18px 20px 20px;
  overflow: auto;
  max-height: calc(min(860px, calc(100vh - 32px)) - 64px);
}
::selection { background: color-mix(in oklch, var(--accent) 25%, transparent); color: var(--text); }
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
  html { scroll-behavior: auto; }
}
a[data-preview-id] {
  border-bottom-style: dashed;
  border-bottom-color: color-mix(in oklch, var(--accent) 40%, transparent);
}
a[data-preview-id]:hover { border-bottom-style: solid; border-bottom-color: var(--accent); }
.link-grid a[data-preview-id], .file-row a[data-preview-id] { border-bottom: 1px solid var(--line); }
.link-grid a[data-preview-id]:hover, .file-row a[data-preview-id]:hover { border-color: var(--accent); }
.preview-dialog {
  width: min(1120px, calc(100vw - 32px));
  max-height: min(880px, calc(100vh - 32px));
}
.preview-head {
  align-items: flex-start;
  padding: 14px 20px 12px;
}
.preview-head-meta { min-width: 0; display: grid; gap: 4px; }
.preview-head h2 {
  font-family: var(--mono-stack);
  font-size: 15px;
  font-weight: 600;
  letter-spacing: -0.005em;
  color: var(--text);
  text-transform: none;
  word-break: break-all;
  line-height: 1.3;
}
.preview-head h2::before { display: none; }
.preview-subline {
  display: flex;
  flex-wrap: wrap;
  gap: 8px 14px;
  align-items: center;
  margin-top: 2px;
  font-size: 11.5px;
}
.preview-subline .badge { margin: 0; }
.preview-size { font-family: var(--mono-stack); font-size: 11px; font-variant-numeric: var(--tnum); }
.preview-open {
  color: var(--accent-ink);
  border-bottom: 1px dashed color-mix(in oklch, var(--accent) 35%, transparent);
  font-weight: 600;
  font-size: 11.5px;
}
.preview-open:hover { border-bottom-style: solid; border-bottom-color: var(--accent); }
.preview-truncated {
  padding: 10px 20px;
  border-top: 1px solid var(--hairline);
  background: var(--panel-soft);
  font-size: 12px;
}
.preview-body {
  padding: 22px 26px 26px;
  color: var(--text-soft);
  font-size: 14px;
  line-height: 1.62;
  max-width: none;
  max-height: calc(min(880px, calc(100vh - 32px)) - 96px);
}
.preview-body.kind-markdown { max-width: 78ch; margin: 0 auto; }
.preview-body h1, .preview-body h2, .preview-body h3, .preview-body h4, .preview-body h5, .preview-body h6 {
  font-family: var(--display-stack);
  font-weight: 560;
  color: var(--text);
  margin: 1.5em 0 .5em;
  letter-spacing: -0.012em;
  text-transform: none;
  line-height: 1.2;
}
.preview-body h1:first-child, .preview-body h2:first-child, .preview-body h3:first-child { margin-top: 0; }
.preview-body h1 { font-size: 26px; }
.preview-body h2 { font-size: 21px; }
.preview-body h2::before { display: none; }
.preview-body h3 { font-size: 17px; }
.preview-body h4 { font-size: 14px; font-family: var(--sans-stack); font-weight: 680; letter-spacing: .04em; text-transform: uppercase; color: var(--muted); margin-top: 1.6em; }
.preview-body h5, .preview-body h6 { font-size: 13px; font-family: var(--sans-stack); font-weight: 700; }
.preview-body p { margin: 0 0 1em; }
.preview-body ul, .preview-body ol { margin: 0 0 1em; padding-left: 1.4em; }
.preview-body li { margin-bottom: .35em; }
.preview-body li > ul, .preview-body li > ol { margin-top: .25em; margin-bottom: .25em; }
.preview-body blockquote {
  margin: 0 0 1em;
  padding: .4em 1em;
  border-left: 3px solid var(--accent-line);
  background: color-mix(in oklch, var(--accent-soft) 50%, var(--panel));
  color: var(--text-soft);
  border-radius: 0 var(--radius) var(--radius) 0;
}
.preview-body blockquote p:last-child { margin-bottom: 0; }
.preview-body hr {
  border: none;
  border-top: 1px solid var(--hairline);
  margin: 1.6em 0;
}
.preview-body code {
  font-family: var(--mono-stack);
  font-size: 12.5px;
  background: var(--panel-soft);
  border: 1px solid var(--hairline);
  padding: 1px 5px;
  border-radius: var(--radius-sm);
  color: var(--accent-ink);
}
.preview-body pre {
  background: var(--panel-soft);
  border: 1px solid var(--hairline);
  border-radius: var(--radius);
  padding: 12px 14px;
  overflow: auto;
  font-size: 12.5px;
  line-height: 1.55;
  color: var(--text);
  margin: 0 0 1em;
}
.preview-body pre code { background: none; border: none; padding: 0; color: inherit; border-radius: 0; }
.preview-body a { color: var(--accent-ink); border-bottom: 1px solid color-mix(in oklch, var(--accent) 35%, transparent); }
.preview-body a:hover { color: var(--accent); border-bottom-color: var(--accent); }
.preview-body strong { color: var(--text); font-weight: 660; }
.preview-body em { font-style: italic; color: var(--text-soft); }
.preview-body table { min-width: 0; border: 1px solid var(--hairline); border-radius: var(--radius); margin: 0 0 1em; }
.preview-body th, .preview-body td { padding: 8px 12px; }
.preview-body.kind-yaml, .preview-body.kind-text {
  padding: 0;
  max-width: none;
}
.preview-body.kind-yaml pre, .preview-body.kind-text pre {
  margin: 0;
  border: none;
  border-radius: 0;
  background: var(--panel-raised);
  padding: 22px 26px;
  font-size: 12.5px;
  line-height: 1.55;
  max-height: calc(min(880px, calc(100vh - 32px)) - 96px);
}
@media (max-width: 1120px) {
  header { position: static; }
  .header-inner { grid-template-columns: 1fr; }
  .review-layout { grid-template-columns: 1fr; }
  .review-content { grid-column: auto; }
  .sidebar {
    position: static;
    width: auto;
    max-height: none;
    box-shadow: var(--shadow-soft);
  }
  .side-nav { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .sidebar-counts { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .sidebar-counts div { display: block; padding: 6px 4px; }
  .metrics { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .metric { border-right: 1px solid var(--hairline); border-bottom: 1px solid var(--hairline); }
  .metric:nth-child(3n) { border-right: none; }
  .metric:nth-last-child(-n+3) { border-bottom: none; }
  .controls { grid-template-columns: 1fr 1fr 1fr; }
  .activity-grid, .blocked-grid, .asset-pilot-grid, .activity-export-grid { grid-template-columns: 1fr; }
}
@media (max-width: 700px) {
  main, .header-inner { padding-left: 16px; padding-right: 16px; }
  h1 { font-size: 26px; }
  .metrics { grid-template-columns: 1fr 1fr; }
  .metric { border-right: 1px solid var(--hairline) !important; border-bottom: 1px solid var(--hairline); }
  .metric:nth-child(2n) { border-right: none !important; }
  .metric:nth-last-child(-n+2) { border-bottom: none; }
  .side-nav, .sidebar-counts, .controls, .meta-grid, .meta-grid.compact, .inline-fields, .details-grid, .dialog-grid, .storyboard-block { grid-template-columns: 1fr; }
  .runtime-map-node, .runtime-lanes, .photo-timing-strip, .screen-strip { grid-template-columns: 1fr; }
  .runtime-step-marker {
    display: flex;
    justify-content: flex-start;
    min-height: 0;
  }
  .runtime-step-marker::after { display: none; }
  .minimum-unblock-row, .blocked-marker-row, .resolved-blocker-row { grid-template-columns: 1fr; }
  .meta-grid > div, .meta-grid.compact > div, .inline-fields > div { border-right: none !important; }
  .dialog-wide { grid-column: auto; }
  .file-row { display: block; }
  .detail-button { margin-top: 8px; }
  .changed-files { text-align: left; margin-top: 8px; }
}
"""
    js = r"""
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

// ----- In-file preview ------------------------------------------------------
const previewDialog = document.getElementById("preview-dialog");
const previewTitle = document.getElementById("preview-title");
const previewBody = document.getElementById("preview-body");
const previewKind = document.getElementById("preview-kind");
const previewSize = document.getElementById("preview-size");
const previewOpen = document.getElementById("preview-open");
const previewClose = document.getElementById("preview-close");
const previewTruncated = document.getElementById("preview-truncated");
let previewLastTrigger = null;

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}
function formatBytes(n) {
  n = Number(n) || 0;
  if (n < 1024) return n + " B";
  if (n < 1024 * 1024) return (n / 1024).toFixed(1) + " KB";
  return (n / 1024 / 1024).toFixed(2) + " MB";
}

// Minimal, dependency-free Markdown renderer. Supports headings, paragraphs,
// bullet / ordered lists, fenced & indented code, blockquotes, horizontal rules,
// inline code, bold, italic, and links. Anything richer is left as text.
function renderMarkdown(src) {
  const lines = src.replace(/\r\n?/g, "\n").split("\n");
  let out = "";
  let inFence = false;
  let fenceBuf = [];
  let listStack = []; // entries: { type, indent }
  let paraBuf = [];
  let quoteBuf = [];

  function inline(s) {
    s = escapeHtml(s);
    s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
    s = s.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
    s = s.replace(/\b_([^_]+)_\b/g, "<em>$1</em>");
    s = s.replace(/(^|[^*])\*([^*][^*]*?)\*(?!\*)/g, "$1<em>$2</em>");
    s = s.replace(/\[([^\]]+)\]\(([^)\s]+)(?:\s+&quot;[^&]*&quot;)?\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    return s;
  }
  function closeListsTo(indent) {
    while (listStack.length && listStack[listStack.length - 1].indent >= indent) {
      out += "</" + listStack.pop().type + ">";
    }
  }
  function flushPara() {
    if (paraBuf.length) {
      out += "<p>" + inline(paraBuf.join(" ")) + "</p>";
      paraBuf = [];
    }
  }
  function flushQuote() {
    if (quoteBuf.length) {
      out += "<blockquote>" + inline(quoteBuf.join(" ")) + "</blockquote>";
      quoteBuf = [];
    }
  }
  function closeBlocks() {
    flushPara();
    flushQuote();
    closeListsTo(-1);
  }

  for (const raw of lines) {
    if (raw.startsWith("```") || raw.startsWith("~~~")) {
      if (inFence) {
        out += "<pre><code>" + escapeHtml(fenceBuf.join("\n")) + "</code></pre>";
        fenceBuf = [];
        inFence = false;
      } else {
        closeBlocks();
        inFence = true;
      }
      continue;
    }
    if (inFence) { fenceBuf.push(raw); continue; }

    if (!raw.trim()) { closeBlocks(); continue; }

    const heading = raw.match(/^(#{1,6})\s+(.*)$/);
    if (heading) {
      closeBlocks();
      const lvl = heading[1].length;
      out += `<h${lvl}>${inline(heading[2].trim())}</h${lvl}>`;
      continue;
    }
    if (/^\s*([-*_])\s*\1\s*\1[\s\1]*$/.test(raw)) {
      closeBlocks();
      out += "<hr>";
      continue;
    }
    const quote = raw.match(/^>\s?(.*)$/);
    if (quote) {
      flushPara();
      closeListsTo(-1);
      quoteBuf.push(quote[1]);
      continue;
    }
    flushQuote();
    const bullet = raw.match(/^(\s*)[-*]\s+(.*)$/);
    const ordered = raw.match(/^(\s*)\d+\.\s+(.*)$/);
    if (bullet || ordered) {
      flushPara();
      const m = bullet || ordered;
      const indent = m[1].length;
      const type = bullet ? "ul" : "ol";
      closeListsTo(indent);
      if (!listStack.length || listStack[listStack.length - 1].indent < indent) {
        out += "<" + type + ">";
        listStack.push({ type, indent });
      } else if (listStack[listStack.length - 1].type !== type) {
        out += "</" + listStack.pop().type + "><" + type + ">";
        listStack.push({ type, indent });
      }
      out += "<li>" + inline(m[2]) + "</li>";
      continue;
    }
    if (listStack.length && /^\s{2,}/.test(raw)) {
      out = out.replace(/<\/li>$/, " " + inline(raw.trim()) + "</li>");
      continue;
    }
    closeListsTo(-1);
    paraBuf.push(raw);
  }
  closeBlocks();
  if (inFence) out += "<pre><code>" + escapeHtml(fenceBuf.join("\n")) + "</code></pre>";
  return out;
}

function openPreview(trigger) {
  if (!previewDialog) return false;
  const id = trigger.dataset && trigger.dataset.previewId;
  if (!id) return false;
  const tpl = document.getElementById(id);
  if (!tpl) return false;
  const meta = tpl.dataset;
  const kind = meta.kind || "Text";
  const label = meta.label || trigger.textContent.trim() || "File";
  const truncated = meta.truncated === "true";
  const raw = (tpl.content && tpl.content.textContent) || tpl.textContent || "";
  previewLastTrigger = trigger;
  previewTitle.textContent = label;
  previewKind.textContent = kind;
  previewSize.textContent = meta.size ? formatBytes(meta.size) : "";
  previewOpen.href = trigger.getAttribute("href");
  previewBody.className = "dialog-body preview-body kind-" + kind.toLowerCase();
  if (truncated || !raw) {
    previewBody.innerHTML = '<p class="muted">Preview not embedded for this file.</p>';
    previewTruncated.classList.toggle("hidden", !truncated);
  } else if (kind === "Markdown") {
    previewBody.innerHTML = renderMarkdown(raw);
    previewTruncated.classList.add("hidden");
  } else {
    previewBody.innerHTML = "<pre><code>" + escapeHtml(raw) + "</code></pre>";
    previewTruncated.classList.add("hidden");
  }
  previewDialog.showModal();
  previewBody.scrollTop = 0;
  return true;
}

if (previewDialog) {
  document.addEventListener("click", event => {
    if (event.defaultPrevented) return;
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button === 1) return;
    const trigger = event.target.closest("a[data-preview-id]");
    if (!trigger) return;
    if (openPreview(trigger)) event.preventDefault();
  });
  if (previewClose) previewClose.addEventListener("click", () => previewDialog.close());
  previewDialog.addEventListener("click", event => {
    if (event.target === previewDialog) previewDialog.close();
  });
  previewDialog.addEventListener("close", () => {
    previewBody.innerHTML = "";
    previewTruncated.classList.add("hidden");
    if (previewLastTrigger) previewLastTrigger.focus();
  });
}
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
    sidebar_links = [
        ("summary-metrics", "Summary"),
        ("run-files", "Run Files"),
        ("dashboard-workflow", "Workflow"),
        ("review-criteria", "Review Criteria"),
        ("activity-details", "Activities"),
        ("blocked-assignments", "Blocked"),
        ("reviewer-coverage", "Reviewers"),
        ("validation-checks", "Validation"),
        ("residual-risk", "Residual Risk"),
    ]
    if reason_guide_html:
        sidebar_links.insert(3, ("blocking-reason-guide", "Blocking Reasons"))
    if resolved_contract_html:
        sidebar_links.insert(3, ("resolved-contract-items", "Resolved Items"))
    if extensibility_html:
        sidebar_links.insert(4, ("extensibility-overview", "Extensibility"))
    if asset_pilot_html:
        sidebar_links.insert(5, ("generated-assets", "Generated Assets"))
    if runtime_asset_html:
        sidebar_links.insert(5, ("runtime-assets", "Runtime Assets"))
    if activity_export_html:
        sidebar_links.insert(6, ("activity-html-exports", "HTML Exports"))
    sidebar_link_html = "\n".join(f'      <a href="#{anchor}">{label}</a>' for anchor, label in sidebar_links)
    sidebar_stats = [
        ("Review cards", len(packages)),
        ("Blocked", len(blocked)),
        ("Runtime assets", len(runtime_asset_entries)),
        ("Asset sheets", len(asset_pilot_entries)),
        ("Failed", summary.get("failed_count", 0)),
        ("Checks", len(manifest_checks) if isinstance(manifest_checks, list) else 0),
    ]
    sidebar_stat_html = "".join(
        f"<div><span>{esc(label)}</span><strong>{esc(value)}</strong></div>"
        for label, value in sidebar_stats
    )
    sidebar_html = f"""  <aside class="sidebar" aria-label="Review navigation">
    <div class="sidebar-title">Review Navigation</div>
    <nav class="side-nav">
{sidebar_link_html}
    </nav>
    <div class="sidebar-counts">{sidebar_stat_html}</div>
  </aside>"""
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
    <div class="header-main">
      <div class="header-rule"></div>
      <div class="eyebrow">WonderLens · Activity Run Review</div>
      <h1>{esc(run_id)}</h1>
      <div class="summary-line">
        <span class="status-strong"><span class="status-dot {_status_dot_class(manifest.get('status', ''))}"></span>Status <strong>{esc(manifest.get('status', 'unknown'))}</strong></span>
        <span>Started <strong>{esc(manifest.get('started_at', 'unknown'))}</strong></span>
        <span>Completed <strong>{esc(manifest.get('completed_at', 'unknown'))}</strong></span>
      </div>
    </div>
    <div class="header-stamp">Run ID <strong>{esc(run_id)}</strong></div>
  </div>
	</header>
	<main>
	  <div class="review-layout">
	{sidebar_html}
	  <div class="review-content">
	  <section class="metrics" id="summary-metrics">{metric_html}</section>

	  <section class="panel" id="run-files">
	    <div class="panel-head"><h2>Run Files</h2></div>
	    <div class="link-grid">{run_link_html}</div>
	  </section>

	{dashboard_workflow(run_id)}

	{criteria_guide_html}

	{reason_guide_html}

	{resolved_contract_html}

	{extensibility_html}

	{asset_pilot_html}

	{runtime_asset_html}

	{activity_export_html}

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

	  <section class="panel" id="reviewer-coverage">
	    <div class="panel-head"><h2>Reviewer Coverage</h2></div>
	    <div class="reviewers">{reviewer_summary(review_notes)}</div>
	  </section>

	  <section class="panel" id="validation-checks">
	    <div class="panel-head"><h2>Validation Checks</h2></div>
	    <div class="table-wrap"><table><thead><tr><th>Command</th><th>Result</th></tr></thead><tbody>{checks}</tbody></table></div>
	  </section>

	  <section class="panel" id="residual-risk">
	    <div class="panel-head"><h2>Residual Risk And Next Actions</h2></div>
	    <div class="note-body">{residual_summary(review_notes)}</div>
	  </section>
	  </div>
	  </div>
	</main>
<dialog class="detail-dialog" id="detail-dialog" aria-labelledby="detail-title">
  <div class="dialog-head">
    <h2 id="detail-title">Activity details</h2>
    <button class="dialog-close" id="detail-close" type="button">Close</button>
  </div>
  <div class="dialog-body" id="detail-body"></div>
</dialog>
<dialog class="detail-dialog preview-dialog" id="preview-dialog" aria-labelledby="preview-title">
  <div class="dialog-head preview-head">
    <div class="preview-head-meta">
      <div class="eyebrow eyebrow-muted">File preview</div>
      <h2 id="preview-title">File</h2>
      <div class="preview-subline">
        <span class="badge badge-metadata" id="preview-kind">Text</span>
        <span class="preview-size muted" id="preview-size"></span>
        <a class="preview-open" id="preview-open" href="#" target="_blank" rel="noopener">Open file in new tab</a>
      </div>
    </div>
    <button class="dialog-close" id="preview-close" type="button">Close</button>
  </div>
  <div class="dialog-body preview-body" id="preview-body"></div>
  <div class="preview-truncated muted hidden" id="preview-truncated">File is larger than the inline-preview limit. Use "Open file in new tab" to read the full contents.</div>
</dialog>
{preview_templates_html()}
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
    has_resolved_blockers = any(
        entry.get("resolved_blockers") for entry in outputs.get("generated_activities", [])
    )
    product_contract_override = ""
    if isinstance(manifest.get("source"), dict):
        product_contract_override = normalize_text(manifest["source"].get("product_contract_override")).lower()
    full_pass_pipeline = bool(
        isinstance(manifest.get("source"), dict)
        and manifest["source"].get("full_pass_pipeline") is True
    )
    full_pass_asset_bundle_issues: list[dict[str, Any]] = []
    if full_pass_pipeline:
        try:
            import validate_full_pass_asset_bundle as asset_bundle
        except ImportError:
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            import validate_full_pass_asset_bundle as asset_bundle  # type: ignore

        full_pass_asset_bundle_issues = asset_bundle.validate_run(run_dir)
    product_capability_gaps = (
        unresolved_product_capability_entries(outputs.get("generated_activities", []))
        if product_contract_override == "minimum_unblock_allowed"
        else []
    )
    has_extensibility = any(
        entry.get("extensibility_notes") or entry.get("extensibility_summary")
        for entry in outputs.get("generated_activities", [])
    )
    package_entries = (
        outputs.get("generated_activities", [])
        + outputs.get("enriched_activities", [])
        + outputs.get("audited_activities", [])
    )
    active_storyboard_root = active_storyboard_root_name(run_dir)
    storyboard_root = run_dir / active_storyboard_root if active_storyboard_root else Path()
    expected_storyboard_images = [
        storyboard_root / normalize_text(entry.get("activity_id")) / "mechanism_grid.png"
        for entry in package_entries
        if active_storyboard_root and normalize_text(entry.get("activity_id"))
    ]
    storyboard_meta_files = [
        storyboard_root / normalize_text(entry.get("activity_id")) / "mechanism_grid.meta.yaml"
        for entry in package_entries
        if active_storyboard_root and normalize_text(entry.get("activity_id"))
    ]
    storyboard_requires_images = bool(expected_storyboard_images) and any(path.exists() for path in expected_storyboard_images)
    asset_pilot_entries = prebuilt_asset_pilot_entries(run_dir)
    runtime_asset_entries = runtime_asset_output_entries(run_dir)
    requested_runtime_mode = requested_runtime_asset_mode(manifest)
    runtime_asset_manifest = load_yaml(run_dir / "generated_assets" / "asset_outputs.yaml")
    actual_runtime_mode = normalize_text(runtime_asset_manifest.get("asset_build_mode") or requested_runtime_mode)
    export_manifest = load_yaml(run_dir / "activity_exports" / "export_manifest.yaml")
    export_entries = export_manifest.get("entries", []) if isinstance(export_manifest.get("entries"), list) else []
    expected_asset_images = [
        run_dir / normalize_text(entry.get("image_href"))
        for entry in asset_pilot_entries
        if normalize_text(entry.get("image_href"))
    ]
    expected_runtime_asset_images = [
        run_dir / normalize_text(variant.get("href"))
        for entry in runtime_asset_entries
        for variant in entry.get("variants", [])
        if isinstance(variant, dict) and normalize_text(variant.get("href"))
    ]
    reviewer_map = reviewer_by_activity(read_text(run_dir / "review_notes.md"))
    package_ids = {normalize_text(entry.get("activity_id")) for entry in package_entries}
    expected_reviewer_pairs = {
        activity_id: reviewer
        for activity_id, reviewer in reviewer_map.items()
        if activity_id in package_ids
    }
    expected_reason_labels = {
        label
        for entry in package_entries
        for label in compact_list(entry.get("resolved_blocker_types"), limit=20)
    }
    expected_reason_labels.update(
        label
        for entry in package_entries
        for blocker in compact_list(entry.get("resolved_blockers"), limit=20)
        for label in classify_reason_text_labels(blocker)
    )
    scorecard_sets = [
        scorecard_rows(read_text(repo_root / normalize_text(entry.get("activity_path")) / "spec.md"))
        for entry in package_entries
    ]
    runtime_sets = [
        runtime_beats(read_text(repo_root / normalize_text(entry.get("activity_path")) / "prod.md"))
        for entry in package_entries
    ]
    generic_policy_findings = [
        finding
        for beats in runtime_sets
        for finding in generic_branch_policy_findings(beats)
    ]
    runtime_quality_findings = [
        finding
        for beats in runtime_sets
        for finding in runtime_contract_quality_findings(beats)
    ]
    dialogue_qa_findings = (
        consumer_dialogue_qa_findings(run_dir)
        if full_pass_pipeline and bool(outputs.get("generated_activities", []))
        else []
    )
    expected_branch_followups = sum(
        len(beat.get("branches", []))
        for beats in runtime_sets
        for beat in beats
    )
    expected_photo_timing = sum(
        1
        for beats in runtime_sets
        for beat in beats
        if normalize_text(beat.get("photo_timing"))
    )
    asset_usage_sets = [
        asset_usage_from_spec(read_text(repo_root / normalize_text(entry.get("activity_path")) / "spec.md"))
        for entry in package_entries
    ]
    criteria_pos = text.find('id="review-criteria"')
    reason_pos = text.find('id="blocking-reason-guide"')
    activity_pos = text.find('id="activity-details"')
    checks = {
        "has_html": "<html" in text,
        "has_style": "<style>" in text,
        "has_script": "<script>" in text,
        "has_run_id": normalize_text(manifest.get("run_id")) in text,
        "activity_card_count": text.count('class="activity-card') == expected_packages,
        "blocked_card_count": text.count('class="blocked-card') == expected_blocked,
        "category_filter": 'id="package-category-filter"' in text and "cat1" in text and "cat5" in text,
        "sort_controls": 'id="package-sort"' in text and "Sort by mechanic" in text,
        "sidebar_navigation": 'class="sidebar"' in text
        and "Review Navigation" in text
        and 'href="#dashboard-workflow"' in text
        and 'href="#review-criteria"' in text
        and 'href="#activity-details"' in text,
        "sidebar_fixed_desktop": "position: fixed" in text
        and "bottom: 24px" in text
        and ".review-content { grid-column: 2" in text,
        "reason_guide_position": expected_blocked == 0
        or (0 <= criteria_pos < reason_pos < activity_pos),
        "blocked_reason_types": text.count("blocked-reason-type") >= expected_blocked,
        "detailed_runtime_beats": "beat-field" in text and "AI" in text and "Child" in text and "Screen" in text,
        "visual_runtime_beat_maps": expected_packages == 0
        or (
            text.count('class="runtime-map"') >= expected_packages
            and "runtime-map-node" in text
            and "runtime-lane-ai" in text
            and "branch-followup-table" in text
            and "branch-followup-ideal" in text
            and "branch-followup-unexpected" in text
            and "branch-followup-no-response" in text
            and "screen-strip" in text
        ),
        "branch_followups_all_paths": expected_branch_followups == 0
        or (
            text.count('<tr class="branch-followup-') >= expected_branch_followups
            and 'class="branch-followup-table"' in text
            and "<th>Branch</th>" in text
            and "<th>Child behavior</th>" in text
            and "<th>AI follow-up</th>" in text
            and (
                "Child branches and AI follow-ups" in text
                or "Child branches and AI follow-up policy" in text
            )
        ),
        "branch_policy_specificity": not generic_policy_findings,
        "runtime_contract_quality": not runtime_quality_findings,
        "consumer_dialogue_qa": not dialogue_qa_findings,
        "photo_capture_timing": expected_photo_timing == 0
        or (
            text.count('class="photo-timing-strip"') >= expected_photo_timing
            and "Photo timing" in text
            and "Photo capture timing" in text
        ),
        "review_criteria": "Review Criteria" in text
        and "10-dimension rubric" in text
        and "Mechanic Fidelity + Scaffold Honesty" in text,
        "dashboard_workflow": "Review Dashboard Workflow" in text
        and f"python3 scripts/generate_storyboard_prompts.py runs/{run_dir.name}" in text
        and f"python3 scripts/repair_full_pass_asset_bundle.py runs/{run_dir.name}" in text
        and f"python3 scripts/build_activity_assets.py runs/{run_dir.name} --mode generate_and_curate" in text
        and f"python3 scripts/validate_asset_build_outputs.py runs/{run_dir.name}" in text
        and f"python3 scripts/validate_full_pass_asset_bundle.py runs/{run_dir.name}" in text
        and f"python3 scripts/generate_asset_pilot_prompts.py runs/{run_dir.name}" in text
        and f"python3 scripts/generate_run_review.py runs/{run_dir.name}" in text
        and f"python3 scripts/generate_run_review.py --validate runs/{run_dir.name}" in text,
        "mechanism_storyboards": not active_storyboard_root
        or (
            text.count("Mechanism Storyboard") >= expected_packages
            and all(path.exists() for path in storyboard_meta_files)
            and "storyboard-caption-row" in text
            and (
                not storyboard_requires_images
                or (
                    text.count("mechanism_grid.png") >= len(expected_storyboard_images)
                    and all(path.exists() for path in expected_storyboard_images)
                )
            )
        ),
        "generated_asset_pilot": not asset_pilot_entries
        or (
            "Generated Prebuilt Assets" in text
            and text.count('class="asset-pilot-card"') == len(asset_pilot_entries)
            and "contact_sheet.prompt.md" in text
            and "contact_sheet.png" in text
            and "When to display" in text
            and "Consistency" in text
            and all(path.exists() for path in expected_asset_images)
        ),
        "runtime_asset_outputs": (
            not runtime_asset_entries
            and not requested_runtime_mode
        )
        or (
            requested_runtime_mode
            and not runtime_asset_entries
            and "Generated Runtime Assets" in text
            and requested_runtime_mode in text
            and (
                "Missing asset_outputs.yaml" in text
                or "No asset output entries recorded" in text
            )
        )
        or (
            "Generated Runtime Assets" in text
            and (not actual_runtime_mode or actual_runtime_mode in text)
            and text.count('class="runtime-asset-card"') == len(runtime_asset_entries)
            and "asset_outputs.yaml" in text
            and "reference_sources.yaml" in text
            and "qa_notes.yaml" in text
            and "source metadata" in text
            and "work item" in text
            and all(path.exists() for path in expected_runtime_asset_images)
        ),
        "full_pass_asset_bundle": not full_pass_pipeline or not full_pass_asset_bundle_issues,
        "activity_html_exports": not export_entries
        or (
            "Activity HTML Exports" in text
            and "standalone reviewer packets" in text
            and text.count('class="activity-export-card"') == len(export_entries)
            and all(normalize_text(entry.get("html_path")) in text for entry in export_entries if isinstance(entry, dict))
        ),
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
        "blocked_marker_clarity": expected_blocked == 0
        or (
            "Inline blocked markers" in text
            and "Unique blocker types" in text
            and "These are occurrences inside the preview steps" in text
        ),
        "minimum_unblock_per_blocked_card": expected_blocked == 0
        or (
            text.count("Minimum To Unblock") >= expected_blocked
            and "minimum-unblock-list" in text
            and "Smallest policy or scope decision needed" in text
        ),
        "blocked_element_chips": expected_blocked == 0
        or ("blocked-element-chip" in text and "blocked-marker-row" in text),
        "blocked_preview_scorecards": expected_blocked == 0
        or (
            text.count("Blocked Preview Scorecard") >= expected_blocked
            and "BLOCKED" in text
            and "This is review evidence only" in text
        ),
        "clickable_detail_cards": text.count("data-detail-template=") >= expected_packages + expected_blocked
        and "<dialog" in text
        and "showModal()" in text
        and "View details" in text,
        "grouped_tag_colors": "badge-mechanic" in text
        and "badge-asset" in text
        and "badge-category" in text
        and "badge-reviewer" in text,
        "reviewer_mapping": not expected_reviewer_pairs
        or all(f'data-reviewer="{reviewer}"' in text for reviewer in expected_reviewer_pairs.values()),
        "asset_usage_timeline": expected_packages == 0
        or (
            text.count("Asset Usage Timeline") >= expected_packages
            and "Asset dependencies" in text
            and "Display beats" in text
            and "Image items" in text
            and (not any(asset_usage_sets) or "asset-usage-table" in text)
        ),
        "reason_guide_descriptions": (expected_blocked == 0 and not expected_reason_labels)
        or (
            "Blocking Reason Guide" in text
            and "What it means" in text
            and "Why it blocks validity" in text
            and "Minimum to unblock" in text
        ),
        "resolved_blocker_reason_coverage": not expected_reason_labels
        or all(f">{label}</span>" in text for label in expected_reason_labels),
        "resolved_blocker_annotations": not has_resolved_blockers
        or (
            "Resolved Contract Items" in text
            and "Resolved Blockers" in text
            and "resolved-blocker-row" in text
        ),
        "product_capability_resolved_annotations": not product_capability_gaps,
        "extensibility_overview": not has_extensibility
        or (
            "Extensibility Overview" in text
            and "Reusable slots" in text
            and "Parameterization mode" in text
            and "Integrity" in text
            and "Extensibility" in text
        ),
        "no_external_assets": not re.search(r"<(?:script|link)[^>]+(?:src|href)=[\"']https?://", text),
        "in_file_preview_wired": (
            'id="preview-dialog"' in text
            and 'data-preview-id="preview-' in text
            and 'id="file-previews"' in text
            and "renderMarkdown" in text
            and text.count("<template ") > expected_packages
        ),
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
    if product_capability_gaps:
        print("product_capability_gaps=" + ", ".join(product_capability_gaps))
    if runtime_quality_findings:
        print("runtime_contract_quality_findings=" + " | ".join(runtime_quality_findings[:20]))
    if full_pass_asset_bundle_issues:
        formatted = [
            f"{issue.get('activity_id')}/{issue.get('missing_asset_id') or issue.get('asset_id')}: {issue.get('kind')}"
            for issue in full_pass_asset_bundle_issues[:20]
        ]
        print("full_pass_asset_bundle_findings=" + " | ".join(formatted))
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
    html_text = strip_trailing_whitespace(build_html(repo_root, run_dir))
    out = run_dir / "review.html"
    out.write_text(html_text)
    print(f"Wrote {out.relative_to(repo_root)}")


if __name__ == "__main__":
    main()
