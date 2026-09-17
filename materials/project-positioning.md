# Project Positioning Router

| Supervisor / program theme | Lead project | Supporting project | Avoid |
|---|---|---|---|
| Agentic AI / multi-agent / LLM systems | Codex Boss | DS-Hns | forcing finance into the opening |
| Software Engineering / coding agents / computer use | DS-Hns | Codex Boss, Privacy Lens | presenting automation as just a GUI tool |
| Financial ML / optimization / data systems | Quant-Ultra | Codex Boss | leading with trading profit/win-rate claims |
| Trustworthy AI / privacy / governance | Privacy Lens | Boss / DS-Hns | treating Privacy Lens as unrelated compliance work |
| AI for Science / autonomous research | Codex Boss | domain simulators / DS-Hns | overcommitting to one application domain |

## Rule of thumb

Use **problem → research question → project evidence → next research step**. Do not use **project list → feature dump → performance bragging** as the application narrative.

## Current reusable evidence — 2026-09-17

### Codex Boss

Use for: multi-agent orchestration, agent evaluation, evidence-based acceptance, autonomous research/software workflows.

Current public development evidence:

- platform-foundation work now spans durable state/events, capability security/plugins, knowledge/data lifecycle, scale/soak verification, dogfooding and semantic acceptance;
- current semantic-acceptance work has an intentionally unresolved false-negative: a vacuous case is rejected, while a genuinely meaningful case still exposes a reader limitation;
- do **not** claim the current semantic-acceptance phase is complete;
- current regression at the relevant branch: **2,508 unit tests / 215 files** plus Electron/renderer/test typechecking.

Best research framing:

> How can autonomous/multi-agent systems distinguish genuine task completion from plausible but weak evidence, while remaining useful on long-running real workflows?

### DS-Hns

Use for: AI4SE, coding agents, autonomous software maintenance, AIOps, reliability, long-horizon execution.

Current public engineering evidence:

- official DeepSeek Harness UI kept as the canonical surface, with optional capabilities isolated as extensions rather than injected into the core;
- ordered and scheduled task queues;
- hardware-adaptive local concurrency;
- unified task lifecycle and terminal events;
- task history / terminal notification handling;
- extension-failure isolation;
- idempotent Windows installer and explicit optional-plugin flow.

Best research framing:

> How should long-horizon software agents persist state, recover from failures, schedule work and prove that a repository-level task is actually complete?

### Combined Boss + DS-Hns

For AI4SE supervisors, the strongest combined story is:

1. **DS-Hns executes** long-running software work and exposes lifecycle/recovery/operational traces.
2. **Codex Boss orchestrates and evaluates** multi-agent work and acceptance evidence.
3. The PhD research question is not “build another agent UI”; it is **reliability + verification + empirical evaluation of autonomous software engineering over real repositories**.

This is the default route for the 2026-09-17 Concordia outreach batch.
