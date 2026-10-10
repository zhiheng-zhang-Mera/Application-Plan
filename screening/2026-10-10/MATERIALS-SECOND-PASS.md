# 2026-10-10 申请材料二次核验报告（证据优先）

> 与首轮“研究方向匹配”不同，本轮采用**实际课程成绩 CSV → 已发出的 UBC 官方成绩单 PDF → 已生成 CV / 研究声明 → Utopia/City 验收证据 → 校方与 PI 官网**逐层交叉核查。当前是 2026-10-10 的可审计筛选，不是录取预测或正式成绩等价认定。新增候选均未获发信授权，也没有生成新 Gmail 草稿。**仓库公开，严禁在本报告记录学号、护照、签证/移民个人信息、私人联系方式。**

## 最新事实更正（2026-10-10，当事人已确认）

**之前把旧 `Credentials: None to date` 注记等同于“最终成绩单不存在／学位尚未获得／必须重新开成绩单”属于错误解释，已纠正。** UBC Okanagan BSc CS 已于 **2024 年获得**；现有本科成绩单是**官方最终版**。这两项均由申请人明确确认。PDF 中出现过的该注记仅作为原文事实记录，不否定学位已取得。是否另交一张独立毕业证，只由目标学校要求决定；本轮不再设置通用新版本科成绩单门禁。详见 [权威状态](../../materials/UBC-DEGREE-TRANSCRIPT-CONFIRMATION.md)。

## 一、申请人可据以决策的证据

