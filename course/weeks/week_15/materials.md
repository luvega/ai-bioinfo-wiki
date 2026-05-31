---
type: course-week
week: 15
title: 差异表达分析与功能解读
hours: 2
status: first_round
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 15 周：差异表达分析与功能解读 · 素材映射

## 课程源文件

- [正式 docx](../../syllabus/36课时-AI前置调整版.docx)
- [主讲稿 Markdown](../../syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)

## 本周定位

本周从 count matrix 进入统计结果和生物学解释。主线是“差异表达不是找 P 值最小的基因，而是在高维检验中同时看效应量、校正显著性、表达模式和功能证据”。AI 可以帮助整理结果表和图注，但不能编造基因功能。

## AIDD 候选素材

- `materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md`
- `09_R_for_Bioinformatics/04_Differential_Gene_Expression_Analysis_with_Deseq2_Preparing_Data.txt`：DESeq2 分析准备、count data 和 metadata。
- `09_R_for_Bioinformatics/05_Deseq2_Code_Understanding.txt`：DESeq2 代码理解、size factor、dispersion、负二项模型。
- `09_R_for_Bioinformatics/06_Converting_Ensembl_Gene_IDs_to_Gene_Symbols_Using_R_Techniques_and_Packages.txt`：基因 ID 转换。
- `09_R_for_Bioinformatics/07_Visualizing_Gene_Expression_Data_Creating_Stunning_Plots_with_ggplot2.txt`：表达数据可视化、ggplot2。
- `10_Microarray_Analysis_on_R/05_Microarray_Analysis_Using_GEO2R.txt`：可作为 GUI 差异分析对照，不作为 DESeq2 主线。

## PDF 候选素材

- `materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R/book.course.md`：用于支撑“高维特征、模型、分类/回归”的统计背景。
- `materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python/book.course.md`：用于补充“模型评估、显著性与预测不是同一件事”的解释。

## 可进 PPT 的元素

- 概念图：`count matrix + metadata -> DESeq2 -> result table -> volcano plot / heatmap -> enrichment / literature check`。
- 示例结果表：gene、log2FoldChange、pvalue、padj、baseMean。
- 图表：火山图坐标解释；热图展示表达模式。
- AI 提示词：整理筛选规则、写图注、列出待核验功能，不允许编造基因功能。

## 课堂小数据字段

| 字段 | 含义 | 课堂解释 |
|---|---|---|
| gene | 基因 ID 或 symbol | 需要核对 ID 类型 |
| baseMean | 平均表达水平 | 低表达基因解释要谨慎 |
| log2FoldChange | 组间表达倍数变化 | 效应量，不等同于显著性 |
| pvalue | 原始 P 值 | 多重检验前结果 |
| padj | 校正后 P 值 | 高维检验中更应关注 |

## 进入 PPT 前需核验

- DESeq2 代码和函数名必须回查原始 txt 或官方文档，PPT 主体只讲概念流程。
- 功能富集解释必须加“需数据库或文献核验”提示。
- 若展示基因功能，不使用 AI 直接生成的事实陈述作为权威来源。
## 样板周质量区块

### 素材来源
- 课程主线：`course/syllabus/36课时-AI前置调整版.docx`。
- 差异表达素材：AIDD DESeq2、ggplot2、基因 ID 转换和 GEO2R 相关章节。

### 可用程度
- 可直接进 PPT：DESeq2 输入输出流程、结果表字段、火山图和热图解释框架。
- 需改写后进 PPT：基因功能解释，只能作为待核验候选，不作为权威事实。

### 待核验
- DESeq2 术语需核对官方文档或原始字幕。
- 所有基因功能和通路解释必须标注数据库或文献核验来源。
