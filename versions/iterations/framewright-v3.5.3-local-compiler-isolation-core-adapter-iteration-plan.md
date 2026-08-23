---
title: "Framewright v3.5.3-local Compiler Isolation and Core-Adapter Architecture Iteration Plan"
document_version: "1.0"
status: "FORMAL PLAN / NOT IMPLEMENTED"
plan_date: "2026-08-13"
baseline_candidate_version: "3.5.2-local"
baseline_branch_at_planning_time: "codex/framewright-minimax-h3-adapter-experiment"
baseline_commit_at_planning_time: "d31b7a25bc6cb45af57bd20ee5f05f641529e70b"
proposed_target_candidate_version: "3.5.3-local"
proposed_target_branch: "codex/framewright-v3.5.3-local-compiler-isolation"
distribution_scope: "local candidate first; Desktop and GitHub require a later explicit approval gate"
external_generation_authorized: false
desktop_sync_authorized: false
github_sync_authorized: false
default_change_policy: "DENY UNLESS EXPLICITLY WHITELISTED"
language: "zh-CN"
---

# Framewright v3.5.3-local 编译隔离与 Core / Adapter Collection 架构迭代计划

## 0. 文档身份

本文是一份可以直接交给独立 iteration 对话执行的正式实施任务书。

本次迭代源于一次真实的编译边界事故：用户明确调用 Framewright 为 Seedance 2.0 编译 Rina 场景时，外部 `seedance-20` Skill 被语义隐性触发，其模板、平台表达和序列化习惯进入了本应由 Framewright 独占的编译过程。

本次迭代只解决这一类架构问题，并正式确立：

> Framewright 由稳定的 Core 与可选的 Adapter Collection 构成。Core 拥有导演逻辑与当前默认的原生序列化器；Adapter 只在用户明确选择对应目标模型时，翻译已经批准的 Core contract。模型决定序列化方言，平台不决定方言。

本文当前只是规划文件。创建本文不代表已经修改 Framewright 实现。

### 0.1 复制到 iteration 对话顶部的执行指令

```text
Read this entire iteration plan before acting, then execute it as a strict local-only Framewright architecture iteration.

Begin with Phase 0 live baseline verification. Treat the live repository as authoritative when it differs from the planning-time branch, commit, checksums, or fixture count. Do not overwrite or discard user changes. If tracked files within the whitelist are already modified, stop and report the overlap before editing.

Implement only the changes explicitly whitelisted by this plan. Preserve every unlisted Framewright behavior by default. Do not invoke, read, consult, or use the external seedance-20 Skill or any of its child skills during this iteration. The incident description in this document is sufficient evidence; the external Skill is not an implementation dependency.

Do not recompile or modify the Rina scene, its prompt, state file, generated video, or any project output. Do not create platform dialects, Jimeng prompts, LibTV prompts, or platform-specific Run Cards. Do not generate images, video, audio, or spend external credits.

Create a local candidate and run deterministic validation. Stop before Desktop synchronization, GitHub push, PR, merge, stable release creation, or release snapshot creation. Those distribution actions require a separate explicit approval. Do not call the Framewright update fully complete until local source, Desktop mirror, and the intended GitHub branch have later been synchronized and verified.

If implementation reveals a contradiction, required out-of-scope change, ambiguous ownership rule, or a need to weaken an existing regression, stop and write a concise decision report instead of resolving it silently.
```

### 0.2 Authorization boundary

When the user explicitly asks the iteration conversation to execute this plan, that authorizes edits only inside the local repository and only to files listed in the change whitelist below.

It does not authorize:

- invoking or reading the external `seedance-20` Skill or any child Skill;
- modifying `/Users/jameslee/.codex/skills/**`;
- modifying the Rina prompt, `framewright_state.yaml`, generated result, or any historical output;
- modifying `Framewright/`, `output/`, `outputs/`, or `storyboard/` untracked directories;
- generating storyboard, keyframe, image, video, or audio;
- using Jimeng, LibTV, Seedance, MiniMax, or another external generation service;
- spending credits;
- modifying the Desktop Framewright mirror;
- pushing, merging, opening a PR, or changing GitHub;
- modifying stable `main`;
- creating a stable release snapshot;
- describing `3.5.3-local` as a stable or distributed release.

