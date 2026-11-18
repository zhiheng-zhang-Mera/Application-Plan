# 2027 PhD 研究画像 — 当前权威入口（2026-11-18）

> ## ⚠️ 2026-11-18 项目状态更新（优先于下方旧内容）
>
> **当前主动开发线为 Celestial 系列；DS-Hns、Codex Boss、Utopia 均为已完成并冻结的历史项目。** Celestial 是多仓库、多方向的软件开发系列，软件开发与系统工程为共同核心，强调实际使用工作流和可靠验证。各子项目成熟度不同，必须逐项区分设计、实现、运行和独立验收，不得把整个系列写成已完成或已投产。


> ## ⚠️ 2026-10-31 主线变更（本行优先于下方全文，已二次收敛）
>
> 申请人两次收敛主线：**① Wearable 长程 agent → Reliable Multi-Agent Composite Systems（多智能体复合系统）；② 再收敛为软件工程导向的多智能体复合系统（agentic software engineering）**——依据是投稿目标锁定 **JSS / IST / SQJ**（三本均为软件工程期刊，CCF-B/B/C），产出共同体已从 HCI/ubicomp 转向 SE。
>
> 叙事顺序：**可靠性机制 → 多 agent 编排与复合执行 → 真实结果验收 → 落在 SE 的可测试性 / 可复现性 / 失败可解释**。**wearable / edge 降为场景之一**；相对权重仍可参考下方 C/A/B，但不再作为主线。
>
> 依据：Codex Boss（多 Agent 编排与证据接纳）、DS-Hns（长任务与重启恢复）、Utopia（跨 Windows worker + Android/Web 有界验收）、Digital-City PCF 700–728、Quant-Ultra（实验治理与负结果）、Privacy Lens（fail-closed 与 claim boundary）。
>
> 本文件正文仍是 2026-10-09 的 v1 表述，**下游 CV / SOP / 邮件模板需按 agentic SE 重写**；新旧冲突时以本行为准。结构化版本见 [Search-Table/00](../Search-Table/00-申请人材料基线与门禁.md) 与 [Search-Table/12](../Search-Table/12-高成功率通道与全表修正.md)。

> **由申请人 20 轮研究方向校准确认。** 用于导师筛选、CV/SOP/Research Statement/邮件的研究意图事实源；不是任何软件能力的验收凭证。
> 当前主线：**Reliable Long-Horizon Personal AI Agents for Wearable and Ubiquitous Computing**（面向可穿戴与泛在计算的可靠长期自主个人 AI Agent）。
> 完整决策见 [20 轮研究决策记录](PROFILE-DECISIONS-20Q.md)，英语母版见 [Research Statement](RESEARCH-STATEMENT-MASTER.md)，考试边界见 [考试准备门禁](EXAM-READINESS-POLICY.md)。

## 研究身份与相对权重

- **C：可穿戴与智能终端 / Ubiquitous Computing — 45%**；其中可穿戴设备 **70%**（眼镜、手表、头盔、指环等），智能空间 **30%**（含复合 VR 娱乐室）。
- **A：异构/边缘计算系统 — 30%**，承担长期任务执行的计算、恢复、可观测与跨设备连续性。
- **B：自主 AI Agent — 25%**，负责理解授权目标、拆解、执行、异常处理及结果验证。
- 以上是研究覆盖的相对兴趣，不是论文篇数或工时配额。**主要原创问题**是长期任务可靠完成，穿戴环境是首要应用和实验场景。
- **导师方向优先，研究切入点灵活**：愿加入导师现有系统、调整或重构个人平台，但不主动转向纯算法、机器人控制/本体、芯片/电路设计。

## 消费级使用价值与研究方法

评价顺序：**真实功能价值 > 稳定性/无缝协同 > 低延迟与即时响应**。软件系统机制与真实体验双证据链：可复现实验、故障注入/消融/基线对照 + 真实设备上的完整结果验收；必要时对真实参与者开展经适当审查的用户研究。模拟不代替无法完全模拟的环境扰动或低视力、色觉差异、ADHD 相关使用体验；无证据不声称验证通过。以普通消费用户为主，不以特定障碍或医疗诊断为主课题。

