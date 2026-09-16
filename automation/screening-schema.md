# Screening Schema

## Decision flow

`Hard Gate → Research Style Fit → Friction → Utility → Action State`

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

## Research Style Fit

The user is implementation/engineering-oriented and is not a good fit for pure-theory PhD work. Evaluate this before generic research-fit scoring.

Capture for each supervisor or vacancy:

- `research_style`: `systems | empirical | applied_ml | mixed | theory_heavy | pure_theory | unknown`
- `theory_burden`: `low | medium | high | unknown`
- `implementation_centrality`: `high | medium | low | unknown`
- `experiment_centrality`: `high | medium | low | unknown`
- `theory_mismatch`: `true | false | unknown`
- `style_evidence`: short note based on recent papers, advertised projects, lab/student work, or vacancy description

Default preference:

`systems / empirical / applied_ml > mixed > theory_heavy > pure_theory`

Positive evidence includes software/system building, agent implementation, benchmarks, experiments, testing, program repair, developer tooling, infrastructure, empirical SE, security engineering, applied trustworthy AI, and performance/reliability evaluation.

Negative evidence includes theorem/proof-centric work, complexity or algorithms theory, logic-heavy PL theory, proof-centric verification, mathematical optimization theory, cryptographic theory, information theory, or learning theory when these are the central research outputs.

Rules:

- Do not reject a mixed supervisor merely because their profile mentions formal methods, verification, optimization, or PL. Check whether there is a concrete systems/empirical track.
- `pure_theory` or `theory_mismatch=true` normally means `BACKUP` or `REJECT`, unless an explicit applied/systems project is available.
- If research style is unclear, keep `theory_mismatch=unknown`; do not promote solely on topic-keyword similarity.
- Recent student projects and papers matter more than broad faculty-profile keywords.

## Friction

Track supervisor-first, interview, exam, proposal, outreach, references, fee, and recorded-video availability.

## Utility

Track funding, cost coverage, research fit, coding/systems fit, **research-style fit / theory burden**, graduation burden, and location practicality.

## Low-weight lifestyle

`lgbt_trans` and `acg` are tie-breakers only. They must never independently flip a confirmed hard-gate result.

## Machine states

Program action states: `APPLY_NOW | APPLY | BACKUP | WATCH | HOLD | REJECT`

Application states: `not_started | researching | outreach | preparing | submitted | interview | waitlisted | offer | rejected | withdrawn | closed_by_user`

## Freshness

If a mutable fact is stale or inherited from archive, downgrade it to `unknown` until refreshed. Never infer “still true” from silence.

Academic score thresholds are mutable enough to require a current-cycle verification whenever a program is promoted into `ACTIVE`.

Research-style evidence should also be refreshed when a supervisor is promoted for outreach; use recent papers/projects rather than relying indefinitely on an old faculty bio.