---
title: "Framewright v3.5 vs ZHIFEIJI Mechanism Diff Report"
status: "AUDIT COMPLETE - NO IMPLEMENTATION AUTHORIZED"
audit_date: "2026-08-10"
primary_framewright_version: "3.5.0-local"
stable_comparison_version: "3.4.0"
framewright_branch: "codex/framewright-v3.5-local-experiment"
target_document_version: "GPT电影感自然出图 Skill V3"
tutorial_video_reviewed: false
generation_tests_run: 0
implementation_changes_authorized: false
---

# Framewright v3.5 vs ZHIFEIJI Mechanism Diff Report

## 0. 中文审阅摘要

### 0.1 这份 ZHIFEIJI MD 实际上是什么

它不是另一套完整的 Framewright，也不是正式封装的 Codex Skill。它是一份面向网页 ChatGPT、自定义 GPT 和兼容 Markdown 的对话工具所写的**垂直题材系统提示词 / 美术指导 recipe**。

它专门处理“边境古森林、沙漠古城遗迹、自然吞噬文明、巨大环境与极小人物”这一类画面。它通过预先锁定空间权力、构图、人物比例、光线、色彩、材质、空气和负面约束，把用户的一句概念迅速收敛成统一的电影感出图 Prompt。

### 0.2 它的核心工作机制

它的工作链可以概括为：

> 识别垂直题材 → 判断用户是在生成还是改写 → 自动补齐大量导演决定 → 按固定十四段顺序组装 → 加入题材专属失败约束 → 输出可复制 Prompt。

它真正有效的地方不是“电影感词汇很多”，而是所有默认值共同服务于一个明确的视觉论点：**环境支配人物，遗迹与自然互相吞噬，人物只负责证明尺度。**

因此，右侧巨型遗迹、中景黑暗森林、左侧夕阳峡谷、下方极小人物、低饱和冷暖关系和厚重空气并不是彼此独立的装饰词，而是一组互相支持的美术导演决策。

### 0.3 它和 Framewright 的根本差异

ZHIFEIJI 追求的是**快速美学收敛**：用户没有说明的地方，尽量由垂直 Profile 直接决定。

Framewright 追求的是**导演意图保持**：先判断决定归谁、缺失信息是否重要、是否可以安全推断，再把被批准的状态编译进 Storyboard、Keyframes 或 Video Prompt。

所以两者并不是同一层级的竞争架构：

- ZHIFEIJI 更像一个强预设的垂直美术 Profile；
- Framewright 是负责权威、状态、镜头、连续性、参考图、阶段和验证的生产编译器。

### 0.4 哪些值得借鉴

值得借鉴的是“**垂直视觉执行 Profile**”这个机制，而不是具体的固定风格。一个未来可测试的 Profile 可以包含：

- 明确的视觉命题；
- 主体、环境与空间之间的权力关系；
- 互相兼容的摄影、光线、色彩、材质和空气载体；
- 题材专属的常见失败倾向；
- 清晰稳定的组装顺序；
- 一份展示规则如何协同的完整示例。

它只能在导演明确选择、批准建议，或者授权某一项视觉决策之后生效，并且必须服从现有 Intent Ledger、Visual Strategy、Material Registry、阶段隔离和 Semantic Preflight。

### 0.5 哪些不能写入 Framewright 核心

以下内容不能成为全局默认：

- 固定 `21:9`；
- 固定右侧遗迹、中景森林、左侧沙漠的空间布局；
- 固定左下角极小人物；
- 固定人物只能作为尺度参照；
- 固定左侧夕阳和深景深；
- 固定色盘；
- 对所有项目追加同一份负面词；
- 仅凭出现“森林、遗迹、沙漠”等关键词自动接管创作权。

这些规则一旦进入核心，会造成 authority drift、同质化构图、Intentional Freedom 丢失，并与 Framewright 的 Visual Strategy、摄影载体、参考图属性权威和阶段规则发生冲突或重复。

### 0.6 对 v3.5 的当前建议

**不因为这份 MD 立即修改 v3.5。**

v3.4 已经拥有 Visual Strategy、Shot/Panel 证据链、Material Registry、Style Survival、Surface Fidelity、Stale-Negative、干净输出和失败分层。v3.5 又新增 Adaptive Questioning、Intent Ledger、因果状态、Blocking Readiness、Capture Necessity 和 Semantic Preflight。

