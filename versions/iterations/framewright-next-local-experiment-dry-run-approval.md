---
title: "Framewright Next Local Experiment Dry-Run Approval Package"
document_version: "1.2"
status: "CORE EXECUTION AUTHORIZED - LOCAL CANDIDATE IMPLEMENTED"
dry_run_date: "2026-08-13"
stable_baseline: "3.5.0"
baseline_commit: "35e529c2fcef3c03c9b19569f138db997d9f84ce"
experimental_branch: "codex/framewright-next-local-experiment"
branch_upstream: "none"
working_candidate_label: "3.5.1"
approved_work_packages: "WP-A through WP-G"
excluded_work_packages: "WP-H and WP-I"
core_modification_authorized: true
external_generation_authorized: false
desktop_sync_authorized: false
github_push_authorized: false
language: "zh-CN"
---

# Framewright 下一轮本地实验 Dry-Run 审批包

## 0. 审批与执行状态

本文件最初作为实际修改前审批包创建。以下 dry-run 工作已经完成并获批：

- 复核 Framewright 3.5.0 live 基线；
- 创建未推送本地实验分支；
- 将已批准的 WP-A–G 映射到现有 Framewright 权威结构；
- 提出 schema、validator、fixture、冲突、冗余与澄清方案。

获批后，本地实验分支已经实施 WP-A–G。以下边界仍未修改：

- README、release snapshot、Desktop mirror 或 GitHub；
- 任何历史 Prompt、项目文件或生成媒体。

实施、回归与剩余风险证据分别记录于：

- `versions/iterations/framewright-v3.5.1-local-candidate-implementation-report.md`；
- `versions/iterations/framewright-v3.5.1-local-candidate-regression-report.md`；
- `versions/iterations/framewright-v3.5.1-local-candidate-remaining-risk-report.md`。

候选仍未发布、未同步、未外部生成。

## 1. Live baseline 与恢复锚点

### 1.1 Git 状态

| Item | Live value |
|---|---|
| Stable branch at start | `main` |
| Stable / remote commit | `35e529c2fcef3c03c9b19569f138db997d9f84ce` |
| Experimental branch | `codex/framewright-next-local-experiment` |
| Upstream | none |
| Push status | not pushed |
| Stable version | `3.5.0` |

### 1.2 Frozen fingerprints

| File | SHA-256 |
|---|---|
| `skill/framewright/SKILL.md` | `c3621e6073b5bee71d1c5e6d7fa48575604ca86b84859164e8959d6fae030ab8` |
| `skill/framewright/references/framewright.md` | `c9d0073b1ac56294689b829f0deb79151e3b8356096d978ba29eb6b984ab6038` |
| `skill/framewright/references/runtime_profiles/seedance_2_5.md` | `57bf7fcb0e23193ae09354b710542136dc284efc642cff06cff04470aca158a5` |
| `versions/releases/framewright-v3.5.0.md` | `c9d0073b1ac56294689b829f0deb79151e3b8356096d978ba29eb6b984ab6038` |
| `README.md` | `1fb7a2183e719a40f9aa9b44fb9fc2cc6b61bcdf5730dd2ba7d10508d9cf80eb` |
| Desktop `Core MD/Framewright.md` | `c9d0073b1ac56294689b829f0deb79151e3b8356096d978ba29eb6b984ab6038` |
| Desktop v3.5.0 release snapshot | `c9d0073b1ac56294689b829f0deb79151e3b8356096d978ba29eb6b984ab6038` |

### 1.3 冻结的工作区内容

以下既有未追踪目录不读取为规范、不纳入 Git、不修改、不清理：

- `Framewright/`
- `output/`
- `outputs/`
- `storyboard/`

恢复方式：实验未晋升时，切回 `main` 即恢复稳定 3.5.0；不删除实验分支，不覆盖历史证据。

## 2. 已批准范围与本轮排除项

### 2.1 进入本地实验

- WP-A：Operational Enforcement 与 Revision-State Persistence
- WP-B：Observable Intent 与 Embodied Performance Translation
- WP-C：Attention / Temporal Feasibility 与 Structural Subtraction Safety
- WP-D：Embodied Camera 与 Motion-State Carryover
- WP-E：Physical Causality 与 Transformation Topology
- WP-F：Reference Conditioning Risk Gate
- WP-G：Dialogue Event 与 Silence Ownership

