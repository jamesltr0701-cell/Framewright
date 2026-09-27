# P10 — Framewright v4.2.0 evaluation

Scope: approved 8-second 16:9 Video Prompt; APPRENTICE MODE; one continuous shot; no references or storyboard; Seedance 2.0 via `framewright_adapter_seedance_2_0`.

## Normal prompt

- File: `prompt_video.txt`; 928 characters including spaces and line breaks; limit 10000.
- Protected semantic anchors: Lin enters breathless after run; expects good news; Mei exact line; small hopeful smile lingers then understanding; reply begins visually then silence; stays beside Mei; residual breath; no added voice.
- Compilation decision: The smile survives into recognition, then Lin visibly starts a reply and chooses silence while post-run breath persists.
- Feasibility: Medium: line, visual reply suppression, and breath compete within eight seconds.
- Validation: `video-prompt` PASS with ownership, registered compiler sources, character limit, and exact final-text performance/vocal trace.
- Sources: `skill/framewright/SKILL.md`, `skill/framewright/references/framewright.md`, `skill/framewright/references/runtime_profiles/adapter_registry.yaml`, `skill/framewright/references/runtime_profiles/seedance_2_0.md`, `skill/framewright/references/craft/camera-motion.md`, `skill/framewright/references/craft/light-sound.md`.

## Compact variant

- File: `prompt_video_compact.txt`; 563 characters including spaces and line breaks; limit 600.
- Protected semantic anchors: Lin enters breathless after run; expects good news; Mei exact line; hopeful smile lingers into understanding; reply starts visibly then silent; stays beside Mei; residual breath; no added voice; 600-character cap.
- Compilation decision: Compressed syntax while retaining the full smile, recognition, withdrawal, silent reply, and breath sequence.
- Feasibility: Medium: the 600-character cap leaves little redundancy for fragile visual timing.
- Validation: `video-prompt` PASS with ownership, registered compiler sources, character limit, and exact final-text performance/vocal trace.
- Sources: `skill/framewright/SKILL.md`, `skill/framewright/references/framewright.md`, `skill/framewright/references/runtime_profiles/adapter_registry.yaml`, `skill/framewright/references/runtime_profiles/seedance_2_0.md`, `skill/framewright/references/craft/camera-motion.md`, `skill/framewright/references/craft/light-sound.md`.

## Run card and limits

- Input: text only; no material uploads or references. Selected active-surface task/UI route and control profile availability were not verified.
- Requested runtime: 8 seconds, 16:9; `single_shot_continuous` generation strategy; naturalistic live action was a reversible execution inference.
- Fidelity allocation: Primary fidelity: the protected performance process; secondary: speaker ownership or silent listener response; economize decorative setting detail.
- Evidence limit: validation confirms prompt structure, ownership, exact trace spans, event counts, and character count. No image, video, or audio was generated, so model adherence is untested.
