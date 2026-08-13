---
title: "Framewright v3.5.2 Local Protected Baseline Manifest"
status: "FROZEN BEFORE IMPLEMENTATION"
freeze_date: "2026-08-13"
baseline_commit: "c89873c86dbac2b8a57635d6cf9b58bd646d29c9"
baseline_version: "3.5.1"
target_candidate: "3.5.2-local"
target_branch: "codex/framewright-v3.5.2-local-seedance-qualification"
external_generation_calls: 0
---

# Framewright v3.5.2 本地受保护基线清单

## Baseline gate

- 原始分支：`codex/framewright-next-local-experiment`
- 原始 HEAD：`c89873c86dbac2b8a57635d6cf9b58bd646d29c9`
- Core：`3.5.1`
- Seedance 2.5 profile：`1.2.0`
- 回归：`25 / 25`
- 目标分支已创建且没有 upstream，不 push。
- 用户已有 `Framewright/`、`output/`、`outputs/`、`storyboard/` 保持未追踪、未修改。

## Baseline fingerprints

| Path | SHA-256 |
|---|---|
| `skill/framewright/SKILL.md` | `79deb8bd85d5a5867371737472ed25ded735dc1416aa21e3100ceb8956a02539` |
| `skill/framewright/references/framewright.md` | `f51dbf4d247b6eb9a6f9860a1d60a52a306007fb9365df48f0fac2d8c8bc7baa` |
| `skill/framewright/references/runtime_profiles/seedance_2_5.md` | `dc0ae58e5c2c1115fdde3f3a7ddc9edebb09966b1f994e6366c375db11c16b25` |
| `skill/framewright/scripts/validate_framewright.py` | `409065dec286daa3b11ec7ddc71eb8075098bc94bda69bdb1abbf011a41bc412` |
| `testing/next-local/run_regression.sh` | `db3882e85e46fa3f8f19159ac176bf720d2f388d5a6d9c1814f984324d178c71` |
| `testing/next-local/expected/protected_anchors.yaml` | `d175d5c937e403814c64dc18b319d02a9930f20848a556938859e2b592852276` |

## Source hierarchy amendment authorized by user

Lark export/download was attempted after explicit authorization but did not expose a usable export path. The current Lark page still provided Grade A evidence: document identity, `08 月 12 日` latest-modified marker, full table of contents, core prompt formula, scope disclaimer, and official BytePlus link.

The user authorized continuing with this evidence set:

1. current BytePlus online document `2607689`, last updated `August 11, 2026 09:41:01`, recovered as complete embedded document text;
2. current Lark Prompt Guide visible page structure and visible passages;
3. local reconciled Prompt Guide PDF created from the same Lark source on 2026-08-03;
4. the approved v3.5.2 alignment plan and compatibility audit.

This candidate must be reported as `BytePlus-current / Lark-visible / reconciled-PDF-qualified`, not as a native Lark-export freeze.

## Official-source ledger

| ID | Contract | Class | Frozen source judgment |
|---|---|---|---|
| S01 | One request supports up to 50 total reference assets | HARD LIMIT | Current BytePlus online text |
| S02 | Images: up to 30, each up to 4K | HARD LIMIT | Current BytePlus online text; matches reconciled PDF |
| S03 | Videos: up to 10; combined duration no more than 30 seconds | HARD LIMIT | Current BytePlus online text; matches reconciled PDF |
| S04 | Audio: up to 10; combined duration no more than 30 seconds | HARD LIMIT | Current BytePlus online text; matches reconciled PDF |
| S05 | Subject images: 1-8 subjects generally better; 9-12 possible with lower stability | RECOMMENDATION | Current BytePlus online text |
| S06 | Subject audio/video: 1-5 subjects generally better; 6-10 possible with lower stability | RECOMMENDATION | Current BytePlus online text |
| S07 | Motion/style reference video: 5-10 seconds generally better | RECOMMENDATION | Current BytePlus online text |
| S08 | Smart Edit: source video under 20 seconds generally better; 1-5 reference images better, 6-8 possible with lower stability | RECOMMENDATION | Current BytePlus online text |
| S09 | Smart Edit ratio locked to source with `adaptive`; duration locked with `-1`; output may differ by about 0.3 seconds | SURFACE HARD RULE / TOLERANCE | Current BytePlus online text |
| S10 | First/last-frame route ratio locked to first frame with `adaptive`; same-ratio endpoint images; duration user-defined | SURFACE HARD RULE | Current BytePlus online text |
| S11 | Extend ratio locked to source with `adaptive`; duration user-defined; forward/backward trigger required; MOV recommended | SURFACE HARD RULE / RECOMMENDATION | Current BytePlus online text |
| S12 | Storyboards work better at 15 panels or fewer; line art recommended; exact panel alignment not guaranteed | RECOMMENDATION / LIMITATION | Current BytePlus online text |
| S13 | Keyframes are ordered independent images and align more strictly than a storyboard grid | RECOMMENDATION | Current BytePlus online text and reconciled PDF |
| S14 | Numeric timestamps use integer seconds and control progression, not guaranteed frame-accurate edit points | SURFACE RULE / LIMITATION | Current BytePlus online text and reconciled PDF |
| S15 | Negative controls explicitly support subtitles, SFX, BGM and dialogue | SURFACE SYNTAX | Current BytePlus online text |
| S16 | Lark reconciled syntax maps music `()`, SFX `<>`, dialogue `{}`, visible subtitle `■■` | SNAPSHOT-QUALIFIED SERIALIZATION | Reconciled PDF; current Lark directory confirms special-syntax section but exact glyphs were not freshly exported |
| S17 | Exact typography, formulas, signs and frame-accurate timing need prepared assets or post-production for reliability | LIMITATION | Reconciled PDF; consistent with current official capability framing |

## Protected interpretation

- `S12` is not a hard 15-panel ban. It must generate an assistant-facing stability warning and must not override the approved one-GU/one-board rule or silently split a GU.
- `S16` remains snapshot-qualified. The adapter may serialize it only for an explicitly requested scope and reports this evidence grade; it must not activate music, dialogue, subtitles or visible text by default.
- A 30-second capability is a ceiling, not the default duration or feasibility proof.
- All unlisted Core behavior is protected by default.

## Planned diff whitelist

- `skill/framewright/SKILL.md`
- `skill/framewright/references/framewright.md`
- `skill/framewright/references/runtime_profiles/seedance_2_5.md`
- `skill/framewright/scripts/validate_framewright.py`
- `testing/next-local/run_regression.sh`
- `testing/next-local/expected/protected_anchors.yaml`
- new `testing/next-local/fixtures/seedance25_*.yaml`
- v3.5.2 local reports explicitly listed by the approved plan

No release snapshot, README, Desktop mirror, GitHub branch or external generation is authorized.
