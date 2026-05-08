# Activity Tag Block 与 Progression Guide

**Version:** 0.1 - 2026-04-30
**Status:** Supplement reference
**English version:** `docs/activity_tag_block_progression_guide.md`
**主要参考:** `activities/_schema/tag_block.schema.json`, `docs/activity_vocabulary.md`, `docs/progression_axes.md`, `docs/activity_tag_block_usage.md`, `docs/superpowers/specs/2026-04-24-progression-algorithm-design.md`

这份文档是给中文读者看的 tag block 总览。它不是英文版的逐字翻译，而是按中文阅读习惯重新组织说明。字段名、enum、runtime action、系统模块名保留 English，例如 `activity_signature`, `matchability`, `progression`, `axis_state`, `promote`, `hold`。

---

## 1. 先建立一个整体模型

`tag_block.yaml` 描述的是一个 activity package。这个 activity 以后可以被很多孩子、在很多 session 中玩到，但 tag block 本身是 catalog-time 的静态声明。

运行时会基于这个声明生成 session event：

1. **upstream matcher** 在活动开始前读取 tag block，先判断这个 activity 能不能用于当前照片、entity、tier，再判断它是不是当前 conversation 的自然延续。
2. **runtime activity layer** 把 `{entity}`、`{color}`、`{matched_color}` 这类 placeholder 渲染成实际文案。
3. **progression engine** 根据 activity 声明的 `progression.topic_axis` 和 `progression.difficulty_level`，再结合孩子的真实表现，更新每个 child、每条 axis 上的 progression state。
4. **downstream surfaces** 读取的是完成后的 session event。child recap 关注孩子做了什么；parent growth path 聚合一段时间里的多个 activity events。

可以把 tag block 按使用方理解：

| Layer | 它回答的问题 | 主要字段 |
|---|---|---|
| Upstream eligibility | 这个 activity 能不能用于当前 photo 和 child tier? | `entity`, `entity_class`, `entity_binding`, `tier_range`, `matchability.*` |
| Upstream coherence | 如果能用，它是不是 conversation 的好延续? | `activity_signature.observation_angle`, `bridge_prerequisites`, `entity_role`, progression target |
| Runtime presentation | 开始活动时要展示什么文案? | `activity_signature.focal_attribute`, `intro`, `preview_label`, `preview_prompt` |
| Progression | 这个 activity 正式练的是哪条 axis / 哪个 rung? 结束后如何更新? | `progression.*`, evidence vector, `axis_state`, `progression_event` |
| Downstream child | 孩子刚才做了什么? | resolved `entity`, `activity_signature.*`, recap template output |
| Downstream parent | 一段时间里出现了什么成长模式? | aggregated `progression.*`, `key_concepts`, `atl_skills`, `activity_signature.*`, `caregiver_role` |

---

## 2. 完整 Tag Block 结构

下面是 migrated activity package 当前使用的完整形态。必填字段由 `activities/_schema/tag_block.schema.json` 约束；部分 optional 字段也放在例子里，因为现有活动已经在使用。

```yaml
activity_id: color_scout_property
version: 1
source_entity_exemplar: ladybug
template_type: cat5
pillar: Adventure
game_style: quest_collector

entity: "{parameterized_by_matched_property}"
entity_class: []
entity_binding: parameterized
tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: "±1"

category: objects
attributes: []

key_concepts: [Form, Connection]
related_concepts: [pattern, similarity, observation, identity]
atl_skills: [observation, classification]
transdisciplinary_theme: How_We_Express_Ourselves
subject_tags: [science]

kud:
  know: ["the focal color appears on many kinds of things"]
  understand: ["color is a property we can use to group things"]
  do: ["find 3 things that share the focal color", "turn the color finds into a team adventure"]

progression:
  topic_axis: form
  difficulty_level: 2
  next_step_hint: "Next time, notice another attribute alongside color"
  reward_hook: "Earned the Color Scout badge"

caregiver_role: [scaffold, co-explorer]

activity_signature:
  observation_angle: color
  mechanic: collect
  entity_role: exemplar
  bridge_prerequisites:
    primary: [color]
    secondary: [pattern, visibility]
  focal_attribute: "{matched_color}"
  intro: "The child finds three {color} things using the photographed {entity} as a starting example."
  preview_label: "Find three {color} things!"
  preview_prompt: "You noticed the {color} of the {entity}. Let's go find more {color} things together."
  role_pivot_note: |
    The {entity} was our subject during the chat; now it becomes an
    example of {color}: we are going to find more {color} things.

matchability:
  entity_class_filter: []
  tier_support:
    T0: true
    T1: true
    T2: true
```

### 2.1 必填 Top-Level Fields