---

## 1. Frozen planning baseline

### 1.1 Planning-time state

| Item | Planning-time value |
|---|---|
| Local repository | `/Users/jameslee/Documents/AI Filmmaking Studio/framewright` |
| Branch | `codex/framewright-minimax-h3-adapter-experiment` |
| Commit | `d31b7a25bc6cb45af57bd20ee5f05f641529e70b` |
| Core candidate | `3.5.2-local` |
| Existing runtime profiles | Seedance 2.5, MiniMax H3 |
| Existing deterministic result | `58 / 58` fixtures matched expectations |
| Tracked worktree changes | none observed at planning time |
| Existing untracked directories | present; preserve and do not touch |
| External generation calls for this plan | `0` |

Phase 0 must re-check every value. Planning-time values are evidence, not permission to reset live state.

### 1.2 Planning-time fingerprints

| File | SHA-256 |
|---|---|
| `skill/framewright/SKILL.md` | `55321834293818d953477cc247440470164f1c07a5681b8ee72d5af378a711e6` |
| `skill/framewright/references/framewright.md` | `5173b237ef3d12e1b04534f7a9487ca96d585a107edd43e9632d6d01aff48951` |
| `skill/framewright/references/runtime_profiles/seedance_2_5.md` | `829f615d92cc8179002450cf55758c14c09f7ca087b6a003678c2c9f7e2f9cbf` |
| `skill/framewright/references/runtime_profiles/minimax_h3.md` | `ff394b7b91b1fabb6f96f26cb995f22400a033b943da645b4c0d6a2c40093848` |
| `skill/framewright/scripts/validate_framewright.py` | `518ffa36e8d42e912ce43f4c717b929e69babc8ed50c71dfb98556048385f577` |
| `testing/next-local/expected/protected_anchors.yaml` | `088c23535b9e927b963b7d06a2dc49f91e607e2790f5fd767186ccd7cdf204d2` |
| `testing/next-local/run_regression.sh` | `db3882e85e46fa3f8f19159ac176bf720d2f388d5a6d9c1814f984324d178c71` |

If a checksum differs, inspect the diff. Never force the file back to the planning checksum.

### 1.3 Mandatory reading order

Read completely before editing:

1. this iteration plan;
2. `skill/framewright/SKILL.md`;
3. `skill/framewright/references/framewright.md`;
4. `skill/framewright/references/runtime_profiles/seedance_2_5.md`;
5. `skill/framewright/references/runtime_profiles/minimax_h3.md`;
6. `skill/framewright/scripts/validate_framewright.py`;
7. `testing/next-local/run_regression.sh`;
8. `testing/next-local/expected/protected_anchors.yaml`;
9. all current `testing/next-local/fixtures/*.yaml` that exercise serialization ownership, Seedance 2.5, or MiniMax H3;
10. the latest `3.5.2-local` implementation, regression, contradictions, and remaining-risk reports.

Do not read the external Seedance 2.0 Skill. This iteration is about Framewright-owned isolation, not importing or comparing external model guidance.

---

## 2. Incident diagnosis frozen for this iteration

The iteration must preserve the following distinction:

### 2.1 Root architecture failure

The Framewright compilation scope did not explicitly exclude external model-prompt Skills. As a result, an external Seedance 2.0 Skill became an undeclared instruction source and influenced serialization.

This is a compiler-isolation failure.

### 2.2 Separate planning failure discovered by the generated Rina result

The same Rina intake also failed to resolve Blocking Readiness before the Shot Spine froze. Dex appeared behind Rina, while Rina's final charge moved away from him.

This is a planning / blocking failure, not the compiler-isolation change being implemented here.

Current Framewright already specifies Causal State Completion and Blocking Readiness. Do not redesign those mechanisms in this iteration. Protect them with regression anchors, but do not use this iteration to add a blocking questionnaire, rewrite the Unified Director Intake, or recompile Rina.

### 2.3 Rina status

The user has already recompiled the current Rina scene through Core native fallback. Therefore:

- do not compile it again;
- do not revise its prompt;
- do not migrate its state file;
- do not treat its generated video as a new global model rule;
- use only the incident facts stated in this plan.

---

## 3. Architecture decision

### 3.1 Two-module product model

