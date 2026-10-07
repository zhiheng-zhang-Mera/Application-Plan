# 2026-10-6 Package Index

> **Frozen snapshot / NOT SENT**  
> **Rev.2 — 2026-10-07：** 所有导师邮件按 Utopia current main、REX/PCF 新分支证据与带 grading scale 的成绩 CSV 二次改写；每封邮件在英文版本后追加中文内部对照译文。

共 **24 个导师包 + 1 个 SUTD Jan-2027 program-level 正式申请包**。

## 香港本部

| 学校 | 导师 | 状态 | 主要文件 |
|---|---|---|---|
| CUHK | James Cheng | SELECTED_ROUND_2026-10-07-B | EMAIL-DRAFT, CV, transcript requirement |
| HKUST | Mo Li | DRAFT_READY_RECHECK | EMAIL-DRAFT, CV |
| HKUST | Shing-Chi Cheung | BLOCKED_MISSING_PHOTO | EMAIL-DRAFT, CV, recent-photo gap |
| HKUST | Song Guo | DRAFT_READY_RECHECK | EMAIL-DRAFT, CV |
| HKU | Chenshu Wu | BLOCKED_ACADEMIC_EQUIVALENCY_AND_RANK | EMAIL-DRAFT, CV, Research-Proposal |
| HKU | Heming Cui | BLOCKED_ACADEMIC_EQUIVALENCY | EMAIL-DRAFT, CV, bachelor transcript requirement |
| HKU | Zuming Jiang | BLOCKED_ACADEMIC_EQUIVALENCY | EMAIL-DRAFT, CV, Research-Interest |
| HKU | Ka Ho Chow | BLOCKED_ACADEMIC_EQUIVALENCY | EMAIL-DRAFT, CV |
| CityUHK | Heqing Huang | CLOSED_TIMEOUT | FOLLOWUP-DRAFT, refreshed CV |
| CityUHK | Zhenjiang Li | SELECTED_ROUND_2026-10-07-B | EMAIL-DRAFT, CV |
| CityUHK | Nan Guan | HOLD_CITYU_THREAD_LOCK | EMAIL-DRAFT, CV |
| CityUHK | Weifa Liang | HOLD_CITYU_THREAD_LOCK | EMAIL-DRAFT, CV, Research-Statement |
| PolyU | Yu Pei | CLOSED_TIMEOUT | FOLLOWUP-DRAFT, refreshed CV |
| PolyU | Yu Liu | SELECTED_ROUND_2026-10-07-B | EMAIL-DRAFT, CV, transcript requirement |

## 港校大陆分校

| 学校 | 导师 | 状态 | 主要文件 |
|---|---|---|---|
| CUHK-Shenzhen | Jinke Ren | BLOCKED_REPRESENTATIVE_PUBLICATION_MATERIAL | EMAIL-DRAFT, CV, Representative-Work gap |
| HKUST(GZ) | Zhidan Liu | WATCH_CAPACITY_RECHECK | capacity-inquiry draft, CV |
| HKUST(GZ) | Tengfei Chang | WATCH_CAPACITY_RECHECK | capacity-inquiry draft, CV |
| HKUST(GZ) | Kaishun Wu | WATCH_NO_CURRENT_RECRUITMENT_SIGNAL | conditional draft, CV |
| HKUST(GZ) | Lingjie Duan | BACKUP_THEORY_BURDEN_AND_RANK_GAP | EMAIL-DRAFT, CV, GPA/rank gap |

## 新加坡

| 学校 | 导师 | 状态 | 主要文件 |
|---|---|---|---|
| SUTD | Ruochen Zhao | SELECTED_ROUND_2026-10-07-B | EMAIL-DRAFT, CV |
| SUTD | Thanh Le-Cong | CLOSED_TIMEOUT | FOLLOWUP-DRAFT, refreshed CV |
| NTU | Rui Tan | WATCH_ACADEMIC_EQUIVALENCY | EMAIL-DRAFT, CV |
| NUS | Chengpeng Wang | BACKUP_NUS_FRICTION | EMAIL-DRAFT, CV, Research-Problems |
| NUS | Abhik Roychoudhury | BACKUP_CAPACITY_RECHECK | capacity-inquiry draft, CV |

## Program-level

### SUTD Jan-2027

`singapore/SUTD/_program-Jan-2027/`

已生成：
- Statement of Objectives
- broad research CV
- formal application checklist
- referee plan
- attachments manifest

标准 SUTD PhD **不要求 supervisor pre-approval**；该 program-level 包与 Ruochen Zhao 的 Fall-2027 opening 分开。

## 共享证据

见 `_shared/`：
- UTOPIA-SNAPSHOT
- APPLICANT-SNAPSHOT
- PUBLICATION-STATUS
- DOCUMENTS-MANIFEST

## 2026-10-07 旧线程 timeout-clear

- Yu Li / CUHK → `CLOSED_TIMEOUT`
- Heqing Huang / CityU → `CLOSED_TIMEOUT`
- Yu Pei / PolyU → `CLOSED_TIMEOUT`
- Thanh Le-Cong / SUTD → `CLOSED_TIMEOUT`

James Cheng、Zhenjiang Li、Yu Liu、Ruochen Zhao 的同校锁因此释放。历史邮件仍保留。

## Rev.2 证据刷新

- Utopia main: `cc799234e7daa3d8ccfde5673b9d07ccb2376742`
- Digital-City main: `78d9efe4774d257678ad09c7c3cfb95d6d352306`
- REX-801～806：COMPLETE
- REX-807：development complete / opposite-host review pending
- PCF-700：accepted audit scope
- PCF-701：Windows CPU 假零修复候选已异机复检 ACCEPTED，但未宣称 main merge
- PCF full-flow `998440c...`：**verified development candidate only**，不是 programme completion / physical acceptance / main merge
- Bachelor / Master CSV：已内嵌官方 grading scale；只在导师要求成绩时使用
- 邮件文件：英文为发送候选；中文仅内部校对，禁止发送

## PDF

所有导师 `CV.tex` 和 SUTD program CV 由 `.github/workflows/build-tracking-cvs.yml` 自动编译为同目录 `CV.pdf`。
