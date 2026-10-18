# 套磁历史日志

> 这是**已发生对外联络事件**的人工事实记录。自 2026-10-07 起，超过默认生命周期且没有已知实质回复证据的旧线程会自动标 `CLOSED_TIMEOUT` 并释放联系锁；历史发送事实仍然保留。

## 2026-09-18

| 日期 | 学校 | 导师 | 事件 | 状态 | 备注 |
|---|---|---|---|---|---|
| 2026-09-18 | PolyU | Yu Pei | 已发送首封套磁 | **SENT / WAITING** | 发送定制 CV + transcripts；Jing Li 暂停 |
| 2026-09-18 | CityUHK | Heqing Huang | 已发送首封套磁 | **SENT / WAITING** | 发送定制 CV + transcripts；Nan Guan 暂停 |
| 2026-09-18 | CUHK | Yu Li | 已发送首封套磁 | **SENT / WAITING** | 发送定制 CV + transcripts |
| 2026-09-18 | SUTD | Thanh Le-Cong | 已发送首封套磁 | **SENT / WAITING** | 发送定制 CV + transcripts；Ezekiel Soremekun 暂停 |
| 2026-09-18 | University of Macau | Li Li | 已发送 supervisor-match 套磁 | **SENT** | 发送定制 CV；正式申请此前已提交，编号 `YPC711655` |
| 2026-09-18 | University of Macau | Li Li | 对方回复并转入私人联系方式 | **REPLIED / PRIVATE CONTACT / WARM LEAD** | 明确正向 engagement signal；私人联系方式不存入仓库；该线活跃时冻结其他 UM/CIS cold outreach |
| 2026-09-18 | Concordia University | Zhijie Wang | 使用 Melbourne 学生邮箱发送 follow-up | **SENT / WAITING** | 无附件；包含 Boss / DS-Hns 链接；此前已经完成短 Zoom / research discussion |

## 2026-09-22 当时设定的失效 / 二封计划

> 以下日期是当时的计划，不代表之后一定“无回复”。现在如需解锁同校，必须先查真实邮件线程。

| 学校 | 前台导师 | 最后 outbound | 当时的一次失效点 | 当时计划动作 | 终止规则 |
|---|---|---:|---|---|---|
| PolyU | Yu Pei | 2026-09-18 | 2026-09-25 | 无实质回复时只发一次 final follow-up，并同时解锁 PolyU | 再等 5 个工作日仍静默 → `NO_REPLY_FINAL / CLOSED`；不发第三封 |
| CityUHK | Heqing Huang | 2026-09-18 | 2026-09-25 | 同上并解锁 CityUHK | 同上 |
| CUHK | Yu Li | 2026-09-18 | 2026-09-25 | 同上并解锁 CUHK | 同上 |
| SUTD | Thanh Le-Cong | 2026-09-18 | 2026-09-25 | 同上并解锁 SUTD | 同上 |
| Concordia | Zhijie Wang | 2026-09-18 follow-up | 2026-09-25 | 若无回复则标 `DORMANT` 并解锁 Concordia | 该邮件本身已经是 follow-up；不发第三封 |
| University of Macau | Li Li | 2026-09-18 + reply/private channel | 无自动 cold-email 失效 | warm line 活跃时继续冻结 | 明确结束/无名额，或私人渠道追一次后完整 10 个工作日静默才解锁 |

## 统一生命周期规则

- 第一封 cold email = `T0`。
- 第 5 个工作日仍无实质人工回复 → `STALE_NO_REPLY`。
- 只允许一次 second/final follow-up；发送后同校/同系可解锁。
- 二封后再静默 5 个工作日 → `NO_REPLY_FINAL / CLOSED`。
- 明确 decline / no capacity → 立即解锁。
- interested / requested materials / interview / supervision discussion / active private channel → 继续冻结同系新 cold outreach。
- 自动回执和普通 OOO 不算实质回复；OOO 若给返岗日期，从返岗后重新计算。

## 历史 pool

2026-09-22、2026-09-23 的 daily contact pool 是历史快照，不自动顺延。  
当前优先级以根 [README](../README.md) 与 [筛选规则](../rules/SCREENING.md) 为准。

## Gmail 集成说明 — 2026-10-06

