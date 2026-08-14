---
profile_name: "Framewright MiniMax H3 Runtime Profile"
profile_version: "0.1.0-local"
target_model: "MiniMax H3"
profile_role: "subordinate_video_prompt_adapter"
maximum_declared_duration_seconds: 15
prompt_character_limit: 7000
---

# MiniMax H3 Runtime Profile

## Contents

1. Authority and Explicit Load Condition
2. Runtime Routes
3. Capability, Parameters, and Feasibility
4. Input Roles and Material Limits
5. Material Registry Bridge and H3 Labels
6. H3 Serialization Schemas
7. Shots, Camera, Timing, and Dialogue
8. Sound Contract
9. Context-IR Boundary
10. Run Card and Saved Prompt
11. Runtime Validation

## 1. Authority and Explicit Load Condition

Read this file completely only when both conditions are true:

1. the active Framewright stage is `Video Prompt`; and
2. the director explicitly requests MiniMax H3 as the target video model.

Treat an unambiguous explicit name such as `MiniMax H3`, `MiniMax-H3`, or `H3` as a target request. If `H3` could mean something else in context, ask one compact target-model question. Do not infer H3 from supplied media, prompt wording, a project folder, or the presence of this profile. If the director does not explicitly select H3, do not load or apply this profile.

`references/framewright.md` remains the highest authority. This profile may translate an approved Production Spine and Material Registry into H3 input roles, task relationships, prompt fields, and model-facing labels. It must not change:

- explicit director locks;
- AUTEUR, APPRENTICE, or SCREENWRITER mode;
- scene grammar;
- Visual Strategy or committed Shot / Phase Spine;
- continuity, performance, sound, or reference-authority contracts;
- active stage;
- generation-unit count or boundaries.

If this profile conflicts with core Framewright, preserve core and report the adapter conflict assistant-facing.

## 2. Runtime Routes

Resolve exactly one H3 route inside the existing Video Prompt stage:

```yaml
minimax_h3_runtime:
  model: MiniMax-H3
  route: t2va | i2va | fl2va | l2va | ref2va
  reference_task_types:
    - keyframe_completion
    - reference_generation
    - video_editing
    - video_continuation
    - audio_reuse
    - audio_reference
  prompt_enhancement: framewright_compile | context_ir_opt_in
  manual_override:
```

Route by input authority:

- `t2va`: text only; build the complete audiovisual timeline from the approved Spine.
- `i2va`: one explicitly assigned first-frame image; develop forward from that frame.
- `fl2va`: explicitly assigned first- and last-frame images; describe the continuous path between them.
- `l2va`: one explicitly assigned last-frame image; infer a plausible approved opening and converge to that image.
- `ref2va`: admitted images, videos, or audio guide subjects, motion, camera, style, voice, sound, rhythm, editing, or continuation without serving as first/last-frame API roles.

First/last-frame roles and reference roles are mutually exclusive in one H3 request. Never combine `first_frame` or `last_frame` with `reference_image`, `reference_video`, or `reference_audio`. If the director requests an incompatible combination, stop and ask which authority contract should control the generation.

H3 route names are serialization choices, not Framewright stages or director modes. The adapter may recommend a route in the Run Card; a compatible explicit director choice wins.

## 3. Capability, Parameters, and Feasibility

H3 declares a 4-15 second integer duration range. Treat 15 seconds only as a capability ceiling supplied to the core Generation-Unit Feasibility Gate. It is not a default duration or proof that a dense montage is practical.

Resolve target parameters assistant-facing:

```yaml
parameter_contract:
  duration_seconds:
    provenance: user_settable | approved_spine_derived
    resolved_value:
  resolution:
    provenance: user_settable | adapter_default
    resolved_value: 768P | 2K
  aspect_ratio:
    provenance: user_settable | locked_to_endpoint_image | adapter_adaptive
    resolved_value: adaptive | 21:9 | 16:9 | 4:3 | 1:1 | 3:4 | 9:16
```

Rules:

- Duration is required and must be an integer from 4 through 15.
- Resolution is required and must be `768P` or `2K`.
- `t2va` requires one concrete ratio and cannot use `adaptive`.
- `i2va`, `fl2va`, and `l2va` inherit the endpoint image ratio; the API ratio is `adaptive`. For `fl2va`, both endpoint images must have compatible aspect ratios.
- `ref2va` may use a concrete ratio or `adaptive`; if the director has locked a ratio, do not silently replace it with `adaptive`.
- Keep parameter values in the Run Card unless a value also carries executable framing or timing meaning inside the H3 prompt.

Apply the core feasibility gate to cut load, state changes, action, performance, dialogue, references, sound, and continuity. A request for 30 shots in 15 seconds means an average of 0.5 seconds per shot; treat it as a high cut-density risk, not as evidence that H3 will execute exactly 30 distinct readable shots. Never auto-delete shots, auto-split a unit, or fabricate exact beat synchronization. Propose a structural change and stop for director approval when needed.

## 4. Input Roles and Material Limits

The H3 API input is a multimodal `content[]` array. Every request includes one non-empty text item. Bind admitted assets through the route-compatible roles:

