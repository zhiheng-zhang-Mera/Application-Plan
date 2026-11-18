# 项目谱系、当前开发线与学术叙事 — 2026-11-18

> **本文件是 Application-Plan 中项目身份、生命周期和当前开发状态的权威定义。** DS-Hns、Codex Boss、Utopia 均为已完成并冻结的历史项目；当前主动开发的是 Celestial 系列。任何申请材料都必须区分历史成果、当前开发、已实现能力和已独立验证能力。

## 项目关系

```text
DS-Hns（历史项目；已完成/冻结） ─┐
                                 ├──> Utopia（整合后继；已完成/冻结）
Codex Boss（历史项目；已完成/冻结）┘                 │
                                                     └──> Celestial 系列（当前主动开发）
```

| 项目 | 当前身份 | 可使用的对外描述 | 证据边界 |
|---|---|---|---|
| [DS-Hns](https://github.com/zhiheng-zhang-Mera/DS-Hns) | 历史项目；已完成并冻结 | 持久编码任务执行、检查点、故障中断与恢复机制 | 不写成当前仍在开发；不把受控场景结果扩大为通用自治证明 |
| [Codex Boss](https://github.com/zhiheng-zhang-Mera/Codex-Boss) | 历史项目；已完成并冻结 | 多 Agent 编排、任务契约、证据治理与完成判断 | 不写成当前仍在开发；不声称全部治理机制均经过真实用户长期验证 |
| [Utopia](https://github.com/zhiheng-zhang-Mera/utopia) | 历史项目；整合前两项成果，已完成并冻结 | 多设备软件系统；有界 Windows worker 执行与 Android/Web 控制路径 | 不写成当前主开发项目；不把有限设备/场景验收扩大为全平台或完整消费级部署 |
| [Celestial-Throne](https://github.com/zhiheng-zhang-Mera/Celestial-Throne) | Celestial 系列当前主要平台之一；持续开发中 | Utopia 的后继重构与迭代，面向多设备、服务、Agent 和外部应用的个人软件工作台 | 当前已有本机真实运行与部分设备链路证据；双机、外部 Provider、公开远程访问、跨平台发布等仍有明确未验收项 |
| [Celestial Research Intelligence](https://github.com/zhiheng-zhang-Mera/Celestial-Research-Intelligence-CRI) | 当前系列中的独立软件项目；持续开发 | 本地优先的混合研究工具，涉及本地模型、任务拆解、隐私网关、外部子任务治理与研究历史 | 已有真实本地模型运行证据；真实外部 Provider、真实 Jev API、Android 真机及第二物理主机等按项目状态表区分，不概括为全部通过 |
| [Celestial Finance](https://github.com/zhiheng-zhang-Mera/Celestial-Finance) | 当前系列中的领域软件项目 | 本地个人投资记账、资金池、策略研究和 AI 辅助分析 | 本机使用链路已有验证；不连接券商、不自动交易；不能把本地验证等同于外部账户/自动交易验证 |
| [Celestial Smart Glass](https://github.com/zhiheng-zhang-Mera/Celestial-Smart-Glass) | 当前系列中的探索性研究/开发方向 | 可穿戴沟通辅助、字幕、发言人关联与用户可控交互 | 当前以研究计划和工程设计为主；无运行原型、硬件兼容性实测或参与者研究完成声明 |
| [Celestial Drug Simulator](https://github.com/zhiheng-zhang-Mera/celestial-drug-simulator) | 当前系列中的领域模拟软件 | 证据治理的药理机制模拟与研究界面 | 已有本机 UI、测试和安装器证据；不声称真实药物联用预测、临床验证或医疗用途 |
| Celestial Books（Mission / Design / Function / Evidence / Verification / Operations / Release） | 当前系列的工程治理与证据档案 | 分别管理任务、设计、功能登记、证据、独立验证、运维和发布生命周期 | 这些仓库主要保存治理文档与索引，不是产品运行时，也不能单独证明功能已实现 |

## Celestial 系列的统一定位

Celestial 是一个**多仓库、多方向的软件开发系列**，不是一个已经全部交付的单体产品。项目方向包括：

- Agent 与研究智能：多 Agent 编排、本地优先研究、任务执行与研究工作流；
- 软件工程基础设施：模块化架构、跨设备/服务集成、权限与接口边界、可恢复执行；
- 知识与证据管理：知识档案、功能登记、任务治理、可追溯证据与独立验证；
- 领域应用：个人金融软件、可穿戴/HCI 研究，以及科学/药理机制模拟等。

**共同主线是软件开发与系统工程，而不是某个单一垂直领域。** 研发优先级是先形成可实际使用的软件入口和完整工作流，再以可复现构建/测试、失败路径检查、运行证据和必要的独立验收确认可靠性。设计文档、代码存在、局部测试通过、真实运行、独立验收是不同状态，不可混写。

## 对外申请材料的状态规则

1. **当前项目：** 使用 “I am currently developing the Celestial series...” 描述当前工作。可介绍系列覆盖多个方向，但要明确软件开发/系统工程是共同核心。
2. **历史项目：** DS-Hns、Codex Boss、Utopia 统一使用过去时，并标记 completed/frozen；可作为已完成工程经验和论文研究来源。
3. **论文状态独立：** DS-Hns 与 Boss-A2 的论文稿件是独立学术成果，不因源项目冻结而改变投稿状态；预印本、期刊在审和期刊录用必须分别标记。
4. **功能声明按组件和证据：** 只写实际实现且与目标申请相关的 2–4 项能力；标注真实运行范围、平台和限制。规划中的 Smart Glass、尚未完成的跨机/外部 Provider 能力不得写成已验收。
5. **禁止整体升级：** 不得因某一个子项目 PASS 就称整个 Celestial 系列完成、投产或通过独立验证。

## 可复用英语措辞

> I previously completed and froze DS-Hns and Codex Boss, then integrated their work into Utopia, which is also completed and frozen. I am now developing the Celestial series, a multi-repository software portfolio spanning agentic research tools, knowledge and evidence systems, personal-finance software, and exploratory wearable and scientific applications. Software engineering is its common core, with an emphasis on building usable systems and validating reliability through reproducible tests, runtime evidence, and real workflows. Implementation and verification status are tracked per component rather than generalized across the series.

## 维护边界

- 历史 DS-Hns、Codex Boss、Utopia 仓库保持冻结，不为更新申请材料而改写历史状态。
- Celestial 主平台与各子项目的实现状态以对应仓库的最新代码、README、证据与验证报告为准。
- Application-Plan 的研究画像、导师路由、CV 和 Research Statement 应同步采用本文件的项目生命周期措辞。
- 不回改已经发送的历史 CV 附件或邮件；新申请/新导师材料从当前母版重新生成。
