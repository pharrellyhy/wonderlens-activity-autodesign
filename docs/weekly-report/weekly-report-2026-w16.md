# WonderLens Activity AutoDesign — 周报 W16（2026-04-11 ~ 2026-04-17）

## Template 0 通用骨架设计

- 提出 Template 0 —— 一个 category-agnostic 的活动骨架，将现有 Template A（Cat1）与 Template B（Cat5）中重复的情绪弧、tag 逻辑、tier 指南上提为共享根，A/B 退化为仅覆盖各自品类差异的 overlay。
- 新增 `docs/template_0_preview.html` / `_cn.html`（各约 4331 行）作为 9 节交互式设计文档，涵盖 tag block、骨架代码面板、7 条 progression axes、5-dial tier 适配模型、金标覆盖表与 overlay hook 规范，供内部团队评审。
- 新增 `docs/template_0_lt_walkthrough.html` / `_cn.html`（约 763 行）的 3×3 矩阵动画，直观演示 L（概念深度 L1/L2/L3）与 T（tier T0/T1/T2）正交关系，每格对话可点击并支持自动播放。
- 引入 7 条 progression axes，对齐 IB 7 Key Concepts（Form / Function / Causation / Change / Connection / Perspective / Responsibility），每条给出 L1 notice → L2 extend → L3 reason 三档梯级与范例。
- 定义 5-dial tier 适配模型（AI role / language / task depth / concept focus / caregiver role），规定活动可向相邻 tier 柔性扩展，但不允许跨两档跳跃。

## Template 0 落地实施规划

- 新增 `docs/plans/2026-04-16-template-0-implementation.md`（213 行）作为评审通过后的执行计划，拆分为 6 个任务，预计覆盖 5 个文件修改 + 1 个文件新建。
- Task 1：新建 `docs/progression_axes.md` 作为 7 轴 L1/L2/L3 的权威参考，包含金标覆盖表与"给定 entity + pillar 如何选轴"的决策指引。
- Task 2–6：在 `templates.md` 顶部插入 Template 0 并把 A/B 改写为 overlay，同步更新 `program.md`、金标设计模板引用路径，保留向后兼容。

## W15 产出批量入库

- 将上周累积的 92 个文件、约 15785 行未提交产出一次性合入 `356f822`，覆盖 property-bridge 模板批量、金标 gold 命名重构、playbook 文档、transform 工作流文档与 game_styles.md。
- 将 12 个 Experience Pillar 金标文件统一重命名为 `{entity}_cat{N}_gold_{spec,prod}.md`，property-bridge 模板采用 `{name}_property_gold_{spec,prod}.md`，与 legacy 设计在文件层面彻底分级。
- 清理 `designs/` 根目录下早期扁平布局的旧 cat5 设计桩（`autumn_leaf_cat5.md` 等），统一由 `designs/cat1/` + `designs/cat5/` 分类目录承载。

## 仓库与运行时整理

- 提交 `b0d38cb` 将 `.claude/worktrees/` 与 `.superpowers/brainstorm/` 下的 runtime 制品（`.server.pid`、`.server-stopped`、各类 brainstorm HTML 草稿）从 git 跟踪中移除，共清掉约 543 行噪声。
- 更新 `.gitignore` 把 `.claude/` 运行时目录纳入忽略，避免后续 session 的 brainstorm 产物再次污染工作树。

## 下周关注点

- 推进 Template 0 实施计划 6 个 Task，优先完成 `progression_axes.md` 新建与 `templates.md` 中 Template 0 插入 + A/B overlay 改写，确保下游设计可直接引用新骨架。
- `template_0_preview.html` / `_cn.html` 仍有未提交修改（`git status` 显示 M），需在合入前确认中英文版本一致再提交。
- `HANDOFF.md` 仍停留在 2026-03-19 的 v2 design / transform 工作状态，已跨越 Entity Bridging、Experience Pillars、Template 0 三个里程碑未更新，建议在 Template 0 落地同时同步重写。
- 未映射实体的 Entity Bridging 实现（`prompts/constellation_bridge.md`、`constellation_map.yaml` 等）仍是 Planned 状态，需排期是否并入 Template 0 这一批。

---

*生成日期：2026-04-17*
