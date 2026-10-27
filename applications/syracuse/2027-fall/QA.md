# 申请包质量检查

检查日期：2026-10-27。

## 正文与 PDF

| 文件 | 页数 | 检查结果 |
|---|---:|---|
| SOP | 2 | 正文按空白分词为 789 words（不含标题/身份行）；没有跨页拆开段落；文字与 Markdown 一致 |
| CV | 2 | 按完整项目分组分页；文字与 Markdown 一致；6 个 PDF 链接 |
| Research Summary | 1 | 文字与 Markdown 一致；4 个 PDF 链接；标为可选补充材料 |

- 用 pypdf 重新读取最终输出，去除页脚/页码并归一化标点后，三份 PDF 与源文全文一致。
- 已逐页查看五页 PNG 预览，检查文字清晰、边界、留白、标题和页脚；修复初版标准字体替代问题。
- 正文与标题使用嵌入的 DejaVu 字体；保留可选择/搜索文字。
- 可上传正文中未发现占位符、其他学校的申请号、错误 UBC 校区或不相关个人信息。
- 文件尺寸与 SHA-256 见 [MANIFEST.json](MANIFEST.json)。

## 内容复核

- 由独立只读审阅检查三份英文正文，并落实具体观察、方法匹配和精简重复表述的建议。
- UBC 校区为 Okanagan；Melbourne MCS 为在读、预计 late 2026，未虚构最后成绩或学位完成。
- DS-Hns 只列手稿准备中，不标已发表、已录用或编造 arXiv ID。
- DS-Hns 恢复观察保留 effect/checkpoint gap，未宣称 exactly-once 或跨运行时速度优势。
- Utopia 明确区分 Windows execution workers 与 Android/Web control。
- AI-assisted implementation/integration 与申请人的架构、评估和证据审查角色一致。
- 研究提议与已完成工作分开；faculty fit 不是教授接收承诺。
- 私人仓库的新实现细节未引入公开包。

## 操作核验

- 初次检查 26 个内部相对链接，均可解析到新包文件或仓库既有文件；后续新增 QA/MANIFEST 入口在提交前一并核对。
- 正文、PDF、模板和事实账本作为一个版本提交。
- 仅计划新增 applications/syracuse/2027-fall/ 和仓库首页导航；保留其他学校文件。
- GitHub Actions 的两个现有 CV 构建流程只监听 CV-generate 或 tracking-hist 中对应的 TeX 路径；本包不修改这些路径或 workflow，提交使用 skip-ci 标识。
- 未运行任何申请人研究项目、私有仓库测试或收费外部服务。
- 未提交学校申请、未付款、未发邮件、未创建 Gmail 草稿、未发送推荐信邀请。

## 未完成且不能由文书检查代替的事项

- 网申内的个人陈述题目、字数/格式、推荐信准确数量及额外必填字段。
- 申请人最终核准、最新成绩单、推荐人同意与实际提交。
- 提交后语言豁免在系统中的生效状态。
- 录取、导师名额和本人资助条件。

本记录证明材料准备与检查范围，不证明申请已完整可审或已获录取。
