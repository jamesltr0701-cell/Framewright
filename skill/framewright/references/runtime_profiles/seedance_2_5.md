---
profile_name: "Framewright Seedance 2.5 Runtime Profile"
profile_version: "1.2.0"
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

Before admission, serialize the result of the core Reference Conditioning Risk Gate as an assistant-facing strategy, not as a second registry:

```yaml
reference_admission_strategy:
  material_key:
  strategy: attach | crop | beat_limited | text_extraction_only | withhold
  active_scope:
  conditioning_risk:
  practical_loss_if_withheld:
  director_decision_required:
```

The adapter may recommend the narrowest strategy, but it must not silently remove, replace, crop, downgrade, or withhold a director-requested runtime material. Ask for a decision when the recommended strategy changes that explicit request. Keep the risk and operator decision in the Run Card; serialize only the resulting active material role and scope into the clean prompt.

### 4.1 Native Material Mention Serialization

Seedance `@` is a structured material-selection operation, not a stable word stored by Framewright.

Resolve three surface forms from the same Material Registry record:

```yaml
surface_binding:
  ui_mention: operator selects the intended uploaded material through @
  text_surrogate: "@Image 1 | @Video 1 | @Audio 1"
  api_binding: provider asset field or asset ID
```

Rules:

- A UI may display a thumbnail, filename, chip, or index after selection. That display does not define material role or authority.
- A `.txt` file cannot preserve the interactive UI chip. It carries the plain-text surrogate, and the Run Card maps that surrogate to the intended file and stable `material_key`.
- An API binding may use a provider-specific ID outside the prompt text. Preserve the same role and authority semantics.
- Do not assume `@Image 1` remains the same physical asset across runs or upload orders.
- Use the native mention itself as the subject when one subject is clear: `@Image 1 crosses the room and stops at the window.`
- With multiple possible subjects, add only a compact disambiguator: `the woman in @Image 1`, `the red vehicle in @Image 2`, or equivalent.
- Avoid padded forms such as `The character from @Image 1` when the mention is already unambiguous.

When active materials need explicit authority, place one compact model-facing block after the Framewright mode line:

```text
MATERIAL ROLES
@Image 1: subject identity and wardrobe only; do not inherit source pose, crop, camera, or composition.
@Video 1: phase-2 motion timing only; do not inherit identity, environment, or final style.
@Audio 1: voice timbre only; dialogue text, emotion, accent, and pacing remain separately specified.
```

Include only active runtime materials. Every listed mention must be used, every used mention must be listed or unambiguously bound by its task schema, and all text surrogates count against the character limit.

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
MATERIAL ROLES
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
MATERIAL ROLES
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

### 6.1 Serialization Procedure

Serialize in this order:

1. emit exactly one Framewright mode line;
2. emit `MATERIAL ROLES` only when active references need model-facing role or authority limits;
3. emit exactly one selected task schema;
4. use native mentions directly inside the action, edit, endpoint, continuation, dialogue, or sound clauses they control;
5. serialize relevant operator body path separately from lens target, and carry only the approved opening or persistent motion-state constraints needed by this unit;
6. serialize production-critical physical causality through the shortest visible trigger-to-aftermath chain that preserves topology and load state;
7. run core Compactness, Compression Safety, Silent Reference Exclusion, Runtime Cleanliness, and character-limit validation.

Do not print UI setup, upload order, chip-selection instructions, Run Card fields, rejected materials, or operator reminders in the prompt. The Run Card owns file-to-mention mapping; the clean prompt owns only model-facing semantics.

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

## 9. Sound and Visible-Text Policy

When the user has not made an explicit sound request, inherit core Framewright unchanged:

- generate scene-appropriate environmental ambience;
- generate synchronized diegetic, practical, and action sound effects;
- do not generate music.

Only an explicit request activates audio-reference, audio-edit, dialogue, subtitle, ambience, SFX, or music policy for the requested scope. These policies never change director mode, scene grammar, active stage, or generation-unit boundaries.

When explicit sound control is active, resolve one adapter-local policy without changing the core route:

```yaml
seedance_audio_policy:
  scope:
  source_audio_master:
  dialogue: inherit | preserve | generate_locked_text | replace | remove
  ambience: inherit_core_default | preserve | replace | remove
  sfx: inherit_core_default | preserve | generate | replace | remove
  music: no_music | preserve | generate_explicit_request | replace | remove
  audio_reference_authority:
  subtitle_or_visible_text: none | preserve | generate_locked_text | replace | remove
  vocal_events:
    - event_id:
      speaker:
      exact_text:
      language:
      delivery_authority:
      beat:
      allowed_count:
  silent_reaction_beats:
```

Rules:

