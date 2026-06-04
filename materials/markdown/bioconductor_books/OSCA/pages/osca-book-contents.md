---
source: OSCA
title: "Orchestrating Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/release/OSCA/book-contents.html
ingested_at: 2026-06-04T01:51:50+00:00
status: source_ingested
---

# [Orchestrating Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/release/OSCA/)

# Book contents

The OSCA book is actually a collection of several sub-books spanning a variety of topics and different levels of assumed reader knowledge.
Each sub-book is generated using *[bookdown](https://CRAN.R-project.org/package=bookdown)*, compiled twice a week to ensure that the examples still run on the current R/Bioconductor code base.
Interlinking between related topics enable readers to seamlessly transition within a sub-book, and even between different sub-books.
To get started, click on the links below to navigate to each sub-book.

## [Introduction](http://bioconductor.org/books/3.23/OSCA.intro)

This describes how to install R and Bioconductor packages, links out to some resources to learn R,
describes how to load datasets into an R session, provides an overview of the `SingleCellExperiment` class,
and performs a “quick start” demonstration for basic single-cell RNA-seq analyses. It is intended for
readers with little-to-no computational background who are just getting started with analyses in R.

## [Basics](http://bioconductor.org/books/3.23/OSCA.basic)

This describes the steps of a simple single-cell RNA-seq analysis, involving quality control,
normalization, various forms of dimensionality reduction, clustering into subpopulations,
detection of marker genes, and annotation of cell types. It is intended for users who already
have some familiarity with R and want to get hands-on with some basic single-cell analyses.

## [Advanced](http://bioconductor.org/books/3.23/OSCA.advanced)

This describes the more complex steps of a single-cell RNA-seq analysis ranging from doublet detection, cell cycle assignment,
specific steps for processing droplet data, nuclei-specific analyses, trajectory analyses, integrated analyses with protein abundances, and interactive visualization. It also elaborates on some of the basic analysis steps, focusing on alternative strategies and theoretical considerations. It is intended for readers who are already familiar with basic single-cell analyses, possibly after reading some of the prior books in this collection.

## [Multi-sample](http://bioconductor.org/books/3.23/OSCA.multisample)

This describes the handling of multiple samples in a single-cell RNA-seq analysis,
starting with integration of multiple datasets into a common space for consistent analyses,
differential expression comparisons between conditions based on pseudo-bulk samples,
and differential abundance analyses for cell subpopulations. It is intended for readers who are already familiar with basic single-cell analyses, possibly after reading some of the prior books in this collection.

## [Workflows](http://bioconductor.org/books/3.23/OSCA.workflows)

This contains worked case studies of analyses of a variety of single-cell datasets, each proceeding from a `SingleCellExperiment` object. Exposition is generally minimal other than for dataset-specific justifications for parameter tweaks;
refer to the other books in the OCSA collection for a detailed explanation of the theoretical basis of each step. It is intended for readers who already know the background and just want some code to copy and paste into their own analyses.
