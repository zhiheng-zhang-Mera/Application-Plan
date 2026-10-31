# Zhiheng Zhang

zhiheng0mera@gmail.com | [GitHub](https://github.com/zhiheng-zhang-Mera)

Academic Curriculum Vitae | PhD Applications, Fall 2027

## Research Interests

Reliable intelligent software systems; multi-agent orchestration; software testing and program analysis; persistent agent execution, failure recovery, and evidence-based evaluation. Wearable and ubiquitous computing as application settings.

## Education

### University of Melbourne, Australia

Master of Computer Science | 2025-present; expected completion December 2026

Two-year program: one year of coursework followed by one year of research. Research supervisor: Professor Richard Sinnott. Master's research concerns Android privacy evidence; final results and degree completion are pending.

### University of British Columbia, Okanagan campus, Canada

Bachelor of Science in Computer Science | 2020-2024; degree awarded 2024

Capstone Software Engineering Project (COSC 499): 93/100.

## Preprints and Manuscripts

1. **Zhiheng Zhang.** **Omission-Safe Conditional Contracts for Evidence-Closed CI Qualification.** 2026. arXiv preprint, [arXiv:2610.39241](https://arxiv.org/abs/2610.39241) [cs.SE].
   Developed source-derived CI qualification contracts and an independent certificate checker to prevent missing observations from silently weakening evidence requirements. Research based on DS-Hns.

2. **Zhiheng Zhang.** **Architectural Debt Enforcement under Incomplete Observation: A Controlled Study of Ratchets and Evidence Qualification.** 2026. Manuscript submitted to arXiv; awaiting moderation.
   Evaluated evidence-qualified architectural debt enforcement on 240 source files and 480 constructed scenarios, examining identity-aware ratchets, observation uncertainty, and provenance binding. Research based on Codex Boss (Boss-A2).

## Research and Systems Experience

### Utopia | Independent systems project

[Implementation](https://github.com/zhiheng-zhang-Mera/utopia) | [Development and acceptance records](https://github.com/zhiheng-zhang-Mera/Digital-City)

- Led architecture, AI-assisted implementation and integration, and evidence-based acceptance of a system combining persistent task execution with multi-agent orchestration.
- Integrated two physical Windows execution workers with Android and web control interfaces, explicit target-device routing, and inspectable cross-host results.
- Maintained failure histories, task-to-evidence links, and replay records to support debugging and reproducible evaluation.
- Completed and froze the integrated successor to DS-Hns and Codex Boss.

### Privacy Lens | Master's research

[Research artifact](https://github.com/zhiheng-zhang-Mera/privacy-lens-research-artifact)

- Worked on an offline Android privacy-evidence prototype and a curated reproducibility artifact under Professor Richard Sinnott's supervision.
- Organized evidence admission, metric checks, and claim-to-evidence traceability, distinguishing observations from interpretations that require human review.
- Worked with a TypeScript/React Native/Expo application and a Kotlin native layer.

### DS-Hns | Persistent coding-task execution

[Public repository](https://github.com/zhiheng-zhang-Mera/DS-Hns)

- Designed durable checkpoints and resume checks around workspace state, repository identity, and unfinished effects before interrupted tasks continue.
- Used controlled interruption scenarios to distinguish committed-progress recovery from effect/checkpoint gaps that can still cause duplicate actions.
- Completed and froze the runtime; subsequently developed the CI evidence-qualification study listed above.

### Codex Boss | Multi-agent orchestration

[Public repository](https://github.com/zhiheng-zhang-Mera/Codex-Boss)

- Developed workflow orchestration around persistent task contracts, bounded recovery, and deterministic acceptance checks.
- Separated model-reported completion from host-observed evidence; subsequently integrated this work into Utopia.
- Completed and froze the platform; subsequently studied architectural debt enforcement and observation uncertainty in Boss-A2.

## Technical and Research Practice

- Systems architecture: task lifecycles, interface contracts, durable state, failure handling, and multi-device integration.
- Evaluation: reproducible task scenarios, controlled fault injection, trace inspection, recovery/replay analysis, and evidence-backed acceptance.
- Software practice: JavaScript/Node.js, TypeScript, React Native/Expo, Kotlin/Jetpack Compose, Git/GitHub, and AI-assisted implementation with explicit review.
- Research development: problem formulation, experiment design, artifact organization, and technical documentation.

## Selected Academic Preparation

Software Engineering; Capstone Software Engineering Project; Research Methods; Analysis of Algorithms.

## Proposed Doctoral Focus

Testing and analyzing intelligent software to determine whether it satisfies intended outcomes under interruption, retries, and changing execution conditions. Interested in combining empirical failure evidence with program analysis and runtime checks, with the specific research problem refined in collaboration with a supervisor.