| 事实对象 | 实际来源/抽取法 | 核验结果及适用边界 |
|---|---|---|
| UBC 本科 | `Documents/Bachelor Score.csv` / 实际已发送给 Peter Chen 的 PDF | UBC Okanagan（须保留 campus 准确性）；四年 BSc CS，完成年份依既有学位历史 2024，本科学位**已于 2024 年获得，现有成绩单为官方最终版（申请人直接确认）**；历史 PDF 曾显示 `UBC Credentials: None to date`，该备注不推翻授位事实。 |
| UBC 全部有分数课程 | 40 条有百分成绩记录，含一次 COSC304 45/F 及之后 90/A+ 重修；按成绩×课程 credit，分母 123 attempted credits | **78.05%**（非官方、含不及格前次及重修；已取得通过学分约 120，不得把 123 attempted 当 123 earned）。旧成绩单如学校采取 last-attempt 或 programme GPA 规则，该数字需另算、不得当作 official cumulative GPA。 |
| UBC 三、四学年 | 同样按课程 credit 加权，60 attempted | **78.75%**。 |
| UBC 第四学年 | 同样，30 attempted | **83.90%**，可作为 *fourth-year coursework average (derived)*，不是官方 final-year honours 或 class rank。 |
| UBC COSC 专业课 | **原表真实记录的 19 个已评分 COSC 课项**，60 attempted，含重修前不及格 | **79.05%**，不能把课程平均当 programme honours。 |
| 墨大研究型 CS MSc | `Documents/Master Score.csv` 8 门 2025 课×12.5 CP + 2026 已评估研究段 COMP90078/79 各25 CP = 150 completed assessed CP | 计算 `(100×授课成绩加权均分 + 50×75)/150` = **67.50 WAM（derived snapshot）**；非最终正式成绩单。 |
| 硕士 Thesis / Research Project | 同一 CSV：已评估 first 40/100 获 30/40，规范化为 75%；COMP90080/81 后续各25 CP 标 pending | 30/40 不等于整份论文 75，也不等于最终硕士分数；尚缺当前官方 Melbourne transcript。 |
| 硕士加权理论上限（仅此模型） | 150 CP 已评估得分 WAM 67.5，剩余50 CP最高100，总200 CP | `(150*67.5+50*100)/200=75.625`。这个是**CSV 的理论上限，不等于 official outcome**，更不能自动外推任何 UK Distinction/First 等价。 |
| 当前研究 CV 和声明 | `tracking-hist/2026-10-9/*/CV.tex` 与 `materials/RESEARCH-STATEMENT-MASTER.md` | 可核已有跨主机软件和系统研究工程，学术科研输出无 confirmed peer-reviewed publication、无已验证生产级 wearable。无可核官方 class rank，不能用课程 class size 和 class average 冒充 rank。 |
| 项目真实证据 | [Utopia README](https://github.com/zhiheng-zhang-Mera/utopia/blob/main/README.md)、[2026-10-07 4-in-1](https://github.com/zhiheng-zhang-Mera/Digital-City/blob/main/mission-book/reports/4IN1-ACCEPTANCE/README.md)、[2026-10-08 REX-890](https://github.com/zhiheng-zhang-Mera/Digital-City/blob/main/mission-book/finished/completed-2026-10-08/research-strengthening/README.md) | 真实双 Windows worker + Android control，有限真实跨主机结果/sha 回执，测试、故障注入与独立有限复现可据实写；REX 有未测量/跳过/Android 缺席/自然语言任务 NOT_TESTED 边界，不得将所有功能泛化成产品完整验证。Utopia 已冻结，Celestial 只是下一版计划。 |

**经申请人更正：** UBC BSc 2024 年已获得，现有本科成绩单就是官方最终版。此前以 `Credentials: None to date` 认定本科材料不完整属于误判。正式申请可以使用该最终版成绩单；仅在院校**单独明示**需要 degree certificate/award confirmation 时核对该额外文件。不得将未附到某封 Gmail 草稿与“文件不存在”混同。

**对外四个严禁：** ①不把 78.05 或67.5写为学校认可的 UK honours / 4.0 GPA；②不把 class size 当 rank；③不把未接收论文/私有 manuscript 说成 publication；④不把 Celestial 未来重构与 wearable / 双服务器实机部署说成已完成。

## 二、原 9 位导师二次裁决

| 导师 / 学校 | 学校/导师官网规则及实际材料冲突 | 新裁决与下一步 |
|---|---|---|
| **Chenshu Wu / HKU** | Lab [Openings](https://aiot.cs.hku.hk/openings/) 要 CV 中成绩/排名、transcript、拟研究方向和推荐 proposal，邮件题目 `[Prospective Student] Your Name - Your Affiliation`；页面部分期限仍为 **2025** 旧年份。你无官方 rank，硕士当前 official transcript 尚待核实；**本科最终官方 transcript 已存在但尚未附到本轮 HKU 草稿**；2027 正式主轮日期按 [HKU Graduate School](https://gradsch.hku.hk/) 核对。 | **A1 / WATCH_DOCUMENTS_CAPACITY**：研究匹配最强之一，申请人可按真实成绩/“rank not reported”答复；把**已存在**的本科最终官方成绩单加入草稿，核实硕士当前官方记录与 PI 的 2027 座位，不能发送自称 rank 的不实 CV。 |
| **Chengpeng Wang / NUS** | [NUS PhD 官方](https://www.comp.nus.edu.sg/programmes/pg/phdcs/admissions/) GRE **非强制**；英语为主授课的大学毕业生无需单靠“international”强制提交英语考试；Research Scholarship 最低 2nd Upper 等价，[奖学金](https://www.comp.nus.edu.sg/programmes/pg/phdcs/scholarships/) 有津贴+学费资助、仍竞争激烈。[RISE](https://chengpeng-wang.github.io/lab.html) PI 要 CV+短 research problems。QE 存在但用户允许准备负担可控的专业考试。 | **A1 / WATCH_SCHOLARSHIP_EQUIVALENCY**：由过往 BACKUP 上调。以 DS-Hns/Boss 和 Utopia 真实 agent 评估做研究对接；需 NUS 判断 UBC 学历/78.05 派生结果可否满足 2nd Upper；考试备考另评估，不因 QE 自动淘汰。 |
| **Zhidan Liu / HKUST(GZ)** | [MobiX group](https://liuzhidan.github.io/group/) 持续招 PhD，mobile/AIoT/GUI agent 与软件系统方法匹配；Fall 2027 特定名额/资金与官方 programme eligibility 未证实。 | **A2 / WATCH_CAPACITY**：有潜力；HKUST 清水湾 Mo Li 正在安排 WANDS 组讨论，暂缓同校系统的另一次盲投，但两校区并非完全相同招生实体。 |
| **Qiaoyu Tan / NYU Courant–Shanghai** | [PI](https://qiaoyu-tan.github.io/index.html) 明确招 Fall 2027 funded PhD，邮件要 CV+transcript；[项目](https://sh.nyu.edu/page/computer-science-phd-program) 前期纽约课程、其后上海长期科研，实际**非美国常驻**；PI 研究较偏 Graph ML / LLM、要避免变成纯模型算法。 | **A2 / WATCH_LOCATION_METHOD**：按 **亚洲实际驻地＋美国学位**分类；用户愿意上海研究及 agent-systems 子课题才提升，2027 申请截止另按官网核验。 |
| **Rui Tan / NTU** | [PI 明确 2027 fully-funded](https://personal.ntu.edu.sg/tanrui/phd.html) 是具体 **continuous-time foundation model for embodied AI with neuromorphic sensing** 课题，不等于任意 edge-runtime。NTU [CCDS 官方](https://www.ntu.edu.sg/computing/admissions/graduate-programmes/detail/ccds-phd-computing-datascience) 规定 strong Bachelor's >= Honours Distinction or equivalent；新版 CCDS GRE/GATE **可增强竞争力**，旧学院镜像曾写 required，需确认适用的 2027 项目规则。 | **A3 / WATCH_METHOD_ACADEMICS**：从 A1 下调；先确认导师能接受 software runtime/evaluation 主导，否则与不做纯算法/机器人控制的画像不符。 |
| **Jinke Ren / CUHK-Shenzhen** | [本人招生页](https://myweb.cuhk.edu.cn/jinkeren) 有 Fall 2027 招生及 CV、transcripts、representative publications；申请人目前没有被证实的 peer-reviewed work。 | **A3 / WATCH_PROTOCOL_GAP**：须先问 PI 是否接受开源 artifact / manuscript 作为代表研究能力，不将未发表稿件冒充 publication。 |
| **Zishen Wan / Columbia** | [PI 2027 全额资助](https://wan-research-group.github.io/join.html) 有 current opening；Columbia 工学院 [GRE optional（2026-07 起）](https://bulletin.columbia.edu/columbia-engineering/graduate-studies/graduate-admissions/)，加拿大本科 English exemption 应按 CS 录取说明确认；但课题偏芯片架构、硬件导向。 | **US-2 / WATCH_METHOD**：学术/标化门槛比英国 First 路线更干净，但纯软系方向占比须具体确认；不把 hard HW project 强行包装为 Utopia fit。 |
| **Jialun Cao / Imperial** | [Computing PhD 标准](https://www.imperial.ac.uk/computing/prospective-students/phd/phd-application-guidelines/) 倾向 First/Distinction 硕士，现有 67.5 加权及当前模型最高75.625 与其正常学术线明显不匹配；有 AI4SE funded position 不代表资格豁免。 | **UK-LOW / LOW_ROI_ACADEMIC_FLOOR**：保留历史供官方特殊评估或定向 PI 强支持，暂停常规材料投入；不标已收到学校正式拒绝。 |
| **Cecilia Mascolo / Cambridge** | [PhD CS](https://www.postgraduate.study.cam.ac.uk/courses/directory/cscspdpcs/requirements) 通常 First；[剑桥 Canadian First 82%](https://www.postgraduate.study.cam.ac.uk/apply/before/international-qualifications)，你的统一 attempted 加权78.05而非82；具体获资助导师位 2027 仍未证实。 | **UK-LOW / LOW_ROI_ACADEMIC_FLOOR**：方向贴，但正常学术资格不够稳；仅保留例外/官方确认路线，不优先投递。 |

### 重要细节：成绩等价不是算术转制

- **University of Edinburgh [加拿大标准](https://study.ed.ac.uk/programmes/regions/canada)**：2:1 对应百分制77%，First 82%。UBC **78.05%** 是含一次失败/重修的自算 attempted average，**在数值上过 2:1 参考值，但不等于招生处已经认定 qualified**。
- **Cambridge [Australia Master's 标准](https://www.postgraduate.study.cam.ac.uk/apply/before/international-qualifications)** 表示 Distinction equivalent 为 `High Distinction or 80%`；不代表“全英国硕士 Distinction 都需要80%”，也不代表墨大最终能等同英国任一等级。
- 奖学金名额及 PI 认可不互相替代；资助覆盖 international tuition 的证据必须核实，不能使用英本地 Home-only 项目伪装全额资助。

## 三、真正值得替代原英国低 ROI 名单的项目级路线

| 项目/地点 | 官方 2027 资格/资助 | 待确认 |
|---|---|---|
| **Edinburgh School of Informatics 2027 Institute-led PhD（优先）** | [ICSA 2027 PhD](https://study.ed.ac.uk/programmes/postgraduate-research/492-informatics-icsa-computer-architecture-compilation-and-system) 通常英国 2:1 或同等；[加拿大本科 2:1 为77%](https://study.ed.ac.uk/programmes/regions/canada)；[2027 IGS PhD fund](https://informatics.ed.ac.uk/study-with-us/our-degrees/postgraduate-research-programmes-and-centres-doctoral-training/postgraduate-research-funding-opportunities-0) 首轮 **2026-11-30 23:59**，每年通常 6–8 名资助、国际学费可覆盖、stipend 3.5 年；竞争强。 | **PROGRAM_WATCH / ACADEMIC_PLAUSIBLE**：须在截止前确定系统/agent 导师、官方加拿大本科计算规则、最新 official transcripts、英文授课证明/语言豁免、推荐信、奖学金与第一学位证明。资助未保证。 |
| **Lancaster Computing PhD 2027（条件保留）** | [2027 官方项目](https://www.lancaster.ac.uk/study/postgraduate/postgraduate-courses/computer-science-mphilphd/2027/) 要 2:1 或国际等价，可考虑 nonstandard；需要先找 PI/有资助项目。[Adrian Friday faculty](https://www.lancaster.ac.uk/sci-tech/about-us/people/adrian-friday) 允许潜在 PhD 主动联系；Pervasive Systems 与用户 ubicomp 相交，但具体项目偏 Sustainability。 | **PROGRAM_WATCH / FUNDING_ENGLISH_UNKNOWN**：未证实 2027 国际生全奖名额；英授学历能否满足英语要求未获校方批准，不能因“考虑其他英语学历”自动记 exempt。 |

## 四、申请文件缺项与校验优先级

1. **UBC 本科学位和官方最终成绩单已确认**：BSc CS 2024 年已获得，现有本科成绩单为官方最终版；无需额外索要新版 transcript。目标校若另要求学位证／award confirmation letter，按其明示清单单独处理；两封待发草稿若还没附本科成绩单，应使用现有官方文件添加附件。
2. **Melbourne 当前官方成绩单**：需覆盖已考核的课程/研究项目，但 `Master Score.csv` 与 Research Proposal 75 都不是 official final Master WAM。
3. **Class rank**：UBC 记录的是课程 `class_size`、`class_average`，不是申请人本人排名；不能推导，若学校未公布须如实报 `not reported / N/A`。
4. **正式国际英语豁免依据**：按每一院系项目检查 UBC 学士用英语授课的官方有效性；UK 部分项目未能核实适用豁免则继续 WATCH，绝不预设新 IELTS/TOEFL。
5. **项目套磁个性化**：确认 2027 PI capacity、personal/lab/contact/subject/附件、奖学金国际生适用、真实研究方法，再决定是否生成新材料；对有强制 publications 要求者必须如实解释没有 peer-reviewed works。
6. **推荐人状态**：当学校实际需要 2/3 封时，查看教授是否知情与愿意、材料是否足以支持，不能把仅看过课程/论文的推荐人描述成 Hns/Boss/Utopia 直接指导者。
7. **论文/软件状态**：Utopia、DS-Hns、Codex Boss 依用户确认完成且冻结；仅表述有界工程与实验，Celestial 未交付。旧个人材料不因论文 pipeline 存在就升级为已录用。

## 五、当前顺序结论

实际执行：**Mo Li / Peter Chen 两条 WARM 先维护** → 亚洲新 PI：**HKU Chenshu Wu、NUS Chengpeng Wang**（优先复用已有本科官方最终成绩单、核实硕士官方材料与奖学金等价）→ HKUST(GZ) Zhidan Liu/跨境 NYU Qiaoyu Tan（条件）→ Columbia 符合软件方向再提升 → 英国 **Edinburgh Institute-led + Lancaster programme WATCH**，而非将 Imperial/Cambridge 当成有把握的英语授课豁免与学术资格路线。

[刷新后的 PI Pool](POOL.md) · [机器版](POOL.yaml) · [审计入口](../README.md) · [实际 Gmail 追踪](../../tracking-hist/2026-10-10/README.md)。本次只写 GitHub 文档，不运行 CV/CI，不触动 Gmail，也不提交大学申请。
