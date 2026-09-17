# Concordia Outreach Drafts — 2026-09-17

> These are **individual** drafts, not a bulk-mail template. Refresh recruitment status before send.
>
> Concordia asks prospective CS/SE PhD students contacting supervisors to include their Student ID, CV, transcripts, and a brief research-interest/background/proposal. Fill `[Concordia Student ID]` and attach the current CV + transcripts before sending.

## Shared project facts — verified from current GitHub state

Use only the subset relevant to each supervisor.

- **Codex Boss** — public repo: https://github.com/zhiheng-zhang-Mera/Codex-Boss
  - Current platform-foundation work covers durable state/events, capability security/plugins, knowledge/data lifecycle, scale/soak verification, dogfooding and semantic acceptance.
  - The current semantic-acceptance branch is intentionally **not being presented as finished**: it now rejects a vacuous case, but a meaningful case still exposes a false-negative in the evidence reader.
  - Current regression at that branch: **2,508 unit tests across 215 files**, plus Electron/renderer/test typechecking.
- **DS-Hns** — public repo: https://github.com/zhiheng-zhang-Mera/DS-Hns
  - Long-horizon software-work harness built around the official DeepSeek Harness UI with isolated optional extensions.
  - Current engineering includes ordered/scheduled task queues, hardware-adaptive local concurrency, unified task lifecycle/terminal events, task-history and notification handling, extension isolation, and an idempotent Windows installer/plugin flow.
  - The research angle is not the UI itself: the useful questions are **how autonomous software agents recover, persist state, verify completion and avoid silently accepting weak results**.

---

## 1 — Tse-Hsun (Peter) Chen

**To:** `tse-hsun.chen@concordia.ca`  
**Subject:** Prospective PhD student — reliable coding agents and autonomous software engineering

Dear Professor Chen,

My name is Zhiheng Zhang (Concordia Student ID: `[Concordia Student ID]`). I am completing a Master’s degree in Computer Science at the University of Melbourne, after a BSc in Computer Science from UBC, and I am looking for a PhD supervisor at Concordia.

Your current work on coding agents, automated debugging, fault localization, issue resolution and AIOps is very close to the direction of two systems I am building. **DS-Hns** is a long-horizon software-work harness with persistent task lifecycle, scheduling, failure isolation and recovery-oriented execution, while **Codex Boss** explores multi-agent orchestration and evidence-based acceptance of agent outputs. I am currently hardening Boss’s semantic acceptance layer so that it rejects vacuous “task completed” evidence without over-rejecting meaningful tests; the current branch runs 2,508 unit tests across 215 files.

I would be especially interested in research on **reliable coding agents for repository-scale tasks: fault localization/recovery, long-running execution, and completion criteria that go beyond plausible patches or superficial test passing**.

Would you be open to discussing whether this direction could fit a PhD project in your group?

I have attached my CV and transcripts. My project repositories are:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Why this draft is specific

Peter Chen currently lists AI for SE, coding agents, trustworthy AI, automated debugging and AIOps, and explicitly accepts supervision inquiries. Lead with DS-Hns; Boss is supporting evidence.

---

## 2 — Peter Rigby

**To:** `peter.rigby@concordia.ca`  
**Subject:** Prospective PhD student — autonomous software maintenance and empirical agent evaluation

Dear Professor Rigby,

My name is Zhiheng Zhang (Concordia Student ID: `[Concordia Student ID]`). I am finishing a Master’s in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I saw your recent note that you are looking for PhD students.

I was particularly interested in your 2026 work on **Agentic RACER and autonomous refactoring at scale**. My current project **DS-Hns** approaches a related problem from the execution-infrastructure side: long-horizon software tasks, durable task state, ordered/scheduled work, failure isolation, recovery and unified completion tracking. A second project, **Codex Boss**, focuses on multi-agent orchestration and evidence-based acceptance; I am currently working on distinguishing meaningful completion evidence from vacuous agent-produced tests rather than treating “tests passed” as sufficient by itself.

The PhD question I would like to explore is how to make autonomous maintenance **measurably useful over long-running real repository work**: deciding/triaging work, surviving execution failures, validating changes, and evaluating downstream maintenance or developer-effort effects rather than only benchmark pass rates.

Would this be close enough to your current research agenda to discuss as a possible PhD direction?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Why this draft is specific

Do not send him a generic “LLM agents” pitch. Anchor on his current Agentic RACER / code-review / empirical-at-scale work and frame DS-Hns as execution + measurement infrastructure.

---

## 3 — Jinqiu Yang

**To:** `jinqiu.yang@concordia.ca`  
**Subject:** Prospective PhD student — testing and reliability of autonomous coding agents

Dear Professor Yang,

My name is Zhiheng Zhang (Concordia Student ID: `[Concordia Student ID]`). I am completing a Master’s in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC. I am contacting you because your work on automated program repair, software testing/reliability, ML-system quality assurance and mining software repositories overlaps strongly with the problems I am encountering in my own agent systems.

