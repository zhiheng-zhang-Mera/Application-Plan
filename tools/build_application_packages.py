from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Applications"
DOCS = ROOT / "Documents"


SCHOOLS = [
    {
        "order": "01",
        "folder": "香港科技大学（广州） (HKUST Guangzhou)",
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
        "folder": "澳门大学 (University of Macau)",
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
        "folder": "德雷塞尔大学 (Drexel University)",
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
        "folder": "北卡罗来纳州立大学 (NC State University)",
        "school": "North Carolina State University",
        "program": "PhD in Computer Science",
        "contact": "Departmental admission; selective faculty contact is recommended but not required.",
        "lor": "3 recommendations from people qualified to assess graduate-study potential",
        "statement": "Personal statement and a two-page resume or curriculum vitae",
        "source": "https://csc.ncsu.edu/academics/graduate/application-procedure/",
        "faculty": [
            ("Timothy Menzies", "data science, artificial intelligence, and software engineering", "data-light and explainable methods for reliable ML software whose claims remain testable under temporal shift"),
            ("Xiaohui Gu", "distributed systems, cloud computing, and machine-learning systems", "self-managing distributed infrastructure for reproducible point-in-time financial ML experiments and monitoring"),
            ("Xipeng Shen", "programming systems, data-intensive computing, and machine-learning systems", "efficient data-intensive infrastructure for traceable financial ML training, evaluation, and deployment"),
            ("Dongkuan Xu", "efficient, robust, and trustworthy generative and agentic AI systems", "reliable agentic financial research workflows with explicit provenance, resource controls, and evidence boundaries"),
        ],
    },
    {
        "order": "05",
        "folder": "纽约州立大学布法罗分校 (University at Buffalo)",
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
        "folder": "康考迪亚大学 (Concordia University)",
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
        "folder": "香港理工大学 (The Hong Kong Polytechnic University)",
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
        "folder": "香港城市大学 (City University of Hong Kong)",
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
        "folder": "康涅狄格大学 (University of Connecticut)",
        "school": "University of Connecticut",
        "program": "PhD in Computer Science and Engineering",
        "contact": "Individual faculty admit PhD students directly into their research groups; targeted contact is required.",
        "lor": "3 letters of recommendation, including at least one addressing readiness for independent research",
        "statement": "Personal statement covering graduate aspirations, relevant background, and research preparation",
        "source": "https://computing.engineering.uconn.edu/graduate-studies/ph-d-program/",
        "faculty": [
            ("Dongjin Song", "machine learning, deep learning, time-series analysis, and graph representation learning", "time-series and graph learning for changing financial regimes with leakage-resistant evaluation"),
            ("Jinbo Bi", "machine learning, data mining, distributed computing, and optimization", "distributed and optimization-aware financial ML supported by point-in-time data and auditable evidence"),
            ("Chuxu Zhang", "machine learning, deep learning, data mining, and graph learning", "robust graph-based financial intelligence using traceable data and explicit temporal validation"),
            ("Shiri Dori-Hacohen", "information retrieval, machine learning, and fairness and safety in AI", "safe retrieval and evidence-ranking methods for financial research agents with bounded conclusions"),
        ],
    },
    {
        "order": "10",
        "folder": "香港中文大学 (The Chinese University of Hong Kong)",
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
        "order": "12",
        "folder": "香港科技大学 (HKUST)",
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
        "folder": "悉尼科技大学 (University of Technology Sydney)",
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
        "order": "14",
        "folder": "科廷大学 (Curtin University)",
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
        "order": "15",
        "folder": "新加坡国立大学 (National University of Singapore)",
        "school": "National University of Singapore",
        "program": "PhD in Computer Science (School of Computing)",
        "contact": "Departmental application; selective faculty contact is useful after reading current work, but supervisor consent is not listed as a formal application prerequisite.",
        "lor": "2 academic references",
        "statement": "Mandatory Statement of Purpose and CV, plus complete academic and identity documents",
        "source": "https://www.comp.nus.edu.sg/programmes/pg/phdis/admissions/",
        "special_checks": [
            "Record GRE as not required; do not order or submit a score solely for this application",
            "Submit the mandatory Statement of Purpose and CV with the online application",
            "Verify the live August and January intake cut-off dates before submission",
        ],
        "faculty": [
            ("Kian Hsiang Low", "learning and optimization, data-centric AI, collaborative AI, decision making, and trustworthy AI", "drift-aware financial learning and optimization with explicit uncertainty, temporal validation, and auditable decision constraints"),
            ("Reza Shokri", "data privacy, trustworthy machine learning, and federated learning", "privacy-aware and auditable financial ML infrastructure with bounded claims, provenance, and failure-oriented evaluation"),
            ("Anthony K H Tung", "database systems, data mining, time series, trustworthy AI, and deployable decision systems", "right-sized and explainable financial AI for rare events and changing regimes, supported by traceable point-in-time data"),
            ("Jiancong Xiao", "learning theory, statistics, optimization, responsible machine learning, calibration, and robustness", "theoretical and empirical foundations for calibrated financial learning under distribution shift and asymmetric risk"),
        ],
    },
    {
        "order": "16",
        "folder": "新加坡科技设计大学 (Singapore University of Technology and Design)",
        "school": "Singapore University of Technology and Design",
        "program": "PhD Programme (ISTD / ESD research alignment)",
        "contact": "Targeted faculty contact is recommended because pillar and supervisor fit shape the research pathway; the formal application remains university-level.",
        "lor": "3 recommenders, preferably faculty able to assess research potential",
        "statement": "Statement of Objectives plus CV, transcripts, identity evidence, and research outputs",
        "source": "https://www.sutd.edu.sg/istd/149-2/",
        "special_checks": [
            "Record GRE as not required; the official ISTD page describes it only as recommended",
            "Prepare the current Statement of Objectives and verify its live word limit",
            "Confirm the chosen faculty member is accepting PhD students for the intended intake",
        ],
        "faculty": [
            ("Yihan Du", "reinforcement learning, online learning, machine learning, AI safety, and alignment", "safe online financial learning that adapts to changing regimes while enforcing explicit risk and evidence constraints"),
            ("Rakesh Nagi", "data science, machine learning, operations research, and optimization", "auditable optimization and ML infrastructure for sequential resource allocation under uncertainty and operational constraints"),
            ("Karthik Natarajan", "data science, machine learning, distributionally robust optimization, and decision science", "distributionally robust financial decisions whose uncertainty sets, costs, and out-of-sample limitations remain transparent"),
        ],
    },
]