Formalize this logical architecture without performing a broad physical refactor:

```text
Framewright
├── Core
│   ├── Unified Director Intake
│   ├── Intent Ledger and Production Spine
│   ├── Causal State Completion and Blocking Readiness
│   ├── Visual Strategy and committed structure
│   ├── continuity, performance, sound, and reference authority
│   └── Core Native Serializer
│       └── current native target: Seedance 2.0
│
└── Adapter Collection
    ├── Seedance 2.5 Adapter
    └── MiniMax H3 Adapter
```

For this iteration, `framewright.md` remains the Core authority and `references/runtime_profiles/` remains the Adapter Collection. Do not split the 1,500-line Core specification merely to make the filesystem resemble the diagram.

### 3.2 Core is not identical to Seedance 2.0

Preserve this conceptual boundary:

- Framewright Core owns cinematic reasoning and approved production state.
- Core Native Serializer is one replaceable serialization component inside Core.
- Core Native Serializer currently targets Seedance 2.0.
- A future version may promote Seedance 2.5 or another model as the new native target without replacing Framewright's director logic.

Retire the term `core_fallback` in new architecture contracts. It incorrectly describes the normal default path as an emergency substitute.

Use:

```yaml
target_model: seedance_2_0
serialization_owner: framewright_core_native
```

### 3.3 Adapter ownership

Use model-level adapter ownership, not route-level ownership:

```yaml
target_model: seedance_2_5
serialization_owner: framewright_adapter_seedance_2_5
adapter_id: seedance_2_5
```

```yaml
target_model: minimax_h3
serialization_owner: framewright_adapter_minimax_h3
adapter_id: minimax_h3
```

Seedance routes such as `omni_reference`, `smart_edit`, or `extend` remain internal choices made by the Seedance 2.5 Adapter. They are not serialization owners.

### 3.4 Model routing contract

Freeze the routing table:

| Director request | Target model | Serialization owner | Adapter loaded |
|---|---|---|---|
| no model specified | `seedance_2_0` | `framewright_core_native` | none |
| explicit Seedance 2.0 | `seedance_2_0` | `framewright_core_native` | none |
| explicit Seedance 2.5 | `seedance_2_5` | `framewright_adapter_seedance_2_5` | Seedance 2.5 only |
| explicit MiniMax H3 | `minimax_h3` | `framewright_adapter_minimax_h3` | MiniMax H3 only |
| unsupported or ambiguous future model | unresolved | none | none; ask or stop |

An unsupported model must never trigger an external Skill as an undeclared fallback.

### 3.5 Platform neutrality

Freeze the following rule:

> The selected model determines serialization. The execution platform does not determine serialization.

Therefore:

- Jimeng and LibTV must not select different prompt dialects for the same target model;
- a user saying “I will use Jimeng” must not activate a Jimeng prompt template;
- a user saying “I will use LibTV” must not activate a LibTV prompt template;
- platform name, UI layout, upload order, chip label, provider route, and website wording must not become model-facing semantics;
- the same approved Production Spine and target model must select the same serialization owner and schema on every platform;
- UI binding differences may be explained operationally only when needed, but they are not a Framewright dialect.

Do not create a platform registry, platform adapter, Jimeng serializer, LibTV serializer, `platform_dialect`, or `surface_serializer` field.

### 3.6 Run Card boundary

Do not create platform-specific Run Cards.

Do not require a Run Card for Core Native output merely because the user names a platform.

Preserve the existing adapter-facing assistant handoff only where the selected model adapter genuinely needs model-specific information such as:

- task route;
- model input roles;
- duration or aspect-ratio provenance;
- native material-label mapping;
- model capability or execution risk.

This handoff remains outside `prompt_video.txt`. It may not contain or imply a Jimeng dialect, LibTV dialect, or platform-specific rewrite. Avoid a broad Run Card rename in this iteration unless a concrete contradiction makes the existing term unusable; if so, stop for a naming decision.

---

## 4. Compiler Isolation contract

### 4.1 Framewright-exclusive compilation scope

When the user explicitly invokes Framewright or asks Framewright to compile an artifact:

