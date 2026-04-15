# Experience Pillars: Game Style Redesign from First Principles

## Context

The current WonderLens game design system has 6 styles (4 Cat1, 2 Cat5) across ~25 designs. While structurally sound and IB-aligned, the designs suffer from four systemic problems:

1. **Samey** — Despite different entities, interaction patterns are repetitive (especially Cat5 where naming_story dominates 9 of 14 designs)
2. **Not fun enough** — Designs are structured conversations, not games. No genuine stakes, surprise, or "magic moments"
3. **Too narrow** — Over-index on imagination/narrative. Missing: spatial reasoning, temporal thinking, scientific method, construction/invention, metacognition
4. **Emotionally flat** — All designs feel warm-and-polite. No distinct emotional signatures between styles

**Solution**: Redesign the game style taxonomy around 6 Experience Pillars — each with a distinct emotional signature, game mechanic, and cognitive domain. Expand from 6 → 12 styles. Rewrite all existing designs + generate new ones.

---

## The 6 Experience Pillars

Each pillar answers: "After 3 minutes of play, how does the child FEEL?"

| # | Pillar | Child feels... | Magic moment | Game element | Cognitive domain |
|---|--------|---------------|-------------|-------------|-----------------|
| 1 | **Mystery** | "I figured it out!" | Hidden truth revealed | Clues → deduction → aha! | Reasoning, spatial |
| 2 | **Creation** | "I made this!" | Invention unveiled | Open-ended building | Divergent thinking |
| 3 | **Performance** | "They loved it!" | Audience ovation | Express → react → encore | Empathy, communication |
| 4 | **Discovery** | "Was I right?!" | Prediction meets reality | Predict → commit → reveal → score | Scientific method |
| 5 | **Adventure** | "Look how far we went!" | Whole journey visible | Progress → choice → map | Narrative, temporal |
| 6 | **Nurture** | "I helped!" | Visible transformation | Need → solve → impact | Responsibility, empathy |

### Why these six?

**Distinctness test**: Can a 4-year-old tell the difference? "Mystery" and "Discovery" are the closest pair — but Mystery is *detective work* (someone hid something, find it) while Discovery is *scientist work* (guess what will happen, then check). Different roles, different emotions.

**Coverage of current gaps**:

| Current gap | Filled by |
|-------------|-----------|
| Spatial reasoning | Mystery (clue geography, where to look) |
| Temporal thinking | Adventure (journey through time/stages) |
| Scientific method | Discovery (hypothesis → test → learn) |
| Construction/invention | Creation (combine → build → reveal) |
| Genuine surprise/stakes | All pillars (each has a "magic moment" with uncertainty) |

**Game-feel test**: Every pillar has *stakes*. Mystery: "Will I solve it?" Discovery: "Was I right?" Creation: "What will emerge?" Performance: "Will they react?" Adventure: "What's next?" Nurture: "Can I fix it?"

---

## The 12 Game Styles

Each pillar produces 1 Cat1 style (stationary + verbal) and 1 Cat5 style (mobile + collection).

### Mystery

**`mystery_lens`** (Cat1) — "I Spy meets 20 Questions in your own photo"
- AI secretly picks a DETAIL in the child's photo. Gives clues one at a time.
- Child deduces: "Is it the bow?" → "Warmer! It's softer than the bow..."
- 3-4 rounds targeting different aspects (texture → shape → function → imaginative)
- Stakes: "Can I spot it before the 3rd clue?"
- IB: Form, Function

**`mystery_trail`** (Cat5) — "Follow clue-riddles, discover the hidden pattern"
- AI gives riddle-clues about things to find: "I'm rough, round, smaller than your hand..."
- Child searches, photographs guess. AI confirms or redirects.
- After 3-4 finds, reveals the HIDDEN CONNECTION: "Everything you found was shaped by water!"
- Stakes: "What's the secret linking my finds?"
- IB: Form, Causation, Connection

### Creation

**`inventor_workshop`** (Cat1) — "What if we modified it?"
- AI asks "what if" questions: "What if your teddy had WHEELS?"
- Child invents. Each round adds a wilder modification.
- Final round: AI describes "Super [Entity]" with ALL modifications combined.
- Stakes: "What will my creation become?"
- IB: Function, Change, Connection

