# Research Interest — James Cheng (English, not submitted)

## Fit with the group

My research interests focus on **reliable long-horizon personal AI agents for wearable and ubiquitous computing**, especially how an authorized user goal remains intact while an agent plans, delegates, recovers and verifies results. For James Cheng's research, the most concrete bridge is evaluation, benchmarking and rubric-based reward design for LLM agents and long-horizon reasoning.

## Specific question

How evaluation can measure fidelity to a user's initial goal and verified end-to-end outcome, instead of counting plausible agent reasoning steps or incomplete tool-use traces as success?

## Research contribution and evaluation plan

I would begin by specifying a goal contract: desired final outcome, explicit action permissions, completion criteria, and which changes require human review. The agent would be permitted to replan within this contract, but would check previous results and dependencies before adopting a new plan. It would preserve failure receipts and distinguish an attempted action from an independently verifiable outcome.

Construct small suites of long-horizon tool-use tasks with hidden dependency regressions and genuine completion oracles, comparing task success, unsupported success claims and intervention rates across baseline agents.

The primary measurements would be real task success, false-completion claims, unnecessary user interruptions, recovery correctness and time-to-result. Where physical environments or differences among user needs matter, I would validate with appropriate real devices and, where applicable, ethically reviewed participants. Simulation and software tests would support but not replace real-world conclusions.

## Reusable platform, not a fixed doctoral prerequisite

Utopia, DS-Hns and Codex Boss are sources of existing engineering experience and bounded evidence. Celestial is a future extensible research-workspace concept; I am happy to adapt the research implementation to the supervisor's systems and ongoing project. My intended main contribution is software-systems reliability and empirical agent evaluation, not pure algorithms, robotics control or electronic hardware design.

## Evidence boundaries

- Utopia main: https://github.com/zhiheng-zhang-Mera/utopia/commit/944f47dd6c7e18b3388b6d769dbbb6dddbe74f00
- Research evaluation: https://github.com/zhiheng-zhang-Mera/Digital-City/blob/main/mission-book/finished/completed-2026-10-08/research-strengthening/README.md
- No claim of accepted peer-reviewed publications, fully validated wearables, automatic dual-server failover or completed consumer deployment.
