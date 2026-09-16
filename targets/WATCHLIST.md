# Watchlist

> **未刷新 ≠ 不值得申请。** 这里专门放“研究匹配不错，但至少还有一个成绩等效、funding、GRE/英语、流程摩擦或当前轮次问题没有核清”的项目。
>
> **成绩门槛优先于导师匹配。** 明确要求 GPA / WAM / degree classification 的项目，在用户成绩不能按学校官方规则确认满足前，不得自动晋级 ACTIVE。

## 成绩门槛待确认

| 学校 | 保留理由 | 当前阻塞项 |
|---|---|---|
| University of Waterloo | Boss / DS-Hns 导师匹配与 funding 都很强 | CS PhD 标准硕士路径要求相关 Master's **78% average**；等待 Melbourne final WAM / 官方等效 |
| Queen's University | SE / AI-for-SE 匹配强，PhD funding 清晰 | Computing PhD 要求 Master's minimum **A standing / first class**；等待 final WAM / classification |
| Dalhousie University | SE / debugging / autonomous systems 导师匹配不错 | CS PhD 要求相关 Master's **minimum A- average**；等待 final WAM / equivalency |
| University of British Columbia | 顶级 SE / verification / LLM-tools 匹配；PhD funding floor 高 | 通用基线约 B+ / 76%，但具体 PhD + 已有 Master's 路径仍需按官方等效核验 |
| University of Alberta | codeLLM / AI-assisted programming / multi-agent 导师池非常强；全校 PhD 有最低 funding guarantee | Computing Science 的 GPA / research-master 路径、英语/GRE 当前口径需精确核验；不可只套大学通用 3.0 |
| Nanyang Technological University | AI agents / AI-assisted development / security fit 强 | PhD 要求 strong Bachelor's + Honours (Distinction) or equivalent；UBC 学位等级等效未确认 |
| NTNU — Trustworthy Agentic AI vacancy | 与 Boss / DS-Hns 几乎正面重合；带薪职位 | 通常要求 NTNU scale **B 或更好**；需做 UBC/Melbourne 等效 + 英语材料核验 |
| NTNU — Multi-Agent Communication vacancy | multi-agent / LLM communication + Software Engineering group | 博士入学成绩等效与英语材料待核验 |

## 资金 / 流程待确认

| 学校 | 保留理由 | 当前阻塞项 |
|---|---|---|
| University of Victoria | Norha Villegas / Ratnadira Widyasari / Amber Horvath 与 agentic AI、AI4SE、GenAI developer tooling 高匹配 | GRE 对国际申请者高度推荐；funding 为 offer-dependent，需先确认够覆盖生活 |
| University of Manitoba | Shaowei Wang 的 AI-for-SE / LLM / bug fixing / AIOps 与 DS-Hns 很直接 | 成绩线看起来较友好，但 supervisor funding 不能视为保证；需确认 funding/capacity |
| HKUST (Guangzhou) | FinTech / AI / data 方向仍有潜在匹配 | GRE、英语、funding、interview、当前 intake |
| Drexel | CS/SE/ML systems 仍可能低套磁成本 | 英语、funding、deadline、interview |
| Stevens | ML systems / time-series 路线仍可匹配 | funding、英语、writing sample、deadline |
| CityUHK | Data Science / trustworthy AI / LLM systems 仍有潜在匹配 | 2027 intake、政府资助名额/studentship、proposal、interview |
| Stony Brook | Systems/ML fit 高 | 英语、funding、GRE current policy、deadline |
| UMass Amherst | Systems/data/ML fit 高但竞争强 | funding、English、current materials |

## 本轮明确不直接晋级 ACTIVE 的高匹配项目

- **NUS CS PhD**：Abhik Roychoudhury / Jin Song Dong / Chengpeng Wang 与 autonomous software engineering / trustworthy agents 非常强，但 programme 有海外 scholarship interview 和 mandatory PhD Qualifying Examination，按低摩擦标准降为 BACKUP。
- **MBZUAI CS PhD**：funding 很有吸引力，但申请含 mandatory screening exam，按“尽量不考试”的偏好降为 BACKUP。
- **UVic**：导师 fit 很高，不是因为研究弱而 WATCH；主要是 GRE 推荐 + funding 需要 supervisor-level confirmation。

## Round-2 数据入口

- `data/expansion-round2-2026-09-16.yaml`：第二轮全球扩池的 programme staging 数据
- `data/supervisors-expansion-round2-2026-09-16.yaml`：对应导师池

当一个候选的 score gate / GRE / English / funding / current intake 均核清后，再合并进 `data/programs.yaml` 和 `data/supervisors.yaml`，并进入 ACTIVE / BACKUP / REJECT。