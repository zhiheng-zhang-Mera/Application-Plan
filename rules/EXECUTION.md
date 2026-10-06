# 申请执行规则

> **当前申请工作流 — 2026-10-06。** 本文件是套磁、材料生成、QA、申请状态与人工审批的唯一主规则书。

## 1. 总原则

仓库是**事实源 + 申请准备系统**，不是“看到机会就盲目提交”的授权。

可确定、可校验的工作尽量自动化；不可逆、高风险动作保留明确人工 checkpoint。

## 2. 语言规则

这是全仓统一约定：

### 内部内容：尽量中文

以下内容默认使用中文：

- README / dashboard；
- rules；
- target / watch / reject 说明；
- application STATUS / CONTACTS / TIMELINE；
- 内部材料索引、项目定位、推荐人说明；
- QA 报告、执行说明、人工提示。

### 对外内容：保持英语

以下内容默认必须保持**英语**，除非目标项目明确要求另一种语言：

- CV / Resume；
- SOP / Personal Statement；
- Research Statement；
- Research Proposal；
- Past Research Experience；
- short-answer application responses；
- writing sample cover note；
- 给导师/招生人员的邮件正文与 subject；
- portal 中准备直接提交的英文文本。

不要为了“仓库中文化”去翻译已经用于对外提交的材料。

### 允许保留英语的内部元素

为避免破坏自动化，以下可继续保留英语：

- YAML / JSON / CSV 字段名；
- 状态枚举，如 `APPLY_NOW`、`WATCH`、`REJECT`；
- 代码、命令、路径、变量名；
- 学校 / 项目 / 论文 / 技术专有名词；
- 需要精确核验的官方原文短语。

## 3. 真相源优先级

Program / supervisor 事实：

1. 当前官方证据；
2. 当前 `data/*.yaml` 结构化状态；
3. 当前 dashboard / 生成视图；
4. dated target snapshot；
5. archive。

Contact history：

1. `applications/OUTREACH-LOG.md` 或 application-specific CONTACTS/TIMELINE 中已确认的 sent/replied event；
2. 可访问时的 mailbox evidence；
3. 当前 README 看板；
4. supervisor 结构化状态；
5. 更旧快照。

旧 YAML 的 `not_contacted` 绝不能覆盖已知的发送/回复事实。

## 4. 申请状态机

统一使用：

`DISCOVERED → VERIFIED → ELIGIBLE → ACTIVE → PACKAGE_READY → HUMAN_REVIEW → SUBMITTED → INTERVIEW / WAITING → OFFER / REJECTED / WITHDRAWN`

辅助状态：

- `BLOCKED`
- `WATCH`
- `HOLD`
- `CLOSED`

没有证据时，状态不得暗示已经 payment、submitted、referee complete、supervisor committed 或 funding confirmed。

## 5. 套磁准入

导师进入当前 send queue 前必须同时满足：

- program 已通过筛选；
- research method 匹配；
- 当前 2027 capacity/recruitment 已验证，或项目明确允许 supervision inquiry；
- official / lab / personal public page 可验证 direct email；
- 当前 route 允许 direct contact；
- program-supervisor compatibility 已确认或足够明确；
- same-school / same-department contact lock 已清。

禁止猜邮箱。

即使公开 email 存在，也不能绕过“form/portal only”或“do not email”。

## 6. 同校联系锁

默认：

> **同一 university + department 同时只保持 1 个新的 cold contact。**

已有 warm / replied / interview 线程优先于新 cold outreach。

普通首封：

- T0 = sent；
- **5 个工作日**无实质回复 → 允许一次 final follow-up，同时 department 可解锁；
- 再 **5 个工作日**无实质回复 → `NO_REPLY_FINAL / CLOSED`；
- 不发第三封。

自动回执、普通 OOO 不算实质回复；若 OOO 给出返岗日期，则从返岗后重新计时。

warm/private channel 使用 application-specific 规则，不硬套普通 timer。

## 7. 材料生成

每个 school/supervisor package 可包含：

- tailored CV；
- SOP / Personal Statement；
- Research Statement；
- Research Proposal；
- Past Research Experience；
- short answers；
- outreach subject/body；
- transcript / supporting-document manifest；
- project links；
- referee plan；
- application checklist。

材料应从复用母版 / verified data 生成，不要给每所学校维护一套互相漂移的个人事实。

### Claim 安全边界

生成内容只能使用：

- 已验证个人事实；
- 已验证成绩 / 文件记录；
- 项目当前 accepted evidence boundary 内的 claim；
- 当前 cycle 已验证的 target facts。

当前重要边界：

- **Utopia / PCF**：PCF 是计划中的下一阶段扩张，不是已完成证据。
- **Utopia**：不得声称 wearable hardware、assistant/persona、general LLM router、Boss/Hns connectors 已全部完成，除非以后有新证据。
- **Boss / Hns 论文**：未正式接收前不得写成 peer-reviewed publication。
- 独立项目不能倒写成推荐人曾指导的项目。

## 8. Package QA Gate

进入 `PACKAGE_READY` 前至少检查：

- university / program / supervisor 正确；
- intake / deadline 当前有效；
- GRE / English / academic / funding gate 当前有效；
- lead project 与导师方向一致；
- word/page limit；
- required sections；
- required documents；
- 不把缺失 attachment 写成已存在；
- supervisor opening 不陈旧；
- score 不互相矛盾；
- publication / project claim 有证据；
- 无重复 cold outreach；
- 无 hard-gate violation；
- 需要 PDF 时 source 可编译且 PDF 实际存在。

