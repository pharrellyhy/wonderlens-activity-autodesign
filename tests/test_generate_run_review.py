import importlib.util
from pathlib import Path
import re
import sys
import tempfile
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

    def test_runtime_contract_quality_flags_thin_instructions(self):
        prod_text = """
#### Step 1: Thin Prompt

**Runtime AI instruction:** Ask about the picture.

**Child responses:**

1. (Ideal) Child answers.
2. (Unexpected) Child talks about something else.
3. (No response) Child is quiet.

**AI follow-up policy:**

1. (Ideal) Continue.
2. (Unexpected) Redirect gently.
3. (No response) Offer a model.

**Screen/state:** Show the activity start.
"""
        findings = self.report.runtime_contract_quality_findings(self.report.runtime_beats(prod_text))

        self.assertEqual(1, len(findings))
        self.assertIn("Thin Prompt", findings[0])
        self.assertIn("missing Example AI line", findings[0])
        self.assertIn("missing runtime contract cues", findings[0])

    def test_runtime_contract_quality_accepts_fullstack_style_instructions(self):
        prod_text = """
#### Step 1: Fluffy Dandelion Hook

**Runtime AI instruction:** Goal: react with wonder to the dandelion's white fluffy seeds as tiny parachutes, then ask one imaginative question about where they might fly. Constraint: T0 max 2 sentences, build from the child's photo, preserve the dandelion-first source frame, and do not turn it into a counting quiz. Emotion/tone: excited and curious. Child progress evidence: the child says, points, blows, or gestures where the seeds might go. Branch behavior: for ideal responses, echo the child's imagined direction and bridge toward finding more soft things; for unexpected flower/color comments, validate the observation and return to fluffiness; for no response, wait briefly and model one tiny-cloud idea.

**Example AI line:** [delighted gasp] "Ooh, look at those tiny fluffy parachutes! Where do you think they want to fly?"

**Child responses:**

1. (Ideal) Child says the seeds fly up, away, to the sky, or blows gently.
2. (Unexpected) Child says it is a flower, names the color, or wants to pick it.
3. (No response) Child quietly looks at the dandelion photo.

**AI follow-up policy:**

1. (Ideal) Echo the child's imagined seed direction, then wonder whether more soft treasures are nearby.
2. (Unexpected) Accept the flower/color comment, name the soft seeds, then invite one fluffy observation.
3. (No response) [wait 2s] Offer "tiny clouds" as a model, then ask for one small look or touch.

**Screen/state:** Dandelion photo remains centered; seed-head sparkles pulse gently while the first mission slot waits.
"""
        findings = self.report.runtime_contract_quality_findings(self.report.runtime_beats(prod_text))

        self.assertEqual([], findings)

    def test_review_validation_fails_thin_runtime_contracts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            run_dir = root / "runs" / "quality_smoke"
            package_dir = run_dir / "activity_packages" / "quality_smoke"
            package_dir.mkdir(parents=True)
            (run_dir / "run_manifest.yaml").write_text(
                "run_id: quality_smoke\n"
                "outputs:\n"
                "  generated_activities:\n"
                "    - activity_id: quality_smoke\n"
                "      activity_path: runs/quality_smoke/activity_packages/quality_smoke\n"
            )
            (run_dir / "review_notes.md").write_text("# Review Notes\n")
            (run_dir / "assignment_snapshot.md").write_text("# Assignments\n")
            (run_dir / "generated_activity_ids.txt").write_text("quality_smoke\n")
            (package_dir / "spec.md").write_text(
                "## Self-Evaluation Scorecard\n\n"
                "| # | Dimension | Score | Notes |\n"
                "|---|---|---|---|\n"
                + "".join(f"| {i} | D{i} | PASS | ok |\n" for i in range(1, 11))
            )
            (package_dir / "prod.md").write_text(
                "## Quality Smoke\n\n"
                "#### Step 1: Thin Prompt\n\n"
                "**Runtime AI instruction:** Ask about the picture.\n\n"
                "**Child responses:**\n\n"
                "1. (Ideal) Child answers.\n"
                "2. (Unexpected) Child talks about something else.\n"
                "3. (No response) Child is quiet.\n\n"
                "**AI follow-up policy:**\n\n"
                "1. (Ideal) Continue.\n"
                "2. (Unexpected) Redirect gently.\n"
                "3. (No response) Offer a model.\n\n"
                "**Screen/state:** Show the activity start.\n"
            )
            (package_dir / "tag_block.yaml").write_text(
                "activity_name: Quality Smoke\n"
                "template_type: cat1\n"
                "activity_signature:\n"
                "  mechanic: describe\n"
            )
            (package_dir / "recap.template.yaml").write_text("{}\n")
            (package_dir / "dashboard.template.yaml").write_text("{}\n")
            (run_dir / "review.html").write_text(self.report.build_html(root, run_dir))

            with self.assertRaisesRegex(SystemExit, "runtime_contract_quality"):
                self.report.validate(root, run_dir)

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
