from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Applications"
DOCS = ROOT / "Documents"


SCHOOLS = [
    {
        "order": "01",
        "folder": "HKUST Guangzhou",
        "school": "The Hong Kong University of Science and Technology (Guangzhou)",
        "program": "PhD in Financial Technology",
        "contact": "Targeted contact strongly recommended; application may proceed in parallel.",
        "lor": "2-5 academic references",
        "statement": "Proposed Research Plan and Past Research Experience",
        "source": "https://fytgs.hkust-gz.edu.cn/wp-content/uploads/2023/07/Guidelines-for-Application-Submission-Research-PG-Programs_gz.pdf",
        "faculty": [
            ("Shuo Sun", "AI and financial technology, including learning-based decision systems", "a research infrastructure that evaluates reinforcement-learning and quantitative strategies under point-in-time data, regime change, and realistic market frictions"),
            ("Sijia Chen", "distributed computing and decision algorithms for financial risk-control systems", "distributed, auditable decision pipelines that connect data provenance, constrained optimization, and risk monitoring"),
            ("Yuyu Luo", "data-centric AI, databases, analytics, and AI agents", "data-centric infrastructure for point-in-time financial datasets, reproducible experiments, and evidence-traceable agent workflows"),
            ("Liang Zhang", "data mining, graph learning, language models, and applied AI", "robust representation learning for non-stationary financial data with leakage-resistant evaluation and bounded claims"),
        ],
    },
    {
        "order": "02",
        "folder": "University of Macau",
        "school": "University of Macau",
        "program": "PhD in Computer Science",
        "contact": "Targeted contact is optional but potentially valuable; verify the 2027/28 call.",
        "lor": "2 references, including at least one academic reference",
        "statement": "Statement of purpose; research proposal if requested by the live portal",
        "source": "https://grs.um.edu.mo/index.php/prospective-students/doctoral-degrees-programmes/",
        "faculty": [
            ("Peng Wang", "mathematical optimization, machine learning, and artificial intelligence", "risk-aware optimization whose objectives and constraints are evaluated with temporal holdouts and transaction costs"),
            ("Pengyang Wang", "data mining, big-data analytics, and machine learning", "auditable mining of non-stationary financial data with point-in-time features and drift-aware validation"),
            ("Dingqi Yang", "spatiotemporal data mining, machine learning, and big data", "methods that treat market observations as temporally structured data and explicitly test distribution shift"),
            ("Huanle Xu", "big-data processing systems, online learning, and distributed systems", "online monitoring and distributed experiment infrastructure for changing financial environments"),
            ("Ye Kanye Wang", "distributed systems, privacy, blockchain, and decentralized finance", "audit-ready data and decision infrastructure for high-stakes financial and decentralized systems"),
        ],
    },
    {
        "order": "03",
        "folder": "Drexel University",
        "school": "Drexel University",
        "program": "PhD in Computer Science",
        "contact": "Departmental admission; email is an optional, selective draft and should not be mass-sent.",
        "lor": "2 letters of recommendation",
        "statement": "Approximately 500-word Statement of Purpose",
        "source": "https://drexel.edu/cci/admissions/doctoral/",
        "faculty": [
            ("Preetha Chatterjee", "software engineering with machine learning and data mining", "reliable ML software engineering: testable temporal data contracts, experiment lineage, and governance gates"),
            ("Xiaohua Tony Hu", "data mining, text mining, and analytics", "robust data-mining workflows for financial signals whose evaluation resists leakage and unstable regimes"),
            ("Weimao Ke", "information systems, distributed systems, machine learning, and data mining", "distributed research infrastructure that makes data provenance and model evidence reproducible"),
            ("Shahin Jabbari", "machine learning, fairness, optimization, and game theory", "risk-aware optimization and accountable decisions under non-stationarity and competing objectives"),
        ],
    },
    {
        "order": "04",
        "folder": "Stevens Institute of Technology",
        "school": "Stevens Institute of Technology",
        "program": "PhD in Computer Science",
        "contact": "Departmental application; a selective email may be sent after checking faculty availability.",
        "lor": "3 letters of recommendation for the Computer Science PhD",
        "statement": "500-1,000-word Statement of Purpose plus a professional writing sample",
        "source": "https://www.stevens.edu/academics/graduate-study/phd-application-process",
        "faculty": [
            ("Shaoyi Huang", "efficient and privacy-preserving machine learning and algorithm-system co-design", "system-level co-design for efficient, reproducible financial ML experiments with explicit governance checks"),
            ("Samantha Kleinberg", "causal inference and time series", "distinguishing predictive association from temporally valid evidence in non-stationary financial time series"),
            ("Tian Han", "probabilistic and generative machine learning and explainable AI", "uncertainty-aware representations whose usefulness is tested through walk-forward, cost-aware evaluation"),
            ("Nikhil Muralidhar", "scientific and domain-aware machine learning", "domain-aware learning in which financial constraints and evidence boundaries are built into experimental design"),
        ],
    },
    {
        "order": "05",
        "folder": "University at Buffalo",
        "school": "University at Buffalo, SUNY",
        "program": "PhD in Computer Science and Engineering",
        "contact": "Do not cold-email generically; faculty fit belongs primarily in the application statement.",
        "lor": "3 letters of recommendation, preferably academic",
        "statement": "Brief personal statement / Statement of Purpose",
        "source": "https://engineering.buffalo.edu/computer-science-engineering/graduate/admissions/application-materials.html",
        "faculty": [
            ("Kaiyi Ji", "optimization, machine learning, and big-data analytics", "risk-aware optimization supported by leakage-resistant validation and auditable decision records"),
            ("Varun Chandola", "anomaly detection and big-data analytics", "regime, drift, and anomaly monitoring as first-class components of financial ML evaluation"),
            ("Tevfik Kosar", "data-intensive distributed and storage systems", "point-in-time financial data infrastructure with reproducible lineage and scalable experiment execution"),
            ("Changyou Chen", "Bayesian inference, generative learning, and reinforcement learning", "uncertainty-aware and sequential decision methods evaluated under realistic temporal and market constraints"),
        ],
    },
    {
        "order": "06",
        "folder": "Concordia University",
        "school": "Concordia University",
        "program": "PhD in Computer Science / Software Engineering",
        "contact": "Supervisor match is required before an admission offer; obtain an application Student ID before outreach where possible.",
        "lor": "3 letters of reference and assessment forms",
        "statement": "Statement of Purpose plus a concise research-interest brief",
        "source": "https://www.concordia.ca/gradstudies/future-students/how-to-apply/programs-with-additional-requirements.html",
        "faculty": [
            ("Nematollaah Shiri", "databases, uncertain data, query optimization, and data analytics", "point-in-time data construction and queryable provenance for leakage-resistant financial ML"),
            ("Brigitte Jaumard", "large-scale optimization and operations research", "risk-aware portfolio and decision optimization with explicit feasibility, turnover, and cost constraints"),
            ("Andrew Delong", "machine learning, deep learning, and optimization", "robust learning and optimization under temporal distribution shift with falsifiable evaluation"),
            ("Emad Shihab", "data-driven software engineering and software engineering for AI", "a unified software-governance agenda across Quant-Ultra and Privacy Lens, emphasizing testing, auditability, and evidence boundaries"),
        ],
    },
    {
        "order": "07",
        "folder": "The Hong Kong Polytechnic University",
        "school": "The Hong Kong Polytechnic University",
        "program": "PhD in Data Science and Artificial Intelligence / Computing",
        "contact": "Targeted contact recommended; use the mandatory standard research-proposal form in the portal.",
        "lor": "2 academic referee reports",
        "statement": "CV, Personal Statement, and standard-form Research Proposal",
        "source": "https://www.polyu.edu.hk/study/pg/research-postgraduate/supporting-documents-application-rpg",
        "faculty": [
            ("Xiao Huang", "data mining, machine learning, and agentic AI", "agentic financial research workflows whose tools, data lineage, and claims remain auditable"),
            ("Houduo Qi", "optimization, data science, and portfolio optimization", "portfolio optimization tied to point-in-time data, realistic frictions, and robust out-of-sample evidence"),
            ("Wanyu Lin", "trustworthy AI, privacy, and explainability", "trustworthy financial ML infrastructure combining provenance, bounded interpretation, monitoring, and privacy-aware governance"),
            ("Wenqi Fan", "machine learning, data mining, graph learning, and recommender systems", "robust graph and representation learning for changing financial relationships, evaluated without temporal leakage"),
        ],
    },
    {
        "order": "08",
        "folder": "City University of Hong Kong",
        "school": "City University of Hong Kong",
        "program": "PhD in Data Science",
        "contact": "Targeted contact recommended; confirm supervisor capacity before relying on a match.",
        "lor": "2 academic referees",
        "statement": "Personal Statement and compulsory Research Proposal",
        "source": "https://www.ds.cityu.edu.hk/en/programmes/postgraduate-programmes/phd-programme-data-science",
        "faculty": [
            ("Qi Wu", "quantitative finance, financial technology, and business analytics", "financial intelligence infrastructure that integrates temporal validity, risk controls, and deployment-oriented auditability"),
            ("Kaidi Xu", "trustworthy AI, uncertainty, and formal verification", "verifiable controls and uncertainty-aware evaluation for high-stakes financial ML pipelines"),
            ("Xinyue Li", "scalable statistical learning for large datasets", "scalable learning on point-in-time financial data with drift-aware and statistically disciplined evaluation"),
        ],
    },
    {
        "order": "09",
        "folder": "Stony Brook University",
        "school": "Stony Brook University",
        "program": "PhD in Computer Science",
        "contact": "Departmental admission; do not spend application time on generic cold email.",
        "lor": "3 letters of recommendation, with a majority from academia preferred",
        "statement": "Statement of Purpose",
        "source": "https://www.cs.stonybrook.edu/admissions/Graduate-Program",
        "faculty": [
            ("Yifan Sun", "large-scale and nonconvex optimization for machine learning", "large-scale risk-aware optimization grounded in realistic, walk-forward financial evaluation"),
            ("Anshul Gandhi", "systems for machine learning, cloud systems, and optimization", "resource-aware, reproducible systems for financial ML experiments and monitoring"),
            ("Ting Wang", "machine learning, security, privacy, and trustworthy decision-making", "trustworthy decision infrastructure joining model evidence, privacy, provenance, and explicit governance gates"),
            ("Praveen Tripathi", "machine learning, data mining, and spatiotemporal analysis", "temporally structured financial learning with distribution-shift and anomaly monitoring"),
        ],
    },
    {
        "order": "10",
        "folder": "The Chinese University of Hong Kong",
        "school": "The Chinese University of Hong Kong",
        "program": "MPhil-PhD in Computer Science and Engineering",
        "contact": "A professor must ultimately agree to supervise after the departmental process; targeted contact is essential.",
        "lor": "At least 3 confidential recommendation reports for full-time doctoral applicants",
        "statement": "CV, updated transcript, class-ranking evidence if available, and interview preparation",
        "source": "https://www.cse.cuhk.edu.hk/admission/mphil-phd/regular-admission/",
        "faculty": [
            ("James Cheng", "high-performance systems for data analytics, machine learning, and inference", "high-performance financial ML infrastructure with reproducible data and experiment lineage"),
            ("Eric Chi Lik Lo", "machine learning, big data, databases, data mining, and distributed systems", "database and distributed-system support for point-in-time datasets and leakage-resistant analytics"),
            ("Songtao Lu", "optimization, machine learning, and data science", "robust optimization under temporal shift, transaction costs, and explicit risk constraints"),
            ("Sinno Jialin Pan", "transfer learning and domain adaptation", "domain adaptation across market regimes without contaminating evaluation through future information"),
            ("Farzan Farnia", "robust machine learning, optimization, and distribution shift", "robust learning objectives and stress tests for distribution shifts in financial decision systems"),
        ],
    },
    {
        "order": "11",
        "folder": "UMass Amherst",
        "school": "University of Massachusetts Amherst",
        "program": "PhD in Computer Science",
        "contact": "Departmental admission; faculty fit should be concentrated in the Personal Statement.",
        "lor": "2 letters of recommendation",
        "statement": "Personal Statement / current application statement prompt",
        "source": "https://www.cics.umass.edu/academics/phd-computer-science/how-apply-phd-program",
        "faculty": [
            ("Marco Serafini", "systems for machine learning, data management, and distributed systems", "reliable systems that connect point-in-time financial data, distributed experiment execution, and audit trails"),
            ("Peter Haas", "data management, applied probability, statistics, and optimization", "statistically disciplined data systems for uncertainty-aware and cost-aware financial decisions"),
            ("Ben Marlin", "multivariate time-series machine learning", "multivariate financial learning under missingness, temporal shift, and strict walk-forward evaluation"),
            ("Alexandra Meliou", "data quality, causality, and trustworthy data systems", "data-quality and provenance mechanisms that expose when financial ML evidence is unsafe to use"),
            ("Mohammad Hajiesmaili", "optimization, algorithms, and learning under uncertainty", "online and risk-aware optimization under uncertain, changing financial environments"),
        ],
    },
    {
        "order": "12",
        "folder": "HKUST",
        "school": "The Hong Kong University of Science and Technology",
        "program": "PhD in Computer Science and Engineering",
        "contact": "Current CSE FAQ says an applicant must have a faculty member who agrees to supervise; targeted contact is a prerequisite, not mass email.",
        "lor": "2-5 academic references",
        "statement": "Proposed Research Plan and Past Research Experience",
        "source": "https://cse.hkust.edu.hk/pg/admissions/faq/",
        "faculty": [
            ("Binhang Yuan", "data management for machine learning and distributed machine learning", "distributed data and experiment infrastructure for point-in-time, reproducible financial ML"),
            ("Kai Chen", "machine-learning systems, high-performance networking, and privacy computing", "efficient and privacy-aware financial ML systems with explicit operational and evidence controls"),
            ("Qiong Luo", "big-data systems and parallel and distributed computing", "scalable point-in-time data processing and reproducible backtest execution"),
            ("Lei Chen", "time-series databases, data-driven machine learning, and DB4AI", "time-series database support for leakage-resistant feature generation, monitoring, and auditable ML"),
        ],
    },
    {
        "order": "13",
        "folder": "University of California Riverside - Reserve",
        "school": "University of California, Riverside",
        "program": "PhD in Computer Science",
        "contact": "Reserve application: send a targeted inquiry first and apply only if the PI signal and full portfolio justify the cost.",
        "lor": "3 letters of recommendation",
        "statement": "Graduate Statement of Purpose",
        "source": "https://www1.cs.ucr.edu/graduate/admissions/international",
        "faculty": [
            ("Eamonn Keogh", "time-series data mining", "falsifiable analysis of non-stationary financial time series, with strong safeguards against data leakage and benchmark overclaiming"),
            ("Vagelis Papalexakis", "data mining, machine learning, and trustworthy AI", "trustworthy mining of multi-relational financial data with transparent failure analysis"),
            ("Vagelis Hristidis", "databases, data systems, and information retrieval", "database infrastructure for traceable financial evidence and reproducible downstream decision studies"),
        ],
    },
    {
        "order": "14",
        "folder": "University of Technology Sydney",
        "school": "University of Technology Sydney",
        "program": "Doctor of Philosophy (PhD Thesis: Computer Science)",
        "contact": "Agreed supervision or faculty approval is required; contact a supervisor and develop the proposal before the formal application.",
        "lor": "Academic referee reports; confirm the current number and submission workflow in the live portal",
        "statement": "Research proposal written with the prospective supervisor, CV, and research-experience evidence",
        "source": "https://www.uts.edu.au/for-students/admissions-entry/how-to-apply/masters-by-research-phd",
        "special_checks": [
            "Attach evidence of agreed supervision or obtain documented faculty approval before submission",
            "Complete the FEIT/faculty pre-approval process when applying for a competitive scholarship",
            "Verify the scholarship closing date separately from the year-round admission pathway",
        ],
        "faculty": [
            ("Jie Lu", "concept drift, transfer learning, computational intelligence, and data-driven decision support", "drift-aware financial learning and decision support evaluated across changing market regimes with explicit evidence boundaries"),
            ("Guodong Long", "trustworthy machine learning, federated learning, privacy-preserving intelligence, and data science", "trustworthy financial ML infrastructure that combines personalised or federated learning with provenance, privacy, and temporal validation"),
            ("Guangquan Zhang", "fuzzy optimization, fuzzy machine learning, multi-objective and bilevel decision making", "multi-objective financial decision systems whose risk, cost, feasibility, and uncertainty constraints remain independently auditable"),
        ],
    },
    {
        "order": "15",
        "folder": "Curtin University",
        "school": "Curtin University",
        "program": "Doctor of Philosophy - Computing",
        "contact": "Supervisor support is a formal pre-application gate: submit an expression of interest with a topic and CV, then apply only if invited.",
        "lor": "Referee details and supporting evidence required by the current expression-of-interest and application forms",
        "statement": "Two-page research proposal plus a separate references page, prepared for the expression of interest",
        "source": "https://www.curtin.edu.au/study/offering/course-research-doctor-of-philosophy---computing--dr-comptg/?region=int",
        "special_checks": [
            "Submit the Expression of Interest before attempting the formal application",
            "Keep the proposal to two pages and place references on a separate additional page",
            "Proceed to the formal application only after the EOI succeeds and a supervisor supports the project",
        ],
        "faculty": [
            ("Aneesh Krishna", "artificial intelligence, data mining, machine learning, software engineering, and formal methods", "reliable financial ML software engineering with testable data contracts, model governance, and reproducible failure analysis"),
            ("Scott Lindstrom", "mathematical optimization, machine learning, and data science", "risk-aware optimization under market frictions and distribution shift, evaluated with leakage-resistant temporal protocols"),
            ("Sourav Das", "data science and statistics", "statistically disciplined evaluation of non-stationary financial models with uncertainty, sensitivity analysis, and reproducible evidence"),
        ],
    },
    {
        "order": "16",
        "folder": "Nanyang Technological University",
        "school": "Nanyang Technological University, Singapore",
        "program": "PhD in Computer Science and Engineering (College of Computing and Data Science)",
        "contact": "Targeted faculty contact is recommended, but first obtain written clarification of the CCDS GRE/GMAT rule for an overseas-degree applicant.",
        "lor": "2 academic references",
        "statement": "Research proposal where applicable, resume, Personal Statement, and verified research-output abstracts",
        "source": "https://www.ntu.edu.sg/admissions/graduate/radmissionguide",
        "special_checks": [
            "Obtain written CCDS clarification of the GRE/GMAT requirement for an overseas-degree applicant",
            "Keep the application at NO-GO if GRE/GMAT is mandatory and no waiver is granted",
            "Verify the CCDS-specific deadline and requirements rather than relying only on the central admission guide",
        ],
        "faculty": [
            ("Bo An", "multi-agent systems, computational game theory, reinforcement learning, optimization, and financial technology", "auditable reinforcement-learning and multi-agent decision infrastructure for financial markets with realistic costs and risk constraints"),
            ("Gao Cong", "data management, data mining, large-scale analytics, and databases for AI", "database support for point-in-time financial data, traceable feature generation, and reproducible ML experiments"),
            ("Anwitaman Datta", "distributed systems, data integrity, cybersecurity, decentralized finance, and technology governance", "resilient and auditable distributed financial systems connecting data integrity, operational risk, and bounded governance claims"),
            ("Sean Du Xuefeng", "reliable machine learning, uncertainty quantification, and robust open-world AI", "reliable financial learning under open-world distribution shifts with explicit uncertainty and failure-oriented evaluation"),
        ],
    },
]


