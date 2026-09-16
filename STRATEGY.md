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

## 2. Research Method Fit

用户不是“只做软件工程”，而是更适合**通过系统实现、实验、benchmark、仿真、数据分析和真实任务验证来完成研究**，不擅长把 theorem / proof / 数学推导作为博士工作的主要产出。

这个门禁在 Hard Gate 之后、Friction / Utility 之前单独评估。

### A. 第一梯队：高匹配研究形态

#### AI4SE / Autonomous Software Engineering

优先级最高之一：

- AI for Software Engineering (AI4SE)
- LLM for Software Engineering
- coding agents / autonomous coding
- program repair / debugging / testing
- code generation / code review / code search
- repository mining / empirical software engineering
- developer tools / human-AI software development
- AIOps / DevOps / software maintenance
- software reliability / fault recovery / self-healing systems

这条路线与 **DS-Hns + Codex Boss** 直接重合。

#### Agentic AI / AI Systems

同样高匹配：

- multi-agent systems / agent orchestration
- LLM systems / agent infrastructure
- autonomous research agents
- agent evaluation / benchmarks / adjudication
- computer-use agents
- trustworthy / secure / reliable agents
- distributed AI systems / serving / runtime / fault tolerance

主要对应 **Codex Boss + DS-Hns + Privacy Lens**。

#### Applied AI for Science

AI4Science 也属于高匹配，但前提是研究方法偏工程/实验，而不是要求先成为某个理论学科专家。

优先：

- scientific agents / autonomous research
- literature / evidence synthesis
- hypothesis generation
- experiment planning / scientific workflow automation
- scientific simulation / surrogate modeling
- computational biology / biomedical AI / health AI
- drug discovery / molecular or physiological simulation with strong computational implementation
- scientific benchmark / model evaluation
- multimodal scientific data analysis
- AI-assisted lab / research tooling

可用项目叙事：**Codex Boss + drug-simulator / Param-Health + DS-Hns**。

### B. 第二梯队：可匹配，但要看具体课题

- applied ML / trustworthy AI / privacy / security engineering
- distributed systems / ML systems
- HCI for developer/scientific tools
- robotics / autonomous systems when software/agent implementation is central
- program analysis / formal methods when the main output is tooling, testing, verification systems, or empirical evaluation
- scientific ML when implementation / experiments are central

### C. 降权方向

以下方向不是自动 REJECT，但默认降低优先级：

- theorem-heavy formal methods
- complexity theory / algorithms theory
- logic-heavy PL theory
- proof-centric verification
- optimization/statistical theory where derivation is the central output
- cryptographic / information / learning theory
- AI4Science that is heavily dependent on advanced theoretical physics, pure mathematics, theoretical chemistry, PDE theory, or domain derivations where software is only auxiliary

### D. 直接避免

如果导师近期主要论文和学生课题显示：

- 核心贡献主要是 theorem / lemma / proof / asymptotic bound；或
- 博士训练强依赖高阶数学/领域理论推导，工程实现只是辅助；或
- 需要先补大量纯理论背景才能开始主要研究；或
- 无法把用户已有 Boss / DS-Hns / Quant / simulation / software-building 能力转换成可执行实验路线；

则标记 `method_mismatch: true`，通常降为 `PRUNED` 或 `REJECT`。

### E. 建议机器字段

- `research_domain`: `ai4se | agentic_ai | ai_systems | ai4science | trustworthy_ai | systems | applied_ml | mixed | other`
- `research_method`: `systems | empirical | simulation | applied_ml | data_driven | mixed | theory_heavy | pure_theory | unknown`
- `theory_burden`: `low | medium | high | unknown`
- `domain_theory_burden`: `low | medium | high | unknown`
- `implementation_centrality`: `high | medium | low | unknown`
- `experiment_centrality`: `high | medium | low | unknown`
- `simulation_centrality`: `high | medium | low | unknown`
- `method_mismatch`: `true | false | unknown`
- `style_evidence`: recent papers / student projects / vacancy description

默认偏好：

**AI4SE / agentic AI / AI systems / applied AI4Science + systems/empirical/simulation > applied ML > mixed > theory-heavy > pure theory**。

## 3. Friction

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

## 4. Utility

只做描述性判断，不制造一个假精确总分：

- funding coverage
- tuition burden
- local living-cost coverage
- research/domain fit
- coding / systems / agentic-AI / AI4SE / AI4Science compatibility
- research-method fit / theory burden / domain-theory burden
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

- **Codex Boss** → autonomous research / multi-agent / orchestration / AI evaluation / LLM systems / scientific agents
- **DS-Hns** → AI4SE / autonomous software engineering / long-horizon coding / computer use / fault recovery / AIOps
- **Quant-Ultra** → financial ML / non-stationary data / temporal validation / optimization / data infrastructure
- **Privacy Lens** → trustworthy software / privacy / auditability / governance
- **drug-simulator / Param-Health** → AI4Science / biomedical AI / scientific simulation / computational health

每所学校、每位导师单独选择 `narrative_route`。

当一个导师同时有理论与应用方向时，默认只保留其 **systems / empirical / simulation / applied** 路线，不因为导师整体声誉而强行进入理论子方向。

## 7. Action State

- `APPLY_NOW`：当前即可推进，硬条件已过，research-method fit 明确合适
- `APPLY`：值得申请，但还有少量非硬门槛前置动作
- `BACKUP`：研究方法基本适合，但申请/培养摩擦明显
- `WATCH`：只差 1–2 个可核验条件，且 research-method fit 已经较清楚
- `PRUNED`：不是硬性不合格，但研究方法、具体导师结构或 ROI 不值得当前投入
- `HOLD`：已申请、已有特殊进展，暂不参与筛校
- `REJECT`：违反硬门槛，或纯理论/重领域理论严重错配且无应用路线

## 8. 信息新鲜度

高变化字段必须带 `last_verified`：deadline、GRE、English、academic score threshold、funding、supervisor requirement、fee、interview/exam。

导师/课题还需记录近期 research-method evidence；不能只根据 faculty profile 上一个宽泛关键词判断“匹配”。

未刷新时宁可写 `unknown`，不要把旧资料伪装成当前事实。