FACULTY_DIRECTION_ZH = {
    "Shuo Sun": "人工智能与金融科技，重点关注基于学习的决策系统；本申请拟对接基于时点数据、市场状态变化和真实交易摩擦评估强化学习及量化策略的研究基础设施。",
    "Sijia Chen": "面向金融风控的分布式计算与决策算法；本申请拟研究连接数据来源、约束优化与风险监控的可审计分布式决策流程。",
    "Yuyu Luo": "以数据为中心的人工智能、数据库、数据分析与智能体；本申请拟研究面向时点金融数据、可复现实验和证据可追溯智能体流程的数据基础设施。",
    "Liang Zhang": "数据挖掘、图学习、语言模型与应用人工智能；本申请拟研究非平稳金融数据的稳健表征学习，并采用防泄漏评估和有边界的结论。",
    "Peng Wang": "数学优化、机器学习与人工智能；本申请拟研究风险感知优化，并通过时间留出和交易成本检验目标与约束。",
    "Pengyang Wang": "数据挖掘、大数据分析与机器学习；本申请拟研究采用时点特征和漂移感知验证的非平稳金融数据可审计挖掘。",
    "Dingqi Yang": "时空数据挖掘、机器学习与大数据；本申请拟将市场观测建模为时间结构数据，并显式检验分布漂移。",
    "Huanle Xu": "大数据处理系统、在线学习与分布式系统；本申请拟研究适应变化金融环境的在线监控和分布式实验基础设施。",
    "Ye Kanye Wang": "分布式系统、隐私、区块链与去中心化金融；本申请拟研究面向高风险金融及去中心化系统的审计就绪数据与决策基础设施。",
    "Preetha Chatterjee": "机器学习和数据挖掘的软件工程；本申请拟研究包含可测试时序数据契约、实验谱系和治理门禁的可靠机器学习工程。",
    "Xiaohua Tony Hu": "数据挖掘、文本挖掘与分析；本申请拟研究能够抵抗信息泄漏和市场状态不稳定的金融信号稳健挖掘流程。",
    "Weimao Ke": "信息系统、分布式系统、机器学习与数据挖掘；本申请拟研究使数据来源和模型证据可复现的分布式研究基础设施。",
    "Shahin Jabbari": "机器学习、公平性、优化与博弈论；本申请拟研究非平稳和多目标条件下的风险感知优化与可问责决策。",
    "Timothy Menzies": "数据科学、人工智能与软件工程；本申请拟研究数据轻量且可解释的可靠机器学习软件，并保证其结论在时间漂移下仍可检验。",
    "Xiaohui Gu": "分布式系统、云计算与机器学习系统；本申请拟研究面向时点金融机器学习实验和监控的自管理、可复现分布式基础设施。",
    "Xipeng Shen": "编程系统、数据密集型计算与机器学习系统；本申请拟研究支持可追溯金融机器学习训练、评估和部署的高效数据基础设施。",
    "Dongkuan Xu": "高效、稳健且可信的生成式与智能体人工智能；本申请拟研究具有明确数据来源、资源控制和证据边界的可靠金融研究智能体流程。",
    "Kaiyi Ji": "优化、机器学习与大数据分析；本申请拟研究由防泄漏验证和可审计决策记录支撑的风险感知优化。",
    "Varun Chandola": "异常检测与大数据分析；本申请拟把市场状态、漂移和异常监控作为金融机器学习评估的一等组成部分。",
    "Tevfik Kosar": "数据密集型分布式与存储系统；本申请拟研究具有可复现数据谱系和可扩展实验执行能力的时点金融数据基础设施。",
    "Changyou Chen": "贝叶斯推断、生成学习与强化学习；本申请拟在真实时间和市场约束下评估不确定性感知与序贯决策方法。",
    "Nematollaah Shiri": "数据库、不确定数据、查询优化与数据分析；本申请拟研究支持防泄漏金融机器学习的时点数据构建和可查询数据来源。",
    "Brigitte Jaumard": "大规模优化与运筹学；本申请拟研究显式纳入可行性、换手率和成本约束的风险感知组合与决策优化。",
    "Andrew Delong": "机器学习、深度学习与优化；本申请拟研究时间分布漂移下的稳健学习与优化，并采用可证伪评估。",
    "Emad Shihab": "数据驱动软件工程与人工智能软件工程；本申请拟以测试、可审计性和证据边界统一 Quant-Ultra 与 Privacy Lens 的软件治理研究。",
    "Xiao Huang": "数据挖掘、机器学习与智能体人工智能；本申请拟研究工具、数据谱系和结论均可审计的智能体金融研究流程。",
    "Houduo Qi": "优化、数据科学与投资组合优化；本申请拟把组合优化与时点数据、真实摩擦及稳健样本外证据结合。",
    "Wanyu Lin": "可信人工智能、隐私与可解释性；本申请拟研究结合数据来源、有边界解释、监控和隐私治理的可信金融机器学习基础设施。",
    "Wenqi Fan": "机器学习、数据挖掘、图学习与推荐系统；本申请拟研究变化金融关系的稳健图表征学习，并避免时间信息泄漏。",
    "Qi Wu": "量化金融、金融科技与商业分析；本申请拟研究整合时间有效性、风险控制和部署审计能力的金融智能基础设施。",
    "Kaidi Xu": "可信人工智能、不确定性与形式化验证；本申请拟研究高风险金融机器学习流程的可验证控制和不确定性感知评估。",
    "Xinyue Li": "面向大规模数据的可扩展统计学习；本申请拟在时点金融数据上开展漂移感知且统计严谨的可扩展学习。",
    "Dongjin Song": "机器学习、深度学习、时间序列分析与图表征学习；本申请拟研究变化市场状态下的时间序列和图学习，并采用防泄漏评估。",
    "Jinbo Bi": "机器学习、数据挖掘、分布式计算与优化；本申请拟研究由时点数据和可审计证据支撑的分布式、优化感知金融机器学习。",
    "Chuxu Zhang": "机器学习、深度学习、数据挖掘与图学习；本申请拟利用可追溯数据和明确时间验证研究稳健的图金融智能。",
    "Shiri Dori-Hacohen": "信息检索、机器学习与人工智能公平和安全；本申请拟研究面向金融研究智能体的安全检索与证据排序，并严格限定结论边界。",
    "James Cheng": "数据分析、机器学习与推断的高性能系统；本申请拟研究具有可复现数据及实验谱系的高性能金融机器学习基础设施。",
    "Eric Chi Lik Lo": "机器学习、大数据、数据库、数据挖掘与分布式系统；本申请拟研究支撑时点数据集和防泄漏分析的数据库及分布式系统。",
    "Songtao Lu": "优化、机器学习与数据科学；本申请拟研究时间漂移、交易成本和明确风险约束下的稳健优化。",
    "Sinno Jialin Pan": "迁移学习与领域自适应；本申请拟研究跨市场状态的领域自适应，同时避免未来信息污染评估。",
    "Farzan Farnia": "稳健机器学习、优化与分布漂移；本申请拟研究金融决策系统面对分布变化时的稳健学习目标与压力测试。",
    "Binhang Yuan": "面向机器学习的数据管理与分布式机器学习；本申请拟研究支持时点数据和可复现实验的分布式金融机器学习基础设施。",
    "Kai Chen": "机器学习系统、高性能网络与隐私计算；本申请拟研究具有明确运行和证据控制的高效、隐私友好金融机器学习系统。",
    "Qiong Luo": "大数据系统及并行与分布式计算；本申请拟研究可扩展时点数据处理和可复现回测执行。",
    "Lei Chen": "时间序列数据库、数据驱动机器学习与数据库智能；本申请拟研究支持防泄漏特征生成、监控和可审计机器学习的时间序列数据库。",
    "Jie Lu": "概念漂移、迁移学习、计算智能与数据驱动决策支持；本申请拟研究跨变化市场状态的漂移感知金融学习与决策支持。",
    "Guodong Long": "可信机器学习、联邦学习、隐私保护智能与数据科学；本申请拟把个性化或联邦学习与来源、隐私和时间验证结合。",
    "Guangquan Zhang": "模糊优化、模糊机器学习、多目标与双层决策；本申请拟研究风险、成本、可行性和不确定性约束均可独立审计的多目标金融决策。",
    "Aneesh Krishna": "人工智能、数据挖掘、机器学习、软件工程与形式化方法；本申请拟研究具备可测试数据契约、模型治理和可复现失败分析的可靠金融机器学习工程。",
    "Scott Lindstrom": "数学优化、机器学习与数据科学；本申请拟研究市场摩擦和分布漂移下的风险感知优化，并采用防泄漏时间评估。",
    "Sourav Das": "数据科学与统计；本申请拟通过不确定性、敏感性分析和可复现证据严谨评估非平稳金融模型。",
    "Kian Hsiang Low": "学习与优化、数据中心人工智能、协作人工智能、决策与可信人工智能；本申请拟研究具有明确不确定性、时间验证和可审计约束的漂移感知金融学习。",
    "Reza Shokri": "数据隐私、可信机器学习与联邦学习；本申请拟研究具有结论边界、数据来源和失败导向评估的隐私友好可审计金融机器学习基础设施。",
    "Anthony K H Tung": "数据库系统、数据挖掘、时间序列、可信人工智能与可部署决策系统；本申请拟研究由可追溯时点数据支撑的稀有事件和变化状态金融人工智能。",
    "Jiancong Xiao": "学习理论、统计、优化、负责任机器学习、校准与稳健性；本申请拟研究分布漂移和非对称风险下校准金融学习的理论与实证基础。",
    "Yihan Du": "强化学习、在线学习、机器学习、人工智能安全与对齐；本申请拟研究适应变化市场状态并执行明确风险和证据约束的安全在线金融学习。",
    "Rakesh Nagi": "数据科学、机器学习、运筹学与优化；本申请拟研究不确定性和运行约束下序贯资源配置的可审计优化与机器学习基础设施。",
    "Karthik Natarajan": "数据科学、机器学习、分布鲁棒优化与决策科学；本申请拟研究不确定集合、成本和样本外局限均透明的分布鲁棒金融决策。",
}