当前最稳妥的动作是继续保留 v3.5 本地实验候选，积累真实项目反馈。如果以后要验证 Profile，应单独做一个 paper-profile 实验：证明它能减少无效提问并增强风格一致性，同时不覆盖导演锁定、不污染 Storyboard、不破坏连续性，也不会令不同项目都长成同一张图。只有重复证据成立，才值得另行批准进入 v3.6 或独立实验。

## 1. Executive conclusion

The audited ZHIFEIJI document is not a competing end-to-end architecture for Framewright. It is a highly vertical **art-direction recipe and prompt policy** for one visual family: ancient border forest, desert ruins, nature consuming civilization, monumental scale, and a tiny human scale anchor.

Its central mechanism is effective and coherent:

> recognize an in-domain concept -> assume a fixed directorial thesis -> complete missing visual decisions -> serialize them in a stable order -> reinforce them with a genre-specific failure-avoidance list.

Framewright solves a different problem:

> preserve director intent and authority -> resolve material uncertainty -> establish causal and cinematic structure -> compile the approved state into a stage- and runtime-appropriate artifact -> validate that intent survived.

The strongest lesson from ZHIFEIJI is therefore **not** its fixed `21:9` ratio, right-side cliff, left-side sunset, tiny traveler, palette, or negative list. The useful architectural idea is that a narrow genre can carry a compact, internally coherent **Visual Execution Profile** containing:

- one explicit visual thesis;
- a spatial power relationship;
- compatible camera, light, atmosphere, material, and palette carriers;
- known failure tendencies;
- a deterministic serialization pattern;
- one worked example showing how the pieces cooperate.

That idea may be worth testing later as an **explicitly selected, subordinate Framewright profile**. It should not be imported into the global core, silently activated by keywords, or allowed to override the Intent Ledger, Visual Strategy, Material Registry, stage isolation, or director locks.

No current Framewright change is recommended from this document alone. The evidence supports a future profile experiment, not a v3.5 core rewrite.

## 2. Scope, evidence, and confidence

### 2.1 Included evidence

| ID | Evidence | Audit use |
|---|---|---|
| ZF-CORE | `/Users/jameslee/Desktop/AI Filmmaking/01 Creative Systems/Other Creative Tools/ZHIFEIJI清道夫同款skill/ZHIFEIJI_清道夫作者同款skill电影感自然出图.md` | Declared role, defaults, modes, visual rules, serialization, output templates, and worked example |
| ZF-USE | `/Users/jameslee/Desktop/AI Filmmaking/01 Creative Systems/Other Creative Tools/ZHIFEIJI清道夫同款skill/ZHIFEIJI_清道夫作者同款电影感自然出图_使用说明.txt` | Intended platform, invocation behavior, operator instructions, troubleshooting, and stated boundaries |
| FW35-ENTRY | `skill/framewright/SKILL.md` | Current v3.5 entry workflow and tool boundary |
| FW35-CORE | `skill/framewright/references/framewright.md` | Current authoritative v3.5 architecture |
| FW35-REPORTS | `versions/iterations/v3.5-local-experimental-implementation-report.md`, regression report, and remaining-risk report | v3.5 change ownership, preserved v3.4 rules, static validation, and unproven risks |
| FW34 | `versions/releases/framewright-v3.4.0.md` and local `main` | Stable comparison baseline |

### 2.2 Excluded evidence

Per the approved audit scope, this report does **not** inspect the accompanying tutorial video. It also does not:

- run ZHIFEIJI through ChatGPT image generation;
- compare generated images;
- measure adherence, quality, retries, stochastic variation, or cost;
- inspect the linked ZHIFEIJI website;
- infer undocumented behavior from the author or platform.

The report can therefore assess the **declared mechanism and architectural fit**, but it cannot prove real image quality or production reliability.

### 2.3 Naming precision

The source calls itself a `Skill`, and that name is retained when referring to the product. Structurally, the inspected directory contains a Markdown instruction document, a text usage guide, and a tutorial video. It is not packaged as a formal Codex Skill with a `SKILL.md` entry, metadata contract, tool policy, scripts, references, or validation layer.

For this audit, it is most accurately treated as a **portable system-prompt / knowledge-file recipe**.

## 3. ZHIFEIJI mechanism reverse-engineering

### 3.1 Product promise