1. Framewright owns the full intake, planning, routing, and serialization scope.
2. Load Framewright Core completely.
3. For Video Prompt, load at most one Framewright-owned Adapter and only after explicit target-model selection.
4. Do not invoke, read, consult, or apply an external model-prompt Skill merely because its model name appears.
5. Do not allow an external Skill to supply headings, timelines, reference syntax, negative templates, platform syntax, or prompt rewriting.
6. Do not merge two serialization schemas.

### 4.2 Explicit external consultation exception

If the user explicitly asks to compare Framewright with an external Skill:

- external material may be inspected only for the requested comparison;
- it remains advisory evidence;
- it receives no serialization ownership;
- it must not directly rewrite the clean Framewright prompt;
- incorporating a useful rule into Framewright requires a separate approved Core or Adapter iteration.

If an external prompt Skill is accidentally loaded during an active Framewright compilation scope, stop before saving the model-facing artifact, disclose the contamination, and restart the compile pass from Framewright-owned instructions only. Do not claim clean isolation while silently retaining external serialization authority.

### 4.3 Allowed compiler instruction sources

For one Video Prompt compilation, the instruction-source whitelist is:

- `skill/framewright/SKILL.md`;
- `skill/framewright/references/framewright.md`;
- the single selected profile under `skill/framewright/references/runtime_profiles/`, when an Adapter is active;
- the new Framewright-owned Adapter registry;
- current user decisions, approved state, admitted assets, and project-local Framewright artifacts as scene inputs rather than compiler specifications.

External model Skills are not compiler instruction sources.

### 4.4 Clean-prompt boundary

`target_model`, `serialization_owner`, `adapter_id`, compiler-source provenance, platform, Run Card data, and validation diagnostics remain internal or assistant-facing. They must not enter the clean model-facing prompt unless a model genuinely requires one of its own native labels.

---

## 5. Change whitelist

### WP-01 — Phase 0 audit and branch safety

Before editing:

1. record live branch, commit, status, tracked changes, and untracked paths;
2. run the existing regression suite and record the exact baseline count;
3. preflight the YAML interpreter with `import yaml`;
4. compare live fingerprints with this plan;
5. inspect the current repository for a root `AGENTS.md`;
6. create or switch to a new `codex/` branch only after confirming it will not discard user work.

Recommended branch:

```text
codex/framewright-v3.5.3-local-compiler-isolation
```

If tracked whitelist files are already modified, stop and report. Preserve all unrelated and untracked content.

### WP-02 — Formalize the Adapter Collection registry

Create one Framewright-owned deterministic registry, recommended path:

```text
skill/framewright/references/runtime_profiles/adapter_registry.yaml
```

Minimum conceptual content:

```yaml
schema_version: "1.0"
core_native:
  target_model: seedance_2_0
  serialization_owner: framewright_core_native
  profile: null
adapters:
  seedance_2_5:
    target_model: seedance_2_5
    serialization_owner: framewright_adapter_seedance_2_5
    profile: seedance_2_5.md
  minimax_h3:
    target_model: minimax_h3
    serialization_owner: framewright_adapter_minimax_h3
    profile: minimax_h3.md
```

Requirements:

- this registry is the one validator whitelist source;
- do not duplicate the owner whitelist in multiple Python constants unless bootstrap validation strictly requires it;
- do not include platforms;
- do not include external Skill paths;
- profile paths must resolve inside Framewright;
- exactly one Core Native target exists;
- each adapter has one unique target, owner, and profile;
- no route name may masquerade as an owner.

### WP-03 — Update `SKILL.md` with Compiler Isolation

Modify `skill/framewright/SKILL.md` narrowly:

- add a concise `Compiler Isolation` rule near required-reference or tool-boundary instructions;
- state that explicit Framewright use creates a Framewright-exclusive compiler scope;
- identify Core Native as the default Seedance 2.0 route;
- load no adapter for Seedance 2.0;
- load exactly one internal profile only for explicit Seedance 2.5 or MiniMax H3 selection;
- forbid automatic invocation or use of external model-prompt Skills;
- state that platforms cannot select dialects;
- require validation with explicit target model and serialization owner before saving Video Prompt output;
- keep detailed registry schema in the registry/Core reference rather than bloating `SKILL.md`.

Do not change the Framewright trigger description to trigger on every generic Seedance request. Framewright remains explicit opt-in.

