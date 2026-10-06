<!-- 中文默认视图 -->

# 历史说明 — 2026-09-16-application-plan-restructure-design.md

> 历史重构设计规格，仅用于追溯；当前仓库结构与规则以 README、rules/ 和 docs/STRUCTURE.md 为准。
>
> 本页属于历史证据/设计快照。为了避免改写历史原文，旧英文内容原样保留在下方折叠区。正常日常操作无需展开。

<details>
<summary><strong>展开历史英文原始快照</strong></summary>

# Application-Plan Restructure Design

## Goal

Rebuild `Application-Plan` from a monolithic school-list README into a low-friction PhD application decision system using **Markdown for human reading** and **YAML for machine-readable state**.

The repository must optimize for two readers:

1. **Human / lazy reading:** a user should understand current application status and next actions within roughly 30 seconds from `README.md`.
2. **Automation / agents:** Boss, DS-Hns, future outreach plugins, and scripts should be able to consume structured school/application data without parsing prose.

## Core Strategy

The repository no longer ranks schools by a single global ordinal ranking. Decisions use a four-stage model:

1. **Hard Gate** — reject programs that violate non-negotiable constraints.
2. **Friction** — measure application and admission burden.
3. **Utility** — measure funding, fit, likely day-to-day suitability, and research compatibility.
4. **Action State** — assign an operational state such as `APPLY_NOW`, `APPLY`, `BACKUP`, `WATCH`, `HOLD`, or `REJECT`.

Historical content remains archived rather than deleted.

---

## 1. Hard Gates

A program is normally moved to `REJECT` when any of the following is true:

- GRE is required.
- A new IELTS / TOEFL / DET result is mandatory and the English-medium bachelor/master background cannot satisfy or waive the requirement.
- The program is substantially self-funded or funding is clearly insufficient relative to mandatory tuition and basic living costs.
- The program falls materially below the accepted academic floor represented approximately by Concordia-level research universities.
- The program is in New Zealand.

Hard-gate decisions must include a short reason code and a source / verification date when based on a university rule.

Suggested reason codes:

- `GRE_REQUIRED`
- `ENGLISH_RETEST_REQUIRED`
- `UNFUNDED`
- `ACADEMIC_FLOOR`
- `REGION_EXCLUDED`
- `PROGRAM_CLOSED`
- `OTHER_HARD_GATE`

---

## 2. Friction Model

Friction is important but usually not a hard reject by itself.

Track at least:

- `supervisor_first`: whether a supervisor must be secured before an offer.
- `interview_burden`: `none | light | normal | heavy`.
- `exam_burden`: `none | light | technical | heavy`.
- `application_fee`.
- `proposal_burden`: `none | short | normal | heavy`.
- `reference_burden`: number of letters / special forms.
- `outreach_burden`: `none | optional | recommended | required`.
- `video_allowed`: whether asynchronous recorded material can replace some synchronous screening.

Interpretation priority:

- No exam and no interview is best.
- Recorded video is acceptable and lower-friction than synchronous panels.
- Normal research conversations are tolerable.
- Mandatory written tests, technical panels, and repeated interview rounds receive a meaningful penalty.
- Required supervisor outreach is a penalty because it increases manual effort.

---

## 3. Utility Model

Utility is descriptive rather than a single authoritative score.

Track:

- funding coverage
- tuition burden
- local living-cost coverage
- research fit
- compatibility with coding / systems / agentic AI work
- likely graduation burden / program rigidity
- location convenience
- application feasibility based on existing academic profile

The repository should prefer readable labels such as `excellent`, `good`, `mixed`, `poor`, and concise notes over dense numerical scoring.

The system must avoid presenting speculative admission probabilities as facts. If probability-like estimates are stored for internal planning, clearly label them as subjective planning estimates and separate them from verified program requirements.

---

## 4. Low-Weight Lifestyle References

Lifestyle references are **secondary context only** and must never override hard admission/funding constraints.

