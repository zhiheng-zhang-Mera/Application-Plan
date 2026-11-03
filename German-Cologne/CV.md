# Zhiheng Zhang

zhiheng0mera@gmail.com

Academic Curriculum Vitae | PhD Applications, Fall 2027

## Research Interests

Reliable multi-agent software systems; trustworthy verification of agent execution and completion claims; evidence-qualified acceptance under incomplete observation; persistent execution, failure recovery, and reproducible evaluation.

## Education

### University of Melbourne, Australia

Master of Computer Science | 2025-present; expected completion December 2026

Two-year program: one year of coursework followed by one year of research. Research supervisor: Professor Richard Sinnott. Master's research concerns Android privacy evidence; final results and degree completion are pending.

### University of British Columbia, Okanagan campus, Canada

Bachelor of Science in Computer Science | 2020-2024; degree awarded 2024

Capstone Software Engineering Project (COSC 499): 93/100.

## Preprints and Manuscripts

1. **Zhiheng Zhang.** **Omission-Safe Conditional Contracts for Evidence-Closed CI Qualification.** 2026. arXiv preprint, arXiv:2610.39241 [cs.SE].
   Developed source-derived CI qualification contracts and an independent certificate checker to prevent missing observations from silently weakening evidence requirements. Research based on DS-Hns.

2. **Zhiheng Zhang.** **Architectural Debt Enforcement under Incomplete Observation: A Controlled Study of Ratchets and Evidence Qualification.** 2026. arXiv preprint, arXiv:2610.41276 [cs.SE].
   Evaluated evidence-qualified architectural debt enforcement on 240 source files and 480 constructed scenarios, examining identity-aware ratchets, observation uncertainty, and provenance binding. Research based on Codex Boss (Boss-A2).

## Research and Systems Experience

### Utopia | Independent systems project


- Led architecture, AI-assisted implementation and integration of a multi-agent system combining persistent task execution with evidence-based acceptance.
- Integrated two physical Windows execution workers with Android and web control interfaces, explicit target-device routing, and inspectable cross-host results.
- Maintained failure histories, task-to-evidence links, and replay records to support debugging and reproducible evaluation.
- Completed and froze the integrated successor to DS-Hns and Codex Boss.

### Privacy Lens | Master's research


- Worked on an offline Android privacy-evidence prototype and a curated reproducibility artifact under Professor Richard Sinnott's supervision.
- Organized evidence admission, metric checks, and claim-to-evidence traceability, distinguishing observations from interpretations that require human review.
- Worked with a TypeScript/React Native/Expo application and a Kotlin native layer.

### DS-Hns | Persistent coding-task execution


- Designed durable checkpoints and resume checks around workspace state, repository identity, and unfinished effects before interrupted tasks continue.
- Used controlled interruption scenarios to distinguish committed-progress recovery from effect/checkpoint gaps that can still cause duplicate actions.
- Completed and froze the runtime; subsequently developed the CI evidence-qualification study listed above.

### Codex Boss | Multi-agent orchestration


- Developed multi-agent workflow orchestration around persistent task contracts, bounded recovery, and deterministic acceptance checks.
- Separated agent-reported completion from host-observed execution evidence, making completion claims subject to explicit acceptance checks; subsequently integrated this work into Utopia.
- Completed and froze the platform; subsequently studied architectural debt enforcement and observation uncertainty in Boss-A2.

## Technical and Research Practice

- Systems architecture: task lifecycles, interface contracts, durable state, failure handling, and multi-device integration.
- Evaluation: reproducible task scenarios, controlled fault injection, trace inspection, recovery/replay analysis, and evidence-backed acceptance.
- Software practice: JavaScript/Node.js, TypeScript, React Native/Expo, Kotlin/Jetpack Compose, Git/GitHub, and AI-assisted implementation with explicit review.
- Research development: problem formulation, experiment design, artifact organization, and technical documentation.

## Selected Academic Preparation

Software Engineering; Capstone Software Engineering Project; Research Methods; Analysis of Algorithms.

## Proposed Doctoral Focus

I aim to study how interacting AI agents can produce outcomes that remain verifiable when observations are incomplete, execution is interrupted, or deployment conditions change. My proposed focus is on evidence-aware coordination and acceptance: determining when available observations justify a completion claim, when agents should seek additional evidence, and when a system should defer acceptance or recover. I would evaluate these mechanisms through controlled failures, traceable execution records, and reproducible multi-agent tasks. This systems-oriented direction connects to the Cologne group's interest in trustworthy AI and interacting agents; statistical or formal guarantees are a doctoral research objective, not a claimed result of my existing platforms.
