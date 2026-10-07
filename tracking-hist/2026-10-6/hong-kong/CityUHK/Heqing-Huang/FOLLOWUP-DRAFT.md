# Follow-up Draft — Rev.2 (2026-10-07) — NOT SENT

> **发送规则：只发送 English Version。中文翻译仅供内部校对，不进入邮件正文。**  
> Evidence basis: `_shared/UTOPIA-SNAPSHOT.md` Rev.2 + updated Bachelor/Master CSV grading scales.  
> PCF wording is intentionally bounded: **verified development candidate ≠ completed/merged/physically accepted fabric**.

**To:** heqhuang@cityu.edu.hk  
**Subject:** [Use existing thread subject]

## English Version

Dear Professor Huang,

I wanted to briefly follow up on my earlier message in case the topic is still relevant to your current PhD intake.

Since that note, the systems/evaluation side of my work has become substantially more concrete. Utopia/Digital City now has a main-branch research path covering controlled scenarios, fault injection, replay/ablation, metrics, and artifact export. A newer Personal Compute Fabric development candidate has also undergone opposite-host verification.

One result is particularly relevant to why I remain interested in your work on software security and program analysis. During cross-host review, a real Windows telemetry path was found to publish a platform placeholder zero as an observed CPU measurement. The repair was independently falsified and re-tested, while remaining uncertainty was kept explicit rather than hidden. The PCF candidate also enforces caller binding, idempotency, and fail-closed control boundaries.

This has strengthened my interest in treating tool-using agents and their runtime as security/testing targets: not only whether an agent produces the intended output, but whether measurement, capability, and recovery paths can be trusted under adversarial or failure conditions.

If you are still considering PhD students in this area, I would be very happy to discuss fit. I have a refreshed CV available if useful.

Best regards,
Zhiheng Zhang

---

## 中文翻译（内部对照，不发送）

黄教授您好：

想简短跟进一下我之前的邮件，如果这一方向仍与您当前博士招生相关。

自上次联系后，我的系统与评估部分已经明显更加具体。Utopia/Digital City 的 main 现在已经包含受控场景、故障注入、回放/消融、指标和 artifact 导出的研究链；新的 Personal Compute Fabric 开发候选也完成了异机 verification。

其中一个结果尤其说明了为什么我仍然很关注您在软件安全与 program analysis 方面的工作。跨机复检真实发现 Windows telemetry 路径把平台固定占位 0 错误发布成 observed CPU measurement；随后修复经过独立证伪与复测，而剩余不确定性被明确保留，而不是被掩盖。PCF 候选同时也验证了 caller binding、幂等和 fail-closed 控制边界。

这进一步强化了我对 tool-using agent 及其 runtime 作为 security/testing target 的兴趣：不仅要判断 agent 是否给出预期结果，还要判断其测量、能力和恢复路径在对抗或故障条件下是否可信。

如果您目前仍考虑这一方向的博士生，我非常希望继续讨论。我也已经有刷新后的 CV 可供参考。

此致
Zhiheng Zhang
