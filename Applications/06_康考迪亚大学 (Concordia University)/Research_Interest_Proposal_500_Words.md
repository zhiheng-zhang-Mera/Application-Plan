# Research Interest Proposal

**Applicant:** Zhiheng Zhang

**School:** Concordia University

**Email:** nicholas_zhang2020@163.com

**Phone:** (+86)15601654187

## Quant-Ultra: Evidence-Aware Data and Software Infrastructure for Reproducible Financial ML

A Quant-Ultra result depends on source records, point-in-time queries, feature transformations, model versions, backtest configurations, validation checks, and decision rules. When these dependencies are scattered across logs and scripts, a favorable metric can be difficult to reproduce or challenge. The proposed research will make quantitative evidence lineage a first-class data and software object that can be queried, tested, optimized, and connected to bounded claims.

Quant-Ultra is the central research platform for this proposal. It combines point-in-time market data, leakage-resistant rolling evaluation, realistic transaction costs and turnover, risk-aware decisions, monitoring, reconciliation, and reproducible evidence bundles. It separates forecast quality from portfolio utility and restricts conclusions when provenance, stability, reconciliation, or baseline evidence is insufficient. My proposed doctoral work will make every quantitative result queryable through typed provenance, database constraints, software contracts, reconciliation, and optimized validation workflows.

## Research Questions

- Which provenance schema can connect market data, queries, features, models, backtests, validation evidence, and portfolio claims without excessive overhead?
- How can database constraints and software contracts prevent temporally invalid or inconsistent evidence from entering Quant-Ultra experiments?
- How should validation effort be allocated when checks differ in cost, latency, coverage, and risk consequence?
- Which engineering controls most improve reproducibility, fault localization, and independent review of quantitative results?

## Proposed Approach

**Quant evidence model.** Design a typed lineage schema for market data, transformations, experiments, backtests, validation outcomes, and bounded decision claims.

**Contract-based assurance.** Implement database constraints, property-based tests, reconciliation rules, and mutation tests that inject known quantitative evidence failures.

**Validation optimization.** Select and schedule checks through constrained optimization balancing coverage, latency, compute cost, and risk consequence.

**Reviewer-oriented evaluation.** Measure failure detection, fault-localization time, provenance-query performance, and effort required to reconstruct a reported result.

Evaluation will begin with transparent baselines and preserve temporal ordering, fold-local model selection, explicit frictions, and negative results. I will report performance across rolling folds and regimes, sensitivity to costs and constraints, and whether conclusions remain stable under alternative data and execution assumptions. Ablations will isolate each added component. Success requires an improvement in reproducible evidence or bounded decision quality after realistic frictions, not merely a higher pooled prediction score.

Each extension will be compared against unchanged Quant-Ultra baselines so that gains cannot be attributed to altered data windows, cost models, or reporting rules. Every experiment will preserve configurations, intermediate evidence, and failure states for independent review and replication. This preserves comparison across applications.

## Fit and Expected Contributions

Concordia's strengths in databases, optimization, machine learning, and software engineering support a Quant-Ultra research agenda on how data and software architecture determine the reliability of quantitative evidence.

- A queryable provenance model linking Quant-Ultra artifacts to validation evidence and claims.
- A failure-injection benchmark for data and software assurance in financial ML pipelines.
- Optimization methods for allocating validation effort under operational constraints.

Year 1: provenance schema and quantitative failure taxonomy. Year 2: contract-based assurance and mutation benchmark. Year 3: validation optimization and reviewer studies. Final period: cross-workflow synthesis, open artifacts, and dissertation integration.
