# WonderLens Activity AutoDesign — 周报 W15（2026-04-04 ~ 2026-04-10）

## Entity Bridging 系统设计

- 提出三层 Bridge 架构（Constellation → Property Bridge → Conversation-only），替代原 Tier C 通用模板，为未映射到 IB mind map 的实体建立质量托底路径。
- 新增 `docs/plans/2026-04-08-entity-bridging.md`（393 行）完整设计文档，包含 21 个已映射实体的 constellation 语义邻接表、5 类 bridge pattern（Same taxonomy / Same role / Shared affordance / Part-of / Same domain），以及 Property Bridge 的 18 模板映射。
- 同步重写 `docs/plans/2026-04-01-style-recommender.md`（537 行），将实体 → 游戏匹配流程由旧 Tier C fallback 切换到新的 Bridge 多层架构，并补齐 12 金标的 constellation_notes 字段规范。
- 明确设计原则："Discovery, not redirection" —— 孩子拍到的实体始终被尊重，bridge 只做加法连接（"your kitten is a cousin of a lion!"），不做替换。

## Property-Bridge 模板批量产出（18 个）

- 为 Property Bridge 层新增 **12 个 Cat5 模板**，覆盖 6 个 Experience Pillar：`shape_quest` / `color_scout` / `movers_quest`（quest_collector × 3 属性）、`material_lab` / `size_experiment` / `nature_vs_made` / `shiny_experiment` / `old_vs_new`（field_experiment × 5 属性）、`pattern_trail`（mystery_trail）、`texture_mix`（mix_lab）、`sound_stage`（ensemble_show）、`living_rescue`（rescue_team），全部 spec + prod 齐备。
- 为 Cat1 端新增 **6 个对应模板**：`detail_detective`（mystery_lens）、`what_if_workshop`（inventor_workshop）、`property_predictor`（prediction_lab）、`time_shifter`（time_traveler）、`fix_it_station`（care_station）、`property_performer`（voice_stage），让 6 个 Pillar 在 Cat1 端也能由属性起题。
- 采用统一的 `{name}_property_gold_prod.md` / `{name}_property_gold_spec.md` 命名规范，与实体金标（`{entity}_cat{N}_gold_*.md`）文件名明确区分。
- 属性选取聚焦视觉可确认维度（shape / color / material / size / pattern / texture / sound / shininess / age 等），确保 AI 可从照片直接评估游戏进行状态，无需额外传感数据。

## 12 金标设计定稿与命名规范

- 将上周完成的 12 个 Experience Pillar 金标设计由 `*_prod.md` / `*_spec.md` 统一重命名为 `*_gold_prod.md` / `*_gold_spec.md`，与 property-bridge 模板及后续 legacy rewrite 在文件层面明确分级。
- Cat1 金标 6 个：lion（voice_stage / Performance）、goldfish（prediction_lab / Discovery）、banana（time_traveler / Adventure）、teddy_bear（care_station / Nurture）、toy_robot（mystery_lens / Mystery）、rubber_duck（inventor_workshop / Creation）。
- Cat5 金标 6 个：playground（field_experiment / Discovery）、dandelion（quest_collector / Adventure）、butterfly（mystery_trail / Mystery）、rock（mix_lab / Creation）、bird（ensemble_show / Performance）、flower（rescue_team / Nurture）。

## Game Design Playbook 文档化

- 新增 `docs/game_design_playbook.md`（约 30KB），系统整理 6 Experience Pillars × 12 styles 的设计框架、10-dimension rubric（Game Feel + Pillar Fidelity 等维度）与 tier 分级写作规范，作为后续设计的统一参考基线。
- 配套渲染出 `docs/game_design_playbook.html` 与 `docs/game_design_playbook_cn.html`（中文版），方便非工程师 / 教育团队直接查阅，不依赖 Markdown 渲染环境。

## 仓库整理

- 删除 `designs/` 根目录下 5 份早期扁平布局的旧设计（`autumn_leaf_cat5.md`、`dandelion_cat5.md`、`feather_cat5.md`、`pinecone_cat5.md`、`puddle_cat5.md`），统一由 `designs/cat1/` + `designs/cat5/` 分类目录承载。

## 下周关注点

- 本周产出基本全部未提交（18 个 property 模板 + 2 份核心设计文档 + playbook + 12 金标的 gold 重命名），需按主题分批 commit，避免堆成一次大而难审的变更。
- Entity Bridging 的实现落地：`prompts/constellation_bridge.md`、`constellation_map.yaml`、`conversation_bridge.md §5` 均在设计文档中标记为 Planned，尚未开工。
- 端到端验证 Bridge 分流比例是否达到目标（~40% Layer 1 / ~40% Layer 2 / ~20% Layer 3），确认无映射实体的体验不劣于原 Tier C。
- `HANDOFF.md` 仍停留在 2026-03-19 的 v2 design / transform 工作状态，与本周的 Experience Pillars 框架和 Bridge 系统完全脱节，需要同步更新。

---

*生成日期：2026-04-10*
