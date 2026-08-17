# 申请材料包验收报告

验收日期：2026-08-17

## 本地环境

- 安装根目录：`D:\PhD-Tools\TinyTeX`
- 发行版：Windows 版 TinyTeX-1，版本 `v2026.05`
- 编译引擎：pdfTeX 3.141592653-2.6-1.40.29（TeX Live 2026）
- 安装程序缓存：`D:\PhD-Tools\downloads\TinyTeX-1-windows-v2026.05.exe`
- 安装程序 SHA-256：`5E9CD432D9278012524E6E0D26E2CE3225C7490905425D356C458D6F9122BBDD`
- 本批源文件安装的附加 TeX 包：`microtype`、`enumitem`、`titlesec`
- 隔离暂存与输出目录：`D:\PhD-Tools\qa-input`、`D:\PhD-Tools\qa-output`

仓库路径含非 ASCII 字符。编译流程会先把每份 TeX 源文件复制到稳定的纯 ASCII 暂存目录，再调用 pdfLaTeX。生成的 PDF、日志、清单和页面渲染图均为验收中间产物，按设计不纳入 Git。

## 自动验收

| 检查项 | 结果 |
|---|---:|
| 按优先级排序的中英双语学校目录 | 15 个通过 |
| 中文学校材料要求 README | 15 个通过；全部含“必须/推荐/不需要”套磁分类 |
| 官方项目介绍及申请通道链接 | 30 个存在 |
| 导师目录 | 58 个通过 |
| 标准导师 README 文件名 | 58 个通过；旧 `00_README.md` 为 0 个 |
| 导师中文方向介绍 | 58 个通过 |
| 学院通用 CV / Research Interest Proposal | 澳门大学、UB 与 Concordia 各 2 份，共 6 份通过；均以 Quant-Ultra 为核心并作学校特化 |
| 约 500 词 Research Interest Proposal（Markdown） | 澳门大学 505 词、UB 479 词、Concordia 505 词；均与本校完整 RP 对齐且为英文可直接使用版 |
| 完整 TeX 源文件 | 470 个通过 |
| 非空 Markdown 文件 | 251 个通过 |
| 官方成绩单副本 | 58 个通过 |
| TeX 编译 | 470 / 470 个通过 |
| 编译失败 | 0 |
| LaTeX 警告 | 0 |
| 行宽溢出 | 0 |
| 行宽不足 | 0 |
| TeX 中的 Unicode 破折号 | 0 |

本轮删除 Stevens、Stony Brook、UMass Amherst 和 UC Riverside，并在原 04、09 位新增 NC State 和 UConn。非美国学校保持原有编号和目录，不因重新编号而删除或重建。澳门大学、UB 和 Concordia 各有一份学院通用 CV、完整 Research Interest Proposal 和约 500 词 Markdown 短文，且不包含任何目标导师姓名。三校材料均以 Quant-Ultra 为共同研究底座，并分别强化时空与图市场智能、异常感知的序列学习与风险响应、证据可追溯的数据和软件基础设施。每校 Markdown 精简版与完整 RP 使用同一标题、问题、方法和预期贡献；完整 RP 进一步展开研究基础、评估标准、可行性和风险，因此二者对齐但不重复。九份学校级材料均写入确认的邮箱与电话，且不含联系方式占位符或内部编辑提示。机器可读编译清单已刷新至 `tmp/pdfs/compile-manifest.json`，共 470 份 TeX，失败、LaTeX 警告、行宽溢出和行宽不足均为 0。

## 视觉验收

对澳门大学、UB 和 Concordia 的 6 份学院通用文档进行了全量渲染和检查，共 15 页：3 份 Departmental General CV 各 2 页，3 份 Research Interest Proposal 各 3 页。所有文档均为美国信纸尺寸，文本可提取；未发现裁切、重叠、不可读字符或内容超出页面边界。

## GRE 硬约束审计

当前项目级 GRE 审查见 `Applications/GRE_AUDIT.md`。南洋理工大学计算与数据科学学院已删除，因为其官方项目页面规定非新加坡自治大学毕业的申请人必须提交 GRE/GMAT。新加坡国立大学计算机学院和新加坡科技设计大学予以保留，因为其当前官方招生页面说明 GRE 不要求。其他保留项目分别属于不要求、可选、建议或未列为项目要求；每次提交前 30 天仍须核对实时申请系统。

## 验收边界

本次验收证明源文件完整、TeX 可编译、文本可提取且代表性版面正常。三校共九份学校级材料已使用确认的邮箱和电话；仓库内其他导师材料仍可能保留事实占位符。准确学位名称与日期、推荐人、英语证明、写作样本详情、导师当前招生状态、项目实时要求和学校特定申请题目，在发送任何材料前仍须核实。
