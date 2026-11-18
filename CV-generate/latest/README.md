# Latest General Academic CV (18 November 2026)

This directory contains the current general English CV source and its upload-ready PDF. This revision corrects both arXiv identifiers, records the two SQJ submissions, and presents the Celestial series as the current development line. Historical supervisor-specific CVs remain unchanged.

## Files

- [Zhiheng-Zhang-Academic-CV.pdf](Zhiheng-Zhang-Academic-CV.pdf): two-page, searchable US Letter PDF for general PhD applications.
- [CV.md](CV.md): single source of truth for CV content.
- [build-cv.py](build-cv.py): offline PDF generator; requires Python 3 and ReportLab.

## Manuscript status

Updated: 18 November 2026.

| Manuscript | arXiv preprint | Journal status |
|---|---|---|
| **Omission-Safe Conditional Contracts for Evidence-Closed CI Qualification** (DS-Hns) | [2610.39241](https://arxiv.org/abs/2610.39241), cs.SE | Submitted to Software Quality Journal (SQJ); awaiting review |
| **Architectural Debt Enforcement under Incomplete Observation: A Controlled Study of Ratchets and Evidence Qualification** (Boss-A2) | [2610.41276](https://arxiv.org/abs/2610.41276) | Submitted to Software Quality Journal (SQJ); awaiting review |

Both manuscripts are listed as submissions, not accepted publications. The arXiv preprints and journal review processes are independent; neither status implies acceptance or completed peer review.

## Current project positioning

DS-Hns, Codex Boss, and Utopia are completed and frozen historical projects. The current active development line is the **Celestial series**, a multi-repository software portfolio spanning agentic research tooling, knowledge/evidence management, personal-finance software, and exploratory wearable/HCI and scientific-simulation applications. Software development and systems engineering are the common core, with emphasis on usable workflows and reliability validated through reproducible tests, runtime evidence, and practical use. Individual projects have different maturity levels; the CV does not imply that the entire series is complete or independently validated.

## Scope of this revision

1. Corrected Boss-A2's public arXiv identifier to 2610.41276 and retained DS-Hns as 2610.39241.
2. Marked both manuscripts as submitted to SQJ and awaiting review.
3. Reframed DS-Hns, Codex Boss, and Utopia as completed/frozen historical projects.
4. Added the Celestial series as the current multi-domain software-development line, while distinguishing implemented, planned, and unverified capabilities.
5. Preserved the existing education and Master's research facts; kept the CV to two pages.
6. Historical supervisor-specific CVs were not changed. No school portal, email, or application record was modified.

## Rebuild and validation

Run from the repository root:

```bash
python3 CV-generate/latest/build-cv.py
```

The regenerated PDF is two pages, US Letter, searchable, and retains clickable links to both arXiv preprints and the cited project repositories.

- Page count: 2
- File size: 8,949 bytes
- SHA-256: `53e20fae9f86a9f8aaa0f4c3d2914e4b914401b918c5dc326c6a6699765fe19f`

