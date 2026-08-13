---
title: "Framewright v3.5.1 vs Seedance 2.5 Official Prompt Guide Compatibility Audit"
status: "AUDIT COMPLETE - NO FRAMEWRIGHT IMPLEMENTATION CHANGES"
audit_date: "2026-08-13"
candidate_version: "3.5.1"
seedance_profile_version: "1.2.0"
candidate_commit: "c89873c"
external_generation_calls: 0
---

# Framewright v3.5.1 × Seedance 2.5 官方 Prompt Guide 兼容性审计

## 0. Executive conclusion

**结论：Framewright v3.5.1 的核心设计与官方 Seedance 2.5 Prompt Guide 在主要原则上高度一致，但当前不能判定为“完整适配”。**

已经对齐的主干包括：素材逐项映射与有限权限、逐场景选择有效素材、30 秒视频的阶段与终态、编辑任务的唯一母版与保留范围、正向延长的边界连续性、首尾帧有限权限、Storyboard / Keyframe 的结构权限、可观察表演、明确摄影机路径，以及 Prompt 不能改变模型固有能力上限的认识。

当前最重要的缺口不是 Framewright 哲学错误，而是 **Seedance 2.5 任务接口尚未完整落地**：

1. 编辑、首尾帧和延长任务的画幅 / 时长参数锁没有被写成明确的 adapter contract；
2. 官方包含向前与向后两种延长，现有 `Extend` 只描述从源视频结尾继续；
3. 多关键帧、粗 / 细 blockout、无缝转场等 control profile 已被声明，但缺少各自完整的序列化 schema 与 fixture；
4. 官方的素材数量 / 稳定工作区间和音频 / 文字特殊语法没有进入当前 profile validation；
5. 现有 `25/25` 回归证明内部规则自洽，但没有证明上述官方任务路线能由 Framewright 真实生成正确 Prompt。

因此建议状态为：

> **ARCHITECTURALLY ALIGNED / RUNTIME QUALIFICATION INCOMPLETE**

这份报告只记录证据与后续候选方向；没有修改 Core、Seedance profile、validator、fixture、版本号、Desktop 副本或 GitHub。

---

## 1. Audit scope and evidence quality

### 1.1 In scope

- Framewright Core `3.5.1`；
- Seedance 2.5 Runtime Profile `1.2.0`；
- `core -> adapter -> validator -> fixture / saved prompt` 的传递链；
- 官方指南中的明确要求、推荐方法、示例模式与能力限制；
- 现有静态 / compile-only 回归和历史 Prompt 抽查。

### 1.2 Out of scope

- 不进行 Seedance 实际生成；
- 不评估画质、服从度、成本、seed、重试率或平台运行稳定性；
- 不把官方示例的视觉风格或模板措辞强制写入 Framewright；
- 不修改任何已锁定机制。

### 1.3 Official-source evidence ladder

| Grade | Evidence | Use in this audit |
|---|---|---|
| A | Chrome 现场打开同一公开 Lark 文档 | 确认页面身份、当前目录、页面显示“最新修改时间为 08 月 12 日”、开篇能力免责声明及 BytePlus Official Release 链接 |
| B | `output/pdf/seedance-2.5-prompt-guide-reconciled.pdf` | 2026-08-03 从同一 Lark URL 整理的可选择文字快照；补齐动态页面难以连续提取的正文。该文件明确声明不是 ByteDance 官方导出 |
| C | 本地 live repo、validator、fixtures 和历史 Prompt | 判断 Framewright 当前实际表达、自动检查覆盖范围和旧产物形态 |

官方页面当前标题为 `Dreamina Seedance 2.5 Prompt Writing Guide`，并指向：

- Lark source: <https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh>
- BytePlus Official Release: <https://docs.byteplus.com/en/docs/ModelArk/2607689>

### 1.4 Freshness limitation

当前 Chrome 页面比本地正文快照更新。目录结构与关键主题仍相符，但本轮没有成功把 08 月 12 日版本整篇导出为静态文本。因此：

- 当前页面直接可见的内容为 Grade A；
- 数值上限、特殊标点语法和页面深处的操作细节主要为 Grade B；
- Grade B 项目可以证明 Framewright 存在待核对接口，但在未来实施前应再冻结最新官方原文，不应直接把旧数值硬编码进 adapter。

这不影响对当前 Framewright 缺少相应 contract / validation surface 的判断，但会影响未来具体数值和标点规则的最终写法。

---

## 2. Baseline frozen for the audit

