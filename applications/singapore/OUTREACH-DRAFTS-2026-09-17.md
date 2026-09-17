# Singapore Outreach Drafts — 2026-09-17

> Individual drafts under the current screening gates. **SUTD 1–4 are send-ready after one final recruitment-page refresh.** NUS/NTU drafts are conditional on their programme gates below.
>
> Project claims are deliberately conservative: Codex Boss Phase 07 semantic acceptance is **not** described as complete. The current branch rejects a vacuous case but still exposes a false-negative on a meaningful case; regression is 2,508 unit tests across 215 files plus typechecking.

## Common attachments / links

Attach where appropriate:
- latest CV
- UBC transcript + current Melbourne transcript
- optional one-page research-interest note if the professor asks for one

Repositories:
- Codex Boss: https://github.com/zhiheng-zhang-Mera/Codex-Boss
- DS-Hns: https://github.com/zhiheng-zhang-Mera/DS-Hns

---

# SUTD — first wave

## 1. Thanh Le-Cong

**To:** `congthanh_le@sutd.edu.sg`  
**Subject:** Prospective Jan 2027 PhD student — reliable coding agents and AI-enabled software engineering

Dear Professor Le-Cong,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing an application for the SUTD ISTD PhD programme for January 2027.

I saw the current PhD opportunity in your group on **reliable and secure software engineering with and for AI**. It is very close to the problems I am working on in two open-source systems. **DS-Hns** is a long-horizon software-work harness with durable task state, scheduling, failure isolation and recovery-oriented execution. **Codex Boss** explores multi-agent orchestration and evidence-based acceptance of agent outputs.

A concrete problem I am working on now is how to prevent an autonomous coding system from treating superficially plausible tests or outputs as sufficient evidence of completion. Boss’s current semantic-acceptance work rejects a vacuous case, while a meaningful case still exposes a false-negative that I am fixing rather than masking; the current branch runs 2,508 unit tests across 215 files. This has pushed me toward research questions around **reliable coding agents, automated debugging, repair validation, capability/security boundaries and QA for agentic software on real repositories**.

Would this direction be a reasonable fit for the advertised PhD project in your group? I would be very happy to discuss a more focused research question for the January 2027 intake.

I have attached my CV and transcripts. My project repositories are:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Routing note

Lead with **DS-Hns → reliable/secure AI4SE**; Boss is evidence/evaluation support. Do not feature UI/plugin work unless asked.

---

## 2. Ezekiel Soremekun

**To:** `ezekiel_soremekun@sutd.edu.sg`  
**Subject:** Prospective Jan 2027 PhD student — validation and testing of autonomous coding systems

Dear Professor Soremekun,

My name is Zhiheng Zhang. I am finishing a Master’s in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing a January 2027 SUTD ISTD PhD application.

Your advertised **Trustworthy Software and AI** PhD direction, especially automated testing/debugging/program analysis and validation of Code LLMs, overlaps strongly with an issue emerging from my current projects. **DS-Hns** executes and manages long-running software tasks with explicit lifecycle, failure isolation and recovery, while **Codex Boss** coordinates multiple AI workers and tries to validate whether their outputs provide meaningful evidence of task completion.

In the current Boss branch I am testing exactly the distinction I would like to study more systematically: an agent can generate a test that looks non-trivial but still fails to establish the intended behavior. The evaluator now refuses a vacuous case, but a genuinely meaningful case has exposed a false-negative rather than being silently accepted. I am interested in turning this into research on **rigorous validation of coding agents and Code LLMs: test adequacy, failure modes, regression-aware evaluation, security/robustness properties and benchmarks on real software systems**.

Would you be open to discussing whether this could fit the current PhD opportunity in your group?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Routing note

Use the real semantic-acceptance failure as the hook. This is a testing/validation email, not a generic LLM-agent pitch.

---

## 3. Ruochen (Esther) Zhao

**To:** `esther_zhao@sutd.edu.sg`  
**Subject:** Prospective Jan 2027 PhD student — trustworthy multi-agent systems and evidence-based evaluation

Dear Professor Zhao,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing an application to the SUTD ISTD PhD programme for January 2027.

