import importlib.util
from pathlib import Path
import re
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_DIR = REPO_ROOT / "runs" / "20260512_172135_batch5_unblocked"


def load_report_module():
    spec = importlib.util.spec_from_file_location(
        "generate_run_review", REPO_ROOT / "scripts" / "generate_run_review.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class GenerateRunReviewRegressionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = load_report_module()
        cls.html = cls.report.build_html(REPO_ROOT, RUN_DIR)

    def test_reviewer_names_are_mapped_from_review_notes(self):
        self.assertIn('data-reviewer="Confucius"', self.html)
        self.assertIn('data-reviewer="Hypatia"', self.html)
        self.assertIn('data-reviewer="Lovelace"', self.html)
        self.assertIn('data-reviewer="Hilbert"', self.html)
        self.assertIn('data-reviewer="Planck"', self.html)
        self.assertNotIn('data-reviewer="unknown"', self.html)

    def test_resolved_blocker_guide_keeps_all_run_categories(self):
        expected_labels = {
            "Runtime image generation",
            "Coloring or recoloring UI",
            "Cat3 material workflow",
            "UI state or progress memory",
            "Prebuilt asset display",
            "Motion safety",
            "Before/after evidence",
            "OCR or text handling",
            "Caregiver setup and pacing",
        }
        for label in expected_labels:
            with self.subTest(label=label):
                self.assertIn(f">{label}</span>", self.html)

    def test_resolved_contract_summary_counts_visible_types(self):
        section = re.search(
            r'id="resolved-contract-items".*?</section>', self.html, flags=re.S
        )
        self.assertIsNotNone(section)
        section_html = section.group(0)
        self.assertIn("<th>Type count</th>", section_html)
        self.assertIn("<th>Resolved notes</th>", section_html)
        for row in re.findall(r"<tr><td>.*?</tr>", section_html, flags=re.S):
            cells = re.findall(r"<td>(.*?)</td>", row, flags=re.S)
            if len(cells) != 4:
                continue
            visible_type_count = cells[1].count("resolved-blocker-chip")
            self.assertEqual(str(visible_type_count), re.sub(r"<.*?>", "", cells[2]))


if __name__ == "__main__":
    unittest.main()
