---
title: "Framewright v3.5.2 Local Seedance 2.5 Official-Guide Alignment Iteration Plan"
document_version: "1.0"
status: "FORMAL PLAN / NOT IMPLEMENTED"
plan_date: "2026-08-13"
baseline_candidate_version: "3.5.1"
baseline_commit: "c89873c"
target_candidate_version: "3.5.2-local"
target_branch: "codex/framewright-v3.5.2-local-seedance-qualification"
distribution_scope: "local repository only"
external_generation_authorized: false
desktop_sync_authorized: false
github_sync_authorized: false
default_change_policy: "DENY UNLESS EXPLICITLY WHITELISTED"
language: "zh-CN"
---

# Framewright v3.5.2 本地 Seedance 2.5 官方指南对齐迭代规划

## 0. 文档身份

本文是一份可直接交给独立 iteration 对话执行的正式实施规格。

本文的目标不是重构 Framewright，也不是追求“官方指南覆盖率”而机械增加功能。目标是：

> 在不改变 Framewright 既有产品哲学、导演权限、工作流、创作机制和未讨论功能的前提下，以最小、可审计、主要由 Seedance adapter 所有的改动，补全 v3.5.1 已确认的 Seedance 2.5 runtime contract 与 qualification gaps。

本文当前只是一份规划文档。创建本文不代表已经实施任何 Framewright 改动。

### 0.1 建议在 iteration 对话框使用的 Kickstarter

```text
Read the attached Framewright v3.5.2 Local Seedance 2.5 Official-Guide Alignment Iteration Plan completely before acting.

Execute it as a strict local-only qualification iteration from the frozen v3.5.1 candidate. Begin with Phase 0 baseline verification and the latest official-guide freeze. Apply only explicitly whitelisted changes. Treat every unlisted behavior, mechanism, file and semantic contract as protected by default.

Do not refactor, simplify, clean up, rename, reformat or “improve” protected Framewright behavior. If implementation reveals a contradiction, redundancy, unclear ownership boundary, required out-of-scope edit, or changed official requirement, stop and write a decision report for my approval instead of resolving it silently.

Do not modify the Desktop Framewright mirror or GitHub. Do not generate images, keyframes, video or audio. Do not spend external credits.
```

### 0.2 Authorization boundary

只有当用户在 iteration 对话中明确要求“按照本文执行”时，执行者才可以修改本文白名单内的本地文件。

即使获得执行授权，以下动作仍未获授权：

- 修改 Desktop AI Filmmaking 中的 Framewright；
- push、merge、创建 PR 或修改 GitHub；
- 修改本地稳定 `main`；
- 创建正式 release snapshot；
- 把 `3.5.2-local` 称为稳定版或正式发布；
- 调用 Seedance 或其他模型进行真实生成；
- 生成或修改 storyboard、keyframe、video、audio；
- 消耗任何外部 credits；
- 修改历史项目、历史 Prompt 或用户现有输出；
- 删除、移动或整理任何 untracked 文件夹。

---

## 1. Frozen baseline and required reading

### 1.1 Baseline

| Item | Frozen planning value |
|---|---|
| Local repository | `/Users/jameslee/Documents/AI Filmmaking Studio/framewright` |
| Branch at planning time | `codex/framewright-next-local-experiment` |
| Commit | `c89873c` |
| Core candidate | `3.5.1` |
| Seedance profile | `1.2.0` |
| Stable local / Desktop / GitHub state recorded by audit | `3.5.0` |
| Existing deterministic result | `25 / 25` fixtures matched expectations |
| External generation calls in audit | `0` |

### 1.2 Baseline fingerprints

