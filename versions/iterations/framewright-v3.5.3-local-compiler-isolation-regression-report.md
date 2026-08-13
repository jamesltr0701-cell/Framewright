---
title: "Framewright v3.5.3 Local Compiler Isolation Regression Report"
status: "PASS"
report_date: "2026-08-14"
candidate_version: "3.5.3-local"
implementation_commit: "fe712d6"
fixtures_passed: 78
fixtures_total: 78
external_generation_calls: 0
credit_spend: 0
---

# Framewright v3.5.3-local 回归报告

## Deterministic results

- YAML runtime preflight: PyYAML `6.0.3`, PASS;
- baseline `sh testing/next-local/run_regression.sh`: Core PASS, `58 / 58` fixtures;
- validator Python syntax compile: PASS;
- final `sh testing/next-local/run_regression.sh`: Core / Skill / registry / both registered profiles PASS, `78 / 78` fixtures, real Core Native prompt path PASS;
- YAML parse: registry plus all 78 fixtures, `79 / 79` files PASS;
- `skill-creator` quick validation: `Skill is valid!`;
- `git diff --check`: PASS.

The suite increased by exactly 20 focused isolation fixtures. No prior fixture was deleted and no expected failure was weakened. Existing adapter fixtures were migrated to the required singular ownership metadata while preserving their original adapter behavior expectations.

## Direct real-file validation

A temporary Core Native prompt under `/private/tmp` passed:

```text
video-prompt PATH --target-model seedance_2_0 --serialization-owner framewright_core_native
```

Temporary prompt files were deleted after validation.

## Deliberate failures

Direct or focused fixture checks produced the intended nonzero result for:

- missing owner: `serialization_owner_missing`;
- unknown / external owner: `serialization_owner_unregistered` plus target mismatch;
- target / owner mismatch: `target_owner_mismatch`;
- foreign compiler source: `compiler_instruction_source_unregistered`;
- platform serializer field: `platform_serializer_forbidden`;
- plural, empty, and list-shaped owners;
- missing adapter ID or matching adapter profile contract;
- Core Native claiming an adapter;
- clean prompt ownership metadata leakage.

## Protected boundaries

Seedance 2.5 and MiniMax H3 profile hashes remained byte-identical to baseline. README, stable releases, historical artifacts, Rina/output paths, Desktop mirror, and GitHub were not changed. External generation calls and credit spend were zero.

This regression proves deterministic ownership isolation and contract enforcement. It does not prove target-model generation quality or runtime behavior.
