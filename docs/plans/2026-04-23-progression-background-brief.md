# Progression Runtime — Background Brief

**Audience:** PMs, authors, eng leadership, anyone who needs the "why" before reading the "how."

**Status:** 2026-04-23. Design shipped (Template 0 §07, walkthrough). Implementation plans shipped in sibling repos. This brief is the connective tissue — what problem it solves, what we get, what it's not.

---

## TL;DR

Template 0 gave us the vocabulary (7 axes × 3 rungs × 3 tiers = a bounded framework every activity fits into). **Progression is what makes that framework come alive across sessions.** Without it, every activity runs independently — the runtime has no memory of what the child did yesterday, no policy for where to take them next, no rule for how to back off when the current rung is too steep.

We're building a small, testable rules engine that reads per-round signals during an activity, classifies each session as **promote / hold / demote / soft-reframe**, updates per-axis state per device, and feeds that state back into game selection for the next activity. Plus three footer rules — dignity reframe, sibling-axis jump, personalization hook — that make it humane.

Net effect: after ~5-6 sessions on an axis, the system starts recognizably adapting. After ~30 sessions, the child's rung-per-axis profile tells a story a parent can recognize. V1 uses fixed thresholds; V2 swaps in a per-child pace model once we have enough data to train one.

---

## 1 · Why we're doing this

### 1.1 What exists today (without progression)

The current activity runtime does three things well:
- **Selects a game** for a photographed entity via Tier A → B → P cascade
- **Runs the activity** through a Director → Script → Visual → Assembler pipeline
- **Adapts to age tier** (T0/T1/T2) via the tier defaults in Template 0 §3

What it does NOT do:
- Remember anything about prior sessions for this child
- Choose a **rung** (L1/L2/L3) for the next activity based on the last one
- React when the child visibly struggles or visibly sprints ahead
- Distinguish a child going quiet because they're tired from a child who genuinely doesn't understand

A child who absolutely nails a Form-L2 activity today gets a Form-L2 activity tomorrow, because there's no mechanism to notice they should have moved to L3. A child who's silent for 8 seconds mid-activity gets the same pressure applied again, because there's no mechanism to distinguish "thinking" from "stuck." A child who hits a wall on Causation for three sessions in a row just keeps hitting the wall.

This is the gap progression fills.

### 1.2 What triggered this work

Three signals converged in April 2026:

1. **Template 0 reviewers** kept asking "when does the system decide to move the child up or down?" The answer was "it doesn't yet" — and §07 was written to answer that. §07 made it spec-complete. Now we need to make it run.

