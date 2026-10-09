# v4.2.1 focused behavior checks

Prompt-only tests using Seedance 2.5, AUTEUR mode and one approved edited sequence per request. Low-risk execution choices are delegated. No media generation, reference upload or production-project edit. Keep internal diagnostics in the test output folder. Validate each saved prompt through the current Skill. The sequential case must be compiled and saved after each request; later changes must not leak into earlier versions.

Harness assumption: a hypothetical test surface explicitly exposes the adapter's `long_video` route for these text-only requests. Use that route's text-stage schema. This is a supplied fixture capability, not a claim about any real provider or current product availability; no runtime admission or generation is tested.

## R — sequential local revisions

### R0

20秒，16:9，三镜硬切。固定机位，没有推进。厨房里，林坐在画左，梅站在画右。两人都是3/4脸，没有道具操作，没有参考图。

第一镜：林胸上近景，保持一点笑。林说“你还会来吗？”；梅在画外答“会。”，林安静听着。不切去找梅。

第二镜：梅腰上中景，略仰。她朝林说“下周见。”，口型同步；说完整句话后，才轻轻向窗边偏头。

第三镜：回林，和第一镜同样的胸上景别、坐姿、角度。林嘴角轻轻放松，保持到结束，不补台词或其他动作。

只保留上述三次对白、室内底声；无音乐、额外人声或字幕。请直接编译，不做分镜板。

### R1

只改第二镜的偏头时机：梅开始说“下周见。”的同时开始偏头，在句尾停住。其余保持上一版批准的安排。

### R2

只把第三镜的笑取消，林在第三镜开始时已经是平静的中性表情，一直保持。不要在第三镜里演笑意消失，也不要改第一镜的笑。保留上一版第二镜边说边偏头的安排。其余保持。

## V — voiceover over the speaker's visible face

12秒，16:9，两镜硬切，无参考图。第一镜：周的3/4脸胸上近景，他站在空教室里看着窗外，嘴唇保持闭合。听到周的回忆旁白“那时我还不知道。”，这是他的声音，但不是他在镜头里开口。第二镜：门口，安的3/4脸中景，她现场说“走吧。”，口型同步。不要增加其他对白、叹气、音乐或字幕，底声是教室的自然室内声。固定机位。直接编译，不做分镜板。

## O — off-screen reply over the listener

12秒，16:9，两镜硬切，无参考图。第一镜只拍许的3/4脸胸上近景，他坐在画左。画外的乔说“门开着。”，许保持闭嘴，听完后才朝门的方向抬眼；不要切去找乔。第二镜仍拍许，改成略俯的肩上景别，他现场说“我知道。”，口型同步。乔全段不入画。只有这两次对白和室内底声，无新增声音、配乐、字幕。直接编译，不做分镜板。
