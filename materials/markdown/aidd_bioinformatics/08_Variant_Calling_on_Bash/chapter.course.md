---
type: course-source-chapter
title: AIDD Chapter 8: Variant Calling on Bash
chapter_no: 8
generated: 2026-05-24 12:34:06
status: generated_draft
tags: [aidd, bioinformatics, course-material, auto-extract]
---

# AIDD Chapter 8: Variant Calling on Bash

## 课程定位

本章来自 AIDD Bioinformatics 字幕清理讲义，适合映射到 第 1 周, 第 5 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周。它是 PDF 教材之外的生信场景素材层。

## 讲义清单

| 课次 | 标题 | 时长 | 推荐周次 | 关键词/实体 | 源文件 |
|---:|---|---:|---|---|---|
| 1 | Introduction to Variant Calling | 3.8 | 第 1 周, 第 5 周, 第 15 周, 第 16 周 | FASTA/FASTQ, Linux/WSL, SRA Toolkit | `08_Variant_Calling_on_Bash/01_Introduction_to_Variant_Calling.txt` |
| 2 | Variants and Types | 7.3 | 第 15 周, 第 16 周 | Linux/WSL | `08_Variant_Calling_on_Bash/02_Variants_and_Types.txt` |
| 3 | Understanding the Metadata and Software | 5.3 | 第 5 周, 第 15 周, 第 16 周 | FASTA/FASTQ, Linux/WSL, SRA Toolkit, samtools, bcftools | `08_Variant_Calling_on_Bash/03_Understanding_the_Metadata_and_Software.txt` |
| 4 | Getting Data From SRA Using SRA Toolkit | 7.3 | 第 5 周, 第 14 周, 第 15 周, 第 16 周 | FASTA/FASTQ, Linux/WSL, SRA Toolkit, RNA-seq | `08_Variant_Calling_on_Bash/04_Getting_Data_From_SRA_Using_SRA_Toolkit.txt` |
| 6 | Quality Control and Trimming | 9.8 | 第 5 周, 第 15 周, 第 16 周 | FASTA/FASTQ, Linux/WSL, SRA Toolkit | `08_Variant_Calling_on_Bash/06_Quality_Control_and_Trimming.txt` |
| 7 | Alignment to Reference Genome | 10.2 | 第 5 周, 第 11 周, 第 15 周, 第 16 周 | Linux/WSL, SRA Toolkit, samtools, IGV/UCSC | `08_Variant_Calling_on_Bash/07_Alignment_to_Reference_Genome.txt` |
| 8 | Sam and Bcf Tools and Fixing NS and Calling Variants | 7.8 | 第 5 周, 第 15 周, 第 16 周 | FASTA/FASTQ, Linux/WSL, samtools, bcftools | `08_Variant_Calling_on_Bash/08_Sam_and_Bcf_Tools_and_Fixing_NS_and_Calling_Variants.txt` |
| 10 | Separation of SNP's and Indels Variants | 5.3 | 第 11 周, 第 15 周, 第 16 周 | Linux/WSL, IGV/UCSC | `08_Variant_Calling_on_Bash/10_Separation_of_SNPs_and_Indels_Variants.txt` |
| 11 | Visualizing Variants Using IGV and UCSC Browser | 3.6 | 第 11 周, 第 15 周, 第 16 周 | Linux/WSL, IGV/UCSC | `08_Variant_Calling_on_Bash/11_Visualizing_Variants_Using_IGV_and_UCSC_Browser.txt` |

## 逐讲义素材卡

### 1. Introduction to Variant Calling

- 源文件：`08_Variant_Calling_on_Bash/01_Introduction_to_Variant_Calling.txt`
- 时长：3.8 分钟；正文字符数：1005
- 推荐周次：第 1 周, 第 5 周, 第 15 周, 第 16 周
- 关键词/实体：FASTA/FASTQ, Linux/WSL, SRA Toolkit
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 在本课程中,我们将处理用于分析 基因组数据,我们将从 SRA 表格或 FASTQ 表格中获取读取文件并将其转换为变体 文件。
- 所以划分这个课程,如果你熟悉NGS数据,你就知道下一个 一代测序数据会产生大量的文件,通过这些文件我们可以分析 基因组变异,比如上一个时代定义的变化 现在已在参考基因组中定义。

### 2. Variants and Types

- 源文件：`08_Variant_Calling_on_Bash/02_Variants_and_Types.txt`
- 时长：7.3 分钟；正文字符数：1969
- 推荐周次：第 15 周, 第 16 周
- 关键词/实体：Linux/WSL
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 所以你现在应该问的一个问题是,NGS 数据如何让我们如此自信 从这种数据中可以识别出 SNP 和 N-DEL 吗?
- 所以回答你的问题,虽然NGS产生了大量的数据测序, 其转化基因药物的能力, 依赖于以高置信度识别相关变体。

### 3. Understanding the Metadata and Software