| Field | Required | 用法 |
|---|---:|---|
| `activity_id` | yes | lowercase snake_case，并且必须和 package directory 名一致。 |
| `version` | yes | activity package 的整数版本。package contract 变化时递增。 |
| `template_type` | yes | `cat1` 或 `cat5`。runtime/template 会读取。 |
| `pillar` | yes | 活动的情感和体验 pillar：`Discovery`, `Performance`, `Mystery`, `Creation`, `Adventure`, `Connection`。 |
| `game_style` | yes | 更具体的活动形式，例如 `field_experiment`, `voice_stage`, `mystery_trail`。 |
| `entity` | yes | bound activity 写具体 entity；parameterized activity 可以写 placeholder。 |
| `entity_binding` | yes | `bound`, `parameterized`, `agnostic`。说明 activity 和 entity 绑定得有多紧。 |
| `tier_range` | yes | 作者设计时的目标 tier，以及可以安全支持的 tier 范围。 |
| `key_concepts` | yes | 这个 activity 明显涉及的 IB key concepts。 |
| `progression` | yes | 这个 activity 正式更新哪条 axis / 哪个 rung。 |
| `caregiver_role` | yes | 预期 adult support 角色。 |
| `activity_signature` | yes | conversation-to-activity coherence 和 presentation metadata。 |
| `matchability` | yes | 顶层 matcher eligibility 过滤条件。它是 `activity_signature` 的 sibling，不在 `activity_signature` 里面。 |

### 2.2 常见 Optional Fields

| Field | 用法 |
|---|---|
| `source_entity_exemplar` | parameterized package 的示例 entity，方便作者和 reviewer 理解。 |
| `entity_class` | 从具体到抽象的 class chain。只有 runtime 会填充的 wide parameterized activity 才应该留空。 |
| `category` | runtime/entity category 或 legacy grouping。 |
| `attributes` | activity 相关的 entity attributes。parameterized activity 通常 runtime 填。 |
| `related_concepts` | child-facing 或 curriculum-adjacent concept labels。 |
| `atl_skills` | WonderLens thinking/learning tags，例如 `observation`, `classification`, `counting`, `logic`, `communication`。 |
| `transdisciplinary_theme` | PYP theme token。 |
| `subject_tags` | curriculum domain tags，例如 `math`, `science`, `language`。 |
| `kud` | authoring audit：孩子应该 know / understand / do 什么。 |

---

## 3. Upstream Usage

upstream selection 分两层：先看 **eligibility**，再看 **coherence / ranking**。

### 3.1 Eligibility: Can It Run?

eligibility 字段是 top-level matcher inputs。它们要稳定、可机器读取。

| Field | 用法 | 例子 |
|---|---|---|
| `entity` | nominal entity 或 placeholder。 | `lion`, `{parameterized_by_matched_property}` |
| `entity_class` | exact entity 没命中时，matcher 可以往更大的 class roll up。 | `[lion, big_cat, mammal, animal]` |
| `entity_binding` | activity 对具体 entity 的依赖程度。 | `bound`, `parameterized`, `agnostic` |
| `tier_range.primary` | activity 作者主要按哪个 tier 写。 | `T1` |
| `tier_range.span` | activity 可以安全支持哪些 tiers。 | `[T0, T1, T2]` |
| `tier_range.elasticity` | tier 伸缩规则，给 reviewer 看。 | `"±1"`, `neighbor`, `strict`, `broad` |
| `matchability.entity_class_filter` | 额外 class allowlist。空数组表示 wide。 | `[]`, `[big_cat]`, `[insect, patterned_thing]` |
| `matchability.tier_support` | tier boolean matrix，应和 `tier_range.span` 一致。 | `{T0: true, T1: true, T2: true}` |

`matchability` 是 tag block 的顶层 section，不属于 `activity_signature`。

一个 activity 进入 eligible candidate set，需要通过这些 hard filters：

1. tag block valid，activity 在 active catalog 里。
2. child runtime tier 在 `tier_range.span` 里。
3. `matchability.tier_support[child_tier]` 是 `true`。
4. photo 检测到的 entity 满足 `entity_binding` 的规则。
5. photo 检测到的 entity 通过 `matchability.entity_class_filter`。filter 为空表示 wide。
6. 必要 runtime properties 可以解析出来。比如 parameterized property activity 需要能拿到 color、shape、material、pattern、quantity 等值。
7. safety 和 runtime availability checks 通过。

eligibility 只表示“可以进入候选集”。它不表示一定会被选中。最终选择还要看 conversation coherence、progression target、freshness、catalog coverage 等 signals。

### 3.1.1 不同 Binding 的 Eligibility

| Binding | 什么时候 eligible | 常见 `entity_class_filter` | 例子 |
|---|---|---|---|
| `bound` | activity 依赖具体 entity 或很窄的 entity family。除非文案已经安全 parameterized，否则优先 exact entity。 | 窄范围：`[big_cat]`, `[butterfly]`, `[ladybug]` | lion voice activity 只有在 big-cat context 下才应该进候选。 |
| `parameterized` | entity 是 slot，关键是它能提供 activity 需要的 property/value。 | universal property hunt 可用 `[]`；需要特定 class 时用 `[animal]`, `[plant]`, `[patterned_thing]`。 | Color Scout 可以用于 red pen、red ladybug、red toy，只要 `{matched_color}` 能解析。 |
| `agnostic` | entity 只是注意力锚点，activity 本身是通用 thinking move。 | 通常 `[]` 或 `[observable_thing]`。如果需要更窄 filter，说明它可能并不是真正 agnostic。 | “name three things you notice” warm-up 可以用于几乎任何安全可识别照片。 |

如果 legacy authoring 里还有 `entity_attributes_covered`，沿用 `program.md` 的 overlap rule：`bound` 用 strict attribute resolution；`parameterized` 用 loose overlap，只要某个 required property 能匹配并填入 runtime parameter 即可。

