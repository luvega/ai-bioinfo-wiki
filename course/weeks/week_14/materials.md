---
type: course-week
week: 14
title: 转录组数据分析基础
hours: 2
status: pilot_ready
source: ../../syllabus/36课时-AI前置调整版.docx
---
# 第 14 周：转录组数据分析基础 · 素材映射

## 课程源文件

- [正式 docx](../../syllabus/36课时-AI前置调整版.docx)
- [主讲稿 Markdown](../../syllabus/课程教学讲稿-医药数据处理与可视化-36课时-AI前置调整版.md)

## 本周定位

本周解决一个关键问题：表达矩阵从哪里来。学生不需要完整掌握命令行上游流程，但必须理解从 FASTQ 到 count matrix 的链条，否则后续 DESeq2、火山图、热图和单细胞可视化都缺少质量判断基础。

## AIDD 候选素材

- `materials/markdown/aidd_bioinformatics/07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/chapter.course.md`
- `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/02_Introduction_to_RNA-Seq.txt`：导入 RNA-seq、NGS 和命令行流程意识。
- `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/04_Getting_the_SRA_Reads.txt`：用于说明公共数据库数据下载。
- `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/06_Checking_the_Quality_of_Data.txt`：用于说明 FASTQ 质量控制。
- `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/08_Quality_Trimming_of_data.txt`：用于说明低质量 reads 修剪。
- `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/09_Aligners_and_Aligning_Reads_to_genome.txt`：用于说明参考基因组比对。
- `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/10_SAM_and_Bam_File_Indexing_and_Sorting.txt`：用于说明 SAM/BAM 的中间文件角色。
- `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/12_Feature_Extraction.txt`：用于说明基因计数矩阵的来源。

## PDF 候选素材

- `materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_Python/book.course.md`：只取“特征、样本、监督学习问题”的概念背景，帮助解释表达矩阵为何是样本特征表。
- `materials/markdown/pdf_library_mineru/An_Introduction_to_Statistical_Learning_with_Applications_R/book.course.md`：作为统计学习概念补充，不直接进入 RNA-seq 上游命令。

## Single-cell Best Practices 候选素材

- [SCBP 课程索引](../../../materials/markdown/sc_best_practices/scbp.course_index.md)：全书章节、代码工程、数据 manifest 和 Week 13-16 映射。
- [Single-cell RNA sequencing](../../../materials/markdown/sc_best_practices/analysis_project/chapters/02_introduction_scrna_seq/chapter.source.md)：用于解释 scRNA-seq 和 bulk RNA-seq 的实验与数据差异。
- [Raw data processing](../../../materials/markdown/sc_best_practices/analysis_project/chapters/03_introduction_raw_data_processing/chapter.source.md)：用于补充 FASTQ、barcode、UMI、reference 和 count matrix 的来源。
- [Fundamental data structures and frameworks](../../../materials/markdown/sc_best_practices/analysis_project/chapters/04_introduction_fundamental_data_structures_and_frameworks/chapter.source.md)：用于引入 AnnData、obs/var/X/layers 等数据结构。
- [Dataset download report](../../../materials/markdown/sc_best_practices/analysis_project/dataset_download_report.md)：用于核查哪些示例数据已下载、哪些需要 LaminDB 或人工处理。

## OWF Shell 辅助参考

- [OWF Learn Linux Shell](../../../materials/markdown/openwaterfoundation_learning/linux_shell/README.md)：只用于解释命令行、脚本、重定向和日志等通用操作素养。
- [OWF Learn Windows Shell](../../../materials/markdown/openwaterfoundation_learning/windows_shell/README.md)：只用于 Windows 课堂环境中的路径、命令提示符和批处理背景。
- 使用边界：Week 14 的 RNA-seq 上游流程仍以 AIDD 生信素材、课程讲稿和后续人工核验为主；OWF shell 教程不替代 FASTQ、SAM/BAM、feature extraction 等生信事实来源。

