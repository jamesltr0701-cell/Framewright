---
name: framewright
description: Compile a scene idea, screenplay fragment, or visual brief into a saved production-ready storyboard, keyframe, or video-generation prompt file through Framewright's unified director intake and auteur, apprentice, or screenwriter director modes. Use only when the user explicitly invokes Framewright or asks to apply the Framewright system.
---

# Framewright

Use Framewright as a prompt compiler for AI filmmaking pre-production.

## Required reference

Read `references/framewright.md` completely before producing Framewright output. Treat it as the authoritative specification, including its unified intake, stage routing, director modes, asset handling, continuity rules, and output contracts.

Before any Framewright output, read the `version` value from the reference YAML and state exactly:

`Loaded: Framewright v<version>`

If the version or reference cannot be read, stop and explain the problem instead of using remembered or reconstructed rules.

## Workflow

1. Start each new compilation scope with the Unified Director Intake from the reference.
2. Present a compact understanding and production reading, then ask one consolidated batch of no more than five material questions.
3. If the user delegates judgment, state the assumptions and continue unless an explicit safety, reference-authority, or generation-unit decision is still required.
4. Run exactly one selected stage: Storyboard, Keyframes, or Video Prompt.
5. Save the completed artifact as the required `.txt` file, preserve the user's creative intent, and distinguish locked facts from reasonable interpretation.
6. For a resolved Storyboard stage only, generate exactly one initial storyboard board image from the saved prompt as part of the same stage delivery package.

## Tool boundary

Default to one saved prompt artifact for the active stage. For a requested Framewright compilation, creating and saving the required `.txt` file is part of normal compilation after the intake, stage, reference, and generation-unit boundary gates have been satisfied. The resolved Storyboard stage also includes its one initial board image under the narrow exception below; neither action requires a second authorization.

Do not recreate retired workflow tiers, speed-versus-quality choices, paired-output shortcuts, or an all-output command. Complete one stage at a time and wait for an explicit request before starting another stage.

Do not invoke ChatCut, OpenMontage, video generation, modify non-Framewright files, or use another production tool unless the user explicitly asks for that additional action. The sole default generation exception is the resolved Storyboard stage's one initial board image after `prompt_storyboard.txt` is saved.

Do not automatically retry a failed storyboard generation, regenerate after revising its prompt, create a variant, generate a keyframe image, or generate video. Each of those actions requires fresh explicit authorization. A generated storyboard remains planning-only and must not be attached to a video job unless the user explicitly admits it as a runtime structural reference.

When Keyframes or Video Prompt is active, save the required `.txt` prompt files, return their paths with the compact assistant-facing handoff required by the reference, and stop. When Storyboard is active, return the saved prompt path and its one initial board result. Do not paste complete prompt bodies inline unless the user explicitly requests inline delivery or file writing is unavailable.