def tex_escape(value: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in value)


def preamble(title: str, school: str, supervisor: str) -> str:
    return rf"""\documentclass[11pt]{{article}}
\usepackage[margin=0.82in]{{geometry}}
\usepackage[T1]{{fontenc}}
\usepackage{{lmodern,microtype,enumitem,tabularx,array,xcolor,hyperref,titlesec}}
\definecolor{{accent}}{{HTML}}{{173B57}}
\hypersetup{{colorlinks=true,urlcolor=accent,linkcolor=accent}}
\setlist{{nosep,leftmargin=*}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.55em}}
\widowpenalty=10000
\clubpenalty=10000
\displaywidowpenalty=10000
\titleformat{{\section}}{{\large\bfseries\color{{accent}}}}{{}}{{0pt}}{{}}
\titleformat{{\subsection}}{{\normalsize\bfseries}}{{}}{{0pt}}{{}}
\newcommand{{\ApplicantName}}{{Zhiheng Zhang}}
\newcommand{{\ApplicantEmail}}{{[CONFIRM EMAIL]}}
\newcommand{{\ApplicantPhone}}{{[CONFIRM PHONE]}}
\newcommand{{\ApplicantGitHub}}{{\href{{https://github.com/zhiheng-zhang-Mera/Quant-Ultra/tree/1988d9a8530da91a8158de864d098ea869098923}}{{Quant-Ultra @ 1988d9a}}}}
\pagestyle{{plain}}
\begin{{document}}
\begin{{center}}
{{\LARGE\bfseries {tex_escape(title)}}}\\[0.25em]
{{\large \ApplicantName}}\\
{tex_escape(school)} --- {tex_escape(supervisor)}
\end{{center}}
\vspace{{0.35em}}\hrule\vspace{{0.65em}}
"""