| Item | Frozen value |
|---|---|
| Branch | `codex/framewright-next-local-experiment` |
| Commit | `c89873c` |
| Core | `3.5.1` |
| Seedance profile | `1.2.0` |
| Core SHA-256 | `f51dbf4d247b6eb9a6f9860a1d60a52a306007fb9365df48f0fac2d8c8bc7baa` |
| Profile SHA-256 | `dc0ae58e5c2c1115fdde3f3a7ddc9edebb09966b1f994e6366c375db11c16b25` |
| Validator SHA-256 | `409065dec286daa3b11ec7ddc71eb8075098bc94bda69bdb1abbf011a41bc412` |
| Official-guide local snapshot SHA-256 | `3a377ea909d0a2406a831493b29b238bf233f9df8cc6c452112b8291a5229dd4` |
| Stable README state | Still identifies `3.5.0` as local / Desktop / GitHub stable release |
| v3.5.1 release snapshot | Absent; candidate remains local and unpromoted |

---

## 3. Requirement-by-requirement ledger

Status meanings:

- `MATCH`: current chain represents the official principle sufficiently；
- `PARTIAL`: principle exists but one operational surface is incomplete；
- `MISSING`: no reliable current contract or validation found；
- `OVER-SPECIFIED`: Framewright adds a rule not required by the guide；
- `NOT APPLICABLE`: official example or platform behavior need not become a core rule；
- `UNVERIFIED`: current official text could not be frozen sufficiently。

