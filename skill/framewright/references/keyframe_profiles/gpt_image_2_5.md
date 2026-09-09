---
profile_name: "Framewright GPT Image 2.5 Image Base-Create Profile"
profile_version: "2.0.0"
target_model: "GPT Image 2.5"
default_model_id: "gpt-image-2.5-sunburst"
speed_model_id: "gpt-image-2.5-flare"
adapter_id: "gpt_image_2_5"
profile_role: "subordinate_image_prompt_adapter"
route: "base_create"
artifact_kinds:
  - "shot_plate"
  - "keyframe"
  - "storyboard"
---

# GPT Image 2.5 Image Base-Create Profile

## Authority and load condition

Load this profile by default when creating a Storyboard. Load it for a new Shot Plate or Keyframe only when the director explicitly selects GPT Image 2.5. Do not infer that selection from uploaded images, the active platform, an available tool, or the existence of the edit profile.

Core remains authoritative for scene intent, Look Development, committed shot or panel scope, artifact function, continuity, identity, geography, reference authority, and candidate status. This profile owns only GPT Image 2.5 base-create serialization, model-facing image-slot role statements, and the assistant-facing Run Card.

The resolved Storyboard stage retains Core's narrow authorization for one initial board generation. Shot Plate and Keyframe prompt compilation does not authorize generation; after explicit authorization, one attempt produces one Candidate and then stops.

## Model selection inside the adapter family

When the active surface exposes an implementation-model selector, use `gpt-image-2.5-sunburst` by default. Framewright Shot Plates, Keyframes, Storyboards, and reference-led production assets are fidelity-sensitive workloads, and Sunburst is the quality-priority GPT Image 2.5 model.

Use `gpt-image-2.5-flare` only when the user explicitly prioritizes speed, rapid iteration, or high-volume generation over the Sunburst quality default and the surface exposes that choice. If the active ChatGPT or Codex surface exposes only ChatGPT Images 2.5, record `surface_managed_chatgpt_images_2_5` in the Run Card and do not claim that it used Sunburst or Flare. This choice changes only the implementation model recorded in the Run Card; it does not create a second workflow, change Core, loosen reference authority, authorize extra attempts, or alter the clean prompt contract.

Set `quality`, `size`, `background`, and output format as Run Card parameters rather than prompt prose when the active surface exposes them. Begin with an explicit quality setting appropriate to the asset and change only one parameter at a time. Use `xhigh` or `max` only when a lower setting fails an approved quality requirement. Preserve the intended aspect ratio; if exact custom dimensions are used, keep each edge at or below 3840 pixels, both edges divisible by 16, the long-to-short ratio at or below 3:1, and total pixels between 655,360 and 8,294,400.

## Base-create contract

Create a new composition from the approved Core contract. Never require or invent an `original_master`; that concept belongs only to the edit route.

For a Shot Plate or Keyframe, serialize one independently executable frozen-image prompt per approved artifact. For a Storyboard, preserve Core's exact board title, grid, panel count, panel geometry, blank cells, panel evidence, asset bindings, monochrome planning style, and one-board boundary. Express aspect ratio in natural model-facing language. Do not add Midjourney flags or invent unsupported controls.

Organize complex prompts through readable labeled sections when useful. Define the intended result, subject, composition, visible action or frozen pose, style, light, material, and constraints concretely. For people, specify body framing, relative scale, gaze, contact, and object interaction. Put any exact required text in quotation marks, define its placement, forbid extra text, and verify legibility after generation.

## Generation references and source-role ledger

Use only admitted generation references. Every admitted image keeps one stable Material Registry ID and one property-level authority role in the assistant-facing source-role ledger. Use the narrowest useful set, resolve conflicting roles before compilation, and withhold sources likely to control forbidden properties.

The Run Card maps stable references to current files and invocation slots such as `Image 1`. Clean prompt text may use those slot labels only as direct model-facing bindings. Identify every reference by number and purpose, then state its allowed and denied authority in plain language. Slot order is an execution binding, not semantic authority.

If the active surface cannot preserve the resolved reference roles, stop before generation. Do not silently drop, merge, reorder, or substitute references.

## Candidate and attempt boundary

Every output begins as `candidate_only`. A generated image does not become a continuity master, Accepted asset, or later-generation source merely because it exists. Only an explicit director decision may promote a named Candidate.

One authorized generation instruction permits at most one Candidate. Do not schedule automatic retry, variant, edit, upscale, or promotion.

## Clean artifact and Run Card

The saved `.txt` contains only the model-facing image instruction and direct image-slot role statements. Keep adapter ID, artifact kind, route, chosen GPT Image 2.5 implementation model, quality, dimensions, background, stable reference IDs, local paths, authority, slot mapping, surface setup, authorization, output count, candidate status, and provenance in the assistant-facing Run Card.

Current official references:

- <https://openai.com/index/introducing-chatgpt-images-2-5/>
- <https://developers.openai.com/api/docs/guides/image-prompting>
- <https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst>
- <https://developers.openai.com/api/docs/models/gpt-image-2.5-flare>
