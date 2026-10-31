#!/usr/bin/env python3
"""从汇总 CSV 生成可复现的统计表（分区分布、档位分布、截止日日历、排除清单）。

输出：Search-Table/_brief/generated-summary.md
用途：README 与 08 总评中的数字全部来自这里，避免手写漂移。
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "search-table.csv"
OUT = ROOT / "_brief" / "generated-summary.md"

BANDS = ["高", "中高", "中", "低", "极低", "排除", "未评级"]
DATE_RE = re.compile(r"(202[67])[-/年.]?(\d{1,2})[-/月.]?(\d{1,2})")


def band(match_rate: str) -> str:
    """只看括号前的主档位词，避免把备注里的「若…则判排除」误读成排除。"""
    head = re.split(r"[（(]", match_rate)[0].strip()
    for key in ("未评级", "排除", "极低", "中高", "高", "中", "低"):
        if head.startswith(key):
            return key
    return "未评级"


def first_date(text: str) -> date | None:
    """取该行最早出现的「2027 Fall 申请周期内」日期。

    Fall 2027 的申请窗口均在 2026-09 之后，故早于 2026-09-01 的日期多半是
    上一轮/入学时间/已关闭轮次的残留，不计入日历；晚于 2027-09-30 的亦然。
    """
    low, high = date(2026, 9, 1), date(2027, 9, 30)
    best: date | None = None
    for y, m, d in DATE_RE.findall(text):
        try:
            cur = date(int(y), int(m), int(d))
        except ValueError:
            continue
        if not (low <= cur <= high):
            continue
        if best is None or cur < best:
            best = cur
    return best


def main() -> int:
    with SRC.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    by_region: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_region[row["region"]].append(row)

    out: list[str] = ["# 自动生成统计（勿手改）", ""]
    out.append(f"> 数据源：`data/search-table.csv`（{len(rows)} 行）；由 `_brief/build_summary.py` 生成。")
    out.append("")

    out.append("## 一、分区 × 档位")
    out.append("")
    out.append("| 区域 | " + " | ".join(BANDS) + " | 合计 |")
    out.append("|---" * (len(BANDS) + 2) + "|")
    totals = Counter()
    for region in sorted(by_region):
        counter = Counter(band(r["match_rate"]) for r in by_region[region])
        totals.update(counter)
        cells = [str(counter.get(b, 0) or "") for b in BANDS]
        out.append(f"| {region} | " + " | ".join(cells) + f" | {len(by_region[region])} |")
    out.append("| **合计** | " + " | ".join(str(totals.get(b, 0)) for b in BANDS) + f" | {len(rows)} |")
    out.append("")

    out.append("## 二、可申池（档位 ≥ 中高）")
    out.append("")
    out.append("| 区域 | 州/省 | 学校 | 项目 | 匹配率 | 导师接收 | 资助要点 |")
    out.append("|---|---|---|---|---|---|---|")
    ranked = [r for r in rows if band(r["match_rate"]) in {"高", "中高"}]
    ranked.sort(key=lambda r: (band(r["match_rate"]) != "高", r["region"], r["university"]))
    for r in ranked:
        fund = r["funding"].replace("|", "/")[:46]
        out.append(
            f"| {r['region']} | {r['state_province']} | {r['university'][:34]} | {r['program'][:30]} | "
            f"{r['match_rate']} | {r['supervisor_acceptance'][:10]} | {fund} |"
        )
    out.append(f"\n合计 **{len(ranked)}** 行达到「中高」及以上（无任何一行被评为「高」）。")
    out.append("")

    out.append("## 三、2027 Fall 申请周期的关键日期（自动提取，含开放日 / 优先轮 / 截止日）")
    out.append("")
    out.append("> 说明：每行只取该行「截止」列中最早出现的、落在 2026-09-01～2027-09-30 的日期。"
               "因此同一行若同时写了开放日与截止日，这里显示的是开放日；**具体截止以表中该行原文为准**。")
    out.append("")
    calendar: dict[date, list[str]] = defaultdict(list)
    undated: list[str] = []
    for r in rows:
        if band(r["match_rate"]) == "排除":
            continue
        d = first_date(r["deadline_2027fall"])
        label = f"{r['university'][:30]}（{r['region']}）"
        if d is None:
            undated.append(label)
        else:
            calendar[d].append(label)
    out.append("| 日期 | 到期项目 |")
    out.append("|---|---|")
    for d in sorted(calendar):
        out.append(f"| {d.isoformat()} | " + "<br>".join(calendar[d]) + " |")
    out.append("")
    out.append(f"未取到明确日期的可申项目 {len(undated)} 个（滚动招生或官网未挂 2027 日期）：")
    out.append("")
    for label in undated:
        out.append(f"- {label}")
    out.append("")

    out.append("## 四、排除清单（硬门槛，不进入概率讨论）")
    out.append("")
    out.append("| 区域 | 学校 | 排除原因（表中原文摘要） |")
    out.append("|---|---|---|")
    for r in rows:
        if band(r["match_rate"]) != "排除":
            continue
        reason = r["key_risk"].replace("|", "/")[:70]
        out.append(f"| {r['region']} | {r['university'][:34]} | {reason} |")
    out.append("")

    OUT.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(rows)} 行 → {OUT}")
    print("档位分布：" + ", ".join(f"{b}={totals.get(b, 0)}" for b in BANDS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
