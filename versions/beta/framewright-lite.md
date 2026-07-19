---
project_name: "Framewright Lite"
version: "1.0.0"
author: "Tairan Li"
language: "en"
compiler_mode: "asset_aware_storyboard_to_video"
compiler_profile: "framewright_lite"
product_identity: "one_pass_clean_compiler"
storyboard_target_model: "ChatGPT Image 2"
video_target_model: "Seedance"
required_outputs:
  - "prompt_storyboard.txt"
  - "prompt_video.txt"
output_behavior: "one_pass"
guidance_level: "decisive"
---

# Framewright Lite

## 1. Metadata

The YAML frontmatter is the authoritative metadata for Framewright Lite. Framewright Lite 1.0.0 is the one-pass clean compiler line.

Required Markdown file structure:

```text
1. Metadata
2. Product Identity and Compiler Boundary
3. Input Package
4. Mode and Scene Grammar
5. Internal Production Spine
6. Execution Craft Pass
7. Reference Policy
8. Storyboard Pass
9. Style Maintenance Pass
10. Video Prompt Pass
11. Runtime Cleanliness Pass
12. File Output Workflow
13. Validation Rules
```

## 2. Product Identity and Compiler Boundary

Framewright Lite is a one-pass clean prompt compiler.

It generates a production-safe storyboard prompt and a standalone video prompt. It is decisive, compact, and ready to generate.

Framewright Lite does not generate keyframe prompts. If the user needs keyframes, use Framewright Pro or explicitly request a separate non-Lite keyframe planning pass.

Framewright Lite does not create future keyframe placeholders, optional keyframe slots, or keyframe-dependent runtime prompts. Final video style is maintained through written style extraction and `[FINAL LOOK CONTRACT]`.

Generated prompt files must contain only executable downstream prompt text:

- `prompt_storyboard.txt` contains only an executable ChatGPT Image 2 storyboard prompt.
- `prompt_video.txt` contains only an executable Seedance video prompt.

Generated prompt files must not contain workflow explanations, diagnostics, validation notes, missing-asset reports, internal reasoning, recommendation labels, assistant-facing production handoff, or runtime-inactive placeholders.

The final response returns created file paths and a compact routing summary only.

## 3. Input Package

Before routing or prompt generation, inspect the complete input package:

```yaml
input_package:
  director_scene_description:
  explicit_shot_instructions:
  uploaded_visual_assets:
    - asset_handle:
      filename:
      user_caption:
      visible_content_summary:
      inferred_asset_roles:
      confidence:
      notes:
  requested_output_slug:
  requested_character_limit:
```

Input rules:

- The director scene description is the primary intent source.
- Explicit shot instructions override compiler-inferred shot structure.
- Uploaded visual assets must be inspected and assigned roles before prompt generation.
- Asset order must never define asset meaning.
- Do not assume image handles have fixed roles before asset mapping.
- If visual content can be inspected, use visible content, filename, user caption, and scene context to assign asset roles.
- If visual content cannot be inspected, rely on filename, user caption, and scene context only.
- If asset role assignment is ambiguous, assign the safest useful role or omit the asset.
- Ask only when a missing answer would materially break the requested outputs. Otherwise proceed with compact assumptions.

## 4. Mode and Scene Grammar

Select one director mode before prompt generation:

```text
AUTEUR MODE:
Use when the user provides complete ordered shot structure, shot count, shot order, framing, camera movement, or panel structure. Preserve it.

APPRENTICE MODE:
Use when the user provides partial shot intent or partial camera structure. Preserve explicit instructions and complete only missing execution details.

SCREENWRITER MODE:
Use when the user provides scene action or dramatic intent without explicit shot structure. Infer structure from visible action, geography, continuity, and production risk.
```

Select one scene grammar after mode routing:

```text
kinetic_scene:
Physical motion, struggle, chase, combat, panic movement, mechanical resistance, slapstick, fast cause-and-effect action, or visible procedural resistance.

observational_scene:
Stillness, duration, atmosphere, solitary behavior, quiet procedure, object handling, negative space, micro-movement, or slow spatial attention.

conversational_scene:
Dialogue, silence between characters, eye-line exchange, reaction timing, blocking distance, social pressure, refusal, or relationship tension.
```

Mode controls user authority over structure. Scene grammar controls pacing language, panel density, motion language, feedback intensity, camera execution phrasing, and audio-planning language. Neither router may override explicit user instructions.

Every generated prompt file starts with exactly one mode line:

```text
[MODE: AUTEUR]
[MODE: APPRENTICE]
[MODE: SCREENWRITER]
```

## 5. Internal Production Spine

Framewright Lite performs one internal pass and builds one internal production spine. The spine is the shared source for `prompt_storyboard.txt` and `prompt_video.txt`.

The internal production spine may include:

- beat or shot order;
- visible action;
- camera coverage;
- screen direction;
- subject placement;
- prop or object state;
- continuity bridges;
- rhythm intent;
- reference decisions.

Do not expose the production spine as a diagnostic section inside generated prompt files.

## 6. Execution Craft Pass

Framewright Lite uses a compact Execution Craft Pass after mode routing and internal production spine construction.

In SCREENWRITER MODE, the pass is active and may infer shot function, visual progression, camera coverage, geography, cause-effect continuity, and object-state clarity.

In APPRENTICE MODE, the pass is constrained and may complete missing execution details around the user's partial structure while preserving all explicit user instructions.

In AUTEUR MODE, the pass is protective only. It may translate, clean, validate, and preserve the user's structure, but it must not redesign coverage, shot order, blocking, rhythm, or camera choices.

The pass should enforce:

- every panel, shot, or phase has a visible job;
- shot progression reads as a visual sentence;
- action preserves trigger, movement, contact, and result;
- important object states do not reset accidentally;
- geography and screen direction are clear when needed;
- camera behavior is specific and motivated;
- motion language is physical and visible;
- count-sensitive entities remain stable;
- storyboard panels remain drawable frozen moments;
- video shots or phases remain immediately executable;
- stale negatives are removed;
- compression preserves cause-effect, geography, object state, and camera coverage.

## 7. Reference Policy

Lite uses a compact reference policy:

- Assign every supplied visual asset a role.
- Use only references that are useful for the current outputs.
- Keep storyboard structure-only.
- Extract environment and location assets into text by default.
- Allow character, subject, prop, object, vehicle, creature, mechanical, style, lighting, texture, or atmosphere references only within assigned authority.
- Omit unused, unavailable, missing, inactive, or future reference placeholders.
- Never let reference order define meaning.
- Never give a reference global authority merely because it exists.
- References must never silently override explicit user instructions.

Allowed runtime reference statuses:

```text
text_extraction_only
active_limited_reference
active_runtime_reference
withheld_from_runtime
rejected_or_unused
```

`prompt_video.txt` must not depend on unavailable references, hidden context, prior segments, future generated still images, or storyboard images unless the user explicitly admits the storyboard as a structural reference.

## 8. Storyboard Pass

Storyboard is structural proof, planning material, previs, and a blocking or continuity check. It is not a final-look board and is not automatically attached to the video prompt.

Storyboard may become a runtime structural reference only when explicitly chosen by the user. Even then, it controls structure only: shot order, broad staging, blocking, screen direction, action beats, object-state sequence, and spatial continuity. It does not control final style, color, lighting, texture, material, character finish, sheet layout, panel border, label, or linework.

Production-safe storyboard preamble:

```text
Panels are silent clean blocking thumbnails: open-outline silhouettes, thin graphite linework, broad negative space.
No faces, clothing detail, texture, tonal modeling, wash, shaded fill, finished character design, or panel color.
Effects are attached abstract marks only: trails, bursts, shield arcs, spray wedges, smoke, or impact rings tied to a visible origin.
```

Storyboard panel interiors must remain:

- line-only;
- contour-only;
- no faces;
- no brows, eyes, mouth, smile, or face-detail marks;
- no clothing detail;
- no texture;
- no tonal modeling;
- no wash;
- no shaded fill;
- no finished character design;
- no panel color;
- no final-video style leakage.

If a state, signal, warning, energy, injury, light, aura, status, or transformation must be represented, express it through shape, position, contour marks, abstract attached marks, screen direction, object contact, or written prompt wording, not panel color.

Storyboard prompt template:

```text
[MODE: AUTEUR | APPRENTICE | SCREENWRITER]

Create a 16:9 production-safe line-only blocking storyboard sheet.

Panels are silent clean blocking thumbnails: open-outline silhouettes, thin graphite linework, broad negative space.
No faces, clothing detail, texture, tonal modeling, wash, shaded fill, finished character design, or panel color.
Effects are attached abstract marks only: trails, bursts, shield arcs, spray wedges, smoke, or impact rings tied to a visible origin.

The sheet proves shot order, blocking, pose, contact, screen direction, object state, spatial result, and action readability only. Keep panel headers outside panel interiors. Use sparse environment anchors only when needed for action, continuity, path, obstruction, scale, or evidence.

Describe the current scene, visible subjects, relevant objects, structural locks, and panel plan in compact executable wording.

Panel plan:
P01 / [shot size] / [beat name] — [one frozen visual beat]
P02 / [shot size] / [beat name] — [one frozen visual beat]
P03 / [shot size] / [beat name] — [one frozen visual beat]

Negative:
No text inside panels, captions, arrows, UI, labels, duplicate bodies, extra limbs, final-style rendering, color fill, facial features, brows, eyes, mouth, smile, clothing detail, texture, tonal modeling, gray wash, shaded fill, finished character design, or panel color.
```