I was particularly interested in your current PhD direction on **trustworthy LLM agents**, including deep-research and multi-agent evaluation, unfaithful/deceptive behavior and self-improving agent systems. My main project, **Codex Boss**, is an experimental multi-agent orchestration platform in which multiple AI workers can plan, execute, critique and adjudicate work. I am now pushing the system beyond orchestration toward a harder question: **what evidence should an autonomous agent or group of agents have to provide before the system accepts a claim that a task or research step is actually complete?**

The current implementation includes durable state, capability boundaries, knowledge/data lifecycle and acceptance/verification infrastructure. In the latest semantic-acceptance work I am deliberately testing failure cases where plausible-looking evidence should not be trusted automatically. I would like to study this at research level through **multi-agent evaluation, faithfulness and uncertainty of agent reports, adversarial/self-critique settings, and long-horizon agent behavior rather than only single-turn benchmark accuracy**.

Would this direction be close enough to the advertised PhD project in your group to discuss further?

I have attached my CV and transcripts. Project repository:
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Routing note

Boss leads. Do not turn this into a software-engineering email; frame acceptance/adjudication as trustworthy-agent evaluation.

---

## 4. Wenxuan Zhang

**To:** `wxzhang@sutd.edu.sg`  
**Subject:** Prospective Jan 2027 PhD student — reliable multi-agent collaboration and LLM systems

Dear Professor Zhang,

My name is Zhiheng Zhang. I am finishing a Master’s in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC, and I am preparing a January 2027 SUTD ISTD PhD application.

I saw the current PhD opportunity around **inclusive, efficient and trustworthy LLMs**, including safety/robustness and multi-agent collaboration. My main project, **Codex Boss**, is a multi-agent orchestration and evaluation platform. Rather than only parallelising model calls, I am interested in how multiple agents should exchange evidence, critique one another, preserve useful state and reach decisions without amplifying shared errors or accepting weak outputs.

The platform now has durable state/event infrastructure, capability boundaries, knowledge/data lifecycle and an acceptance layer. The research direction I would like to explore is **reliable multi-agent collaboration under long-horizon tasks**: how role/division-of-labour choices affect quality and cost, how evidence can be aggregated or challenged, how failures propagate across agents, and how to evaluate collaboration against strong single-agent baselines.

Would this be a plausible fit for your current PhD direction, particularly the multi-agent collaboration and trustworthy-LLM side?

I have attached my CV and transcripts. Repository:
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

### Routing note

Focus on collaboration/evaluation/reliability. Avoid selling Boss as merely a desktop orchestrator.

---

# NUS — prepared but programme remains BACKUP

## 5. Chengpeng Wang

> **Gate:** technically excellent and explicitly recruiting, but NUS remains `BACKUP` because the scholarship-equivalency condition is unresolved and the programme has scholarship interview + mandatory QE. Draft is ready; send only when this backup route is intentionally activated.

**To:** `wang-chengpeng@nus.edu.sg`  
**Subject:** Prospective PhD student — agentic software engineering and reliable coding agents

Dear Professor Wang,

My name is Zhiheng Zhang. I am completing a Master’s degree in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC. I saw that RISE Lab is currently looking for PhD students working on program analysis, agentic software engineering and agent security, and I would like to ask whether my current direction could fit the group.

I am building **DS-Hns**, a long-horizon software-work harness, and **Codex Boss**, a multi-agent orchestration and evaluation platform. A problem that has become central in the current work is how to make coding agents **prove enough about their own changes**: persistent execution and recovery are useful only if the system can also detect weak or vacuous completion evidence. The current Boss semantic-acceptance work deliberately distinguishes those cases and has exposed both a correctly rejected vacuous test and a false-negative on meaningful evidence.

The research problems I would most like to explore are **agentic software engineering with program-analysis/testing support, security of tool-using coding agents, and principled completion/repair validation on real repositories**. I am especially interested in systems where program analysis provides evidence or guardrails rather than being purely theorem/proof-oriented.

I have attached my CV as requested on the RISE Lab page. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Would this be a useful direction to discuss for a PhD position in RISE Lab?

Best regards,
Zhiheng Zhang

### Short research-problem paragraph for his requested format