**`mix_lab`** (Cat5) — "Collect ingredients, invent something new"
- Collect 3-4 items. AI identifies a "superpower" per item (sticky, bouncy, smooth...).
- Synthesis: "Combine the bounciness of the ball with the stickiness of the pinecone — what would you invent?"
- Stakes: "What will these ingredients become?"
- IB: Form, Function, Connection

### Performance

**`voice_stage`** (Cat1) — evolved from voice_acting — "Perform for your audience!"
- AI sets performance CHALLENGES: "Your lion is auditioning! Show me your BIGGEST roar!"
- Audience reaction mechanic: AI responds AS audience ("The judges almost fell off their chairs!")
- Escalation with surprise twists: "Now do it WHISPERING!"
- Stakes: "Can I make the crowd react?"
- IB: Perspective, Form

**`ensemble_show`** (Cat5) — "Assemble your cast, put on a show"
- Collect 3-4 items. For each: "If this could make ONE sound, what would it be?"
- Synthesis: AI narrates a "concert" — each item performs, then all together.
- Stakes: "What will my band sound like?"
- IB: Form, Connection, Perspective

### Discovery

**`prediction_lab`** (Cat1) — evolved from prediction_game — "Commit, reveal, score!"
- AI describes scenario. Child COMMITS to prediction BEFORE reveal.
- Dramatic reveal + scoring: "*drumroll*... TEDDY WIGGLES HIS NOSE! Half point!"
- Running score: "You're 2 for 3! Can you go perfect?"
- Stakes: "Was I right? What's my score?"
- IB: Causation, Function

**`field_experiment`** (Cat5) — "Test a hypothesis outdoors"
- AI proposes question: "Are most things near the ground rough or smooth?"
- Child PREDICTS. Collects 4-5 items, reports property for each.
- AI tallies real results: "3 rough, 2 smooth — your hypothesis was CORRECT!"
- Stakes: "Will my prediction hold up?"
- IB: Form, Causation

### Adventure

**`time_traveler`** (Cat1) — evolved from storytelling_chain — "Journey through time"
- AI takes entity through TIME: "3 months ago, your banana was a tiny green flower..."
- Each round = different time jump (past → present → future → far future).
- Choice points: "Banana arrives at the store — fruit bowl or smoothie machine?" → different paths.
- Final: Timeline assembled showing whole journey.
- Stakes: "Where does this journey go?"
- IB: Change, Connection, Causation

**`quest_collector`** (Cat5) — evolved from naming_story — "Mission with a purpose"
- AI gives QUEST with criterion: "Find 3 things that USED to be something else"
- Each find evaluated: "A fallen leaf — it USED to be green! Quest item #1!"
- Detail harvesting preserved: "What does it remind you of?" → character name.
- Synthesis: Quest story with detail-driven character roles.
- Stakes: "Can I find things that match?"
- IB: Change, Form, Connection

### Nurture

**`care_station`** (Cat1) — evolved from helper_hotline — "Help it get better"
- AI presents need: "Your teddy is shivering!"
- Child proposes solution. AI narrates VISIBLE TRANSFORMATION: "Teddy stops shivering... smiles... 'Warm!'"
- Escalation: physical → emotional → complex (scared AND cold AND lonely).
- Relationship arc: By round 3, entity calls child by name.
- Stakes: "Can I figure out what it needs?"
- IB: Responsibility, Function, Connection

**`rescue_team`** (Cat5) — "Find things that need help"
- For each find, AI identifies a "need": "This leaf looks dry — it needs water!"
- Child proposes care. After 3-4 rescues, synthesis: "How would the feather help the leaf?"
- Stakes: "What does this one need?"
- IB: Responsibility, Connection, Perspective

### Lineage from Current Styles

| Current style | → New style | What changes |
|--------------|------------|-------------|
| voice_acting | **voice_stage** | Add audience reaction mechanic, escalating expression challenge, surprise twists |
| storytelling_chain | **time_traveler** | Add journey map, genuine choice points that branch the narrative, timeline visualization |
| prediction_game | **prediction_lab** | Add commitment-before-reveal, dramatic reveals, running score/tally |
| helper_hotline | **care_station** | Add visible transformation (entity gets BETTER), relationship arc with deepening gratitude |
| comparison_chart | **field_experiment** | Add pre-collection hypothesis, "was I right?" mechanic, data tallying |
| naming_story | **quest_collector** | Keep detail-harvesting, add quest framing with criterion, mission progression tracking |

