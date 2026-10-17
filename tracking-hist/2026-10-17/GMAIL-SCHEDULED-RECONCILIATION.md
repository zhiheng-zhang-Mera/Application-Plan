# 2026-10-17 Gmail 五封已安排发送邮件实证核对

> 查验时间：2026-10-17（Melbourne）。连接 Gmail 执行 `in:scheduled`、`in:sent after:2026/10/14`、`list_drafts` 与实际 `batch_read_email`。**事实从 2026-10-16 DRAFT 跃迁为 2026-10-17 已安排发送。** 该定时操作已由用户/邮箱端完成，本次 ChatGPT **没有创建/修改/发送任何邮件**。

| 学校 | PI | Gmail Scheduled message ID | 安排发送（Melbourne AEDT） | 目标大学当地时刻 | 已核附件 |
|---|---|---|---|---|---:|
| POSTECH | Inseok Hwang | `1a151ac2acbe5d7e` | **2026-10-19 12:00** | Mon 10/19 10:00 KST | 2 |
| KAIST | Ian Oakley | `1a151ac2a152f4ae` | **2026-10-19 12:00** | Mon 10/19 10:00 KST | 4 |
| SUSTech | 李雪亮 | `1a151ac2b6924861` | **2026-10-19 12:00** | Mon 10/19 09:00 CST | 2 |
| ShanghaiTech | 李权 | `1a151ac2af8ccf6c` | **2026-10-19 12:00** | Mon 10/19 09:00 CST | 2 |
| HKBU | Henry Dai | `1a156d286d5cc43f` | **2026-10-20 12:00** | Tue 10/20 09:00 HKT | 4 |

说明：
- `in:scheduled` 确认上述**恰好5封**；`list_drafts(max_results=100)` 返回空；与 10/16 旧 `DRAFT` ID 不一致是 Gmail 定时安排产生的新 message ID。
- `in:sent after:2026/10/14` 仅找到 2026-10-16 HKUST WANDS 感谢邮件，不包括这5封。因此它们**尚未发出**，既不是草稿也不能标 `SENT_WAITING`。
- Gmail scheduled messages 逐条展开确有附件：POSTECH CV+Research Note；KAIST CV+Cover Letter+UBC本科成绩单+Melbourne现有WAM；南科大/上科大各 CV+Research Note；HKBU CV+Research Note+UBC本科成绩单+Melbourne现有WAM。
- 没有创建发送任务（包括 ChatGPT 自动化），没有改动用户 Gmail 的已安排发送；继续用户指定的**整校1位联系人锁**，防止定时发送后又冷投同校候补。
- 连接 Gmail 原有 10/09–12 实发、HKUST WANDS 10/15 面谈、10/16 感谢信、Concordia Peter Chen 10/09 积极回复、UM warm/历史已提交状态依旧，历史不可回退。
- 当前真实收件与发送时间为 Gmail 可检索值，**之后若用户在 Gmail 调整或取消，需再次以邮箱为准**。
