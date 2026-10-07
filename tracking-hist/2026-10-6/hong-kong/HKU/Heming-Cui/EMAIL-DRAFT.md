# Email Draft — Rev.2 (2026-10-07) — NOT SENT

> **发送规则：只发送 English Version。中文翻译仅供内部校对，不进入邮件正文。**  
> Evidence basis: `_shared/UTOPIA-SNAPSHOT.md` Rev.2 + updated Bachelor/Master CSV grading scales.  
> PCF wording is intentionally bounded: **verified development candidate ≠ completed/merged/physically accepted fabric**.

**To:** heming@cs.hku.hk  
**Subject:** Prospective PhD student — reliable distributed AI systems and multi-device runtimes

## English Version

Dear Professor Cui,

I am completing a research Master's in Computer Science at the University of Melbourne after a BSc in Computer Science at UBC. I am contacting you because your emphasis on systems building—and on consistency, reliability, and security rather than pure AI modeling—matches how I have been developing my own research.

Utopia/Digital City now provides a real multi-device runtime with authenticated control paths, lifecycle-aware availability, strict target-device routing, and a main-branch research path covering fault injection, replay/ablation, metrics, and artifact export.

The newer PCF work has made the reliability problem much more concrete. Its telemetry layer intentionally reports UNKNOWN rather than inventing values; during opposite-host review, a real Windows defect was found where a platform placeholder zero had been mislabeled as observed CPU usage. The repair was independently re-tested rather than hidden. A complete PCF development candidate has also passed opposite-host candidate verification with caller binding, idempotency, exact-digest result consumption, and byte-identical local CPU outputs reproduced on two physical hosts.

I am keeping the system boundary explicit: the candidate is not yet a merged or physically accepted cross-host fabric. For me, that open boundary is the research opportunity—how heterogeneous personal/edge devices can maintain consistent routing, bounded recovery, and trustworthy state under partial failure.

I have prepared a PDF CV and my bachelor course transcript in line with your instructions, and would be very interested in discussing this systems direction.

Best regards,
Zhiheng Zhang

---

## 中文翻译（内部对照，不发送）

崔教授您好：

我目前正在墨尔本大学完成计算机科学研究型硕士，本科毕业于 UBC。我联系您，是因为您强调真正的 systems building，以及 consistency、reliability、security，而不是单纯 AI modeling；这与我现在研究项目的构建方式非常一致。

Utopia/Digital City 现在已经形成真实的多设备 runtime，包含认证控制路径、lifecycle-aware availability、严格目标设备路由；其 main 上也已经具备故障注入、回放/消融、指标和 artifact 导出的研究链。

新的 PCF 工作让 reliability 问题更加具体。其 telemetry 层明确选择在无法测量时报告 UNKNOWN，而不是编造数值；异机复检中曾真实发现 Windows 平台固定占位 0 被错误标记为 observed CPU usage，之后修复又经过独立复测，而不是把失败记录清掉。一个完整 PCF 开发候选也已经通过异机 candidate verification，验证了 caller binding、幂等、精确 digest 的结果消费，以及同一 SHA 在两台物理主机上复现一致的本机 CPU 输出。

我会明确保留系统边界：该候选还没有合并，也没有完成真实跨机 fabric 的物理验收。对我而言，这个开放边界正是研究机会——异构个人/边缘设备在部分故障下如何维持一致路由、有界恢复和可信状态。

我已经按您的说明准备 PDF CV 和本科课程成绩单，也非常希望进一步讨论这一 systems 方向。

此致
Zhiheng Zhang