### LGBT / Trans Reference

Track a lightweight field for practical day-to-day environment, not a moral or political ranking.

Recommended fields:

```yaml
lifestyle:
  lgbt_trans:
    level: unknown   # comfortable | workable | mixed | difficult | unknown
    notes: ""
    last_verified: null
```

Possible considerations:

- practical campus / city environment
- access to ordinary healthcare and administrative services
- day-to-day social tolerance
- whether there are obvious legal or institutional constraints relevant to a student

This field remains a small tie-breaker and must not dominate academic/funding decisions.

### ACG / Anime / Gaming / Comic Reference

Use `acg` as the canonical name. This is also a small tie-breaker.

```yaml
lifestyle:
  acg:
    level: unknown   # strong | decent | limited | weak | unknown
    notes: ""
```

Possible considerations:

- anime / manga / game shops and events
- cosplay / convention activity
- gaming / hobby communities
- access to imported Japanese / Chinese ACG goods

Do not spend excessive research time maintaining this field.

---

## 5. Research Portfolio Positioning

The repository must no longer lock the application narrative to Quant-Ultra.

Use a portfolio-routing model:

### Codex Boss

Best aligned with:

- autonomous research
- multi-agent systems
- agent orchestration
- AI evaluation
- LLM systems

### DS-Hns

Best aligned with:

- autonomous software engineering
- long-horizon coding agents
- computer use
- fault recovery
- unattended task execution

### Quant-Ultra

Best aligned with:

- financial ML
- temporal validation
- non-stationary data
- research infrastructure
- optimization / data systems

### Privacy Lens and other projects

Secondary supporting evidence for:

- trustworthy software
- privacy / governance
- applied systems work

Each program / supervisor may specify a `narrative_route` rather than inheriting one universal story.

---

## 6. Repository Structure

```text
Application-Plan/
├── README.md
├── STRATEGY.md
├── STATUS.md
├── data/
│   ├── programs.yaml
│   ├── supervisors.yaml
│   └── applications.yaml
├── targets/
│   ├── ACTIVE.md
│   ├── BACKUP.md
│   ├── WATCHLIST.md
│   └── REJECTED.md
├── applications/
│   └── <school-slug>/
│       ├── STATUS.md
│       ├── CONTACTS.md
│       ├── TIMELINE.md
│       └── SUPERVISORS.md
├── materials/
│   ├── MATERIALS.md
│   ├── research-profile.md
│   └── project-positioning.md
├── automation/
│   ├── outreach-policy.md
│   ├── screening-schema.md
│   └── auto-application-spec.md
├── archive/
│   └── README-2026-08-15.md
├── docs/
│   └── superpowers/
│       ├── specs/
│       └── plans/
└── Documents/
```

`Documents/` remains untouched during restructuring except for removal of meaningless placeholders if safe.

---

## 7. README: Lazy-Reading Control Center

`README.md` must be short, operational, and skimmable.

It should contain only:

1. current cycle and strategy in 3–6 lines
2. a compact status summary
3. active applications
4. next actions
5. high-priority targets
6. recently rejected / changed programs
7. links to deeper documents

Avoid putting full program requirements, faculty lists, essay checklists, or long explanations in the README.

The target user experience is:

> Open README → immediately know what has already been submitted, what to do next, and which programs still deserve attention.

---

## 8. YAML Data Model

### `data/programs.yaml`

Canonical program-level facts and decision state.

Example schema:

```yaml
programs:
  - id: concordia-cs-phd
    university: Concordia University
    program: PhD in Computer Science
    country_region: Canada
    action_state: APPLY
    verification:
      last_verified: null
      source_urls: []
    hard_gates:
      gre_required: false
      english_retest_required: unknown
      funded: unknown
      academic_floor_pass: true
      region_pass: true
    friction:
      supervisor_first: true
      interview_burden: normal
      exam_burden: none
      outreach_burden: required
      proposal_burden: short
      reference_count: 3
    utility:
      funding: unknown
      research_fit: good
      coding_systems_fit: good
      graduation_burden: unknown
      cost_coverage: unknown
    lifestyle:
      lgbt_trans:
        level: unknown
        notes: ""
        last_verified: null
      acg:
        level: unknown
        notes: ""
    narrative_route:
      - codex-boss
      - ds-hns
```