- 源文件：`08_Variant_Calling_on_Bash/03_Understanding_the_Metadata_and_Software.txt`
- 时长：5.3 分钟；正文字符数：1575
- 推荐周次：第 5 周, 第 15 周, 第 16 周
- 关键词/实体：FASTA/FASTQ, Linux/WSL, SRA Toolkit, samtools, bcftools
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 所以我们需要一个 Linux 操作系统,或者如果你使用 Windows 操作系统, 你只需要为你的 Windows 操作系统提供 WSL 终端。
- Sam 工具也可在 APT 系统、伪 APT 安装、samtools和 bcftools上使用。

### 4. Getting Data From SRA Using SRA Toolkit

- 源文件：`08_Variant_Calling_on_Bash/04_Getting_Data_From_SRA_Using_SRA_Toolkit.txt`
- 时长：7.3 分钟；正文字符数：1987
- 推荐周次：第 5 周, 第 14 周, 第 15 周, 第 16 周
- 关键词/实体：FASTA/FASTQ, Linux/WSL, SRA Toolkit, RNA-seq
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- # Getting Data From SRA Using SRA Toolkit 所以现在是我们要使用的第一步。
- 因此,SRA 是我们用来检索所有 RNA-seq 和 DNA-seq 数据的数据库。

### 6. Quality Control and Trimming

- 源文件：`08_Variant_Calling_on_Bash/06_Quality_Control_and_Trimming.txt`
- 时长：9.8 分钟；正文字符数：2584
- 推荐周次：第 5 周, 第 15 周, 第 16 周
- 关键词/实体：FASTA/FASTQ, Linux/WSL, SRA Toolkit
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 那么基本上什么是质量控制 所以 FastQC 是一个对原始序列数据进行质量控制检查和检查的工具 来自高通量测序流程。
- 对于你的分析,你有你的管道,你可以使用管道来获取你所有的 测序数据和读数提取已完成。

### 7. Alignment to Reference Genome

- 源文件：`08_Variant_Calling_on_Bash/07_Alignment_to_Reference_Genome.txt`
- 时长：10.2 分钟；正文字符数：2967
- 推荐周次：第 5 周, 第 11 周, 第 15 周, 第 16 周
- 关键词/实体：Linux/WSL, SRA Toolkit, samtools, IGV/UCSC
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 例如,如果我们有 参考基因组中的比对,我们想要可视化单个基因的比对, 例如,在 CHR 17 染色体中,在 17 号染色体中,我们需要使用 IGV。
- 所以如果你使用我们不知道的数据 我们从哪里得到这些数据,我们的客户没有告诉我们我们拥有什么样的数据,还有一些 就像这样。

### 8. Sam and Bcf Tools and Fixing NS and Calling Variants

- 源文件：`08_Variant_Calling_on_Bash/08_Sam_and_Bcf_Tools_and_Fixing_NS_and_Calling_Variants.txt`
- 时长：7.8 分钟；正文字符数：2206
- 推荐周次：第 5 周, 第 15 周, 第 16 周
- 关键词/实体：FASTA/FASTQ, Linux/WSL, samtools, bcftools
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 所以 BCF 通过使用 bcftools,我们可以在变体调用格式文件中操作变体调用, 以及它的二进制对应物 BCF。
- 那么如何安装这些 samtools以及如何使用这些 samtools。

### 10. Separation of SNP's and Indels Variants

- 源文件：`08_Variant_Calling_on_Bash/10_Separation_of_SNPs_and_Indels_Variants.txt`
- 时长：5.3 分钟；正文字符数：1331
- 推荐周次：第 11 周, 第 15 周, 第 16 周
- 关键词/实体：Linux/WSL, IGV/UCSC
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 因此可以使用这两个工具查看变体调用的结果 比如论坛、IGV 或 UCSC 浏览器。
- 那么我们如何通过再次使用 SNP 来区分它们 像我们一样查看系统,我们可以从这里分离 SNP,你可以看到我们刚刚 把 SNP 从 SNP 文件中分离出来,现在我要为它创建一个新的 SNP 文件 点 VCF。

### 11. Visualizing Variants Using IGV and UCSC Browser

- 源文件：`08_Variant_Calling_on_Bash/11_Visualizing_Variants_Using_IGV_and_UCSC_Browser.txt`
- 时长：3.6 分钟；正文字符数：1046
- 推荐周次：第 11 周, 第 15 周, 第 16 周
- 关键词/实体：Linux/WSL, IGV/UCSC
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 所以我希望你现在对变体调用有了更好的理解,对于代码部分,我会将所有这些代码上传到一个文件中,然后你可以使用它来分析你自己的数据。
- # Visualizing Variants Using IGV and UCSC Browser 为了可视化我们刚刚调用的变体(我们刚刚制作了变体调用文件),我们需要使用板载 IGV 或 UCSC 基因组浏览器。