研究问题：
1. **RQ1 Goal-grounded autonomous execution**：开工前将终局目标、范围、验收条件和例外授权表达清楚，避免过早定论、目标漂移及表面成功。
2. **RQ2 Globally consistent bounded replanning**：在授权、成本和风险边界内自主调整实现方案、处理故障，调整前检查现有成果、依赖链与后续计划；越权须说明利弊并申请授权，拒绝后寻找替代路线。
3. **RQ3 Real-world outcome-grounded validation**：通过真实设备任务结果而不只是代码编译/单测判断完成。不得把人工用户变成常规测试员；用户可随时查看、修改方向、暂停或终止。

## 目标系统架构（研究愿景，不是现有产品完工声明）

- **任务授权自治**：授权一个终局目标后，Agent 尽可能端到端自行规划、执行、修复和验收；只升级真正需要用户选择的事项，拒绝后可在原授权内重规划。
- **中心式个人计算**：配置好的个人服务器是主计算和协调中心，第二服务器日常互监并在主机故障时尝试自动接管；需要避免网络分区下的双主问题。普通 PC 是需用户批准的按需扩容资源，不是常规自动征用的并列节点。
- **轻终端独立降级**：眼镜、手表、指环、手机主要用于感知、交互和最基本离线能力；失联时有限离线功能与临时缓存，复杂任务等待服务器恢复，不假称大型计算能在穿戴端执行。
- **软件优先硬件辅助**：优先购买与连接现成设备；必要时开发板和 3D 打印补充原型；不以电路、芯片、新传感器或机器人控制为主要贡献。
- **感知 B/C 各 50%**：轻量低功耗常驻 + 明确授权范围内的深度/持续情境理解；长期开启多模态理解不等于全天永久录音录像。
- **记忆知识**：AI 自动提炼观察，按领域/权限归档，在适用授权下保存并定期提醒用户审查；保留来源、纠错、失效与依赖安全删除能力。
- **个性化 A60/B30/D10**：显式偏好为默认主权威；周期性观察提出改进建议；小比例后台自我演化与建议同期汇报。自主实验、独立验证允许；**正式上线须用户明确批准**。允许卸载知识、策略、功能、界面，但必须先审查连锁影响，避免破坏其他模块并明示高风险依赖。

## 项目谱系与当前开发线（2026-11-18）

**DS-Hns + Codex Boss（已完成/冻结的历史前代）→ Utopia（整合后继，已完成/冻结）→ Celestial 系列（当前主动开发）。** 完整生命周期和对外措辞见 [PROJECT-LINEAGE.md](PROJECT-LINEAGE.md)。

Celestial 是多仓库、多方向的软件开发系列，覆盖 Agent/研究智能、知识与证据管理、个人金融软件、可穿戴/HCI 探索及科学模拟等应用。**共同主线是软件开发与系统工程**，侧重形成可实际使用的入口和工作流，并通过可复现测试、失败路径检查、运行证据及独立验收验证可靠性。各仓库成熟度不同，不得将整个系列概括为已完成或已投产。

