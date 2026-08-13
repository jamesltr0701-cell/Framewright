---
title: "Framewright v3.5.3 Local Compiler Isolation Remaining Risk Report"
status: "LOCAL CANDIDATE RISKS DISCLOSED"
report_date: "2026-08-14"
candidate_version: "3.5.3-local"
implementation_commit: "fe712d6"
external_generation_calls: 0
credit_spend: 0
---

# Framewright v3.5.3-local 剩余风险

## R01 — Host obedience remains partly procedural

The repository now states exclusivity in both `AGENTS.md` and `SKILL.md`, and the validator rejects unregistered compiler sources. A host that ignores repository instructions could still consult another tool before validation; the final clean prompt cannot pass if that source is honestly recorded, but validator evidence cannot prove an opaque host never consulted it.

Mitigation: treat the registry-backed compile trace as mandatory provenance and preserve the project-level instruction boundary.

## R02 — Actual prompt validation depends on the declared metadata

The `video-prompt` command validates real prompt text plus operator-supplied target and owner arguments. It can reject mismatches against the registry but cannot infer the true remote model from a provider UI.

Mitigation: target resolution remains an intake decision and the Run Card records the selected model separately from platform execution.

## R03 — Deterministic isolation is not generation evidence

The 78-fixture suite proves mapping, ownership, cleanliness, and rejection behavior. It does not test visual quality, prompt adherence, audio behavior, model availability, latency, or credit cost for Seedance 2.0, Seedance 2.5, or MiniMax H3.

Mitigation: gather separately authorized scene-local generation evidence during future use; do not promote one result into Core or adapter law automatically.

## R04 — Distribution is intentionally incomplete

The local repo candidate is `3.5.3-local`, while Desktop Framewright and GitHub were deliberately not synchronized. The current working skill path can use this local candidate, but it is not a three-location release.

Mitigation: promote only after explicit approval, preserving immutable prior releases and verifying Core, registry, profiles, Skill entrypoint, validator, and regression assets by version metadata plus SHA-256 across all three required locations.

## Status

LOCAL CANDIDATE COMPLETE / DISTRIBUTION INCOMPLETE