def closing() -> str:
    return "\\end{document}\n"


def academic_cv(school: dict, supervisor: str, area: str, hook: str) -> str:
    return preamble("Academic Curriculum Vitae", school["school"], supervisor) + rf"""
\textbf{{Contact}}: \ApplicantEmail\quad | \quad \ApplicantPhone\quad | \quad \ApplicantGitHub

\section*{{Research Profile}}
Computer-science-trained applicant focused on reliable machine-learning and data systems for non-stationary, high-stakes decisions. Primary work develops auditable, leakage-resistant financial ML research infrastructure; secondary work studies auditability and governance in privacy-sensitive software. Current fit with {tex_escape(supervisor)}: {tex_escape(hook)}.

\section*{{Education}}
\textbf{{University of Melbourne}} \hfill 2025--present\\
Postgraduate computing coursework and research project. \textit{{Exact degree title and expected completion date must be confirmed before submission.}}
\begin{{itemize}}
\item Completed coursework includes Research Methods (69), Machine Learning Applications for Health (76), Information Visualization (70), and Evaluating User Experience (78).
\item Computer Science Research Project in progress; the supplied progress record shows 30/40 for proposal and oral-presentation components, with remaining project components pending.
\end{{itemize}}

\textbf{{The University of British Columbia, Okanagan}} \hfill 2020--2024\\
Bachelor of Science program and computing coursework. \textit{{The supplied 2024 transcript lists no credential to date; confirm completion, exact awarded major, and conferral date against the degree certificate before changing this wording.}}
\begin{{itemize}}
\item Selected results: Capstone Software Engineering Project 93; Databases 90 on successful retake; Image Processing 88; Data Analytics 86; Software Engineering 86; Numerical Analysis 85; Analysis of Algorithms 82.
\item Academic record shows a clear later-stage improvement in advanced computing and project-based work.
\end{{itemize}}

\section*{{Research and Engineering Projects}}
\textbf{{Quant-Ultra --- Auditable Financial ML Research Infrastructure}}
\begin{{itemize}}
\item Builds point-in-time data, temporal-leakage controls, walk-forward evaluation, transaction-cost-aware backtesting, risk-aware decisions, monitoring, and machine-readable audit evidence.
\item Treats stage completion as engineering evidence rather than investment validity; failed governance or reconciliation evidence triggers review-only outputs.
\item Research direction for this application: {tex_escape(hook)}.
\end{{itemize}}

\begin{{samepage}}
\textbf{{Privacy Lens --- Trustworthy Software and Compliance Evidence}}
\begin{{itemize}}
\item Explores auditability, provenance, replay boundaries, and fail-closed handling in privacy-sensitive software.
\item Provides a second domain for studying how technical systems should state evidence limits and avoid unsupported real-world claims.
\end{{itemize}}
\end{{samepage}}

\section*{{Technical Preparation}}
Python; data structures and algorithms; databases; numerical methods; probability and statistics; machine learning; software engineering; data analytics; experiment design; research communication. \textit{{Replace this list with verified tools, languages, and proficiency levels before submission.}}

\section*{{Research Interests}}
{tex_escape(area)}; reliable ML systems; temporal data validity; non-stationarity and distribution shift; data provenance; risk-aware optimization; trustworthy decision systems.

\section*{{References}}
Three referees are planned: the Melbourne research supervisor, a CS/ML/algorithms academic, and an academic able to assess later-stage UBC project work. Names and institutional contact details must be added only after consent.
""" + closing()


