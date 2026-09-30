# Screening Schema

## Decision flow

`Hard Gate → Research Method Fit → Public Contact Email Gate → Direct-Contact Channel Gate → Current Recruitment / Capacity → Program-Supervisor Compatibility → Friction → Utility → Action State`

## Hard Gate

Reject when a confirmed rule violates a non-negotiable constraint. Store a reason code and verification date.

Academic eligibility is part of the Hard Gate, not a soft competitiveness score. For every program, capture where available:

- `score_basis`: undergraduate / last-60 / upper-level / master's / honours-classification / unspecified
- `minimum_score`: official wording and scale
- `applicant_score`: only when directly comparable under the university's own rules
- `academic_floor_pass`: `true | false | unknown`
- `score_gate_note`
- `last_verified`

Rules:

- `academic_floor_pass=false` -> `REJECT` with `ACADEMIC_SCORE_BELOW_MINIMUM`.
- If eligibility depends on an unfinished degree or final WAM/classification, set `academic_floor_pass=unknown` and keep the program at `WATCH` at most.
- Do not convert WAM/percentage/GPA across grading systems using an invented linear conversion. Use the target university's published equivalency or leave it unknown.
- Distinguish cumulative, last-60-credit, upper-level, final-two-year, master's, and honours-classification requirements.
- Preferred/competitive averages are risk signals; only explicit eligibility minima are hard gates.

## Research Method Fit

The user is strongest when research is completed through implementation, experiments, benchmarks, simulation, data analysis, or real-task evaluation. The user is not restricted to software engineering: **AI4SE and applied/engineering-oriented AI4Science are both high-fit domains**.

Capture for each supervisor or vacancy:

- `research_domain`: `ai4se | agentic_ai | ai_systems | edge_ai | ubiquitous_computing | wearable_computing | embodied_systems | ai4science | trustworthy_ai | systems | applied_ml | mixed | other`
- `research_method`: `systems | empirical | simulation | applied_ml | data_driven | mixed | theory_heavy | pure_theory | unknown`
- `theory_burden`: `low | medium | high | unknown`
- `domain_theory_burden`: `low | medium | high | unknown`
- `implementation_centrality`: `high | medium | low | unknown`
- `experiment_centrality`: `high | medium | low | unknown`
- `simulation_centrality`: `high | medium | low | unknown`
- `method_mismatch`: `true | false | unknown`
- `style_evidence`: short note based on recent papers, advertised projects, lab/student work, or vacancy description

### High-fit evidence

- AI4SE / LLM-for-SE / coding agents / autonomous software engineering
- testing / debugging / program repair / code review / code search
- empirical SE / repository mining / developer tooling
- AIOps / DevOps / maintenance / self-healing software
- agentic AI / multi-agent systems / agent evaluation / orchestration
- LLM systems / AI infrastructure / distributed AI systems
- edge AI / multi-device AI systems / heterogeneous-device execution
- ubiquitous / wearable computing where software systems, sensing, device coordination and experiments are central
- embodied-enabling systems / agent-device action infrastructure when robotics/control theory is not the primary burden
- trustworthy / secure / reliable agents
- scientific agents / autonomous research
- hypothesis generation / experiment planning / scientific workflow automation
- simulation / surrogate modeling / computational health / biomedical AI
- scientific benchmark / model evaluation / multimodal scientific data analysis

### Medium-fit evidence

- applied ML / trustworthy AI / security engineering
- distributed systems / ML systems
- robotics / autonomous systems when software implementation and experiments are central
- program analysis / formal methods when tooling/testing/empirical evaluation is the main output
- scientific ML with moderate mathematics but implementation/experiments remain central

### Negative evidence

- theorem/proof-centric work
- complexity / algorithms theory
- logic-heavy PL theory
- proof-centric verification
- mathematical optimization/statistical theory where derivation is the central output
- cryptographic / information / learning theory
- AI4Science dominated by advanced theoretical physics, pure mathematics, theoretical chemistry, PDE theory, or domain derivations where software is only auxiliary

Rules:

- Do not reject a mixed supervisor merely because their profile mentions formal methods, verification, optimization, PL, scientific ML, or simulation. Check whether there is a concrete systems/empirical/applied project track.
- **Pure algorithm/theory routes are hard-excluded from outreach.** If the supervisor/vacancy is primarily algorithms theory, theorem/proof work, complexity, proof-centric formal methods, theoretical ML/optimization, or derivation-first research with implementation only auxiliary, delete it from outreach candidate surfaces.
- `pure_theory` -> exclude. `method_mismatch=true` -> exclude. A mixed supervisor survives only when a concrete systems/empirical/applied subtrack is explicitly available and that subtrack is the proposed route.
- `theory_heavy` with a clear implementation/experiment subtrack may remain `BACKUP` or `WATCH`.
- If research method is unclear, keep `method_mismatch=unknown`; do not promote solely on topic-keyword similarity.
- Recent student projects and papers matter more than broad faculty-profile keywords.

## Public Contact Email Gate

A supervisor is **not eligible for any outreach candidate pool** unless a publicly verifiable direct contact email exists.

Capture:

- `public_contact_email`
- `public_contact_email_source_url`
- `public_contact_email_last_verified`
- `public_contact_email_status`: `verified | missing`

Rules:

