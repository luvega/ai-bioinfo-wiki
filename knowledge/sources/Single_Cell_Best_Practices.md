---
type: source
title: Single-cell best practices
authors: [Lukas Heumos, Anna Schaar, single-cell best practices consortium]
year: 2026
raw_path:
  - materials/raw/sc_best_practices/upstream/
  - materials/markdown/sc_best_practices/scbp.course_index.md
  - materials/markdown/sc_best_practices/analysis_project/
ingested: 2026-06-04
language: en
kind: online-book
license: Apache-2.0
status: generated_draft
tags: [single-cell, scRNA-seq, scanpy, anndata, multimodal, course-material]
---

# Single-cell best practices

## 一句话定位

**本课程 Week 13-16 的单细胞与多组学高级素材源**：提供 scRNA-seq 质控、标准化、特征选择、降维、聚类、注释、整合、差异表达、GSEA、trajectory、空间组学和免疫受体分析的 Jupyter Book 章节、notebook 代码、发布输出和数据入口。

## 来源与固定版本

- Upstream repository: [theislab/single-cell-best-practices](https://github.com/theislab/single-cell-best-practices)
- Online book: [sc-best-practices.org](https://www.sc-best-practices.org/preamble.html)
- Fixed commit: `735f26fd270b3beceb4ba79f4a556c912192fe83`
- License: Apache License 2.0

## 本地素材位置

- Upstream raw bundle: `materials/raw/sc_best_practices/upstream/`
- Course index: [scbp.course_index](../../materials/markdown/sc_best_practices/scbp.course_index.md)
- Runnable analysis project: [analysis_project/README](../../materials/markdown/sc_best_practices/analysis_project/README.md)
- Extracted notebook outputs: [extracted_outputs/outputs_index](../../materials/markdown/sc_best_practices/extracted_outputs/outputs_index.md)
- Dataset download report: [dataset_download_report](../../materials/markdown/sc_best_practices/analysis_project/dataset_download_report.md)

## 课程使用边界

- Week 13：只取 PCA、UMAP、clustering 和 heatmap 的图形解释与参数敏感性，不默认学生能完整运行 Scanpy 流程。
- Week 14：用于解释 scRNA-seq 数据结构、AnnData、raw data processing 和 count matrix 来源。
- Week 15：用于补充 single-cell differential expression、composition analysis、GSEA/pathway 的证据边界。
- Week 16：用于单细胞图形解读、QC、normalization、feature selection、annotation、integration 和 trajectory。

## 注意事项

- `knowledge/` 只做备课辅助；课程事实主线仍以 `course/syllabus/` 与 `course/weeks/` 为准。
- notebook 发布输出可以作为课堂图形候选，但正式进 PPT 前需核对数据来源、图注、许可证和统计解释。
- 数据下载清单包含 manual/blocked 项；LaminDB、Zenodo、10x 页面和过期签名 URL 不应被静默当成已下载数据。
