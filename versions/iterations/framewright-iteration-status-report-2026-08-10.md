---
title: "Framewright Iteration Status Report"
document_version: "1.1"
status: "AUDIT REVISED - NO IMPLEMENTATION AUTHORIZED"
audit_date: "2026-08-10"
revision_basis: "five actual Framewright production conversations"
current_local_candidate: "3.5.0-local"
stable_release: "3.4.0"
local_candidate_branch: "codex/framewright-v3.5-local-experiment"
local_candidate_commit: "97d5b398bc64f472bd3f2948ad8f99cc9cea5004"
stable_commit: "fff816962f4fe6ae7272ac88a4b2e11c00b8d281"
language: "zh-CN"
implementation_authorized: false
external_generation_calls: 0
---

# Framewright Iteration Status Report

> v1.1 revision note：在 v1.0 的对话决策与仓库审计基础上，追加五个实际制作对话的 field evidence，修正“缺少真实生产证据”的过度判断，并重新标定 revision-state persistence、Temporal Budget 与 Seedance runtime validation。没有修改任何 Framewright 规则或版本。

## 0. 报告目的

本报告将三条证据链合并为一个 Framewright iteration 状态总表：

1. 当前对话中明确讨论、批准、搁置、拒绝或尚未决定的 Framewright 迭代；
2. 仓库中的 iteration drafts、release snapshots、approved decision logs、implementation reports、regression reports、remaining-risk reports、当前 `3.5.0-local` core，以及 Desktop 产品文档中的产品路线与设计备忘录。
3. Freefall、Zolla、Loong、Blade & Havoc v2、Idol 五个实际制作对话及其 prompt、storyboard、生成结果复盘和 revision chain。

本报告回答四个问题：

- 哪些迭代已经进入稳定版本；
- 哪些只在本地实验版本中实现；
- 哪些已经获得实际制作证据，但仍缺少受控对照、结构化记录或稳定执行；
- 哪些曾被讨论，却被搁置、替代、拒绝或从未获得实施授权。

本报告是只读审计产物，不修改 Framewright core、Skill、runtime adapter、Desktop mirror、GitHub `main`、历史 prompt 或项目输出，也不授权下一轮实施、生成、retry、发布或同步。

## 1. 证据边界

### 1.1 当前对话证据

当前对话覆盖了以下主要 iteration 主题：

- v2.2.0 / v2.1.0 差异复盘；
- 默认声音政策；
- prompt 默认保存为 TXT，而不是 inline-only；
- v2.2.1 patch 定位；
- Lite / Pro / Quick Compile / Full Compile 的移除；
- 统一入口与主动提问；
- v3.0.0、v3.0.1、v3.0.2、v3.1.0 的 Storyboard 和镜头设计修复；
- Keyframe 的保留、数量、shot-spine 归属与潜在隐藏调用；
- Seedance 2.5 用户手册、提示词指南与 Framewright 适配；
- v3.2-v3.4 全部 contradiction、redundancy、clarification 审批；
- v3.5 local experiment；
- ZHIFEIJI competitive audit；
- 历史 prompt structure drift 与实际运行遵守度；
- 五个实际制作对话中的询问、授权、素材绑定、Storyboard、视频生成、失败诊断与 revision 行为；
- 本轮全局落实状态审计。

### 1.2 仓库与产品文档证据

主要依据：

- `skill/framewright/references/framewright.md`；
- `skill/framewright/references/runtime_profiles/seedance_2_5.md`；
- `skill/framewright/SKILL.md`；
- `versions/releases/framewright-v2.0.0.md` 至 `framewright-v3.4.0.md`；
- `versions/iterations/v1*.md`、`v2*.md`、`v3*.md`；
- `v3.2-v3.4-unified-iteration-spec.md`；
- `v3.2-v3.4-approved-decision-log.md`；
- v3.2-v3.4 implementation / regression / remaining-risk reports；
- `v3.5-local-experimental-iteration-plan.md`；
- v3.5 implementation / regression / remaining-risk reports；
- `Framewright_Evolution_Memo_v0.1.md`；
- `Framewright_Evolution_Memo_v0.2_Detailed_Design_Rationale.md`；
- `Framewright_Seedance_2.5_Iteration_Roadmap.md`；
- `Framewright_Shot_Design_Blandness_Audit_and_Targeted_Repair.md`；
- `Framewright_Independent_Product_Vision.docx`；
- `Framewright_v3.5_vs_ZHIFEIJI_Mechanism_Diff_Report.md`；
- 历史项目 prompt，特别是剁椒鱼头、机甲与 idol 的 revision chain。

