---
type: entity
name: R
category: language
domain: [statistics, bioinformatics, visualization]
status: stable
tags: [language, r, statistics, ggplot2, deseq2]
---

# R

## 定位

统计与生信主导语言。本课程的**第二语言**（第 4 周开始），
在第 11、14、15 周成为主导工具（差异表达、scRNA-seq、Microarray）。

## 在本课程中的使用范围

| 周 | 用 R 干什么 |
|---:|---|
| 4 | 入门（向量、矩阵、数据框、因子）+ Python 数据结构对应 |
| 8-10 | 经典统计（`lm`、`glm`、`anova`、`chisq.test`） |
| 11 | 差异表达分析（[DESeq2](DESeq2.md)） |
| 12 | 高维可视化（[ggplot2](ggplot2.md)、`pheatmap`、`prcomp`） |
| 14 | 单细胞 RNA-seq 简介（Seurat） |
| 15 | Microarray / GEO2R |

## 关键包

| 包 | 用途 | 引入周次 |
|---|---|---:|
| `tidyverse`（dplyr/tidyr/readr） | 数据整形 | 4 |
| [ggplot2](ggplot2.md) | 可视化 | 7 / 11 / 12 |
| [DESeq2](DESeq2.md) | 差异表达 | 11 |
| `pheatmap` / `ComplexHeatmap` | 热图 | 12 |
| `AnnotationDbi` / `org.Hs.eg.db` | 基因 ID 转换 | 11-12 |
| `Seurat` | scRNA-seq | 14 |
| `GEOquery` / `limma` | Microarray | 15 |

## 在 AIDD 中

- AIDD Ch.9（R for Bioinformatics）：DESeq2、ggplot2、scRNA-seq 入门。
- AIDD Ch.10（Microarray Analysis on R）：GEO2R + R 微阵列分析。
- 这两章与本课程**重叠最多**，可作直接教学素材。

## 与 [ISLR](../sources/ISLR.md) 的关系

- ISLR Ch.2-3 是经典 R 数据框 + 回归教学。
- ISLR Lab 与 AIDD R 章节风格相似，可在第 4、9-10 周对照使用。

## 与 AI 协作

- AI 给 R 代码的常见错误：
  - 把分类变量当连续变量
  - 数据框列名拼错（特别是含空格或中文）
  - 老用 `aggregate()`，不推荐用现代 `dplyr` 风格
  - tidyverse vs base R 风格混杂
- 解决：在 prompt 中明确"请用 tidyverse 风格"或"请用 base R"。

## 安装建议

- R 主程序：[CRAN](https://cran.r-project.org/)
- IDE：RStudio（教学统一）
- 包管理：`install.packages()` + Bioconductor `BiocManager::install()`
- 复现：`renv` 锁定包版本（项目级）

## 相关页面

- 概念：[工具分工_Python_R_Bash](../concepts/工具分工_Python_R_Bash.md) · [差异表达分析](../concepts/差异表达分析.md)
- 实体：[Python](Python.md) · [Bash](Bash.md) · [DESeq2](DESeq2.md) · [ggplot2](ggplot2.md)
- 来源：[ISLR](../sources/ISLR.md) · [AIDD Ch.9, Ch.10](../sources/AIDD_Bioinformatics_Course.md)
