# Screening Schema

## Decision flow

`Hard Gate → Research Method Fit → Friction → Utility → Action State`

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

- `research_domain`: `ai4se | agentic_ai | ai_systems | ai4science | trustworthy_ai | systems | applied_ml | mixed | other`
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
- `pure_theory` or `method_mismatch=true` normally means `PRUNED` or `REJECT`, unless an explicit applied/systems project is available.
- `theory_heavy` with a clear implementation/experiment subtrack may remain `BACKUP` or `WATCH`.
- If research method is unclear, keep `method_mismatch=unknown`; do not promote solely on topic-keyword similarity.
- Recent student projects and papers matter more than broad faculty-profile keywords.

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
