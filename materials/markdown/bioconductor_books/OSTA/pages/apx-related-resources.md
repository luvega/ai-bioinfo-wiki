---
source: OSTA
title: "Appendix B — Related resources"
original_url: https://bioconductor.org/books/release/OSTA/pages/apx-related-resources.html
ingested_at: 2026-06-04T01:51:36+00:00
status: source_ingested
---

# Appendix B — Related resources

## B.1 Introduction

This chapter provides links to several related resources from the Bioconductor and other communities.

## B.2 Data preprocessing procedures

* [**Visium data preprocessing**](https://lmweber.org/Visium-data-preprocessing/): Online book containing details on data preprocessing procedures for spatial transcriptomics data from the 10x Genomics Visium platform (using tools outside R and Bioconductor).

## B.3 Resources for other spatial omics platforms

Workflows and other resources for data from other spatial omics platforms:

* [**Analysis workflow for IMC data**](https://bodenmillergroup.github.io/IMCDataAnalysis/): Online book providing a workflow highlighting the use of R/Bioconductor packages to analyze single-cell data obtained from segmented imaging mass cytometry (IMC) images. Examples focus on IMC data and can also be applied to images obtained by other highly-multiplexed imaging technologies, e.g. CODEX, MIBI, and mIF.
* [**VectraPolarisData**](https://bioconductor.org/packages/VectraPolarisData): Bioconductor data package providing multiplex single-cell imaging datasets collected on Vectra Polaris and Vectra 3 instruments.

## B.4 Data structures

Data structures for storing data from spatial transcriptomics and other spatial omics platforms outside R/Bioconductor:

* [**AnnData**](https://anndata.readthedocs.io/en/latest/): Python class for storing single-cell and spatial data in the [scverse](https://scverse.org/) framework.
* [**Giotto classes**](https://drieslab.github.io/Giotto_website/articles/structure.html): R classes used to store spatial omics data within the [Giotto Suite](https://drieslab.github.io/Giotto_website/index.html) framework ([Chen et al. 2025](https://bioconductor.org/books/release/OSTA/pages/apx-related-resources.html#ref-Chen2025-Giotto-Suite); [Dries et al. 2021](https://bioconductor.org/books/release/OSTA/pages/apx-related-resources.html#ref-Dries2021-Giotto)).
* [**SpatialData**](https://spatialdata.scverse.org/en/latest/): Python class for storing data from spatial transcriptomics and other spatial omics platforms.

## B.5 Statistical concepts

* [**Modern Statistics for Modern Biology**](https://www.huber.embl.de//msmb/index.html): Online textbook on concepts in modern statistics for high-throughput and high-dimensional biology. This book includes a detailed chapter on [image data and spatial statistics](https://www.huber.embl.de//msmb/Chap-Images.html).
* [**Harnessing the Potential of Spatial Statistics for Spatial Omics Data with `pasta`**](https://robinsonlabuzh.github.io/pasta): Online resource describing concepts from spatial statistics that apply to spatial -omics datasets. This online resource also has a preprint published at [arXiv:2412.01561](https://arxiv.org/abs/2412.01561).

## References

Chen, Jiaji G, Joselyn C Chávez-Fuentes, Matthew O’Brien, Junxiang Xu, Edward C Ruiz, Wen Wang, Iqra Amin, et al. 2025. “Giotto Suite: A Multiscale and Technology-Agnostic Spatial Multiomics Analysis Ecosystem.” *Nature Methods*, 1–13. <https://doi.org/10.1038/s41592-025-02817-w>.

Dries, Ruben, Qian Zhu, Rui Dong, Chee-Huat Linus Eng, Huipeng Li, Kan Liu, Yuntian Fu, et al. 2021. “Giotto: A Toolbox for Integrative Analysis and Visualization of Spatial Expression Data.” *Genome Biology* 22 (78). <https://doi.org/10.1186/s13059-021-02286-2>.

Back to top