### 3.1.2 Eligibility Examples

#### Bound: 窄 entity/family

```yaml
entity: lion
entity_binding: bound
entity_class: [big_cat, mammal, animal]
tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: "±1"
matchability:
  entity_class_filter: [big_cat]
  tier_support: {T0: true, T1: true, T2: true}
```

Eligible for: lion，或者文案已经能安全适配的其他 big-cat context。

Not eligible for: dog、beetle、toy car，或者 class chain 和 `[big_cat]` 没交集的照片。

#### Parameterized: wide property bridge

```yaml
entity: "{parameterized_by_matched_property}"
entity_binding: parameterized
entity_class: []
tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: "±1"
activity_signature:
  observation_angle: color
  focal_attribute: "{matched_color}"
matchability:
  entity_class_filter: []
  tier_support: {T0: true, T1: true, T2: true}
```

Eligible for: 任何安全照片，只要 entity 有可靠可用的 color value。

Not eligible for: 没法可靠提取 color/property 的照片，或者 runtime context 不允许移动/search activity 的场景。

#### Parameterized: restricted property bridge

```yaml
entity: "{parameterized_by_matched_property}"
entity_binding: parameterized
entity_class: []
activity_signature:
  observation_angle: pattern
  focal_attribute: "{matched_pattern}"
matchability:
  entity_class_filter: [patterned_thing]
  tier_support: {T0: true, T1: true, T2: true}
```

Eligible for: ladybug、striped shirt、spotted ball，或者 class chain 包含 `patterned_thing` 且 pattern 可解析的 entity。

Not eligible for: plain object，即使 child tier 匹配，也不应该进这个 activity。

#### Agnostic: any safe observable thing

```yaml
entity: any
entity_class: [observable_thing]
entity_binding: agnostic
tier_range:
  primary: T1
  span: [T0, T1, T2]
  elasticity: broad
activity_signature:
  observation_angle: state
  focal_attribute: "{observed_detail}"
matchability:
  entity_class_filter: []
  tier_support: {T0: true, T1: true, T2: true}
```

Eligible for: 几乎任何安全、可识别照片，因为这个 activity 练的是通用 thinking move。

Not eligible for: unsafe/unclear photos，或者脚本其实偷偷依赖具体 property 的活动。只要脚本需要 color、shape、living thing、animal 等条件，它就不是真正 agnostic。

### 3.2 Coherence: Should It Follow?

coherence 字段主要在 `activity_signature` 里。它们帮助 selector 在 eligible candidates 里排序。

| Field | 用法 | 例子 |
|---|---|---|
| `activity_signature.observation_angle` | activity 关注的主要 attribute/dimension。 | `color`, `quantity`, `emotion` |
| `activity_signature.bridge_prerequisites.primary` | 1-3 个最自然衔接的 conversation angles。 | `[color]`, `[behavior, function]` |
| `activity_signature.bridge_prerequisites.secondary` | 辅助 angles 或 editorial descriptors。优先用 enum。 | `[pattern, visibility]` |
| `activity_signature.entity_role` | 照片里的 entity 在 activity 中扮演什么角色。 | `subject`, `exemplar`, `catalyst`, `reference` |
| `activity_signature.role_pivot_note` | 如果从 subject pivot 到 exemplar/catalyst/reference，用一句话说明。 | "The pen becomes one example of red." |

selector scoring 的基本思路：

| Match | Selector effect |
|---|---|
| candidate `observation_angle` 等于 conversation `dominant_angle` | strong bonus |
| candidate `observation_angle` 出现在 conversation `secondary_angles` | smaller bonus |
| candidate `bridge_prerequisites.primary` 和 conversation angles 有 overlap | continuity bonus |
| candidate 匹配 progression state 的 target axis/rung | progression bonus |

progression target 是强偏好，不是 hard promise。photo context、catalog coverage、safety、tier、entity eligibility 都可能让 selector 选择别的 activity。

### 3.3 `conversation_signature` 和 `progression_target` 从哪里来

upstream selector 在打分前会收到两个不同的 runtime inputs：

| Runtime input | Owner | 如何产生 | 用途 |
|---|---|---|---|
| `conversation_signature` | Conversation/photo understanding layer | 来自当前 photo、detected entity/properties 和最近几轮 chat。V1 用 keyword/attribute heuristics：统计 angle hits，例如 red/blue → `color`，round/square → `shape`，more/three → `quantity`；命中最多的是 `dominant_angle`，其他明显命中进入 `secondary_angles`。 | 和 `activity_signature.observation_angle`、`bridge_prerequisites` 做 coherence scoring。 |
| `progression_target` | Progression service | 从 child 已存的 per-axis `axis_state`，加上最近的 `progression_event` / policy output 推出。通常包含 preferred next `target_axis` 和 `target_rung`；如果到 L3 ceiling 或持续 overload，可能指向 sibling axis。 | 给 activity ranking 加 progression bonus。 |

最小 runtime flow：

```text
photo + recent chat
  -> entity/properties + conversation_signature

child_id + stored axis_state + latest progression_event
  -> progression_target

conversation_signature + progression_target + active tag blocks
  -> activity selector
```

