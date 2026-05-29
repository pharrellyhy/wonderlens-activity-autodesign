# Selected Source Design Snapshot

Run id: `20260529_172332_source_intent_pilot`

This snapshot preserves the original workbook wording for the selected pilot rows. The TSV row controls over normalized helper wording when they conflict.

## 1. TSV Row 2: 音素寻宝

- Normalized helper: `inputs/source_activity_concepts.md#source_phoneme_hunt`
- Activity ID: `concept_phoneme_hunt_collect`

| Field | Original workbook value |
|---|---|
| 活动名称 | 音素寻宝 |
| 添加时间 | 2026/04/30 |
| 主体类型 | 属性 |
| 形式(单选) | Cat 5. 需结合拍照 |
| 场景 | 室内 |
| 机制(Mechanic)(单选) | 3. 收集/配对 Collect/Match/Pair/Associate/Generalize |
| 对屏幕的依赖度（特指视觉展示，不包括拍照行为） | 低 |
| 活动简介/举例 | 我今天很饿，我想吃一些以 /b/ /b/ /b/ 开头的词语。你能找一个这样的‘宝贝’给我看吗？ |
| 备注 | 是Scavenger的形式，但是因为特殊属性因此单独列出，屏幕上可以展示对应的字母 |

## 2. TSV Row 4: 画画

- Normalized helper: `inputs/source_activity_concepts.md#source_guided_drawing`
- Activity ID: `concept_guided_drawing_probe`

| Field | Original workbook value |
|---|---|
| 活动名称 | 画画 |
| 添加时间 | 2026/04/30 |
| 主体类型 | 物体 |
| 形式(单选) | Cat 3. 需借助外部材料 |
| 场景 | 室内 |
| 机制(Mechanic)(单选) | 6. 搭建/创意 Build/Create/Assemble/Transform/Experiment/Invent |
| 对屏幕的依赖度（特指视觉展示，不包括拍照行为） | 高 |
| 活动简介/举例 | AI引导孩子拿纸笔，一步一步完成一个简单的画作 |
| 备注 | 简笔，sketch形式（无需填色），可以预设大量的简笔画，但是需要模板化，使AI能进行步骤拆解。无需每步确认，留足时间即可。孩子最后拍出整体作品“验证”，不用评估质量，重在过程，给予鼓励+小庆祝 |

## 3. TSV Row 20: 星座的恒星数量

- Normalized helper: `inputs/source_activity_concepts.md#source_constellation_star_count`
- Activity ID: `concept_constellation_star_count_enumerate`

| Field | Original workbook value |
|---|---|
| 活动名称 | 星座的恒星数量 |
| 添加时间 | 2026/04/30 |
| 主体类型 | 物体 |
| 形式(单选) | Cat 1. 纯语音（含屏幕显示及互动） |
| 场景 | 室内,户外 |
| 机制(Mechanic)(单选) | 1. 识别/计数 Enumerate/Identify/Count/Measure |
| 对屏幕的依赖度（特指视觉展示，不包括拍照行为） | 中 |
| 活动简介/举例 | 后台预制一个列表，是重点星座以及对应的恒星数量（不限于12星座，包括大熊、猎户等常见星座），让孩子在两个数字中选择（比如7还是29），然后给孩子展示他选择数字对应的星座，并进行简单的介绍（如多个星座对应相同的恒星数，可以随机选择） |
| 备注 | 预制AI生图，可以配合星座的名字标签展示。要把恒星点体现出来，让孩子在了解星座的同时练习数感。可以考虑排除恒星数量特别多星座，但只要AI生图足够清晰，也可以包括 |

## 4. TSV Row 15: 植物不同部位

- Normalized helper: `inputs/source_activity_concepts.md#source_plant_parts_explorer`
- Activity ID: `concept_plant_parts_enumerate`

| Field | Original workbook value |
|---|---|
| 活动名称 | 植物不同部位 |
| 添加时间 | 2026/04/30 |
| 主体类型 | 属性 |
| 形式(单选) | Cat 5. 需结合拍照 |
| 场景 | 室内,户外 |
| 机制(Mechanic)(单选) | 1. 识别/计数 Enumerate/Identify/Count/Measure |
| 对屏幕的依赖度（特指视觉展示，不包括拍照行为） | 低 |
| 活动简介/举例 | 引导孩子拍摄植物的不同位置（叶，花，花蕊等），AI用比较有趣味的方式介绍植物的不同部位和作用 |
| 备注 | 需要让AI生成一些介绍方式，保证多样和有趣 |

## 5. TSV Row 26: 职业决策

- Normalized helper: `inputs/source_activity_concepts.md#source_career_decision`
- Activity ID: `concept_career_decision_decide`

| Field | Original workbook value |
|---|---|
| 活动名称 | 职业决策 |
| 添加时间 | 2026/04/30 |
| 主体类型 | 属性,类别 |
| 形式(单选) | Cat 1. 纯语音（含屏幕显示及互动） |
| 场景 | 室内,户外 |
| 机制(Mechanic)(单选) | 8. 选择/决策 Decide/Choose/Correct |
| 对屏幕的依赖度（特指视觉展示，不包括拍照行为） | 低 |
| 活动简介/举例 | 告诉孩子假定现在是某个职业，然后在工作的过程中遇到了一个具体的场景，有一些问题需要小朋友这位“专家”来做决策。让孩子进行是非选择或者简单二选一。比如孩子是消防员，如果着火了，1）我们要不要立刻派消防车？2）我们应该用水还是油来灭火？ |
| 备注 | 问题不用太复杂，可以考虑对应不同的职业配合预制的职业画像进行屏幕展示+预制问题库。让孩子有专业感，自豪感。 |

## 6. TSV Row 11: 看部分，猜一猜

- Normalized helper: `inputs/source_activity_concepts.md#source_partial_reveal_guess`
- Activity ID: `concept_partial_reveal_deduce`

| Field | Original workbook value |
|---|---|
| 活动名称 | 看部分，猜一猜 |
| 添加时间 | 2026/04/30 |
| 主体类型 | 物体 |
| 形式(单选) | Cat 1. 纯语音（含屏幕显示及互动） |
| 场景 | 室内,户外 |
| 机制(Mechanic)(单选) | 1. 识别/计数 Enumerate/Identify/Count/Measure |
| 对屏幕的依赖度（特指视觉展示，不包括拍照行为） | 高 |
| 活动简介/举例 | 给出动物的一半，或者一个关键的部分，让孩子猜是什么动物 |
| 备注 | 需要AI预制图，统一风格，每次选择3-5张挑战，同一动物可以有多张图（不同部分）。除了动物，可以考虑这种玩法可以扩展到什么其他的类别 |

## 7. TSV Row 33: Would you rather

- Normalized helper: `inputs/source_activity_concepts.md#source_would_you_rather`
- Activity ID: `concept_would_you_rather_compare`

| Field | Original workbook value |
|---|---|
| 活动名称 | Would you rather |
| 添加时间 | 2026/04/30 |
| 主体类型 | 物体 |
| 形式(单选) | Cat 1. 纯语音（含屏幕显示及互动） |
| 场景 | 室内,户外 |
| 机制(Mechanic)(单选) | 2. 比较/对比 Compare/Contrast |
| 对屏幕的依赖度（特指视觉展示，不包括拍照行为） | 低 |
| 活动简介/举例 | 这种一种非常经典的玩法，主要用语音的形式，连续问问题，让孩子二选一。这种玩法中可以带有非常强的趣味性（搞笑的感觉）。比如Would you rather brush your teeth with ketchup, or wash your hair with chocolate milk? |
| 备注 | 注意问题不要太长 |
