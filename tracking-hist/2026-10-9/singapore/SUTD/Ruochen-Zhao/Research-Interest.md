# Research Interest — Ruochen (Esther) Zhao (English, not submitted)

## Fit with the group

My research interests focus on **reliable long-horizon personal AI agents for wearable and ubiquitous computing**, especially how an authorized user goal remains intact while an agent plans, delegates, recovers and verifies results. For Ruochen (Esther) Zhao's research, the most concrete bridge is faithful reasoning, honest reporting and reliable self-improvement in LLM agents, particularly deep-research and multi-agent evaluation.

## Specific question

How an authorized goal and its acceptance conditions can stay stable through long tool-use episodes, and how to detect incomplete or unfaithful completion reports?

## Research contribution and evaluation plan

I would begin by specifying a goal contract: desired final outcome, explicit action permissions, completion criteria, and which changes require human review. The agent would be permitted to replan within this contract, but would check previous results and dependencies before adopting a new plan. It would preserve failure receipts and distinguish an attempted action from an independently verifiable outcome.

Develop controlled long-horizon tool-use tasks with planted dependency faults, rejected permission requests and failed subprocesses; measure goal drift, truthfulness of status reports, intervention burden and actual outcome success.

The primary measurements would be real task success, false-completion claims, unnecessary user interruptions, recovery correctness and time-to-result. Where physical environments or differences among user needs matter, I would validate with appropriate real devices and, where applicable, ethically reviewed participants. Simulation and software tests would support but not replace real-world conclusions.

## Reusable platform, not a fixed doctoral prerequisite

DS-Hns and Codex Boss are separate projects that I previously completed and froze. I subsequently integrated their work into Utopia, another completed and frozen multi-device platform with bounded validation evidence. Celestial is my planned redesign and next iteration of Utopia, not an unrelated or already completed platform. I would gladly adapt that future iteration—or its research mechanisms—to my supervisor's existing systems. My intended main contribution is software-systems reliability and empirical agent evaluation, not pure algorithms, robotics control or electronic hardware design.

## Evidence boundaries

- Utopia main: https://github.com/zhiheng-zhang-Mera/utopia/commit/944f47dd6c7e18b3388b6d769dbbb6dddbe74f00
- Research evaluation: https://github.com/zhiheng-zhang-Mera/Digital-City/blob/main/mission-book/finished/completed-2026-10-08/research-strengthening/README.md
- No claim of accepted peer-reviewed publications, fully validated wearables, automatic dual-server failover or completed consumer deployment.
