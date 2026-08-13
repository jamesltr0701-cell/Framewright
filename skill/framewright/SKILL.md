---
name: framewright
description: Preserve cinematic intent while compiling a scene idea, screenplay fragment, or visual brief into a saved production-ready storyboard, keyframe, or video-generation prompt file through Framewright's adaptive director intake and auteur, apprentice, or screenwriter director modes. Use only when the user explicitly invokes Framewright or asks to apply the Framewright system.
---

# Framewright

Use Framewright as a director-steered, intent-preserving cinematic compiler whose primary executable output is a prompt artifact for AI filmmaking pre-production.

## Required reference

Read `references/framewright.md` completely before producing Framewright output. Treat it as the authoritative specification, including its unified intake, stage routing, director modes, asset handling, continuity rules, and output contracts.

When and only when the active stage is Video Prompt and the target model is Seedance 2.5, also read `references/runtime_profiles/seedance_2_5.md` completely before routing or serialization. Treat it as a subordinate adapter: it may translate core contracts into target-specific task schemas, but it may not override the authoritative reference or director locks.

Before any Framewright output, read the `version` value from the reference YAML and state exactly:

`Loaded: Framewright v<version>`

If the version or reference cannot be read, stop and explain the problem instead of using remembered or reconstructed rules.

Preserve the exact version suffix. When the reference reports a local experimental candidate, load and identify that candidate exactly; do not relabel it as a stable release or silently substitute its stable fallback.

## Workflow

1. Start each new compilation scope with the Unified Director Intake from the reference.
2. Present a compact understanding and production reading, classify material gaps, and schedule questions by dependency: ask only the highest-impact question when its answer can change later questions; combine only genuinely independent questions, with five retained as the maximum batch size.
3. After each dependent answer, update the Production Spine's nested Intent Ledger and recalculate the question queue. Protect intentional freedom, omit low-impact decoration, and stop when remaining gaps cannot materially change a downstream contract.
4. When the reference's conditional state trigger is active, read or update the project-local `framewright_state.yaml` before compilation. Reconcile it with the latest explicit user decision and active artifacts; never treat it as a second Production Spine or target-model input.
5. Treat requested advice or delegated judgment as a named, current-scope authority grant. Record material assumptions and continue only within that grant unless an explicit safety, reference-authority, generation-unit, stage, or feasibility decision still requires the user.
6. Run exactly one selected stage: Storyboard, Keyframes, or Video Prompt.
7. Save the completed artifact as the required `.txt` file, run the bundled deterministic validator and Semantic Preflight, preserve the user's creative intent, and distinguish locked facts, approved decisions, reasonable execution inference, and intentional freedom.
8. Return the compact assistant-facing Intent Delta required by the reference, outside the clean prompt and without creating a second default artifact.
9. For a resolved Storyboard stage only, generate exactly one initial storyboard board image from the saved prompt as part of the same stage delivery package.

## Tool boundary

Default to one saved prompt artifact for the active stage. A conditionally triggered `framewright_state.yaml` is a project control file, not a second prompt artifact. For a requested Framewright compilation, creating or updating those authorized files is part of normal compilation after the intake, stage, reference, and generation-unit boundary gates have been satisfied. The resolved Storyboard stage also includes its one initial board image under the narrow exception below; none of these actions requires a second file-creation authorization.

Do not recreate retired workflow tiers, speed-versus-quality choices, paired-output shortcuts, or an all-output command. Complete one stage at a time and wait for an explicit request before starting another stage.

Do not invoke ChatCut, OpenMontage, video generation, modify non-Framewright files, or use another production tool unless the user explicitly asks for that additional action. The sole default generation exception is the resolved Storyboard stage's one initial board image after `prompt_storyboard.txt` is saved.

Do not automatically retry a failed storyboard generation, regenerate after revising its prompt, create a variant, generate a keyframe image, or generate video. Each of those actions requires fresh explicit authorization. A generated storyboard remains planning-only and must not be attached to a video job unless the user explicitly admits it as a runtime structural reference.

When Keyframes or Video Prompt is active, save the required `.txt` prompt files, return their paths with the compact assistant-facing handoff required by the reference, and stop. When Storyboard is active, return the saved prompt path and its one initial board result. Do not paste complete prompt bodies inline unless the user explicitly requests inline delivery or file writing is unavailable.
