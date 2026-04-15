# Style Recommender: Entity-to-Game Matching System

## Problem

WonderLens has 12 game styles across 6 Experience Pillars, but only a limited number of hand-designed games for specific entities. When a child photographs an entity without a pre-designed game, the system needs to:

1. Select the best game style for that entity
2. Find a compatible existing game to reuse, OR generate a new one from templates
3. Do this for potentially thousands of entities, many without mapping data

The upstream flow: child photographs entity → entity recognition → multi-turn conversation → **game selection happens here** → game plays.

### The 6 Experience Pillars × 12 Styles

Each pillar defines a distinct emotional experience. Each has one Cat1 (indoor/verbal) and one Cat5 (outdoor/collection) style:

| Pillar | Child feels... | Cat1 Style | Cat5 Style |
|---|---|---|---|
| **Mystery** | "I figured it out!" | `mystery_lens` — deduce hidden details from clues | `mystery_trail` — follow riddle-clues, discover hidden pattern |
| **Creation** | "I made this!" | `inventor_workshop` — imagine wild modifications | `mix_lab` — collect ingredients, combine into invention |
| **Performance** | "They loved it!" | `voice_stage` — perform for an audience | `ensemble_show` — assemble a cast, put on a show |
| **Discovery** | "Was I right?!" | `prediction_lab` — commit, reveal, score | `field_experiment` — test a visually-verifiable hypothesis, AI assesses from photos |
| **Adventure** | "Look how far we went!" | `time_traveler` — journey through time | `quest_collector` — quest with criterion + detail-driven story |
| **Nurture** | "I helped!" | `care_station` — help it get better (visible transformation) | `rescue_team` — find things that need help, mutual aid |

### Current Game Inventory

**12 gold standard designs** (1 per style, Phase 1 complete). Gold standard files use `{entity}_cat{N}_gold_spec.md` / `{entity}_cat{N}_gold_prod.md` naming convention to distinguish from legacy designs:

| Style | Entity | Cat | Tier | Activity Name | Files |
|---|---|---|---|---|---|
| `voice_stage` | lion | 1 | T0 | The Lion's Big Show | `lion_cat1_gold_*` |
| `prediction_lab` | goldfish | 1 | T1 | Goldfish Scientist | `goldfish_cat1_gold_*` |
| `time_traveler` | banana | 1 | T1 | The Banana Time Machine | `banana_cat1_gold_*` |
| `care_station` | teddy_bear | 1 | T0 | Teddy's Care Station | `teddy_bear_cat1_gold_*` |
| `field_experiment` | playground | 5 | T1 | The Playground Material Detective | `playground_cat5_gold_*` |
| `quest_collector` | dandelion | 5 | T1 | Dandelion Quest | `dandelion_cat5_gold_*` |
| `mystery_lens` | toy_robot | 1 | T1 | Robot Inspector | `toy_robot_cat1_gold_*` |
| `mystery_trail` | butterfly | 5 | T1 | The Butterfly World Detectives | `butterfly_cat5_gold_*` |
| `inventor_workshop` | rubber_duck | 1 | T0 | Super Duck Workshop | `rubber_duck_cat1_gold_*` |
| `mix_lab` | rock | 5 | T1 | Nature Inventor's Lab | `rock_cat5_gold_*` |
| `ensemble_show` | bird | 5 | T1 | The Nature Orchestra | `bird_cat5_gold_*` |
| `rescue_team` | flower | 5 | T1 | The Garden Rescue Squad | `flower_cat5_gold_*` |

**~25 legacy designs** (from the old 6-style system, pending rewrite into new pillars):

The old system had 6 styles — 4 Cat1, 2 Cat5 — without the Experience Pillar framework:

| Old Style | Cat | → Evolved Into | Pillar | What was added |
|---|---|---|---|---|
| `voice_acting` | 1 | `voice_stage` | Performance | Audience reaction mechanic, surprise twists |
| `storytelling_chain` | 1 | `time_traveler` | Adventure | Time-based progression, choice points, timeline |
| `prediction_game` | 1 | `prediction_lab` | Discovery | Commit-before-reveal, scoring, dramatic reveals |
| `helper_hotline` | 1 | `care_station` | Nurture | Visible transformation, relationship arc |
| `comparison_chart` | 5 | `field_experiment` | Discovery | Pre-collection hypothesis, data tallying |
| `naming_story` | 5 | `quest_collector` | Adventure | Quest criterion, mission progression |

6 entirely new styles were added to fill cognitive gaps: `mystery_lens`, `mystery_trail` (Mystery), `inventor_workshop`, `mix_lab` (Creation), `ensemble_show` (Performance Cat5), `rescue_team` (Nurture Cat5).

Legacy designs pending rewrite:
- Cat1: crayons, raincoat, piano, eye, firefighter, toothbrush_holder, city_library, green_apple, sunflower, stop_sign, bicycle
- Cat5: feather, puddle, sandy_beach, autumn_leaf, pinecone, crayons, double_rainbow, raincoat

Once legacy designs are rewritten (Phase 2), total hand-designed games: ~37. Even then, this covers only ~20 unique entities — a fraction of the thousands a child could photograph. Hence the need for this Recommender.

## Solution: Two-Stage Recommender Pipeline

### Architecture

```
Conversation ends
    ↓
Stage 1: Conversation Analyzer (LLM call)
  Input:  conversation transcript
  Output: structured conversation signals
    ↓
Stage 2: Style Matcher + Game Compatibility + Seed Generator (LLM call)
  Input:  conversation signals + entity data + category + game inventory
  Output: top-3 ranked styles with compatible games + creative seeds
    ↓
Game Selection Logic:
  Tier A: entity has its own gold standard → use it
  Tier B: compatible game exists (score ≥ 0.7) → adapt it
  Tier C: no compatible game → generate from template using seeds
```

### Deployment Modes

**Runtime mode**: Full two-stage pipeline runs after conversation ends (~3-5 seconds, 2 LLM calls). Used for unknown entities not in the pre-computed lookup.

**Batch mode**: Pre-compute entity → game assignments for all known entities using Stage 2 only (no conversation signals). Store in `entity_game_assignments.yaml`. At runtime, instant lookup. Conversation signals can optionally refine the pre-computed ranking.

---

## Stage 1: Conversation Analyzer

**Purpose**: Extract structured signals from the raw conversation transcript that predict which pillar/style will feel most natural as the next activity.

**Input**: Full conversation transcript (5-15 turns of AI + child dialogue)

**Output schema**:

```yaml
conversation_signals:
  # What dimensions of the entity did the child explore?
  dimensions_explored:
    - dimension: "emotions"         # maps to tier_guidance dimension types
      intensity: 0.8                # proportion of turns spent here
      example: "child said lion looks happy"
    - dimension: "function"
      intensity: 0.6
      example: "child asked why lions roar"
    - dimension: "appearance"
      intensity: 0.3
      example: "child noticed the mane"

  # What was the child's engagement pattern?
  engagement_pattern: "cause-and-effect curious"
  # Options: expressive, caring, imaginative, observational, narrative, cause-and-effect curious

  # What emotional tone dominated?
  emotional_tone: "excited and playful"
  # Options: excited/playful, gentle/caring, curious/focused, silly/creative, quiet/reflective

  # Specific topics that could seed game content
  key_topics:
    - "lion's loud roar"
    - "why lions have manes"
    - "lion sounds happy when it's sunny"

  # Pre-computed pillar affinity from conversation patterns
  pillar_signals:
    Performance: 0.7
    Discovery: 0.6
    Mystery: 0.2
    Creation: 0.1
    Adventure: 0.3
    Nurture: 0.1
```

### Pillar Signal Heuristics

How conversation patterns map to pillar affinity:

| Conversation pattern | Pillar signal |
|---|---|
| Child made sounds, performed, expressed emotions vocally | Performance ↑ |
| Child asked "why?" or "what happens if?" questions | Discovery ↑ |
| Child observed fine details, described specific features | Mystery ↑ |
| Child said "what if it could..." or imagined changes | Creation ↑ |
| Child discussed journeys, sequences, before/after | Adventure ↑ |
| Child expressed concern, wanted to help or care for entity | Nurture ↑ |

### Stage 1 Prompt Location

`prompts/stage1_conversation_analyzer.md`

---

## Stage 2: Style Matcher + Game Compatibility + Seed Generator

**Purpose**: Rank the 6 eligible styles (constrained by category), check compatibility with existing games, generate creative variable seeds.

**Input**:
- Stage 1 conversation signals (if available; omitted in batch mode)
- Entity mapping YAML (if available) OR entity name only
- Category constraint: Cat1 (6 styles) or Cat5 (6 styles)
- Game inventory: list of all existing gold-standard games with their entities, styles, and key affordances

**Output schema**:

```yaml
entity: "cat"
category: 1
tier: "T1"

recommendations:
  - rank: 1
    pillar: "Performance"
    style: "voice_stage"
    confidence: 0.85
    reasoning: "Cat has rich vocal personality, child was expressive in conversation"

    compatible_game:
      exists: true
      source_entity: "lion"
      source_game: "The Lion's Big Show"
      compatibility_score: 0.82
      adaptation_notes: "Replace 'roar' with cat sounds (meow, purr, hiss). Keep talent show framing and judge characters. Change 'jungle' to 'neighborhood'."

    seeds:
      metaphor: "Kitty's Got Talent — cat auditions for the neighborhood talent show"
      role_title: "Purr Star"
      scenarios:
        - "Happy purr in a sunny spot"
        - "Sleepy stretch purr on the couch"
        - "Surprised MEOW at a cucumber (twist challenge)"
      magic_moment: "Three neighborhood judges (dog, hamster, parrot) leap to their feet"

  - rank: 2
    pillar: "Mystery"
    style: "mystery_lens"
    confidence: 0.65
    compatible_game:
      exists: true
      source_entity: "toy_robot"
      compatibility_score: 0.55
      adaptation_notes: "Robot parts → cat features (whiskers, paw pads, ear tufts). Weaker fit."
    seeds:
      metaphor: "Cat Inspector — spot the hidden feature"
      role_title: "Whisker Detective"
      scenarios:
        - "Something soft and thin near the mouth (whiskers)"
        - "Something round that changes size (pupils)"
        - "Something hidden between the toes (retractable claws)"

  - rank: 3
    pillar: "Nurture"
    style: "care_station"
    confidence: 0.40
    compatible_game:
      exists: true
      source_entity: "teddy_bear"
      compatibility_score: 0.72
      adaptation_notes: "Replace 'teddy' with cat. Care needs transfer well (cold, scared, lonely)."
    seeds:
      metaphor: "Kitty Care Clinic — your cat needs help"
      role_title: "Cat Carer"
      scenarios:
        - "Cat is cold and shivering (needs warmth)"
        - "Cat heard a loud noise and is hiding (needs comfort)"
        - "Cat is bored AND hungry AND lonely (complex)"
```

### Game Compatibility Scoring

The LLM evaluates compatibility using these factors:

| Factor | Weight | What it measures |
|---|---|---|
| **Affordance match** | Critical | Can the entity DO what the game mechanic requires? (voice_stage needs sounds, mystery_lens needs observable details, field_experiment needs visually-verifiable properties) |
| **Domain similarity** | High | Same type of entity? (animal↔animal: high, animal↔object: low) |
| **Scenario transferability** | Medium | Do the game's round scenarios make sense for this entity? |
| **Tone match** | Low | Does the entity's emotional register fit the game's arc? |

**Compatibility thresholds:**
- **≥ 0.7**: Reuse game with minor adaptation → **Tier B**
- **0.5-0.7**: Reuse possible but template generation may produce better results
- **< 0.5**: Don't reuse → **Tier C** (generate from template)