| ID | Official-guide item | Class | Core / adapter evidence | Status | Audit judgment |
|---|---|---|---|---|---|
| G01 | Prompt围绕主体、动作 / 事件、环境，并按需加入视觉风格、摄影机与音频 | RECOMMENDED | Core 从 approved Production Spine 编译；Video Prompt 强制可见动作、环境、风格、camera、sound，并允许省略无价值标题 | MATCH | Framewright 更详细，但方向一致 |
| G02 | 只加入真正影响结果的控制层；Prompt 结构改善可控性，不改变模型能力上限 | CAPABILITY_NOTE | `compact_runtime`、Feasibility Gate、conditional blocks、scene-local repair；adapter 明确不得用文字伪装 runtime / model limitation | MATCH | 属于架构强项 |
| G03 | 每个素材单独命名、映射主体、说明提供什么以及禁止继承什么 | HARD / RECOMMENDED | Material Registry、allowed / denied authority、`MATERIAL ROLES`、native `@` binding | MATCH | 与官方模式高度一致 |
| G04 | 按场景选择 active subset，不要求所有素材同时出现 | RECOMMENDED | `active_stages_or_beats`、Silent Reference Exclusion、仅 active runtime materials 进入 Prompt | MATCH | Framewright 的权限模型更严格但不冲突 |
| G05 | 素材数量、视频 / 音频总时长和稳定工作区间 | SURFACE_RULE | Profile 只有任务所需素材检查和 conditioning-risk gate，没有 current-source 数量 / 合计时长 schema | MISSING | 在多素材任务中可能无法提前阻止平台不稳定组合；具体数值实施前须用最新 Grade A 原文复核 |
| G06 | 音乐、SFX、对白、字幕 / 可见文字有专门语法与语言强化方法 | SURFACE_SYNTAX | Adapter 有精细 audio policy、speaker / exact text / language / count，但只序列化通用 headings | PARTIAL | 语义控制很强，Seedance 专用标点 / 语法没有成为 profile contract 或 validator rule |
| G07 | 多参考工作流：逐项角色 -> 主体映射 -> 分组 -> 重要主体 profile -> 逐场景选材 | RECOMMENDED | Registry + role / scope + runtime admission 已覆盖；没有独立重复 registry | MATCH | 不需要照搬示例模板 |
| G08 | 30 秒复杂视频按连续 stages 组织；每段一个主要状态变化和可见终态 | RECOMMENDED | Long Video route 明确 stage entry / end state 和 one principal state change；30 秒仅作为 ceiling | MATCH | Framewright 的 feasibility gate 防止把 30 秒误当可靠性证明 |
| G09 | 时间范围连续不重叠；时间戳主要控制节奏；精确时刻需写 trigger、camera 与后续持续状态 | RECOMMENDED | Core 默认 semantic timing，只在用户明确要求或同步技术需要时使用数字 | PARTIAL | 哲学一致；若用户启用 timestamps，validator 不检查连续 / 非重叠、触发与后续状态 |
| G10 | 编辑任务锁定输入视频画幅，近似继承输入时长；首尾帧锁定首图画幅；延长锁定输入视频画幅 | SURFACE_RULE | Run Card 有 duration / aspect；route prerequisites 只写“compatible requested aspect / composition” | MISSING | 目前可能在 Run Card 中接受平台不能设置的参数，属于高优先级接口缺口 |
| G11 | 视频编辑必须指定唯一 source master、精确 edit scope、目标数量和所有保留内容 | HARD | Smart Edit：sole editing master、bounded scope、`CONTENT TO PRESERVE`、未授权内容全部保留 | MATCH | Adapter 对 motion、timing、occlusion、event order、camera、audio 的保护充分 |
| G12 | 正向延长从源视频最后一帧的真实状态继续，先写边界再写新内容 | HARD | Extend 的 `SOURCE END BOUNDARY`、ending composition / pose / object / motion / lighting / audio continuity | MATCH | 与官方模式高度一致 |
| G13 | 向后延长的最后一帧必须连接源视频第一帧 | HARD | 当前 `Extend` 只从 source ending 开始；schema 只有 `SOURCE END BOUNDARY` | MISSING | 现有 route 无 direction 字段、source-start boundary 或 backward schema |
| G14 | 首帧 / 尾帧分别映射；首尾图画幅兼容；中间运动独立解决 | HARD / SURFACE_RULE | First / Last authority 与 middle motion 已存在；画幅只写 compatibility | PARTIAL | 权限边界正确，平台参数锁不完整 |
| G15 | 多关键帧需按顺序绑定并说明每张代表的状态；控制 stage order 与 major states | RECOMMENDED | `multi_keyframe` 已声明，Storyboard 可派生 multi-keyframes | PARTIAL | 缺少 ordered-anchor schema、每帧 state mapping 和 route-specific fixture |
| G16 | Storyboard grid 控制故事、镜头顺序和近似构图；panel 数与视觉格式属于建议 | RECOMMENDED / EXAMPLE | Framewright 将 storyboard 作为 planning-only，显式 admission 后只给结构权限；panel 不自动变 cuts / beats | MATCH | 官方“约 15 panel 或更少”不应变成固定 panel 默认，更不应制造新的 8-panel 偏置 |
| G17 | Coarse blockout 控制路径 / blocking / camera / cut / light / sound；Fine blockout 保留结构与 motion 并重渲染外观 | RECOMMENDED | `blockout_coarse` / `blockout_fine` 已声明，但没有各自 role schema、denied inheritance 和 validation | PARTIAL | 目前 control profile 名称领先于可审计的序列化实现 |
| G18 | 指南以“one-click video”描述把多种素材编排成完整视频的复合案例：素材角色、顺序、运动量、剪辑节奏、视觉处理和音频 | RECOMMENDED / EXAMPLE | Framewright 可由现有创作规划与适当 Seedance task route 表达这些编排要求；Seedance 2.5 没有需要单独映射的 `one-click video` 界面模式 | NOT APPLICABLE | 不新增独立 route。只保留该案例中可泛化的编排原则，并根据用户的真实输入选择现有 runtime route |
| G19 | Seamless transition 要定义前后素材、触发、camera、视觉变化、arrival state、audio bridge；不保证像素级保持 | RECOMMENDED / CAPABILITY_NOTE | `seamless_transition` 已声明，无独立 schema 或 limitation wording | PARTIAL | 存在路由名但缺少可验证执行 contract |
| G20 | 抽象情绪应由可见 / 可听 carriers 表达；摄影机术语应落到目标、方向、速度和可见结果 | RECOMMENDED | Observable performance carriers、shot-scale legibility、camera agency、body path / lens target separation | MATCH | v3.5.1 在这一点比通用模板更完整 |
| G21 | 关键文字、公式、标牌和 frame-accurate timing 不能只依赖 Prompt，应结合 prepared assets / post | CAPABILITY_NOTE | 有 locked visible text 与 subtitle scope；没有明确 post-production limitation gate | PARTIAL | 可能让用户误以为 exact text / exact frame 可仅靠 prompt 保证 |
| G22 | 示例只是写法示范，结果仍受素材、复杂度和参数影响 | DISCLAIMER | Generation evidence 分层、one success is scene-local、不得把模型 / runtime 故障伪装成 prompt 缺陷 | MATCH | 与 Framewright 的 evidence philosophy 完全一致 |

---

## 4. Confirmed strengths that should remain locked

