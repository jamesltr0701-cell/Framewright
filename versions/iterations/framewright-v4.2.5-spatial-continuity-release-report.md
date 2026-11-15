# Framewright v4.2.5 — fixed-position spatial continuity

This patch keeps an approved room arrangement stable when a sequence changes camera direction or widens from a close view. Screen-left and screen-right are derived for each camera, while seats, landmarks, shared targets and anatomical sides retain their established relationships.

## Changes

- Core §8.2.3.1 derives camera views from the approved arrangement in the existing Production Spine. A cut or continuous camera path accounts for a changed observation direction. Widening, changed OTS foregrounds and newly revealed landmarks trigger a spatial review.
- The camera craft reference illustrates rear and face-facing views of two seated people. Foreground shoulders and backgrounds depend on the actual camera offset.
- Core §16.1 uses existing source-review fields to bind reviewed spatial relations to the affected final-text blocks. No new trace schema or validator geometry engine is introduced.

Blocking establishment remains selective. This patch does not require every generation to open with a wide shot. An adequate admitted spatial reference can support an approved face-only opening through the existing reference route. Model adapters and the optional director profile retain their existing content.

## Validation

The release passed the Core/package checks, all 140 regression fixtures, 18 existing source-review tests, 17 Kling adapter tests, and three prompt CLI smoke checks. Four added spatial source-review tests cover accepted evidence, post-review text drift, coverage of affected views, and the validator's semantic limit. The Skill metadata check also passed.

The added tests check exact text and scope. A geometrically wrong clause can still pass if its trace repeats the same wrong claim. Spatial compatibility therefore requires source-grounded semantic review before binding final spans. These tests do not demonstrate that the compiler will always make the right spatial decision.

No controlled video generation or independent blind comparison was performed for this patch. Improved generated-video continuity has not been measured. Earlier releases remain preserved for comparison and rollback.