PROGRAM_LINKS = {
    "The Hong Kong University of Science and Technology (Guangzhou)": {
        "program": "https://soch.hkust-gz.edu.cn/wp-content/uploads/2025/12/PhD-in-Financial-Technology-2026-27-Intake-20251218.pdf",
        "apply": "https://pgoas.hkust-gz.edu.cn/",
    },
    "University of Macau": {
        "program": "https://www.cis.um.edu.mo/phd_computer_science.html",
        "apply": "https://isw.um.edu.mo/naweb_grs/faces/index.jspx",
    },
    "Drexel University": {
        "program": "https://drexel.edu/cci/academics/doctoral-programs/",
        "apply": "https://drexel.edu/admissions/apply/grad-instructions/online-app",
    },
    "North Carolina State University": {
        "program": "https://csc.ncsu.edu/academics/graduate/phd/",
        "apply": "https://gradapply.ncsu.edu/apply/",
    },
    "University at Buffalo, SUNY": {
        "program": "https://engineering.buffalo.edu/computer-science-engineering/graduate/phd.html",
        "apply": "https://ubgradconnect.buffalo.edu/apply/",
    },
    "Concordia University": {
        "program": "https://www.concordia.ca/academics/graduate/computer-science-phd.html",
        "apply": "https://www.concordia.ca/gradstudies/future-students/how-to-apply/start-your-application.html",
    },
    "The Hong Kong Polytechnic University": {
        "program": "https://www.polyu.edu.hk/study/pg/research-postgraduate",
        "apply": "https://rpgadmission.polyu.edu.hk/",
    },
    "City University of Hong Kong": {
        "program": "https://www.ds.cityu.edu.hk/en/programmes/postgraduate-programmes/phd-programme-data-science",
        "apply": "https://www.cityu.edu.hk/zh-hk/pg/research-degree-programmes/apply-now",
    },
    "University of Connecticut": {
        "program": "https://computing.engineering.uconn.edu/graduate-studies/ph-d-program/",
        "apply": "https://connect.grad.uconn.edu/apply/",
    },
    "The Chinese University of Hong Kong": {
        "program": "https://www.cse.cuhk.edu.hk/admission/mphil-phd/regular-admission/",
        "apply": "https://www.gradsch.cuhk.edu.hk/onlineapp/login_email.aspx",
    },
    "The Hong Kong University of Science and Technology": {
        "program": "https://cse.hkust.edu.hk/pg/programs/phd/",
        "apply": "https://fytgs.hkust.edu.hk/apply",
    },
    "University of Technology Sydney": {
        "program": "https://www.uts.edu.au/courses/doctor-of-philosophy-phd-thesis-computer-science",
        "apply": "https://www.uts.edu.au/for-students/admissions-entry/how-to-apply/masters-by-research-phd",
    },
    "Curtin University": {
        "program": "https://www.curtin.edu.au/study/offering/course-research-doctor-of-philosophy---computing--dr-comptg/?region=int",
        "apply": "https://www.curtin.edu.au/study/applying/research/",
    },
    "National University of Singapore": {
        "program": "https://www.comp.nus.edu.sg/programmes/pg/phdis/",
        "apply": "https://gradapp.nus.edu.sg/apply",
    },
    "Singapore University of Technology and Design": {
        "program": "https://www.sutd.edu.sg/programme-listing/sutd-phd-programme/",
        "apply": "https://www.sutd.edu.sg/programme-listing/sutd-phd-programme/application/",
    },
}

SCHOOL_README_ZH = {
    "The Hong Kong University of Science and Technology (Guangzhou)": {
        "gre": "当前审计未发现金融科技博士项目强制要求 GRE；提交前仍须按所选轮次复核。",
        "statement": "拟议研究计划、既往研究经历及项目要求的个人陈述。",
        "lor": "2–5 位学术推荐人，最终数量以在线系统为准。",
        "outreach": "建议有针对性地联系导师，同时可以并行准备和提交学校申请。",
    },
    "University of Macau": {
        "gre": "已核对的博士申请材料中未将 GRE 列为强制项。",
        "statement": "目的陈述；若在线系统要求，另交研究计划。",
        "lor": "2 封推荐信，其中至少 1 封为学术推荐信。",
        "outreach": "套磁并非硬性前置，但可用于确认招生名额和研究匹配。",
    },
    "Drexel University": {
        "gre": "GRE 可选但官方建议提交；因并非强制要求，保留该申请。",
        "statement": "约 500 词目的陈述。",
        "lor": "2 封推荐信。",
        "outreach": "院系统一录取；仅在确认研究匹配后选择性联系导师，不群发。",
    },
    "North Carolina State University": {
        "gre": "计算机科学博士未将 GRE 列为强制申请材料；项目页面中针对国际硕士申请人的 GRE 要求不应套用到博士。",
        "statement": "个人陈述以及建议不超过 2 页的简历。",
        "lor": "3 封能够评价研究生学习潜力的推荐信。",
        "outreach": "院系统一录取；官方 FAQ 允许联系研究匹配的导师以便其支持申请，建议定向联系而不群发。",
    },
    "University at Buffalo, SUNY": {
        "gre": "计算机科学与工程博士申请不要求 GRE。",
        "statement": "简短个人陈述或目的陈述。",
        "lor": "3 封推荐信，优先使用学术推荐人。",
        "outreach": "无需泛化套磁，主要在申请陈述中写清 2–3 位导师匹配。",
    },
    "Concordia University": {
        "gre": "已核对的项目材料未将 GRE 列为强制项。",
        "statement": "目的陈述和简洁的研究兴趣说明。",
        "lor": "3 封推荐信及配套评估表。",
        "outreach": "录取前必须完成导师匹配；建议先建立申请并取得 Student ID，再重点联系导师。",
    },
    "The Hong Kong Polytechnic University": {
        "gre": "当前计算机相关研究型项目材料未把 GRE 列为强制项；不得套用商学院项目要求。",
        "statement": "简历、个人陈述和学校标准格式研究计划。",
        "lor": "2 份学术推荐人报告。",
        "outreach": "建议定向联系导师，并严格使用在线系统要求的研究计划模板。",
    },
    "City University of Hong Kong": {
        "gre": "数据科学博士项目当前未列强制 GRE。",
        "statement": "个人陈述和必需的研究计划。",
        "lor": "2 位学术推荐人。",
        "outreach": "建议联系匹配导师并确认招生容量，但仍须完成学校在线申请。",
    },
    "University of Connecticut": {
        "gre": "计算机科学与工程博士不要求 GRE，可选择提交。",
        "statement": "说明研究生学习目标、相关背景和独立研究准备的个人陈述。",
        "lor": "3 封推荐信，至少 1 封应明确评价独立学习和研究准备。",
        "outreach": "博士录取由单位导师决定并直接录入其课题组；必须定向联系并确认导师匹配。",
    },
    "The Chinese University of Hong Kong": {
        "gre": "已核对的计算机科学与工程研究型项目材料未列强制 GRE。",
        "statement": "简历、最新成绩单、可用的排名证明，并准备院系面试。",
        "lor": "全日制博士至少 3 份保密推荐报告。",
        "outreach": "最终必须获得教授非正式指导意向；应进行高质量定向套磁。",
    },
    "The Hong Kong University of Science and Technology": {
        "gre": "工程学院研究型研究生申请不要求 GRE。",
        "statement": "拟议研究计划和既往研究经历。",
        "lor": "2–5 位学术推荐人，最终数量以在线系统为准。",
        "outreach": "计算机科学与工程项目要求有导师同意指导，定向联系属于申请前置步骤。",
    },
    "University of Technology Sydney": {
        "gre": "已核对的研究学位申请流程未列强制 GRE。",
        "statement": "与拟合作导师共同打磨的研究计划、简历及研究经历证明。",
        "lor": "学术推荐报告；数量和提交方式以当轮系统为准。",
        "outreach": "正式申请前须取得导师同意或学院批准，并单独核对奖学金预审流程。",
    },
    "Curtin University": {
        "gre": "计算机方向 HDR 流程当前未列强制 GRE。",
        "statement": "用于 EOI 的 2 页研究计划，参考文献另起一页。",
        "lor": "按 EOI 和正式申请表要求填写推荐人及上传证明。",
        "outreach": "先提交 EOI 并取得导师支持；只有收到邀请后才能进入正式申请。",
    },
    "National University of Singapore": {
        "gre": "NUS School of Computing 博士申请不要求 GRE。",
        "statement": "必需的目的陈述、简历、完整学术材料和身份证明。",
        "lor": "2 位学术推荐人。",
        "outreach": "院系统一申请；精读导师近期工作后可选择性联系，但导师同意不是提交前置条件。",
    },
    "Singapore University of Technology and Design": {
        "gre": "GRE 不强制，仅为官方建议提交项。",
        "statement": "Statement of Objectives、简历、成绩单、身份证明和研究成果材料。",
        "lor": "3 位推荐人，优先选择能评价研究潜力的教师。",
        "outreach": "建议联系匹配导师并确认招生状态；正式申请仍通过学校系统完成。",
    },
}


