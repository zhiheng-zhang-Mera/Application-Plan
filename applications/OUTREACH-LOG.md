# Outreach Tracking Log

> Manual source of truth for outbound supervisor contact events. Keep this synchronized with the README control center.

## 2026-09-18

| Date | University | Supervisor | Event | State | Notes |
|---|---|---|---|---|---|
| 2026-09-18 | PolyU | Yu Pei | First outreach sent | **SENT / WAITING** | Tailored CV + transcripts sent; wait before unlocking Jing Li |
| 2026-09-18 | CityUHK | Heqing Huang | First outreach sent | **SENT / WAITING** | Tailored CV + transcripts sent; Nan Guan remains on hold |
| 2026-09-18 | CUHK | Yu Li | First outreach sent | **SENT / WAITING** | Tailored CV + transcripts sent |
| 2026-09-18 | SUTD | Thanh Le-Cong | First outreach sent | **SENT / WAITING** | Tailored CV + transcripts sent; Ezekiel Soremekun remains on hold |
| 2026-09-18 | University of Macau | Li Li | Supervisor-match outreach sent | **SENT** | Tailored CV sent; application already submitted under `YPC711655` |
| 2026-09-18 | University of Macau | Li Li | Replied and moved discussion to private contact channel | **REPLIED / PRIVATE CONTACT / WARM LEAD** | Positive engagement signal; private contact detail intentionally not stored; freeze Xiaobo Zhou and other UM/CIS cold outreach while active |
| 2026-09-18 | Concordia University | Zhijie Wang | Follow-up sent from University of Melbourne student email | **SENT / WAITING** | No attachment; Boss and DS-Hns links included; prior interview/discussion already completed |

## 2026-09-22 — Invalidation / second-contact schedule

| University | Foreground supervisor | Last outbound | First-line invalidation | Trigger action | Terminal rule |
|---|---|---:|---|---|---|
| PolyU | Yu Pei | 2026-09-18 | **2026-09-25** if no substantive reply | Send one second/final follow-up **and unlock PolyU simultaneously** | 5 more business days silent → `NO_REPLY_FINAL / CLOSED`; no third email |
| CityUHK | Heqing Huang | 2026-09-18 | **2026-09-25** if no substantive reply | Send one second/final follow-up **and unlock CityUHK simultaneously** | 5 more business days silent → `NO_REPLY_FINAL / CLOSED`; no third email |
| CUHK | Yu Li | 2026-09-18 | **2026-09-25** if no substantive reply | Send one second/final follow-up **and unlock CUHK simultaneously** | 5 more business days silent → `NO_REPLY_FINAL / CLOSED`; no third email |
| SUTD | Thanh Le-Cong | 2026-09-18 | **2026-09-25** if no substantive reply | Send one second/final follow-up **and unlock SUTD simultaneously** | 5 more business days silent → `NO_REPLY_FINAL / CLOSED`; no third email |
| Concordia | Zhijie Wang | 2026-09-18 follow-up | **2026-09-25** if no reply | Mark `DORMANT` and unlock Concordia | This message was already a follow-up; **no third email** |
| University of Macau | Li Li | 2026-09-18 + reply/private channel | **No automatic cold-email expiry** | Keep frozen while warm line is active | Unlock on explicit end/no-capacity, or after one private-channel follow-up + 10 full business days of silence |

### Deterministic lifecycle rule

- First cold email = `T0`.
- At **10:00 receiver-local time on business day 5**, if there is no substantive human reply, set `STALE_NO_REPLY`.
- On the same trigger: send exactly one second/final follow-up and set the same university/department to `UNLOCKED`.
- A new same-school supervisor becomes eligible immediately after that unlock; the old silent thread can continue waiting in parallel.
- After the second email, 5 additional business days of silence → `NO_REPLY_FINAL / CLOSED`; never send a third email.
- Explicit decline/no-capacity unlocks immediately. Interest, requested materials, interview, supervision discussion, or an active private channel keeps the school frozen.
- Delivery receipts and generic auto-replies do not count. If an OOO specifies a return date, defer the timer accordingly.

## 2026-09-22 — Fresh pool selection

The prior hold queue is **not** reused as today's queue. The new pool is recorded in `targets/CONTACT-POOL-2026-09-22.md`.

Excluded because a 2026-09-18 relationship still occupies the school lock: **Concordia, SUTD, PolyU, CityUHK, CUHK, University of Macau**.

Fresh schools/actions: **University of Alberta / Jocelyn Qiaochu Chen; HKU / Ka Ho Chow; SFU / Keval Vora; KAUST / Marco Canini; NYU Abu Dhabi SANAD / Sarah Nadi & Karim Ali internal interest form.**
