# PhD Screening Strategy

## 1. Hard Gate

默认直接 `REJECT`：

- GRE required
- 必须重新考 IELTS / TOEFL / DET，且英语授课本硕不能满足或豁免
- **明确的 GPA / WAM / 百分制 / honours classification / class standing 硬门槛未达到**
- 明显自费，或 funding 无法合理覆盖 mandatory tuition + 基本生活
- 学术层级明显低于当前可接受底线（约 Concordia-level research university）
- New Zealand

### Academic score gate

成绩门槛必须在学校进入 `ACTIVE` 之前单独核验，不能用导师匹配、项目经历或 research fit 覆盖。

至少记录：

- `score_basis`: undergraduate / final-two-years / upper-level / master's / best-degree / unspecified
- `minimum_score`: 官方原始写法，例如 `78%`, `A-`, `3.5/4.33`, `First Class Honours`
- `applicant_score`: 按对方规则可直接比较的成绩；不能可靠换算时写 `unknown`
- `academic_floor_pass`: `true / false / unknown`
- `score_gate_note`: 换算、重修、在读硕士、final WAM 未出等说明
- `last_verified`

规则：

1. 官方有硬分数线且当前已确定低于门槛 → `REJECT`，reason code `ACADEMIC_SCORE_BELOW_MINIMUM`。
2. 依赖尚未完成的 Melbourne 硕士 final WAM / degree classification → 最多 `WATCH`，不得提前标 `APPLY_NOW`。
3. 官方只写 competitive / preferred / normally successful，而非 eligibility minimum → 记录为竞争风险，不作为硬淘汰。
4. 不自行粗暴把澳洲 WAM、UBC percentage 与 4.0 GPA 一比一换算。优先使用学校自己的 equivalency / honours classification；无法确认时写 `unknown`。
5. 对本科成绩，要区分 cumulative、last 60 credits、upper-level、final two years；不得拿最有利的局部成绩冒充对方要求的口径。

当前可用成绩证据：UBC 官方 transcript；Melbourne 目前仅能使用已出成绩，最终硕士 WAM / classification 未出时视为未定。

每个硬淘汰必须保存 reason code 与核验日期，避免未来重复捞回。

## 2. Friction

不一定淘汰，但显著影响是否值得花时间：

- supervisor-first
- interview burden: none / light / normal / heavy
- exam burden: none / light / technical / heavy
- proposal burden: none / short / normal / heavy
- outreach burden: none / optional / recommended / required
- reference count / special forms
- application fee
- 是否支持 recorded video 替代部分同步筛选

偏好顺序：**直接申请 > 简单导师聊天 > 录视频 > 正式 panel > 技术考试 / 多轮筛选**。

## 3. Research Style Fit

用户不擅长纯理论方向。这个限制在通过 Hard Gate 之后、计算 research fit 之前单独评估。

### 优先方向

优先寻找可以主要依靠以下能力完成博士工作的导师/课题：

- systems building / software systems / infrastructure
- autonomous software engineering / coding agents / developer tools
- LLM systems / agent orchestration / multi-agent evaluation
- empirical software engineering / mining software repositories
- testing / debugging / program repair / reliability / fault recovery
- applied ML / trustworthy AI / security / privacy engineering
- benchmarks / experiments / ablation / user studies / performance evaluation
- 能把数学作为工具使用，但论文核心贡献仍然是系统、方法实现、实验结果或实证研究

### 降权方向

下列方向并非自动 REJECT，但默认降低优先级：

- theorem-heavy formal methods
- complexity theory / algorithms theory
- logic-heavy programming languages theory
- proof-centric verification where novel proofs are the main contribution
- optimization/statistical theory where derivation is the central research output
- cryptographic theory / information theory / learning theory

### 直接避免

如果导师近期主要论文和学生课题显示：

- 大部分核心贡献是 theorem / lemma / proof / asymptotic bound
- 博士训练强依赖高阶数学推导，而工程实现只是辅助
- 与用户现有 Boss / DS-Hns / Quant / software-building 能力无法形成可执行实验路线

则标记 `theory_mismatch: true`，通常降为 `BACKUP` 或 `REJECT`；除非该导师同时有明确的 applied/systems 子方向可走。

建议机器字段：

- `research_style`: systems / empirical / applied_ml / mixed / theory_heavy / pure_theory
- `theory_burden`: low / medium / high
- `implementation_centrality`: high / medium / low
- `experiment_centrality`: high / medium / low
- `theory_mismatch`: true / false / unknown

用户偏好：**systems / empirical / applied > mixed > theory-heavy > pure theory**。

## 4. Utility

只做描述性判断，不制造一个假精确总分：

- funding coverage
- tuition burden
- local living-cost coverage
- research fit
- coding / systems / agentic-AI compatibility
- **research style fit / theory burden**
- graduation rigidity / burden
- location convenience
- existing-profile feasibility

推荐标签：`excellent / good / mixed / poor / unknown`。

## 5. Lifestyle：低权重参考

### LGBT / trans

只看实际学生生活便利度，例如校园/城市日常环境、普通医疗与行政服务可及性、是否存在明显制度性障碍。

字段：`comfortable / workable / mixed / difficult / unknown`。

### ACG

简单记录动漫、游戏、漫展、cosplay、周边与兴趣社群生态。

字段：`strong / decent / limited / weak / unknown`。

**二者都不能单独推翻 Hard Gate 或 funding 判断。**

## 6. Research Narrative Routing

不要再全局绑定 Quant-Ultra。

- **Codex Boss** → autonomous research / multi-agent / orchestration / AI evaluation / LLM systems
- **DS-Hns** → autonomous software engineering / long-horizon coding / computer use / fault recovery
- **Quant-Ultra** → financial ML / non-stationary data / temporal validation / optimization / data infrastructure
- **Privacy Lens** → trustworthy software / privacy / auditability / governance

每所学校、每位导师单独选择 `narrative_route`。

当一个导师同时有理论与应用方向时，默认只保留其 **systems / empirical / applied** 路线，不因为导师整体声誉而强行进入理论子方向。

## 7. Action State

- `APPLY_NOW`：当前即可推进，**包括成绩门槛在内的硬条件已过**，且 research style 没有明显理论错配
- `APPLY`：值得申请，但还有少量非硬门槛前置动作
- `BACKUP`：可投，但摩擦、匹配、性价比或 theory burden 有明显折损
- `WATCH`：信息未刷新、等待新轮次、成绩门槛依赖尚未完成的学位/最终 WAM，或 research style 尚未核清
- `HOLD`：已申请、已有特殊进展，暂不参与筛校
- `REJECT`：确认违反硬条件、纯理论严重错配且没有应用路线，或用户主动关闭

## 8. 信息新鲜度

高变化字段必须带 `last_verified`：deadline、GRE、English、**academic score threshold**、funding、supervisor requirement、fee、interview/exam。

导师/课题还需记录近期研究风格证据；不能只根据 faculty profile 上一个宽泛关键词判断“匹配”。

未刷新时宁可写 `unknown`，不要把旧资料伪装成当前事实。