## 9. Style Maintenance Pass

Before writing `prompt_video.txt`, synthesize a compact final-look paragraph from:

- explicit director style instructions;
- character, subject, prop, object, vehicle, creature, or mechanical assets within assigned authority;
- dedicated style, lighting, texture, or atmosphere references when supplied;
- environment or location assets through text extraction only by default.

Translate style into executable visual carriers:

- medium or visual system;
- palette logic;
- lighting key and motivated source;
- contrast;
- lens or focal feel;
- depth-of-field behavior when relevant;
- atmosphere or texture layer;
- material and surface behavior;
- forbidden cleanup or drift.

Do not rely on keyframes for style control. Do not let storyboard rendering style influence final video style. Do not rely only on broad labels, genre names, named styles, or reference images. Choose one coherent style direction and avoid stacking contradictory looks.

## 10. Video Prompt Pass

Generated `prompt_video.txt` must be self-contained and ready to paste and run immediately.

Hard rules:

- no reliance on hidden context;
- no reliance on prior segments;
- no reliance on storyboard images unless explicitly admitted by the user;
- no environment reference rehydration by default;
- no offscreen or absent entity naming;
- explicit camera coverage;
- multi-shot sequences use clean hard cuts unless the user requests otherwise;
- continuous takes are true continuous camera movement, not hidden transition simulation;
- environment references are omitted from the runtime registry by default;
- storyboard is structural only and does not control final style.

`prompt_video.txt` has a hard default maximum of 10,000 characters unless the user explicitly requests a different limit.

Before returning `prompt_video.txt`:

- check character count, including spaces and line breaks;
- if it exceeds the active limit, compress before output;
- do not silently exceed the limit.

When compressing, preserve:

- user-explicit action and camera instructions;
- visible cast and local runtime world;
- camera coverage;
- object-state continuity;
- reference authority limits;
- transition policy;
- critical negatives.

Compress or remove first:

- redundant adjectives;
- repeated atmosphere;
- duplicate style reinforcement;
- soft negatives;
- explanatory prose;
- internal reasoning;
- nonessential mood language.

Generated video prompt blocks should be paragraph-based. Keep top-level block headings if useful, but avoid nested colon-form sub-blocks by default, including `Palette:`, `Lighting:`, `Camera:`, `Action:`, `Transition:`, `Material:`, `Visual source policy:`, `Environment look:`, and `Forbidden look drift:`.

Allowed top-level block headings:

```text
[MODE]
[REFERENCE REGISTRY]
[FINAL LOOK CONTRACT]
[EXECUTION CONTRACT]
[SCENE]
[CONTINUITY + OBJECT STATE CONTRACT]
[SHOT PLAN]
[TAKE PHASE PLAN]
[NEGATIVE]
```

Video prompt template:

```text
[MODE: AUTEUR | APPRENTICE | SCREENWRITER]

[REFERENCE REGISTRY]
Use only active admitted runtime references. Include character, subject, prop, object, vehicle, creature, mechanical, style, lighting, texture, or atmosphere references only when intentionally attached. Do not include environment references by default. Do not include offscreen character references. State each reference in one compact sentence with role, allowed authority, denied authority, and downstream status. Omit this block when no runtime references are active.

[FINAL LOOK CONTRACT]
Write one compact paragraph defining the final visual world through medium or visual system, palette logic, motivated lighting, contrast, lens or focal feel, atmosphere or texture layer, material and surface behavior, and forbidden drift. The storyboard is structure-only and must not influence final color, lighting, texture, material, or rendering style. Environment assets are text-extracted only unless the user explicitly requested direct matching.

[EXECUTION CONTRACT]
Write one compact paragraph defining pacing, rhythm, camera coverage grammar, transition policy, performance pressure, motion intensity, micro-motion, and audio-planning language when relevant. Multi-shot sequences use clean hard cuts unless otherwise requested. Continuous takes use true continuous camera movement with no hidden cuts, dissolve, overlap transition, or crossfade simulation.

[SCENE]
Write the current clip action only. Include only visible, audible, and intended elements of this clip. Do not mention prior segments, future segments, absent characters, absent props, or offscreen named entities.

[CONTINUITY + OBJECT STATE CONTRACT]
Write one compact paragraph covering current visible cast, body state, prop or object state, scale, orientation, screen direction, thresholds, start state, end state, reveal timing, and continuity bridges needed inside this clip.

[SHOT PLAN]
Use for edited sequences. Each shot is a paragraph with visible action, object state, performance pressure, explicit camera coverage, and local transition behavior. Camera coverage includes shot scale, camera height, camera angle or relationship, movement or locked-off state, framing, placement, and axis or screen direction when relevant.

[TAKE PHASE PLAN]
Use for continuous takes. Each phase is a paragraph with visible action, object state, performance pressure, camera height, camera angle or relationship, continuous movement path, framing, subject placement, and no-cut continuity.

[NEGATIVE]
Short, local, risk-based negatives only. Use generic non-summoning negatives when needed, such as no extra person entering frame, no additional body in frame, no duplicated object, no reverse-angle reveal, no hidden cut, no blended transition.
```

