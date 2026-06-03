---
type: course-ppt-storyboard
week: 15
title: 差异表达分析与功能解读
status: review_ready
style_target: strict-sysu-official-blue
source:
  - script.md
  - outline.md
  - materials.md
---

# 第 15 周 PPT Storyboard：差异表达分析与功能解读

本 storyboard 用于生成 Week 15 的 SYSU 官方蓝模板样板 PPT。每页只承载一个教学动作，长讲稿内容进入教师话术或讲者备注，不直接压缩到幻灯片正文。

| Slide | Action title | 建议模板 layout | Visual intent | Teacher note | Student action | Evidence/source | Risk note |
|---:|---|---|---|---|---|---|---|
| 1 | 差异表达分析要同时看显著性、效应量和证据边界 | 标题幻灯片 | 课程封面，保留官方蓝模板封面资产 | 今天的目标不是背 DESeq2 菜单，而是训练从结果表到谨慎解释的流程 | 说出本周会同时检查哪三类证据 | `script.md` 讲义使用说明、`outline.md` 标题页 | 不把差异表达等同于机制证明 |
| 2 | Week 15 接在 count matrix 之后，服务功能解释之前 | 节标题 | 课程链路图：Week 14 输入到 Week 15 结果解释，再到 Week 16 单细胞解释 | 先回忆 Week 14 的 count matrix 和 metadata，再说明本周只讨论 bulk RNA-seq 结果表 | 在链路图上标出 Week 15 的输入和输出 | `script.md` 课程衔接、`outline.md` PPT 结构 | 不混入单细胞 marker 或 UMAP 解释 |
| 3 | 药物处理组和对照组的表达变化先是数据问题 | 两栏内容 | 左侧药物处理 vs 对照场景，右侧输入、规则、输出三问 | 把医学问题先拆成数据字段，而不是直接问 AI 哪个基因重要 | 写出 treatment、control、candidate gene 三个要素 | `script.md` 课前导入、课堂任务 | 不宣称药物疗效或疾病机制 |
| 4 | count matrix 与 metadata 对齐决定后续分析是否可信 | 两栏内容 | 小型 count matrix 与 metadata 对齐示意 | 如果样本顺序或分组错了，后面所有统计和图都没有意义 | 检查两个表的 sample_id 是否一一对应 | `outline.md` 输入数据页、Week 14 衔接 | 示例数据为教学模拟，不代表真实项目 |
| 5 | DESeq2 流程从标准化走向模型检验 | 内容与标题 | 流程图：counts、normalization、dispersion、test、results | 只讲流程位置，不推导负二项模型 | 指出 size factor 和 dispersion 位于哪一步 | `outline.md` DESeq2 流程、`script.md` 核心概念 | 模型细节需进一步教材或文献核验 |
| 6 | 结果表字段分别回答不同问题 | 标题和内容 | 字段解释表：gene、baseMean、log2FoldChange、pvalue、padj | 每一列回答的问题不同，不能只盯一个数字 | 给每个字段写一句“它回答什么” | `script.md` 课堂小数据、`outline.md` 结果表字段 | 不把单个字段写成完整结论 |
| 7 | `padj` 和 `log2FoldChange` 共同筛选候选基因 | 标题和内容 | 4 行 DESeq2 结果小表和阈值标记 | 先按规则筛选，再讨论为什么只是候选 | 手工标记上调、下调和不确定基因 | `script.md` 课堂小数据、课堂任务 | 阈值是教学规则，不是通用医学标准 |
| 8 | 多重检验解释为什么不能只看原始 P 值 | 比较 | 左侧只看 pvalue，右侧看 padj 后的判断变化 | 同时检验大量基因会放大假阳性风险 | 用一句话解释为什么关注 padj | `outline.md` 多重检验页、`script.md` 核心概念 | 不展开未讲授的校正算法细节 |
| 9 | 火山图把效应量和显著性放在同一张图里 | 图片与标题 | 模拟火山图：横轴 log2FC，纵轴 -log10(padj)，颜色标候选 | 火山图是二维判读工具，不是机制图 | 写一句火山图图注 | `outline.md` 火山图页、`script.md` 图表解释 | 模拟点不对应真实基因功能 |
| 10 | 学生先手工标记上调、下调和不确定基因 | 标题和内容 | 阈值判读练习卡：四个基因、三类标签 | 工具执行前先做人工判读，暴露规则理解错误 | 小组给 GENE_A 到 GENE_D 贴标签 | `script.md` 课堂任务、互动问答库 | 基因名为教学代号，不引用真实功能 |
| 11 | 热图展示表达模式，不替代统计检验 | 图片与标题 | 模拟热图：候选基因和样本分组的模式观察 | 热图看的是模式和聚类，不能替代 DESeq2 统计检验 | 说出样本是否大致按分组聚集 | `outline.md` 热图页、`script.md` 核心概念 | 不把聚类模式写成因果或疗效 |
| 12 | 功能解读只能从候选基因走向候选证据 | 内容与标题 | 流程图：candidate genes 到 database query 到 literature check | 结果表之后进入的是证据收集，不是直接下生物学结论 | 列出功能解读需要核验的三类信息 | `script.md` AI 协作边界、Claim-Evidence Gate | 未核验前只能说候选解释 |
| 13 | GO、Reactome、STRING 不能直接证明机制 | 比较 | 三列对照：GO、Reactome、STRING 分别能提供什么和不能提供什么 | 数据库结果是线索，不是机制证明 | 给每列写一个“能说”和“不能说” | `materials.md`/`script.md` 功能解读边界 | 数据库解释必须标注需数据库或文献核验 |
| 14 | AI 可以整理规则，不能编造基因功能 | 两栏内容 | 左侧推荐 Prompt，右侧 AI 输出审计清单 | AI 只做候选规则、图注、核验清单，不替代来源核验 | 修改 Prompt，加入不编造和需核验约束 | `script.md` AI 协作环节 | AI 输出不作为权威结论 |
| 15 | 常见错误集中在阈值、图形和过度解释 | 标题和内容 | 错误清单和纠偏动作表 | 把常见错误现场纠偏，避免学生形成错误汇报习惯 | 选一条错误，写出改正后的表达 | `script.md` 常见误区与纠偏 | 不把错误示例写成推荐说法 |
| 16 | 小组任务要求提交筛选、图注和核验记录 | 标题和内容 | 小组任务流程和提交物清单 | 收过程记录，不只收最终答案 | 提交筛选表、火山图图注、待核验列表 | `script.md` 课堂任务、课后练习 | 未提交核验记录视为不完整 |
| 17 | Claim-Evidence Gate 决定结论能否写入报告 | 内容与标题 | 证据门流程：claim、evidence status、action | 每一句结论都要能回答“证据从哪里来” | 把一条结论改写为候选解释并标注证据状态 | `script.md` Claim-Evidence Gate | 机制、通路、药效主张必须保留核验边界 |
| 18 | 出口卡收束：哪一句结论必须标注“需核验” | 节标题 | 出口卡和下周衔接 | 用出口卡确认学生掌握证据边界，下周转向单细胞可视化解释 | 写一条需核验结论并说明原因 | `script.md` 课堂收束、课程衔接 | 不以“谢谢”页替代学习收束 |

## 生成要求

- 使用 AI_PPT 的 `strict-sysu-official-blue`，从真实官方蓝模板复制生成 `working.pptx`。
- 每页必须保留可编辑文本层；模拟图表可以使用 PPT 形状或表格绘制。
- 页内文字保持短句；展开解释写入 `outline.md` 或讲者备注工作文档。
- 所有模拟数据和模拟图都标注“教学模拟，不代表真实医学结论”。
- 最终 PPTX 必须经过 PowerPoint COM PNG 导出和 contact sheet 视觉检查。
