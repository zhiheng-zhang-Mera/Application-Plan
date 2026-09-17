# Hong Kong Outreach Drafts — 2026-09-17

> Individual drafts under the current screening gates. **Yu Pei / Heqing Huang / Yu Li / Nan Guan are send-ready after one same-day recruitment-page refresh.** Zhisong Zhang needs exact 2027-capacity refresh. HKU drafts are prepared but blocked by the current bachelor-honours/equivalency gate.
>
> Project claims remain conservative. Codex Boss Phase 07 semantic acceptance is **not** described as complete: the current branch rejects a vacuous case, while a meaningful case still exposes a false-negative; regression is 2,508 unit tests across 215 files plus typechecking.

## Common attachments / links

Attach where appropriate:
- latest CV
- UBC transcript + current Melbourne transcript
- short research-interest note if requested

Repositories:
- Codex Boss: https://github.com/zhiheng-zhang-Mera/Codex-Boss
- DS-Hns: https://github.com/zhiheng-zhang-Mera/DS-Hns

---

# First Hong Kong wave

## 1. Yu Pei — PolyU

**To:** `csypei@comp.polyu.edu.hk`  
**Subject:** Prospective PhD student — autonomous program repair and reliable coding-agent evaluation

Dear Professor Pei,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing PhD applications for 2027.

Your research on automated program repair, software testing, fault localization and mining software repositories is very close to the problems I am encountering in two systems I am building. **DS-Hns** is a long-horizon software-work harness with durable task state, scheduling, explicit task lifecycle, failure isolation and recovery-oriented execution. **Codex Boss** coordinates multiple AI workers and evaluates whether their outputs provide meaningful evidence of task completion.

A concrete issue I am working on now is that an autonomous coding agent can generate a test that looks plausible while still providing weak evidence that the intended behavior was repaired. Boss’s current semantic-acceptance work rejects a vacuous case, while a genuinely meaningful case has exposed a false-negative that I am fixing rather than masking; the current branch runs 2,508 unit tests across 215 files.

I would like to study this problem more systematically as **repair validation for autonomous coding agents: test adequacy, regression-aware acceptance, failure localization and empirical evaluation on real repositories**.

I saw that you are currently looking for PhD students. Would this direction be a possible fit for your group?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Routing note

Lead with DS-Hns + the real semantic-acceptance failure mode. Keep this about repair/testing/evidence, not generic LLM agents.

---

## 2. Heqing Huang — CityUHK

**To:** `heqhuang@cityu.edu.hk`  
**Subject:** Prospective PhD student — secure and reliable autonomous coding agents

Dear Professor Huang,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing a 2027 PhD application to CityUHK.

I am particularly interested in your work on software security and reliability, program analysis and fuzzing, and I noticed your recent work on performance vulnerabilities in AI agents. These topics overlap directly with problems emerging from my current projects. **DS-Hns** is a long-horizon software-work harness with explicit capability boundaries, durable task state, failure isolation and recovery; **Codex Boss** is a multi-agent orchestration and evidence-based acceptance platform.

The research direction I would like to pursue is how to make tool-using coding agents **secure and verifiably reliable on real repositories**: combining program-analysis/testing signals with runtime traces to detect unsafe actions, constrain tool capabilities, validate patches and recovery decisions, and distinguish meaningful completion evidence from superficially plausible outputs.

Would you be open to discussing whether this direction could fit a PhD project in your group?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Routing note

Use security/reliability + program analysis as the main research bridge. Privacy Lens can be mentioned later if the discussion moves toward permission/audit surfaces.

---

## 3. Yu Li — CUHK

**To:** `liyu@cse.cuhk.edu.hk`  
**Subject:** Prospective 2027 PhD student — scientific agents and computational health workflows

Dear Professor Li,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing an application to the CUHK CSE PhD programme for 2027.

