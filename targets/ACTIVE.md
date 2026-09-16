# Active Targets

> 这里只放**现在值得主动推进**的项目。已提交项目不放这里。
>
> 排序不是“学校排名”，而是按当前时间点的**行动紧迫度 + 硬条件已核验程度 + Boss / DS-Hns 匹配**方便执行。
>
> **重要：成绩门槛属于 Hard Gate。** 有明确 GPA/WAM/等级线但尚不能确认满足的学校，不进入无条件 `APPLY_NOW`。

| 学校 | 状态 | 为什么还值得做 | 当前最匹配导师 | 下一步 |
|---|---|---|---|---|
| KAUST | **APPLY_NOW / APPLY** | Spring 2027 PhD Round 1 截止 **2026-09-27**；Fall 2027 Round 2 于 **2026-09-28** 开放、2027-01-03 截止；最低允许 GPA 3.0/4.0，录取群体通常更高；全奖含 tuition + housing + insurance + relocation + stipend | Marco Canini / Di Wang / Ali Shoker | 先确认官方对 UBC percentage 的等值判断无硬性问题；不必为了 Spring 硬赶，优先 Fall 2027 |
| Hong Kong Polytechnic University | **APPLY_NOW** | Computing 4-year PhD 可凭 recognised Master's + Bachelor's；当前未发现额外硬 GPA 数字线；英语授课学位可免语言成绩 | Yu Pei / Jing Li / Hongxia Yang | 若要 Jan 2027，优先处理；否则按 Sep 2027 正常准备 |
| HKUST | **APPLY_NOW** | CSE FAQ 明确没有统一 PhD minimum GPA，整体 profile 综合判断；Spring/Fall 2027 轮次有效 | Junxian He / Jiasi Shen / Shuai Wang | 可直接走 regular application；套磁作为加成而非阻塞项 |
| University of Hong Kong | **APPLY_NOW / VERIFY CLASSIFICATION** | 4-year PhD 可走 honours Bachelor's + taught Master's 路径；PGS 通常要求本科达到 second-upper equivalent 以上 | Ka Ho Chow / Zuming Jiang / Heming Cui | 在付款前确认 UBC degree standing 对 HKU 的 honours / 2:1 equivalency；满足后保持 ACTIVE |
| Simon Fraser University | **APPLY / VERIFY MASTER ROUTE** | 持相关 Master's 可申请 PhD；无硕士直博才有明确 3.5/4.33 cumulative 或 last-60 3.67/4.33 门槛；funding 与研究匹配仍好 | Linyi Li / Keval Vora / Hang Ma | 按完成 Melbourne Master's 的路径核验 general graduate GPA equivalency，再推进下一 intake |
| Concordia University | **APPLY / SUPERVISOR TRACK** | 已有实际导师接触/面试历史；Boss + DS-Hns 叙事匹配度高 | Zhijie Wang | 继续澄清 supervisor commitment、funding、正式 application/offer 流程，并保留成绩资格复核 |

## 成绩门槛暂时移出 ACTIVE

下面三所上一轮研究/资金条件很好，但现在发现有明确硕士成绩硬线，因此在 **Melbourne final WAM / classification 出来前降到 WATCH**：

| 学校 | 官方成绩线 | 当前处理 |
|---|---|---|
| University of Waterloo | 标准 CS PhD 路径：相关 CS Master's **78% average**；本科直博只描述为 outstanding record，无可直接套用固定分数 | **WATCH — ACADEMIC_GATE_PENDING_FINAL_WAM** |
| Queen's University | 2027-28 Computing PhD：Master's degree + minimum **“A” standing (first class)** | **WATCH — ACADEMIC_GATE_PENDING_FINAL_WAM** |
| Dalhousie University | CS PhD：相关 Master's **minimum A- average** | **WATCH — ACADEMIC_GATE_PENDING_FINAL_WAM** |

当前已出的 Melbourne 成绩记录包括 78 / 76 / 70 / 69，不能据此假装最终硕士成绩已经满足上述门槛；等 final transcript 出来后再按学校自己的换算规则重判。

## 这一轮的执行优先级

1. **KAUST / PolyU / HKUST**：成绩硬门槛目前没有发现像 Waterloo / Queen's / Dalhousie 那样直接卡住的明确规则，继续推进。
2. **HKU**：先做 honours / second-upper equivalency 核验，再交不可退申请费。
3. **Concordia**：已有导师线，继续现有流程。
4. **SFU**：等 Melbourne 完成后按 Master's-entry 口径核验；不要误套 bachelor-direct 的 3.5/4.33 / 3.67/4.33 门槛。
5. **Waterloo / Queen's / Dalhousie**：暂不花申请费、不做高成本材料；final WAM 出来后自动重筛。

## 套磁优先导师

- **Yu Pei (PolyU)**：program repair / testing / automatic fault repair 与 DS-Hns 的 recovery 路线直接。
- **Junxian He / Jiasi Shen / Shuai Wang (HKUST)**：Boss / DS-Hns 的 LLM systems 与 software engineering 路线。
- **Ka Ho Chow (HKU)**：LLM + trustworthy AI + cybersecurity + systems；先过 classification 核验。
- **Marco Canini / Ali Shoker (KAUST)**：系统、可靠性和 fault tolerance，适合 DS-Hns。
- **Linyi Li (SFU)**：LLM + trustworthy ML/security + software engineering；等成绩口径核验后推进。

## 升级规则

WATCHLIST 中的学校只有在重新核验以下项目后才进入 ACTIVE：**academic score/classification gate、GRE、英语豁免、funding、考试/面试负担、当前 intake、application deadline**。

所有自动化应以 `data/programs.yaml`、`data/supervisors.yaml` 和成绩门槛规则为机器真源；本页只做懒人视图。