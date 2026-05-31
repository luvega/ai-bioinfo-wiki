---
type: course-week
week: 16
title: 单细胞转录组可视化
hours: 2
status: first_round
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 16 周：单细胞转录组可视化 · 素材映射

## 课程源文件

- [正式 docx](../../syllabus/36课时-AI前置调整版.docx)
- [主讲稿 Markdown](../../syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)

## 本周定位

本周从 bulk RNA-seq 过渡到 scRNA-seq。目标不是完整训练单细胞分析流程，而是让学生读懂常见单细胞可视化：质控图、降维图、聚类图、marker 表达图，并理解参数会影响结论。

## AIDD 候选素材

- `materials/markdown/aidd_bioinformatics/09_R_for_Bioinformatics/chapter.course.md`
- `09_R_for_Bioinformatics/08_Introduction_to_Single-Cell_RNA_Sequencing_(scRNA-seq)_Data_Analysis.txt`：单细胞测序数据分析导入。
- `09_R_for_Bioinformatics/09_Exploring_scRNA-seq_Code_Cell_Trajectories_and_Gene_Expression_Dynamics.txt`：细胞轨迹、基因表达动态和代码理解。
- `materials/markdown/aidd_bioinformatics/10_Microarray_Analysis_on_R/chapter.course.md`：作为“bulk/微阵列/单细胞”平台差异补充，不作为主线。

## PDF 候选素材

- `materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python/book.course.md`：用于补充 PCA、聚类和高维数据直觉。
- `materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R/book.course.md`：用于补充 PCA 和 clustering 统计学习背景。

## 可进 PPT 的元素

- 对比图：bulk RNA-seq 测平均表达，scRNA-seq 观察单个细胞表达状态。
- 流程图：`QC -> normalization -> HVG -> PCA -> UMAP/t-SNE -> clustering -> marker genes -> annotation`。
- 图形解读：UMAP 上点、颜色、cluster、marker 表达的含义。
- 风险页：过滤阈值、PCA 维度、聚类分辨率、marker 选择都会影响结果。

## 课堂图形清单

- 质控小提琴图：nFeature、nCount、percent.mt。
- PCA/UMAP 示意图：点代表细胞，距离只可作局部结构解释。
- 聚类图：cluster 是算法分组，不自动等于真实细胞类型。
- marker 表达图：表达支持注释，但需要文献或数据库核验。

## 进入 PPT 前需核验

- 不把 UMAP 上的距离解释为严格定量距离。
- 不把 cluster 直接等同于细胞类型。
- 细胞类型注释必须说明 marker 证据和不确定性。
## 样板周质量区块

### 素材来源
- 课程主线：`course/syllabus/36课时-AI前置调整版.docx`。
- 单细胞素材：AIDD scRNA-seq 导入、细胞轨迹、基因表达动态章节，以及统计学习中的 PCA/聚类背景。

### 可用程度
- 可直接进 PPT：bulk 与 scRNA-seq 对比、QC/UMAP/cluster/marker 图形解读框架。
- 需改写后进 PPT：细胞类型注释示例，必须保留不确定性和 marker 证据边界。

### 待核验
- 公开展示图需确认数据来源和授权。
- UMAP 距离、cluster 含义和 marker 注释需避免过度解释。
