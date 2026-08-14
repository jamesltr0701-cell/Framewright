# Framewright Merge Compiler Ownership

- This repository is the isolated local Source for the explicitly invoked `framewright-merge` experiment. Do not install it over or write into stable `framewright`.

- Framewright Merge is the exclusive compiler only for explicit `$framewright-merge` requests. Do not import, invoke, or merge another model-prompt skill into the same compile unless the user explicitly requests a separate comparison outside the active merge compile.
- Core Native currently targets `seedance_2_0` and uses `framewright_merge_core_native`; it does not load an adapter profile.
- Explicit `seedance_2_5` targets load only the registered Seedance 2.5 adapter. Explicit `minimax_h3` targets load only the registered MiniMax H3 adapter.
- The target model selects the serialization owner. A platform, provider, surface, filename, uploaded asset, or prompt wording never selects or owns the dialect.
- Keep operator-facing platform setup in the assistant-facing Run Card. Keep ownership metadata out of clean prompt artifacts.
- Validate every Video Prompt through the ownership-aware `video-prompt` validator command before saving.