ZF-CORE defines a web-ChatGPT image-prompt assistant specialized in border forests, deserts, monumental ruins, nature-eroded civilization, realistic film-still imagery, low CG/game-concept-art appearance, and `21:9` spectacle.

It does not promise a neutral interpretation of any visual request. It promises a recognizable and repeatable house treatment for a narrow subject family. ZF-USE explicitly says the version is vertical rather than universal and recommends separate specialist Skills for unrelated subjects such as beauty, products, interiors, and modern cities.

### 3.2 Invocation and activation

The practical invocation mechanism has two layers:

1. The operator uploads the Markdown document to a chat or Custom GPT knowledge area and tells the model to read and obey it.
2. Inside the document, domain keywords such as ancient forest, desert border, canyon, rust-red cliff, ruined city, giant gate, nature-consuming civilization, tiny human, and sunset dust trigger priority use.

This is a **lexical/domain trigger**, not a capability router with explicit scope state. There is no formal distinction between:

- “the user mentioned a forest”;
- “the user selected this complete visual doctrine”;
- “the user wants only one property, such as material aging, borrowed from the doctrine.”

ZF-USE partially mitigates this by telling the user to state what must be preserved. That is useful operator advice, but it is not an internal authority model.

### 3.3 Two working modes

#### Generation mode

When the user provides only a concept, story fragment, or short scene description, the document instructs the model to auto-complete:

- medium lock;
- aspect ratio;
- spatial layers;
- subject placement;
- light direction;
- material detail;
- atmospheric perspective;
- negative constraints.

This is a high-authority completion mode. It is fast because it treats unspecified creative variables as opportunities for profile defaults rather than unresolved decisions.

#### Rewrite mode

When the user supplies an existing prompt, the document instructs the model to:

- tighten the subject;
- fix the composition relationship;
- remove wavering language;
- translate lore into photographic language;
- strengthen environmental pressure, motivated light, material, air, camera/film texture, and negatives.

This is not merely prose cleanup. It is a **normalization pass toward the profile's preferred image**, including structural composition changes unless the user explicitly protects them.

### 3.4 Embedded directorial doctrine

The document's most important mechanism is its hard-coded hierarchy of visual decisions.

#### Narrative focus

- Space, ruins, erosion, darkness, and a light/shadow danger boundary are primary.
- A person is a scale reference rather than a performance subject.

#### Power relationship

- Environment dominates person.
- Ruins dominate forest while forest simultaneously consumes ruins.
- Cliff mass presses down on the frame.
- The human figure is visually swallowed by scale.

#### Default geography

- Right: rust-red cliff and ruined human city.
- Middle: dark ancient forest.
- Left distance: sunset desert canyon.
- Lower-left or lower-center: tiny traveler.

#### Default capture and look

- `21:9` ultra-wide composition.
- Wide or medium-wide distant observation.
- Deep or medium-deep depth of field.
- Slightly low human-height viewpoint.
- Warm sunset entering from the far left.
- Selective illumination with most of the forest in shadow.
- Low-saturation warm gold, rust brown, dark copper, deep moss, cool gray-blue, and mist white.
- Weathering, cracks, dust, roots, vines, moss, cold mist, particles, leaves, and sparse birds.
- Fine grain, low-contrast film gray, soft highlight roll-off, lifted but readable shadows.

These decisions form a coherent aesthetic grammar. They also explain the document's efficiency: the user is not starting from an empty visual design space.

### 3.5 Internal pipeline

```mermaid
flowchart LR
    A["Concept, story fragment, or existing prompt"] --> B["Domain recognition"]
    B --> C{"Input shape"}
    C -->|"Short concept"| D["Generation mode"]
    C -->|"Existing prompt"| E["Rewrite mode"]
    D --> F["Apply fixed directorial doctrine"]
    E --> F
    F --> G["Complete composition, light, material, air, and palette"]
    G --> H["Serialize in fourteen-part order"]
    H --> I["Append genre failure constraints"]
    I --> J["Copyable prompt plus advice or rewrite note"]
```

There is no declared intermediate scene state, decision ledger, reference-authority record, continuity model, or validation trace. The stable result comes from the consistency of the recipe rather than from state ownership.

### 3.6 Fourteen-part serialization

ZF-CORE requires the final prompt to proceed in this order:

