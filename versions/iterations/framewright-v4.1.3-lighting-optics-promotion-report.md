# Framewright v4.1.3 — Lighting and Optics Promotion

Date: 2026-09-22. Base release: v4.1.2. This is a narrow maintenance release of the previously isolated `codex/lighting-optics-iteration` candidate. The director workflow, stage boundaries, image/video routes, and generation permissions are unchanged.

## Changes

- Core adds conditional lighting and optical-geometry consistency checks for Shot Plates and Keyframes, with reference-authority and post-generation protection checks. It does not create another state file or require a questionnaire for every shot.
- Camera/motion and light/sound craft references expose the relevant still-image checks. Midjourney V8.2 and GPT Image 2.5 image adapters serialize approved relationships without becoming new directing authorities.
- GPT Image 2.5 editing protects only properties outside the authorized edit scope: local subject relighting may hold the room, while an authorized whole-scene relight may change the room. The immutable-original-master rule remains.
- Current release metadata, validator wording, provenance wording, and the GitHub homepage banner are aligned with v4.1.3. Older immutable release snapshots are preserved.

## Evidence and limits

- The [candidate report](framewright-lighting-optics-local-candidate-2026-09-22.md) records the source changes and initial offline cases.
- [Independent compile and image-trial results](../../testing/next-local/lighting-optics-run-2026-09-22/RESULTS.md) include two separately loaded compiler contexts, 14 behavior checks, and six image outputs. Both versions handled the tested core judgments. The revised candidate gave a more explicit account of some lighting/geometry relationships, but this sample does **not** establish a general improvement in visual success rate.
- The actual image trials were exploratory: backlight was only partially satisfied in both versions; scale/focus was observably acceptable in both; one local and one whole-scene edit visually respected their distinct scopes. There was no controlled multi-seed or complex-reference-stack study. The test images remain local, gitignored media; their prompts, manifests, and hashes are recorded in the linked results.
- Release checks: 128/128 regression fixtures matched expectations; Video/Keyframe/Storyboard smoke prompts passed; Skill validator passed; `git diff --check` passed; Core and v4.1.3 immutable snapshot were byte-identical. These checks establish structural consistency, not universal model compliance.

The separately installed `image-master` maintenance changes are archived as a recoverable patch in `image-master-lighting-optics-2026-09-22.patch`. That patch is not a second Framewright compiler and is not silently installed by this release.
