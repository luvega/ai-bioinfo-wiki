# AI_Course 素材到周次对照表（2026-06-04）

> 本表用于执行“课程主线先行、素材分层进入”的升级计划。`course/syllabus/` 与 `course/weeks/` 仍是事实主线；本表只规定素材如何服务课堂、在线教材和后续 PPT storyboard。

## 使用原则

- 课堂主素材：课程大纲、周次 `materials.md`、`outline.md`、`script.md`。
- 支撑素材：AIDD、ISLP/ISLR、AI 编程、GenAI 数据分析等已课程化 Markdown。
- 拓展素材：SCBP、OSCA、OSTA，用于 Week 13-16 的现代组学图形、数据结构和教师备课。
- 教师备课素材：完整 notebook、Bioconductor workflow、空间组学 workflow 和命令行细节；进入课堂前必须简化。
- 禁止直接引用 `materials/raw/` 作为在线教材或课堂来源。

## 周次对照

| 周次 | 课堂主线 | 主要支撑素材 | 现代组学拓展 | PPT / 教材边界 |
|---:|---|---|---|---|
| 01 | 课程导论、医药数据特征、AI 边界 | AIDD Ch1、医药数据特征、AI 协作边界 | 只作表达矩阵与单细胞 metadata 预告 | 课程地图、工具分工、AI 红线 |
| 02 | 数据分析流程、复现规范、AI 记录 | AIDD pipeline、AIDD GitHub、OWF Git/Shell | 不展开组学流程 | 项目目录、Prompt 记录、Git 小步提交 |
| 03 | Python 入门与 AI 辅助调试 | AIDD Python/Biopython、AI 编程参考、嵩天 Python PPT | Biopython 只作文件/序列类比 | 血糖列表、手算核验、代码解释边界 |
| 04 | R 数据框、因子、代码核验 | AIDD R、ISLR/ISLP R 背景 | DESeq2 只作后续预告 | R 数据框、分组变量、列名核验 |
| 05 | 表格读入、列名、长宽表 | GenAI 数据分析、AIDD 文件格式 | FASTQ/SAM/BAM 只作“文件有结构”类比 | 原始表到分析表、字段字典 |
| 06 | 缺失、异常、分组汇总 | GenAI 数据分析、AIDD QC/trimming 类比 | 低质量样本/低表达过滤只作类比 | 清洗日志、IQR、分组汇总 |
| 07 | 描述统计与分布可视化 | AIDD ggplot2、GenAI 数据分析 | 表达图只作读图素材 | 分布图、箱线图、图形解释 |
| 08 | 统计推断基础 | ISLP/ISLR、AIDD DESeq2 多重检验动机 | 不讲 DESeq2 细节 | P 值误区、检验前提 |
| 09 | 相关与线性回归 | ISLP/ISLR、AIDD R 统计背景 | 基因表达关系只作散点图类比 | 相关不等于因果、残差检查 |
| 10 | 分类与逻辑回归 | ISLP/ISLR、AIDD variant 分类类比 | 不进入 variant calling 流程 | 混淆矩阵、阈值风险 |
| 11 | 科研图表与 SCI 表达 | AIDD ggplot2/microarray、ISLR/ISLP 图形 | SCBP/OSCA/OSTA 图可作读图素材，需核授权 | 图注、配色、导出、AI 润色边界 |
| 12 | 高维矩阵、标准化、距离 | AIDD count matrix、ISLP/ISLR | AnnData/SCE 只作数据容器预告 | 矩阵直觉、标准化前后距离 |
| 13 | PCA、聚类、热图 | AIDD scRNA/microarray、ISLP/ISLR | SCBP dimensionality reduction/clustering；OSCA clustering 备课 | 参数记录、探索图形解释边界 |
| 14 | 表达矩阵从哪里来 | AIDD RNA-seq 上游流程 | SCBP raw processing/data structures；OSCA QC/normalization；OSTA reads-to-counts/QC | FASTQ 到 count matrix、metadata 对齐 |
| 15 | DESeq2、火山图、功能解释 | AIDD DESeq2/GEO2R/ggplot2 | SCBP DGE/GSEA/compositional；OSCA marker/multi-sample；OSTA spatial differential features | bulk、single-cell、spatial 差异边界 |
| 16 | 单细胞与空间组学图形解读 | AIDD scRNA 入门 | SCBP QC/annotation/integration/spatial；OSCA QC/clustering/annotation；OSTA spatial domains/deconvolution | QC/UMAP/marker/spatial 图形四栏解读 |
| 17 | 项目工作坊、AI 审计 | AIDD GitHub/pipeline、OWF Git/Shell、GenAI 数据分析 | SCBP/OSCA project structure 只作高级项目示例 | README、AI 使用声明、结果核验 |
| 18 | 项目汇报、答辩、课程总结 | AIDD GitHub、课程 rubric、AI 协作模板 | 只作拓展方向，不作为必答 | 汇报结构、答辩问题、AI 反思 |

## Week 13-16 深度边界

- Week 13：学生能解释 PCA、UMAP、聚类和热图依赖参数；不要求运行 SCBP/OSCA workflow。
- Week 14：学生能说明 FASTQ、count matrix、metadata 的关系；不要求安装上游 RNA-seq 工具。
- Week 15：学生能读 DESeq2 结果表、火山图和功能解读边界；不把 single-cell 或 spatial 的差异分析混同于 bulk DESeq2。
- Week 16：学生能用“观察、可能解释、不确定性、待核验点”读 QC/UMAP/marker/spatial 图；不把 cluster 或 marker 直接写成最终细胞类型结论。

## 下一轮优先级

| 优先级 | 周次 | 交付物 | 验收点 |
| --- | --- | --- | --- |
| P0 | Week 13 | outline/script + Coursebook 样章候选 | 清楚区分表格矩阵、bulk expression matrix、single-cell matrix 与 spatial matrix |
| P0 | Week 17-18 | 项目工作坊与汇报 rubric | 有 Git/GitHub、素材溯源、AI 使用声明和图表证据边界 |
| P1 | Week 11-12 | 图表证据边界与表达矩阵桥接 | 能承接 Week 13，不默认生信或统计背景 |
| P1 | Week 14/16 | PPT storyboard | 只标记 storyboard/review，不标记 PPTX 完成 |
