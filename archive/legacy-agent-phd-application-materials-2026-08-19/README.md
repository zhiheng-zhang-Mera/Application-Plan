# Legacy archive — agent/phd-application-materials

Archived from branch `agent/phd-application-materials` at commit `5bb33176f8671290adf1f0a1e71a59ca7dbc9424` (2026-08-19 snapshot).

## Why this exists

The repository was later restructured around the current lowercase `applications/`, `materials/`, `targets/`, `automation/`, and `docs/` layout. This archive preserves the older application-package generation without mixing legacy files into the active workflow.

## What was mapped into the current structure

- `Documents/` was not duplicated here because its tree is identical to the current root `Documents/`.
- Referee workflow guidance has been superseded by the maintained packs under `materials/referees/`.
- Current application tracking and outreach use `applications/` and the root README/STATUS/STRATEGY files.

## What remains only as legacy material

- `Applications/`: old per-school / per-supervisor full application packages, including historical CV, SOP, research proposal, contact-email and checklist drafts.
- `tools/`: scripts/utilities from the old packaging workflow.
- `ReadMe.md`: the large historical planning document from that branch.
- `.gitignore`: kept only to make the snapshot structurally complete.

Treat everything in this folder as read-only historical reference. Do not use it as the source of truth for current outreach or application status.