OUTREACH_LEVEL_ZH = {
    "The Hong Kong University of Science and Technology (Guangzhou)": "推荐",
    "University of Macau": "推荐",
    "Drexel University": "不需要",
    "North Carolina State University": "推荐",
    "University at Buffalo, SUNY": "不需要",
    "Concordia University": "必须",
    "The Hong Kong Polytechnic University": "推荐",
    "City University of Hong Kong": "推荐",
    "University of Connecticut": "必须",
    "The Chinese University of Hong Kong": "必须",
    "The Hong Kong University of Science and Technology": "必须",
    "University of Technology Sydney": "必须",
    "Curtin University": "必须",
    "National University of Singapore": "推荐",
    "Singapore University of Technology and Design": "推荐",
}


SCHOOL_GENERAL_MATERIALS = {
    "University of Macau": {
        "cv_focus": "trustworthy spatiotemporal intelligence for dynamic urban and networked environments",
        "cv_project": "Reframe Quant-Ultra's point-in-time data contracts as a foundation for temporally valid learning over evolving spatial, mobility, and network data.",
        "cv_secondary": "Use Privacy Lens to study provenance and fail-closed validation when contextual or location-linked data create privacy and evidence risks.",
        "interests": "spatiotemporal data mining; online learning; distributed intelligence; graph and mobility analytics; privacy-aware data systems; robust optimization",
        "fit": "UM's breadth in data intelligence, optimization, and online and distributed systems supports an agenda connecting dynamic data, reliable learning, and accountable decisions.",
        "rp_title": "Trustworthy Spatiotemporal Learning for Dynamic Urban Decision Systems",
        "motivation": "Urban, mobility, and networked data change across locations, populations, sensors, and time. Models trained on convenient historical snapshots can fail when spatial coverage shifts, observations arrive late, or context changes. The proposed research asks how spatiotemporal learning systems can remain temporally valid, privacy-aware, and operationally useful under these changes.",
        "questions": [
            "How can spatiotemporal data contracts represent observation time, location context, revisions, missingness, and permitted feature transformations?",
            "Which online or graph-learning methods remain calibrated when spatial coverage and temporal regimes change together?",
            "How should privacy, latency, resource, and decision constraints be incorporated without hiding failures behind a single aggregate score?",
            "What provenance and monitoring evidence is sufficient to reproduce and challenge an urban decision result?",
        ],
        "methods": [
            ("Spatiotemporal benchmark", "Construct versioned public and synthetic mobility or network datasets with controlled spatial gaps, delayed observations, revisions, and regime changes."),
            ("Adaptive learning", "Compare temporal, graph, and online-learning baselines using location-held-out and rolling-window evaluation with fold-local preprocessing."),
            ("Constrained decisions", "Evaluate calibrated predictions through separately auditable decision rules with privacy, latency, resource, and robustness constraints."),
            ("Distributed evidence", "Prototype provenance-aware pipelines that preserve data lineage, geographic coverage, model versions, monitoring results, and failure states."),
        ],
        "contributions": [
            "A benchmark for coupled spatial and temporal distribution shift.",
            "Evaluation protocols that separate predictive accuracy, geographic robustness, privacy, and decision utility.",
            "A provenance-aware architecture for distributed spatiotemporal learning.",
        ],
        "plan": "Year 1: literature review and benchmark design. Year 2: adaptive spatiotemporal learning and calibration. Year 3: constrained decision and distributed provenance experiments. Final period: cross-dataset validation and dissertation integration.",
    },
    "University at Buffalo, SUNY": {
        "cv_focus": "robust sequential learning and anomaly-aware decision systems under distribution shift",
        "cv_project": "Emphasize Quant-Ultra's walk-forward evaluation, uncertainty-aware monitoring, risk constraints, and separation of forecast quality from decision utility.",
        "cv_secondary": "Use Privacy Lens as a second failure-oriented testbed for anomaly detection, provenance, replay boundaries, and conservative automated responses.",
        "interests": "sequential and Bayesian learning; anomaly detection; robust optimization; uncertainty calibration; distributed ML systems; trustworthy analytics",
        "fit": "UB CSE's complementary strengths in learning, optimization, anomaly detection, and data-intensive systems support a committee-facing agenda that can later be refined through faculty matching.",
        "rp_title": "Anomaly-Aware Sequential Learning for Reliable High-Stakes Decisions",
        "motivation": "Sequential decision systems must distinguish ordinary variation from structural change while acting under uncertainty and cost. In financial and other streaming settings, labels arrive late, anomalies may be rare, and repeated model selection can make apparent improvements fragile. The proposed research joins sequential learning, anomaly detection, and constrained optimization in an auditable evaluation framework.",
        "questions": [
            "How can sequential models distinguish transient anomalies, persistent regime change, and data-quality failures?",
            "Which uncertainty and calibration measures remain informative under delayed labels and distribution shift?",
            "How should anomaly signals interact with turnover, cost, exposure, and risk constraints in a decision layer?",
            "Can distributed monitoring and provenance reduce false confidence without making the system unusably conservative?",
        ],
        "methods": [
            ("Sequential evaluation", "Use rolling and expanding windows, delayed-label simulations, and regime-aware splits while preserving fold-local model selection."),
            ("Anomaly taxonomy", "Inject data, context, and behavioral anomalies and compare statistical, representation, and Bayesian baselines."),
            ("Risk-aware response", "Map calibrated anomaly evidence into abstention, review, or constrained decisions and measure both detection and downstream utility."),
            ("Distributed monitoring", "Record model, data, uncertainty, alert, and decision lineage across reproducible pipeline stages."),
        ],
        "contributions": [
            "A benchmark separating anomaly, drift, and data-integrity failures in sequential ML.",
            "Calibration and evaluation methods for delayed and shifting feedback.",
            "Auditable response policies connecting anomaly evidence to bounded decisions.",
        ],
        "plan": "Year 1: anomaly taxonomy, sequential baselines, and delayed-feedback benchmark. Year 2: uncertainty calibration and shift-aware learning. Year 3: constrained response policies and distributed monitoring. Final period: cross-domain evaluation and dissertation integration.",
    },
    "Concordia University": {
        "cv_focus": "evidence-aware data and software infrastructure for reliable artificial intelligence",
        "cv_project": "Present Quant-Ultra as a software and data-governance system whose typed contracts, reconciliation checks, and reproducible runs make AI evidence queryable and testable.",
        "cv_secondary": "Use Privacy Lens to examine traceability, invalid-source handling, replay boundaries, and engineering assurance for privacy-sensitive AI software.",
        "interests": "data provenance; database support for ML; software engineering for AI; constrained optimization; uncertainty-aware analytics; reproducible systems",
        "fit": "Concordia's combination of databases, optimization, machine learning, and software engineering supports research on how data and software architecture determine the reliability of AI evidence; the agenda is designed for refinement during required supervisor matching.",
        "rp_title": "Evidence-Aware Data and Software Infrastructure for Reliable AI",
        "motivation": "AI reliability depends not only on a model but also on the data queries, transformations, software stages, configurations, and validation rules that surround it. These dependencies are often difficult to inspect after a result is produced. The proposed research treats evidence lineage as a first-class data and software object that can be queried, tested, optimized, and governed.",
        "questions": [
            "Which provenance schema can connect source records, queries, transformations, models, tests, and decision claims without excessive overhead?",
            "How can database constraints and software contracts detect temporally invalid or inconsistent ML evidence before downstream use?",
            "How should validation effort be optimized when checks have different costs, coverage, and operational consequences?",
            "Which software-engineering practices make failure states reproducible and understandable to independent reviewers?",
        ],
        "methods": [
            ("Evidence data model", "Design a typed lineage schema for datasets, queries, transformations, experiments, validation results, and bounded claims."),
            ("Contract-based assurance", "Implement database constraints, property-based tests, reconciliation rules, and mutation tests that inject known evidence failures."),
            ("Validation optimization", "Formulate check selection and execution as a constrained optimization problem balancing coverage, latency, and compute cost."),
            ("Software evaluation", "Study reproducibility, fault localization, reviewer effort, and false assurance across financial ML and privacy-sensitive prototypes."),
        ],
        "contributions": [
            "A queryable provenance model linking ML artifacts to validation evidence and claims.",
            "A failure-injection benchmark for data and software assurance in AI pipelines.",
            "Optimization methods for allocating validation effort under operational constraints.",
        ],
        "plan": "Year 1: provenance schema, literature review, and failure taxonomy. Year 2: contract-based assurance and mutation benchmark. Year 3: validation optimization and reviewer studies. Final period: cross-domain synthesis, open artifacts, and dissertation integration.",
    },
}

