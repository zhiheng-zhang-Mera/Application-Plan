#!/usr/bin/env python3
"""v2 复评：在 v1 检索表基础上，加入「2 篇 arXiv 预印本 + 公开项目池 + 院校背景」重算全部 258 行。

设计原则
--------
1. **硬门槛不动**：GRE 必须、英语必须新考、无招生入口、论文条款写入报考条件 —— 不会因为多了预印本
   而消失，仍保持 `排除`；信息缺失的行仍保持 `未评级`。
2. **区分「短板类型」**：预印本与项目只能对冲「无论文 / 无研究证据」，**不能**修复「硕士成绩 67.5 或
   硕士未授予」这类学位等级门槛。学术门槛判 `不达标` 的行，加成 ×0.4。
3. **选择性折减**：基线越低（低 / 极低），说明约束是「够不够强」而非「有没有产出」，边际作用更小。
4. **精度纪律**：输出「平移后的区间」而不是单点；档位按区间中点判定，中点封顶 54%（无一行具备
   「已核实 2027 名额 + warm lead」，故 v2 不产生「高」）。

输出：data/search-table-v2.csv，并回填 09-成功率复评.md 中的 <!-- AUTO:* --> 段。
"""
from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "search-table.csv"
OUT_CSV = ROOT / "data" / "search-table-v2.csv"
DOC = ROOT / "09-成功率复评.md"

BANDS = ["高", "中高", "中", "低", "极低", "排除", "未评级"]
BAND_MID = {"高": 62.0, "中高": 45.0, "中": 27.5, "低": 14.0, "极低": 4.0}
MID_CAP = 54.0
HI_CAP = 70.0  # 区间上沿不硬截断，避免把不同学校压成同一个「60%」

# (A 预印本, B 项目池, C 院校背景)
UPLIFT = {
    "美国": (6, 2, 1),
    "中国香港": (5, 2, 2),
    "中国大陆-合办与港校校区": (5, 2, 2),
    "新加坡": (5, 2, 2),
    "加拿大": (4, 3, 1),
    "英国": (3, 3, 1),
    "中国大陆-本地院校": (3, 3, 3),
}
SEL = {"中高": 1.0, "中": 0.85, "低": 0.55, "极低": 0.35}
DRIVER = {
    "美国": "委员会制、论文权重最高",
    "中国香港": "委员会制 + 论文权重高",
    "中国大陆-合办与港校校区": "委员会制 + 港式评审口径",
    "新加坡": "委员会制 + 论文权重高",
    "加拿大": "导师主导，看可做性与预印本进度",
    "英国": "导师主导，看 fit 与 proposal",
    "中国大陆-本地院校": "申请-考核制，院校层次与论文都计分",
}
RANGE_RE = re.compile(r"(\d+(?:\.\d+)?)\s*[–\-~]\s*(\d+(?:\.\d+)?)")


def band_of(text: str) -> str:
    head = re.split(r"[（(]", text)[0].strip()
    for key in ("未评级", "排除", "极低", "中高", "高", "中", "低"):
        if head.startswith(key):
            return key
    return "未评级"


def range_of(text: str) -> tuple[float, float] | None:
    m = RANGE_RE.search(text)
    if not m:
        return None
    lo, hi = float(m.group(1)), float(m.group(2))
    return (lo, hi) if lo <= hi else (hi, lo)


def base_range(text: str) -> tuple[float, float]:
    r = range_of(text)
    if r:
        return r
    if "<" in text:
        return (1.0, 7.0)
    mid = BAND_MID.get(band_of(text), 27.5)
    return (mid - 6, mid + 6)


def band_from(mid: float) -> str:
    if mid >= 55:
        return "高"
    if mid >= 35:
        return "中高"
    if mid >= 20:
        return "中"
    if mid >= 8:
        return "低"
    return "极低"


def r5(x: float) -> int:
    return int(round(x / 5.0) * 5)


def floor_factor(text: str) -> tuple[float, str]:
    if "不达标" in text:
        return 0.4, "学位等级门槛未变，仅部分对冲"
    if "边缘" in text:
        return 1.0, "门槛边缘，可被材料对冲"
    if "UNKNOWN" in text or "未知" in text:
        return 0.85, "门槛未核实，打折计入"
    return 1.0, "门槛达标，材料直接生效"


