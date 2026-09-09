---
profile_name: "Framewright GPT Image 2.5 Image Edit Profile"
profile_version: "3.0.0"
target_model: "GPT Image 2.5"
default_model_id: "gpt-image-2.5-sunburst"
speed_model_id: "gpt-image-2.5-flare"
adapter_id: "gpt_image_2_5_edit"
profile_role: "subordinate_image_edit_adapter"
route: "edit"
artifact_kinds:
  - "shot_plate"
  - "keyframe"
  - "storyboard"
---

# GPT Image 2.5 Image Edit Profile

## Authority and trigger

Load this profile only when the user explicitly asks to modify a current Shot Plate, Keyframe, or Storyboard, or supplies an equivalent bounded edit instruction. It is the sole registered editor for all three artifact kinds. That instruction authorizes one edit attempt. It does not authorize automatic retries, variants, unrelated redesign, Video generation, or a new master.

Core remains authoritative for identity, composition, Look Development, shot scope, continuity, and all protected properties. This profile owns only the bounded edit request and clean-master attempt contract.

When the active surface exposes an implementation-model selector, use `gpt-image-2.5-sunburst` by default because Framewright editing is fidelity-sensitive and depends on precise preservation. Use `gpt-image-2.5-flare` only after an explicit speed-priority instruction and only when the surface exposes that choice. If the active ChatGPT or Codex surface exposes only ChatGPT Images 2.5, record `surface_managed_chatgpt_images_2_5` in the Run Card and do not claim that it used Sunburst or Flare. Never let the implementation choice change the approved edit scope or authorize extra attempts.

## Immutable original master

At the start of the edit loop, identify the user-uploaded or user-selected clean Shot Plate, Keyframe, or Storyboard that predates GPT Image 2.5 edits as `original_master`. Preserve it unchanged.

Every attempt must use:

```text
pixel input = original_master
semantic instruction = cumulative active edit specification
output = one disposable candidate
```

Never use a rejected, accepted, or otherwise edited candidate as the next attempt's pixel input. Editing intent may accumulate; edited pixels may not accumulate. Preserve every still-active accepted edit by restating it in the cumulative specification when returning to the original master.

GPT Image 2.5 supports multi-turn editing, but Framewright intentionally keeps this stricter clean-master rule to prevent cumulative pixel drift. An accepted candidate is a deliverable, not automatically a replacement master. Reset `original_master` only when the user explicitly identifies a named image as the new base. State the reset assistant-facing before editing again. For Storyboard edits, preserve Core's board title, grid, panel geometry, panel count, blank cells, and planning-only authority unless the user's bounded instruction explicitly changes one of those properties.

## Edit instruction

Write one bounded request that distinguishes:

- the exact change requested;
- the local region, subject, or property affected;
- every protected identity, composition, light, color, texture, object, text, and background property that must remain unchanged;
- cumulative earlier edits that must still appear;
- forbidden collateral changes.

Use direct language such as `change only [X]` and restate every preservation constraint that matters. Identify each input by number and purpose when multiple references are present. Do not add generic enhancement, beautification, sharpening, relighting, restyling, or cleanup unless requested. Do not silently regenerate the whole composition to solve a local edit. If a region must remain pixel-identical, stop and recommend compositing instead of claiming prompt-only editing can guarantee that result.

## Attempt boundary

Create at most one candidate per explicit user edit instruction. If the candidate fails review, stop. A later correction authorizes one fresh attempt from `original_master` with the revised cumulative specification. Never schedule an automatic retry loop.

## Clean artifact and Run Card

The saved `.txt` contains only the bounded model-facing edit instruction and direct image-slot role statements. Keep adapter ID, artifact kind, route, chosen GPT Image 2.5 implementation model, quality, dimensions, original-master identity, cumulative edit specification, protected properties, slot mapping, authorization, candidate status, and provenance in the assistant-facing Run Card.

Current official references:

- <https://openai.com/index/introducing-chatgpt-images-2-5/>
- <https://developers.openai.com/api/docs/guides/image-prompting>
- <https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst>
- <https://developers.openai.com/api/docs/models/gpt-image-2.5-flare>
