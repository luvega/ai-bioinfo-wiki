---
type: course-source-chapter
title: AIDD Chapter 7: NGS data Analysis on Bash (Gene Expression Using Command Line)
chapter_no: 7
generated: 2026-05-24 12:34:06
status: generated_draft
tags: [aidd, bioinformatics, course-material, auto-extract]
---

# AIDD Chapter 7: NGS data Analysis on Bash (Gene Expression Using Command Line)

## 课程定位

本章来自 AIDD Bioinformatics 字幕清理讲义，适合映射到 第 1 周, 第 3 周, 第 5 周, 第 11 周, 第 14 周, 第 15 周。它是 PDF 教材之外的生信场景素材层。

## 讲义清单

| 课次 | 标题 | 时长 | 推荐周次 | 关键词/实体 | 源文件 |
|---:|---|---:|---|---|---|
| 2 | Introduction to RNA-Seq | 4.9 | 第 1 周, 第 14 周, 第 15 周 | Galaxy, Linux/WSL, RNA-seq | `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/02_Introduction_to_RNA-Seq.txt` |
| 4 | Getting the SRA Reads | 8.3 | 第 5 周, 第 14 周, 第 15 周 | FASTA/FASTQ, Linux/WSL, SRA Toolkit, RNA-seq | `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/04_Getting_the_SRA_Reads.txt` |
| 6 | Checking the Quality of Data | 8 | 第 5 周, 第 14 周, 第 15 周 | FASTA/FASTQ, Linux/WSL, RNA-seq | `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/06_Checking_the_Quality_of_Data.txt` |
| 8 | Quality Trimming of data | 4.5 | 第 14 周, 第 15 周 | Linux/WSL, RNA-seq | `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/08_Quality_Trimming_of_data.txt` |
| 9 | Aligners and Aligning Reads to genome | 12.8 | 第 5 周, 第 11 周, 第 14 周, 第 15 周 | FASTA/FASTQ, Linux/WSL, IGV/UCSC, RNA-seq | `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/09_Aligners_and_Aligning_Reads_to_genome.txt` |
| 10 | SAM and Bam File Indexing and Sorting | 7.5 | 第 14 周, 第 15 周 | Linux/WSL, samtools, RNA-seq | `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/10_SAM_and_Bam_File_Indexing_and_Sorting.txt` |
| 12 | Feature Extraction | 8.7 | 第 3 周, 第 14 周, 第 15 周 | Linux/WSL, RNA-seq | `07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/12_Feature_Extraction.txt` |

## 逐讲义素材卡

### 2. Introduction to RNA-Seq

- 源文件：`07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/02_Introduction_to_RNA-Seq.txt`
- 时长：4.9 分钟；正文字符数：1494
- 推荐周次：第 1 周, 第 14 周, 第 15 周
- 关键词/实体：Galaxy, Linux/WSL, RNA-seq
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 正如我们在bash 入门课程中看到的那样,当你学习贝叶斯时 和 Linux shell,你知道 Linux shell 是一个强大的子系统,用于与 基因组数据。
- # Introduction to RNA-Seq 大家好,欢迎使用命令行进行基因组数据分析和 NGS 数据处理, 图形用户界面。

### 4. Getting the SRA Reads

- 源文件：`07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/04_Getting_the_SRA_Reads.txt`
- 时长：8.3 分钟；正文字符数：2278
- 推荐周次：第 5 周, 第 14 周, 第 15 周
- 关键词/实体：FASTA/FASTQ, Linux/WSL, SRA Toolkit, RNA-seq
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 之后,我们将看到,如果我们的 fastqdump 是一个软件 用于从 SRA 数据库中检索读取次数。
- NCBI 的 SRA Toolkit是使用 NIN/SDC 序列读取档案中的数据的工具和库的集合。

### 6. Checking the Quality of Data

- 源文件：`07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/06_Checking_the_Quality_of_Data.txt`
- 时长：8 分钟；正文字符数：2204
- 推荐周次：第 5 周, 第 14 周, 第 15 周
- 关键词/实体：FASTA/FASTQ, Linux/WSL, RNA-seq
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 我要应用 FastQC,FastQC 工具,然后我要写一个快速 概述一下,然后我会检查我们的文件 file.FastQC,然后我会生成一个输出 进入数据文件夹,d8data 和正斜杠。
- 因此,FastQC 提供了一种对原始测序数据进行一些质量控制检查的简单方法 来自高通量测序流程、高通量测序公司。

### 8. Quality Trimming of data

- 源文件：`07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/08_Quality_Trimming_of_data.txt`
- 时长：4.5 分钟；正文字符数：1234
- 推荐周次：第 14 周, 第 15 周
- 关键词/实体：Linux/WSL, RNA-seq
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- # Quality Trimming of data 现在我们知道如何检查数据的质量控制以及如何获得数据,因此好数据和坏数据质量之间也存在区别。
- Dream dot fast 在这里您可以看到质量控制很好,因为它没有任何采用者,但这些是我们数据中表示的条形码,所以我们只有两次读取,所以这些都是他们可以生成一些数据集的条形码,所以这就是质量调整过程。

### 9. Aligners and Aligning Reads to genome

- 源文件：`07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/09_Aligners_and_Aligning_Reads_to_genome.txt`
- 时长：12.8 分钟；正文字符数：3412
- 推荐周次：第 5 周, 第 11 周, 第 14 周, 第 15 周
- 关键词/实体：FASTA/FASTQ, Linux/WSL, IGV/UCSC, RNA-seq
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 例如,如果你正在使用人类基因组,如果你大量使用人类基因组,我只是 去寻找人类,它已经在你的第一部分中被引导了,我认为在银河系中你可以 使用更快的格式下载基因组序列,因此您可以更快地下载基因组 我们需要的格式,所以它是 928 GB 左右,之后我会关闭它 当我们获得基因组文件时,我们将安装 botac,因此这是我们的基因组文件,获得了我们的基因组 文件,所以…
- 例如,对于Illumina 平台,有很多正在开发的工具 通过使用Illumina 平台 NGS 数据,我们可以得到该读数。

### 10. SAM and Bam File Indexing and Sorting

- 源文件：`07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/10_SAM_and_Bam_File_Indexing_and_Sorting.txt`
- 时长：7.5 分钟；正文字符数：1969
- 推荐周次：第 14 周, 第 15 周
- 关键词/实体：Linux/WSL, samtools, RNA-seq
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- # SAM and Bam File Indexing and Sorting 在上一个视频中,我们结束了索引部分,但我忘了讨论 关于高顶礼帽。
- 首先我们要安装 samtools,然后我们要转换 SAM 文件 转换为 BAM 文件,然后我们对 BAM 和 SAM 文件进行排序。

### 12. Feature Extraction

- 源文件：`07_NGS_data_Analysis_on_Bash_(Gene_Expression_Using_Command_Line)/12_Feature_Extraction.txt`
- 时长：8.7 分钟；正文字符数：2231
- 推荐周次：第 3 周, 第 14 周, 第 15 周
- 关键词/实体：Linux/WSL, RNA-seq
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 因此,HTsec 计数的主要预期用例是差异表达分析 我们使用该工具的主要目的是什么。
- HTsec count 是我们需要的命令,格式是我们正在使用的完整 BAM 格式 整理出 BAM 是一个包含我们表达式的文件,而 GTA 文件是一个色度文件, 我们需要。