> I am interested in reliable agentic software engineering for long-horizon repository tasks. In particular, I want to study how coding agents can combine program-analysis/testing signals with execution traces and explicit capability boundaries to decide whether a change is actually correct, secure and complete. My current systems work exposes a practical failure mode: agent-generated tests can appear plausible while providing weak evidence, while overly strict validators can also reject meaningful evidence. I would like to build and empirically evaluate methods that reduce both failure modes on real repositories, including repair/debugging tasks, tool-use security and recovery from partial execution failures.

---

## 6. Abhik Roychoudhury — capacity verification draft

> **Do not send as first wave yet.** Current 2026–31 Agentic AI project and technical fit are excellent, but this refresh did not find a fresh explicit PhD-opening statement. Use only after capacity is confirmed / if NUS backup is activated.

**To:** `abhik@comp.nus.edu.sg`  
**Subject:** Prospective PhD student — trustworthy autonomous software engineering and repair validation

Dear Professor Roychoudhury,

My name is Zhiheng Zhang. I am completing a Master’s in Computer Science at the University of Melbourne after a BSc in Computer Science from UBC. I have been following the current NUS work around AutoCodeRover and the 2026–31 project **Agentic AI based Software of the Future: from Scale to Trust**.

My current systems, **DS-Hns** and **Codex Boss**, approach trustworthy autonomous software engineering from the long-horizon execution and acceptance side. DS-Hns manages persistent software tasks, recovery and task lifecycle; Boss coordinates multiple AI workers and is being hardened against accepting vacuous completion evidence. The latest semantic-acceptance work has made me particularly interested in **repair validation beyond benchmark success: whether agent-generated tests actually discriminate intended behavior, how repair evidence can be checked, and how agents should recover when validation remains ambiguous**.

I would be interested in research combining autonomous repair/coding agents with testing, program analysis and empirical evaluation on real software repositories. Are you currently considering new PhD students for work connected to the Agentic AI / trustworthy-software project?

I have attached my CV and transcripts. Repositories:
- https://github.com/zhiheng-zhang-Mera/DS-Hns
- https://github.com/zhiheng-zhang-Mera/Codex-Boss

Best regards,
Zhiheng Zhang

---

# NTU — WATCH; no outbound email until academic equivalency clears

## Penghui Li — use the form, not email

> Current opening explicitly says **there is no need to email** and asks candidates to submit the form. Respect that. Official email `penghui.li@ntu.edu.sg` is stored for records only.
>
> **Gate:** NTU CCDS requires a strong Bachelor's with minimum Honours (Distinction) or equivalent. Do not submit the supervisor form until UBC equivalency is verified.

### Form-ready research-interest text

I am interested in the security and reliability of autonomous coding agents operating on real software repositories. My current project DS-Hns is a long-horizon software-work harness with durable task state, explicit capability boundaries, failure isolation and recovery; Codex Boss adds multi-agent orchestration and evidence-based acceptance. These systems have exposed a research problem I would like to study more rigorously: tool-using agents can produce plausible patches or tests while still leaving weak evidence of correctness or security. I am interested in combining program analysis, vulnerability/patch reasoning and runtime evidence to detect unsafe agent actions, validate repairs, constrain tool capabilities and recover safely from partial failures. I would especially like to evaluate such methods on real vulnerability, patch-analysis and repository-maintenance tasks rather than only synthetic prompts.

## Yewen Pu — research-only note

- Email for records: `yewen.pu@ntu.edu.sg`
- Strong fit with Boss: agent failure benchmarks, human-AI collaboration, code generation.
- No explicit current PhD opening found in this refresh + NTU academic gate unresolved.
- **No draft/send action yet.** Refresh capacity only after NTU equivalency clears.

---

# Send checklist — SUTD

- [ ] Refresh the ISTD PhD-opportunities page on send day.
- [ ] Attach latest CV and transcripts.
- [ ] Keep each email individual; no CC/BCC batch.
- [ ] Do not claim scholarship is guaranteed — SUTD in-house funding is competitive.
- [ ] Do not claim Boss Phase 07 is complete.
- [ ] Log `sent_at`, subject and reply state in the application repo.
- [ ] In parallel, start the SUTD application before the **2026-09-30** deadline; supervisor replies should not be allowed to make the formal deadline slip.
