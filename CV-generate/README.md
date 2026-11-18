# CV 生成区

> **当前通用母版：2026-11-18** — [两页 PDF](latest/Zhiheng-Zhang-Academic-CV.pdf) · [英文正文](latest/CV.md) · [状态与重建说明](latest/README.md)。DS-Hns（arXiv:2610.39241）与 Boss-A2（arXiv:2610.41276）两篇稿件均已投稿 Software Quality Journal (SQJ)，等待审稿；DS-Hns、Boss、Utopia 为历史冻结项目，当前开发线为 Celestial 多方向软件项目系列。

本目录保存可复用的 LaTeX CV 母版，以及针对不同导师/路线生成的**英语 Research CV**。

## 文件说明

| 文件 | 导师 / 路线 | 主要侧重点 |
|---|---|---|
| `latest/CV.md` · `latest/Zhiheng-Zhang-Academic-CV.pdf` | 当前通用母版（2026-11-18） | Celestial 系列当前开发 + Hns/Boss/Utopia 历史成果；两篇 SQJ 在审稿件 |
| `template/research-cv-template.tex` | 旧 LaTeX 母版（历史排版参考） | 个人事实及论文状态以 `latest/CV.md` 为准 |
| `polyyu-yu-pei.tex` | Yu Pei, PolyU | program repair / testing / fault localization |
| `cityuhk-heqing-huang.tex` | Heqing Huang, CityUHK | software security / program analysis |
| `cuhk-yu-li.tex` | Yu Li, CUHK | scientific agents / computational health |
| `sutd-thanh-le-cong.tex` | Thanh Le-Cong, SUTD | reliable/secure AI4SE |
| `um-li-li.tex` | Li Li, University of Macau | resource-aware LLM/agent systems |
| `concordia-zhijie-wang.tex` | Zhijie Wang, Concordia | autonomous SE / multi-agent evaluation |
| `concordia-tse-hsun-peter-chen.tex` | Peter Chen, Concordia | coding agents / debugging / AIOps |
| `sutd-ezekiel-soremekun.tex` | Ezekiel Soremekun, SUTD | trustworthy software / Code LLM validation |
| `cityuhk-nan-guan.tex` | Nan Guan, CityUHK | LLM-aided system design / scheduling |
| `um-xiaobo-zhou.tex` | Xiaobo Zhou, UM | systems ML / OS / distributed support |
| `polyyu-jing-li.tex` | Jing Li, PolyU | NLP / reasoning / trustworthy agents |
| `hku-ka-ho-chow.tex` | Ka Ho Chow, HKU | trustworthy agent systems / LLM security |
| `sfu-keval-vora.tex` | Keval Vora, SFU | scalable systems / runtime reliability |
| `cuhksz-xiaoxue-gao.tex` | Xiaoxue Gao, CUHK-Shenzhen | agentic AI / multimodal / robustness |

## 维护规则

1. 对外 CV **始终保持英语**。
2. 项目事实必须与 `materials/project-positioning.md` 同步。
3. 新的 broad systems 申请以 **Celestial 当前开发线** 为主，但只展示已有运行/验证证据的相关组件；DS-Hns、Codex Boss、Utopia 作为 completed/frozen 历史成果。AI4SE / repair / testing 导师可重点引用 Hns/Boss 历史研究和对应论文稿件。
4. 不得虚构 skill、publication、experiment、supervisor-specific experience。
5. Quant-Ultra 默认是辅助项目，除非目标就是 Financial ML / optimization / data systems。
6. 新导师应从母版生成，不要直接改另一个导师版本。
7. `.tex` 存在不等于附件 ready；只有 PDF 实际生成并检查后才能标 `CV_PDF_READY`。
8. PCF 只能作为 planned research direction，不能写成 completed work。

## 联系信息

Primary email：`m15601654187@163.com`  
Student email：`zhihezhang@student.unimelb.edu.au`

教育时间：
- University of Melbourne — Master's degree in Computer Science, expected 2026
- University of British Columbia — BSc in Computer Science, completed Summer 2024

## 新导师 CV：Celestial 系列实时刷新

**硬规则：给任何新导师发送材料前，必须刷新当前 Celestial 证据，并按目标方向生成 tailored CV；历史项目可复用，但必须保持 completed/frozen 的过去时。**

刷新流程：

1. 读取 `Celestial-Throne/main` 当前 HEAD，以及与目标导师相关的 CRI、Finance、Smart Glass 或其他子项目；
2. 读取相关 Mission / Design / Function / Evidence / Verification Book，确认功能状态、依赖、运行证据和独立验收边界；
3. 记录各仓库当前 SHA；不得把旧证据自动升级到新版本；
4. 只把已实现且有运行证据的能力写成 completed/implemented；将 planned、NOT_RUN、NOT_IMPLEMENTED 明确保留；
5. Celestial 系列可概括为多方向软件开发组合，但 CV 只选择目标导师相关的 2–4 条证据；
6. DS-Hns、Codex Boss、Utopia 统一作为已完成并冻结的历史项目，不再描述为当前施工；
7. 重新编写 Research Profile / Current Research Direction，突出实际软件工作流、可靠性和可验证性；
8. 重新编译 PDF 并检查分页、链接、状态和实际运行边界；
9. 完成后才能标记 `CV_PDF_READY`。

### 历史项目与当前开发线

旧导师版 CV 可保留 Utopia、DS-Hns 和 Codex Boss 的历史工程证据；它们不是“过时到不能使用”，而是必须准确标注为已完成/冻结。Celestial 是当前主动开发系列，但各子项目成熟度不同，不能用某个仓库的局部 PASS 代表整个系列已交付。

### 实时刷新 ≠ 功能堆砌

CV 应反映与目标导师相关、且有证据支撑的系统价值，而不是仓库数量或最新 commit 列表。优先写：

- 与该导师最相关的软件工程问题；
- 当前已经有证据的实现和真实运行结果；
- 一条真实 limitation / failure / verification boundary；
- 下一步可自然转成 PhD research question 的方向。

不得将研究计划、设计书或未运行的功能写成 completed work。
