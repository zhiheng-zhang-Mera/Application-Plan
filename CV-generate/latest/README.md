# 最新通用学术 CV（2026-10-31）

本目录是当前通用英文 CV 母版及可上传 PDF。以 2026-10-27 最新学校申请版 CV 的事实和写作风格为基础，移除 Syracuse 专属标识，加入 DS-Hns 与 Boss-A2 两篇研究稿件。历史学校/导师定制版保持原状。

## 使用文件

- [Zhiheng-Zhang-Academic-CV.pdf](Zhiheng-Zhang-Academic-CV.pdf)：两页、US Letter、文字可检索，适合当前网申 CV 上传。
- [CV.md](CV.md)：唯一正文源；后续更新从这里开始。
- [build-cv.py](build-cv.py)：沿用仓库现有 PDF 生成器的排版，离线重建 PDF。

Buffalo 网申下拉选择 **Resume/Curriculum Vitae**。本次只更新仓库材料，没有上传学校系统，也没有发送邮件。

## 论文状态与依据

核验日期：2026-10-31（Asia/Shanghai）。

| 项目 | CV 中使用的准确标题 | 当前状态 |
|---|---|---|
| DS-Hns | Omission-Safe Conditional Contracts for Evidence-Closed CI Qualification | **arXiv preprint**，公开编号 [2610.39241](https://arxiv.org/abs/2610.39241)，cs.SE，v1 提交于 2026-10-29；唯一作者 Zhiheng Zhang |
| Boss-A2 | Architectural Debt Enforcement under Incomplete Observation: A Controlled Study of Ratchets and Evidence Qualification | **Manuscript submitted to arXiv; awaiting moderation**；唯一作者 Zhiheng Zhang；不填写尚未取得的公开 arXiv ID |

- DS-Hns 的标题、作者、编号与状态已按 arXiv 官方公开页面核对；DOI：[10.48550/arXiv.2610.39241](https://doi.org/10.48550/arXiv.2610.39241)。
- Boss-A2 使用最终 V8 提交包的标题和作者；“已提交并等待 moderation”按申请人本轮明确确认记录。V8 是内部稿件版本，不称为 arXiv v8。
- 两篇统一列于 **Preprints and Manuscripts**，均不表述为已被期刊/会议接收或经过同行评审。Boss-A2 已完成并提交，不再放入 Manuscripts in Preparation。
- Boss-A2 公开后，核对公开页面，再更新该条为 arXiv preprint 并补上实际编号与链接；不得自动猜测。
- 冻结项目的生命周期措辞依据 [PROJECT-LINEAGE](../../materials/PROJECT-LINEAGE.md) 和 [执行规则 §21](../../rules/EXECUTION.md)，不据此扩张项目的功能/实机验收边界。

## 本次范围

1. 以既有最新 CV 为基础，添加两篇论文、准确状态及一行研究内容。
2. 将 DS-Hns 旧的 Preparing a research manuscript 描述更新为对应已完成研究；补充 Boss-A2 研究关联。
3. 明确 Master of Computer Science 为一年授课加一年研究，预计 2026 年 12 月完成；不写成已经取得学位。
4. 保留既有学历、导师、技能与项目证据；不新增未经确认的成绩、录用、实验、身份或语言豁免结果。
5. 不回写历史学校定制包，不触发 GitHub Actions，不修改邮箱或招生系统。

## 重建与检查

依赖：Python 3、reportlab；优先使用 DejaVu 字体，缺失时使用 reportlab 自带字体。不联网、不运行研究项目。

```bash
python3 CV-generate/latest/build-cv.py
```

可在内存中生成 base64（不在磁盘写 PDF）：

```bash
python3 CV-generate/latest/build-cv.py --stdout-base64
```

本次 PDF 已完成文本提取、两页逐页渲染检查与链接核验；两个论文标题和 Boss-A2 状态在第一页完整可见。PDF 页数：2；文件大小：91606 bytes；SHA-256：

```text
c7d73b74ccd0dcc5cb349e26da11e14ecbdb26b4712ef163bf7d824a96e4a247
```

正文变更后必须重建 PDF，并复查分页、链接与状态；不能只改 Markdown。未来首次联系新导师仍需按仓库规则另做针对性调整和当前证据刷新，本通用 CV 不自动等于某位导师的 outreach-ready 附件。