这两个 input 都可能为空。`conversation_signature` 为 null 时，selector 不加 conversation-angle bonus。`progression_target` 为 null 时，selector 不加 progression bonus，退回 eligibility、coherence、freshness、product policy 等信号。

### 3.4 Upstream Example

孩子拍了一支 red pen。conversation signature 可能是：

```yaml
conversation_signature:
  entity: pen
  dominant_angle: color
  secondary_angles: [shape, function]
  child_tier: T1
progression_target:
  axis: form
  rung: 2
```

`color_scout_property` 会是强匹配：

```yaml
entity_binding: parameterized
matchability:
  entity_class_filter: []
  tier_support: {T0: true, T1: true, T2: true}
activity_signature:
  observation_angle: color
  bridge_prerequisites:
    primary: [color]
  entity_role: exemplar
progression:
  topic_axis: form
  difficulty_level: 2
```

为什么它成立：

- eligibility passes，因为它是 wide parameterized activity。
- conversation coherence passes，因为 dominant angle 是 `color`。
- progression fit passes，因为 target 是 `form` L2。
- `entity_role: exemplar`，pen 不是整个活动的 subject，而是 red 这个 property 的一个例子。

---

## 4. Runtime Presentation Usage

runtime presentation 字段是作者写好的 templates。等 runtime 拿到真实 entity/property 后，再把 placeholder 渲染出来。

| Field | Runtime use |
|---|---|
| `activity_signature.focal_attribute` | 当前活动关注的具体 attribute 或 placeholder，例如 `{matched_color}`, `lion_voice`, `more_less`。 |
| `activity_signature.intro` | observer-facing 的一句话说明，用于 preview、logs、recap payload、parent timeline card。 |
| `activity_signature.preview_label` | 短 activity card / button label。 |
| `activity_signature.preview_prompt` | 从 conversation 转入 activity 的过渡文案。 |
| `activity_signature.role_pivot_note` | 当 entity 从 subject 变成 exemplar/catalyst/reference 时，用于解释 pivot。 |

渲染前：

```yaml
preview_label: "Find three {color} things!"
preview_prompt: "You noticed the {color} of the {entity}. Let's go find more {color} things together."
```

渲染后：

```yaml
preview_label: "Find three red things!"
preview_prompt: "You noticed the red of the pen. Let's go find more red things together."
```

runtime 不应该编造无法从照片或孩子回答中确认的事实。对于 smell、taste、sound、temperature 这类 photo-limited 属性，必须用 child-confirmed phrasing，或者避免直接声称。

---

## 5. Tag Block 里的 Progression Declaration

`progression` block 说明这个 activity 正式练哪一条 axis、哪个 rung。

```yaml
progression:
  topic_axis: form
  difficulty_level: 2
  next_step_hint: "Next time, notice another attribute alongside color"
  reward_hook: "Earned the Color Scout badge"
```

| Field | 含义 |
|---|---|
| `topic_axis` | 7 条 axis 之一：`form`, `function`, `causation`, `change`, `connection`, `perspective`, `responsibility`。 |
| `difficulty_level` | rung，整数 `1`, `2`, `3`。tag block 不写 `L1`/`L2`/`L3`。 |
| `next_step_hint` | 建议的下一步方向。不是对下一次 selected activity 的保证。 |
| `reward_hook` | optional reward/badge copy 或 achievement label。 |

`progression.topic_axis` 和 `activity_signature.observation_angle` 是 orthogonal：

```yaml
activity_signature:
  observation_angle: quantity
progression:
  topic_axis: form
```

意思是：孩子通过 quantity evidence 练了 Form。它不会产生一个单独的 `form/quantity` level。孩子仍然只有一个 Form state；parent dashboard 可以在这个 state 的 evidence 下按 angle 拆分。

常见组合：

| Observation angle | Possible axis | Example |
|---|---|---|
| `quantity` | `form` | 数一数有几个 objects 或 parts。 |
| `quantity` | `causation` | 追问为什么一组更多。 |
| `emotion` | `perspective` | 推测不同角色可能的 feeling。 |
| `function` | `responsibility` | 观察某个 object/living thing 需要怎样的 care。 |
| `pattern` | `connection` | 在不同东西之间找 shared patterns。 |

---

## 6. Progression Algorithm

progression algorithm 不只是 tag block 里的 `progression` block。它是 runtime 在看到孩子表现后，用来更新 per-child state 的策略。

V1 模型来自 `docs/superpowers/specs/2026-04-24-progression-algorithm-design.md`：

1. 把每一轮 response 转成 evidence vector。
2. 更新 per-child、per-axis、per-rung score state。
3. 应用 hard pedagogical guardrails。
4. 用可解释的 action policy 输出 action。
5. 对外仍然只发 runtime 已经理解的 action types。

### 6.1 Evidence Vector

每一轮不应该只给 pass/fail，而应该记录更细的 evidence。

```yaml
evidence:
  correctness: 0.85
  correctness_confidence: 0.72
  spontaneity: 0.40
  latency_bucket: long_wait
  latency_confidence: 1.0
  hint_level: multiple_choice
  hint_confidence: 1.0
  language_depth: name
  language_depth_confidence: 0.68
  on_topic_persistence: 0.90
  prompt_repetition: false
  off_topic: false
  affect_energy: hesitant
```

核心字段怎么看：

