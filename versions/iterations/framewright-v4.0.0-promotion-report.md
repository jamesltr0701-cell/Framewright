---
title: "Framewright 4.0.0 Promotion Report"
version: "4.0.0"
status: "stable_release"
date: "2026-08-24"
predecessor: "3.5.3-local"
candidate_lineage: "3.5.4 merge experiment through merge.10"
---

# Framewright 4.0.0 Promotion Report

## Promotion decision

The director approved the tested merge line as the next stable Framewright major release. The product and callable Skill return to the single name `framewright`; `framewright-merge` is retired as a callable test edition. Historical merge reports remain unchanged as provenance.

Framewright 3.5.3-local remains recoverable through its preserved Git commit, rollback branch or tag, and immutable Core snapshot. Version 4.0.0 does not overwrite earlier release snapshots.

## Promoted capability groups

- Framewright remains the only Core compiler and keeps director intent, state, shot structure, reference authority, generation-unit boundaries, and active-stage ownership.
- Seedance 2.0, Seedance 2.5, and MiniMax H3 are formal subordinate Video Prompt adapters rather than competing compilers.
- Every registered Video Prompt adapter attempts complete lossless Chinese payload re-serialization before content-bearing deletion when an English prompt exceeds the active character limit.
- Intake preserves professional wording, adapts its presentation to the user, and tracks material decisions in the Production Spine's nested Intent Ledger.
- Director Core includes directing intention, instrument coherence, selective directorial voice, pattern and rupture logic, living-director safeguards, and endpoint purpose.
- Storyboard Preflight asks once per current generation unit whether visual shot-structure review is needed before Video Prompt.
- Look Development branches across live action, near-live action, stylized 3D, 2D, mixed media, and visible VFX without turning intake into a fixed questionnaire.
- A provisional Shot Spine may be visualized by Storyboard, but only director feedback and approved state changes can produce the Committed Shot Spine.
- Generation Strategy distinguishes one continuous shot, one edited sequence generated as a unit, and shot-by-shot generation.
- Keyframes are shot- or function-scoped. Midjourney V7 is the default Keyframe prompt adapter; ordered multi-keyframes are recommended only for explicitly documented target workflows and manageable continuous-shot complexity.
- ChatGPT Image 2 Keyframe edits always return to the immutable original master. Semantic edit intent may accumulate; edited pixels may not.
- Generation-evidence and selected-take reconciliation stay bounded: no automatic retry, no silent boundary change, and no generated artifact may rewrite the Production Spine by itself.

## Name and installation migration

- Skill directory: `skill/framewright/`
- Skill name: `framewright`
- Explicit invocation: `$framewright`
- UI display name: `Framewright`
- Retired callable name: `$framewright-merge`

The former merge repository remains historical development evidence only. It is not a second product line or installed Skill after promotion.

## Release gates

Promotion is complete only after:

1. the complete regression suite and Skill structure validator pass from the renamed package;
2. the authoritative Core and `framewright-v4.0.0.md` snapshot are byte-identical;
3. the local Source, Desktop mirror, and GitHub `main` report version 4.0.0;
4. the required Video Prompt and Keyframe adapters are present in the local Source and Desktop mirror;
5. the global `$framewright` installation resolves to the 4.0.0 package and the former merge invocation is removed;
6. the live GitHub commit and version are verified after push.
