# 2026-10-16 Wearable V3 — Gmail 实物草稿、附件与 PDF QA

## Result
PASS: 5 个不同大学、5 封 Gmail DRAFT，已核验收件人、主题、全文非空、附件数量与真实 Gmail attachment metadata；全程没有 Send，未交 admission、未支付费用。

| University | PI | Gmail message_id | draft_id | attachment count |
|---|---|---|---|---:|
| HKBU | Henry Dai | 1a1431c44c36f547 | r4006917016328847035 | 4 |
| POSTECH | Inseok Hwang | 1a144a04f39a8838 | r-8889791772818514675 | 2 |
| KAIST | Ian Oakley | 1a144a091bdd51f8 | r2817542136591518821 | 4 |
| SUSTech | Xueliang Li | 1a144a0b195b79d6 | r1068073041116440001 | 2 |
| ShanghaiTech | Quan Li | 1a144a0d6bd1fe3e | r-3081954922322332966 | 2 |

## School-level lock
- Only one current PI per university. SUSTech Zhang Jin and Sun Xiaohua are watch/deferred, KAIST Junehwa Song watch/deferred, HKBU Amelie Zhou watch/deferred. ShanghaiTech only Quan Li retained.
- All five exact Gmail messages returned DRAFT on re-read; old Lingnan and Lancaster drafts sent to recoverable Trash with explicit success result; Gmail list_drafts rechecked and returned precisely the five rows listed.
- The old HKBU draft was retained without body/attachments editing.
- Previous warm and sent supervisor threads remain immutable historical facts.

## New PDF compilation facts
- CV PDF: four new pdflatex builds + retained original HKBU = 5 (each verified 1 page).
- Research Note PDF: four new ReportLab documents + retained HKBU = 5 (each verified 1 page); source .md provided.
- KAIST WIT Brief Cover Letter PDF: new 1-page ReportLab build; for explicit recruiting protocol.
- Manual PDF render review at reduced contact-sheet scale; no clipping detected.
- Professional documents generated locally, not by committing sensitive transcripts or TeX to public GitHub. ReportLab/LaTeX source archive available in conversation ZIP.
- The attached KAIST transcript set contains an official UBC undergraduate transcript and existing Melbourne WAM record, not final MSc graduation transcript. Explicitly explained in email/cover letter.

## Claims audit
- Utopia completed and frozen; DS-Hns + Codex Boss completed and frozen predecessors; Utopia current main SHA 944f47dd6c7e18b3388b6d769dbbb6dddbe74f00 (checked); Digital-City current main cde01b0f71b4d165484540c1c740abc168e43c90 (checked).
- In candidate descriptions, capabilities bounded to actual two Windows execution workers, Android/Web interfaces and cross-host/fault/replay evidence; no already-finished wearable, medical trials, or complete personal AI claimed.
- CV/BSc/MSc claimed only from existing Application-Plan evidence; master's still in progress, no fabricated final GPA/rank or peer-reviewed paper.
- Lab papers cited according to 2026 verified public lab pages, with existing limits. Missing 2027 seat/program details marked UNKNOWN, not invented.

## Individual send-time gates
- POSTECH Hwang: generic lab recruit invitation, but **specific Fall 2027 PhD seat, international English waiver, funding** remain UNKNOWN.
- KAIST Oakley: WIT recruitment explicit; external applicant via School of Electrical Engineering, cross-discipline eligibility and funding still conditional. Canada BSc physical-completion English waiver route effective Fall 2027, personal approval pending.
- SUSTech Li Xueliang: 2027 School of Design PhD 081200 listing explicit; individual quota/academic and full-time constraints remain conditional; domestic admissions includes English/overall evaluation.
- ShanghaiTech Quan Li: PhD quota not demonstrated; 2027 webpage capacity statement concerns master's only; 2027 SIST admissions timeline unverified.
- HKBU Henry Dai: 2027 quota/funding and postgraduate document finality outstanding.

## Disclosure boundaries
No transcripts stored in public GitHub or ZIP. UK Surrey stays on user HOLD. No drafts created for SUSTech alternative faculty or KAIST Junehwa Song. Existing application statuses not changed.