1. medium lock;
2. aspect ratio and lens;
3. overall setting;
4. main spatial structure;
5. right-side cliff and ruins;
6. midground forest and natural erosion;
7. left-side desert canyon;
8. tiny human scale reference;
9. light direction;
10. atmosphere and depth;
11. color control;
12. material realism;
13. camera/film texture;
14. negative constraints.

The order performs three useful functions:

- it moves from global medium and composition toward local finish;
- it prevents atmosphere adjectives from replacing spatial description;
- it produces a predictable artifact that is easy for a user to copy and inspect.

However, several slots are not neutral serializer fields. They embed the one fixed geography and therefore cannot safely become a universal Framewright serialization order.

### 3.7 Failure control

The document includes a broad negative library against fantasy forest, fairy village, game art, CG concept art, anime, glowing plants, modern architecture, neon, pristine ruins, oversized people, over-bright color, detail clutter, exaggerated magic, text, logos, watermarks, and UI.

ZF-USE then gives symptom-specific operator repairs:

- reinforce real-camera observation when the result looks like game art;
- reinforce erosion and cold severity when it becomes fairy-tale fantasy;
- restate the tiny lower-frame human anchor when character scale grows;
- restate the palette and selective light when the image becomes bright or saturated;
- restore the four-layer composition and reduce particles when the frame becomes cluttered.

This is a practical troubleshooting library, but the repair model is predominantly **prompt reinforcement**. It does not classify whether a failure came from planning, serialization, reference authority, runtime capability, rendering, or stochastic model behavior.

### 3.8 Output contract

Generation mode returns:

- one complete cinematic image prompt;
- a separate negative constraint block;
- aspect ratio, subject position, palette, and camera-relationship advice.

Rewrite mode returns:

- one optimized prompt;
- a separate negative block;
- one sentence explaining the rewrite emphasis.

There is no required saved artifact, version fingerprint, source-to-output provenance, or recovery contract. Persistence depends on the chat platform or user copy/paste behavior.

## 4. Framewright baseline and v3.5 evolution

### 4.1 Capabilities already present in v3.4

Framewright v3.4 was already substantially more than a generic prompt improver. Its stable architecture contained:

- one stage at a time across Storyboard, Keyframes, and Video Prompt;
- AUTEUR, APPRENTICE, and SCREENWRITER authority modes;
- Unified Director Intake with a maximum-five material-question batch;
- Visual Strategy and tests against generic coverage;
- one Production Spine as the current production state;
- Committed Shot logic and editorial function;
- Panel Evidence Plan, Board Feasibility, and content-derived panel count;
- concrete Cinematography carriers rather than hollow “cinematic” adjectives;
- Style Survival and Surface Fidelity;
- one property-scoped Material Registry;
- Compactness, Stale-Negative, and Compression Safety passes;
- stage-specific prompt files and clean-output validation;
- generation-evidence recording and scene-local failure repair.

Therefore, the following ZHIFEIJI qualities are **not missing architectural concepts** in v3.4:

- translating abstract cinema language into camera/light/material carriers;
- making composition serve dramatic meaning;
- protecting a distinctive surface and palette;
- controlling stale or irrelevant negatives;
- using a predictable clean artifact;
- separating image structure from final-look authority;
- diagnosing generated output without rewriting unrelated contracts.

### 4.2 Material v3.5 additions

Framewright v3.5-local preserves the v3.4 owners and adds an intent-preservation layer rather than a new parallel workflow:

- dependency-sensitive Adaptive Questioning;
- named, scope-limited delegated authority;
- an Intent Ledger nested inside the Production Spine;
- `director_lock`, `delegated_decision`, `compiler_inference`, `intentional_freedom`, and `unresolved_ambiguity` states;
- Causal State Completion;
- Blocking Readiness before shot commitment;
- Capture Necessity for compiler-inferred shots;
- Semantic Trace and Semantic Preflight;
- a compact assistant-facing Intent Delta;
- finer caution around stochastic and model-behavior failures.

This matters for the comparison because ZHIFEIJI's efficiency comes from silent profile completion, while v3.5 explicitly asks **who owns a decision, why it exists, and whether it may be inferred**.

### 4.3 Architecture contrast

