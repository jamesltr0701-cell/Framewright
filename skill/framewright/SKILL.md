---
name: framewright
description: Compile a scene idea, screenplay fragment, or visual brief into saved production-ready storyboard, keyframe, and video-generation prompt files with Framewright's Lite or Pro profiles and auteur, apprentice, or screenwriter director modes. Use only when the user explicitly invokes Framewright or asks to apply the Framewright system.
---

# Framewright

Use Framewright as a prompt compiler for AI filmmaking pre-production.

## Required reference

Read `references/framewright.md` completely before producing Framewright output. Treat it as the authoritative specification, including its profile gates, director modes, asset handling, continuity rules, and output contracts.

Before any Framewright output, read the `version` value from the reference YAML and state exactly:

`Loaded: Framewright v<version>`

If the version or reference cannot be read, stop and explain the problem instead of using remembered or reconstructed rules.

## Workflow

1. Identify the requested Framewright profile, director mode, scene grammar, available assets, and desired outputs.
2. If a required choice or asset is missing, follow the intake and gating rules in the reference instead of silently inventing production facts.
3. Compile only the requested storyboard, keyframe, and/or video prompts, then save the completed outputs as `.txt` files using the filenames and paths required by the reference.
4. Preserve the user's creative intent and clearly distinguish locked facts from reasonable creative interpretation.

## Tool boundary

Default to prompt-artifact generation only. For a requested Framewright compilation, creating and saving Framewright's required `.txt` prompt outputs is part of normal compilation after the operating-profile gate and any applicable Pro stage or generation-unit boundary gate have been satisfied. It does not require a second file-creation authorization.

Do not invoke ChatCut, OpenMontage, image generation, video generation, modify non-Framewright files, or use another production tool unless the user explicitly asks for that additional action.

When the user asks only for prompts, save the required `.txt` prompt files, return their paths with the compact assistant-facing handoff required by the reference, and stop. Do not paste complete prompt bodies inline unless the user explicitly requests inline delivery or file writing is unavailable.
