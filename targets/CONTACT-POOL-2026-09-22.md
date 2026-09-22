# Contact Pool — 2026-09-22

> **Full refresh.** This pool does not inherit ordering from the 2026-09-17 / 2026-09-18 pool.
>
> **Hard exclusion for this refresh:** any supervisor already contacted, and the whole university/department currently occupied by that contact. Therefore **Concordia, SUTD, PolyU, CityUHK, CUHK, and University of Macau are excluded from today's new-contact pool**.
>
> Evidence below was refreshed on **2026-09-22**. Before an actual send, re-open the recruitment page once; do not send if the signal has changed.

## Today's fresh five

| Priority | University | Supervisor / lab | Contact action | Current signal | Best narrative | State |
|---:|---|---|---|---|---|---|
| 1 | University of Alberta | **Jocelyn Qiaochu Chen** | Email `jocelyn.chen@ualberta.ca`; subject must include **Prospective Student** | Recruiting **1–2 fully funded PhD students in the upcoming cycle**; AI-assisted programming, program synthesis, formal methods, LLM/program abstractions | **DS-Hns + Codex Boss**: reliable coding agents, acceptance/verification, reproducible software-agent evaluation | **READY — fresh 2026-09-22** |
| 2 | University of Hong Kong | **Ka Ho Chow** | Email `kachow@cs.hku.hk` | Official profile says **several openings for PhD students**; trustworthy AI, cybersecurity, ML/systems, LLM security | **Boss + DS-Hns + Privacy Lens**: permission/security boundaries, trustworthy autonomous systems | **READY — fresh 2026-09-22** |
| 3 | Simon Fraser University | **Keval Vora** | Email `keval@sfu.ca`; send brief research-interest description + CV | Current page says **Open Positions** and multiple research-team opportunities; asks prospective grads to contact him with interests + CV | **DS-Hns + Boss**: scalable runtime/orchestration, long-running systems, performance/reliability | **READY — fresh 2026-09-22** |
| 4 | KAUST | **Marco Canini** | Email `marco@kaust.edu.sa`; read his PhD-contact instructions before sending | SANDS page says he is **always looking** for people to join the group and explicitly addresses prospective PhD students; focus is distributed/cloud systems and systems support for AI/ML | **DS-Hns + Boss**: distributed execution, AI/ML systems infrastructure, fault-tolerant orchestration | **READY — fresh 2026-09-22** |
| 5 | NYU Abu Dhabi — SANAD Lab | **Sarah Nadi / Karim Ali** | **Use the SANAD internal interest form; do not cold-email**. Formal NYU application is still separately required | Recruiting **fully funded Fall 2027 PhD** students; AI for SE, correctness of LLM-generated code, program analysis/security; deadline **2026-12-12** | **DS-Hns + Boss**: AI4SE, code correctness, software-agent benchmarking and reproducibility | **READY — FORM ACTION** |

## Why these five

- All five are from universities **not occupied by the 2026-09-18 contact batch**.
- Every slot has a **current recruitment/contact signal**, not just historical faculty-fit keywords.
- The pool deliberately mixes exact AI4SE/reliable-code work with systems/orchestration work so Boss and DS-Hns can be presented as research artifacts without pretending they are already finished research results.
- NYUAD is intentionally a form action rather than an email: the lab explicitly asks candidates to indicate interest through its internal system instead of emailing.
- University of Alberta is worth contacting now, but Jocelyn Chen's page says the direct PhD route assumes prior research training; if the current master's is not treated as research-based, her stated route is the funded research MSc first. Do not hide this in the outreach.
- KAUST Fall 2027 applications open **2026-09-28**; supervisor contact is optional at university level, so the Marco Canini email is a targeted fit signal rather than an admission prerequisite.

## Explicitly not reused today

The previous hold queue is retired for today's batch:

- Tse-Hsun (Peter) Chen / Concordia
- Ezekiel Soremekun / SUTD
- Nan Guan / CityUHK
- Xiaobo Zhou / University of Macau
- Jing Li / PolyU

They are **not rejected**. They remain behind their live school relationship and may become eligible only through the unlock state machine below.

## Contact invalidation / school unlock state machine

### Cold first contact

- **T0 = first email sent.**
- Count receiver-local **business days**, excluding Saturday/Sunday.
- If there is **no substantive human reply by 10:00 receiver-local time on business day 5**, the first contact becomes `STALE_NO_REPLY`.
- At that trigger, perform both actions together:
  1. send **one** concise second/final follow-up to the same supervisor; and
  2. set the university/department to **UNLOCKED**, allowing the next supervisor to enter the queue immediately.
- State becomes `FOLLOWUP_SENT / SCHOOL_UNLOCKED`.
- If the follow-up also receives no substantive reply after another **5 business days**, mark `NO_REPLY_FINAL / CLOSED`. **No third email.**

### Immediate outcomes

- Explicit `DECLINED` / `NO_CAPACITY`: unlock the school immediately; do **not** send the second follow-up unless the reply itself invites it.
- `INTERESTED`, `REQUESTED_MATERIALS`, `INTERVIEW`, `SUPERVISION_DISCUSSION`, or migration to an active private channel: keep the school **FROZEN**.
- Auto-replies, delivery receipts and generic out-of-office messages are not substantive replies. If an out-of-office message gives a return date, move the five-business-day trigger to begin after that return date rather than treating the contact as failed.

### Existing 2026-09-18 batch

- Yu Pei / PolyU, Heqing Huang / CityUHK, Yu Li / CUHK, Thanh Le-Cong / SUTD: if still silent, **2026-09-25** is the business-day-5 trigger → second/final follow-up + simultaneous school unlock.
- Zhijie Wang / Concordia: the 2026-09-18 message was already a follow-up on an existing relationship. If still silent on **2026-09-25**, mark the line `DORMANT` and unlock Concordia; **do not send a third message**.
- Li Li / University of Macau: active warm/private-channel lead, so the ordinary cold-contact timer does not apply. Unlock only after an explicit end/no-capacity signal, or after one private-channel follow-up followed by **10 full business days** of silence.

## Evidence refreshed 2026-09-22

- Jocelyn Qiaochu Chen: https://sites.ualberta.ca/~qiaochu8/
- University of Alberta admissions: https://www.ualberta.ca/en/computing-science/graduate-studies/programs-and-admissions/applications-and-admissions/index.html
- Ka Ho Chow: https://www.cs.hku.hk/people/academic-staff/kachow
- Keval Vora: https://www.cs.sfu.ca/~keval/
- SFU Computing Science PhD: https://www.sfu.ca/fas/study/future-graduates/programs/phd-computing/
- Marco Canini / SANDS: https://sands.kaust.edu.sa/
- KAUST 2026–27 admissions timeline: https://admissions.kaust.edu.sa/how-to-apply/admission-timelines
- KAUST entry requirements: https://admissions.kaust.edu.sa/how-to-apply/entry-requirements
- SANAD Fall 2027 PhD: https://sanadlab.org/positions/phd/
