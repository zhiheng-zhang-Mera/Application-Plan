# Research Interest Proposal — 500-Word Version

> 中文说明：本文件是根据同目录完整 RP 提炼的英文约 500 词版本；提交前须按在线系统的实时题目和字数规则复核。

**Applicant:** Zhiheng Zhang

**School:** University at Buffalo, SUNY

**Working title:** Anomaly-Aware Sequential Learning for Reliable High-Stakes Decisions

## Research Interest

Sequential decision systems must distinguish ordinary variation from structural change while acting under uncertainty and cost. In financial and other streaming settings, labels arrive late, anomalies may be rare, and repeated model selection can make apparent improvements fragile. The proposed research joins sequential learning, anomaly detection, and constrained optimization in an auditable evaluation framework.

Quant-Ultra, an auditable financial ML system, connects point-in-time data, controlled evaluation, constrained decisions, monitoring, reconciliation, and evidence bundles. Privacy Lens adds a second setting for provenance and fail-closed behavior. These implementations motivate doctoral work on when computational evidence is traceable and robust enough to support a bounded decision; they do not establish novelty, publication, investment validity, or legal compliance.

## Research Questions

- How can sequential models distinguish transient anomalies, persistent regime change, and data-quality failures?
- Which uncertainty and calibration measures remain informative under delayed labels and distribution shift?
- How should anomaly signals interact with turnover, cost, exposure, and risk constraints in a decision layer?
- Can distributed monitoring and provenance reduce false confidence without making the system unusably conservative?

## Proposed Approach

**Sequential evaluation.** Use rolling and expanding windows, delayed-label simulations, and regime-aware splits while preserving fold-local model selection.

**Anomaly taxonomy.** Inject data, context, and behavioral anomalies and compare statistical, representation, and Bayesian baselines.

**Risk-aware response.** Map calibrated anomaly evidence into abstention, review, or constrained decisions and measure both detection and downstream utility.

**Distributed monitoring.** Record model, data, uncertainty, alert, and decision lineage across reproducible pipeline stages.

## School Fit and Expected Contribution

UB CSE's complementary strengths in learning, optimization, anomaly detection, and data-intensive systems support a committee-facing agenda that can later be refined through faculty matching. The expected contributions are: A benchmark separating anomaly, drift, and data-integrity failures in sequential ML.; Calibration and evaluation methods for delayed and shifting feedback.; Auditable response policies connecting anomaly evidence to bounded decisions. The proposal remains school-wide and does not imply support from a particular supervisor. Its scope can be narrowed after faculty consultation and a verified review of the relevant literature.

## Feasibility and Plan

Early prototyping is feasible, but research will begin with simple baselines, explicit contracts, controlled failure injection, and reproducible records. Where licensing prevents release, experiments will use redistributable data and synthetic controls. Evaluation will retain negative results, separate prediction from decision utility, and report uncertainty across environments. Modular experiments and preregistered ablations, where appropriate, will reduce the risk that system complexity obscures causal conclusions.

Year 1: anomaly taxonomy, sequential baselines, and delayed-feedback benchmark. Year 2: uncertainty calibration and shift-aware learning. Year 3: constrained response policies and distributed monitoring. Final period: cross-domain evaluation and dissertation integration.

Before submission, the final version will add a supervisor-reviewed bibliography, confirm ethical and licensing requirements, and match the live prompt. This brief communicates a specific, testable direction while keeping claims within current evidence.