- verify the email from an official university/faculty page or the supervisor/lab's own public page;
- do not infer, pattern-generate, or guess an address from a university naming convention;
- `missing` -> **delete the person from outreach candidate surfaces immediately**; do not keep them as `WATCH`, `HOLD`, `BACKUP`, a form-only exception, or a daily-pool placeholder;
- a contact form, application portal, LinkedIn account, or private contact channel does **not** substitute for the public-email gate;
- if a public email exists but the advertised position explicitly asks applicants to use a form rather than email, the candidate may remain eligible, but the stored action must follow the advertised form route and the public email is kept only as verified contact identity;
- historical outreach events may remain in the audit log even if the old address is no longer publicly recoverable; the deletion rule applies to **candidate eligibility**, not destruction of historical evidence.

## Direct-Contact Channel Gate

A public email is necessary but **not sufficient**. The advertised PhD/supervisor route must also permit direct outreach.

Capture:

- `contact_channel`: `direct_email_allowed | email_or_form | internal_only | unknown`
- `contact_channel_evidence`
- `contact_channel_source_url`
- `contact_channel_last_verified`

Rules:

- `direct_email_allowed` or `email_or_form` -> eligible, subject to the other gates;
- `internal_only` -> **delete from outreach candidate surfaces immediately**, even if the supervisor has a public email;
- treat a route as `internal_only` when the current recruitment page explicitly says to use only an internal form/portal, explicitly says not to email, or provides no direct-contact application path;
- a normal university application that is required **in addition to** a supervisor who explicitly welcomes direct email is not `internal_only`;
- `unknown` -> verify before promotion; do not place in the current contact pool.

## Current Recruitment / Capacity Gate

A supervisor is not eligible for the **first-contact batch** merely because the research fit is strong. Before outreach, verify a current signal that the person is still taking students or at least accepting supervision inquiries.

Capture:

- `recruitment_status`: `seeking_students | accepting_inquiries | open_phd_position | funding_available | likely_open | unknown | not_accepting`
- `recruitment_scope`: `phd | masters_and_phd | program_specific | unspecified`
- `recruitment_evidence`: exact short description of the current signal
- `recruitment_source_url`
- `recruitment_last_verified`
- `program_supervisor_compatibility`: `confirmed | likely | unknown | incompatible`
- `compatibility_note`: whether the supervisor can supervise the exact target program, not merely another PhD in the same school

Evidence priority:

1. current official faculty profile explicitly saying `Seeking students` / `Accepting inquiries`;
2. current lab/personal page explicitly advertising PhD openings or funding;
3. recent dated post/vacancy explicitly recruiting PhD students;
4. recent supervision activity without an explicit recruitment statement = `likely_open`, not confirmed;
5. old/stale recruitment language = `unknown` until refreshed.

Rules:

- `not_accepting` -> exclude from outreach immediately.
- `unknown` -> research/verify first; do **not** place in the first-contact five.
- `likely_open` -> may remain in the wider pool, but loses to equally matched candidates with explicit current recruitment evidence.
- A generic evergreen statement such as “always interested in hearing from potential students” proves contact openness, **not current-intake PhD capacity**. It cannot promote a supervisor into the daily outreach pool without intake-specific or otherwise current capacity evidence.
- If current sources conflict on capacity, use `recruitment_status=unknown` and exclude from the current outreach pool until resolved.
- For supervisor-match programmes such as Concordia CS/SE PhD, current capacity and exact program compatibility are high-priority execution criteria because an admission offer depends on establishing a supervisor match.
- If a faculty member recruits for a different PhD program only, do not assume they can complete the current application's supervisor match. Mark compatibility `unknown` or `incompatible` until verified.
- Re-verify recruitment status immediately before every outreach batch; do not inherit it indefinitely from an earlier screening round.

## Friction

Track supervisor-first, interview, exam, proposal, outreach, references, fee, and recorded-video availability.

## Utility

Track funding, cost coverage, research/domain fit, coding/systems fit, **AI4SE fit, AI4Science fit, research-method fit, theory burden, domain-theory burden**, graduation burden, and location practicality.

## Low-weight lifestyle

`lgbt_trans` and `acg` are tie-breakers only. They must never independently flip a confirmed hard-gate result.

## Machine states

Program action states: `APPLY_NOW | APPLY | BACKUP | WATCH | PRUNED | HOLD | REJECT`

Application states: `not_started | researching | outreach | preparing | submitted | interview | waitlisted | offer | rejected | withdrawn | closed_by_user`

## Freshness

If a mutable fact is stale or inherited from archive, downgrade it to `unknown` until refreshed. Never infer “still true” from silence.

Academic score thresholds are mutable enough to require a current-cycle verification whenever a program is promoted into `ACTIVE`.

Research-method evidence should also be refreshed when a supervisor is promoted for outreach; use recent papers/projects rather than relying indefinitely on an old faculty bio.

The current portfolio router is `materials/research-profile.md` + `materials/project-positioning.md`. As of 2026-09-30, Utopia adds first-class screening routes for edge / multi-device / ubiquitous / wearable / embodied-enabling systems. Keyword overlap alone is insufficient: an embodied/edge candidate is downgraded when the actual project is theory-, control-, optimization- or game-theory-first.

Supervisor recruitment/capacity is treated as a fast-changing field and must be refreshed for the current outreach date.

Public contact email must also be verified on each promotion into a current outreach pool. A candidate with no verified public email is removed rather than carried forward.