| Evidence | SHA-256 at planning time |
|---|---|
| `skill/framewright/SKILL.md` | `79deb8bd85d5a5867371737472ed25ded735dc1416aa21e3100ceb8956a02539` |
| `skill/framewright/references/framewright.md` | `f51dbf4d247b6eb9a6f9860a1d60a52a306007fb9365df48f0fac2d8c8bc7baa` |
| `skill/framewright/references/runtime_profiles/seedance_2_5.md` | `dc0ae58e5c2c1115fdde3f3a7ddc9edebb09966b1f994e6366c375db11c16b25` |
| `skill/framewright/scripts/validate_framewright.py` | `409065dec286daa3b11ec7ddc71eb8075098bc94bda69bdb1abbf011a41bc412` |
| `testing/next-local/run_regression.sh` | `db3882e85e46fa3f8f19159ac176bf720d2f388d5a6d9c1814f984324d178c71` |
| `testing/next-local/expected/protected_anchors.yaml` | `d175d5c937e403814c64dc18b319d02a9930f20848a556938859e2b592852276` |
| Official-guide reconciled PDF | `3a377ea909d0a2406a831493b29b238bf233f9df8cc6c452112b8291a5229dd4` |
| Compatibility audit after C01-C05 decisions | `4adc6cab11339bbc6f2edbb8911303ce9ff47b2befeab8dcaffcef7baedc1441` |

The audit checksum may differ if this planning document was created after a later report-only wording correction. Phase 0 must distinguish report-only changes from Framewright implementation changes and record the live checksum rather than overwriting either silently.

### 1.3 Mandatory reading order

执行者必须完整阅读：

1. `versions/iterations/framewright-v3.5.1-seedance-2.5-official-guide-compatibility-audit-2026-08-13.md`
2. `versions/iterations/framewright-v3.5.1-local-candidate-regression-report.md`
3. `versions/iterations/framewright-v3.5.1-local-candidate-remaining-risk-report.md`
4. `versions/iterations/v3.2-v3.4-approved-decision-log.md`
5. `versions/iterations/v3.2-v3.4-protected-rule-manifest.md`
6. `versions/iterations/v3.5-local-experimental-iteration-plan.md`
7. `skill/framewright/SKILL.md`
8. `skill/framewright/references/framewright.md`
9. `skill/framewright/references/runtime_profiles/seedance_2_5.md`
10. `skill/framewright/scripts/validate_framewright.py`
11. `testing/next-local/run_regression.sh`
12. `testing/next-local/expected/protected_anchors.yaml`
13. 本计划全文。

还必须重新打开最新官方页面：

- <https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh>
- <https://docs.byteplus.com/en/docs/ModelArk/2607689>

本地 `output/pdf/seedance-2.5-prompt-guide-reconciled.pdf` 只能作为可检索辅助证据，不能覆盖更新后的官方原文。

---

## 2. Iteration thesis

审计结论是：

> `ARCHITECTURALLY ALIGNED / RUNTIME QUALIFICATION INCOMPLETE`

因此本次不是 Core philosophy iteration，而是 target adapter qualification iteration。

本次只处理五类问题：

1. Seedance 任务参数来源与锁定关系没有明确编码；
2. Extend 缺少 backward direction；
3. 已声明的高级 control profile 缺少完整 adapter schema；
4. 官方 surface rules、特殊语法、条件性 timestamps 和能力限制尚未形成可验证 contract；
5. 现有 fixtures 证明内部规则自洽，但没有证明各 Seedance route 的 compile-only 合格性。

本次不以增加 Prompt 长度为成功，也不以复制官方示例模板为成功。成功标准是：

- 更正确的 route selection；
- 更明确的 operator-facing parameter provenance；
- 更严格的 reference / boundary / syntax ownership；
- 更可靠的 deterministic qualification；
- 对既有 Framewright 行为零意外改变。

---

## 3. Anti-drift change contract

### 3.1 Default-deny rule

本次采用以下规则：

> 除本文明确列入语义白名单的变化外，所有现有文件、功能、措辞所承载的语义、默认行为、权限关系、输出边界和测试预期均自动受到保护。

“本文没有提到”不代表可自由调整，而代表 **不得调整**。

### 3.2 No opportunistic cleanup

执行者不得借本次迭代进行：

- 全文重写；
- 通篇改写措辞；
- 重排章节；
- 命名统一；
- 删除看起来重复的保护语句；
- 抽象新 framework；
- 合并 Core 与 adapter；
- 为减少行数而压缩语义；
- 为“更优雅”而改变既有 schema；
- 顺便修复 blandness、8-panel tendency 或其他未列入本计划的问题；
- 修改其他 target model 的行为；
- 将官方示例的视觉风格写成 Framewright 默认风格。

