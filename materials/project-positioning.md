# 项目定位路由

> 更新于 **2026-10-06**。内部说明使用中文；自动生成的申请材料与邮件继续保持英语。

| 导师 / 项目主题 | 主项目 | 支撑项目 | 安全研究切入点 | 避免 |
|---|---|---|---|---|
| **Ubiquitous / personal computing** | **Utopia** | Hns, Boss | 一个 logical personal environment 如何跨异构设备投射，并保留用户控制、provenance、recoverability | 把 Utopia 写成已经完成的 universal assistant |
| **Personal Compute Fabric / heterogeneous edge runtime** | **Utopia → planned PCF** | Hns | telemetry、explainable placement/offloading、queueing、recovery、cross-device policy | 声称 PCF 已完成 |
| **Distributed / edge AI systems** | **Utopia** | Hns, Boss | multi-device action substrate、authenticated gateway、truthful degradation、durable execution、未来 heterogeneous scheduling | 声称尚未验收的 remote / LLM routing 已完成 |
| **Wearable / ubiquitous computing** | **Utopia** | Boss | device-aware personal terminal 与 edge execution 作为 systems substrate | 假装已有 dedicated wearable experiment |
| **Embodied-enabling systems** | **Utopia** | Boss, Hns | action routing、human confirmation、device coordination、runtime reliability | 声称未证明的 robotics/control/RL expertise |
| **Human-agent interaction / end-user control** | **Utopia** | Boss | explicit confirmation、ambiguity handling、user override、inspectable action state | 夸大 persona / relationship layer |
| **AI systems / agent infrastructure** | **Utopia 或 Boss** | Hns | device substrate + orchestration + durable execution + evidence | generic “multi-agent platform” 功能堆砌 |
| **AI4SE / coding agents / autonomous maintenance** | **DS-Hns** | Boss, Utopia | long-horizon execution、crash/restart recovery、task continuation、repository qualification | 把 Hns 写成普通 automation/UI |
| **Agent reliability / verification / governance** | **Codex Boss** | Hns, Utopia | evidence-based completion、adjudication、longitudinal evolution、bounded claims | 声称 strict full-city completion 或 peer-reviewed publication |
| **Trustworthy AI / privacy / governance** | **Boss 或 Privacy Lens** | Utopia, Hns | provenance、bounded claims、reproducibility、auditability | 把 privacy work 写成泛泛 compliance |
| **Financial ML / decision systems** | **Quant-Ultra** | Boss | temporal validation、non-stationarity、auditable decision infrastructure | 以 trading profit 为主叙事 |
| **AI4Science / computational health** | **Utopia 或 Boss** | Hns / domain evidence | 当 systems implementation 是核心时做 reliable scientific/health workflow | 没有基础却硬转 domain-theory-heavy |

## 当前证据边界

### Utopia

可以写：

- Web + Android surfaces 通过 authenticated gateway；
- Rooms / Actions / City-task integration；
- deterministic Ask/Do；
- confirmation / fallback；
- truthful degradation 与 idempotency；
- 独立 reject → repair → accept 的验收历史。

暂时不能写成已完成：

- PCF / heterogeneous edge runtime；
- dedicated wearable hardware；
- complete assistant/persona；
- general LLM router；
- Boss/Hns connectors。

### DS-Hns

可以写：

- long-horizon task execution；
- crash/resume recovery；
- durable continuation；
- qualification / recovery evidence；
- repository-level engineering-agent experimentation。

### Codex Boss

可以写：

- frozen / traceable evidence checkpoints；
- governance / acceptance / completion-evidence research；
- preserved limitations / unresolved states；
- 有证据支持的 multi-agent / evidence orchestration。

未正式接受前不得称其 manuscript / artifact 为 peer-reviewed publication。

## 组合叙事

**Utopia = action 所在的设备/产品底座**  
**Hns = 长时间工作如何执行并跨故障持续**  
**Boss = claim 与 decision 如何治理和验证**

面向 broad systems 申请时，默认 **Utopia first**，再用 Hns / Boss 证明它不是单纯 UI 概念。

## 对外写作规则

保持：

**problem → existing evidence → failure/limitation → next systems question**

禁止：

**I built a universal AI system / everything is complete / the paper is published**。