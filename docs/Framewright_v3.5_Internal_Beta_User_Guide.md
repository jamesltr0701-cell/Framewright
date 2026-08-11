---
title: "Framewright 3.5 内测用户快速说明"
version: "3.5.0"
status: "internal_beta_user_guide"
updated: "2026-08-11"
language: "zh-CN"
---

# Framewright 3.5 内测用户快速说明

## 1. 你会收到哪些文件

基础内测使用两个文件：

1. `framewright-v3.5.0.md`：Framewright 3.5.0 的正式版本文件。
2. `Framewright_v3.5_Internal_Beta_User_Guide.md`：这份快速说明。

如果测试目标是 **Seedance 2.5 Video Prompt**，再增加：

3. `seedance_2_5.md`：Seedance 2.5 专属运行时适配文件。

不需要安装 Skill，也不需要访问 GitHub。

## 2. 最简单的使用方法

1. 新建一个 Codex 对话。
2. 把 `framewright-v3.5.0.md` 直接拖进对话。
3. 发送：

```text
请完整读取我上传的 framewright-v3.5.0.md。
本轮使用 Framewright 3.5.0，并以这份文件作为唯一规则来源。
请先回复：Loaded: Framewright v3.5.0
然后等待我提供场景。
```

4. Codex 确认版本后，再发送你的故事、场景、参考素材和任务。

这种方式只对当前对话生效。新开对话时，需要重新拖入 MD。

### 测试 Seedance 2.5 Video Prompt

同时拖入 `framewright-v3.5.0.md` 和 `seedance_2_5.md`，然后发送：

```text
请先完整读取 framewright-v3.5.0.md，再完整读取 seedance_2_5.md。
本轮使用 Framewright 3.5.0，并以主 Framewright 文件作为最高规则来源；
seedance_2_5.md 只负责 Seedance 2.5 Video Prompt 的目标模型适配，不得覆盖主规则或导演锁定内容。
请确认：Loaded: Framewright v3.5.0 + Seedance 2.5 Runtime Profile v1.1.0
然后等待我提供场景。
```

只有同时满足“当前阶段是 Video Prompt”并且“目标模型是 Seedance 2.5”时，才需要读取这个适配文件。Storyboard、Keyframes 或其他目标模型不需要它。

## 3. 选择一个制作阶段

Framewright 一次只处理一个阶段：

| 阶段 | 用途 | 默认结果 |
|---|---|---|
| Storyboard | 检查镜头、空间、动作和连续性 | 分镜 Prompt，以及一张初始分镜板 |
| Keyframes | 设计最终构图、光线、色彩和关键瞬间 | 关键帧 Prompt |
| Video Prompt | 编写目标视频模型使用的 Prompt | 视频 Prompt |

如果你不知道从哪里开始，可以说：

```text
请先阅读这个场景，建议我应该从 Storyboard、Keyframes 还是 Video Prompt 开始。先不要生成。
```

## 4. 推荐启动模板

```text
请使用 Framewright 3.5.0 处理下面的场景。

我想先制作：Storyboard / Keyframes / Video Prompt

场景：
【粘贴故事、场景或剧本】

必须保留：
【不能改变的剧情、镜头、动作、对白或视觉方向】

可以由 Framewright 判断：
【你愿意授权它补充或推荐的部分】

参考素材：
【说明每份素材负责什么、不负责什么】
```

不需要提前想清全部细节。Framewright 会询问真正可能改变结果的问题。

## 5. 怎样说明参考素材

不要只说“参考这些图片”。最好明确每份素材的作用：

```text
人物图只负责脸、发型和服装，不要照搬姿势与构图。
场景图只负责建筑结构，不要继承天气和色调。
动作视频只参考动作节奏，不要改变角色身份。
```

素材上传顺序不代表权威大小。如果 Framewright 理解错误，请立即纠正。

## 6. 怎样回答 Framewright 的问题

你可以直接选择选项并补充原因：

```text
选 B。人物此时还不知道门后有什么。
```

也可以保留创作自由：

```text
背景人物的具体动作保持开放，只要不抢主角注意力。
```

或者只授权一个范围：

```text
焦段和景深由你判断，但不要改变镜头数量、顺序和人物走位。
```

如果某项内容不能被改动，请明确说它是“导演锁定内容”。

## 7. 需要知道的边界

- Framewright 不会自动连续制作三个阶段。
- Storyboard 默认是黑白结构分镜，不是最终电影画面。
- Storyboard 只生成一张初始分镜板，不会自动 retry 或制作变体。
- Keyframes 默认只交付 Prompt，不会自动生成图片。
- Video Prompt 默认只交付 Prompt，不会自动生成视频。
- 生成视频、retry、变体和可能产生额度费用的操作，都需要另外批准。
- Framewright 不会自动调用 ChatCut、OpenMontage、编辑时间线或导出影片。

Seedance 2.5 专属的 `@` 素材映射、任务路由和 Run Card 来自独立的 `seedance_2_5.md`。主 Framewright 文件始终拥有更高权威。

## 8. 内测时重点观察什么

请特别记录：

- 哪个问题问得有价值；
- 哪个问题没有必要；
- 哪个重要细节没有被问到；
- 是否改变了你已经锁定的内容；
- 是否把本应开放的细节规定得过多；
- 参考素材的用途是否理解正确；
- Prompt 正确但生成模型仍然失败的情况。

推荐反馈格式：

```markdown
# Framewright 3.5 内测反馈

- 项目 / 场景：
- 使用阶段：Storyboard / Keyframes / Video Prompt
- 目标模型：
- 原始输入：
- 参考素材及其用途：

## 做得好的地方
- （填写）

## 问题
- 多余的问题：
- 遗漏的问题：
- 被改变或遗漏的导演决定：
- 被过度规定的内容：
- 参考素材问题：

## 生成结果（如有）
- 成功部分：
- 失败部分：
- 尝试次数和额度成本：
- 我认为是 Framewright 问题还是模型随机问题：

## 希望怎样改进
- （填写）
```

最好同时保留原始输入、Framewright 输出的 Prompt、生成结果和你的判断。

## 9. 当前文件位置

Framewright 3.5.0 正式版本文件：

```text
/Users/jameslee/Documents/AI Filmmaking Studio/framewright/versions/releases/framewright-v3.5.0.md
```

Seedance 2.5 适配文件：

```text
/Users/jameslee/Documents/AI Filmmaking Studio/framewright/skill/framewright/references/runtime_profiles/seedance_2_5.md
```

本手册：

```text
/Users/jameslee/Documents/AI Filmmaking Studio/framewright/docs/Framewright_v3.5_Internal_Beta_User_Guide.md
```

未经作者允许，请不要转发、公开发布、重新包装或将 Framewright 规则用于其他产品、Skill 或训练材料。

Copyright © 2026 Tairan Li. All rights reserved.
