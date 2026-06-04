# Full-Pass Agentic Pipeline Presentation Transcript（中文版）

Source presentation: `docs/full_pass_agentic_pipeline_presentation.zh.html`

使用方式：这是面向 product 和 engineering audience 的讲稿，不是逐字朗读页面上的所有标签。讲稿会解释 pipeline 怎么用、谁生成什么、每个 gate 为什么存在。技术术语保留英文，例如 `full-pass`、`agentic pipeline`、`Autodesign`、`runtime.yaml`、`step_instructions`、`asset_manifest.yaml`、`Cat5`、`PNG` 和 `TSV`。

## Opening

今天我会介绍 WonderLens 的 full-pass agentic pipeline。

这套 pipeline 的目标，是把一个 source activity idea 变成经过验证的 WonderLens activity package。成功输出不只是一个 package directory。它还包括 runtime text、image assets、downstream consumer checks、live 或 runtime-equivalent dialogue QA、repair evidence，以及 final review。

这里最重要的是 ownership。Autodesign 负责 source intent、package quality、runtime instructions、assets，以及所有 package-owned repairs。Fullstack-demo 和 WonderLens AI 是 direct consumers。它们应该按原样加载和验证 package，而不是在 downstream 静默补强一个本来就弱的 package。

## 为什么需要 Full Pass

一个 package 即使通过 static structure checks，也可能没有兑现 product promise。

常见问题不是缺文件，而是 drift。比如 workbook activity 原本承诺一个 child action、一个 source object、一个 reveal 方式，但生成出来的 package 可能把它变成更简单、更泛化的 activity。这样的 package 仍然可能通过 schema。

Full pass 会在最容易漂移的地方增加检查：source intent、runtime behavior、visual assets、consumer conversion、repair routing 和 final review。

这套流程有五个核心原则：

Intent：保住 source play frame。

Runtime：让 `prod.md` 可执行，而不是只写得好听。

Assets：匹配真实 beat，而不是只匹配整体氛围。

Consumers：同时验证 Fullstack-demo 和 WonderLens AI。

Repair：每个 failure 都要路由给正确 owner。

## Source Rules

更新后的 contract 从原始 workbook promise 开始。

对于 workbook-derived activities，`inputs/original_activity_concepts_2026-05-29.tsv` 是控制源。`inputs/source_activity_concepts.md` 很有用，但它只是 normalized helper。它可以帮助统一名称、mechanics、asset hints 和 capability notes，但不能削弱原始 source promise。

在任何 package writing 开始前，`run_manifest.yaml` 必须记录 `source.full_pass_pipeline: true` 和 `source.asset_build: generate_and_curate`。

Runtime contract 也在这里锁定。Step 1、Step 2、每个 Step 3 round、Cat5 synthesis、celebration、closing 和 early exits 都需要 machine-convertible instruction。Instruction 需要包含 goal、constraint、tone、progress evidence、branch behavior 和 frame guardrail。

对于 Cat5，collection、synthesis 和 celebration 要保持分离。如果 Cat5 activity 有 synthesis behavior，importers 必须单独保留它，而不是压成一个泛化的 final step。

## Pipeline Map

Pipeline map 是 full pass 的操作视图。

它有三条 lane：

Autodesign 负责 source、text package、audits、package repair 和 final reporting。

Image phase 负责 manifest completion、image generation、reference curation、asset build、Image QA 和 image repair。

Consumers 负责 Fullstack-demo import、Fullstack QA、WonderLens AI runtime checks、AI dialogue QA、issue classification 和 final review。

讲解时可以点击每个 step。右侧 detail panel 会显示这个 step 的 owner、inputs、outputs、validation gate，以及 repair route。

关键点是，这些 step 不是同一种工作。有些是 deterministic checks，有些依赖 agent judgment，有些依赖 downstream runtime systems。Pipeline 的价值就在于，它不会把这些差异藏起来。

## Workflow Animation

Workflow animation 展示 run packet 如何穿过整个 pipeline。

先看 Source lock：master orchestrator 和 source-intent auditor 冻结必须保留下来的内容。

然后是 Text package：writer 生成 package files、demo support、runtime beats 和 text-only asset contract。

接着是 Post audit：independent package auditor 检查 package 是否仍然匹配 source contract。

然后是 Bundle repair：manifest 被补齐到 asset-ready。这个 step 确保 image generation 开始前，每个 required visual role 都已经存在。

之后是 Generate / curate：image agents 生成 PNGs，或者接收真实 source material。

接着是 Build assets：builder 写入最终 package-local runtime assets 和 manifest paths。

然后是 Image QA：validator 检查 manifest coverage、runtime size、style、crop safety、beat fit、reference fidelity、duplicate items，以及是否提前泄露答案。

接下来是 Consumer QA：Fullstack-demo 和 WonderLens AI 加载 package，并执行 runtime behavior。

最后是 Final review：independent reviewer 在 acceptance 前检查完整 evidence chain。

