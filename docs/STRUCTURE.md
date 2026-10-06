# 仓库结构

仓库分成**极小的日常控制面**和更深层的证据 / 历史区。

## 平时只看这些

- `README.md` — 懒人看板：当前优先级、截止日期、阻塞项、下一步
- `rules/SCREENING.md` — 唯一的筛选 / 研究方向 / 优先级规则书
- `rules/EXECUTION.md` — 唯一的套磁 / 材料 / QA / 提交规则书

## 状态与证据

- `data/` — program / supervisor / application 的机器可读状态
  - `data/integrations.yaml` — 外部连接配置；当前默认 Gmail 为 `zhiheng0mera@gmail.com`，不存凭据
  - `data/outreach.yaml` — Gmail thread/message 与导师/application 的映射
- `targets/` — 筛选视图与按日期冻结的候选快照
- `applications/` — 真实申请、联络记录与学校级工作流
- `materials/` — 可复用研究 / 申请素材
- `Documents/` — 学术原始文件与派生结构化成绩
- `CV-generate/` — 英文定制 CV 源文件 / PDF 与构建输入
- `archive/` — 历史材料，只用于追溯
- `docs/` — 设计 / 历史说明，不作为当前策略规则

## 语言约定

- **内部控制面、规则、状态、说明：尽量使用中文。**
- **对外申请材料与邮件：默认保持英语。**
- 机器字段名、状态枚举、代码、命令、路径、专有名词可保留英语，避免破坏自动化。
- 官方原文短语在需要精确核验时可保留原语言。

## 优先级

当前官方证据与已确认的申请 / 联络事件优先于旧快照。

日常不要浏览 archive 或旧 dated target 文件，除非主页为了某个具体判断明确链接过去。