### Stage 2 Prompt Location

`prompts/stage2_style_matcher.md`

---

## Game Selection (Updated — see also `2026-04-08-entity-bridging.md`)

```
Entity photographed
    ↓
Entity in IB mind map?
    ├── YES → Has pre-designed game for this exact entity + best style?
    │         ├── YES → Tier A: Use gold standard directly (10/10 quality)
    │         └── NO  → Run Recommender (or lookup pre-computed assignment)
    │                   ↓
    │              Top style has compatible game (score ≥ 0.7)?
    │                   ├── YES → Tier B: Adapt existing game (8/10 quality)
    │                   └── NO  → Tier P: Property-bridge template (7-8/10)
    │
    └── NO  → Entity Bridging System (see 2026-04-08-entity-bridging.md)
              ├── Layer 1: Constellation match → Bridge in conversation → Tier A/B
              ├── Layer 2: Property bridge → Attribute-driven game (Tier P)
              └── Layer 3: No match → Conversation-only mode (no game)
```

> **Note**: Tier C (template generation, 6-7/10) has been replaced. Unmapped entities without constellation or property bridges get a rich conversation-only experience instead of a mediocre generated game. See `2026-04-08-entity-bridging.md` for the full Entity Bridging design.

### Tier B: Game Adaptation

When reusing a gold-standard game with a different entity:
- The game's STRUCTURE stays (steps, mechanics, scoring, magic moment)
- The ENTITY references change (name, photo, entity-specific dialogue)
- The SCENARIOS may need light adaptation per `adaptation_notes`
- The adaptation is done by the LLM at game-play time using the adaptation notes as guidance

### Tier C: Template Generation

When no compatible game exists:
- The template system (templates.md) generates a fresh game
- Creative variable seeds from the Recommender dramatically improve quality
- Seeds include: metaphor, role_title, scenarios, magic_moment — the hardest parts to invent from scratch

---

## Batch Pre-computation

### Purpose

Pre-compute entity → game assignments for all known entities so runtime is instant lookup instead of LLM call.

### Process

```
For each entity in IB mapping database:
  1. Run Stage 2 WITHOUT conversation signals (entity data only)
  2. Score compatibility with all existing gold-standard games
  3. Compute per-category recommendations (Cat1 top-3 + Cat5 top-3)
  4. Store in entity_game_assignments.yaml
```

### Output: entity_game_assignments.yaml

```yaml
animals_cat:
  entity_name: "Cat"
  category_1:
    - style: voice_stage
      pillar: Performance
      confidence: 0.88
      compatible_game: { source: lion, game: "The Lion's Big Show", score: 0.82 }
      seeds: { metaphor: "Kitty's Got Talent", role_title: "Purr Star", ... }
    - style: mystery_lens
      pillar: Mystery
      confidence: 0.65
      compatible_game: null
      seeds: { metaphor: "Cat Inspector", role_title: "Whisker Detective", ... }
    - style: care_station
      pillar: Nurture
      confidence: 0.40
      compatible_game: { source: teddy_bear, game: "Teddy's Care Station", score: 0.72 }
      seeds: { metaphor: "Kitty Care Clinic", role_title: "Cat Carer", ... }
  category_5:
    - style: ensemble_show
      pillar: Performance
      confidence: 0.75
      compatible_game: { source: bird, game: "The Nature Orchestra", score: 0.68 }
      seeds: { ... }
    - ...
```

### IB-Based Entity Clustering

For efficient batch processing and handling new entities, group entities by shared IB attributes:

