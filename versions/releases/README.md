# Framewright Release Archive

This directory stores immutable, version-numbered Framewright release snapshots.

For every patch or feature release:

1. Preserve the current authoritative specification as its existing versioned snapshot before editing.
2. Increment the YAML `version` in the new authoritative specification.
3. Create a new immutable snapshot named `framewright-vX.Y.Z.md`.
4. Keep the desktop canonical file, desktop release snapshot, repository authoritative reference, and repository release snapshot byte-identical.
5. Update the repository README version, validate the Markdown and version metadata, then commit and push the same version to GitHub.

Never overwrite or repurpose an existing versioned snapshot.