2. **Author feedback** after the matchability-tags PR (#10): "Fine, the upstream matcher knows which activity to pick. But how does it know which **rung** to pick?" Without progression, the runtime always enters at whatever the tag block declares — no escalation, no fallback.

3. **Parent-dashboard design** (parent_growth_path_preview.html §03) committed to a 7-axis curiosity radial. That radial is just a visualization of `rung-per-axis state over time` — which doesn't exist until we implement progression.

The progression walkthrough (`template_0_progression_walkthrough.html`) made the behavior visceral through 4 scenarios. It's the pitch deck; this implementation is the follow-through.

### 1.3 Why per-axis state (not one global level)

This is the single most important mental-model shift:

> Mia is at L3 on Form AND L1 on Causation AND uninitialized on Change.
> There is no XP bar. There are 7 bars, and they drift independently.

Every previous education-gamification system we looked at models one number: "your level." That's wrong for this product. A four-year-old can be eagle-eyed about what a ladybug looks like (Form L3) and still bewildered by why it's red (Causation L1). Forcing those two into a single summary erases the distinction the whole IB key-concept framework is built on.

Per-axis state is what makes the parent-dashboard radial truthful. It's also what makes the sibling-axis jump possible — you can't jump laterally without independent axis state.

---

## 2 · What we're going to build

### 2.1 The rules engine (the quantified part)

Five triggers, two scopes, all thresholds configurable:

| Trigger | What fires it |
|---|---|
| **Within-activity promote** | 2+ clean-correct rounds, OR a spontaneous L+1 response |
| **Within-activity hold** | mixed or slow but on-topic |
| **Within-activity demote** | 2 failed attempts (silence > 6s, off-topic, repeats prompt) |
| **Across-activity promote** | 3 consecutive same-axis successes → next is rung + 1 |
| **Across-activity demote** | 2 consecutive same-axis in-activity demotes → next is rung − 1 |

Implemented as pure functions (`classify_round_trail`, `apply_session_outcome`, `resolve_next_rung`). No I/O, no LLM, no DB — just takes signals and policy, returns an outcome. Trivially testable.

### 2.2 The humane part (the three footer rules)

Technical rules alone produce a cold system. Three additions keep it warm:

| Rule | What it does |
|---|---|
| **Dignity reframe** | When a demote fires, the AI script switches from "let's try again" to **"let me show you what I notice first"**. The child experiences variety, not regression. |
| **Sibling-axis jump** | When a child hits L3 on one axis (ceiling) or gets stuck at L1 after consecutive demotes (floor), the next activity pivots to L1 on a *related* axis (Form→Connection, Causation→Change). Keeps novelty without forcing depth. |
| **Personalization hook** | Thresholds live in a `progression_policy` object — not hardcoded. V1 ships three profiles (`v1_default/strict/loose`); ≥~200 sessions/child triggers a future swap to a per-child pace model without any activity redesign. |

### 2.3 The soft-reframe distinction (most-missed subtlety)

A single 8-second silence after a correct response is **not** a demote trigger. The runtime has a separate **soft-reframe** move: same rung, gentler prompt, second exemplar. Demote requires 2 attempts with failure patterns. The runtime isn't rung-greedy — it has intermediate moves that preserve rung without pushing.

This distinction is what the reluctance-vs-inability scenario in the walkthrough exists to make visceral.

### 2.4 Two repos, one truth

- **`wonderlens-ai`** — production backend; client-driven API; DB-persisted multi-device (Android app is the client).
- **`wonderlens-activity-fullstack-demo`** — prototype; single-user; local SQLite.

The two implementations use different styles (Pydantic vs dataclasses, `DatabaseManager` vs `aiosqlite`), but produce **identical behavior on the 4 walkthrough scenarios**, verified by a shared `progression_scenarios.json` test vector. Byte-level parity on the fixture; logic parity on the outcomes.

---

## 3 · What we're going to achieve

### 3.1 For the child

- **Adaptive pacing.** A child who's ready moves up. A child who's struggling moves down — gently, not punitively.
- **Across-axis independence.** Being new to Causation doesn't mean losing hard-won Form L3. Different axes, different rungs, same day.
- **Continuous experience, not graded.** The AI never says "that's wrong" or "let's try something easier." Demotes are surfaced as reframes: *"let me show you what I notice first."*
- **Novelty without forcing.** Hitting L3 on Form doesn't mandate L3 on Connection. Sibling jumps preserve breadth.

### 3.2 For authors

- **Progression is runtime-owned.** Authors set `progression.topic_axis` and `progression.difficulty_level` in the tag block. The runtime decides when to move. Authors don't hand-tune per-child pacing.
- **Activities are portable.** A single Form-L2 activity works whether the child is arriving at it fresh (first time on Form) or escalating into it after 3 L1 wins. Same content, different entry context.
- **Dignity rule is a script-agent flag, not a content change.** Authors don't have to write "fallback dialogue." The script agent rewrites its opener when needed.

### 3.3 For parents (via the dashboard)

- **The curiosity radial becomes truthful.** Today it's a mockup; with progression, it reflects real rung-per-axis state over time.
- **The drift story is visible.** "Your child has climbed to L3 on Form over 6 sessions, held steady at L2 on Causation, and only just began exploring Responsibility" — this is what the radial shows, month over month.
- **Demotes are never surfaced to parents as setbacks.** The dashboard shows current state + direction of travel; individual session-level demotes appear as pivots, not regressions. Parity with how the child experiences them.

### 3.4 For PM / eng

- **A measurable signal.** Every session produces a `SessionOutcome` record: axis, entry rung, exit rung, final result, whether dignity fired, whether sibling jump applied. This is the substrate for every progression-related metric we'll want to compute.
- **Policy variants are trivial to swap.** Changing a threshold means editing one YAML field, not chasing through the codebase. The per-child pace model slots in behind the same `ProgressionPolicy` interface.
- **Parity across repos is enforced.** The JSON scenario vector catches any rules-engine drift between prod and demo the instant it happens.

### 3.5 The reviewer test

The Template 0 §07 review conversation kept producing variants of one question: *"when does this move the child up or down?"* Post-implementation, that question has a one-sentence answer: **"when the quantified trigger in §07 fires."** No ambiguity, no hand-waving, no "well, it depends." That alone is the qualitative win this work delivers.

---

## 4 · What success looks like (concrete)

### Launch signals (ship day)

- Both repos' 4-scenario test vectors green
- A full end-to-end session in the demo shows a non-empty rung-per-axis state in the debug panel after completion
- `GET /api/v1/progression/{device_id}` returns the expected state shape on prod backend

### Week-1 signals (after first 10+ real sessions)

- At least one `promote` outcome logged (proves the promote path fires)
- At least one `demote` outcome logged AND the associated session's dialogue verifiably includes the reframe phrase (proves dignity wiring works)
- At least one sibling-axis jump in the wild OR a synthetic integration test that exercises the path (proves the L3 ceiling → L1 sibling path is live, not theoretical)

### Month-1 signals

- Distribution of session outcomes looks right: majority `hold`, minority `promote`, rare `demote`, occasional `soft_reframe`. If we see 50%+ demotes, thresholds are wrong. If we see 0% demotes, outcome classification is too generous.
- At least one device with >10 sessions shows rung drift on at least 2 axes (proves per-axis independence manifests in real play, not just theory)
- Zero cases of the AI saying "let's try something easier" / "try again" in a demote turn (regression test on script-agent output)

### Quarterly signals

- Per-child data maturity — devices crossing ~200 sessions become candidates for the per-child pace model. Triggers the V2 work stream.
- Parent-dashboard radial ships and uses this API directly; no separate data pipeline needed.

---

## 5 · What this is NOT (scope clarity)

These are intentional cuts. Each gets its own follow-up plan when its time comes.

- **NOT an LLM-based outcome classifier.** V1 uses shallow heuristics (silent → silence counted; non-empty input → tentatively correct). A proper classifier that labels *was_correct / was_spontaneous_l_plus_1 / prompt_was_repeated* from raw dialogue is a separate design — it needs its own prompt-engineering work and its own cost/latency budget.
- **NOT the per-child pace model.** V1 ships three static threshold profiles. The per-child model is a future ML spec that needs ≥200 sessions/child of data to train. The interface is wired (`policy_version` on every `ProgressionState`), the implementation is not.
- **NOT the parent-dashboard UI.** The API feeds the 7-axis radial; the dashboard's visual wiring is a separate plan tied to `parent_growth_path_preview.html` §03.
- **NOT topic_axis backfill for gold-standard games.** Tier A/B games currently lack complete `progression.topic_axis` metadata. A follow-up task inventories the 12 gold standards and adds missing fields.
- **NOT cross-session continuity beyond last state.** V1 keeps counters, not trajectory. A child who promoted smoothly and a child who clawed their way up look the same in the current state; only the *rate* of arrival would distinguish them. That's a per-child-pace-model concern.
- **NOT a simulator.** The walkthrough scenarios are hand-authored narratives. We are not building a state-machine playground UI where authors tweak parameters and watch trajectories. YAGNI until an author specifically asks for it.

---

## 6 · Dependencies, ordering, risks

### What must land first

- **Template 0 §07** — shipped. Rules text is authoritative; implementation follows it, not the other way.
- **Matchability tags (PR #10)** — shipped. Gives game selector the metadata it needs to filter by `topic_axis` and rung.
- **Walkthrough (PR #11)** — shipped. Provides the 4 scenarios the test vector encodes.

### Execution order

1. **Backend plan** (`wonderlens-ai`) ships first — it's the production target and authors the canonical JSON vector.
2. **Demo plan** (`fullstack-demo`) ships second — pure mirror, copies the fixture, runs the same vector for parity.
3. Two separate PRs; can merge independently.

### Risks worth naming

| Risk | Mitigation |
|---|---|
| **Shallow outcome classifier produces wrong signals.** With placeholder heuristics, "was_correct=True" just means "child said something." Real classification needs LLM judgment. | V1 ships as structural scaffolding; we expect outcomes to trend `hold` heavily until the LLM classifier lands. The infrastructure works; the *signal quality* upgrades in V2. |
| **Thresholds are wrong.** 2/2/3 numbers are informed guesses, not validated. | Policy profiles (`strict/default/loose`) let us A/B profiles without code changes. Swap is an API call. |
| **Drift between the two repo implementations.** | Shared JSON scenario vector + mandatory parity check in both CI pipelines. Divergence blocks both PRs. |
| **Dignity reframe phrase is too stiff or too cutesy in practice.** | Phrase is configurable in `ProgressionPolicy.dignity_reframe_instruction`. Can be iterated on without touching rules code. First-pass phrasing from §07 footer is the V1 baseline. |
| **Sibling pairs table encodes editorial judgment.** | Table is small (7 entries), explicit in code, and easy to revise. If "Form's sibling is Function, not Connection" turns out to be right in practice, it's a 1-line change. |

### What this work unlocks

- **Parent dashboard** — curiosity radial with real data instead of mock
- **Author tooling** — can now report "this activity has been played 12 times at L2 and passed 10/12" because outcomes are logged
- **Cross-session content design** — authors can start thinking in *arcs* (sequences of 3-5 related activities) because the runtime can now sustain state across them
- **V2 per-child pace model** — once we have 200+ sessions/child, the interface is already in place

---

## 7 · One-paragraph pitch (for a skeptical reader)

Template 0 told us what a single activity looks like. The progression runtime tells us what **a sequence of activities** looks like for a specific child. It's the difference between a question bank and a tutor. Without it, the 7-axis framework is decorative; with it, the framework does the work authors are currently being asked to do manually. We're spending roughly one backend engineer-week to ship V1 with baked-in defaults, instrumented outcomes, and a clean path to the per-child pace model later. The alternative is continuing to ask "when does the runtime adapt?" and answering "it doesn't."

---

## Appendix — related docs

- **Design spec (authoritative rules):** `docs/template_0_preview.html` §07 "Promotion & demotion"
- **Visual walkthrough (4 scenarios):** `docs/template_0_progression_walkthrough.html` + `_cn.html`
- **Cross-repo coordination:** `docs/plans/2026-04-21-progression-runtime-integration.md`
- **Backend implementation plan:** `wonderlens-ai/docs/plans/2026-04-21-progression-runtime-backend.md` (15 tasks)
- **Demo port implementation plan:** `wonderlens-activity-fullstack-demo/docs/plans/2026-04-21-progression-runtime-demo.md` (5 tasks)
- **Template 0 roadmap (Item 8 = this work):** `docs/plans/2026-04-20-template-0-roadmap.md`

---

## Revnote

- **v0.1** (2026-04-23) — Inaugural background brief. Covers problem statement, design intent, expected outcomes by audience, scope limits, risks, and pitch. Written after design (§07) + walkthrough (PR #11) + implementation plans (2026-04-21) all shipped; serves as the connective tissue for readers who need the why without the 3000-line how.
