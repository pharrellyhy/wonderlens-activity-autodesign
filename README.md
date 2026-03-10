# WonderLens Activity Auto-Designer

> Adapted from [karpathy/autoresearch](https://github.com/karpathy/autoresearch) pattern.
> Human writes `program.md` + `assignments.md`. AI agent generates activity designs autonomously.

## How it works

```
program.md          — Agent instructions, constraints, rubric, seed exemplars (human edits this)
templates.md        — Category templates: structural skeletons with variable slots (human edits this)
assignments.md      — List of entity+category assignments to design (human edits this)
run.md              — Kick-off prompt for the agent (human edits this once)
designs/            — Output folder. Each completed design is saved as a separate .md file
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
Read program.md, templates.md, run.md, and assignments.md. Then begin the autonomous design loop. Start with setup, then work through every assignment.
```

### 5. Walk away

The agent will work through each assignment, generating full activity designs and saving them. Check `results.tsv` in the morning for a summary.

## Project Structure

```
.
├── README.md                 ← You are here
├── program.md                ← Agent instructions (the "skill file")
├── templates.md              ← Category templates (structural skeletons per activity type)
├── assignments.md            ← Input: entity+category pairs to design
├── run.md                    ← Kick-off instructions for the agent loop
├── designs/                  ← Output: one .md file per completed design
│   └── .gitkeep
└── results.tsv               ← Experiment log
```

## Design Choices

Following the autoresearch philosophy:

- **Single agent, sequential processing.** One assignment at a time, fully completed before moving on.
- **Self-evaluation built in.** The agent evaluates against an 8-dimension rubric before saving. Failed dimensions are auto-fixed.
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
