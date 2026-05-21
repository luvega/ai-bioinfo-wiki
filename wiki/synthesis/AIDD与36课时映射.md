---
type: synthesis
title: AIDD 章节 → 36 课时教学大纲 映射
status: stable
related_sources: [AIDD_Bioinformatics_Course, 36课时讲稿, AIDD课程结构整理]
tags: [mapping, course-design]
---

# AIDD 章节 → 36 课时教学大纲 · 映射表

## 一句话

**AIDD 是案例素材，36 课时大纲是教学骨架。**
每一节 AIDD 字幕只在它能服务某一周教学时才被使用，**不照搬课程结构**。

## 主映射表

| 36 课时周 | 主题 | AIDD 章节 | 使用方式 |
|---:|---|---|---|
| 1 | 课程导论 | Ch.1 §1, §2 | 引入"生物编程"与"工具分工"概念，作为药学问题的扩展视角 |
| 2 | 复现规范 | Ch.5 §2, Ch.6 §1, Ch.12 §1, §3 | WSL 5 分钟演示、pipeline 思维、GitHub 入门 |
| 3 | Python 入门 + AI 辅助 | Ch.2 §1, §2, §3 | Python 环境与 Biopython 作为"Python 不止处理 csv"的扩展案例 |
| 4 | R 入门 | Ch.9 §1, §2, §3 | R 安装、变量、包管理直接借用 |
| 5 | 数据读取与整形 | Ch.2 §4（文件格式扩展）、Ch.7 §4（SRA 下载示例） | 多种文件格式作为"读取多样性"案例 |
| 6 | 数据清洗 | — | 本课程自有案例（临床指标表） |
| 7 | 描述统计与可视化 | Ch.9 §7（ggplot2 简介） | ggplot2 入门 PPT |
| 8 | 假设检验 | — | 来自 [ISLP](../sources/ISLP.md) Ch.13 |
| 9 | 相关与回归 | — | 来自 [ISLP](../sources/ISLP.md) Ch.3 / [ISLR](../sources/ISLR.md) Ch.3 |
| 10 | 多元统计与分类 | Ch.2 §10 Machine Learning in Bioinformatics（轻量） | 作为分类的生信场景例 |
| **11** | **差异表达 + DESeq2 + [富集分析](../concepts/富集分析_GO_KEGG.md)** | **Ch.9 §4-7** | AIDD 提供 DESeq2，**富集分析需外部素材补**（AIDD 未涉及） |
| 12 | 高维可视化 | Ch.9 §7 + ISLP Ch.12（PCA / 聚类） | volcano / heatmap / PCA |
| 13 | 机器学习入门 | — | 主要来自 [ISLP](../sources/ISLP.md) Ch.2, §5, §8 |
| 14 | scRNA-seq 概览 | Ch.9 §8, §9 | scRNA-seq 概念 + 简化 Seurat 演示 |
| 15 | Microarray / GEO2R | Ch.10 §2, §3, §5, §7 | 核心教学素材 |
| 16 | 组学综合分析 | Ch.7 全章 + Ch.8 全章 | 流程演示（不让学生跑）+ 用现成下游数据 |
| 17 | 项目实战 I | Ch.12 §4, §5, §6（GitHub Fork / Clone / Collaborate） | 协作流程 |
| 18 | 项目实战 II + 复盘 | Ch.12 §7（Project Management） | 项目管理 + 复盘 |

## 不映射的 AIDD 内容（本课程不用）

- AIDD Ch.3（Python GUI 应用 / Tkinter）—— 与药学数据分析关联弱。
- AIDD Ch.4 §3-5（NCBI E-utilities、本地 BLAST）—— 仅作选修。
- AIDD Ch.2 §7-9（基因组、系统发育、蛋白质组细节）—— 偏生信深度，不展开。
- AIDD 大部分命令行细节 —— 36 课时课程不教 NGS 上游处理。

## 反向映射：每节 AIDD 字幕能去哪一周

> 这部分按需展开，目前先给前 30 节示例：

| AIDD 章节路径 | 36 课时落点 | 使用方式 |
|---|---|---|
| `01_.../01_Introduction_To_Biological_Programming.txt` | Week 1 | 导入 PPT，1 张图 |
| `01_.../02_Powerhouse_Trio_of_Bioinformatics.txt` | Week 1 | [工具分工](../concepts/工具分工_Python_R_Bash.md) 概念页 |
| `02_.../01_BioPython_Introduction.txt` | Week 3 扩展 | Python 不止处理 csv |
| `02_.../02_Setting_up_Coding_Environment.txt` | Week 3 | 环境配置参考 |
| `02_.../03_Explaining_the_libraries_for_the_course.txt` | Week 3 | 库认知 |
| `02_.../04_Advance_File_Formats_...txt` | Week 5 | 文件格式多样性 |
| `09_R_for_Bioinformatics/01_..._Intersection_of_Biology.txt` | Week 4 | R 在生信中的角色 |
| `09_R_for_Bioinformatics/02_Getting_Started_with_R_...txt` | Week 4 | R 安装 / 变量 |
| `09_R_for_Bioinformatics/04_Differential_Gene_Expression_..._DESeq2_Preparing_Data.txt` | Week 11 | DESeq2 输入数据 |
| `09_R_for_Bioinformatics/05_Deseq2_Code_Understanding.txt` | Week 11 | DESeq2 代码逐行讲 |
| `09_R_for_Bioinformatics/07_Visualizing_..._ggplot2.txt` | Week 7 / Week 11 | ggplot2 入门 / volcano |
| `09_R_for_Bioinformatics/08_Introduction_to_Single-Cell_RNA_Sequencing.txt` | Week 14 | scRNA-seq 概览 |
| `10_Microarray_..._on_R/02_Introduction_of_Microarray.txt` | Week 15 | microarray 概念 |
| `10_..._/05_Microarray_Analysis_Using_GEO2R.txt` | Week 15 | GEO2R 实操 |

更多映射在后续 ingest 中补充到本表。

## 注意

- **AIDD 字幕需要术语校正**，见 [TERMS.md](../../raw/AIDD_Bioinformatics/TERMS.md)。
- 引用 AIDD 字幕段落作为讲稿时，**先在 [doc/AIDD_Bioinformatics_课程结构与内容整理.md] 里找节摘要**，
  再回到 txt 校对。

## 相关页面

- 来源：[AIDD 课程](../sources/AIDD_Bioinformatics_Course.md) · [AIDD 课程结构整理](../sources/AIDD课程结构整理.md) · [36 课时讲稿](../sources/36课时讲稿.md)
- 课程主页：[课程主页_36课时](../topics/课程主页_36课时.md)