### 3.3 Stop-and-report rule

只要出现下列任一情况，立即停止对应 work package，不得自行解决：

- 最新官方原文与审计记录存在 material difference；
- 实现必须修改白名单外文件；
- 实现必须改变受保护机制；
- 必须删除或弱化现有 regression 才能通过；
- Core 与 adapter ownership 无法通过窄澄清解决；
- 一个新规则会对非 Seedance stage 或非目标 route 产生影响；
- 发现新的 contradiction、redundancy 或 ambiguous requirement；
- 需要猜测官方数值、标点语法或平台行为；
- 需要用真实生成证明才能继续；
- 需要触碰用户原有 untracked 文件。

停止后只输出独立 decision report，列明：证据、冲突、最小选项、影响范围和推荐项，等待用户批准。

---

## 4. Protected behavior manifest

以下机制必须保持原有语义。除 C01 的窄例外外，不允许任何修改：

### 4.1 Product and authority

- director-steered、asset-aware、intent-preserving cinematic compiler 身份；
- one workflow / one user entry；
- AUTEUR、APPRENTICE、SCREENWRITER 三种且只有三种 Director Mode；
- Kinetic、Observational、Conversational 三种 scene grammar；
- 最新明确用户决定高于 approved Spine，Spine 高于 derived views，adapter 最低；
- explicit director locks override inference and adapters；
- advisor behavior 不是第四个 mode、stage 或 workflow；
- Core 始终高于 target adapter。

### 4.2 Workflow and state

- Storyboard、Keyframes、Video Prompt 三个且只有三个 stage；
- exactly one active stage；
- 一个 current approved Production Spine；
- Intent Ledger 嵌套在 Spine 内，不成为第二 source of truth；
- Unified Material Registry 是唯一 material truth；
- conditionally triggered `framewright_state.yaml` 不是第二 Spine 或 target input；
- adaptive dependency-sensitive questioning；
- 每个独立 material-question batch 最多五问；
- Intake Hard Stop；
- intentional freedom protection；
- no historical backfill。

### 4.3 Storyboard and Keyframes

- one GU / one storyboard board；
- Storyboard 一次 initial board generation 的窄例外；
- Storyboard planning-only，除非用户明确 runtime admission；
- identical landscape 16:9 panels 和 landscape 16:9 board；
- line-only planning style、exterior masthead、no panel-interior paperwork；
- Panel Evidence Plan 是 panel count 的唯一内部 owner；
- panel 不自动等于 cut、beat 或 keyframe；
- 不新增或强化 8-panel 默认倾向；
- Keyframes 与 Video Prompt 继续 prompt-only by default；
- 不自动生成 keyframe image。

### 4.4 Cinematic planning

- Visual Strategy 的 scene-level ownership；
- Committed Shot / Phase Spine 的 execution ownership；
- start/end state、geography、continuity、object-state preservation；
- Shot Design visual sentence 与 Sequence Shuffle Test；
- no camera-angle quotas 或 arbitrary camera variation；
- production-critical camera move 必须有 start、path、landing、direction、evidence、motivation；
- camera body path 与 lens target 不混为一谈；
- observable performance carriers；
- Causal State Completion 与 Blocking Readiness；
- physical causality 与 transformation topology 仅在 production-critical 时展开；
- Performance Vitality、Final Payoff Hold、Style Survival、Surface Fidelity；
- blandness audit 和 shot-design repair 不属于本次改动范围。

### 4.5 Generation-unit and timing

- Generation-Unit Feasibility Gate；
- no automatic split / merge；
- 30 seconds 是 ceiling，不是 target 或 reliability proof；
- semantic timing default；
- continuous-take phases are not cuts；
- generation-unit boundary 必须由用户批准。

### 4.6 Materials and references

