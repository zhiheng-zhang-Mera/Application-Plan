# Screening Schema

## Decision flow

`Hard Gate → Friction → Utility → Action State`

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

## Friction

Track supervisor-first, interview, exam, proposal, outreach, references, fee, and recorded-video availability.

## Utility

Track funding, cost coverage, research fit, coding/systems fit, graduation burden, and location practicality.

## Low-weight lifestyle

`lgbt_trans` and `acg` are tie-breakers only. They must never independently flip a confirmed hard-gate result.

## Machine states

Program action states: `APPLY_NOW | APPLY | BACKUP | WATCH | HOLD | REJECT`

Application states: `not_started | researching | outreach | preparing | submitted | interview | waitlisted | offer | rejected | withdrawn | closed_by_user`

## Freshness

If a mutable fact is stale or inherited from archive, downgrade it to `unknown` until refreshed. Never infer “still true” from silence.

Academic score thresholds are mutable enough to require a current-cycle verification whenever a program is promoted into `ACTIVE`.