# 2026-10-16 二次重构 QA：学校级去重 + PDF 编译 + Gmail 草稿替换

> **SECOND_PASS_COMPLETE / DRAFTS_NOT_SENT / OFFICIAL_APPLICATION_NOT_SUBMITTED**。当前有效执行池：[10/16 V2 Pool](../../targets/CONTACT-POOL-2026-10-16-UK-HK-SUTD.md)。旧 v1 邮件历史原文仍保存在 [OUTREACH-DRAFTS.md](OUTREACH-DRAFTS.md)，但 v1 Gmail 草稿已移 Trash。

## 1. 原因与实际纠偏

- 旧 v1 同时给 HKBU **Henry Dai + Amelie Zhou** 建了草稿，违反用户希望避免同校同期联络的限制。
- 旧 v1 给 Edinburgh **Antonio Barbalace** 建了草稿，但 Edinburgh **Mahesh Marina 10/12 已发首信、仍在等回复**；这也违反大学级别互斥原则。
- 旧 v1 Henry Dai 草稿缺本人主页要求的 CV + 两份 transcript；Amelie 和其他草稿也缺 CV。
- 本轮选用 **HKBU Henry / Lingnan Yiqin / Lancaster Adrian** 三所不同大学；HKBU Amelie、Edinburgh Antonio 停止 active 准备；Surrey Gregory Chockler 列 WATCH（学费、入学面试和资助不利）。
- SUTD Ruochen Zhao 10/09 已发，标准 Jan 2027 PhD 不要求导师提前同意，**不得发重复首信**；仅编译程序级正式申请材料。

## 2. Gmail 唯一有效草稿（已读取核实邮箱 Labels=DRAFT）

