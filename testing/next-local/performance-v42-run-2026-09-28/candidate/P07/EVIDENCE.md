# P07 — Framewright v4.2.0 evaluation

Scope: approved 8-second 16:9 Video Prompt; APPRENTICE MODE; one continuous shot; no references or storyboard; Seedance 2.0 via `framewright_adapter_seedance_2_0`.

## Normal prompt

- File: `prompt_video.txt`; 816 characters including spaces and line breaks; limit 10000.
- Protected semantic anchors: still indoor no wind; one head turn toward offscreen friend; dark long loose hair identity; clump and silhouette lag; gravity settling; no hair-brush action; no voice.
- Compilation decision: Head acceleration causes broad clump lag and gravity settling; no wind or intentional adjustment.
- Feasibility: Low: prioritize silhouette rather than strand detail.
- Validation: `video-prompt` PASS with ownership, registered compiler sources, character limit, and exact final-text performance/vocal trace.
- Sources: `skill/framewright/SKILL.md`, `skill/framewright/references/framewright.md`, `skill/framewright/references/runtime_profiles/adapter_registry.yaml`, `skill/framewright/references/runtime_profiles/seedance_2_0.md`, `skill/framewright/references/craft/camera-motion.md`, `skill/framewright/references/craft/light-sound.md`, `skill/framewright/references/craft/identity-material.md`.

## Run card and limits

- Input: text only; no material uploads or references. Selected active-surface task/UI route and control profile availability were not verified.
- Requested runtime: 8 seconds, 16:9; `single_shot_continuous` generation strategy; naturalistic live action was a reversible execution inference.
- Fidelity allocation: Primary fidelity: the single head turn and causal hair silhouette; secondary: persistent hair identity; economize individual strand detail.
- Evidence limit: validation confirms prompt structure, ownership, exact trace spans, event counts, and character count. No image, video, or audio was generated, so model adherence is untested.