SCHOOL_BRIEF_ESSAYS = {
    "University of Macau": """My research interest is trustworthy spatiotemporal learning for urban and networked environments. Mobility traces, sensor streams, and location-linked observations are never static: coverage changes across districts, observations arrive late, populations shift, and the meaning of a feature can change with time and context. A model that performs well on a convenient historical snapshot may therefore fail when deployed in a different place or period. I want to develop learning systems that make these spatial and temporal assumptions explicit and that remain useful when the environment changes.

The first part of the research will create a benchmark for coupled spatial and temporal shift. Versioned public datasets and synthetic controls will reproduce delayed observations, missing regions, revised records, changing network structure, and abrupt regime changes. Each dataset will carry machine-readable contracts describing observation time, geographic scope, revision state, and permitted transformations. Evaluation will use rolling windows and location-held-out tests so that preprocessing and model selection cannot borrow information from the future or the target region.

The second part will compare temporal, graph-based, and online-learning methods under these controlled changes. The goal is not simply to maximize a pooled accuracy score. I will examine calibration, geographic robustness, adaptation speed, and uncertainty across locations and periods. Predictions will then enter a separately auditable decision layer with privacy, latency, resource, and robustness constraints. This separation will reveal whether an apparently stronger model actually produces more dependable decisions.

My preparation comes from Quant-Ultra, where I have implemented point-in-time data controls, walk-forward evaluation, monitoring, reconciliation, and evidence records for non-stationary financial data. Privacy Lens provides complementary experience with provenance and fail-closed validation in privacy-sensitive software. I would adapt these engineering foundations to spatiotemporal data while treating existing systems as prototypes rather than completed research contributions.

The University of Macau is a strong setting for this agenda because its work spans data intelligence, optimization, and online and distributed systems. These strengths support a coherent project connecting dynamic data, reliable learning, and accountable decisions. I expect the research to contribute a reproducible shift benchmark, evaluation protocols that separate predictive accuracy from geographic and operational robustness, and a provenance-aware architecture for distributed spatiotemporal learning.

The initial study will use a small set of transparent baselines before introducing more complex models. Success will be measured by performance stability across held-out locations and time periods, calibrated uncertainty, adaptation after controlled changes, and the ability to reconstruct every reported result from its data and configuration record. Ablation studies will isolate the value of spatial structure, online adaptation, and provenance controls. If sophisticated methods do not outperform simpler alternatives consistently, that negative result will guide the design rather than be discarded. This evaluation strategy keeps the project scientifically testable and relevant to real systems whose operating conditions cannot be assumed to remain fixed.""",
    "University at Buffalo, SUNY": """My proposed research studies anomaly-aware sequential learning for reliable decisions under distribution shift. In streaming environments, a sudden change may indicate a corrupted data source, a rare but temporary event, or a persistent regime transition. These cases require different responses, yet they are often collapsed into a single anomaly score. Delayed labels and repeated model selection make the problem harder: a system may appear accurate while remaining poorly calibrated precisely when a decision is most consequential.

I plan to build a benchmark that separates data-integrity failures, transient anomalies, and structural drift. Rolling and expanding windows will preserve temporal order, while delayed-feedback simulations will test how quickly a method can recognize and respond to change. Controlled interventions will introduce missing observations, altered feature distributions, unusual sequences, and persistent shifts. Statistical detection methods, representation models, and Bayesian baselines will be compared using detection delay, false alarms, calibration, and performance after adaptation.

A central feature of the project is the connection between anomaly evidence and action. Rather than treating an alert as an automatic decision, I will map calibrated evidence into abstention, human review, or constrained responses. In financial experiments, those responses will include explicit turnover, cost, exposure, concentration, and risk limits. Forecast quality and downstream utility will be reported separately so that a favorable decision outcome cannot hide weak predictive evidence, and a strong detector cannot be credited for an impractical response policy.

Quant-Ultra provides an initial testbed through its point-in-time data, walk-forward evaluation, risk controls, monitoring, reconciliation, and machine-readable audit records. Privacy Lens offers a second domain for studying anomalous inputs, provenance, replay boundaries, and conservative automated behavior. These systems give me practical experience with failure-oriented evaluation and reproducible pipelines, while the doctoral work will supply the formal problem definitions, literature-grounded baselines, and independent empirical evidence.

The University at Buffalo's strengths in machine learning, optimization, anomaly detection, and data-intensive systems align closely with this project. I aim to contribute a benchmark distinguishing anomaly, drift, and data-quality failures; calibration methods for delayed and shifting feedback; and auditable response policies that connect uncertainty to bounded decisions. The department's breadth would allow the learning, optimization, and systems components to be developed as one integrated research program.

The empirical studies will begin with interpretable statistical detectors and simple response rules, then add learned representations and Bayesian uncertainty only when they produce measurable gains. Evaluation will report behavior before, during, and after each injected change, not just an average over the full stream. I will test whether calibration deteriorates before accuracy, whether review policies reduce costly false responses, and how conclusions change under alternative delay and cost assumptions. Reproducible configurations and preserved negative results will make comparisons independently auditable. These criteria define success as reliable behavior under change, rather than a single favorable score on a static test set.""",
    "Concordia University": """My research interest is evidence-aware data and software infrastructure for reliable artificial intelligence. An AI result depends on far more than a trained model: it also depends on source records, database queries, transformations, software versions, configurations, tests, and validation rules. When these dependencies are scattered across logs and scripts, a result may be difficult to reproduce or challenge even if the final metric appears convincing. I want to make evidence lineage a first-class object that can be queried, tested, and governed.

The project will begin with a typed provenance model connecting datasets, queries, transformations, experiments, validation results, and bounded claims. The model will record both successful stages and invalid or missing evidence. Database constraints and software contracts will then check temporal consistency, source validity, schema expectations, and reconciliation rules before downstream use. Property-based and mutation tests will inject known failures to measure which controls detect them, how quickly the cause can be localized, and whether the system communicates the failure clearly to an independent reviewer.

Because exhaustive validation can be expensive, a second component will study how to allocate assurance effort. I will formulate check selection and execution as a constrained optimization problem in which tests differ in cost, latency, coverage, and consequence. Policies will be evaluated against simple fixed test suites and risk-based baselines. The objective is not to remove human judgment, but to identify when automated evidence is sufficient for routine continuation and when the system should abstain or require review.

My preparation comes from Quant-Ultra, an implemented financial ML pipeline with typed stage contracts, point-in-time controls, reconciliation checks, monitoring, and reproducible evidence bundles. Privacy Lens provides complementary experience with invalid-source handling, replay boundaries, and audit records in privacy-sensitive software. Together they offer two settings for failure injection and cross-domain evaluation without assuming that existing engineering artifacts already establish research novelty.

Concordia's strengths in databases, optimization, machine learning, and software engineering make it an excellent environment for this work. I expect the research to produce a queryable provenance model linking AI artifacts to validation evidence, a failure-injection benchmark for data and software assurance, and optimization methods for allocating validation effort under operational constraints. The resulting infrastructure would help researchers reproduce results, locate failures, and state more defensible boundaries around AI-supported decisions.

Evaluation will compare the proposed architecture with conventional experiment logs and fixed validation pipelines. Key measures will include failure-detection coverage, false alarms, time to locate a fault, provenance-query latency, compute cost, and the effort required for an independent reviewer to reconstruct a claim. Ablation studies will test whether each schema element or contract adds useful assurance. The optimization component will be considered successful only if it preserves critical coverage while reducing cost or latency relative to transparent baselines. By publishing failure cases as well as successful runs, the project will support cumulative evidence about which engineering controls genuinely improve AI reliability.""",
}

