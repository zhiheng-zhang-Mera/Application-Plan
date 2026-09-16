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

## 3. Utility

只做描述性判断，不制造一个假精确总分：

- funding coverage
- tuition burden
- local living-cost coverage
- research fit
- coding / systems / agentic-AI compatibility
- graduation rigidity / burden
- location convenience
- existing-profile feasibility

推荐标签：`excellent / good / mixed / poor / unknown`。

## 4. Lifestyle：低权重参考

### LGBT / trans

只看实际学生生活便利度，例如校园/城市日常环境、普通医疗与行政服务可及性、是否存在明显制度性障碍。

字段：`comfortable / workable / mixed / difficult / unknown`。

### ACG

简单记录动漫、游戏、漫展、cosplay、周边与兴趣社群生态。

字段：`strong / decent / limited / weak / unknown`。

**二者都不能单独推翻 Hard Gate 或 funding 判断。**

## 5. Research Narrative Routing

不要再全局绑定 Quant-Ultra。

- **Codex Boss** → autonomous research / multi-agent / orchestration / AI evaluation / LLM systems
- **DS-Hns** → autonomous software engineering / long-horizon coding / computer use / fault recovery
- **Quant-Ultra** → financial ML / non-stationary data / temporal validation / optimization / data infrastructure
- **Privacy Lens** → trustworthy software / privacy / auditability / governance

每所学校、每位导师单独选择 `narrative_route`。

## 6. Action State

- `APPLY_NOW`：当前即可推进，**包括成绩门槛在内的硬条件已过**
- `APPLY`：值得申请，但还有少量非硬门槛前置动作
- `BACKUP`：可投，但摩擦/匹配/性价比有明显折损
- `WATCH`：信息未刷新、等待新轮次、或**成绩门槛依赖尚未完成的学位/最终 WAM**
- `HOLD`：已申请、已有特殊进展，暂不参与筛校
- `REJECT`：确认违反硬条件或用户主动关闭

## 7. 信息新鲜度

高变化字段必须带 `last_verified`：deadline、GRE、English、**academic score threshold**、funding、supervisor requirement、fee、interview/exam。

未刷新时宁可写 `unknown`，不要把 8 月旧资料伪装成 9 月当前事实。