| Evidence field | 为什么重要 |
|---|---|
| `correctness` | 回答是否满足当前 rung 目标。 |
| `spontaneity` | 孩子是否独立回答，而不是靠大量 support。 |
| `latency_bucket` | 区分正常思考时间、processing overload、no attempt。 |
| `hint_level` | 避免把 scaffolded correctness 过早当作 mastery。 |
| `language_depth` | 把孩子语言映射到 L1 name、L2 extend、L3 reason。 |
| `on_topic_persistence` | 保护 engaged struggle，不把努力中的困难误判为 failure。 |
| `prompt_repetition` / `off_topic` | 可能表示任务没有处理进去或已经 overload。 |
| `affect_energy` | V1 只做 advisory，不单独触发 `promote` 或 `demote`。 |

### 6.2 Evidence Reliability

engine 应该更信任 runtime-owned facts，而不是软性 classifier guess。

| Reliability tier | Examples | V1 usage |
|---|---|---|
| Hard telemetry | wait time、hint count、prompt count、runtime 记录的 support move | 可以直接使用。 |
| Structured interaction facts | selected option、completed count、tapped target | 简单验证后使用。 |
| Shallow language classification | correctness、off-topic、prompt repetition、language depth | 必须带 confidence 和 reason codes。 |
| Affect/energy | tired、hesitant、frustrated、playful | 只做 advisory，等验证后再扩大用途。 |

low-confidence positive evidence 可以支持 `hold` 或 internal `promote_ready`，但不应该单独触发 `promote`。low-confidence negative evidence 可以稍微提高 `support_needed`，但不应该单独触发 `demote`。

### 6.3 Axis State

progression state 是 per child、per axis 的，不是一个 global child level。

```yaml
axis_state:
  axis: form
  current_rung: 2
  mastery:
    l1: 0.92
    l2: 0.71
    l3: 0.28
  engagement: 0.84
  support_needed: 0.31
  stability: 0.76
  novelty_readiness: 0.68
  recent_events:
    - hold
    - soft_reframe
    - promote_ready_internal
  policy_version: evidence_v1_default
```

| Score | 高值表示 |
|---|---|
| `mastery[rung]` | 孩子能处理这条 axis 上的这个 rung。 |
| `engagement` | 孩子还在参与，并且情绪上可以继续。 |
| `support_needed` | 需要更多 scaffolding；如果持续偏高，才考虑 hold/soften/demote。 |
| `stability` | 最近 evidence 足够稳定，可以更有信心调整 rung。 |
| `novelty_readiness` | 适合换 exemplar、更高 rung，或 sibling axis。 |

### 6.4 Score Update Policy

V1 使用 hand-authored weights。它们故意保持简单、可检查、可替换。这里的目标不是在 V1 做一个完美的 learning model，而是比 pass/fail 更细，同时让每一次更新都能解释清楚。

Example deltas:

| Evidence | Mastery | Engagement | Support needed | Novelty readiness |
|---|---:|---:|---:|---:|
| Clean correct, no hint | `+0.18` | `+0.06` | `-0.05` | `+0.08` |
| Spontaneous L+1 | `+0.20` current rung, `+0.10` next rung | `+0.08` | `-0.04` | `+0.30` |
| Correct after light hint | `+0.10` | `+0.04` | `+0.08` | `+0.02` |
| Correct after multiple choice | `+0.06` | `+0.03` | `+0.14` | `0.00` |
| Modeling needed | `+0.04` | `0.00` | `+0.20` | `-0.03` |
| Mixed but on-topic | `+0.04` | `+0.05` | `+0.08` | `0.00` |
| Off-topic | `-0.08` | `-0.12` | `+0.10` | `-0.04` |
| Repeats prompt | `-0.06` | `-0.04` | `+0.15` | `-0.03` |
| Long silence after correct | `0.00` | `-0.02` | `+0.10` | `0.00` |
| Silence no attempt | `-0.05` | `-0.10` | `+0.12` | `-0.04` |

使用 bounded exponential smoothing：

```text
new_score = clamp(old_score * retention + evidence_delta, 0.0, 1.0)
```

Recommended V1 retention:

| Score | Retention |
|---|---:|
| `mastery` | `0.90` |
| `engagement` | `0.80` |
| `support_needed` | `0.85` |
| `novelty_readiness` | `0.75` |

`stability` 不直接用 deltas 更新，而是从近期 score variance 和 outcome consistency 计算。

### 6.5 External Actions

对外 action enum 保持小而稳定。

| Action | 含义 | Child-facing handling |
|---|---|---|
| `promote` | 下一次 prompt/activity 可以在同 axis 上更深入。 | 问更丰富的问题，不把 level 机制直接暴露给孩子。 |
| `hold` | 留在同一 rung，换一个 variation 或 exemplar。 | 自然继续。 |
| `soft_reframe` | 放慢、给 hint，或换一种更温和的问法，不降低 rung。 | 用支持性语言。 |
| `demote` | 在多次可靠 overload evidence 后降低 cognitive load。 | 不暴露 demotion language；必须用 Dignity Reframe。 |
| `sibling_jump` | 横向跳到相关 axis，用于 novelty 或 relief。 | 说成新的探索方向，不说成失败。 |

