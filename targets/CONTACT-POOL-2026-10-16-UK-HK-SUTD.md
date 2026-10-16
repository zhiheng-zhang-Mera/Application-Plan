# 2026-10-16 今日联络池 — 第二轮重构（学校级去重）

> **本版覆盖 10/16 上一版候选排序。新建/替换 3 封 Gmail 草稿，但全部 `DRAFT_NOT_SENT`。** [第二版附件/草稿 QA](../tracking-hist/2026-10-16/V2-MATERIALS-AND-GMAIL-QA.md)。马来西亚 USM/UTP 仍保留在早期预核池，但不进入本日联络队列。

## 同校互斥原则

- **按整个 university / institutional brand 互斥**，不以院系、研究组、校园或城市分拆：同校同时最多一个活跃导师 cold/warm/sent 待处理链路；新建第二导师仅可 WATCH/DEFER，绝不同时进入待发队列。
- 已发邮件/获得回复/有面试的导师优先于新草稿；不将「只建草稿」误写成实际联系。
- 历史线程可以按执行规则关闭，只有复核 Gmail 后确认现有沟通已结束，才能释放同校锁；warm、申请沟通和面试不能自动超时释放。
- 同校替代导师可保存研究记录和历史草稿审计，但不能保有并列**活跃** Gmail 草稿。本轮已将旧 Amelie、Antonio 以及 Henry/Adrian 的 v1 草稿移到 Gmail Trash（非永久删除）。

## A. 今天实际可继续准备的不同学校

