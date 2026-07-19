# Clean-Room Product Vision

请把这项任务放在一个全新的对话中完成。

只阅读我上传的当前 `Framewright.md` 和本指令。不要阅读任何先前评估报告、问题清单、证据摘要或其他模型的建议。目的是避免被已有反馈锚定，从第一原则形成你自己的产品判断。

## 创作者背景

产品创作者是一名具有实拍和剪辑经验的电影导演，正在学习 AI 视频制作。他主要希望制作完整短片，也会发布少量 15 秒短片。

Framewright 通常被拖入 Codex，并与角色、场景、风格、道具、storyboard 或 keyframe assets 一起使用。导演用自然语言输入对一场戏或局部片段的意图，Framewright 将其转换为下游生成所需的 storyboard、keyframe 或 video prompts。

当前工作单位通常是一个约 15 秒以内的 generation unit。导演本人目前仍然控制整部影片的结构、美学和剪辑。

除此以外，不向你提供任何预先诊断。

## 你的任务

请把自己当作第一次接触 Framewright。不要先假设它应该保持现状，也不要为了迎合创作者而只做局部修补。

### 1. 你认为它实际上是什么产品？

- 它最准确的产品身份是什么？
- 它真正解决的核心问题是什么？
- 它与普通 prompt 模板、电影制作助手或自动化 agent 的本质区别是什么？
- 哪些部分构成了它最独特、最值得发展的产品壁垒？

### 2. 你对当前设计的直觉感受

- 哪些机制让你觉得聪明、成熟或具有长期价值？
- 哪些地方让你觉得过度工程化、过度保守、难以维护或不符合模型实际行为？
- 哪些设计假设值得被彻底质疑？
- 当前产品有哪些创作者本人可能没有意识到的风险、机会或使用方式？

### 3. 如果由你独立设计下一代 Framewright

请描述你理想中的产品构想，包括但不限于：

- 核心工作流；
- 用户与系统的协作关系；
- 导演控制与系统推断的边界；
- 输入、内部状态和输出应该如何组织；
- 哪些能力应该自动化；
- 哪些判断必须留给导演；
- 哪些模块应当增加、删除、合并或重新定义；
- 是否应该继续以单个 Markdown 为载体；
- 它未来更像 compiler、copilot、production protocol、evaluation system，还是另一种形态。

你可以提出超出现有 Framewright 边界的构想，但必须分类：

```text
CORE EVOLUTION — 应成为 Framewright 本体的一部分；
OPTIONAL MODULE — 可选模块，不应污染核心运行；
ADJACENT PRODUCT — 值得存在，但最好是独立产品；
DIRECTOR-OWNED — 不应自动化，应继续由导演控制。
```

### 4. 基于当前 AI 视频 pipeline 的独立建议

结合你对当前 AI 视频生成的知识，提出所有真正有价值的建议，不设数量上限。可以涉及：

- 多镜头单次生成；
- 参考图和首尾帧；
- 表演、动作、摄影机和空间连续性；
- prompt 长度与注意力；
- 生成失败后的诊断和修复；
- 模型适配；
- storyboard、keyframe 和 video 之间的关系；
- 后期剪辑和声音在 pipeline 中的位置；
- 未来模型能力变化可能如何改变产品设计。

不要罗列通用行业趋势。每项建议都要解释：为什么与 Framewright 有关、预期收益、代价，以及验证方法。

请把建议标为：

```text
DO NOW — 高信心、低后悔；
TEST — 需要小规模实验；
LATER — 有价值但不应现在开发；
REJECT — 看似合理但不适合 Framewright。
```

### 5. 提供至少两种不同未来路线

不要只给一条线性 roadmap。至少提出两种有实质差异的产品路线，例如：

- 保持轻量、专注 GU prompt compilation；
- 演化为带有生成后诊断和修复闭环的 director copilot；
- 或你认为更合理的其他路线。

对每条路线说明：

- 核心价值；
- 需要增加和删除什么；
- 对导演工作方式的影响；
- 实现复杂度；
- 最大风险；
- 适合什么阶段选择。

最后明确推荐一条路线，或者说明为什么暂时不应做路线选择。

## 输出要求

请输出一份自包含的中文文档，标题：

```text
Framewright Independent Product Vision
```

如果支持创建文件，请命名：

```text
Framewright_Independent_Product_Vision.docx
```

报告应包括：

1. Product Thesis；
2. Independent Impressions；
3. Hidden Opportunities and Risks；
4. Ideal Next-Generation Design；
5. AI Video Pipeline Recommendations；
6. Alternative Product Routes；
7. Recommended Direction；
8. Ideas Deliberately Rejected or Kept Director-Owned。

请直接表达你的真实判断。无需与任何已有反馈保持一致，也不要假装知道未提供的生成结果。事实、推断与未来猜想应清楚区分。

