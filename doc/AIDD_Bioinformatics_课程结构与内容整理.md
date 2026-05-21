# AIDD Bioinformatics 课程结构与内容整理

## 1. 整理范围

来源目录：`G:\医药数据处理与可视化\AIDD Bioinformatics`

课程主体：`Bioinformatics Data Analysis Crash Course Python R and Linux`

本次整理对象为该目录下的视频字幕文件与课程目录结构。共发现字幕文件 142 个，其中 `.srt` 71 个、`.vtt` 71 个。两类字幕按文件名和目录成对出现，去重后对应 71 节课。字幕内容实际采用 `WEBVTT` 风格，文件头包含 `Language: zh-CN`，说明字幕主体为中文。

累计字幕时长约 772.6 分钟，清洗时间轴后的字幕文本约 191,670 个字符。

## 2. 总体课程定位

这套课程是一门面向生物信息学初学者的跨工具入门课，主线围绕 Python、R、Linux/Bash 三类工具展开，并逐步进入常见生信分析场景：

- Python 与 Biopython：用于序列处理、数据库检索、文件格式解析、系统发育、蛋白质组和机器学习入门。
- Python GUI 应用开发：使用 Tkinter 将常见生信任务封装为桌面工具。
- Linux/Bash：用于命令行环境、NCBI E-utilities、BLAST、序列比对和系统发育分析。
- NGS/RNA-seq 命令行流程：涵盖 SRA 数据下载、FASTQ 质控、修剪、比对、SAM/BAM 处理和 feature extraction。
- Variant calling：涵盖变异类型、质控、参考基因组比对、samtools/bcftools、SNP/indel 分离与 IGV/UCSC 可视化。
- R 生信分析：涵盖 R 包、DESeq2、基因 ID 转换、ggplot2、单细胞 RNA-seq。
- Microarray 与 GitHub：涵盖 GEO2R、微阵列分析、GitHub 仓库与协作流程。

## 3. 文件与结构注意事项

- `.srt` 与 `.vtt` 文件内容基本重复，可优先使用其中一种作为后续课程文本来源。
- `.srt` 文件虽然扩展名为 SRT，但内容实际以 `WEBVTT` 开头。
- 字幕为中文机器翻译风格，部分专业术语需要人工校对。例如 DESeq2 在字幕中多次被识别为 `DSEC` 或 `DSEC2`。
- 第 11 章目录未在字幕中出现。部分章节存在课程序号缺口，应在后续建站或课程整理时标记为“缺失字幕/待补充”。

## 4. 建议重构后的课程模块

### 模块 1：生物编程总览

对应原课程第 1 章。用于解释为什么生物信息学需要 Python、R 和 Bash，以及这些工具分别适合解决什么问题。

### 模块 2：Python 与 Biopython

对应原课程第 2 章。可作为 Python 生信实战基础模块，重点放在序列、格式、数据库、系统发育、蛋白质组和机器学习入门。

### 模块 3：Python GUI 生信工具开发

对应原课程第 3 章。适合重构为项目制课程，每个项目对应一个小工具：序列比对工具、基因组注释工具、系统发育树工具、变异分离工具。

### 模块 4：Linux/Bash 生信基础

对应原课程第 4、5、6 章。可整合为命令行与流程基础模块，补充 WSL、基础命令、NCBI 工具、BLAST 与 pipeline 思维。

### 模块 5：NGS 与 RNA-seq 命令行流程

对应原课程第 7 章。适合整理为一条完整 RNA-seq 上游流程：下载数据、质控、修剪、比对、排序索引、feature extraction。

### 模块 6：Variant Calling

对应原课程第 8 章。适合整理为 DNA-seq 变异检测流程：数据准备、质控、比对、变异检测、VCF 处理、可视化。

### 模块 7：R、DESeq2 与单细胞

对应原课程第 9、10 章。可拆为 R 基础、差异表达、数据可视化、scRNA-seq、microarray/GEO2R。

### 模块 8：GitHub 与项目协作

对应原课程第 12 章。适合放在课程末尾，作为项目管理、代码托管和协作补充。

## 5. 章节整理

## Chapter 1. Introduction To Biological Programming (PY, R and Linux)

课数：2 节  
累计时长：约 20.9 分钟  
字幕字符：约 5,519  
关键词：Python、R、Bash、GUI、RNA、Linux、GitHub、Biopython

