# Framewright v4.1.0 Unified Lightweight Local Implementation Report

Date: 2026-09-05  
Status: isolated local candidate; not promoted  
Implementation branch: `codex/framewright-unified-local`  
Prepared craft baseline: `4ca9e27854ccd8be30536bb832f1184395f52dd8`

## Scope implemented

This candidate keeps Framewright as one product with one explicit `$framewright` entry. It does not add Public/James variants, a personal Profile, a clip/movie router, a new director mode, a new output stage, or another canonical state system.

The implementation adds:

1. integrated, on-demand Framewright-owned craft references for camera/action, identity/material, light/sound, and diagnosis/repair;
2. scoped authoritative-source loading and same-context reuse, with restoration after compaction, version, scope, stage, target, or source conflict;
3. one persistence owner per active production scope, using a reliable host-project authority when available and a lightweight `framewright_state.yaml` fallback only at durable checkpoints;
4. an Approved Compile Boundary so a clear approval compiles the current Spine directly and asks only about a real blocker;
5. clearer generation routing after the Committed Shot Spine: one continuous shot, one multi-shot edited sequence generated as a unit, or one active shot at a time;
6. sequence-versus-shot asset allocation, including suppression of duplicated authority already carried by an active Keyframe;
7. explicit allowance for generated material to supply a segment, a complete edit shot, or multiple edit positions without creating another timeline or registry;
8. the retained assistant-facing delivery package: short shot/revision summary, prompt link, applicable settings, prompt-marker-to-asset responsibility mapping, and a small watch list.
9. retained MJ Plate exploration: an approved Plate may carry composition, light, atmosphere, space, or visual-relationship authority directly into the selected video strategy without mandatory Keyframe regeneration.

## Preserved boundaries

- Core remains the sole owner of director intent, Production Spine, Shot Spine, continuity, reference authority, generation-unit boundaries, and active stage.
- Exactly one registered target adapter owns each Video Prompt serialization.
- All tasks still pass through intake and a current Shot Spine before generation strategy is resolved.
- Storyboard, Keyframes, and Video Prompt remain separate stages.
- Storyboard is planning-only until separately admitted for Video Prompt runtime.
- Keyframes default to Midjourney V7; ChatGPT Image 2 edits keep the immutable clean-master contract.
- Default sound remains environmental ambience plus synchronized diegetic/action effects, without music unless explicitly requested.
- No external generation, credit spend, automatic retry, ChatCut action, or OpenMontage action was performed.

## State simplification

The fallback state schema retains its existing accepted-artifact and continuity safeguards but makes inactive historical/continuity groups conditional. Ordinary candidates and rejected drafts remain recoverable through their files and version history without creating global checkpoints. Only accepted or promoted artifacts, selected takes, cross-task/cross-unit continuity, material authority changes, high-risk conflicts, or explicit requests cause durable state work.

## Validation changes

- Core version validation now reads the candidate version from the protected-anchor manifest instead of hard-coding `4.0.0`.
- Prompt IR schema `1.1` now carries generation strategy, active shot scope, reference allocation, and an optional intended editorial-use relationship.
- Generation-strategy validation rejects neighboring-shot action leakage, edited-sequence/one-take conflation, duplicated Keyframe/reference authority, and unsupported editorial-use values.
- A lightweight fallback-state fixture proves that inactive history and continuation groups are not mandatory.

## Verification

- Shared YAML runtime preflight: PyYAML `6.0.3` PASS.
- Framewright Core and adapter validation: PASS.
- Regression suite: `124/124` fixtures matched expectations.
- Bundled ownership-aware Seedance 2.0 prompt validation: PASS.
- Bundled Midjourney V7 Keyframe prompt validation: PASS.
- Skill Creator `quick_validate.py`: PASS.
- Core and `versions/releases/framewright-v4.1.0.md` byte identity: PASS.
- Current Core SHA-256: `12e2622ab445f4b7853221eabb551ae4be5f7857d9ceaf9a73f5dc11313083d1`.

## Deliberately not performed

- no modification of `/Users/jameslee/Documents/AI Filmmaking Studio/framewright`;
- no modification of the Desktop Framewright mirror;
- no global Skill installation change;
- no removal of the external Seedance 2.0 Skill;
- no GitHub push, release promotion, or release tag update;
- no modification or promotion of the separate Midjourney V8.2 and ChatGPT Image 2 base-create candidates.

Those actions require a separate release decision after the local candidate is reviewed.
