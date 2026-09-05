---
profile_name: "Framewright Midjourney V8.2 Image Base-Create Profile"
profile_version: "1.0.0"
target_model: "Midjourney V8.2"
adapter_id: "midjourney_v8_2"
profile_role: "subordinate_image_prompt_adapter"
route: "base_create"
artifact_kinds:
  - "shot_plate"
  - "keyframe"
---

# Midjourney V8.2 Image Base-Create Profile

## Authority and load condition

Load this profile only to create a new Shot Plate or Keyframe. It is the default creator for both artifact kinds. Do not use it for Storyboard creation or any image edit, and do not infer a separate Midjourney Edit Model route.

Core remains authoritative for scene intent, Look Development, committed shot scope, image function, frozen instant, continuity, and reference authority. This profile owns only Midjourney V8.2 base-create serialization and the assistant-facing Run Card.

Prompt compilation does not authorize Midjourney generation. Save and validate the prompt, return its Run Card separately, and stop unless the user explicitly requests generation.

## Base-create output

Serialize one independently copyable block per approved Shot Plate or Keyframe. For a Keyframe, describe exactly one frozen production instant. For a Shot Plate, describe one exploratory composition, lighting, atmosphere, spatial-depth, or visual-relationship proposition without silently promoting it to a first frame or continuity master.

Order the visible instruction when relevant as:

1. artifact job and supported shot;
2. subject, count, identity-relevant features, and current state;
3. pose, contact, gaze, and one frozen action instant;
4. framing, camera position, lens geometry, depth, and composition;
5. environment, geography, and continuity-critical objects;
6. motivated light, color discipline, materials, atmosphere, texture, and finish;
7. narrow exclusions that prevent a likely production failure.

Append `--v 8.2`. Resolve `--ar` from the intended video frame when known. Do not add `--edit`. Do not write video timing, dialogue delivery, camera paths, `then`, `continues`, or multi-beat motion into a still-image prompt.

## Image Prompt and Style Reference

V8.2 base creation may use admitted Image Prompts and Style References when Core grants a clear property-level authority role.

- Image Prompts may influence content, composition, and color only within their admitted authority. Use `--iw` only when the user supplies or approves the weight.
- Style References may carry visual style properties such as color, medium, texture, or lighting. Use `--sref` and `--sw` only with supplied or approved references and weights.
- Keep reference ID, input type, property-level authority, current binding, and missing-URL reminders in the Run Card. A local filename is not an executable URL.
- Reject V7-only `--oref`, `--ow`, `--cref`, and `--cw`; never translate or silently drop them.

## Clean artifact and handoff

The saved `.txt` contains only the executable visual prompt, admitted executable reference syntax, and resolved parameters. Keep adapter ID, artifact kind, route, reference authority mapping, platform setup, generation authorization, and provenance in the assistant-facing Run Card.

Current official references:

- <https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version>
- <https://docs.midjourney.com/hc/en-us/articles/32040250122381-Image-Prompts>
- <https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference>
