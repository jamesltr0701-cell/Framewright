# Framewright Merge

Framewright Merge is the isolated local fusion experiment derived from Framewright. It preserves Framewright's director, state, and compiler ownership while testing selectively absorbed Seedance 2.0 knowledge.

- Current merge version: **3.5.4-merge.0-local**
- Base: **Framewright 3.5.3-local plus the reviewed Intake candidate**
- Release status: **local experiment**
- Global invocation: **`$framewright-merge` only**

Author: **Tairan Li**

## Repository structure

- [`skill/framewright-merge/`](skill/framewright-merge/) — installable Codex Skill
- [`skill/framewright-merge/references/framewright.md`](skill/framewright-merge/references/framewright.md) — current authoritative Framewright specification
- [`skill/framewright-merge/references/runtime_profiles/`](skill/framewright-merge/references/runtime_profiles/) — subordinate, target-versioned Video Prompt adapters
- [`versions/releases/`](versions/releases/) — immutable, version-numbered release snapshots
- [`versions/iterations/`](versions/iterations/) — preserved development iterations
- [`versions/beta/`](versions/beta/) — preserved historical beta experiments
- [`docs/product-vision.md`](docs/product-vision.md) — clean-room product evaluation brief

This local repository is the editable Source for `framewright-merge`. It has no publication remote and must not replace, publish to, or mutate the stable `framewright` Source.

## Install in Codex

Install the validated local package from `skill/framewright-merge/` into a separately named global `framewright-merge/` folder. Never install it over `framewright/`.

After installation, invoke it explicitly with `$framewright-merge`.

Framewright Merge is configured for explicit invocation and one active stage at a time. The 3.5.0 release adds dependency-sensitive Adaptive Questioning, a nested Intent Ledger, causal-state and blocking readiness passes, and Semantic Preflight while preserving the existing Material Registry and stage contracts. Target-specific Video Prompt behavior is subordinate to the Core: Seedance 2.5 uses its surface-aware adapter, while the local MiniMax H3 experiment loads a separate H3 adapter only after the director explicitly selects H3. Each adapter owns only target routing and serialization; neither may override the Production Spine, director locks, sound defaults, stage, or generation-unit boundaries. A resolved Storyboard stage still generates exactly one initial board image as part of the same stage package; automatic retries, variants, Keyframe generation, Video generation, ChatCut, and OpenMontage remain outside the default boundary.

## Repository policy

This repository intentionally excludes films, image case studies, active projects, generated media, private working files, and third-party tools.

## Versioning policy

An experimental candidate may remain isolated on an unpushed local branch with a `-local` suffix. It does not receive a formal release snapshot and does not update the Desktop mirror or GitHub `main` until a separate promotion approval.

Every promoted Framewright patch or feature release preserves the previous version and publishes one matching new version locally and on GitHub:

1. Archive the current authoritative specification as an immutable `framewright-vX.Y.Z.md` snapshot before editing.
2. Increment the canonical specification's YAML `version`.
3. Create the matching new release snapshot.
4. Verify that the desktop canonical file, desktop snapshot, repository reference, and repository snapshot are byte-identical.
5. Commit and push the same version metadata and README version to GitHub.

Existing versioned snapshots are never overwritten or repurposed.

Copyright © 2026 Tairan Li. All rights reserved. No license for reuse or redistribution is granted unless stated separately.
