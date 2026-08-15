from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import shutil
import subprocess
import time
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEX_ROOT = Path(r"D:\PhD-Tools\TinyTeX")
DEFAULT_QA_ROOT = Path(r"D:\PhD-Tools")


@dataclass
class CompileResult:
    source: str
    key: str
    exit_code: int
    pdf: str
    pdf_bytes: int
    elapsed_seconds: float
    overfull_boxes: int
    underfull_boxes: int
    latex_warnings: int
    error_excerpt: str


def compile_one(source: Path, tex_root: Path, qa_root: Path) -> CompileResult:
    relative = source.relative_to(ROOT).as_posix()
    key = hashlib.sha256(relative.encode("utf-8")).hexdigest()[:16]
    input_dir = qa_root / "qa-input" / key
    output_dir = qa_root / "qa-output" / key
    input_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)
    staged = input_dir / "document.tex"
    shutil.copyfile(source, staged)

    pdflatex = tex_root / "bin" / "windows" / "pdflatex.exe"
    command = [
        str(pdflatex),
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-file-line-error",
        f"-output-directory={output_dir.as_posix()}",
        "document.tex",
    ]
    environment = os.environ.copy()
    environment["TEMP"] = str(qa_root / "tmp")
    environment["TMP"] = str(qa_root / "tmp")
    started = time.monotonic()
    combined_output = []
    exit_code = 0
    for _ in range(2):
        process = subprocess.run(
            command,
            cwd=input_dir,
            env=environment,
            text=True,
            encoding="utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        combined_output.append(process.stdout)
        exit_code = process.returncode
        if exit_code:
            break

    log_path = output_dir / "document.log"
    log_text = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else "\n".join(combined_output)
    pdf_path = output_dir / "document.pdf"
    errors = []
    if exit_code:
        errors.extend("\n".join(combined_output).splitlines()[-30:])
    return CompileResult(
        source=relative,
        key=key,
        exit_code=exit_code,
        pdf=str(pdf_path) if pdf_path.exists() else "",
        pdf_bytes=pdf_path.stat().st_size if pdf_path.exists() else 0,
        elapsed_seconds=round(time.monotonic() - started, 3),
        overfull_boxes=log_text.count("Overfull \\hbox") + log_text.count("Overfull \\vbox"),
        underfull_boxes=log_text.count("Underfull \\hbox") + log_text.count("Underfull \\vbox"),
        latex_warnings=log_text.count("LaTeX Warning:"),
        error_excerpt="\n".join(errors),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Compile every application TeX source from an ASCII-only D-drive staging area.")
    parser.add_argument("--tex-root", type=Path, default=DEFAULT_TEX_ROOT)
    parser.add_argument("--qa-root", type=Path, default=DEFAULT_QA_ROOT)
    parser.add_argument("--workers", type=int, default=min(8, os.cpu_count() or 1))
    args = parser.parse_args()

    tex_root = args.tex_root.resolve()
    qa_root = args.qa_root.resolve()
    if qa_root != DEFAULT_QA_ROOT.resolve():
        raise SystemExit(f"Refusing QA root outside {DEFAULT_QA_ROOT}")
    pdflatex = tex_root / "bin" / "windows" / "pdflatex.exe"
    if not pdflatex.exists():
        raise SystemExit(f"pdflatex not found: {pdflatex}")
    (qa_root / "tmp").mkdir(parents=True, exist_ok=True)

    sources = sorted((ROOT / "Applications").rglob("*.tex"))
    started = time.monotonic()
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda p: compile_one(p, tex_root, qa_root), sources))

    manifest_dir = ROOT / "tmp" / "pdfs"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "generated_at_epoch": int(time.time()),
        "tex_root": str(tex_root),
        "qa_root": str(qa_root),
        "source_count": len(sources),
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "results": [asdict(result) for result in results],
    }
    manifest_path = manifest_dir / "compile-manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    failures = [r for r in results if r.exit_code or not r.pdf_bytes]
    overfull = [r for r in results if r.overfull_boxes]
    print(f"COMPILED={len(results)} FAILURES={len(failures)} OVERFULL_DOCUMENTS={len(overfull)}")
    print(f"ELAPSED_SECONDS={manifest['elapsed_seconds']}")
    print(f"MANIFEST={manifest_path}")
    for result in (failures + overfull)[:30]:
        print(
            f"ISSUE source={result.source!r} exit={result.exit_code} "
            f"overfull={result.overfull_boxes} excerpt={result.error_excerpt[-500:]!r}"
        )
    return 1 if failures or overfull else 0


if __name__ == "__main__":
    raise SystemExit(main())