def research_cv(school: dict, supervisor: str, area: str, hook: str) -> str:
    return preamble("Research Curriculum Vitae", school["school"], supervisor) + rf"""
\textbf{{Contact}}: \ApplicantEmail\quad | \quad \ApplicantPhone\quad | \quad \ApplicantGitHub

\section*{{Research Objective}}
I seek doctoral training in reliable machine-learning and data systems for non-stationary, high-stakes environments. My central question is how a research system can make temporal validity, data provenance, model uncertainty, decision constraints, and claim boundaries inspectable rather than implicit. The proposed collaboration with {tex_escape(supervisor)} focuses on {tex_escape(hook)}.

\section*{{Education and Evidence of Preparation}}
\textbf{{University of Melbourne, postgraduate computing study}} \hfill 2025--present
\begin{{itemize}}
\item Research Methods (69), Machine Learning Applications for Health (76), Information Visualization (70), Evaluating User Experience (78), plus advanced algorithms, databases, machine learning, and social computing.
\item Current Computer Science Research Project: supplied progress record reports 30/40 across the proposal and oral-presentation components; the remaining 60 percent is pending. This is reported as progress evidence, not as a final thesis result.
\end{{itemize}}

\textbf{{The University of British Columbia, Okanagan, Bachelor of Science program}} \hfill 2020--2024\\
\textit{{The supplied transcript lists no credential to date; verify the final award and conferral wording from the degree certificate.}}
\begin{{itemize}}
\item Strong later-stage evidence in Capstone Software Engineering (93), Databases retake (90), Image Processing (88), Data Analytics and Software Engineering (86 each), Numerical Analysis (85), Algorithms (82), and Computer Ethics (84).
\item The transcript also contains weaker early and individual results. Applications should present the full record and use research artifacts and referee evidence to explain growth without minimizing the record.
\end{{itemize}}

\section*{{Primary Project: Quant-Ultra}}
\textbf{{Problem.}} Financial ML experiments are unusually vulnerable to time leakage, survivorship and feature availability errors, unstable regimes, cost-blind objectives, and post-hoc selection. A numerically attractive backtest is not decision-grade evidence if its data and evaluation path cannot be reconstructed.

\textbf{{System direction.}} Quant-Ultra is framed as research infrastructure rather than a stock-picking product. It connects point-in-time data construction, leakage-resistant fold design, walk-forward evaluation, execution assumptions, transaction costs, risk-aware portfolio decisions, monitoring, reconciliation, and an audit trail. The design makes failure states visible and separates pipeline success from claims of investment validity.

\textbf{{Research contribution sought.}} The doctoral extension would formalize temporal data contracts, evaluate robustness across regimes and data perturbations, compare constrained decision rules, and study which provenance and monitoring evidence is sufficient for reproducibility. In the context of {tex_escape(supervisor)}'s work, the most direct bridge is {tex_escape(hook)}.

\textbf{{Evaluation principles.}}
\begin{{itemize}}
\item Use time-respecting train/validation/test splits, embargo where relevant, and fold-local parameter selection.
\item Separate predictive metrics from economic utility and report turnover, costs, risk, and sensitivity.
\item Preserve negative and failed runs; require reconciliation and governance evidence before decision-oriented output.
\item Compare against simple baselines and report uncertainty instead of selecting only favorable intervals.
\end{{itemize}}

\section*{{Secondary Project: Privacy Lens}}
Privacy Lens provides a second testbed for trustworthy software. Its contribution to the application is methodological: fail-closed validation, provenance, replay limits, audit records, and careful separation between simulator evidence and broad real-world claims. The connection to Quant-Ultra is a common concern with accountable software behavior, not an assertion that privacy compliance and financial prediction are the same problem.

\section*{{Methods and Preparation}}
Preparation includes algorithms, databases, numerical analysis, probability, statistics, machine learning, data analytics, software engineering, human-computer interaction, ethics, and research methods. Current methodological interests include temporal validation, distribution-shift diagnostics, constrained optimization, data-quality contracts, experiment lineage, and interpretable failure analysis.

\section*{{Research Outputs and Open-Science Plan}}
No publication is claimed in the supplied evidence. Before submission, add only verified releases, archived commits, preprints, talks, or thesis artifacts. Planned artifact practice includes immutable experiment configurations, data-snapshot identifiers, environment manifests, test suites, negative-result logs, and concise model/data cards.

\section*{{References}}
Referee names are intentionally withheld until consent is confirmed. The target mix is a current research supervisor, an academic who can evaluate mathematical/ML depth, and an academic who can evaluate the later UBC engineering trajectory.
""" + closing()