### WP-04 — Add project-level `AGENTS.md`

No repository-root `AGENTS.md` existed at planning time. If it is still absent, create:

```text
/Users/jameslee/Documents/AI Filmmaking Studio/framewright/AGENTS.md
```

It must contain only concise project-level execution boundaries needed by future agents:

- Framewright is the exclusive compiler when explicitly invoked;
- generic model-name matching does not authorize external prompt Skills;
- `seedance-20` and its children must not be invoked or used during Framewright work unless the user explicitly requests an external comparison;
- explicit comparison remains advisory and cannot become serialization ownership;
- target model, not platform, selects serialization;
- only Framewright Core Native or a registered Framewright Adapter may own serialization;
- do not modify or invoke ChatCut, OpenMontage, or generation services without explicit permission;
- preserve project-local output and user changes;
- use the declared project or approved shared YAML runtime for validator work.

Do not copy large sections of `SKILL.md` into `AGENTS.md`. It is a repository guardrail, not a second specification.

### WP-05 — Update Core target and routing semantics

Modify `skill/framewright/references/framewright.md` narrowly:

1. bump the local candidate version to `3.5.3-local` only after implementation begins;
2. replace ambiguous default metadata such as `video_target_model_default: "Seedance"` with explicit Seedance 2.0 Core Native metadata;
3. list Seedance 2.0, Seedance 2.5, and MiniMax H3 with distinct native/adapter roles;
4. formalize Core versus Adapter Collection ownership;
5. replace new uses of `core fallback` with `Core Native` without rewriting historical reports;
6. declare the routing table in Section 13;
7. declare platform neutrality;
8. constrain model-specific assistant handoff so it cannot become a platform dialect;
9. require one explicit serialization owner in internal validation for every Video Prompt;
10. keep Director Mode, scene grammar, Production Spine, Blocking Readiness, reference authority, and all creative locks above serialization.

Do not alter the current Core Native prompt headings or rewrite Seedance 2.0 wording merely to demonstrate the new architecture. This is an ownership iteration, not a prompt-style iteration.

### WP-06 — Strengthen deterministic validator ownership

Modify `skill/framewright/scripts/validate_framewright.py` so that Video Prompt validation cannot pass without a valid owner.

#### Required schema behavior

Use singular scalar ownership:

```yaml
target_model: seedance_2_0
serialization_owner: framewright_core_native
adapter_id: null
compiler_instruction_sources:
  - skill/framewright/SKILL.md
  - skill/framewright/references/framewright.md
```

Requirements:

- `serialization_owner` is required for Video Prompt compile validation;
- it must be a non-empty scalar string, not an optional list;
- the owner must exist in `adapter_registry.yaml`;
- `target_model` is required and must match the registered owner;
- Core Native must reject a non-null `adapter_id`;
- Adapter owners must require the exact matching `adapter_id`;
- an Adapter owner must require its matching profile contract and reject another adapter's contract;
- multiple or list-shaped owners fail;
- unknown owners fail;
- route names such as `seedance_omni_reference` fail as owners;
- external owners such as `seedance_20_skill` fail;
- non-whitelisted compiler instruction sources fail;
- fields that claim platform-controlled serialization, such as `platform_dialect` or `surface_serializer`, fail;
- prompt text remains free of ownership metadata.

#### Actual artifact validation

Do not limit the new checks to synthetic fixtures. Add or extend a deterministic command that validates a real Video Prompt path with target and owner, for example:

```bash
/Users/jameslee/Documents/Codex/_shared-tools/python/yaml-runtime/bin/python \
  skill/framewright/scripts/validate_framewright.py video-prompt PATH \
  --target-model seedance_2_0 \
  --serialization-owner framewright_core_native
```

Equivalent CLI design is acceptable if it provides the same hard guarantee. The existing generic `prompt` validator may remain for Storyboard and Keyframes, but the Framewright workflow must use the ownership-aware command for Video Prompt.

The registry path should resolve deterministically from the Framewright package unless the test harness explicitly injects a fixture registry.

#### Migration rule

Current fixtures use plural `serialization_owners` in a few places and sometimes use route names as owners. Migrate only fixtures whose purpose includes serialization ownership or model-adapter qualification. Preserve their creative and adapter test meaning.