如果要讨论 failure route，可以点 Pause。如果要重新讲一遍 sequence，可以点 Restart。如果只是演示整体流动，可以保持 Loop 开启。

## Text Package Detail

Package writing 是 text-only，但它仍然是 runtime contract。

Package 预期包含 `spec.md`、`prod.md`、`tag_block.yaml`、`recap.template.yaml`、`dashboard.template.yaml`、`demo_support.yaml` 和 `asset_manifest.yaml`。

`spec.md` 是 reviewer reference。它记录 source promise、adaptation rationale、asset brief、usage timeline、residual risk，以及一个 self-evaluation scorecard。

`prod.md` 是 runtime guide。它必须描述 Step 1 到 Step 5、完整展开的 Step 3 rounds、screen states、child branches、follow-up policy，以及带 display/fallback behavior 的 asset IDs。

`tag_block.yaml` 是 machine contract。它记录 category、mechanic、pillar、game style、focal attribute、progression、tags 和 entity coverage vocabulary。

`demo_support.yaml` 是诚实的 demo gate。它说明 activity 是 supported、degraded 还是 unsupported，并记录 UI template、entity binding、runtime requirements 和 limitations。

`asset_manifest.yaml` 是 text-only asset contract。它命名独立的 runtime assets、variants、fallback behavior、paths 和 reference provenance requirements。

这里最重要的结论是：example lines 不够。`prod.md` 必须为每个 live beat 提供 `Runtime AI instruction`。这个 instruction 才能让 fullstack-demo 生成有用的 `step_instructions`，也能让 WonderLens AI 保留相同的 behavior。

## Agent Roles

Master agent 负责 orchestration，但 independent agents 要拥有独立的 review surface。

Authoring side 里，master orchestrator 控制 scope、snapshots、blockers、credentials、servers、commits 和 final report。Source-intent auditor 在写作前后锁住 play frame。Text-only package writer 写 runtime prose 和 package metadata。

Asset side 里，image-only generator 或 curator 生成 PNGs 和 source-backed assets。Image quality validator 检查 style、crop safety、beat fit 和 reference fidelity。Image improver 只修 visual artifacts，不改 dialogue。

Consumer side 里，package/import validator 检查 schema、paths、converted instruction shape 和 gates。Fullstack 和 WonderLens AI validators 运行 runtime-equivalent dialogue checks。Dialogue improvers 修 package-owned guidance gaps。Final reviewer 审 evidence 和 residual-risk ownership。

核心规则是：writer 不能成为自己 artifact 的唯一 reviewer。

## QA Criteria

这一节是三个最高风险 validation surface 的 pass/fail contract。

Image QA 验证 asset bundle。它检查 manifest coverage、package-local 512x512 PNGs、asset IDs 和 paths、flat Nordic style、round-screen crop safety、beat alignment、reference provenance、reference fidelity、duplicate selectable items、readable text、logos、watermarks，以及是否提前泄露答案。

Image QA evidence 应该包括 asset inventory、built file paths、thumbnails 或 review notes、reference-bound assets 的 source metadata，以及每个 failure 的 per-asset QA notes。

Image QA 只有在每个 required asset 都能加载、匹配对应 runtime beat 和 style、source-bound assets 真实且 faithful，并且剩余 issue 都已 repaired、blocked 或 explicitly accepted as degraded 时，才算 pass。

Fullstack QA 验证 web demo 作为 direct consumer 的行为。它检查 package 是否 import as authored、entity binding 是否生效、supported/degraded/unsupported gates 是否被遵守、assets 是否 resolve、`step_instructions` 是否保留 goal、constraint、tone、progress evidence、branch behavior 和 frame guardrail、Cat5 synthesis 是否保持分离，以及 expected UI state 是否出现。

Fullstack QA 必须覆盖 ideal、minimal、wrong、off-topic、help、done、silence、photo 和 item flows。Evidence 应该包括 import report、converted runtime YAML 或 demo MD、asset path report、screenshots 或 UI notes、representative transcripts，以及 classified failures。

Fullstack QA 只有在 web demo 没有 unsafe fallbacks 就能加载、遵守 demo gates、展示 declared assets、保留 package runtime beats，并且每个 mismatch 都分类为 package-owned 或 fullstack-owned 时，才算 pass。

AI dialogue QA 用 generated YAML 和 `prod.md` 验证 WonderLens AI runtime behavior。它检查 real camera 或 `photo_id` assumptions、Cat5 response types、collection catalog use、source guardrails、branch behavior、synthesis、celebration，以及 unsupported visual claims。

AI dialogue QA evidence 应该包括 runtime artifact report、prompt 或 context trace、和 fullstack QA 相同策略下的 transcripts、comparison notes，以及 mismatch owner classification。

AI dialogue QA 只有在 responses 在 ideal 和 recovery paths 中遵循 package goal、constraint、tone、progress evidence、branch policy 和 source guardrails，并且每个 discrepancy 都已 repaired 或 assigned to correct owner 时，才算 pass。

