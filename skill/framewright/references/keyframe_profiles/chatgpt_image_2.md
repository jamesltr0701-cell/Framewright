---
profile_name: "Framewright ChatGPT Image 2 Image Base-Create Profile"
profile_version: "1.0.0"
target_model: "ChatGPT Image 2"
model_id: "gpt-image-2"
adapter_id: "chatgpt_image_2"
profile_role: "subordinate_image_prompt_adapter"
route: "base_create"
artifact_kinds:
  - "shot_plate"
  - "keyframe"
  - "storyboard"
---

# ChatGPT Image 2 Image Base-Create Profile

## Authority and load condition

Load this profile by default when creating a Storyboard. Load it for a new Shot Plate or Keyframe only when the director explicitly selects ChatGPT Image 2. Do not infer that selection from uploaded images, the active platform, an available tool, or the existence of the edit profile.

Core remains authoritative for scene intent, Look Development, committed shot or panel scope, artifact function, continuity, identity, geography, reference authority, and candidate status. This profile owns only Image 2 base-create serialization, model-facing image-slot role statements, and the assistant-facing Run Card.

The resolved Storyboard stage retains Core's narrow authorization for one initial board generation. Shot Plate and Keyframe prompt compilation does not authorize generation; after explicit authorization, one attempt produces one Candidate and then stops.

## Base-create contract

Create a new composition from the approved Core contract. Never require or invent an `original_master`; that concept belongs only to the edit route.

For a Shot Plate or Keyframe, serialize one independently executable frozen-image prompt per approved artifact. For a Storyboard, preserve Core's exact board title, grid, panel count, panel geometry, blank cells, panel evidence, asset bindings, monochrome planning style, and one-board boundary. Express aspect ratio in natural model-facing language. Do not add Midjourney flags or invent unsupported controls.

## Generation references and source-role ledger

Use only admitted generation references. Every admitted image keeps one stable Material Registry ID and one property-level authority role in the assistant-facing source-role ledger. Use the narrowest useful set, resolve conflicting roles before compilation, and withhold sources likely to control forbidden properties.

The Run Card maps stable references to current files and invocation slots such as `Image 1`. Clean prompt text may use those slot labels only as direct model-facing bindings and must state allowed and denied authority in plain language. Slot order is an execution binding, not semantic authority.

If the active surface cannot preserve the resolved reference roles, stop before generation. Do not silently drop, merge, reorder, or substitute references.

## Candidate and attempt boundary

Every output begins as `candidate_only`. A generated image does not become a continuity master, Accepted asset, or later-generation source merely because it exists. Only an explicit director decision may promote a named Candidate.

One authorized generation instruction permits at most one Candidate. Do not schedule automatic retry, variant, edit, upscale, or promotion.

## Clean artifact and Run Card

The saved `.txt` contains only the model-facing image instruction and direct image-slot role statements. Keep adapter ID, artifact kind, route, stable reference IDs, local paths, authority, slot mapping, surface setup, authorization, output count, candidate status, and provenance in the assistant-facing Run Card.

Current official references:

- <https://help.openai.com/en/articles/11084440-chatgpt-images>
- <https://developers.openai.com/api/docs/models/gpt-image-2>
- <https://developers.openai.com/api/docs/guides/image-generation>