- property-scoped reference authority；
- allowed / denied inheritance；
- UI order 与 display text 不产生 semantic authority；
- Silent Reference Exclusion；
- Storyboard / keyframe / blockout 只有被显式 admitted 后才获得其限定权限；
- offscreen character、identity、motion、audio、style 不得静默外溢；
- 不创建第二 registry。

### 4.7 Sound

- model-ready video prompt 默认包含适当环境声与同步 diegetic/action SFX；
- **默认无音乐**；只有用户明确要求才允许 music / score / soundtrack / song / melody；
- 未请求对白、字幕、audio reference 或 audio edit 时保持 inactive；
- sound scope 不得改变 mode、grammar、stage 或 GU boundary；
- C03 决定为锁定规则，不得在本次重新讨论。

### 4.8 Output and generation boundary

- 一个 active stage 默认只保存一个 clean prompt artifact；
- Run Card 与 Intent Delta 保持 assistant-facing，不默认另存；
- clean Prompt 不含 workflow、approval、risk、Ledger、Trace、Run Card 内容；
- 不自动 retry、variant、keyframe generation 或 video generation；
- validation before save；
- 一次真实生成成功不得自动升级为 global rule；
- scene-local repair 与 smallest affected scope。

---

## 5. Explicitly approved semantic changes

本节是本次唯一的语义变化白名单。

### WP-01. Framewright clean Prompt mode-label separation

User decision C01：Director Mode 必须在与用户的对话中明确声明，但未来 model-facing clean Prompt 不需要包含 literal `[MODE: ...]`。

最小实现：

- 新 compilation scope 仍必须选择一个且只有一个 Director Mode；
- assistant 必须在生成 Prompt 前或交付时明确告诉用户当前 mode；
- internal state、Production Spine、compile trace 继续保存 director mode；
- mode 的 authority boundary 和实际创作影响完全保留；
- Storyboard、Keyframes、Video Prompt 的 model-facing clean artifacts 均移除 literal mode label；
- 除这一个 literal label 外，三个 stage 的 output structure、authority、content obligations、generation boundary 与产品行为全部保持不变；
- prompt-only validation 应拒绝 mode label 作为 compiler metadata 泄漏；
- compile trace 必须证明一个且只有一个 Director Mode 已解析、保存在 internal state，并在 conversation 层向用户声明；
- 不得通过删除 Director Mode selection、authority、internal state 或 user-visible declaration 来实现。

### WP-02. Task parameter provenance and locks

在 Seedance adapter 内增加明确 parameter provenance：

```yaml
parameter_contract:
  duration:
    provenance: user_settable | inherited_from_source | platform_locked
    resolved_value:
  aspect_ratio:
    provenance: user_settable | locked_to_source_video | locked_to_first_image
    resolved_value:
```

Route obligations：

| Route | Aspect | Duration |
|---|---|---|
| Omni Reference | 依当前 surface 可设置项 | 依当前 surface 可设置项 |
| Smart Edit | locked to source video | 继承 / 接近 source；精确容差必须由最新官方原文确认 |
| Long Video | user-settable within verified ceiling | user-settable within verified ceiling |
| First / Last Frames | locked to first image | user-settable if current official surface confirms |
| Extend | locked to source video | extension duration independently settable if current official surface confirms |

要求：

- Run Card 清楚标明 `locked`、`derived` 或 `user-settable`；
- 不把 locked field 呈现为用户可自由修改；
- 参数说明不进入 model-facing Prompt，除非它本身是执行语义；
- 不改变 Core timing、GU 或 aspect philosophy；
- 所有数值与容差必须来自 Phase 0 冻结的最新官方原文。

### WP-03. Forward / backward extension

保留现有 `extend` route，只增加：

```yaml
extension_direction: forward | backward
```

Forward：

- source video 最后一帧是新片段第一帧的 boundary truth；
- 保留现有 `SOURCE END BOUNDARY` 语义。

Backward：

- 新片段最后一帧必须连接 source video 第一帧；
- 新增 source-start boundary ownership；
- 明确 composition、pose、object state、motion vector、lighting、environment 与 audio bridge；
- 不允许把 forward schema 机械反写后继续引用 source ending。