| 大学 | 联系人 | 新 Gmail message ID | 状态 | Gmail 附件 |
|---|---|---|---|---|
| HKBU | Henry Hong-Ning Dai | [1a1431c44c36f547](https://mail.google.com/mail/u/?authuser=zhiheng0mera%40gmail.com#all/1a1431c44c36f547) | DRAFT_NOT_SENT | **4件**：HKBU_Henry_Dai_CV.pdf, HKBU_Henry_Dai_Research_Note.pdf, UBCTranscript_Zhang_Zhiheng_final.pdf, Unimelb WAM.pdf |
| Lingnan University | Yiqin Deng | [1a1431c6660af6be](https://mail.google.com/mail/u/?authuser=zhiheng0mera%40gmail.com#all/1a1431c6660af6be) | DRAFT_NOT_SENT | **4件**：Lingnan_Yiqin_Deng_CV.pdf, Lingnan_Yiqin_Deng_Research_Note.pdf, UBCTranscript_Zhang_Zhiheng_final.pdf, Unimelb WAM.pdf |
| Lancaster University | Adrian Friday | [1a14316bf60f34e4](https://mail.google.com/mail/u/?authuser=zhiheng0mera%40gmail.com#all/1a14316bf60f34e4) | DRAFT_NOT_SENT | **2件**：Lancaster_Adrian_Friday_CV.pdf, Lancaster_Adrian_Friday_Research_Note.pdf |

Draft IDs (not message IDs):
- Henry: `r4006917016328847035`
- Yiqin: `r7272833963742749606`
- Adrian: `r-6260439245680269276`

### 旧草稿替换记录（Gmail 真正执行）

| v1 导师 | Gmail old message ID | 实际 Gmail 状态 |
|---|---|---|
| Henry Dai | `1a1430b1337bea27` | `DRAFT + TRASH`，被新 v2 替代 |
| Amelie Zhou | `1a1430b1ccf92402` | `DRAFT + TRASH`，HKBU 同校候补冻结 |
| Antonio Barbalace | `1a1430b2743fe0ac` | `DRAFT + TRASH`，Edinburgh Marina 已发 |
| Adrian Friday | `1a1430b32c0d125a` | `DRAFT + TRASH`，被新 v2 替代 |

邮箱 `list_drafts` 实际复验：今天只剩 **Henry / Yiqin / Adrian** 这三封新导师草稿，且互不属于同一大学。Trash 为可恢复状态；未执行永久删除。

### 同日再次核正成绩记录措辞

在第一次 V2 草稿验证后，发现不能从 `Unimelb WAM.pdf` 的文件名推断其为 official final transcript。因此重新建立 Henry 和 Yiqin 的最终草稿，邮件明确写出“available Melbourne WAM record; final master's transcript pending”。两封中间 V2 草稿 `1a14316685a9c678` 与 `1a143169fd03bcd0` 已移入 Gmail Trash。最终草稿 message ID 如 §2。

## 3. 材料编译结果（8 个 PDF，含源文件；均非模拟文件）

由此前 GitHub Application-Plan 的 CV LaTeX 结构派生，分别真实运行 `pdflatex`；Research Note 和 SOP 根据新稿实际生成 PDF。PDF 已通过文本提取、页数、页面边界和样张渲染人工检查。

| PDF | 页数 | SHA256 首16位 | 角色 |
|---|---:|---|---|
| `HKBU_Henry_Dai_CV.pdf` | 1 | `e833cd07620745a6` | 招生页要求 CV |
| `HKBU_Henry_Dai_Research_Note.pdf` | 1 | `94502bfbf247db42` | ASE'25 VRExplorer 技术连接 |
| `Lingnan_Yiqin_Deng_CV.pdf` | 1 | `011c8255238bc5b5` | 招生页要求 CV |
| `Lingnan_Yiqin_Deng_Research_Note.pdf` | 1 | `de28b9265fb2ffb8` | edge task reliability / software systems |
| `Lancaster_Adrian_Friday_CV.pdf` | 1 | `8f9fe0af291b5643` | 研究履历 |
| `Lancaster_Adrian_Friday_Research_Note.pdf` | 1 | `36fbfe19af42f8be` | 泛在计算、真实任务与用户干预 |
| `SUTD_Jan2027_CV.pdf` | 1 | `f636e271e435f08a` | 标准 Jan intake direct PhD |
| `SUTD_Jan2027_Statement_of_Objectives.pdf` | 2 | `932f5d0d4d353f19` | 正式网申文字稿，未提交 |

**离线交付物**：`Application-Plan_2026-10-16_Outreach_v2.zip`；内有上表8个PDF、4个 CV.tex、4份研究/SOP的 Markdown 源、3封电子邮件纯文本和说明文件，**不含成绩单原件**。ZIP 是会话工作空间生成的附件，不是 GitHub 二进制文件，不能使用 GitHub 相对链接假装已上传到 repo。

## 4. 论文、项目和申请声明审查

- 10/16 重新读取 Utopia `main`，SHA `944f47dd6c7e18b3388b6d769dbbb6dddbe74f00`。
- 10/16 重新读取 Digital-City `main`，SHA `cde01b0f71b4d165484540c1c740abc168e43c90`；检验 [4IN1 acceptance](https://github.com/zhiheng-zhang-Mera/Digital-City/blob/main/mission-book/reports/4IN1-ACCEPTANCE/README.md) 对跨 Windows 主机有界结果与 limitations 的记录。
- **事实叙事**：已完成、冻结 DS-Hns / Codex Boss → 融合后已完成、冻结的 Utopia。Celestial 仍是未完成的下一代重构计划。
- 未声称本人已有正式录用/同行评审论文；Henry Dai 研究连接采用其实际 ASE 2025 论文 **VRExplorer** 的 Entity-Action-Task VR 交互测试机制，并讨论独立的长任务结果验收问题。
- 未声称构建完成商用 wearable/VR，未声称两台个人服务器已主备自动接管。
- `Unimelb WAM.pdf` 为已取得的墨大学业材料，**不能写成最终硕士成绩或完成证明**。官方 transcript/豁免资格仍以目标学校最终审核为准。

## 5. 导师协议及剩余发送门禁

| 导师 | 本人公开要求及现状 | Remaining Gate |
|---|---|---|
| Henry Dai | 个人主页要求 read recent research、CV、undergraduate/postgraduate transcript、publications(if any)。v2 已看 ASE'25 VRExplorer、附 CV+UBC transcript+现有 Melbourne WAM 记录；后者不是已核实的硕士最终正式成绩单，若导师必须 official postgraduate transcript 则仍有发送前材料缺口。 | **2027 实际 capacity、资金/自费可行性、本人审查** |
| Yiqin Deng | 个人页面明确 Spring/Fall 2027 PhD、CV、transcripts、brief research interests；v2 已附 CV、UBC transcript、现有 Melbourne WAM record 和研究兴趣说明；最终硕士正式成绩单尚未完成，不得称已满足 official transcript 门槛。 | Research Assistant Professor 能否担任主导师、Data Science PhD项目与本人的 software-focused systems methods 是否兼容 |
| Adrian Friday | 本人官网欢迎研究实务类 ubicomp PhD inquiry；v2 附 CV + initial one-page concept。 | 国际生 funding/自费总成本、2027 具体 capacity/招生面试与语言要求 |
| SUTD direct Jan | CV/SOP PDF 已编译；申请截止 2026-10-30、无需导师提前同意。 | 3封推荐、portal 中成绩/学历/英语要求、最后申请费/正式提交：**全部未执行** |

## 6. 数据保护和动作权限

- UBC 正式成绩单与现有 Melbourne WAM 记录只从已发 Gmail 的原附件恢复到临时工作空间并按教授个人要求**附在未发送的 Gmail 草稿中**；从未写入本 public GitHub repo，也未打包进 ZIP。
- 为防止混淆，旧 v1 草稿已移动到 Gmail Trash；这是可恢复操作，不涉及 SENT 实际历史邮件。
- 用户尚未要求发送任何邮件或提交大学正式申请：`NO_SEND`、`NO_APPLICATION_PAYMENT`、`NO_SUBMISSION`。
- 如用户要正式发送，须先重新对账同校锁及目标大学最新 eligibility/funding/admissions；与材料已编译是两回事。

## 7. Primary links

- HKBU Dai recruiting page: https://www.comp.hkbu.edu.hk/~henrydai/
- HKBU VRExplorer: https://www.comp.hkbu.edu.hk/~henrydai/pubs/VRExplorer_ASE25.pdf
- Lingnan Deng recruiting page: https://www.ln.edu.hk/sds/dids/division/people/professor-deng-yiqin
- Lingnan admissions: https://www.ln.edu.hk/rpg/admission/application-for-admission
- Lancaster Friday: https://www.lancaster.ac.uk/sci-tech/about-us/people/adrian-friday
- Lancaster research degree: https://www.lancaster.ac.uk/scc/study/phd/self-funded-phd/
- SUTD admissions: https://www.sutd.edu.sg/programme-listing/sutd-phd-programme/application/
