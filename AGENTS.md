# Framewright Compiler Ownership

- This repository is the canonical editable Source for the explicitly invoked `framewright` Skill. Build installed copies and mirrors only from a validated release state.
- Framewright is the exclusive compiler for explicit `$framewright` requests. Do not import, invoke, or merge another model-prompt skill into the same compile unless the user explicitly requests a separate comparison outside the active Framewright compile.
- Every registered Video Prompt target, including `seedance_2_0`, loads exactly one subordinate adapter and uses its registered scalar serialization owner.
- Explicit `seedance_2_5` targets load only the registered Seedance 2.5 adapter. Explicit `minimax_h3` targets load only the registered MiniMax H3 adapter.
- Keyframes default to the registered Midjourney V7 adapter. ChatGPT Image 2 Keyframe edits always return to the immutable original master and never reuse a prior edited candidate as pixel input.
- The target model selects the serialization owner. A platform, provider, surface, filename, uploaded asset, or prompt wording never selects or owns the dialect.
- Keep operator-facing platform setup in the assistant-facing Run Card. Keep ownership metadata out of clean prompt artifacts.
- Validate every Video Prompt through the ownership-aware `video-prompt` validator command before saving.
