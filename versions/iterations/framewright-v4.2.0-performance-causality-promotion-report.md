# Framewright v4.2.0 — Performance Causality Promotion

Date: 2026-09-28. Base: v4.1.3 (`2860d3b`). Scope: text compilation and offline validation only; no media was generated, and no frozen THE WEAVER artifact was modified.

## What changed

- Core §8.7 now permits a performance process to be the dominant shot objective. A material stimulus, emotional transition, selected physical response, listener effect, and residual state cannot be discarded as merely subordinate detail during compression or translation.
- Core §8.11 uses the existing `performance_progression` and Intent Ledger to devise low-risk physical expression within established meaning. One to three **coordinated carrier groups** replace a mechanical count of individual verbs; groups cannot hide an unrelated action list. Contextual hair, fabric, strap, and bodily follow-through require a perceptible cause and settling state. Intentional adjustment requires motive, a free limb, timing, and continuity. Stillness and stylization remain valid choices.
- Core §8.12 keeps unauthorized speech forbidden while allowing a narrow, traceable scope or persistent user/production preference for a brief response or nonlexical vocal event. Locked dialogue, strict silence, and current prohibitions override a general preference. Each added event is specified by speaker, timing, exact wording or sound description, and count in the existing `sound_contract`; it is not an open-ended invitation to the video model.
- The Skill now loads performance craft for ordinary dialogue, listening, and emotional change. Seedance 2.0, Seedance 2.5, and MiniMax H3 each retain their own serialization dialect while preserving the Core process. No new stage, state owner, default output file, or parallel compiler was added. Prompt IR remains schema 1.1, with optional performance and sound detail; legacy records remain valid.
- The validator checks optional carrier-group bounds, vocal authorization and event counts, legacy/strict silence, and exact saved-prompt evidence in a temporary `video-prompt --trace` check. The trace must contain the exact final prompt text. These are structural checks, not proof of acting naturalness or generated-video compliance.

## Evidence

- Existing v4.1.3 offline baseline: 128/128 fixtures matched expectations. Final v4.2.0 suite: **140/140**; new cases include positive and failing performance, sound, silence, and optional-IR fixtures. Skill validator and `git diff --check`: PASS.
- [Raw director requests](../../testing/next-local/performance_v42_raw_requests.md), [v4.1.3 control outputs](../../testing/next-local/performance-v42-run-2026-09-28/control/EVALUATION.md), [v4.2.0 candidate outputs](../../testing/next-local/performance-v42-run-2026-09-28/candidate/SUMMARY.md), and per-case prompts/traces are preserved. Separate GPT-6-sol/high text-compilation runs loaded isolated v4.1.3 and candidate skill copies with identical requests. API stream retries, nondeterminism, and one sample per case were not controlled; this is an exploratory comparison, not a measured success-rate study.
- All seven requested Seedance 2.0 scopes (P01A, P01B, P02, P03, P04, P07, P10) yielded clean saved prompts in both versions. P10 normal and compact variants passed; candidate compact is 563/600 characters, control compact 571/600. Candidate P02 also passed separate Seedance 2.5 and MiniMax H3 serialization checks with its locked line, transition, listener response, and no-added-voice boundary intact. A deliberate prompt/trace mismatch failed validation.

Three actual before/after comparisons, quoted from the saved prompt files:

| Scope | v4.1.3 control | v4.2.0 candidate | Reading |
|---|---|---|---|
| P01A, sincere agreement | “Lin takes in what she has heard, then gives one small, unhurried nod as her gaze settles on Mei.” | “Lin receives the last thought with her gaze on Mei. Lin lets a small nod form as her shoulders ease. She meets Mei's eyes again…” | Both make agreement observable. Candidate articulates the reception and return to contact a little more explicitly; no evidence of a categorical improvement. |
| P02, restrained cancellation | “the smile remains for a brief beat while understanding catches up. Her gaze searches Mei's face, then the smile gradually loosens…” | “her earlier smile remains while her gaze registers the meaning; understanding arrives after the words. Her smile subsides and her posture draws slightly inward…” | Both preserve old joy, delayed understanding, and withdrawal. The old compiler was not a weak baseline. |
| P07, head-turn secondary motion | “The roots follow her head; the longer hair briefly lags, then swings in a few connected clumps… and settles after the head stops.” | “The long loose hair follows with a slight weighted lag in broad clumps… As the turn ends, the clumps settle by gravity…” | Both distinguish fixed hair identity from transient movement in a windless room. Candidate is slightly more causal, but no video outcome was tested. |

The candidate [P10 compact final prompt](../../testing/next-local/performance-v42-run-2026-09-28/candidate/P10/prompt_video_compact.txt) still states the run's residual breath, Mei's exact line, the hopeful smile lingering before understanding, an unvoiced attempted reply, and faster-than-rest breathing afterward. These relationships occur in the final 563-character prompt, not merely in an internal field.

## Remaining limits

The structural regression and actual text-compile behavior are verified separately. Human review of these saved texts found no tested scope where v4.2.0 materially regressed, but also no basis for claiming general prompt or video-quality superiority over v4.1.3. String/span checks cannot prove semantic equivalence or natural performance, and the carrier-group bound cannot by itself recognize every incoherent action pile. P05, P06, P08, P09, P11–P14 are represented by rules and selected structural tests, not independent saved-prompt A/B runs. Real video adherence, 480p legibility, model reliability, and multi-seed outcomes are **not verified**; they require later user-authorized generation trials.

## Release boundary

The director's persistent limited-vocal preference is user-specific, not a public default; an existing host preference or production-state owner must carry the grant into a future scope, and the current Intent Ledger must record its source. A new project without that grant keeps the no-added-voice default. Release completion additionally requires byte-matched Core/snapshot, validated installed Skill and Desktop mirror, and live GitHub `main`/tag verification.
