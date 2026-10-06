# Short Description of Research Problems

## 1. State-aware analysis for long-running coding agents

Most coding-agent evaluation focuses on the final patch or task outcome. In a long-running repository workflow, however, important failures can occur much earlier: stale assumptions, partially applied edits, incorrect recovery after restart, or a trajectory that remains locally plausible while drifting away from the intended repository state.

I would like to study program-analysis signals that can be exposed during the agent's execution rather than only after completion. The goal is to detect when the evolving repository state becomes inconsistent with task intent, test expectations, dependency structure, or previously established invariants. Such signals could be used to stop, redirect, or require additional evidence from the agent before more changes accumulate.

## 2. Evidence-preserving recovery for autonomous software work

Restart and retry mechanisms can make an agent process robust while still corrupting the semantics of the engineering task. A recovered process may duplicate work, lose the reason behind an earlier decision, or satisfy a weak terminal condition.

I am interested in combining explicit task-state persistence with program-analysis and testing evidence so that recovery can be judged by repository correctness, not merely by process liveness. This could be evaluated on real multi-step maintenance tasks with controlled interruption, replay, and comparison of alternative recovery policies.

My current DS-Hns and Codex Boss projects provide a systems substrate for these experiments, but the research contribution I would pursue is the analysis/evaluation method rather than the existing platform itself.
