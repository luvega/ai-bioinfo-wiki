---
type: source
title: Orchestrating Single-Cell Analysis with Bioconductor
authors: [Aaron Lun, Davide Risso, Stephanie Hicks, Dario Righelli]
year: 2026
raw_path:
  - materials/raw/bioconductor_books/archives/
  - materials/raw/bioconductor_books/extracted/
  - materials/raw/bioconductor_books/github/OSCA-source/
  - materials/markdown/bioconductor_books/OSCA/
ingested: 2026-06-04
language: en
kind: online-book-family
license: CC BY 4.0
status: ingesting
tags: [bioconductor, single-cell, r, osca, workflow, week-14, week-15, week-16, week-17]
---

# OSCA · Orchestrating Single-Cell Analysis with Bioconductor

## 一句话定位

**单细胞分析课程案例库**，服务 Week 14-17 的表达矩阵、质控、归一化、降维聚类、差异表达、多样本整合和 workflow 案例拓展。

## 当前入库边界

- Release 站点：`https://bioconductor.org/books/release/OSCA/`
- Bioconductor 版本：3.23
- Landing 页版本：`OSCA 1.22.0`，Compiled `2026-04-29`
- 主要子书：`OSCA.intro`、`OSCA.basic`、`OSCA.multisample`、`OSCA.workflows`
- 补充来源：`https://github.com/OSCA-source`
- 已知例外：`OSCA.advanced` release 链接当前不可用，使用 `OSCA-source/OSCA.advanced` 作为补充来源，并在 manifest 标记。

## 课程用法

- Week 14：把 `SingleCellExperiment`、counts、metadata 和 QC 指标作为表达矩阵入门案例。
- Week 15：把 marker testing、差异表达和多重检验作为 RNA-seq/单细胞统计扩展。
- Week 16：把 PCA、UMAP、聚类和可视化作为高维表达矩阵教学素材。
- Week 17：把 `OSCA.workflows` 和 `OSCA-source` 代码结构作为端到端案例库，不自动提升周次状态。

## 待核验点

- GitHub 源码结构用于后续案例拓展；本轮不运行完整 Bioconductor 工作流。
- 代码片段进入课堂前需确认依赖包版本、数据下载大小和运行时间。
- 若 release 站点与 `course/syllabus/` 的教学主线冲突，以 `course/syllabus/` 为准。