| 顺位 | 大学 | 唯一活跃联系人 / 项目 | 2027 招生信号 | Gmail / 附件状态 | 主要风险 |
|---:|---|---|---|---|---|
| 0 | SUTD | Ruochen Zhao；**Jan 2027 标准 PhD 直接网申** | 2026-10-30 截止；提前导师同意非前置 | 10/09 首信已发，无新首信；v2 Jan SOP PDF + CV PDF 本地已编译，申请未提交 | 可能面试、3位推荐人、语言豁免个人认定待核 |
| 1 | HKBU | Henry Hong-Ning Dai | 本人主页明确 PhD 招生意向，未承诺 2027 座位 | [新 Gmail 草稿](https://mail.google.com/mail/u/?authuser=zhiheng0mera%40gmail.com#all/1a14316685a9c678) 4附件：CV、Research Note、UBC transcript、Melbourne record | 与 XR/IoT 系统可靠性贴近；确认 2027 capacity/funding/录取门禁 |
| 2 | Lingnan University | Yiqin Deng | 本人明确招聘 **Spring & Fall 2027 PhD** | [新 Gmail 草稿](https://mail.google.com/mail/u/?authuser=zhiheng0mera%40gmail.com#all/1a143169fd03bcd0) 4附件（同上种类） | 重点是无线网络/LLM适配；用户软件系统方法是否适配、Research Assistant Professor 能否主导导师待确认；Data Science PhD 有课程要求 |
| 3 | Lancaster University | Adrian Friday | 官网公开欢迎潜在 PhD 联系，具体 2027 座位未知 | [新 Gmail 草稿](https://mail.google.com/mail/u/?authuser=zhiheng0mera%40gmail.com#all/1a14316bf60f34e4) 2附件：CV + Research Note | 研究偏真实环境/可持续性；国际费用/导师容量/资助不明 |

**这不是录取成功率的百分比排名**。已发邮件/有实质回复的 warm leads 另为 A0 优先级；新 Gmail 草稿不代表已经发送，更不是正式申请。

## B. 旧信优先与同校暂停

| University 锁 | 当前唯一优先对象 / 证据 | 不得同期另发 |
|---|---|---|
| HKUST（含 GZ 同品牌学校的保守锁定） | Mo Li / WANDS：10/15 面谈、10/16 感谢信已发 | HKUST(GZ) Zhidan Liu 等 |
| Edinburgh | Mahesh Marina：10/12 SENT_WAITING | Antonio Barbalace、Paul Patras、Adriana Sejfia |
| HKBU | Henry Dai：V2 DRAFT，待人工审核 | Amelie Chi Zhou（原草稿已移 Trash） |
| SUTD | Ruochen Zhao：10/09 SENT_WAITING | 其他 SUTD 导师的同期 cold email；允许标准 Jan 2027 直申 |
| Concordia | Peter Chen：已正面回复、国际身份已说明 | 该校其他导师 |
| UM | Li Li：旧渠道 warm + 历史申请 | 其他 UM 导师；核对提交批次 |
| HKU | Chenshu Wu：10/12 已发 | 其他 HKU 导师 |
| NUS | Chengpeng Wang：10/12 已发 | 其他 NUS 导师 |
| CityUHK | Zhenjiang Li：10/09 已发 | 其他 CityUHK 导师，除非复核后释放锁 |
| PolyU | Yu Liu：10/09 已发 | 其他 PolyU 导师，除非复核后释放锁 |
| NYU (Courant / Shanghai) | Qiaoyu Tan：10/12 已发 | 其他 NYU 导师 |
| CUHK | James Cheng：10/13 已明确组内无名额（含自费），线程已结束 | 不将整个 CUHK 判无名额；新 PI 可另行筛选，但本轮不主动联系 |

## C. 候补 / 低 ROI

- **HKBU Amelie Zhou**：已公开招 HPC/distributed PhD；仅当 Henry 的线索正式关闭且新研究适配核验后释放。
- **Edinburgh Antonio Barbalace**：OS/runtime 研究契合，但是 Mahesh Marina 的主动线程仍在等待；禁止并发。旧草稿移至 Trash。
- **Lancaster Nigel Davies**：同校候补，被 Adrian 的活跃草稿锁定。
- **Surrey Gregory Chockler**：分布式容错方向契合，但 2027 overseas tuition、入学面试和无明确 2027 PI capacity，使其只列 WATCH；不建草稿。
- **UCL / Southampton**：原候选保留历史，分别等 2027 项目与学术/资助门槛核验；不为填名额勉强投递。
- CUHK James Cheng 已明确无组内名额；Dartmouth Shawn Shan / Penn State Yuchen Yang HOLD 不动。

## D. 当期可执行状态与证据边界

- 三封 Gmail 新草稿均核验 `DRAFT` 与真实附件；**没有发信授权**。
- CV PDF ×4（含 SUTD Jan），Research Note PDF ×3，SUTD Jan Statement of Objectives PDF ×1 均已从源编译并渲染校验。保存于当期本地 ZIP；GitHub 只存文件名、SHA、状态，不公开 UBC/Melbourne 官方成绩单。
- Utopia 冻结 main SHA `944f47dd6c7e18b3388b6d769dbbb6dddbe74f00`；Digital-City 当前 main SHA `cde01b0f71b4d165484540c1c740abc168e43c90`（2026-10-16 本轮读取）。邮件以有界实物 Windows×2、Android 控制和可复核跨机执行/回放为证据；Celestial / wearable / XR consumer validation 不写成已完成。
- HKBU Henry 已结合 ASE 2025 **VRExplorer** 真正具体技术点（Entity-Action-Task scene interaction）形成 research bridge；不是只把论文标题填进模板。
- Lingnan 2027 PhD 招收与主导师资格不是同一回事；2027 预期导师体系仍须确认。
- 全批保留 **NO_SEND**, **NO_APPLICATION_SUBMISSION**。

## Official references (rechecked 2026-10-16)

- SUTD application and FAQ: https://www.sutd.edu.sg/programme-listing/sutd-phd-programme/application/ ; https://www.sutd.edu.sg/programme-listing/sutd-phd-programme/faq/
- HKBU Dai homepage / requirements: https://www.comp.hkbu.edu.hk/~henrydai/
- HKBU VRExplorer paper: https://www.comp.hkbu.edu.hk/~henrydai/pubs/VRExplorer_ASE25.pdf
- Lingnan Deng recruitment: https://www.ln.edu.hk/sds/dids/division/people/professor-deng-yiqin
- Lingnan direct admissions: https://www.ln.edu.hk/rpg/admission/application-for-admission
- Lingnan Data Science requirements: https://www.ln.edu.hk/rpg/admission/requirement/additional-for-mphil-phd-in-data-science-programmes
- Lancaster Friday profile: https://www.lancaster.ac.uk/sci-tech/about-us/people/adrian-friday
- Lancaster programme: https://www.lancaster.ac.uk/scc/study/phd/self-funded-phd/
- Surrey CS PhD: https://www.surrey.ac.uk/postgraduate/computer-science-phd
