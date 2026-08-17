# Research Interest Proposal

**Applicant:** Zhiheng Zhang

**School:** Concordia University

## Evidence-Aware Data and Software Infrastructure for Reliable AI

My research interest is evidence-aware data and software infrastructure for reliable artificial intelligence. An AI result depends on far more than a trained model: it also depends on source records, database queries, transformations, software versions, configurations, tests, and validation rules. When these dependencies are scattered across logs and scripts, a result may be difficult to reproduce or challenge even if the final metric appears convincing. I want to make evidence lineage a first-class object that can be queried, tested, and governed.

The project will begin with a typed provenance model connecting datasets, queries, transformations, experiments, validation results, and bounded claims. The model will record both successful stages and invalid or missing evidence. Database constraints and software contracts will then check temporal consistency, source validity, schema expectations, and reconciliation rules before downstream use. Property-based and mutation tests will inject known failures to measure which controls detect them, how quickly the cause can be localized, and whether the system communicates the failure clearly to an independent reviewer.

Because exhaustive validation can be expensive, a second component will study how to allocate assurance effort. I will formulate check selection and execution as a constrained optimization problem in which tests differ in cost, latency, coverage, and consequence. Policies will be evaluated against simple fixed test suites and risk-based baselines. The objective is not to remove human judgment, but to identify when automated evidence is sufficient for routine continuation and when the system should abstain or require review.

My preparation comes from Quant-Ultra, an implemented financial ML pipeline with typed stage contracts, point-in-time controls, reconciliation checks, monitoring, and reproducible evidence bundles. Privacy Lens provides complementary experience with invalid-source handling, replay boundaries, and audit records in privacy-sensitive software. Together they offer two settings for failure injection and cross-domain evaluation without assuming that existing engineering artifacts already establish research novelty.

Concordia's strengths in databases, optimization, machine learning, and software engineering make it an excellent environment for this work. I expect the research to produce a queryable provenance model linking AI artifacts to validation evidence, a failure-injection benchmark for data and software assurance, and optimization methods for allocating validation effort under operational constraints. The resulting infrastructure would help researchers reproduce results, locate failures, and state more defensible boundaries around AI-supported decisions.

Evaluation will compare the proposed architecture with conventional experiment logs and fixed validation pipelines. Key measures will include failure-detection coverage, false alarms, time to locate a fault, provenance-query latency, compute cost, and the effort required for an independent reviewer to reconstruct a claim. Ablation studies will test whether each schema element or contract adds useful assurance. The optimization component will be considered successful only if it preserves critical coverage while reducing cost or latency relative to transparent baselines. By publishing failure cases as well as successful runs, the project will support cumulative evidence about which engineering controls genuinely improve AI reliability.
