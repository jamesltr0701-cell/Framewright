# Framewright

Framewright is an asset-aware prompt compiler for AI filmmaking. It turns a director's scene intent and production assets into structured storyboard, keyframe, and video-generation prompts.

Current core version: **2.2.1**
Author: **Tairan Li**

## Repository structure

- [`skill/framewright/`](skill/framewright/) — installable Codex Skill
- [`skill/framewright/references/framewright.md`](skill/framewright/references/framewright.md) — current authoritative Framewright specification
- [`versions/releases/`](versions/releases/) — immutable, version-numbered release snapshots
- [`versions/iterations/`](versions/iterations/) — preserved development iterations
- [`versions/beta/`](versions/beta/) — Lite and Pro beta branches
- [`docs/product-vision.md`](docs/product-vision.md) — clean-room product evaluation brief

The GitHub repository is the source of truth. An installed local Skill is a runtime copy that can be replaced whenever the repository is updated.

## Install in Codex

Ask Codex:

> Install the Framewright skill from `https://github.com/jamesltr0701-cell/framewright/tree/main/skill/framewright`

After installation, invoke it explicitly with `$framewright`.

Framewright is configured for explicit invocation and saved prompt-file generation only. After the required profile and stage gates are satisfied, it saves the applicable `.txt` prompt artifacts by default. It does not automatically run ChatCut, OpenMontage, image generation, or video generation.

## Repository policy

This repository intentionally excludes films, image case studies, active projects, generated media, private working files, and third-party tools.

## Versioning policy

Every Framewright patch or feature release preserves the previous version and publishes one matching new version locally and on GitHub:

1. Archive the current authoritative specification as an immutable `framewright-vX.Y.Z.md` snapshot before editing.
2. Increment the canonical specification's YAML `version`.
3. Create the matching new release snapshot.
4. Verify that the desktop canonical file, desktop snapshot, repository reference, and repository snapshot are byte-identical.
5. Commit and push the same version metadata and README version to GitHub.

Existing versioned snapshots are never overwritten or repurposed.

Copyright © 2026 Tairan Li. All rights reserved. No license for reuse or redistribution is granted unless stated separately.
