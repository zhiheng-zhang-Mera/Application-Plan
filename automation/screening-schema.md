# Screening Schema

## Decision flow

`Hard Gate → Friction → Utility → Action State`

## Hard Gate

Reject when a confirmed rule violates a non-negotiable constraint. Store a reason code and verification date.

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