### 章节目标

本章介绍“生物编程”的概念，说明生命科学研究如何借助计算机编程处理复杂问题。课程强调 Python、R、Bash 三类工具在生物信息学中的互补作用：Python 适合开发工具和算法，R 适合统计分析和可视化，Bash 适合自动化流程和处理大规模数据。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 1.1 | Introduction To Biological Programming | 11.4 分钟 |
| 1.2 | Powerhouse Trio of Bioinformatics | 9.5 分钟 |

### 内容摘要

本章从基因组学、蛋白质组学、系统生物学等应用场景引出编程的必要性。字幕中提到的典型任务包括序列比对、基因预测、蛋白质结构预测、系统发育分析、基因组组装、转录组分析和系统发育重建。

课程还讨论了语言选择问题：没有唯一“最佳”语言，选择取决于具体任务、个人偏好、可用库、易用性和计算性能。对于 RNA-seq 等流程化分析，Bash 的自动化能力被强调；对于数据分析和机器学习，Python 和 R 更常被使用。

### 可整理成网站内容的结构

- 概念页：什么是 biological programming。
- 对比页：Python、R、Bash 在生信中的分工。
- 案例页：序列比对、基因预测、蛋白结构预测、系统发育树。
- 学习建议页：如何选择第一门工具语言。

## Chapter 2. Python Language for Bioinformatics (Biopython for Bioinformatics)

课数：10 节  
累计时长：约 151.5 分钟  
字幕字符：约 38,743  
关键词：Biopython、Python、RNA、BAM、BLAST、VCF、SAM、机器学习

### 章节目标

本章围绕 Biopython 展开，目标是让学习者掌握 Python 在生物序列、格式解析、数据库访问、基因组处理、系统发育、蛋白质组和机器学习中的基础用法。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 2.1 | BioPython Introduction | 10.0 分钟 |
| 2.2 | Setting up Coding Environment | 14.1 分钟 |
| 2.3 | Explaining the libraries for the course | 15.4 分钟 |
| 2.4 | Advance File Formats of Bioinformatics with BioPython | 19.4 分钟 |
| 2.5 | Sequence Analysis Using Biopython | 16.2 分钟 |
| 2.6 | Database RetrievalAccessing Using Biopython | 11.5 分钟 |
| 2.7 | Working With Genomes Using Biopython | 19.1 分钟 |
| 2.8 | Phylogenetic Tree Construction using Biopython | 14.1 分钟 |
| 2.9 | Proteomics Analysis Using Biopython | 19.9 分钟 |
| 2.10 | Machine Learning in Bioinformatics | 11.8 分钟 |

### 内容摘要

本章先介绍 Biopython 的作用和环境配置，再进入常见生物信息学文件格式和序列分析。字幕中提到可以用 Biopython 读取和写入生物序列，处理 DNA、RNA、蛋白质序列，计算序列长度、GC 含量等属性。

在序列比对部分，课程解释了全局比对和局部比对的区别，并将比对结果与进化关系、突变、插入和缺失联系起来。后续课程覆盖数据库检索、基因组数据处理、系统发育树构建、蛋白质组分析和机器学习在生信中的入门应用。

### 可整理成网站内容的结构

- 环境配置教程：Python、Biopython、相关库安装。
- 文件格式教程：FASTA、FASTQ、SAM、BAM、VCF 等。
- 序列分析教程：读取序列、计算长度、GC 含量、翻译、反向互补。
- 数据库教程：用 Biopython 访问 NCBI 等数据库。
- 项目练习：用 Biopython 构建一个简单序列分析脚本。

## Chapter 3. Python For Bioinformatics Application Development (Tkinter App Development)

课数：15 节  
累计时长：约 133.2 分钟  
字幕字符：约 35,436  
缺失序号：7、14  
关键词：Python、Tkinter、GUI、VCF、alignment、annotation、phylogenetic、variant

### 章节目标

