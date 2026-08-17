# Research Interest Proposal

**Applicant:** Zhiheng Zhang

**School:** University of Macau

## Trustworthy Spatiotemporal Learning for Dynamic Urban Decision Systems

My research interest is trustworthy spatiotemporal learning for urban and networked environments. Mobility traces, sensor streams, and location-linked observations are never static: coverage changes across districts, observations arrive late, populations shift, and the meaning of a feature can change with time and context. A model that performs well on a convenient historical snapshot may therefore fail when deployed in a different place or period. I want to develop learning systems that make these spatial and temporal assumptions explicit and that remain useful when the environment changes.

The first part of the research will create a benchmark for coupled spatial and temporal shift. Versioned public datasets and synthetic controls will reproduce delayed observations, missing regions, revised records, changing network structure, and abrupt regime changes. Each dataset will carry machine-readable contracts describing observation time, geographic scope, revision state, and permitted transformations. Evaluation will use rolling windows and location-held-out tests so that preprocessing and model selection cannot borrow information from the future or the target region.

The second part will compare temporal, graph-based, and online-learning methods under these controlled changes. The goal is not simply to maximize a pooled accuracy score. I will examine calibration, geographic robustness, adaptation speed, and uncertainty across locations and periods. Predictions will then enter a separately auditable decision layer with privacy, latency, resource, and robustness constraints. This separation will reveal whether an apparently stronger model actually produces more dependable decisions.

My preparation comes from Quant-Ultra, where I have implemented point-in-time data controls, walk-forward evaluation, monitoring, reconciliation, and evidence records for non-stationary financial data. Privacy Lens provides complementary experience with provenance and fail-closed validation in privacy-sensitive software. I would adapt these engineering foundations to spatiotemporal data while treating existing systems as prototypes rather than completed research contributions.

The University of Macau is a strong setting for this agenda because its work spans data intelligence, optimization, and online and distributed systems. These strengths support a coherent project connecting dynamic data, reliable learning, and accountable decisions. I expect the research to contribute a reproducible shift benchmark, evaluation protocols that separate predictive accuracy from geographic and operational robustness, and a provenance-aware architecture for distributed spatiotemporal learning.

The initial study will use a small set of transparent baselines before introducing more complex models. Success will be measured by performance stability across held-out locations and time periods, calibrated uncertainty, adaptation after controlled changes, and the ability to reconstruct every reported result from its data and configuration record. Ablation studies will isolate the value of spatial structure, online adaptation, and provenance controls. If sophisticated methods do not outperform simpler alternatives consistently, that negative result will guide the design rather than be discarded. This evaluation strategy keeps the project scientifically testable and relevant to real systems whose operating conditions cannot be assumed to remain fixed.
