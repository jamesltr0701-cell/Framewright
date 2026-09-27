# Framewright v4.2.0 candidate — Seedance 2.0 evaluation

Seven requested independent scopes were compiled sequentially in APPRENTICE MODE from this candidate's Core and Seedance 2.0 adapter. Each prompt is text only, one continuous 8-second 16:9 shot, without runtime references or a storyboard. All saved prompts passed the ownership-aware `video-prompt` validator with a current-scope trace. No scope required a `BLOCKED.md`. No media was generated; model adherence remains untested.

| Scope | Artifact | Characters | Result |
|---|---|---:|---|
| P01A | `P01A/prompt_video.txt` | 643 | PASS |
| P01B | `P01B/prompt_video.txt` | 647 | PASS |
| P02 | `P02/prompt_video.txt` | 898 | PASS |
| P03 | `P03/prompt_video.txt` | 790 | PASS |
| P04 | `P04/prompt_video.txt` | 681 | PASS |
| P07 | `P07/prompt_video.txt` | 816 | PASS |
| P10 | `P10/prompt_video.txt` | 928 | PASS |
| P10 | `P10/prompt_video_compact.txt` | 563 | PASS |

P10 compact cap: 600 characters; actual: 563. The cross-target P02 note in `requests.md` was outside the requested Seedance 2.0-only sequence. Per-case evidence and exact validation traces are saved beside each prompt.