本章将 Python 生信功能封装为图形界面应用，重点使用 Tkinter 开发可运行的小工具，并使用 PyInstaller 打包为 exe。课程偏项目制，适合整理为多个“工具开发项目”。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 3.1 | Introduction to Bioinformatics Application Developemnt | 10.9 分钟 |
| 3.2 | Python For Bioinformatics Application Developemnt | 7.8 分钟 |
| 3.3 | Setting Up the Coding Environment | 14.1 分钟 |
| 3.4 | Introduction to Sequence Alignment and its Algorithms | 7.3 分钟 |
| 3.5 | Code for Sequence Alignment Tool | 10.2 分钟 |
| 3.6 | Testing and Creating Exe File of Alignment Tool | 6.5 分钟 |
| 3.8 | Introduction to Genome Annotation | 7.4 分钟 |
| 3.9 | Code for Genome Annotation Tool | 8.3 分钟 |
| 3.10 | Testing and Creating Exe File of Genome Annotation Tool | 11.3 分钟 |
| 3.11 | Introduction to Phytogenetics and Trees Constructing Algorithms | 9.5 分钟 |
| 3.12 | Code for Phylogenetic Tree Constructor | 9.9 分钟 |
| 3.13 | Testing and Running Phylogenetic Tree Constructor | 9.4 分钟 |
| 3.15 | Introduction to Variant Calling | 8.7 分钟 |
| 3.16 | Code for Variant Seperator | 6.3 分钟 |
| 3.17 | Testing and Creating Exe file of Variant Seperator | 5.8 分钟 |

### 内容摘要

本章首先介绍生信应用开发的目的，然后讲解环境配置。随后以项目形式开发四类工具：

- 序列比对工具：介绍序列比对算法，并实现 GUI 工具。
- 基因组注释工具：介绍 genome annotation，并实现对应工具。
- 系统发育树工具：使用 Biopython 与 Matplotlib 构建和展示系统发育树。
- 变异分离工具：围绕 variant calling 和 VCF 文件，将 SNP 与 indel 等变异进行分离。

目录中另有 `12.1 libraries.txt`，记录了系统发育树工具使用的库：Tkinter、Biopython、Matplotlib，以及用 PyInstaller 打包 exe 的命令。

### 可整理成网站内容的结构

- 项目 1：序列比对 GUI 工具。
- 项目 2：基因组注释 GUI 工具。
- 项目 3：系统发育树构建器。
- 项目 4：VCF 变异分离器。
- 附录：Tkinter、Biopython、Matplotlib、PyInstaller 安装与常见问题。

## Chapter 4. Bash for bioinformatics (Linux use in Bioinformatics)

课数：7 节  
累计时长：约 93.0 分钟  
字幕字符：约 21,349  
关键词：Linux、Bash、BLAST、NCBI E-utilities、sequence alignment、phylogenetic

### 章节目标

本章介绍 Linux/Bash 在生物信息学中的基础使用。重点是命令行环境、基础命令、NCBI E-utilities、常见生信工具安装、BLAST、序列比对和系统发育分析。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 4.1 | Introduction to linux (bash for bioinformatics) | 18.7 分钟 |
| 4.2 | Bash Basic Commands | 15.8 分钟 |
| 4.3 | Ncbi E-utilities on bash (Sequence Analysis) | 16.7 分钟 |
| 4.4 | Famous Bioinformatics Tools (Installation and Introduction) | 9.2 分钟 |
| 4.5 | Blast for Linux (Sequences Homology) | 12.3 分钟 |
| 4.6 | Sequence Alignment Analysis | 6.0 分钟 |
| 4.7 | Phylogenetic Analysis (Tree Construction) | 14.5 分钟 |

### 内容摘要

本章将 Bash 作为生物信息学自动化分析的基础工具。课程先介绍 Linux 命令行的作用，再讲常用命令和 NCBI E-utilities。后半部分进入典型生信工具：安装常见工具、使用 BLAST 做同源性搜索、进行序列比对和系统发育树构建。

### 可整理成网站内容的结构

- Bash 基础命令速查。
- NCBI E-utilities 使用教程。
- BLAST 命令行入门。
- 命令行序列比对示例。
- 系统发育树命令行流程。

## Chapter 5. Linux for Windows Users (WSL)

课数：1 节  
累计时长：约 5.1 分钟  
字幕字符：约 1,664  
关键词：Linux、WSL、Bash

### 章节目标

本章面向 Windows 用户介绍 WSL 环境搭建，帮助学习者在 Windows 系统中使用 Linux 命令行环境。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 5.2 | How to Setup Linux for Windows (WSL) | 5.1 分钟 |

### 内容摘要

课程主要介绍如何在 Windows 上安装和使用 Linux 子系统，为后续 Bash、NGS 和生信命令行分析做准备。

