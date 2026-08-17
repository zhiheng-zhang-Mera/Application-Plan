# Research Interest Proposal

**Applicant:** Zhiheng Zhang

**School:** University of Macau

**Email:** nicholas_zhang2020@163.com

**Phone:** (+86)15601654187

## Quant-Ultra: Trustworthy Spatiotemporal and Graph Learning for Dynamic Financial Markets

Quant-Ultra already treats temporal validity, data provenance, realistic frictions, and bounded claims as first-class requirements in financial ML. The next research step is to model markets as evolving relational systems: assets, sectors, and risk exposures interact through structures that change across time. A reliable quantitative system must learn from these changing relationships without leaking future information or hiding instability behind pooled performance.

Quant-Ultra is the central research platform for this proposal. It combines point-in-time market data, leakage-resistant rolling evaluation, realistic transaction costs and turnover, risk-aware decisions, monitoring, reconciliation, and reproducible evidence bundles. It separates forecast quality from portfolio utility and restricts conclusions when provenance, stability, reconciliation, or baseline evidence is insufficient. My proposed doctoral work will develop point-in-time representations of evolving asset, sector, and market relationships, then evaluate temporal and graph-learning methods under regime change.

## Research Questions

- How should point-in-time data contracts represent evolving asset universes, graph edges, observation times, revisions, and permitted transformations?
- Which temporal, graph, or online-learning methods remain calibrated when market relationships and regimes change together?
- How can distributed feature and experiment pipelines preserve lineage while controlling latency and computational cost?
- Do relational signals improve risk-adjusted decisions after turnover, transaction costs, exposure limits, and uncertainty are applied?

## Proposed Approach

**Point-in-time relational benchmark.** Extend Quant-Ultra with versioned market graphs and controlled changes to membership, edges, missingness, revisions, and regimes.

**Adaptive graph learning.** Compare transparent temporal baselines with graph and online-learning methods using rolling windows, fold-local preprocessing, and regime-aware evaluation.

**Constrained portfolio layer.** Feed calibrated forecasts into auditable allocation rules with turnover, cost, exposure, concentration, and drawdown constraints.

**Distributed evidence.** Preserve source, feature, graph, model, and decision lineage across reproducible pipeline stages and measure the cost of stronger controls.

Evaluation will begin with transparent baselines and preserve temporal ordering, fold-local model selection, explicit frictions, and negative results. I will report performance across rolling folds and regimes, sensitivity to costs and constraints, and whether conclusions remain stable under alternative data and execution assumptions. Ablations will isolate each added component. Success requires an improvement in reproducible evidence or bounded decision quality after realistic frictions, not merely a higher pooled prediction score.

Each extension will be compared against unchanged Quant-Ultra baselines so that gains cannot be attributed to altered data windows, cost models, or reporting rules. Every experiment will preserve configurations, intermediate evidence, and failure states for independent review and replication. This preserves comparison across applications.

## Fit and Expected Contributions

UM's strengths in data intelligence, optimization, and online and distributed systems support a Quant-Ultra extension focused on dynamic market structure and temporally valid graph evidence.

- A point-in-time benchmark for evolving financial graphs and temporal distribution shift.
- Evaluation protocols separating relational predictive value from cost- and risk-adjusted decision utility.
- A provenance-aware distributed architecture for reproducible graph-based quantitative research.

Year 1: relational data contracts and transparent baselines. Year 2: adaptive graph learning and calibration. Year 3: constrained portfolio experiments and distributed provenance. Final period: cross-market validation and dissertation integration.
