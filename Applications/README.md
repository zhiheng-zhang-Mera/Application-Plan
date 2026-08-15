# 2027 PhD application packages

Generated from the application plan and the supplied background evidence on 2026-08-15.

Every final supervisor folder contains the authored application materials, a tailored email draft, a program checklist, a fact-check ledger, and copies of the supplied academic evidence. TeX source is used for every newly authored document intended to become a PDF. Original official evidence remains in its original format.

| Priority | School | Program | Supervisor packages | Outreach strategy |
|---:|---|---|---:|---|
| 01 | The Hong Kong University of Science and Technology (Guangzhou) | PhD in Financial Technology | 4 | Targeted contact strongly recommended; application may proceed in parallel. |
| 02 | University of Macau | PhD in Computer Science | 5 | Targeted contact is optional but potentially valuable; verify the 2027/28 call. |
| 03 | Drexel University | PhD in Computer Science | 4 | Departmental admission; email is an optional, selective draft and should not be mass-sent. |
| 04 | Stevens Institute of Technology | PhD in Computer Science | 4 | Departmental application; a selective email may be sent after checking faculty availability. |
| 05 | University at Buffalo, SUNY | PhD in Computer Science and Engineering | 4 | Do not cold-email generically; faculty fit belongs primarily in the application statement. |
| 06 | Concordia University | PhD in Computer Science / Software Engineering | 4 | Supervisor match is required before an admission offer; obtain an application Student ID before outreach where possible. |
| 07 | The Hong Kong Polytechnic University | PhD in Data Science and Artificial Intelligence / Computing | 4 | Targeted contact recommended; use the mandatory standard research-proposal form in the portal. |
| 08 | City University of Hong Kong | PhD in Data Science | 3 | Targeted contact recommended; confirm supervisor capacity before relying on a match. |
| 09 | Stony Brook University | PhD in Computer Science | 4 | Departmental admission; do not spend application time on generic cold email. |
| 10 | The Chinese University of Hong Kong | MPhil-PhD in Computer Science and Engineering | 5 | A professor must ultimately agree to supervise after the departmental process; targeted contact is essential. |
| 11 | University of Massachusetts Amherst | PhD in Computer Science | 5 | Departmental admission; faculty fit should be concentrated in the Personal Statement. |
| 12 | The Hong Kong University of Science and Technology | PhD in Computer Science and Engineering | 4 | Current CSE FAQ says an applicant must have a faculty member who agrees to supervise; targeted contact is a prerequisite, not mass email. |
| 13 | University of California, Riverside | PhD in Computer Science | 3 | Reserve application: send a targeted inquiry first and apply only if the PI signal and full portfolio justify the cost. |
| 14 | University of Technology Sydney | Doctor of Philosophy (PhD Thesis: Computer Science) | 3 | Agreed supervision or faculty approval is required; contact a supervisor and develop the proposal before the formal application. |
| 15 | Curtin University | Doctor of Philosophy - Computing | 3 | Supervisor support is a formal pre-application gate: submit an expression of interest with a topic and CV, then apply only if invited. |
| 16 | National University of Singapore | PhD in Computer Science (School of Computing) | 4 | Departmental application; selective faculty contact is useful after reading current work, but supervisor consent is not listed as a formal application prerequisite. |
| 17 | Singapore University of Technology and Design | PhD Programme (ISTD / ESD research alignment) | 3 | Targeted faculty contact is recommended because pillar and supervisor fit shape the research pathway; the formal application remains university-level. |

## Important limitations

- These are complete drafts, not submission-ready official records. The repository does not contain a current official Melbourne transcript, degree certificates, passport, English evidence, referee identities, or the complete writing sample.
- No publication, award, employment, rank, converted GPA, or supervisor interest is asserted.
- Faculty research hooks come from the plan and must be checked against current official profiles and recent work before sending.
- The current GRE screen is recorded in `Applications/GRE_AUDIT.md`; NTU CCDS was removed because its programme-level rule requires GRE/GMAT for this overseas-degree profile.
- HKUST CSE is treated as requiring a faculty member who agrees to supervise because its current FAQ says so; do not rely on the older optional-contact classification.
- Department-level programs include individual faculty-fit packages for organization, but their email files are clearly marked as optional or not for mass outreach.

## Build and validation

Run:

```powershell
python tools/build_application_packages.py
python tools/validate_application_packages.py
```

Compile TeX only after replacing placeholders. A compile check can still be run on drafts because placeholders are TeX-safe, but visual and factual approval is required before external use.

## D-drive QA environment

The verified local TeX environment is installed at `D:\PhD-Tools\TinyTeX` (TeX Live 2026). Because TeX cannot reliably create logs beneath the repository's non-ASCII path, the compile script copies each source to an ASCII-only staging folder under `D:\PhD-Tools\qa-input` and writes QA PDFs/logs under `D:\PhD-Tools\qa-output`.

```powershell
python tools/build_application_packages.py
python tools/validate_application_packages.py
python tools/compile_application_packages.py --workers 8
python tools/render_qa_representatives.py
```

The compile and render manifests are written below `tmp/pdfs/` and are intentionally ignored by Git.
