from __future__ import annotations

import re
import subprocess
import sys
from difflib import SequenceMatcher
from pathlib import Path

from build_application_packages import (
    FACULTY_DIRECTION_ZH,
    OUTREACH_LEVEL_ZH,
    PROGRAM_LINKS,
    SCHOOL_GENERAL_MATERIALS,
    SCHOOLS,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Applications"
REQUIRED = {
    "README.md",
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
    tex_count = 0
    expected_school_names = {
        f"{school['order']}_{school['folder']}" for school in SCHOOLS
    }
    school_dirs = {path.name: path for path in OUT.iterdir() if path.is_dir()}
    if set(school_dirs) != expected_school_names:
        missing = sorted(expected_school_names - set(school_dirs))
        unexpected = sorted(set(school_dirs) - expected_school_names)
        fail(f"school folder mismatch; missing={missing}, unexpected={unexpected}")
    for name, school_dir in school_dirs.items():
        if not re.search(r"[\u4e00-\u9fff]", name) or not re.search(r"\([A-Za-z]", name):
            fail(f"school folder is not bilingual: {name}")
        school_readme = school_dir / "README.md"
        if not school_readme.exists() or not school_readme.read_text(encoding="utf-8").strip():
            fail(f"missing or empty school requirements README: {school_readme}")
        readme_text = school_readme.read_text(encoding="utf-8")
        school = next(item for item in SCHOOLS if f"{item['order']}_{item['folder']}" == name)
        links = PROGRAM_LINKS[school["school"]]
        expected_level = f"套磁分类：**{OUTREACH_LEVEL_ZH[school['school']]}**"
        if expected_level not in readme_text:
            fail(f"school README lacks explicit outreach classification: {school_readme}")
        for heading in ["## 官方链接", "## GRE 筛查", "## 学校级材料清单", "## 学校特定检查", "## 导师申请包", "## 提交边界"]:
            if heading not in readme_text:
                fail(f"school README lacks Chinese section {heading}: {school_readme}")
        for label, url in [("项目介绍页面", links["program"]), ("在线申请通道", links["apply"])]:
            if f"[{label}]({url})" not in readme_text:
                fail(f"school README lacks {label}: {school_readme}")
        expected_school_tex = (
            {"Departmental_General_CV.tex", "Research_Interest_Proposal.tex"}
            if school["school"] in SCHOOL_GENERAL_MATERIALS
            else set()
        )
        actual_school_tex = {path.name for path in school_dir.glob("*.tex")}
        if actual_school_tex != expected_school_tex:
            fail(
                f"school-level TeX mismatch for {school_readme}; "
                f"expected={sorted(expected_school_tex)}, actual={sorted(actual_school_tex)}"
            )
        if expected_school_tex:
            if "## 学院通用材料" not in readme_text:
                fail(f"school README lacks general-material section: {school_readme}")
            for filename in expected_school_tex:
                if f"[`{filename}`]({filename})" not in readme_text:
                    fail(f"school README lacks general-material link {filename}: {school_readme}")
            brief_name = "Research_Interest_Proposal_500_Words.md"
            brief = school_dir / brief_name
            if not brief.exists():
                fail(f"school-level 500-word proposal missing: {brief}")
            if f"[`{brief_name}`]({brief_name})" not in readme_text:
                fail(f"school README lacks general-material link {brief_name}: {school_readme}")
            brief_text = brief.read_text(encoding="utf-8")
            brief_words = len(re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", brief_text))
            if not 475 <= brief_words <= 525:
                fail(f"{brief}: expected approximately 500 English words, found {brief_words}")
            if re.search(r"[\u4e00-\u9fff]", brief_text):
                fail(f"{brief}: submission-ready proposal must remain English")
            markdown_layout = [
                r"(?m)^\s*#{1,6}\s+",
                r"(?m)^\s*[-*+]\s+",
                r"(?m)^\s*\d+[.)]\s+",
                r"(?m)^\s*>",
                r"\*\*|__|```|`[^`]+`|\[[^\]]+\]\([^)]+\)",
            ]
            if any(re.search(pattern, brief_text) for pattern in markdown_layout):
                fail(f"{brief}: concise RP must be plain essay prose without Markdown layout")
            editorial_markers = ["before submission", "submission note", "中文说明", "[confirm"]
            if any(marker in brief_text.lower() for marker in editorial_markers):
                fail(f"{brief}: contains internal editorial instructions")
            full_rp = (school_dir / "Research_Interest_Proposal.tex").read_text(encoding="utf-8")
            full_tokens = re.findall(r"[A-Za-z][A-Za-z'-]*", full_rp.lower())
            brief_tokens = re.findall(r"[A-Za-z][A-Za-z'-]*", brief_text.lower())
            similarity = SequenceMatcher(None, full_tokens, brief_tokens, autojunk=False).ratio()
            if similarity < 0.20:
                fail(f"{brief}: insufficiently aligned with full RP ({similarity:.3f})")
            if similarity >= 0.80:
                fail(f"{brief}: too close to full RP rather than a concise version ({similarity:.3f})")
            for term in SCHOOL_GENERAL_MATERIALS[school["school"]]["alignment_terms"]:
                if term.lower() not in full_rp.lower() or term.lower() not in brief_text.lower():
                    fail(f"{brief}: alignment term missing from one version: {term}")

            cv_text = (school_dir / "Departmental_General_CV.tex").read_text(encoding="utf-8")
            contact_texts = [cv_text, full_rp]
            for contact in ["nicholas_zhang2020@163.com", "(+86)15601654187"]:
                if any(contact not in text for text in contact_texts):
                    fail(f"{school_dir}: one or more school-level materials lack confirmed contact: {contact}")
            if any("[CONFIRM EMAIL]" in text or "[CONFIRM PHONE]" in text for text in contact_texts):
                fail(f"{school_dir}: school-level material still contains contact placeholders")
        for tex in school_dir.glob("*.tex"):
            text = tex.read_text(encoding="utf-8")
            if "\\begin{document}" not in text or "\\end{document}" not in text:
                fail(f"{tex}: incomplete LaTeX document")
            if text.count("{") != text.count("}"):
                fail(f"{tex}: unbalanced braces")
            tex_count += 1

    expected_packages = sum(len(s["faculty"]) for s in SCHOOLS)
    package_dirs = [p for p in OUT.glob("*/*") if p.is_dir() and p.name != "Attachments"]
    if len(package_dirs) != expected_packages:
        fail(f"expected {expected_packages} package folders, found {len(package_dirs)}")

    md_count = 1 + len(school_dirs) + len(SCHOOL_GENERAL_MATERIALS)
    for package in package_dirs:
        names = {p.name for p in package.iterdir() if p.is_file()}
        missing = REQUIRED - names
        if missing:
            fail(f"{package}: missing {sorted(missing)}")
        if "00_README.md" in names:
            fail(f"{package}: legacy 00_README.md still exists")
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
            md_text = md.read_text(encoding="utf-8")
            if not md_text.strip():
                fail(f"{md}: empty Markdown")
            if md.name != "08_Contact_Email.md" and not re.search(r"[\u4e00-\u9fff]", md_text):
                fail(f"{md}: non-email Markdown lacks Chinese content")
            md_count += 1

        supervisor_readme = (package / "README.md").read_text(encoding="utf-8")
        if "## 导师研究方向与申请切入点" not in supervisor_readme:
            fail(f"{package}: supervisor README lacks research-direction section")
        direction = FACULTY_DIRECTION_ZH.get(package.name)
        if not direction or direction not in supervisor_readme:
            fail(f"{package}: supervisor README lacks individualized Chinese direction")

        sop = (package / "03_Statement_of_Purpose.tex").read_text(encoding="utf-8")
        sop_words = len(re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", sop))
        if sop_words < 650:
            fail(f"{package}: SOP too short ({sop_words} words including preamble)")
        email = (package / "08_Contact_Email.md").read_text(encoding="utf-8")
        if "Dear Professor" not in email or "Quant-Ultra" not in email:
            fail(f"{package}: contact email lacks required personalization skeleton")
        if re.search(r"[\u4e00-\u9fff]", email):
            fail(f"{package}: contact email must remain English")

    for markdown in OUT.rglob("*.md"):
        if markdown.name in {"08_Contact_Email.md", "Research_Interest_Proposal_500_Words.md"}:
            continue
        if not re.search(r"[\u4e00-\u9fff]", markdown.read_text(encoding="utf-8")):
            fail(f"{markdown}: non-email Markdown lacks Chinese content")

    tracked_pdfs = list(OUT.rglob("*.pdf"))
    unexpected = [p for p in tracked_pdfs if p.name != "Transcript-ZhihengZhang.pdf"]
    if unexpected:
        fail(f"unexpected authored PDFs found: {unexpected[:3]}")

    print(f"PASS: {len(school_dirs)} priority-ordered bilingual school folders and requirements READMEs")
    print(f"PASS: {expected_packages} supervisor packages")
    print(f"PASS: {tex_count} complete TeX sources")
    print(f"PASS: {md_count} non-empty Markdown files")
    print(f"PASS: {len(tracked_pdfs)} PDFs are copies of the supplied official transcript only")


if __name__ == "__main__":
    main()