def sop(school: dict, supervisor: str, area: str, hook: str) -> str:
    return preamble("Statement of Purpose", school["school"], supervisor) + rf"""
I want to study a deceptively simple question: when should we trust the output of a machine-learning research pipeline operating on changing data? In financial applications, a model may look successful because future information entered a feature, a universe was reconstructed with hindsight, hyperparameters were selected on the test period, transaction costs were ignored, or one favorable regime dominated the result. My goal is to build data and ML systems that make those failure modes testable and that preserve enough evidence for another researcher to reproduce, challenge, or reject a conclusion.

My preparation combines computer science training in the Bachelor of Science program at the University of British Columbia with postgraduate computing coursework and an ongoing research project at the University of Melbourne. My undergraduate record is uneven, but it also documents meaningful improvement. Later results include 93 in the capstone software engineering project, 90 in databases on a successful retake, 88 in image processing, 86 in both data analytics and software engineering, 85 in numerical analysis, and 82 in analysis of algorithms. At Melbourne, my strongest completed results include 78 in Evaluating User Experience, 76 in Machine Learning Applications for Health, 70 in Information Visualization, and 69 in Research Methods. I do not present these numbers as a substitute for research potential; instead, they show the trajectory that led me toward more disciplined, project-centered work. The final UBC degree award and exact Melbourne degree title will be stated only after the corresponding official documents are added.

That trajectory is clearest in Quant-Ultra, my primary research and engineering project. I frame Quant-Ultra as auditable, leakage-resistant infrastructure for financial ML, not as a trading product. The system is intended to connect point-in-time data construction, temporal validation, walk-forward backtesting, transaction-cost assumptions, risk-aware decisions, monitoring, and machine-readable governance evidence. A central design principle is that completing every pipeline stage does not prove investment validity. Reconciliation failures, missing provenance, weak baselines, or unstable model checks should lead to a review-only outcome rather than an overstated recommendation.

This engineering work has shaped a research agenda. I want to formalize temporal data contracts, study how distribution shifts interact with model selection, evaluate constrained decision rules under realistic frictions, and identify the minimum evidence needed for a result to be reproducible and decision-relevant. The project also raises systems questions: how should large experiment graphs preserve data lineage; how can monitoring distinguish a data failure from a genuine regime change; and how should an infrastructure expose uncertainty to researchers without hiding it behind a single score?

My secondary project, Privacy Lens, gives me another view of the same methodological problem. It studies auditability, provenance, replay boundaries, and fail-closed behavior in privacy-sensitive software. I use it in this application as evidence of a broader interest in trustworthy systems and bounded claims. I do not equate compliance simulation with legal validity, just as I do not equate a successful backtest with investment validity. In both settings, the research value lies in designing systems that state what their evidence does and does not support.

{tex_escape(school['school'])} is a strong setting for this agenda because the {tex_escape(school['program'])} can connect rigorous computer science with consequential data-driven decisions. I am particularly interested in {tex_escape(supervisor)}'s work on {tex_escape(area)}. A concrete starting point would be {tex_escape(hook)}. I would bring an existing problem formulation and engineering testbed, while seeking deeper training in theory, experimental design, and the relevant systems or learning methods. I also see value in collaborating beyond a single application domain: the same temporal-validity and provenance questions arise in scientific, health, and operational data systems.

In doctoral study, I would begin by constructing a reproducible benchmark suite for temporal data and evaluation failures. I would then compare methods under controlled distribution shifts and realistic decision constraints, preserving both positive and negative results. The objective would not be to claim universal market predictability. It would be to produce general methods, open artifacts, and empirically defensible guidance for building reliable ML and data systems in non-stationary environments.

My long-term goal is to work as a researcher or research engineer at the intersection of ML systems, data infrastructure, and quantitative decision-making. I want to contribute tools that let research teams move faster without weakening evidentiary standards. Doctoral training at {tex_escape(school['school'])}, and especially the opportunity to learn from {tex_escape(supervisor)}, would help me turn a production-oriented prototype into a precise and publishable research program.

\textit{{Submission note: adapt this draft to the live prompt and word limit. Do not submit until the bracketed contact fields, exact Melbourne degree title, project links, and any verified thesis details have been completed.}}
""" + closing()


def research_statement(school: dict, supervisor: str, area: str, hook: str) -> str:
    return preamble("Research Statement", school["school"], supervisor) + rf"""
\section*{{Research Vision}}
My research goal is to make machine-learning evidence dependable in non-stationary, high-stakes environments. I focus on the infrastructure between raw data and a decision: temporal data construction, experiment design, model selection, constrained optimization, monitoring, provenance, and claim governance. Financial ML is my primary application because it combines severe distribution shift with strong incentives to overfit; the methods should generalize to other temporal decision systems.

\section*{{1. Auditable Temporal Data and Evaluation}}
Point-in-time correctness is often discussed as a dataset property, but in practice it is a system property. A feature can be temporally correct at ingestion and still leak information through revision handling, universe construction, imputation, cross-validation, or parameter tuning. I propose explicit temporal data contracts that record availability time, effective time, revision policy, and permitted downstream transformations. Experiments would inject controlled contract violations and measure which checks detect them, which metrics are distorted, and which downstream decisions change.

The empirical design would combine synthetic controls, where the ground truth of a leak is known, with carefully versioned public financial datasets. Evaluation would use walk-forward folds, fold-local preprocessing and selection, embargo where dependence requires it, simple baselines, and sensitivity analyses. The output would be a benchmark of failure modes and a reference implementation whose lineage can be independently inspected.

\section*{{2. Learning and Decisions under Shift and Friction}}
Predictive performance does not directly translate into decision quality. A model can improve an average error metric while producing an unstable or infeasible portfolio after turnover, costs, liquidity, and risk constraints. I therefore want to study learning and optimization as a coupled but separately auditable pipeline. Models would be evaluated across regime partitions and controlled shifts; decision rules would be compared under identical information sets and explicit cost models.

The emphasis is not on reporting the best Sharpe ratio. It is on understanding when apparent gains survive alternative windows, delayed information, higher costs, simpler baselines, and uncertainty in estimated parameters. Negative results would be preserved. Governance gates would prevent a decision-oriented result when reconciliation, provenance, or robustness checks fail.

\section*{{3. Systems for Reproducible Research}}
Large experiment programs create operational questions that are themselves researchable: how to identify equivalent data snapshots, cache without contaminating folds, schedule dependent experiments, trace a reported number back to code and data, and surface failures without overwhelming the researcher. Quant-Ultra is an initial testbed for studying these questions. I plan to develop immutable run fingerprints, typed stage contracts, data-quality assertions, resource-aware execution, and evidence bundles that connect a table or figure to its generating configuration.

Privacy Lens provides a complementary testbed for fail-closed validation and bounded interpretation. Its role is to test whether provenance and governance patterns transfer across domains, while respecting the fact that simulator evidence does not establish legal compliance or broad device behavior.

\section*{{Fit and Proposed Collaboration}}
At {tex_escape(school['school'])}, I am particularly interested in {tex_escape(supervisor)}'s research on {tex_escape(area)}. The proposed bridge is {tex_escape(hook)}. This fit would let me deepen the theoretical or systems foundations of the work while contributing an existing implementation context, a strong concern for reproducibility, and a willingness to report failure modes as research results.

\section*{{Expected Contributions}}
\begin{{enumerate}}
\item A taxonomy and benchmark suite for temporal-data and evaluation failures in non-stationary ML.
\item Methods for drift-aware, cost-aware, and risk-constrained evaluation that separate prediction from decisions.
\item A reproducible systems architecture linking data contracts, experiment lineage, monitoring, and governance gates.
\item Open artifacts and reporting templates that state evidence boundaries and preserve negative results.
\end{{enumerate}}

Success would be measured by detection coverage, reproducibility, robustness across shifts and assumptions, computational cost, and clarity of claim boundaries---not by a single favorable backtest.
""" + closing()


