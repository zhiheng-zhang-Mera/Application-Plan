# Application package QA report

Acceptance run: 2026-08-15

## Local environment

- Installation root: `D:\PhD-Tools\TinyTeX`
- Distribution: TinyTeX-1 for Windows, release `v2026.05`
- Engine: pdfTeX 3.141592653-2.6-1.40.29 (TeX Live 2026)
- Installer cache: `D:\PhD-Tools\downloads\TinyTeX-1-windows-v2026.05.exe`
- Installer SHA-256: `5E9CD432D9278012524E6E0D26E2CE3225C7490905425D356C458D6F9122BBDD`
- Additional TeX packages installed for these sources: `microtype`, `enumitem`, and `titlesec`
- Isolated staging/output roots: `D:\PhD-Tools\qa-input` and `D:\PhD-Tools\qa-output`

The repository path contains non-ASCII characters. The compile workflow therefore copies each TeX source to a stable ASCII-only staging directory before invoking pdfLaTeX. Generated PDFs, logs, manifests, and page renders are QA intermediates and are intentionally excluded from Git.

## Automated acceptance

| Check | Result |
|---|---:|
| Supervisor folders | 53 passed |
| Complete TeX sources | 424 passed |
| Non-empty Markdown files | 213 passed |
| Official transcript copies | 53 passed |
| TeX compilations | 424 / 424 passed |
| Compile failures | 0 |
| LaTeX warnings | 0 |
| Overfull boxes | 0 |
| Underfull boxes | 0 |
| Unicode dash characters in TeX | 0 |

Each TeX source was compiled twice. The machine-readable compile manifest is written to `tmp/pdfs/compile-manifest.json` during acceptance.

## Visual acceptance

Eight representative document types from the Sinno Jialin Pan package were rendered and inspected, covering 13 pages:

1. Academic CV
2. Research CV
3. Statement of Purpose
4. Research Statement
5. Research Proposal
6. Quant-Ultra Research Summary
7. Privacy Lens Research Summary
8. Writing Sample Cover Note

All inspected pages used US Letter media boxes and had extractable text. No clipping, overlap, unreadable glyphs, or content outside page bounds was observed. The acceptance pass also corrected a long-link overflow, prevented an orphaned Academic CV project heading, and removed an obsolete replacement instruction from the Quant-Ultra summary.

## Acceptance boundary

This run establishes source completeness, TeX compilability, text extraction, and representative visual layout. It does not clear factual placeholders or make the packages submission-ready. Email, phone, exact degree titles and dates, referees, English-language evidence, writing-sample details, Privacy Lens permanent links, current faculty availability, current program requirements, and school-specific portal prompts must still be verified before any material is sent.