support 不等于 failure。孩子如果在 modeling 或 multiple choice 后答对，通常是 `hold` 或 `soft_reframe`，不是立刻 `promote`。

### 6.6 Guardrails

algorithm 有 score state，但 pedagogy guardrails 是 hard constraints。

| Guardrail | Runtime effect |
|---|---|
| 6-10 second wait time | 不要太早把 no-response 当成 failure。 |
| No demote after one silence | 一次 silence 不能单独降低 rung。 |
| Soft-Reframe | processing-time 或 hesitant-but-engaged 时必须优先使用。 |
| Dignity Reframe | 每个 `demote` 都必须有 dignity surface。 |
| Banned phrases | agent-prompt constraint 不变。 |
| Two failed attempts | 只是 demotion eligibility threshold，不是自动 `demote`。 |
| Three same-axis successes | 是 promotion evidence，不是自动 `promote`。 |
| Sibling-axis jump | 保留在 L3 ceiling 或 persistent L1 overload 时使用。 |

### 6.7 Timing, Activity Coverage, and Axis Routing

这一段回答三个会影响 implementation 和 catalog planning 的问题：

1. progression 什么时候影响下一次 activity？
2. 每条 axis / 每个 rung 是否都要单独准备一个 activity？
3. 孩子在某条 axis 上超过 L3 以后，系统应该转向哪条 axis？

#### 6.7.1 Progression 什么时候生效

progression 有两个时间尺度：

| Time scale | 是否发生在 live activity 中 | 可以变什么 | 不应该变什么 |
|---|---|---|---|
| Turn-level adaptation | Yes | wait time、hint、multiple choice、modeling、`soft_reframe`、Dignity Reframe wording | 不要突然替换整个 activity。 |
| Activity/session outcome | activity 结束后 | axis state、mastery scores、next recommended rung、next recommended axis | 不要 retroactively rewrite completed activity。 |

runtime 可以在 activity 内部调整提示方式，但 durable progression state 通常应该在 activity 结束后 commit。这样 live experience 比较稳定，孩子不会感觉系统在中途突然换游戏。

Example:

```text
Current activity: Form L1
Child response: names color quickly, then adds "red warns birds"
During activity: agent can ask one richer follow-up
After activity: Form state updates; selector recommends Form L2 or L3-ready content next
Next activity: chosen from catalog using updated Form state
```

`promote` 最好理解成“下一次 activity 应该 target higher rung”，不是“现在立刻打断当前 activity 并加载一个新的 L2 activity”。例外是 activity 本身已经有 authored elastic prompts，可以在同一个 activity 里问更丰富的问题；但 persisted rung state 仍然在 session end 更新。

#### 6.7.2 避免 Activity Explosion

最粗暴的 catalog 设计会要求 `7 axes x 3 rungs = 21` 个 activity types，再乘上 entities、pillars、age tiers。这个内容成本太高。

推荐的 catalog model 是 **activity families with elastic rung variants**，而不是每个 cell 都写一个 bespoke activity。

| Catalog layer | 作者准备什么 | Example |
|---|---|---|
| Activity family | 可复用的 game mechanic 和 entity/pillar structure | "Color Scout" 或 "Part Detective" |
| Primary axis | 这个 activity 正式更新的唯一 axis | `form` |
| Rung variant pack | 同一个 family 内的 L1/L2/L3 prompt patterns | L1 name color; L2 name and locate features; L3 explain why feature exists |
| Runtime selector | 根据孩子当前 axis state 选择最合适的 family/rung | 有 Form L2 就选；没有就用 elastic Form L1 加 L2 micro-challenge |

一个 Form activity family 可以覆盖三个 rungs：

| Rung | Prompt shape | Child evidence |
|---|---|---|
| Form L1 | "What color/shape/part do you notice?" | Names one attribute |
| Form L2 | "Where do you see two or three details?" | Names multiple attributes and locates them |
| Form L3 | "Why might it have that color, shape, or pattern?" | Explains purpose or reason |

promotion 不要求团队立刻为每个 L1 activity 都写一个全新的 L2 activity。selector 应该 availability-aware：

1. 优先 exact match：same axis、recommended rung、suitable tier、fresh entity/pillar。
2. 如果没有 exact match，用同一个 activity family 的 higher-rung prompt variant。
3. 如果连 higher-rung variant 都没有，hold rung，但加一个 richer micro-challenge。
4. 如果 axis 已经 saturated 或到 ceiling，用 sibling-axis routing。

catalog coverage 最终应向 strong axis/rung families 的矩阵靠近。但 V1 可以从较少的高质量 families 开始，只要每个 family 有 elastic prompt variants，并且 selector 记录 fallback reason。

#### 6.7.3 超过 L3 后怎么办

当前模型没有 L4。当孩子在某条 axis 上出现稳定 L3 evidence 时，系统应该保留这条 axis 的 L3 mastery，然后把下一次 activity 横向转到相关 sibling axis 的 L1 或 L2。

`sibling_jump` 不是 demotion。它表达的是：“你已经在这里走得很深了，现在把这个能力连接到旁边的 thinking lens。”

Recommended default sibling graph:

