from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

from build_application_packages import SCHOOLS


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Applications"
REQUIRED = {
    "00_README.md",
    "01_Academic_CV.tex",
    "02_Research_CV.tex",
    "03_Statement_of_Purpose.tex",
    "04_Research_Statement.tex",
    "05_Research_Proposal.tex",
    "06_Quant_Ultra_Research_Summary.tex",
    "07_Privacy_Lens_Research_Summary.tex",
    "08_Contact_Email.md",
    "09_Application_Checklist.md",
    "10_Fact_Check.md",
    "11_Writing_Sample_Cover_Note.tex",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def main() -> None:
    expected_packages = sum(len(s["faculty"]) for s in SCHOOLS)
    package_dirs = [p for p in OUT.glob("*/*") if p.is_dir() and p.name != "Attachments"]
    if len(package_dirs) != expected_packages:
        fail(f"expected {expected_packages} package folders, found {len(package_dirs)}")

    tex_count = 0
    md_count = 1  # root README
    for package in package_dirs:
        names = {p.name for p in package.iterdir() if p.is_file()}
        missing = REQUIRED - names
        if missing:
            fail(f"{package}: missing {sorted(missing)}")
        attachments = package / "Attachments"
        for attachment in ["Transcript-ZhihengZhang.pdf", "Master-WAM.png"]:
            path = attachments / attachment
            if not path.exists() or path.stat().st_size == 0:
                fail(f"{package}: missing or empty attachment {attachment}")
        for tex in package.glob("*.tex"):
            text = tex.read_text(encoding="utf-8")
            if "\\begin{document}" not in text or "\\end{document}" not in text:
                fail(f"{tex}: incomplete LaTeX document")
            if text.count("{") != text.count("}"):
                fail(f"{tex}: unbalanced braces")
            tex_count += 1
        for md in package.glob("*.md"):
            if not md.read_text(encoding="utf-8").strip():
                fail(f"{md}: empty Markdown")
            md_count += 1

        sop = (package / "03_Statement_of_Purpose.tex").read_text(encoding="utf-8")
        sop_words = len(re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", sop))
        if sop_words < 650:
            fail(f"{package}: SOP too short ({sop_words} words including preamble)")
        email = (package / "08_Contact_Email.md").read_text(encoding="utf-8")
        if "Dear Professor" not in email or "Quant-Ultra" not in email:
            fail(f"{package}: contact email lacks required personalization skeleton")

    tracked_pdfs = list(OUT.rglob("*.pdf"))
    unexpected = [p for p in tracked_pdfs if p.name != "Transcript-ZhihengZhang.pdf"]
    if unexpected:
        fail(f"unexpected authored PDFs found: {unexpected[:3]}")

    print(f"PASS: {expected_packages} supervisor packages")
    print(f"PASS: {tex_count} complete TeX sources")
    print(f"PASS: {md_count} non-empty Markdown files")
    print(f"PASS: {len(tracked_pdfs)} PDFs are copies of the supplied official transcript only")


if __name__ == "__main__":
    main()
