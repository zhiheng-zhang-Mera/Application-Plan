#!/usr/bin/env python3
"""v4：材料 v1.3（arXiv ×2 + JSS/IST/SQJ 三条投稿线 + 主线细化为 SE 导向）+ 条件概率（找 80%+ 通道）。

与 v3 的差别
------------
1. 材料加成（现状）
   · 主线由「多 agent 复合系统」细化为 **软件工程导向的多智能体复合系统（agentic SE）**：目标期刊
     JSS / IST / SQJ 全部是 SE venue，说明产出方向已从 HCI/wearable 收敛到 SE。
   · **「准备投递」不等于「在审」也不等于「接收」**，因此只给方向契合加分，不给产出加分：
       导师主导行（导师接收 = 是 / 条件）: +3   （fit 与可做性更清楚，PI 熟悉这些 venue）
       委员会制行                        : +1   （方向匹配更好，但无在审/接收记录）
2. 条件概率（回答「80%+ 在哪」）
   · 场景 A「已拿到导师内诺/书面同意」：导师主导行 +18（该行的最大不确定性正是导师）
   · 场景 B「接受自费（不依赖全奖）」：可自费通道 +12（澳 / 新西兰 / 日本国立 / 澳门 / 资助列为低）
   · 已带 warm lead 的行（澳门 UM、Concordia）不再重复加 A 的 18
   · 上限 88%（不声称「几乎确定」）
3. 回写：把所有分区文档（01–07l、10a–10f）的「匹配率」列统一改写为 **v4 现状概率（%）**，
   并在文件头插入指向 12 号文档的说明。原始区间仍保留在 08/09/11 与 _raw 历史 commit 中。

输出：data/search-table-v4.csv、回写各分区文档、回填 12-高成功率通道与全表修正.md 的 AUTO 段。
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_csv import split_row, EXPECTED  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "search-table-v3.csv"
OUT = ROOT / "data" / "search-table-v4.csv"
DOC = ROOT / "12-高成功率通道与全表修正.md"

TIERS = [
    ("SS", 80, "兜底"),
    ("S", 60, "保底"),
    ("S-", 55, "准保底"),
    ("A", 50, "稳妥"),
    ("B", 40, "主申"),
    ("C", 30, "可试"),
    ("D", 20, "偏低"),
    ("E", 10, "低"),
    ("F", 0, "极低"),
]
WARM = ("University of Macau", "Concordia")          # 已有在途申请 / PI 回信，不重复加内诺分
CHEAP = ("新西兰", "日本", "澳大利亚", "韩国与澳门")   # 可自费或学费极低的通道


def tier_of(p: float) -> str:
    for code, floor, name in TIERS:
        if p >= floor:
            return f"{code} {name}"
    return "F 极低"


def has(p: float) -> str:
    return f"{p:.0f}%"


def main() -> int:
    with SRC.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    out: list[dict[str, str]] = []
    for r in rows:
        raw = r["admit_pct"]
        if raw in {"—", ""} or r["tier"].startswith("X") or r["tier"] == "未评级":
            out.append({**r, "p_now": "—", "tier_v4": r["tier"], "p_cond": "—",
                        "tier_cond": r["tier"], "cond_note": "—"})
            continue

        p3 = float(raw.rstrip("%"))
        sup = r["supervisor_acceptance"].startswith(("是", "条件"))
        bounce = 3.0 if sup else 1.0
        p_now = min(70.0, p3 + bounce)

        warm = any(w in r["university"] for w in WARM)
        cheap = r["region"] in CHEAP or r["fund_confidence"] == "低"
        plus = 0.0
        note = []
        if sup and not warm:
            plus += 18.0
            note.append("内诺 +18")
        if cheap:
            plus += 12.0
            note.append("可自费 +12")
        if warm:
            note.append("已有 warm lead，不重复加内诺")
        p_cond = min(88.0, p_now + plus)

        out.append({
            **r,
            "p_now": has(p_now),
            "tier_v4": tier_of(p_now),
            "p_cond": has(p_cond),
            "tier_cond": tier_of(p_cond),
            "cond_note": "；".join(note) if note else "无条件加成",
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)

    t_now = Counter(r["tier_v4"] for r in out)
    t_cond = Counter(r["tier_cond"] for r in out)
    order = [f"{c} {n}" for c, _, n in TIERS] + ["X 排除", "未评级"]
    print(f"{len(out)} 行 → {OUT}")
    print("现状：" + ", ".join(f"{k}={t_now.get(k,0)}" for k in order if t_now.get(k)))
    print("条件：" + ", ".join(f"{k}={t_cond.get(k,0)}" for k in order if t_cond.get(k)))

    # ---------- 回写各分区文档的「匹配率」列 ----------
    lookup = {}
    for r in out:
        lookup[(r["region"], r["university"][:30])] = r
    written = 0
    for doc in sorted(ROOT.glob("0[1-9]*.md")) + sorted(ROOT.glob("10*.md")):
        if doc.name.startswith(("00-", "08-", "09-")):
            continue
        lines = doc.read_text(encoding="utf-8").splitlines()
        changed = 0
        for i, line in enumerate(lines):
            cells = split_row(line)
            if cells is None or len(cells) != EXPECTED:
                continue
            if "学校" in cells[1]:
                continue
            m = [r for r in out if r["university"][:30] == cells[1].strip()[:30]
                 or r["university"] == cells[1].strip()]
            if not m:
                continue
            p = m[0]["p_now"]
            if p == "—":
                continue
            cells[12] = f"**{p}**"
            lines[i] = "| " + " | ".join(cells) + " |"
            changed += 1
        if changed:
            note = ("> **2026-10-31 修正：** 本表「匹配率」列已统一改为 v4 **现状概率（%）**"
                    "（材料 = 2 篇 arXiv + JSS/IST/SQJ 三条投稿线 + SE 导向主线）。"
                    "条件概率与 80%+ 通道见 [`12-高成功率通道与全表修正.md`](12-高成功率通道与全表修正.md)。"
                    "原始区间保留在 `08`/`09`/`11` 与历史 commit 中。")
            if note not in "\n".join(lines[:12]):
                insert_at = next((k for k, l in enumerate(lines) if l.startswith("# ")), 0) + 2
                lines.insert(insert_at, note)
                lines.insert(insert_at + 1, "")
            doc.write_text("\n".join(lines) + "\n", encoding="utf-8")
            written += changed
            print(f"{doc.name}: 回写 {changed} 行")
    print(f"共回写 {written} 行匹配率")

    # ---------- 生成 12 号文档片段 ----------
    def pct(r: dict[str, str], key: str) -> float:
        try:
            return float(r[key].rstrip("%"))
        except ValueError:
            return -1.0

    matrix = ["| 区域 | " + " | ".join(["SS ≥80", "S 60–79", "S- 55–59", "A 50–54", "B 40–49",
                                        "C 30–39", "D 20–29", "E 10–19", "F <10", "排除/未评级"]) + " | 行数 |",
              "|---" * 11 + "|"]
    by_region: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in out:
        by_region[r["region"]].append(r)
    for region in sorted(by_region):
        sub = by_region[region]
        c = Counter(r["tier_v4"] for r in sub)
        cells = [str(c.get(f"{code} {name}", 0) or "") for code, _, name in TIERS]
        cells.append(str(c.get("X 排除", 0) + c.get("未评级", 0) or ""))
        matrix.append(f"| {region} | " + " | ".join(cells) + f" | {len(sub)} |")

    def tbl(rows_: list[dict[str, str]], with_cond: bool = True) -> list[str]:
        if with_cond:
            head = ["| 区域 | 学校 | 现状 | 条件概率 | 条件加成 | 资助 | 关键风险 |",
                    "|---|---|---|---|---|---|---|"]
            body = [
                f"| {r['region']} | {r['university'][:30]} | **{r['p_now']}** | **{r['p_cond']}** | "
                f"{r['cond_note'][:18]} | {r['fund_confidence']} | {r['key_risk'][:22].replace('|','/')} |"
                for r in rows_
            ]
        else:
            head, body = ["| 区域 | 学校 | 现状 | 档位 | 资助 |", "|---|---|---|---|---|"], [
                f"| {r['region']} | {r['university'][:30]} | {r['p_now']} | {r['tier_v4']} | {r['fund_confidence']} |"
                for r in rows_
            ]
        return head + body

    now80 = sorted([r for r in out if pct(r, "p_now") >= 80], key=lambda r: -pct(r, "p_now"))
    cond80 = sorted([r for r in out if pct(r, "p_cond") >= 80], key=lambda r: -pct(r, "p_cond"))
    near = sorted([r for r in out if 70 <= pct(r, "p_cond") < 80], key=lambda r: -pct(r, "p_cond"))
    top_now = sorted([r for r in out if pct(r, "p_now") >= 50], key=lambda r: -pct(r, "p_now"))

    full = ["| 区域 | 学校 | 现状 | 档位 | 条件 | 条件档 | 资助 |", "|---|---|---|---|---|---|---|"]
    for r in sorted(out, key=lambda x: (-pct(x, "p_now"), x["region"])):
        full.append(
            f"| {r['region']} | {r['university'][:28]} | {r['p_now']} | {r['tier_v4']} | "
            f"{r['p_cond']} | {r['tier_cond']} | {r['fund_confidence']} |"
        )

    if DOC.exists():
        text = DOC.read_text(encoding="utf-8")
        blocks = {
            "MATRIX": "\n".join(matrix),
            "COUNTS": (
                f"全表 **{len(out)} 行**。**现状**：SS ≥80% **{t_now.get('SS 兜底',0)} 行**、"
                f"S 60–79% {t_now.get('S 保底',0)}、S- 55–59% {t_now.get('S- 准保底',0)}、"
                f"A {t_now.get('A 稳妥',0)}、B {t_now.get('B 主申',0)}、C {t_now.get('C 可试',0)}、"
                f"D {t_now.get('D 偏低',0)}、E {t_now.get('E 低',0)}、F {t_now.get('F 极低',0)}、"
                f"排除/未评级 {t_now.get('X 排除',0) + t_now.get('未评级',0)}。"
                f"**条件概率（拿到内诺 + 可自费）**：SS ≥80% **{t_cond.get('SS 兜底',0)} 行**、"
                f"S {t_cond.get('S 保底',0)}、S- {t_cond.get('S- 准保底',0)}、"
                f"A {t_cond.get('A 稳妥',0)}、B {t_cond.get('B 主申',0)}。"
            ),
            "NOW80": "\n".join(tbl(now80)) if now80 else "_（现状无一行达到 80%）_",
            "COND80": "\n".join(tbl(cond80)) if cond80 else "_（即使加上条件加成，也没有一行达到 80%）_",
            "NEAR": "\n".join(tbl(near)) if near else "_（无）_",
            "TOP": "\n".join(tbl(top_now, with_cond=False)),
            "FULL": "\n".join(full),
            "N_NOW80": str(len(now80)),
            "N_COND80": str(len(cond80)),
            "N_NEAR": str(len(near)),
            "N_TOP": str(len(top_now)),
        }
        for key, body in blocks.items():
            if key.startswith("N_"):
                # 行内占位（表格单元格内），不能插入换行
                text = re.sub(
                    rf"(<!-- AUTO:{key} -->).*?(<!-- /AUTO:{key} -->)",
                    lambda m, b=body, k=key: f"<!-- AUTO:{k} -->{b}<!-- /AUTO:{k} -->",
                    text,
                    flags=re.S,
                )
                continue
            text = re.sub(
                rf"(<!-- AUTO:{key} -->)(?:.|\n)*?(<!-- /AUTO:{key} -->)",
                lambda m, b=body, k=key: f"<!-- AUTO:{k} -->\n{b}\n<!-- /AUTO:{k} -->",
                text,
            )
        DOC.write_text(text, encoding="utf-8")
        print("已回填 12-高成功率通道与全表修正.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