| Cluster | Shared IB traits | Default pillar fit | Compatible games |
|---|---|---|---|
| Sound-making animals | Function=vocalization, emotions=rich | Performance | lion/voice_stage, bird/ensemble_show |
| Growing/changing things | Change=high, lifecycle present | Adventure | banana/time_traveler, dandelion/quest_collector |
| Complex objects with parts | Structure=rich, Form=high | Mystery | toy_robot/mystery_lens |
| Living things needing care | Responsibility=high, Connection=high | Nurture | teddy_bear/care_station, flower/rescue_team |
| Things with visually-distinct properties | Form=varied, visual properties=rich | Creation/Discovery | rock/mix_lab, playground/field_experiment |
| Things with hidden patterns | Causation=high, structure=varied | Mystery/Discovery | butterfly/mystery_trail |

When a new entity arrives without pre-computed data:
1. Determine its IB cluster from available attributes
2. Use the cluster's default pillar/style as a fast fallback
3. Optionally run full two-stage pipeline for higher accuracy

### Style-Specific Constraints

**`field_experiment` visual verification constraint**: Hypotheses must use properties the AI can reliably assess from a photo. Allowed: color, shape, material type, size, count, alive/not-alive, category membership. Banned: texture, weight, temperature, sound, smell, flexibility. The AI is the property assessor (announces what it sees in the photo) — the child does NOT self-report. This preserves the "Was I right?!" surprise. Stage 2 must generate `{hypothesis}` seeds that comply with this constraint.

---

## Deployment Timing

The pipeline supports three deployment timings without design changes. Stage 1 (conversation signals) is an OPTIONAL input to Stage 2 — when absent, Stage 2 uses entity data alone.

### Three Timing Points

| Timing | What's available | How it works | Quality |
|---|---|---|---|
| **At photo time** | Entity ID + mapping only | Stage 2 only — identical to batch pre-computation. Look up `entity_game_assignments.yaml` or run Stage 2 with no conversation signals. | Good (entity fit only) |
| **During conversation** | Partial transcript + entity data | Stage 1 runs incrementally on partial transcript, `pillar_signals` update each turn. Stage 2 can run in background with latest signals. | Better (progressive) |
| **After conversation** | Full transcript + entity data | Full pipeline. Best signal quality. | Best |

### Progressive Mode (During Conversation)

The Recommender can run Stage 1 incrementally as the conversation progresses:

```
Turn 1: child says "wow, big cat!"
  → pillar_signals: { Performance: 0.3, Mystery: 0.2, ... }
  → tentative recommendation: Performance/voice_stage (low confidence)

Turn 5: child makes roaring sounds, asks "can lions whisper?"
  → pillar_signals: { Performance: 0.8, Discovery: 0.4, ... }
  → recommendation solidifies: Performance/voice_stage (high confidence)

Turn 10: conversation ends
  → final pillar_signals: { Performance: 0.7, Discovery: 0.6, ... }
  → recommendation ready instantly — zero latency at transition
```

**Benefits of progressive mode:**
1. **Zero latency at transition** — recommendation is pre-computed by the time conversation ends
2. **Conversation shaping** — if the system is 80% confident the child will get a Discovery game, the conversation can subtly explore more cause-effect dimensions, making the game transition feel more natural
3. **Asset pre-loading** — the likely game's assets (animations, sounds) can begin loading before the game starts

**Risk mitigation**: Don't commit to a game until conversation ends. Progressive signals are tentative — they narrow candidates but the final selection waits for complete data.

### Scoring Across Timing Points

The `final_score` formula adapts to available signal:

```
final_score = (entity_confidence × entity_weight) + (conversation_pillar_signal × conversation_weight)
```

| Timing | entity_weight | conversation_weight | Rationale |
|---|---|---|---|
| At photo time | 1.0 | 0.0 | No conversation yet |
| Mid-conversation | 0.5 | 0.5 | Partial signal from both |
| After conversation | 0.4 | 0.6 | Full conversation is the stronger signal |

Conversation context gets higher weight at completion because it reflects what THIS child was interested in RIGHT NOW — the same entity can lead to different games depending on the child's engagement.

---

## Runtime Flow Summary