### 1.3 实际制作对话证据

本轮追加审阅以下五个 Framewright 制作对话：

| Production conversation | Framewright baseline | 主要证据 |
|---|---|---|
| Freefall no asset | v3.0.0 | 无资产 intake、SCREENWRITER、一个连续 GU、Storyboard prompt、一次初始 board generation、明确拒绝 Storyboard runtime admission、TXT Video Prompt |
| Zolla | v2.2.0 / v2.2.1 | 两 GU 连续结构、GU01 尾部视频引用、真实生成复盘、director refinement / compiler loss / model drift / pipeline break 分类、非覆盖 revision |
| Loong | v2.2.1 | 两轮真实生成、AUTEUR 锁定、极暗曝光、巨物尺度、单桥拓扑、雨水与实拍材质、镜头情绪弧和尾部状态复盘 |
| Blade & Havoc v2 | v3.4.0 | Seedance 2.5 30 秒、多图 material roles、两轮真实生成、timestamp 重分配、机械因果、台词重复、字幕与动作密度问题 |
| Idol | v3.5.0-local | Adaptive Questioning、APPRENTICE → AUTEUR、Semantic Preflight、Intent Delta、角色/场景权限、一镜到底与镜面调度、多轮真实生成、结构性减法 |

这些案例证明 Framewright 已存在真实生产证据，但版本跨度很大。只有 Idol 是较完整的 v3.5 local production sample；其余案例不能倒算为 v3.5 验证。现有证据主要是定性、对话内和项目局部的，尚未构成受控 A/B、统一指标或 release qualification dataset。

## 2. 状态定义

| 状态 | 含义 |
|---|---|
| `STABLE IMPLEMENTED` | 已进入稳定 release，并在 local main、Desktop mirror、GitHub main 的目标版本中成立 |
| `LOCAL IMPLEMENTED` | 已写入 `3.5.0-local` 实验分支，但未晋升为稳定 release |
| `PARTIAL / UNPROVEN` | 规则、schema 或报告已经存在，但缺少真实生产验证、持续状态、可执行检查或稳定调用证据 |
| `HELD / NO CHANGE` | 明确讨论过，但用户选择暂不修改，当前行为继续有效 |
| `SUPERSEDED / REJECTED` | 被后续明确决策取代，或明确拒绝进入当前产品核心 |
| `PLANNING ONLY` | 只存在于产品愿景、roadmap、competitive audit 或 future research 中，没有实施授权 |
| `OPERATING REGRESSION` | 规范本身存在，但实际 Framewright 输出没有遵守该规范 |
| `AUDIT COMPLETED` | 审计或归因工作已完成，但本身不构成 core iteration 或实施授权 |

`FIELD-OBSERVED` 是本报告使用的证据限定词，不是新的 release 状态。它表示某项机制已在实际制作对话中出现，但不自动证明跨案例稳定、可推广或已满足晋升条件。

## 3. 当前版本与分发状态

| Location | Version / commit | Status |
|---|---|---|
| Local experimental branch | `3.5.0-local` / `97d5b39` | local-only candidate |
| Local `main` | `3.4.0` / `fff8169` | stable |
| Desktop Framewright core | `3.4.0` | byte-identical to v3.4 snapshot |
| GitHub `main` | `3.4.0` / `fff8169` | live remote verified |

因此，本报告中的 v3.5 项不能描述为正式发布或三处同步完成。

## 4. 当前对话中的 Iteration Decision Ledger

### 4.1 v2.2.1：声音与 prompt 文件交付

