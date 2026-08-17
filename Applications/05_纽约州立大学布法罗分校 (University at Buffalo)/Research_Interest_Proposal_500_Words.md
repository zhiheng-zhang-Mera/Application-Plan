# Research Interest Proposal

**Applicant:** Zhiheng Zhang

**School:** University at Buffalo, SUNY

## Anomaly-Aware Sequential Learning for Reliable High-Stakes Decisions

My proposed research studies anomaly-aware sequential learning for reliable decisions under distribution shift. In streaming environments, a sudden change may indicate a corrupted data source, a rare but temporary event, or a persistent regime transition. These cases require different responses, yet they are often collapsed into a single anomaly score. Delayed labels and repeated model selection make the problem harder: a system may appear accurate while remaining poorly calibrated precisely when a decision is most consequential.

I plan to build a benchmark that separates data-integrity failures, transient anomalies, and structural drift. Rolling and expanding windows will preserve temporal order, while delayed-feedback simulations will test how quickly a method can recognize and respond to change. Controlled interventions will introduce missing observations, altered feature distributions, unusual sequences, and persistent shifts. Statistical detection methods, representation models, and Bayesian baselines will be compared using detection delay, false alarms, calibration, and performance after adaptation.

A central feature of the project is the connection between anomaly evidence and action. Rather than treating an alert as an automatic decision, I will map calibrated evidence into abstention, human review, or constrained responses. In financial experiments, those responses will include explicit turnover, cost, exposure, concentration, and risk limits. Forecast quality and downstream utility will be reported separately so that a favorable decision outcome cannot hide weak predictive evidence, and a strong detector cannot be credited for an impractical response policy.

Quant-Ultra provides an initial testbed through its point-in-time data, walk-forward evaluation, risk controls, monitoring, reconciliation, and machine-readable audit records. Privacy Lens offers a second domain for studying anomalous inputs, provenance, replay boundaries, and conservative automated behavior. These systems give me practical experience with failure-oriented evaluation and reproducible pipelines, while the doctoral work will supply the formal problem definitions, literature-grounded baselines, and independent empirical evidence.

The University at Buffalo's strengths in machine learning, optimization, anomaly detection, and data-intensive systems align closely with this project. I aim to contribute a benchmark distinguishing anomaly, drift, and data-quality failures; calibration methods for delayed and shifting feedback; and auditable response policies that connect uncertainty to bounded decisions. The department's breadth would allow the learning, optimization, and systems components to be developed as one integrated research program.

The empirical studies will begin with interpretable statistical detectors and simple response rules, then add learned representations and Bayesian uncertainty only when they produce measurable gains. Evaluation will report behavior before, during, and after each injected change, not just an average over the full stream. I will test whether calibration deteriorates before accuracy, whether review policies reduce costly false responses, and how conclusions change under alternative delay and cost assumptions. Reproducible configurations and preserved negative results will make comparisons independently auditable. These criteria define success as reliable behavior under change, rather than a single favorable score on a static test set.
