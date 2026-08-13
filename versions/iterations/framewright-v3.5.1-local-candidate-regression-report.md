---
title: "Framewright v3.5.1 Local Candidate Regression Report"
status: "STATIC AND COMPILE-ONLY PASS"
test_date: "2026-08-13"
baseline_version: "3.5.0"
candidate_version: "3.5.1"
external_generation_calls: 0
---

# Framewright v3.5.1 本地候选回归报告

## 1. Test surfaces

- Skill folder validation；
- Core / Skill / Seedance profile YAML frontmatter；
- Markdown fence 与 whitespace integrity；
- protected semantic anchors；
- deterministic prompt / state / compile-trace validator；
- positive 与 deliberate-failure fixtures；
- Idol、Zolla、Loong、Blade & Havoc、剁椒鱼头、Freefall 六案例脱敏 compile-only trace；
- destructive reverse checks；
- frozen baseline / branch / no-upstream / Desktop no-change checks。

## 2. Deterministic suite

最终 fixture suite 共 25 项：

- Batch 1 positive canonical traces：6；
- Batch 1 state positive：1；
- Batch 1 deliberate failures：5；
- Batch 2 positive traces：6；
- Batch 2 deliberate failures：5；
- validator dialect / binding fixtures：2。

结果：`25 / 25` 与预期一致。Deliberate-failure fixtures 必须被 validator 拒绝；因此结果不是依靠只检查“能否运行”的假绿灯。

## 3. Covered failure classes

- missing / duplicate mode line、workflow leakage、unresolved placeholder、character limit；
- native mention mapping、generic handle placement；
- state schema、duplicate active revision、active / superseded overlap、unselected take；
- single serialization owner、single active Stage / Mode / Spine / Registry；
- split-unit start / end state 与 independent execution；
- observable-intent orphan、dialogue causality、carrier density、shot-scale legibility；
- feasibility system explanation、weakest beat、competing objectives、priority stack；
- unapproved structural subtraction；
- operator path / lens target conflation、motion-state handoff；
- incomplete physical chain、missing transformation topology；
- silent change to requested reference strategy；
- vocal event count 与 silence ownership。

## 4. Protected behavior

以下 3.5.0 行为通过 semantic anchor 与 compile-only trace 保持：

- 一个入口、一个 active Stage、三个 Director Mode、三个 Stage；
- Unified Director Intake、authority order、一个 Spine / Ledger / Registry；
- one GU / one storyboard board、board / panel 16:9、Panel Evidence provenance；
- Storyboard one-initial-generation exception 与 planning-only runtime admission；
- Keyframe 仍 prompt-only 且产品定位未改；
- no auto-split / merge、semantic timing、continuous phases are not cuts；
- 默认环境声与同步动效、默认无音乐；
- Seedance native mention、Run Card / clean prompt separation；
- no automatic retry、variant、Keyframe image 或 Video generation；
- generated prompt 不含 Ledger、Trace、Delta、approval 或 risk commentary。

## 5. Reverse checks

反向验证临时破坏候选副本中的关键语义与 negative fixture expectation；validator / regression 必须退出失败。临时副本位于系统临时目录，不修改仓库文件。

## 6. Conclusion

规范完整性、隔离边界与 compile-only 行为通过。此结论不证明 Seedance 2.5 实际渲染服从度、成本、重试率或跨任务真实对话体验。
