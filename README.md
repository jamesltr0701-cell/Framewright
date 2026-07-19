# Framewright

Framewright is an asset-aware prompt compiler for AI filmmaking. It turns a director's scene intent and production assets into structured storyboard, keyframe, and video-generation prompts.

Current core version: **2.0.0**  
Author: **Tairan Li**

## Repository structure

- [`skill/framewright/`](skill/framewright/) — installable Codex Skill
- [`skill/framewright/references/framewright.md`](skill/framewright/references/framewright.md) — current authoritative Framewright specification
- [`versions/iterations/`](versions/iterations/) — preserved development iterations
- [`versions/beta/`](versions/beta/) — Lite and Pro beta branches
- [`docs/product-vision.md`](docs/product-vision.md) — clean-room product evaluation brief

The GitHub repository is the source of truth. An installed local Skill is a runtime copy that can be replaced whenever the repository is updated.

## Install in Codex

Ask Codex:

> Install the Framewright skill from `https://github.com/jamesltr0701-cell/framewright/tree/main/skill/framewright`

After installation, invoke it explicitly with `$framewright`.

Framewright is configured for explicit invocation and prompt generation only. It does not automatically run ChatCut, OpenMontage, image generation, or video generation.

## Repository policy

This repository intentionally excludes films, image case studies, active projects, generated media, private working files, and third-party tools.

Copyright © 2026 Tairan Li. All rights reserved. No license for reuse or redistribution is granted unless stated separately.
