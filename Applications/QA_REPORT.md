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
| Supervisor folders | 66 passed |
| Complete TeX sources | 528 passed |
| Non-empty Markdown files | 265 passed |
| Official transcript copies | 66 passed |
| TeX compilations | 528 / 528 passed |
| Compile failures | 0 |
| LaTeX warnings | 0 |
| Overfull boxes | 0 |
| Underfull boxes | 0 |
| Unicode dash characters in TeX | 0 |

Each TeX source was compiled twice. The machine-readable compile manifest is written to `tmp/pdfs/compile-manifest.json` during acceptance.

## Visual acceptance

Eight representative document types from one package at each newly added university were rendered and inspected, covering 26 pages in total. The representative packages were Kian Hsiang Low at the National University of Singapore and Yihan Du at the Singapore University of Technology and Design:

1. Academic CV
2. Research CV
3. Statement of Purpose
4. Research Statement
5. Research Proposal
6. Quant-Ultra Research Summary
7. Privacy Lens Research Summary
8. Writing Sample Cover Note

All inspected pages used US Letter media boxes and had extractable text. No clipping, overlap, unreadable glyphs, or content outside page bounds was observed. Each representative proposal remained a readable two-page document.

## GRE hard-constraint audit

The current programme-level GRE review is recorded in `Applications/GRE_AUDIT.md`. NTU CCDS was removed because its official programme page states that GRE/GMAT is required for applicants who did not graduate from a Singapore Autonomous University. NUS School of Computing and SUTD were retained because their current official admissions pages state that GRE is not required. All other retained programmes were reviewed as not required, optional, recommended, or not listed as a programme requirement; each must still be checked against the live portal 30 days before submission.

## Acceptance boundary

This run establishes source completeness, TeX compilability, text extraction, and representative visual layout. It does not clear factual placeholders or make the packages submission-ready. Email, phone, exact degree titles and dates, referees, English-language evidence, writing-sample details, Privacy Lens permanent links, current faculty availability, current program requirements, and school-specific portal prompts must still be verified before any material is sent.
