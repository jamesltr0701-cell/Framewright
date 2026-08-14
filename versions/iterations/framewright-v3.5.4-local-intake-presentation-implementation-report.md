---
title: "Framewright v3.5.4 Local Intake Presentation Implementation Report"
status: "LOCAL CANDIDATE IMPLEMENTED"
report_date: "2026-08-14"
baseline_commit: "3f7b190ed0f1cb4fbcfb299dbf88f17738c473f8"
implementation_commit: "5e176fa88041a409d5184f8eb105bcfbc530fbc0"
branch: "codex/framewright-v3.5.4-local-intake-presentation"
candidate_version: "3.5.4-local"
external_generation_calls: 0
credit_spend: 0
---

# Framewright v3.5.4-local Intake Presentation 实施报告

## Outcome

Framewright 现已在本地候选中吸收经过审计的 Seedance Intake 方法，但
Framewright 仍是唯一决策引擎、状态所有者和 compiler。融合只改变 Intake
的表达方式与审阅透镜，不引入 Seedance runtime dependency、第二套 Intake、
第二份 canonical state 或新的 serializer owner。

## Absorbed selectively

- one Framewright-owned `Intake Presentation Layer` with `blank-slate`,
  `rough-idea`, and `production-fluent` expression profiles;
- explicit separation between expression proficiency and Director Mode;
- preservation of distinctive user wording and professional instructions as
  source evidence;
- provisional proposal behavior without silent director locks;
- `NON-NARRATIVE REFUSAL` for utility-led work;
- `visible suppressed behavior` as an observable performance review;
- `non-transferable detail` with source provenance;
- review-lens-only status, nested under the existing Production Spine and
  Intent Ledger authority.

## Explicitly excluded

- external Seedance Skill invocation, import, routing, or fallback;
- Fast Lane or any bypass of the Intake Hard Stop;
- fixed interview questions replacing dependency-sensitive scheduling;
- expression proficiency selecting AUTEUR, APPRENTICE, or SCREENWRITER mode;
- a Director's Read record, ten-field mandatory state, or second memory;
- platform, provider, or surface ownership of prompt serialization;
- automatic multi-stage output, generation, installation, or credit spend.

## Changed files

- `skill/framewright/references/framewright.md`;
- `skill/framewright/SKILL.md`;
- `skill/framewright/scripts/validate_framewright.py`;
- `testing/next-local/expected/protected_anchors.yaml`.

Runtime adapter profiles, adapter registry, stable release snapshots, README,
Desktop Framewright, global installed Skills, GitHub, generated media, and user
output directories were not changed.

## Source and judge identity

- audited Seedance source tag: `v6.7.0`;
- audited Seedance commit: `8802978eb17bea7b1fa4e8bd230d9edfbe58e0dd`;
- Framewright baseline: `3f7b190ed0f1cb4fbcfb299dbf88f17738c473f8`;
- implementation commit: `5e176fa88041a409d5184f8eb105bcfbc530fbc0`;
- frozen Intake judge contracts hash:
  `668b9348ef8446f50ae144cd03c53afb7f2e3b33e37a64d3b1f337ed98fda510`;
- frozen 14-case set hash:
  `66d37105df25a958493e629fe295045953833cf80a706de94c3b1de63a6f0761`.

## Boundary

This is a local candidate only. It is not installed, promoted, pushed, or
synchronized to the Desktop mirror. Release and three-location synchronization
remain a separate explicit approval gate.
