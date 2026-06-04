---
type: course-week
week: 15
title: 差异表达分析与功能解读
hours: 2
status: pilot_ready
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

## Single-cell Best Practices 候选素材

- [Differential gene expression](../../../materials/markdown/sc_best_practices/analysis_project/chapters/18_conditions_differential_gene_expression/chapter.source.md)：用于对比 bulk DESeq2 主线和 single-cell pseudobulk / cell-level DE 的差异。
- [GSEA pathway](../../../materials/markdown/sc_best_practices/analysis_project/chapters/20_conditions_gsea_pathway/chapter.source.md)：用于功能解读、通路分析和 gene set 证据边界。
- [Compositional analysis](../../../materials/markdown/sc_best_practices/analysis_project/chapters/19_conditions_compositional/chapter.source.md)：用于说明“细胞比例变化”和“基因表达变化”不是同一类问题。
- [Dataset manifest](../../../materials/markdown/sc_best_practices/analysis_project/datasets_manifest.json)：用于回查差异分析和 GSEA 示例数据的下载/blocked/manual 状态。

## OWF Shell 辅助参考

- [OWF Learn Git](../../../materials/markdown/openwaterfoundation_learning/git/README.md)：只用于项目记录、结果表版本管理和协作审阅背景。
- [OWF Learn Linux Shell](../../../materials/markdown/openwaterfoundation_learning/linux_shell/README.md)：只用于解释脚本运行、日志和退出状态等通用 shell 语义。
- 使用边界：Week 15 的统计与生物学解释仍以 DESeq2、AIDD R 素材、课程讲稿和数据库/文献核验为主；OWF 教程不作为差异表达或功能解读的事实来源。

## 素材分层使用原则（2026-06-04）

- 课堂主素材：AIDD DESeq2/GEO2R 和课堂 DESeq2 结果表；主线是 bulk 差异表达与功能核验。
- 支撑素材：SCBP DGE/GSEA/compositional、OSCA marker/multi-sample comparison、OSTA feature testing/signatures/differential spatial patterns。
- 拓展素材：single-cell 和 spatial 的差异分析只作对比，不替代 bulk DESeq2 教学。
- 教师备课素材：准备 bulk、single-cell、spatial 三类差异问题的边界表。
- 教材 / PPT 边界：可进 PPT：result table、火山图、富集解释待核验、三类差异分析对照。

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

## 试点课交付清单

- 课堂核心问题：学生能否同时使用 `padj`、`log2FoldChange` 和 `baseMean` 判断候选基因，而不是只按 P 值排序。
- 课堂数据：使用 10 行简化 DESeq2 结果表，基因名只作为字段示例，不在课堂中声称具体功能。
- 讲授材料：12 页 PPT 大纲、2 学时授课脚本、火山图解释模板、功能核验清单。
- 上机产物：筛选后的上调/下调候选表、火山图图注草稿、至少 3 条待核验信息。
- 验收标准：学生能说明“统计显著、效应量、表达水平、功能证据”四者的关系。

## 课堂示例结果表

| gene | baseMean | log2FoldChange | pvalue | padj | 课堂判读 |
|---|---:|---:|---:|---:|---|
| CYP1A1 | 320 | 1.8 | 0.0008 | 0.012 | 上调候选 |
| ABCB1 | 210 | -1.3 | 0.0040 | 0.031 | 下调候选 |
| IL6 | 18 | 2.4 | 0.0300 | 0.180 | 校正后不显著 |
| GAPDH | 5000 | 0.2 | 0.0010 | 0.020 | 显著但效应量小 |
| GENE_A | 6 | -3.1 | 0.0200 | 0.210 | 低表达且校正后不显著 |
| GENE_B | 95 | 1.1 | 0.0120 | 0.049 | 上调候选 |
| GENE_C | 130 | -0.9 | 0.0020 | 0.040 | 效应量未达阈值 |
| GENE_D | 80 | -1.6 | 0.0005 | 0.008 | 下调候选 |
| GENE_E | 760 | 0.0 | 0.9000 | 0.950 | 无差异 |
| GENE_F | 42 | 1.4 | 0.0400 | 0.070 | 校正后不显著 |

筛选规则：`padj < 0.05` 且 `abs(log2FoldChange) > 1`。课堂预期候选为 `CYP1A1`、`ABCB1`、`GENE_B`、`GENE_D`。其中基因功能必须回查数据库或文献，不能由 AI 直接写成事实。

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
