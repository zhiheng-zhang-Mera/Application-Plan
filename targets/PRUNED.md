# Pruned Targets

> 这里放**不是硬性不合格，但目前不值得继续消耗申请时间**的候选。
>
> 新门禁已经扩大到 **AI4SE + agentic AI + AI systems + applied AI4Science**，因此 PRUNED 不再代表“不是软件工程就不合适”。只有在**缺少具体可执行的 implementation/experiment/simulation/data-driven 路线**时才继续 prune。

| 学校 / 项目 | Prune reason | 重洗后为什么仍然移出主候选池 | 重开条件 |
|---|---|---|---|
| Drexel CS PhD | `LOW_ROI_STALE_GENERIC_FIT` | 即使允许 AI4Science，目前候选记录仍只有泛 CS/SE/ML 匹配，没有明确高匹配 AI4SE / scientific-agent / simulation / systems PI 和资金优势 | 找到当前明确招人的 AI4SE / agentic systems / applied AI4Science PI，且 funding/英语/成绩线干净 |
| Stevens CS PhD | `LOW_ROI_STALE_GENERIC_FIT` | 旧版 ML systems / time-series 泛匹配不足以形成具体可执行博士路线；AI4Science 新门禁也没有提供当前具体 PI 证据 | 出现强匹配 PI + 清晰全奖 + 低摩擦申请 |
| Stony Brook CS PhD | `HIGH_COMPETITION_WEAK_SPECIFIC_FIT` | 学校强，但现池中仍缺直接做 AI4SE / coding agents / scientific agents / applied systems evaluation 的具体 PI | 找到明确 implementation/experiment-first PI |
| UMass Amherst CS PhD | `HIGH_COMPETITION_WEAK_SPECIFIC_FIT` | Systems/ML 强，但当前没有比现有目标更直接的 Boss/DS-Hns 或 applied AI4Science 工程路线 | 出现明确招收且研究方式偏系统实现、实验或仿真的 PI |
| UC Riverside CS PhD | `ACADEMIC_ROI_WEAK` | academic-profile 风险仍在，且没有形成足够强的 AI4SE / agentic / AI4Science 工程型导师优势 | 明确 PI 兴趣 + 硬门槛通过 + funding 清晰 |

## 不应放进 PRUNED 的情况

- 明确违反 GRE / 英语 / 成绩 / funding 等硬门槛 → `REJECTED`
- 只差一个可核验条件且 research-method fit 很好 → `WATCHLIST`
- 研究方法合适但流程麻烦 → `BACKUP`

## Research Method 原则

优先：

- AI4SE / autonomous software engineering
- agentic AI / AI systems / LLM systems
- applied AI4Science / scientific agents
- systems / empirical / simulation / data-driven / applied ML
- tooling / benchmarks / experiments / real-task evaluation

降权：

- pure theory / theorem-heavy / proof-centric
- domain-theory-heavy AI4Science where software is auxiliary
- 需要大量 theoretical physics / pure math / theoretical chemistry / PDE derivation 才能开始主要研究的方向

**AI4Science 不会自动把 PRUNED 学校捞回来；必须出现具体 PI / vacancy / funding 证据。**

## Reopened 2026-09-23

- **NYU Courant CS PhD / NYU Shanghai Global Track** moved from PRUNED to ACTIVE because the documented reopen condition is now met: Qiaoyu Tan is a current tenure-track CS faculty member explicitly recruiting multiple fully funded Fall 2027 PhD students from NYU Courant in Agent / Trustworthy AI, direct email is invited, and the selected route is empirical/system-oriented rather than pure theory.
