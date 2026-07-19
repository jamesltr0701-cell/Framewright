---
name: framewright
description: Compile a scene idea, screenplay fragment, or visual brief into production-ready storyboard, keyframe, and video-generation prompts with Framewright's Lite or Pro profiles and auteur, apprentice, or screenwriter director modes. Use only when the user explicitly invokes Framewright or asks to apply the Framewright system.
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
3. Compile only the requested storyboard, keyframe, and/or video prompts in the formats required by the reference.
4. Preserve the user's creative intent and clearly distinguish locked facts from reasonable creative interpretation.

## Tool boundary

Default to prompt generation only. Do not invoke ChatCut, OpenMontage, image generation, video generation, file mutation, or another production tool unless the user explicitly asks for that additional action.

When the user asks only for prompts, return prompts and stop.