```mermaid
flowchart TB
    subgraph ZF["ZHIFEIJI: style convergence"]
        Z1["Domain cue"] --> Z2["Profile defaults"] --> Z3["Fixed visual recipe"] --> Z4["Prompt"]
    end
    subgraph FW["Framewright v3.5: intent-preserving compilation"]
        F1["Director intent and assets"] --> F2["Authority and adaptive intake"] --> F3["Intent Ledger and Production Spine"] --> F4["Shot, panel, and stage compilation"] --> F5["Semantic Preflight"] --> F6["Clean artifact"]
    end
```

ZHIFEIJI optimizes for **rapid aesthetic convergence**. Framewright optimizes for **traceable directorial control across production stages**.

## 5. Mechanism-level diff matrix

| Dimension | ZHIFEIJI V3 | Framewright v3.4 | Framewright v3.5-local | Audit finding |
|---|---|---|---|---|
| Primary scope | One narrow image genre | General AI-filmmaking stage compiler | Intent-preserving evolution of v3.4 | Complementary scope, not competing product identity |
| Activation | Upload/read instruction plus domain keywords | Explicit Framewright invocation and selected active scope | Same explicit invocation; adaptive scope handling | Keyword activation is too implicit for core authority |
| Input types | Short concept, story fragment, or existing image prompt | Scene intent, assets, stage request, prior approved state | Same, plus explicit decision ownership | ZHIFEIJI has a simpler operator surface but less state precision |
| Working modes | Generate or rewrite | Three director modes and three output stages | Same modes/stages; advisor is scoped authority, not a mode | Do not add Generate/Rewrite as new Framewright modes |
| Questioning | No formal intake; user is advised to state protected details | One consolidated material-question batch, maximum five | Dependency-sensitive one-at-a-time or independent batch, maximum five | ZHIFEIJI speed comes partly from skipping authority resolution |
| Creative authority | Profile defaults fill silence | Director remains authority; mode controls inference | Every material decision has owner, scope, rationale, and status | Direct import would conflict with v3.5's central design principle |
| Intentional openness | Treated mainly as a field to complete | Minor/decorative gaps may remain open | `intentional_freedom` is protected from over-specification | Profile defaults must not consume intentional freedom |
| Scene state | Implicit inside one prompt | Production Spine owns scene and unit state | Spine plus nested Intent Ledger, causal state, and blocking readiness | ZHIFEIJI is unsuitable as a state owner |
| Spatial strategy | One fixed right/middle/left/lower composition | Visual Strategy establishes a scene-specific viewer premise | Same, with rationale and lock protection | Spatial-power thesis is borrowable; fixed geography is not |
| Shot design | Distant wide/medium-wide profile preference | Committed shots require editorial and camera function | Adds causal/blocking readiness and Capture Necessity | A profile may propose carriers but cannot originate shot necessity |
| Panel logic | None | Evidence-derived panel count; layout cannot originate count | Same protected contract | No transferable panel architecture |
| Storyboard role | Not defined | Monochrome line-only planning stage | Same, explicitly a structure-inspection surface | ZHIFEIJI final color/material must not bleed into Storyboard rendering |
| Final look | Fixed palette, light, atmosphere, film texture | Cinematography, final look, Style Survival, Surface Fidelity | Same, now traceable to approved intent | Most natural optional-profile connection point |
| References | User may upload references; no property authority model | Material Registry scopes identity, pose, structure, style, motion, etc. | Same registry; Preflight checks unauthorized inheritance | ZHIFEIJI must never become a second reference registry |
| Negative constraints | Fixed broad list | Stale-Negative removes obsolete or inactive negatives | Same, plus provenance/preflight checks | Failure themes are useful; a permanent verbatim block is not |
| Prompt order | One fixed fourteen-part recipe | Stage- and runtime-specific serializers | Same, with semantic trace and clean-output boundary | Borrow ordering principles, not fixed geography slots |
| Output | Prompt, negatives, advice/rewrite note | One saved stage artifact plus narrow Storyboard exception | Same plus assistant-facing Intent Delta | Framewright has stronger persistence and provenance |
| Sequence continuity | Not represented | Production Spine and unit continuity | Adds causal completion and blocking readiness | ZHIFEIJI is a single-image profile, not a sequence compiler |
| Validation | Human inspection and symptom repair | Large pre-save contract validation | Adds Intent Coverage, Provenance, Silent Invention, Freedom, Compression, and Cross-Stage tests | v3.5 should validate any future profile; profile must not validate itself |
| Failure diagnosis | Restate desired traits and negatives | Planning/serialization/render/reference/runtime/model layers | Adds causal confidence and stochastic caution | Troubleshooting examples may inform tests but not replace taxonomy |
| Version/recovery | Document version only; chat persistence | Versioned core, releases, artifacts, local repair | Local candidate with stable v3.4 fallback | Framewright recovery model remains superior and authoritative |

