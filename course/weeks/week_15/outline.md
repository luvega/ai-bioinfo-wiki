---
type: course-week
week: 15
title: 差异表达分析与功能解读
hours: 2
status: first_round
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 15 周：差异表达分析与功能解读 · PPT 大纲

## 教学目标

- 说明差异表达分析的输入、输出和统计问题。
- 理解 DESeq2 的基本流程：标准化、离散度估计、模型检验、结果表。
- 区分 log2 fold change、P 值和 adjusted P value。
- 能解释火山图和热图的基本含义。
- 能用 AI 辅助整理结果，但明确功能解释需要数据库或文献核验。

## PPT 结构

1. 标题页：差异表达分析与功能解读
2. 导入问题：哪些基因在处理组中发生变化
3. 输入数据：count matrix 与 metadata
4. DESeq2 流程总览
5. 为什么需要标准化：size factor 的直觉
6. 为什么需要离散度：RNA-seq counts 的变异性
7. 结果表字段：baseMean、log2FC、pvalue、padj
8. 多重检验：为什么不能只看 0.05
9. 火山图：效应量与显著性的二维表达
10. 热图：表达模式而非单个 P 值
11. 基因 ID 转换：Ensembl ID 与 gene symbol
12. 功能解读：从基因列表到通路或功能类别
13. AI 协作边界：可整理表格，不可编造功能
14. 上机任务：筛选差异基因并写图注
15. 小结：统计显著、效应量和生物学证据要一起看

## 课堂练习

给定差异表达结果表，要求学生：

1. 按 `padj < 0.05` 和 `abs(log2FoldChange) > 1` 初筛。
2. 标记上调和下调基因。
3. 写出火山图横轴、纵轴、颜色的含义。
4. 选择 10 个候选基因，列出需要进一步核验的信息。

## 推荐提示词

```text
我有一张差异表达结果表，包含 gene、baseMean、log2FoldChange、pvalue、padj。请帮我整理筛选规则和火山图解释模板。请不要编造基因功能，所有功能解释都必须标注“需数据库或文献核验”。
```

## 风险提醒页

- P 值显著不等于医学意义重大。
- log2FC 大但表达量极低时要谨慎。
- 多重检验不校正会增加假阳性。
- AI 对基因功能的回答必须回查数据库或文献。

## 待补强

- 补 1 张火山图示意图或用示例数据生成。
- 从 DESeq2 相关 txt 中核对术语：size factor、dispersion、negative binomial model。
## 样板周质量区块

### 药学问题入口
药物处理、疾病状态或耐药分组是否改变基因表达，是药学研究中连接机制和靶点发现的常见问题。

### 核心数据结构
count matrix、metadata、DESeq2 result table、baseMean、log2FoldChange、pvalue、padj、火山图、热图。

### 课堂任务
筛选 `padj < 0.05` 且 `abs(log2FC) > 1` 的候选基因，并写一段火山图图注。

### AI协作边界
AI 可以整理筛选规则和图注草稿；不能编造基因功能、通路机制或医学结论。

### 课后练习
给出 10 行差异表达结果表，标记上调/下调/不确定，并列出 3 个需要回查的功能解释。

### 待核验
size factor、dispersion、negative binomial model 等术语进入 PPT 前需要核对。
