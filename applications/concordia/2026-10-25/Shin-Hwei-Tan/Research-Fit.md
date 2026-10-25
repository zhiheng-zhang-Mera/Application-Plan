# State-based test oracles for interrupted agentic workflows

Research-fit statement | Shin Hwei Tan

zhiheng0mera@gmail.com | Melbourne, Australia | Fall 2027

Concordia application/student ID: 20814667 | Doctor of Philosophy - Computer Science

International applicant; neither a Canadian citizen nor a permanent resident.

## Motivation and fit

Your group's Understanding Bugs in Modern Agentic Frameworks provides a particularly direct bridge from my project experience to an empirical software-engineering study. Its distinction between framework defects and task-level model failures suggests a disciplined way to classify failures before designing tests. I would use Utopia as one inspectable seed system, then test whether selected fault triggers and outcome checks transfer to other frameworks.

## Proposed research question

Can independent state-based test oracles and controlled interruption/replay expose false completion and duplicate effects more reliably than agent self-reports or log-only assertions, and which failures transfer across frameworks?

## Preparation I can bring

I led architecture, AI-assisted integration and evidence-backed acceptance of Utopia, a completed and frozen multi-device system. Its bounded records cover two Windows execution workers, Android/Web control, fault/replay histories and independently inspectable results. My Android privacy-evidence research provides additional experience in separating observed signals from stronger claims. These artifacts are a starting point for research, not substitutes for a controlled scientific evaluation.

## Initial method

Build a small benchmark of benign, verifiable tasks with expected filesystem or application-state outcomes. Categorize failures as framework-level, application-integration or model/task failures before attributing responsibility. Inject interrupted tool calls, changed permissions, stale observations and altered retry order. Compare self-report checks, ordinary logs and independent postcondition oracles. A later phase would implement a narrow detection or repair mechanism only after the empirical study identifies recurring causes. The goal is a research contribution beyond adding more features to my own project.

# Evaluation and feasible starting scope

Shin Hwei Tan | State-based test oracles for interrupted agentic workflows

## 1. Oracle validity

Compare completion reports with external state checks using independently labeled cases. Measure false-success detection, missed failures, agreement and the cost of building each oracle; audit oracle bugs separately.

## 2. Fault-trigger transfer

Port a selected set of interruption, configuration and ordering triggers to two or more frameworks. Measure reproducibility, failure yield and transfer rate, keeping framework versions and tasks fixed.

## 3. Mechanism ablations

Remove state provenance, weaken checkpoints or alter retry ordering in a sandbox. Measure duplicate effects, permission violations, regression-detection rate and runtime overhead; retain negative and inconclusive results.

## First 12 weeks after project agreement

Weeks 1-3: reproduce the relevant taxonomy on a small audited sample and define outcome oracles. Weeks 4-7: construct the controlled fault/replay corpus and baseline checks. Weeks 8-12: run a cross-framework pilot, assess annotation agreement and decide whether a targeted repair mechanism is warranted.

## Scope and evidence boundaries

Utopia is a completed engineering baseline, not proof of general agent reliability or a peer-reviewed result. No unrestricted natural-language autonomy, production high availability or deployed wearable assistant is claimed. Public release would use benign tasks and remove credentials, personal traces and nonredistributable data.

## Selected sources and artifacts

Official CS PhD supervision listing

Current recruitment and research

Agentic-framework bug study

Utopia implementation and bounded acceptance evidence

Prepared 25 October 2026. Proposed experiments are not completed results. Topic and supervision arrangements remain open for discussion.

## Source and project links

- <https://www.concordia.ca/faculty/shinhwei-tan.html>

- <https://www.shinhwei.com/>

- <https://arxiv.org/html/2604.08906v4>

- <https://github.com/zhiheng-zhang-Mera/utopia>
