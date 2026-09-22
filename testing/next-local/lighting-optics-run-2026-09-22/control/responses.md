# Independent compilation responses

Loaded: Framewright v4.1.2

Director mode: AUTEUR MODE. Stage: Keyframes. Each case is an independent approved scope, not a multi-shot production. The approved request supplies the intake and compilation authority. These are text-only outputs; no media was generated. No durable production-state checkpoint was triggered.

## G1

Saved `G1.txt`: one frozen, photorealistic 16:9 waist-up shot. GPT Image 2.5 base-create route; no references. The bright screen-right window remains the only strong source, with a narrow cheek/shoulder edge and a mostly dim face and jacket. The room and workbench remain recognizable. Role: shot_first_frame, planning-only until admitted for downstream use.

INTENT DELTA: All supplied locks retained. Low-level shadow detail is the execution inference used to preserve material visibility without adding a lamp or flattening the backlight. No unresolved material decision. Text validation PASS; no visual result exists to assess.

## G2

Saved `G2.txt`: one frozen, photorealistic 21:9 shot. GPT Image 2.5 base-create route; no references. The distant-camera viewpoint carries compression; the 24 cm pot stays a modest lower-left layer, 60 cm forward of the man, and the closed door stays 70 cm behind him. Role: shot_first_frame, planning-only until admitted for downstream use.

INTENT DELTA: Body framing, object sizes and placements, face focus, softer pot, recognizable door, level eye-height camera and warm household light retained. Lens choice is expressed as a long-lens framing at a distant position; no unnecessary numeric lens or distance lock was invented. Residual risk: actual generated focus and relative scales require image inspection. Text validation PASS.

## B01

UNDERSTANDING: Preserve the approved even workshop lighting, not a dramatic redesign. PRODUCTION READING: AUTEUR, one frozen portrait; broad overhead panels own the light. DECISIONS: None unresolved.

Saved `B01.txt`:

> An evenly lit workshop portrait under broad overhead light panels. Soft, broad illumination falls evenly across the subject, with restrained shadows and a clearly legible back wall. Preserve this flat, even lighting relationship without adding a dramatic side key or rim light.

INTENT DELTA: No new source or contrast scheme added. Text validation PASS.

## B02

UNDERSTANDING: A luminous doorway behind a deliberately unreadable person. PRODUCTION READING: AUTEUR, one frozen lighting relationship; darkness is intentional rather than a defect. DECISIONS: None unresolved.

Saved `B02.txt`:

> A person stands in front of a bright doorway. The luminous opening behind the person provides strong backlight; most of the face and chest remain dark and unreadable. Keep the bright background and dark figure relationship without introducing frontal fill to reveal the face or clothing.

INTENT DELTA: Face/chest unreadability retained; no generic face-clarity correction. Text validation PASS.

## B03

UNDERSTANDING: The portrait supplies facial identity only; the rainy room supplies the scene's light. PRODUCTION READING: AUTEUR, text-only property binding. No actual reference has been supplied or inspected, and no upload slot is assigned. DECISIONS: No blocker for the requested binding exercise; a real generation would require the actual portrait.

Saved `B03.txt`:

> Use the neutral studio portrait only for the person's facial identity and facial proportions. Do not transfer its studio lighting, neutral color balance, background, pose, or framing. Place the person in the yellow-green rainy room, with the face illuminated and colored by that room's yellow-green light, integrated into its rainy atmosphere while preserving the referenced identity.

INTENT DELTA: Studio lighting is denied authority; scene lighting remains yellow-green. This is a descriptive binding, not a verified runtime attachment. Text validation PASS does not verify a reference.

## B04

UNDERSTANDING: The subject stays facing north while the camera changes sides. PRODUCTION READING: AUTEUR; explain the two existing camera views without turning the subject or moving the window. DECISIONS: None unresolved.

The window is east of the subject, on the subject's anatomical right. Camera A faces south, so east is screen left; it sees the front of the north-facing subject. Camera B faces north, so east is screen right; it sees the back of the same subject. The physical light source has not changed sides relative to the body.

Saved `B04.txt` lighting clauses:

> Camera A view: the window is on screen left. Window light illuminates the subject's anatomical right side, seen on the left side of the frontal view; the opposite side is relatively dimmer.
>
> Camera B view: the same window is on screen right. It still illuminates the subject's anatomical right side, now seen on the right side of the rear view; the opposite side is relatively dimmer. The subject maintains the same north-facing orientation.

INTENT DELTA: Only the screen-relative description changes. These are clauses for the two stated views, not a new two-panel generation instruction. Text validation PASS.

## B05

UNDERSTANDING: All lens, sensor crop, distance and vertical-framing values are explicit locks. PRODUCTION READING: AUTEUR; physically incompatible framing prevents a faithful photographic compile.

