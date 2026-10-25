# State-aware confirmation and recovery in AI-assisted VR workflows

Research-fit statement | Yiming Xiao

zhiheng0mera@gmail.com | Melbourne, Australia | Fall 2027

Concordia application/student ID: 20814667 | Doctor of Philosophy - Computer Science

International applicant; neither a Canadian citizen nor a permanent resident.

## Motivation and fit

SAMIRA provides a concrete connection between my interests and Health-X: an immersive interface coordinates conversational input, inference, refinement and visualization. I am interested in the interaction problems that arise when those components respond late or disagree about current state. A first project could extend an existing lab platform rather than build a medical system from scratch, with software reliability and user correction as the principal contribution.

## Proposed research question

Can confirmation that considers both model uncertainty and application-state freshness reduce erroneous acceptance and recovery effort in AI-assisted VR workflows, compared with fixed confirmation or confidence-only warnings?

## Preparation I can bring

I led architecture, AI-assisted integration and evidence-backed acceptance of Utopia, a completed and frozen multi-device system. Its bounded records cover two Windows execution workers, Android/Web control, fault/replay histories and independently inspectable results. My Android privacy-evidence research provides additional experience in separating observed signals from stronger claims. These artifacts are a starting point for research, not substitutes for a controlled scientific evaluation.

## Initial method

Add explicit state versions, provenance-linked undo and stale-result cues to a bounded interactive task. Begin with public data and a nonclinical task; introduce delays, reordered responses, tracking interruptions and conflicting user corrections. Compare ordinary confirmation, confirmation at every step, confidence-only warnings and a state-aware policy. After a stable technical pilot, design an appropriately reviewed user study with counterbalanced conditions and a predeclared analysis. I would work with the lab on clinically meaningful task design rather than infer clinical benefit from interface metrics.

# Evaluation and feasible starting scope

Yiming Xiao | State-aware confirmation and recovery in AI-assisted VR workflows

## 1. Controlled service failures

Inject response delay, reordering and disconnection while the user's active target changes. Measure mistaken acceptance, task completion, correction count and recovery time, using fixed task-state ground truth.

## 2. Undo and diagnosis

Compare ordinary event logs, undo alone and provenance-linked recovery. Measure successful restoration, fault-localization time, repeated errors and interaction burden.

## 3. User-facing trade-offs

Subject to ethics approval, compare confirmation policies on decision accuracy, task time, perceived workload and usable task coverage. I would determine and justify the study size using a pilot.

## First 12 weeks after project agreement

Weeks 1-3: reproduce a lab-approved interaction task and identify failure points. Weeks 4-7: implement state/version cues and recovery baselines. Weeks 8-12: complete a nonclinical technical pilot and prepare an ethics/study plan if the mechanism warrants user evaluation.

## Scope and evidence boundaries

My ESP32 glove work is exploratory, not a validated custom device. Celestial Smart Glass is a research proposal, not a deployed assistant. I do not claim diagnostic-model expertise, clinical accuracy or prior patient studies. My preferred focus is interactive systems; I would confirm that this is compatible with Health-X's medical research agenda.

## Selected sources and artifacts

Official CS PhD supervision listing

SAMIRA research paper

Utopia implementation and bounded acceptance evidence

Prepared 25 October 2026. Proposed experiments are not completed results. Topic and supervision arrangements remain open for discussion.

## Source and project links

- <https://www.concordia.ca/faculty/yiming-xiao.html>

- <https://arxiv.org/abs/2505.07214>

- <https://github.com/zhiheng-zhang-Mera/utopia>
