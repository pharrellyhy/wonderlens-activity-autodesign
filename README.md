# WonderLens Activity Auto-Designer

> Adapted from [karpathy/autoresearch](https://github.com/karpathy/autoresearch) pattern.
> Human writes `program.md` + `assignments.md`. AI agent generates activity designs autonomously.

## How it works

```
program.md          — Agent instructions, constraints, rubric, seed exemplars (human edits this)
templates.md        — Category templates: structural skeletons with variable slots (human edits this)
entity_guidance.md  — Mapping schema and selection rules for mapping-informed designs
conversation_bridge.md — Warm/cold bridge patterns for conversation-aware activities
assignments.md      — List of entity+category assignments to design (human edits this)
run.md              — Kick-off prompt for the agent (human edits this once)
data/mappings_dev20_0318/ — Source entity mappings used by Batch 2 assignments
designs/cat1/       — Cat 1 prod + spec files (in-device verbal interactions)
designs/cat5/       — Cat 5 prod + spec files (out-of-device collection activities)
docs/game_styles.md — Game style taxonomy (6 styles across 2 categories)
results.tsv         — Tracking log: assignment, status, rubric scores, timestamp
```

The agent reads `program.md` for context, picks the next unfinished assignment from `assignments.md`, generates the full activity design with self-evaluation, saves it to `designs/`, logs the result in `results.tsv`, and moves to the next assignment. Repeat until all assignments are done.

## Quick Start

### 1. Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed (`npm install -g @anthropic-ai/claude-code`)
- Anthropic API key set (`export ANTHROPIC_API_KEY=sk-ant-...`)

### 2. Clone and set up

```bash
git clone https://github.com/<your-username>/wonderlens-activity-autodesign.git
cd wonderlens-activity-autodesign
git checkout -b autodesign/$(date +%b%d)
```

### 3. Edit assignments

Open `assignments.md` and add your entity+category pairs. A starter batch of 10 is included.

### 4. Run the agent

```bash
claude --dangerously-skip-permissions
```

Then paste:

```
Read program.md, templates.md, entity_guidance.md, conversation_bridge.md, run.md, and assignments.md. Then begin the autonomous design loop. Start with setup, then work through every assignment.
```

### 5. Walk away

The agent will work through each assignment, generating full activity designs and saving them. Check `results.tsv` in the morning for a summary.

## Project Structure

```
.
├── README.md                 ← You are here
├── program.md                ← Agent instructions (the "skill file")
├── templates.md              ← Category templates (structural skeletons per activity type)
├── entity_guidance.md        ← How to read mapping YAML files and ground designs in them
├── conversation_bridge.md    ← Warm/cold bridge rules for mapping-informed designs
├── assignments.md            ← Input: entity+category pairs to design
├── run.md                    ← Kick-off instructions for the agent loop
├── data/mappings_dev20_0318/ ← Entity mapping dataset used by mapping-informed assignments
├── designs/                  ← Output folder
│   ├── cat1/                 ← Cat 1 (In-Device Verbal) prod + spec files
│   ├── cat5/                 ← Cat 5 (Out-of-Device Collection) prod + spec files
│   └── *_cat{1,5}.md        ← Legacy base designs (pre-prod/spec split)
├── docs/
│   ├── game_styles.md        ← Game style taxonomy and distribution
│   └── plans/                ← Implementation plans
└── results.tsv               ← Experiment log
```

## Design File Conventions

Each entity has up to two files per category:

- **`_prod.md`** — Production format. Cold-start transition bridge, full interaction flow, self-evaluation scorecard.
- **`_spec.md`** — Full specification. Adds mapping metadata (Trigger Entity, Mapping Source, IB Theme, Dimension Anchors), warm-start + cold-start bridges, and detailed scorecard.

All prod and spec files carry version metadata:

| Field | Example |
|-------|---------|
| Design Version | `1.0` (original) or `2.0 — naming_story redesign` |
| Last Updated | `2026-03-19` |

## Game Styles

Six reusable interaction patterns across two categories:

**Cat 1 — In-Device Verbal (4 styles):** `voice_acting` (4), `storytelling_chain` (1), `prediction_game` (2), `helper_hotline` (3)

**Cat 5 — Out-of-Device Collection (2 styles):** `comparison_chart` (5), `naming_story` (9)

See [`docs/game_styles.md`](docs/game_styles.md) for full definitions and design lists.

## Current Coverage

| Category | Entities | Prod | Spec | Total |
|----------|----------|------|------|-------|
| Cat 1 | 16 | 16 | 6 | 22 |
| Cat 5 | 19 | 19 | 19 | 38 |

## Design Choices

Following the autoresearch philosophy:

- **Single agent, sequential processing.** One assignment at a time, fully completed before moving on.
- **Self-evaluation built in.** The agent evaluates against a 9-dimension rubric before saving. Dimension 9 applies only to mapping-informed designs; failed dimensions are auto-fixed.
- **Git as the ratchet.** Each completed design is committed. If the agent crashes mid-design, no work is lost.
- **Human edits .md files, agent edits designs/.** Clean separation of concerns.

## Iterating

After reviewing the first batch:

1. If quality is consistently weak on a specific dimension → edit the rubric in `program.md`
2. If a certain activity category produces flat results → add more seed exemplars to `program.md`
3. If you want to refine the tone/style → edit the "Core Design Principles" in `program.md`
4. Add new assignments to `assignments.md` and re-run

## License

MIT
