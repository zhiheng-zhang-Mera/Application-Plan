# Daily Outreach Pack — 2026-09-22

> Generated together with `targets/CONTACT-POOL-2026-09-22.md`.
>
> **Contract:** a candidate needs (1) a publicly verified direct supervisor email, (2) a current route that permits direct contact, and (3) a non-pure-theory research route. Failure on any gate deletes the candidate from outreach surfaces. Only then may this file generate the individualized body and material package. Refreshing the pool must regenerate this file rather than reusing an old body unchanged.

## Common material base

Use only what the target asks for. Do not attach everything by default.

- Transcript on repo: [Documents/Transcript-ZhihengZhang.pdf](../Documents/Transcript-ZhihengZhang.pdf)
- Research-CV mother template: [CV-generate/template/research-cv-template.tex](../CV-generate/template/research-cv-template.tex)
- Project-positioning guardrails: [materials/project-positioning.md](../materials/project-positioning.md)
- Research profile: [materials/research-profile.md](../materials/research-profile.md)
- Codex Boss: https://github.com/zhiheng-zhang-Mera/Codex-Boss
- DS-Hns: https://github.com/zhiheng-zhang-Mera/DS-Hns
- Quant-Ultra: https://github.com/zhiheng-zhang-Mera/Quant-ultra

> Current repo does **not** yet contain candidate-specific PDF CVs for today's five. Material-package rows therefore distinguish the generated body from the CV-PDF state instead of pretending a PDF exists.

---

## 1. Jocelyn Qiaochu Chen — University of Alberta

**To:** `jocelyn.chen@ualberta.ca`  
**Subject:** Prospective Student — reliable AI-assisted programming and coding-agent verification

Dear Professor Chen,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing PhD applications for 2027.

I was particularly interested in your work on AI-assisted programming, program synthesis, formal methods, and abstractions for reasoning about programs and language models. These topics connect closely to problems emerging from two systems I am building. **DS-Hns** is a long-horizon software-work runtime with durable task state, scheduling, failure isolation and recovery; **Codex Boss** coordinates multiple AI workers and evaluates whether the evidence they produce is sufficient to accept a task as complete.

A research problem I would like to study more rigorously is how AI-assisted programming systems can combine **generation with verification**: using program-analysis, synthesis, testing or formal evidence to distinguish genuinely correct repairs and implementations from outputs that merely look plausible or pass weak tests. I am especially interested in implementation- and experiment-led work where these methods are evaluated on real repository tasks.

I also noticed your note about prior research training for direct PhD applicants. My current master’s includes a research component, and I would be happy to clarify its scope and provide my thesis/research materials if useful. Would my background and this direction be appropriate to discuss for your upcoming fully funded PhD openings?

I have attached my CV and transcript. Relevant repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,  
Zhiheng Zhang

### Material package

- **Body:** this section.
- **Attach:** [tailored CV source](../CV-generate/ualberta-jocelyn-chen.tex) → compile to PDF before send + [transcript](../Documents/Transcript-ZhihengZhang.pdf).
- **Links in body:** DS-Hns + Codex Boss.
- **Do not claim:** that formal verification is already implemented in Boss/DS-Hns; frame it as the proposed research bridge.
- **CV state:** `SOURCE_GENERATED / PDF_PENDING`.

---

## 2. Ka Ho Chow — University of Hong Kong

**To:** `kachow@cs.hku.hk`  
**Subject:** Prospective PhD student — trustworthy agent systems, capability boundaries and LLM security

Dear Professor Chow,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing PhD applications for 2027.

I saw that your group currently has several PhD openings, and I am interested in your work on trustworthy AI systems, cybersecurity, ML systems and LLM security. My current projects approach trustworthy agents from the systems side. **DS-Hns** runs long-horizon software tasks with durable state, failure isolation and recovery, while **Codex Boss** coordinates multiple AI workers and evaluates whether their outputs provide sufficient evidence for task completion. I have also explored privacy and auditability questions through a separate Privacy Lens project.

The research direction I would like to pursue is **security and reliability for tool-using autonomous agents**: capability and permission design, containment of unsafe actions, adversarial or misleading agent outputs, runtime evidence, and mechanisms that prevent a model mistake from being converted directly into a system-level action.

Would this systems-and-security direction be relevant to the current PhD openings in your group?

I have attached my CV and transcript. Relevant repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,  
Zhiheng Zhang

### Material package

- **Body:** this section.
- **Attach:** [tailored CV source](../CV-generate/hku-ka-ho-chow.tex) → compile to PDF before send + [transcript](../Documents/Transcript-ZhihengZhang.pdf).
- **Links in body:** DS-Hns + Codex Boss.
- **Supporting narrative:** Privacy Lens only as secondary evidence; do not turn the opening into a generic privacy/compliance pitch.
- **CV state:** `SOURCE_GENERATED / PDF_PENDING`.

---

## 3. Keval Vora — Simon Fraser University

**To:** `keval@sfu.ca`  
**Subject:** Prospective PhD student — reliable long-running AI systems and software runtime infrastructure

Dear Professor Vora,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing PhD applications for 2027.

I am interested in your work on scalable and data-intensive systems, software infrastructure, and performance. My current project **DS-Hns** is a long-horizon software-work runtime with durable task state, ordered and scheduled execution, hardware-adaptive local concurrency, explicit task lifecycle, extension-failure isolation and restart/recovery-oriented operation. **Codex Boss** sits above that runtime as a multi-agent orchestration and acceptance layer.

The systems question I would like to develop into PhD research is how long-running AI/agent workloads should be engineered as **reliable systems rather than short-lived model calls**: persistent state, resource-aware scheduling, failure containment, recovery, reproducibility and measurable completion semantics. I am particularly interested in building and evaluating these mechanisms under realistic workloads and comparing their performance/reliability trade-offs.

