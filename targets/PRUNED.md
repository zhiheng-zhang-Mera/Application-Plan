# Pruned Targets

> 这里放**不是硬性不合格，但目前不值得继续消耗申请时间**的候选。
>
> 和 `REJECTED` 的区别：REJECTED 是违反硬门槛；PRUNED 是研究风格、导师结构、流程摩擦或 ROI 不合适。自动筛选默认**不要重新推荐**，除非出现新的具体导师、funding、vacancy 或政策变化。

| 学校 / 项目 | Prune reason | 为什么移出主候选池 | 重开条件 |
|---|---|---|---|
| Drexel CS PhD | `LOW_ROI_STALE_GENERIC_FIT` | 旧候选只剩泛 CS/SE/ML systems 匹配，没有当前明确高匹配工程型导师或资金优势 | 找到明确做 coding agents / AI4SE / autonomous software systems 的当前 PI，且 funding/英语/成绩线干净 |
| Stevens CS PhD | `LOW_ROI_STALE_GENERIC_FIT` | 主要是旧版 ML systems / time-series 泛匹配，当前没有足够理由优先于现有加拿大/HK/欧洲候选 | 出现强匹配 PI + 清晰全奖 + 低摩擦申请 |
| Stony Brook CS PhD | `HIGH_COMPETITION_WEAK_SPECIFIC_FIT` | 学校强，但现池中没有足够具体的 implementation-first 导师路线，且竞争强；不值得为“学校名气”单独投入 | 找到直接做 agentic software engineering / coding agents / systems evaluation 的 PI |
| UMass Amherst CS PhD | `HIGH_COMPETITION_WEAK_SPECIFIC_FIT` | Systems/ML 很强但候选过泛，当前没有比已有目标更直接的 Boss/DS-Hns 工程路线 | 出现明确招收且研究方式偏系统实现/实验的 PI |
| UC Riverside CS PhD | `ACADEMIC_ROI_WEAK` | 旧资料显示 academic-profile 风险，且没有形成明显强于现有候选的工程型导师匹配 | 明确 PI 兴趣 + 所有硬门槛通过 + funding 清晰 |
| NYU Courant CS PhD | `RESEARCH_STYLE_MISMATCH` | funding/GRE 条件干净，但上一轮具体导师池有错误；Thomas Wies 当前核心工作以 verification / automated deduction / proof-oriented program reasoning 为主，和 implementation-first 偏好不够合；没有找到足够直接的 AI4SE/agent-systems 主导师来抵消超高竞争 | 找到当前 tenure-track PI，明确以 empirical agent evaluation / software systems / developer tooling 为主要产出方式 |

## 不应放进 PRUNED 的情况

- 明确违反 GRE / 英语 / 成绩 / funding 等硬门槛 → `REJECTED`
- 只差一个可核验条件（如 final WAM / degree equivalency / supervisor funding）且研究风格很好 → `WATCHLIST`
- 流程麻烦但研究 fit 仍很强 → `BACKUP`

## 研究风格原则

默认优先：systems / empirical / software engineering / applied ML / agent evaluation / tooling / benchmarks。

默认降权：pure theory / theorem-heavy / proof-centric / complexity-first / semantics-first / 需要较强数学证明能力才能作为主要产出。
