# Email Draft — Rev.2 (2026-10-07) — NOT SENT

> **发送规则：只发送 English Version。中文翻译仅供内部校对，不进入邮件正文。**  
> Evidence basis: `_shared/UTOPIA-SNAPSHOT.md` Rev.2 + updated Bachelor/Master CSV grading scales.  
> PCF wording is intentionally bounded: **verified development candidate ≠ completed/merged/physically accepted fabric**.

**To:** wang-chengpeng@nus.edu.sg  
**Subject:** Prospective PhD student — agentic software engineering and reliable coding agents

## English Version

Dear Professor Wang,

I am completing a research Master's in Computer Science at the University of Melbourne after a BSc in Computer Science at UBC. I am interested in the RISE Lab's work on program analysis, agentic software engineering, and agent security because it maps directly to the reliability problems I encounter in long-running coding agents.

DS-Hns studies repository-level execution with durable task state and restart recovery. Codex Boss studies evidence-based acceptance. Utopia/Digital City now contributes a stronger experimental layer: its main branch supports controlled scenarios, fault injection, replay/ablation, metrics, and research-artifact export.

The newer PCF candidate also makes delegation semantics explicit. Its development candidate defines execution-provider boundaries and an origin-agent remote-job bridge, and opposite-host verification has exercised caller binding, idempotency, exact-digest result consumption, and local executor isolation. I am not treating the remote-agent bridge as physically accepted yet; the real cross-host provider path remains an open validation boundary.

The research problem I would like to explore is how program analysis can observe an agent's evolving repository and execution state early enough to detect unsafe trajectories before weak results are accepted or returned to the originating agent.

I have attached a short research-problem note with two concrete directions around state-aware analysis and evidence-preserving recovery, together with a tailored CV.

Best regards,
Zhiheng Zhang

---

## 中文翻译（内部对照，不发送）

王教授您好：

我目前正在墨尔本大学完成计算机科学研究型硕士，本科毕业于 UBC。我对 RISE Lab 在 program analysis、agentic software engineering 和 agent security 方面的研究非常感兴趣，因为这些问题与我在长程 coding agent 中遇到的 reliability 问题直接对应。

DS-Hns 研究 repository-level execution、持久任务状态和重启恢复；Codex Boss 研究基于证据的验收。Utopia/Digital City 现在还提供了更强的实验层：其 main 已支持受控场景、故障注入、回放/消融、指标和 research-artifact 导出。

新的 PCF 候选也让 delegation semantics 更加明确。其 development candidate 定义了 execution-provider boundary 和 origin-agent remote-job bridge；异机 verification 还验证了 caller binding、幂等、exact-digest result consumption 和本机 executor 隔离。我不会把 remote-agent bridge 写成已经完成物理验收；真实跨机 provider path 仍是开放验证边界。

我希望研究的问题是：program analysis 如何在长程 agent 工作过程中尽早观察 repository 与 execution state，及时识别危险轨迹，而不是等到薄弱结果已经被验收或回传到 originating agent 后才判断。

我已经准备了简短 Research-Problems 文档，其中列出 state-aware analysis 与 evidence-preserving recovery 两个具体方向，并附有定制 CV。

此致
Zhiheng Zhang