### 2.2 明确排除

- WP-H：Evidence Normalization 与自动学习实现；
- WP-I：Seedance route qualification；
- 任何 Seedance、图像或视频生成；
- Timing Proof / animatic；
- Keyframe 产品定位修改；
- mixed grammar、完整 camera / subject / world 三分轨；
- multi-model adapter；
- 自动 repair memory；
- 正式 release、Desktop sync 或 GitHub push。

## 3. Dry-run section map

### 3.1 Core authority map

| Work package | Existing owner | Proposed change type | New parallel owner? |
|---|---|---|---|
| WP-A | §2 Scope and State; §7 Production Spine; §15 File Output; §16 Validation; §17 Boundary | extend + narrow exception | no |
| WP-B | §7 `performance_progression`; §8.7 Compression; §8.11 Performance Vitality; §13 Video Prompt; §16.1 Preflight | extend | no |
| WP-C | §6.1 Visual Strategy; §8.7 Compactness; §8.9 Feasibility; §8.9.1 Timing; §16.1 Rationale Conflict | extend | no |
| WP-D | §7 `camera_logic` and continuity; §8.4 Dramatic Camera; §8.9.1 continuous take; §13 Video Prompt | extend | no |
| WP-E | §7 `object_state_progression`; §8.6 Count / State; §8.7 Compression; §13 Video Prompt | extend | no |
| WP-F | §8.2.2 Storyboard Asset Use; §9 Reference Policy; Silent Reference Exclusion; Runtime Attachments | extend | no |
| WP-G | §7 `sound_contract`; §8.12 Sound; §13 Video Prompt; §16 Validation | extend | no |

### 3.2 Seedance adapter map

| Work package | Existing adapter owner | Proposed change |
|---|---|---|
| WP-D | §5 Task Router; §6 task schemas; §10 Advanced Feasibility | serialize relevant optical / motion handoff only |
| WP-F | §4 Material Registry Bridge; §7 Storyboard Admission; §10 Advanced Feasibility | serialize approved admission strategy; never choose assets silently |
| WP-G | §9 Sound and Visible-Text Policy; §12 Runtime Validation | add vocal-event count and silence ownership inside explicit dialogue scope |

WP-B、WP-C、WP-E 的通用逻辑留在 Core；adapter 只翻译目标模型需要的最短执行 carrier，不复制通用 operator。

### 3.3 Skill entrypoint map

`skill/framewright/SKILL.md` 只在以下两项获批后做最小修改：

1. 在多 GU、多 revision 或已授权真实生成循环中，读取／更新条件式项目状态文件；
2. 在保存 Prompt 前调用确定性 validator。

不把 A–G 的详细 schema 复制进 SKILL.md；详细规则仍只存在于 authoritative reference。

## 4. Proposed Production Spine delta

不新增第二个 Spine。现有字段继续拥有其语义；只补充下面的条件式内部结构。

### 4.1 `performance_progression` extension

```yaml
performance_progression:
  - beat_id:
    trigger:
    baseline:
    onset:
    physical_carriers:
    dialogue_delivery:
    listener_response:
    release_or_aftermath:
    shot_scale:
```

规则：

- 只对 material performance beat 建立；
- 每个 beat 最多保留一至三个最强 carrier；
- 远景不写不可读的微表情；
- 该结构是现有字段的内部形态，不成为默认输出文件。

### 4.2 `camera_logic` extension

```yaml
camera_logic:
  scene_camera_contract:
  camera_agency:
    operator_goal:
    body_path:
    lens_target:
    distance_change:
    orientation_or_horizon:
    framing_error_behavior:
    recovery_behavior:
    viewer_attachment:
```

仅在主观摄影、手持目击、奔跑、受冲击或 attention transfer 对执行重要时展开。普通稳定跟拍保持简洁。

### 4.3 `object_state_progression` extension

