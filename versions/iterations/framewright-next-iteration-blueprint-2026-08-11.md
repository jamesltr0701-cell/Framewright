---
title: "Framewright Next Iteration Blueprint"
document_version: "1.0"
status: "PLANNING ONLY - IMPLEMENTATION NOT AUTHORIZED"
planning_date: "2026-08-11"
current_baseline: "Framewright 3.5.0"
baseline_branch: "main"
baseline_commit: "064ea41"
recommended_next_candidate: "3.5.1-local (working label only; not approved)"
implementation_authorized: false
external_generation_authorized: false
promotion_authorized: false
desktop_sync_authorized: false
github_sync_authorized: false
language: "zh-CN"
---

# Framewright 下一轮迭代蓝图

## 0. 文档用途

本文件只定义 Framewright 从当前 `3.5.0` 基线继续演进时需要完成的迭代内容、依赖关系、实施批次、测试与审批门。它不重复版本历史，不把已实现机制重新包装成新功能，也不构成实施、生成、发布或同步授权。

当前真实基线为 `main` / `064ea41` / Framewright `3.5.0`。旧状态报告中“3.5.0-local 尚未晋升”的版本描述已经过时；其中尚未完成的工作方向仍作为本蓝图输入，但全部按当前 3.5.0 重新归位。

建议将下一轮定位为：

> **Intent、Performance 与 Revision Hardening**：先让既有 3.5 架构更稳定地保存、翻译、约束和验证导演意图，再考虑新增产品表面或更大的架构扩张。

`3.5.1-local` 仅是便于讨论的候选标签。最终版本号必须在实施范围获批后另行确认。

## 1. 总体路线

下一轮不应新增更多 Prompt 模板，而应补齐下面这条执行链：

```mermaid
flowchart LR
    A["导演决定、理由与有意留白"] --> B["可观察意图与具身表演"]
    B --> C["具身摄影机与物理因果"]
    C --> D["Attention / Temporal Feasibility"]
    D --> E["Production Spine 与 Prompt 编译"]
    E --> F["Artifact Lint 与 Semantic Preflight"]
    F --> G["生成证据与最小修复"]
    G --> H["获选成片的真实连续状态"]
    H -. "下一 GU / revision" .-> A
```

这里的新增内容都必须作为现有 Production Spine、Intent Ledger、Performance Vitality、Generation-Unit Feasibility Gate、Material Registry、Semantic Preflight 和 Generation Evidence 的扩展存在，不建立平行架构。

## 2. 保护边界

以下 3.5.0 规则在下一轮默认锁定，不因本蓝图自动改写：

- 保留一个 Framewright 入口，不恢复 Lite、Pro、Quick Compile 或 Full Compile。
- 保留 `AUTEUR / APPRENTICE / SCREENWRITER` 三种 Director Mode，不新增第四种模式。
- 保留 `Storyboard / Keyframes / Video Prompt` 三个 Stage，不新增第四个 Stage。
- 保留一个 Production Spine、其内部 Intent Ledger，以及一个 Material Registry；不建立第二套 source of truth。
- 默认仍只保存当前 Stage 的 clean prompt artifact；不把诊断、Run Card、Intent Ledger 或工作流文字写入模型 Prompt。
- Storyboard 的一次初始图片生成授权、planning-only 边界和后续 runtime admission 规则不变。
- Keyframe 仍维持当前薄层行为，直到用户单独批准 keep / restore / retire 决策。
- 不自动拆分或合并 GU；只可提出自然边界并等待批准。
- 不制造逐镜固定秒数、肌肉百分比、FACS 编码或其他虚假精度。
- 默认生成环境声与同步动效，不生成音乐；对白、字幕和额外声音控制仍须由用户明确提出。
- 不把题材、风格 recipe 或单一案例偏好提升为全局规则。
- ZHIFEIJI 式固定视觉 Profile 已被后续审阅明确判定为 `NO ACTION`，不进入本轮路线。
- 本文件本身不触发 Desktop mirror 或 GitHub 更新。只有未来正式版本获批时，才执行 local repo、Desktop Framewright 与 GitHub intended branch 三处同步验证。

## 3. 下一轮工作包

### WP-A — Operational Enforcement 与 Revision-State Persistence

#### 目标