SPECIAL_CHECKS_ZH = {
    "University of Technology Sydney": [
        "提交前附上导师同意证明，或取得书面的学院批准。",
        "申请竞争性奖学金时，完成 FEIT/学院预审流程。",
        "奖学金截止日期与全年开放的入学申请通道必须分别核对。",
    ],
    "Curtin University": [
        "正式申请前先提交 Expression of Interest（EOI）。",
        "研究计划正文控制在 2 页，参考文献放在单独附加页。",
        "仅在 EOI 通过且导师明确支持后进入正式申请。",
    ],
    "National University of Singapore": [
        "记录为 GRE 不要求，不为该申请单独订购或提交 GRE 成绩。",
        "在线申请必须同时提交目的陈述和简历。",
        "提交前复核 8 月和 1 月入学轮次的实时截止日期。",
    ],
    "Singapore University of Technology and Design": [
        "记录为 GRE 非强制；官方仅表述为建议提交。",
        "按当轮要求准备 Statement of Objectives，并复核实时字数限制。",
        "确认所选导师在目标入学轮次仍接收博士生。",
    ],
}


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


def departmental_cv(school: dict) -> str:
    details = SCHOOL_GENERAL_MATERIALS[school["school"]]
    return preamble("Departmental Curriculum Vitae", school["school"], "School-wide application") + rf"""
\textbf{{Contact}}: \ApplicantEmail\quad | \quad \ApplicantPhone\quad | \quad \ApplicantGitHub

\section*{{School-Specific Research Profile}}
Computer-science-trained applicant seeking doctoral study in {tex_escape(details['cv_focus'])}. The application is anchored in two implemented systems and is tailored to {tex_escape(school['school'])}: {tex_escape(details['cv_project'])} {tex_escape(details['cv_secondary'])}

\section*{{Education}}
\textbf{{University of Melbourne}} \hfill 2025--present\\
Postgraduate computing coursework and research project. \textit{{Confirm the exact degree title and expected completion date from current official records before submission.}}
\begin{{itemize}}
\item Completed results include Evaluating User Experience (78), Machine Learning Applications for Health (76), Information Visualization (70), and Research Methods (69).
\item The supplied Computer Science Research Project progress record reports 30/40 across proposal and oral-presentation components; remaining components are pending and no final thesis result is claimed.
\end{{itemize}}

\textbf{{The University of British Columbia, Okanagan}} \hfill 2020--2024\\
Bachelor of Science program and computing coursework. \textit{{The supplied transcript lists no credential to date; confirm the exact award, major, and conferral date against the degree certificate.}}
\begin{{itemize}}
\item Selected later results: Capstone Software Engineering Project 93; Databases 90 on successful retake; Image Processing 88; Data Analytics 86; Software Engineering 86; Numerical Analysis 85; Analysis of Algorithms 82.
\item The complete transcript should accompany the application; the later record demonstrates stronger performance in advanced computing and project-based work without concealing weaker earlier results.
\end{{itemize}}

\section*{{Research and Engineering Projects}}
\textbf{{Quant-Ultra --- Primary Evidence for This Application}}
\begin{{itemize}}
\item {tex_escape(details['cv_project'])}
\item Existing implementation connects point-in-time data, leakage controls, walk-forward evaluation, constrained decisions, monitoring, reconciliation, and machine-readable audit evidence.
\item Missing provenance, failed reconciliation, unstable results, or weak baselines trigger review-only conclusions; successful execution is not presented as scientific or investment validity.
\end{{itemize}}

\begin{{samepage}}
\textbf{{Privacy Lens --- Complementary Cross-Domain Evidence}}
\begin{{itemize}}
\item {tex_escape(details['cv_secondary'])}
\item Provides a second domain for testing provenance and failure handling; simulator evidence is not presented as legal or device-wide validity.
\end{{itemize}}
\end{{samepage}}

\section*{{Research Interests at {tex_escape(school['school'])}}}
{tex_escape(details['interests'])}.

{tex_escape(details['fit'])}

\section*{{Relevant Preparation}}
Python; algorithms and data structures; databases; numerical methods; probability and statistics; machine learning; data analytics; software engineering; experiment design; research communication. The strongest supporting coursework includes Databases (90), Data Analytics (86), Software Engineering (86), Numerical Analysis (85), Analysis of Algorithms (82), and a Capstone Software Engineering Project (93). \textit{{Replace the generic tool summary with verified proficiency levels before submission.}}

\section*{{References and Evidence Boundary}}
Three referees are planned: the Melbourne research supervisor, a CS/ML/algorithms academic, and an academic able to assess later-stage UBC project work. Add names and institutional contact details only after consent. No publication, award, rank, or unverified research outcome is claimed in this draft.
""" + closing()


def departmental_research_interest_proposal(school: dict) -> str:
    details = SCHOOL_GENERAL_MATERIALS[school["school"]]
    questions = "\n".join(rf"\item {tex_escape(item)}" for item in details["questions"])
    methods = "\n\n".join(
        rf"\textbf{{{tex_escape(title)}.}} {tex_escape(description)}"
        for title, description in details["methods"]
    )
    contributions = "\n".join(rf"\item {tex_escape(item)}" for item in details["contributions"])
    return preamble("Research Interest Proposal", school["school"], "School-wide application") + rf"""
\setlength{{\parskip}}{{0.45em}}
\textbf{{Research title:}} {tex_escape(details['rp_title'])}

\section*{{Research Interest and Motivation}}
{tex_escape(details['motivation'])}

My preparation for this agenda includes Quant-Ultra, which connects point-in-time data, controlled evaluation, constrained decisions, monitoring, reconciliation, and evidence bundles. Privacy Lens supplies a second setting for provenance and fail-closed behavior. These systems provide practical foundations for literature-grounded doctoral research with defensible baselines and independently reproducible experiments.

\section*{{Research Questions}}
\begin{{enumerate}}
{questions}
\end{{enumerate}}

\section*{{Proposed Methodology}}
{methods}

\newpage
\section*{{Departmental Fit}}
{tex_escape(details['fit'])} This department-level framing allows the project to integrate complementary expertise while preserving a focused problem definition, evaluation strategy, and set of expected contributions.

\section*{{Expected Contributions}}
\begin{{enumerate}}
{contributions}
\end{{enumerate}}

\section*{{Preparation, Feasibility, and Risks}}
The existing systems make early prototyping feasible. The doctoral research will add a verified literature review, ethical and licensing review, simple baselines, preregistered ablations where appropriate, and independent replication. Negative or unstable results will remain part of the evidence record.

Data licensing may restrict redistribution, so experiments will combine redistributable sources, synthetic controls, and published transformation code. System complexity may obscure causal conclusions; modular experiments and failure injection will keep individual mechanisms testable.

\section*{{Indicative Plan}}
{tex_escape(details['plan'])}
""" + closing()