DECISION REQUIRED: Which lock may change? With a 36 mm image width cropped to 21:9, the image height is approximately 15.43 mm. At 110–135 mm and 3.5–4 m, the approximate vertical field is only 0.40–0.56 m, below the required 0.85 m even before headroom. The most permissive combination, 110 mm at 4 m, still cannot fit the span.

Options: keep the lens and crop but move farther away (approximately 6.1 m at 110 mm, or 7.4 m at 135 mm, before extra framing margin); keep distance and crop but shorten the lens (roughly 64–73 mm at 3.5–4 m); or change the crop/framing requirement. Recommendation: allow greater camera distance if preserving the long-lens compressed portrait is the priority. These are approximate geometric checks, not measured production specifications.

No clean prompt saved. I will not silently unlock any of your explicit constraints. Unresolved blocker: the director must authorize which lock to relax.

## B06

UNDERSTANDING: Compressed depth and the full 0.85 m waist-to-head span are yours; the earlier numbers were compiler inventions. PRODUCTION READING: AUTEUR; withdraw those non-authoritative numbers and preserve the framing. DECISIONS: No need to ask you to resolve a contradiction the compiler introduced.

Saved `B06.txt`:

> Compressed-depth waist-up portrait from a distant camera position. Include the full 0.85 m vertical span from waist to crown, with space above the head. Use a suitably long lens and sufficient camera distance to fit the entire required span without cutting off the waist or head. Keep the distant-camera perspective and restrained depth expansion; do not enforce a fixed focal length or camera distance at the expense of the framing.

INTENT DELTA: Withdrawn 135 mm / 3.5 m compiler assumptions; director framing and compression remain. Text validation PASS.

## B07

No—the foreground/background perspective relationship stays the same if the camera viewpoint and scene geometry remain fixed and the final crop recovers the same composition. Focal length changes the recorded field of view and image scale; cropping can match the framing, but neither changes the relative viewpoint distances that determine perspective. Focus, blur, optical distortion, and resolution can still differ. A wider lens moved closer to recover framing would be a different case: moving the camera changes perspective.

This is an explanation-only request; no prompt artifact or generation was needed.

## B08

UNDERSTANDING: Face clarity outranks the wall, but fixtures must remain identifiable. PRODUCTION READING: AUTEUR; a long lens does not require an unreadable background. DECISIONS: None unresolved.

Saved `B08.txt`:

> A long-lens portrait with the face as the clearest, most sharply focused plane. The wall stands one meter behind the face. Give the wall a gentler level of detail than the face while keeping its fixtures recognizable in shape and placement; avoid dissolving the wall fixtures into indistinct bokeh.

INTENT DELTA: Focus hierarchy retained without imposing maximum blur or an unnecessary aperture number. Text validation PASS.

## B09

I would inspect different possible causes before asking to correct either image. In the close portrait, camera proximity can exaggerate near/far facial proportions; placing the face at the edge of a wide rectilinear view can also stretch its shape. I would check face position, camera distance and angle, and whether straight lines bend from lens distortion. Correcting bent lines is not the same as changing viewpoint-driven facial perspective or edge projection.

For the room view from across the room, I would inspect straight architectural lines, vertical convergence from tilt, edge stretching, and the intended room geometry. A wide field of view alone does not establish a defect, and a distant viewpoint does not have the close portrait's same near/far facial exaggeration. I would first distinguish an unwanted artifact from approved perspective or stylization, then ask about a correction only if it would alter a protected composition or intentional appearance.

No pixels were supplied or inspected; this is an inspection plan, not a diagnosis of an actual image. No prompt artifact needed.

## B10

UNDERSTANDING: A clearly readable figure with compressed corridor depth. PRODUCTION READING: AUTEUR; minor camera execution is delegated, not a request for a technical questionnaire. DECISIONS: No lens or sensor number is required from you.

Saved `B10.txt`:

> View a legible figure in a corridor from a distant camera position, using a long-lens framing that compresses the apparent separation of the figure and the corridor behind. Keep the figure's silhouette and relevant body detail readable against the surrounding space. Use a level camera and stable composition; choose focal length and framing distance together to preserve this compressed-depth relationship without crowding or accidentally cropping the figure.

INTENT DELTA: Level camera and stable framing are minor execution inferences. No arbitrary optical numbers or new lighting design. Text validation PASS.

## B11

Based on your report, the candidate fails the bounded prop-only edit: the device correction succeeded, but the protected background softness/detail level changed. I have not inspected the pixels, so both the success and collateral drift are reported, not observed. A sharper background is not an acceptable improvement when its softness was protected.

Do not promote this candidate as a successful full edit on that evidence alone. Preserve the corrected-device requirement in the cumulative semantic edit specification, but any newly authorized attempt must return to the immutable original master, not use this candidate's edited pixels. The next investigation would compare the original, candidate and actual edit instruction; the report alone cannot establish whether the primary cause was serialization, rendering, or model behavior. If deterministic compositing can isolate the correct device while keeping the original background, inspect that option before promising it.