Do not weaken unrelated fixtures merely to avoid adding required test context.

### WP-07 — Protected anchors

Update `testing/next-local/expected/protected_anchors.yaml` with concise anchors for:

- `framewright_core_native`;
- `framewright_adapter_seedance_2_5`;
- `framewright_adapter_minimax_h3`;
- Seedance 2.0 as current Core Native target;
- explicit Framewright compiler exclusivity;
- platform neutrality;
- one owner per Video Prompt;
- external advisory material cannot own serialization;
- Blocking Readiness remains required before committed structure freezes.

Do not remove existing protected anchors unless the exact old wording is replaced by an approved semantically stronger anchor. Record every replacement in the implementation report.

### WP-08 — Deterministic regression fixtures

Add focused fixtures with at least these cases.

#### Passing cases

1. no model supplied resolves to Seedance 2.0 Core Native;
2. explicit Seedance 2.0 uses Core Native with no adapter;
3. explicit Seedance 2.5 uses only the Seedance 2.5 Adapter owner;
4. explicit MiniMax H3 uses only the MiniMax H3 Adapter owner;
5. the same Seedance 2.0 compile contract remains valid regardless of an assistant-facing Jimeng or LibTV execution note, with no platform field affecting serialization;
6. Core Native prompt validation passes through the real-path ownership-aware command.

#### Deliberate failure cases

1. missing `serialization_owner`;
2. owner supplied as an empty value;
3. owner supplied as a list or multiple owners;
4. unknown owner;
5. `seedance_omni_reference` used as an owner;
6. `seedance_20_skill` or another external Skill used as an owner;
7. Seedance 2.0 paired with the Seedance 2.5 Adapter owner;
8. Seedance 2.5 paired with Core Native;
9. MiniMax H3 paired with the Seedance 2.5 Adapter;
10. Adapter owner without matching `adapter_id` or profile contract;
11. Core Native with an adapter ID;
12. non-whitelisted compiler instruction source;
13. `platform_dialect`, `jimeng_serializer`, `libtv_serializer`, or equivalent platform ownership field;
14. ownership metadata leaking into the clean prompt.

Keep these tests compile-only. Do not call a model.

### WP-09 — Preserve Adapter profiles

The Seedance 2.5 and MiniMax H3 profiles are protected by default.

Do not modify their model capability, route, syntax, timing, sound, reference, or prompt schemas in this iteration.

A profile may receive only the smallest ownership-frontmatter clarification if the registry cannot otherwise validate its identity. Prefer leaving both profile files byte-identical and placing ownership in the registry.

If profile content must materially change, stop and request an explicit scope expansion.

### WP-10 — Documentation and reports

After implementation, create concise iteration evidence under `versions/iterations/`:

- `framewright-v3.5.3-local-compiler-isolation-implementation-report.md`;
- `framewright-v3.5.3-local-compiler-isolation-regression-report.md`;
- `framewright-v3.5.3-local-compiler-isolation-remaining-risk-report.md`.

Reports must state:

- live baseline and final commit/branch;
- exact changed files;
- exact registry and owner mapping;
- baseline and final fixture counts;
- all commands run and pass/fail outcomes;
- whether adapter profiles remained byte-identical;
- whether any external Skill was read or invoked;
- external generation calls and credit spend, both expected to be zero;
- untracked paths preserved;
- Desktop and GitHub synchronization status;
- why the update remains local-candidate-only until all required locations are synchronized.

Do not modify `README.md`, stable release documentation, or historical iteration reports as part of this local candidate.

---

## 6. Explicit file whitelist

### May create

- `AGENTS.md` at repository root, if still absent;
- `skill/framewright/references/runtime_profiles/adapter_registry.yaml`;
- new focused fixtures under `testing/next-local/fixtures/`;
- the three `3.5.3-local` implementation/regression/risk reports listed above.

### May modify

- `skill/framewright/SKILL.md`;
- `skill/framewright/references/framewright.md`;
- `skill/framewright/scripts/validate_framewright.py`;
- `testing/next-local/expected/protected_anchors.yaml`;
- only existing fixtures directly requiring ownership-schema migration;
- `testing/next-local/run_regression.sh` only if necessary to exercise the ownership-aware real-path command.

### Protected and must remain untouched