| ID | 对话决定 | 最终状态 | 当前证据 |
|---|---|---|---|
| DLG-01 | 所有故事默认生成声音，但只生成环境声和同步动效，不自动生成音乐 | `STABLE IMPLEMENTED` | v2.2.1 写入 universal diegetic sound policy；v3.4/v3.5 保留 |
| DLG-02 | 明确要求音乐、dialogue、audio edit 或字幕时才启用对应控制 | `STABLE IMPLEMENTED` | core 默认 no music；Seedance adapter 按显式 scope 激活音频政策 |
| DLG-03 | `prompt-only` 不应被理解成 inline-only；prompt 应保存为 `.txt` | `STABLE IMPLEMENTED` | v2.2.1 Default Prompt Artifact Delivery |
| DLG-04 | required prompt file 不需要第二次 file-creation authorization | `STABLE IMPLEMENTED` | Skill 和 core 均将保存 TXT 视为 compilation 正常部分 |
| DLG-05 | 该修正应命名为 `2.2.1` | `STABLE IMPLEMENTED` | `framewright-v2.2.1.md` 与 commit `eb5b35c` |

### 4.2 v3.0：统一入口与主动提问

| ID | 对话决定 | 最终状态 | 当前证据 |
|---|---|---|---|
| DLG-06 | 移除 Lite | `STABLE IMPLEMENTED` | v3.0.0 移除 Lite workflow |
| DLG-07 | 移除 Quick Compile | `STABLE IMPLEMENTED` | retired workflow labels；不再存在 speed/quality shortcut |
| DLG-08 | 移除 Full Compile / compile-all | `STABLE IMPLEMENTED` | 一个 active stage；不再自动创建全套输出 |
| DLG-09 | Lite 被移除后也不再保留 Pro 这个产品名称 | `STABLE IMPLEMENTED` | 当前只有 Framewright 统一入口 |
| DLG-10 | Framewright 应像 Leader 一样主动询问真正重要的问题 | `STABLE IMPLEMENTED` | v3.0 Unified Director Intake；Freefall 的高影响问题与 Idol 的 dependency-sensitive questioning 已 `FIELD-OBSERVED`；v3.5 进一步扩展 |
| DLG-11 | 最终版本目标为 `3.0.0` | `STABLE IMPLEMENTED` | v3.0.0 release |

### 4.3 Storyboard 恢复与 v3.1 镜头设计审计

| ID | 对话决定 | 最终状态 | 当前证据 |
|---|---|---|---|
| DLG-12 | `header` 指的是整张 board title，而不是每个小 panel 的内部标题 | `STABLE IMPLEMENTED` | BOARD TITLE 顶部 exterior masthead |
| DLG-13 | 完整 board 为 16:9 | `STABLE IMPLEMENTED` | Storyboard Layout Contract；Freefall 与 Idol 实际 board 均为 1672×941，已 `FIELD-OBSERVED` |
| DLG-14 | 每个内部 panel 也必须为等尺寸 landscape 16:9 | `STABLE IMPLEMENTED` | v3.0.1 起明确锁定；Idol GU02 prompt 明确 3×3 等尺寸 landscape 16:9 panels |
| DLG-15 | panel 无法填满网格时允许空缺，不允许拉伸、旋转或改变比例 | `STABLE IMPLEMENTED` | intentional blank cells；实际案例未覆盖非满格 layout，仍缺该边界的 field evidence |
| DLG-16 | Storyboard 恢复剁椒鱼头时代的资产使用行为 | `STABLE IMPLEMENTED` | v3.0.2 Storyboard Asset Use；Idol GU02 使用两张角色卡与一张 location board 生成结构板 |
| DLG-17 | 角色、场景、道具资产只提供其被授权的结构信息，不带入 board layout 或最终风格 | `STABLE IMPLEMENTED` | Storyboard Asset Bindings + authority limits；Idol 实际 prompt 明确排除 source layout、color、lighting、pose 与 finish |
| DLG-18 | Storyboard 是否继续严格 monochrome 曾被重新考虑，但没有授权取消 | `HELD / NO CHANGE` | 当前继续 line-only monochrome |
| DLG-19 | 视频 prompt、APPRENTICE 与 SCREENWRITER 镜头逻辑需要审计，防止 v3 抹去旧决策 | `STABLE IMPLEMENTED` | v3.1 Shot Spine、camera function、semantic timing、Style Survival 等修复 |

