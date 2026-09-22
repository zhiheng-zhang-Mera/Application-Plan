# Contact Pool — 2026-09-22

> **Full refresh.** This pool does not inherit ordering from the 2026-09-17 / 2026-09-18 pool.
>
> **Hard exclusion for this refresh:** any supervisor already contacted, and the whole university/department currently occupied by that contact. Therefore **Concordia, SUTD, PolyU, CityUHK, CUHK, and University of Macau are excluded from today's new-contact pool**.
>
> Evidence below was refreshed on **2026-09-22**. Before an actual send, re-open the recruitment page once; do not send if the signal has changed.
>
> **Hard gates:** every supervisor must have a publicly verifiable direct email, the current route must explicitly permit direct outreach, and the proposed research route must not be pure algorithms/theory. Missing email, internal-only/form-only routing, or pure-theory fit = delete the candidate rather than carrying them as WATCH/HOLD/BACKUP.
>
> **Daily-pack rule:** every pool refresh must also regenerate `applications/OUTREACH-PACK-YYYY-MM-DD.md` with an individualized body/form response and a material package for every selected candidate. A row may not be `READY` if the body/package is missing.

## Today's fresh five

| Priority | University | Supervisor / lab | Contact action | Generated body + material package | Current signal | State |
|---:|---|---|---|---|---|---|
| 1 | University of Alberta | **Jocelyn Qiaochu Chen** | Email `jocelyn.chen@ualberta.ca`; subject contains **Prospective Student** | [正文 + package](../applications/OUTREACH-PACK-2026-09-22.md#1-jocelyn-qiaochu-chen--university-of-alberta) · [CV source](../CV-generate/ualberta-jocelyn-chen.tex) · [transcript](../Documents/Transcript-ZhihengZhang.pdf) | Recruiting **1–2 fully funded PhD students in the upcoming cycle** | **BODY_READY / CV_PDF_PENDING** |
| 2 | University of Hong Kong | **Ka Ho Chow** | Email `kachow@cs.hku.hk` | [正文 + package](../applications/OUTREACH-PACK-2026-09-22.md#2-ka-ho-chow--university-of-hong-kong) · [CV source](../CV-generate/hku-ka-ho-chow.tex) · [transcript](../Documents/Transcript-ZhihengZhang.pdf) | Official profile says **several openings for PhD students** | **BODY_READY / CV_PDF_PENDING** |
| 3 | Simon Fraser University | **Keval Vora** | Email `keval@sfu.ca`; brief interests + CV | [正文 + package](../applications/OUTREACH-PACK-2026-09-22.md#3-keval-vora--simon-fraser-university) · [CV source](../CV-generate/sfu-keval-vora.tex) · transcript only if requested | Current page says **Open Positions** and asks prospective grads to contact him with interests + CV | **BODY_READY / CV_PDF_PENDING** |
| 4 | KAUST | **Marco Canini** | Email `marco@kaust.edu.sa`; read his PhD-contact instructions before sending | [正文 + package](../applications/OUTREACH-PACK-2026-09-22.md#4-marco-canini--kaust) · [CV source](../CV-generate/kaust-marco-canini.tex) · [transcript](../Documents/Transcript-ZhihengZhang.pdf) | SANDS page explicitly addresses prospective PhD students; distributed/cloud + AI/ML systems fit | **BODY_READY / CV_PDF_PENDING** |
| 5 | CUHK-Shenzhen — School of Artificial Intelligence | **Xiaoxue Gao** | Email `gaoxiaoxue@cuhk.edu.cn`; professor explicitly asks interested PhD applicants to email CV + target position/intake | [正文 + package](../applications/OUTREACH-PACK-2026-09-22.md#5-xiaoxue-gao--cuhk-shenzhen) · [CV source](../CV-generate/cuhksz-xiaoxue-gao.tex) · [transcript](../Documents/Transcript-ZhihengZhang.pdf) | **Fully funded Spring/Fall 2027 PhD**; agentic AI in speech/audio, multimodal LMs, trustworthy AI; direct outreach allowed | **BODY_READY / CV_PDF_PENDING** |

## Why these five

- All five are from universities **not occupied by the 2026-09-18 contact batch**.
- Every slot has a **current recruitment/contact signal**, not just historical faculty-fit keywords.
- The pool deliberately mixes exact AI4SE/reliable-code work with systems/orchestration work so Boss and DS-Hns can be presented as research artifacts without pretending they are already finished research results.
- SANAD was removed from the pool because the advertised Fall 2027 route explicitly requires the internal interest system rather than direct outreach; public faculty emails do not override the direct-contact gate.
- Xiaoxue Gao replaces that slot because she explicitly recruits fully funded Spring/Fall 2027 PhD students and explicitly asks interested applicants to email her. The selected narrative is **agentic AI + trustworthy multimodal systems + empirical evaluation**; speech/audio is treated as the application domain, not as a requirement to pretend prior specialist experience.
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
- Xiaoxue Gao personal recruitment page: https://xiaoxue1117.github.io/
- CUHK-Shenzhen SAI MPhil-PhD requirements: https://sai.cuhk.edu.cn/en/node/35
