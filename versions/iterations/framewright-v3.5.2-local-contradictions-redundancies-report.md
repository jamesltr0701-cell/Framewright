---
title: "Framewright v3.5.2 Local Official-Source Freeze Decision Report"
status: "RESOLVED - IMPLEMENTATION RESUMED"
report_date: "2026-08-13"
baseline_version: "3.5.1"
baseline_commit: "c89873c"
target_candidate: "3.5.2-local"
external_generation_calls: 0
core_files_modified: false
---

# Framewright v3.5.2 本地官方来源冻结阻塞报告

## 1. Safe pause result

Phase 0 的本地基线检查通过：

- branch：`codex/framewright-next-local-experiment`；
- HEAD：`c89873c`；
- Core：`3.5.1`；
- Seedance adapter：`1.2.0`；
- baseline regression：`25 / 25`；
- Core、Skill、adapter、validator 与 testing 文件没有新 diff；
- `Framewright/`、`output/`、`outputs/`、`storyboard/` 未触碰；
- 外部生成与 credits：0。

本轮尚未创建目标 branch，因为正式计划要求先完成两份最新官方指南 freeze；该门未完全通过时，不启动 implementation。

## 2. Retry result — one official source recovered

正式计划要求重新读取并冻结以下最新官方页面全文：

1. `https://bytedance.larkoffice.com/docx/A88jd0B47oAd8zxWp5ycZFMfnxh`
2. `https://docs.byteplus.com/en/docs/ModelArk/2607689`

2026-08-13 重试结果：

- BytePlus ModelArk 页面成功返回 HTTP 200，页面标注 `Last updated: August 11, 2026 09:41:01`；
- 取得的 HTML 为 579,501 bytes；从页面内嵌文档数据恢复出约 39,487 characters 的正文；
- 正文能够核对 Seedance 2.5 的 locked / unlocked route、最多 50 个 reference assets、forward / backward extension、`ratio=adaptive`、first / last frame role、storyboard / keyframe、audio edit、30-second examples、20-second edit recommendation、15-panel storyboard recommendation等项目；
- Lark 页面在已登录 Chrome 中存在两份可见标签页，标题均为 `Dreamina Seedance 2.5 Prompt Writing Guide`，因此页面身份与账号可见性已确认；
- 但 Lark 长文档正文不是普通网页文本层。正文读取、截图与只读全选复制均在浏览器控制超时；命令行读取则进入登录重定向循环；
- 此前提及的本地两份 reflowed PDF 当前已不在原 Downloads 路径，不能作为本轮辅助复核来源。

因此，先前“两个官方页面均不可读取”的结论已撤销；当前阻塞缩小为：**BytePlus 用户指南已冻结，Lark 官方提示词指南仍未取得可审计正文。**

## 3. Remaining blocking condition B01

按计划 §3.3 与 Phase 0，Lark prompt guide 与 BytePlus user guide 都属于 mandatory official sources。BytePlus 正文虽覆盖大部分 capability contract，但不能证明它完整包含 Lark 指南中的：

- exact prompt-facing wording；
- 特殊音频与可见文字写法；
- prompt compactness / structure guidance；
- 示例与硬规则、建议、限制之间的语义分层；
- 可能只在 prompt guide 中出现的表面语法更新。

继续 WP-06、WP-07、WP-09 与相应 WP-10 fixtures 将需要推测 Lark 原文。按 default-deny 和 source hierarchy，本轮仍须停在 implementation 之前。

## 4. What is now verified from the current BytePlus source

以下信息可以进入后续 official-source ledger，但在 Lark freeze 完成前不实施：

- Seedance 2.5 将 editing、first / last frames、extension 归为 locked route；reference、storyboard、keyframe 通常属于 unlocked route；
- reference assets 单次请求最多 50 个，包含 image、audio、video；
- extension 支持 forward / backward，并要求 prompt 包含明确 extension trigger；
- extension 与 first / last frame route 的 ratio 必须使用 `adaptive`，由输入资产锁定；
- first / last frame 使用 `first_frame` / `last_frame` role；
- video editing 可按 timestamp 指定生效时间；20 秒以内通常更稳定；
- multi-panel storyboard 当前建议不超过 15 panels，推荐 stick-figure / line-art，避免在 storyboard 画面内直接加字；
- keyframes 对输入图像对齐更严格，而 storyboard reference 不保证严格对齐；
- extension 为保持音画连续性，官方建议输入与输出都用 MOV；
- 官方示例包含 30 秒生成，但示例本身不能自动上升为所有 route 的硬限制。

