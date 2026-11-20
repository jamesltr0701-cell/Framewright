---
profile_name: "Framewright Kling 4.0 Runtime Profile"
profile_version: "0.1.1"
target_model: "Kling 4.0"
profile_role: "subordinate_video_prompt_adapter"
maximum_declared_duration_seconds: 30
prompt_token_limit: 8000
overflow_language_strategy: "lossless_zh_payload"
verified_surface: "Kling official web creation workspace"
source_checked: "2026-10-22"
---

# Kling 4.0

## Ownership and scope

Load this complete adapter only for an explicit Kling 4.0 / 可灵4.0 Video Prompt target. Resolve `target_model: kling_4_0`, `adapter_id: kling_4_0`, and `serialization_owner: framewright_adapter_kling_4_0`. An unspecified “Kling” needs version clarification if the conversation has not already selected 4.0. **Flash is not an alias for this target.**

Core retains director intent, mode, stage, approved Prompt IR, generation boundaries, performance, sound, and reference authority. This adapter translates those decisions into Kling-facing text and upload bindings. Do not import Seedance punctuation, H3 field schemas, or another prompt skill. Do not redesign the scene because Kling can expand simple prompts or automatically choose cuts.

This adapter is distributed with Framewright v4.2.3. It describes the official web workflow; it does not supply an API model ID, request schema, provider availability, account entitlement, or generation authorization. Compile text without spending generation credits. Recheck the selected surface when an operator reports a different limit.

## Entry selection

Use one entry per generation:

| Entry | Use | Binding rule |
|---|---|---|
| `omni_reference` | Text-only generation, reference-guided generation, or editing an admitted video | Keep each asset's appearance, geometry, action, camera, voice, or edit authority explicit. An edit identifies exactly one primary video. |
| `keyframes` | Approved first, last, or intermediate visual states placed on a timeline | Uploaded inputs are image keyframes only. Preserve their assigned times and the process between them. |

Do not combine the two entries' upload controls. Omni text may describe an image as the intended opening or ending; that remains reference guidance, not proof that a dedicated timeline keyframe slot has been bound. If precise keyframe placement and an independent voice/video reference cannot coexist in the selected entry, expose that specific conflict before compiling; do not silently discard either requirement. A reference card's pose never becomes an endpoint merely because it was uploaded first.

## Verified limits

These are launch-document limits, not recommended shot density or defaults for the director's scene.

| Item | Standard 4.0 |
|---|---|
| Duration | Integer 3–30 seconds |
| Resolution | 720p, 1080p, 4K |
| Omni aspect | 21:9, 16:9, 1:1, 9:16, Auto |
| Keyframes aspect | Follows the first uploaded keyframe; with no images, choose a listed concrete ratio |
| Prompt | 8,000 **tokens**, not characters |
| Images | ≤10; each ≤30 MB; ratio 2:5–5:2 |
| Video pool | ≤5 clips, ≤30 seconds combined; reference/edit clips each 3–30 seconds, ≤300 MB, ratio 2:5–5:2 |
| Elements | ≤7, including ≤3 video elements; video-element source 3–8 seconds |
| Voice profiles | ≤3; creation audio 5–30 seconds, ≤50 MB |
| Combined Omni inputs | ≤15 images, videos, elements and voice profiles |

Reference videos, primary edit video, and video elements consume the **same** video pool. Count uploaded inputs, not every textual mention. A video element counts once toward the combined total, once toward the element subtotal, and once toward the video pool. Unmeasured size/duration is unknown, not zero; verify required media properties before declaring an upload feasible.

Flash has different launch limits (20 seconds, 720p, no start/end or multiple-keyframe control). It remains unregistered in this adapter. Extension and HDR availability are not treated as established capabilities: the guide contains “coming soon” wording, including an HDR/table inconsistency. Never promise them from a marketing heading or silently switch to Flash.

## Material and voice binding

Keep stable Material Registry IDs internally. Map admitted inputs to the **actual current upload mentions**, such as `@Image1`, `@Video1`, or the UI's element/voice-profile mention. Upload order can change these mentions. A prose asset name or fabricated `@Audio1` is not evidence of a selected voice profile.

For every used source, preserve its allowed authority and exclusions: a character card may own identity without owning pose, lighting, layout, or shot design; a motion reference may own movement without owning the performer. Keep exclusions concise, adjacent to the relevant role.

Imported audio is a **voice-profile source**, not a general music, sound-effect, dialogue-waveform, or exact timing reference. Bind each approved speaker to the selected voice profile and keep the director's words, delivery, visible/offscreen placement, and counts. With no admitted voice profile, use the approved textual voice description without claiming a cloned voice. Do not turn an unavailable audio-reuse request into a voice-cloning request.

## Serialization

Write clear prose in the language resolved by Core §8.7. Use compact sections only when useful to express source roles, shared conditions, shot or phase progression, sound, and final state. Keep platform settings, ownership fields, and compiler rationale in the Run Card.

