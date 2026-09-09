# Framewright v4.1.2 — GPT Image 2.5 Adapter Promotion Report

Date: 2026-09-09  
Status: promoted stable patch

## Scope

Framewright 4.1.2 replaces every active GPT Image 2 creation and editing route with one GPT Image 2.5 adapter family. Historical release snapshots and iteration records remain immutable and continue to describe the versions they documented.

The director workflow, Production Spine, Shot Spine authority, stage boundaries, Midjourney V8.2 role, Video Prompt adapters, generation permissions, and clean-master editing policy are unchanged.

## Registered image routes

| Artifact | Default create | Explicit alternative create | Edit |
| --- | --- | --- | --- |
| Storyboard | GPT Image 2.5 | none | GPT Image 2.5 |
| Shot Plate | Midjourney V8.2 | GPT Image 2.5 | GPT Image 2.5 |
| Keyframe | Midjourney V8.2 | GPT Image 2.5 | GPT Image 2.5 |

Active image adapter IDs:

- `midjourney_v8_2` / `base_create`
- `gpt_image_2_5` / `base_create`
- `gpt_image_2_5_edit` / `edit`

The former `chatgpt_image_2` and `chatgpt_image_2_edit` IDs are no longer registered and are rejected by regression coverage.

## GPT Image 2.5 implementation choice

The GPT Image 2.5 family contains two official API models. When the active surface exposes an implementation-model selector:

- `gpt-image-2.5-sunburst` — Framewright default for fidelity-sensitive creation and precision editing;
- `gpt-image-2.5-flare` — available only after an explicit speed-priority instruction.

Flare is not a second workflow or a second adapter. When a ChatGPT or Codex surface exposes only ChatGPT Images 2.5, the Run Card records it as surface-managed and does not falsely attribute the result to either API model. The implementation choice may not change Core authority, reference roles, clean prompt content, or attempt authorization.

## Prompt and edit alignment

The new profiles align to the official GPT Image 2.5 guidance by:

- organizing complex visual instructions through clear, maintainable sections;
- describing visible subject, action or frozen pose, composition, style, light, material, and constraints concretely;
- assigning an explicit purpose and allowed authority to every image input;
- separating the requested edit from the properties that must remain unchanged;
- keeping exact required text quoted, placed, and checked for extra or illegible text;
- recording quality, size, background, output format, and selected implementation model as Run Card parameters instead of contaminating clean prompt prose.

Framewright deliberately retains its stricter immutable-original-master loop even though GPT Image 2.5 supports multi-turn editing. Every attempt returns to the clean original master with the cumulative active semantic edit specification, preventing candidate-on-candidate pixel drift.

## Verification

- Core and adapter bundle validation: PASS
- Regression suite: 128 / 128 matched expectations
- Image route smoke checks: PASS
- Codex Skill validator: PASS
- Legacy GPT Image 2 adapter rejection fixture: PASS
- Hero banner version render: visually verified at 2048 × 768

## Official sources

- <https://openai.com/index/introducing-chatgpt-images-2-5/>
- <https://developers.openai.com/api/docs/guides/image-prompting>
- <https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst>
- <https://developers.openai.com/api/docs/models/gpt-image-2.5-flare>
