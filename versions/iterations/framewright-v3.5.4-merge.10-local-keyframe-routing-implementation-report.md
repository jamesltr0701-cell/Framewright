---
title: "Framewright v3.5.4 Merge.10 Local Storyboard, Look, and Keyframe Routing Implementation Report"
version: "3.5.4-merge.10-local"
status: "local_experimental_candidate"
date: "2026-08-24"
---

# Framewright v3.5.4 Merge.10 Local Implementation Report

## Scope

This isolated merge-only iteration adds:

- a once-per-generation-unit Storyboard Preflight decision before Video Prompt;
- branching live-action, two-dimensional, mixed-media, and VFX Look Development intake;
- provisional Shot Spine -> Storyboard review -> Committed Shot Spine authority flow;
- generation strategies for continuous single shots, edited sequences in one generation, and shot-by-shot generation;
- shot-scoped Keyframe roles and a complexity-sensitive Keyframe Eligibility Gate;
- Midjourney V7 as the default Keyframe prompt adapter;
- a ChatGPT Image 2 edit adapter that always returns to an immutable original master;
- deterministic fixtures for routing, look contracts, Keyframe scope, official-support qualification, and non-stacking image edits.

## Preserved boundaries

- Stable Framewright 3.5.3 is not modified.
- One active stage at a time remains protected.
- Storyboard remains planning-only unless explicitly admitted for a supported runtime route.
- Seedance 2.5 ordered multi-keyframes are treated as an official-guide advanced workflow, not a separate UI mode, a cut contract, or a reliability guarantee.
- Keyframe prompt compilation does not authorize Midjourney generation.
- One explicit Keyframe edit instruction authorizes one Image 2 attempt; automatic retries and candidate-on-candidate edits remain forbidden.

## Validation target

The candidate must pass the unchanged legacy regression set plus the new merge.10 fixtures, validate exactly the registered Video Prompt and image adapter profile sets, and leave the stable repository commit and working tree untouched.
