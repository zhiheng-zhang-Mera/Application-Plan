#!/usr/bin/env python3
"""Rebuild three English application PDFs from adjacent Markdown sources.

Requires Python 3 and reportlab. No network access or project tests are used.
Run from any directory: python3 build-pdfs.py
"""

from pathlib import Path
import os
import reportlab
from reportlab import rl_config
import re
from html import escape

from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, KeepTogether, PageBreak

FONT_DIR = Path(os.environ.get("SYRACUSE_FONT_DIR", "/usr/share/fonts/truetype/dejavu"))
FONT_FILES = {
    "BodySerif": FONT_DIR / "DejaVuSerif.ttf",
    "BodySerifBold": FONT_DIR / "DejaVuSerif-Bold.ttf",
    "HeadSans": FONT_DIR / "DejaVuSans.ttf",
    "HeadSansBold": FONT_DIR / "DejaVuSans-Bold.ttf",
}
if not all(path.is_file() for path in FONT_FILES.values()):
    bundled = Path(reportlab.__file__).resolve().parent / "fonts"
    FONT_FILES = {
        "BodySerif": bundled / "Vera.ttf",
        "BodySerifBold": bundled / "VeraBd.ttf",
        "HeadSans": bundled / "Vera.ttf",
        "HeadSansBold": bundled / "VeraBd.ttf",
    }
for name, path in FONT_FILES.items():
    pdfmetrics.registerFont(TTFont(name, str(path)))
pdfmetrics.registerFontFamily("BodySerif", normal="BodySerif", bold="BodySerifBold")
pdfmetrics.registerFontFamily("HeadSans", normal="HeadSans", bold="HeadSansBold")
rl_config.invariant = 1

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "upload"
OUTPUT = ROOT / "output" / "pdf"
FILES = {
    "SOP": "Zhiheng-Zhang-Syracuse-CISE-SOP.pdf",
    "CV": "Zhiheng-Zhang-Syracuse-CISE-CV.pdf",
    "Research-Summary": "Zhiheng-Zhang-Syracuse-CISE-Research-Summary.pdf",
}

def inline(text):
    chunks = []
    cursor = 0
    for match in re.finditer(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", text):
        chunks.append(escape(text[cursor:match.start()]))
        chunks.append('<a href="{}" color="#243746">{}</a>'.format(
            escape(match.group(2), quote=True), escape(match.group(1))))
        cursor = match.end()
    chunks.append(escape(text[cursor:]))
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", "".join(chunks))

def style_set(kind):
    compact = kind in ("CV", "Research-Summary")
    body = ParagraphStyle(
        "Body", fontName="BodySerif", fontSize=9.6 if kind == "Research-Summary" else (10.2 if compact else 11.0),
        leading=12.4 if kind == "Research-Summary" else (13.0 if compact else 15.0), spaceAfter=6 if compact else 9,
        textColor=colors.HexColor("#202020"), alignment=TA_LEFT,
        allowWidows=0, allowOrphans=0)
    return {
        "body": body,
        "title": ParagraphStyle(
            "Title", parent=body, fontName="HeadSansBold",
            fontSize=19 if kind == "CV" else 16, leading=22,
            spaceAfter=10, keepWithNext=True),
        "h2": ParagraphStyle(
            "H2", parent=body, fontName="HeadSansBold",
            fontSize=10.4, leading=13, spaceBefore=9,
            spaceAfter=5, keepWithNext=True),
        "h3": ParagraphStyle(
            "H3", parent=body, fontName="BodySerifBold",
            fontSize=10.5, leading=13.2, spaceBefore=5,
            spaceAfter=3, keepWithNext=True),
        "bullet": ParagraphStyle(
            "Bullet", parent=body, leftIndent=10,
            firstLineIndent=-7, spaceAfter=4),
        "meta": ParagraphStyle(
            "Meta", parent=body, fontName="HeadSans",
            fontSize=8.7, leading=11.5, spaceAfter=5,
            textColor=colors.HexColor("#4b4b4b")),
    }

def footer(canvas, doc):
    canvas.saveState()
    width, _ = letter
    canvas.setStrokeColor(colors.HexColor("#cccccc"))
    canvas.setLineWidth(0.35)
    canvas.line(47, 35, width - 47, 35)
    canvas.setFont("HeadSans", 8)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.drawString(47, 23, "Zhiheng Zhang | Syracuse CISE Ph.D. | Fall 2027")
    canvas.drawRightString(width - 47, 23, str(doc.page))
    canvas.restoreState()

def build(kind, output_name):
    text = (SOURCE / f"{kind}.md").read_text(encoding="utf-8")
    styles = style_set(kind)
    story = []
    body_started = False
    for block in re.split(r"\n\s*\n", text.strip()):
        if block.startswith("# "):
            story.append(Paragraph(inline(block[2:]), styles["title"]))
        elif block.startswith("## "):
            body_started = True
            story.append(Paragraph(inline(block[3:]), styles["h2"]))
        elif block.startswith("### "):
            if kind == "CV" and block.startswith("### DS-Hns"):
                story.append(PageBreak())
            story.append(Paragraph(inline(block[4:]), styles["h3"]))
        elif block.startswith("- "):
            body_started = True
            for item in re.split(r"\n(?=- )", block):
                story.append(Paragraph(
                    "- " + inline(item[2:].replace("\n", " ")), styles["bullet"]))
        else:
            is_meta = not body_started and (" | " in block or block.startswith("Ph.D."))
            if not is_meta:
                body_started = True
            paragraph = Paragraph(
                inline(block.replace("\n", " ")),
                styles["meta"] if is_meta else styles["body"])
            if kind == "SOP" and not is_meta:
                story.append(KeepTogether([paragraph]))
            else:
                if kind == "CV" and block.startswith("["):
                    paragraph.keepWithNext = True
                story.append(paragraph)
    output = OUTPUT / output_name
    doc = SimpleDocTemplate(
        str(output), pagesize=letter, rightMargin=47, leftMargin=47,
        topMargin=43, bottomMargin=48,
        title=f"Zhiheng Zhang - Syracuse CISE - {kind}",
        author="Zhiheng Zhang", subject="Fall 2027 Ph.D. application")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(output.relative_to(ROOT))

if __name__ == "__main__":
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for kind, output_name in FILES.items():
        build(kind, output_name)
