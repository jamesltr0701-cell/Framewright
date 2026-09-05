# Framewright 4.1.1 — Workflow Diagram Final Creative Brief

**Status:** Final direction for visual production

## Purpose

Explain the 4.1.1 compiler relationship in one readable schematic. The
diagram must teach the reader that one approved Production Spine can feed an
independent active stage; it must not imply automatic batch generation or a
mandatory Storyboard → Keyframe → Video sequence.

## Format

- README-safe wide diagram; target working canvas 1600 × 760 px, 8:3.8.
- Design for a rendered width of approximately 900 px and test at 50% scale.
- Provide a static SVG or PNG for the README, plus an accessible text/Mermaid
  equivalent when practical.
- Use the same black, off-white, graphite, and restrained grey system as the
  Hero Banner.

## Required structure

Use a left-to-right schematic with one central state and four independent
branches:

```text
APPROVED DIRECTOR INTENT
PRODUCTION ASSETS
SHOT DECISIONS
          │
          ▼
   PRODUCTION SPINE
   central compiler state
      ┌────┼────┬────┐
      ▼    ▼    ▼    ▼
 STORYBOARD  SHOT PLATE  KEYFRAME  VIDEO PROMPT
                                      │
                                      ▼
                                TARGET ADAPTER
```

The branch labels must be visually equal in status. The central Production
Spine is the only dominant structural node. Place a small side note or legend
near it: `ONE ACTIVE STAGE AT A TIME`.

## Meaning to preserve

- Storyboard, Shot Plate, Keyframe, and Video Prompt are artifacts available
  from the approved Production Spine; they are not compulsory sequential
  steps.
- Framewright executes one active stage at a time.
- Target Adapter belongs downstream of model-facing compilation and only
  serializes an approved prompt for the selected target.
- The director's intent and production decisions remain upstream and
  authoritative.
- The diagram describes the compiler state, not automatic generation, retry,
  or a batch pipeline.

## Visual treatment

- Thin graphite rules, solid arrows, restrained line weights, and clear node
  hierarchy.
- Use a slightly heavier outline or off-white field for `PRODUCTION SPINE`.
- Keep branch nodes unfilled or lightly tinted so no stage appears privileged.
- Use compact editorial labels, small registration ticks, or frame coordinates
  only where they improve orientation.
- Maintain generous whitespace and high contrast; no decorative network mesh.

## Do not include

- A single vertical funnel or `Storyboard → Keyframe → Video` chain.
- Automatic batch, retry, variant, or generation claims.
- Unsupported model names, extra stages, external tools, or autonomous-director
  language.
- Neon, gradients, glowing connectors, sci-fi UI chrome, or dense explanatory
  paragraphs inside the graphic.

## Acceptance test

A first-time reader should understand in seconds that the Production Spine is
the compiler's central state, the stages branch independently, and the target
adapter is downstream of the director's approved decision—not a director of
its own.
