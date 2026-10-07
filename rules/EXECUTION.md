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
- **5 个工作日**无实质回复 → 默认 `CLOSED_TIMEOUT`，立即释放 university / department contact lock；
- final follow-up 不再是默认动作，只有用户明确选择保留该导师时才允许发送一次；
- 被关闭的旧线程继续保留历史记录，但不再阻塞新导师；
- 不发第三封。

默认清除只清**当前执行锁与等待状态**，不删除历史邮件、发送事实或证据。

以下情况不得自动 timeout-close：已有实质回复、interview / supervision discussion、requested materials、active private/warm channel，或 OOO 给出返岗日期且重新计算窗口尚未到期。

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

## 15. 套磁邮件必须“专人专用”

**允许复用邮件结构，不允许复用实质正文。**

模板只能规定结构，例如：

1. 称呼；
2. 导师专属 opening / hook；
3. 与该导师研究直接相关的申请人证据；
4. 一个具体 research bridge / question；
5. 按导师要求设计的 ask / next step；
6. 简短结束语与签名。

模板**不能**提供“把导师名字替换掉就能发”的完整正文。

### 15.1 每封邮件必须具备的个性化内容

每位导师至少需要单独生成：

- **Supervisor-specific hook**：基于其个人主页、lab/openings 页面、近期论文、正在招的具体项目或明确 research agenda；
- **Why this supervisor / lab**：解释为什么是这个导师，而不是同校其他方向相近的人；
- **Project selection**：只选择与该导师最相关的 1–2 个项目，不要求所有邮件都按同样顺序介绍 Utopia / Hns / Boss；
- **Concrete connection**：明确指出申请人已有工作与导师某个具体问题、系统、论文或项目之间的技术连接；
- **Research question / idea**：至少给出一个适合该导师语境的具体问题、下一步实验或系统方向；
- **Customized ask**：根据该导师自己的 contact protocol 决定是询问 PhD supervision、某个 advertised project、是否愿意讨论某个方向，还是只提交 CV/form。

其中至少 **opening、research bridge、ask** 三部分必须针对该导师重新写，不能从另一位导师邮件复制。

### 15.2 可以复用的内容

以下内容可以复用事实，但不等于必须逐字复制：

- 姓名、学位、预计毕业时间；
- 官方成绩事实；
- 项目名称；
- GitHub / artifact URL；
- publication / preprint 的真实状态；
- 联系方式；
- 极短的项目事实描述。

允许复用这些**事实源**，但正文应根据导师语境选择、压缩和重组。

### 15.3 禁止的“伪个性化”

以下情况直接 QA FAIL：

- 只替换 `Professor X`、学校名和 lab 名，其余正文基本相同；
- 每封邮件都固定写同样的三项目介绍，只改顺序；
- 用“your impressive work in AI / systems”这类泛句代替具体研究连接；
- 引用一篇论文标题，但正文没有体现实际理解；
- 所有导师都收到同一个 research question；
- 明明导师招的是某个具体 project，却发送完全通用的“我想申请您的 PhD”；
- 为了显得个性化而虚构自己读过、实现过、发表过或掌握过的内容。

### 15.4 Personalization Manifest

每封准备发送的邮件都应有一个内部中文 manifest，至少记录：

- `supervisor_name`
- `target_program`
- `personal_page_or_lab_source`
- `recent_work_or_project_selected`
- `supervisor_specific_hook`
- `why_this_supervisor`
- `selected_applicant_evidence`
- `specific_research_bridge`
- `proposed_question_or_idea`
- `customized_ask`
- `protocol_requirements_satisfied`
- `cross_email_duplication_check`

这个 manifest 不发送给导师，只用于生成和 QA。

### 15.5 跨邮件重复检查

发送前应把本封邮件与当前 batch 中其他导师邮件做 duplicate/similarity 检查。

允许重复：

- 称呼格式；
- 签名；
- 联系方式；
- URL；
- 简短固定事实。

需要拦截：

- 完整实质段落重复；
- 长句连续重复；
- 相同 research bridge；
- 相同具体 research question；
- 大段只替换导师名 / 学校名的正文。

如果发现正文主要内容可以通过“搜索替换导师名字”得到另一封邮件，则直接判定 **PERSONALIZATION_QA_FAIL**。

### 15.6 完成定义

一封导师邮件只有同时满足：

`PROTOCOL_VERIFIED + PERSONALIZATION_VERIFIED + CLAIMS_VERIFIED + ATTACHMENTS_VERIFIED`

才允许进入：

`OUTREACH_READY`

所以：

> **结构可以模板化，证据可以复用，但研究连接、讨论内容和申请动机必须专人专用。**

## 16. 新导师 CV 的 Utopia 实时刷新门禁

任何**首次联系的新导师**，都不得直接复用旧版 tailored CV 中的 Utopia 段落。

