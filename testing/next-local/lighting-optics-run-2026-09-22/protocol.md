# Lighting / optics experiment protocol

Authorized by the director on 2026-09-22: correct the reviewed implementation and generate a few images to test actual behavior. This is skill R&D, not a THE WEAVER production revision or release.

## Before seeing outputs

Two independent compiler runs receive the same raw requests and no answer key, patch description, or prior audit. Control reads the exact `main` skill extracted from `9a7d1fc0c9502321c5354c47b06292e20dfda7d5`; candidate reads this experimental branch after the bounded-light-edit and loading-index corrections. Both carry out actual compilation, saving G1/G2 payloads and B01–B14 responses. Parent compares actual outputs, not merely the presence of rule text. Both compilers may succeed: a change in rule coverage does not necessarily produce measurable improvement on an already capable model.

Generation: four separate text-to-image calls, one per compiler × G1/G2. Use each saved payload verbatim. No positive image references, no project images, no conversation images, no added aesthetic instructions. Same built-in image generation tool for all calls; no implementation-model, seed, quality, or exact-size controls are exposed by this interface. Requested aspect ratios come from the common briefs. Record actual dimensions if available. This is exploratory comparison, not a seed-matched causal A/B or proof of a named API model's behavior. Do not label the built-in route Sunburst, Flare, or Midjourney without returned evidence. Costs are unknown; budget is a finite call count.

Stop the first generation round after four calls regardless of which compiler looks better. If useful for the corrected edit-scope rule, allow at most two additional edits (six total calls): subject-only and whole-scene relighting, each independently from the same immutable generated original. This is a new paired scope test, not a retry until a preferred result appears. No automatic variants or failure-driven spending beyond this cap.

## Evaluation criteria

- G1: bright window with localized edge light; most face/jacket dim but not a featureless silhouette; room/bench recognizable; source direction and subject orientation coherent; waist-up framing; one person; no added lamp, mist, text, or material/structural defect. Brightness judgments are relative visible appearance, not inferred lux or physical exposure stops.
- G2: complete waist-to-head framing; pot modest and lower-left, smaller in image width than the person's shoulder span; near/man/door scales suggest compressed depth; face the clearest plane; pot soft; door still recognizable; no extra people, text, geometry defect or framing loss. Observable relationships do not establish an actual lens or camera distance.
- B cases: make/withhold decisions according to current director locks and actual available facts; hard numeric conflict must be surfaced, invented numeric conflict may be corrected without renewed taste approval; world-side lighting must follow camera orientation; permitted styles survive; reference binding and reported-only evidence are not fabricated; local and whole-scene edits preserve only out-of-scope properties.
- Result labels: pass, partial, fail, uncertain, with concrete visible or textual evidence. Any material protected-property failure overrides attractiveness. Compare same scale; if an image input cannot be viewed, mark it unevaluated.
- Preserve all runs, prompts and unfavorable findings. No claim of general improvement from one image pair. Generating an image does not itself establish compiler improvement; textual decisions and pixels are separate evidence.

## Recovery

`versions/iterations/image-master-lighting-optics-2026-09-22.patch` captures the earlier installed-only image-master additions across three files. Its before state is reconstructed by removing the exact recorded additions from the inspected installed files, not claimed to be a historical repository commit. `git apply --reverse --check` succeeds against the current installed copy; `git apply --check` succeeds against the reconstructed pre-change copy. The patch is archival evidence, not an auto-install instruction. No rollback was applied to the installed skill.
