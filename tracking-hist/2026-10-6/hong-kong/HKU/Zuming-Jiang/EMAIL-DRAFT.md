# Email Draft — Rev.2 (2026-10-07) — NOT SENT

> **发送规则：只发送 English Version。中文翻译仅供内部校对，不进入邮件正文。**  
> Evidence basis: `_shared/UTOPIA-SNAPSHOT.md` Rev.2 + updated Bachelor/Master CSV grading scales.  
> PCF wording is intentionally bounded: **verified development candidate ≠ completed/merged/physically accepted fabric**.

**To:** jzuming.hku@gmail.com  
**Subject:** Prospective PhD student — systems reliability and agentic software infrastructure

## English Version

Dear Professor Jiang,

I am a research Master's student in Computer Science at the University of Melbourne, with a BSc in Computer Science from UBC. I am interested in your work across systems, security, and testing because my recent projects repeatedly expose the same problem: a system can keep running while its state, evidence, or recovery behavior is already wrong.

DS-Hns studies this in long-horizon repository execution. Utopia/Digital City now adds a stronger experimental substrate: on main, its research path covers repeated controlled scenarios, fault injection, replay/ablation, metrics, and research-artifact export.

The newer PCF work produced a concrete example of why I care about this. An opposite-host reviewer found that a Windows placeholder value of zero had been reported as an observed CPU measurement. The repair was independently challenged and accepted, and the remaining instability was preserved as an explicit UNKNOWN rather than converted into a convenient number. A complete PCF development candidate has also been independently reproduced on a second physical host, but I still treat unvalidated remote/provider paths as open.

For a PhD, I would like to study how testing can systematically reveal false-success and silent-corruption modes in agentic and distributed infrastructure, while preserving enough provenance for independent reproduction.

I have prepared a CV and brief research-interest note around this direction.

Best regards,
Zhiheng Zhang

---

## 中文翻译（内部对照，不发送）

姜教授您好：

我目前在墨尔本大学攻读计算机科学研究型硕士，本科毕业于 UBC。我对您在 systems、security 与 testing 交叉方向的研究很感兴趣，因为我的近期项目不断暴露同一个问题：一个系统可以继续运行，但其状态、证据或恢复行为实际上已经错误。

DS-Hns 从长程 repository execution 的角度研究这个问题。Utopia/Digital City 现在则提供了更强的实验底座：其 main 上的研究链已经包括重复受控场景、故障注入、回放/消融、指标和 research artifact 导出。

新的 PCF 工作提供了一个非常具体的例子。异机 reviewer 发现 Windows 平台的固定占位 0 被错误标记成 observed CPU measurement；之后修复被独立攻击和复测并接受，而剩余不稳定性仍被保留为明确 UNKNOWN，而不是为了好看转成一个数字。完整 PCF 开发候选也已经在第二台物理主机上独立复现，但我仍把未验证的 remote/provider 路径明确视为开放问题。

博士阶段我希望研究：如何系统性测试 agentic 和 distributed infrastructure 中的 false-success 与 silent-corruption，并保留足够 provenance，使独立复现成为验收的一部分。

我已围绕这一方向准备 CV 和简短 Research Interest。

此致
Zhiheng Zhang
