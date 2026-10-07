# Follow-up Draft — Rev.2 (2026-10-07) — NOT SENT

> **发送规则：只发送 English Version。中文翻译仅供内部校对，不进入邮件正文。**  
> Evidence basis: `_shared/UTOPIA-SNAPSHOT.md` Rev.2 + updated Bachelor/Master CSV grading scales.  
> PCF wording is intentionally bounded: **verified development candidate ≠ completed/merged/physically accepted fabric**.

**To:** congthanh_le@sutd.edu.sg  
**Subject:** [Use existing thread subject]

## English Version

Dear Professor Le-Cong,

I wanted to briefly follow up on my earlier message regarding PhD opportunities in trustworthy software engineering with and for AI.

Since that note, the empirical reliability side of my work has become substantially stronger. DS-Hns continues to study long-horizon repository execution with durable task state and restart recovery. Utopia/Digital City now has a main-branch research path covering repeated controlled scenarios, fault injection, replay/ablation, metrics, and research-artifact export.

The newer Personal Compute Fabric work has also produced useful reliability evidence. During opposite-host review, a Windows telemetry path was found to report a platform placeholder zero as an observed CPU measurement. The repair was independently falsified and re-tested, while remaining uncertainty was kept explicit as UNKNOWN. A broader PCF development candidate has also been verified on a second physical host with caller binding, idempotency, and exact-digest result-consumption semantics.

This has reinforced the PhD problem I hoped to explore: how should software/AI engineering systems distinguish “the agent is still running” from “the engineering task is correct,” especially after retries, recovery, tool calls, and multi-stage acceptance?

If you are still recruiting PhD students in this area, I would be very happy to discuss whether this direction could fit your group. I have a refreshed CV available if useful.

Best regards,
Zhiheng Zhang

---

## 中文翻译（内部对照，不发送）

Le-Cong 教授您好：

想简短跟进一下我之前关于 trustworthy software engineering with/for AI 博士方向的邮件。

自上次联系后，我的实证 reliability 部分已经明显增强。DS-Hns 继续研究长程 repository execution，包括持久任务状态和重启恢复；Utopia/Digital City 的 main 现在已经具备重复受控场景、故障注入、回放/消融、指标和 research-artifact 导出的研究链。

新的 Personal Compute Fabric 工作也产生了有价值的 reliability 证据。异机复检真实发现一个 Windows telemetry 路径把平台固定占位 0 错误报告成 observed CPU measurement；之后修复经过独立证伪与复测，而剩余不确定性被明确保留为 UNKNOWN。更完整的 PCF 开发候选也已经在第二台物理主机上验证了 caller binding、幂等和精确 digest 的结果消费语义。

这进一步强化了我最希望研究的博士问题：software/AI engineering system 应如何区分“agent 还在运行”与“工程任务真的正确完成”，尤其是在 retry、recovery、tool call 和多阶段验收之后？

如果您目前仍在这一方向招收博士生，我非常希望讨论是否匹配。我也已经有刷新后的 CV 可供参考。

此致
Zhiheng Zhang
