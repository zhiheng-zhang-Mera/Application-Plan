#!/usr/bin/env python3
"""Build the current academic CV from CV.md, without network access.

Adapted from applications/syracuse/2027-fall/build-pdfs.py.
Requires Python 3 and reportlab. Run: python3 build-cv.py
Use --stdout-base64 to render in memory without writing a PDF to disk.
"""
from pathlib import Path
from io import BytesIO
from html import escape
import argparse
import base64
import re

import reportlab
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, KeepTogether, PageBreak

UPDATED = "31 October 2026"
OUTPUT_NAME = "Zhiheng-Zhang-Academic-CV.pdf"

def register_fonts():
    font_dir = Path("/usr/share/fonts/truetype/dejavu")
    files = {
        "BodySerif": font_dir / "DejaVuSerif.ttf",
        "BodySerifBold": font_dir / "DejaVuSerif-Bold.ttf",
        "HeadSans": font_dir / "DejaVuSans.ttf",
        "HeadSansBold": font_dir / "DejaVuSans-Bold.ttf",
    }
    if not all(path.is_file() for path in files.values()):
        bundled = Path(reportlab.__file__).resolve().parent / "fonts"
        files = {
            "BodySerif": bundled / "Vera.ttf",
            "BodySerifBold": bundled / "VeraBd.ttf",
            "HeadSans": bundled / "Vera.ttf",
            "HeadSansBold": bundled / "VeraBd.ttf",
        }
    for name, path in files.items():
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily("BodySerif", normal="BodySerif", bold="BodySerifBold")
    pdfmetrics.registerFontFamily("HeadSans", normal="HeadSans", bold="HeadSansBold")

def inline(value):
    chunks = []
    cursor = 0
    for match in re.finditer(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", value):
        chunks.append(escape(value[cursor:match.start()]))
        chunks.append('<a href="{}" color="#243746">{}</a>'.format(
            escape(match.group(2), quote=True), escape(match.group(1))))
        cursor = match.end()
    chunks.append(escape(value[cursor:]))
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", "".join(chunks))

def styles():
    body = ParagraphStyle(
        "Body", fontName="BodySerif", fontSize=10.2, leading=13.0,
        spaceAfter=6, textColor=colors.HexColor("#202020"), alignment=TA_LEFT,
        allowWidows=0, allowOrphans=0)
    return {
        "body": body,
        "title": ParagraphStyle(
            "Title", parent=body, fontName="HeadSansBold",
            fontSize=19, leading=22, spaceAfter=9, keepWithNext=True),
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
        "citation": ParagraphStyle(
            "Citation", parent=body, leftIndent=13, firstLineIndent=-13,
            spaceAfter=3, keepWithNext=True),
        "citation_note": ParagraphStyle(
            "CitationNote", parent=body, fontSize=9.4, leading=12,
            leftIndent=13, spaceAfter=7),
    }

def footer(canvas, doc):
    canvas.saveState()
    width, _ = letter
    canvas.setStrokeColor(colors.HexColor("#cccccc"))
    canvas.setLineWidth(0.35)
    canvas.line(47, 35, width - 47, 35)
    canvas.setFont("HeadSans", 8)
    canvas.setFillColor(colors.HexColor("#555555"))
    canvas.drawString(47, 23, f"Zhiheng Zhang | Academic CV | Updated {UPDATED}")
    canvas.drawRightString(width - 47, 23, str(doc.page))
    canvas.restoreState()

def render_pdf(markdown):
    register_fonts()
    rl_config.invariant = 1
    st = styles()
    story = []
    body_started = False
    for block in re.split(r"\n\s*\n", markdown.strip()):
        if block.startswith("# "):
            story.append(Paragraph(inline(block[2:]), st["title"]))
        elif block.startswith("## "):
            body_started = True
            story.append(Paragraph(inline(block[3:]), st["h2"]))
        elif block.startswith("### "):
            if block.startswith("### Privacy Lens"):
                story.append(PageBreak())
                story.append(Paragraph("Research and Systems Experience (continued)", st["h2"]))
            story.append(Paragraph(inline(block[4:]), st["h3"]))
        elif block.startswith("- "):
            body_started = True
            for item in re.split(r"\n(?=- )", block):
                story.append(Paragraph("- " + inline(item[2:].replace("\n", " ")), st["bullet"]))
        elif re.match(r"^\d+\.\s", block):
            body_started = True
            lines = block.splitlines()
            parts = [Paragraph(inline(lines[0]), st["citation"])]
            if len(lines) > 1:
                parts.append(Paragraph(inline(" ".join(line.strip() for line in lines[1:])), st["citation_note"]))
            story.append(KeepTogether(parts))
        else:
            is_meta = not body_started
            paragraph = Paragraph(inline(block.replace("\n", " ")), st["meta"] if is_meta else st["body"])
            if block.startswith("["):
                paragraph.keepWithNext = True
            story.append(paragraph)
    output = BytesIO()
    doc = SimpleDocTemplate(
        output, pagesize=letter, rightMargin=47, leftMargin=47,
        topMargin=43, bottomMargin=48,
        title="Zhiheng Zhang - Academic Curriculum Vitae",
        author="Zhiheng Zhang",
        subject="Fall 2027 PhD applications; updated 31 October 2026")
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    return output.getvalue()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stdout-base64", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    data = render_pdf((root / "CV.md").read_text(encoding="utf-8"))
    if args.stdout_base64:
        print(base64.b64encode(data).decode("ascii"))
    else:
        output = root / OUTPUT_NAME
        output.write_bytes(data)
        print(output)

if __name__ == "__main__":
    main()
