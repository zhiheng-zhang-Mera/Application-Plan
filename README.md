# PhD Application Control Center — 2027

> **Lazy dashboard — updated 2026-10-06.** If you only read one file, read this one.  
> Detailed history, old contact batches and dated screening snapshots stay elsewhere; this page only shows **what matters now**.

## Current application story

**Primary direction:** **Utopia → Personal Compute Fabric / ubiquitous agentic computing**

Default PhD framing:

**Ubiquitous / Personal Computing + AI Systems + Distributed / Edge Systems**

- **Utopia** = primary platform evidence and future research substrate.
- **PCF — Personal Compute Fabric / Heterogeneous Edge Runtime** = next research-facing expansion; **planned, not claimed complete**.
- **DS-Hns** = long-horizon execution / recovery / AI4SE evidence.
- **Codex Boss** = governance / verification / multi-agent evidence.
- Wearable glasses, health terminals, entertainment rooms, etc. = **verticals**, not the default PhD identity.
- Privacy Lens / Quant-Ultra = supporting routes when the target genuinely matches them.

Rules: [Screening & Priority](rules/SCREENING.md) · [Application Execution](rules/EXECUTION.md)

---

## NOW — spend time here

| Priority | Target | State | Next action |
|---|---|---|---|
| **P0** | **University of Macau — Li Li** | **SUBMITTED / WARM** | Continue the private/warm line. Do **not** open parallel UM/CIS cold outreach while it remains active. |
| **P0** | **SUTD PhD — Jan 2027** | **APPLY_NOW** | Formal application first. **Deadline: 2026-10-30.** Reconcile the existing Thanh Le-Cong thread before another same-school contact; Ruochen Zhao is the strongest fresh Utopia/agent route. |
| **P0** | **CUHK CSE — James Cheng** | **APPLY / strong Utopia-Boss fit** | Reconcile the existing Yu Li thread, then refresh James Cheng's Aug-2027 recruitment page and build a new package. |
| **P0** | **CUHK-Shenzhen — Jinke Ren** | **ACTIVE** | Verify exact 2027 program/supervisor compatibility, then generate a Utopia-first package. |
| **P1** | **NYU — Qiaoyu Tan / Dartmouth — Shawn Shan / Penn State — Yuchen Yang** | **OUTREACH_READY** | Re-open the current recruitment pages, refresh claims/CV to the new Utopia-aware profile, then enter the send queue. |
| **P1** | **UBC / SFU** | **APPLY** | Keep formal applications alive. UBC = high competition; SFU/Keval Vora = strong scalable-systems route. |
| **P1** | **Concordia** | **ACTIVE / FLOOR** | Reconcile the old Zhijie lifecycle first; then keep only one clean supervisor thread active. Concordia is the minimum acceptable floor, not the center of the pool. |

### One cleanup item before new cold outreach

The 2026-09-18 contact batch has follow-up/lock dates that are already past.  
Before opening another same-school thread, reconcile the actual contact history in:

- [applications/OUTREACH-LOG.md](applications/OUTREACH-LOG.md)
- application-specific `CONTACTS.md` / `TIMELINE.md`
- mailbox evidence when needed

Do not infer “no reply” merely because an old table was not updated.

---

## VERIFY NEXT — high value, not ready to send

| Target | Why it matters | Blocking check |
|---|---|---|
| **KAIST — Junehwa Song** | Excellent Utopia → mobile / IoT / wearable / ubiquitous / distributed route | Fall-2027 dates + current PhD capacity |
| **HKUST(GZ) — Information Hub / IoT** | Very strong PCF / edge / ubiquitous direction | Find a systems/edge PI with lower theory burden + verify current admission/funding |
| **KAUST — Marco Canini route** | Strong distributed / ML-systems fit and funding | Reconcile conflicting capacity evidence before outreach |
| **HKU** | Strong trustworthy / systems candidates | Clear honours / academic-equivalency gate |
| **HKUST CSE** | Strong school-level systems / SE / security fit | Fresh 2027 PI capacity; old shortlist is stale |
| **Alberta / Manitoba** | Strong AI4SE alternatives | Refresh 2027 capacity + funding |

---

## DO NOT SPEND TIME NOW

| Target | Reason |
|---|---|
| Waterloo | confirmed academic hard floor |
| Queen's | confirmed academic hard floor |
| Dalhousie | confirmed academic hard floor |
| UNIST | mandatory English test conflicts with no-retest rule |
| SMU | GRE/GMAT hard gate |
| TU Delft WALTZ | vacancy deadline passed |
| pure-theory / proof-first / game-theory-first routes | research-method mismatch |

NUS and MBZUAI remain **BACKUP**, not rejects: research can fit, but known QE/screening/equivalency friction makes them lower ROI.

---

## Critical deadlines

| Item | Date | Status |
|---|---:|---|
| **SUTD Jan-2027 PhD** | **2026-10-30** | **ACTIVE — do not wait for supervisor replies before progressing the formal application** |

Other deadlines must be refreshed from the current official program page before a package is promoted to submission-ready.

---

## Materials — quick health check

### Ready / structured

- [x] UBC official transcript — `Documents/Transcript-ZhihengZhang.pdf`
- [x] Bachelor structured scores — `Documents/Bachelor Score.csv`
- [x] Melbourne progress/WAM source image — `Documents/Master-WAM.png`
- [x] Master structured scores — `Documents/Master Score.csv`
- [x] Tailored-CV build workflow — `.github/workflows/build-cv-pdfs.yml`
- [x] Referee knowledge-boundary packs — `materials/referees/`
- [x] Current research profile — `materials/research-profile.md`
- [x] Project-positioning router — `materials/project-positioning.md`

### Still worth completing

- [ ] UBC degree certificate / completion evidence
- [ ] latest official Melbourne transcript when available
- [ ] final Melbourne transcript / completion evidence when available
- [ ] English-medium instruction evidence where a school asks for it
- [ ] reusable current SOP / research-statement mother versions
- [ ] application-package QA / validator returned to the live pipeline

Full material index: [materials/MATERIALS.md](materials/MATERIALS.md)

---

## Where details live

| Need | Open |
|---|---|
| **Who should be targeted and why?** | [rules/SCREENING.md](rules/SCREENING.md) |
| **How do outreach, packages, QA and submission work?** | [rules/EXECUTION.md](rules/EXECUTION.md) |
| Current active schools | [targets/ACTIVE.md](targets/ACTIVE.md) |
| High-value unresolved gates | [targets/WATCHLIST.md](targets/WATCHLIST.md) |
| Lower-ROI viable routes | [targets/BACKUP.md](targets/BACKUP.md) |
| Hard removals | [targets/REJECTED.md](targets/REJECTED.md) |
| Current broad pool snapshot | [targets/POOL-REFRESH-2026-09-30.md](targets/POOL-REFRESH-2026-09-30.md) |
| Contact history | [applications/OUTREACH-LOG.md](applications/OUTREACH-LOG.md) |
| Machine-readable program state | `data/programs.yaml` / `data/applications.yaml` / `data/supervisors.yaml` |

---

## Lazy operating mode

For normal use, the intended commands are effectively:

- **“刷新申请池”** → re-check gates, 2027 recruitment, funding and current priorities.
- **“今天该做什么”** → return only P0/P1 actions and deadlines.
- **“给 X 学校生成申请包”** → generate target-specific materials, then QA.
- **“检查套磁状态”** → reconcile actual contact history before unlocking another PI.
- **“检查材料缺口”** → only show blockers that can affect a live application.
- **“检查申请状态”** → submitted / waiting / interview / offer / closed.

Everything else should stay behind the dashboard unless it is needed for a decision.
