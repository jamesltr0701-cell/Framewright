---
name: framewright
description: Preserve cinematic intent while compiling a scene idea, screenplay fragment, or visual brief into a saved production-ready storyboard, keyframe, or video-generation prompt file. Use when the user explicitly invokes the framewright Skill or explicitly asks to apply Framewright.
---

# Framewright

Use Framewright as a director-steered, intent-preserving cinematic compiler whose primary executable output is a prompt artifact for AI filmmaking pre-production.

## Required reference

Read `references/framewright.md` completely before producing Framewright output. Treat it as the authoritative specification, including its unified intake, stage routing, director modes, asset handling, continuity rules, and output contracts.

For Video Prompt, first compile the approved Production Spine into the model-neutral Prompt IR defined by the authoritative reference. Then read `references/runtime_profiles/adapter_registry.yaml`, resolve exactly one registered target-model / serialization-owner pair, and read exactly that model's subordinate runtime profile completely before feasibility qualification or serialization:

- Seedance 2.0: `references/runtime_profiles/seedance_2_0.md`
- Seedance 2.5: `references/runtime_profiles/seedance_2_5.md`
- MiniMax H3: `references/runtime_profiles/minimax_h3.md`

Do not infer a target model from supplied media, prompt style, platform, provider, surface, or profile availability. Target model—not platform—selects the dialect. Load exactly one adapter profile for exactly one target. If the requested target is unsupported or ambiguous, ask one compact target-model question. An adapter may qualify feasibility and serialize the approved Prompt IR, but it may not reinterpret creative intent, modify the IR, or override the authoritative reference, director locks, state, stage, or compiler ownership.

For Keyframes, read `references/keyframe_profiles/adapter_registry.yaml`, resolve the default `midjourney_v7` target unless the director explicitly selects another registered image target, and read only its profile completely. Core owns the frozen instant, Keyframe role, shot scope, look contract, continuity, and reference authority; the profile owns Midjourney prompt syntax and parameters. When the user explicitly asks to modify a current Keyframe, also read `references/keyframe_profiles/chatgpt_image_2_edit.md` and apply its clean-master editing contract. Do not load either image profile for Storyboard or ordinary Video Prompt work.

Framewright is the exclusive compiler whenever the user explicitly invokes Framewright. Do not treat another installed model-prompt skill as an implicit compiler source and do not merge its rules into the active Framewright compile. A separately requested comparison may remain outside the clean artifact and must not change the active serialization owner.

Before any Framewright output, read the `version` value from the reference YAML and state exactly:

`Loaded: Framewright v<version>`

If the version or reference cannot be read, stop and explain the problem instead of using remembered or reconstructed rules.

Preserve the exact version value. Do not silently substitute a remembered, local-experimental, or older release.

## Workflow

1. Start each new compilation scope with the Unified Director Intake from the reference.
2. Present a compact understanding and production reading. Use the reference's Framewright-owned Intake Presentation Layer only to adapt language and proposal timing; it never selects Director Mode, state, questions, stage, target, or compiler ownership. Apply the relevant content review lens, classify material gaps, and schedule questions by dependency: ask only the highest-impact question when its answer can change later questions; combine only genuinely independent questions, with five retained as the maximum batch size.
3. Select exactly one Director Mode and state it explicitly to the user before compilation. Keep that mode in internal compile state, but never serialize its literal label into a clean model-facing Prompt.
4. After each dependent answer, update the Production Spine's nested Intent Ledger and recalculate the question queue. Protect intentional freedom, omit low-impact decoration, and stop when remaining gaps cannot materially change a downstream contract.
5. When the reference's conditional state trigger is active, read or update the project-local `framewright_state.yaml` before compilation. Reconcile it with the latest explicit user decision and active artifacts; never treat it as a second Production Spine or target-model input.
6. Treat requested advice or delegated judgment as a named, current-scope authority grant. Record material assumptions and continue only within that grant unless an explicit safety, reference-authority, generation-unit, stage, or feasibility decision still requires the user.
7. Before Video Prompt, resolve the current generation unit's Storyboard Preflight decision. After the Committed Shot Spine is current, resolve one generation strategy: one continuous shot, one edited multi-shot sequence, or one active shot at a time.
8. Run exactly one selected stage: Storyboard, Keyframes, or Video Prompt.
9. For Video Prompt, build and validate one approved model-neutral Prompt IR, resolve `target_model`, scalar `serialization_owner`, adapter contract, and compiler instruction sources from the registry, then let the selected adapter serialize that IR. Validate the actual `.txt` artifact with the bundled ownership-aware `video-prompt` command. For Keyframes, compile only the allowed generation-strategy scope and validate it with the registered image adapter contract. For Storyboard, run the applicable generic deterministic validator. In every stage, run Semantic Preflight, preserve the user's creative intent, and distinguish locked facts, approved decisions, reasonable execution inference, and intentional freedom.
10. Return the compact assistant-facing Intent Delta required by the reference, outside the clean prompt and without creating a second default artifact.
11. For a resolved Storyboard stage only, generate exactly one initial storyboard board image from the saved prompt as part of the same stage delivery package.

## Tool boundary

Default to one saved prompt artifact for the active stage. A conditionally triggered `framewright_state.yaml` is a project control file, not a second prompt artifact. For a requested Framewright compilation, creating or updating those authorized files is part of normal compilation after the intake, stage, reference, and generation-unit boundary gates have been satisfied. The resolved Storyboard stage also includes its one initial board image under the narrow exception below; none of these actions requires a second file-creation authorization.

Do not recreate retired workflow tiers, speed-versus-quality choices, paired-output shortcuts, or an all-output command. Complete one stage at a time and wait for an explicit request before starting another stage.

Do not invoke ChatCut, OpenMontage, video generation, modify non-Framewright files, or use another production tool unless the user explicitly asks for that additional action. The sole default generation exception is the resolved Storyboard stage's one initial board image after `prompt_storyboard.txt` is saved.

Do not automatically retry a failed storyboard generation, regenerate after revising its prompt, create a variant, generate a keyframe image, or generate video. Each of those actions requires fresh explicit authorization. A generated storyboard remains planning-only and must not be attached to a video job unless the user explicitly admits it as a runtime structural reference.

When Keyframes or Video Prompt is active, save the required `.txt` prompt files, return their paths with the compact assistant-facing handoff required by the reference, and stop. When Storyboard is active, return the saved prompt path and its one initial board result. Do not paste complete prompt bodies inline unless the user explicitly requests inline delivery or file writing is unavailable.