## 5. Safe next options

### A — 取得 Lark 当前正文（仍为完整计划的合规路线）

不要求用户向聊天导入 PDF 或 Markdown。可改为以下任一方式：

- 用户在 Lark 中将该文档临时设为“任何获得链接的人可查看”，再重新读取；
- 用户明确授权执行一次 Lark 自带的导出 / 下载，由执行者在已登录页面取得文档副本；
- 用户把正文复制到本地普通 `.txt` 文件路径，执行者直接读取该路径。

### B — 修改 source hierarchy

用户明确批准以 2026-08-11 BytePlus 当前在线正文作为本轮唯一 mandatory official source，并把 Lark prompt guide 降级为 deferred corroboration。

影响：可以继续，但这是对正式计划的 material amendment；实施报告必须标记 `BytePlus-qualified / Lark-deferred`，不得声称完成原蓝图定义的双源冻结。

## 6. Source-gate resolution

The user explicitly authorized the fallback source hierarchy after Lark export failed. The frozen implementation evidence is now:

- current BytePlus online full text, last updated August 11, 2026;
- current Lark visible document identity, August 12 modified marker, table of contents and visible core passages;
- local reconciled Prompt Guide PDF from the same Lark source;
- the approved compatibility audit and v3.5.2 plan.

This resolves the prior B01 source blocker under the label `BytePlus-current / Lark-visible / reconciled-PDF-qualified`. A protected baseline manifest has been created, and the local target branch exists without upstream.

## 7. C01 — existing-fixture migration conflicts with the file whitelist

Implementation exposed a new plan-internal contradiction before any Core edit:

- WP-10 says the existing 25 fixtures must remain, and fixtures directly testing the old mode-line contract must be equivalently migrated;
- Acceptance Criterion 14 repeats that C01-related existing expectations must be migrated rather than deleted or weakened;
- the existing suite contains 22 fixture files with literal `[MODE: ...]` lines;
- §6.1 does not whitelist edits to `testing/next-local/fixtures/*.yaml`;
- §6.2 permits only **new** `testing/next-local/fixtures/seedance25_*.yaml` files.

Once the validator implements WP-01, unchanged positive legacy fixtures containing literal mode labels will correctly fail with `mode_metadata_leak`. Keeping a legacy bypass in the runner would preserve a second obsolete clean-prompt contract and would not satisfy Acceptance Criteria 4 or 14. Silently editing existing fixtures would violate the default-deny path whitelist.

### Recommended narrow amendment

Add one path exception:

> Existing `testing/next-local/fixtures/*.yaml` files may be edited only to remove literal mode lines and, where the fixture directly tests the old mode-line rule, replace that expectation with equivalent conversation-visible / internal-single-mode / clean-prompt-leak protection. All non-C01 prompt content, expectations and error classes remain frozen.

This permits the migration explicitly required by WP-10 without authorizing general fixture rewrites.

### Rejected workaround

Do not add a `legacy_mode_allowed` validator or runner bypass. It would make the suite certify two contradictory definitions of a clean Prompt and weaken the acceptance gate.

## 8. Current boundary

At this pause point:

- target branch `codex/framewright-v3.5.2-local-seedance-qualification` exists locally with no upstream;
- protected baseline manifest exists;
- Core、Skill、adapter、validator 和 fixtures 尚未修改；
- no release snapshot, Desktop update, GitHub push or external generation occurred.

## 9. C01 resolution

The user approved the recommended narrow fixture-whitelist amendment. Existing fixtures were changed only to:

- remove literal clean-Prompt mode labels;
- retain exactly one internal `director_modes` entry in compile traces;
- add `conversation_mode_declared: true` to compile traces;
- remove the retired `mode_line_missing` expectation from the one prompt-hygiene fixture that directly tested it.

No non-C01 expectation or error class was weakened. A dedicated negative fixture now rejects mode metadata leakage and undeclared conversation mode. C01 is closed.
