<!-- 中文默认视图 -->

# 历史说明 — 2026-09-16-application-plan-restructure.md

> 历史重构计划，仅用于追溯当时设计过程；当前执行规则已经合并到 rules/。
>
> 本页属于历史证据/设计快照。为了避免改写历史原文，旧英文内容原样保留在下方折叠区。正常日常操作无需展开。

<details>
<summary><strong>展开历史英文原始快照</strong></summary>

# Application-Plan Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert `Application-Plan` into a lazy-readable Markdown dashboard plus YAML-backed application decision system without trusting stale August program facts.

**Architecture:** `README.md` becomes the human control center; canonical machine state lives in `data/*.yaml`; target lists and per-application folders are views over that state. Historical prose is preserved verbatim under `archive/`. Program requirements that have not been refreshed are represented as `unknown` rather than copied as current facts.

**Tech Stack:** Markdown, YAML, GitHub repository files.

**Spec:** `docs/superpowers/specs/2026-09-16-application-plan-restructure-design.md`

## Global Constraints

- No legacy global ordinal school ranking.
- Hard gates are separate from friction and low-weight lifestyle references.
- LGBT/trans and ACG are tie-breakers only.
- Existing `Documents/` artifacts remain intact.
- Old requirements are not promoted to current facts without re-verification.
- Already-submitted applications are tracked separately from screening candidates.
- Human-facing pages put next actions first and stay concise.

---

### Task 1: Preserve History and Establish Canonical Data Files

**Files:**
- Create: `archive/README-2026-08-15.md`
- Create: `data/programs.yaml`
- Create: `data/applications.yaml`
- Create: `data/supervisors.yaml`

**Interfaces:**
- Consumes: existing `ReadMe.md` and approved design spec.
- Produces: canonical program/application/supervisor state used by all Markdown views.

- [ ] Copy the existing `ReadMe.md` verbatim to `archive/README-2026-08-15.md`.
- [ ] Create `programs.yaml` with the known candidate set, but mark mutable August facts `unknown` unless confirmed later.
- [ ] Record University of Macau as already submitted.
- [ ] Record University at Buffalo as closed by user due to confirmed mandatory English-test requirement.
- [ ] Record Concordia as an active supervisor/outreach case without inventing formal admission state.
- [ ] Include lifestyle fields for every program with neutral `unknown` defaults unless explicitly refreshed.
- [ ] Validate YAML indentation and unique IDs by manual structural review.

### Task 2: Replace the Monolithic README with a Lazy Dashboard

**Files:**
- Modify: `ReadMe.md`
- Create: `README.md`
- Create: `STRATEGY.md`
- Create: `STATUS.md`

**Interfaces:**
- Consumes: `data/*.yaml`.
- Produces: 30-second human-readable entry points.

- [ ] Create a concise `README.md` dashboard with current state, next actions, active applications, candidate buckets, recent closures, and links.
- [ ] Create `STRATEGY.md` documenting hard gates, friction, utility, lifestyle tie-breakers, and portfolio routing.
- [ ] Create `STATUS.md` as an operational snapshot separate from long-term strategy.
- [ ] Replace legacy `ReadMe.md` with a compatibility redirect to `README.md` so GitHub/case-sensitive links do not leave two competing dashboards.
- [ ] Confirm no legacy `#1/#2/...` overall ranking appears in the new dashboard.

### Task 3: Build Target Views

**Files:**
- Create: `targets/ACTIVE.md`
- Create: `targets/BACKUP.md`
- Create: `targets/WATCHLIST.md`
- Create: `targets/REJECTED.md`

**Interfaces:**
- Consumes: `data/programs.yaml`.
- Produces: human-readable filtered views.

- [ ] Put currently actionable non-submitted programs in ACTIVE only when they are not known to violate a hard gate.
- [ ] Put conditional/high-friction choices in BACKUP.
- [ ] Put stale/unverified choices in WATCHLIST rather than pretending they are application-ready.
- [ ] Put Buffalo in REJECTED with reason code `ENGLISH_RETEST_REQUIRED` and a concise reconsideration condition.
- [ ] Ensure every entry has a one-line “why still here” or “why rejected” note.

### Task 4: Separate Real Applications from Candidate Screening

**Files:**
- Create: `applications/university-of-macau/STATUS.md`
- Create: `applications/university-of-macau/CONTACTS.md`
- Create: `applications/university-of-macau/TIMELINE.md`
- Create: `applications/university-of-macau/SUPERVISORS.md`
- Create: `applications/concordia/STATUS.md`
- Create: `applications/concordia/CONTACTS.md`
- Create: `applications/concordia/TIMELINE.md`
- Create: `applications/concordia/SUPERVISORS.md`
- Create: `applications/university-at-buffalo/STATUS.md`

**Interfaces:**
- Consumes: `data/applications.yaml`, known conversation state, archived August notes.
- Produces: operational application histories that do not contaminate screening logic.

- [ ] Record UM submission/payment as completed and keep unresolved reference/follow-up details explicitly uncertain where necessary.
- [ ] Record Concordia supervisor contact/interview history conservatively without claiming an offer that is not stored as formal evidence.
- [ ] Record Buffalo as closed by user following the English-testing response.
- [ ] Keep each page next-action-first and short.

### Task 5: Rebuild Materials and Narrative Routing

**Files:**
- Create: `materials/MATERIALS.md`
- Create: `materials/research-profile.md`
- Create: `materials/project-positioning.md`

**Interfaces:**
- Consumes: current portfolio model.
- Produces: reusable application narrative routing rules.

- [ ] Build a concise common-materials checklist.
- [ ] Replace Quant-Ultra-only identity with Boss / DS-Hns / Quant-Ultra / Privacy Lens portfolio routing.
- [ ] Describe which project leads for agentic AI, software engineering, ML/data/finance, and trustworthy systems supervisors.
- [ ] Explicitly prevent raw trading-performance claims from becoming the universal research narrative.

### Task 6: Add Automation Contracts

**Files:**
- Create: `automation/outreach-policy.md`
- Create: `automation/screening-schema.md`
- Create: `automation/auto-application-spec.md`

**Interfaces:**
- Consumes: `data/*.yaml`, strategy rules.
- Produces: contracts for Boss, DS-Hns, and future outreach/application automation.

- [ ] Define when outreach is required/recommended/low-ROI.
- [ ] Define screening order Hard Gate → Friction → Utility → Action State.
- [ ] Define automation safety rules: never auto-promote stale facts, never silently spend fees, never fabricate application completion, and preserve source freshness metadata.
- [ ] Define machine states used by downstream tools.

### Task 7: Verify the Restructure

**Files:**
- Review all new and modified files.

**Interfaces:**
- Consumes: entire restructure branch.
- Produces: verified branch suitable for PR/merge review.

- [ ] Fetch repository tree and confirm required paths exist.
- [ ] Check `README.md` is substantially shorter than the archived monolith and answers next-action questions immediately.
- [ ] Search new content for legacy global priority numbering patterns and remove them.
- [ ] Search for stale August dates presented as current requirements and convert them to archive-only or `unknown`.
- [ ] Confirm `Documents/` binary source materials are unchanged.
- [ ] Compare branch against `main` and review all changed filenames before completion.


</details>