QA 失败后回到 `BLOCKED` 或 `DRAFT`，不能自动豁免。

## 9. 文件与成绩

`Documents/` 是 academic source evidence 区。

当前结构化成绩：

- `Documents/Bachelor Score.csv`
- `Documents/Master Score.csv`

派生 CSV / 计算结果是分析输入，不是 official transcript。

必须区分：

- official transcript；
- screenshot / progress record；
- derived CSV；
- calculated WAM/GPA/equivalency；
- target university 的最终 equivalency judgment。

绝不能把 derived file 当官方成绩单提交。

## 10. 推荐人

每个 referee × application 至少区分：

- invited；
- accepted；
- submitted；
- unknown；
- deadline。

同时区分：

- 推荐人实际知道的事实；
- 上次联系后新增的信息；
- 用户提供的 draft；
- 推荐人实际提交的 final letter（除非明确确认，否则未知）。

Boss / Hns / Utopia 等独立项目不能倒推成旧推荐关系里的 supervised work。

## 11. 人工 checkpoint

以下动作必须人工确认：

- 支付 application fee；
- final portal submission；
- 发送尚未被证据支持的高风险 statement；
- accept / decline offer；
- 承诺 supervisor / funding arrangement；
- 任何可能实质性误报身份、成绩、publication status、project completion 的动作。

research、package generation、QA、状态刷新、材料准备可以自动执行。

## 12. README 规则

根 `README.md` 是**懒人看板**，不是历史档案和规则书。

只展示：

- 当前研究/申请主线；
- 现在需要做什么；
- 正在等待什么；
- 哪些是 BLOCKED / verification-only；
- 关键 deadline；
- 关键材料缺口；
- 深层证据入口。

历史大表放到 applications log、dated target snapshot 或 archive。

## 13. 完成定义

“申请包已准备”必须意味着：

- eligibility 已刷新；
- package 已生成；
- QA 已通过；
- references / deadlines 已知；
- portal requirements 已映射；
- 用户可以直接审核最终 bundle。

“已提交”必须有真实 submission evidence，不能因为 draft 做完就标 submitted。

## 14. 导师专属套磁协议

任何自动生成的 supervisor outreach 都必须先读取该导师的**个人维护主页 / lab / openings 页面**（如存在），不能只套用通用邮件母版。

### 14.1 生成顺序

固定顺序：

`program gate → supervisor capacity → personal/lab page → contact protocol extraction → applicant evidence mapping → English email generation → protocol QA → HUMAN_REVIEW`

如果 `contact protocol extraction` 没完成，不生成“send-ready”邮件。

### 14.2 Protocol Manifest

每个准备联系的导师应在 package 中形成一个简短内部 manifest，至少包含：

- 联系入口与来源 URL；
- 页面最后核验日期；
- 是否找到个人主页 / lab / openings page；
- subject 要求；
- 邮件正文必填内容；
- 必须附件；
- 禁止附件；
- 成绩要求及口径；
- publication / preprint 要求；
- 指定论文 / topic / question；
- form / screening task；
- 当前申请人对每一项的满足状态：`READY | MISSING | NOT_APPLICABLE | UNKNOWN`。

这个 manifest **是内部中文控制文件**；最终发送邮件仍为英语。

### 14.3 自动材料映射

遇到导师要求时：

- “include GPA / grades” → 从 `Bachelor Score.csv`、`Master Score.csv` 与 official transcript 取真实数据；
- “include transcript” → 只使用真实官方 transcript，不拿 derived CSV 冒充；
- “include publications” → 从经过验证的 publication/preprint registry 生成，并保留准确 publication status；
- “discuss one of my papers” → 先读取论文，再生成针对性 discussion；
- “describe a concrete research idea” → 结合该导师近期工作与当前 Utopia/Hns/Boss evidence 生成一个可执行 research question；
- “send only CV” → 不擅自塞 transcript / proposal；
- “use form, do not email” → 邮件生成器停止，改走 form-ready English text；
- “subject must be XXX” → 严格按指定 subject pattern。

### 14.4 缺项时怎么处理

- 缺成绩口径 → BLOCKED，先计算/核验；
- 没有导师要求的 peer-reviewed publication → 如只是“请列出”，如实写无或只列准确标注的 preprint；如是硬门槛则转 screening gate；
- 没读指定论文 → BLOCKED，不允许生成假装读过的段落；
- 缺 required attachment → `PACKAGE_READY=false`；
- contact instruction 冲突 → BLOCKED，先解决证据冲突。

### 14.5 Protocol QA

在原有 Package QA Gate 之外，新增：

- personal/lab/openings page 已检查或明确 not_found；
- current contact instruction 已记录；
- subject pattern 正确；
- required email fields 全部出现；
- required attachments 全部真实存在；
- forbidden attachments 未加入；
- grade / WAM / GPA 数值与口径正确；
- publication status 无夸大；
- 指定论文 / topic discussion 有具体内容且与原文一致；
- 若要求 form-only，未生成误导性的 send-ready email。

任何一项失败，不能进入 `OUTREACH_READY / PACKAGE_READY`。

