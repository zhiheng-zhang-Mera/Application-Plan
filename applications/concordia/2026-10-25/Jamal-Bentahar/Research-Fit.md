# Evidence-based coordination and recovery in bounded multi-agent systems

Research-fit statement | Jamal Bentahar

zhiheng0mera@gmail.com | Melbourne, Australia | Fall 2027

Concordia application/student ID: 20814667 | Doctor of Philosophy - Computer Science

International applicant; neither a Canadian citizen nor a permanent resident.

## Motivation and fit

Your work on multi-agent interaction, trust and verification offers a way to connect system behavior with inspectable commitments. Your trust-driven federated-learning deployment work is a relevant methodological analogy for monitoring participants, not evidence about LLM agents. I would investigate a practical coordination mechanism in an existing group platform, with any formal analysis limited to a clearly modeled task state machine.

## Proposed research question

Can a coordinator combining component reliability evidence with current task state reduce cascading failures more effectively than retry rules or trust scores alone, while avoiding excessive isolation of components that are merely slow?

## Preparation I can bring

I led architecture, AI-assisted integration and evidence-backed acceptance of Utopia, a completed and frozen multi-device system. Its bounded records cover two Windows execution workers, Android/Web control, fault/replay histories and independently inspectable results. My Android privacy-evidence research provides additional experience in separating observed signals from stronger claims. These artifacts are a starting point for research, not substitutes for a controlled scientific evaluation.

## Initial method

Instrument benign multi-step workflows with state/version identifiers, authorization scope and pre/postcondition evidence. Compare no gating, fixed timeouts/retries, a static allowlist, trust-only scoring and a combined trust-plus-state policy. Inject stale observations, conflicting reports, duplicate acknowledgements and transient outages. Define a few operational invariants, such as not committing an effect after cancellation, and check them against traces. Treat adversarial and accidental faults separately. Any claim of a guarantee must state its assumptions and exclude unconstrained model behavior.

# Evaluation and feasible starting scope

Jamal Bentahar | Evidence-based coordination and recovery in bounded multi-agent systems

## 1. Cascading faults

Vary the number and location of faulty components and measure verified task completion, invariant violations, wasted calls and recovery time. Use identical fault schedules across policies.

## 2. False isolation

Distinguish slow but correct components from inconsistent ones. Measure detection precision/recall, false isolation and the cost of unnecessary escalation or replacement.

## 3. Minimal useful evidence

Ablate timestamps, state versions, postcondition receipts and full provenance. Measure diagnosis accuracy, reproducibility and storage/runtime overhead to identify the smallest useful trace.

## First 12 weeks after project agreement

First confirm supervision or co-supervision within the existing CS PhD route. Weeks 1-3 after project agreement: select a bounded platform and invariants. Weeks 4-7: implement trace collection and policy baselines. Weeks 8-12: run fault campaigns and analyze where trust scores fail without state checks.

## Scope and evidence boundaries

I do not claim prior expertise in model checking, federated-learning theory or new formal logics. Utopia has bounded replay evidence, not a proof of general multi-agent safety. My preference is systems construction and empirical validation, with focused formal modeling where it materially supports correctness. Current Concordia CS PhD supervision eligibility remains to be confirmed.

## Selected sources and artifacts

Current official role, contact and research

Trust-driven federated-learning deployment paper

Utopia implementation and bounded acceptance evidence

Prepared 25 October 2026. Proposed experiments are not completed results. Topic and supervision arrangements remain open for discussion.

## Source and project links

- <https://www.concordia.ca/faculty/jamal-bentahar.html>

- <https://arxiv.org/abs/2405.00395>

- <https://github.com/zhiheng-zhang-Mera/utopia>
