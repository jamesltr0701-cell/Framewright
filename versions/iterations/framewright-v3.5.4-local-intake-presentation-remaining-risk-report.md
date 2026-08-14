---
title: "Framewright v3.5.4 Local Intake Presentation Remaining Risk Report"
status: "LOCAL CANDIDATE RISKS DISCLOSED"
report_date: "2026-08-14"
candidate_version: "3.5.4-local"
implementation_commit: "5e176fa88041a409d5184f8eb105bcfbc530fbc0"
external_generation_calls: 0
credit_spend: 0
---

# Framewright v3.5.4-local 剩余风险

## R01 — Static coverage is not live conversational evidence

The frozen judge proves that required contracts exist and remain protected. It
does not prove that every host will select the correct expression profile or
produce a concise, natural Intake response.

Mitigation: review representative live invocations after an explicitly approved
local installation; keep outputs provisional and do not generate media.

## R02 — Presentation profiles can be over-applied

If a host treats `blank-slate`, `rough-idea`, or `production-fluent` as permanent
user identity, it could become patronizing or override later evidence.

Mitigation: the Core defines them as ephemeral current-expression conditions,
requires recalculation, and forbids serialization into state or prompts.

## R03 — Review lenses can become a hidden checklist

Visible suppressed behavior and non-transferable detail are useful only when
relevant. Mechanical application could overdirect performance or decorate a
utility task.

Mitigation: the Core makes each lens conditional, preserves the Question Value
Test and Performance Overdirection Test, and explicitly refuses mandatory
ten-field completion.

## R04 — The audited global Seedance copy has identity drift

The currently installed global copy also reports `v6.7.0` but is not identical
to the audited official tag. Framewright does not depend on that copy, so its
drift cannot change this candidate's compiler behavior.

Mitigation: keep the fusion self-contained and use the frozen official commit
only as audit evidence. Any global Seedance update remains a separate decision.

## R05 — Distribution is intentionally incomplete

This local repository now has `3.5.4-local`; Desktop Framewright, the global
installed Framewright Skill, and GitHub remain unchanged.

Mitigation: do not describe the candidate as released. Promotion requires a
separate approval, immutable release snapshot, full validation, and verified
version plus SHA-256 identity across all required locations.

## Status

LOCAL CANDIDATE IMPLEMENTED / STATIC AND EXISTING REGRESSION GREEN /
LIVE INTAKE REVIEW AND DISTRIBUTION PENDING