### 4.4 Keyframe 讨论

| ID | 对话决定 | 最终状态 | 当前证据 |
|---|---|---|---|
| DLG-20 | Keyframe 是否应该保留、移除或成为隐形调用功能 | `HELD / NO CHANGE` | 用户最终决定暂不修改 |
| DLG-21 | Keyframe 必须属于 Shot Spine 中某个 shot / phase / state，不能是游离画面 | `STABLE IMPLEMENTED` | 当前 Keyframes Stage 要求每个 keyframe 有明确 downstream job 和 supported shot/state，但实现层较薄 |
| DLG-22 | 每次应该输出几张 Keyframe | `PARTIAL / UNPROVEN` | 当前 core 没有正式 count strategy；旧版本的 cluster/count 机制未恢复 |
| DLG-23 | 不默认每个 panel / shot 一张 Keyframe | `SUPERSEDED / REJECTED` | 当前 Keyframes 仅在 active stage 创建，且禁止无生产功能 beauty images |

### 4.5 Seedance 2.5 适配与 v3.2-v3.4 审批

| ID | 对话决定 | 最终状态 | 当前证据 |
|---|---|---|---|
| DLG-24 | 先完整理解 Seedance 2.5 文档，再判断对 Framewright 的价值 | `STABLE IMPLEMENTED` | Roadmap 与 unified spec 将文档结论转化为完整 adapter 方案 |
| DLG-25 | 一开始不修改，因为尚无 Seedance 2.5 使用权限 | `SUPERSEDED / REJECTED` | 该临时暂停后来被正式 v3.2-v3.4 实施授权取代 |
| DLG-26 | 使用统一 image/video/audio asset registry | `STABLE IMPLEMENTED` | C03：`uploaded_assets` + Material Registry |
| DLG-27 | 后文用稳定 material role；Seedance 表面使用 `@` 选择实际资产 | `STABLE IMPLEMENTED` | Material Registry role 与 native mention binding 分离 |
| DLG-28 | `@Image 1` 不是固定语义名字，而是 UI 资产选择操作 | `STABLE IMPLEMENTED` | L05 |
| DLG-29 | 无歧义时 `@Image 1` 可直接作为语法主语 | `STABLE IMPLEMENTED` | Seedance adapter direct-subject rule |
| DLG-30 | 有歧义时只加最短必要限定 | `STABLE IMPLEMENTED` | compact qualifier rule |
| DLG-31 | 未明确声音要求时保持旧默认；明确要求时按 2.5 规则标记/控制 | `STABLE IMPLEMENTED` | C04 + adapter audio policy |
| DLG-32 | Seedance 2.5 最长 30 秒会影响 GU feasibility，但不能自动证明可行 | `STABLE IMPLEMENTED` | C05：30-second capability ceiling |
| DLG-33 | 一个 GU 一张 board；装不下时审查是否有自然 GU 边界 | `STABLE IMPLEMENTED` | C01 / L03；拆分仍需明确批准 |
| DLG-34 | 创建 resolved Storyboard prompt 即授权生成一次初始 board image | `STABLE IMPLEMENTED` | C06；Freefall 与 Idol 均已 `FIELD-OBSERVED` |
| DLG-35 | Storyboard image 生成不等于批准其用于视频 | `STABLE IMPLEMENTED` | L04；Freefall 明确生成 board 后拒绝 runtime admission，边界被正确执行 |
| DLG-36 | First frame / last frame / both / Extend 由用户指定；模糊时提问 | `STABLE IMPLEMENTED` | L06；Zolla 明确选择 GU01 最后三秒，Idol 明确选择独立新镜头而非 Extend |
| DLG-37 | Run Card 只在 assistant-facing handoff，不另存默认文件 | `STABLE IMPLEMENTED` | C02 |
| DLG-38 | task-specific schema 与 generic fallback 不得混用 | `STABLE IMPLEMENTED` | R05 |

