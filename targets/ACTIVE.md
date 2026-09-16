# Active Targets

> 这里只放**现在值得主动推进**的项目。已提交项目不放这里。
>
> 排序不是“学校排名”，而是按当前时间点的**行动紧迫度 + 硬条件已核验程度 + Boss / DS-Hns 匹配**方便执行。

| 学校 | 状态 | 为什么还值得做 | 当前最匹配导师 | 下一步 |
|---|---|---|---|---|
| KAUST | **APPLY_NOW / APPLY** | Spring 2027 PhD Round 1 截止 **2026-09-27**；Fall 2027 Round 2 于 **2026-09-28** 开放、2027-01-03 截止；全奖含 tuition + housing + insurance + relocation + stipend | Marco Canini / Di Wang / Ali Shoker | 不必为了 Spring 硬赶；若材料能直接复用可投，否则 9 月 28 日起走 Fall 2027 |
| Hong Kong Polytechnic University | **APPLY_NOW** | Computing Jan 2027 截止 **2026-09-30**；同时 Sep 2027 轮次已开；AI + software systems 匹配很强 | Yu Pei / Jing Li / Hongxia Yang | 若要 Jan 2027，优先处理；否则按 Sep 2027 正常准备 |
| HKUST | **APPLY_NOW** | Spring 2027 非本地截止 **2026-11-01**；Fall 2027 截止 **2027-06-01**；AI / systems / SE fit 强 | Junxian He / Jiasi Shen / Shuai Wang | 可直接走 regular application；套磁作为加成而非阻塞项 |
| University of Hong Kong | **APPLY_NOW** | 2027/28 Main Round **2026-12-01** 截止；英语授课学位可免语言重考；PGS 资金可用 | Ka Ho Chow / Zuming Jiang / Heming Cui | Main Round 内完成申请，并优先定向 Ka Ho Chow |
| University of Waterloo | **APPLY_NOW** | Fall 2027 截止 **2026-12-01**；GRE 不要求；加拿大本科满足英语豁免；CS PhD funding 强 | Yuntian Deng / Pengyu Nie / Xinyue Shen | 先做 Yuntian Deng + Pengyu Nie 两封高定制套磁，再准备正式申请 |
| Queen's University | **APPLY_NOW** | 2027 funding consideration 截止 **2027-01-15**；明确 **GRE not required**；PhD 页面明确 fully funded | Filipe Cogo / Yuan Tian / Bram Adams | 先提交/准备申请，再联系少量高匹配导师 |
| Dalhousie University | **APPLY** | GRE 仅 recommended、不 required；SE / debugging / autonomous systems 导师适配不错 | Tushar Sharma / Masud Rahman / Nils Wilde | supervisor-first，先套磁确认 funding/capacity 后再投 |
| Simon Fraser University | **APPLY** | PhD 最低 funding 保证 **CAD 30k/年 × 4 年**；GRE 不看；LLM + SE + systems 匹配强 | Linyi Li / Keval Vora / Hang Ma | Spring 2027 已关闭，准备下一 intake，并提前联系导师 |
| Concordia University | **APPLY / SUPERVISOR TRACK** | 已有实际导师接触/面试历史；Boss + DS-Hns 叙事匹配度高 | Zhijie Wang | 澄清 supervisor commitment、funding、正式 application/offer 流程 |

## 这一轮的执行优先级

### 立刻处理

1. **KAUST**：Spring 2027 截止 9 月 27 日，但不值得为了早一学期制造额外压力；材料现成就顺手投，否则直接等 9 月 28 日开放的 Fall 2027。
2. **PolyU**：如果 Jan 2027 也接受，9 月 30 日是最近硬截止。
3. **HKUST Spring 2027**：如果想抢 Feb 2027 入学，11 月 1 日前完成；否则可走 Fall 2027。
4. **Waterloo + HKU**：都在 12 月 1 日形成自然批次，适合自动化一起准备。
5. **Queen's**：材料相对干净，截止稍晚，可放在前一批之后。

### 套磁优先导师

- **Yuntian Deng (Waterloo)**：Boss 的 LLM communication / multi-agent / division-of-labour 几乎正面匹配。
- **Pengyu Nie (Waterloo)**：DS-Hns 的 software lifecycle / testing / maintenance 很顺。
- **Yu Pei (PolyU)**：program repair / testing / automatic fault repair 与 DS-Hns 的 recovery 路线非常直接。
- **Ka Ho Chow (HKU)**：LLM + trustworthy AI + cybersecurity + systems，而且当前公开有 PhD openings。
- **Linyi Li (SFU)**：LLM + trustworthy ML/security + software engineering，Boss/DS-Hns/Privacy Lens 可以合并叙事。
- **Tushar Sharma / Masud Rahman (Dalhousie)**：适合用“自主软件工程 + 调试/维护/评测”而不是泛 AI 套磁。
- **Marco Canini / Ali Shoker (KAUST)**：更偏系统、可靠性和 fault tolerance，适合 DS-Hns 的 24h 托管/恢复设计。

## 升级规则

WATCHLIST 中的学校只有在重新核验以下项目后才进入 ACTIVE：GRE、英语豁免、funding、考试/面试负担、当前 intake、申请 deadline。

所有自动化应以 `data/programs.yaml` 和 `data/supervisors.yaml` 为机器真源；本页只做懒人视图。