两者都仍是一个 Video Prompt stage、一个 GU contract，不创建新 stage 或新 workflow。

### WP-04. Complete schemas for already-declared control profiles

只补全已经存在于 adapter 的 control profiles，不新增无关能力。

#### Multi-keyframe

- ordered anchor list；
- 每张素材的 state / role / active stage mapping；
- anchor order 与 major-state progression；
- denied inheritance；
- 不把 keyframe 自动解释为 cut；
- 不自动生成 keyframe image。

#### Coarse blockout

- 可拥有 path、blocking、camera、cut structure、lighting progression、sound timing；
- 不自动拥有 identity、surface、texture、costume 或最终 visual style。

#### Fine blockout

- 可保留 approved structure、blocking、motion 与 camera；
- 外观重渲染仍受 Material Registry 与 director locks 控制；
- 不把 blockout 的临时材质或简化人物当作 identity truth。

#### Seamless transition

- before material；
- after material；
- trigger；
- camera path；
- transformation / transition behavior；
- arrival state；
- audio bridge；
- assistant-facing limitation：不承诺 pixel-identical preservation。

#### Explicit exclusion

`one-click video` 不新增 route、mode、control profile 或 fixture family。它只是指南中的复合案例标签。Framewright 保留其中可泛化的素材编排原则，并根据真实输入选择现有 route。

### WP-05. Material quantity and combined-duration admission

- Phase 0 从最新官方原文确认 image、video、audio 和 edit-source 的 hard limits；
- 分开记录 platform hard limit 与 recommended stable range；
- hard limit 触发 validation failure；
- stable range 只产生 assistant-facing warning / feasibility risk，不伪装成绝对禁止；
- 逐场景 active subset 继续优先，不能因为平台上限提高而默认上传全部素材；
- counts 与 combined duration 属于 Run Card / feasibility surface，不默认污染 clean Prompt；
- 不使用 2026-08-03 快照中的旧数值，除非最新官方页面逐项确认一致。

### WP-06. Seedance-specific audio and visible-text syntax

- 仅编码最新官方页面明确确认的 syntax；
- music、SFX、dialogue、subtitle / visible text 分开；
- exact dialogue 保留 speaker、exact text、language、beat、allowed count；
- special syntax 是 serialization，不得改变 sound ownership；
- 未请求 music 时不得因“官方语法支持”而自动增加 music；
- 未请求 dialogue / subtitle / visible text 时不得激活相应 block；
- exact typography、formula 或 signage 不得被描述为仅靠 Prompt 可保证。

### WP-07. Conditional numeric timing qualification

C02 decision：semantic timing 仍是默认。

仅在以下条件之一成立时启用 numeric timestamps：

- Long Video 的段落节奏确实需要；
- 用户要求 critical exact moment；
- dialogue、audio、edit 或动作同步必须数字化；
- selected technique 明确要求时间范围。

启用后验证：

- ranges 连续且不重叠；
- 不超过 resolved duration；
- 每个 critical moment 有 trigger；
- production-critical camera event 有 camera instruction；
- event 之后需要持续的 state 被明确保留；
- impossible action density 进入 feasibility risk；
- 普通场景不得被自动改写成逐秒计划。

### WP-08. Typography and frame-accuracy limitation

- 当用户要求关键文字、公式、标牌或 frame-accurate timing 时，assistant-facing Run Card / handoff 必须说明 Prompt-only 的可靠性边界；
- 优先建议 prepared asset、locked reference 或 post-production，而不是堆叠保证性形容词；
- 用户仍可要求模型尝试；该 limitation 不自动取消用户目标；
- limitation 不进入 clean Prompt，除非某条具体 constraint 对执行有用。

### WP-09. Compactness qualification

- 继续保留 10,000-character hard ceiling，除非最新官方原文明示不同；
- 不把“低于 10,000”当成充分的 compactness proof；
- 为每条 representative route 记录字符数、active materials、stage count 与关键 semantic anchors；
- 检查重复 instruction、inactive block、assistant-facing leakage 和低价值标题；
- 压缩不得删除 identity、state、boundary、reference authority、camera causality、dialogue ownership 或 explicit negatives；
- 本次不凭空引入新的统一软字符上限。

