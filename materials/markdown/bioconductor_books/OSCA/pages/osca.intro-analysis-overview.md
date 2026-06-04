---
source: OSCA
title: "Introduction to Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.intro/analysis-overview.html
ingested_at: 2026-06-04T01:52:39+00:00
status: source_ingested
---

# [Introduction to Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/3.23/OSCA.intro/)

# Chapter 5 Analysis overview

## 5.1 Outline

This chapter provides an overview of the framework of a typical scRNA-seq analysis workflow (Figure [5.1](https://bioconductor.org/books/3.23/OSCA.intro/analysis-overview.html#fig:scworkflow)).

![Schematic of a typical scRNA-seq analysis workflow. Each stage (separated by dashed lines) consists of a number of specific steps, many of which operate on and modify a `SingleCellExperiment` instance.](../../../../raw/bioconductor_books/assets/OSCA/osca.intro-analysis-overview/workflow.png)

Figure 5.1: Schematic of a typical scRNA-seq analysis workflow. Each stage (separated by dashed lines) consists of a number of specific steps, many of which operate on and modify a `SingleCellExperiment` instance.

In the simplest case, the workflow has the following form:

1. We compute quality control metrics to remove low-quality cells that would interfere with downstream analyses.
   These cells may have been damaged during processing or may not have been fully captured by the sequencing protocol.
   Common metrics includes the total counts per cell, the proportion of spike-in or mitochondrial reads and the number of detected features.
2. We convert the counts into normalized expression values to eliminate cell-specific biases (e.g., in capture efficiency).
   This allows us to perform explicit comparisons across cells in downstream steps like clustering.
   We also apply a transformation, typically log, to adjust for the mean-variance relationship.
3. We perform feature selection to pick a subset of interesting features for downstream analysis.
   This is done by modelling the variance across cells for each gene and retaining genes that are highly variable.
   The aim is to reduce computational overhead and noise from uninteresting genes.
4. We apply dimensionality reduction to compact the data and further reduce noise.
   Principal components analysis is typically used to obtain an initial low-rank representation for more computational work,
   followed by more aggressive methods like \(t\)-stochastic neighbor embedding for visualization purposes.
5. We cluster cells into groups according to similarities in their (normalized) expression profiles.
   This aims to obtain groupings that serve as empirical proxies for distinct biological states.
   We typically interpret these groupings by identifying differentially expressed marker genes between clusters.

Subsequent chapters will describe each analysis step in more detail.

## 5.2 Quick start (simple)

Here, we use the a droplet-based retina dataset from Macosko et al. ([2015](https://bioconductor.org/books/3.23/OSCA.intro/analysis-overview.html#ref-macosko2015highly)), provided in the *[scRNAseq](https://bioconductor.org/packages/3.23/scRNAseq)* package.
This starts from a count matrix and finishes with clusters (Figure [5.2](https://bioconductor.org/books/3.23/OSCA.intro/analysis-overview.html#fig:quick-start-umap)) in preparation for biological interpretation.
Similar workflows are available in abbreviated form in later parts of the book.

```
library(scRNAseq)
sce <- MacoskoRetinaData()

# Quality control (using mitochondrial genes).
library(scater)
is.mito <- grepl("^MT-", rownames(sce))
qcstats <- perCellQCMetrics(sce, subsets=list(Mito=is.mito))
filtered <- quickPerCellQC(qcstats, percent_subsets="subsets_Mito_percent")
sce <- sce[, !filtered$discard]

# Normalization.
sce <- logNormCounts(sce)

# Feature selection.
library(scran)
dec <- modelGeneVar(sce)
hvg <- getTopHVGs(dec, prop=0.1)

# PCA.
library(scater)
set.seed(1234)
sce <- runPCA(sce, ncomponents=25, subset_row=hvg)

# Clustering.
library(bluster)
colLabels(sce) <- clusterCells(sce, use.dimred='PCA',
    BLUSPARAM=NNGraphParam(cluster.fun="louvain"))    

# Visualization.
sce <- runUMAP(sce, dimred = 'PCA')
plotUMAP(sce, colour_by="label")
```

![UMAP plot of the retina dataset, where each point is a cell and is colored by the assigned cluster identity.](../../../../raw/bioconductor_books/assets/OSCA/osca.intro-analysis-overview/quick-start-umap-1.png)

Figure 5.2: UMAP plot of the retina dataset, where each point is a cell and is colored by the assigned cluster identity.

```
# Marker detection.
markers <- findMarkers(sce, test.type="wilcox", direction="up", lfc=1)
```

## 5.3 Quick start (multiple batches)

Here we use the pancreas Smart-seq2 dataset from Segerstolpe et al. ([2016](https://bioconductor.org/books/3.23/OSCA.intro/analysis-overview.html#ref-segerstolpe2016singlecell)), again provided in the *[scRNAseq](https://bioconductor.org/packages/3.23/scRNAseq)* package.
This starts from a count matrix and finishes with clusters (Figure [5.2](https://bioconductor.org/books/3.23/OSCA.intro/analysis-overview.html#fig:quick-start-umap)) with some additional tweaks to eliminate uninteresting batch effects between individuals.
Note that a more elaborate analysis of the same dataset with justifications for each step is available in [Workflow Chapter 8](http://bioconductor.org/books/3.23/OSCA.workflows/segerstolpe-human-pancreas-smart-seq2.html#segerstolpe-human-pancreas-smart-seq2).

```
sce <- SegerstolpePancreasData()

# Quality control (using ERCCs).
qcstats <- perCellQCMetrics(sce)
filtered <- quickPerCellQC(qcstats, percent_subsets="altexps_ERCC_percent")
sce <- sce[, !filtered$discard]

# Normalization.
sce <- logNormCounts(sce)

# Feature selection, blocking on the individual of origin.
dec <- modelGeneVar(sce, block=sce$individual)
hvg <- getTopHVGs(dec, prop=0.1)

# Batch correction.
library(batchelor)
set.seed(1234)
sce <- correctExperiments(sce, batch=sce$individual, 
    subset.row=hvg, correct.all=TRUE)

# Clustering.
colLabels(sce) <- clusterCells(sce, use.dimred='corrected')

# Visualization.
sce <- runUMAP(sce, dimred = 'corrected')
gridExtra::grid.arrange(
    plotUMAP(sce, colour_by="label"),
    plotUMAP(sce, colour_by="individual"),
    ncol=2
)
```

![UMAP plot of the pancreas dataset, where each point is a cell and is colored by the assigned cluster identity (left) or the individual of origin (right).](../../../../raw/bioconductor_books/assets/OSCA/osca.intro-analysis-overview/quick-start2-umap-1.png)

Figure 5.3: UMAP plot of the pancreas dataset, where each point is a cell and is colored by the assigned cluster identity (left) or the individual of origin (right).

```
# Marker detection, blocking on the individual of origin.
markers <- findMarkers(sce, test.type="wilcox", direction="up", lfc=1)
```

## Session Info

View session info

```
R version 4.6.0 RC (2026-04-17 r89917)
Platform: x86_64-pc-linux-gnu
Running under: Ubuntu 24.04.4 LTS

Matrix products: default
BLAS:   /home/biocbuild/bbs-3.23-bioc/R/lib/libRblas.so 
LAPACK: /usr/lib/x86_64-linux-gnu/lapack/liblapack.so.3.12.0  LAPACK version 3.12.0

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_GB              LC_COLLATE=C              
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

time zone: America/New_York
tzcode source: system (glibc)

attached base packages:
[1] stats4    stats     graphics  grDevices utils     datasets  methods  
[8] base     

other attached packages:
 [1] batchelor_1.28.0            bluster_1.22.0             
 [3] scran_1.40.0                scater_1.40.0              
 [5] ggplot2_4.0.3               scuttle_1.22.0             
 [7] scRNAseq_2.25.0             SingleCellExperiment_1.34.0
 [9] SummarizedExperiment_1.42.0 Biobase_2.72.0             
[11] GenomicRanges_1.64.0        Seqinfo_1.2.0              
[13] IRanges_2.46.0              S4Vectors_0.50.0           
[15] BiocGenerics_0.58.0         generics_0.1.4             
[17] MatrixGenerics_1.24.0       matrixStats_1.5.0          
[19] BiocStyle_2.40.0            rebook_1.22.0              

loaded via a namespace (and not attached):
  [1] RColorBrewer_1.1-3        jsonlite_2.0.0           
  [3] CodeDepends_0.6.7         magrittr_2.0.5           
  [5] ggbeeswarm_0.7.3          GenomicFeatures_1.64.0   
  [7] gypsum_1.8.0              farver_2.1.2             
  [9] rmarkdown_2.31            BiocIO_1.22.0            
 [11] vctrs_0.7.3               DelayedMatrixStats_1.34.0
 [13] memoise_2.0.1             Rsamtools_2.28.0         
 [15] RCurl_1.98-1.18           htmltools_0.5.9          
 [17] S4Arrays_1.12.0           AnnotationHub_4.2.0      
 [19] curl_7.1.0                BiocNeighbors_2.6.0      
 [21] Rhdf5lib_2.0.0            SparseArray_1.12.0       
 [23] rhdf5_2.56.0              sass_0.4.10              
 [25] alabaster.base_1.12.0     bslib_0.10.0             
 [27] alabaster.sce_1.12.0      httr2_1.2.2              
 [29] cachem_1.1.0              ResidualMatrix_1.22.0    
 [31] GenomicAlignments_1.48.0  igraph_2.3.0             
 [33] lifecycle_1.0.5           pkgconfig_2.0.3          
 [35] rsvd_1.0.5                Matrix_1.7-5             
 [37] R6_2.6.1                  fastmap_1.2.0            
 [39] digest_0.6.39             AnnotationDbi_1.74.0     
 [41] RSpectra_0.16-2           dqrng_0.4.1              
 [43] irlba_2.3.7               ExperimentHub_3.2.0      
 [45] RSQLite_2.4.6             beachmat_2.28.0          
 [47] labeling_0.4.3            filelock_1.0.3           
 [49] httr_1.4.8                abind_1.4-8              
 [51] compiler_4.6.0            bit64_4.8.0              
 [53] withr_3.0.2               S7_0.2.2                 
 [55] BiocParallel_1.46.0       viridis_0.6.5            
 [57] DBI_1.3.0                 HDF5Array_1.40.0         
 [59] alabaster.ranges_1.12.0   alabaster.schemas_1.12.0 
 [61] rappdirs_0.3.4            DelayedArray_0.38.0      
 [63] rjson_0.2.23              tools_4.6.0              
 [65] vipor_0.4.7               otel_0.2.0               
 [67] beeswarm_0.4.0            glue_1.8.1               
 [69] h5mread_1.4.0             restfulr_0.0.16          
 [71] rhdf5filters_1.24.0       grid_4.6.0               
 [73] cluster_2.1.8.2           gtable_0.3.6             
 [75] ensembldb_2.36.0          metapod_1.20.0           
 [77] BiocSingular_1.28.0       ScaledMatrix_1.20.0      
 [79] XVector_0.52.0            RcppAnnoy_0.0.23         
 [81] ggrepel_0.9.8             BiocVersion_3.23.1       
 [83] pillar_1.11.1             limma_3.68.0             
 [85] dplyr_1.2.1               BiocFileCache_3.2.0      
 [87] lattice_0.22-9            FNN_1.1.4.1              
 [89] rtracklayer_1.72.0        bit_4.6.0                
 [91] tidyselect_1.2.1          locfit_1.5-9.12          
 [93] Biostrings_2.80.0         knitr_1.51               
 [95] gridExtra_2.3             bookdown_0.46            
 [97] ProtGenerics_1.44.0       edgeR_4.10.0             
 [99] xfun_0.57                 statmod_1.5.1            
[101] UCSC.utils_1.8.0          lazyeval_0.2.3           
[103] yaml_2.3.12               evaluate_1.0.5           
[105] codetools_0.2-20          cigarillo_1.2.0          
[107] tibble_3.3.1              alabaster.matrix_1.12.0  
[109] BiocManager_1.30.27       graph_1.90.0             
[111] cli_3.6.6                 uwot_0.2.4               
[113] jquerylib_0.1.4           dichromat_2.0-0.1        
[115] Rcpp_1.1.1-1.1            GenomeInfoDb_1.48.0      
[117] dir.expiry_1.20.0         dbplyr_2.5.2             
[119] png_0.1-9                 XML_3.99-0.23            
[121] parallel_4.6.0            blob_1.3.0               
[123] AnnotationFilter_1.36.0   sparseMatrixStats_1.24.0 
[125] bitops_1.0-9              viridisLite_0.4.3        
[127] alabaster.se_1.12.0       scales_1.4.0             
[129] crayon_1.5.3              rlang_1.2.0              
[131] cowplot_1.2.0             KEGGREST_1.52.0
```

Islam, S., A. Zeisel, S. Joost, G. La Manno, P. Zajac, M. Kasper, P. Lonnerberg, and S. Linnarsson. 2014. “Quantitative single-cell RNA-seq with unique molecular identifiers.” *Nat. Methods* 11 (2): 163–66.

Lun, A. T. L., F. J. Calero-Nieto, L. Haim-Vilmovsky, B. Gottgens, and J. C. Marioni. 2017. “Assessing the reliability of spike-in normalization for analyses of single-cell RNA sequencing data.” *Genome Res.* 27 (11): 1795–1806.

Macosko, E. Z., A. Basu, R. Satija, J. Nemesh, K. Shekhar, M. Goldman, I. Tirosh, et al. 2015. “Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets.” *Cell* 161 (5): 1202–14.

Mereu, Elisabetta, Atefeh Lafzi, Catia Moutinho, Christoph Ziegenhain, Davis J. MacCarthy, Adrian Alvarez, Eduard Batlle, et al. 2019. “Benchmarking Single-Cell Rna Sequencing Protocols for Cell Atlas Projects.” *bioRxiv*. <https://doi.org/10.1101/630087>.

Muraro, M. J., G. Dharmadhikari, D. Grun, N. Groen, T. Dielen, E. Jansen, L. van Gurp, et al. 2016. “A Single-Cell Transcriptome Atlas of the Human Pancreas.” *Cell Syst* 3 (4): 385–94.

Segerstolpe, A., A. Palasantza, P. Eliasson, E. M. Andersson, A. C. Andreasson, X. Sun, S. Picelli, et al. 2016. “Single-Cell Transcriptome Profiling of Human Pancreatic Islets in Health and Type 2 Diabetes.” *Cell Metab.* 24 (4): 593–607.

Srivastava, A., L. Malik, T. Smith, I. Sudbery, and R. Patro. 2019. “Alevin efficiently estimates accurate gene abundances from dscRNA-seq data.” *Genome Biol* 20 (1): 65.

Svensson, V., E. da Veiga Beltrame, and L. Pachter. 2019. “Quantifying the Tradeoff Between Sequencing Depth and Cell Number in Single-Cell Rna-Seq.” *bioRxiv*, 762773.

Wilson, N. K., D. G. Kent, F. Buettner, M. Shehata, I. C. Macaulay, F. J. Calero-Nieto, M. Sanchez Castillo, et al. 2015. “Combined single-cell functional and gene expression analysis resolves heterogeneity within stem cell populations.” *Cell Stem Cell* 16 (6): 712–24.

Zhang, M. J., V. Ntranos, and D. Tse. 2020. “Determining sequencing depth in a single-cell RNA-seq experiment.” *Nat Commun* 11 (1): 774.

Zheng, G. X., J. M. Terry, P. Belgrader, P. Ryvkin, Z. W. Bent, R. Wilson, S. B. Ziraldo, et al. 2017. “Massively parallel digital transcriptional profiling of single cells.” *Nat Commun* 8 (January): 14049.

Ziegenhain, C., B. Vieth, S. Parekh, B. Reinius, A. Guillaumet-Adkins, M. Smets, H. Leonhardt, H. Heyn, I. Hellmann, and W. Enard. 2017. “Comparative Analysis of Single-Cell RNA Sequencing Methods.” *Mol. Cell* 65 (4): 631–43.

### References

Macosko, E. Z., A. Basu, R. Satija, J. Nemesh, K. Shekhar, M. Goldman, I. Tirosh, et al. 2015. “Highly parallel genome-wide expression profiling of individual cells using nanoliter droplets.” *Cell* 161 (5): 1202–14.

Segerstolpe, A., A. Palasantza, P. Eliasson, E. M. Andersson, A. C. Andreasson, X. Sun, S. Picelli, et al. 2016. “Single-Cell Transcriptome Profiling of Human Pancreatic Islets in Health and Type 2 Diabetes.” *Cell Metab.* 24 (4): 593–607.
