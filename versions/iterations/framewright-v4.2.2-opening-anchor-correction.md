# Framewright v4.2.2 — opening-anchor correction

Date: 2026-10-14. The director explicitly requested this bounded correction without a version-number change, with Source, Desktop mirror, installed Skill and GitHub synchronized. Base: `bda89ca6d7260f19603d31380f53236baa6d9aec`.

## Changed behavior

When an applicable generation unit needs a generated blocking anchor, that anchor occupies its **first shot**. An anchor belonging to an earlier generation or a wide view later in the same generation cannot substitute for this opening baseline. A retained establishing view is preferred; an accepted removable setup may instead precede the finished sequence. This is a planning rule, not measured evidence of model reliability.

A later move or swap still needs updated visible state before subsequent tight coverage. That re-establishment has a different job from the opening anchor. Detail sequences and intentionally withheld information retain the existing selective gate and director locks.

A single close-up can use an actual admitted spatial reference without a generated wide opening. If a generated wide-to-close setup is needed, approve the changed two-shot scope and resolve `edited_sequence_single_generation`; do not hide a second shot in `shot_by_shot` or a locked continuous take.

The entrypoint, Core shot-design rule, generation routing, handoff and semantic preflight now express the same opening requirement. Target adapters, validator schema/code, personal profiles and production assets are unchanged.

## Review and validation

The parent checked the changed rules against four concrete scope situations:

| Situation | Required decision under the corrected rule |
| --- | --- |
| A multi-shot job has two tight shots before its proposed establishing wide | Recommend an accepted opening anchor; do not count the later wide as the opening baseline or silently reorder locked shots. |
| A new generation continues a scene whose previous job already had a wide | Assess this job's incoming state; use its own opening generated anchor when needed, or an actual admitted spatial reference. Earlier output is not automatic visual memory. |
| Only one close-up is authorized, with a supported admitted blocking image | Keep one close-up and the image's limited spatial authority. Adding a generated wide requires a separately accepted two-shot scope and sequence strategy. |
| Characters change places after a valid opening two-shot | Keep the opening baseline and visibly carry the move's new end state or re-establish it before later tight shots. |

These are manual rule/scope checks, not new independent model samples. The earlier [eight planning cases and follow-up](framewright-v4.2.2-blocking-establishment-release-report.md) remain historical evidence for the initial release; they were not rerun or relabeled as validation of this correction. **140/140 existing regression fixtures**, **18 existing mutation/installation test groups**, Core/profile checks, Skill format and whitespace checks passed. Two unchanged historical prompt artifacts also passed the installed validator's ownership/source-review checks with only their temporary trace version updated; these test installation compatibility, not the new anchor decision. No media was generated and no continuity gain is claimed.

## Same-version packaging

The corrected Core and `versions/releases/framewright-v4.2.2.md` are byte-identical. The original snapshot is preserved as `versions/releases/framewright-v4.2.2-initial.md` and as the corresponding Desktop archive file. The existing `v4.2.2` Git tag retains its original commit; it is not force-moved. Download current `main` to obtain the corrected package. The version and Skill display name remain v4.2.2.

Full pre-correction source, installed-package and Desktop Core backups are kept locally. v4.2.1 and v4.2.0 snapshots and tags remain intact. Synchronization evidence identifies the actual corrected commit and hashes, because the shared version number alone cannot distinguish these two revisions.