以下不是本次迭代建议删除或重写的区域：

1. **Core authority remains above adapter**：避免目标平台范例反向改写导演意图、Scene Grammar、Shot Spine 或 GU boundary。
2. **One active stage / one serialization owner**：避免 Core fallback 与 target schema 双重输出。
3. **Unified Material Registry**：官方要求素材逐项分工，但不要求制造第二套 registry；当前 bridge 设计正确。
4. **Limited reference authority**：identity、motion、audio timbre 不自动外溢，是官方素材角色方法的可靠增强。
5. **Silent Reference Exclusion**：只让当前场景需要的素材进入 Prompt，直接符合逐场景选材原则。
6. **30 seconds is a ceiling, not a target**：官方支持长视频不等于每个复杂 30 秒单位都可靠；保留 Feasibility Gate。
7. **No auto split / merge**：平台能力不应替用户决定叙事边界。
8. **Storyboard / Keyframe planning-only by default**：官方允许作为控制参考，但 Framewright 的显式 runtime admission 防止网格风格、标签和 panel geometry 污染视频。
9. **Smart Edit sole master + preservation contract**：这是当前 adapter 与官方最强的直接对齐点之一。
10. **Forward Extend boundary recovery**：composition、pose、object state、motion、lighting、environment 和 audio continuity 均已覆盖。
11. **Observable performance and camera agency**：v3.5.1 新增的 camera body / lens separation、physical causality 和 vocal ownership 与官方“可观察结果”原则一致。
12. **Run Card / clean prompt separation**：上传映射和风险说明留给 operator，Prompt 只保留 model-facing semantics。

---

## 5. Gaps ranked by implementation risk

### P1 - Must resolve before claiming full Seedance 2.5 guide compliance

#### P1-A. Task parameter locks are not encoded

Current profile can display `DURATION / ASPECT RATIO` but does not state that some task surfaces derive or lock those parameters from input materials. This is a correctness risk, not a stylistic preference.

Smallest future evolution path:

- add adapter-local resolved parameter provenance, e.g. `user_settable | locked_to_source_video | locked_to_first_image`；
- prevent Run Card from presenting a locked value as freely editable；
- add fixture pairs for Smart Edit, First / Last Frames and Extend；
- do not change Core timing or GU logic。

#### P1-B. Backward extension is missing

Current `Extend` is structurally forward-only. A backward request could be rejected, misrouted, or incorrectly compiled from the source ending.

Smallest future evolution path:

- add `extension_direction: forward | backward` inside the existing Extend route；
- forward owns source last-frame -> new segment first-frame；
- backward owns new segment last-frame -> source first-frame；
- keep both as one Video Prompt stage and one GU contract；
- require distinct positive and deliberate-failure fixtures。

#### P1-C. Official route coverage is not tested end to end

The validator checks prompt hygiene, bindings, state, ownership, performance, physics, camera and vocal events. It does not compile a user brief through Framewright, select a route, and then validate the produced Prompt against official route obligations.

Smallest future evolution path:

- build route-specific compile traces for Omni Reference, Smart Edit, Long Video, First / Last, Forward Extend and Backward Extend；
- freeze expected semantic anchors, not whole prose；
- keep aesthetic judgment outside deterministic pass / fail。

### P2 - Important but can remain a targeted adapter iteration

#### P2-A. Material quantity and combined-duration admission

The current Feasibility Gate assesses `active-reference complexity`, but no target-specific limits or stable-range warning exists. Latest official numbers must be refrozen before implementation.

#### P2-B. Special audio / text syntax

Speaker, exact dialogue, language and subtitle scope are represented semantically, but Seedance-specific surface syntax is not. A future change should be adapter-local and should not replace Core's sound contract.

#### P2-C. Declared control profiles without complete schemas

`multi_keyframe`, `blockout_coarse`, `blockout_fine` and `seamless_transition` are selectable names, yet no dedicated serialization contract or fixtures demonstrate their official authority pattern. This is a **representation gap**, not evidence that Core must be expanded.

#### P2-D. Numeric timing validation

Core correctly prefers semantic timing. When numeric timing is explicitly selected, however, there is no check for consecutive / non-overlapping ranges, impossible action density, or continued state after a critical timed event.

#### P2-E. Critical typography and frame-accuracy limitation

Framewright can lock requested text but should not imply that Prompt wording alone guarantees exact typography or frame-accurate execution. The appropriate future response may be an assistant-facing limitation note rather than more model-facing prose.

