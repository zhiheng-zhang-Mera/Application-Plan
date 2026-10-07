# Email Draft — Rev.2 (2026-10-07) — NOT SENT

> **发送规则：只发送 English Version。中文翻译仅供内部校对，不进入邮件正文。**  
> Evidence basis: `_shared/UTOPIA-SNAPSHOT.md` Rev.2 + updated Bachelor/Master CSV grading scales.  
> PCF wording is intentionally bounded: **verified development candidate ≠ completed/merged/physically accepted fabric**.

**To:** nanguan@cityu.edu.hk  
**Subject:** Prospective PhD student — LLM-aided system design and edge-device intelligence

## English Version

Dear Professor Guan,

I am completing a research Master's in Computer Science at the University of Melbourne after a BSc in Computer Science at UBC. Your work on LLM-aided system design and real-time intelligence on edge/device platforms is close to the runtime problem I want to study next.

Utopia/Digital City already spans multiple real devices with accepted strict target-device routing. The important recent change is that my Personal Compute Fabric work has moved from a planned scheduler into an executable development candidate. Its resource layer now has explicit telemetry semantics for CPU/RAM, path latency/throughput, queue sources, and runtime occupancy, with UNKNOWN preserved rather than silently treated as zero.

A complete 700–728 candidate has also passed opposite-host development-candidate verification, including real local CPU execution, idempotency, caller binding, and reproducible result digests across two physical hosts. I am intentionally not claiming that remote cross-host execution is complete; that physical provider path is still an acceptance gap.

The question I would like to study is the boundary between intelligent placement and systems guarantees: an LLM or learned policy may propose where work should run, but the runtime should enforce capability, timing, resource, and recovery constraints, and the resulting decision should be reproducible.

I would be interested in exploring this as a PhD systems project in your group and have prepared a tailored CV.

Best regards,
Zhiheng Zhang

---

## 中文翻译（内部对照，不发送）

关教授您好：

我目前正在墨尔本大学完成计算机科学研究型硕士，本科毕业于 UBC。您在 LLM-aided system design 和 edge/device 实时智能方面的研究，与我下一步希望研究的 runtime 问题非常接近。

Utopia/Digital City 已经跨多个真实设备运行，并通过严格目标设备路由的验收。最近最重要的变化是 Personal Compute Fabric 已经从计划中的 scheduler 进入可执行开发候选阶段。其资源层现在有明确的 telemetry 语义，包括 CPU/RAM、按路径延迟/吞吐、queue source 和 runtime occupancy；无法测量时保留 UNKNOWN，而不是静默当成 0。

覆盖 700–728 的完整候选也已经通过异机 development-candidate verification，包括真实本机 CPU 执行、幂等、caller binding，以及两台物理主机间可复现的结果 digest。我不会把真实跨机执行描述成已经完成；remote provider 路径仍然是待验收缺口。

我希望研究的是 intelligent placement 与 systems guarantee 之间的边界：LLM 或 learned policy 可以提出执行位置，但 runtime 必须强制 capability、timing、resource 和 recovery 约束，并且最终决策应该可复现。

我很希望把这一问题作为博士 systems project 深入研究，并已经准备了对应 CV。

此致
Zhiheng Zhang
