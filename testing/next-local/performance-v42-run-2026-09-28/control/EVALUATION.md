# Framewright v4.1.3 control evaluation

## Route and scope

- Local source: `skill/framewright/SKILL.md`; Core `4.1.3`; Seedance 2.0 adapter `2.2.0`.
- Video Prompt, APPRENTICE MODE, one 8-second 16:9 continuous unit per case; no runtime references, storyboard, music, or media generation.
- Target `seedance_2_0`; scalar serialization owner `framewright_adapter_seedance_2_0`; adapter contract `seedance_2_0`.
- Task route: text-to-video. Active surface access, surface syntax, and returned model adherence were not tested.

## Saved-artifact validation

Each final file below was passed to the local ownership-aware `video-prompt` validator with the registered target, scalar owner, adapter ID, profile contract, listed compiler instruction sources, and its character limit. Character counts include spaces and the final newline.

| Scope | File | Characters | SHA-256 | Validator | Semantic check |
|---|---|---:|---|---|---|
| P01A | `outputs/P01A/prompt_video.txt` | 630 | `073de211dde710d143353da6d4f6f292f93ec217dd9c52f9fadec8855f1986c5` | PASS | Delegated, restrained nod and warm gaze; Mei listens; no voice. |
| P01B | `outputs/P01B/prompt_video.txt` | 704 | `4105f43fd69cce8a5713d61eecb4574a43449bd1a7ea40752de6be40c32eef38` | PASS | Hearing completes, nod with eyelid lowering, then raised head and reconnected gaze. |
| P02 | `outputs/P02/prompt_video.txt` | 960 | `84b765c07db7e4c80e64fd939fc306d19b877adf22ed8c75aee931ad975f5447` | PASS | Exact Mei line; lingering joy, delayed understanding, restrained withdrawal, Mei reception. |
| P03 | `outputs/P03/prompt_video.txt` | 654 | `2ece625a1a3eff2297b1ee1ac41cb5ac4546bb65d11644c15362b9bf01bef2a3` | PASS | Observable listening with an inaudible account and no human vocalization. |
| P04 | `outputs/P04/prompt_video.txt` | 720 | `c4861c3b425fd5743fbb0e88cd771d4c86b227d451288e440ad2263fcfa0da20` | PASS | One chosen “Mm.” before the exact locked sentence; no other vocal event. |
| P07 | `outputs/P07/prompt_video.txt` | 755 | `b8fa30d30615b0952803cb050ae9d7404261cada1414ca217cf0d776c36b1f15` | PASS | One head turn; fixed hair identity; clump lag, follow-through, settling; no wind. |
| P10 normal | `outputs/P10/prompt_video.txt` | 926 | `eb48cd536ef1fb9a353645e0e2444ec0a7ac3e083a1044388f2a773a52915059` | PASS | Hopeful smile, delayed understanding, silent attempted reply, residual visible breath. |
| P10 compact | `outputs/P10/prompt_video_compact.txt` | 571 | `75bf3ec11e53015f394fd4be37e696382af9e518dc56378fcf9c1e57a2b14836` | PASS | Same locked P10 process under the 600-character production cap. |

## Decision and risk notes

- All seven independent scopes compiled; P10 has two separate clean variants. No material blocker remained.
- P01A uses the director-delegated physical expression. P01B keeps all three locked observable relations in order.
- P03 presents listening through Lin’s eyeline and restrained response while keeping the entire human soundtrack silent.
- P04 selects one short nonlexical acknowledgement, `Mm.`, before `We can try tomorrow.`; the line remains verbatim.
- P10 compact is complete at 571 characters, so no meaning was removed to meet the cap.
- Validator PASS checks format, length, and registered ownership. The semantic checks above are a separate manual reading of the saved text; no generated take was available to assess adherence.