def proposal(school: dict, supervisor: str, area: str, hook: str) -> str:
    return preamble("Research Proposal", school["school"], supervisor) + rf"""
\setlength{{\parskip}}{{0.45em}}
\textbf{{Provisional title:}} Auditable Financial Machine Learning under Temporal Leakage, Distribution Shift, and Market Frictions

\section*{{Motivation and Problem}}
Financial ML is a useful stress test for reliable data and learning systems. Data are revised, assets enter and leave the observable universe, market regimes change, decisions incur costs, and repeated experimentation makes accidental selection bias likely. Many studies treat these concerns as reporting details. This proposal treats them as coupled systems and methodological problems: how can an experiment ensure that every decision uses only information available at that time, how can a result remain reproducible across data and code revisions, and how can a system prevent weak evidence from being promoted into a decision claim?

\section*{{Research Questions}}
\begin{{enumerate}}
\item Which temporal data contracts are necessary to detect leakage introduced by data revisions, universe construction, feature transformation, cross-validation, and model selection?
\item How should evaluation separate predictive quality, decision utility, market frictions, and uncertainty under distribution shift?
\item Which provenance, reconciliation, and monitoring evidence is sufficient for an independent researcher to reproduce or falsify a reported result?
\item Can fail-closed governance gates reduce unsupported claims without making the research workflow unusably rigid?
\end{{enumerate}}

\section*{{Methodology}}
\textbf{{Work package 1: temporal contract benchmark.}} I will define machine-readable contracts for observation time, effective time, revision state, universe membership, and permitted transformations. A benchmark suite will inject known violations into synthetic and versioned real-data pipelines. Detection coverage, false alarms, downstream metric distortion, and decision impact will be measured.

\textbf{{Work package 2: shift-aware evaluation.}} Models will be trained and selected using rolling or expanding windows with fold-local preprocessing and hyperparameter governance. Tests will include natural regime partitions and controlled perturbations to feature distributions, missingness, noise, and label relationships. Comparisons will include simple statistical and ML baselines. Results will report dispersion across folds and regimes rather than only a pooled average.

\textbf{{Work package 3: decision layer with frictions.}} Predictive outputs will feed explicit decision rules subject to turnover, transaction-cost, exposure, concentration, and risk constraints. The study will vary cost and liquidity assumptions and will distinguish forecast metrics from decision outcomes. Any economic result will be presented as historical experimental evidence, not as prospective investment advice.

\textbf{{Work package 4: reproducible systems and governance.}} Each run will preserve code revision, environment, data snapshot identifiers, configuration, random seeds, stage results, and reconciliation checks. Typed stage contracts will prevent downstream use of missing or invalid evidence. A governance layer will issue research-only, observation-only, or hold-for-review outcomes based on predefined checks. Human-subject, legal, and investment-validity claims remain outside scope unless separately established.

\section*{{Evaluation}}
The evaluation will measure: (i) leak-detection precision and recall on injected failures; (ii) reproducibility of tables and figures from archived evidence; (iii) sensitivity of model and decision rankings to regimes, costs, and reasonable hyperparameter choices; (iv) computational overhead of lineage and checks; and (v) analyst usability through task-based studies if ethics approval and resources permit. Ablations will isolate temporal contracts, monitoring, optimization constraints, and governance gates.

\section*{{Expected Contribution and Fit}}
The expected contribution is not a universal trading algorithm. It is a set of methods and open infrastructure for more credible research on temporal decision systems. The work would contribute a failure-mode benchmark, explicit data/evaluation contracts, robust decision-evaluation protocols, and an auditable reference architecture.

The proposed fit with {tex_escape(supervisor)} is {tex_escape(hook)}, grounded in their broader work on {tex_escape(area)}. At {tex_escape(school['school'])}, this project could connect financial ML with data systems, optimization, trustworthy AI, or ML systems while retaining a precise empirical core.

\section*{{Risks and Mitigations}}
Financial data access may limit redistribution; the benchmark will therefore combine public or redistributable sources with synthetic generators and publish transformation code rather than restricted raw data. Market results may be unstable; instability is treated as a finding and evaluated across regimes. System complexity may obscure causal conclusions; preregistered ablations and simple baselines will keep individual claims testable. Any claims about legal compliance, deployment safety, or future financial performance are explicitly excluded.

\section*{{Indicative Timeline}}
Year 1: literature review, formal problem definitions, temporal-contract benchmark, and baseline pipeline. Year 2: shift-aware learning studies and decision layer. Year 3: reproducible systems architecture, governance experiments, and cross-domain validation. Final period: integrated evaluation, publications, open artifacts, and dissertation.

\section*{{Selected Literature to Verify and Expand}}
Before submission, replace this section with a supervisor-specific bibliography verified against current papers. Core areas are backtest overfitting, concept drift, time-series validation, data provenance, ML reproducibility, constrained portfolio optimization, and trustworthy ML systems. No unverified citation has been inserted into this draft.
""" + closing()


def quant_summary(school: dict, supervisor: str, hook: str) -> str:
    return preamble("Quant-Ultra: One-Page Research Summary", school["school"], supervisor) + rf"""
\textbf{{Positioning.}} Quant-Ultra is an auditable, leakage-resistant research infrastructure project for financial machine learning. It is not presented as a validated investment product.

\textbf{{Problem.}} Financial ML can produce attractive but non-reproducible results when future information enters features, assets are selected with hindsight, model choices reuse test evidence, costs are omitted, or weak diagnostics are hidden behind an aggregate metric.

\textbf{{System concept.}}
\begin{{itemize}}
\item Point-in-time data construction and explicit feature-availability rules.
\item Time-respecting walk-forward evaluation with fold-local selection.
\item Transaction-cost-aware backtesting and risk-constrained decisions.
\item Monitoring for drift, anomalies, and evidence-quality failures.
\item Run fingerprints, reconciliation, stage contracts, and audit bundles.
\item Fail-closed governance: missing or failed evidence leads to hold-for-review or observation-only output.
\end{{itemize}}

\textbf{{Research questions.}} Which temporal contracts detect the most consequential leakage? How stable are model and decision rankings across regimes and cost assumptions? What evidence is sufficient to reproduce a claim? How can governance checks remain strict without preventing useful iteration?

\textbf{{Targeted doctoral extension.}} With {tex_escape(supervisor)}, I would study {tex_escape(hook)}.

\textbf{{Evidence boundary.}} A completed run, passing software tests, or a favorable historical metric does not establish investment validity or future performance. The project is designed to make that boundary operational and visible.

\textbf{{Artifact link.}} \ApplicantGitHub
""" + closing()


