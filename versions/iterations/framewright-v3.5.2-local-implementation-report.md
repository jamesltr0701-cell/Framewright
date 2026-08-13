---
title: "Framewright v3.5.2 Local Implementation Report"
status: "IMPLEMENTATION COMPLETE - LOCAL CANDIDATE"
report_date: "2026-08-13"
baseline_commit: "c89873c86dbac2b8a57635d6cf9b58bd646d29c9"
candidate_version: "3.5.2-local"
seedance_profile_version: "1.3.0"
branch: "codex/framewright-v3.5.2-local-seedance-qualification"
external_generation_calls: 0
---

# Framewright v3.5.2-local 实施报告

## Outcome

WP-01 至 WP-10 已在本地候选中实施。Core 保持 default-deny：除版本号与 C01 clean-output contract 外，没有修改 Director Mode authority、intake、Production Spine、scene grammar、Storyboard / Keyframe 行为、GU boundary、sound default 或 generation boundary。

该候选的来源资格为：`BytePlus-current / Lark-visible / reconciled-PDF-qualified`。Lark 原生导出失败；用户明确授权使用当前在线可见证据、BytePlus 在线全文和本机核对补全 PDF 继续。

## Implemented work packages

### WP-01 — mode-label separation

- 每个 compilation scope 仍选择且仅选择一个 Director Mode；
- mode 必须在对话中向用户声明，并保存在 internal compile trace；
- Storyboard、Keyframes、Video Prompt clean artifacts 不再包含 literal `[MODE: ...]`；
- validator 将 literal mode label 判定为 `mode_metadata_leak`；
- compile trace 缺少唯一 mode 或 conversation declaration 时失败。

### WP-02 / WP-03 — parameter locks and Extend direction

- 增加 duration / aspect-ratio provenance；
- Smart Edit 使用 source-ratio `adaptive` 和 duration `-1`；
- First / Last 使用 first-image-ratio `adaptive`，并要求 endpoint ratio compatible；
- Extend 使用 source-ratio `adaptive`，duration independently user-settable；
- Extend 增加 `forward | backward`，分别绑定 source end / source start boundary，并要求明确 trigger。

### WP-04 — existing advanced controls

- multi-keyframe：ordered anchors、state mapping、denied authority、no implied cuts；
- coarse blockout：路径 / blocking / camera 等结构权限，否认 identity / final surface / final style；
- fine blockout：保留结构 / motion / camera，否认临时材质与 identity authority；
- seamless transition：before / after、trigger、camera path、transformation、arrival state、audio bridge、no pixel-identical promise；
- `one-click video` 明确保留为案例标签，不成为 route。

### WP-05 — material admission

- hard limits：50 total assets；30 images；10 videos / 30 combined seconds；10 audio clips / 30 combined seconds；
- stable ranges 与 hard limits 分离；stable-range excess 只生成 warning；
- 15-panel storyboard 是稳定性建议，不覆盖 one GU / one board，也不自动拆分。

### WP-06 / WP-07 — syntax and timing

- explicit-scope-only music `(...)`、SFX `<...>`、dialogue `{...}`、visible subtitle `■■...■■`；
- 未请求 music / dialogue / visible text 不得被特殊语法激活；
- exact glyph mapping 标注为 snapshot-qualified；
- semantic timing 保持默认；numeric timing 只在合格触发下启用，并验证连续、非重叠、duration、trigger、camera instruction 与 continued state。

### WP-08 / WP-09 — limitation and compactness

- 关键排版、公式、标牌和 frame accuracy 必须 assistant-facing 提示 Prompt-only 边界，并推荐 prepared asset、locked reference 或 post；
- 10,000-character ceiling 保留，但不等同于 compactness proof；
- qualification 记录字符数与 semantic anchors，并拒绝 leakage / inactive blocks。

### WP-10 — deterministic qualification

- 原 25 个 fixtures 完整保留并等价迁移 C01；
- 新增 28 个 `seedance25_*.yaml` positive / deliberate-failure fixtures；
- total suite：53 fixtures。

## Files changed

Core / skill / adapter / validator：

- `skill/framewright/SKILL.md`
- `skill/framewright/references/framewright.md`
- `skill/framewright/references/runtime_profiles/seedance_2_5.md`
- `skill/framewright/scripts/validate_framewright.py`

Qualification：

- `testing/next-local/expected/protected_anchors.yaml`
- 22 个 C01-related legacy fixture narrow migrations；
- 28 个新增 `seedance25_*.yaml` fixtures。

Reports：

- protected baseline manifest；
- contradictions / redundancies report；
- implementation report；
- regression report；
- remaining-risk report。

## Explicitly untouched

- `README.md`
- `versions/releases/**`
- Desktop Framewright mirror
- GitHub / remote branches
- historical prompts and project outputs
- `Framewright/`、`output/`、`outputs/`、`storyboard/`

No external generation or credit spend occurred.
