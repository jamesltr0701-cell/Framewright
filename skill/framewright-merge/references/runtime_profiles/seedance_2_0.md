---
profile_name: "Framewright Merge Seedance 2.0 Runtime Profile"
profile_version: "2.0.0"
profile_role: "subordinate_video_prompt_adapter"
target_model: "seedance_2_0"
evidence_scope: "model_execution_heuristics_not_platform_guarantees"
---

# Seedance 2.0 Runtime Profile

## 1. Authority and Load Condition

Read this file completely only when the active Framewright stage is `Video Prompt` and the resolved target model is Seedance 2.0.

`references/framewright.md` remains the sole director and compiler authority. This adapter accepts one approved model-neutral `video_prompt_ir`, qualifies Seedance-specific execution risk, and serializes the final model-facing prompt. It must not select or change Director Mode, scene grammar, directing intention, directorial voice, generation-unit boundaries, endpoint purpose, reference authority, scene structure, continuity canon, or active stage. Treat the input IR as read-only; return to Core when it is incomplete or contradictory.

## 2. Evidence Boundary

Keep four claims separate in the assistant-facing Run Card:

1. model capability;
2. active-surface access;
3. request syntax on that surface;
4. returned adherence in the actual take.

Treat official model documentation as capability evidence only for the stated model/version. Treat model tendencies and community observations as hypotheses to test, never guarantees. If a current surface fact was not verified in the active task, mark it unknown instead of inventing a limit, toggle, tag, language, lip-sync behavior, or API field. Keep evidence labels and uncertainty out of the clean prompt.

## 3. Fidelity Allocation and Overload Warning

When identity fidelity, motion boldness, scene density, camera complexity, dialogue, and audio compete, identify one primary fidelity spend, one secondary spend, and one area to economize. Warn assistant-facing when several fragile systems compete in the same beat, especially voice plus identity plus precise motion plus dense staging plus moving camera plus synchronized audio. This is a feasibility explanation, not permission to rewrite the story. Preserve every director lock; if simplification changes material intent or a generation-unit boundary, return the choice to Core and the director.

## 4. Reference Transfer

Let an admitted source carry only its approved state or attributes; let text carry the requested delta. Bind every source to one primary role and name important exclusions. Stable Material Registry identity owns the role; upload order, filename, thumbnail, chip, provider, or UI index never does.

For I2V, do not re-describe static identity, form, wardrobe, palette, composition, or background already carried by the image. State what moves or changes, one camera path, sound intent, and fragile anchors that remain.

For first/last-frame work, let the first frame define the opening and the last frame define the target. Describe only the transition, persistent carrier, camera behavior, light continuity, sound, and preservation locks. Do not treat endpoint images as two competing style prompts.

For R2V, bind video separately to approved motion, camera, timing, composition, or edit behavior. Deny performer identity, wardrobe, location, and sound unless explicitly authorized.

An artistic source-look lock comes from Core's approved final-look and source-authority contract. This adapter may explain target stability risk but may not invent, weaken, or broaden that artistic authority.

## 5. Seedance Execution Grammar

- Use one legible focal action path with cause, consequence, and terminal state.
- Use one primary camera idea with start, path, speed, subject relationship, and landing frame.
- Give fragile faces, hands, products, logos, text, or lip-sync more stable framing and less simultaneous competition.
- Keep dialogue speaker-owned and physically playable. Do not claim supported languages, lip-sync reliability, or surface audio behavior unless verified for the active route.
- Prefer ambience plus a small number of synchronized diegetic cues; music remains absent unless requested.
- For VFX, state source, material, path, object interaction, light interaction, dissipation, and endpoint only when materially visible.
- Prefer a positive observable state over stacked negatives. Retain a negative only when it prevents a realistic current failure.

For multi-character scenes, establish a conditional focus hierarchy only when competing action needs it: one focal action, subordinate reaction or counter-action, and simple persistent background motion. Do not force an exact three-tier pattern, prohibit large action, or flatten intentionally equal ensemble staging. Warn when fragile contact, crossing, occlusion, identity, or lip-sync objectives compete.

Choose one temporal grammar:

- `dense_multishot`: explicit ordered shots, one main action and endpoint per shot, continuity locks across cuts;
- `phased_single_take`: one uninterrupted camera path expressed as beginning, development, and landing phases, with no shot labels or hidden resets.

Never mix hard-cut shot labels with a single-continuous-take contract. Future generation units remain reserved and stay out of the current prompt.

## 6. Endpoint Execution

Translate Core's approved `endpoint_purpose` without changing it:

- `resolve`: complete the action and settle the new state clearly;
- `extension_anchor`: preserve open subject motion, gaze, camera movement, environment activity, and audio tail needed by the next unit;
- `loop_seam`: align position, motion phase, exposure, environment behavior, and audio phase with the opening seam;
- `hero_hold`: let movement settle into a stable, readable hero state;
- `edit_point`: create a clean visual and audio boundary without accidental unfinished motion;
- `reveal_or_payoff`: land the peak, then protect enough readability for the reveal or consequence to register.

## 7. Prompt IR Input Contract

Accept only an IR whose `adapter_input_status` is `approved`, whose target is `seedance_2_0`, whose unresolved material decisions are empty, and whose completed/current/future beat scopes are disjoint. Never serialize internal fields such as Director Mode, directing-intention rationale, directorial-voice rationale, Intent Ledger, risk analysis, target ownership, or provenance.

## 8. Serialization

Choose one schema from the approved IR. Omit empty blocks and avoid nested colon-heavy formatting.

Preferred compact block order:

```text
REFS
VISUAL STYLE
AUDIO
ENVIRONMENT
CONTINUITY LOCKS
EMOTIONAL GUIDANCE
RHYTHM + ESCALATION
CAMERA EXECUTION
SCALE LOCK
OBJECT-STATE TIMELINE
BEATS
NEGATIVE
```

Use paragraph blocks. For an edited sequence, each beat states visible action, relevant object state, performance pressure, camera relationship, and any local transition exception; hard cuts are the shared default. For a continuous take, each phase states visible action, relevant object state, camera relationship, continuous path, framing, subject placement, and no-cut continuity without resetting camera, geography, identity, object state, or optics.

When a fuller execution contract is required, the allowed alternate block order is:

```text
[REFERENCE REGISTRY]
[MATERIAL ROLES]
[FINAL LOOK CONTRACT]
[EXECUTION CONTRACT]
[SCENE]
[CONTINUITY + OBJECT STATE CONTRACT]
[SHOT PLAN]
[TAKE PHASE PLAN]
[NEGATIVE]
```

Use only one schema. Native material surrogates such as `@Image 1`, `@Video 1`, or `@Audio 1` must map assistant-facing to one stable Material Registry role. They never become stable identities.

## 9. Compression and Validation

Remove hollow boosters, repeated adjectives, duplicated authority, repeated camera explanation, repeated continuity, then secondary atmosphere. Preserve identity and count, active source roles, actual opening state, current action, camera causality, dialogue ownership, sound cues, terminal state, endpoint execution, continuity, completed-beat exclusions, and reserved-future exclusions.

The final clean prompt contains executable direction only and stays within the active character limit. Put capability uncertainty, surface setup, evidence labels, fidelity allocation, overload warnings, reference map, and residual risk in the Run Card.