- Do not activate this policy merely because audio material is attached; the user's requested scope controls it.
- Keep dialogue text, speaker, language, and any locked delivery exact. Timbre authority does not grant new wording, emotion, accent, or pacing.
- Give every approved vocal event one speaker, exact text, language, beat, and allowed count. Use a native mention as speaker only when its identity is unambiguous and actively bound.
- Serialize a silent reaction as nonverbal performance only. Do not add a whisper, repeated name, extra speech, subtitle, or visible text to fill silence.
- Map an admitted audio reference with `@Audio n` only to its allowed properties and active beats.
- In Smart Edit, source-video audio remains part of the sole editing master unless the explicit edit scope says preserve, remove, or replace a named component.
- State the environmental bed once. Keep synchronized action SFX in the beat that visibly causes them.
- Music remains `no_music` unless the user explicitly requests music or an explicit Smart Edit operation preserves / replaces existing music.
- Subtitle or visible-text control uses exact locked text, language, placement purpose, and persistence only when requested. Do not invent subtitles from unstated dialogue.
- Preserve room tone, reverb, noise floor, and action-sound continuity across Extend unless the user explicitly requests an audio change.

Use concise markers only when they improve task execution:

```text
DIALOGUE:
AMBIENCE:
SFX:
MUSIC:
SUBTITLE / VISIBLE TEXT:
```

Omit inactive markers. Never add an empty `MUSIC` block to a default no-music prompt when one compact no-music instruction is sufficient.

## 10. Advanced Task Feasibility

Before serialization, verify route prerequisites and target-surface support:

- Omni Reference has every material required by the selected control profiles.
- Smart Edit has exactly one admitted source-video editing master and a bounded edit scope.
- Long Video remains within the declared 30-second ceiling and its stages do not conceal overloaded cuts, references, dialogue, or state changes.
- First and Last Frames has explicit endpoint assignments and compatible requested aspect / composition logic.
- Extend has an admitted source video and a recoverable actual ending boundary.
- Storyboard control has explicit runtime admission and limited structural authority.
- Every admitted reference passed the core conditioning-risk gate; any strategy that changes a director-requested attachment has explicit approval.
- Audio, dialogue, and subtitle control has an explicit requested scope.
- Explicit vocal control has unique event ownership and silent-reaction boundaries.

If a required material or assignment is missing, ask one compact Intake question. Do not switch routes silently. If the route is valid but execution remains dense, return to the core Generation-Unit Feasibility Gate; never auto-split or auto-merge.

Count the final plain-text prompt, including mode line, material-role declarations, native mention surrogates, dialogue, audio cues, negatives, spaces, and line breaks. UI chip rendering does not excuse an over-limit `.txt` artifact.

## 11. Generation Evidence and Repair

Prompt compilation never starts a generation. When generation is separately authorized and a result exists, extend the core assistant-facing evidence record with:

```yaml
seedance_generation_evidence:
  target_surface:
  profile_version:
  task_route:
  control_profiles:
  surface_binding_map:
  source_master_check:
  duration_and_aspect:
  prompt_fingerprint:
  attempt_index:
  retry_or_credit_cost:
  observed_result:
  primary_failure_layer:
  scene_local_repair:
  evidence_status:
```

Use one primary failure layer:

```text
planning
serialization
rendering
reference_authority
runtime_or_surface
model_behavior
```

Repair the smallest affected scope. Examples: correct one material binding for a reference-authority failure; rewrite one task clause for a serialization failure; revise the Shot / Phase or feasibility plan only for a demonstrated planning failure. Do not use prompt wording to pretend a runtime outage or model limitation is a planning defect.

One successful generation is scene-local evidence, not a global adapter rule. A retry or regeneration requires its own applicable authorization and should record attempt and cost when known.

## 12. Runtime Validation

Before saving, verify:

- exactly one task route and one serialization owner are active;
- director mode, scene grammar, stage, and generation-unit boundaries are unchanged;
- the 30-second ceiling was not used as default duration or feasibility proof;
- the director's route override was honored when valid;
- each active material has limited allowed and denied authority;
- every text surrogate maps to the intended file and stable Material Registry role; UI labels and upload order do not define authority;
- every listed native mention is used and every used mention is mapped;
- unambiguous single-subject mentions are not padded, while ambiguous multi-subject mentions are compactly qualified;
- Smart Edit has exactly one source-video editing master and preserves all unedited content;
- first-frame, last-frame, both-endpoint, and Extend assignments are explicit;
- storyboard material is absent unless explicitly admitted for Video Prompt runtime;
- continuous-take phases remain phases, not cuts;
- relevant operator body path remains distinct from lens target, and opening-only motion constraints are not incorrectly made persistent;
- cross-unit motion continuity inherits only approved Spine state or a director-selected take;
- production-critical physical chains preserve required contact, settling, part provenance, and load state without generic topology blocks;
- inactive materials and UI instructions do not enter the prompt;
- reference conditioning strategy is disclosed assistant-facing, and no director-requested runtime material is silently removed, replaced, cropped, downgraded, or withheld;
- unspecified sound inherits ambience plus synchronized diegetic/action SFX and no music;
- explicit dialogue, audio, music, SFX, and subtitle policies affect only their requested scope;
- each approved vocal event appears only for its speaker, text, beat, and allowed count; silent reactions do not acquire extra speech or visible text;
- the Run Card remains assistant-facing and the clean prompt is saved;
- generation evidence is recorded only after separately authorized generation and does not promote one result into a global rule;
- core timing, sound, continuity, performance, compression, and character-limit checks pass.
