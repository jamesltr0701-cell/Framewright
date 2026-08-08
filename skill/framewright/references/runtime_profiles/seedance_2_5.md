---
profile_name: "Framewright Seedance 2.5 Runtime Profile"
profile_version: "1.0.0"
target_model: "Seedance 2.5"
profile_role: "subordinate_video_prompt_adapter"
maximum_declared_duration_seconds: 30
---

# Seedance 2.5 Runtime Profile

## 1. Authority and Load Condition

Read this file completely only when the active Framewright stage is `Video Prompt` and the target model is Seedance 2.5.

`references/framewright.md` remains the highest authority. This profile may translate an approved Framewright Production Spine and Material Registry into a Seedance 2.5 task route, execution schema, and model-facing prompt. It must not change:

- explicit director locks;
- AUTEUR, APPRENTICE, or SCREENWRITER mode;
- scene grammar;
- Visual Strategy or committed Shot / Phase Spine;
- Storyboard Panel Evidence Plan;
- continuity, performance, sound, or reference-authority contracts;
- active stage;
- generation-unit count or boundaries.

If this profile conflicts with core Framewright, preserve core and report the adapter conflict assistant-facing.

## 2. Runtime Profile

Resolve one task route inside the existing Video Prompt stage:

```yaml
seedance_runtime:
  model: seedance_2_5
  ui_mode: omni_reference | smart_edit | long_video | first_last_frames | extend
  control_profiles:
    - multi_reference
    - multi_keyframe
    - storyboard
    - blockout_coarse
    - blockout_fine
    - seamless_transition
    - marked_edit
    - dialogue_control
    - audio_reference
    - audio_edit
    - subtitle_control
  generation_strategy:
  manual_override:
```

Director mode and `ui_mode` are independent. A task route is model execution syntax, not a new Framewright stage or scene grammar.

The router may recommend one route and explain the reason in the Run Card. The director may override the recommendation when the requested route is compatible with the supplied materials and target surface. If an override would violate a core lock or lacks required material, ask one compact material question.

## 3. Capability and Feasibility

Seedance 2.5 declares a maximum duration capability of 30 seconds. Treat this only as a ceiling supplied to Framewright's Generation-Unit Feasibility Gate.

Never infer that:

- 30 seconds is the default duration;
- every scene up to 30 seconds is feasible;
- longer capability makes dense action, many cuts, many references, dialogue, or state transitions reliable;
- one unit should be merged to fill the ceiling;
- a unit should split merely because another duration might be easier.

Use the core gate to assess practical action load, cut resets, state progression, performance, reference complexity, dialogue, sound, and continuity. Any split or merge still requires a natural boundary and explicit director approval.

## 4. Material Registry Bridge

Use the core unified Material Registry as the only source of truth. Each active runtime material resolves:

```yaml
runtime_material:
  material_key:
  media_type: image | video | audio
  native_ref:
  role:
  master_status:
  allowed_authority:
  denied_authority:
  active_stages_or_beats:
  planning_or_runtime_status:
```

Rules:

- Attachment never grants full authority.
- Identity authority does not silently grant source pose, camera, crop, framing, or composition.
- Motion authority does not silently grant identity, environment, final style, or edit-master status.
- Audio timbre authority does not silently grant dialogue text, emotion, accent, pacing, ambience, or music.
- Authority may be local to one shot, phase, or beat.
- Inactive, withheld, planning-only, rejected, and text-extraction-only materials obey core Silent Reference Exclusion.
- Native references are surface bindings for the current run; they do not replace stable core material identity.

## 5. Task Router

### 5.1 Omni Reference

Use when the task builds a new video from text plus one or more admitted image, video, or audio references and no existing video is the sole editing master.

Common control profiles include `multi_reference`, `multi_keyframe`, `storyboard`, `blockout_coarse`, `blockout_fine`, `dialogue_control`, and `audio_reference`.

### 5.2 Smart Edit

Use when the user wants to change an existing source video while preserving content outside the authorized edit scope.

The source video is the sole editing master. Unless explicitly authorized, preserve its motion, timing, occlusion, event order, environment, identity, camera, and audio. Other materials may guide only the named replacement or edit property.

### 5.3 Long Video

Use when the target surface exposes the long-video route and the approved unit benefits from semantic stages within the 30-second ceiling.

Each stage has one principal state change, a visible entry state, a visible end state, and local reference / dialogue / sound authority. Stages do not create new Framewright generation units and do not bypass the core feasibility gate.

### 5.4 First and Last Frames

Use when the user explicitly assigns first-frame material, last-frame material, or both endpoints.

Endpoint authority controls the assigned boundary only. Resolve the middle motion and state change independently while preserving aspect and composition compatibility. Neither endpoint silently controls every intermediate pose, motion, camera path, or object state.

### 5.5 Extend