### P3 - Field-test watch points, not immediate rule changes

#### P3-A. Realistic compactness is not demonstrated

Historical Prompt artifacts range from roughly 4,000 to almost 10,000 characters. Many predate the candidate and therefore cannot prove v3.5.1 behavior, but they show why a mere 10,000-character ceiling is not a sufficient compactness test.

#### P3-B. Official values may have changed after the local snapshot

Do not hard-code August 3 quantities or punctuation solely from the reconciled PDF. Freeze the latest page or an official export immediately before implementation.

---

## 6. Contradictions, redundancies, and clarification candidates

No confirmed contradiction currently justifies rewriting Framewright Core. The audit candidates below now include the user's decisions and the resolved C05 clarification. They define constraints for a future iteration but do not themselves authorize implementation.

### C01. Framewright mode line inside the clean model-facing Prompt - DECIDED

Current validator requires every Prompt to begin with `[MODE: AUTEUR|APPRENTICE|SCREENWRITER]`. The Seedance guide does not define these tokens, and the adapter itself says director mode and Seedance task route are independent.

Possible interpretations:

- **Not a contradiction**: the mode line is a compact model-facing behavioral instruction understood through surrounding Prompt content；
- **Clarification needed**: it is assistant-facing compiler metadata leaking into a supposedly clean target Prompt；
- **Potential redundancy**: the actual creative decisions are already serialized in shot, performance and authority clauses, so the label may add no execution value。

**User decision, 2026-08-13:** Director mode remains mandatory conversational state and must be explicitly declared to the user. It does not need to remain as a literal `[MODE: ...]` label inside future model-facing Prompt output.

Future implementation meaning:

- the conversation must state which director mode is active and let the user understand or change it；
- the compiler must retain director mode as internal session / compile metadata；
- the generated decisions must still reflect that mode；
- a later iteration may remove the literal mode line from the final Seedance Prompt and update its validator requirement accordingly；
- this audit does not perform that removal。

### C02. Semantic timing default versus official timestamp examples - DECIDED

This is not presently a contradiction. The guide treats timestamps primarily as pacing control and recommends exact numbers for critical moments; Core uses semantic timing by default and allows numeric timing when explicitly requested or required by a synchronization technique.

Needed clarification: make the adapter state when official Long Video timestamps are worth selecting. Do not turn all scenes into second-by-second plans.

**User decision, 2026-08-13:** Accepted. Preserve semantic timing as the default. Use numeric timestamps only when they materially control long-video pacing, a critical exact moment, synchronization, or another technique that genuinely requires them. Do not convert ordinary scenes into second-by-second plans.

### C03. Default generated ambience / SFX and default no music - DECIDED

The guide treats audio as optional and music as intentional. Framewright makes ambience and synchronized diegetic SFX the default while forbidding unrequested music.

This is a **Framewright product philosophy**, not an official-guide conflict. Changing it would alter locked behavior beyond this audit and is not recommended without field evidence.

**User decision, 2026-08-13:** Keep the original policy. Default to no music unless the user explicitly requests music. Preserve the existing treatment of ambience and synchronized diegetic SFX.

### C04. Core and adapter repeat reference, sound and boundary rules - DECIDED

Some wording appears in both Core and profile, but the responsibilities are distinct:

- Core owns intent, authority and invariants；
- Adapter owns task routing and Seedance serialization。

Do not delete repeated semantic anchors merely to reduce line count. Only remove text if ownership can be clarified without weakening either side's validation surface.

**User decision, 2026-08-13:** Accepted. Preserve semantically necessary anchors in both layers while maintaining the ownership boundary: Core owns intent / authority / invariants；adapter owns Seedance routing / serialization. Future cleanup may clarify ownership but must not delete protections merely to shorten the files.

### C05. `one-click video` support claim - CLARIFIED / CLOSED

`One-click video` is wording used by the guide for a composite use case: assembling multiple supplied materials into a coherent finished video with declared roles, order, motion, edit rhythm, visual treatment and audio. It is not a visible Seedance 2.5 task option that Framewright needs to expose beside Omni Reference, Smart Edit, Long Video, First / Last Frames or Extend.

**Clarification, 2026-08-13:** Close C05 without adding a new route. When a user asks for this kind of result, Framewright should understand the creative assembly goal, perform its normal planning, and select the actual supported Seedance task route from the materials and requested operation. The reusable planning principles remain useful；the example label does not become product architecture.

---

## 7. Validator and fixture findings

