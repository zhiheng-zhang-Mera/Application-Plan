# Research Interest Proposal — 500-Word Version

> 中文说明：本文件是根据同目录完整 RP 提炼的英文约 500 词版本；提交前须按在线系统的实时题目和字数规则复核。

**Applicant:** Zhiheng Zhang

**School:** Concordia University

**Working title:** Evidence-Aware Data and Software Infrastructure for Reliable AI

## Research Interest

AI reliability depends not only on a model but also on the data queries, transformations, software stages, configurations, and validation rules that surround it. These dependencies are often difficult to inspect after a result is produced. The proposed research treats evidence lineage as a first-class data and software object that can be queried, tested, optimized, and governed.

Quant-Ultra, an auditable financial ML system, connects point-in-time data, controlled evaluation, constrained decisions, monitoring, reconciliation, and evidence bundles. Privacy Lens adds a second setting for provenance and fail-closed behavior. These implementations motivate doctoral work on when computational evidence is traceable and robust enough to support a bounded decision; they do not establish novelty, publication, investment validity, or legal compliance.

## Research Questions

- Which provenance schema can connect source records, queries, transformations, models, tests, and decision claims without excessive overhead?
- How can database constraints and software contracts detect temporally invalid or inconsistent ML evidence before downstream use?
- How should validation effort be optimized when checks have different costs, coverage, and operational consequences?
- Which software-engineering practices make failure states reproducible and understandable to independent reviewers?

## Proposed Approach

**Evidence data model.** Design a typed lineage schema for datasets, queries, transformations, experiments, validation results, and bounded claims.

**Contract-based assurance.** Implement database constraints, property-based tests, reconciliation rules, and mutation tests that inject known evidence failures.

**Validation optimization.** Formulate check selection and execution as a constrained optimization problem balancing coverage, latency, and compute cost.

**Software evaluation.** Study reproducibility, fault localization, reviewer effort, and false assurance across financial ML and privacy-sensitive prototypes.

## School Fit and Expected Contribution

Concordia's combination of databases, optimization, machine learning, and software engineering supports research on how data and software architecture determine the reliability of AI evidence; the agenda is designed for refinement during required supervisor matching. The expected contributions are: A queryable provenance model linking ML artifacts to validation evidence and claims.; A failure-injection benchmark for data and software assurance in AI pipelines.; Optimization methods for allocating validation effort under operational constraints. The proposal remains school-wide and does not imply support from a particular supervisor. Its scope can be narrowed after faculty consultation and a verified review of the relevant literature.

## Feasibility and Plan

Early prototyping is feasible, but research will begin with simple baselines, explicit contracts, controlled failure injection, and reproducible records. Where licensing prevents release, experiments will use redistributable data and synthetic controls. Evaluation will retain negative results, separate prediction from decision utility, and report uncertainty across environments. Modular experiments and preregistered ablations, where appropriate, will reduce the risk that system complexity obscures causal conclusions.

Year 1: provenance schema, literature review, and failure taxonomy. Year 2: contract-based assurance and mutation benchmark. Year 3: validation optimization and reviewer studies. Final period: cross-domain synthesis, open artifacts, and dissertation integration.

Before submission, the final version will add a supervisor-reviewed bibliography, confirm ethical and licensing requirements, and match the live prompt. This brief communicates a specific, testable direction while keeping claims within current evidence.