Your open-positions page asks prospective graduate students to send a brief description of their research interests with a CV, so I wanted to ask whether this systems direction could fit current work in your group.

I have attached my CV. Relevant repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,  
Zhiheng Zhang

### Material package

- **Body:** this section; it doubles as the requested brief research-interest description.
- **Attach:** [tailored CV source](../CV-generate/sfu-keval-vora.tex) → compile to PDF before send. Transcript is **not default** unless requested.
- **Links in body:** DS-Hns + Codex Boss.
- **Lead project:** DS-Hns; Boss is supporting orchestration/evaluation infrastructure.
- **CV state:** `SOURCE_GENERATED / PDF_PENDING`.

---

## 4. Marco Canini — KAUST

**To:** `marco@kaust.edu.sa`  
**Subject:** Prospective PhD student — reliable distributed systems for long-running AI/agent workloads

Dear Professor Canini,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing a Fall 2027 PhD application to KAUST.

I am particularly interested in the SANDS group’s work on distributed and cloud systems and systems support for AI/ML. My current project **DS-Hns** is a runtime for long-horizon autonomous software work, with durable task state, scheduling, hardware-adaptive concurrency, failure isolation and restart/recovery mechanisms. **Codex Boss** provides a higher-level multi-agent orchestration and evidence-based acceptance layer.

I would like to study how long-running AI and agent workloads can be supported by **reliable distributed infrastructure**: state persistence and recovery, resource-aware execution, fault containment, reproducibility, and mechanisms for determining when a distributed autonomous workflow has actually reached a valid terminal state. I am interested in systems implementation and empirical evaluation rather than treating orchestration as only an application-layer prompt problem.

Would this direction be potentially relevant to current PhD work in SANDS? I am also preparing the formal KAUST application and would not treat a supervisor reply as a substitute for the admissions process.

I have attached my CV and transcript. Relevant repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,  
Zhiheng Zhang

### Material package

- **Body:** this section.
- **Attach:** [tailored CV source](../CV-generate/kaust-marco-canini.tex) → compile to PDF before send + [transcript](../Documents/Transcript-ZhihengZhang.pdf).
- **Links in body:** DS-Hns + Codex Boss.
- **Route:** systems/runtime first; avoid generic “multi-agent AI” framing.
- **CV state:** `SOURCE_GENERATED / PDF_PENDING`.
- **Separate action:** formal KAUST Fall 2027 application remains required.

---

## 5. Dongxia Wu — MBZUAI — ATLAS Lab

**To:** `dongxia.wu@mbzuai.ac.ae`  
**Subject:** Zhiheng Zhang — PhD — Foundation Models & Agents / AI for Science — ATLAS Lab Application

Dear Professor Wu,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing PhD applications for Fall 2027.

I saw that the ATLAS Lab is recruiting Fall 2027 PhD students and that you explicitly welcome applications by email. Among the directions listed on your page, I am most interested in **Foundation Models & Agents** and **AI for Science**, especially where the work is driven by system building, simulation/data workflows, rigorous evaluation and reproducibility.

My main project, **Codex Boss**, is a multi-agent orchestration and evidence-based acceptance platform for long-running tasks. **DS-Hns** is a long-horizon software-work runtime with durable state, scheduling, failure isolation and recovery. These projects have made me interested in a broader research question: how scientific agents should combine tools, persistent state, evidence, uncertainty and explicit acceptance criteria so that long-running research workflows remain auditable rather than merely plausible.

For your group, I would like to explore **trustworthy scientific agents and reproducible AI-for-science workflows**: agents that can coordinate simulation or data-analysis steps, preserve experiment state, expose evidence for intermediate decisions, and be evaluated on reproducibility and failure modes. I would prefer this systems/agent/evaluation route rather than a pure probabilistic-modeling or optimization-theory project.

Would this direction be relevant to your Fall 2027 PhD recruitment?

I have attached my CV and academic transcript. Relevant repositories:
- https://github.com/zhiheng-zhang-Mera/Codex-Boss
- https://github.com/zhiheng-zhang-Mera/DS-Hns

Best regards,  
Zhiheng Zhang

### Material package

- **Body:** this section.
- **Attach:** [tailored CV source](../CV-generate/mbzuai-dongxia-wu.tex) → compile to PDF before send + [transcript](../Documents/Transcript-ZhihengZhang.pdf).
- **Links in body:** Codex Boss + DS-Hns.
- **Selected route:** Foundation Models & Agents / AI for Science; do **not** pitch the probabilistic-ML or combinatorial-optimization lines as the main PhD route.
- **Research-method gate:** systems/agents/evaluation/data-workflow route only; pure algorithm/theory route is excluded.
- **CV state:** `SOURCE_GENERATED / PDF_PENDING`.

---

## Send / submit gate

Before changing any row from `READY` to `SENT` / `SUBMITTED`:

- [x] public direct supervisor email exists and is verified from an official/public source;
- [x] advertised route permits direct email/contact and is not internal-form/portal-only;
- [x] proposed research route is systems/empirical/applied rather than pure algorithm/theory;
- [ ] recruitment/capacity page re-opened on send day;
- [x] individualized body/form text exists in this daily pack;
- [ ] candidate-specific CV PDF exists if the target requests a CV;
- [ ] requested transcript/supporting material attached;
- [ ] links and project claims checked against `materials/project-positioning.md`;
- [ ] no unsupported publication, funding, formal-method, benchmark or completion claim;
- [ ] event is logged in `applications/OUTREACH-LOG.md` after actual send/submission.
