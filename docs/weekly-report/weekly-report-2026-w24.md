# WonderLens Activity AutoDesign — 周报 W24（2026-06-06 ~ 2026-06-12）

## 团队协作与全量跑批准备

- 完善协作者上手路径，使新成员可以按运行队长、文本审查、素材审查和集成验证的角色进入同一套全量跑批流程。
- 建立按活动拆分的 review_status 状态契约，使并行审查可以分 lane 记录负责人、证据、阻塞原因和下一任 owner。
- 收敛角色分支、文件归属和交付边界，使多人协作时不再依赖口头约定来避免包文本、素材和下游验证互相踩踏。
- 明确 Gemini 凭据和 provider 设置方式，使不能使用 Codex 内置 imagegen 的协作者也能参与素材生成而不把密钥带进仓库。

## Gemini 素材生成链路

- 接入 Gemini 作为第三方素材 provider，使 illustrative 素材可以从活动 manifest 生成到 builder inbox，并继续交给确定性构建器产出运行时图片。
- 加固 provider 审计与路径约束，使生成记录可以保留模型、输出、哈希和错误类别，同时避免泄露密钥、本机路径和请求敏感内容。
- 补齐素材 provider 的单元测试和 live smoke，使生成、构建、验证和审计清洗在非生产样例上形成可复现证据。
- 规划 Gemini 多候选质量层，使后续素材生成先产出可审查候选，再由 curator 明确接受后进入正式构建入口。

## 分角色目标文件与日常流程

- 重构全量跑批目标文件，把一次性 baseline、文本审查、素材审查和集成验证拆成可重复执行的独立目标。
- 更新运行队长、文本审查、素材审查和角色提示指南，使日常 session 可以直接调用 scoped goal，而不是复制长提示或重述规则。
- 同步并行工作流展示页中的命令和时间线，使页面指向新的 scoped goal，并减少旧版 monolithic full-pass 入口造成的误导。
- 明确集成 owner 的下游验证边界，使 WonderLens AI 和 fullstack-demo 失败可以按 package、image、consumer 或产品能力分类回传。

## Runtime-Ready 包审查状态

- 补齐现有 runtime-ready 活动集的 review_status 文件，使每个包都可以进入文本、素材、契约、运行时和 PM 审查的同一状态模型。
- 保留完整活动包、素材、manifest 和 WonderLens AI 运行时生成报告，使后续审查可以从已有证据继续推进而不是重新拼装上下文。
- 纳入 Cat1 对话类、Cat5 采集类和降级适配类活动到同一审查队列，使不同支持模式的剩余风险可以被统一追踪。

## 质量修复与代码清理

- 修复并行工作流页面的文本重叠问题，使角色步骤和命令区在展示时更容易阅读。
- 补强本地密钥忽略规则，降低 Gemini 和 fullstack-demo 凭据在协作准备阶段被误提交的风险。
- 补充 README 的实体兼容性说明，使参数化、兼容性和运行时 handoff 的语义更容易被后续操作者理解。

## 下周关注点

- 推进 Gemini 多候选和 curator 接受流程，避免低质量单张输出直接进入 builder inbox。
- 启动一轮基于 scoped goal 的小型全量 dry run，验证运行队长和各角色 lane 是否能在真实分支协作中闭环。
- 推进 runtime-ready 活动集的 review_status 从初始 pending 进入真实审查结果，优先闭环文本、素材和下游验证证据。
- 继续跟进 WonderLens AI 与 fullstack-demo 的运行时对齐，确保动态 handoff、Cat5 采集和降级适配不会在消费端被静默弱化。

---

*生成日期：2026-06-12*