### `data/applications.yaml`

Contains actual application workflow state, not program facts.

Recommended states:

- `not_started`
- `researching`
- `outreach`
- `preparing`
- `submitted`
- `interview`
- `waitlisted`
- `offer`
- `rejected`
- `withdrawn`
- `closed_by_user`

### `data/supervisors.yaml`

Stores supervisor-specific fit, contact history, and narrative route. Avoid duplicating program-wide requirements here.

---

## 9. Existing Applications

Already-submitted applications must be separated from the candidate screening pool.

For example, University of Macau belongs under `applications/` with its actual workflow history and next actions. It may still appear in the dashboard, but the question is no longer “should we apply?” — it is “what happens next?”.

Programs eliminated by a confirmed requirement should remain in `REJECTED.md` / YAML rather than disappearing, so future searches do not repeatedly rediscover them.

---

## 10. Source Freshness

Program requirements change. Every important verified fact should support:

- `last_verified`
- a source URL where practical
- optional short note

High-change fields include:

- deadlines
- GRE requirement
- English requirement / waiver
- funding
- supervisor requirement
- application fee
- interview / exam process

Stale information should degrade to `unknown` rather than silently being treated as current.

Lifestyle fields may be maintained at lower freshness because they are low-weight references.

---

## 11. Human-Reading Rules

Use these conventions throughout the repository:

- Put **next action first**.
- Prefer short tables to prose.
- Keep each school detail page independent.
- Use status symbols sparingly and consistently.
- Do not repeat full requirements in multiple files.
- Put archive/history below current state.
- Prefer `unknown` over speculative filler.
- Every rejection must state one concise reason.
- Every active target must state one concise reason why it remains worth attention.
- Lifestyle notes should usually fit in one line.

---

## 12. Migration Rules

1. Copy current `ReadMe.md` verbatim to `archive/README-2026-08-15.md` before replacing it.
2. Preserve `Documents/` source materials.
3. Re-express current schools as structured records instead of copying old rankings.
4. Treat old deadlines / GRE / English / funding information as unverified until refreshed.
5. Do not preserve the old global school ranking numbers.
6. Do not preserve Quant-Ultra as the universal application narrative.
7. Separate verified facts from subjective planning notes.
8. Keep already-submitted applications operationally distinct from candidate targets.

---

## 13. Initial Migration Priorities

The first migration should prioritize correctness of structure over exhaustive re-research.

Order:

1. archive old README
2. create new dashboard README
3. create strategy and status documents
4. establish YAML schema
5. migrate known application states
6. migrate current target / rejected school names with stale fields explicitly marked `unknown`
7. create research-profile routing docs
8. create automation policy docs
9. validate links and YAML syntax
10. only then perform a separate live-data refresh of active schools

This prevents old factual claims from being accidentally promoted into the new structured system.

---

## Success Criteria

The restructure is successful when:

- opening README answers “what should I do next?” in under 30 seconds;
- no school is assigned a legacy global ordinal ranking;
- all active programs have a machine-readable YAML record;
- hard gates are visually and structurally distinct from low-weight preferences;
- LGBT/trans and ACG context exists but cannot independently drive accept/reject decisions;
- project positioning can route among Boss, DS-Hns, Quant-Ultra, and supporting projects;
- submitted applications are tracked separately from candidate screening;
- historical content is preserved in `archive/`;
- stale program facts are clearly marked rather than silently trusted;
- the repository can later be consumed by Boss / DS-Hns / automated outreach tooling without scraping long Markdown prose.


</details>
