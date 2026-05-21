import importlib.util
import pathlib
import tempfile
import unittest
import zipfile


REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_script(name):
    path = REPO_ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_source_workbook(path):
    strings = [
        "活动名称",
        "添加时间",
        "主体类型",
        "形式(单选)",
        "场景",
        "机制(Mechanic)(单选)",
        "对屏幕的依赖度（特指视觉展示，不包括拍照行为）",
        "活动简介/举例",
        "备注",
        "音素寻宝",
        "Cat 5. 需结合拍照",
        "3. 收集/配对 Collect/Match/Pair/Associate/Generalize",
        "低",
        "Find a thing whose word starts with /b/.",
        "Letter support can be shown.",
        "看部分，猜一猜",
        "Cat 1. 纯语音（含屏幕显示及互动）",
        "1. 识别/计数 Enumerate/Identify/Count/Measure",
        "高",
        "Show one part and let the child guess the whole animal.",
        "Needs prebuilt partial images.",
        "画画",
        "Cat 3. 需借助外部材料",
        "6. 搭建/创意 Build/Create/Assemble/Transform/Experiment/Invent",
        "AI guides a child to draw with paper and pencil.",
        "Requires external materials.",
    ]
    shared = ["<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>",
              "<sst xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\" count=\"26\" uniqueCount=\"26\">"]
    shared.extend(f"<si><t>{value}</t></si>" for value in strings)
    shared.append("</sst>")
    rows = [
        list(range(0, 9)),
        [9, 1, 2, 10, 4, 11, 12, 13, 14],
        [15, 1, 2, 16, 4, 17, 18, 19, 20],
        [21, 1, 2, 22, 4, 23, 18, 24, 25],
    ]
    sheet_rows = []
    for row_number, row in enumerate(rows, 1):
        cells = []
        for col_index, string_index in enumerate(row):
            col = chr(ord("A") + col_index)
            cells.append(f'<c r="{col}{row_number}" t="s"><v>{string_index}</v></c>')
        sheet_rows.append(f'<row r="{row_number}">{"".join(cells)}</row>')
    sheet = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<worksheet xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\">"
        "<sheetData>"
        f"{''.join(sheet_rows)}"
        "</sheetData></worksheet>"
    )
    workbook = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<workbook xmlns=\"http://schemas.openxmlformats.org/spreadsheetml/2006/main\" "
        "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\">"
        "<sheets><sheet name=\"Sheet1\" sheetId=\"1\" r:id=\"rId1\"/></sheets></workbook>"
    )
    rels = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
        "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet\" "
        "Target=\"worksheets/sheet1.xml\"/></Relationships>"
    )
    root_rels = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
        "<Relationship Id=\"rId1\" Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" "
        "Target=\"xl/workbook.xml\"/></Relationships>"
    )
    content_types = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">"
        "<Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>"
        "<Default Extension=\"xml\" ContentType=\"application/xml\"/>"
        "</Types>"
    )
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", root_rels)
        zf.writestr("xl/workbook.xml", workbook)
        zf.writestr("xl/_rels/workbook.xml.rels", rels)
        zf.writestr("xl/worksheets/sheet1.xml", sheet)
        zf.writestr("xl/sharedStrings.xml", "".join(shared))