### WP-10. Route-specific deterministic qualification

对下列 route / control 至少增加一个 positive fixture 和一个 deliberate-failure fixture：

1. Storyboard、Keyframes、Video Prompt clean artifacts 均无 mode label，但 conversation 已声明 mode；
2. mode 未声明或 mode label 泄漏；
3. Omni Reference active-subset mapping；
4. Smart Edit sole master、scope、preserve 与 parameter lock；
5. Long Video stage entry / end state 与 conditional timestamps；
6. First / Last aspect provenance 与 anchor authority；
7. Forward Extend boundary；
8. Backward Extend boundary；
9. multi-keyframe order / state mapping；
10. coarse blockout authority；
11. fine blockout authority；
12. seamless transition arrival state / audio bridge；
13. material hard limit 与 stable-range warning 的差异；
14. audio / dialogue / subtitle special syntax；
15. default no-music protection；
16. critical typography / frame-accuracy limitation routing。

Fixtures 必须冻结 semantic obligations，不冻结整段美学 prose。

现有 25 个 fixtures：

- 不得删除；
- 除直接验证旧 mode-line contract 的 fixture 外，不得把原 `expected: fail` 改为 `pass` 或弱化 expected error；
- 直接验证旧 mode-line contract 的 fixture 必须进行等价迁移：`missing literal mode line` 不再是错误，替换为 `conversation mode undeclared`、`multiple internal modes` 或 `mode metadata leaked into clean prompt`；
- 除 C01 所需的 mode-line removal 外，不得批量重写 fixture Prompt；
- baseline fixture inventory 必须继续全部匹配各自迁移后的明确 expectation；所有非 C01 expectation 必须与 v3.5.1 相同；
- 新 fixtures 在此基础上额外通过。

---

## 6. File-level write whitelist

获得执行授权后，只允许修改或新增以下路径。

### 6.1 Existing files allowed for narrow edits

| File | Allowed purpose only |
|---|---|
| `skill/framewright/SKILL.md` | 声明 Director Mode 必须对话可见；所有 clean Prompt 不输出 literal mode label |
| `skill/framewright/references/framewright.md` | 版本号与 C01 的最小 clean-output contract 变化；不得借机修改其他 Core 机制 |
| `skill/framewright/references/runtime_profiles/seedance_2_5.md` | WP-01 至 WP-09 的 adapter-owned contracts |
| `skill/framewright/scripts/validate_framewright.py` | 实现 C01 的 prompt / compile-trace 分层验证，并增加 Seedance route qualification；除 C01 外保持原 validation 行为 |
| `testing/next-local/run_regression.sh` | 纳入新 qualification surfaces，不降低现有检查 |
| `testing/next-local/expected/protected_anchors.yaml` | 更新 candidate version，并增加防漂移 anchors；不得移除旧保护语义 |

### 6.2 New files allowed

- `testing/next-local/fixtures/seedance25_*.yaml`
- `versions/iterations/framewright-v3.5.2-local-protected-baseline-manifest.md`
- `versions/iterations/framewright-v3.5.2-local-implementation-report.md`
- `versions/iterations/framewright-v3.5.2-local-regression-report.md`
- `versions/iterations/framewright-v3.5.2-local-remaining-risk-report.md`
- `versions/iterations/framewright-v3.5.2-local-contradictions-redundancies-report.md`，仅当实际发现问题时创建。

### 6.3 Explicitly forbidden paths

- `README.md`
- `versions/releases/**`
- Desktop Framewright mirror
- `.git` remote configuration
- `Framewright/**`
- `output/**`
- `outputs/**`
- `storyboard/**`
- 所有历史项目目录与历史 Prompt
- 任何本计划未列出的 repo 文件。

如 implementation 认为必须修改 forbidden path，必须停止并报告，不能扩大 whitelist。

---

## 7. Execution phases

### Phase 0. Live-state freeze and dry run

