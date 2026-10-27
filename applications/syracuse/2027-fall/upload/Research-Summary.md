# Research Summary

Zhiheng Zhang | Syracuse University CISE Ph.D. | Fall 2027

## Reliable Intelligent Software Systems

My research interest is how intelligent software can preserve an intended goal, recover from partial failures, and demonstrate that the requested outcome has actually been achieved. I am particularly interested in agent-based workflows that act across tools or devices, where a plausible explanation or a successful tool call may not establish correct end-to-end behavior.

## Preparation

My master's research at the University of Melbourne, supervised by Professor Richard Sinnott, concerns Android privacy evidence. The Privacy Lens prototype and research artifact emphasize traceable observations, reproducible checks, and bounded interpretation. My independent projects address complementary systems problems: DS-Hns investigates persistent coding-task execution and recovery; Codex Boss addresses multi-agent orchestration and evidence-based acceptance; Utopia integrates these ideas across two Windows execution workers with Android and web control. My contribution centers on architecture, AI-assisted integration, evaluation, and reviewing completion evidence.

## A Tractable Starting Study

I propose beginning with a small benchmark of benign software tasks whose final states can be independently checked. Examples include a prescribed repository edit or a local application-state update. Expected states and admissible effects would be specified before execution, with the checker validated separately from the executing agent. Controlled perturbations would include interruptions, retries, stale state, and conflicting tool reports.

- Question: When do independent outcome checks detect false completion or incorrect recovery that self-reports and log-only checks miss?
- Comparison: Hold task definitions and execution conditions fixed while comparing self-reports, log-based assertions, and state-based outcome checks.
- Measures: False-completion rate, recovery correctness, repeated effects, runtime overhead, and diagnosis effort assessed with a defined, reproducible protocol.
- Extensions: Test whether failure patterns transfer across implementations; investigate task contracts, runtime checks, or program analyses for preserving constraints during replanning.

The study would start with narrow, reproducible tasks and explicit assumptions. Subsequent experiments would separate the effect of the proposed mechanism from changes in the underlying model, tool setup, or task difficulty.

## Syracuse Fit and Flexibility

Professor Endadul Hoque's work on fuzzing, verification, and LLM-driven security analysis is relevant to systematic failure discovery. Professor Kristopher Micinski's work on logical reasoning and program analysis offers a foundation for stronger checks on software behavior. Professor Yuzhe Tang's research on software and distributed-systems security, including AI agents, provides a complementary systems perspective.

The precise question and application domain would be refined with a supervisor, using an existing research platform where appropriate. Wearable and ubiquitous computing motivate my interest in cross-device behavior; the intended contribution is a generalizable systems or analysis result.

## Selected Public Artifacts

[Utopia](https://github.com/zhiheng-zhang-Mera/utopia) | [DS-Hns](https://github.com/zhiheng-zhang-Mera/DS-Hns) | [Codex Boss](https://github.com/zhiheng-zhang-Mera/Codex-Boss) | [Privacy Lens](https://github.com/zhiheng-zhang-Mera/privacy-lens-research-artifact)