## Artifact Flow

Artifact flow 说明谁生成什么，以及每一组 artifact 怎么用。

Source and run artifacts 由 master orchestrator 和 source-intent auditor 生成。它们用于冻结 scope、source promise、run flags、blockers 和 evidence paths。输出包括 source snapshot、assignment snapshot、pre-package audit 和 run manifest。

Autodesign package artifacts 由 text-only package writer，加上 image-only asset generator 和 builder 生成。它们是 fullstack-demo 和 WonderLens AI 的 direct import contract。输出包括 required package files、demo support、asset manifest、PNG assets、selectable items 和 reference sources。

Consumer evidence 由 import validators、runtime validators、Image QA 和 final reviewer 生成。它用于决定 activity 应该 accepted、回到 package repair、进入 downstream follow-up，还是因为 product capability 被 blocked。

这里也能看清 ownership。Weak package evidence 回 Autodesign。Good package evidence 如果被 runtime 忽略，就成为 downstream issue。

## Asset Phase

当前 asset style 是 flat Nordic nursery illustration：安静的白底、克制的 boho pastels、稀疏线条、足够留白，每个 beat 或 item 一个独立文件，并且不内嵌 device chrome。

每个 package 都需要 standard scene bundle：`activity_icon`、`intro_scene`、`rules_scene`、三个 round scenes、`celebrate_scene` 和 `closing_scene`。Cat5 或 synthesis flows 还需要 `synthesis_scene`。

Selectable items、targets、distractors、reference sources 和 badges 是额外 assets。它们不能替代 scene bundle。

Reference-bound assets 和纯 illustrative assets 不一样。如果 activity 承诺真实 artwork、constellation、landmark、animal、plant 或其他 reference-bound object，那么 asset 必须有 source 支撑。随机生成的近似图不够。

Vegetable Sort example 展示的是目标形态：每个 major beat 都有 scene 和 icon assets，每个 selectable vegetable card 还有独立 item PNG。

## Repair Routing

这套 pipeline 的价值在于不隐藏 ownership。

如果出现 source intent drift，就修 text package，并重新跑 source-intent audit。

如果 runtime instruction 太薄，就修 package，并重新跑 import 和 dialogue validation。

如果 image 不对，就修 image-owned artifact，并重新跑 Image QA。

如果 fullstack-demo 忽略了好的 package instructions，就记录 fullstack follow-up。

如果 product capability 目前 unsupported，就不要把它假装成 playable。应该标记为 blocked、degraded，或者只有在 product approval 后接受 minimum behavior。

如果 credentials 或 provider access 缺失，就记录具体缺失的 prerequisite 和 retry evidence。

## Acceptance Gates

Full pass 只有在每个 gate 都有 evidence，或者每个 blocker 都明确、可归属、可复现时，才算 accepted。

关键 gates 包括 run flags、source intent、package quality、runtime instruction quality、assets、fullstack import、WonderLens AI runtime、dialogue QA、marker-free runtime input 和 final review。

这意味着 final acceptance standard 不是“package exists”。真正的标准是：两个 direct consumers 都能加载并运行 package，而且不会削弱 activity promise。

## Team Views

Product 应该用 run output 判断：generated activity 是否保住了原始 promise，是否存在当前 unsupported 的 required capability，degraded behavior 是否可接受，image assets 是否适合 child-facing experience，以及 dialogue transcripts 是否像预期的 activity。

Engineering 应该用 run output 验证：schema、vocabulary、`prod.md` conversion、fullstack-demo behavior、WonderLens AI behavior、asset path resolution，以及 issue ownership。

同一份 run output 同时服务两个视角，但两个视角回答的问题不同。

## Invocation

Full production pass 使用这个命令：

`/goal Execute goals/2026-06-01-run-full-pass-agentic-pipeline-goal.md end to end.`

Scoped goal 负责 full-pass flags、delegated-agent rules、credential boundaries、live validation order 和 final acceptance criteria。

Asset phase 使用 builder sequence：

先跑 `repair_full_pass_asset_bundle.py`，再跑 `build_activity_assets.py`，最后跑 asset validation scripts。

完成标准不是 package 存在。完成标准是 package、assets 和 direct consumers 都保留 activity promise，或者每个剩余 limitation 都有明确 owner 和 evidence。

## Closing

实际建议是把它当作 release-quality validation path，而不是每个 exploratory package 的最低成本路径。

Full pipeline 有意保持严格。它也确实很长、容易失败，因为它跨过 text generation、asset generation、consumer import、runtime behavior 和 live dialogue。正因为如此，artifacts、owners 和 repair routes 必须写清楚。

当 pipeline 通过时，我们能说的不只是“package 生成了”。我们可以说：source promise 经过 package text、image assets、consumer runtime conversion、dialogue behavior 和 final review 后仍然保留下来了。
