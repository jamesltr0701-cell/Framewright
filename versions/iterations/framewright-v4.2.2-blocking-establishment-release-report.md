# Framewright v4.2.2 — blocking establishment release

Date: 2026-10-14. Base release: v4.2.1 (`a2f8de58b84b3a2e9754b12cbcb04f5c3ba1e96e`). The director approved installing this version, synchronizing the Desktop mirror, and publishing it to GitHub. The director reported that a visible shared arrangement can help later tighter views maintain character blocking, and requested this iteration.

## Resulting behavior

During shot planning, Framewright selectively checks whether dependent tighter views have an adequate visible spatial baseline. It first looks for an existing or motivated retained establishing view and recommends where it fits. A legible two-shot can suffice; a wide/master shot is not a quota. Where the finished sequence cannot accommodate that view, it may recommend a short removable setup, with 1–2 seconds as a starting suggestion only.

An accepted removable setup has a production function within the existing Shot Spine and generation strategy. It does not carry indispensable dialogue, reactions, action, or sound cues. Its ending matches the first retained shot's starting state, and the handoff distinguishes generated duration from retained edit duration and identifies the planned removal boundary. A locked opening, count, duration, continuous take, or generation boundary is preserved until an applicable decision allows a change.

Separate generations do not inherit an earlier wide shot's visual memory. A claimed visual anchor must be a specific accepted material, admitted for limited blocking authority and delivered through a supported route. Otherwise the active shot carries textual spatial relations and the remaining risk is disclosed. Identity-only portraits and planning-only boards are insufficient grounds to claim visual transfer. Reverse angles preserve world positions and eye-lines rather than mechanically copying screen-left/right; later position changes require current state evidence.

Detail sequences, already adequate views, and intentional concealment can pass without an added establishing shot. There is no new stage, mandatory board or image, state owner, reference role, prompt dialect, automatic generation, or validator schema.

## Source changes

- Core §7 routes relevant Blocking Readiness work to new §8.2.3.1. That section owns the selective establishment decision and its scope boundaries.
- Shot design admits the narrowly scoped production-function exception to Capture Necessity. AUTEUR guidance permits an assistant-facing technical remedy while preserving the supplied sequence.
- Generation routing and Video Prompt handoff carry the accepted setup's actual scope, timing, removal, and reference delivery. Existing semantic validation checks the result.
- Skill entrypoint, Core version, display label, release snapshot, and protected-baseline version agree on v4.2.2.
- Registered target adapters, validator code, personal profiles, production files, and previous immutable release snapshots are unchanged.

## Validation

Existing Core/protected-baseline and registered-profile checks pass. **140/140 regression fixtures** match their expected outcomes; **18 existing mutation/installation test groups** pass. Skill format validation and whitespace checks pass. These checks protect prior behavior and packaging; they do not evaluate the new creative recommendation by themselves.

Independent planning behavior review uses eight fictional [raw requests](../../testing/next-local/blocking_establishment_raw_requests.md). The reviewing agent receives only those requests and the candidate Skill's relevant references, without the patch diff, expected answers, historical prompts, or production inputs. It writes actual answers to a temporary directory. The parent reviews the answers against the request constraints. No prompt compilation or media generation is part of this planning test.

The [initial actual answers](../../testing/next-local/blocking-establishment/initial-review.md) meet the blocking-specific expectations in B01–B07. B08 correctly accounts for the 2-second removable setup, 14-second generation and 12-second edit, and keeps essential speech/sound out of the removable material. However, it calls the unspecified locked retained plan "three shots". That count is absent from B08's source and must not be treated as approved structure.

This observed gap prompted one narrow clarification in §10.1: reuse the actual approved retained plan; if unavailable, recommend only the setup/handoff and obtain the missing plan before freezing or compiling. Do not infer the retained count or redistribute its rhythm to accommodate a setup. The original answer is preserved, and a fresh independent agent reviews the unchanged B08 request in isolation after this clarification, without the earlier answers or diagnosis.

| Initial case | Parent observation |
| --- | --- |
| B01 | Retained two-shot establishes table, facing, door/window relation before close coverage; no duplicate production prelude. |
| B02 | Fixed count, opening and duration remain; optional setup is a pending decision, not an inserted fourth shot. |
| B03 | No establishing wide is added to the brush/paint detail sequence; contact and object-state continuity remain explicit. |
| B04 | No setup exposes the withheld person or geography; the genuine timing ambiguity of the voice reveal is surfaced. |
| B05 | Identity-only input is not treated as transferred visual blocking; the answer states the remaining risk and necessary axis information. |
| B06 | The admitted arrangement reference has limited spatial authority; the active close-up never acquires a wide opening or first-frame assignment. |
| B07 | The existing view carries the move and visibly lands on the new positions before tight coverage; later shots inherit the updated axis/state. |
| B08 | Removal, sound boundary and duration are correct; an unsupported retained-shot count is inferred. Partial result; clarified and retested. |

The [isolated B08 follow-up answer](../../testing/next-local/blocking-establishment/b08-followup-review.md) preserves 2 seconds of setup, 12 seconds of retained material and 14 seconds of generation. It does not assign a retained-shot count or add a reaction shot, requests the actual locked plan before freezing, and keeps the setup's cut, state and sound handoff explicit. The parent reviewed the actual saved answer as satisfactory for this request. [Assessment and artifact hashes](../../testing/next-local/blocking-establishment/validation.json) preserve both rounds.

The first eight cases share one independent reviewer; the follow-up uses a fresh reviewer and B08 alone. Each is a single planning sample. There is no baseline comparison, generated prompt test or measured media result, so the follow-up cannot establish general reliability or attribute all behavior differences to the clarification.

## Activation and limits

Promotion installs the validated v4.2.2 package and synchronizes the Desktop Core, supporting references, and immutable release snapshot. The repository and Desktop retain v4.2.1 and v4.2.0 snapshots. The `v4.2.1` Git tag and full pre-install package/Desktop backups provide rollback; restoring only the Core file is insufficient. A `v4.2.2` Git tag records the same package published on `main`. Local and live remote verification records are retained outside the public source tree.

Planning answers and passing existing tests cannot establish improved generated-video blocking continuity. Future production checks should compare position, facing, distance, eye-line, relevant object state, and cut continuity with and without the proposed visible baseline, using a defined generation scope. The proposed 1–2-second duration remains a practical starting point to test.
