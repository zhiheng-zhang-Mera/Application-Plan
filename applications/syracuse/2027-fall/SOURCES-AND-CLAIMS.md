# 来源、已确认事实与未确认项

核验日期：2026-10-27。事实层级分为：官方公开政策、招生办对本人的邮件回复、申请人确认、公开项目证据、写作推断/未来计划。

## 招生与操作

| 事项 | 结论及边界 | 来源 |
|---|---|---|
| 项目名称 | Ph.D. in Computer and Information Science and Engineering，EECS / ECS | [CISE 官方页](https://ecs.syracuse.edu/academics/graduate-programs/doctor-of-philosophy-in-computer-and-information-science-and-engineering) |
| Fall 截止 | 公开列 12 月 15 日；本包按 Fall 2027 周期安排 2026-12-15，时间/时区待网申 | [ECS requirements](https://ecs.syracuse.edu/admissions/graduate/application-requirements) |
| 基本材料与费用 | 成绩单、推荐信、personal statement、CV、适用考试信息、申请及 USD 75 费用 | 同上 |
| SOP 限制 / 推荐信封数 | 当前公开清单没有给出；必须在 CISE 网申确认，不标为无限制或固定三封 | 同上 |
| 额外 writing sample / research proposal | 公共清单未列；不保证程序特定页面完全无额外要求 | 同上 |
| GRE | Spring/Fall 2027 optional | 同上 |
| 语言豁免 | 学校 2026-10-26 美国时间邮件确认本人可免语言考试，提交后发邮件请求处理；对应墨尔本 10 月 27 日 | 原始邮件已在本人邮箱核验；不公开原邮件、头信息或私有链接 |
| 招生面试 | ECS FAQ 明确不强制入学面试，不外推至整个博士期间 | [ECS Graduate Admissions FAQ](https://ecs.syracuse.edu/admissions/graduate) |
| 提前导师接收 | 已核公共清单没有列为申请前置，不等于教授承诺或无任何后续匹配 | CISE 页与 ECS requirements |
| 资助 | 随申请由系里考虑，RA/TA/fellowship 竞争分配；本人尚无资助决定 | ECS requirements 的 Tuition and Financial Aid |
| Fellowship 服务 | 对相应 fellowship 支持期，官方描述无额外服务职责；不能外推至以后转 RA/TA 的年份 | 同上及 Graduate Admissions |
| 财力材料 | 不是招生审核必需；录取后的 I-20 流程仍有证明要求 | ECS requirements |
| 非官方成绩单 | 可用于审理；正式学历文件仍须按录取及入学要求补齐 | ECS requirements |

当前 catalog 页面在公开检索中遇到验证页面，本包未将未读到的 catalog 条款写成事实。网申登录后题目也未实际读取。

## 申请人事实

- 姓名/学术邮箱：Zhiheng Zhang，zhiheng0mera@gmail.com，沿用已发送雪城咨询与既有 CV。
- UBC Okanagan，BSc Computer Science，2020-2024，2024 年获学位：申请人确认与既有当前申请材料一致；不沿用旧模板的 Vancouver 错误。
- Melbourne，Master of Computer Science，2025-present，预计 late 2026 完成；两年制第一年课程、第二年研究：申请人当前说明。最终成绩及学位状态仍待完成。
- Richard Sinnott / Android privacy-evidence master's research：沿用 [2026-10-25 CV](../../concordia/2026-10-25/Shin-Hwei-Tan/CV.md) 及该批已核材料；独立系统项目不包装成导师指导成果。
- COSC 499 的 93/100：已有 Bachelor Score.csv 中 2024 Summer 课程记录，且 10 月 25 日来源账本已记录。不宣称该 CSV 是可替代正式成绩单的官方文件。
- 软件工程、算法、Research Methods 等课程名沿用既有 CV/学术记录。没有新造 GPA、排名、学历或奖项。
- 研究手稿准备中：来自申请人最近的 DS-Hns 文稿修订工作说明。没有独立核实正式发表、录用或 arXiv 公开号，因此只写 in preparation。

写作基线：[研究画像](../../../materials/research-profile.md)、[英文研究陈述母版](../../../materials/RESEARCH-STATEMENT-MASTER.md)、[最近 CV](../../concordia/2026-10-25/Shin-Hwei-Tan/CV.md)。其中旧文件是历史材料，不是对每个项目最新能力的认证。

## 公开项目证据

| 对象 | 本次允许使用的表述 | 可追溯来源 |
|---|---|---|
| Utopia | 整合型后继项目，两台 Windows 执行端 + Android/Web 控制；架构、AI 辅助集成与证据验收 | [实现快照](https://github.com/zhiheng-zhang-Mera/utopia/tree/944f47dd6c7e18b3388b6d769dbbb6dddbe74f00) |
| Utopia / Digital-City | 有界跨主机结果、失败/重试与可核对轨迹；不宣称开放世界通用自治 | [REX-990](https://github.com/zhiheng-zhang-Mera/Digital-City/blob/6d639d4a38f29e3edeab8805f623216d8101e41a/mission-book/reports/REX-990/ACCEPTANCE_REPORT.md) |
| DS-Hns | 持久任务状态、检查点与恢复检查 | [checkpoint](https://github.com/zhiheng-zhang-Mera/DS-Hns/blob/4023749389233a424b48320f6d30c160784986bd/app/engineering/checkpoint.cjs)；[task continuity](https://github.com/zhiheng-zhang-Mera/DS-Hns/blob/4023749389233a424b48320f6d30c160784986bd/app/core/task-continuity.cjs) |
| DS-Hns 具体观察 | 已持久化边界的恢复与 effect/checkpoint gap 不同，后者仍可重复动作；这是有界组件实验，不是产品级 exactly-once 结论 | [2026-10-26 实验进展](https://github.com/zhiheng-zhang-Mera/DS-Hns/blob/4023749389233a424b48320f6d30c160784986bd/docs/paper-material/revision-2026-10/PROGRESS.md) |
| Codex Boss | 多智能体编排、持久恢复、确定性验收与主机观察证据 | [recovery scheduler](https://github.com/zhiheng-zhang-Mera/Codex-Boss/blob/8df428eaa437a409368401e95194e40266b83080/electron/commander/recovery-scheduler.ts)；[verification collector](https://github.com/zhiheng-zhang-Mera/Codex-Boss/blob/8df428eaa437a409368401e95194e40266b83080/electron/commander/verification-collector.ts) |
| Privacy Lens | Android 隐私证据研究原型与可复核产物 | [公开 artifact](https://github.com/zhiheng-zhang-Mera/privacy-lens-research-artifact)；[既有来源账本](../../concordia/2026-10-25/SOURCES-AND-CLAIMS.md) |

不复制大规模历史测试计数作为个人能力或泛化性能排名；不加入缺乏证据的运行时速度优势。DS-Hns 的遗留 recoveryMs 定义另有 [metric erratum](https://github.com/zhiheng-zhang-Mera/DS-Hns/blob/4023749389233a424b48320f6d30c160784986bd/docs/paper-material/revision-2026-10/METRIC_ERRATUM.md)，因此本包不使用相关速度比较。

Celestial-Throne 的私人实现细节未进入申请包；Smart Glass 的提案也未当成已实现产品。项目方向可以延伸，但实际博士成果和未来实验均没有被写成既有成果。

## 导师与研究计划

公开教师主页及推断见 [FACULTY-FIT.md](FACULTY-FIT.md)。匹配是基于方法和研究主题的判断，不等于名额或接收证据。

SOP/Research Summary 的基准任务、状态检查、扰动、指标和分析方向均是拟研究方案，未宣称已经取得这些未来实验的结果。摘要中特别区分执行 agent 与独立定义/验证的 outcome checker。

## 发布边界

只发布该公开申请库所需的学术材料与管理模板。未新增原始邮件、证件、原始成绩单、银行/投资资料、私有仓库实现或不相关个人信息。邮件模板的占位符不是已发生的外部动作。
