#!/usr/bin/env python3
"""把 _raw/*.md 的检索原始表升级为 Search-Table 下的正式分区文档。

- 只替换标题行并插入导语，表格与结论原样保留（不重写代理结论，保可追溯）。
- 运行后删除 _raw 目录，避免同一张表在仓库里出现两份。
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "_raw"

DOCS: dict[str, tuple[str, str, list[str]]] = {
    "hk-hongkong": (
        "01-中国香港.md",
        "# 01 · 中国香港：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖香港八所教资会资助院校（HKU / CUHK / HKUST / CityUHK / PolyU / HKBU / Lingnan / EdUHK），"
            "含 HKPFS 2027/28 与各校常规 PGS 两条路线。",
            "本表是**主战场**：英语豁免全部成立、GRE 全免、资助覆盖完整、截止集中在 2026-12-01。",
        ],
    ),
    "cn-mainland": (
        "02-中国大陆-本地院校.md",
        "# 02 · 中国大陆（本地院校）：2027 Fall 计算机博士招生流程完整表",
        [
            "覆盖 22 个大陆本地招生单位，以「申请-考核制」为主线（清北复交浙 + 中科院三所 + 南科大/上科大/西湖等）。",
            "三个结构性差异：**导师同意是事实上的硬前置**、**论文条款一旦写进报考条件即无破格空间**、"
            "**应届硕士（2027-09-01 前取得学位）普遍被接受**。",
        ],
    ),
    "cn-joint-and-branches": (
        "03-中国大陆-合办与港校校区.md",
        "# 03 · 中国大陆（中外合作办学 + 港校内地校区）：2027 Fall 博士招生流程完整表",
        [
            "A 组为中外合作办学（NYU Shanghai / XJTLU / UNNC / BNBU 等），B 组为港校内地校区"
            "（HKUST-GZ / CUHK-Shenzhen / CityU 东莞等）。",
            "本组最容易被忽略的是**学位授予方与学历认证路径**差异：港校内地校区走「中外合作办学学历学位认证」，"
            "不等于留服国外学历认证；XJTLU 还牵涉 ATAS 审查。",
        ],
    ),
    "sg-singapore": (
        "04-新加坡.md",
        "# 04 · 新加坡：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖 NUS / NTU / SUTD / SMU / SIT（SIT 无 CS 博士）。",
            "本区是**边际成本最低的加申区**：免英语、免 GRE（SMU 除外）、申请费 15–50 SGD、"
            "委员会制不要求导师前置。",
        ],
    ),
    "uk-a": (
        "05a-英国-综合与理工学院.md",
        "# 05a · 英国（A 组：综合与理工学院）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖 Oxford / Cambridge / Imperial / UCL / Edinburgh / Manchester / KCL / Bristol / "
            "Southampton / Warwick 十校。",
            "英国是**导师主导制**：录取几乎都要求先取得 supervisor consent；但国际生全额资助极稀缺，"
            "这是本区最大的结构性约束（见本文件末节资金结论）。",
        ],
    ),
    "uk-b": (
        "05b-英国-其他重点院校.md",
        "# 05b · 英国（B 组：其他重点院校）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖 Sheffield / Glasgow / St Andrews / Lancaster / Surrey / Newcastle / Nottingham / "
            "Leeds / Durham / QMUL 十校。",
            "B 组的实际定位是「录取可及性略高、但资金更依赖 CSC 或自费」，判断前请先看资金列。",
        ],
    ),
    "ca-ontario": (
        "06a-加拿大-安大略.md",
        "# 06a · 加拿大（安大略省）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖 Toronto / Waterloo / McMaster / Queen's / Western / Ottawa / Carleton / York / TMU / "
            "Guelph / Ontario Tech 十一校。",
            "安大略是加拿大 CS 博士最密集的一省，也是「保证最低资助 + 国际生学费差额」矛盾最突出的一省。",
        ],
    ),
    "ca-quebec-atlantic": (
        "06b-加拿大-魁北克与大西洋.md",
        "# 06b · 加拿大（魁北克 + 大西洋四省）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖 McGill / Concordia / UdeM / Polytechnique / Sherbrooke + Dalhousie / UNB / Memorial / "
            "Saint Mary's 九校。",
            "Concordia 是当前唯一已提交并在等导师接收的 Fall 2027 申请（申请号 20814667）。",
        ],
    ),
    "ca-bc-prairies": (
        "06c-加拿大-BC与草原省.md",
        "# 06c · 加拿大（BC / 阿尔伯塔 / 萨斯喀彻温 / 曼尼托巴）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖 UBC / SFU / UVic + UAlberta / UCalgary / USask / UManitoba / Regina 八校。",
            "UBC 是申请人本科母校：成绩单与原校评分口径由本校直接承认，这是该校唯一的隐性便利。",
        ],
    ),
    "us-california": (
        "07a-美国-加利福尼亚.md",
        "# 07a · 美国（加利福尼亚州）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖加州 12 所 CS PhD 项目。加州是**成绩硬线最密集**的一州（UCLA / UCSB / UCR 均有明文 GPA 期待）。",
        ],
    ),
    "us-northeast": (
        "07b-美国-新英格兰.md",
        "# 07b · 美国（新英格兰六州）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖 MA / RI / CT / NH / VT / ME 六州 18 校。",
            "本区确立了一条关键口径：**MIT 的英语豁免只认本科、只认最近 5 年、只认指定 6 国**"
            "（研究生学位不计），这类「只认本科」条款在其它美国校也存在。",
        ],
    ),
    "us-ny-nj-pa": (
        "07c-美国-纽约新泽西宾州.md",
        "# 07c · 美国（纽约 / 新泽西 / 宾夕法尼亚）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖 NY / NJ / PA 三州 19 校，含已备好全套材料的 Syracuse CISE"
            "（招生办已书面确认其语言考试豁免资格）。",
        ],
    ),
    "us-midwest": (
        "07d-美国-中西部.md",
        "# 07d · 美国（IL / OH / MI / IN / WI）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖五州 20 校。本区推翻了「GRE 已普遍取消」的通行假设：Northwestern、IIT、"
            "Indiana Bloomington 三校构成硬门槛，UIUC 则有「录取可免、但拿资助必须交口语分」的特殊条款。",
        ],
    ),
    "us-mid-atlantic": (
        "07e-美国-中大西洋.md",
        "# 07e · 美国（MD / DC / DE / VA / WV）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖中大西洋五州/特区 CS PhD 项目。",
        ],
    ),
    "us-upper-midwest": (
        "07f-美国-上中西部.md",
        "# 07f · 美国（MN / IA / MO / KS / NE）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖上中西部五州 CS PhD 项目。这一带的公立旗舰是申请人相对最现实的一档。",
        ],
    ),
    "us-plains": (
        "07g-美国-平原与俄克拉何马.md",
        "# 07g · 美国（ND / SD / OK / AR）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖北部平原与俄克拉何马、阿肯色两州 CS PhD 项目。",
        ],
    ),
    "us-texas-louisiana": (
        "07h-美国-得克萨斯与路易斯安那.md",
        "# 07h · 美国（Texas / Louisiana）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖得州 9 校与路易斯安那 3 校。UT Dallas / UTSA / Houston / LSU 是本区现实档。",
        ],
    ),
    "us-southeast": (
        "07i-美国-东南部.md",
        "# 07i · 美国（GA / NC / SC / TN）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖东南部四州 12 校。NC State / UNCC / Clemson 是本区现实档。",
        ],
    ),
    "us-deep-south-florida": (
        "07j-美国-深南部与佛罗里达.md",
        "# 07j · 美国（AL / MS / KY / FL）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖深南部与佛罗里达 13 校。UCF / USF / FIU / Auburn / UAB 是本区现实档。",
        ],
    ),
    "us-pacific-northwest": (
        "07k-美国-太平洋西北与岛屿.md",
        "# 07k · 美国（WA / OR / ID / MT / HI / AK / WY）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖太平洋西北、山地北缘与夏威夷/阿拉斯加。WSU / Oregon State / Portland State / "
            "Idaho / Montana State 是本区现实档。",
        ],
    ),
    "us-mountain": (
        "07l-美国-山地州.md",
        "# 07l · 美国（CO / UT / AZ / NM / NV）：2027 Fall CS PhD 招生流程完整表",
        [
            "覆盖山地五州 11 校。ASU / Arizona / Utah / UNM / UNLV 是本区现实档。",
        ],
    ),
}


def main() -> int:
    moved = 0
    missing = []
    for stem, (doc_name, title, intro) in DOCS.items():
        src = RAW / f"{stem}.md"
        if not src.exists():
            missing.append(stem)
            continue
        text = src.read_text(encoding="utf-8")
        lines = text.splitlines()
        if lines and lines[0].startswith("# "):
            lines = lines[1:]
        block = [title, ""]
        block += [f"> {line}" for line in intro]
        block += [
            "",
            "> 字段规范与「匹配率」档位定义见 [`00-申请人材料基线与门禁.md`](00-申请人材料基线与门禁.md)；"
            "检索方法、并发分区与总评见 [`README.md`](README.md)。核验日与官方来源写在各行末尾；"
            "凡标 `UNKNOWN` 的格子表示**未在官方页面取得依据**，不得按惯例推断。",
            "",
        ]
        out = ROOT / doc_name
        out.write_text("\n".join(block + lines) + "\n", encoding="utf-8")
        moved += 1
        print(f"{stem}.md → {doc_name}")

    if missing:
        print("\n尚未生成的分区：" + ", ".join(missing))
        return 1

    if RAW.exists():
        shutil.rmtree(RAW, ignore_errors=True)
        print("\n_raw 已删除（内容已迁入正式分区文档，历史可查 git）")
    print(f"共转换 {moved} 个分区")
    return 0


if __name__ == "__main__":
    sys.exit(main())

