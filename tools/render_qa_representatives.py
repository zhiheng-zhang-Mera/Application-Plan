from __future__ import annotations

import json
from pathlib import Path, PurePosixPath

import pypdfium2 as pdfium
from PIL import Image, ImageDraw
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "tmp" / "pdfs" / "compile-manifest.json"
OUTPUT = ROOT / "tmp" / "pdfs" / "rendered"
REPRESENTATIVES = {
    "uts_jie_lu": "Applications/14_University of Technology Sydney/Jie Lu/",
    "curtin_aneesh_krishna": "Applications/15_Curtin University/Aneesh Krishna/",
    "ntu_bo_an": "Applications/16_Nanyang Technological University/Bo An/",
}


def render_pdf(pdf_path: Path, output_path: Path) -> dict[str, object]:
    document = pdfium.PdfDocument(str(pdf_path))
    pages: list[Image.Image] = []
    for page in document:
        image = page.render(scale=1.65).to_pil().convert("RGB")
        target_width = 1000
        target_height = round(image.height * target_width / image.width)
        pages.append(image.resize((target_width, target_height), Image.Resampling.LANCZOS))
    gap = 24
    label_height = 52
    canvas = Image.new(
        "RGB",
        (1000, label_height + sum(p.height for p in pages) + gap * max(0, len(pages) - 1)),
        "#d9dee3",
    )
    draw = ImageDraw.Draw(canvas)
    draw.text((18, 16), pdf_path.name, fill="#173b57")
    top = label_height
    for page in pages:
        canvas.paste(page, (0, top))
        top += page.height + gap
    canvas.save(output_path, optimize=True)

    reader = PdfReader(str(pdf_path))
    extracted = "\n".join((page.extract_text() or "") for page in reader.pages)
    return {
        "pages": len(reader.pages),
        "text_characters": len(extracted),
        "media_boxes": [
            [float(page.mediabox.width), float(page.mediabox.height)] for page in reader.pages
        ],
        "render": str(output_path),
    }


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    summary: dict[str, object] = {}
    selected_count = 0
    for label, prefix in REPRESENTATIVES.items():
        selected = [r for r in data["results"] if r["source"].startswith(prefix)]
        if len(selected) != 8:
            raise SystemExit(f"Expected 8 representative documents for {label}, found {len(selected)}")
        selected_count += len(selected)
        for result in sorted(selected, key=lambda r: r["source"]):
            source_name = PurePosixPath(result["source"]).stem
            pdf_path = Path(result["pdf"])
            output_path = OUTPUT / f"{label}__{source_name}.png"
            summary[result["source"]] = render_pdf(pdf_path, output_path)
    summary_path = OUTPUT / "render-summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"RENDERED={selected_count} SUMMARY={summary_path}")
    for source, evidence in summary.items():
        print(
            f"{source}: pages={evidence['pages']} text_characters={evidence['text_characters']} "
            f"media_boxes={evidence['media_boxes']}"
        )


if __name__ == "__main__":
    main()
