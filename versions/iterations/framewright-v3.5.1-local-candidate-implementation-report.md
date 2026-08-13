---
title: "Framewright v3.5.1 Local Candidate Implementation Report"
status: "LOCAL CANDIDATE IMPLEMENTED - NOT RELEASED"
report_date: "2026-08-13"
baseline_version: "3.5.0"
candidate_version: "3.5.1"
baseline_commit: "35e529c2fcef3c03c9b19569f138db997d9f84ce"
branch: "codex/framewright-next-local-experiment"
external_generation_calls: 0
desktop_sync: false
github_push: false
release_snapshot_created: false
---

# Framewright v3.5.1 本地候选实施报告

## 1. Scope

本轮按已批准 dry-run 实施 WP-A–G。WP-H、WP-I、Keyframe 产品定位、Timing Proof、multi-model adapter、自动 repair memory、外部生成、release snapshot、Desktop sync 与 GitHub push 均未进入范围。

实现遵守一个 Core、一个 Production Spine、一个嵌套 Intent Ledger 与一个 Material Registry。新增结构均扩展既有 owner，没有新增 Mode、Stage、默认 Prompt artifact 或平行 Registry。

## 2. Batch 1

### WP-A — Operational Enforcement / Revision State

- Core 候选版本标识更新为 `3.5.1`；稳定 README 与 release snapshot 未改。
- 增加条件式 `Framewright/outputs/[project_slug]/framewright_state.yaml`：仅多 GU、第二次 material revision、用户选定 generated take、或跨任务继续同一制作时触发。
- State 只序列化已批准 Spine / Ledger 的 material subset；最新用户决定优先，不上传目标模型，不自动回填历史项目。
- 明确 active / superseded revision、change class、selected take 与 `PROGRESS.md` 冲突边界。
- 入口只加入最短 state 与 validator 工作流，不复制 Core schema。

### WP-B — Observable Intent / Embodied Performance

- material abstract intent 必须有 visible、audible、spatial 或 temporal carrier。
- `performance_progression` 增加 conditional performance-beat 内部形态。
- material dialogue 使用准备、delivery、句尾、aftermath 与 listener response 的因果路径。
- 每个 material beat 保留一至三个强 carrier，并检查 shot-scale legibility 与 overdirection。

### WP-C — Attention / Temporal Feasibility

- 分开评估 dialogue、blocking、camera attention、performance / silence、transformation / VFX、world / object state、reference 与 sound load。
- 使用解释性 `low / medium / high`，不使用总分、固定 quota 或假秒数。
- Experience Priority Stack 只在场景内冲突时启用。
- Structural Subtraction Safety 要求功能转移与 director approval；不自动删除、合并或拆 GU。

## 3. Batch 2

### WP-D — Embodied Camera / Motion Handoff

- `camera_logic` 条件式展开 operator goal、body path、lens target、error / recovery 与 viewer attachment。
- `continuity_locks` 条件式保存 camera / horizon / optical / world / sound motion state，区分 opening-only 与 persistent constraints。
- 只有用户明确选择的 generated take 可成为 continuity truth。

### WP-E — Physical Causality / Transformation Topology

- `object_state_progression` 条件式展开 trigger、force、resistance、contact、release / lock、settling 与 aftermath。
- 机械变形在 material 时保存 part provenance 与 load-bearing state。
- 普通动作不强制工程化展开；scene-local negative containment 仍受 Stale-Negative Pass 约束。

### WP-F — Reference Conditioning Risk

- Material authority 解析后、runtime admission 前新增 conditioning-risk pass。
- 支持 attach、crop、beat-limited、text-extraction-only 与 withhold 建议。
- 用户明确要求的 runtime material 不得被静默移除、替换、裁切、降级或 withholding。
- Seedance adapter 只序列化获批后的最窄 strategy；风险与决策保留在 Run Card。

### WP-G — Dialogue Event / Silence Ownership

- explicit vocal scope 中记录 speaker、exact text、language、beat 与 allowed count。
- silent reaction 保持非语言，不自动获得 whisper、重复姓名、额外 speech、subtitle 或 visible text。
- 默认声音政策不变：环境声与同步动效，默认无音乐，不自动启用对白。

## 4. Implementation files

- `skill/framewright/references/framewright.md`
- `skill/framewright/references/runtime_profiles/seedance_2_5.md`
- `skill/framewright/SKILL.md`
- `skill/framewright/scripts/validate_framewright.py`
- `testing/next-local/fixtures/*.yaml`
- `testing/next-local/expected/protected_anchors.yaml`
- `testing/next-local/run_regression.sh`

## 5. Boundary result

- 外部生成：0
- Desktop 修改：0
- GitHub push：0
- release snapshot：0
- README 稳定状态修改：0
- 冻结未追踪目录修改：0
- 历史项目或 Prompt 迁移：0

本报告描述本地候选实施，不构成发布、晋升或三处同步完成声明。