I was interested in your group’s work across machine learning, healthcare and bioinformatics, especially recent projects that combine multimodal learning and LLM agents for biomedical or drug-mechanism analysis. My main project, **Codex Boss**, is a multi-agent orchestration and evaluation platform designed to coordinate planning, evidence gathering, critique and acceptance across long-running tasks. I have also been prototyping computational health/simulation ideas, which have made me interested in using agent systems for scientific workflows rather than only software-engineering automation.

The research direction I would like to explore is **trustworthy scientific agents for computational health**: agents that can synthesize heterogeneous evidence, propose and revise hypotheses or experiment plans, interact with simulation/data-analysis tools, and provide inspectable evidence for their conclusions instead of merely generating plausible narratives.

Would this be close enough to your current research agenda to discuss as a possible PhD direction?

I have attached my CV and transcripts. Project repository:
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Routing note

This is the AI4Science route. Do not force DS-Hns into the opening; Boss + scientific-workflow/evidence evaluation is the cleaner story.

---

## 4. Nan Guan — CityUHK

**To:** `nanguan@cityu.edu.hk`  
**Subject:** Prospective PhD student — LLM-aided system design and reliable long-horizon agents

Dear Professor Guan,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing a 2027 PhD application to CityUHK.

I saw that you are recruiting PhD students for **LLM-aided System Design**, and I was particularly interested in the systems side of this direction. My project **DS-Hns** is a long-horizon software-work harness with durable task state, ordered/scheduled execution, hardware-adaptive concurrency, explicit lifecycle tracking, failure isolation and recovery. **Codex Boss** adds multi-agent planning and evidence-based acceptance on top of a durable state/event architecture.

I would like to study how LLM agents can assist system design and analysis while preserving **traceable state, explicit evidence, predictable recovery and system-level constraints**. In particular, I am interested in tool-using agents that interact with mechanized analysis or verification components, and in evaluating when agent assistance improves engineering throughput without silently weakening correctness or timing/reliability guarantees.

Would this systems-oriented direction be a possible fit for your current LLM-aided System Design PhD openings?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Routing note

Frame DS-Hns as systems/runtime evidence, not a desktop tool. Avoid implying a preference for the theory-heavy subtrack; explicitly target system implementation and empirical evaluation.

---

## 5. Zhisong Zhang — CityUHK

> **Refresh exact 2027 capacity before sending.** The current CityU profile says Accepting PhD Students, but the personal recruiting page still contains 2026 intake wording.

**To:** `zhisong.zhang@cityu.edu.hk`  
**Subject:** Prospective PhD student — long-context agent systems and long-horizon memory/evaluation

Dear Professor Zhang,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing PhD applications for 2027.

Your work on long-context language models and LLM-based agent systems is closely related to a problem I am exploring in **Codex Boss**, a multi-agent orchestration and evaluation platform. Boss now has durable state/event infrastructure, a knowledge/data lifecycle, capability boundaries and an acceptance layer for long-running work. As tasks become longer, the difficult problem is no longer simply “give the model more context”, but deciding **what state should persist, what can be compressed or forgotten, how agents share memory without propagating errors, and how the system evaluates claims produced after many steps or multiple agents**.

I would like to study long-horizon agent systems through questions around **context/memory management, state drift, cross-agent information sharing and empirical evaluation against strong single-agent baselines**.

Are you currently considering new PhD students for 2027, and would this direction be relevant to your group?

I have attached my CV and transcripts. Repository:
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

---

# HKU — drafts prepared, but blocked by academic-equivalency gate

> Current HKU CS/CDS admission language normally requires a bachelor's degree with honours or equivalent. Until the UBC route is documented as satisfying that condition, these drafts are **not send-ready** under the repo's hard-gate rules.

## Zuming Jiang

**To:** `jzuming.hku@gmail.com`  
**CC/official address for records only:** `jzuming@hku.hk`  
**Subject:** Prospective PhD student — testing and reliability of autonomous software systems