def privacy_summary(school: dict, supervisor: str) -> str:
    return preamble("Privacy Lens: One-Page Research Summary", school["school"], supervisor) + r"""
\textbf{Positioning.} Privacy Lens is a trustworthy-software research prototype used to study auditability, provenance, replay boundaries, and fail-closed validation in privacy-sensitive application flows.

\textbf{Research value.} The project asks how a software system can preserve the source and context of an event, reject invalid or unsafe inputs, and generate audit evidence whose interpretation is explicit. It treats simulator output and short device tests as bounded engineering evidence, not as proof of universal device behavior or legal compliance.

\textbf{Connection to Quant-Ultra.} The projects share a methodology: evidence should be traceable, invalid inputs should fail closed, and successful execution should not be confused with external validity. Privacy Lens supplies a second domain in which to test governance and provenance patterns. It remains secondary in this application so that the research narrative stays coherent.

\textbf{Potential doctoral relevance.} The reusable questions concern provenance schemas, evidence contracts, monitoring, reproducible replay, human-readable audit records, and the boundary between technical checks and broader claims. These ideas can inform trustworthy data and ML systems without asserting that privacy compliance and financial modeling are interchangeable.

\textbf{Artifact link.} [CONFIRM PRIVACY LENS PERMALINK AND THESIS/REPORT LINK BEFORE SENDING]
""" + closing()


def cover_note(school: dict, supervisor: str) -> str:
    return preamble("Writing Sample Cover Note", school["school"], supervisor) + r"""
Please find attached my strongest completed thesis or research report. The sample is submitted to demonstrate problem formulation, methodological discipline, implementation, evidence interpretation, and research writing.

The final writing sample itself is not present in the supplied repository and has therefore not been invented or reconstructed. Before submission:
\begin{enumerate}
\item insert the verified title, institution, course or thesis context, date, and individual contribution;
\item attach the complete original sample in the format required by the application portal;
\item remove assessor comments or personal data only if permitted, while preserving the integrity of the work;
\item confirm that any co-authorship and reused material are clearly disclosed.
\end{enumerate}

\textbf{Verified sample title:} [ADD]\\
\textbf{Context and date:} [ADD]\\
\textbf{Individual contribution:} [ADD]\\
\textbf{Related artifact or repository:} [ADD]
""" + closing()


def email_md(school: dict, supervisor: str, area: str, hook: str) -> str:
    low_roi = any(term in school["contact"].lower() for term in ["do not", "departmental admission", "departmental application"])
    status = "OPTIONAL DRAFT - DO NOT MASS-SEND" if low_roi else "TARGETED OUTREACH DRAFT"
    student_id = "\n> Add the Concordia Student ID before sending." if school["folder"] == "Concordia University" else ""
    return f"""# Contact email to {supervisor}

> Status: **{status}**
> School strategy: {school['contact']}
> Verify the professor's current title, email address, recent work, and 2027 recruiting status on the official profile before sending.{student_id}

**Subject:** Prospective 2027 PhD applicant - auditable ML/data systems under temporal shift

Dear Professor {supervisor.split()[-1]},

My name is Zhiheng Zhang. My background includes computer science training in the Bachelor of Science program at the University of British Columbia, and I am currently undertaking postgraduate computing study and a research project at the University of Melbourne. I am preparing an application to the {school['program']} at {school['school']} for 2027 entry.

My main project, Quant-Ultra, is an auditable, leakage-resistant research infrastructure for financial machine learning. It connects point-in-time data construction, walk-forward evaluation, transaction-cost and risk constraints, monitoring, and machine-readable audit evidence. The project deliberately separates engineering checks and historical experimental results from claims of investment validity.

I am writing because your work on {area} appears closely related to a doctoral direction I want to pursue: {hook}. I would be grateful to know whether this direction could fit your group and whether you expect to consider new PhD students for the 2027 intake.

I have attached a concise research CV, a one-page Quant-Ultra summary, my research proposal, and the available academic records. If the direction is relevant to your current work, I would be happy to discuss a narrower research question or provide any additional information that would help you assess fit.

Thank you for your time and consideration.

Best regards,<br>
Zhiheng Zhang<br>
[CONFIRM EMAIL]<br>
[CONFIRM PHONE]<br>
https://github.com/zhiheng-zhang-Mera/Quant-Ultra/tree/1988d9a8530da91a8158de864d098ea869098923

## Attachments to send

- `02_Research_CV.tex` compiled to PDF after filling all placeholders
- `05_Research_Proposal.tex` compiled to PDF
- `06_Quant_Ultra_Research_Summary.tex` compiled to a one-page PDF
- Official UBC transcript and current Melbourne academic evidence
- Add the full writing sample only if relevant and requested

## Follow-up rule

If there is no response, send one concise follow-up after 7-10 days. Do not send repeated reminders and do not send the same wording to multiple faculty members.
"""


def checklist_md(school: dict, supervisor: str) -> str:
    special_checks = school.get("special_checks", [])
    special_section = ""
    if special_checks:
        special_section = "\n## School-specific gates\n\n" + "\n".join(
            f"- [ ] {item}" for item in special_checks
        ) + "\n"
    return f"""# Application checklist - {school['school']} - {supervisor}

Last package build: 2026-08-15. Treat dates and portal wording as time-sensitive and re-check the official page 30 days before submission.

Official starting point: {school['source']}

## Authored materials in this folder

- [ ] Fill contact, degree-title, project-link, and referee placeholders in both CVs.
- [ ] Adapt `03_Statement_of_Purpose.tex` to the live prompt and word limit.
- [ ] Verify every claim in `04_Research_Statement.tex` and `05_Research_Proposal.tex`.
- [ ] Replace the placeholder bibliography with current, verified literature.
- [ ] Compile and visually inspect every TeX source before portal upload.
- [ ] Use `08_Contact_Email.md` only in line with this strategy: {school['contact']}

## Program package

- [ ] Online application and fee or approved fee waiver
- [ ] Resume / Academic CV and Research CV
- [ ] {school['statement']}
- [ ] {school['lor']}
- [ ] Transcripts from every post-secondary institution
- [ ] Degree certificate(s) or current-enrolment / expected-completion evidence
- [ ] Official grading scale or legend where requested
- [ ] English-proficiency score or accepted official medium-of-instruction evidence
- [ ] Passport / identity document
- [ ] Writing sample if required or beneficial
- [ ] Verified permanent project links, release tags, and commit hashes
- [ ] Supervisor field / consent evidence where required
{special_section}
## Current supervisor/contact gate

- [ ] Verify {supervisor}'s current institutional profile and email
- [ ] Read at least two recent relevant papers or project pages
- [ ] Replace the broad research hook with one precise, accurate connection
- [ ] Confirm 2027 student capacity before treating any reply as a positive signal
- [ ] Save replies and any supervision commitment in the application record

## Missing user-supplied official items

- [ ] Exact University of Melbourne degree title and expected completion date
- [ ] Current official Melbourne transcript
- [ ] UBC degree certificate
- [ ] Melbourne enrolment / expected-completion letter or final certificate when available
- [ ] Official medium-of-instruction evidence if the portal requires it
- [ ] Passport / ID scan
- [ ] English-test evidence if no exemption applies
- [ ] Consenting referee names, titles, institutional emails, and submission status
- [ ] Complete thesis or research-report writing sample
- [ ] Verified Quant-Ultra and Privacy Lens permanent links

## Final claim-boundary review

- [ ] No publication, award, employment, language score, GPA conversion, ranking, or supervisor interest is claimed without evidence.
- [ ] Quant-Ultra is described as research infrastructure, not investment advice or proven future performance.
- [ ] Privacy Lens engineering evidence is not described as legal compliance or universal device validation.
- [ ] The complete transcript is submitted; the academic trajectory is contextualized but no weak result is hidden.
"""