- Give each active mention its job. Reuse identities and objects across cuts without restating a character biography in every shot.
- Preserve the approved shot count, cut order, action triggers, local performance changes, and end state. A continuous shot explicitly remains uninterrupted; describe changes as phases, not numbered shots. Kling's automatic storyboarding is not permission to add cuts, and no separate “disable Smart Storyboard” switch is assumed.
- Keep physical movement and camera response distinct. A quick pan stays inside its shot when directed; a source-approved cut remains a cut. Timestamps express approved timing, not guaranteed frame accuracy. Do not invent durations to make an infeasible sequence appear resolved.
- For Keyframes, name each assigned visual state and time, then describe the transition to the next. Do not merely list images, collapse a process into a morph, or inherit an endpoint's pose at the start. Preserve incoming motion and any intended editorial omission.
- For editing, identify the primary video, the exact requested changes, and the aspects that must remain. Supplementary videos retain their narrow reference role. Do not imply that general edit support guarantees pixel-perfect preservation.
- Put dialogue in ordinary quotation marks with the speaker, language, delivery, and on/offscreen relationship. Preserve protected literals and authorized vocal events exactly. Do not apply Seedance braces or angle-bracket sound tags as required Kling syntax.
- Prefer concrete positive descriptions; retain necessary director prohibitions. A concise-expression recommendation never deletes strict silence, no-cut, passive-body, or identity locks. State music and subtitle intent explicitly where resolved, since leaving them open can allow additions. Native audiovisual generation does not authorize extra speech, vocal reactions, music, or subtitles.

If over budget, compact the prose in the selected language. Reserialize in Chinese only when the director allows that fallback under Core §8.7. Preserve dialogue, asset mentions, order, and meaning. Recount using the surface's token counter if available. Mark an unmeasured Kling token count as unverified. If the prompt still exceeds budget, return the material tradeoff to the director.

## Run Card and validation

Report the selected entry/task, intended duration/resolution/aspect and their provenance, actual upload-to-material mapping, voice-profile binding, keyframe placements or primary edit video, and any unresolved surface limit. Never treat a successful text check as evidence that uploads exist or video quality is established.

Carry this adapter's qualification inside the existing temporary current-scope compile trace, alongside Core's normal performance/source evidence when applicable. Do not create a second persistent production state. Example **qualification only**, not an approved scene or a complete trace:

```yaml
kling40:
  explicit_target_selection: true
  entry: omni_reference       # or keyframes
  task: generate              # or edit; edit uses Omni
  duration_seconds: 12
  resolution: 1080p
  aspect_ratio: "9:16"        # keyframes with images: inherited
  input_bindings: []          # text-only; replace with admitted inputs
  # prompt_token_count:      # optional, only a trusted Kling count
```

Each binding contains `material_key`, `kind` (`image`, `video`, `image_element`, `video_element`, `voice_profile`), `role` (`reference`, `edit_base`, `voice`, `first_frame`, `middle_frame`, `last_frame`), `native_mention`, `allowed_authority`, and `denied_authority`. Include measured `duration_seconds`, `size_mb`, and `aspect_ratio` when applicable. A binding's media `aspect_ratio` is a numeric width/height ratio (e.g. `0.5625` for 9:16); the output setting above is a string such as `"9:16"` or `"inherited"`. Dedicated image-keyframe bindings include `time_seconds`; first/last are at zero/output duration. Do not assume element internals are separate uploads. A voice profile already created in Kling does not require re-uploading its creation audio.

Validate the exact saved text with `video-prompt`, `--target-model kling_4_0 --serialization-owner framewright_adapter_kling_4_0 --adapter-id kling_4_0 --profile-contract kling_4_0 --trace <current-trace>`, plus the compiler sources actually used and `--source-review` when Core requires it. The command requires the matching Kling qualification, checks declared entry/role compatibility, pool counts, duration, measured media limits, and supplied token count. An unknown token count or unmeasured media attribute remains a Run Card limitation; PASS does not certify it. Optional `--character-limit` is an operator's additional text budget, never Kling's token limit.

## Sources and unresolved points

Verified 2026-10-22 against Kling's [4.0 User Guide](https://kling.ai/quickstart/kling-4-model-user-guide) (dated 2026-10-14), especially §§1.2, 2.1–2.2, 3.1–3.2 and FAQ; [official tutorial index](https://kling.ai/quickstart) confirms the model-specific guide. No third-party prompt pack is a compiler dependency.

The guide includes an example with video references under the Keyframes chapter despite its explicit images-only entry rule. Follow the entry's stated input contract; do not infer a mixed-upload exception from the example. Exact voice-profile mention spelling, account rollout, provider/API mappings, extension and HDR require surface-specific confirmation. These uncertainties do not block ordinary Standard 4.0 prompt compilation for the verified entries.
