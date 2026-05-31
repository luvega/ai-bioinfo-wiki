---
type: course-source-chapter
title: AIDD Chapter 10: Microarray Analysis on R
chapter_no: 10
generated: 2026-05-24 12:34:06
status: generated_draft
tags: [aidd, bioinformatics, course-material, auto-extract]
---

# AIDD Chapter 10: Microarray Analysis on R

## 课程定位

本章来自 AIDD Bioinformatics 字幕清理讲义，适合映射到 第 1 周, 第 4 周, 第 5 周, 第 11 周, 第 14 周, 第 16 周, 第 17 周。它是 PDF 教材之外的生信场景素材层。

## 讲义清单

| 课次 | 标题 | 时长 | 推荐周次 | 关键词/实体 | 源文件 |
|---:|---|---:|---|---|---|
| 2 | Introduction of Microarray | 18.8 | 第 1 周, 第 4 周, 第 5 周, 第 14 周, 第 16 周 | RNA-seq, GEO/GEO2R | `10_Microarray_Analysis_on_R/02_Introduction_of_Microarray.txt` |
| 3 | Microarray Databases | 12.3 | 第 4 周, 第 5 周, 第 14 周, 第 16 周 | RNA-seq, GEO/GEO2R | `10_Microarray_Analysis_on_R/03_Microarray_Databases.txt` |
| 5 | Microarray Analysis Using GEO2R | 18.6 | 第 4 周, 第 5 周, 第 16 周 | GEO/GEO2R | `10_Microarray_Analysis_on_R/05_Microarray_Analysis_Using_GEO2R.txt` |
| 7 | Microarray Analysis on R | 33.8 | 第 4 周, 第 5 周, 第 11 周, 第 16 周, 第 17 周 | GEO/GEO2R, GitHub | `10_Microarray_Analysis_on_R/07_Microarray_Analysis_on_R.txt` |

## 逐讲义素材卡

### 2. Introduction of Microarray

- 源文件：`10_Microarray_Analysis_on_R/02_Introduction_of_Microarray.txt`
- 时长：18.8 分钟；正文字符数：4746
- 推荐周次：第 1 周, 第 4 周, 第 5 周, 第 14 周, 第 16 周
- 关键词/实体：RNA-seq, GEO/GEO2R
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 所以本课程主要讲的是GEO 数据库和微阵列数据集 互联网上可用的数据集,以及如何利用这些可用的数据集以及 这些基本上是微阵列数据分析,我们为什么要使用这项技术, 这在基因组学领域中属于什么部分以及为什么它对功能基因组学很重要 这也可能包括在课程中。
- 现在我们将对 MicroEdit 数据集进行命令行分析,然后我们将 首先我们将进行图形用户界面分析,因为它们更相似 使用 Jio 到 R,我们还将向你介绍 Jio 数据库,然后 我们将使用您的命令行界面来解释 R 上的数据。

### 3. Microarray Databases

- 源文件：`10_Microarray_Analysis_on_R/03_Microarray_Databases.txt`
- 时长：12.3 分钟；正文字符数：2715
- 推荐周次：第 4 周, 第 5 周, 第 14 周, 第 16 周
- 关键词/实体：RNA-seq, GEO/GEO2R
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 因此,如果你想分析数据,有两种选择,例如你可以控制 整个系列,然后进入命令行并为其编写代码,或者直接使用 我将为您提供代码,然后根据您自己的需求进行分析,或者只是 编写代码。
- 但如果你不想这样做,你没有那么多时间,你可以 使用作为GEO 数据库一部分的平台,称为 geo2r。

### 5. Microarray Analysis Using GEO2R

- 源文件：`10_Microarray_Analysis_on_R/05_Microarray_Analysis_Using_GEO2R.txt`
- 时长：18.6 分钟；正文字符数：3978
- 推荐周次：第 4 周, 第 5 周, 第 16 周
- 关键词/实体：GEO/GEO2R
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- # Microarray Analysis Using GEO2R 大家好,现在让我们来讨论一下图形用户界面上的微阵列数据分析。
- 首先,我们需要明白的是,一旦我们有了数据集,一旦我们有了 加入后,我们可以使用它来分析命令行操作系统上的数据 并在我们的图形用户界面操作系统上识别不同的表达基因。

### 7. Microarray Analysis on R

- 源文件：`10_Microarray_Analysis_on_R/07_Microarray_Analysis_on_R.txt`
- 时长：33.8 分钟；正文字符数：6950
- 推荐周次：第 4 周, 第 5 周, 第 11 周, 第 16 周, 第 17 周
- 关键词/实体：GEO/GEO2R, GitHub
- 备课用途：优先作为生信场景案例、课堂演示任务或项目素材池；正式进入 PPT 前需要回到 txt 原文核对术语和步骤。

#### 回查片段

- 我会再见 在下一节中,或者我可能要在这里结束,因为没有什么可以补充的 在微阵列数据分析中,你得到了本课程中使用的所有条带 所有使用的数据都将在代码中提供,并可在我的 github 个人资料上查看 非常感谢你的关注,你也可以通过我的 github 存储库联系我 如果你需要指导,如果你想做这些分析,也可以通过我的网站联系我 如果你遇到困难,我也会尽力帮助你,你…
- 现在你 大家已经了解了如何安装我们的工作室、不同的图书馆以及如何 使用这些库,我们现在将继续分析数据,就像我们 图形用户界面到命令行界面。
