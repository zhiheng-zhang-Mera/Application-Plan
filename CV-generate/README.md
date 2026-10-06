# CV 生成区

本目录保存可复用的 LaTeX CV 母版，以及针对不同导师/路线生成的**英语 Research CV**。

## 文件说明

| 文件 | 导师 / 路线 | 主要侧重点 |
|---|---|---|
| `template/research-cv-template.tex` | 母版 | Autonomous AI / reliable agent systems |
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
3. 新的 broad systems 申请默认使用 **Utopia-first**；AI4SE / repair / testing 导师可切换到 Hns-first。
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

## 新导师 CV：Utopia 实时刷新

**硬规则：给任何新导师发送套磁前，必须重新生成 tailored CV；旧 PDF 不能直接复用。**

刷新流程：

1. 读取 `Utopia/main` 当前 HEAD 与已合并能力；
2. 读取 `Digital-City/main` 当前 mission-book / reports，确认最新验收边界与 planned direction；
3. 记录两边当前 SHA；
4. 只把已完成/已验收内容写成 completed work；
5. PCF、wearable、尚未施工/验收的系列继续明确写成 planned research direction；
6. 根据目标导师只选最相关的 2–4 条 Utopia evidence；
7. 重写 Utopia bullets / Research Profile / Current Research Direction；
8. 重新编译 PDF 并检查；
9. 完成后才能标 `CV_PDF_READY`。

### 旧 CV 状态

对**新导师**，仓库中已经存在的 supervisor-specific CV 只能作为格式与事实参考。

其中 Utopia 部分一律按：

`STALE_FOR_NEW_OUTREACH`

处理，除非它在当前这次套磁 run 中已经完成实时刷新并记录当前 Utopia / Digital-City SHA。

### 实时刷新 ≠ 功能堆砌

CV 应反映 Utopia 的**最新真实研究价值**，而不是最新 commit 列表。

优先写：

- 与该导师最相关的系统问题；
- 当前已经有证据的实现；
- 一条真实 limitation / failure / verification signal；
- 下一步可自然转成 PhD research question 的方向。

不要为了“最新”把所有新功能都塞进 CV。