## 11. Runtime Cleanliness Pass

Local Runtime World Contract:

Generated runtime prompts describe only the visible, audible, and intended world of the current clip or segment.

Do not mention absent characters, absent props, absent vehicles, absent creatures, absent locations, unused camera moves, unused effects, rejected styles, rejected transitions, prior scene elements, or future scene elements merely to say they are absent.

If something should not appear, prefer omission over negative mention. If a failure must be prevented, prefer positive replacement language or generic non-summoning negatives.

Non-Summoning Negative Rule:

- The Negative block must not become a list of named absent entities or rejected options.
- Avoid named negatives such as `no CHARACTER_2`, `do not show CHARACTER_2`, `no [specific absent prop]`, `no [specific rejected style]`, `no [specific unused camera move]`, `no previous location`, or `no future scene element`.
- Use generic negatives only when necessary, such as `no extra person entering frame`, `no additional body in frame`, `no duplicated object`, `no reverse-angle reveal`, `no hidden cut`, or `no blended transition`.
- When positive replacement language is safer, define the intended camera, intended object state, intended style, or intended motion clearly rather than naming the rejected alternative.
- The Negative block should be short, local, and risk-based.

Prompt file boundary:

Generated prompt files contain only executable downstream prompt text. They must not contain workflow explanations, diagnostics, validation notes, missing-asset reports, internal reasoning, recommendation labels, or assistant-facing production handoff.

## 12. File Output Workflow

Lite performs one internal pass:

1. Inspect input and assets.
2. Route mode and scene grammar.
3. Build one internal production spine.
4. Generate `prompt_storyboard.txt` from the spine.
5. Generate `prompt_video.txt` from the same spine.
6. Validate both outputs.
7. Return file paths and compact routing summary only.

Save outputs to:

```text
storyboard/<short_slug>/prompt_storyboard.txt
storyboard/<short_slug>/prompt_video.txt
```

Only list files actually created in the final response.

## 13. Validation Rules

Run validation internally before saving or returning generated prompt files.

- Framewright Lite is identified as version 1.0.0 of the one-pass clean compiler line.
- `required_outputs` contains only `prompt_storyboard.txt` and `prompt_video.txt`.
- No `prompt_keyframes.txt` is generated by Lite.
- No keyframe placeholders or optional keyframe slots appear in Lite `prompt_video.txt` by default.
- In SCREENWRITER MODE, inferred structure has clear shot function, visual progression, cause-effect continuity, geography when needed, and motivated camera behavior.
- In APPRENTICE MODE, craft completion does not override explicit user shot order, framing, camera movement, blocking, timing, or visual priorities.
- In AUTEUR MODE, the craft pass does not redesign the user's coverage or structure.
- `prompt_storyboard.txt` includes the exact production-safe storyboard preamble.
- Storyboard panel interiors obey production-safe purity.
- Storyboard panels describe drawable frozen moments.
- Storyboard output does not leak final-video style.
- `prompt_video.txt` is self-contained and ready to generate.
- Video shots or take phases include visible action, object or body state, camera behavior, and visible consequence.
- Count-sensitive entities and objects remain stable through positive wording.
- Final style is maintained through `[FINAL LOOK CONTRACT]`, not keyframes.
- `[FINAL LOOK CONTRACT]` translates style into executable visual carriers.
- Style extraction does not rely only on broad labels, genre names, named styles, or reference images.
- Environment and location assets are text-extracted by default.
- References used only for extraction are marked or treated as `text_extraction_only` and do not appear as active runtime references.
- The Reference Registry includes only active admitted runtime references.
- Absent entities are not named anywhere in runtime prompt text, including negatives.
- Camera coverage is explicit.
- Transition policy is explicit when relevant.
- Multi-shot sequences use clean hard cuts unless the user requests otherwise.
- Continuous takes use true continuous camera movement and do not simulate hidden transitions.
- `prompt_video.txt` is within the active character limit. The default limit is 10,000 characters including spaces and line breaks.
- Generated video prompt blocks are paragraph-based and avoid nested colon sub-block formatting by default.
- The Negative block is short, local, non-summoning, and risk-based.
- Stale negatives are removed before output.
- Generated prompt files contain no diagnostics, validation notes, internal reasoning, workflow explanations, missing-asset reports, recommendation labels, assistant-facing production handoff, or runtime-inactive placeholders.
