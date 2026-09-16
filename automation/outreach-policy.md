# Outreach Policy

## Required

Use targeted outreach when supervisor commitment is a formal or practical prerequisite to admission/offer.

## Recommended

Use outreach when one strong supervisor signal can materially improve admission value or clarify funding, but do not block the application while waiting unless the program requires it.

## Low ROI

For department-admission programs, prefer strong faculty-fit prose in SOP over mass cold-emailing.

## Candidate-state precedence

Before generating or sending any outreach, resolve the human-control state in this order:

`REJECTED > PRUNED > BACKUP > WATCH > ACTIVE`

- `REJECTED`: never contact unless the documented hard-gate reopening condition is met.
- `PRUNED`: never auto-contact. A stale record in `data/programs.yaml`, a dated staging file, or `data/supervisors*.yaml` does **not** override PRUNED.
- `BACKUP`: contact only when the user explicitly activates that programme/current run.
- `WATCH`: research/verify only; do not send mail until the blocking gate is cleared and state is promoted.
- `ACTIVE`: eligible for outreach subject to the rules below.

## Research-style gate

The user is implementation-first and not strong in pure-theory research. Before a supervisor enters an outreach batch, require:

- `research_style`: prefer `systems | empirical | applied_ml`; allow `mixed` only when the proposed project is implementation/experiment-led.
- `implementation_centrality`: medium/high preferred.
- `experiment_centrality`: medium/high preferred.
- theorem/proof/semantics/complexity-heavy work must not be selected merely because keywords overlap with agents, verification, PL, or AI.
- formal methods is acceptable when the actual project centers on tooling, testing, verification systems, coding-agent evaluation, or empirical software reliability.

If research style is unknown, inspect recent papers/projects before outreach. Do not guess from a faculty bio keyword list.

## Automation rules

- Never mass-email every faculty member in a department.
- Never send to a supervisor whose programme is PRUNED/REJECTED, even if they remain in historical/staging YAML.
- Stop repeated follow-ups after clear non-response unless new evidence changes the case.
- Use the program's `narrative_route` to select Boss / DS-Hns / Quant-Ultra / Privacy Lens evidence.
- Log every sent message and reply state in structured application/supervisor data.
- Do not claim prior contact, interest, funding, or supervision unless it is recorded as evidence.
- If candidate-state sources conflict, the stricter human-control file under `targets/` wins until data is reconciled.
