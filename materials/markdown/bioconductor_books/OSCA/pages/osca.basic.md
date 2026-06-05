---
source: OSCA
title: "Basics of Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.basic/index.html
ingested_at: 2026-06-04T01:52:21+00:00
status: source_ingested
---

# [Basics of Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/3.23/OSCA.basic/)

# Basics of Single-Cell Analysis with Bioconductor

***Authors:** Robert Amezquita [aut], Aaron Lun [aut], Stephanie Hicks [aut], Raphael Gottardo [aut], Peter Hickey [cre]  
 **Version:** 1.20.0  
 **Modified:** 2025-09-29  
 **Compiled:** 2026-04-29  
 **Environment:** R version 4.6.0 RC (2026-04-17 r89917), Bioconductor 3.23  
 **License:** CC BY 4.0  
 **Copyright:** Bioconductor, 2026  
 **Source:** <https://github.com/OSCA-source/OSCA.basic>*

# Welcome

[![Bioconductor Sticker](https://github.com/Bioconductor/BiocStickers/raw/master/Bioconductor/Bioconductor-serial.gif)](https://bioconductor.org)

This site contains the basic analysis chapters for the [**“Orchestrating Single-Cell Analysis with Bioconductor”** book](http://bioconductor.org/books/3.23/OSCA).
This describes the steps of a simple single-cell RNA-seq analysis, involving quality control,
normalization, various forms of dimensionality reduction, clustering into subpopulations,
detection of marker genes, and annotation of cell types. It is intended for users who already
have some familiarity with R and want to get hands-on with some basic single-cell analyses.