```yaml
object_state_progression:
  - object_or_system:
    initial_state:
    trigger:
    force_or_acceleration:
    resistance:
    contact:
    release_or_lock:
    rebound_or_settling:
    aftermath:
    part_provenance:
    load_bearing_state:
```

`part_provenance` 与 `load_bearing_state` 只用于机械变形、程序性动作或物理过程对叙事可读性重要的场景。

### 4.4 `continuity_locks` extension

在相关跨 GU handoff 中补充：

```yaml
motion_state_handoff:
  camera_velocity_and_direction:
  horizon_and_body_inertia:
  focal_focus_exposure_state:
  subject_and_world_motion:
  sound_continuity:
  opening_only_constraints:
  persistent_constraints:
  selected_take_source:
```

`selected_take_source` 只能指向用户明确选中的生成结果；未选结果不能成为 continuity truth。

### 4.5 `sound_contract` extension

仅在用户明确启用对白或 vocal control 时补充：

```yaml
vocal_events:
  - event_id:
    speaker:
    exact_text:
    language:
    delivery_authority:
    beat:
    allowed_count:
silent_reaction_beats:
```

不因环境声默认政策自动激活对白、字幕或 visible-text control。

## 5. Conditional `framewright_state.yaml`

### 5.1 Proposed trigger

满足任一条件时创建或继续使用：

- 一个项目包含两个或以上批准 GU；
- 同一 artifact 进入第二个 material revision；
- 用户明确选择一个 generated take 供 repair 或下一 GU 使用；
- 用户明确要求跨任务继续同一 Framewright 制作。

一次性单 GU、单 revision、没有生成循环的 Prompt 编译不创建状态文件。

### 5.2 Proposed path

```text
Framewright/outputs/[project_slug]/framewright_state.yaml
```

它放在项目输出根，而不是 Skill、repo root、release snapshot 或单个 GU 文件夹。

### 5.3 Proposed minimum schema

```yaml
framewright_state:
  schema_version:
  core_version:
  project_slug:
  current_scope:
  active_stage:
  director_mode:
  approved_generation_units:
  active_artifacts:
  superseded_artifacts:
  active_intent_entries:
  intentional_freedom:
  unresolved_material_decisions:
  active_material_roles:
  cross_gu_continuity:
  selected_generated_takes:
  last_approved_revision:
  last_updated:
```

### 5.4 Ownership rules

- 它是当前批准 Production Spine / Intent Ledger 的持久化快照，不是另一套创作输入。
- 最新明确用户决定高于旧 state；发生冲突时先更新 state，再编译新 artifact。
- State 与当前 artifact 或用户决定不一致时，停止受影响的编译并报告；不静默选择其中一个。
- 不把完整 Prompt、Semantic Trace、Run Card、风险报告或生成媒体嵌入 state。
- 不作为 Seedance 或其他目标模型的输入附件。
- 用户可审阅，但 Framewright 不把未经确认的手工编辑静默解释为新导演决定。

## 6. New and extended operators

### 6.1 Observable Intent Translation

扩展现有 `Intent Coverage Test`：material abstract intent 必须对应可见、可听或时序 carrier。

示例类别：

- `巨大` → 相对尺度、共同地平面、裁切、视差；
- `恐惧` → 身体路径、呼吸、保护动作、错误取景；
- `克制不舍` → onset、句尾收住、未完成动作、listener aftermath；
- `疲惫` → 重心、恢复时间、呼吸与动作速度。

不要求每个形容词结构化，不增加独立 `observable_intent_registry`。

### 6.2 Embodied Performance Translation

扩展 Performance Vitality：

- 重要台词检查 `before → delivery → ending → aftermath → listener response`；
- 只序列化当前景别能读到的 carrier；
- 禁止肌肉编号、百分比与循环性微动作清单；
- Compression Safety 继续保护被选中的 performance carriers。

### 6.3 Attention / Temporal Feasibility

扩展 Generation-Unit Feasibility Gate，分别审查：

- dialogue / vocal turns；
- blocking / character handoff；
- camera path / attention transfer；
- world response；
- transformation / VFX；
- object-state progression；
- silence / held reaction；
- active-reference complexity。

输出只使用解释性 `low / medium / high` 风险，不发明总分、硬阈值或固定秒数。