在生成该导师最终英语 CV 前，必须在**同一次套磁准备 run**里重新读取 Utopia 的当前证据，并重写 Utopia 相关内容。

### 16.1 当前证据源

默认按以下顺序刷新：

1. **`zhiheng-zhang-Mera/Utopia` 的当前 `main`**：确认已经合并、实际存在的能力与最新可验证状态；
2. **`zhiheng-zhang-Mera/Digital-City` 的当前 mission-book / reports / 当前规划**：确认最新研究方向、验收结论、已完成/未完成边界；
3. Application-Plan 中的 `materials/research-profile.md` / `project-positioning.md`：只作为叙事路由参考，**不能替代对 Utopia 当前仓库状态的刷新**。

默认只把**已合并 / 已验收 / 有明确证据**的内容写成 completed work。未完成工程书、planned series、尚未验收模块只能写成 future direction / planned extension。

### 16.2 每次刷新必须记录

在内部 package / manifest 中记录：

- `utopia_refresh_required: true`
- `utopia_refresh_at`
- `utopia_main_sha`
- `digital_city_main_sha`
- `utopia_completed_evidence_used`
- `utopia_current_limitations`
- `utopia_planned_direction_used`
- `utopia_cv_tailoring_reason`
- `utopia_refresh_status: VERIFIED | BLOCKED`

没有记录当前 SHA / evidence boundary，就不能把 CV 标成 ready。

### 16.3 CV 不是“项目更新日志”

实时刷新不等于把 Utopia 最近所有功能都塞进 CV。

生成时应：

1. 先确认 Utopia 当前真实状态；
2. 再根据导师方向挑选最相关的 **2–4 条**证据；
3. 用导师专属研究语言重新组织；
4. 保留一个清晰的 limitation / next research direction；
5. 删除与该导师无关的旧 Utopia bullet，而不是无限累加。

例如：

- ubiquitous / wearable PI → 强调 multi-device substrate、cross-device action、user confirmation、heterogeneous runtime direction；
- distributed / edge PI → 强调 gateway、device coordination、degraded-state handling、未来 placement/offloading；
- human-agent PI → 强调 ambiguity handling、confirmation、user override、inspectable action state；
- AI4SE PI → Utopia 可以缩短，把 Hns/Boss 放前面，只保留与 systems integration / validation 相关的 Utopia evidence。

### 16.4 旧 CV 的处理

旧 CV 可以作为：

- 排版模板；
- 个人基础信息源；
- 已验证教育/技能事实源。

但对**新导师**：

> 旧 CV 中的 Utopia 项目段落默认视为 `STALE_FOR_NEW_OUTREACH`。

必须先 refresh，再生成新的 `.tex` / PDF。

### 16.5 发送门禁

新导师套磁只有在：

`UTOPIA_REFRESH_VERIFIED + CV_REBUILT + CV_PDF_VERIFIED + PROTOCOL_VERIFIED + PERSONALIZATION_VERIFIED`

全部通过后，CV 才能作为附件进入：

`OUTREACH_READY`

如果 Utopia 当前状态无法可靠读取或验收边界不清楚，宁可保留更保守的旧安全 claim，也不能根据 commit 名称或规划文件猜测“已经完成”。

## 17. Gmail 内嵌执行层

默认申请邮箱已经验证为：

`zhiheng0mera@gmail.com`

仓库只保存**账号标识、thread/message 映射、状态与标签约定**，不保存 Gmail 密码、OAuth token 或其他认证秘密。

机器配置：

- `data/integrations.yaml`
- `data/outreach.yaml`

### 17.1 分工

**Gmail connector 负责动作：**

- search；
- read message/thread；
- create/update draft；
- send draft / send email；
- label；
- archive。

**Application-Plan 负责状态：**

- supervisor/application ID；
- contact email；
- Gmail thread ID；
- last message ID；
- sent/replied/waiting 状态；
- follow-up lifecycle；
- application dashboard。

### 17.2 默认邮箱标签

统一使用：

- `PhD-Application`
- `PhD-Application/Outreach`
- `PhD-Application/Waiting`
- `PhD-Application/Replied`
- `PhD-Application/Referee`

新发送的导师套磁默认进入 `Outreach + Waiting`。检测到实质回复后，应加入 `Replied` 并移除 `Waiting`。

推荐人邮件使用 `Referee`。

### 17.3 在当前对话中直接操作

当前 ChatGPT 对话可作为邮箱控制面。

支持的自然语言操作包括：

- “检查申请邮箱”
- “查 X 导师有没有回复”
- “打开 X 导师整个线程”
- “给 X 导师生成并保存 Gmail 草稿”
- “修改 X 的草稿”
- “发送刚才审核过的 X 草稿”
- “给 X 导师回复这封邮件”
- “同步套磁状态”
- “把结束的申请邮件归档”

不需要用户自己复制到 Gmail 再执行。

### 17.4 发送策略

默认流程：

