# Outreach Policy

## Required

Use targeted outreach when supervisor commitment is a formal or practical prerequisite to admission/offer.

## Recommended

Use outreach when one strong supervisor signal can materially improve admission value or clarify funding, but do not block the application while waiting unless the program requires it.

## Low ROI

For department-admission programs, prefer strong faculty-fit prose in SOP over mass cold-emailing.

## Human manual-operation surface

The repository root `README.md` is the **human manual-outreach control center and contact ledger**.

It should let the user quickly:

1. see the current manual send queue;
2. copy a supervisor email address;
3. open the exact individualized email draft;
4. open the relevant attachment/supporting-material checklist;
5. manually send the message from the user's email client; and
6. record the resulting contact history (`last_contact`, contact count/history, reply state, next action/cooldown).

`data/*.yaml` remains the machine-oriented candidate/program source, but stale structured data must **not** overwrite a newer human contact-history entry in the root README or the relevant `applications/*/CONTACTS.md` / `TIMELINE.md`.

For the question **"has this supervisor already been contacted / what happened?"**, use this precedence:

`README manual ledger -> applications/* contact/timeline records -> structured data -> old staging/search notes`.

Do not fabricate an exact date or contact count when the historical record only supports a qualitative statement such as "existing thread", "interviewed", or "multiple unanswered follow-ups".

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

## Current recruitment and program-compatibility gate

Before a supervisor enters the **first-contact queue**, verify both:

1. a current signal that the supervisor is seeking students, accepting supervision inquiries, advertising a PhD opening, or explicitly stating PhD funding/capacity; and
2. compatibility with the exact target program, especially when a school has multiple PhD programs with separate supervisor lists.

Store `recruitment_status`, `recruitment_evidence`, `recruitment_source_url`, `recruitment_last_verified`, `program_supervisor_compatibility`, and `compatibility_note`.

Rules:

- `not_accepting` -> never contact in the current round.
- `unknown` -> verify first; do not include in the first-contact five.
- recent explicit `seeking_students`, `accepting_inquiries`, `open_phd_position`, or `funding_available` outranks an equally matched supervisor with only historical supervision evidence.
- do not infer current capacity merely because a professor has current students.
- re-check this gate immediately before each new outreach batch.
- for Concordia CS/SE PhD, treat the supervisor-match step as execution-critical: the official admissions process states that an admission offer is not issued until a supervisor match is made. This increases the priority of verified-active Concordia supervisors without changing the academic hard gates.

## Same-school / same-department contact lifecycle

Do not expose multiple professors in the same department to a burst of similar cold emails. Use a deterministic lifecycle instead of an approximate cooldown.

Default manual/automation behavior:

- keep **one new cold contact per `university + department` in the foreground at a time**;
- `T0` is the timestamp of the first cold email;
- count business days in the receiver's local calendar; Saturday/Sunday do not count;
- if there is **no substantive human reply by 10:00 receiver-local time on business day 5**, set `STALE_NO_REPLY`;
- at that exact trigger, do both: **(1) send exactly one second/final follow-up to the same supervisor; (2) set the university/department to `UNLOCKED` for the next supervisor**;
- after the second email, another 5 business days without a substantive reply sets `NO_REPLY_FINAL / CLOSED`; **never send a third email**;
- an explicit `declined` or `no_capacity` response unlocks immediately and normally suppresses the second follow-up;
- `interested`, `requested_materials`, `interview`, `supervision_discussion`, or an active private-channel relationship freezes the remaining same-department cold-outreach queue;
- delivery receipts and generic auto-replies are not substantive replies; if an out-of-office response provides a return date, defer the waiting window until after that return date;
- an already-existing follow-up thread is not restarted as a new cold contact. If its final follow-up expires, mark it `DORMANT` and unlock the school rather than sending another message;
- a warm/private-channel lead is exempt from the ordinary 5-business-day cold timer. Use the explicit relationship state and documented manual-clear condition instead.

The root README and `applications/OUTREACH-LOG.md` must show the foreground contact, the exact invalidation/unlock date when known, and which same-school candidates are `HOLD` behind that contact.

## Automation rules

- Never mass-email every faculty member in a department.
- Never send to a supervisor whose programme is PRUNED/REJECTED, even if they remain in historical/staging YAML.
- Stop repeated follow-ups after clear non-response unless new evidence changes the case.
- Use the program's `narrative_route` to select Boss / DS-Hns / Quant-Ultra / Privacy Lens evidence.
- For fully automatic sending, log every sent message and reply state in structured application/supervisor data **and** refresh the README human ledger.
- For manual sending, do not mark a message `SENT` until the user actually confirms/sends it; prepared drafts remain `READY` / `HOLD`.
- Do not claim prior contact, interest, funding, or supervision unless it is recorded as evidence.
- If candidate-state sources conflict, the stricter human-control file under `targets/` wins until data is reconciled.
- If contact-history sources conflict, the newer explicit human ledger/application contact record wins over stale `not_contacted` YAML.