| 证据对象 | 可在申请材料中表述 | 不得推导的结论 |
|---|---|---|
| [Celestial-Throne](https://github.com/zhiheng-zhang-Mera/Celestial-Throne) | 当前主要平台之一，持续开发；2026-11-13 README 记录 Windows 本机桌面/独立运行时、Android 实机经 ADB reverse 的移动控制入口、子项目真实启动和有界运行证据 | 双物理主机正式验收、外部模型 Provider、公开远程访问、macOS/Linux 发布和全系列完成均未证实 |
| [Celestial Research Intelligence](https://github.com/zhiheng-zhang-Mera/Celestial-Research-Intelligence-CRI) | 当前本地优先研究工具；已有真实本地模型研究流程与本机 UI/安装/测试证据 | 真实外部 Provider、Jev API、Android 原生真机和第二物理主机不能写成已通过 |
| [Celestial Finance](https://github.com/zhiheng-zhang-Mera/Celestial-Finance) | 当前个人金融软件；本地账本、策略研究、分析工作流已有分阶段实现和本机验证记录 | 不连接券商、不自动下单；不声称自动交易或全外部数据链路已验证 |
| [Celestial Smart Glass](https://github.com/zhiheng-zhang-Mera/Celestial-Smart-Glass) | 可穿戴/HCI 研究方向与开发计划 | README 明确无运行原型、硬件兼容性实测、招募数据或伦理批准，不得写成已完成产品 |
| [Celestial Drug Simulator](https://github.com/zhiheng-zhang-Mera/celestial-drug-simulator) | 证据治理的领域模拟软件；已有本机 UI、测试与安装器证据 | 不做真实组合预测，不是临床验证产品，不提供诊断或剂量建议 |
| Celestial Books（Mission / Design / Function / Evidence / Verification / Operations / Release） | 任务、架构、功能、证据、独立验证、运维和发布治理 | 文档登记不等于对应运行时功能已实现或通过验收 |
| [Utopia](https://github.com/zhiheng-zhang-Mera/utopia) | 已完成并冻结的历史融合后继；有界 Windows worker + Android/Web 控制路径和历史验收材料 | 不作为当前开发项目；不把有界验收扩大为所有设备/场景完成 |
| [DS-Hns](https://github.com/zhiheng-zhang-Mera/DS-Hns) / [Codex Boss](https://github.com/zhiheng-zhang-Mera/Codex-Boss) | 已完成并冻结的历史前代；分别提供持久任务恢复、Agent 编排与证据治理经验，也是两篇研究稿件的项目来源 | 不写成当前仍在开发，也不以项目冻结推导所有能力均已独立验证 |

项目生命周期与功能证据是两个维度。Celestial 系列处于持续开发，不代表每个子项目都处于相同阶段；代码、设计、用户可见入口、真实运行和独立验收必须分别标记。论文、预印本与项目完成状态也相互独立。
## 已确认申请偏好及当前六位导师

- **英语/GRE**：继续优先并要求适用的英语授课豁免和 GRE 不要求/可豁免；不主动承担新考 TOEFL/IELTS/GRE 的负担。
- **其他考试**：允许入学面试、招生考试及在读 QE / Comprehensive，前提是**知晓时间后准备窗口充足，考核范围可预测，准备无需大范围重温多学科或自学大量新知识**。不因“有考试”自动降级或淘汰；证据不足标 UNKNOWN，见 [考试策略](EXAM-READINESS-POLICY.md)。
- 六位继续评估：CityUHK Zhenjiang Li、HKUST Mo Li、Concordia Peter Chen、SUTD Ruochen Zhao、PolyU Yu Liu、CUHK James Cheng；研究方向排序与申请门槛分开判断，不构成录取概率。
- Dartmouth Shawn Shan 与 Penn State Yuchen Yang：用户明确 **HOLD**，不得自动加入发送池或更新/发送 Gmail。
- **当前绝无邮件发送授权**；本次 GitHub 文件写入不代表 Gmail 草稿或邮件附件已同步。

## 对外申请叙事规则

- 通用英语主张：**I want to study reliable, goal-grounded long-horizon AI agents in wearable and ubiquitous computing, using real-device outcomes to evaluate systems mechanisms.**
- 每封邮件选最相关的 1–2 个已验证项目，以**问题 → 证据 → 局限/反例 → 拟研究问题 → 适配导师项目**组织；不要每封都复述整套 Celestial 宇宙架构。
- 不必主动写 GRE/QE 偏好到导师研究兴趣邮件；把考试负担留在内部申请 gate。
- 详见 [Project Positioning](project-positioning.md) 与 [20Q 校准记录](PROFILE-DECISIONS-20Q.md)。
