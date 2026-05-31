---
type: course-week
week: 16
title: 单细胞转录组可视化
hours: 2
status: pilot_ready
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

## 试点课交付清单

- 课堂核心问题：学生能否把单细胞图形解读成“观察、可能解释、不确定性、待核验点”，而不是直接把 cluster 当细胞类型。
- 课堂数据：使用一套文字化示例图表，包含 QC 指标、UMAP/cluster 描述和 marker 表达模式；公开展示图后续再替换。
- 讲授材料：12 页 PPT 大纲、2 学时授课脚本、单细胞图形解读表、AI 审计提示词。
- 上机产物：一张图形解读表、一段参数敏感性说明、一条带人工核验约束的 AI 提示词。
- 验收标准：学生能说出 QC 阈值、降维参数、聚类分辨率和 marker 选择都会影响解释。

## 课堂示例解读表

| 图形/指标 | 图上看到什么 | 可能解释 | 不确定性 | 待核验点 |
|---|---|---|---|---|
| QC: nFeature_RNA | 一群细胞基因数很低 | 可能是低质量细胞或空液滴 | 阈值依赖样本和平台 | 回查过滤阈值与原始分布 |
| QC: percent.mt | 部分细胞线粒体比例偏高 | 可能存在受损或应激细胞 | 不同组织阈值不同 | 核对组织背景和实验记录 |
| UMAP cluster | 图上出现 4 个 cluster | 算法找到 4 个表达相近群 | 分辨率改变会改 cluster 数 | 记录 PCA 维度和 resolution |
| Marker A | cluster 2 高表达 | 支持某类候选细胞注释 | 单个 marker 证据不足 | 回查 marker 组合、数据库、文献 |

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