---

## Template Architecture

### Base Structure (universal, 5 steps)

| Step | Purpose | What varies per pillar |
|------|---------|----------------------|
| 1. Hook | Emotional entry | Same across pillars |
| 2. Game Setup | Rules + demo | Pillar-specific: how the game works, demonstrated through an example |
| 3. Core Loop | 3-4 rounds | Pillar-specific mechanic with escalation |
| 4. Payoff | Magic moment | Pillar-specific climax — the emotional peak |
| 5. Celebration | IB as praise | Same across pillars |

### Pillar Overlays

Each pillar defines:
- **Game elements** specific to the experience (what makes it feel like THIS pillar)
- **Creative variables** per style (entity-specific content to fill in)
- **Magic moment specification** (the emotional climax that MUST exist — this is the D10 litmus test)
- **Escalation pattern** (how rounds get harder/deeper)
- **3-branch response handling** (ideal / unexpected / silence) — universal across all pillars

### Creative Variables by Pillar

| Pillar | Cat1 variables | Cat5 variables |
|--------|---------------|---------------|
| Mystery | `{hidden_details}`, `{clue_types}`, `{reveal_drama}` | `{riddle_clues}`, `{pattern_connection}`, `{reveal_narrative}` |
| Creation | `{modifications}`, `{combination_name}`, `{absurdity_escalation}` | `{superpowers_per_item}`, `{combination_prompt}`, `{invention_name}` |
| Performance | `{challenges}`, `{audience_character}`, `{twist_challenge}` | `{sound_per_item}`, `{ensemble_narrative}`, `{conductor_moments}` |
| Discovery | `{scenarios}`, `{reveal_drama}`, `{scoring_system}` | `{hypothesis}`, `{data_property}`, `{tally_result}` |
| Adventure | `{time_periods}`, `{choice_points}`, `{timeline_visualization}` | `{quest_criterion}`, `{detail_harvesting}`, `{quest_narrative}` |
| Nurture | `{needs_escalation}`, `{transformation_arc}`, `{relationship_deepening}` | `{needs_per_item}`, `{care_solutions}`, `{mutual_aid_synthesis}` |

---

## Rubric: 10 Dimensions

8 existing dimensions (2 merged) + 2 new game-design dimensions.

| # | Dimension | Status | Evaluates |
|---|-----------|--------|-----------|
| D1 | Technical Constraints | Keep | V1 hardware limits respected |
| D2 | Emotional Hook | Keep (absorb old D3) | First turn emotional + natural transition |
| D3 | Edge Cases | Keep (was D4) | Handles unexpected, silence, off-topic |
| D4 | IB Alignment | Keep (was D5) | Key Concepts, ATL Skills correctly mapped |
| D5 | Tier Fit | Keep (was D6) | Language/complexity matches target age |
| D6 | Dialogue Quality | Keep (was D7) | Natural, varied, 2-3 branches per prompt |
| D7 | Screen Design | Keep (was D8) | Visuals support interaction |
| D8 | Entity Grounding | Keep (was D9) | Uses mapping data correctly |
| **D9** | **Game Feel** | **NEW** | Genuine stakes + uncertainty + satisfying resolution |
| **D10** | **Pillar Fidelity** | **NEW** | Delivers promised emotional signature; blind reader could identify pillar |

### New Dimension Scoring Criteria

**D9 (Game Feel)**:
- PASS: Design has at least one moment of genuine uncertainty + a satisfying resolution. The child experiences stakes ("will I get it right?", "what will happen?", "can I make them react?")
- FAIL: Design feels like structured Q&A with no stakes or surprise

**D10 (Pillar Fidelity)**:
- PASS: A blind reader could identify which pillar this design belongs to from the interaction alone. The emotional arc matches the pillar's promise.
- FAIL: Design could be re-labeled to a different pillar without feeling wrong

---

## Migration: Entity → Pillar Remapping