### 4.6 v3.5 Local Experiment

| ID | 对话决定 | 最终状态 | 当前证据 |
|---|---|---|---|
| DLG-39 | v3.5 只在未推送本地实验分支实施 | `LOCAL IMPLEMENTED` | branch `codex/framewright-v3.5-local-experiment` |
| DLG-40 | local main、Desktop、GitHub 保持 v3.4 | `LOCAL IMPLEMENTED` | 三处当前状态符合计划 |
| DLG-41 | 不进行任何外部生成 | `LOCAL IMPLEMENTED` | implementation regression generation count = 0 |
| DLG-42 | Intent Ledger、Adaptive Questioning、Causal State、Blocking、Semantic Preflight | `LOCAL IMPLEMENTED` | 当前 v3.5 core；Idol 已部分 `FIELD-OBSERVED`，包括问题依赖、mode update、11,425→8,093 字符 Preflight 与 Intent Delta |
| DLG-43 | v3.5 尚未正式晋升或同步 | `LOCAL IMPLEMENTED` | local candidate 完成，但 promotion 未获授权；无 v3.5 stable snapshot，remote main 仍 v3.4 |

### 4.7 Competitive Audit 与运行时 drift

| ID | 对话决定 | 最终状态 | 当前证据 |
|---|---|---|---|
| DLG-44 | 对 ZHIFEIJI 做机制审计，不立即改 Framewright | `PLANNING ONLY` | competitive report 明确 no implementation authorized |
| DLG-45 | 可选 Visual Execution Profile 可能值得未来测试 | `PLANNING ONLY` | 仅建议 paper-profile experiment |
| DLG-46 | 历史 prompt 需要区分版本变化与无依据 drift | `AUDIT COMPLETED` | 剁椒鱼头、机甲、idol prompt audit |
| DLG-47 | v2.2 compact runtime 与 v3.4 Seedance task schema 的差异属于合法版本变化 | `AUDIT COMPLETED` | release timeline 与 schema 对照 |
| DLG-48 | idol GU01 v4 丢失 mode line、脱离 schema | `OPERATING REGRESSION` | 规范存在但实际输出未执行 |
| DLG-49 | idol 跨 GU 门状态、encore、dialogue 出现未记录变更 | `OPERATING REGRESSION` | Intent/rationale/revision protection 未稳定运行 |
| DLG-50 | 项目进度记录必须与实际制作状态一致 | `OPERATING REGRESSION` | Idol `PROGRESS.md` 仍称 Storyboard / Video Prompt 未开始，但对应 prompts、boards 与生成复盘已经存在 |

## 5. 仓库与产品路线的全局落实状态

### 5.1 已进入稳定 v3.4 的系统机制

以下机制属于 `STABLE IMPLEMENTED`：

- 统一入口、显性调用、一个 active stage；
- saved TXT artifact 默认；
- director modes 与权限边界；
- scene grammar、Production Spine、Committed Shot Spine；
- Visual Strategy 与 creative prevention tests；
- Storyboard strict 16:9 board/panels、masthead、blank cells、asset bindings；
- Panel Evidence、Board Feasibility、one GU / one board；
- Material Registry 与 reference lifecycle；
- planning/runtime separation；
- Seedance 2.5 versioned adapter；
- task router 与 task-native schemas；
- Run Card 与 native `@` material mentions；
- generated ambience/SFX + no-music default；
- 30-second ceiling + GU Feasibility Gate；
- one initial storyboard generation exception；
- failure taxonomy、generation evidence schema、scene-local repair rule。

### 5.2 已进入 v3.5 local candidate 的机制

以下机制属于 `LOCAL IMPLEMENTED`：

- intent-preserving cinematic compiler product identity；
- dependency-sensitive Adaptive Questioning；
- one Production Spine 内的 Intent Ledger；
- materially important rationale preservation；
- scope-limited Advisor authority；
- intentional freedom；
- Causal State Completion；
- World-Response Proposal；
- Blocking Readiness；
- Capture Necessity Test；
- Storyboard as structure inspection surface；
- Semantic Trace；
- Semantic Preflight；
- assistant-facing Intent Delta。

