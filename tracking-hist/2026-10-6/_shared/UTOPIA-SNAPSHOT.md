# Utopia / PCF 证据快照 — Rev.2（2026-10-07）

> 本文件更新 2026-10-6 素材包的证据基础。原始包未发送；本次只用于第二轮材料修订。

## 当前身份

- **Utopia main:** `cc799234e7daa3d8ccfde5673b9d07ccb2376742`
- **Digital-City main:** `78d9efe4774d257678ad09c7c3cfb95d6d352306`
- Utopia current-main CI: success
- reciprocal linkage: OK

相对 2026-10-06 初始素材快照，Utopia main 已前进 43 个提交。

## Main 上现在可以安全声称

### 产品 / 多设备

- Android + Web control surfaces drive a real City runtime through a platform-neutral protocol.
- V0.2 / Capability Bridge V0.3 / V0.3 hardening 保持已验收。
- **MESH-301 accepted**：Alien + Mech 两个真实 Windows worker 与 Android control surface 在同一 canonical City 上完成 strict target-device routing 与跨机 Formal Review。
- 生命周期可用性、typed errors、显式 degraded-state / fallback 继续作为安全边界。

### Research & Evaluation Fabric

Digital-City 当前权威状态：

- REX-801 Experiment Manifest + Registry — COMPLETE
- REX-802 Trace / Provenance / Metrics Foundation — COMPLETE
- REX-803 Scenario Runner + Repetition Engine — COMPLETE
- REX-804 Fault Injection + Recovery Probes — COMPLETE
- REX-805 Trace Replay + Ablation — COMPLETE
- **REX-806 Metrics + Research Artifact Export — COMPLETE，并已合入 current main**
- REX-807 Research Control Surface — **development complete at `9ad888279be07220fe7ac7d91e419e8fe69fc439`，等待对侧实体主机正式复检**
- REX-890 final reproducibility freeze — 等待 REX-807 验收

因此现在可以比上一版邮件更强地写：

> Utopia contains a reproducible research/evaluation path covering controlled scenarios, fault injection, replay/ablation, metrics and research-artifact export.

但不能把 REX-807 / REX-890 写成已经正式验收完成。

## REX-807 分支的新能力（**开发完成，未正式验收**）

分支：`rex/REX-807-mech-research-control-surface @ 9ad8882`

当前开发证据包括：

- Research 页面不污染普通主导航；
- 实验路径可通过真实 Web UI 使用，而不是要求 console/raw API；
- JSON artifact / metrics CSV 有真实可操作的 Export 控件，并校验下载字节；
- Danger Zone 的 confirmation 是实际 gate，而不是提示文字；
- metric name / value / unit / unreadable reason 能真实渲染；
- Android 已接只读 research observation surface；
- 9 处源码突变均能把测试打红。

邮件只允许写：
- “a research control surface is implemented and under opposite-host review”
- “development is closed / formal acceptance pending”

禁止写：
- “REX-807 accepted”
- “Research Fabric v1 fully frozen”

## PCF：不再只是“未来概念”，但仍不能写成已完成产品

### PCF-700

- ownership/reality audit 已由对侧物理主机 **ACCEPTED**；
- 明确测量哪些既有接口真正 LIVE_WIRED、哪些只是 component/test evidence；
- 保留 “two-host verified / origin-agent consumed” 等未证明层级为空，而不是自动升级。

### PCF-701

- 已落地真实 resource observation / telemetry contract；
- missing/NaN/negative/out-of-range 不会被填成 0；
- CPU/RAM、memory/disk facets、path-scoped RTT、actual byte-transfer throughput、queue source、runtime occupancy 均有明确“测得/未知/不支持”语义；
- Windows 上曾出现 `os.loadavg()=[0,0,0]` 被误报为 observed CPU 的真实缺陷；
- 对侧提出修复 `cf07f4a...`，Mech 已独立复检 **ACCEPTED**；
- 该修复候选仍不等于 PCF main merge；
- Windows CPU 可用率实测约六成，未测时明确保留 UNKNOWN，而不是美化为稳定可用。

### PCF 700–728 完整开发候选

候选：
- Utopia `pcf/full-flow-alien-pending-verification-20261007 @ 998440c7772cc032d012b457c2a59cd1059826c0`
- 第二物理主机 Mech 已完成 **SINGLE_BATCH_OPPOSITE_HOST_VERIFICATION**

当前最强的可复用事实：

- **VERIFIED AS A DEVELOPMENT CANDIDATE**
- 真实本机 CPU executor pilot（不是 fixture 恒真回调）
- canonical Task → COMPLETED / Action → SUCCEEDED
- resultRef digest 与 exact-digest consumption acknowledgement
- idempotency / caller-binding / fail-closed default control
- 两台实体主机在同一冻结 SHA 上独立运行，`cpu-sort` / `cpu-sum` 得到逐字节一致的 result digests，且 PID 不同
- 冻结 study 对 dirty source 会 fail-closed
- 候选包含从 resource telemetry / placement 到 execution-provider contract、local controls、origin-agent remote-job bridge 等完整设计/实现面

**必须同时写出的边界：**

- programme completion = NOT ESTABLISHED
- main merge = NOT DONE
- physical acceptance = NOT_RUN
- real Mech↔Alien authenticated transfer / provider execution = NOT ESTABLISHED
- phone worker / full restart-SLO matrix / model runtime + HA = NOT ESTABLISHED
- origin-agent remote result consumption 的完整真实闭环仍属于待验收边界

所以邮件可以写：

> a complete PCF development candidate now exists and has passed opposite-host candidate verification; I treat it as a verified candidate rather than a completed/merged fabric.

不能写：

> PCF is complete / deployed / fully validated across devices.

## 对不同导师的当前最佳证据选择

### Ubiquitous / mobile / edge / systems
优先：
- MESH-301
- current-main REX-801..806
- PCF-700 accepted audit
- PCF-701 honest telemetry
- PCF full-flow verified development candidate
- 明确保留 remote/provider/phone/HA 未验收边界

### Trustworthy / security
优先：
- caller binding
- exact digest consumption
- idempotency
- fail-closed default
- explicit UNKNOWN rather than fabricated zero
- fault injection / replay / independent cross-host verification

### AI4SE / coding agents
优先：
- Hns/Boss
- REX controlled failures + replay/artifact evidence
- PCF executor/provider/origin-agent bridge 只写成 verified development candidate / pending physical validation

### Human-agent
优先：
- confirmation / fallback / user control
- REX-807 progressive-disclosure research UI 仅写 development complete / review pending
