# Application Execution Rules

> **Current application workflow — 2026-10-06.** This is the single rulebook for outreach, material generation, QA, application-state handling and human approval.

## 1. Operating principle

The repository is a **source of truth and preparation system**, not permission to submit blindly.

Automation should do as much deterministic work as possible, but retain explicit human checkpoints for irreversible/high-stakes actions.

## 2. Source-of-truth precedence

For program/supervisor facts:

1. current cited evidence / official source;
2. current structured state in `data/*.yaml`;
3. current generated dashboard/views;
4. dated target snapshots;
5. archive.

For contact history:

1. confirmed sent/replied events in `applications/OUTREACH-LOG.md` or application-specific CONTACTS/TIMELINE;
2. current mailbox evidence when available;
3. current README dashboard;
4. structured supervisor state;
5. older snapshots.

A stale YAML `not_contacted` value must never erase a known sent/replied event.

## 3. Application state machine

Use:

`DISCOVERED → VERIFIED → ELIGIBLE → ACTIVE → PACKAGE_READY → HUMAN_REVIEW → SUBMITTED → INTERVIEW / WAITING → OFFER / REJECTED / WITHDRAWN`

Side states:

- `BLOCKED`
- `WATCH`
- `HOLD`
- `CLOSED`

No state may imply payment, submission, referee completion, supervisor commitment or funding unless evidence exists.

## 4. Outreach eligibility

A supervisor can enter a current send queue only when all are true:

- program has survived screening;
- research method is compatible;
- current 2027 capacity/recruitment is verified or the program explicitly supports supervision inquiries;
- a public direct email is verified from an official/lab/personal page;
- the current route permits direct email/contact;
- exact program-supervisor compatibility is confirmed or sufficiently explicit;
- same-school/same-department contact lock is clear.

Do not guess email addresses.

Do not use a public email to bypass an explicit “form/portal only” or “do not email” instruction.

## 5. Same-school contact lock

Default rule:

> **one new cold contact per university + department at a time.**

Existing warm/replied/interview threads take precedence over fresh cold outreach.

For a normal first email:

- T0 = sent;
- after **5 business days** with no substantive reply → one final follow-up may be prepared/sent and the department may be unlocked;
- after another **5 business days** with no substantive reply → `NO_REPLY_FINAL / CLOSED`;
- never send a third cold follow-up.

Automatic acknowledgements and ordinary OOO messages do not count as substantive replies. If an OOO supplies a return date, recalculate from that date.

Private/warm channels use their explicit application-specific rule rather than the generic timer.

## 6. Material generation

A school/supervisor package may contain:

- tailored CV;
- SOP / personal statement;
- research statement;
- research proposal;
- past-research response;
- short-answer responses;
- outreach subject/body;
- transcript and supporting-document manifest;
- project links;
- referee plan;
- application checklist.

Generate from reusable sources; do not maintain independent factual copies of the same biography/project claim for every school.

### Claim safety

Generated text may use only:

- verified applicant facts;
- verified score/document records;
- project claims inside the current accepted evidence boundary;
- target-specific facts verified for the current cycle.

Important current boundaries:

- **Utopia/PCF**: PCF is planned research/engineering expansion, not completed evidence.
- **Utopia**: do not claim completed wearable hardware, completed assistant/persona layer, completed LLM router or completed Boss/Hns connectors unless later verified.
- **Boss/Hns papers**: do not claim peer-reviewed publication unless actually accepted/published.
- Independent projects must not be described as referee-supervised work when they were not.

## 7. Package QA gate

A package cannot become `PACKAGE_READY` until checks pass for:

- correct university/program/supervisor;
- current intake/deadline;
- current GRE/English/academic/funding gates;
- correct project lead for the supervisor;
- word/page limits;
- required sections;
- required documents;
- no missing attachment represented as real;
- no stale supervisor opening;
- no contradictory scores;
- no unsupported publication/project claims;
- no duplicated cold outreach;
- no hard-gate violation;
- compilable PDF/source where applicable.

A failed check returns the package to `BLOCKED` or `DRAFT`; it does not silently waive the requirement.

## 8. Documents and scores

Use `Documents/` as source evidence.

Current structured score files:

- `Documents/Bachelor Score.csv`
- `Documents/Master Score.csv`

Derived scores are analysis outputs, not replacements for official transcripts.

Keep clear separation among:

- official transcript;
- screenshot/progress record;
- derived CSV;
- calculated WAM/GPA/equivalency;
- target-university equivalency decision.

Never present a derived file as an official transcript.

## 9. Referees

Reference tracking must distinguish:

- invited;
- accepted;
- submitted;
- unknown;
- deadline.

Also distinguish:

- facts the referee actually knows;
- new information supplied since last contact;
- a user-provided draft;
- the referee's actual submitted letter, which is unknown unless confirmed.

Do not backfill Boss, Hns, Utopia or other independent projects into an old referee relationship as if they were previously supervised.

## 10. Human checkpoints

Human approval is required for:

- paying an application fee;
- final portal submission;
- sending a high-stakes statement not already supported by stored evidence;
- accepting/declining an offer;
- committing to a supervisor/funding arrangement;
- any action that would materially misrepresent identity, scores, publication status or project completion.

Routine research, package generation, QA, status refresh and preparation may be automated.

## 11. Dashboard rule

The root `README.md` is a **lazy dashboard**, not an archive and not a rulebook.

It should show only:

- current research/application focus;
- what needs action now;
- what is waiting;
- what is blocked/verification-only;
- critical deadlines;
- critical material gaps;
- links to detailed evidence.

Historical tables belong in application logs, dated target snapshots or archive.

## 12. Completion definition

“Application prepared” means:

- eligibility rechecked;
- package generated;
- QA passed;
- references/deadlines known;
- portal requirements mapped;
- user-facing review bundle ready.

“Submitted” means there is actual submission evidence, not merely a completed draft.
