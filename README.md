# Framewright

Framewright is a director-steered, asset-aware, intent-preserving cinematic compiler for AI filmmaking. It turns a director's approved scene intent, decision state, and production assets into structured storyboard, keyframe, and video-generation prompts.

- Current core version: **4.1.1**
- Release status: **stable**
- Desktop Framewright mirror: **4.1.1**
- GitHub `main`: **4.1.1**
- Global invocation: **`$framewright` only**

Author: **Tairan Li**

## Repository structure

- [`skill/framewright/`](skill/framewright/) — installable Codex Skill
- [`skill/framewright/references/framewright.md`](skill/framewright/references/framewright.md) — current authoritative Framewright specification
- [`skill/framewright/references/runtime_profiles/`](skill/framewright/references/runtime_profiles/) — subordinate, target-versioned Video Prompt adapters
- [`skill/framewright/references/keyframe_profiles/`](skill/framewright/references/keyframe_profiles/) — subordinate image adapters for Midjourney V8.2 creation and ChatGPT Image 2 creation/editing
- [`skill/framewright/references/craft/`](skill/framewright/references/craft/) — integrated, on-demand camera/action, identity/material, light/sound and diagnosis guidance
- [`versions/releases/`](versions/releases/) — immutable, version-numbered release snapshots
- [`versions/iterations/`](versions/iterations/) — preserved development iterations
- [`versions/beta/`](versions/beta/) — preserved historical beta experiments
- [`docs/product-vision.md`](docs/product-vision.md) — clean-room product evaluation brief

GitHub `main` is the source of truth for the synchronized stable release. Framewright 4.1.1 is the intended release across the local Source, Desktop mirror, global installation, and GitHub `main`.

## Install in Codex

Install the stable package from `https://github.com/jamesltr0701-cell/framewright/tree/main/skill/framewright` into the global `framewright/` folder.

After installation, invoke it explicitly with `$framewright`.

Version 4.1.1 promotes the 4.1 craft and lightweight-workflow improvements and deliberately narrows image routing to the user's real two-tool workflow. Midjourney V8.2 is the default and only Midjourney creator for Shot Plates and Keyframes. ChatGPT Image 2 is the default Storyboard creator, an explicit alternative creator for Shot Plates and Keyframes, and the sole editor for all three image artifacts. Midjourney V7 and a separate Midjourney Edit Model adapter are not part of the active package. The external Seedance 2.0 skill pack is not required. Core retains all director decisions; each selected adapter retains only its serialization responsibility. Adapted reference material and its MIT notice are identified in [craft provenance](skill/framewright/references/craft/PROVENANCE.md).

Framewright is configured for explicit invocation and one active stage at a time. The once-per-unit Storyboard Preflight gate, branching Look Development, provisional-to-committed Shot Spine review, and generation routing for continuous single shots, whole edited sequences, or one shot at a time remain intact. Image 2 edits always return to the immutable original master rather than stacking edited pixels. Target-specific Video Prompt behavior remains subordinate to Core: Seedance 2.0, Seedance 2.5, and MiniMax H3 each retain separate registered adapters. A resolved Storyboard stage still generates exactly one initial board image; automatic retries, variants, unrequested Shot Plate or Keyframe generation, Video generation, ChatCut, and OpenMontage remain outside the default boundary.

## Repository policy

This repository intentionally excludes films, image case studies, active projects, generated media, private working files, and third-party tools. Selected adapted knowledge may be included with explicit attribution and its applicable notice; the external tool or skill package is not bundled.

## Versioning policy

An experimental candidate may remain isolated on an unpushed local branch with a `-local` suffix. It does not receive a formal release snapshot and does not update the Desktop mirror or GitHub `main` until a separate promotion approval.

Every promoted Framewright patch or feature release preserves the previous version and publishes one matching new version locally and on GitHub:

1. Archive the current authoritative specification as an immutable `framewright-vX.Y.Z.md` snapshot before editing.
2. Increment the canonical specification's YAML `version`.
3. Create the matching new release snapshot.
4. Verify that the desktop canonical file, desktop snapshot, repository reference, and repository snapshot are byte-identical.
5. Commit and push the same version metadata and README version to GitHub.

Existing versioned snapshots are never overwritten or repurposed.

Copyright © 2026 Tairan Li. All rights reserved. No license for reuse or redistribution is granted unless stated separately. Third-party portions remain subject to their notices, including [the MIT notice for adapted craft material](skill/framewright/references/craft/PROVENANCE.md).
