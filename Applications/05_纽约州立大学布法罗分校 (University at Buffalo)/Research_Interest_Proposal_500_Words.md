# Research Interest Proposal

**Applicant:** Zhiheng Zhang

**School:** University at Buffalo, SUNY

**Email:** nicholas_zhang2020@163.com

**Phone:** (+86)15601654187

## Quant-Ultra: Anomaly-Aware Sequential Learning for Risk-Constrained Financial Decisions

Quant-Ultra provides point-in-time data, walk-forward evaluation, realistic costs, risk controls, monitoring, reconciliation, and audit evidence for financial ML. Its next research challenge is to distinguish data failure, transient anomaly, and persistent regime change while feedback is delayed. A quantitative system should not only detect unusual behavior; it should calibrate uncertainty and choose whether to continue, constrain, abstain, or request review.

Quant-Ultra is the central research platform for this proposal. It combines point-in-time market data, leakage-resistant rolling evaluation, realistic transaction costs and turnover, risk-aware decisions, monitoring, reconciliation, and reproducible evidence bundles. It separates forecast quality from portfolio utility and restricts conclusions when provenance, stability, reconciliation, or baseline evidence is insufficient. My proposed doctoral work will strengthen walk-forward evaluation with explicit anomaly, drift, delayed-feedback, uncertainty, and response-policy layers.

## Research Questions

- How can sequential models distinguish corrupted market data, transient anomalies, and persistent regime change?
- Which uncertainty and calibration measures remain informative under delayed labels, repeated model selection, and distribution shift?
- How should anomaly evidence change position limits, turnover, exposure, or abstention policies?
- Can distributed monitoring and provenance reduce false confidence while preserving a usable quantitative workflow?

## Proposed Approach

**Sequential failure benchmark.** Extend Quant-Ultra with delayed-feedback simulations and controlled data, context, and regime anomalies evaluated through rolling windows.

**Detection and calibration.** Compare statistical, representation, and Bayesian baselines using detection delay, false alarms, calibration, and post-change recovery.

**Risk-aware response.** Map calibrated evidence into normal operation, constrained exposure, abstention, or review and measure downstream utility after costs.

**Monitoring evidence.** Record data, model, uncertainty, alert, response, and portfolio lineage across reproducible pipeline stages.

Evaluation will begin with transparent baselines and preserve temporal ordering, fold-local model selection, explicit frictions, and negative results. I will report performance across rolling folds and regimes, sensitivity to costs and constraints, and whether conclusions remain stable under alternative data and execution assumptions. Ablations will isolate each added component. Success requires an improvement in reproducible evidence or bounded decision quality after realistic frictions, not merely a higher pooled prediction score.

Each extension will be compared against unchanged Quant-Ultra baselines so that gains cannot be attributed to altered data windows, cost models, or reporting rules. Every experiment will preserve configurations, intermediate evidence, and failure states for independent review and replication. This preserves comparison across applications.

## Fit and Expected Contributions

UB CSE's strengths in machine learning, optimization, anomaly detection, and data-intensive systems support a Quant-Ultra research agenda on detecting market change and responding through bounded decisions.

- A financial benchmark separating data failure, transient anomaly, and market regime change.
- Calibration protocols for delayed and shifting quantitative feedback.
- Auditable response policies connecting anomaly evidence to risk-constrained portfolio decisions.

Year 1: failure taxonomy and sequential baselines. Year 2: uncertainty calibration and shift-aware learning. Year 3: constrained response policies and distributed monitoring. Final period: cross-market evaluation and dissertation integration.
