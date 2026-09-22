# Auto-Application / Agent Contract

This repository is a source of truth, not permission to blindly submit applications.

## Allowed automation

- refresh public program requirements
- update structured screening fields with source + verification date
- generate school-specific checklists
- verify each proposed supervisor has a public direct email; delete candidates that fail this gate
- refresh the daily outreach pool only together with a same-date `applications/OUTREACH-PACK-YYYY-MM-DD.md`
- generate individualized outreach subjects/bodies or form-ready text from `narrative_route`
- generate/refresh candidate-specific CV source when a CV is requested and expose the remaining PDF/material state explicitly
- assemble one per-candidate material package (body/form + CV + transcript/supporting files + project links)
- track deadlines and missing materials
- prepare application packages for review

## Human checkpoint required

- paying application fees
- final submission
- sending high-stakes claims not already supported by stored evidence
- accepting/declining offers
- committing to a supervisor or funding arrangement

## Never do

- treat archived requirements as current
- change `unknown` to a factual value without evidence
- fabricate submission/payment/reference completion
- resurrect a `REJECT` program without checking its reopen condition
- mass-email faculty
- retain an outreach candidate without a publicly verified direct email
- let LGBT/trans or ACG preference override a hard-gate decision

## Output contract

For ordinary screening, agents should update structured data and refresh the human-readable views.

For a **daily outreach-pool refresh**, completion requires all of the following in the same run:

- public-email verification for every selected supervisor;
- current pool file;
- same-date daily outreach pack;
- individualized body/form text for every selected target;
- one material-package entry per target;
- candidate-specific CV source when required;
- explicit pending state for any artifact that does not actually exist.

A candidate with only a name/email/recruitment signal is **not** a completed outreach-pool row. Never synthesize a fake attachment path or mark a missing PDF as ready.

For contact history, the explicit human ledger/application record overrides stale structured `not_contacted` data.