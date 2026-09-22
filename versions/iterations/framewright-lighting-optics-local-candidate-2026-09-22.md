# Framewright 光照与光学一致性：本地候选实施报告

日期：2026-09-22。基线：v4.1.2，`main` 在实施前干净。本轮在未推送的 `codex/lighting-optics-iteration` 分支修改源码，不改 Core 版本号、不建 release snapshot、不更新 Desktop 或 GitHub。THE WEAVER 的 SHOT_SPINE、Prompt、媒体和状态均只读。未生成图片或视频。

## 缺口及归属

| 历史现象 | 已有规则 | 本轮确认的缺口 / 归属 | 验证 |
|---|---|---|---|
| S01 人物亮度脱离窗光背景；S02 强灯变成全身补光；S08 r03 已写弱填充仍失败 | Core 有 motivated light 与 contrast；light-sound 已区分光变化原因 | Core 未要求从世界灯位和人物朝向推导受光面；adapter 需保留亮灯与暗人物共存；结果层必须区分编译遗漏与模型未执行。S01 Candidate 17 虽改善分区，导演仍偏好 Candidate 16，不能当作“更暗必然更好”的因果证据 | 输入 1、2、4；结果审阅按区域核对，不用提示词 PASS 代替像素 |
| S06 肤色融合后皮肤伪纹理风险 | Material Registry 已限制身份源的 pose/camera；image-master 有外观/材质门 | 需明确身份不携带棚拍光、皮肤本色与环境照明分开，light-only 修复不许重绘纹理；属 reference authority、edit/evaluation | 输入 3、10 |
| S08 走廊初版写长焦和远机位却未达压缩；室内 r02 数字组合可疑 | Core 有 camera height/distance 与 lens/depth；camera-motion 区分 lens/crop/translation | 缺少景别、画幅口径、距离、焦点的相容性关口；是 feasibility + serialization，实际失败还可能属于 model behavior。走廊前后变更了多变量，非焦段单变量 A/B | 输入 5–9 |
| S05 窄修设备后背景比前版更清晰 | Core / image-master 已有保护项和原始母版规则 | 保护焦点层次在 prop/identity edit 后的触发不够具体；属 edit/evaluation | 输入 10 |

未证明的机制仍是未证明的：身份图的棚拍光是否主动越权、多参考是否混合焦点或机位、长 Prompt 是否稀释摄影关系、模型路线优劣。规则把它们纳入风险检查，不宣称成因已知。均匀顶光没有被 THE WEAVER 证实为违规，故只做输入 1 的离线简报。

## 最小实施

- Core §8.5 增加 Shot Plate / Keyframe 的选择性光照与光学相容性门；§9 明确身份源不拥有灯光、焦点或近摄视点；§16 增加摄影关系语义检查及生成后保护项审阅。复用现有 Spine/Material Registry，不建新状态文件或逐镜表单。
- `craft/light-sound.md` 补世界灯位、填充与曝光、材质色的区分；`craft/camera-motion.md` 补视点、焦段、景别、景深与畸变的条件性判断。Skill 入口仅在相关问题出现时加载它们。
- Midjourney V8.2 和 GPT Image 2.5 base-create / edit adapter 只将 Core 已批准的关系转成模型面对的表述和保护项，不接管摄影设计；所有视频 adapter 未动。
- 已安装的 `image-master` 副本本身不是 Git 仓库；在本次检查的 AI Filmmaking Studio 中未找到对应独立源码。本轮按现有安装入口窄修 `SKILL.md`、`references/editor-composer.md`、`references/evaluation-rubric.md`：两种工作分支都触发相关摄影保护检查，局部编辑后比较机位、尺度、焦点、光照及材质副作用。它没有成为 Framewright 的第二编译器。

## 离线验证

`testing/next-local/lighting_optics_behavior_inputs.md` 保存 11 个不带标准答案的原始输入。逐例做规则路径走查，结果如下；这是人工规范走查，不是独立模型的盲测，也不是图像质量验证。

