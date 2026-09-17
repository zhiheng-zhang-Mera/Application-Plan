# Supervisor Outreach Folder Restructure — Design

## Purpose

Refactor the PhD outreach materials so that every supervisor has a dedicated folder with an auditable, conservative, current email package. The repository root `README.md` remains the human-operated control panel: copy the email address, open the supervisor-specific email, check attachments/supporting evidence, send manually, then record contact history.

This design applies to all supervisors for whom the repository already contains outreach content or active outreach metadata in the current Concordia, Singapore, Hong Kong, and University of Macau application tracks.

## Goals

1. One supervisor = one folder.
2. Separate first-contact email from follow-up text.
3. Keep contact history and send-state close to the supervisor-specific text.
4. Rewrite every existing email using the latest verifiable GitHub project state.
5. Do not exaggerate implementation status, evaluation status, skill stack, funding, admission probability, supervision interest, or publication status.
6. Allow different supervisors to receive different emphasis, but only by selecting different verified facts from a shared factual baseline.
7. Preserve old combined outreach documents as historical indexes only; they must no longer remain competing send-ready sources.

## Canonical folder layout

Each school keeps its existing application directory. Supervisor-specific material moves under `supervisors/<slug>/`.

```text
applications/
  concordia/
    supervisors/
      zhijie-wang/
        README.md
        EMAIL.md
        FOLLOWUP.md
      tse-hsun-peter-chen/
        README.md
        EMAIL.md
        FOLLOWUP.md
      ...
  singapore/
    supervisors/
      sutd-thanh-le-cong/
        README.md
        EMAIL.md
        FOLLOWUP.md
      ...
  hong-kong/
    supervisors/
      polyu-yu-pei/
        README.md
        EMAIL.md
        FOLLOWUP.md
      ...
  university-of-macau/
    supervisors/
      li-li/
        README.md
        EMAIL.md
        FOLLOWUP.md
      ...
```

Slug rule: lowercase ASCII where practical, hyphen-separated, and prefixed with university shorthand when needed to avoid ambiguity inside multi-school regional folders.

## File responsibilities

### `README.md`

Supervisor control card only. It must contain:

- supervisor name
- university / department / target programme
- email address
- current outreach state
- recruitment/capacity evidence summary and verification date
- exact research-overlap emphasis for this supervisor
- recommended supporting materials
- `EMAIL.md` and `FOLLOWUP.md` links
- contact history table with last-contact date, count, state, reply summary, and next action
- same-school cooldown / freeze note when applicable

It must not contain a second copy of the full outreach email.

### `EMAIL.md`

The canonical first-contact email. Structure:

```markdown
# First Contact

**To:** `...`
**Subject:** ...

<complete email body>

## Evidence notes

- fact used → source/repository state
- fact deliberately not claimed → reason

## Attachments

- ...
```

For supervisors who explicitly forbid email, `EMAIL.md` must start with `DO NOT EMAIL` and explain the required alternative workflow. It may store form-ready text if that is the supervisor's required route.

### `FOLLOWUP.md`

Supervisor-specific follow-up material. It must include:

- default no-reply follow-up draft
- when not to send it
- how to respond if the professor requests CV/transcript/research summary
- freeze/unlock rule for other supervisors at the same school/department

For an existing live thread such as Zhijie Wang, this file becomes the primary sendable artifact; `EMAIL.md` records that a new cold introduction must not be sent.

## Root README behavior

The root `README.md` remains the human manual-send console.

For each front-line supervisor, the table must provide:

- school
- supervisor
- copyable email
- link to supervisor folder
- direct link to `EMAIL.md` or `FOLLOWUP.md`
- attachments/supporting-material hint
- last contact
- contact count
- current state
- next action / cooldown

The root README must not duplicate complete email bodies.

The root README contact ledger is the fastest human-view history. Detailed history lives in each supervisor folder. If a historical YAML record conflicts with an updated manual contact state, the manual contact record controls outreach behavior until reconciled.

## Shared factual baseline for project claims

All rewritten emails must draw from a shared conservative evidence baseline.

### Codex Boss

Allowed current claims:

- It is a public project for multi-agent / long-running autonomous work orchestration and evidence-based acceptance.
- Platform-foundation work includes durable state/events, capability/security boundaries, plugin-related architecture, knowledge/data lifecycle, scale/verification work, dogfooding, and semantic acceptance.
- Phase 07 semantic acceptance is now recorded as PASS on branch `platform-foundation/07-semantic-acceptance`.
- The recorded exact-head local gate includes 2,517 unit tests across 215 files, 113 postbuild tests across 10 files, clean typecheck, a passing 17/17 platform certificate, and other recorded local checks.
- These are local exact-head executions, not remote CI evidence.

Disallowed or qualified claims:

- Do not say Boss has solved autonomous research, autonomous coding, or semantic verification in general.
- Do not call local gate evidence remote CI.
- Do not imply every evolution/autonomy acceptance path is complete; the evolution prestart attestation is a separate line and must not be silently conflated with Phase 07.
- Do not claim publication-quality evaluation, human-study validation, or production reliability without evidence.

### DS-Hns

Allowed current claims:

- Long-horizon software-work / DeepSeek Harness extension project.
- Current code includes a plugin adapter framework, native HNS adapter path, Cordis/DSH community-plugin adaptation, a managed-process adapter with bounded restart/fault isolation semantics, a health scheduler that only requests restart through a separate capability, and a unified plugin install pipeline.
- The architecture separates monitoring from restart authority and keeps plugin/process boundaries explicit.

Disallowed or qualified claims:

- Do not claim proven 24/7 unattended operation as an empirical result.
- Do not claim complete Computer Use capability unless separately verified in the current codebase.
- Do not say the health scheduler itself performs restart.
- Do not imply all plugin compatibility or installation paths are universally production-complete.
- Do not turn planned restart/recovery UX into demonstrated research results.

### Quant-Ultra

Allowed current claims:

- The `8-30` branch contains an evidence-governed quantitative research architecture with a Research OS layer around the existing quant pipeline.
- It uses point-in-time controls, deterministic evidence gates, reproducible research artifacts, and human authorization boundaries.
- The public README reports backtest/audit metrics with explicit limitations.

Disallowed or qualified claims:

- Do not use informal recent live-account profitability/win-rate figures unless a current repository artifact independently supports them.
- Do not present backtests as guaranteed live performance.
- Do not present the project as autonomous live trading authority.

### Privacy Lens / GDPR project

Allowed current claims:

- Offline, evidence-first Android privacy-review research prototype.
- Version 1.15.0 is the current repository delivery candidate.
- It separates observed evidence from synthetic demonstrations, uses fail-closed governance/evidence boundaries, and explicitly avoids unsupported legal conclusions.
- It includes deterministic checks and bounded physical-device evidence from one OPPO device.

Disallowed or qualified claims:

- Do not say the app determines GDPR infringement.
- Do not imply a one-device observation is broad real-world validation.
- Do not imply legal certification, peer review, participant-study validation, or store-production readiness.

## Writing rules for all supervisor emails

1. Prefer “I am building / I have implemented / the current repository includes” over inflated phrases such as “I specialize in” unless the user's formal training or repeated evidence supports the claim.
2. Describe the user's degree history factually: UBC BSc in Computer Science; University of Melbourne Master's in Computer Science in progress/completing, as already used in the repository.
3. Research-interest language may be aspirational: “I would like to study…” is allowed even when the user has not yet implemented that exact research direction.
4. Separate project fact from proposed PhD question.
5. Never turn a supervisor's topic into a claimed existing skill. Example: if a supervisor works on program analysis, the email may say the user's projects create a problem that could be studied with program-analysis/testing methods; it must not say the user is already an expert in program analysis unless evidence exists.
6. Avoid prestige flattery and generic phrases. Use one or two concrete overlap points.
7. Keep first-contact messages compact enough to be manually reviewed before sending.
8. Funding, scholarship, capacity, admission, and programme-compatibility claims must remain conditional unless explicitly documented.
9. Existing contact history must be preserved. Do not regenerate a cold-introduction email for a live thread and then accidentally surface it as send-ready.

## Supervisor-specific emphasis rules

Different supervisors may receive different emphasis using the same verified project facts.

Examples:

- AI4SE / testing / repair supervisors: Boss semantic acceptance + DS-Hns execution/failure boundaries; frame the PhD question around repair evidence, test adequacy, regression-aware acceptance, or empirical repository evaluation.
- Systems / distributed / runtime supervisors: DS-Hns process/plugin boundaries, state, failure isolation, resource-aware orchestration; Boss as higher-level workload/evidence layer.
- Trustworthy AI / security supervisors: capability boundaries, tool-use containment, evidence provenance, Privacy Lens as a secondary evidence-governance example where relevant.
- Multi-agent / agent-evaluation supervisors: Boss long-horizon state, coordination, evidence acceptance, and comparison to strong single-agent baselines; do not claim mature multi-agent learning expertise.
- AI4Science / computational-health supervisors: Boss as workflow/orchestration infrastructure plus the user's simulation prototypes as motivation; do not present those prototypes as validated biomedical systems.
- Quant / RL / financial-data supervisors: Quant-Ultra as an evidence-governed empirical research system; avoid live-profit claims.

## Migration of current combined outreach files

Current files such as:

- `applications/concordia/OUTREACH-DRAFTS-2026-09-17.md`
- `applications/singapore/OUTREACH-DRAFTS-2026-09-17.md`
- `applications/hong-kong/OUTREACH-DRAFTS-2026-09-17.md`
- `applications/university-of-macau/OUTREACH-DRAFTS-2026-09-17.md`

must no longer contain the canonical send-ready body after migration. They will be replaced with compact migration indexes pointing to the supervisor folders and stating that per-supervisor files are authoritative.

This preserves Git history while preventing duplicate editable versions.

## Initial migration scope

The migration must include every supervisor for whom the current repository already stores an email draft, form-ready outreach text, or live follow-up draft.

At minimum this includes:

### Concordia
- Zhijie Wang
- Tse-Hsun (Peter) Chen
- Peter Rigby
- Jinqiu Yang
- Shin Hwei Tan
- Yann-Gaël Guéhéneuc

### Singapore
- Thanh Le-Cong
- Ezekiel Soremekun
- Ruochen (Esther) Zhao
- Wenxuan Zhang
- Chengpeng Wang
- Abhik Roychoudhury
- Penghui Li (form workflow; do not email)

### Hong Kong
- Yu Pei
- Heqing Huang
- Yu Li
- Nan Guan
- Zhisong Zhang
- Zuming Jiang
- Ka Ho Chow
- Heming Cui

### University of Macau
- Li Li
- Xiaobo Zhou
- Leong Hou U
- Cheng-Zhong Xu

If an existing combined draft contains another complete supervisor-specific email, that supervisor is added to migration rather than left behind.

## Contact-state integrity

No migration operation may silently change historical contact state.

Examples:

- Zhijie Wang remains an existing-contact/follow-up case.
- Lin Yan remains do-not-pursue after repeated non-response unless new evidence changes the case.
- Supervisors blocked by programme hard gates remain WATCH/BACKUP even if their email text is ready.
- Penghui Li remains form-only and must not become an email action.

## Verification after migration

The migration is complete only when:

1. Every canonical root-README outreach link resolves to a supervisor folder.
2. Every migrated supervisor folder has `README.md`, `EMAIL.md`, and `FOLLOWUP.md`.
3. No combined `OUTREACH-DRAFTS-*` file remains a competing source of complete send-ready email bodies.
4. A repository search for outdated claims such as `2,508 unit tests across 215 files` in current send-ready email files has been reviewed and updated where the claim referred to the now-newer Phase 07 state.
5. No current send-ready email claims Phase 07 is unfinished when the latest recorded Phase 07 status is PASS.
6. No current send-ready email upgrades local exact-head tests into remote CI claims.
7. No current send-ready email claims DS-Hns has complete 24/7 empirical validation, complete Computer Use, or direct health-scheduler restart authority.
8. No current send-ready email uses unverified Quant live-profit figures.
9. Every root README contact-history row points to the correct supervisor folder and keeps the same-school cooldown state.
10. Historical contact facts are unchanged except for explicit migration/path updates.

## Maintenance rule going forward

All future outreach editing happens inside the relevant supervisor folder. A new email version replaces `EMAIL.md`; a new follow-up replaces or appends to `FOLLOWUP.md`; contact events update the supervisor `README.md` and the root ledger. Regional or school-level documents may summarize status but must not regain full duplicate email bodies.