`PACKAGE_READY → Gmail Draft → HUMAN_REVIEW → explicit SEND → thread mapping → Waiting`

因此：

- 生成新套磁时默认先建 draft；
- 用户明确说“发送/发出去”时，可以从当前对话直接发送；
- 回复邮件前必须先读取原 thread；
- 发送后必须把真实 Gmail `thread_id` / `message_id` 回写 `data/outreach.yaml`；
- 只有 Gmail 实际返回发送成功，才能把状态改为 `SENT / WAITING`。

### 17.5 历史邮件迁移

2026-09-18 等旧套磁历史仍以 `applications/OUTREACH-LOG.md` 为真实证据。

如果默认邮箱中暂时找不到对应 thread：

- 不得推断“没发过”；
- 不得推断“没回复”；
- `data/outreach.yaml` 中保持 `mailbox_mapping_status: PENDING`；
- 等找到真实 thread、导入其他邮箱证据或用户确认后再完成映射。

### 17.6 邮箱同步规则

“同步申请邮箱”至少执行：

1. 读取 `data/outreach.yaml` 中已经映射的 thread；
2. 搜索当前 inbox / sent 中新的申请相关消息；
3. 判断是否为 substantive reply / OOO / bounce；
4. 更新 Gmail labels；
5. 更新 `data/outreach.yaml`；
6. 必要时更新 `applications/OUTREACH-LOG.md`；
7. 重新计算 follow-up / unlock 状态；
8. 刷新 README 看板。

### 17.7 安全边界

允许从当前对话直接执行，但：

- **draft 创建/修改**不需要额外“发送确认”；
- **真正发送新邮件或回复**需要用户在当次对话明确要求发送；
- archive / label 等非破坏性整理可以按用户指令直接执行；
- 删除邮件、Trash 等破坏性动作不属于默认 application pipeline。

## 18. Outreach 批次去同校规则

导师套磁按 **batch / round** 组织。批次层规则比 §6 的同系联系锁更严格。

### 18.1 每轮一校一人

> **同一 outreach round 中，同一 university 最多放 1 位导师。**

无论是否属于不同 department / school，只要归属于同一大学实体，就不能在同一轮里同时发送。

示例：

- HKUST：Mo Li / Shing-Chi Cheung / Song Guo 同一轮只能选一个；
- HKU：Chenshu Wu / Heming Cui / Zuming Jiang / Ka Ho Chow 同一轮只能选一个；
- CityU：Heqing Huang / Zhenjiang Li / Nan Guan / Weifa Liang 同一轮只能选一个；
- SUTD：Ruochen Zhao / Thanh Le-Cong 同一轮只能选一个。

### 18.2 批次唯一键

机器层统一使用：

`institution_batch_key`

每个 batch 中该键必须唯一。

若发现重复 university：

`BATCH_SAME_SCHOOL_DUPLICATE = QA_FAIL`

不得靠“不同系”“不同 campus 页面”或“不同导师研究方向”绕过。

港校大陆分校如果是**独立招生实体 / 独立申请系统**，可以使用独立 institution key，例如：

- `cuhk-hk`
- `cuhk-shenzhen`
- `hkust-hk`
- `hkust-guangzhou`

但必须按真实招生实体记录，不能为了多发邮件人为拆 key。

### 18.3 什么算一轮中的投递

计入 supervisor outreach batch：

- 新 cold email；
- final follow-up；
- 对已有导师线程的主动 research follow-up；
- form-based supervisor inquiry。

不计入 supervisor outreach batch：

- 正式 PhD portal submission；
- application fee；
- referee invitation；
- 已收到导师回复后的被动 reply；
- warm/private channel 中对方明确要求的材料回传。

因此 **SUTD Jan-2027 formal application 可以独立提交**，即使当日没有安排新的 SUTD supervisor cold outreach。

### 18.4 选批次顺序

生成“今天最合适的一轮”时，按：

`OUTREACH_READY > 只差 send-time refresh > 可当天补完 protocol/package > WATCH/BLOCKED`

并在满足研究优先级的前提下：

1. 每校最多 1 人；
2. 优先 current explicit recruitment / funding；
3. 优先已经解除历史 thread lock 的学校；
4. 有 academic hard/unclear gate 的导师不进入当前发送轮；
5. 缺 required attachment / publication / rank 的导师不进入当前发送轮；
6. 同校的第二导师自动进入下一轮候选，不与第一导师竞争同一轮。

### 18.5 批次状态

每轮至少区分：

- `SELECTED_FOR_ROUND`
- `NEEDS_SEND_TIME_REFRESH`
- `READY_FOR_HUMAN_REVIEW`
- `SENT`
- `DEFERRED_SAME_SCHOOL`
- `DEFERRED_BLOCKED`

只有全部 selected 项通过各自 send-time QA 后，才称该 round 为 ready；不要求同一时刻发送，可以按目标学校当地工作时段分开发送。