解决“规则已经存在，但实际编译未遵守”和“锁定决定在 turn、文件、GU 或 revision 之间丢失”的最高优先级问题。

#### 需要实现

1. **两层验证**

   - Artifact Lint：不依赖项目状态即可检查 schema owner、必要结构、字符预算、material handle、dialogue / visible text、clean prompt 边界和禁入的工作流文字。
   - Semantic Revision Lint：在存在批准状态时，检查 director locks、rationale、intentional freedom、cross-GU start/end state、压缩存活和 revision conflict。

2. **唯一活跃 revision**

   每个 Storyboard、Keyframe、Video Prompt 和获选 generated take 必须能判断：

   - 当前 active artifact；
   - superseded artifacts；
   - 当前批准 revision；
   - 哪些变更是 director refinement、compiler inference、repair 或 model workaround；
   - 下一个 GU 应继承哪一个真实结束状态。

3. **项目状态一致性检查**

   当项目已有 `PROGRESS.md` 或等价状态文件时，Framewright 不得报告与实际 artifacts 相冲突的阶段状态。发现冲突时先报告，不静默覆盖。

4. **持久化载体审批**

   单靠当前对话无法可靠完成跨任务 persistence。建议未来增加一个项目本地、非模型输入、可审阅的 continuity state record，只在多 revision、跨 GU 或真实生成循环中启用；一次性编译不创建它。

   推荐载体为单一 `framewright_state.yaml`，作为 Production Spine / Intent Ledger 当前批准状态的序列化快照，而不是第二套可编辑 Spine。该文件是否创建、何时自动更新、是否替代或补充 `PROGRESS.md`，必须先单独审批，不能在实施时自行决定。

#### 验收

- 同一 prompt 只能有一个 active serialization owner。
- 已锁定台词、material mapping、GU 边界和重要 rationale 在压缩与 revision 后仍可追踪。
- 旧 Prompt 不会因新 Prompt 出现而被误报为 active。
- 状态文件与实际 artifact 不一致时能够停止并报告。
- Linter 不修改 creative content，也不调用外部模型。

### WP-B — Observable Intent 与 Embodied Performance Translation

#### 目标

把当前已有但较薄的 `Performance Vitality` 和 `performance_progression` 扩展为可执行的表演翻译，而不是新建表演模式。

#### 需要实现

1. **Observable Intent Translation**

   对会实质影响画面判断的抽象意图，必须找到可观察证据。`巨大、恐惧、疲惫、警惕、克制、不舍、混乱` 不能孤立停留为形容词；它们需要被翻译为尺度关系、动作顺序、呼吸、视线、身体路径、接触、节奏或 aftermath。

   只处理 material intent。装饰性形容词不需要全部结构化。

2. **Performance Action Contract**

   内部可使用下面的最小结构：

   ```yaml
   performance_beat:
     trigger:
     baseline:
     onset:
     physical_carriers:
     dialogue_delivery:
     listener_response:
     release_or_aftermath:
     shot_scale:
   ```

   它属于 `performance_progression` 的内部推导，不保存为第二份默认文件，也不要求每个字段进入 Prompt。

3. **每个重要 beat 只保留 1–3 个强 carrier**

   优先从三类中选择：

   - face / gaze；
   - body / hand / breath；
   - timing / release / aftermath。

   避免把微表演写成动作清单，或让人物在每句台词后重复眨眼、吞咽、握拳和叹气。

4. **对白必须包含表演因果**

   对重要台词，至少判断：

   `台词前的触发与准备 → 说话时的身体控制 → 句尾如何收住 → 台词后的残留 → 对方如何接收`

   不是每一项都要序列化，但不能只有 `sadly / coldly / emotionally` 一类副词。

5. **Shot-scale legibility**

   只编译当前景别能读到的 carrier。远景依靠姿态、路径和重量；近景才依靠眼睑、嘴角、吞咽或细小呼吸。

6. **禁止伪科学精度**

   不使用肌肉编号、百分比收缩或表演生理学术语堆砌。优先使用可见动作及其速度、阻力、释放和后果。

#### 验收

