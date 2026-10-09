# 2027 PhD 研究画像 — 当前权威入口（2026-10-09）

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

## 个人项目与现有可验证事实（截至 2026-10-09）

| 证据对象 | 已有事实 / 可在申请材料中表述 | 不得推导的结论 |
|---|---|---|
| [Utopia main](https://github.com/zhiheng-zhang-Mera/utopia/commit/944f47dd6c7e18b3388b6d769dbbb6dddbe74f00) | 两 Windows worker + Android 控制端的有界三端运行/目标设备路由；Android/Web 控制；相关 PCF/REX 代码已集成，main 对应 [CI success](https://github.com/zhiheng-zhang-Mera/utopia/actions/runs/37747311973) | 不能说完整消费级 wearable assistant、双服务器主备或所有多平台场景已实体验收 |
| [Digital-City 4-in-1 报告](https://github.com/zhiheng-zhang-Mera/Digital-City/blob/main/mission-book/reports/4IN1-ACCEPTANCE/README.md) | PCF 700–728 整包验收，真实跨 Windows 主机执行/可核对返回 digest；部分分项验证有 Owner 豁免 | 不得写为 Linux / 手机 worker、所有物理矩阵、真实 LLM 闭环全部通过 |
| [REX-890](https://github.com/zhiheng-zhang-Mera/Digital-City/blob/main/mission-book/finished/completed-2026-10-08/research-strengthening/README.md) | 以有界范围完成独立复现、实验收据/trace/join 验证与限定的研究评估工作；REX 后续整合由产品 main 记录 | 不等于所有自然语言 Agent 结论、Android 实验或长期用户研究完成 |
| [DS-Hns](https://github.com/zhiheng-zhang-Mera/DS-Hns) | 持久任务生命周期、隔离、重启恢复和代码任务执行研究工程 | 不是已经被独立广泛验证的通用自治能力 |
| [Codex Boss](https://github.com/zhiheng-zhang-Mera/Codex-Boss) | 多 Agent 编排、证据治理、完成判断与可审查的故障留存 | 不能说全部治理机制或自进化能力已获正式用户验证 |
| [Celestial-Throne](https://github.com/zhiheng-zhang-Mera/Celestial-Throne) | **未来主平台/研究承载愿景**，计划建多领域、跨学科知识档案室和导师课题独立区域；可与导师项目融合 | 当前初始仓库/文档初始化，不可叙述为已交付、通过验收的运行产品 |

Utopia 是**现有软件工程证据**；Celestial 是**未来可灵活演进的研究载体**。项目能力随未来提交变化必须实时复验，不能只引用这份申请画像自动升级能力声明。论文候选、preprint 和公开软件证据都不等于 peer-reviewed publication。

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
