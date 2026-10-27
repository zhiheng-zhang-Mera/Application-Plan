# 雪城大学 CISE PhD · Fall 2027 申请材料包

更新：2026-10-27（Australia/Melbourne）。

状态：**材料已准备，尚未提交网申；语言考试豁免资格已获招生办确认，须在提交后请求录入系统。** 本次没有创建或发送 Gmail 草稿，没有触发推荐信邀请，也没有接受任何录取或资助条件。

## 直接使用的材料

| 文件 | 用途 | 使用说明 |
|---|---|---|
| [SOP / Personal statement PDF](output/pdf/Zhiheng-Zhang-Syracuse-CISE-SOP.pdf) · [可编辑正文](upload/SOP.md) | 主申请文书 | 两页工作版；先核对网申中的准确题目、字数和文件格式要求。公开 ECS 页面未说明这些限制。 |
| [CV PDF](output/pdf/Zhiheng-Zhang-Syracuse-CISE-CV.pdf) · [可编辑正文](upload/CV.md) | 研究型简历 | UBC Okanagan 本科、墨大在读硕士，以及可核查的研究/系统经历。 |
| [Research Summary PDF](output/pdf/Zhiheng-Zhang-Syracuse-CISE-Research-Summary.pdf) · [可编辑正文](upload/Research-Summary.md) | 一页补充研究摘要 | 仅在网申允许补充文件、导师索取或推荐人需要时使用；不是已确认的必交项目，不与 SOP 强行重复上传。 |
| [网申字段与短回答](PORTAL-ANSWERS.md) | 填表辅助 | 区分可直接复用的研究描述与必须从证件/正式成绩单填写的字段。 |

## 申请管理资料：不要上传招生系统

- [投递清单与时间安排](APPLICATION-CHECKLIST.md)
- [导师匹配依据](FACULTY-FIT.md)
- [提交后语言豁免及后续邮件模板](EMAIL-TEMPLATES.md)
- [事实来源与写作边界](SOURCES-AND-CLAIMS.md)
- [质量检查记录](QA.md)
- [文件清单与校验值](MANIFEST.json)

## 这套材料采用的定位

主线为 **Reliable Intelligent Software Systems**：用测试、程序分析和实证评估研究智能软件的可靠执行、故障恢复与真实完成判断。穿戴/泛在计算作为有兴趣的应用场景，不将 SOP 写成必须执行某个个人产品开发计划的承诺。

匹配重点是 Endadul Hoque 与 Kristopher Micinski，Yuzhe Tang 为互补方向。列名表示研究兴趣匹配，不表示教授已接收、正在为本申请保留名额或已承诺资助。

本包按当前 Fall 2027 决定准备；不继承旧材料中不适用于此次申请的入学季或导师排序。共享历史记录保持原状。

## 还需完成的事项

1. 在官方网申确认 personal statement 的题目、长度、上传格式、推荐信数量，以及有无额外必填材料。
2. 提供最新 Melbourne 学术记录；本包不把尚未公布的成绩或学位完成状态写成既成事实。
3. 确认推荐人同意并由网申系统发送邀请。现有推荐人中心只有两条可复用关系；不能据此假设雪城推荐信已齐。
4. 用户确认后自行提交并支付申请费；本次未执行。
5. 提交后，向 topgrads@syr.edu 回复原豁免线程，请求将语言豁免应用至该申请；再检查系统材料是否齐全。
6. 收到决定后，单独核验资助类型、服务职责、保障年限与覆盖项目，再决定是否入学。

官网目前列出的博士 Fall 截止日为 12 月 15 日；本包据此按 **2026-12-15** 安排 Fall 2027 申请。具体截止时刻、时区及系统显示以当期网申为准，不等到最后一天提交。来源及未确认项见 [事实记录](SOURCES-AND-CLAIMS.md)。

## 文件维护

英文 Markdown 是正文源；PDF 由 [build-pdfs.py](build-pdfs.py) 生成，使用 US Letter 页面和可选择/检索文字。重建依赖 Python 3 与 reportlab，不联网、不运行研究项目、不调用 GitHub Actions。

修改正文后须重建 PDF，重新检查分页/链接和 MANIFEST；不要只修改一个版本。这里的排版目标是内部工作规格，不是学校规定。

本仓库公开：不新增原始邮件、证件、完整财务材料或私人项目内部实现。成绩单使用既有来源并在学校系统提交，本包不复制它们。返回 [申请控制中心](../../../README.md)。