- `Abstract Emotion Orphan Test`：重要情绪词不能没有画面 carrier。
- `Embodied Dialogue Test`：台词存在 onset、delivery 或 aftermath 中至少一个可见因果。
- `Shot-Scale Legibility Test`：carrier 与景别匹配。
- `Performance Overdirection Test`：单个 beat 不超过必要动作密度。
- `Compression / Revision Survival Test`：被选中的 carrier 和情绪 rationale 不因压缩或改稿丢失。

### WP-C — Attention / Temporal Feasibility 与 Structural Subtraction Safety

#### 目标

把“感觉太密”转化为可解释、可比较、不会伪造精确秒数的 feasibility gate。

#### 需要实现

1. 分开评估以下注意力系统：

   - dialogue / vocal turns；
   - blocking 与人物交接；
   - camera path / attention transfer；
   - world response；
   - physical transformation / VFX；
   - object-state change；
   - silence / held reaction；
   - active-reference complexity。

2. 对每个 GU 报告：

   - 最脆弱的 beat；
   - 哪些目标正在争夺同一生成注意力；
   - 哪个高优先级体验可能被低优先级 coverage 破坏；
   - 建议保留、合并、删减或拆分的理由。

3. **Experience Priority Stack**

   当目标发生冲突时，明确场景的优先顺序。例如主观逃生镜头可以是：

   `求生行为 > POV 可信度 > 空间和尺度 > 关键事件可辨认 > 完整战斗 coverage > 漂亮构图`

   该顺序由导演意图和 Visual Strategy 推导，不成为全局固定列表。

4. **Structural Subtraction Safety**

   任何结构性减法都必须回答：

   - 被删 beat 原本承载什么剧情、关系、主题或 continuity 信息；
   - 该功能是否由其他 beat 接管；
   - 减法是否改善执行，却破坏了原始 rationale；
   - 哪些 loss 是用户明确接受的 intentional loss。

   “更短、更少、更容易生成”不能自动等同于“更好”。

5. 只使用 `low / medium / high` 或等价的解释性风险，不在缺少经验数据时发明统一分数和硬阈值。

#### 验收

- 30 秒 ceiling 不再被当作容量保证。
- 能指出 Idol 式对白／调度／镜面／摄影转移过载，以及 Blade & Havoc 式双重机械变形过载。
- 能提出结构性减法，但不自动删 beat、改 GU 或破坏主题载体。
- 用户坚持高风险单元时，保留结构并报告 residual risk。

### WP-D — Embodied Camera 与 Motion-State Carryover

#### 目标

让主观摄影机、手持目击、奔跑摄影或受冲击镜头拥有身体逻辑；让跨 GU 连续性继承运动，而不只是末帧外观。

#### 需要实现

