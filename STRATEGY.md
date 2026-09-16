# PhD Screening Strategy

## 1. Hard Gate

默认直接 `REJECT`：

- GRE required
- 必须重新考 IELTS / TOEFL / DET，且英语授课本硕不能满足或豁免
- 明显自费，或 funding 无法合理覆盖 mandatory tuition + 基本生活
- 学术层级明显低于当前可接受底线（约 Concordia-level research university）
- New Zealand

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

- `APPLY_NOW`：当前即可推进，硬条件已过
- `APPLY`：值得申请，但还有少量前置动作
- `BACKUP`：可投，但摩擦/匹配/性价比有明显折损
- `WATCH`：信息未刷新或等待新轮次
- `HOLD`：已申请、已有特殊进展，暂不参与筛校
- `REJECT`：确认违反硬条件或用户主动关闭

## 7. 信息新鲜度

高变化字段必须带 `last_verified`：deadline、GRE、English、funding、supervisor requirement、fee、interview/exam。

未刷新时宁可写 `unknown`，不要把 8 月旧资料伪装成 9 月当前事实。