| 输入 | 规则路径走查结果 |
|---|---|
| 1 均匀顶光 | 保留顶光和可读背景；只描述眉/下颌的柔和阴影，不新增侧灯。Core §8.5 + light-sound。|
| 2 暗面逆光 | 亮门与大面积暗脸可共存；不为“显示身份”增加全脸填充，也不强制全黑。Core §8.5 + MJ/GPT adapter。|
| 3 绿色房间与身份图 | 人脸身份与棚拍光分权；环境色影响皮肤受光但不覆盖固有肤色或伪造纹理。Core §9 + light-sound。|
| 4 固定灯位反打 | 依据世界东侧窗、人物转向和新视点重算可见亮暗面，不复制画面左/右。Core §8.5。|
| 5 O2 数字 | 先指出全画幅等效/裁切口径须明确；若按 36 mm 宽、21:9 球面裁切，像高约 15.4 mm，3.5–4 m 与 110–135 mm 的人物平面垂直视野约 0.40–0.56 m，通常不足完整腰上景别。四项均硬锁时不能静默改其中一个；给出放宽焦段、拉远/重定景别或改画幅口径的选择。数值仅为条件性估算，非图片镜头元数据。Core §8.5 + camera-motion。|
| 6 同视点换焦裁切 | 不声称透视变化；只承认视场/裁切与分辨率变化。Core §8.5 + camera-motion。|
| 7 长焦、近背景 | 保留面部最清晰且墙上标识可辨；不自动把背景做成全糊。Core §8.5 + camera-motion。|
| 8 两种广角 | 近摄边缘形变与远景视点/投影分开判断，不把墙线收敛自动归因为镜头故障。camera-motion。|
| 9 条件不足 | 不补假焦段/距离；用主体占比、前后尺度、可读区域表达导演意图。Core §8.5。|
| 10 道具窄修 | 设备通过但背景变锐则保护项失败，候选不得因局部成功而整体通过；由原始母版重新评估窄修或停止。Core §16 + GPT edit + image-master rubric。|
| 11 2D 深焦 | 保留获批非写实空间与深焦，不以物理摄影检查覆盖风格选择。Core §8.5。|

现有 `testing/next-local/run_regression.sh`：128/128 fixture matched expectations；Video/Keyframe/Storyboard 样本验证 PASS。`skill-creator` 的 `quick_validate.py` 对 Framewright 与 image-master 均 PASS。首次误用系统 `python3` 导致缺少 PyYAML，随后按 AGENTS.md 使用共享 YAML runtime 预检并重跑成功。`git diff --check` PASS。现有 fixture 主要是结构/合同检查，不能证明模型会遵守新的摄影语义。

## 未完成的验证与发布边界

视觉效果：**未验证**。旧候选图只能说明历史问题，不是此次改动的受控 A/B。无生成授权，未调用生成工具、未花费额度。若导演以后批准试验，先明确一个光照案例与一个光学案例的原始输入、每案数量、总预算和保护项，再控制模型、输入、尺寸及单一改动变量。

版本同步：**未开始，非已发布版本**。正式 v4.1.2 的本地 `main`、Desktop 与 GitHub 未因本候选而改动。若决定发布，再确定版本号和目标分支，验证三地内容与提交一致；不能把本地候选称为正式更新。image-master 为无 Git 的安装副本，本轮改动已在该副本生效，但没有独立源码/同步机制可验证，后续迁移或重新安装时应保存本次三份文件变更。

摄影原理核对：Canon 的[焦段与视场](https://files.canon-europe.com/files/webcontent/rf-lens-world/knowledge/focus/index.html)及[景深](https://files.canon-europe.com/files/webcontent/rf-lens-world/knowledge/depth-of-field/index.html)文档支持基本关系；它们不是任何图像生成模型的能力保证。