```yaml
h3_input_binding:
  material_key:
  media_type: image | video | audio
  api_role: first_frame | last_frame | reference_image | reference_video | reference_audio
  model_labels:
    - <Subject 1>
    - <Picture 1>
    - <Video 1>
    - <Audio 1>
  allowed_authority:
  denied_authority:
  active_shots_or_beats:
```

Hard limits:

- prompt: no more than 7,000 characters;
- endpoint images: at most one first frame and one last frame;
- reference images: at most 9;
- reference videos: at most 3, each 2-15 seconds, combined duration at most 15 seconds;
- reference audio: at most 3, each 2-15 seconds, combined duration at most 15 seconds;
- mixed reference assets: at most 12 total;
- request body: at most 64 MB;
- image: at most 30 MB, width and height each 256-5760 px, aspect ratio 0.4-2.5;
- video: MP4 or MOV, H.264/H.265 video, at most 50 MB, 23.976-60 fps, width and height each 256-5760 px, aspect ratio 0.4-2.5;
- audio: WAV or MP3, at most 15 MB.

Exceeding a hard limit is a validation failure. Never silently remove an explicitly requested material to pass a limit; explain the conflict and ask for a narrower admitted set.

## 5. Material Registry Bridge and H3 Labels

Use the core unified Material Registry as the only source of truth. H3 labels are current-prompt semantic bindings and never replace stable `material_key` identity.

- `<Subject N>` identifies reusable visible content abstracted from one or more sources: a person, object, environment, costume, style, action, expression, pose, or effect.
- `<Picture N>` identifies a concrete image acting as a first frame, last frame, keyframe, edited frame, storyboard anchor, or composition anchor.
- `<Video N>` identifies a whole-video relationship such as editing source, continuation source, camera/cut/rhythm reference, or temporal structure.
- `<Audio N>` identifies a standalone audio signal or an explicitly enabled synchronized audio track used for copying or reference.

One source asset may define several subjects, and one subject may draw different allowed properties from several assets. State each source's limited contribution; do not let appearance authority inherit motion, framing, composition, environment, voice, or editing-master authority.

For `ref2va`, use these relationship markers only within the authority already approved by the Material Registry:

```yaml
visible_relationship: fully_preserved | partially_preserved | attribute_transfer | weak_reference
audio_relationship: fully_copy | partially_copy | reference | weak_reference
```

`fully_preserved` applies to the defined role, not every accidental source property. `fully_copy` means the audio signal itself becomes the target track; `reference` means only named properties such as timbre, rhythm, music style, dialogue content, sound texture, or continuity guide new output.

An ordinary reference video does not automatically activate its audio. Audio reuse or reference requires explicit admission and an `<Audio N>` role. Material order and upload order never define label meaning. The Run Card maps every H3 label to its source file and stable Material Registry role.

## 6. H3 Serialization Schemas

Use exactly one schema as the clean-prompt serialization owner. Write H3 rewrite fields in English while preserving approved dialogue, lyrics, and visible text in their original language.

### 6.1 Base Modes: T2VA, I2VA, FL2VA, L2VA

Use these three fields in this order:

```text
integrated_multimodal_description: [Shot 1] ...
overall_soundscape: ...
non_diegetic_music: N/A
```

For `i2va`, prepend the first-frame alignment instruction. For `fl2va`, prepend the first- and last-frame alignment instruction. For `l2va`, prepend the last-frame alignment instruction. The instruction owns endpoint placement only; it does not grant the endpoint image global authority over unassigned motion, camera, or intermediate states.

`integrated_multimodal_description` carries the timeline's visual style, composition, subjects, environment, actions, reactions, camera, dialogue, singing, and synchronized diegetic sound. `overall_soundscape` summarizes ambience, physical action sounds, and non-verbal human sound without repeating dialogue. `non_diegetic_music` describes audience-only score or uses `N/A` under Framewright's default no-music rule.

### 6.2 Full-Reference Mode: Ref2VA

Use these six sections in this order:

```text
subject_definitions:
summary:
retention_analysis:
detailed_description:
overall_soundscape:
non_diegetic_music:
```

Rules:

- `subject_definitions` defines every H3 label, its sources, reference role, and main properties to follow.
- `summary` begins with the applicable task relationship or combined relationships and gives one short account of the target video.
- `retention_analysis` records where each label applies and its approved visible or audio relationship marker.
- `detailed_description` describes the target video shot by shot in playback order, inserting labels exactly where their authority applies.
- `overall_soundscape` and `non_diegetic_music` follow the same sound ownership rules as the base modes.
- Do not duplicate all registry detail in every section. Repeat only what H3 needs to preserve reference identity and relationships.

## 7. Shots, Camera, Timing, and Dialogue

For H3 multi-shot serialization:

- `[Shot 1]` has no timestamp.
- Each later shot begins with a strictly increasing cut point inside the resolved duration: `[Shot 2] At 00:03.500, the camera cuts to...`.
- A cut must introduce new subject, spatial, state, viewpoint, or temporal information. Prefer camera movement when only distance or a slight angle changes.
- Write camera motion as natural English inside the shot. Distinguish camera-body movement from lens-only movement and add amplitude or speed only when material.
- Keep shot numbering consecutive and make all cut times consistent with the approved rhythm and end state.