### 7.1 Current suite result

Command used:

```sh
sh testing/next-local/run_regression.sh
```

Result:

- Core / Skill / profile integrity: PASS；
- `25 / 25` fixtures matched expectations；
- positive and deliberate-failure cases both participated；
- external generation calls: `0`。

### 7.2 What the suite proves

- single mode line and single serialization owner；
- native mention mapping and prompt cleanliness；
- state and active artifact ownership；
- split unit start / end state；
- observable performance carriers；
- feasibility explanation；
- camera body / lens separation and motion-state handoff；
- physical causality and mechanical topology；
- reference admission approval；
- vocal ownership and silent reactions。

### 7.3 What the suite does not prove

No fixture directly demonstrates:

- Smart Edit task parameter locks；
- Long Video timestamp range validation；
- First / Last image aspect lock；
- Forward versus Backward Extend routing；
- multi-keyframe order and state binding；
- coarse / fine blockout authority；
- seamless-transition arrival state and audio bridge；
- Seedance-specific music / SFX / dialogue / subtitle syntax。

The current fixtures are hand-authored prompt / trace documents. They validate stated properties but do not prove the conversational compiler will always produce those properties from a real user brief.

### 7.4 Historical Prompt sample

Twenty existing `prompt_video*.txt` / `video_prompt.md` artifacts were inspected as contextual evidence:

- 18 pass the current generic prompt validator；
- 2 older / alternate-format artifacts fail because they do not begin with the required mode line; one also uses obsolete named handle placeholders；
- the sample is not a clean v3.5.1 output benchmark, because many files predate this candidate；
- most historical prompts do not exercise current Seedance native task routes or target-specific parameter rules。

Therefore they are useful for identifying validator blind spots, but they must not be reported as evidence that v3.5.1 either passes or fails the latest guide.

---

## 8. Incremental evolution path - proposal only

No item below is authorized for implementation.

### Phase A - Freeze latest official contract

- obtain current official export or reliable full-text snapshot；
- record update date, URL and checksum；
- classify every item as hard surface rule, recommended practice, example, or limitation；
- reconcile any difference from the August 3 snapshot。

### Phase B - Patch only adapter-owned gaps

- parameter provenance / locks；
- extension direction and boundary ownership；
- route-local schemas for currently declared advanced controls；
- Seedance-specific syntax only where current official text confirms it。

Do not change director modes, scene grammars, core authority, GU approval, Material Registry, Storyboard admission, default sound philosophy or Run Card separation unless a genuine contradiction is approved separately.

### Phase C - Add route qualification fixtures

- one positive and at least one deliberate-failure fixture per supported route；
- freeze semantic obligations rather than exact prose；
- preserve current test count / skip count and existing protected anchors；
- add reverse checks for parameter locks and forward / backward boundary inversion。

### Phase D - Compile-only prompt qualification

- use representative briefs for reference-heavy creation, Smart Edit, Long Video, First / Last, both Extend directions, blockout and dialogue；
- inspect resulting saved Prompt and Run Card separately；
- no external generation required for this phase。

### Phase E - Optional field test under separate approval

- only after compile-only approval；
- define cost / retry budget and scene-local success criteria；
- never promote one successful generation into a global rule；
- compare against stable `3.5.0` when the change could affect locked behavior。

---

## 9. Promotion boundary

This audit does not promote `3.5.1` and does not authorize `3.5.2` or `3.6`.

Current release boundary remains:

- local experimental branch: `3.5.1` candidate；
- local `main`, Desktop Framewright and GitHub `main`: stable `3.5.0`；
- no immutable `3.5.1` release snapshot；
- no Desktop or GitHub synchronization performed。

Any future implementation should begin from an approved iteration plan derived from this report, preserve a file whitelist, and finish with a separate contradictions / redundancies decision log.

---

## 10. Final verdict

Framewright v3.5.1 **does not exhibit a broad philosophical drift away from the Seedance 2.5 guide**. Its strongest architectural additions - intent preservation, material authority, observable carriers, feasibility reasoning, boundary continuity and task-specific subordinate adaptation - move in the same direction as the official guidance.

The remaining risk is narrower and more actionable:

> Framewright currently knows *how to think about* most Seedance 2.5 tasks, but it has not yet encoded or tested every task surface's exact runtime contract.

Recommended next decision is not a Core rewrite. It is a **small, adapter-owned qualification iteration** after the latest official text is frozen, with separate approval for C01-C05 and no change to locked Core behavior by default.
