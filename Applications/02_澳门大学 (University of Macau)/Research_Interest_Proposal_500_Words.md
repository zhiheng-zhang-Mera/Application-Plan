# Research Interest Proposal — 500-Word Version

> 中文说明：本文件是根据同目录完整 RP 提炼的英文约 500 词版本；提交前须按在线系统的实时题目和字数规则复核。

**Applicant:** Zhiheng Zhang

**School:** University of Macau

**Working title:** Trustworthy Spatiotemporal Learning for Dynamic Urban Decision Systems

## Research Interest

Urban, mobility, and networked data change across locations, populations, sensors, and time. Models trained on convenient historical snapshots can fail when spatial coverage shifts, observations arrive late, or context changes. The proposed research asks how spatiotemporal learning systems can remain temporally valid, privacy-aware, and operationally useful under these changes.

Quant-Ultra, an auditable financial ML system, connects point-in-time data, controlled evaluation, constrained decisions, monitoring, reconciliation, and evidence bundles. Privacy Lens adds a second setting for provenance and fail-closed behavior. These implementations motivate doctoral work on when computational evidence is traceable and robust enough to support a bounded decision; they do not establish novelty, publication, investment validity, or legal compliance.

## Research Questions

- How can spatiotemporal data contracts represent observation time, location context, revisions, missingness, and permitted feature transformations?
- Which online or graph-learning methods remain calibrated when spatial coverage and temporal regimes change together?
- How should privacy, latency, resource, and decision constraints be incorporated without hiding failures behind a single aggregate score?
- What provenance and monitoring evidence is sufficient to reproduce and challenge an urban decision result?

## Proposed Approach

**Spatiotemporal benchmark.** Construct versioned public and synthetic mobility or network datasets with controlled spatial gaps, delayed observations, revisions, and regime changes.

**Adaptive learning.** Compare temporal, graph, and online-learning baselines using location-held-out and rolling-window evaluation with fold-local preprocessing.

**Constrained decisions.** Evaluate calibrated predictions through separately auditable decision rules with privacy, latency, resource, and robustness constraints.

**Distributed evidence.** Prototype provenance-aware pipelines that preserve data lineage, geographic coverage, model versions, monitoring results, and failure states.

## School Fit and Expected Contribution

UM's breadth in data intelligence, optimization, and online and distributed systems supports an agenda connecting dynamic data, reliable learning, and accountable decisions. The expected contributions are: A benchmark for coupled spatial and temporal distribution shift.; Evaluation protocols that separate predictive accuracy, geographic robustness, privacy, and decision utility.; A provenance-aware architecture for distributed spatiotemporal learning. The proposal remains school-wide and does not imply support from a particular supervisor. Its scope can be narrowed after faculty consultation and a verified review of the relevant literature.

## Feasibility and Plan

Early prototyping is feasible, but research will begin with simple baselines, explicit contracts, controlled failure injection, and reproducible records. Where licensing prevents release, experiments will use redistributable data and synthetic controls. Evaluation will retain negative results, separate prediction from decision utility, and report uncertainty across environments. Modular experiments and preregistered ablations, where appropriate, will reduce the risk that system complexity obscures causal conclusions.

Year 1: literature review and benchmark design. Year 2: adaptive spatiotemporal learning and calibration. Year 3: constrained decision and distributed provenance experiments. Final period: cross-dataset validation and dissertation integration.

Before submission, the final version will add a supervisor-reviewed bibliography, confirm ethical and licensing requirements, and match the live prompt. This brief communicates a specific, testable direction while keeping claims within current evidence.
