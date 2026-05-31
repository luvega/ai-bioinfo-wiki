---
type: course-source-chapter
title: AIDD Chapter 9: R for Bioinformatics
chapter_no: 9
generated: 2026-05-24 12:34:06
status: generated_draft
tags: [aidd, bioinformatics, course-material, auto-extract]
---

# AIDD Chapter 9: R for Bioinformatics

## 课程定位

本章来自 AIDD Bioinformatics 字幕清理讲义，适合映射到 第 1 周, 第 3 周, 第 4 周, 第 5 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周, 第 17 周。它是 PDF 教材之外的生信场景素材层。

## 讲义清单

| 课次 | 标题 | 时长 | 推荐周次 | 关键词/实体 | 源文件 |
|---:|---|---:|---|---|---|
| 1 | Introduction to Bioinformatics and R Exploring the Intersection of Biology | 8 | 第 1 周, 第 4 周, 第 5 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周 | Linux/WSL, GEO/GEO2R | `09_R_for_Bioinformatics/01_Introduction_to_Bioinformatics_and_R_Exploring_the_Intersection_of_Biology.txt` |
| 2 | Getting Started with R Installation and Variables Understanding | 10.3 | 第 1 周, 第 3 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周 | Linux/WSL | `09_R_for_Bioinformatics/02_Getting_Started_with_R_Installation_and_Variables_Understanding.txt` |
| 3 | Working with R Packages Installing, Loading, and Exploring Bioinformatics | 9.6 | 第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周, 第 17 周 | GitHub | `09_R_for_Bioinformatics/03_Working_with_R_Packages_Installing,_Loading,_and_Exploring_Bioinformatics.txt` |
| 4 | Differential Gene Expression Analysis with Deseq2 Preparing Data | 5.4 | 第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周 | RNA-seq, DESeq2 | `09_R_for_Bioinformatics/04_Differential_Gene_Expression_Analysis_with_Deseq2_Preparing_Data.txt` |
| 5 | Deseq2 Code Understanding | 17.7 | 第 1 周, 第 4 周, 第 5 周, 第 11 周, 第 14 周, 第 16 周, 第 17 周 | SRA Toolkit, RNA-seq, DESeq2, GitHub | `09_R_for_Bioinformatics/05_Deseq2_Code_Understanding.txt` |
| 6 | Converting Ensembl Gene IDs to Gene Symbols Using R Techniques and Packages | 11.5 | 第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 16 周, 第 17 周 | DESeq2, GitHub | `09_R_for_Bioinformatics/06_Converting_Ensembl_Gene_IDs_to_Gene_Symbols_Using_R_Techniques_and_Packages.txt` |
| 7 | Visualizing Gene Expression Data Creating Stunning Plots with ggplot2 | 10.3 | 第 1 周, 第 4 周, 第 5 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周, 第 17 周 | RNA-seq, ggplot2, GEO/GEO2R, GitHub | `09_R_for_Bioinformatics/07_Visualizing_Gene_Expression_Data_Creating_Stunning_Plots_with_ggplot2.txt` |
| 8 | Introduction to Single-Cell RNA Sequencing (scRNA-seq) Data Analysis | 7.2 | 第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周 | Linux/WSL, RNA-seq, scRNA-seq | `09_R_for_Bioinformatics/08_Introduction_to_Single-Cell_RNA_Sequencing_(scRNA-seq)_Data_Analysis.txt` |
| 9 | Exploring scRNA-seq Code Cell Trajectories and Gene Expression Dynamics | 21.5 | 第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周, 第 17 周 | Linux/WSL, RNA-seq, scRNA-seq, GitHub | `09_R_for_Bioinformatics/09_Exploring_scRNA-seq_Code_Cell_Trajectories_and_Gene_Expression_Dynamics.txt` |

## 逐讲义素材卡

### 1. Introduction to Bioinformatics and R Exploring the Intersection of Biology

- 源文件：`09_R_for_Bioinformatics/01_Introduction_to_Bioinformatics_and_R_Exploring_the_Intersection_of_Biology.txt`
- 时长：8 分钟；正文字符数：2274
- 推荐周次：第 1 周, 第 4 周, 第 5 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周
- 关键词/实体：Linux/WSL, GEO/GEO2R
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 我们还可以使用 R 用于从 NCBI、GEO 数据库等在线资源访问生物信息学数据, ensemble 数据库,我们还可以使用它们的 API 和 Web 服务器。
- 因此,R 生态系统还可以在综合 R Archive 网络上使用, 也被称为 CRAN,它提供了各种各样的统计分析和数据软件包 操纵。

### 2. Getting Started with R Installation and Variables Understanding

- 源文件：`09_R_for_Bioinformatics/02_Getting_Started_with_R_Installation_and_Variables_Understanding.txt`
- 时长：10.3 分钟；正文字符数：2834
- 推荐周次：第 1 周, 第 3 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周
- 关键词/实体：Linux/WSL
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 我们可以使用 R 进行统计数据分析、遗传和基因组分析、微阵列 世代排序分析和可视化。
- 如果您使用的是 Debian、Cedora 或 Ubuntu,则可以下载您的 Linux 操作系统。

### 3. Working with R Packages Installing, Loading, and Exploring Bioinformatics