| Current axis at L3 | Primary sibling jump | Fallback sibling | Rationale |
|---|---|---|---|
| `form` | `connection` L1 | `function` L1 | 从 noticing attributes 转到 grouping shared attributes，或问 parts 是做什么的 |
| `function` | `causation` L1 | `change` L1 | 从 how it works 转到 why it behaves that way，或 part changes 后会怎样 |
| `causation` | `change` L1 | `function` L1 | 从 why something happens 转到 cause 如何随时间展开 |
| `change` | `causation` L1 | `responsibility` L1 | 从 transformation sequence 转到 why it changed，或接下来需要什么 care |
| `connection` | `perspective` L1 | `form` L2 | 从 things 之间的关系转到不同 viewpoints |
| `perspective` | `responsibility` L1 | `connection` L1 | 从 seeing another viewpoint 转到 deciding what helpful action follows |
| `responsibility` | `perspective` L1 | `connection` L1 | 从 care/action 转到 who needs what，或 child 和 system 的 connection |

这张表是 default，最终 sibling choice 应综合：

- 表里的 conceptual adjacency；
- child 在 candidate sibling axes 上的 current mastery 和 engagement；
- recent exposure，避免重复；
- catalog availability；
- entity/pillar freshness；
- parent 或 educator policy constraints，如果有。

在 L3 ceiling 时，sibling routing 通常应选择相关但 evidence 更少、最近较少探索的 axis。在 L1 floor 且 repeated overload 时，sibling routing 应选择 predicted engagement 更高、support need 更低、或近期成功更强的 axis。

| Sibling-jump case | Goal | Selection bias |
|---|---|---|
| L3 ceiling | 保持 novelty，拓宽 thinking | conceptually adjacent、recently less explored axis |
| L1 persistent overload | 恢复 confidence 和 engagement | engagement 更高、support need 更低、或 prior success 更强的 axis |

Example L3 ceiling:

```text
Mia reaches Form L3 on ladybugs:
"Red warns birds not to eat it."

Next activity should not invent Form L4.
Recommended jump: Connection L1
"Can you find another small thing with warning colors or spots?"
```

Example L1 overload:

```text
Mia struggles with Causation L1 twice:
no answer, then repeats the prompt.

Next activity should not keep forcing Causation.
Recommended relief jump: Form L1 or Connection L1, depending on her stronger recent engagement.
```

completed activity 仍然只更新它声明的 primary axis。`sibling_jump` 影响下一次 selection，不改变刚结束 activity 的 credit。

### 6.8 Progression Event

每次 progression action 都应该产出一个 compact explainability event。

```yaml
progression_event:
  axis: form
  entry_rung: 2
  exit_rung: 2
  action: soft_reframe
  reason_codes:
    - long_silence_after_correct
    - adequate_engagement
    - demotion_blocked_single_silence
  evidence_confidence:
    correctness: 0.61
    language_depth: 0.58
    latency_bucket: 1.0
    hint_level: 1.0
  scores_before:
    mastery_current: 0.58
    engagement: 0.79
    support_needed: 0.37
  scores_after:
    mastery_current: 0.58
    engagement: 0.77
    support_needed: 0.46
  policy_version: evidence_v1_default
```

reason codes 让 debugging 更容易，也能支持 parent-facing aggregation，同时不暴露 raw transcript。

---

## 7. Downstream Usage

downstream surfaces 应该读取 resolved session events，并谨慎聚合。它们不应该展示 matcher-only declarations，例如 `entity_binding` 或 `matchability`。

### 7.1 Child Recap

child recap 讲的是孩子刚才做了什么，不是 catalog 为什么选中了这个 activity。

| Field | Child recap use |
|---|---|
| resolved `entity` | 说清楚孩子刚才围绕哪个 object / creature 做活动。 |
| `activity_signature.observation_angle` | 用于 "you noticed red"、"you counted how many" 这类表达。 |
| `activity_signature.mechanic` | 用于 "you collected"、"you compared"、"you cared"。 |
| `activity_signature.entity_role` | 解释照片里的东西是 subject，还是被用作 bridge。 |
| `activity_signature.focal_attribute` | child-friendly 的具体值，例如 `red`, `three`, `happy`。 |
| `highlight_moment` | session 中的代表性时刻。 |

child recap 不应该把 `progression.topic_axis` 当 label 展示给孩子。它可以作为 hidden context，帮助生成更好的 highlight sentence。

### 7.2 Parent Growth Path

parent view 是 windowed aggregate。一个 completed activity append 一个 event；growth path 聚合一段时间里的多个 events。

| Field | Per-activity meaning | Window aggregation | Parent effect |
|---|---|---|---|
| `progression.topic_axis` | 这个 activity 爬的 axis。 | 按 axis group events。 | LxT ladder row。 |
| `progression.difficulty_level` | attempted/reached rung。 | 用 progression policy 算每条 axis 的 current rung。 | axis 下的 evidence，可能推动 visible rung。 |
| `progression.next_step_hint` | 这个 activity 后的建议方向。 | 近期可用 hints 进入 suggestion pool。 | "Try at home" 或 possible next direction copy。 |
| `key_concepts` | activity 涉及的 conceptual lenses。 | 按 concept 统计 exposure。 | Curiosity profile / framework chips。 |
| `atl_skills` | 练到的 thinking/learning modes。 | 按 skill 统计。 | thinking-skill trail。 |
| `subject_tags` | 涉及的 curriculum domains。 | domain balance。 | subject balance 和 parent summaries。 |
| `activity_signature.observation_angle` | 关注的 attribute/dimension。 | 按 angle 拆分 axis evidence。 | color vs quantity vs emotion exposure。 |
| `activity_signature.mechanic` | 孩子的 action pattern。 | 和 angle 做 cross-tab。 | exploration matrix。 |
| `activity_signature.entity_role` | photo 在 activity 中的角色。 | 追踪 subject/exemplar/catalyst/reference patterns。 | timeline explanation 和 pivot clarity。 |
| `caregiver_role` | adult support expectation/usage。 | support mix。 | parent guidance 和 support gauges。 |

