# Framewright Release Archive

This directory stores version-numbered Framewright release snapshots and preserved original release bytes.

Current release for director trial is [`framewright-v4.2.7.md`](framewright-v4.2.7.md), with recorded dialogue on Seedance 2.5 Omni Reference and body performance cues timed to the speaking or listening beat. The [v4.2.6 snapshot](framewright-v4.2.6.md) is the immediately preceding release. The [v4.2.5 snapshot](framewright-v4.2.5.md) and [v4.2.4 snapshot](framewright-v4.2.4.md) remain preserved. The [v4.2.3 package](https://github.com/jamesltr0701-cell/Framewright/tree/32769bce98bd32f8c160bdd3043b9be397682aa6) includes the Kling 4.0 Standard adapter and the November 7 update to the optional Ran director profile.
Rollback release: `framewright-v4.2.1.md`; the complete Skill is preserved by Git tag `v4.2.1`. Earlier snapshots and tags, including v4.2.0, remain intact.

The director explicitly requested the opening-anchor correction without changing v4.2.2. `framewright-v4.2.2.md` therefore reflects that correction; `framewright-v4.2.2-initial.md` and the existing `v4.2.2` tag preserve the original release. That correction carries forward into v4.2.3. This was a bounded exception to the normal immutable-snapshot policy, not a tag rewrite.

For every patch or feature release:

1. Preserve the current authoritative specification as its existing versioned snapshot before editing.
2. Increment the YAML `version` in the new authoritative specification.
3. Create a new immutable snapshot named `framewright-vX.Y.Z.md`.
4. Keep the desktop canonical file, desktop release snapshot, repository authoritative reference, and repository release snapshot byte-identical.
5. Update the repository README version, validate the Markdown and version metadata, then commit and push the same version to GitHub.

Outside the explicitly documented same-version correction above, never overwrite or repurpose an existing versioned snapshot. Preserved initial snapshots remain immutable.