### 6.4 Experience Priority Stack

作为 Visual Strategy 与 Feasibility 的派生判断存在。只有目标相互冲突时使用；不写成全局固定优先级，也不自动删除低优先级内容。

### 6.5 Structural Subtraction Safety

扩展 Rationale Conflict Test：删除或合并 beat 前，检查其剧情、关系、主题与 continuity 功能是否被接管。任何 intentional loss 必须由用户接受。

### 6.6 Reference Conditioning Risk Gate

在 material authority 已解析后、runtime admission 前判断：

- 是否必须上传；
- 是否应裁切、限时、限 beat 或只做文字提取；
- 构图、pose、多人排版、风格或照明污染风险；
- 更窄替代材料；
- 移除材料的实际损失。

用户明确要求使用的 runtime asset 不可被静默移除；发生 material risk 时必须说明并请求决定，或在已授予的 advisor scope 内提出一项推荐。

### 6.7 Dialogue Event / Silence Ownership

扩展现有 exact dialogue 与 adapter audio policy：

- 每个批准 vocal event 有唯一 speaker、text、beat 与 count；
- 静默反应不自动获得低语、重复姓名或额外发声；
- `no subtitles / visible text none` 只在用户明确声音／文字 scope 中序列化；
- 单次模型重复仍归 `model_behavior`，不自动升级为 Core 缺陷。

## 7. Deterministic validator design

### 7.1 Proposed files

```text
skill/framewright/scripts/validate_framewright.py
testing/next-local/fixtures/
testing/next-local/expected/
testing/next-local/run_regression.sh
```

不新增 README、Quick Guide 或第二份规范。

### 7.2 Deterministic checks

脚本可可靠检查：

- Skill / Core YAML frontmatter；
- exact mode line；
- active serialization owner；
- clean prompt 禁入词与 placeholder；
- native mention 声明／使用映射；
- exact dialogue event count；
- character limit；
- state schema、active / superseded 唯一性与路径存在性；
- split-unit start/end state 必填；
- forbidden extra artifact、Mode、Stage、Registry；
- protected semantic anchors；
- Markdown fence 与 whitespace integrity。

### 7.3 Non-deterministic checks

脚本不声称判断：

- 情绪是否细腻；
- carrier 是否具有好表演；
- 镜头是否真正有电影感；
- 物理动作是否在成片中可信；
- Seedance 是否执行成功。

这些由 compile-only trace、人工审阅和未来另行授权的 field test 判断。不得用关键词存在代替创作质量验收。

### 7.4 Anti-false-green rules

- 不删除或放宽失败 fixture；
- 不用 `|| true`、无条件 PASS 或 mock validator 自身；
- 同时提供应该 PASS 和应该 FAIL 的 fixture；
- validator 规则改变时，旧 fixture 继续运行；
- 测试数量、skip 数和 failure expectation 记录在 regression report；
- 同一检查连续修复三次仍失败时停止该工作包并报告。

## 8. Regression fixture plan

所有 fixture 使用合成或最小脱敏文本；历史项目与媒体保持只读，不复制私人素材。

| Case family | Positive fixture | Deliberate failure fixture |
|---|---|---|
| Idol | embodied dialogue + rationale-preserving subtraction | abstract emotion only; lost theme carrier; duplicate active revision |
| Zolla | body path differs from lens target; motion handoff | camera moves toward threat; inertia resets at GU02 |
| Loong | terminal state and successful locks preserved | obsolete negative or reappearing terminal object |
| Blade / Havoc | part provenance + load bearing + two vocal events | morph-like missing intermediate; duplicate dialogue name |
| Amei | gravity / contact / settle + narrow reference authority | object slides without force; environment asset controls camera |
| Freefall | no-asset single take remains compact | forced asset question; auto-split; storyboard auto-admission |

Compile-only regression不得生成 storyboard image、keyframe image 或 video。

## 9. Protected-rule delta

以下 3.5.0 行为必须语义保持：

