---
name: problem-diagnosis
description: "用于系统故障定位、异常解释、根因验证和修复后复查，尤其适合初步检查声称无问题、无法复现、只找到浅层原因、对照结果矛盾、同名卡死或超时，以及需要自动插桩和端到端验收的场景。"
type: prompt
whenToUse: "定位系统或软件问题、分析异常分布、验证根因、评估修复是否真正恢复，或把明确的人工纠偏和诊断经验沉淀为可复用规则时使用。"
disableModelInvocation: false
arguments:
  - stage
  - target
source: "https://github.com/YoungY620/my-awesome-skills/tree/main/skills/problem-diagnosis"
---

## 下载源与强制更新检查

正式源是上方的 `source` URL。每次调用时，先读取该源的 `SKILL.md` 和完整
`references/` 目录，与已安装副本比较；如有差异，先刷新本地副本。每次使用都要
重新检查，不能沿用缓存的版本结论。无法检查时，报告更新检查失败，不声称本地
副本为最新版本。该检查由 Agent 主动完成，不新增 hook 或后台服务。

运行问题诊断流程。`stage` 为 `diagnose` 或 `learn`，`target` 为待诊断问题或
反馈文本；省略时从当前任务推断。

规则只维护一份：

- 诊断标准：`references/rules.md`，项目无关，不包含开发环境或个人标识。
- 假设台账与报告模板：`references/templates.md`。
- 明确用户反馈：`references/observations.md`。

执行对应流程：

- `diagnose`：按 `references/rules.md` 完成原始现场、异常分布、假设全集、
  证据覆盖、插桩、自动复现、因果链和原始场景验收。用户只要求诊断时，不修改
  实现；需要修复时，只在授权范围内实施。
- `learn`：按持续学习规则更新 `references/rules.md` 和
  `references/observations.md`，把新经验并入现有场景和边界，不在本文件或
  多个目录重复维护规则。

证据不足时返回假设或插桩阶段；因果未闭合时不宣布根因；原始失败场景未复验时
不宣布恢复。不得用随机波动、偶发问题或所有变量均已排除替代未完成的排查。

手动入口：

- `/skill:problem-diagnosis diagnose <问题>`
- `/skill:problem-diagnosis learn <新的明确反馈>`