def departmental_research_interest_brief_md(school: dict) -> str:
    details = SCHOOL_GENERAL_MATERIALS[school["school"]]
    return f"""# Research Interest Proposal

**Applicant:** Zhiheng Zhang

**School:** {school['school']}

## {details['rp_title']}

{SCHOOL_BRIEF_ESSAYS[school['school']]}
"""


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
    special_checks = SPECIAL_CHECKS_ZH.get(
        school["school"],
        ["提交前重新核对实时项目页面、截止日期、申请费用、材料格式和文件大小限制。"],
    )
    special_section = ""
    if special_checks:
        special_section = "\n## 学校特定门槛\n\n" + "\n".join(
            f"- [ ] {item}" for item in special_checks
        ) + "\n"
    details = SCHOOL_README_ZH[school["school"]]
    return f"""# 申请清单｜{school['folder']}｜{supervisor}

材料包最近生成日期：2026-08-16。截止日期和申请系统文案均可能变化，须在提交前 30 天重新核对官方页面。

官方核对入口：{school['source']}

## 本目录内的申请材料

- [ ] 补全两版简历中的联系方式、学位名称、项目链接和推荐人占位符。
- [ ] 按实时申请题目和字数限制调整 `03_Statement_of_Purpose.tex`。
- [ ] 核验 `04_Research_Statement.tex` 和 `05_Research_Proposal.tex` 中的每项陈述。
- [ ] 用最新且已核实的文献替换参考文献占位内容。
- [ ] 上传申请系统前编译并逐页检查所有 TeX 文件。
- [ ] 仅按以下策略使用英文套磁邮件 `08_Contact_Email.md`：{details['outreach']}

## 项目申请材料

- [ ] 在线申请表及申请费，或获批的费用减免证明
- [ ] 学术简历和研究简历
- [ ] {details['statement']}
- [ ] {details['lor']}
- [ ] 所有高等教育阶段的正式成绩单
- [ ] 学位证书，或在读及预计完成时间证明
- [ ] 项目要求时提供官方评分标准或成绩图例
- [ ] 英语能力成绩，或学校接受的英语授课证明
- [ ] 护照或其他身份证明
- [ ] 项目要求或有利于评审时提交写作样本
- [ ] 已核实的项目永久链接、发布标签和提交哈希
- [ ] 项目要求时提供导师选择或同意指导证明
{special_section}
## 当前导师及联系门槛

- [ ] 核实 {supervisor} 当前所在机构的官方主页和邮箱
- [ ] 阅读至少两篇近期相关论文或项目页面
- [ ] 用一个准确、具体的研究连接替换宽泛切入点
- [ ] 确认 2027 年招生名额后，才把回复视为积极信号
- [ ] 将回复和任何指导承诺保存在申请记录中

## 尚缺的申请人正式材料

- [ ] 墨尔本大学准确学位名称和预计完成日期
- [ ] 墨尔本大学最新正式成绩单
- [ ] 英属哥伦比亚大学学位证书
- [ ] 墨尔本大学在读或预计完成证明；取得最终证书后及时替换
- [ ] 申请系统要求时提供官方英语授课证明
- [ ] 护照或身份证明扫描件
- [ ] 不适用豁免时提供英语考试证明
- [ ] 已同意推荐的推荐人姓名、职称、机构邮箱和提交状态
- [ ] 完整论文或研究报告写作样本
- [ ] 已核实的 Quant-Ultra 和 Privacy Lens 永久链接

## 最终陈述边界检查

- [ ] 未在缺乏证据时声称论文、奖励、工作经历、语言成绩、绩点换算、排名或导师兴趣。
- [ ] 将 Quant-Ultra 描述为研究基础设施，而非投资建议或已证明的未来业绩。
- [ ] 未把 Privacy Lens 的工程证据描述为法律合规结论或全部设备验证。
- [ ] 提交完整成绩单；可以解释学业轨迹，但不得隐藏较弱成绩。
"""


def fact_check_md(school: dict, supervisor: str, area: str, hook: str) -> str:
    direction = FACULTY_DIRECTION_ZH[supervisor]
    return f"""# 事实核对记录

## 可依据现有证据使用的事实

- 申请人姓名：Zhiheng Zhang。
- 现有英属哥伦比亚大学成绩单记录了理学学士项目就读情况，但标注 `Credentials: None to date`；在补充学位证书或最终成绩单前，不得声称已完成学位。
- 英属哥伦比亚大学成绩单日期为 2024-08-28，其中包含草稿引用的课程成绩。
- 后期课程证据包括：毕业项目 93、数据库重修 90、图像处理 88、数据分析 86、软件工程 86、数值分析 85、算法 82。
- 墨尔本大学 WAM 图片列出 2025 年课程及 2026 年进行中的计算机科学研究项目；图片将剩余项目部分标为待定。
- 申请定位和项目描述遵循仓库中的 2027 年申请计划。

## 提交前必须核实

- 墨尔本大学准确学位名称、在读状态、预计完成日期和最新正式成绩。
- 根据学位证书核实英属哥伦比亚大学准确专业及授予文字。
- 所有联系方式、项目网址、发布版本、提交哈希和个人贡献。
- 任何论文、预印本、奖励、奖学金、实习、工作经历、排名、绩点或 WAM 汇总及语言成绩陈述。
- {supervisor} 当前研究方向、所在机构和招生状态。工作匹配说明：{direction}
- {school['folder']} 2027 年实时申请要求和截止日期。

## 申请清单采用的官方来源

{school['source']}

该网址仅是核对起点，不能证明页面内容以后不会变化。提交申请时应保存带日期的实时要求页面 PDF 或截图。
"""


def school_readme_md(school: dict) -> str:
    faculty_rows = "\n".join(
        f"- [{supervisor}](<{supervisor}/>)"
        for supervisor, _, _ in school["faculty"]
    )
    details = SCHOOL_README_ZH[school["school"]]
    links = PROGRAM_LINKS[school["school"]]
    special_checks = SPECIAL_CHECKS_ZH.get(
        school["school"],
        ["提交前重新核对实时项目页面、截止日期、申请费用、材料格式和文件大小限制。"],
    )
    school_checks = "\n".join(f"- [ ] {item}" for item in special_checks)
    general_materials = (
        """
## 学院通用材料

- [`Departmental_General_CV.tex`](Departmental_General_CV.tex)：不绑定单一导师的学院通用学术与研究履历
- [`Research_Interest_Proposal.tex`](Research_Interest_Proposal.tex)：不绑定单一导师的研究兴趣计划
- [`Research_Interest_Proposal_500_Words.md`](Research_Interest_Proposal_500_Words.md)：采用独立叙事、可直接使用的英文约 500 词版本

三份材料均直接存放在学校目录下。对外使用前须核实占位符、实时项目要求、篇幅限制和学院名称；不得把学院通用版本误写成已获得任何导师支持。

"""
        if school["school"] in SCHOOL_GENERAL_MATERIALS
        else ""
    )
    return f"""# {school['folder']}

申请优先级：**{school['order']}**<br>
申请项目：**{school['program']}**
套磁分类：**{OUTREACH_LEVEL_ZH[school['school']]}**

## 官方链接

- [项目介绍页面]({links['program']})
- [在线申请通道]({links['apply']})
- [材料要求核对页]({school['source']})

> 链接已于 2026-08-15 核对。申请入口、截止日期和材料要求可能调整，实际提交前必须再次访问官方页面确认。

## GRE 筛查

**{details['gre']}** 全部学校的筛查记录见 [GRE_AUDIT.md](../GRE_AUDIT.md)。如果实时规则变为对当前申请背景强制要求 GRE，应暂停或删除该学校，不得绕过硬约束。

## 学校级材料清单

- [ ] 在线申请表及申请费，或获批的费用减免证明
- [ ] 学术简历和研究简历
- [ ] {details['statement']}
- [ ] 所有高等教育阶段的正式成绩单和最终学位证书
- [ ] 英语能力证明，或有文件依据的豁免结论
- [ ] 护照或在线系统接受的其他身份证明
- [ ] {details['lor']}
- [ ] 实时项目要求中的研究计划、写作样本或补充题目
- [ ] 从学校官方页面核实导师研究匹配及当前招生状态

## 学校特定检查

{school_checks}

{general_materials}## 导师申请包

套磁策略：**{details['outreach']}**

{faculty_rows}

每个导师目录均包含完整工作包：两版简历、目的陈述、研究陈述、研究计划、项目摘要、定制套磁邮件、申请清单、事实核对表、写作样本说明页及现有证据附件。

## 提交边界

这些文件是结构化草稿，不代表已经获准提交申请或发送邮件。对外使用前必须替换全部占位符，补充墨尔本大学最新正式成绩单、已确认的学位证书、身份及英语证明和已同意推荐的推荐人，并再次核对实时申请系统要求及导师最新主页。
"""