1. 一个入口、一个 active stage；
2. 只有三个 Director Mode 和三个 Stage；
3. Unified Director Intake 与 dependency-sensitive questioning；
4. AUTEUR / APPRENTICE / SCREENWRITER authority；
5. 一个 Production Spine、一个 Intent Ledger owner、一个 Material Registry；
6. Storyboard board / panel 16:9、one GU / one board；
7. Storyboard initial generation exception 与 planning-only runtime boundary；
8. Panel Evidence Plan、Board Feasibility 和 layout dependency order；
9. Visual Strategy、Shot Spine、Sequence Shuffle 与 Capture Necessity；
10. semantic timing 与 no auto-split / merge；
11. Compactness、Compression Safety 与 Stale-Negative Pass；
12. 默认环境声／同步动效、默认无音乐；
13. Seedance task router、native `@` bridge 与 clean saved prompt；
14. no automatic retries、variants、Keyframe generation 或 Video generation；
15. prompt files 不含 workflow、Ledger、Trace、Delta 或 risk commentary。

任何实现 diff 触及上述语义而未由审批项明确授权，立即停止。

## 10. Contradictions requiring approval

### C01 — Persistent state vs prompt-artifact-only default

**Tension**：当前默认只创建 active Stage prompt；条件式 state 会增加第二个项目文件。

**Approved resolution A**：增加窄例外。State 是项目控制文件，不是 Stage output、模型 Prompt 或默认每次交付；只在 §5.1 条件满足时创建。

**Alternative B**：只设计 schema，本轮不启用 state；WP-A 只能做 turn-local / artifact-local lint。

### C02 — Persisted state vs one editable source of truth

**Tension**：可审阅 YAML 可能被误当成第二套 Production Spine。

**Approved resolution A**：State 只能序列化一个已批准 Spine 的 material subset；禁止独立派生新决定。明确用户新决定优先，冲突时必须先 reconcile。

**Alternative B**：State 只存 artifact pointers 与 hashes，不保存 Intent Ledger entries；persistence 能力明显减弱。

### C03 — Experimental version identity vs no formal version lock

**Tension**：Core 一旦改变却仍显示 `Loaded: Framewright v3.5.0`，会与稳定版混淆；但用户选择实验期间不确定正式版本号。

**Approved resolution**：实验 Core 直接使用候选版本号 `3.5.1`。该版本号已锁定，但在本地实验通过并获得晋升授权前，不创建正式 release snapshot、不改稳定 README、不更新 Desktop、不推送 GitHub，也不得描述为已发布。

原 `3.5.0-next-local` 工作标识与“不改版本字段”方案均被用户明确取代。

### C04 — Reference risk gate vs director-requested asset use

**Tension**：Gate 可能判断资产会污染，但用户可能明确要求使用。

**Approved resolution A**：Gate 只能警告、建议 crop / text extraction / narrower authority 或请求决定；不得静默移除、替换或降级明确指定资产。

**Alternative B**：允许 SCREENWRITER 在已确认 advisor scope 内自动选择较窄 admission，但仍必须在 Intent Delta 中披露。

### C05 — Structural subtraction vs protected director structure

**Tension**：Feasibility 可能认为应删 beat，但 AUTEUR locks、APPRENTICE structure 和 no-auto-split 仍受保护。

**Approved resolution A**：Structural Subtraction Safety 只做分析和建议；任何 material deletion、merge、GU split 或 intentional loss 都停下等待用户批准。

**Alternative B**：允许 SCREENWRITER 在已批准的 structure-authority scope 内执行减法，但必须保留 rationale 和报告 delta。

## 11. Redundancies requiring approval

以下建议全部选择“扩展现有 owner”，不新增蓝图中的独立 Contract 文件或 Registry：

| ID | Apparent duplicate | Proposed owner |
|---|---|---|
| R01 | Observable Intent Contract vs Intent Coverage / Semantic Trace | 扩展 §16.1 `Intent Coverage Test` |
| R02 | Performance Action Contract vs `performance_progression` / Performance Vitality | 扩展现有 field 与 §8.11 |
| R03 | Objective Conflict Gate vs Visual Strategy / dominant generation objective / Feasibility | 扩展 §6.1、§8.7、§8.9 |
| R04 | Embodied Camera Contract vs `camera_logic` / Dramatic Camera Language | 扩展现有 `camera_logic` 与 §8.4 |
| R05 | Motion-State Carryover vs continuity locks / start-end state | 扩展现有 continuity owner |
| R06 | Physical Causality Contract vs object-state progression | 扩展现有 `object_state_progression` 与 §8.6 |
| R07 | Reference Conditioning Gate vs Material Registry / Silent Reference Exclusion | 在现有 §9 admission flow 中新增 risk pass |
| R08 | Dialogue Event Contract vs `sound_contract` / Seedance audio policy | 扩展现有 sound owner 与 adapter §9 |

