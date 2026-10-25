# Selective coordination for reliable distributed agent execution

Research-fit statement | Gengrui Zhang

zhiheng0mera@gmail.com | Melbourne, Australia | Fall 2027

Concordia application/student ID: 20814667 | Doctor of Philosophy - Computer Science

International applicant; neither a Canadian citizen nor a permanent resident.

## Motivation and fit

DISCOS's work on distributed AI infrastructure and multi-agent coordination is a direct match to the systems questions emerging from Utopia. Making CRDTs Not So Eventual motivates a useful distinction between inexpensive progress updates and operations whose ordering or invariants matter. I would investigate that distinction for an agent task ledger, treating the lab's existing protocols as research foundations rather than recreating them.

## Proposed research question

Can an agent task ledger coordinate only authorization-sensitive and externally consequential transitions while allowing ordinary progress updates to remain asynchronous, without increasing lost tasks, repeated effects or stale-permission execution under a stated failure model?

## Preparation I can bring

I led architecture, AI-assisted integration and evidence-backed acceptance of Utopia, a completed and frozen multi-device system. Its bounded records cover two Windows execution workers, Android/Web control, fault/replay histories and independently inspectable results. My Android privacy-evidence research provides additional experience in separating observed signals from stronger claims. These artifacts are a starting point for research, not substitutes for a controlled scientific evaluation.

## Initial method

Separate speculative progress from committed external effects in a versioned ledger. Start with crash/restart and network partitions; do not assume Byzantine tolerance. Compare a centralized durable baseline, eventually replicated task state and selective coordination at commit boundaries. Use explicit idempotency keys and independent state-based outcome checks. Utopia supplies the controller/worker harness, but the replication mechanism and any correctness argument would be new research. The first implementation would reuse established lab components where appropriate.

# Evaluation and feasible starting scope

Gengrui Zhang | Selective coordination for reliable distributed agent execution

## 1. Crash and partition campaign

Crash a worker before/after commitment and partition the ledger replicas. Measure verified completion, lost or duplicated tasks, availability and recovery time under a documented fault schedule.

## 2. Concurrent permission changes

Race cancellation or authorization revocation against action submission. Measure stale-permission execution, invariant violations and commit latency; compare coordination at every update with selective coordination.

## 3. Load and coordination cost

Vary task length, concurrent workers and fault frequency. Report throughput, p50/p95 latency, coordination messages and recovery correctness; do not trade correctness away silently to improve speed.

## First 12 weeks after project agreement

Weeks 1-3: study the group's relevant consistency mechanisms and formalize a small task state machine. Weeks 4-7: implement centralized and replicated baselines. Weeks 8-12: add selective commit coordination, run controlled faults and document assumptions, counterexamples and performance trade-offs.

## Scope and evidence boundaries

The existing system does not establish Byzantine tolerance, consensus correctness or physical dual-server failover. Any guarantee would apply only to the explicit model. I would develop the required distributed-systems theory alongside the implementation and retain CS PhD registration, subject to the department's approval.

## Selected sources and artifacts

Official CS PhD supervision listing

DISCOS research directions

Making CRDTs Not So Eventual

Utopia implementation and bounded acceptance evidence

Prepared 25 October 2026. Proposed experiments are not completed results. Topic and supervision arrangements remain open for discussion.

## Source and project links

- <https://www.concordia.ca/faculty/gengrui-zhang.html>

- <https://www.gengruizhang.com/rd/>

- <https://doi.org/10.14778/3705829.3705850>

- <https://github.com/zhiheng-zhang-Mera/utopia>