def write_fixture(repo_root):
    run_dir = repo_root / "runs" / "test_run"
    (repo_root / "inputs").mkdir(parents=True)
    (run_dir / "adaptation_briefs").mkdir(parents=True)
    (run_dir / "activity_packages").mkdir(parents=True)
    (run_dir / "activity_exports").mkdir(parents=True)
    (run_dir / "generated_assets_pilot" / "concept_phoneme_hunt_collect" / "phoneme_letter_card_01").mkdir(parents=True)
    (run_dir / "generated_assets_pilot" / "concept_partial_reveal_deduce" / "partial_reveal_cards_01").mkdir(parents=True)
    (run_dir / "visual_storyboards" / "concept_phoneme_hunt_collect").mkdir(parents=True)
    (run_dir / "visual_storyboards" / "concept_partial_reveal_deduce").mkdir(parents=True)

    (repo_root / "inputs" / "source_activity_concepts.md").write_text(
        "### source_phoneme_hunt\n\n"
        "| Field | Value |\n|---|---|\n"
        "| source_row | 1 |\n| activity_concept | Phoneme Treasure Hunt |\n"
        "| normalized_description_en | The child finds an object whose word starts with a target sound. |\n"
        "| normalized_notes_en | Letter support can be shown. |\n"
        "| mechanic | collect |\n| category | cat5 |\n| assignment_type | match_pattern |\n\n"
        "### source_partial_reveal_guess\n\n"
        "| Field | Value |\n|---|---|\n"
        "| source_row | 2 |\n| activity_concept | Partial Reveal Guess |\n"
        "| normalized_description_en | The child guesses a whole animal from one visible part. |\n"
        "| normalized_notes_en | Needs prebuilt partial images. |\n"
        "| mechanic | deduce |\n| category | cat1 |\n| assignment_type | activity_concept |\n\n"
        "### source_guided_drawing\n\n"
        "| Field | Value |\n|---|---|\n"
        "| source_row | 3 |\n| activity_concept | Guided Drawing |\n"
        "| normalized_description_en | The AI guides a paper-and-pencil drawing. |\n"
        "| normalized_notes_en | Requires external materials. |\n"
        "| mechanic | build |\n| category | cat3 |\n| assignment_type | capability_probe |\n"
    )
    (run_dir / "run_manifest.yaml").write_text(
        "run_id: test_run\noutputs:\n  generated_activities:\n"
        "  - activity_id: concept_phoneme_hunt_collect\n"
        "    activity_path: runs/test_run/activity_packages/concept_phoneme_hunt_collect\n"
        "    assignment: assignment_type=match_pattern, concept_source=inputs/source_activity_concepts.md#source_phoneme_hunt,\n"
        "  - activity_id: concept_partial_reveal_deduce\n"
        "    activity_path: runs/test_run/activity_packages/concept_partial_reveal_deduce\n"
        "    assignment: assignment_type=activity_concept, concept_source=inputs/source_activity_concepts.md#source_partial_reveal_guess,\n"
        "  - activity_id: concept_guided_drawing_probe\n"
        "    activity_path: runs/test_run/activity_packages/concept_guided_drawing_probe\n"
        "    assignment: assignment_type=capability_probe, concept_source=inputs/source_activity_concepts.md#source_guided_drawing,\n"
    )
    briefs = {
        "001.yaml": ("Phoneme Treasure Hunt", "source_phoneme_hunt", "collect", "cat5", "ready_to_generate", "match_pattern"),
        "002.yaml": ("Partial Reveal Guess", "source_partial_reveal_guess", "deduce", "cat1", "ready_to_generate", "activity_concept"),
        "003.yaml": ("Guided Drawing", "source_guided_drawing", "build", "cat3", "resolved_from_blocked_until_product_decision", "capability_probe"),
    }
    for filename, (name, slug, mechanic, category, readiness, assignment_type) in briefs.items():
        (run_dir / "adaptation_briefs" / filename).write_text(
            "adaptation_brief:\n"
            f"  activity_concept: {name}\n"
            f"  canonical_mechanic: {mechanic}\n"
            f"  category_decision: {category}\n"
            f"  readiness: {readiness}\n"
            f"  assignment_type: {assignment_type}\n"
            "  core_promise: Child-facing promise.\n"
            "  source:\n"
            f"    concept_source: inputs/source_activity_concepts.md#{slug}\n"
            "  product_capability_flags:\n"
            "    - requires_materials\n"
        )
    packages = {
        "concept_phoneme_hunt_collect": "B-Sound Treasure Hunt",
        "concept_partial_reveal_deduce": "Partial Reveal Guess",
        "concept_guided_drawing_probe": "Guided Drawing",
    }
    for activity_id, title in packages.items():
        package_dir = run_dir / "activity_packages" / activity_id
        package_dir.mkdir(parents=True)
        (package_dir / "prod.md").write_text(f"## {title}\n\n**1. Brief Description**\n\nGenerated loop summary.\n")
        (package_dir / "tag_block.yaml").write_text("activity_signature:\n  mechanic: collect\n")
    (run_dir / "activity_exports" / "export_manifest.yaml").write_text(
        "entries:\n"
        "  - activity_id: concept_phoneme_hunt_collect\n"
        "    html_path: activity_exports/concept_phoneme_hunt_collect.html\n"
        "    image_path: generated_assets_pilot/concept_phoneme_hunt_collect/phoneme_letter_card_01/contact_sheet.png\n"
        "    storyboard_image_path: visual_storyboards/concept_phoneme_hunt_collect/mechanism_grid.png\n"
        "  - activity_id: concept_partial_reveal_deduce\n"
        "    html_path: activity_exports/concept_partial_reveal_deduce.html\n"
        "    image_path: generated_assets_pilot/concept_partial_reveal_deduce/partial_reveal_cards_01/contact_sheet.png\n"
        "    storyboard_image_path: visual_storyboards/concept_partial_reveal_deduce/mechanism_grid.png\n"
    )
    for path in [
        run_dir / "generated_assets_pilot" / "concept_phoneme_hunt_collect" / "phoneme_letter_card_01" / "contact_sheet.png",
        run_dir / "generated_assets_pilot" / "concept_partial_reveal_deduce" / "partial_reveal_cards_01" / "contact_sheet.png",
        run_dir / "visual_storyboards" / "concept_phoneme_hunt_collect" / "mechanism_grid.png",
        run_dir / "visual_storyboards" / "concept_partial_reveal_deduce" / "mechanism_grid.png",
    ]:
        path.write_bytes(b"png")
    return run_dir


class SourceComparisonReviewTest(unittest.TestCase):
    def test_build_report_classifies_rows_and_selects_visual_examples(self):
        comparison = load_script("generate_source_comparison_review")
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = pathlib.Path(tmp) / "repo"
            repo_root.mkdir()
            workbook = pathlib.Path(tmp) / "活动库内部初版.xlsx"
            write_source_workbook(workbook)
            run_dir = write_fixture(repo_root)

            report = comparison.build_report(repo_root, run_dir, workbook)
            html = comparison.render_html(report)

        self.assertEqual(3, report["summary"]["source_rows"])
        self.assertEqual(3, report["summary"]["covered_rows"])
        self.assertEqual(1, report["summary"]["mechanic_changed"])
        self.assertEqual(1, report["summary"]["capability_dependent"])
        self.assertEqual(0, report["summary"]["missing_generated"])
        self.assertGreaterEqual(len(report["visual_examples"]), 2)
        self.assertIn("Product Source Fidelity Review", html)
        self.assertIn("Visual Examples", html)
        self.assertIn("data-filter=\"changed\"", html)
        self.assertIn("data:image/png;base64,cG5n", html)
        self.assertIn("Mechanic changed", html)
        self.assertIn("Capability-dependent", html)
        self.assertNotIn(str(workbook.parent), html)

    def test_validate_report_rejects_missing_coverage_and_visuals(self):
        comparison = load_script("generate_source_comparison_review")
        issues = comparison.validate_report(
            {
                "rows": [{"activity_id": ""}],
                "summary": {"source_rows": 1, "covered_rows": 0},
                "visual_examples": [],
            }
        )

        self.assertIn("not all source rows are covered", "\n".join(issues))
        self.assertIn("no visual examples selected", "\n".join(issues))