### 可整理成网站内容的结构

- Windows 安装 WSL。
- WSL 与 Linux 发行版基本概念。
- WSL 中运行 Bash 命令。
- 常见安装问题与验证命令。

## Chapter 6. Understanding Bioinformatics Pipeline

课数：1 节  
累计时长：约 7.8 分钟  
字幕字符：约 1,913  
关键词：bioinformatics pipeline、NGS

### 章节目标

本章介绍生物信息学 pipeline 的基本概念，为后续 RNA-seq 和 variant calling 流程做铺垫。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 6.1 | Bioinformatics Pipeline | 7.8 分钟 |

### 内容摘要

本章适合整理为“流程思维”导论，解释为什么生信分析通常不是单个命令，而是一组按顺序连接的步骤。对于后续课程，可将 pipeline 概念与数据输入、软件工具、参数、输出文件、日志和可重复性联系起来。

### 可整理成网站内容的结构

- 什么是 pipeline。
- pipeline 与单步分析的区别。
- 生信流程中的输入、处理、输出。
- 可重复性与自动化。

## Chapter 7. NGS data Analysis on Bash (Gene Expression Using Command Line)

课数：7 节  
累计时长：约 54.7 分钟  
字幕字符：约 14,451  
缺失序号：3、5、7、11  
关键词：RNA-seq、SRA、FASTQ、quality control、trimming、alignment、SAM、BAM、feature extraction

### 章节目标

本章围绕命令行 RNA-seq 或基因表达分析流程展开。重点是从 SRA 获取 reads，进行质控、修剪、比对、SAM/BAM 排序索引，并进行 feature extraction。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 7.2 | Introduction to RNA-Seq | 4.9 分钟 |
| 7.4 | Getting the SRA Reads | 8.3 分钟 |
| 7.6 | Checking the Quality of Data | 8.0 分钟 |
| 7.8 | Quality Trimming of data | 4.5 分钟 |
| 7.9 | Aligners and Aligning Reads to genome | 12.8 分钟 |
| 7.10 | SAM and Bam File Indexing and Sorting | 7.5 分钟 |
| 7.12 | Feature Extraction | 8.7 分钟 |

### 内容摘要

本章是 NGS 命令行实战的核心部分。字幕中介绍了为什么命令行适合处理 NGS 数据：数据量大、文件多、需要重复执行相同步骤、可重复性优于 GUI。课程从 RNA-seq 简介进入 SRA 数据获取，再依次执行数据质量检查、质量修剪、reads 到 genome 的比对、SAM/BAM 文件排序和索引，以及后续 feature extraction。

### 推荐整理为流程图

SRA accession -> FASTQ 下载 -> FastQC 质控 -> trimming -> aligner 比对 -> SAM/BAM -> sort/index -> featureCounts 或类似工具 -> count matrix

### 可整理成网站内容的结构

- RNA-seq 上游分析概览。
- SRA Toolkit 下载数据。
- FASTQ 质量检查。
- reads 修剪。
- reads 比对到参考基因组。
- SAM/BAM 排序与索引。
- feature extraction 与 count matrix。

## Chapter 8. Variant Calling on Bash

课数：9 节  
累计时长：约 60.5 分钟  
字幕字符：约 15,970  
缺失序号：5、9  
关键词：variant calling、FASTQ、VCF、BAM、SAM、SRA、SNP、indel、IGV、UCSC

### 章节目标

本章介绍命令行变异检测流程。重点包括变异类型、元数据和软件、SRA 数据获取、质控修剪、参考基因组比对、samtools/bcftools 调用变异、SNP 与 indel 分离，以及 IGV/UCSC 可视化。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 8.1 | Introduction to Variant Calling | 3.8 分钟 |
| 8.2 | Variants and Types | 7.3 分钟 |
| 8.3 | Understanding the Metadata and Software | 5.3 分钟 |
| 8.4 | Getting Data From SRA Using SRA Toolkit | 7.3 分钟 |
| 8.6 | Quality Control and Trimming | 9.8 分钟 |
| 8.7 | Alignment to Reference Genome | 10.2 分钟 |
| 8.8 | Sam and Bcf Tools and Fixing NS and Calling Variants | 7.8 分钟 |
| 8.10 | Separation of SNP's and Indels Variants | 5.3 分钟 |
| 8.11 | Visualizing Variants Using IGV and UCSC Browser | 3.6 分钟 |

