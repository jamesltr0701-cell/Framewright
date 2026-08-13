---
title: "Framewright v3.5.1 Local Candidate Remaining Risk Report"
status: "LOCAL REVIEW OR FUTURE FIELD TEST REQUIRED"
report_date: "2026-08-13"
candidate_version: "3.5.1"
external_generation_calls: 0
---

# Framewright v3.5.1 本地候选剩余风险报告

## 1. Not proven

本轮没有外部生成，因此仍未证明：

- Seedance 2.5 是否稳定执行 embodied performance、camera body / lens separation、motion handoff、physical topology、reference crop strategy 与 vocal count；
- `framewright_state.yaml` 在真实跨任务制作中是否比对话状态更可靠且不会增加维护负担；
- validator 是否会在未覆盖的合法 Prompt 方言上产生 false positive；
- richer derivation 是否会使简单 Prompt 变长或问询疲劳；
- surface / provider / seed / retry / cost 的真实基线。

## 2. Principal watch points

| Risk | Watch for | Smallest response |
|---|---|---|
| State duplication | 用户把 state 当第二份可自由改写的 Spine | 先 reconcile，保持最新明确决定优先 |
| Performance overdirection | 每个 beat 都出现眨眼、吞咽、握拳、叹气 | 收缩为一至三个 shot-legible carrier |
| Feasibility bureaucracy | low-risk 场景也输出完整风险报告 | 无 material risk 时 silent pass |
| Camera contamination | 稳定镜头被加上失焦、摇晃或错误修正 | 只在 embodied camera material 时展开 |
| Physics bloat | 普通动作变成工程说明 | 只展开 production-critical causality |
| Reference paralysis | 风险门导致所有附件都被拒绝 | 说明实际 loss，优先窄 admission 而非全移除 |
| Dialogue overcontrol | 未请求对白时仍激活 event schema | explicit vocal scope 之外保持 inactive |
| Validator false confidence | 关键词通过被误认成创作质量通过 | 保持 semantic / aesthetic judgment 人工审阅 |

## 3. Deferred work

- WP-H Evidence Normalization；
- WP-I Seedance 2.5 runtime qualification；
- 外部 A/B generation；
- Keyframe keep / restore / retire 决策；
- Timing Proof / animatic；
- multi-model adapter 与自动 repair memory。

## 4. Promotion boundary

当前是未发布、未推送的本地 `3.5.1` 候选。晋升仍需独立授权；届时才可创建 immutable release snapshot、更新稳定 README、同步 Desktop Framewright 与推送 GitHub，并按三处同步规则逐项核对。

回退方式：切回本地 `main` 即恢复稳定 `3.5.0`。保留实验分支与报告作为可审阅证据，不需要删除。