- 源文件：`09_R_for_Bioinformatics/03_Working_with_R_Packages_Installing,_Loading,_and_Exploring_Bioinformatics.txt`
- 时长：9.6 分钟；正文字符数：2483
- 推荐周次：第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周, 第 17 周
- 关键词/实体：GitHub
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 因此,通过安装本地文件,您可以下载任何文件,有时您必须使用 R 包 您必须下载本地存储的数据,然后从其他来源下载 或者您只需自己开发代码部分。
- R 是一种广泛使用的编程语言,我们讨论过它用于统计和数据 分析。

### 4. Differential Gene Expression Analysis with Deseq2 Preparing Data

- 源文件：`09_R_for_Bioinformatics/04_Differential_Gene_Expression_Analysis_with_Deseq2_Preparing_Data.txt`
- 时长：5.4 分钟；正文字符数：1416
- 推荐周次：第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周
- 关键词/实体：RNA-seq, DESeq2
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- # Differential Gene Expression Analysis with Deseq2 Preparing Data 那么让我们来谈谈 RNA-seq或差异基因表达。
- 我们所做的就是得到广泛使用的 DESeq2 数据,DESeq2 广泛用于 RNA-seq分析的软件包。

### 5. Deseq2 Code Understanding

- 源文件：`09_R_for_Bioinformatics/05_Deseq2_Code_Understanding.txt`
- 时长：17.7 分钟；正文字符数：4149
- 推荐周次：第 1 周, 第 4 周, 第 5 周, 第 11 周, 第 14 周, 第 16 周, 第 17 周
- 关键词/实体：SRA Toolkit, RNA-seq, DESeq2, GitHub
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 这就是 DESeq2 的全部内容,我将把此代码提供给我的 github 帐户的 R 然后您也可以使用它来进行分析。
- 因此,DESeq2 是一个功能强大且广泛使用的 R 包,用于基于我们的 RNA-seq数据进行差异基因表达分析。

### 6. Converting Ensembl Gene IDs to Gene Symbols Using R Techniques and Packages

- 源文件：`09_R_for_Bioinformatics/06_Converting_Ensembl_Gene_IDs_to_Gene_Symbols_Using_R_Techniques_and_Packages.txt`
- 时长：11.5 分钟；正文字符数：3012
- 推荐周次：第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 16 周, 第 17 周
- 关键词/实体：DESeq2, GitHub
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 首先,我将使用之前的代码示例来向你展示这一点 DESeq2,我们从中获取集合 ID 中的计数数据。
- 因此其他命令是运行过滤器获取 em 在这里你可以看到我们的结果所以这里是 集合的基因 ID,然后是外部基因,所以在这里你可以看到基因名称 这些基因 ID,例如 cd 971a 是我们的基因,因此让我们在这里搜索某种类型的基因 适用于 momosapiens,所以在这里你可以看到 cd 91a 适用于肌肉 颜色人类 momosapiens 也适用于人类所以在…

### 7. Visualizing Gene Expression Data Creating Stunning Plots with ggplot2

- 源文件：`09_R_for_Bioinformatics/07_Visualizing_Gene_Expression_Data_Creating_Stunning_Plots_with_ggplot2.txt`
- 时长：10.3 分钟；正文字符数：2719
- 推荐周次：第 1 周, 第 4 周, 第 5 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周, 第 17 周
- 关键词/实体：RNA-seq, ggplot2, GEO/GEO2R, GitHub
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- # Visualizing Gene Expression Data Creating Stunning Plots with ggplot2 让我们来谈谈基因表达数据。
- 这就是 RNA 的全部内容 序列可视化和数据,如果你们有任何问题并想 学习想要从中得到一些东西想要帮我做一些分析或者你 想要联系我你也可以在我的 github 页面上联系我也可以 通过我的 Udemy 收件箱等方式联系我。

### 8. Introduction to Single-Cell RNA Sequencing (scRNA-seq) Data Analysis

- 源文件：`09_R_for_Bioinformatics/08_Introduction_to_Single-Cell_RNA_Sequencing_(scRNA-seq)_Data_Analysis.txt`
- 时长：7.2 分钟；正文字符数：1921
- 推荐周次：第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周
- 关键词/实体：Linux/WSL, RNA-seq, scRNA-seq
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- # Introduction to Single-Cell RNA Sequencing (scRNA-seq) Data Analysis 所以,单细胞测序数据分析。
- 在本视频中,我们将了解单细胞测序的工作原理, 它的基本流程,以及如何使用 R 工具分析单细胞数据 测序,以及我们可以在哪里获取单细胞测序的数据。

### 9. Exploring scRNA-seq Code Cell Trajectories and Gene Expression Dynamics

- 源文件：`09_R_for_Bioinformatics/09_Exploring_scRNA-seq_Code_Cell_Trajectories_and_Gene_Expression_Dynamics.txt`
- 时长：21.5 分钟；正文字符数：4605
- 推荐周次：第 1 周, 第 4 周, 第 11 周, 第 14 周, 第 15 周, 第 16 周, 第 17 周
- 关键词/实体：Linux/WSL, RNA-seq, scRNA-seq, GitHub
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 你可以使用它来分析 你的结果,因为我认为代码应该对你可用,这样你就可以 轻松使用它进行分析,如果你们想让我分析你们的数据 你也可以通过我的电子邮件、我的 网站是 bio datanerd,我的 Instagram 帐户也是 bio datanerd 以及我的个人 Instagram 帐户,也可以使用 在 Udemy 上讨论生物信息学技术等 那。
- 您可以使用我的代码 github 帐户,然后编辑它,然后使用你的任何文件来创建你的 数据集,然后将其用于单细胞测序分析。