- 默认申请邮箱已连接：`zhiheng0mera@gmail.com`。
- 新的导师邮件可以直接在 ChatGPT 内创建 draft、审核后发送，并把 Gmail thread/message ID 写回 `data/outreach.yaml`。
- 旧 2026-09-18 套磁历史仍然有效；当前默认 Gmail 中尚未完成 thread 映射时，标记为 `PENDING`，不能据此推断没有发送或没有回复。
- 邮箱标签采用 `PhD-Application/*` 命名空间。


## 2026-10-06 — Concordia Zhijie Wang 路线关闭

| 日期 | 学校 | 导师 | 事件 | 状态 | 备注 |
|---|---|---|---|---|---|
| 2026-10-06 | Concordia University | Zhijie Wang | 用户确认拒收并关闭该路线 | **DECLINED / DO_NOT_CONTACT / TRASH** | 释放 Concordia 同系联系锁；除非用户明确重开，否则不再联系。已连接的 `zhiheng0mera@gmail.com` 中未找到对应线程；历史 follow-up 来自 Melbourne 学生邮箱，因此无法从当前 Gmail 连接执行实体 Trash。 |


## 2026-10-07 — 旧线程默认超时清除

用户更新策略：旧 cold-outreach 线程超过默认生命周期、且没有已知实质回复 / interview / requested-material / warm-channel 证据时，**默认关闭并释放学校锁**，不再要求先做 final follow-up。

| 学校 | 导师 | 最后 outbound | 新状态 | 结果 |
|---|---|---:|---|---|
| PolyU | Yu Pei | 2026-09-18 | **CLOSED_TIMEOUT** | 释放 PolyU 锁；Yu Liu 可进入新一轮 |
| CityUHK | Heqing Huang | 2026-09-18 | **CLOSED_TIMEOUT** | 释放 CityUHK 锁；Zhenjiang Li / Nan Guan 可进入新一轮 |
| CUHK | Yu Li | 2026-09-18 | **CLOSED_TIMEOUT** | 释放 CUHK 锁；James Cheng 可进入新一轮 |
| SUTD | Thanh Le-Cong | 2026-09-18 | **CLOSED_TIMEOUT** | 释放 SUTD supervisor-outreach 锁；Ruochen Zhao 可进入新一轮 |

“清除”只清当前 `WAITING` / lock 状态，**不删除历史邮件**。UM / Li Li 因已有实质回复 + warm/private channel，不进入自动 timeout-close。


## 2026-10-10 — 对账：六封 10 月 9 日首信实际发送与回复（优先级高于旧“草稿未发”快照）

| 首封日期 | 学校 / 导师 | Gmail 事件 | 2026-10-10 状态 | 跟进约束 |
|---|---|---|---|---|
| 2026-10-09 | HKUST / Mo Li | 首信已发送；导师转 WANDS 团队邀请 Zoom | **REPLIED / INTERVIEW_COORDINATION**，10-10 已同意讨论并请求候选时段 | 等会议排期，**尚未确定具体时间**；禁止重复首信 |
| 2026-10-09 | Concordia / Peter Chen | 首信已发送；导师称研究背景契合并询问申请状态 | **REPLIED / POSITIVE_FIT**，10-10 已回复 | 等导师后续；尚无录取/经费承诺 |
| 2026-10-09 | CityUHK / Zhenjiang Li | 首信及 CV.pdf 已发送 | **SENT_WAITING** | 不重复发 |
| 2026-10-09 | PolyU / Yu Liu | 首信及 CV.pdf 已发送 | **SENT_WAITING** | 不重复发 |
| 2026-10-09 | CUHK / James Cheng | 首信已发送仅 CV.pdf，标题不符合 PI 指定 `phd application` | **SENT_PROTOCOL_QA_RISK** | transcript 缺项，人工决定补救，不自动二次寄出 |
| 2026-10-09 | SUTD / Ruochen Zhao | 首信及 CV.pdf 已发送 | **SENT_WAITING** | 与 Jan 2027 项目级正式申请独立 |

本次是写回真实邮件状态，而不是新发送；先前 [2026-10-9/OUTREACH-SCHEDULE](../tracking-hist/2026-10-9/OUTREACH-SCHEDULE.md) 的未来安排已由实际发送记录取代。完整映射：[2026-10-10 追踪表](../tracking-hist/2026-10-10/README.md)。美英放开后新候选见 [Pool](../screening/2026-10-10/POOL.md)。

