#!/usr/bin/env python3
"""v3：改为「按百分比分档」，并把录取概率与资助确定性拆成两个轴，加入第二批扩区数据。

输入
----
- data/search-table.csv           第一批 258 行（v1 基线信息）
- data/search-table-v2.csv        v2 复评（提供调整后的区间）
- data/search-table-expansion.csv 第二批扩区（澳洲/新西兰/日本/韩国·澳门/欧洲）

输出
----
- data/search-table-v3.csv
- 回填 11-百分比分档与保底投递清单.md 中的 <!-- AUTO:* --> 段

模型（公开、可改）
------------------
录取概率 p = 基线区间中点 + 主线契合加成(2) ，封顶 70%。
  · 主线已改为「多 agent 复合系统」，与 Codex Boss / Utopia / Digital-City / Quant-Ultra 的项目组合
    高度一致，委员会与 PI 都更容易定位，故统一 +2；不再对 top 校额外加码。
  · 排除 / 未评级 行不参与打分。

资助确定性 D（启发式，从「资助」列原文判断）
  高 = 出现 guarantee / 保证 / 全奖 / 全额 / 自动 / PGS / HKPFS / 覆盖学费（且无否定词）
  低 = 出现 无保证 / 不保证 / 非保证 / 自费 / 未公布 / limited
  中 = 出现 竞争 / 申请 / typically / eligible
  未知 = 其余

组合建议
  保底   = p ≥ 60 且 D ≠ 低
  高成功 = 50 ≤ p < 60 且 D = 高
  主申   = 40 ≤ p < 60（其余）
  冲刺   = 25 ≤ p < 40
  不建议 = p < 25
  排除   = 硬门槛 / 未评级
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data" / "search-table.csv"
V2 = ROOT / "data" / "search-table-v2.csv"
EXP = ROOT / "data" / "search-table-expansion.csv"
OUT = ROOT / "data" / "search-table-v3.csv"
DOC = ROOT / "11-百分比分档与保底投递清单.md"

MAINLINE_BONUS = 2.0
CAP = 70.0
RANGE_RE = re.compile(r"(\d+(?:\.\d+)?)\s*[–\-~]\s*(\d+(?:\.\d+)?)")

TIERS = [
    ("S", 60, "保底"),
    ("S-", 55, "准保底"),
    ("A", 50, "稳妥"),
    ("B", 40, "主申"),
    ("C", 30, "可试"),
    ("D", 20, "偏低"),
    ("E", 10, "低"),
    ("F", 0, "极低"),
]

FUND_HIGH = ("guarantee", " Guaranteed", "保证", "全奖", "全额", "自动", "PGS", "HKPFS",
             "覆盖学费", "含学费", "fellowship", "Fellowship", "stipend", "月")
FUND_LOW = ("无保证", "不保证", "非保证", "no guarantee", "not guaranteed", "自费",
            "未公布", "limited", "不承诺", "无固定")
FUND_MID = ("竞争", "申请", "typically", "eligible", "may", "可争")


def mid(text: str) -> float | None:
    m = RANGE_RE.search(text or "")
    if m:
        lo, hi = float(m.group(1)), float(m.group(2))
        return (lo + hi) / 2 if lo <= hi else (hi + lo) / 2
    if "<" in (text or ""):
        return 4.0
    return None


def tier_of(p: float) -> str:
    for code, floor, name in TIERS:
        if p >= floor:
            return f"{code} {name}"
    return "F 极低"


def fund_class(text: str) -> str:
    """关键词启发式：区分「制度性覆盖」「竞争性/按年续」「基本自费」「未知」。

    注意：`非保证` 表示「按年续、非终身」，不等于「没钱」，因此归入「中」而不是「低」。
    """
    t = text or ""
    if not t:
        return "未知"
    if any(k in t for k in ("自费", "自筹", "无资助", "无具名", "无国际生全奖", "无 stipend", "no funding")):
        return "低"
    neg = any(k in t for k in ("非保证", "不保证", "无保证", "not guaranteed"))
    if not neg and ("guarantee" in t or "保证" in t or any(
            k in t for k in ("全奖", "全额", "自动", "PGS", "HKPFS", "fully funded", "full funding"))):
        return "高"
    if neg or any(k in t for k in ("竞争", "申请", "typically", "limited", "eligible", "按年", "可争",
                                   "assistantship", "TA/RA", "teaching assistant", "fellowship",
                                   "tuition", "学费减免", "助教", "助研",
                                   "国家助学金", "学业奖学金", "三助", "津贴", "scholarship", "stipend")):
        return "中"
    if "月" in t or "年" in t:
        return "中"
    return "未知"


def portfolio(p: float | None, fund: str, excluded: bool) -> str:
    if excluded:
        return "排除"
    if p is None:
        return "未评级"
    if p >= 60 and fund != "低":
        return "保底"
    if p >= 55 and fund != "低":
        return "准保底"
    if p >= 50 and fund == "高":
        return "高成功率"
    if p >= 40:
        return "主申"
    if p >= 30:
        return "冲刺"
    return "不建议"


def main() -> int:
    with BASE.open(encoding="utf-8-sig", newline="") as fh:
        base = list(csv.DictReader(fh))
    v2 = {}
    if V2.exists():
        with V2.open(encoding="utf-8-sig", newline="") as fh:
            v2 = {(r["region"], r["university"]): r for r in csv.DictReader(fh)}
    exp: list[dict[str, str]] = []
    if EXP.exists():
        with EXP.open(encoding="utf-8-sig", newline="") as fh:
            exp = list(csv.DictReader(fh))

    out: list[dict[str, str]] = []

    def push(region: str, sp: str, univ: str, prog: str, deadline: str, eng: str, gre: str,
             outr: str, itv: str, sup: str, fund: str, mat: str, floor: str, raw: str,
             risk: str, src: str, where: str, status: str | None = None) -> None:
        # 状态（排除/未评级）以 v1 原判定为准；百分比以 v2 区间为基线
        status = status if status is not None else raw
        excluded = "排除" in (status or "")
        unrated = "未评级" in (status or "") or "UNKNOWN" in (status or "")
        p = None if (excluded or unrated) else mid(raw)
        if p is not None:
            p = min(CAP, p + MAINLINE_BONUS)
            p = float(int(p + 0.5))  # 与展示的整数百分比保持一致，避免「显示 40% 却判 30–39 档」
        d = fund_class(fund)
        out.append(
            {
                "region": region,
                "state_province": sp,
                "university": univ,
                "program": prog,
                "admit_pct": "—" if p is None else f"{p:.0f}%",
                "tier": "X 排除" if excluded else ("未评级" if p is None else tier_of(p)),
                "fund_confidence": d,
                "portfolio": portfolio(p, d, excluded),
                "deadline_2027fall": deadline,
                "english_waiver": eng,
                "gre": gre,
                "supervisor_acceptance": sup,
                "funding": fund,
                "academic_floor": floor,
                "key_risk": risk,
                "sources": src,
                "where": where,
            }
        )

    for r in base:
        key = (r["region"], r["university"])
        v2r = v2.get(key, {}).get("range_v2") or ""
        raw = v2r if v2r and v2r != "—" else r["match_rate"]
        push(r["region"], r["state_province"], r["university"], r["program"],
             r["deadline_2027fall"], r["english_waiver"], r["gre"], r["outreach"],
             r["interview"], r["supervisor_acceptance"], r["funding"],
             r["other_materials"], r["academic_floor"], raw, r["key_risk"],
             r["sources"], "第一批（01–07l）", status=r["match_rate"])

    for r in exp:
        push(r["region"], r["state_province"], r["university"], r["program"],
             r["deadline_2027fall"], r["english_waiver"], r["gre"], r["outreach"],
             r["interview"], r["supervisor_acceptance"], r["funding"],
             r["other_materials"], r["academic_floor"], r["match_rate"], r["key_risk"],
             r["sources"], "第二批（10a–10f）")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)

    tiers = Counter(r["tier"] for r in out)
    port = Counter(r["portfolio"] for r in out)
    print(f"{len(out)} 行（第一批 {len(base)} + 扩区 {len(exp)}）→ {OUT}")
    for r in out:
        pass
    order = ["S 保底", "S- 准保底", "A 稳妥", "B 主申", "C 可试", "D 偏低", "E 低", "F 极低",
             "X 排除", "未评级"]
    print("分档：" + ", ".join(f"{k}={tiers.get(k,0)}" for k in order if tiers.get(k)))
    print("组合：" + ", ".join(f"{k}={v}" for k, v in port.most_common()))

    # ---------- 生成文档片段 ----------
    by_region: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in out:
        by_region[r["region"]].append(r)

    def pct(r: dict[str, str]) -> float:
        try:
            return float(r["admit_pct"].rstrip("%"))
        except ValueError:
            return -1.0

    tier_matrix = ["| 区域 | " + " | ".join(["S ≥60", "S- 55–59", "A 50–54", "B 40–49", "C 30–39",
                                              "D 20–29", "E 10–19", "F <10", "排除/未评级"]) + " | 行数 |",
                   "|---" * 10 + "|"]
    for region in sorted(by_region):
        sub = by_region[region]
        c = Counter(r["tier"] for r in sub)
        cells = [str(c.get(f"{code} {name}", 0) or "") for code, _, name in TIERS]
        cells.append(str(c.get("X 排除", 0) + c.get("未评级", 0) or ""))
        tier_matrix.append(f"| {region} | " + " | ".join(cells) + f" | {len(sub)} |")

    def table(rows: list[dict[str, str]]) -> list[str]:
        head = ["| 区域 | 州/省 | 学校 | 项目 | 录取概率 | 档位 | 资助确定性 | 资助要点 | 截止 |",
                "|---|---|---|---|---|---|---|---|---|"]
        body = []
        for r in rows:
            body.append(
                f"| {r['region']} | {r['state_province']} | {r['university'][:30]} | "
                f"{r['program'][:26]} | **{r['admit_pct']}** | {r['tier']} | {r['fund_confidence']} | "
                f"{r['funding'][:40].replace('|','/')} | {r['deadline_2027fall'][:22].replace('|','/')} |"
            )
        return head + body

    safety = sorted([r for r in out if r["portfolio"] in {"保底", "准保底", "高成功率"}],
                    key=lambda r: -pct(r))
    mainline = sorted([r for r in out if r["portfolio"] == "主申"], key=lambda r: -pct(r))
    reach = sorted([r for r in out if r["portfolio"] == "冲刺"], key=lambda r: -pct(r))

    full = ["| 区域 | 州/省 | 学校 | 录取概率 | 档位 | 资助 | 组合建议 | 关键风险 |",
            "|---|---|---|---|---|---|---|---|"]
    for r in sorted(out, key=lambda x: (-pct(x), x["region"], x["university"])):
        full.append(
            f"| {r['region']} | {r['state_province']} | {r['university'][:28]} | {r['admit_pct']} | "
            f"{r['tier']} | {r['fund_confidence']} | {r['portfolio']} | "
            f"{r['key_risk'][:22].replace('|','/')} |"
        )

    if DOC.exists():
        text = DOC.read_text(encoding="utf-8")
        blocks = {
            "TIER_MATRIX": "\n".join(tier_matrix),
            "COUNTS": (
                f"全表 **{len(out)} 行**（第一批 {len(base)} + 扩区 {len(exp)}）。"
                f"分档：S 保底 {tiers.get('S 保底',0)} / S- 准保底 {tiers.get('S- 准保底',0)} / "
                f"A 稳妥 {tiers.get('A 稳妥',0)} / B 主申 {tiers.get('B 主申',0)} / "
                f"C 可试 {tiers.get('C 可试',0)} / D 偏低 {tiers.get('D 偏低',0)} / "
                f"E 低 {tiers.get('E 低',0)} / F 极低 {tiers.get('F 极低',0)} / "
                f"排除 {tiers.get('X 排除',0)} / 未评级 {tiers.get('未评级',0)}。"
                f"组合建议：保底 {port.get('保底',0)} + 准保底 {port.get('准保底',0)} + "
                f"高成功率 {port.get('高成功率',0)} = "
                f"**{port.get('保底',0) + port.get('准保底',0) + port.get('高成功率',0)} 个可直接进投递清单的选项**。"
            ),
            "SAFETY": "\n".join(table(safety)),
            "MAINLINE": "\n".join(table(mainline)),
            "REACH": "\n".join(table(reach)),
            "FULL": "\n".join(full),
            "EXP_N": str(len(exp)),
        }
        for key, body in blocks.items():
            text = re.sub(
                rf"(<!-- AUTO:{key} -->)(?:.|\n)*?(<!-- /AUTO:{key} -->)",
                lambda m, b=body, k=key: f"<!-- AUTO:{k} -->\n{b}\n<!-- /AUTO:{k} -->",
                text,
            )
        DOC.write_text(text, encoding="utf-8")
        print("已回填 11-百分比分档与保底投递清单.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