- `skill/framewright/references/runtime_profiles/seedance_2_5.md`, except the narrow WP-09 exception;
- `skill/framewright/references/runtime_profiles/minimax_h3.md`, except the narrow WP-09 exception;
- `skill/framewright/agents/openai.yaml`, unless a final validation proves its existing UI description materially false;
- `README.md`;
- `docs/**`;
- `versions/releases/**`;
- all historical iteration files;
- all user outputs and project artifacts;
- `Framewright/**`;
- `output/**`;
- `outputs/**`;
- `storyboard/**`;
- the Rina scene and generated result;
- Desktop mirror;
- remote repository and GitHub branches.

If a required change falls outside this whitelist, stop and report.

---

## 7. Protected behavior manifest

Every behavior below remains unchanged unless this plan explicitly says otherwise:

- one workflow and one user entry;
- Storyboard, Keyframes, and Video Prompt as the only stages;
- AUTEUR, APPRENTICE, and SCREENWRITER as the only Director Modes;
- kinetic, observational, and conversational scene grammar;
- Unified Director Intake and dependency-sensitive questioning;
- Intake Hard Stop;
- one current approved Production Spine;
- nested Intent Ledger authority;
- Causal State Completion;
- Blocking Readiness before committed structure freezes;
- Visual Strategy and committed Shot / Phase Spine ownership;
- explicit user decisions above every inference and adapter;
- no automatic generation-unit split or merge;
- property-scoped material authority;
- storyboard planning-only default;
- one GU / one Storyboard board;
- prompt-only Keyframes and Video Prompt by default;
- one initial Storyboard generation exception only;
- semantic timing default;
- hard-cut edited-sequence default;
- continuous-take phases are not cuts;
- observable performance carriers;
- generated environmental ambience and synchronized diegetic effects;
- no music unless explicitly requested;
- no invented dialogue or narration;
- no automatic image, video, or audio generation;
- no ChatCut or OpenMontage use without explicit permission;
- no historical state backfill;
- no modification of existing output artifacts merely because the Core version changes.

---

## 8. Validation protocol

### 8.1 YAML runtime preflight

Use the approved shared runtime because the project currently has no declared isolated Python environment for the validator:

```bash
/Users/jameslee/Documents/Codex/_shared-tools/python/yaml-runtime/bin/python -c "import yaml; print(yaml.__version__)"
```

Do not install PyYAML globally or switch parsers silently.

### 8.2 Static checks

Run at minimum:

- YAML parsing for the new registry and all fixtures;
- Python syntax compilation for the validator;
- Framewright Core validator with the new candidate version and registry;
- Markdown fence-balance validation;
- protected-anchor validation;
- Skill folder validation if the available `skill-creator` tooling can validate this nonstandard repository path without mutation.

### 8.3 Regression

Run the existing suite before edits and the expanded suite after edits:

```bash
bash testing/next-local/run_regression.sh
```

Success requires:

- every pre-existing fixture still matches its expected result;
- every new isolation fixture matches its expected result;
- the suite count increases by exactly the number of added fixtures;
- no failure expectation is weakened to manufacture a pass;
- no model generation occurs.

### 8.4 Direct real-file validation

Create a temporary minimal Core Native Video Prompt in `/private/tmp` or another approved temporary directory. Validate it using the new ownership-aware command.

Also confirm deliberate failures for:

- missing owner;
- unknown owner;
- owner/target mismatch;
- external compiler source;
- platform serializer field.

Delete only temporary test artifacts created by the iteration. Do not delete any user output.

### 8.5 Repository diff review

Before reporting completion:

1. inspect `git diff --check`;
2. inspect the complete diff, not only filenames;
3. confirm no protected file changed;
4. confirm no output or Rina artifact changed;
5. confirm adapter profiles are byte-identical unless the narrow exception was approved;
6. confirm no platform dialect exists;
7. confirm no external Skill content was copied into Framewright;
8. confirm all new owner names come from the registry;
9. confirm the clean prompt contains no compiler metadata.

---

## 9. Acceptance criteria

The local candidate passes only when all statements below are true.

### Architecture

