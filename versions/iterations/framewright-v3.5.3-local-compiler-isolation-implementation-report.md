---
title: "Framewright v3.5.3 Local Compiler Isolation Implementation Report"
status: "LOCAL CANDIDATE IMPLEMENTED"
report_date: "2026-08-14"
baseline_commit: "d31b7a25bc6cb45af57bd20ee5f05f641529e70b"
implementation_commit: "fe712d6"
branch: "codex/framewright-v3.5.3-local-compiler-isolation"
candidate_version: "3.5.3-local"
external_generation_calls: 0
credit_spend: 0
---

# Framewright v3.5.3-local Compiler Isolation 实施报告

## Outcome

Framewright 现已在本地候选中形成一个 Core 与一个内部 Adapter Collection。Core Native 当前明确指向 Seedance 2.0；Seedance 2.5 与 MiniMax H3 继续作为 subordinate adapters。目标模型选择序列化 owner，平台、provider、surface、route 与外部 prompt Skill 均不能取得 ownership。

## Baseline and branch

- live baseline branch: `codex/framewright-minimax-h3-adapter-experiment`;
- live baseline commit: `d31b7a25bc6cb45af57bd20ee5f05f641529e70b`;
- implementation branch: `codex/framewright-v3.5.3-local-compiler-isolation`;
- implementation commit: `fe712d6`;
- baseline regression: `58 / 58`;
- final regression: `78 / 78`.

Baseline had no tracked changes. Untracked `Framewright/`, `output/`, `outputs/`, `storyboard/`, and the supplied v3.5.3 plan were preserved and excluded from the commit.

## Registry and owner mapping

| target_model | serialization_owner | adapter_id | profile |
|---|---|---|---|
| `seedance_2_0` | `framewright_core_native` | `null` | `null` |
| `seedance_2_5` | `framewright_adapter_seedance_2_5` | `seedance_2_5` | `seedance_2_5.md` |
| `minimax_h3` | `framewright_adapter_minimax_h3` | `minimax_h3` | `minimax_h3.md` |

`adapter_registry.yaml` is the single validator source for this mapping and the allowed core compiler instruction sources. Adapter route names remain adapter-internal task choices and cannot act as owners.

## Files

Created:

- `AGENTS.md`;
- `skill/framewright/references/runtime_profiles/adapter_registry.yaml`;
- 20 focused `testing/next-local/fixtures/isolation_*.yaml` fixtures.

Modified:

- `skill/framewright/SKILL.md`;
- `skill/framewright/references/framewright.md`;
- `skill/framewright/scripts/validate_framewright.py`;
- `testing/next-local/expected/protected_anchors.yaml`;
- `testing/next-local/run_regression.sh`;
- 35 existing ownership-related Seedance 2.5, MiniMax H3, and structure-owner fixtures, migrated only to the singular registry-backed ownership schema.

Protected and byte-identical:

- `skill/framewright/references/runtime_profiles/seedance_2_5.md`: `829f615d92cc8179002450cf55758c14c09f7ca087b6a003678c2c9f7e2f9cbf`;
- `skill/framewright/references/runtime_profiles/minimax_h3.md`: `ff394b7b91b1fabb6f96f26cb995f22400a033b943da645b4c0d6a2c40093848`;
- `README.md`, `skill/framewright/agents/openai.yaml`, `docs/**`, `versions/releases/**`, historical reports, and user outputs were untouched.

Evidence reports created after the implementation commit:

- `versions/iterations/framewright-v3.5.3-local-compiler-isolation-implementation-report.md`;
- `versions/iterations/framewright-v3.5.3-local-compiler-isolation-regression-report.md`;
- `versions/iterations/framewright-v3.5.3-local-compiler-isolation-remaining-risk-report.md`.

## Validator implementation

- registry schema and referenced paths are validated deterministically;
- every Video Prompt path requires a resolved target model and one scalar registered owner;
- target, owner, adapter ID, profile contract, and compiler sources must match;
- Core Native rejects adapter IDs and adapter profile contracts;
- missing, empty, list, multiple, unknown, external, mismatched, and route-level owners fail;
- foreign compiler instruction sources and platform-controlled serializer fields fail;
- ownership metadata in clean prompt text fails;
- the new `video-prompt` command validates the actual saved `.txt` path rather than only an abstract fixture.

## Boundaries

No external model-prompt Skill was read or invoked, and no external Skill content was copied into Framewright. The procedural local `skill-creator` validation tool was used only to validate the Framewright skill folder. No image, video, or audio was generated; external generation calls and credit spend were both zero.

Desktop and GitHub remain on their prior distributed state. This version is intentionally a local candidate and is not release-complete until a separately approved promotion synchronizes local repo, Desktop Framewright, and GitHub with checksum verification.
