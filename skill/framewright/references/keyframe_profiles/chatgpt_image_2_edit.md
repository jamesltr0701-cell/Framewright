---
profile_name: "Framewright ChatGPT Image 2 Image Edit Profile"
profile_version: "2.0.0"
target_model: "ChatGPT Image 2"
adapter_id: "chatgpt_image_2_edit"
profile_role: "subordinate_image_edit_adapter"
route: "edit"
artifact_kinds:
  - "shot_plate"
  - "keyframe"
  - "storyboard"
---

# ChatGPT Image 2 Image Edit Profile

## Authority and trigger

Load this profile only when the user explicitly asks to modify a current Shot Plate, Keyframe, or Storyboard, or supplies an equivalent bounded edit instruction. It is the sole registered editor for all three artifact kinds. That instruction authorizes one edit attempt. It does not authorize automatic retries, variants, unrelated redesign, Video generation, or a new master.

Core remains authoritative for identity, composition, Look Development, shot scope, continuity, and all protected properties. This profile owns only the bounded edit request and clean-master attempt contract.

## Immutable original master

At the start of the edit loop, identify the user-uploaded or user-selected clean Shot Plate, Keyframe, or Storyboard that predates Image 2 edits as `original_master`. Preserve it unchanged.

Every attempt must use:

```text
pixel input = original_master
semantic instruction = cumulative active edit specification
output = one disposable candidate
```

Never use a rejected, accepted, or otherwise edited candidate as the next attempt's pixel input. Editing intent may accumulate; edited pixels may not accumulate. Preserve every still-active accepted edit by restating it in the cumulative specification when returning to the original master.

An accepted candidate is a deliverable, not automatically a replacement master. Reset `original_master` only when the user explicitly identifies a named image as the new base. State the reset assistant-facing before editing again. For Storyboard edits, preserve Core's board title, grid, panel geometry, panel count, blank cells, and planning-only authority unless the user's bounded instruction explicitly changes one of those properties.

## Edit instruction

Write one bounded request that distinguishes:

- exact change requested;
- local region, subject, or property affected;
- every protected identity, composition, light, color, texture, object, and background property that must remain unchanged;
- cumulative earlier edits that must still appear;
- forbidden collateral changes.

Do not add generic enhancement, beautification, sharpening, relighting, restyling, or cleanup unless requested. Do not silently regenerate the whole composition to solve a local edit.

## Attempt boundary

Create at most one candidate per explicit user edit instruction. If the candidate fails review, stop. A later correction authorizes one fresh attempt from `original_master` with the revised cumulative specification. Never schedule an automatic retry loop.