### 内容摘要

本章与第 7 章结构相似，但分析目标从表达量变为变异检测。课程先定义 variants 及其类型，然后讲解元数据、软件准备和 SRA 数据下载。流程主体包括 FASTQ 质控与修剪、reads 到参考基因组比对、SAM/BAM 处理、使用 samtools/bcftools 调用变异，并将 SNP 与 indel 分开处理。最后通过 IGV 和 UCSC Browser 查看变异。

### 推荐整理为流程图

SRA accession -> FASTQ -> QC/trimming -> reference genome alignment -> BAM -> variant calling -> VCF -> SNP/indel filtering -> IGV/UCSC visualization

### 可整理成网站内容的结构

- 什么是 variant calling。
- SNP、indel 和其他变异类型。
- 变异检测所需数据和参考基因组。
- samtools/bcftools 基础流程。
- VCF 文件结构。
- IGV/UCSC 可视化。

## Chapter 9. R for Bioinformatics

课数：9 节  
累计时长：约 101.5 分钟  
字幕字符：约 24,363  
关键词：R、DESeq2、RNA-seq、ggplot2、Ensembl ID、gene symbol、scRNA-seq

### 章节目标

本章介绍 R 在生物信息学分析中的使用，覆盖 R 安装、变量、包管理、DESeq2 差异表达、基因 ID 转换、ggplot2 可视化和单细胞 RNA-seq 入门。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 9.1 | Introduction to Bioinformatics and R Exploring the Intersection of Biology | 8.0 分钟 |
| 9.2 | Getting Started with R Installation and Variables Understanding | 10.3 分钟 |
| 9.3 | Working with R Packages Installing, Loading, and Exploring Bioinformatics | 9.6 分钟 |
| 9.4 | Differential Gene Expression Analysis with Deseq2 Preparing Data | 5.4 分钟 |
| 9.5 | Deseq2 Code Understanding | 17.7 分钟 |
| 9.6 | Converting Ensembl Gene IDs to Gene Symbols Using R Techniques and Packages | 11.5 分钟 |
| 9.7 | Visualizing Gene Expression Data Creating Stunning Plots with ggplot2 | 10.3 分钟 |
| 9.8 | Introduction to Single-Cell RNA Sequencing (scRNA-seq) Data Analysis | 7.2 分钟 |
| 9.9 | Exploring scRNA-seq Code Cell Trajectories and Gene Expression Dynamics | 21.5 分钟 |

### 内容摘要

本章从 R 的安装和变量基础开始，进入 R 包安装和加载。核心内容是使用 DESeq2 做 RNA-seq 差异表达分析。字幕中提到的步骤包括导入 count data、准备 metadata、构建 DESeq2 dataset、探索性数据分析、归一化、质量控制、过滤低表达基因、估计 size factor 和 dispersion、负二项模型、结果提取和可视化。

可视化部分强调火山图、热图和 ggplot2。后续课程介绍 Ensembl Gene ID 到 gene symbol 的转换，以及 scRNA-seq 数据分析、细胞轨迹和基因表达动态。

### 推荐整理为流程图

count matrix + metadata -> DESeqDataSet -> normalization -> QC/EDA -> model fitting -> differential expression results -> volcano/heatmap -> annotation

### 可整理成网站内容的结构

- R 与 RStudio 环境。
- R 包安装与加载。
- DESeq2 差异表达分析。
- Ensembl ID 转 gene symbol。
- ggplot2 表达数据可视化。
- scRNA-seq 基础概念。
- 单细胞轨迹和表达动态。

## Chapter 10. Microarray Analysis on R

课数：4 节  
累计时长：约 83.5 分钟  
字幕字符：约 18,051  
缺失序号：1、4、6  
关键词：microarray、GEO、GEO2R、R、RNA

### 章节目标

本章介绍微阵列分析，重点是 microarray 概念、数据库、GEO2R 和 R 中的微阵列分析流程。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 10.2 | Introduction of Microarray | 18.8 分钟 |
| 10.3 | Microarray Databases | 12.3 分钟 |
| 10.5 | Microarray Analysis Using GEO2R | 18.6 分钟 |
| 10.7 | Microarray Analysis on R | 33.8 分钟 |

### 内容摘要