I am building **DS-Hns**, a long-horizon software-work harness, and **Codex Boss**, a multi-agent orchestration and evaluation platform. One issue I am working on now is particularly relevant to testing/repair research: an agent can generate a test that looks meaningful syntactically but provides weak evidence about whether the intended behavior was actually repaired. Boss’s current semantic-acceptance work is therefore trying to reject vacuous evidence while avoiding false negatives on genuinely discriminating tests; the current branch has 2,508 unit tests across 215 files.

I would like to turn this engineering problem into a research direction around **robust evaluation of coding-agent repairs: failure modes, regression-aware testing, semantic completion criteria, and empirical benchmarks on real repositories**.

Would you be interested in discussing whether this could fit a PhD project under your supervision? I noticed that your current page indicates funding is available for Master’s and PhD students.

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Why this draft is specific

Lead with testing/reliability and the real semantic-acceptance failure mode. Her current student/funding page makes a capacity question unnecessary in the first sentence; ask fit instead.

---

## 4 — Shin Hwei Tan

**To:** `shinhwei.tan@concordia.ca`  
**Subject:** Prospective PhD student — autonomous program repair beyond superficial test passing

Dear Professor Tan,

My name is Zhiheng Zhang (Concordia Student ID: `[Concordia Student ID]`). I am finishing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am looking for a PhD supervisor at Concordia.

Your research on automated program repair and software testing, including repair with large language models, is closely related to a problem emerging from my current projects. **DS-Hns** runs and manages long-horizon software tasks with explicit lifecycle and failure handling, while **Codex Boss** coordinates multiple AI workers and evaluates their outputs. In the current Boss branch, I am hardening semantic acceptance because “the generated patch/test suite passes” can still be weak evidence: the evaluator now rejects a vacuous case, while a genuinely meaningful case has exposed a false-negative that I am fixing rather than masking.

That has pushed me toward a research question I would like to pursue more systematically: **how should autonomous repair agents generate, select and validate repair evidence so that accepted fixes are behaviorally meaningful and regression-resistant?** I would be interested in combining agent execution infrastructure with repair/testing benchmarks and empirical evaluation on real repositories.

Would you be open to a short discussion about whether this direction could fit your group and the Computer Science PhD program?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Why this draft is specific

Keep it focused on repair evidence/testing. Do not feature the plugin/UI work unless asked; it is engineering proof, not the research question.

---

## 5 — Yann-Gaël Guéhéneuc

**To:** `yann-gael.gueheneuc@concordia.ca`  
**Subject:** Prospective PhD student — empirical evaluation of long-horizon autonomous software engineering

Dear Professor Guéhéneuc,

My name is Zhiheng Zhang (Concordia Student ID: `[Concordia Student ID]`). I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am seeking a PhD supervisor at Concordia.

I am interested in your work on empirical software engineering, software comprehension/quality, and the analysis of development, release and testing processes. My main current system, **DS-Hns**, is a long-horizon software-work harness with ordered/scheduled execution, hardware-adaptive concurrency, isolated extensions, explicit task lifecycle and terminal-state tracking. **Codex Boss** complements it with multi-agent orchestration and evidence-based acceptance of generated work.

Rather than treating these only as automation products, I would like to study them as an empirical software-engineering setting: **what traces and quality signals predict whether autonomous development work is actually correct and maintainable; how failures and recoveries evolve over long tasks; and how agent-generated changes affect future maintenance, testing and comprehension**.

Would you be open to discussing whether a systems-and-empirical PhD project along these lines could fit your group?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Why this draft is specific

This is the broad empirical-SE version. Focus on traces, quality and maintainability rather than pitching the agent architecture itself as the research contribution.

---

# Parallel follow-up — Zhijie Wang

> Use this only for the existing email thread. Do not restart with a cold-email introduction.

**To:** `zhijie.wang@concordia.ca`  
**Suggested subject:** keep the existing thread subject

Dear Professor Wang,

Thank you again for our earlier discussion. I wanted to send a short update because the two projects we discussed have moved forward substantially.

For **Codex Boss**, I have been restructuring the platform around durable state/events, capability boundaries, plugin isolation, knowledge/data lifecycle and acceptance/verification. The current semantic-acceptance work is deliberately testing cases where an agent can produce superficially plausible evidence; the latest branch rejects the vacuous case but still exposes a false-negative on a meaningful case, which I am treating as an evaluation problem rather than marking the phase complete. The current regression suite is 2,508 tests across 215 files.

**DS-Hns** has also become a more concrete long-horizon software-engineering system, with scheduled/ordered tasks, hardware-adaptive execution, explicit task lifecycle, failure isolation and a plugin-oriented architecture.

These developments have made me even more interested in research around reliable autonomous software engineering and evaluation. If you still see a possible supervision fit, could I ask what the next concrete step would be on your side, and how the funding / scholarship / RA or TA structure would normally work for a PhD student in your group?

Best regards,
Zhiheng Zhang

## Send checklist

- [ ] Fill Concordia Student ID in each new-contact email.
- [ ] Attach latest CV.
- [ ] Attach UBC + Melbourne transcripts in the form Concordia expects.
- [ ] Refresh each supervisor's recruitment page on send day.
- [ ] Send individually, not CC/BCC batch.
- [ ] Log `sent_at`, subject, attachments and response state in the repo.
- [ ] Do not claim Boss Phase 07 is complete until its own acceptance condition passes.