## 6. What Framewright already represents

### 6.1 “Space power relationship” already has an owner

ZHIFEIJI's most distinctive phrase-level idea is that the environment should dominate the human. Framewright already has the correct general owner for this: `Visual Strategy`, followed by executable composition, viewpoint, scale, information-control, and camera carriers.

What ZHIFEIJI contributes is a **good example of a strong visual thesis**, not a missing global field.

### 6.2 “Photographic language instead of lore” already has an owner

Framewright's Cinematography Layer requires motivated sources, light direction, contrast/exposure behavior, lens/depth behavior, camera distance, texture, atmosphere, composition, negative space, and color relationships. It explicitly rejects unsupported labels such as “cinematic,” “premium,” “beautiful,” and “moody.”

ZHIFEIJI demonstrates this translation well for one genre, but does not require a new core operator.

### 6.3 Material and film texture already have owners

Weathering, cracks, dust, root pressure, grain, highlight roll-off, shadow detail, and restrained palette map naturally to existing `Style Survival` and, when identity-critical and explicitly authorized, `Surface Fidelity`.

They should not be added as global material defaults or as a second Material Registry.

### 6.4 Negative-list hygiene already has an owner

ZHIFEIJI's negative library captures real failure tendencies for its domain. Framewright's Stale-Negative Pass already determines whether a negative is current, relevant, and necessary, while preferring positive containment when possible.

The compatible lesson is to maintain **profile-local known failure tendencies**, then compile only the relevant subset. The incompatible move would be to append the same long negative block to every artifact.

### 6.5 Stable serialization already has an owner

Framewright already separates planning state, stage compilation, runtime serialization, clean prompt output, and assistant-facing handoff. The useful lesson from ZHIFEIJI is that profile-local carriers should appear in a readable global-to-local order. It does not justify a second pipeline or universal fourteen-slot schema.

## 7. Borrowability assessment

### 7.1 Borrowable as a future optional profile

The following mechanism is worth preserving as an architectural candidate:

| Candidate element | Why useful | Required Framewright boundary |
|---|---|---|
| Profile thesis | Quickly establishes a coherent visual argument | Must be explicitly selected or approved |
| Spatial power relation | Prevents generic subject-centered framing | Becomes an approved Visual Strategy carrier, not a global rule |
| Compatible carrier bundle | Keeps camera, light, palette, atmosphere, and material mutually supportive | Each material decision remains subordinate to locks and stage authority |
| Domain failure library | Encodes recurring genre-specific failure modes | Compile selectively through Stale-Negative and positive containment |
| Serialization recipe | Improves prompt readability and reduces omission | Remain subordinate to active stage and runtime serializer |
| Worked example | Demonstrates interaction among rules better than isolated vocabulary | Clearly label as example, never hidden default authority |

### 7.2 Conceptual profile boundary

If separately approved in a future iteration, a Framewright-compatible profile would conceptually need to declare:

```yaml
visual_execution_profile:
  profile_id:
  intended_domain:
  activation: explicit_approval_only
  visual_thesis:
  spatial_power_proposal:
  camera_carriers:
  lighting_carriers:
  palette_logic:
  material_and_atmosphere_carriers:
  known_failure_tendencies:
  stage_permissions:
  denied_authority:
  override_and_exit_policy:
```

This is an **audit sketch**, not an implementation specification. It shows the minimum boundary needed to avoid silent authority expansion.

### 7.3 Correct architectural position

The best provisional position is a subordinate, explicitly admitted **Visual Execution Profile**, not:

- a fourth director mode;
- a fourth output stage;
- a runtime adapter;
- a second Production Spine;
- a second Material Registry;
- a universal negative library;
- a replacement for Adaptive Questioning.

Its stage permissions should differ:

- **Storyboard:** only approved structural relationships such as scale, geography, and subject/environment hierarchy may influence planning composition; final color, grain, material finish, and cinematic grade remain excluded.
- **Keyframes:** approved final-look carriers may be expressed fully because this is the natural final-image planning surface.
- **Video Prompt:** approved profile carriers may survive through motion, continuity, runtime feasibility, and target serialization.

