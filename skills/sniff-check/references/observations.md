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