| Pillar | Cat1 (from existing) | Cat5 (from existing) | New designs needed |
|--------|---------------------|---------------------|-------------------|
| Mystery | — | — | 4 new (2 Cat1, 2 Cat5) |
| Creation | — | — | 4 new (2 Cat1, 2 Cat5) |
| Performance | lion, piano, crayons, raincoat | — | 2 new Cat5 |
| Discovery | goldfish, eye | playground, sunflower, stop_sign, green_apple | 0-1 new |
| Adventure | banana, city_library | dandelion, feather, puddle, sandy_beach, autumn_leaf, pinecone | 0-1 new |
| Nurture | teddy_bear, firefighter, toothbrush_holder | — | 2 new Cat5 |

**Total**: ~25 existing remapped + ~12 new = ~37 designs across 12 styles

---

## Execution Plan

### Phase 0: Infrastructure (~1 session)

Update the design system files:

| File | Change |
|------|--------|
| `docs/game_styles.md` | Rewrite: 12 style definitions under 6 pillars (replace current 6-style taxonomy) |
| `templates.md` | Rewrite: base templates + 6 pillar overlays with creative variables |
| `program.md` | Update: 10-dimension rubric (add D9 Game Feel + D10 Pillar Fidelity, merge D2+D3, renumber) |
| `run.md` | Update: pillar-aware generation loop, gold standard reference |

### Phase 1: Gold Standards (~3-4 sessions)

12 exemplar designs, 1 per style. These set the quality bar.

**6 evolved from best existing** (strongest current designs, upgraded with game mechanics):
1. `voice_stage` ← lion (add audience reaction, twist challenges)
2. `prediction_lab` ← goldfish (add commit-before-reveal, scoring)
3. `time_traveler` ← banana (add choice points, timeline visualization)
4. `care_station` ← teddy_bear (add visible transformation, relationship arc)
5. `field_experiment` ← playground (add hypothesis-testing, tally)
6. `quest_collector` ← dandelion (add quest criterion, preserve detail harvesting)

**6 entirely new** (styles that have no existing designs):
7. `mystery_lens` — new entity TBD
8. `mystery_trail` — new entity TBD
9. `inventor_workshop` — new entity TBD
10. `mix_lab` — new entity TBD
11. `ensemble_show` — new entity TBD
12. `rescue_team` — new entity TBD

Each gold standard goes through full spec + prod pipeline with new 10-dimension rubric.

### Phase 2: Full Library (~4-6 sessions)

- Rewrite remaining ~19 existing designs into new pillars using gold standards as reference
- Generate ~6 new designs for underrepresented styles
- Target: 2-3 designs per style minimum
- Can parallelize: independent styles can be generated simultaneously

### Phase 3: Cleanup (~1 session)

- Archive old-style design files
- Update HANDOFF.md, assignments.md
- Rebuild concatenated design document
- Final rubric pass on all designs

---

## Verification

After each phase:

1. **Infrastructure (Phase 0)**:
   - Read all 4 updated files and verify consistency
   - Confirm 12 styles are fully defined with creative variables
   - Confirm rubric has 10 dimensions with clear pass/fail criteria

2. **Gold Standards (Phase 1)**:
   - Each design passes all 10 rubric dimensions (D1-D10)
   - D9 test: Does the design have at least one moment of genuine uncertainty + satisfying resolution?
   - D10 test: Could a blind reader identify which pillar this design belongs to?
   - Cross-pillar test: Do 2 designs from different pillars feel genuinely distinct?

3. **Full Library (Phase 2)**:
   - All designs pass 10-dimension rubric
   - Each style has 2-3 designs minimum
   - Entity diversity within each style (different tiers, different entities)

4. **Cleanup (Phase 3)**:
   - No orphaned files from old system
   - All documentation reflects new 12-style system
   - Git history clean

---

## Critical Files

| File | Role |
|------|------|
| `docs/game_styles.md` | Style taxonomy — **rewrite** |
| `templates.md` | Design templates — **rewrite** |
| `program.md` | Agent instructions + rubric — **update** |
| `run.md` | Execution loop — **update** |
| `designs/cat1/` | Cat1 designs — **rewrite all** |
| `designs/cat5/` | Cat5 designs — **rewrite all** |
| `entity_guidance.md` | Entity mapping — **no change** |
| `conversation_bridge.md` | Bridge patterns — **minor update** (add pillar-awareness) |
| `results.tsv` | Experiment log — **reset for new generation** |
| `assignments.md` | Work queue — **rebuild for new assignments** |
