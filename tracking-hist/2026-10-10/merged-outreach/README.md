# 2026-10-10 亚洲 + 英国合并后的导师联络池

> **用户要求：合并今日两个地区候选池、筛选今日联络对象、生成逐导师特化邮件+附件，绝不发送。** 执行时间 2026-10-10。所有 Gmail 新邮件均是 `DRAFT`，四名不同学校，亚洲优先（包括纽约授学位但后续上海研究的 NYU Shanghai 路线）。所有其它导师保留，无人被删除。

## 今日四位当期材料准备对象

| 顺序 | 学校及地区 | 导师 | 特化研究路径 | Gmail 实际状态 | 素材包 |
|---:|---|---|---|---|---|
| 1 | Singapore / NUS School of Computing | Chengpeng Wang | Agentic program analysis; executable evidence and state-aware repository-agent recovery | **DRAFT_REVIEW_SCHOLARSHIP_EQUIVALENCY** | [材料](singapore/NUS/Chengpeng-Wang/README.md) |
| 2 | Hong Kong / The University of Hong Kong | Chenshu Wu | Software-first AIoT context-aware placement, goal continuity, and recoverable wearable-to-hub execution | **DRAFT_BLOCKED_TRANSCRIPTS_NOT_ATTACHED** | [材料](hong-kong/HKU/Chenshu-Wu/README.md) |
| 3 | United Kingdom / University of Edinburgh | Mahesh Marina | Software-centric mobile edge AI infrastructure and goal-preserving recovery under network outages | **DRAFT_REVIEW_IGS_FULL_APPLICATION_PENDING** | [材料](united-kingdom/Edinburgh/Mahesh-Marina/README.md) |
| 4 | China/United States (cross-border) / NYU Shanghai / NYU Courant | Qiaoyu Tan | Trustworthy and empirical long-horizon tool-using agent evaluation; actual outcomes and false completion | **DRAFT_BLOCKED_TRANSCRIPTS_NOT_ATTACHED** | [材料](crossborder/NYU-Shanghai/Qiaoyu-Tan/README.md) |

**邮件草稿实际存活**：四封均由 Gmail 直接创建并再次读取确认 `DRAFT`，实际附件均为 PDF。没有发送、新增正式大学申请或修改历史已发送邮件。ZIP 离线副本提供全部 **4 份 CV.pdf、4 份 Research-Note.pdf** 与对应 LaTeX 源文件；NYU 的 Research-Note PDF 是候选素材，未附在其 Gmail 草稿，因为该 PI 只明确要求 CV 和 transcripts。

## 当日全池合并：18 位候选一人不丢

- **亚洲/跨境（6）**：HKU Chenshu Wu；NUS Chengpeng Wang；HKUST(GZ) Zhidan Liu；NYU Shanghai Qiaoyu Tan；NTU Rui Tan；CUHK-Shenzhen Jinke Ren。
- **美国常驻（1）**：Columbia Zishen Wan。
- **英国（11，旧两位保留）**：Edinburgh Mahesh Marina / Antonio Barbalace / Paul Patras / Adriana Sejfia；UCL Earl Barr / Mark Harman；Lancaster Nigel Davies / Adrian Friday；Southampton BooJoong Kang；Imperial Jialun Cao；Cambridge Cecilia Mascolo。
- **英国 3 条项目资金路线（不计入 18 人）**：Edinburgh ICSA + IGS（overseas round 2026-11-30）；UCL 2027 UELA（目录预计 2026-10-26，截止 2027-01-08）；Lancaster 2027 CS programme（international funded seat 未证实）。
- **历史已外联六名不重发**：HKUST Mo Li（WANDS 讨论邀请已同意）、Concordia Peter Chen（积极回复，已说明申请情况）、CityUHK Zhenjiang Li、PolyU Yu Liu、CUHK James Cheng、SUTD Ruochen Zhao。UM Li Li 申请已提交并有私人联络；Dartmouth Shawn Shan 和 Penn State Yuchen Yang 均 HOLD。

