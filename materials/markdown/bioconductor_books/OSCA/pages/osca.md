---
source: OSCA
title: "Orchestrating Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/release/OSCA/index.html
ingested_at: 2026-06-04T01:52:47+00:00
status: source_ingested
---

# [Orchestrating Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/release/OSCA/)

# Orchestrating Single-Cell Analysis with Bioconductor

***Authors:** Robert Amezquita [aut], Aaron Lun [aut], Stephanie Hicks [aut], Raphael Gottardo [aut], Alan O’Callaghan [cre]  
 **Version:** 1.22.0  
 **Modified:** 2022-09-05  
 **Compiled:** 2026-04-29  
 **Environment:** R version 4.6.0 RC (2026-04-17 r89917), Bioconductor 3.23  
 **License:** CC BY 4.0  
 **Copyright:** Bioconductor, 2020  
 **Source:** <https://github.com/OSCA-source/OSCA>*

# Welcome

[![Bioconductor Sticker](../../../../raw/bioconductor_books/assets/OSCA/osca/Bioconductor-serial.gif)](https://bioconductor.org)

This is the landing page for the **“Orchestrating Single-Cell Analysis with Bioconductor”** book,
which teaches users some common workflows for the analysis of single-cell RNA-seq data (scRNA-seq).
This book will show you how to make use of cutting-edge Bioconductor tools to process, analyze, visualize, and explore scRNA-seq data.
Additionally, it serves as an online companion for the [paper of the same name](https://dx.doi.org/10.1038/s41592-019-0654-x).

## What you will learn

The goal of this book is to provide a solid foundation in the usage of Bioconductor tools for single-cell RNA-seq analysis by walking through various steps of typical workflows using example datasets.
We strive to tackle key concepts covered in the manuscript, **“Orchestrating Single-Cell Analysis with Bioconductor”**, with each workflow covering these in varying detail, as well as essential preliminaries that are important for following along with the workflows on your own.

## What you won’t learn

The field of bioinformatic analysis is large and filled with many potential trajectories depending on the biological system being studied and technology being deployed. Here, we only briefly survey some of the many tools available for the analysis of scRNA-seq, focusing on Bioconductor packages. It is impossible to thoroughly review the plethora of tools available through R and Bioconductor for biological analysis in one book, but we hope to provide the means for further exploration on your own.

Thus, it goes without saying that you may not learn the optimal workflow for your own data from our examples - while we strive to provide high quality templates, they should be treated as just that - a template from which to extend upon for your own analyses.

## Who we wrote this for

We’ve written this book with the interested experimental biologist in mind, and do our best to make few assumptions on previous programming or statistical experience. Likewise, we also welcome more seasoned bioinformaticians who are looking for a starting point from which to dive into single-cell RNA-seq analysis. As such, we welcome any and all feedback for improving this book to help increase accessibility and refine technical details.

## Why we wrote this

This book was conceived in the fall of 2018, as single-cell RNA-seq analysis continued its rise in prominence in the field of biology. With its rapid growth, and the ongoing developments within Bioconductor tailored specifically for scRNA-seq, it became apparent that an update to the [Orchestrating high-throughput genomic analysis with Bioconductor](https://www.nature.com/articles/nmeth.3252) paper was necessary for the age of single-cell studies.

We strive to highlight the fantastic software by people who call Bioconductor home for their tools, and in the process hope to showcase the Bioconductor community at large in continually pushing forward the field of biological analysis.