## 素材分层使用原则（2026-06-04）

- 课堂主素材：AIDD RNA-seq 上游链条和课堂 count matrix / metadata 核验。
- 支撑素材：SCBP raw data processing / data structures、OSCA SCE/QC/normalization、OSTA reads-to-counts/QC/normalization。
- 拓展素材：空间转录组作为表达矩阵来源扩展框，不覆盖 RNA-seq 主线。
- 教师备课素材：OSCA/OSTA workflow 只用于确认文件角色和质量控制表述。
- 教材 / PPT 边界：可进 PPT：FASTQ -> count matrix 流程、AnnData/SCE 概念框、metadata 对齐检查。

## 可进 PPT 的元素

- 流程图：`SRA/FASTQ -> QC -> trimming -> alignment -> SAM/BAM -> sorting/indexing -> feature extraction -> count matrix`。
- 表格：FASTQ、SAM、BAM、count matrix、metadata 的文件角色。
- 示例矩阵：3 个基因 x 4 个样本的小型 count matrix。
- 讨论题：为什么不能直接比较不同样本的原始 counts。

## 课堂小数据

| gene | Ctrl_1 | Ctrl_2 | Drug_1 | Drug_2 |
|---|---:|---:|---:|---:|
| GeneA | 120 | 98 | 240 | 260 |
| GeneB | 30 | 42 | 28 | 35 |
| GeneC | 500 | 520 | 410 | 390 |

## 课堂 metadata 示例

| sample_id | group | batch |
|---|---|---|
| Ctrl_1 | control | B1 |
| Ctrl_2 | control | B2 |
| Drug_1 | drug | B1 |
| Drug_2 | drug | B2 |

## 试点课交付清单

- 课堂核心问题：学生能否说明 count matrix 从何而来，并在进入 DESeq2 前检查样本名、分组和总 counts。
- 课堂数据：使用上方 3 基因 x 4 样本 count matrix 和 metadata，不要求运行上游命令。
- 讲授材料：12 页 PPT 大纲、2 学时授课脚本、文件角色对照表、样本对齐检查表。
- 课堂产物：样本名对齐检查、每个样本总 counts、标准化必要性解释、AI 流程表审计记录。
- 验收标准：学生能说出 FASTQ、SAM/BAM、count matrix、metadata 的角色，并解释为什么原始 counts 不能直接跨样本比较。

## 课堂预期输出

| sample_id | group | total_counts | 核验说明 |
|---|---|---:|---|
| Ctrl_1 | control | 650 | `120 + 30 + 500` |
| Ctrl_2 | control | 660 | `98 + 42 + 520` |
| Drug_1 | drug | 678 | `240 + 28 + 410` |
| Drug_2 | drug | 685 | `260 + 35 + 390` |

预期解释：四个样本总 counts 不同，说明测序深度或文库规模可能不同。进入差异表达分析前，不能直接用原始 counts 下结论，需要标准化和统计模型处理。

## 进入 PPT 前需核验

- AIDD 上游流程素材来自字幕清理，命令名和软件名进入 PPT 前需回查 txt。
- 本课程只讲流程边界，不在本周要求学生完整安装 SRA Toolkit、FastQC、aligner。
- count matrix 示例必须和 metadata 样本名严格对齐。
## 样板周质量区块

### 素材来源
- 课程主线：`course/syllabus/36课时-AI前置调整版.docx`。
- 上游流程素材：AIDD RNA-seq 命令行章节、FASTQ/QC/alignment/feature extraction 字幕。

### 可用程度
- 可直接进 PPT：FASTQ 到 count matrix 的流程图、文件角色对照表、3 基因 x 4 样本 count matrix。
- 需改写后进 PPT：具体命令行流程，只保留输入、输出和质量问题，不要求学生完整安装上游工具。

### 待核验
- 软件名、命令名和文件格式解释进入 PPT 前必须回查原始 txt。
- count matrix 示例必须和 metadata 样本名严格对齐。
