# Latest General Academic CV (18 November 2026)

This directory contains the current general English CV source and its upload-ready PDF. This revision updates the publication status of both research manuscripts to reflect their submission to Software Quality Journal (SQJ). Historical supervisor-specific CVs remain unchanged.

## Files

- [Zhiheng-Zhang-Academic-CV.pdf](Zhiheng-Zhang-Academic-CV.pdf): two-page, searchable US Letter PDF for general PhD applications.
- [CV.md](CV.md): single source of truth for CV content.
- [build-cv.py](build-cv.py): offline PDF generator; requires Python 3 and ReportLab.

## Manuscript status

Updated: 18 November 2026.

| Manuscript | Public preprint status | Journal status |
|---|---|---|
| **Omission-Safe Conditional Contracts for Evidence-Closed CI Qualification** (DS-Hns) | Public arXiv preprint: [2610.39241](https://arxiv.org/abs/2610.39241), cs.SE | Submitted to Software Quality Journal (SQJ); awaiting review |
| **Architectural Debt Enforcement under Incomplete Observation: A Controlled Study of Ratchets and Evidence Qualification** (Boss-A2) | arXiv submission awaiting moderation; no public identifier claimed | Submitted to Software Quality Journal (SQJ); awaiting review |

Both manuscripts are listed as submissions, not accepted publications. The arXiv and journal workflows are independent; neither status implies acceptance or completed peer review.

## Scope of this revision

1. Updated the section heading and both manuscript entries to show the SQJ submission status.
2. Retained the public arXiv identifier for DS-Hns and the separate moderation-pending status for Boss-A2.
3. Preserved the existing education, project evidence, skills, and proposed doctoral focus.
4. Kept the CV to two pages; historical supervisor-specific versions were not changed.
5. No school portal, email, or application record was modified.

## Rebuild and validation

Run from the repository root:

```bash
python3 CV-generate/latest/build-cv.py
```

The regenerated PDF is two pages, US Letter, searchable, and retains the existing layout and hyperlinks.

- Page count: 2
- File size: 8,092 bytes
- SHA-256: `052f98c3c6c82c1ca31f67184a821052e2c0dd768ed31e24bab93ce6d4cfd6f2`