## 2026-10-12 — Gmail 四封实发记录（10/14 核验）

| 日期 | 学校 | 导师 | 真实收件人 | Gmail 证据 | 状态 |
|---|---|---|---|---|---|
| 2026-10-12 | NUS | Chengpeng Wang | `wang-chengpeng@nus.edu.sg` | [`1a12d9fa7a7325a8`](https://mail.google.com/mail/u/0/#all/1a12d9fa7a7325a8)，2 PDF | **SENT_WAITING** |
| 2026-10-12 | HKU | Chenshu Wu | `chenshu@cs.hku.hk` | [`1a12d9fa7bff7ec9`](https://mail.google.com/mail/u/0/#all/1a12d9fa7bff7ec9)，4 PDF | **SENT_WAITING** |
| 2026-10-12 | NYU Shanghai | Qiaoyu Tan | `qiaoyu.tan@nyu.edu` | [`1a12d9fa78e64e15`](https://mail.google.com/mail/u/0/#all/1a12d9fa78e64e15)，3 PDF | **SENT_WAITING** |
| 2026-10-12 | Edinburgh | Mahesh Marina | `mahesh@ed.ac.uk` | [`1a12f202de545136`](https://mail.google.com/mail/u/0/#all/1a12f202de545136)，2 PDF | **SENT_WAITING** |

HKU、NYU 的实际邮件已附 UBC 本科和 `Unimelb WAM.pdf`，与 10/10 草稿时不同；这不意味着学校正式认可资格或成绩单。HKU 实发主题与历史 PI 要求的模板不完全一致。四条已核验线程暂无答复，**不自动补发**。

## 2026-10-13 — CUHK James Cheng 无名额回复

| 日期 | 学校 | 导师 | 事件 | 当前状态 | Gmail 证据 |
|---|---|---|---|---|---|
| 2026-10-13 | CUHK | James Cheng | 回复 10/09 首信：**课题组已用尽名额，包括自费 PhD** | **REPLIED_NO_CAPACITY / 当前排除** | [`1a13439fb5be5840`](https://mail.google.com/mail/u/0/#all/1a13439fb5be5840)；thread `1a11f13e3d945d40` |

仅针对 James Cheng 的课题组，不代表 CUHK 整校停止招收，更不是申请人研究能力被否定。原信与研究匹配等历史全部保留。[10/14 完整对账](../tracking-hist/2026-10-14/GMAIL-RECONCILIATION.md)。

## 2026-10-18 — Concordia Peter Chen 用户决定终止等待

| 日期 | 学校 / 导师 | 经 Gmail 核查的真实往来 | 申请管理状态 | 联系锁与后续 |
|---|---|---|---|---|
| 2026-10-18 | Concordia University / Tse-Hsun (Peter) Chen | 10/09首信、10/09教授正面回复并询问加拿大身份、10/10申请人回复国际学生身份；截至10/18当前连接Gmail没有后续人工回复（原线程及搜索双重确认） | **`CLOSED_USER_TIMEOUT / USER_MARKED_UNSUCCESSFUL`**。申请人明确选择按本轮套磁未成功处理、停止等待；**不等于PI明确拒绝，也不等于正式录取被拒** | **`CONCORDIA_UNIVERSITY_LOCK_RELEASED`**；不向Peter再次follow-up，不删除历史邮件，恢复同校其他导师的初次套磁资格，但仍以“同一时间最多1个活跃PI”执行。下一预核第一候选 Bentaleb，其余Lago/Guéhéneuc/Jun Yan/Chun Wang按研究适配候补。 |

- Gmail 记录：[10/09首次回复](https://mail.google.com/mail/u/?authuser=zhiheng0mera%40gmail.com#all/1a120b218e27365d) · [10/10申请人回复](https://mail.google.com/mail/u/?authuser=zhiheng0mera%40gmail.com#all/1a12497a0f1d74bb)。
- 这里的“超时”是**用户主动止损/释放资源决定**，并非系统自动把正面回复线程判定成学术拒绝，也不必达到恰好10个完整日历日。
- 本次只刷新追踪仓库：未发Peter新邮件，未给新Concordia导师建草稿、安排发送或发送。Pitt、UConn、Northeastern既有明日自动任务不变。