### 5.3 已获得的实际制作证据

以下机制不再适合描述为“完全未经生产验证”：

- Unified / Adaptive Questioning 已在 Freefall 与 Idol 中帮助确定 stage、GU 边界、角色年龄、台词、情绪、runtime material route 与 Extend 决策；
- Storyboard prompt → 一次初始 generation → planning-only runtime boundary 已在 Freefall 与 Idol 中实际执行；
- Material authority 已在 Idol 与 Blade & Havoc 中实际限制为 identity、geometry、wardrobe 或 structural geography，没有把 source layout 自动当成镜头设计；
- Seedance 2.5 的 30 秒 Long Video、多图引用、对白、字幕风险、复杂动作密度与一镜到底已经多次进入真实生成；
- Semantic Preflight 在 Idol 中实际发现字符超限并保护指定对白与关键 beats 后完成压缩；
- Zolla、Loong、Blade & Havoc 与 Idol 均形成了 generation → evidence review → revision 的人工闭环，并出现了逐秒、逐帧、动作状态或 prompt timestamp 对照；
- non-destructive revision 已在 Zolla、Loong 与 Idol 中实际保留旧稿并创建新文件。

这些是重要的 qualitative field evidence，但仍不是统一、可重复的 release qualification evidence。

### 5.4 仍属 `PARTIAL / UNPROVEN` 的部分

1. Roadmap P0 要求的至少十个 canonical cases 与三个真实 bland cases 没有完整生成对照集。
2. Visual Strategy 已出现跨案例定性证据，但缺少受控 A/B、统一评价口径与明确的版本归因，不能证明改善来自哪一项 core mechanism。
3. Seedance 2.5 runtime risk 已被部分实际触发，而不是完全未测试；字幕、重复台词、长镜头剪切、空间瞬移、30 秒容量与复杂机械动作仍未关闭。
4. 3.4 路线承诺的 retry 与 credit cost baseline 尚不存在；现有多轮生成没有统一记录成本、seed、provider、参数与成功率。
5. Generation Evidence 不再只是 schema：制作对话里已有大量原始证据，但没有持续数据集、统一统计、自动记录、capability profile 或可查询索引。
6. v3.5 已有 Idol 这一强 production sample，覆盖 relationship-led、AUTEUR 与 real revision cycle；仍缺足够的 large action、causal world-state、无资产与不同 director-mode 样本。
7. Adaptive Questioning、Semantic Preflight 与 Intent Delta 已局部有效；但 Intent Ledger 尚未可靠跨 turn、跨文件和跨 revision 持续，也不能替代对模型执行漂移的生成后验证。
8. Blandness forensic protocol 作为外部文档存在，但 Framewright Skill 没有自动加载入口。
9. Attention / Temporal Budget 不再只是理论缺口：Idol 的容量枯竭、Loong 的揭示时间分配和 Blade & Havoc 的变形可读性已提供实证；但仍没有可比较的密度模型、经验阈值或 gate 输出。
10. 当前 validation 仍主要是自然语言合同、人工 trace 与对话内复盘，没有可执行 CI / linter。
11. 项目状态记录缺少同步机制；Idol 的 `PROGRESS.md` 与实际 prompt、storyboard 和 generation 状态已经发生直接冲突。

### 5.5 Drift 必须按责任层分类

实际制作对话证明，后续审计不能再把所有失败统一称为 prompt drift：

| Drift layer | 定义 | 实际证据 | Framewright 可处理范围 |
|---|---|---|---|
| `COMPILER DRIFT` | 导演已经锁定的内容在 prompt 编译、压缩或 revision 中丢失或被替换 | Idol 一度丢失 GU01 的门、走廊光线、摄影机系统、紧景别与部分连续性 | 可通过 Intent Ledger、Semantic Preflight、revision diff 与 linter 处理 |
| `MODEL EXECUTION DRIFT` | Prompt 已明确，但视频模型仍剪切、瞬移、重复台词、morph、缩小尺度或忽略 blocking | Idol 的隐藏切、人物瞬移与重复表演；Blade & Havoc 的机械 morph；Loong 的双桥与龙再次露头 | 需要 generation evidence、repair/retry 与 capability profiling；不能全部归责 core |
| `PRODUCTION-STATE DRIFT` | 当前批准状态、项目文档、文件版本与制作对话互相不一致 | Idol `PROGRESS.md` 仍停留在 Storyboard / Video Prompt 未开始 | 可通过 project-level state record、revision safety 与 artifact consistency check 处理 |

