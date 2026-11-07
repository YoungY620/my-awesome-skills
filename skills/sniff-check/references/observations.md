# Observations

Records of explicit user feedback used by the continuous-learning workflow in
`rules.md`. Publish only generic preferences, without private project material,
credentials, machine paths or personal identifiers. Quotes below are selected
original user statements, not a complete conversation archive. The date is the
date of this update, not an invented timestamp for each earlier statement.

| Date | Source | Rule | User words | Resolution |
| --- | --- | --- | --- | --- |
| 2026-10-31 | Direct user feedback | S02 | “分布式部署相比单体部署、多设备部署相比于单设备网络部署都是增加复杂度。如非论证必要都采用后者” | Default to monolith/single-device deployment; justify necessary exceptions. Explicit general principle, not a ban on isolation. |
| 2026-10-31 | Direct user feedback | Reporting workflow | “用中文做计划，我来审查。用中文再给我整体讲一下你的设计计划。”；“现在这种风格的报告或者回复，比较符合我想要的形式。之后的开发当中，对于方案迭代的报告，按照这个标准来。” | Chinese iteration reports explain architecture, current evidence, changes and open issues; preserve feedback correspondence. |
| 2026-10-31 | Direct user feedback | Design validation / S09 | “整理方案要经过多轮的交叉验证，多个角度独立方案汇总和多轮交叉验证收敛”；“自己说的话通过交叉验证多角度核实” | Check plans and technical explanations against original requirements, actual consumers and independent angles, not only final code. |
| 2026-10-31 | User-provided work instructions | Independent review | “默认两轮，最多三轮”；“三轮仍未收敛，停止交付/合并，报告具体阻塞项并重新审视方案；不能更换提示词或无限重试直到模型同意。” | Two fresh-context rounds, at most one necessary final review; unresolved blockers stop delivery and trigger design reconsideration. |
| 2026-10-31 | Direct user feedback | S04 | “这种一次性的代码，如果是一次性的，应该在当时需要的版本使用过之后，就全部删掉。” | Retire completed one-off tooling and sole-use consumers together; preserve currently required schema lifecycle mechanisms. |
| 2026-10-31 | Direct user feedback | S04 / S09 | “完全不改变前段交互方式和界面风格、组件设计等，做到用户完全无感知，在此基础上进行尽可能大的代码精简和整理” | For an explicitly invisible cleanup, prove observable behavior is retained. This does not make all future UI changes forbidden. |
| 2026-10-31 | User-provided work instructions | Workflow | “规则直接写在本文，不另建多层规则、Hook、自动检查脚本或评审服务。”；“流程由 Agent 按本文主动执行；不新增用于启动它的 Hook、包装命令、阶段环境变量、凭证配置或自动后台任务。” | Use a manual evidence-based workflow; remove the former stage-marker requirement. Do not claim technical enforcement. |
| 2026-11-03 | Direct user feedback | S02 / S05 | “先按照最简单的方式实现这个思路”；“尽可能少增加环境变量配置，优先使用静态变量” | Start with existing interfaces and static policy; expose configuration only for a demonstrated external need. |
| 2026-11-03 | Direct user feedback | S07 | “所有相关定义文件的摘要或hash比较合理，也就是文件变了就需要新的”；“只要再加入task路径” | Artifact reuse needs a stable unit key plus an immutable revision or input digest; a commit suffices only when it covers every relevant input. Identity alone does not prove success. |
| 2026-11-03 | Direct user feedback | S13 | “成功通过的步骤可以跳过，从第一个失败的步骤开始”；“本质上是一个durable的设计模式” | Use durable stages with explicit success evidence; resume at the earliest unverified stage and preserve successful work. |
| 2026-11-03 | Direct user feedback | S13 | “分成更聚合的统一的大类”；“全局搜索是不合理的，要结构化的返回的解析” | Parse structured errors and group them by recovery action; retry only safe failed stages rather than repeating completed side effects. |
| 2026-11-03 | Direct user feedback | Design validation / S09 | “交叉验证鼓励使用多个独立subagent来做”；“交叉独立验证” | Reaffirms independent fresh-context review for designs and conclusions; no additional review rounds beyond the bounded workflow. |
| 2026-11-03 | Direct user feedback | S02 / S09 | “回忆总结之前的真实问题现场……是否能解决真实的问题，真实论证能够增加稳定性？” | Map reliability mechanisms to observed failures and verify the outcome they improve; check existing support before adding machinery. |
| 2026-11-03 | Direct user feedback | Design validation | “每次做设计的时候独立交叉验证和独立方案收敛应该是默认动作” | Every design includes independently developed alternatives, cross-validation and convergence by default; small designs scale depth rather than skipping the independent pass. |
| 2026-11-03 | Direct user feedback | Distribution / updates | “skill当中记录下载的来源，并且每次使用必须检查更新” | Record the canonical download source in `SKILL.md`; every invocation checks all upstream skill files and refreshes changed local copies before the workflow. Failed checks must be disclosed. |
| 2026-11-06 | Direct user feedback | S02 | “不要提前优化，任何优化都要对应一个待解决的问题，且必须论证其他的方案都无法满足这个需求，或者会付出更大的代价。每一项优化都要系统调研有什么其他方面的代价” | Optimizations name the present problem they answer, show the alternatives cannot satisfy the need or cost more, and account for their own added costs. |
| 2026-11-08 | Direct user feedback | Review independence, brief schema, S09, S01, learning loop, C02/C03 | “同意这些更正，包括细粒度的PR提、细粒度的Commit提交来修正这些问题。每个Commit关注一个聚焦的修改点，整体上融入这两篇文章的内容。”；“尽可能克制调整幅度。” | User approved a focused correction set derived from two public articles on skill evals and agent architecture failures, landed as separate focused requests: reviewer-seat independence and model identity, brief schema, S09 fail-loud, S01 commit granularity, learning write-audit and derivation rebuild. This record accompanies candidates C02 (equal-budget control) and C03 (catalogue hygiene). |
