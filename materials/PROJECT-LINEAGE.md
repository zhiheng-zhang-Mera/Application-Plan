# 项目谱系、完成状态与学术叙事 — 2026-10-09 用户修正确认

> **本文件是 Application-Plan 中项目身份/谱系的权威定义。** 与旧的“Utopia 正在建设，Boss/Hns 是并列当前项目，Celestial 是另外一个无关平台”叙述冲突时，以本文件为准。本文件记录的是用户确认的工程状态；每个能力的实机/集成/性能证据仍需按 GitHub 实际报告核查。

## 正确的连续演进关系

```text
DS-Hns（前代；已完成并冻结） ─┐
                               ├──> Utopia（融合前代成果；已完成并冻结）
Codex Boss（前代；已完成并冻结）┘                 │
                                                   └──> Celestial（规划中的 Utopia 重构／迭代版）
```

| 项目 | 用户明确确认的阶段 | GitHub 参照（供历史证据核对） | 对外陈述可使用 |
|---|---|---|---|
| [DS-Hns](https://github.com/zhiheng-zhang-Mera/DS-Hns) | **过去完成、已冻结的独立前代** | [main SHA eeb57ca5](https://github.com/zhiheng-zhang-Mera/DS-Hns/commit/eeb57ca5c2c56bdf2e58c1216c610b4b9fbc973b) | Completed and frozen predecessor; durable long-horizon execution/recovery experience |
| [Codex Boss](https://github.com/zhiheng-zhang-Mera/Codex-Boss) | **过去完成、已冻结的独立前代** | [main SHA 8df428ea](https://github.com/zhiheng-zhang-Mera/Codex-Boss/commit/8df428eaa437a409368401e95194e40266b83080) | Completed and frozen predecessor; multi-agent orchestration/evidence governance |
| [Utopia](https://github.com/zhiheng-zhang-Mera/utopia) | **融合 DS-Hns 与 Codex Boss 成果、已完成并冻结的后继项目** | [main SHA 944f47dd](https://github.com/zhiheng-zhang-Mera/utopia/commit/944f47dd6c7e18b3388b6d769dbbb6dddbe74f00)；[Digital-City 控制面](https://github.com/zhiheng-zhang-Mera/Digital-City) | Completed and frozen integrated successor; main software project evidence |
| [Celestial / Celestial-Throne](https://github.com/zhiheng-zhang-Mera/Celestial-Throne) | **规划中的 Utopia 重构与迭代版本，尚未完成** | [初始项目 SHA b21d8040](https://github.com/zhiheng-zhang-Mera/Celestial-Throne/commit/b21d8040a6c0074965c4a7d4d8afc8a62a434948) | Planned redesign/refactoring and next iteration of Utopia, not a shipped separate platform |

## 完成/冻结 ≠ 所有能力全部物理验收

1. “已完成并冻结”是用户确认的**项目生命周期状态**，不是虚构特定 GitHub Release/tag 的名称，也不是“所有设想功能都已完成”。
2. Utopia **确实融合了 DS-Hns 与 Codex Boss 的成果**，对外可以称 integrated/fused successor；但某个原 Boss/Hns 模块在 Utopia 内是否有特定 runtime connector、是否端到端接线、是否在指定实机上完成验收，必须由 Utopia 当前冻结 SHA、City/PCF/REX 报告逐项佐证。不能把“融合”解读为所有代码逐字迁移或所有接口在任何设备环境都通过测试。
3. Utopia 冻结版本拥有有界的 Windows x2 + Android 控制、PCF/REX 相关代码与验证；不能因此说专用眼镜/指环、双服务器物理自动接管、Linux worker/手机 worker、完整消费级部署或真人长期用户研究均已验证。
4. Celestial **不是**与 Utopia 并列的独立“另一项目”；它是 Utopia 的规划中**下一代重构和迭代方向**，以软件系统为主，可增设跨专业档案室/知识区或融合导师课题；在初始源码阶段不能写 completed/shipped。
5. 三个冻结项目可分列 CV 中的 **Completed & Frozen Projects** 或形成一个递进叙事：DS-Hns + Codex Boss → integrated Utopia → planned Celestial。不要写 “DS-Hns is building”, “Boss explores” 或 “Utopia is being built”，不得在 CV/邮件中暗示冻结项目会持续迭代。
6. 论文和 artifact 是**另一独立状态维度**：冻结代码/完成项目不等于 peer-reviewed publication；任何 Hns/Boss 稿件只有真实公开记录或录用证明才可按正确身份列出。

## 可复用的英语措辞

**项目关系（完整）：**
> I previously completed and froze DS-Hns and Codex Boss as separate projects. I subsequently integrated their work into Utopia, a completed and frozen multi-device software platform. Celestial is my planned redesign and next iteration of Utopia, intended to support further research rather than a system I claim to have finished.

**精简版（导师套磁更合适）：**
> My completed and frozen Utopia platform integrates earlier work from my completed DS-Hns and Codex Boss projects.

**Future plan（在具体需要时）：**
> I plan to redesign and extend Utopia through Celestial, while adapting the research implementation to the supervisor's existing systems.

本文件不要求每封套磁都列所有仓库；只要求**一旦提及任一项目，时间状态和项目谱系正确**。

## 维护范围

- 改动现在的画像、项目路由、规则、六导师的最新版本邮件/CV/Research Interest、SUTD Jan 2027 SOP、UM Li Li warm lead 当前版资料。
- **不回改** `tracking-hist/2026-10-6/` 历史快照，也不改 DS-Hns/Boss/Utopia 冻结仓库本身。
- 不触发 PDF/CI 构建，不修改或发送 Gmail；Shawn Shan 与 Yuchen Yang 保持 HOLD。
