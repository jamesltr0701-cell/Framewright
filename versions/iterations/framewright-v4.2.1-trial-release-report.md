# Framewright v4.2.1 — Director trial release

Date: 2026-10-09. Base: v4.2.0 (`64c27759fe2b5cf3650b454e18b6a739436f3022`). The director requested that this patch become the active version for practical use, with v4.2.0 retained for rollback. Trial status describes the evidence boundary, not a separate compiler mode.

## Changes

- Core distinguishes a source-supported visible emotional transition from intentional ellipsis or withheld response. A later-shot constraint must not silently govern an earlier shot. Low-risk expression remains delegated; new dramatic meaning remains the director's decision.
- Camera returns compare with the same subject's earlier landing frame. A cumulative approach must not restart at the original distance, and different characters need not tighten symmetrically.
- Source-to-plan review precedes plan-to-final-text checks. Optional source-bound semantic evidence is localized to actual shot blocks; the `--source-review` flag requires that evidence. This extends the existing derived trace, with no new default user document or editable state owner.
- Explicit voice presentation remains attached to its existing vocal event: on-screen speech, off-screen speech, or voiceover, with the corresponding visible lip-sync relationship. Repeated content needs evidence for each approved occurrence. Voiceover over a visible face must not silently become on-screen speech. Legacy events remain valid.
- The validator resolves registered source paths from its own package root, so the same package works in a standalone Skill installation as well as the source repository. The package-prefix and path-containment checks remain enforced.
- Skill entrypoint and display label identify v4.2.1. Target adapters, personal director profiles, production projects and previously accepted creative artifacts are unchanged.

## Validation

- Existing regression fixtures: **140/140** matched expectations.
- New source-review, vocal-presentation and installation tests: **18 test groups passed**, including deletion, wrong-shot evidence, scope expansion, intentional omission, asymmetric camera returns, conflicting lip synchronization, repeated vocal occurrences and escaped source paths.
- Skill format and whitespace checks passed. The canonical Core and the new immutable v4.2.1 snapshot are byte-identical; the v4.2.0 snapshot is preserved.
- Two isolated compiler agents received only the current Skill and [raw requests](../../testing/next-local/v421_behavior_requests.md). One compiled a three-stage local revision sequence; the other compiled two voice/image cases. They did not read the patch diff, historical approved answers or each other's outputs. All five final prompts passed the current ownership-aware `video-prompt --source-review --trace` validator. The parent separately read the actual text and revalidated the saved artifacts.

| Test | Observed behavior |
| --- | --- |
| [R0](../../testing/next-local/v421-behavior/R0.txt) | Three fixed shots; first-shot smile; off-screen reply remains over the listener; second-shot head turn follows the complete line. |
| [R1](../../testing/next-local/v421-behavior/R1.txt) | Only the second-shot turn timing changes to overlap the line. First and third shot text remain identical. |
| [R2](../../testing/next-local/v421-behavior/R2.txt) | Only the third-shot expression changes to an already neutral state. First-shot smile and the revised second-shot timing remain intact. |
| [V](../../testing/next-local/v421-behavior/V.txt) | Remembered voiceover plays over a visible closed mouth; the next speaker's in-scene line has synchronized lips. |
| [O](../../testing/next-local/v421-behavior/O.txt) | The off-screen speaker stays unseen; the visible listener stays silent, then speaks with lip sync in the second shot. |

[Validation results and prompt hashes](../../testing/next-local/v421-behavior/validation.json) accompany the prompts and traces. Published traces normalize source locator paths to repository-relative paths; prompt bytes are unchanged.

The initial test harness omitted a supported text-only route assumption. Both agents stopped rather than invent a real surface capability. The fixture then explicitly supplied a hypothetical surface exposing `long_video`; no real platform availability or media generation was tested. One voice trace initially omitted ownership fields; the validator rejected it, the trace was corrected, and the prompt text did not change. Original local logs retain these failures.

Earlier exploratory prompt comparisons informed the source-review patch. They showed useful scene-specific differences but did not establish categorical superiority; private production inputs and the personal profile are not included in this release.

## Limits and rollback

One sample per case cannot establish general creative quality, revision reliability or generated-video adherence. The validator cannot independently authenticate source excerpts, discover all omitted meaning, or judge performance quality. More rules were not added for speculative timing, profile-learning or information-reveal problems.

Activation requires the source, Desktop Core and archive, installed Skill package, and GitHub `main` to match v4.2.1. A versioned Git tag records the release. The v4.2.0 tag preserves the entire previous Skill, including adapters and validator; rollback must restore the package and mirrors together, not only replace the Core Markdown. Pre-install Desktop and installed-package backups are retained locally. Production files and personal profiles are outside this rollback scope.