```
Entity recognized → Check entity_game_assignments.yaml
    │
    ├── FOUND (known entity):
    │   Get pre-computed top-3 styles (entity-only ranking)
    │   Start progressive refinement during conversation (optional)
    │   At transition: apply final conversation signals to refine ranking
    │   Apply three-tier selection (A → B → C)
    │
    └── NOT FOUND (unknown entity):
        Run Stage 1 (conversation analyzer) — progressively or at end
        Run Stage 2 (style matcher + compatibility + seeds)
        Apply three-tier selection (A → B → C)
        Optionally: save result to assignments for next time
```

### Conversation Signal Refinement

When pre-computed assignments exist, conversation signals can REFINE the ranking:

```
Pre-computed for cat: #1 Performance (0.88), #2 Mystery (0.65), #3 Nurture (0.40)
Conversation signals: child was caring, worried about the cat → Nurture ↑↑

Refined ranking: #1 Nurture (0.72), #2 Performance (0.70), #3 Mystery (0.55)
→ Cat gets care_station game instead of voice_stage
```

The refinement uses the timing-appropriate weights (see Scoring Across Timing Points above). Conversation context gets higher weight because it reflects what THIS child was interested in RIGHT NOW.

---

## Implementation Artifacts

| Artifact | Purpose | Location |
|---|---|---|
| `prompts/stage1_conversation_analyzer.md` | Stage 1 LLM prompt | New file |
| `prompts/stage2_style_matcher.md` | Stage 2 LLM prompt | New file |
| `style_recommender.md` | Run instructions for the pipeline | New file |
| `entity_game_assignments.yaml` | Pre-computed assignments (output of batch mode) | Generated |
| `game_inventory.md` | Catalog of all existing games with compatibility metadata | Auto-generated from designs/ |

### game_inventory.md Structure

Auto-generated from existing gold-standard designs:

```yaml
games:
  - entity: lion
    category: 1
    pillar: Performance
    style: voice_stage
    game_name: "The Lion's Big Show"
    design_files: ["lion_cat1_gold_spec.md", "lion_cat1_gold_prod.md"]
    key_affordances: ["makes sounds", "has personality", "can perform"]
    domain: animals
    tier: T0
    ib_concepts: [Perspective, Form]

  - entity: goldfish
    category: 1
    pillar: Discovery
    style: prediction_lab
    design_files: ["goldfish_cat1_gold_spec.md", "goldfish_cat1_gold_prod.md"]
    ...
```

This inventory is what Stage 2 uses to evaluate game compatibility.

---

## Verification

### Stage 1 Accuracy

Test with 10+ conversation transcripts:
- Do extracted `dimensions_explored` match what a human would identify?
- Do `pillar_signals` correlate with which game style a human would recommend?
- Are `key_topics` specific enough to seed creative variables?

### Stage 2 Accuracy

Test with 20+ entities (mix of mapped and unmapped):
- Does the top-ranked style match human expert judgment?
- Are compatibility scores reasonable? (high for same-domain, low for cross-domain)
- Are creative seeds entity-specific (not generic)?
- Do adaptation notes actually work when applied to the source game?

### End-to-End

For 5+ entities without gold-standard games:
- Run full pipeline
- Apply Tier B (adapted game) or Tier C (template generation)
- Evaluate: does the resulting game feel natural for this entity?
- Compare: Tier B adapted game vs. Tier C generated game — which is better?

### Batch Mode

Run batch for all 20 mapped entities:
- Verify all get reasonable assignments
- Spot-check: do entities in the same IB cluster get similar assignments?
- Check coverage: are all 12 game styles represented in the assignments?

---

## Critical Files

| File | Role |
|---|---|
| `docs/game_styles.md` | Style definitions — Stage 2 reads this |
| `templates.md` | Templates for Tier C generation |
| `program.md` | Design format + rubric for quality evaluation |
| `entity_guidance.md` | How to read entity mapping YAMLs |
| `data/mappings_dev20_0318/` | Entity mapping YAML files |
| `designs/cat1/`, `designs/cat5/` | Gold-standard games (game inventory source) |