如果周一是 `topic_axis: form` L2，周二的新照片触发了 `topic_axis: connection` L1，Form row 仍然保留在这个 window 的 history 里，Connection 获得自己的 event。selector 应尽量延续方向，但 dashboard 必须保留孩子真实走过的 path。

---

## 8. Worked Examples

### 8.1 Color Scout From A Red Pen

Static tag block:

```yaml
entity_binding: parameterized
matchability:
  entity_class_filter: []
  tier_support: {T0: true, T1: true, T2: true}
activity_signature:
  observation_angle: color
  mechanic: collect
  entity_role: exemplar
  focal_attribute: "{matched_color}"
progression:
  topic_axis: form
  difficulty_level: 2
```

Runtime event:

```yaml
session_event:
  entity: pen
  rendered_focal_attribute: red
  axis: form
  rung: 2
  angle: color
  mechanic: collect
  entity_role: exemplar
  completed_count: 3
```

Progression effect:

- 更新孩子的 Form state，因为 `topic_axis: form`。
- 在 Form 下面增加 color evidence，因为 `observation_angle: color`。
- 如果孩子独立找到了多个 red items，并能解释相似点，progression engine 可能把 Form L2 标为 strong，或准备未来的 Form L3 prompt。
- 如果孩子需要 multiple-choice support 但仍然 engaged，更可能是 `hold` 或 `soft_reframe`，不是立即 `promote`。

Parent effect:

- selected window 里增加一个 Form-row event。
- 增加 Form 下的 `color` exposure。
- exploration matrix 增加 `collect x color`。
- 如果 tag block 有 `observation` / `classification`，thinking-skill trail 增加对应 evidence。

### 8.2 Voice Stage From A Lion

Static tag block:

```yaml
entity: lion
entity_class: [big_cat, mammal, animal]
entity_binding: bound
matchability:
  entity_class_filter: [big_cat]
  tier_support: {T0: true, T1: true, T2: true}
activity_signature:
  observation_angle: behavior
  mechanic: voice
  entity_role: subject
  focal_attribute: lion_voice
progression:
  topic_axis: connection
  difficulty_level: 2
```

Interpretation:

- eligibility 比 Color Scout 更窄，因为 `entity_class_filter: [big_cat]`。
- lion 仍然是 `subject`，不需要 pivot。
- 孩子通过 behavior/voice evidence 练 Connection。
- parent dashboard 可以说孩子使用了 expressive / communication skills，但不展示 matcher fields。

---

## 9. Authoring Checklist

接受一个 `tag_block.yaml` 前，至少检查：

- `activity_id` 和 directory name 一致。
- `entity_binding`, `entity_class`, `tier_range`, `matchability` 清楚表达 eligibility boundary。
- `matchability.tier_support` 和 `tier_range.span` 一致。
- `activity_signature.observation_angle` 是 `docs/activity_vocabulary.md` 里的 closed enum。
- `activity_signature.bridge_prerequisites.primary` 使用 1-3 个 closed observation-angle values。
- `activity_signature.mechanic` 描述孩子实际做什么，而不只是 `game_style`。
- `activity_signature.entity_role` 能解释 photo 是 subject、exemplar、catalyst 还是 reference。
- `progression.topic_axis` 只有一条 axis，并且没有被当成 `observation_angle` 的同义词。
- `progression.difficulty_level` 是 integer `1`, `2`, `3`。
- `next_step_hint` 写成 suggestion，不写成 guarantee。
- `atl_skills`, `kud.do`, `activity_signature.mechanic` 彼此一致。
- parent-facing fields 足够稳定，可以长期聚合。
- child recap 可以生成，不需要暴露 matcher-only fields。

---

## 10. Source Map

| Need | Source |
|---|---|
| Activity matcher and progression workflow diagrams | `docs/activity_matcher_progression_workflows.md` / `docs/activity_matcher_progression_workflows_cn.md` |
| Schema-required fields and machine validation | `activities/_schema/tag_block.schema.json` |
| Closed `activity_signature` enums and `atl_skills` vocabulary | `docs/activity_vocabulary.md` |
| Field ownership and authoring examples | `docs/activity_tag_block_usage.md` |
| Activity signature design rationale | `docs/plans/2026-04-23-activity-signature-design.md` |
| 7-axis progression ladder and tag-block contract | `docs/progression_axes.md` |
| Evidence-based progression algorithm | `docs/superpowers/specs/2026-04-24-progression-algorithm-design.md` |
| Parent growth path read contract | `docs/parent_growth_path_preview.html` |
| Template 0 tag block preview | `docs/template_0_preview.html` |