- Framewright exposes one Core and one Adapter Collection architecture.
- Core Native is the normal default, not a fallback.
- Seedance 2.0 is explicitly the current Core Native target.
- Seedance 2.5 and MiniMax H3 remain subordinate internal adapters.
- future target promotion can change the native serializer without redefining director logic.

### Isolation

- explicit Framewright use excludes implicit external prompt-Skill participation;
- project `AGENTS.md` reinforces the boundary;
- external consultation cannot become serialization ownership;
- an unsupported model stops or asks instead of invoking an external fallback.

### Routing

- target model is explicit in compile validation;
- every Video Prompt has exactly one scalar `serialization_owner`;
- owner and target must match the registry;
- adapter and route identities are not conflated;
- no adapter is loaded for Seedance 2.0 Core Native;
- exactly one adapter is loaded for an explicit supported adapter target.

### Platform neutrality

- Jimeng and LibTV cannot select different Framewright dialects for the same model;
- no platform serializer or dialect field exists;
- no platform-specific prompt or Run Card is created;
- model-specific adapter handoff remains allowed only for actual model contracts.

### Validation

- missing, multiple, unknown, external, mismatched, and route-level owners fail;
- foreign compiler instruction sources fail;
- platform-controlled serialization fields fail;
- actual Video Prompt file validation requires target and owner;
- all baseline and new fixtures pass their expectations;
- adapter profiles retain their existing model behavior;
- no clean prompt contains ownership metadata.

### Scope and safety

- Rina is not recompiled or modified;
- no historical output or state is migrated;
- no image, video, or audio is generated;
- external generation calls: `0`;
- external credits spent: `0`;
- no Desktop or GitHub mutation occurs;
- untracked user content is preserved.

---

## 10. Stop-and-report conditions

Stop the affected work package and request a decision if:

- live tracked changes overlap a whitelisted file;
- the current branch or commit contains unreviewed work that the new branch would obscure;
- Core Native Seedance 2.0 wording cannot be separated from an external Skill without rewriting prompt behavior;
- the registry would require platform entries;
- a target model needs two simultaneous serialization owners;
- the validator cannot enforce ownership on actual prompt files without a materially broader CLI redesign;
- adapter profile semantics must change;
- Blocking Readiness changes become necessary to pass isolation tests;
- a baseline fixture must be deleted or weakened;
- implementation requires modifying outputs, Rina, Desktop, GitHub, or release snapshots;
- a real generation call appears necessary;
- any ambiguity would change user-visible Framewright behavior beyond compiler ownership.

The decision report should contain only:

1. evidence;
2. exact conflict;
3. smallest viable options;
4. affected files and contracts;
5. recommendation;
6. what remains safely completed.

---

## 11. Delivery and synchronization boundary

At the end of this plan, deliver a local candidate only.

Report it as:

```text
Framewright v3.5.3-local local candidate implemented and validated.
Distribution remains incomplete: Desktop mirror and intended GitHub branch have not yet been synchronized.
```

Do not call the version update complete until a later, explicitly authorized distribution phase verifies all three locations:

1. `/Users/jameslee/Documents/AI Filmmaking Studio/framewright`;
2. `/Users/jameslee/Desktop/AI Filmmaking/01 Creative Systems/Framewright`;
3. `jamesltr0701-cell/framewright` on the intended branch.

That later phase must preserve older immutable release snapshots and verify version metadata plus byte identity or SHA-256 for the intended Core, Adapter registry, runtime profiles, Skill entrypoint, validator, and protected regression assets.

---

## 12. Final implementation report template

```text
OUTCOME
[Local candidate result.]

BASELINE
- branch / commit:
- candidate version:
- baseline regression:
- tracked and untracked state:

ARCHITECTURE
- Core Native target:
- Adapter registry:
- serialization owners:
- platform-neutrality result:

FILES
- created:
- modified:
- protected and byte-identical:

VALIDATION
- YAML preflight:
- Core validation:
- regression result:
- direct Video Prompt validation:
- deliberate failure checks:
- git diff checks:

BOUNDARIES
- external Skills read or invoked:
- external generation calls:
- credit spend:
- Rina / outputs touched:
- Desktop sync:
- GitHub sync:

REMAINING RISK
[Only genuine residual risk.]

STATUS
LOCAL CANDIDATE COMPLETE / DISTRIBUTION INCOMPLETE
```
