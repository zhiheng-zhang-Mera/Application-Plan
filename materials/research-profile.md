# 研究画像

> **当前默认申请画像 — 2026-10-06。** 本文件是内部叙事素材源；目标筛选规则见 `rules/SCREENING.md`。  
> **注意：本文件中文化不影响对外申请材料；实际 CV / SOP / RP / 邮件继续生成英语版本。**

## 核心身份

计算机科学背景的 research engineer，当前主线是构建：

> **面向泛在智能体应用的持久个人计算底座（persistent personal-computing fabric）。**

最强博士方向：

**Ubiquitous / Personal Computing + AI Systems + Distributed / Edge Systems**

核心问题不是“堆了多少功能”，而是：

**异构设备、agent execution、用户控制、provenance 与 recovery 如何组成一个长期可靠的个人计算环境。**

## 主平台 — Utopia

广义新申请默认先用 Utopia。

当前研究安全证据：

- Web + Android 产品面通过 authenticated gateway 集成；
- Rooms / canonical Actions / City tasks 进入统一 action substrate；
- deterministic Ask/Do 支持 ambiguity handling、confirmation 和 manual fallback；
- truthful health/degradation 与 idempotency；
- 曾有一个候选版本被独立验收因真实 Android integration defect 而 REJECT，修复后重新独立验收通过。

### 下一阶段研究扩张

**PCF — Personal Compute Fabric / Heterogeneous Edge Runtime**

计划研究：

- heterogeneous resource telemetry；
- explainable placement / offloading；
- queueing 与 execution policy；
- failure recovery；
- cross-device scheduling；
- experiment / evaluation integration。

**这是下一阶段研究方向，不是已完成功能。**

### 垂直应用

可穿戴眼镜、个人医疗终端、娱乐室等属于平台之上的 vertical applications。除非特定导师就是该领域，否则不让它们替代核心 systems identity。

## 支撑平台 — DS-Hns

以下方向优先 Hns：

- AI4SE / coding agents；
- long-horizon repository execution；
- crash/restart recovery；
- durable task continuation；
- autonomous maintenance / AIOps；
- lifecycle / terminal-state evidence。

研究问题：

> 软件智能体如何跨故障持久化并继续 repository-level 工作，同时避免把“进程还活着”误认为“任务真正完成”？

## 支撑平台 — Codex Boss

以下方向优先 Boss：

- reliable / verifiable agents；
- evidence-based completion；
- governance / adjudication；
- multi-agent orchestration；
- auditability / longitudinal evolution。

研究问题：

> 长时自治系统如何在自身持续演化时，仍能对任务完成给出可检查、可证伪、可信的证据？

## 组合叙事

**Utopia + Hns + Boss = device substrate + durable execution + governance/evidence**

这是目前最强的桥接路线：

- ubiquitous / personal computing；
- heterogeneous edge runtime；
- distributed AI systems；
- wearable / embodied-enabling infrastructure；
- reliable human-agent systems。

## 次级项目

### Privacy Lens

用于 privacy、bounded interpretation、reproducibility、auditability、trustworthy software。

### Quant-Ultra

仅用于 financial ML、temporal validation、non-stationarity 或 decision-system infrastructure。

### Health / AI4Science

只作为 vertical/application route；前提是 systems implementation 与 empirical evaluation 是核心。不要仅因为 health 可以成为产品方向，就转去 theory-heavy biomedical/scientific derivation。

## 当前禁止声称

除非以后有新证据，不得声称：

- PCF 已完成；
- 已做 dedicated wearable / robotics hardware experiment；
- assistant/persona layer 已完成；
- general LLM router 已完成；
- Boss/Hns connector integration 已完成；
- Boss/Hns 已有 accepted peer-reviewed publication。

## 对外写作结构

英语材料统一采用：

**problem → evidence already built → observed failure/limitation → proposed PhD question**

避免：

**project list → feature dump → universal-AI claim**。