Current disposition: do_not_generate, because this turn requests judgment only. No retry, repair or new master is authorized, and no image inspection is claimed.

## B12

UNDERSTANDING: Approved graphic 2D space is intentionally nonphysical and deeply legible. PRODUCTION READING: AUTEUR; photographic lens feasibility must not override that style. DECISIONS: None unresolved.

Saved `B12.txt`:

> A graphic 2D keyframe with deep focus: keep foreground, figure, and background sharply legible within an intentionally impossible compressed space. Preserve the approved graphic spatial relationships without correcting them into realistic optical perspective or adding photographic background blur.

INTENT DELTA: Intentional impossibility retained. Text validation PASS.

## B13

UNDERSTANDING: Weaken window-side illumination on the person only; room/window brightness are protected. PRODUCTION READING: AUTEUR, GPT Image 2.5 bounded edit-text route; the descriptive binding is provisional. No image, file path or slot has been invented, and no generation is authorized.

Saved `B13.txt`:

> In the supplied current keyframe, change only the person's illumination to a weaker window-side light. Reduce the light falling on the window-facing areas of the person while preserving the existing direction of that light. Keep the room and window brightness unchanged; do not darken the entire image or reduce the window's brightness. Preserve the person’s identity, pose, clothing and materials, the camera viewpoint, crop, focus and background detail level, scene layout, props, and all other existing color and lighting relationships outside the person. Do not add new light sources or redesign the scene.

INTENT DELTA: Person illumination changes; environment exposure does not. Real execution must resolve the immutable original master and any cumulative prior edits. The requested text-only draft is complete, but it is not an executable verified edit package.

Validation limitation: the keyframe-prompt validator rejects the edit adapter with `image_edit_prompt_requires_trace`, directing the operator to the clean-master edit validator. No clean-master trace or actual master was supplied; none was fabricated. No edit-validation PASS is claimed.

## B14

UNDERSTANDING: Darker, cooler illumination across both person and room, with scene content protected. PRODUCTION READING: AUTEUR, GPT Image 2.5 bounded edit-text route; provisional descriptive binding only. No generation is authorized.

Saved `B14.txt`:

> Relight the supplied current keyframe as a whole so both the person and the room become darker and cooler. Apply the reduced illumination and cooler color consistently across the person, room surfaces, and existing light-dependent reflections and shadows. Preserve the scene layout, the person's identity and pose, clothing design and material, prop design and placement, camera viewpoint, framing, focus relationships and background detail level. Change the lighting and its visible color effect, not the underlying identities, wardrobe, objects, or architecture; do not introduce new lamps or redesign the composition.

INTENT DELTA: Person and environment lighting may both change. Their old brightness/color are not incorrectly protected. Identity, clothing and prop design, layout, camera and focus remain protected. Real execution needs the immutable original master and cumulative edit state; no asset locator is invented.

Validation limitation: the same `image_edit_prompt_requires_trace` rejection occurred for B14. This is a completed provisional instruction, not a validated runtime edit or inspected image result.

## Source reads and validation record

Only the supplied baseline skill tree and the supplied raw requests were used as compiler evidence. No alternative run, report, diff, repository instructions, git history, external prompt skill or answer key was inspected.

Read sources (paths relative to `/private/tmp/framewright-lighting-baseline.xyw6ZF/skill/framewright/`):

- `SKILL.md`, completely.
- `references/framewright.md`, frontmatter and section map; sections 1–7, 8 integrated craft support, 8.3–8.8, 9–10, 12, 14–17. Truncated relevant ranges were re-read in smaller spans.
- `references/keyframe_profiles/adapter_registry.yaml`, completely.
- `references/keyframe_profiles/gpt_image_2_5.md`, completely, for base-create requests.
- `references/keyframe_profiles/gpt_image_2_5_edit.md`, completely, for bounded edit-text requests.
- `references/craft/light-sound.md`, completely, for light/exposure relationships.
- `references/craft/identity-material.md`, completely, for restricted reference authority and protected edit properties.
- `references/craft/diagnosis-repair.md`, completely, for B11's report-only evaluation and repair boundary.
- `/Users/jameslee/Documents/AI Filmmaking Studio/framewright/testing/next-local/lighting-optics-run-2026-09-22/raw-requests.md`, completely.

Also enumerated the supplied skill tree to locate the bundled validator and read its CLI help. No inactive video or Midjourney adapter was loaded. The Python YAML runtime was preflighted with `import yaml`, reporting PyYAML 6.0.3. Used the supplied `scripts/validate_framewright.py keyframe-prompt` with the supplied image registry and selected adapter ID. G1, G2, B01, B02, B03, B04, B06, B08, B10, B12 passed. B13 and B14 were rejected for missing edit-trace validation as stated above; no success was fabricated. B05 remained blocked by explicit physical locks. B07, B09 and B11 are explanation/judgment responses rather than generation prompts.

All writes were confined to this control output directory. No media generation, production mutation, source edit, or automatic retry occurred.
