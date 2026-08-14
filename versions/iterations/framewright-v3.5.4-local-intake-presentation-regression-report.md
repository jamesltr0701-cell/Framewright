---
title: "Framewright v3.5.4 Local Intake Presentation Regression Report"
status: "DETERMINISTIC PASS"
report_date: "2026-08-14"
candidate_version: "3.5.4-local"
implementation_commit: "5e176fa88041a409d5184f8eb105bcfbc530fbc0"
intake_contracts_passed: 15
intake_contracts_total: 15
synthetic_cases_passed: 14
synthetic_cases_total: 14
existing_fixtures_passed: 78
existing_fixtures_total: 78
external_generation_calls: 0
credit_spend: 0
---

# Framewright v3.5.4-local 回归报告

## Frozen forward-test result

The unmodified `3f7b190` baseline covered `8 / 15` Intake contracts and `6 / 14`
synthetic cases. With the same frozen judge, candidate commit `5e176fa` covers:

- Intake contracts: `15 / 15`;
- synthetic cases: `14 / 14`;
- missing candidate contracts: `0`.

The judge ran with `--require-all`, so a missing contract produces a nonzero
exit. Judge hashes were verified after the candidate run.

## Existing regression

`sh testing/next-local/run_regression.sh` passed:

- Core / Skill / registry / both registered profiles: PASS;
- existing positive and deliberate-negative fixtures: `78 / 78` matched
  expectations;
- real temporary Core Native prompt path validation: PASS;
- `git diff --check`: PASS before the implementation commit.

No fixture was deleted, skipped, or converted from expected failure to expected
pass. The only protected-manifest changes were the candidate version and new
positive semantic anchors for the approved Intake contracts.

## Negative boundary checks

- modified path list contained only the four approved files;
- no external Seedance install path, `seedance-20` import, or external Skill
  runtime reference appeared in Framewright's active Skill/Core text;
- no runtime adapter profile or adapter registry changed;
- platform-neutral compiler ownership tests remained green;
- no generation service was called and no credit was spent.

## Evidence limitation

The new forward judge verifies explicit static contracts in the authoritative
Framewright text. It does not execute a live host conversation and therefore
does not prove response quality, tone, or perfect host obedience. That remains
the next review layer before promotion.
