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

> Current repo does **not** yet contain candidate-specific PDF CVs for today's three. Material-package rows therefore distinguish the generated body from the CV-PDF state instead of pretending a PDF exists.

---

## 1. Ka Ho Chow — University of Hong Kong

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

## 2. Keval Vora — Simon Fraser University

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

## 3. Xiaoxue Gao — CUHK-Shenzhen

**To:** `gaoxiaoxue@cuhk.edu.cn`  
**Subject:** Prospective PhD Student — Fall 2027 — Zhiheng Zhang

Dear Professor Gao,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing PhD applications for Fall 2027.

I saw that you are recruiting fully funded PhD students for Spring and Fall 2027, and that you welcome interested applicants to contact you directly by email. I am particularly interested in the **agentic AI, multimodal language-model, and trustworthy-AI** parts of your research.

My main project, **Codex Boss**, is a multi-agent orchestration and evidence-based acceptance platform for long-running tasks. **DS-Hns** is a long-horizon software-work runtime with durable state, scheduling, failure isolation and recovery. These projects have made me interested in how agentic systems should preserve state, coordinate tools and evidence, recover from failure, and expose enough information to evaluate whether their outputs are trustworthy.

A direction I would like to explore is **trustworthy agentic and multimodal AI systems**: evaluating robustness and safety of agents that operate across multiple modalities or tools, studying how errors propagate across long-horizon workflows, and building reproducible benchmarks or system mechanisms that make those failures observable. I would approach speech/audio as an application domain for agentic and multimodal systems rather than claim prior specialist speech-processing experience.

Would this direction be relevant to your Fall 2027 PhD recruitment?

I have attached my CV and academic transcript. Relevant repositories:
- https://github.com/zhiheng-zhang-Mera/Codex-Boss
- https://github.com/zhiheng-zhang-Mera/DS-Hns

Best regards,  
Zhiheng Zhang

### Material package

- **Body:** this section.
- **Attach:** [tailored CV source](../CV-generate/cuhksz-xiaoxue-gao.tex) → compile to PDF before send + [transcript](../Documents/Transcript-ZhihengZhang.pdf).
- **Links in body:** Codex Boss + DS-Hns.
- **Selected route:** agentic AI / multimodal LMs / trustworthy AI with systems and empirical evaluation.
- **Do not claim:** prior specialist expertise in speech/audio processing; use it as the application domain for agentic/multimodal reliability questions.
- **Program gate already checked:** the SAI programme allows prior supervisor contact; an English-medium degree satisfies the listed English requirement route.
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
