#!/usr/bin/env python3
"""第二批扩区（澳大利亚 / 新西兰 / 日本 / 韩国·澳门 / 欧洲两组）的合并脚本。

幂等设计（重要）：代理分批落盘，_raw 可能中途被重写。规则是
  · 若 `_raw/<stem>.md` 存在且**行数不少于**现有正式文档，则用 raw 重建正式文档（raw 更新更全）；
  · 否则保留现有正式文档不动；
  · CSV 一律从正式文档（10a–10f）解析，而不是 _raw；
  · 只有全部 _raw 文件都被消费后才清理目录。
"""
from __future__ import annotations

import csv
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_csv import clean, split_row, EXPECTED  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "_raw"
OUT_CSV = ROOT / "data" / "search-table-expansion.csv"

DOCS = [
    ("au-australia", "10a-澳大利亚.md", "澳大利亚",
     "# 10a · 澳大利亚：2027 入学 CS PhD 完整表（扩区一批）",
     ["覆盖墨尔本 / UNSW / 悉尼 / ANU / Monash / UQ / 阿德莱德 / UTS / RMIT / UWA / Macquarie / Deakin。",
      "澳洲的结构是**录取与资助分离**：拿到 admission 相对容易，RTP stipend 才是竞争点。"]),
    ("nz-newzealand", "10b-新西兰.md", "新西兰",
     "# 10b · 新西兰：2027 入学 CS PhD 完整表（扩区一批）",
     ["覆盖 Auckland / Canterbury / VUW / Otago / Waikato / AUT。",
      "新西兰是全球罕见的「**国际博士生按本地学费收费**」国家，是本轮最现实的「可负担保底」。"]),
    ("kr-mo", "10c-韩国与澳门.md", "韩国与澳门",
     "# 10c · 韩国与澳门：2027 入学 CS PhD 完整表（扩区一批）",
     ["A 组韩国（KAIST / POSTECH / SNU / Yonsei / Korea / UNIST / GIST），B 组澳门（UM / MUST / CityU Macau / USJ）。",
      "两组都是**教授内诺制**，且资助覆盖度高；澳门已有在途申请。"]),
    ("jp-japan", "10d-日本.md", "日本",
     "# 10d · 日本：2027 入学 CS PhD 完整表（扩区一批）",
     ["覆盖东大 / 京大 / 阪大 / 东北 / 科学大 / 九大 / 北大 / NAIST / JAIST。",
      "日本的门槛是**教授内诺 + 入学考试**；2027 年 4 月窗口多数已关，主战场是 **2027 年 10 月**；MEXT 是主要资助。"]),
    ("eu-dach-nl", "10e-欧洲德语区与荷兰.md", "欧洲（德荷瑞奥）",
     "# 10e · 欧洲（德国 / 荷兰 / 瑞士 / 奥地利）：2027 入学 CS PhD 完整表（扩区一批）",
     ["覆盖 TUM / Saarland+MPI-SWS / KIT / RWTH / Freiburg / TU Darmstadt / TU Delft / TU/e / UvA / Twente / ETH / EPFL / TU Wien。",
      "几乎全是**带薪雇员岗位**：不交学费、拿工资、PI 直接招人——资金最好，门槛是「已获硕士 + 岗位存在性」。"]),
    ("eu-nordics-ie-be", "10f-北欧与爱尔兰比利时.md", "欧洲（北欧与爱尔兰比利时）",
     "# 10f · 欧洲（北欧 / 爱尔兰 / 比利时）：2027 入学 CS PhD 完整表（扩区一批）",
     ["覆盖 KTH / Chalmers / Linköping / DTU / UCPH / NTNU / UiO / Aalto / Helsinki / TCD / UCD / KU Leuven。",
      "北欧多为**带薪岗位**（无固定截止，要盯 vacancy）；爱尔兰是「英语可豁免 + 硕士可后补」的半保底路线。"]),
]

HEADER = ("| 州/省 | 学校 | 项目 | 2027F截止 | 英语豁免 | GRE | 套磁 | 面试 | 导师接收 | 资助 | "
          "其他材料 | 学术门槛 | 匹配率 | 风险 | 来源 | 核验日 |")
SEP = "|" + "---|" * EXPECTED
NOTE = ("> 字段规范见 [`00-申请人材料基线与门禁.md`](00-申请人材料基线与门禁.md)；本文件的「匹配率」列是"
        "**百分比区间**，档位折算见 [`11-百分比分档与保底投递清单.md`](11-百分比分档与保底投递清单.md)。")


def count_rows(path: Path) -> int:
    if not path.exists():
        return 0
    n = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = split_row(line)
        if cells is not None and len(cells) == EXPECTED and "学校" not in cells[1] \
                and cells[0] not in {"州/省", "城市/省", "省/州"} and not re.fullmatch(r"[-: ]+", cells[0] or "-"):
            n += 1
    return n


def main() -> int:
    for stem, doc_name, _region, title, intro in DOCS:
        doc, raw = ROOT / doc_name, RAW / f"{stem}.md"
        if not raw.exists():
            print(f"{doc_name}: 无新 raw，保留现有 {count_rows(doc)} 行")
            continue
        n_raw, n_doc = count_rows(raw), count_rows(doc)
        if n_raw < n_doc:
            print(f"{doc_name}: raw 行数 {n_raw} < 现有 {n_doc}，保留现有")
            continue
        lines = raw.read_text(encoding="utf-8").splitlines()
        if lines and lines[0].startswith("# "):
            lines = lines[1:]
        block = [title, ""] + [f"> {x}" for x in intro] + ["", NOTE, ""]
        doc.write_text("\n".join(block + lines) + "\n", encoding="utf-8")
        print(f"{doc_name}: 由 raw 重建，{n_raw} 行")

    rows: list[dict[str, str]] = []
    for _stem, doc_name, region, _title, _intro in DOCS:
        doc = ROOT / doc_name
        if not doc.exists():
            print(f"缺少 {doc_name}")
            continue
        count = 0
        header_seen = False
        for line in doc.read_text(encoding="utf-8").splitlines():
            cells = split_row(line)
            if cells is None or len(cells) != EXPECTED:
                continue
            if "学校" in cells[1] or cells[0] in {"州/省", "城市/省", "省/州"}:
                header_seen = True
                continue
            if re.fullmatch(r"[-: ]+", cells[0] or "-"):
                continue
            v = [clean(c) for c in cells]
            rows.append({
                "region": region, "region_file": doc_name, "state_province": v[0],
                "university": v[1], "program": v[2], "deadline_2027fall": v[3],
                "english_waiver": v[4], "gre": v[5], "outreach": v[6], "interview": v[7],
                "supervisor_acceptance": v[8], "funding": v[9], "other_materials": v[10],
                "academic_floor": v[11], "match_rate": v[12], "key_risk": v[13],
                "sources": v[14], "verified_date": v[15],
            })
            count += 1
        _ = header_seen
        print(f"{doc_name}: {count} 行")

    if not rows:
        print("没有可合并的扩区数据")
        return 1
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"\n合计 {len(rows)} 行 → {OUT_CSV}")

    pending = [p for p in RAW.glob("*.md")] if RAW.exists() else []
    consumed = {f"{s}.md" for s, *_ in DOCS}
    leftover = [p for p in pending if p.name not in consumed]
    if RAW.exists() and not leftover:
        shutil.rmtree(RAW, ignore_errors=True)
        print("_raw 已清理")
    return 0


if __name__ == "__main__":
    sys.exit(main())