1. 重新读取 branch、HEAD、status 和所有 baseline fingerprints；
2. 明确列出用户已有 untracked paths，并承诺不触碰；
3. 运行现有 regression，必须先得到 `25 / 25`；
4. 重新读取官方指南最新修改时间与全文可核对内容；
5. 建立 hard rule / recommendation / example / limitation ledger；
6. 若官方原文与审计 material difference，停止并报告；
7. 创建本地实施 branch，不设置 upstream，不 push；
8. 写入 protected baseline manifest；
9. 输出 planned diff whitelist，等待或确认执行授权范围。

### Phase 1. C01 narrow contract change

- 先修改 specification 与 validator contract；
- 证明 conversation declaration、internal mode state 和 final Prompt separation；
- 三个 stage 除 mode-label contract 外的 validation 保持原样；
- 单独运行 C01 positive / negative fixtures；
- 若必须全局移除 mode line，停止并报告。

### Phase 2. Parameter and extension contracts

- 实现 WP-02；
- 实现 WP-03；
- 先测试 Smart Edit / First-Last / Forward Extend；
- 再增加 Backward Extend；
- 明确 reverse-boundary negative fixture；
- 不触碰 Core GU 或 timing rules。

### Phase 3. Advanced existing controls

- 按 multi-keyframe、coarse blockout、fine blockout、seamless transition 顺序逐个补全；
- 每完成一个 control，立即运行其 fixture pair 与完整 regression；
- 不新增 `one-click video` route。

### Phase 4. Surface limits, syntax and timing

- 实现最新官方 hard / recommended material rules；
- 实现经确认的 special syntax；
- 实现 conditional timestamps；
- 实现 typography / frame-accuracy assistant-facing limitation；
- 每项都证明 default no-music、semantic timing 和 clean Prompt boundaries 未变化。

### Phase 5. Compile-only qualification

至少用以下 brief classes 建立不调用模型的 compile traces：

- reference-heavy creation；
- Smart Edit；
- Long Video；
- First / Last Frames；
- Forward Extend；
- Backward Extend；
- multi-keyframe；
- coarse blockout；
- fine blockout；
- seamless transition；
- dialogue / subtitle / audio；
- exact text / frame-accuracy limitation。

每个 trace 分开检查：

- internal decision state；
- route selection；
- material authority；
- parameter provenance；
- clean Prompt；
- assistant-facing Run Card；
- character count；
- protected behavior anchors。

### Phase 6. Final regression and report package

必须输出：

1. implementation report；
2. regression report；
3. remaining-risk report；
4. path whitelist verification；
5. before / after semantic diff summary；
6. official-source freeze record；
7. contradictions / redundancies report，仅在确有发现时输出。

不得创建 release snapshot、更新 README、同步 Desktop 或 push GitHub。

---

## 8. Required validation gates

### Gate A. Baseline integrity

- branch / commit / version 与 Phase 0 记录一致；
- 用户已有 untracked paths 未变化；
- baseline regression 为 `25 / 25`。

### Gate B. Scope integrity

- changed paths 全部属于 whitelist；
- 没有 historical output diff；
- 没有 README / release / Desktop / GitHub diff；
- 没有 broad formatting diff；
- 每一处 Core diff 都能映射到 C01 或 version metadata。

### Gate C. Protected behavior

- 所有旧 protected anchors 仍存在；
- 新 anchors 覆盖 default-deny、conversation-visible mode、all clean Prompts exclude mode metadata、no-music、semantic timing、one-click exclusion；
- 旧 fixtures 的 expectation 与 error class 未弱化；C01 直接相关 fixture 已等价迁移而非删除保护；
- Storyboard / Keyframes 除 literal mode label removal 外的行为未变化；
- Director Mode selection、authority、internal state 与 conversation declaration 未变化。

### Gate D. Route correctness

- parameter provenance 正确；
- locked values 不呈现为 user-settable；
- forward / backward boundary 不混淆；
- advanced control authority 不外溢；
- active subset 与 denied inheritance 有效；
- Run Card 与 clean Prompt 不互相污染。

### Gate E. Sound and timing

