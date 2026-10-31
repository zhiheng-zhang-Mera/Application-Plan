#!/usr/bin/env python3
"""把 Search-Table/_raw/*.md 的 16 列明细表汇总成一份 CSV。

用法：python Search-Table/_brief/build_csv.py
输出：Search-Table/data/search-table.csv
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "_raw"
OUT = ROOT / "data" / "search-table.csv"

COLUMNS = [
    "region_file",
    "region",
    "state_province",
    "university",
    "program",
    "deadline_2027fall",
    "english_waiver",
    "gre",
    "outreach",
    "interview",
    "supervisor_acceptance",
    "funding",
    "other_materials",
    "academic_floor",
    "match_rate",
    "key_risk",
    "sources",
    "verified_date",
]

# 原始表规范：| 州/省 | 学校 | 项目 | 截止 | 英语 | GRE | 套磁 | 面试 | 导师接收 | 资助 | 其他材料 | 学术门槛 | 匹配率 | 风险 | 来源 | 核验日 |
EXPECTED = 16

SEP_RE = re.compile(r"^\|[\s:|-]+\|$")


def clean(cell: str) -> str:
    cell = cell.strip()
    cell = cell.replace("<br>", " / ").replace("<br/>", " / ")
    cell = cell.replace("**", "")
    cell = re.sub(r"\s+", " ", cell)
    return cell


def split_row(line: str) -> list[str] | None:
    line = line.rstrip()
    if not line.startswith("|"):
        return None
    if SEP_RE.match(line):
        return None
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    # 处理单元格内被转义的竖线
    parts = re.split(r"(?<!\\)\|", body)
    return [p.replace("\\|", "|") for p in parts]


def region_of(path: Path) -> str:
    stem = path.stem
    legacy = {
        "hk-hongkong": "中国香港",
        "cn-mainland": "中国大陆-本地院校",
        "cn-joint-and-branches": "中国大陆-合办与港校校区",
        "sg-singapore": "新加坡",
        "uk-united-kingdom": "英国",
        "ca-ontario-quebec": "加拿大",
        "ca-west-and-atlantic": "加拿大",
    }
    if stem in legacy:
        return legacy[stem]
    prefixes = (
        ("01", "中国香港"),
        ("02", "中国大陆-本地院校"),
        ("03", "中国大陆-合办与港校校区"),
        ("04", "新加坡"),
        ("05", "英国"),
        ("06", "加拿大"),
        ("07", "美国"),
    )
    for prefix, name in prefixes:
        if stem.startswith(prefix):
            return name
    return stem


def sources() -> list[Path]:
    """正式分区文档优先；尚未转换时回退到 _raw。"""
    docs = sorted(
        p
        for p in ROOT.glob("*.md")
        if p.name[:2].isdigit() and p.name != "00-申请人材料基线与门禁.md"
    )
    if docs:
        return docs
    return sorted(RAW.glob("*.md"))



def table_blocks(text: str) -> list[list[tuple[int, list[str]]]]:
    """按「连续的 | 行」切出表格块，保留行号。"""
    blocks: list[list[tuple[int, list[str]]]] = []
    current: list[tuple[int, list[str]]] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        cells = split_row(line)
        if cells is None:
            if current:
                blocks.append(current)
                current = []
            continue
        current.append((lineno, cells))
    if current:
        blocks.append(current)
    return blocks


def main() -> int:
    rows: list[dict[str, str]] = []
    problems: list[str] = []

    for path in sources():
        text = path.read_text(encoding="utf-8")
        count = 0
        blocks = table_blocks(text)
        data_blocks = [b for b in blocks if b and len(b[0][1]) == EXPECTED]
        if not data_blocks:
            print(f"{path.name}: 0 行（未找到 {EXPECTED} 列表格）")
            continue
        for block in data_blocks:
            header: list[str] | None = None
            for lineno, cells in block:
                if len(cells) != EXPECTED:
                    problems.append(
                        f"{path.name}:{lineno} 列数={len(cells)}（期望 {EXPECTED}）：{cells[1][:24] if len(cells) > 1 else ''}"
                    )
                    continue
                if SEP_RE.match("|" + "|".join(cells) + "|"):
                    continue
                if header is None and ("学校" in cells[1] or "州/省" in cells[0] or "城市/省" in cells[0]):
                    header = [c.strip() for c in cells]
                    continue
                if cells[0].strip() in {"州/省", "省份", "州", "省/州", "城市/省"}:
                    continue
                values = [clean(c) for c in cells]
                if not values[1] or not values[2]:
                    problems.append(f"{path.name}:{lineno} 学校或项目为空")
                    continue
                record = {
                    "region_file": path.name,
                    "region": region_of(path),
                    "state_province": values[0],
                    "university": values[1],
                    "program": values[2],
                    "deadline_2027fall": values[3],
                    "english_waiver": values[4],
                    "gre": values[5],
                    "outreach": values[6],
                    "interview": values[7],
                    "supervisor_acceptance": values[8],
                    "funding": values[9],
                    "other_materials": values[10],
                    "academic_floor": values[11],
                    "match_rate": values[12],
                    "key_risk": values[13],
                    "sources": values[14],
                    "verified_date": values[15],
                }
                rows.append(record)
                count += 1
        print(f"{path.name}: {count} 行")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n合计 {len(rows)} 行 → {OUT}")
    if problems:
        print("\n列数异常：")
        for p in problems[:40]:
            print("  " + p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