1. 在相关场景内部推导：

   ```yaml
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

2. 明确区分：

   - 摄影者身体往哪里移动；
   - 镜头朝哪里看；
   - 是否允许丢失、遮挡、拍晚、过冲或错误修正；
   - 相机为什么继续看、停止跟随或把注意力交给另一个人。

3. 跨 GU handoff 在相关时继承：

   - camera velocity 与移动方向；
   - 水平线、身体惯性与震动状态；
   - 当前焦距、焦点、曝光和运动模糊；
   - 主体、尘土、碎片、水体和车辆的运动方向；
   - room tone、reverb 与动作声连续性；
   - 哪些状态只约束开头，哪些继续作用于整个 GU。

4. 用户明确选择某一条真实生成结果后，才允许该成片或尾部状态成为后续 continuity truth。未选中的抽卡结果不能反向覆盖批准的 Production Spine。

#### 验收

- Zolla 式“身体逃离、镜头回望”不会被编译成摄影机向威胁靠近。
- 连续镜头的注意力转移有真实位移、视差和中间构图，不用隐藏切代替。
- GU02 不会只继承尘土画面而重置身体惯性。
- 普通稳定跟拍不被强制加入慌乱、失焦或错误取景。

### WP-E — Physical Causality 与 Transformation Topology

#### 目标

补足当前 `initial / intermediate / final object state` 对动作过程描述仍不够的部分，避免“状态正确但过程像 morph”。

#### 需要实现

1. 对 production-critical 物理动作，按需要推导：

   `起始状态 → trigger → 加速或施力 → resistance → contact → release / lock → rebound / settling → aftermath`

2. 对机械变形额外保存：

   - part provenance：零件从哪里来、到哪里去；
   - topology：连接关系与可见转轴／滑轨；
   - load-bearing：哪一部分何时承重；
   - mass and inertia：重量如何改变速度、停顿和冲击；
   - intermediate readability：最终状态不得提前闪现。

3. 对掉落、放下、撞击、水体、脚步、刀具、车辆和建筑破坏，只在其对叙事或可读性重要时展开物理阶段，避免所有动作都被写成工程说明。

4. 当同一错误已经被生成证据反复证明时，可在 repair 中使用“正向终态 + 最短必要的负向禁止”。该策略必须服从 Stale-Negative Pass，不能演变成全局负面词堆积。

#### 验收

- 剁椒鱼头的刀具落下具有重力、接触与稳定，不再水平漂移。
- Blade 弹射能读出肢体形成、承重、压缩、释放和车体被顶飞的因果。
- Havoc / Blade 零件不闪现、不复制，轮胎数量与去向可追踪。
- Loong 的入水终态与水体 aftermath 能保持，且不把项目特定龙动作写成全局规则。

### WP-F — Reference Conditioning Risk Gate

#### 目标

承认“文字权限声明不一定压得住强图像条件”，在 Material Registry 权限之外增加是否应当上传、裁切、限时或只做文字提取的判断。

#### 需要实现

对每个候选 runtime material 评估：

- 所需 authority 是否真的需要视觉附件；
- asset 的构图、姿势、多人排版、风格或照明是否会污染未授权属性；
- 是否可改为文字锁、局部 crop、单 beat 限定或 planning-only；
- 是否存在更窄的替代材料；
- 移除该 asset 会损失什么。

该 gate 只决定 admission strategy，不改变 Material Registry 的角色和 authority，也不自动创建新图。

#### 验收

- 厨房环境图不会因“布局参考”而接管所有全景机位。
- 多视图角色卡造成伴舞复制风险时，能建议单人 crop 或更窄 identity reference。
- Character identity 不自动授予材质、光照、pose 或 camera authority。
- 不因担心污染而把所有资产一律移除。

### WP-G — Dialogue Event 与 Silence Ownership

#### 目标

在用户明确启用对白时，保护说话人、次数、顺序、静默反应和可见文字边界；不改变默认声音政策。

#### 需要实现

- 为每个 vocal event 内部记录 speaker、exact text、language、delivery authority、发生 beat 和 event count。
- 明确哪些 beat 为 `silent reaction only`，并保留其非语言表演 carrier。
- 检查同一名字、台词或工作人员呼叫是否被无意重复。
- 将 exact dialogue、no extra speech、subtitle / visible-text policy 编译到 Seedance adapter 的现有 sound scope，而不是新建音频系统。

#### 验收

- Havoc 的 “Blade!” 和 Blade 的 “Havoc...” 各只拥有一个批准 vocal event。
- 静默反应不会被编译成第二次台词、低语或无意义发声。
- 明确 `no subtitles / visible text none` 时不主动生成字幕指令。
- 仍承认重复台词或字幕可能属于 model execution drift，不能把单次失败全部归责于 core。

### WP-H — Evidence Normalization 与 Minimal Repair Learning

#### 目标

把已经存在的人工复盘转化为可比较的 evidence，而不是直接构建未经验证的“自动学习系统”。

#### 需要实现

1. 规范记录：

   - Framewright / adapter version；
   - provider、surface、task route 与参数；
   - active materials 与权限；
   - prompt fingerprint；
   - attempt、retry、seed（若可得）、credit cost；
   - observed success / failure；
   - current root-cause owner；
   - minimal prompt delta；
   - protected successful conditions；
   - selected take 与 continuity status。

2. 所有诊断词映射回当前 `planning / serialization / rendering / reference_authority / runtime_or_surface / model_behavior` owner，不再建立平行 failure taxonomy。

3. 每轮 repair 默认修改最小受影响范围，并明确哪些成功条件不得回退。

4. 在积累足够重复证据前，不实施 repair memory 自动改 core，也不从单个成功抽卡推导全局规则。

#### 验收

- 同一案例的多轮结果可以比较修改变量与结果。
- DIRECTOR_REFINEMENT、COMPILER LOSS、MODEL DRIFT 和 PIPELINE BREAK 可映射到现有 owner，而不混为一类。
- 选定结果能进入后续 continuity；未选结果保持 evidence，不成为事实。
- 成本、retry 与 provider 信息不再系统性缺失。

### WP-I — Seedance 2.5 Remaining Runtime Qualification

#### 目标

把状态报告中仍未关闭的 Seedance 2.5 adapter 假设变成受控 runtime evidence；没有失败证据时不提前改写 core。

#### 需要验证

按最低成本、单变量顺序验证：

1. native `@` mention 与稳定 material role 的实际映射；
2. Smart Edit 中 source video 作为唯一 editing master 的边界；
3. First Frame、Last Frame、Both 与 Extend 的 endpoint authority；
4. dialogue、audio、subtitle / visible-text 的重复、遗漏与错误归属；
5. 用户明确 admitted storyboard 后的窄结构 authority；
6. provider、surface、seed、retry、credit cost 与成功率 baseline。

这些验证复用 WP-H 的 evidence schema。只有 repeatable evidence 指向 serializer 或 adapter 缺陷时，才修改 `seedance_2_5.md`；model behavior failure 只进入 capability profile 与 scene-local repair。

#### 验收

- 每个 route 的输入前提、authority 和失败 owner 可被区分。
- UI chip / filename / index 不会取代 Material Registry 的稳定角色。
- Storyboard panel 不会因上传而自动变成 cut、最终画风或整段构图 authority。
- Smart Edit、Extend 和 endpoint route 不会互相静默替换。
- 运行时结论包含真实 surface 与成本信息，不再只依据官方声明。

## 4. 对话中遗漏迭代方向的去重结论

| 对话积累的想法 | 下一步处理 | 理由 |
|---|---|---|
| Observable Intent Contract | 纳入 WP-B | 当前 Semantic Trace 能追踪 carrier，但没有强制把 material abstract intent 翻译成可观察证据 |
| Embodied Camera Contract | 纳入 WP-D | 当前 camera path 规则尚未稳定区分 operator body 与 lens target |
| Objective Conflict Gate | 纳入 WP-C，命名为 Experience Priority Stack | 当前只有每 shot dominant objective，仍缺场景级体验冲突排序 |
| Motion-State Carryover Contract | 纳入 WP-D 与 WP-A | 当前 continuity 能保存状态，但对惯性、光学和实际获选成片的继承不足 |
| 道具重力与机械过程 | 纳入 WP-E | 现有初中末状态不足以保证 contact、load-bearing、resistance 和 release 可读 |
| 表演从肌肉控制、动作快慢、微动作出发 | 纳入 WP-B，但拒绝肌肉编号与假精度 | 当前 Performance Vitality 有方向，缺少完整 derivation 与 dialogue aftermath |
| 结构性减法后的主题损失 | 纳入 WP-C | 当前 feasibility 会建议减法，但需要 Dramatic Remainder / Rationale 检查 |
| 环境图与多视图角色卡造成视觉污染 | 纳入 WP-F | Material authority 已存在，缺的是 admission 层的 conditioning risk 判断 |
| 台词重复与静默反应被重新配音 | 纳入 WP-G | exact dialogue 已存在，缺 event count、silence ownership 与针对性 runtime 验证 |
| 正向终态 + 负向禁止 | 作为 WP-E / WP-H 的 scene-local repair tactic | 有效但不应成为全局负面词模板 |
| 同功能反应镜头的安全变化 | 不新增独立机制；作为 Visual Strategy / Sequence Shuffle 回归项 | 当前规则已经覆盖有功能的变化，问题是执行与验证，不是缺第四套 shot rule |
| Scale Contract | 不新增平行合同；由现有 Scale Lock + WP-B Observable Intent 强化 | 避免重复 source of truth |
| Causal world response | 不重复实现；只进入 3.5 field evaluation | 3.5 已有 Causal State Completion 与 World-Response Proposal |
| Blandness forensic protocol | 不自动加载整份外部文档；提取最小回归检查进入 WP-H fixtures | 避免第二套权威，同时保留 Visual Strategy、reference contamination 与 coverage collapse 的测试价值 |
| Camera / subject / world 三分轨 | 暂留未来研究；本轮先实现 WP-D 的最小具身摄影机状态 | 直接全量分轨会扩大 schema 和认知负担 |
| 从获选成片反推真实 continuity | 纳入 WP-D / WP-H，但必须由用户明确选择结果 | 不能让任意抽卡覆盖导演批准状态 |
| Timing Proof / animatic | 暂缓 | 当前优先先建立解释性 feasibility gate，避免伪精度 |
| Keyframe keep / restore / retire | 单独产品决策，不进入本轮默认 implementation | 用户此前明确 held / no change |
| ZHIFEIJI-inspired Visual Execution Profile | 排除 | 后续审阅已明确 `NO ACTION`，固定风格模板与 Framewright 哲学冲突 |

## 5. 推荐实施批次

### Batch 0 — 审批与 dry run

实施前必须先确认：

1. 是否批准项目本地 persistence record；若批准，采用什么触发条件和文件位置。
2. 下一候选是仅包含 WP-A/B/C，还是将 WP-D/E/F/G 一并纳入同一个本地实验。
3. Keyframe 是否继续保持 held；默认答案为保持不变。
4. 哪些真实项目材料可以进入静态 regression fixtures；默认只读使用，不复制私人媒体。

Batch 0 只输出 section map、protected-rule map、schema delta、contradiction / redundancy / clarification report 和测试计划，不修改 core。

### Batch 1 — 推荐的最小本地候选

建议先实施 `WP-A + WP-B + WP-C`：

- revision safety 和 artifact lint 保护所有后续新增 carrier；
- Embodied Performance 是用户当前最明确的新需求；
- Attention / Temporal Gate 防止“为了细腻表演继续加词”反而造成过载。

这三个工作包可以作为 `3.5.1-local` 的最小候选，不修改 Desktop 或 GitHub，不进行外部生成。

### Batch 2 — 已有证据支持的执行深化

在 Batch 1 静态回归通过后，再实施 `WP-D + WP-E + WP-F + WP-G`。它们分别强化摄影机身体逻辑、物理因果、runtime material admission 和对白事件控制。

若 Batch 2 导致 core 明显膨胀，应优先：

- 把 Seedance-specific serialization 留在 adapter；
- 把通用 derivation 保留在现有 core operator；
- 删除重复 schema，而不是增加新 Mode、Stage 或默认 artifact。

### Batch 3 — Evidence qualification

由 WP-H 统一 evidence，再按 WP-I 的 route 顺序验证。先运行 compile-only regression；只有用户另行批准后才做外部 A/B generation。真实生成应按最小成本顺序验证，一个案例一次只改变一个主要变量。

完成证据后再决定：

- 保留为 3.5.1；
- 扩展为更大的后续版本；
- 回退某个 work package；
- 只保留 adapter 层修复；
- 是否启动 Keyframe 单独产品决策。

## 6. 文件影响图

实施时优先修改现有权威位置，不创建重复文档体系：

| 目标 | 预期作用 | 当前授权 |
|---|---|---|
| `skill/framewright/references/framewright.md` | 扩展 Performance Vitality、Feasibility、Camera、Physical Causality、Semantic Preflight 与 revision safety | 未授权 |
| `skill/framewright/references/runtime_profiles/seedance_2_5.md` | 扩展 dialogue event、silence、reference admission 与 continuity serialization | 未授权 |
| `skill/framewright/SKILL.md` | 仅当入口工作流确实需要暴露新 persistence / lint 行为时做最小修改 | 未授权 |
| project-local state record | 可选的跨 revision persistence；路径与触发条件待审批 | 未授权 |
| local validator script | read-only artifact / revision lint，不调用外部模型 | 未授权 |
| regression fixtures | 保存最小化、可复现的输入与期望检查，不复制不必要的私人媒体 | 未授权 |
| release / implementation / regression reports | 只在实际 iteration 获批后创建 | 未授权 |

当前本地 repo、Desktop mirror 和 GitHub 均不得因本计划文件发生版本变化。

## 7. Compile-only Regression Matrix

| Case | 主要检查 | 必须保护 |
|---|---|---|
| Idol | Embodied Performance、对白 aftermath、camera ownership、结构性减法、revision persistence | 成熟克制而非怨恨；角色与门／走廊连续；不因减法丢失主题 rationale |
| Zolla | Observable scale、Embodied Camera、Experience Priority、motion carryover | 逃生身体路径高于完整战斗 coverage；GU 间继承运动惯性 |
| Loong | 主体 awareness、欠曝与材质 carrier、paired terminal lock、主观反应 | 单桥、头先入水、入水后不再露头等已成功条件不得回退 |
| Blade & Havoc | Transformation topology、load-bearing、dialogue event count、30 秒 attention load | 角色身份、位置交换、轴线、机械零件来源与批准台词 |
| 剁椒鱼头 | 道具重力、程序性动作、reference conditioning、timing-critical SFX | 正确工序、快节奏、厨房 continuity 与默认无音乐 |
| Freefall | 无资产 SCREENWRITER、single-take continuity、低信息 intake | 不强迫新增资产，不把 storyboard 自动用于 runtime，不拆一镜到底 |

每个 case 使用 `PASS / PARTIAL / FAIL`，至少检查：

- protected rules 是否未改变；
- material intent 是否有 carrier；
- carrier 是否能通过压缩；
- 是否出现新的 silent invention；
- attention gate 是否能解释风险；
- output schema 是否稳定；
- 是否错误新增 artifact、Stage、Mode 或 generation authorization。

## 8. 外部 field validation 顺序

本节仅定义未来测试顺序，不授权生成。

1. Idol：同一 brief 对比当前 3.5.0 与 performance hardening candidate。
2. Zolla：测试 operator body / lens target 分离与 GU motion carryover。
3. Blade & Havoc：测试 mechanical causality；不同时改变镜头结构、资产和台词。
4. 剁椒鱼头：测试小型物理动作与环境 reference admission。
5. Loong：测试已成功条件保护和 scene-local paired containment。
6. Freefall：确认新机制没有让无资产简洁场景过度问询或过度结构化。
7. Seedance route qualification：另行使用最小测试素材验证 native `@`、Smart Edit、First / Last / Both / Extend、dialogue / subtitle 与 admitted storyboard；不与创作质量 A/B 混在同一次生成中。

每个外部测试必须单独记录生成授权、provider、surface、参数、retry、成本和最终选择。

## 9. 停止条件

遇到以下任一情况，实施必须停止并提交 contradiction / redundancy / clarification report：

- persistence record 与“默认只保存一个 clean prompt artifact”发生未获批冲突；
- 新 schema 成为第二个 editable Production Spine、Intent Ledger 或 Material Registry；
- performance carrier 要求迫使所有场景过度表演；
- attention gate 变成固定 beat quota、自动拆 GU 或伪精度打分；
- physical causality 规则使普通动作 Prompt 明显膨胀；
- reference risk gate 静默移除用户明确要求的 runtime asset；
- dialogue event control 改写用户台词或激活未请求的声音／字幕范围；
- regression 发现当前 3.5.0 未发现问题的行为发生变化；
- 需要外部生成、Desktop 更新、GitHub push 或版本晋升才能继续。

## 10. 完成定义

只有以下条件全部成立，本轮候选才可被称为完成：

1. 获得明确实施范围与 persistence carrier 授权。
2. 通过 protected-rule diff 和 contradiction review。
3. 完成获批 work packages，未新增平行 source of truth。
4. 六个 compile-only regression case 均无保护性回归。
5. Artifact Lint 与 Semantic Preflight 能发现预设的 schema、revision、dialogue、material 与 compression failures。
6. Performance、camera、physical causality 与 feasibility 的新增规则在不相关场景中保持静默。
7. 外部生成若被另行授权，证据记录完整，且 failure owner 没有被错误归责。
8. 用户随后单独决定版本号、保留范围与是否晋升。
9. 只有正式晋升获批后，才执行 local repo、Desktop Framewright、GitHub intended branch 三处同步并逐项验证版本与内容一致。

## 11. 暂不进入下一轮的方向

以下内容继续保留为未来研究，不与本轮 hardening 绑在一起：

- Timing Proof / animatic；
- beat-level mixed grammar；
- 完整 camera / subject / world 三分轨；
- director-specific personal grammar；
- multi-model adapters；
- 自动 generation evidence ingestion；
- 自动 repair memory；
- project-level full-film operating system；
- structured schema 全量移出 Markdown；
- Keyframe 产品定位变更。

其中 persistent state 与 local validator 是本轮唯一可能新增的基础设施；它们也必须先通过独立审批，不得借“实现更稳定”绕过现有 artifact 边界。
