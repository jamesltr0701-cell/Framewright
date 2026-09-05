# Framewright 4.1.1 — Public Release Readiness Checklist

**Review date:** 2026-09-05

This checklist covers the GitHub presentation package. Items marked pending
still require an explicit human decision or external production step.

## Completed in this package

- [x] README follows the approved public-facing information hierarchy.
- [x] First-screen language states what Framewright is, how it differs from a
      generic prompt generator, and that the director remains authoritative.
- [x] `You direct. Framewright compiles.` is used as the primary product
      boundary statement.
- [x] Workflow explanation uses a branch structure, not a forced linear
      funnel.
- [x] Current model routes match the Framewright 4.1.1 image and runtime
      adapter registries.
- [x] Quick Start stays short and stage-oriented.
- [x] Personal-by-design language is present without turning into a disclaimer.
- [x] Design principles are limited to high-level orientation.
- [x] Maintainer details, repository policy, and versioning are moved below
      onboarding content.
- [x] `LICENSE`, `NOTICE`, and `THIRD_PARTY_NOTICES.md` distinguish original
      Framewright material from the identified adapted MIT material.
- [x] Tairan Li attribution is preserved for software/Skill redistribution,
      while no final-film credit requirement is introduced.
- [x] Hero Banner final brief is included.
- [x] Workflow Diagram final brief is included.
- [x] Generated Hero Banner final PNG, source SVG composition, and background
      plate are included under `docs/public-release/assets/`.
- [x] Workflow Diagram is included as a deterministic, README-safe SVG with
      accessible title and description.
- [x] Existing `PROVENANCE.md` remains the detailed source record for the
      adapted craft references.
- [x] Revised README information architecture is documented in
      [`readme-information-architecture.md`](readme-information-architecture.md).

## Required before public publication

- [ ] Have human legal counsel review the proposed Apache License 2.0 +
      Commons Clause combination, including whether the wording expresses the
      intended restriction on selling Framewright itself or a substantially
      Framewright-derived service.
- [ ] Confirm the named licensor, copyright ownership, contribution policy,
      and the exact scope of “original Framewright material.”
- [ ] Confirm that all contributors and third-party material in the release
      are accounted for before removing the draft markers from legal files.
- [x] Produce and add the final Hero Banner using
      [`hero-banner-brief.md`](hero-banner-brief.md).
- [x] Replace the README Mermaid draft with a rendered static diagram produced
      from [`workflow-diagram-brief.md`](workflow-diagram-brief.md), retaining
      an accessible text equivalent.
- [ ] Review the rendered GitHub README at desktop and narrow widths for
      Mermaid, table, link, and banner presentation.
- [ ] Reconfirm the release commit, tag, and `main` branch version are all
      `4.1.1` immediately before publication.
- [ ] After any manual change, rerun the repository checks and inspect the
      final diff for accidental internal paths, private assets, or unsupported
      model claims.

## Release boundary

The package is presentation-complete as a draft. It should be called publicly
ready only after the legal review, final visual asset step, and final GitHub
render/version checks above are complete.