批准：`R01–R08 = APPROVE DEDUPLICATION`。

## 12. Clarification-only approvals

### L01 — “Non-model input” meaning

State 可以被 Framewright 读取以恢复项目状态，但绝不上传或粘贴给 Seedance／其他生成模型。“Non-model”在本轮只表示“非 target-model-facing material”，不是“Codex 永远不能读取”。

### L02 — State creation authorization

一旦本轮规则获批，满足 §5.1 trigger 时，创建／更新 state 属于 Framewright 项目状态管理，不需要每次单独申请文件创建授权；它不授权生成、上传或发布。

### L03 — `PROGRESS.md` relationship

State 不自动替代 `PROGRESS.md`。若项目已有 progress file，两者冲突时先报告；本轮不自动编辑 `PROGRESS.md`。

### L04 — Validator authority

Validator 只拥有确定性结构判定权。它不能以关键词或分数裁决审美、表演、镜头质量或模型能力。

### L05 — Adapter ownership

Seedance adapter 只序列化 D/F/G 中 target-specific 的最短行为，不复制 Performance、Feasibility、Physical Causality 的通用逻辑。

### L06 — No external generation

本地候选完成的含义仅是 specification + validator + compile-only regression 通过，不声称 Seedance 质量获得验证。

### L07 — Keyframe remains unchanged

本轮 D–G 不以 motion continuity 或 physical causality 为理由改造 Keyframe stage、默认生成 Keyframe 或改变其授权。

### L08 — No automatic state backfill

不扫描或迁移历史项目来批量创建 state。只有未来继续某个项目且 trigger 成立时，才从当前获批材料建立初始 state，并让用户审阅 material assumptions。

批准：`L01–L08 = APPROVE CLARIFICATION`。

## 13. Planned implementation order after approval

### Batch 1

1. 写入工作标识与 3.5.0 protected manifest；
2. 实施 C01–C03 获批的 state / revision 边界；
3. 建立 validator 基础与正反 fixtures；
4. 实施 WP-B / WP-C；
5. 运行 Skill validation、protected anchors、fixture suite 与六案例 compile-only traces；
6. 失败则停在 Batch 1，不进入 Batch 2。

### Batch 2

1. 实施 WP-D / WP-E；
2. 实施 C04 对应的 WP-F；
3. 实施 WP-G 与 adapter serialization；
4. 扩展 validator / fixtures；
5. 重跑全部 Batch 1 与 Batch 2 regression；
6. 输出 implementation、regression、remaining-risk reports。

每个 Batch 完成后保留独立 diff；不修改或放宽旧测试来换取 PASS。

## 14. Approval ledger

| ID | Approved choice | Status |
|---|---|---|
| C01 | A | approved |
| C02 | A | approved |
| C03 | version `3.5.1` | approved |
| C04 | A | approved |
| C05 | A | approved |
| R01–R08 | approve deduplication | approved |
| L01–L08 | approve clarification | approved |

所有 dry-run 决策已经批准。用户已于 2026-08-13 明确授权按本审批包实施本地 `3.5.1` 候选的 WP-A–G，并要求 Batch 1 通过后才进入 Batch 2。

仍然不授权：

- 外部生成；
- WP-H / WP-I；
- Desktop sync；
- GitHub push；
- 正式 release snapshot；
- 将候选 `3.5.1` 描述为已发布。

已收到的 Core execution authorization 原文：

```text
批准执行 Framewright 3.5.1 本地候选：按已批准 dry-run 实施 WP-A–G，完成 Batch 1 回归后再进入 Batch 2；不得外部生成、创建 release snapshot、更新 Desktop 或推送 GitHub。
```
