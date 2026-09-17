# PhD Application Control Center — 2027

> **目标**：低摩擦、全奖/高覆盖、尽量不考试、不重复考英语、少面试；研究方向以 **Boss / DS-Hns / Quant-Ultra** 动态匹配导师；优先 implementation-first 的 systems / empirical / software-engineering / applied-ML 研究，不把纯理论方向当主线。
>
> **读法**：只看这一页也能知道下一步。学校细节去 `targets/`，真实申请进度去 `applications/`，机器数据在 `data/`。

## 现在最该做什么

1. **University of Macau**：已提交，进入等待 / 导师匹配阶段；不再作为“要不要申请”的候选。
2. **Concordia**：继续作为活跃导师匹配案例，重点处理 supervisor / funding / offer 细节，并已扩充当前仍收人的导师池。
3. **TU Delft WALTZ**：直接 vacancy，deadline 2026-09-24。
4. **SUTD Jan 2027**：新加坡筛选后进入 `APPLY_NOW`；deadline **2026-09-30**，正式申请与导师联系并行推进。
5. **ACTIVE / WATCH / BACKUP**：继续严格按 hard gate → research-method fit → recruitment/capacity → friction 执行。
6. **Buffalo / SMU CS-IS**：分别因英语重考、GRE/GMAT 硬门槛当前关闭。

## 当前主线

| 项目 | 状态 | 备注 |
|---|---|---|
| University of Macau | **SUBMITTED** | 等待后续 |
| Concordia University | **ACTIVE / SUPERVISOR TRACK** | 已有导师接触 + 新扩导师池 |
| TU Delft WALTZ PhD vacancy | **APPLY_NOW** | implementation/system-heavy，当前直接带薪 vacancy |
| **SUTD PhD / ISTD — Jan 2027** | **APPLY_NOW** | GRE not required；英语授课本科可免语言考试；current PhD opportunities 与 Boss/DS-Hns 高匹配；2026-09-30 截止 |
| PolyU / HKUST / KAUST | **ACTIVE** | 当前工程型 fit 较干净 |
| HKU / SFU | **ACTIVE WITH VERIFICATION** | 先核 degree/classification route |
| NUS Computing | **BACKUP** | AI4SE fit 很强，但 scholarship equivalency + interview + mandatory QE 摩擦 |
| NTU CCDS | **WATCH** | Honours (Distinction) equivalency 未核清；Penghui Li 2027 在招但暂不越过 academic gate |
| University at Buffalo | **CLOSED** | 英语重考硬门槛 |
| SMU CS / IS PhD | **REJECTED** | GRE/GMAT 硬门槛；除非获得书面 special waiver |

## 懒人筛选规则

**直接淘汰**：GRE required / 强制重新考英语且不能豁免 / 明确 academic score/classification 硬线未达到 / 明显自费或 funding 不够 / 学术层级明显低于底线 / 新西兰。

**研究风格降权/清理**：pure theory / theorem-heavy / proof-centric / complexity-first / semantics-first；如果主要成果依赖数学证明而不是系统实现、实验、benchmark 或软件工程产出，默认不进入主线。

**优先**：systems、software engineering、coding agents、agent evaluation、testing、program repair、developer tooling、distributed/AI systems、empirical/applied ML。

**强烈扣分**：强制笔试、多轮 technical panel、必须长期套磁、重 proposal、高申请摩擦。

**小参考**：LGBT/trans 日常环境、ACG/二次元生态。二者仅用于条件接近时 tie-break。

→ 完整规则：[STRATEGY.md](STRATEGY.md)

## 候选池

- [ACTIVE](targets/ACTIVE.md) — 现在值得推进
- [Singapore 2026-09-17](targets/SINGAPORE-2026-09-17.md) — SUTD/NUS/NTU/SMU 本轮清洗 + 导师池
- [WATCHLIST](targets/WATCHLIST.md) — 研究风格合适，但有少量硬条件待核
- [BACKUP](targets/BACKUP.md) — 研究合适，但流程/考试/摩擦太重
- [PRUNED](targets/PRUNED.md) — 当前不值得继续花时间；默认不自动重新推荐
- [REJECTED](targets/REJECTED.md) — 已确认违反硬条件

## 申请进度

- [总状态](STATUS.md)
- [University of Macau](applications/university-of-macau/STATUS.md)
- [Concordia](applications/concordia/STATUS.md)
- [Singapore](applications/singapore/STATUS.md)
- [University at Buffalo](applications/university-at-buffalo/STATUS.md)

## 推荐人

→ [Referee Control Center](materials/referees/README.md)

当前核心推荐人：**Sinott / Ting Dang**。

- Sinott：上次由老师自行撰写，默认继续走“简短提醒 + CV/更新 + 系统请求”。
- Ting Dang：上次由用户提供 draft 供 review；旧稿只作为历史基线。
- **Boss / DS-Hns 对两位推荐人都属于此前不知道的新项目**；下一次如果提及，只能作为上次联系后新增的独立项目首次介绍。

## 研究项目怎么用

| 导师方向 | 主叙事 |
|---|---|
| Agentic AI / Multi-agent / LLM systems | **Codex Boss** |
| Software Engineering / Coding agents / Computer Use | **DS-Hns + Boss** |
| Financial ML / Data / Optimization | **Quant-Ultra + Boss** |
| Trustworthy software / privacy / governance | **Privacy Lens + Boss/DS-Hns** |

→ [research-profile](materials/research-profile.md) · [project-positioning](materials/project-positioning.md)

## 给自动化工具

长期结构化数据仍在 `data/`，但发送动作必须先服从 `targets/` 的人工控制状态：

`REJECTED > PRUNED > BACKUP > WATCH > ACTIVE`

也就是说：即使旧 YAML / staging 里还残留某个导师，只要它已经进入 PRUNED / REJECTED，自动套磁工具就**不得发送**。

→ [screening schema](automation/screening-schema.md) · [outreach policy](automation/outreach-policy.md) · [auto application spec](automation/auto-application-spec.md)

---

历史版申请工作表已原样归档：[archive/README-2026-08-15.md](archive/README-2026-08-15.md)。旧版 deadline、funding、GRE、英语政策默认视为历史信息，重新核验前不自动继承。