def readme_md(school: dict, supervisor: str) -> str:
    direction = FACULTY_DIRECTION_ZH[supervisor]
    details = SCHOOL_README_ZH[school["school"]]
    return f"""# {school['folder']}｜{supervisor}

申请项目：**{school['program']}**

套磁分类：**{OUTREACH_LEVEL_ZH[school['school']]}**

套磁策略：**{details['outreach']}**

## 导师研究方向与申请切入点

{direction}

> 该方向说明根据现有申请计划整理。发送邮件或提交申请前，必须用导师最新官方主页、近期论文和当前招生信息再次核实，不得把工作匹配写成导师已经表达兴趣。

## 材料包说明

本目录是申请该导师的自包含工作包。所有拟导出为 PDF 的新撰写材料均以 LaTeX 源文件提供。英属哥伦比亚大学正式成绩单保留为原始 PDF 附件，墨尔本大学 WAM 证据保留为原始图片，二者均未重新制作。

## 文件清单

- `01_Academic_CV.tex`：精简学术简历
- `02_Research_CV.tex`：研究导向简历
- `03_Statement_of_Purpose.tex`：学校与导师匹配目的陈述
- `04_Research_Statement.tex`：可复用研究陈述
- `05_Research_Proposal.tex`：完整研究计划草稿
- `06_Quant_Ultra_Research_Summary.tex`：一页项目摘要
- `07_Privacy_Lens_Research_Summary.tex`：第二项目摘要
- `08_Contact_Email.md`：英文定制套磁邮件及发送规则；按用户要求保留英文
- `09_Application_Checklist.md`：项目材料和未解决事项清单
- `10_Fact_Check.md`：本申请包的事实与陈述边界记录
- `11_Writing_Sample_Cover_Note.tex`：写作样本说明页；仍需补充实际样本
- `Attachments/`：现有正式材料和背景证据

## 对外使用前

检索所有文件中的 `CONFIRM`、`ADD`、`TBD` 和方括号占位符并逐项补全。核实导师最新主页及实时申请系统要求，编译全部 TeX 文件并逐页检查生成的 PDF。标记为低投入回报或仅供院系申请使用的草稿，不得因为文件已经生成就直接发送。
"""


def root_index() -> str:
    rows = []
    for s in sorted(SCHOOLS, key=lambda item: int(item["order"])):
        folder = f"{s['order']}_{s['folder']}"
        level = OUTREACH_LEVEL_ZH[s["school"]]
        outreach = SCHOOL_README_ZH[s["school"]]["outreach"]
        rows.append(f"| {s['order']} | [{s['folder']}](<{folder}/>) | {s['program']} | {len(s['faculty'])} | **{level}** | {outreach} |")
    return """# 2027 年博士申请材料包

本目录依据申请计划和现有背景证据生成，最近更新日期为 2026-08-16。

每个导师目录均包含为该导师准备的申请材料、英文定制套磁邮件、项目申请清单、事实核对记录及现有学业证据副本。所有拟生成 PDF 的新撰写材料均使用 TeX 源文件；原始正式证据保持原格式不变。除套磁邮件外，全部 Markdown 说明文件使用中文。
澳门大学、纽约州立大学布法罗分校与康考迪亚大学的学校目录下另有不绑定单一导师的学院通用 CV、完整 RP 和约 500 词 RP。

| 优先级 | 学校 | 申请项目 | 导师申请包数量 | 套磁分类 | 套磁策略 |
|---:|---|---|---:|---|---|
""" + "\n".join(rows) + """

## 重要边界

- 这些文件是完整草稿，不是可以直接提交的正式记录。仓库尚不包含墨尔本大学最新正式成绩单、学位证书、护照、英语证明、推荐人身份和完整写作样本。
- 未在缺乏证据时声称论文、奖励、工作经历、排名、绩点换算或导师兴趣。
- 导师研究切入点来自当前计划；发送前必须根据导师最新官方主页和近期成果重新核对。
- 当前 GRE 筛查记录见 `Applications/GRE_AUDIT.md`。南洋理工大学计算与数据科学学院因其项目规则对当前海外学历背景强制要求 GRE/GMAT，已从清单删除。
- 香港科技大学计算机科学与工程博士按“必须有导师同意指导”处理，因为当前常见问题页面明确写有该条件；不得沿用旧的可选联系分类。
- 院系统一录取项目仍按导师分别建包以便组织材料，但英文邮件中已明确标记为可选或禁止群发。

## 生成与验证

执行：

```powershell
python tools/build_application_packages.py
python tools/validate_application_packages.py
```

替换占位符后再正式编译 TeX。占位符对 TeX 安全，因此草稿也可以执行编译检查；但任何对外使用仍须经过版面和事实审核。

## D 盘验收环境

已验证的本地 TeX 环境安装于 `D:\\PhD-Tools\\TinyTeX`（TeX Live 2026）。由于 TeX 无法在含非 ASCII 字符的仓库路径下稳定创建日志，编译脚本会将源文件复制到 `D:\\PhD-Tools\\qa-input` 的纯 ASCII 暂存目录，并将验收 PDF 和日志写入 `D:\\PhD-Tools\\qa-output`。

```powershell
python tools/build_application_packages.py
python tools/validate_application_packages.py
python tools/compile_application_packages.py --workers 8
python tools/render_qa_representatives.py
```

编译和渲染清单写入 `tmp/pdfs/`，并按设计排除在 Git 跟踪之外。
"""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def build() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    write(OUT / "README.md", root_index())
    for school in sorted(SCHOOLS, key=lambda item: int(item["order"])):
        school_dir = OUT / f"{school['order']}_{school['folder']}"
        write(school_dir / "README.md", school_readme_md(school))
        if school["school"] in SCHOOL_GENERAL_MATERIALS:
            write(school_dir / "Departmental_General_CV.tex", departmental_cv(school))
            write(
                school_dir / "Research_Interest_Proposal.tex",
                departmental_research_interest_proposal(school),
            )
            write(
                school_dir / "Research_Interest_Proposal_500_Words.md",
                departmental_research_interest_brief_md(school),
            )
        for supervisor, area, hook in school["faculty"]:
            target = school_dir / supervisor
            attachments = target / "Attachments"
            attachments.mkdir(parents=True, exist_ok=True)
            legacy_readme = target / "00_README.md"
            if legacy_readme.exists():
                legacy_readme.unlink()
            write(target / "README.md", readme_md(school, supervisor))
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
