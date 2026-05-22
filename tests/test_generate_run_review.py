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

    def test_runtime_beats_have_visual_map(self):
        self.assertGreaterEqual(self.html.count('class="runtime-map"'), 40)
        self.assertIn('class="runtime-map-node', self.html)
        self.assertIn('class="runtime-lane runtime-lane-ai"', self.html)
        self.assertIn('class="runtime-lane runtime-lane-followup"', self.html)
        self.assertIn('class="branch-chip branch-chip-ideal"', self.html)
        self.assertIn('class="screen-strip"', self.html)

    def test_runtime_behavior_contract_beats_parse_and_render(self):
        prod_text = """
#### Step 1: Story Gate

**Runtime AI instruction:** Tell a short story beat first, pause at the gate, then ask for one blue-object photo challenge before unlocking the next beat.

**Example AI line:** [mysterious story tone] "The moon gate is closed. Can you find something blue to wake it up?"

**Child responses:**

1. (Ideal) Child finds and photographs a blue object.
2. (Unexpected) Child names a blue object instead of taking a photo.
3. (No response) Child is quiet.

**AI follow-up policy:**

1. (Ideal) Celebrate the found color and unlock the next story line.
2. (Unexpected) Validate the idea, then ask for a real photo if available.
3. (No response) Offer a smaller hint.

**Screen/state:** Moon gate card stays locked until the challenge is complete.
"""
        beats = self.report.runtime_beats(prod_text)
        self.assertEqual(1, len(beats))
        beat = beats[0]
        self.assertEqual("runtime_contract", beat["speech_mode"])
        self.assertIn("story beat first", beat["runtime_instruction"])
        self.assertIn("moon gate", beat["example_ai_line"])
        self.assertIn("unlock the next story line", beat["followup"])
        self.assertIn("Moon gate card", beat["screen"])

        rendered_map = self.report.runtime_beat_map(beats)
        rendered_detail = self.report.runtime_beat_html(beat)
        self.assertIn("Runtime behavior contract", rendered_map)
        self.assertIn("Example AI line", rendered_map)
        self.assertIn("Screen/state", rendered_detail)

    def test_runtime_branch_policy_renders_as_horizontal_table(self):
        prod_text = """
#### Step 1: Story Gate

**Runtime AI instruction:** Tell a short story beat first, pause at the gate, then ask for one blue-object photo challenge before unlocking the next beat.

**Example AI line:** [mysterious story tone] "The moon gate is closed. Can you find something blue to wake it up?"

**Child responses:**

1. (Ideal) Child finds and photographs a blue object.
2. (Unexpected) Child names a blue object instead of taking a photo.
3. (No response) Child is quiet.

**AI follow-up policy:**

1. (Ideal) Celebrate the found color and unlock the next story line.
2. (Unexpected) Validate the idea, then ask for a real photo if available.
3. (No response) Offer a smaller hint.

**Screen/state:** Moon gate card stays locked until the challenge is complete.
"""
        rendered_map = self.report.runtime_beat_map(self.report.runtime_beats(prod_text))
        self.assertIn('class="branch-followup-table"', rendered_map)
        self.assertIn("<th>Branch</th>", rendered_map)
        self.assertIn("<th>Child behavior</th>", rendered_map)
        self.assertIn("<th>AI follow-up</th>", rendered_map)

    def test_generic_branch_policy_detection_flags_boilerplate(self):
        prod_text = """
#### Step 3: Start The Source Action

**Runtime AI instruction:** Preserve the workbook promise: the child tells a story gate challenge.

**Example AI line:** [story tone] "The gate opens after a blue-object challenge."

**Child responses:**

1. (Ideal) The child gives the first source-aligned action.
2. (Unexpected) Child gives an unrelated answer, unsafe action, or asks to change the task.
3. (No response) Child stays quiet, waits, or looks at the screen.

**AI follow-up policy:**

1. (Ideal) [specific] Confirm the action and name how it matches the source rule.
2. (Unexpected) [redirect] Validate the idea, restate the safe rule, and offer one easier choice.
3. (No response) [wait 2s] [gentle] Model a tiny answer and invite one small try.

**Screen/state:** Shows the active round token.
"""
        findings = self.report.generic_branch_policy_findings(self.report.runtime_beats(prod_text))
        self.assertEqual(1, len(findings))
        self.assertIn("Step 3", findings[0])
        self.assertIn("Unexpected", findings[0])
        self.assertIn("No response", findings[0])

    def test_generic_branch_policy_detection_flags_keyword_substitution(self):
        prod_text = """
#### Step 3: Start The Source Action

**Runtime AI instruction:** Preserve the workbook promise: the child chooses between two story paths.

**Example AI line:** [story tone] "Do you choose the cave path or the bridge path?"

**Child responses:**

1. (Ideal) The child chooses a path.
2. (Unexpected) Child veers away from "Start The Source Action" in Branching Choice Story, skips the decision action, or proposes an unsafe/out-of-scope version.
3. (No response) Child pauses at "Start The Source Action", watches the current screen, or needs a first tiny decision model.

**AI follow-up policy:**

1. (Ideal) Continue the chosen path.
2. (Unexpected) [redirect] Validate briefly, keep the Branching Choice Story frame, and offer one safe choice that still completes "Start The Source Action".
3. (No response) [wait 2s] [gentle] Model one tiny decision step for "Start The Source Action", then invite the child to copy or choose.

**Screen/state:** Shows two path tokens.
"""
        findings = self.report.generic_branch_policy_findings(self.report.runtime_beats(prod_text))
        self.assertEqual(1, len(findings))
        self.assertIn("keyword-substitution", findings[0])

    def test_generic_branch_policy_detection_flags_repeated_round_policy(self):
        prod_text = """
#### Step 3: Multi-Round Core Loop

**Round 1 -- Cave Door:**

**Runtime AI instruction:** Ask the child to choose the cave path or bridge path.

**Example AI line:** "Which path should the fox try first?"

**Child responses:**

1. (Ideal) The child chooses the cave path.
2. (Unexpected) Child invents a third path or talks about the fox without choosing.
3. (No response) Child studies the two path tokens without picking one.

**AI follow-up policy:**

1. (Ideal) Narrate the cave path opening.
2. (Unexpected) Restate the two available paths and ask for one choice.
3. (No response) [wait 2s] Read the path labels again and ask for one tap or word.

**Screen/state:** Two path tokens are visible.

**Round 2 -- Bridge Door:**

**Runtime AI instruction:** Ask the child to choose the owl bridge or moon boat.

**Example AI line:** "Now should the fox cross the bridge or ride the boat?"

**Child responses:**

1. (Ideal) The child chooses the bridge.
2. (Unexpected) Child invents a third path or talks about the fox without choosing.
3. (No response) Child studies the two path tokens without picking one.

**AI follow-up policy:**

1. (Ideal) Narrate the bridge path opening.
2. (Unexpected) Restate the two available paths and ask for one choice.
3. (No response) [wait 2s] Read the path labels again and ask for one tap or word.

**Screen/state:** Two path tokens are visible.
"""
        findings = self.report.generic_branch_policy_findings(self.report.runtime_beats(prod_text))
        self.assertEqual(1, len(findings))
        self.assertIn("repeated branch policy", findings[0])


if __name__ == "__main__":
    unittest.main()