### 7.4 Authority admission rule

A future profile should enter Framewright only through one of these routes:

1. The director explicitly selects the profile and its declared scope.
2. Framewright presents it as an advisor option and the director approves it.
3. The director delegates a named look-development area, allowing Framewright to recommend and apply it within that area only.

Domain keywords alone must never grant authority. A forest, ruin, desert, or tiny person can exist in many visual systems that intentionally reject the ZHIFEIJI doctrine.

## 8. Conflict and rejection report

### 8.1 Do not import into Framewright core

| ZHIFEIJI rule | Conflict if globalized | Decision |
|---|---|---|
| Default `21:9` | Overrides requested stage, platform support, composition, or runtime surface | Reject as core default |
| Right cliff / middle forest / left desert | Replaces scene-specific geography and Visual Strategy | Reject as core default |
| Tiny lower-left or lower-center person | Can erase performance, relationship, and character-led intent | Reject as core default |
| Person only as scale anchor | Conflicts with character-led and performance-led scenes | Reject as core default |
| Left sunset as main light | Overrides motivated light and director locks | Reject as core default |
| Deep or medium-deep focus | Overrides shot-specific information control | Reject as core default |
| Fixed palette | Can overwrite supplied art direction and reference authority | Reject as core default |
| Full negative block | Can become stale, contradictory, target-ineffective, or token-heavy | Reject as universal serializer content |
| Keyword-priority activation | Grants creative authority without explicit selection | Reject as activation policy |
| “Must” normalization in rewrite mode | Can silently redesign an authored composition | Reject without scoped delegation |

### 8.2 Potential redundancies if implemented carelessly

| Proposed duplication | Existing owner that must remain sole owner |
|---|---|
| A second “style state” object | Production Spine plus Intent Ledger |
| Profile-specific composition registry | Visual Strategy and Committed Shot fields |
| Separate material/style reference list | Material Registry |
| New generation/rewrite director modes | Existing three director modes and active stages |
| Fourteen new workflow passes | Existing craft operators and serializers |
| New anti-CG global negative system | Stale-Negative, Style Survival, and target serialization |
| Profile-specific validation truth | Semantic Preflight and current validation owners |

### 8.3 Apparent conflicts that are actually clarifications

Some differences are compatible if their authority is made explicit:

- “Environment dominates person” is not inherently incompatible with director control; it becomes compatible when the director selects it as the scene's Visual Strategy.
- Auto-completing air, wear, or minor particles is not inherently silent invention; it can be safe compiler inference when reversible, low impact, within delegated scope, and not consuming intentional freedom.
- A stable prompt order is not a rival workflow; it can be a subordinate serializer pattern when it does not own creative state.
- A genre-specific negative is not always stale; it is valid when the corresponding failure risk remains active and the target surface responds to it.
- An example composition is not a forbidden preset; it becomes a problem only when example provenance turns into hidden authority.

These cases require clarification and admission rules, not deletion of the underlying idea.

## 9. Mechanism strengths worth learning from

### 9.1 It starts from a visual argument, not isolated adjectives

The document's strongest design move is to define who visually dominates whom. Camera, geography, scale, light, atmosphere, and material all reinforce that argument. This creates more coherence than a flat vocabulary list.

### 9.2 It makes defaults cooperate

The fixed left light, right mass, dark midground, small lower-frame human, restrained palette, and atmospheric separation form one mutually reinforcing system. Even though the defaults are too specific for Framewright core, their **internal compatibility** is exemplary.

### 9.3 It converts a vague request into an immediately usable artifact

The two-mode surface is easy to understand: give it an idea or give it a prompt. The result has a predictable structure and a short explanation. Framewright should preserve its deeper architecture, but this simplicity is a useful usability reference for future profile interaction.

### 9.4 It documents common visual failure symptoms in user language

“Looks like game concept art,” “forest is too fairy-tale,” “person is too large,” and “everything competes for attention” are actionable human observations. They could become useful qualitative test prompts for a future profile experiment, while Framewright retains its more precise failure ownership.

## 10. Limitations that should not be romanticized

### 10.1 Coherence can become sameness

The same aspect ratio, geography, human placement, light direction, palette, and atmosphere will tend toward a recognizable repeated composition. Without generation samples, this report cannot quantify repetition, but the specification itself contains the convergence pressure.