完整输入而非口头推断：[亚洲及旧全球池](../../../screening/2026-10-10/POOL.yaml) · [英国 11 PI](../../../screening/united-kingdom/2026-10-10/UK-SUPERVISOR-POOL.yaml) · [材料实物审计](../../../screening/2026-10-10/MATERIALS-SECOND-PASS.md)。

## 首轮决策 / 机构互斥

- 选中：**NUS 1、HKU 1、Edinburgh 1、NYU Shanghai 1**，无同校冲突，亚洲 3/4。
- 英国 Edinburgh 其他 3 位 **同校锁 `DEFER_SAME_INSTITUTION`**；UCL Earl Barr/Mark Harman 待 UELA 正式 catalogue，不能假设具体 funded PI；Lancaster 因海外全额奖学金未知，列 `FUNDING_WATCH`。美国 Columbia 学校路线仍 `METHOD_WATCH`；HKUST(GZ) 暂让 Mo Li 已有积极接触优先，不在本轮重复冷套。
- NUS：仅须 CV + short research problems（均已附），但竞争性奖学金和学术等价未批准。
- HKU：邮件标题须严格 `[Prospective Student] Your Name - Your Affiliation`；CV 诚实写自算成绩及未报告 rank；**两个官方 transcript 没有出现在实际 Gmail 附件中，禁止发送**。
- Edinburgh：指导教师必须先讨论、ICSA 海外奖学金需要完整申请；实际 CV 与 research concept 已附，但导师名额与奖学金非既定事实。
- NYU Shanghai：PI 明确要求 CV **和 transcripts**；草稿目前只附 CV，**禁止发送**。NYU Shanghai 的跨境驻地不能伪称长期驻纽约。

## 发送前需要满足的门禁

1. `NO_SEND`：此轮未授权发送，仅创建 Gmail 草稿。四位新对象不得写回 SENT；不能启用自动发送任务。
2. `REAL_DOCUMENTS`：UBC 已寄的 2024-08-28 PDF 缺最终 degree-conferral，Melbourne 正式当前 transcript 未核，派生 CSV 不能冒充 official PDFs；HKU 和 NYU 缺必要附件。
3. `NO_FABRICATION`：UBC 78.05% 属包含重修前 F 的本人按123 attempted credits 加权；Melbourne 67.5/150CP 是 pending 的派生 WAM。无官方 rank、无已确认 peer-reviewed publications，不声称穿戴实机/双服务器切换已验收。
4. `CORE_TRUTH`：DS-Hns / Boss 为已完成冻结前代，Utopia 为已完成冻结的融合后继，Celestial 是未来改造；Utopia head **944f47dd6c7e18b3388b6d769dbbb6dddbe74f00**，Digital-City 当前 main **9efbeeb739a5035774ba34516d5d5b1dce4be8cf**（这仅为指向，具体实验凭已审阅 REX/PCF 报告）。
5. `LIVE_PROTOCOL`：任何未来想发送前须再次检查官网 PI/current opening/2027/邮箱/附件要求、官方学校资金和招生、是否有同校新的正面答复；本次的 Gmail Draft 不自动转 send-ready。
6. 只在单独明确授权后才可以 SEND，不因 2026-10-10 今日池自动排定时任务。

## 材料产物

- 每位包：`README.md`、`EMAIL-DRAFT.md`（Gmail 英文正文原样留档+中文校对摘要）、`CV-SOURCE.md`、`Research-Note.md`、`ATTACHMENTS.md`、`protocol.yaml`。
- 已生成 PDF：所有四位 `CV.pdf` 和 `Research-Note.pdf` 均本地编译检查 A4/1页；真实附件名按 Gmail `CV.pdf` / `Research-Note.pdf`，其字节大小与 SHA-256 记在 manifest。**PDF 二进制未上传公开 GitHub**，用户可从本轮会话生成的 ZIP 或 Gmail 各自草稿取得。
- 写入此处的 `.md` 和 `.yaml` 不触发 `tracking-hist/**/*.tex` 监听的 GitHub Actions CV 构建，避免私有 runner / bill 消耗。
- [机器池决策](../../../screening/2026-10-10/MERGED-OUTREACH-2026-10-10.yaml) · [来源/保留](../../../screening/united-kingdom/2026-10-10/PRESERVATION-AUDIT.md)。
