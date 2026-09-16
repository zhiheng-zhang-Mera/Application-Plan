# Auto-Application / Agent Contract

This repository is a source of truth, not permission to blindly submit applications.

## Allowed automation

- refresh public program requirements
- update structured screening fields with source + verification date
- generate school-specific checklists
- draft outreach/SOP variants from `narrative_route`
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
- let LGBT/trans or ACG preference override a hard-gate decision

## Output contract

Agents should update `data/*.yaml` first, then refresh human-readable Markdown views. If YAML and Markdown disagree, YAML is canonical and the inconsistency should be flagged.