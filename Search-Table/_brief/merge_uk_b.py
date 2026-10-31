#!/usr/bin/env python3
"""把英国 B 组被拆分出的多个分片（uk-b / uk-c / uk-d / uk-4-schools）合并成一张表。

首轮英国代理中途失败，其子代理留下了 uk-c、uk-d、uk-4-schools 三份可用分片。
本脚本按「学校」去重合并到 uk-b.md，保留原有 16 列格式与每行自带的来源与核验日。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "_raw"
PARTS = ["uk-b.md", "uk-c.md", "uk-d.md", "uk-sheffield-newcastle-nottingham-leeds.md"]
TARGET = RAW / "uk-b.md"
EXPECTED = 16
SEP_RE = re.compile(r"^\|[\s:|-]+\|$")


def split_row(line: str) -> list[str] | None:
    if not line.startswith("|"):
        return None
    body = line.strip()[1:]
    if body.endswith("|"):
        body = body[:-1]
    cells = re.split(r"(?<!\\)\|", body)
    if len(cells) != EXPECTED:
        return None
    if SEP_RE.match(line.strip()):
        return None
    return [c.strip() for c in cells]


def key(cells: list[str]) -> str:
    name = cells[1]
    for token in ("（", "(", " - ", ","):
        if token in name:
            name = name.split(token)[0]
    return re.sub(r"[^a-z]", "", name.lower())[:18]


def main() -> int:
    rows: dict[str, list[str]] = {}
    order: list[str] = []
    notes: list[str] = []

    for part in PARTS:
        path = RAW / part
        if not path.exists():
            print(f"跳过（不存在）：{part}")
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            cells = split_row(line)
            if not cells:
                continue
            if cells[0] in {"州/省", "省份", "城市/省"}:
                continue
            k = key(cells)
            if k in rows:
                continue
            rows[k] = cells
            order.append(k)
            _ = notes.append(part) if False else None

    if not rows:
        print("没有可合并的行", file=sys.stderr)
        return 1

    header = (
        "| 州/省 | 学校 | 项目 | 2027F截止 | 英语豁免 | GRE | 套磁 | 面试 | 导师接收 | 资助 | "
        "其他材料 | 学术门槛 | 匹配率 | 风险 | 来源 | 核验日 |"
    )
    sep = "|" + "---|" * EXPECTED

    out = [
        "# 英国 B 组（10 校）2027 Fall CS PhD 检索原始表",
        "",
        "> 检索代理：uk-b（含 uk-c / uk-d / uk-4-schools 三个分片合并）；核验日：2026-10-31；覆盖 10 校："
        "Sheffield、Glasgow、St Andrews、Lancaster、Surrey、Newcastle、Nottingham、Leeds、Durham、QMUL。",
        "> 总体置信度：中偏低 —— 10 校均拿到「是否需要先联系导师」与「英语豁免口径」中的至少一条官方原文，"
        "但 Durham 全站 403、Nottingham/Leeds 正文未取全、Surrey/QMUL 的 2027 截止与金额未取到，"
        "故资助与学术门槛多格为 UNKNOWN。",
        "",
        "## 一、明细表（每校一行）",
        "",
        header,
        sep,
    ]
    for k in order:
        out.append("| " + " | ".join(rows[k]) + " |")

    out += [
        "",
        "## 二、分区结论（B 组）",
        "",
        "- **导师先决是本组唯一一致的硬规则**：St Andrews、Lancaster、Glasgow、Nottingham 四校明写"
        "「必须先联系/取得导师支持」；Newcastle、Durham、Leeds、QMUL、Sheffield 未取到明文。",
        "- **英语豁免对本申请人成立**：Glasgow 明文含加拿大英语授课学位、Surrey 明确加拿大/澳洲在名单、"
        "Sheffield 的 5 年内首学位口径覆盖 2024 UBC 学位；Newcastle 属「需充分证据」的条件类。",
        "- **GRE 在本组不是障碍**：已取到的 9 校页面无一要求 GRE（Durham 除外，因全站 403）。",
        "- **资金是本组的死结**：Sheffield 明示 CSC 与校级奖学金对 2027 entry 已关闭；Nottingham 的 EPSRC DLA "
        "已截止；Glasgow 的学院 studentship 是唯一明示「含国际生学费 + UKRI stipend £22,437」的一条，但名额未公布。",
        "- **门槛普遍卡硕士**：QMUL「normally have an MSc」、Glasgow「usually a 2.1」、Lancaster "
        "「First Class or Distinction」，而申请人硕士 WAM 67.5（派生）且 2026 年末才授予。",
        "- 排序（录取可能性）：Glasgow ≈ Newcastle ≈ Nottingham ≈ Surrey(中) > St Andrews / Lancaster / "
        "Sheffield / QMUL(低) > Durham（零信息）。若同时要求「录取 + 全奖」，除 Glasgow 外基本不成立。",
        "",
        "## 三、未能核实项",
        "",
        "1. Durham 全站 CloudFront 403（含系页与 /study/），零信息，需换抓取方式或人工打开。",
        "2. Nottingham 课程页正文、Leeds 英语豁免条款、Newcastle 学位页 entry requirements 段均未取到。",
        "3. Surrey / QMUL 的 2027 Fall 常规截止日与申请费未取到（滚动招生页未标年份）。",
        "4. St Andrews / Lancaster 的推荐信数量、申请费、2027 专属截止日未取到。",
        "5. 全组没有一校公布 2027 entry 的国际生全奖名额，金额均为年度重定。",
    ]
    TARGET.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"合并 {len(order)} 校 → {TARGET.name}")

    for part in PARTS[1:]:
        path = RAW / part
        if path.exists():
            path.unlink()
            print(f"已删除分片：{part}")
    stub = RAW / "uk-united-kingdom.md"
    if stub.exists():
        stub.unlink()
        print("已删除首轮失败留下的空壳：uk-united-kingdom.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
