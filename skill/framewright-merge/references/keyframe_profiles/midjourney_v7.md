---
profile_name: "Framewright Midjourney V7 Keyframe Profile"
profile_version: "1.0.0"
target_model: "Midjourney V7"
adapter_id: "midjourney_v7"
profile_role: "subordinate_keyframe_prompt_adapter"
---

# Midjourney V7 Keyframe Profile

## Authority and load condition

Load this profile only when Keyframes is the active stage and the director has not selected a different registered image target. The Core reference remains authoritative for scene intent, Look Development, committed shot scope, Keyframe role, frozen instant, continuity, reference authority, and generation strategy. This profile owns only Midjourney V7 prompt serialization and the assistant-facing parameter handoff.

Midjourney generation consumes GPU time and is not authorized by Keyframe prompt compilation alone. Save the prompt and stop unless the user explicitly requests image generation.

## Default output

Serialize one independently copyable block per approved Core Keyframe. Describe a frozen image in this order when relevant:

1. subject, count, identity-relevant visible features, and current state;
2. pose, contact, gaze, and one frozen action instant;
3. framing, camera position, lens geometry, depth, and composition;
4. environment, geography, and continuity-critical objects;
5. motivated light, color discipline, materials, atmosphere, texture, and finish;
6. narrow exclusions that prevent a likely production failure.

Do not write video timing, dialogue delivery, camera paths, `then`, `continues`, or multi-beat motion into a still-image prompt. Translate movement intent into one legible pose, balance state, directional cue, or environmental response.

Append `--v 7`. Resolve `--ar` from the intended video frame when known. Do not invent personalization IDs, style-reference codes, URLs, seeds, or parameter values that the user has not supplied or approved.

## Omni Reference

Use Omni Reference only when one admitted image has a necessary character, object, vehicle, or creature identity role. Midjourney V7 accepts one Omni Reference image. In the saved text prompt, use an assistant-facing placeholder only when the user still needs to paste the real URL; never claim that a local filename is an executable `--oref` URL.

Keep the text prompt complete: Omni Reference does not replace scene, composition, or look description. `--ow` defaults to `100`; remain below `400` unless the director has a specific reason to trade flexibility for stronger reference influence. A Style Reference, moodboard, or personalization profile may coexist only when its role is explicit and it does not silently overwrite the Core Look Development Contract.

Omni Reference is identity/form conditioning, not pose, crop, camera, or composition authority unless those properties are separately admitted by Core. Do not use it when no reference role is active.

## Clean artifact and handoff

The `.txt` block contains only the Midjourney-ready visual prompt and resolved executable parameters. Keep the Keyframe role, supported shot ID, reference mapping, missing URL reminder, and downstream status in the assistant-facing handoff.

Current official references:

- <https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference>
- <https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference>
- <https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version>
