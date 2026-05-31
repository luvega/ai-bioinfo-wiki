---
type: course-week
week: 14
title: 转录组数据分析基础
hours: 2
status: first_round
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