本章围绕微阵列数据分析展开。课程先介绍 microarray 的基本原理，再介绍微阵列数据库，尤其是 GEO 相关数据来源。随后讲解 GEO2R 的使用，并进一步进入 R 语言中的微阵列分析。

### 可整理成网站内容的结构

- Microarray 与 RNA-seq 的区别。
- GEO 数据库和数据检索。
- GEO2R 在线差异分析。
- R 中读取和分析 microarray 数据。
- 微阵列分析结果可视化。

## Chapter 12. GitHub Guide for Students

课数：6 节  
累计时长：约 60.9 分钟  
字幕字符：约 14,211  
缺失序号：2  
关键词：GitHub、repository、fork、clone、collaboration、project management

### 章节目标

本章介绍 GitHub 在生物信息学学习和项目协作中的作用。内容包括 GitHub 入门、个人主页和仓库设置、查找生物信息学项目、fork 和 clone、协作流程、项目管理。

### 课程清单

| 编号 | 课程标题 | 时长 |
|---|---|---:|
| 12.1 | Introduction to Github for Bioinformatics | 11.1 分钟 |
| 12.3 | GitHub Profile and Repository Setup for First Time | 12.3 分钟 |
| 12.4 | Bioinformatics Projects Searching on GitHub | 7.4 分钟 |
| 12.5 | Forking and Cloning Repositories on GitHub | 15.4 分钟 |
| 12.6 | How to Collaborate on GitHub | 6.6 分钟 |
| 12.7 | Learn GitHub for Project Mangement | 8.2 分钟 |

### 内容摘要

本章适合作为课程末尾的协作与项目管理模块。它帮助学生理解 GitHub 账号、个人主页、仓库、搜索项目、fork、clone、协作和项目管理的基本流程。对生物信息学学习者而言，GitHub 可用于保存代码、复现实验、查找开源 pipeline 和参与协作。

### 可整理成网站内容的结构

- GitHub 基础概念。
- 创建个人主页和仓库。
- 搜索生物信息学项目。
- Fork 与 clone。
- 协作流程。
- 项目管理与课程作业提交。

## 6. 后续加工建议

### 6.1 建站数据模型

建议将本课程整理为以下结构化数据：

- `Course`：课程名、来源目录、总课数、总时长、简介。
- `Chapter`：章节编号、章节标题、简介、关键词、课数、累计时长、缺失课程序号。
- `Lesson`：课程序号、标题、字幕路径、时长、摘要、知识点、相关工具。
- `Topic`：Python、R、Bash、RNA-seq、Variant Calling、DESeq2、scRNA-seq、Microarray、GitHub 等主题。
- `Asset`：字幕文件、代码文件、附件文本、后续可补充的视频或练习文件。

### 6.2 字幕转讲义流程

建议后续按以下步骤处理字幕：

1. 去除 WEBVTT 文件头、时间轴和空行。
2. 按语义段落重新断句。
3. 修正机器翻译术语，如 DESeq2、RNA-seq、FASTQ、featureCounts、samtools、bcftools、Biopython。
4. 为每节课补充“学习目标、核心概念、操作步骤、常见问题、练习任务”。
5. 将代码片段从视频或附件中单独抽出，放入可复制代码块。

### 6.3 优先重构顺序

建议优先整理以下内容，因为它们最适合直接转成学习网站模块：

1. Chapter 7 RNA-seq 命令行流程。
2. Chapter 8 Variant Calling 流程。
3. Chapter 9 R/DESeq2/ggplot2/scRNA-seq。
4. Chapter 2 Biopython 基础。
5. Chapter 4 Bash 生信基础。
6. Chapter 3 Python GUI 项目制内容。

## 7. 质量风险

- 字幕存在机器翻译痕迹，不能直接作为正式教材发布。
- 部分课程缺号，可能是视频或字幕文件缺失，也可能是原课程编号跳号。
- 标题中存在拼写错误，例如 `Developemnt`、`Seperator`、`Phytogenetics`、`Project Mangement`，后续正式整理时应修正为 `Development`、`Separator`、`Phylogenetics`、`Project Management`。
- 有些专业术语在字幕中被错误识别，例如 DESeq2 被写作 DSEC/DSEC2，应统一校正。
- 课程内容覆盖面广，但深度不均，后续建站时需要补充概念图、流程图、代码复现和测验题。
