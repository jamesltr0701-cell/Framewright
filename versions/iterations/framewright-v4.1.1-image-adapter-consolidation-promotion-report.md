# Framewright v4.1.1 Image Adapter Consolidation and Promotion Report

Date: 2026-09-05

## Outcome

Framewright 4.1.1 promotes the prepared 4.1 lightweight/craft release line while replacing the prior image-routing candidates with one deliberately narrow two-tool architecture.

Active image routes:

| Artifact | Default creator | Explicit alternative creator | Editor |
|---|---|---|---|
| Shot Plate | Midjourney V8.2 | ChatGPT Image 2 | ChatGPT Image 2 |
| Keyframe | Midjourney V8.2 | ChatGPT Image 2 | ChatGPT Image 2 |
| Storyboard | ChatGPT Image 2 | none | ChatGPT Image 2 |

Only three image adapters are registered:

- `midjourney_v8_2` / `base_create`
- `chatgpt_image_2` / `base_create`
- `chatgpt_image_2_edit` / `edit`

Midjourney V7 and the candidate Midjourney V8.2 Edit Model adapter are intentionally absent from the active package. Framewright may still help the director reason about an edit performed manually on the Midjourney website, but that activity has no dedicated Framewright adapter.

## Preserved boundaries

- Shot Plate remains an optional artifact inside the existing Keyframes/material workflow, not a fourth stage.
- Storyboard remains the only stage whose resolved initial delivery includes one image-generation attempt.
- Shot Plate and Keyframe compilation remain prompt-only unless the user separately authorizes generation.
- All Image 2 edits use the immutable original master plus a cumulative semantic edit specification; edited candidates are never stacked as new pixel inputs.
- A generated image begins as a Candidate and gains stronger authority only through an explicit director decision.
- The Shot Spine, Production Spine, generation strategy, and Video Prompt adapter ownership rules are unchanged.

## Validation

- Full Framewright regression: 127/127 fixtures matched expectations.
- Skill package validation: PASS.
- Core and `versions/releases/framewright-v4.1.1.md` are required to remain byte-identical.
- Negative route checks confirm that Midjourney V7, Midjourney `--edit`, and Midjourney Storyboard routing are rejected.

## Official capability check

The implementation was checked against current official product documentation on 2026-09-05:

- Midjourney identifies V8.2 as its current default image model and documents `--v 8.2` selection.
- Midjourney Image Prompts are a creation-reference mechanism rather than instructions for changing an existing image.
- ChatGPT Images supports both creating new images and editing uploaded or generated images.

These product capabilities do not override Framewright's narrower product decision: the Midjourney Edit Model is intentionally not registered, and Image 2 owns every Framewright image-edit route.