### 10.2 “Low AI” language is not a causal guarantee

Repeatedly saying “not CG,” “not concept art,” or “real camera” may help on some models, but the document does not distinguish prompt causality from model prior, surface behavior, stochastic variation, or selection bias.

### 10.3 Single-image success does not establish sequence fitness

The profile does not define start/end state, shot function, continuity, object progression, reference lifecycle, sound, temporal rhythm, generation-unit feasibility, or cross-stage authority. It should not be treated as evidence for long-form video architecture.

### 10.4 User-provided references remain under-specified

ZF-USE permits uploaded references but does not define whether a reference controls identity, pose, crop, composition, environment, material, light, or style. Framewright's property-scoped authority must remain superior.

### 10.5 Repair is mostly additive

The troubleshooting method usually reinforces more desired language or exclusions. This can work, but it can also lengthen prompts or conceal a planning/runtime problem. Framewright should keep smallest-layer diagnosis and selective repair.

## 11. Incremental evolution path — planning only

No step below is authorized by this audit.

### Path 0 — Preserve v3.5 unchanged

Keep the current local experiment exactly as it is while collecting real v3.5 production feedback. This is the recommended immediate action because the ZHIFEIJI document does not expose a critical Framewright defect.

### Path 1 — Paper-profile experiment

Without changing core architecture, describe one temporary ZHIFEIJI-inspired profile outside the authoritative core and manually test whether Framewright can admit it through existing authority and Visual Strategy rules.

Suggested cases:

1. an in-domain scene with broad delegated art direction;
2. the same domain with a conflicting director lock, such as frontal character emphasis or right-side sunset;
3. an out-of-domain forest scene that must not activate the profile;
4. a Storyboard request where final-look color and texture must remain isolated;
5. a multi-shot Video Prompt where the look must survive without replacing continuity or shot function.

### Path 2 — Evaluate profile value

Record qualitative evidence:

- Did the profile reduce repetitive questioning?
- Did it add useful world texture without taking story authority?
- Which defaults were accepted, revised, or rejected?
- Did intentional freedom survive?
- Did the resulting composition become samey?
- Did Stale-Negative remove irrelevant exclusions?
- Did Storyboard isolation and reference authority remain intact?

### Path 3 — Separately approve or reject architecture work

Only repeatable evidence should justify a later iteration proposal. That proposal would need to decide:

- whether profiles are a real architectural layer or merely reusable reference documents;
- how explicit activation and exit work;
- whether profile state belongs inside existing Visual Strategy/Intent Ledger fields or needs a minimal derived view;
- how profiles remain stage-aware without duplicating runtime adapters;
- how profile libraries are versioned, tested, and prevented from drifting into global defaults.

This decision belongs to a future v3.6 or separately named experiment, not an unreviewed amendment to the current v3.5 candidate.

## 12. Final classification

| Question | Conclusion |
|---|---|
| Is ZHIFEIJI an alternative Framewright architecture? | No. It lacks production state, authority, continuity, reference lifecycle, stage separation, validation, and recovery. |
| Is it merely a bag of cinematic adjectives? | No. It contains a coherent spatial thesis, compatible carrier bundle, stable serializer, and failure library. |
| Should its concrete defaults enter Framewright core? | No. They are intentionally genre-specific and would create authority drift and visual sameness if globalized. |
| Is there a transferable mechanism? | Yes: an explicitly selected vertical Visual Execution Profile subordinate to existing Framewright owners. |
| Does v3.5 need immediate iteration because of this audit? | No. Preserve v3.5 and collect evidence before proposing a profile layer. |
| Where is the strongest future fit? | Keyframe final-look planning and Video Prompt style survival; structural influence on Storyboard only after approval, with final-look isolation preserved. |

The durable lesson is:

> Framewright should learn from ZHIFEIJI's **coherent vertical defaults**, but must preserve its own **explicit authority, stage isolation, state ownership, and intent traceability**. A profile may propose a visual world; it may not silently become the director.

## 13. Audit boundary and current status

This report is the only artifact authorized by the audit. It does not amend Framewright v3.5, approve a profile implementation, modify the stable v3.4 fallback, analyze the tutorial video, or claim generated-image evidence.

Any later profile experiment, core change, adapter change, generation test, Desktop synchronization, GitHub synchronization, release promotion, or deletion/redundancy cleanup requires a separate review and explicit approval.