Dear Professor Jiang,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC. I am interested in your current PhD openings across systems, security, databases and AI applications.

My project **DS-Hns** is a long-horizon software-work harness with persistent task state, explicit lifecycle tracking, failure isolation and recovery. **Codex Boss** adds multi-agent orchestration and evidence-based acceptance. The problem I am most interested in is how autonomous software agents should be tested and validated when they operate across long repository tasks: patches may appear plausible, generated tests may be weak, and recovery from partial failure can itself introduce new states that need verification.

Your work on systems testing/fuzzing and reliability makes me interested in research combining **agent execution traces, fuzzing/testing signals and semantic acceptance** for real systems software or distributed-system workloads.

Would you be open to discussing whether this could fit one of your current PhD directions?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

---

## Ka Ho Chow

**To:** `kachow@cs.hku.hk`  
**Subject:** Prospective PhD student — trustworthy agent systems, capability boundaries and LLM security

Dear Professor Chow,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC. I saw that your group currently has several PhD openings, and I am interested in your work on trustworthy AI systems, cybersecurity, ML systems and LLM security.

My current projects approach trustworthy agents from the systems side. **DS-Hns** runs long-horizon software tasks with explicit capability boundaries, failure isolation and recovery, while **Codex Boss** coordinates multiple AI workers and validates whether their outputs provide sufficient evidence for task completion. I am also interested in privacy/auditability through a separate Privacy Lens project.

The PhD questions I would like to explore include **security of tool-using agents, capability/permission design, adversarial or misleading agent outputs, and runtime/evidence mechanisms that prevent an autonomous system from turning a model mistake into an unsafe action**.

Would this systems-and-security direction be relevant to your current PhD openings?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

---

## Heming Cui

**To:** `heming@cs.hku.hk`  
**Subject:** Prospective PhD student — reliable distributed AI runtime and long-horizon execution

Dear Professor Cui,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC. I am interested in your work on distributed AI training/serving and reliable, secure systems, and I saw that you recruit systems-relevant PhD students regularly.

My main engineering project **DS-Hns** is a long-horizon software-work runtime with durable task state, scheduling, hardware-adaptive concurrency, explicit task lifecycle, isolated extensions and failure recovery. **Codex Boss** provides a higher-level multi-agent orchestration layer with durable events and acceptance/verification.

I would like to turn these systems into research around **reliable distributed AI/agent runtimes: state persistence and recovery, resource-aware execution, failure containment, reproducible long-running tasks and verification of terminal state**. I am especially interested in work where these mechanisms are evaluated as systems infrastructure rather than as an application-layer agent demo.

Would this be relevant to the systems directions in your group?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

---

# Not drafted for immediate send

## Hongxia Yang — PolyU

- Email: `hongxia.yang@polyu.edu.hk`
- Explicit fully-funded PhD recruitment and excellent GenAI/agentic fit.
- Current recruitment process requires a **coding test** followed by a **presentation**.
- Under the current low-friction preference, keep as BACKUP rather than spending an outreach slot now.

## Jing Li — PolyU

- Email: `jing-amelia.li@polyu.edu.hk`
- Explicitly open to PhD applicants.
- Good NLP/reasoning/agent fit, but less direct than the first-wave DS-Hns/Boss matches. Keep as second wave.

---

# Send checklist

- [ ] Refresh each PI's recruitment/capacity page on send day.
- [ ] Attach latest CV and transcripts.
- [ ] Keep emails individual; no CC/BCC batch.
- [ ] Do not claim scholarship/funding is guaranteed unless the PI/programme says so specifically.
- [ ] Do not claim Boss Phase 07 is complete.
- [ ] For Zhisong Zhang, confirm exact 2027 intake wording before sending.
- [ ] Do not send HKU drafts until the bachelor-honours/equivalency gate is resolved.
- [ ] Log `sent_at`, subject, attachments and reply state in the application repo.
