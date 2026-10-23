# Framewright v4.2.3 — Kling 4.0 and optional Ran profile

Date: 2026-10-23. Scope: publish the locally tested Kling adapter and the director-approved personal profile. This release retains v4.2.2's blocking behavior and preserves all earlier release snapshots and tags.

## Resulting behavior

- An explicit Kling 4.0 Standard target selects only `framewright_adapter_kling_4_0`, adapter version `0.1.0`. The official web Omni Reference and dedicated Keyframes entries have separate qualification rules. Flash is not an alias and no provider/API model identifier is claimed.
- The ownership-aware validator requires the current Kling qualification, checks entry/role compatibility, native asset mappings, primary edit video, per-kind and combined quotas, the shared video pool, keyframe times, declared source properties, and an optional trusted token count. Kling's 8,000-token limit is not replaced with another model's character limit.
- The bundled [Ran director profile](../../skill/framewright/references/director_profiles/RAN_DIRECTOR_PROFILE.md) loads only when a director or project explicitly selects it. Its latest approved additions cover scene energy, interfering actions, background participants, dramatic wide shots and explicitly delegated exploration. It remains director input, outside the compiler-source list and adapter registry. Current instructions and stricter sound boundaries take priority.
- The public profile preserves the approved creative sections while replacing project-specific hookup text and removing local paths. Private production chats and evidence documents are not included.
- The regression runner uses configurable `FRAMEWRIGHT_PYTHON` (default `python3`) and portable temporary paths, with a PyYAML preflight. Use an isolated project environment that supplies PyYAML; no maintainer-specific interpreter path is published.

Kling facts were checked on 2026-10-22 against the [official 4.0 User Guide](https://kling.ai/quickstart/kling-4-model-user-guide), dated 2026-10-14. Exact voice-profile mention spelling, account rollout, API mappings, HDR and extension availability still require surface-specific confirmation.

## Validation

The v4.2.3 package passed Core/registry checks, **140/140 existing fixtures**, **18 existing source-review tests**, **17 Kling tests**, and existing Video Prompt / image adapter CLI smoke checks. Skill-format validation and whitespace checks also passed.

An independent forward run against the preceding local candidate used raw requests without previous answers or implementation tests. A 24-second uninterrupted dialogue required a real speaker-to-voice-profile clarification, then passed ownership-aware validation. Three incompatible requests were correctly stopped: dedicated timeline keyframes plus an independent voice profile, six clips in the five-video shared pool, and an explicit unsupported Flash request. The run exposed a media-ratio representation ambiguity; the adapter now distinguishes numeric input width/height ratios from string output settings. This is historical behavioral evidence for the same adapter logic, not a newly repeated model evaluation of the v4.2.3 label.

No media was generated. Text/contract validation does not establish upload state, reference fidelity, blocking continuity, lip synchronization, or generated-video quality. An unknown token count or unmeasured media attribute is not certified by PASS. The optional profile's selection boundaries were inspected; no new generation-quality claim is made for its preferences.

## Packaging

Core, Skill entrypoint and display name use v4.2.3. The new immutable `versions/releases/framewright-v4.2.3.md` is byte-identical to the authoritative Core. The corrected v4.2.2 and its initial snapshot remain untouched. Local source, installed Skill, Desktop mirror and GitHub are checked by file hashes as part of publication; operational backups and private synchronization evidence stay local.