- 未请求 music 的所有 fixture 均明确保持 no music；
- special syntax 不激活未请求 sound scope；
- semantic timing 默认不变；
- numeric timestamps 只在触发条件成立时出现；
- ranges 与 resolved duration 合法。

### Gate F. Qualification honesty

- deterministic tests 不能被称为真实生成证明；
- 没有外部调用；
- compactness 报告不能把字符上限等同于质量；
- official recommendation 不被伪装成 platform hard failure；
- local candidate 不被称为 stable release。

---

## 9. Acceptance criteria

只有全部满足才可将本地实施称为 `Framewright v3.5.2-local candidate complete`：

1. 最新官方 contract 已冻结并分类；
2. 所有 changed paths 在 whitelist 内；
3. Core 除 version 与 C01 narrow exception 外无语义变化；
4. Director Mode 在对话中明确、内部仍唯一，所有 Framewright clean Prompt 均不含 literal mode label；
5. Smart Edit、First / Last、Extend parameter locks 已编码并验证；
6. Forward 与 Backward Extend 均有正反 fixtures；
7. multi-keyframe、coarse/fine blockout、seamless transition 均有明确 authority schema；
8. `one-click video` 未成为新 route；
9. 最新官方 material limits / stable ranges 被正确区分；
10. special syntax 只在明确 scope 内启用；
11. 默认无音乐保持；
12. semantic timing 保持默认；
13. exact typography / frame accuracy 有 assistant-facing limitation；
14. 原 25 个 fixture 文件全部保留；非 C01 expectations 原样通过，C01 直接相关 expectations 已按等价保护完成迁移；
15. 所有新增 positive / deliberate-failure fixtures 通过；
16. 无 external generation、无 credit spend；
17. Desktop 与 GitHub 未修改；
18. implementation、regression、remaining risk reports 完整；
19. 未解决 contradiction / redundancy 已停止并提交用户决定，而不是被静默处理。

任一项未满足时，必须报告 `PARTIAL / NOT COMPLETE`，不得用“大部分完成”替代完整边界说明。

---

## 10. Explicit non-goals

本次不处理：

- Framewright blandness repair；
- 8-panel tendency；
- 新 scene grammar；
- 新 Director Mode；
- 新 stage；
- timing proof / animatic；
- Keyframe keep / restore / retire 产品决策；
- multi-model adapter；
- automatic repair memory；
- automatic generation / retry / variant；
- storyboard visual style redesign；
- Prompt 美学模板统一；
- 历史 Prompt migration；
- 真实 Seedance output quality、cost、seed、retry 或 provider stability；
- Desktop / GitHub promotion。

这些项目即使与本次工作相邻，也必须保持现状。

---

## 11. Promotion and rollback boundary

本轮目标状态只能是：

```text
Framewright v3.5.2-local
LOCAL QUALIFICATION CANDIDATE
NOT RELEASED
NOT SYNCHRONIZED
NO EXTERNAL GENERATION EVIDENCE
```

稳定 `3.5.0`、Desktop 与 GitHub 不动。现有 `3.5.1` candidate commit 必须保留为可比较回退点。

若未来用户决定正式保留本轮结果，必须另行授权：

- immutable release snapshot；
- README/version metadata；
- local stable promotion；
- Desktop mirror synchronization；
- GitHub intended branch push；
- 三处版本与 SHA-256 核对。

在上述独立授权前，不得宣称 Framewright 已完成正式版本更新。

---

## 12. Final instruction to the implementation agent

本计划的优先级顺序是：

```text
Preserve user-approved Framewright behavior
    > preserve explicit director intent and authority
    > obey current official Seedance surface rules
    > implement the smallest adapter-owned change
    > add deterministic proof
    > improve elegance, brevity or abstraction
```

当“更干净的架构”与“零 drift”发生冲突时，选择零 drift。

当官方指南的示例与 Framewright product philosophy 不同时，先区分 hard surface rule、recommendation、example 与 limitation；不得把示例升级为 Core rule。

当一个改动无法被清楚映射到 WP-01 至 WP-10 时，它不属于本次迭代。