def main() -> int:
    with SRC.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))

    out: list[dict[str, str]] = []
    moved: list[tuple[str, str, str, str, str]] = []
    for r in rows:
        region, b1 = r["region"], band_of(r["match_rate"])
        a, b, c = UPLIFT.get(region, (4, 2, 2))
        fac, fnote = floor_factor(r["academic_floor"])
        uplift = (a + b + c) * SEL.get(b1, 0.85) * fac

        if b1 in {"排除", "未评级"}:
            b2, rng, delta, uplift = b1, "—", "—", 0.0
        else:
            lo, hi = base_range(r["match_rate"])
            nlo, nhi = lo + uplift, hi + uplift
            mid = min(MID_CAP, (nlo + nhi) / 2)
            b2 = band_from(mid)
            rng = f"{r5(max(0, nlo))}–{r5(min(HI_CAP, nhi))}%"
            delta = "↑" if BANDS.index(b2) < BANDS.index(b1) else ("=" if b2 == b1 else "↓")
            if delta == "↑":
                moved.append((region, r["university"], b1, b2, rng))

        out.append(
            {
                "region": region,
                "state_province": r["state_province"],
                "university": r["university"],
                "program": r["program"],
                "band_v1": b1,
                "match_v1": r["match_rate"],
                "band_v2": b2,
                "range_v2": rng,
                "delta": delta,
                "uplift_pp": f"{uplift:.1f}",
                "driver": f"{DRIVER.get(region, '')}；{fnote}",
                "deadline_2027fall": r["deadline_2027fall"],
                "funding": r["funding"],
                "academic_floor": r["academic_floor"],
                "key_risk": r["key_risk"],
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
        writer.writeheader()
        writer.writerows(out)

    def mid_of_range(text: str) -> float:
        r = range_of(text)
        return (r[0] + r[1]) / 2 if r else 0.0

    c1 = Counter(x["band_v1"] for x in out)
    c2 = Counter(x["band_v2"] for x in out)
    core = [x for x in out if mid_of_range(x["range_v2"]) >= 45]
    edge = [x for x in out if 35 <= mid_of_range(x["range_v2"]) < 45]

    print(f"{len(out)} 行 → {OUT_CSV}")
    print("v1: " + ", ".join(f"{k}={c1.get(k,0)}" for k in BANDS))
    print("v2: " + ", ".join(f"{k}={c2.get(k,0)}" for k in BANDS))
    print(f"升级 {len(moved)} 行；核心池(≥45%) {len(core)} 行；边界带(35–44%) {len(edge)} 行")

    by_region: dict[str, list[dict[str, str]]] = defaultdict(list)
    for r in out:
        by_region[r["region"]].append(r)

    def fmt(cnt: Counter) -> str:
        parts = [f"{k} {cnt[k]}" for k in BANDS if cnt.get(k)]
        return " / ".join(parts) if parts else "—"

    summary = [
        "| 区域 | v1 档位分布 | v2 档位分布 | v2 ≥45%（核心池） | 行数 |",
        "|---|---|---|---|---|",
    ]
    for region in sorted(by_region):
        sub = by_region[region]
        n_core = len([x for x in sub if mid_of_range(x["range_v2"]) >= 45])
        summary.append(
            f"| {region} | {fmt(Counter(x['band_v1'] for x in sub))} | "
            f"{fmt(Counter(x['band_v2'] for x in sub))} | {n_core} | {len(sub)} |"
        )
    summary.append(f"| **合计** | {fmt(c1)} | {fmt(c2)} | **{len(core)}** | {len(out)} |")

    up_md = ["| 区域 | 学校 | v1 → v2 | v2 区间 |", "|---|---|---|---|"]
    for region, univ, b1, b2, rng in sorted(moved, key=lambda x: (x[0], x[1])):
        up_md.append(f"| {region} | {univ} | {b1} → **{b2}** | {rng} |")

    hi2 = [x for x in out if x["band_v2"] in {"高", "中高"}]
    pool = [
        "| 区域 | 州/省 | 学校 | v1 | v2 区间 | 门槛 | 关键风险 |",
        "|---|---|---|---|---|---|---|",
    ]
    for x in sorted(hi2, key=lambda x: (-mid_of_range(x["range_v2"]), x["region"], x["university"])):
        pool.append(
            f"| {x['region']} | {x['state_province']} | {x['university'][:34]} | {x['band_v1']} | "
            f"{x['range_v2']} | {x['academic_floor'][:14]} | {x['key_risk'][:24].replace('|', '/')} |"
        )

    full = [
        "| 区域 | 州/省 | 学校 | v1 | v2 区间 | Δ | 调分 | 门槛 | 驱动 |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for x in sorted(out, key=lambda x: (x["region"], x["state_province"], x["university"])):
        full.append(
            f"| {x['region']} | {x['state_province']} | {x['university'][:30]} | {x['band_v1']} | "
            f"{x['range_v2']} | {x['delta']} | {x['uplift_pp']} | {x['academic_floor'][:10]} | "
            f"{x['driver'][:32].replace('|', '/')} |"
        )

    if DOC.exists():
        text = DOC.read_text(encoding="utf-8")
        blocks = {
            "SUMMARY": "\n".join(summary),
            "UPGRADED": "\n".join(up_md),
            "POOL": "\n".join(pool),
            "FULL": "\n".join(full),
            "COUNTS": (
                f"v1：高 {c1.get('高',0)} / 中高 {c1.get('中高',0)} / 中 {c1.get('中',0)} / "
                f"低 {c1.get('低',0)} / 极低 {c1.get('极低',0)} / 排除 {c1.get('排除',0)} / "
                f"未评级 {c1.get('未评级',0)}。"
                f"**v2：高 {c2.get('高',0)} / 中高 {c2.get('中高',0)} / 中 {c2.get('中',0)} / "
                f"低 {c2.get('低',0)} / 极低 {c2.get('极低',0)} / 排除 {c2.get('排除',0)} / "
                f"未评级 {c2.get('未评级',0)}**。"
                f"共 **{len(moved)} 行升级**、0 行降级；**{c2.get('低',0) + c2.get('极低',0)} 行仍是低/极低**"
                f"（材料升级不改它们的现实性）。"
            ),
            "BOUNDARY": (
                f"按 v2 区间中点分层：**≥45%（核心池）{len(core)} 行**；"
                f"**35–44%（中/中高边界带）{len(edge)} 行**；其余 {len(out) - len(core) - len(edge)} 行"
                f"（含排除 {c2.get('排除',0)}、未评级 {c2.get('未评级',0)}）。"
                f"边界带的行按档位算「中高」，实质仍偏中——35% 是人为阈值，±5pp 内不应视为质变。"
            ),
            "MOVED_N": str(len(moved)),
            "POOL_N": str(len(hi2)),
        }
        for key, body in blocks.items():
            text = re.sub(
                rf"(<!-- AUTO:{key} -->)(?:.|\n)*?(<!-- /AUTO:{key} -->)",
                lambda m, b=body, k=key: f"<!-- AUTO:{k} -->\n{b}\n<!-- /AUTO:{k} -->",
                text,
            )
        DOC.write_text(text, encoding="utf-8")
        print("已回填 09-成功率复评.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())

