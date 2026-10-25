# Evidence-grounded recovery for authorized agent workflows

Research-fit statement | Jun Yan

zhiheng0mera@gmail.com | Melbourne, Australia | Fall 2027

Concordia application/student ID: 20814667 | Doctor of Philosophy - Computer Science

International applicant; neither a Canadian citizen nor a permanent resident.

## Motivation and fit

Your research on agentic/autonomous systems, trustworthy intelligence and resilient cyber-physical infrastructure provides a concrete setting for studying recovery decisions. I am especially interested in the point where an agent's plan becomes an action whose effect must be checked. I would start with software and a simulated IoT endpoint, then adapt the study to an existing lab platform rather than assume expertise in power-system modeling.

## Proposed research question

When an agent loses contact with an execution endpoint, what evidence is sufficient to decide whether to retry, wait, ask for authorization, or stop without duplicating an effect or accepting a false success?

## Preparation I can bring

I led architecture, AI-assisted integration and evidence-backed acceptance of Utopia, a completed and frozen multi-device system. Its bounded records cover two Windows execution workers, Android/Web control, fault/replay histories and independently inspectable results. My Android privacy-evidence research provides additional experience in separating observed signals from stronger claims. These artifacts are a starting point for research, not substitutes for a controlled scientific evaluation.

## Initial method

Represent each consequential step with an authorization scope, state version, expected postcondition and evidence receipt. A recovery controller would compare current observations with the last committed action before choosing a bounded response. The first prototype would use the frozen Utopia baseline and a small set of benign desktop tasks, with an explicitly simulated IoT endpoint. The study would separate faults in execution, state observation and memory summarization. It would not require a new foundation model or claim that natural-language plans are formally safe.

# Evaluation and feasible starting scope

Jun Yan | Evidence-grounded recovery for authorized agent workflows

## 1. Interrupted execution

Inject worker disconnects, delayed acknowledgements and crashes after an effect but before its receipt. Compare retry-on-timeout, checkpoint replay and evidence-grounded recovery. Measure verified completion, duplicate effects, false-success reports and recovery-time distributions.

## 2. Changing authorization

Revoke or narrow a task permission while observations are stale. Measure prohibited-action attempts, correct escalation and unnecessary interruptions, with the permitted task outcome fixed before each trial.

## 3. Longer task histories

Compare full history, ordinary summaries and provenance-preserving summaries. Measure retention of permissions and unresolved actions, completion rate, token cost and recovery latency.

## First 12 weeks after project agreement

Weeks 1-3: reproduce selected Utopia runs, define a fault model and agree operational invariants. Weeks 4-7: build baseline recovery policies and an injection harness. Weeks 8-12: run repeated campaigns, audit negative cases and assess whether an IoT/digital-twin extension is justified.

## Scope and evidence boundaries

The energy/IoT application is proposed, not existing experimental evidence. I have not validated physical power-grid control, production high availability, or unrestricted LLM autonomy. I would scope the thesis around a measurable reliability mechanism and acquire the necessary domain background with the group.

## Selected sources and artifacts

Current research directions

Utopia implementation and bounded acceptance evidence

Prepared 25 October 2026. Proposed experiments are not completed results. Topic and supervision arrangements remain open for discussion.

## Source and project links

- <https://sites.google.com/view/jyan/home>

- <https://github.com/zhiheng-zhang-Mera/utopia>