## 6. 历史机制中未恢复或已变薄的部分

### 6.1 Keyframe Strategy

旧 v2.2.1 / v2.3.x 曾包含：

- shot-energy risk classification；
- high-motion keyframe 默认 text-extraction-only / withheld；
- `none / single_global / cluster_anchors / per_shot_or_panel`；
- keyframe count 按视觉连续性风险推导；
- cluster coverage；
- `none / loose / partial / strong` composition authority；
- keyframe execution basis；
- shot-to-shot style mismatch warning；
- detailed downstream propagation audit。

当前只保留 Keyframe 的 shot/state 归属、frozen instant、production job 和 planning-only runtime boundary。

状态：`PARTIAL / HELD`。用户已经讨论过，但明确选择暂不修改。

### 6.2 Storyboard 旧细节

以下旧机制没有作为独立规则保留：

- Insert / ECU crop fidelity；
- one-or-two primary visual anchors；
- sparse schematic state-color exception；
- every-panel external header 默认要求。

其中 state-color exception 与当前 strict monochrome 合同冲突，视为 `SUPERSEDED`。其余属于低优先级的未恢复细节。

## 7. 产品愿景中尚未实施的方向

以下属于 `PLANNING ONLY`，没有实施授权：

- Timing Proof / animatic；
- optional persistent intent record；
- stronger revision diff；
- empirical semantic-loss metrics；
- surface-specific generation evidence automation；
- repair memory；
- 从选定成片或尾帧反推真实 continuity state；
- director-specific personal grammar；
- beat-level mixed scene grammar，而不是一个 primary grammar；
- camera motion / subject motion / world change 分轨；
- character card / state frame / style board 三类窄 Keyframe authority；
- Seedance 2.5 之外的 model adapters；
- structured schema 与 executable validators 移出单一 Markdown；
- automated mode-line / schema-owner / cross-GU linting；
- ZHIFEIJI-inspired optional Visual Execution Profile；
- project-level full-film operating system。

## 8. 已明确取代或拒绝的方向

以下属于 `SUPERSEDED / REJECTED`，不应重新统计为遗漏：

- Lite / Pro / Quick Compile / Full Compile；
- 默认一次输出 Storyboard、Keyframes、Video Prompt；
- 自动把 Storyboard 用作视频 reference；
- 一个 GU 生成多张 storyboard board；
- 为每个 shot 强制 Keyframe；
- 默认生成 Keyframe image 或 Video；
- 默认另存 Run Card / Attachment Manifest；
- 固定 per-shot seconds 或 fake-precision animatic；
- shot-angle、shot-size 或 movement quota；
- genre-specific look 自动成为全局默认；
- Framewright 自动替导演决定唯一镜头方案；
- 当前阶段自动管理全片剪辑、成片声音、团队生产和项目 OS。

## 9. 当前最重要的未完成工作

### Priority 0 — Operational Enforcement and Revision-State Persistence

需要同时解决“规则存在但调用没有遵守”和“项目状态没有随制作推进持续”的问题：

- exact mode line；
- active serialization owner；
- Seedance task schema；
- active material mapping；
- locked dialogue；
- cross-GU start/end state；
- prompt compression survival；
- active prompt / board / generated take 的 source-of-truth revision；
- project progress 与实际 artifacts 的一致性；
- director locks、rationale 与 intentional freedom 的跨 turn 持续。

这是 Idol 的 compiler drift 与过期 `PROGRESS.md` 已经直接证明的当前最高优先级风险。

### Priority 1 — v3.5 Production Evaluation and Evidence Normalization