def fact_check_md(school: dict, supervisor: str, area: str, hook: str) -> str:
    return f"""# Fact-check record

## Safe to use from supplied evidence

- Applicant name: Zhiheng Zhang.
- The supplied UBC transcript records enrollment in a Bachelor of Science program but says `Credentials: None to date`; degree completion must not be claimed until a degree certificate or final transcript is added.
- UBC transcript date: 2024-08-28; it contains the course results cited in the drafts.
- UBC later-stage evidence includes capstone 93, databases retake 90, image processing 88, data analytics 86, software engineering 86, numerical analysis 85, and algorithms 82.
- Melbourne WAM image lists the 2025 coursework and an in-progress 2026 Computer Science Research Project; the image labels the remaining project component as TBD.
- Application positioning and project descriptions follow the repository's 2027 plan.

## Must be verified before submission

- Exact Melbourne degree title, enrollment status, expected completion date, and current official grades.
- Exact UBC degree major and conferral wording from the degree certificate.
- All contact details, project URLs, releases, commit hashes, and individual contributions.
- Any publication, preprint, award, scholarship, internship, employment, ranking, GPA/WAM summary, or language-test claim.
- Current research area and recruiting status of {supervisor}; the working fit is `{area}` and the proposed hook is `{hook}`.
- The live 2027 requirements and deadline at {school['school']}.

## Official source used for the package checklist

{school['source']}

The source URL is a starting point, not proof that the page will remain unchanged. Save a dated PDF/screenshot of the live requirement page when the application is submitted.
"""


def readme_md(school: dict, supervisor: str) -> str:
    return f"""# {school['school']} - {supervisor}

Program: **{school['program']}**

Contact strategy: **{school['contact']}**

This is a self-contained working package. Authored documents that will eventually be PDFs are supplied as LaTeX source, as requested. The official UBC transcript remains an original PDF attachment and the Melbourne WAM evidence remains its original image; neither has been reconstructed.

## Files

- `01_Academic_CV.tex` - concise academic CV
- `02_Research_CV.tex` - research-focused CV
- `03_Statement_of_Purpose.tex` - school and faculty-fit statement
- `04_Research_Statement.tex` - reusable research agenda
- `05_Research_Proposal.tex` - full proposal draft
- `06_Quant_Ultra_Research_Summary.tex` - one-page project summary
- `07_Privacy_Lens_Research_Summary.tex` - secondary project summary
- `08_Contact_Email.md` - individualized outreach draft and sending rule
- `09_Application_Checklist.md` - program materials and unresolved official items
- `10_Fact_Check.md` - claim ledger for this package
- `11_Writing_Sample_Cover_Note.tex` - cover note; the actual sample is still required
- `Attachments/` - supplied official/background evidence

## Before any external use

Search all files for `CONFIRM`, `ADD`, `TBD`, and square-bracket placeholders. Complete those fields, verify the professor's current profile and the live portal requirements, compile the TeX files, and visually inspect the resulting PDFs. Drafts marked as low-ROI or department-only should not be sent merely because they exist.
"""


def root_index() -> str:
    rows = []
    for s in SCHOOLS:
        rows.append(f"| {s['order']} | {s['school']} | {s['program']} | {len(s['faculty'])} | {s['contact']} |")
    return """# 2027 PhD application packages

Generated from the application plan and the supplied background evidence on 2026-08-15.

Every final supervisor folder contains the authored application materials, a tailored email draft, a program checklist, a fact-check ledger, and copies of the supplied academic evidence. TeX source is used for every newly authored document intended to become a PDF. Original official evidence remains in its original format.

| Priority | School | Program | Supervisor packages | Outreach strategy |
|---:|---|---|---:|---|
""" + "\n".join(rows) + """

## Important limitations

- These are complete drafts, not submission-ready official records. The repository does not contain a current official Melbourne transcript, degree certificates, passport, English evidence, referee identities, or the complete writing sample.
- No publication, award, employment, rank, converted GPA, or supervisor interest is asserted.
- Faculty research hooks come from the plan and must be checked against current official profiles and recent work before sending.
- HKUST CSE is treated as requiring a faculty member who agrees to supervise because its current FAQ says so; do not rely on the older optional-contact classification.
- Department-level programs include individual faculty-fit packages for organization, but their email files are clearly marked as optional or not for mass outreach.

## Build and validation

Run:

```powershell
python tools/build_application_packages.py
python tools/validate_application_packages.py
```

Compile TeX only after replacing placeholders. A compile check can still be run on drafts because placeholders are TeX-safe, but visual and factual approval is required before external use.

## D-drive QA environment

The verified local TeX environment is installed at `D:\\PhD-Tools\\TinyTeX` (TeX Live 2026). Because TeX cannot reliably create logs beneath the repository's non-ASCII path, the compile script copies each source to an ASCII-only staging folder under `D:\\PhD-Tools\\qa-input` and writes QA PDFs/logs under `D:\\PhD-Tools\\qa-output`.

```powershell
python tools/build_application_packages.py
python tools/validate_application_packages.py
python tools/compile_application_packages.py --workers 8
python tools/render_qa_representatives.py
```

The compile and render manifests are written below `tmp/pdfs/` and are intentionally ignored by Git.
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def build() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT / "README.md", root_index())
    for school in SCHOOLS:
        school_dir = OUT / f"{school['order']}_{school['folder']}"
        for supervisor, area, hook in school["faculty"]:
            target = school_dir / supervisor
            attachments = target / "Attachments"
            attachments.mkdir(parents=True, exist_ok=True)
            write(target / "00_README.md", readme_md(school, supervisor))
            write(target / "01_Academic_CV.tex", academic_cv(school, supervisor, area, hook))
            write(target / "02_Research_CV.tex", research_cv(school, supervisor, area, hook))
            write(target / "03_Statement_of_Purpose.tex", sop(school, supervisor, area, hook))
            write(target / "04_Research_Statement.tex", research_statement(school, supervisor, area, hook))
            write(target / "05_Research_Proposal.tex", proposal(school, supervisor, area, hook))
            write(target / "06_Quant_Ultra_Research_Summary.tex", quant_summary(school, supervisor, hook))
            write(target / "07_Privacy_Lens_Research_Summary.tex", privacy_summary(school, supervisor))
            write(target / "08_Contact_Email.md", email_md(school, supervisor, area, hook))
            write(target / "09_Application_Checklist.md", checklist_md(school, supervisor))
            write(target / "10_Fact_Check.md", fact_check_md(school, supervisor, area, hook))
            write(target / "11_Writing_Sample_Cover_Note.tex", cover_note(school, supervisor))
            shutil.copyfile(DOCS / "Transcript-ZhihengZhang.pdf", attachments / "Transcript-ZhihengZhang.pdf")
            shutil.copyfile(DOCS / "Master-WAM.png", attachments / "Master-WAM.png")


if __name__ == "__main__":
    build()