Use when an existing source video should continue from its actual ending boundary.

Recover the source ending's composition, identity and pose, object and damage state, motion direction and momentum, camera-subject relationship, lighting and environment, room tone, reverb, noise floor, and action-sound continuity. Extend begins at that boundary and does not treat a merely similar still image as the source ending.

### 5.6 Distinct Boundary Contracts

Core `First-Frame Continuation`, Seedance `First and Last Frames`, and Seedance `Extend` are distinct:

- First-Frame Continuation uses a prior final frame as the next unit's opening anchor for the same shot.
- First and Last Frames uses explicitly assigned endpoint materials for one generation.
- Extend continues from an admitted source video's actual ending state.

Obey the user's explicit assignment. If supplied material could plausibly serve more than one contract and the user is unclear, return to the Intake Hard Stop and ask before freezing the Spine.

## 6. Base Task Schemas

Use exactly one task schema as the serialization owner. Do not combine it with core fallback headings.

### Omni Reference

```text
GENERATION GOAL
MATERIAL-TO-ROLE MAP
ALLOWED / DENIED AUTHORITY
SHOT OR PHASE PROGRESSION
CONTINUITY + END STATE
AUDIO
NEGATIVE
```

### Smart Edit

```text
EDIT GOAL
SOURCE VIDEO ROLE
TARGET MATERIAL ROLE
EDIT SCOPE
CONTENT TO PRESERVE
AUDIO EDIT POLICY
```

### Long Video

```text
GENERATION GOAL
MATERIAL-TO-ROLE MAP
STAGE PLAN
CONTINUITY + END STATE
AUDIO
NEGATIVE
```

### First and Last Frames

```text
FIRST-FRAME AUTHORITY
LAST-FRAME AUTHORITY
MIDDLE MOTION + STATE CHANGE
CONTINUITY + END STATE
AUDIO
NEGATIVE
```

### Extend

```text
SOURCE END BOUNDARY
CONTINUATION ACTION
CAMERA + MOTION CONTINUITY
OBJECT + ENVIRONMENT CONTINUITY
AUDIO CONTINUITY
END STATE
NEGATIVE
```

Omit a heading when it adds no executable value, except Smart Edit must retain explicit edit scope and content-to-preserve language.

## 7. Storyboard Runtime Admission

A generated storyboard is planning-only by default. Storyboard generation does not activate `storyboard` control.

Only explicit user admission during Video Prompt routing may choose one of:

- full board;
- selected panel crops;
- selected structural panels;
- multi-keyframes derived from approved panels;
- no storyboard attachment.

Record whether each admitted panel maps to a shot or a phase. Grant only the named structural authority and deny board title, labels, line style, sheet geometry, panel borders, final color, final lighting, final material, and final texture. Panels representing a continuous take never imply cuts, and panel count never becomes video beat count automatically.

## 8. Run Card and Saved Prompt

Return this structure assistant-facing:

```text
RUN CARD
MODE: [Framewright director mode]
TASK / UI MODE: [resolved Seedance route]
CONTROL PROFILES: [active profiles]
DURATION / ASPECT RATIO: [resolved values]
MATERIALS TO UPLOAD: [active runtime materials]
REFERENCE MAPPING: [material role and limited authority]
GENERATION STRATEGY: [concise operator plan]
KNOWN RISKS: [residual risks]
```

The Run Card is an extension of the core assistant-facing handoff. Do not save `run_card.md` by default.

Save only the clean model-facing `prompt_video.txt` or approved split-unit prompt files. The saved prompt must not contain UI instructions, upload procedure, risk commentary, approval status, rejected materials, workflow explanation, or the Run Card itself.

## 9. Sound Boundary

When the user has not made an explicit sound request, inherit core Framewright unchanged:

- generate scene-appropriate environmental ambience;
- generate synchronized diegetic, practical, and action sound effects;
- do not generate music.

Only an explicit request activates audio-reference, audio-edit, dialogue, subtitle, ambience, SFX, or music policy for the requested scope. These policies never change director mode, scene grammar, active stage, or generation-unit boundaries.

## 10. Runtime Validation

Before saving, verify:

- exactly one task route and one serialization owner are active;
- director mode, scene grammar, stage, and generation-unit boundaries are unchanged;
- the 30-second ceiling was not used as default duration or feasibility proof;
- the director's route override was honored when valid;
- each active material has limited allowed and denied authority;
- Smart Edit has exactly one source-video editing master and preserves all unedited content;
- first-frame, last-frame, both-endpoint, and Extend assignments are explicit;
- storyboard material is absent unless explicitly admitted for Video Prompt runtime;
- continuous-take phases remain phases, not cuts;
- inactive materials and UI instructions do not enter the prompt;
- the Run Card remains assistant-facing and the clean prompt is saved;
- core timing, sound, continuity, performance, compression, and character-limit checks pass.