Idol 已经覆盖 character/relationship-led、AUTEUR 与 real revision cycle。下一步不是从零开始验证，而是把现有对话证据规范化，并扩展尚未覆盖的样本：

- large action / causal world-state scene；
- SCREENWRITER 与低信息无资产 scene；
- APPRENTICE 中依赖 Adaptive Questioning 的 scene；
- 相同 brief 的 v3.4 / v3.5 对照；
- 至少一个失败后局部 repair / retry cycle。

每个样本至少记录：Framewright version、provider / surface、上传素材、生成参数、问题价值、问题疲劳、遗漏状态、rationale conflict、intentional freedom、compiler drift、model drift、retry、成本与最终选择。

### Priority 1 — Attention / Temporal Feasibility

把已经出现的容量证据转成可用 gate，而不是继续依赖“感觉太密”：

- 区分 dialogue、blocking、camera transfer、world response、VFX / transformation 与 silence 的注意力竞争；
- 在 15 秒与 30 秒 route 下报告最脆弱的 beats；
- 允许提出结构性减法、自然 GU boundary 或 intentional loss；
- 不输出虚假的逐秒精度，也不自动拆 GU。

### Priority 1 — Keyframe Product Decision

需要明确选择：

1. 保持当前薄层 Keyframe stage；
2. 恢复窄版 shot-energy / cluster / authority strategy；
3. 正式移除 Keyframe stage；
4. 另行设计显式或隐藏调用，但不得静默改变 generation authorization。

在新决策前，当前行为继续有效。

### Priority 2 — Remaining Seedance Runtime Evidence

真实生产已经覆盖复杂 30 秒 Long Video、多图角色引用、对白/字幕风险和若干 continuation 选择。仍需按最低成本顺序验证：

1. native `@` mention mapping；
2. Smart Edit sole master；
3. 系统化 First / Last / both / Extend 对照；
4. dialogue / audio / subtitle 的重复与可见文字控制；
5. admitted storyboard structural reference；
6. provider、seed、retry 与 credit cost baseline。

### Priority 3 — Future Architecture

只有在真实 evidence 成立后，再考虑：

- Timing Proof；
- mixed grammar；
- Visual Execution Profiles；
- multi-model adapters；
- generation evidence automation；
- repair memory；
- structured schema / executable validators。

## 10. 总体成熟度判断

```text
Architecture and rule design:          HIGH
Historical decision preservation:      MEDIUM-HIGH
Release recoverability:                HIGH
Static specification regression:       MEDIUM-HIGH
Real production evidence quantity:      MEDIUM-HIGH
Real Seedance 2.5 validation:           MEDIUM
v3.5-specific production validation:    LOW-MEDIUM
Cross-revision state persistence:       LOW
Operational rule adherence:             INCONSISTENT
Executable automated validation:        LOW
Generation evidence learning loop:      LOW
```

Framewright 当前最主要的 iteration debt 不是缺少更多 prompt 技巧，而是：

1. decision state 没有可靠跨 revision 持续；
2. 规范缺少可执行 enforcement；
3. generation evidence 没有形成学习闭环；
4. Keyframe 产品定位仍未正式收束。

## 11. 建议的下一次审批边界

本报告不建议把所有未完成项一次塞入新版本。若进入下一轮 planning，建议只审批以下三个独立 track：

```text
Track A — Operational Lint and Persistent Revision Safety
Track B — v3.5 Evidence Normalization and Sample Expansion
Track C — Keyframe Keep / Restore / Retire Decision
```

三个 track 应分别审批，避免 Keyframe 产品选择、v3.5 promotion 和 validator 实现相互绑架。

## 12. 审计边界

本报告没有：

- 修改任何 Framewright 规则；
- 将 v3.5 晋升为稳定版本；
- 同步 Desktop 或 GitHub；
- 运行任何外部 generation；
- 重写历史 prompt；
- 清理 untracked project/output directories；
- 将 planning-only idea 解释为实施授权。

任何后续 iteration 仍需要新的 blueprint、冲突审查、明确授权、回归验证，以及适用时的 local repo / Desktop mirror / GitHub 三处同步。