These cut points are H3 serialization required by the selected runtime technique. They do not create, delete, or reorder Core shots. If more than one materially different timing allocation is plausible, ask the director rather than silently choosing one. Exact timestamps guide H3 pacing and are not a promise of frame-accurate editing or beat adherence.

When dialogue or singing is explicitly approved:

- assign stable speaker IDs `(S1)`, `(S2)`, and so on in actual vocal-event order;
- write exact content as `<d>[Language] approved text</d>`;
- keep identifying action, delivery, and speaker outside the `<d>` block;
- preserve exact approved words and punctuation; never invent dialogue from an audio reference;
- when an audio asset supplies only timbre, rhythm, emotion, or delivery, do not carry its original words into the target video.

## 8. Sound Contract

Inherit Core Framewright's sound policy. When the director has not explicitly requested music:

```text
overall_soundscape: [scene-appropriate ambience and synchronized practical/action sound]
non_diegetic_music: N/A
```

Do not omit the `non_diegetic_music` field and do not let genre, montage rhythm, dramatic intensity, an audio reference, or an H3 example activate music. Dialogue, narration, singing, copied audio, and visible text remain inactive unless explicitly requested or admitted.

When an audio asset is active, distinguish:

- copied signal from referenced property;
- dialogue/lyrics from timbre or delivery;
- ambience/SFX from audience-only music;
- synchronized source-video audio from an ordinary video attachment.

Put shot-local dialogue and synchronized sound inside the current shot. Put the overall ambience and physical sound summary in `overall_soundscape`. Put only audience-only music in `non_diegetic_music`; use `N/A` when absent.

## 9. Context-IR Boundary

Default to `prompt_enhancement: framewright_compile`. Do not call H3-Context-IR merely because the adapter is active. It is an external asynchronous prompt-enhancement operation, not a required H3 route and not permission to generate video.

Activate `context_ir_opt_in` only after separate explicit authorization. Its returned prompt is a candidate rewrite, not new Production Spine truth. Before adoption, diff it against the Framewright-compiled prompt and report any added or changed:

- shot or cut;
- subject, identity, wardrobe, environment, or action;
- reference relationship;
- dialogue, narration, singing, or visible text;
- ambience, sound effect, audio reuse, or music;
- timing, transition, end state, or continuity fact.

Reject or repair additions that violate director locks, reference authority, feasibility, or Core's default no-music rule. Never silently replace the saved Framewright prompt with Context-IR output.

## 10. Run Card and Saved Prompt

Return this assistant-facing structure:

```text
RUN CARD
MODE: [Framewright director mode]
TARGET / ROUTE: MiniMax H3 / [t2va | i2va | fl2va | l2va | ref2va]
REFERENCE TASK TYPES: [active Ref2VA relationships or none]
DURATION / RESOLUTION / ASPECT RATIO: [resolved values and provenance]
MATERIALS TO UPLOAD: [active runtime materials]
H3 INPUT ROLES: [first/last/reference API roles]
H3 LABEL MAPPING: [label -> file -> limited authority]
PROMPT ENHANCEMENT: [Framewright compile or separately authorized Context-IR]
GENERATION STRATEGY: [concise operator plan]
KNOWN RISKS: [residual risks]
```

Keep the Run Card outside `prompt_video.txt`. Save only the clean model-facing prompt or approved split-unit prompt files. Do not print upload order, API JSON, workflow history, rejected materials, risk commentary, or operator instructions inside the prompt.

Prompt compilation never calls H3, spends credits, or starts video generation.

## 11. Runtime Validation

Before saving, verify:

- H3 was explicitly selected and Video Prompt is the active stage;
- exactly one H3 route and one serialization schema own the prompt;
- Core remains authoritative and director mode, scene grammar, stage, and generation-unit boundaries are unchanged;
- duration, resolution, ratio, prompt length, media counts, durations, formats, dimensions, and request size satisfy H3 limits;
- endpoint roles and reference roles are not mixed;
- every active asset has one route-compatible API role and limited authority;
- every H3 label is defined, consistently mapped, and used only for its approved role;
- `ref2va` relationship markers do not overstate preservation, transfer, copying, or reference authority;
- base modes use the three-field schema in order; `ref2va` uses the six-section schema in order;
- Shot 1 has no timestamp; later shots are consecutive and use increasing in-range cut points;
- H3 timestamps did not alter the approved Core shot structure or become frame-accuracy promises;
- `overall_soundscape` is present and default ambience plus synchronized diegetic/action sound survives compression;
- `non_diegetic_music` is `N/A` unless music is explicitly requested;
- audio/video attachment did not silently activate audio reuse, dialogue, lyrics, voice, or music;
- Context-IR remains inactive unless separately authorized, and any returned rewrite is diff-reviewed before adoption;
- the Run Card remains assistant-facing and only the clean prompt is saved;
- no generation, retry, regeneration, or external credit spend occurred without separate authorization.
