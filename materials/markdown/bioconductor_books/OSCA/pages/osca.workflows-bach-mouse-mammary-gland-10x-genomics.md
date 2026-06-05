---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/bach-mouse-mammary-gland-10x-genomics.html
ingested_at: 2026-06-04T01:52:12+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 12 Bach mouse mammary gland (10X Genomics)

## 12.1 Introduction

This performs an analysis of the Bach et al. ([2017](https://bioconductor.org/books/3.23/OSCA.workflows/bach-mouse-mammary-gland-10x-genomics.html#ref-bach2017differentiation)) 10X Genomics dataset,
from which we will consider a single sample of epithelial cells from the mouse mammary gland during gestation.

## 12.2 Data loading

```
library(scRNAseq)
sce.mam <- BachMammaryData(samples="G_1")
```

```
library(scater)
rownames(sce.mam) <- uniquifyFeatureNames(
    rowData(sce.mam)$Ensembl, rowData(sce.mam)$Symbol)

library(AnnotationHub)
ens.mm.v97 <- AnnotationHub()[["AH73905"]]
rowData(sce.mam)$SEQNAME <- mapIds(ens.mm.v97, keys=rowData(sce.mam)$Ensembl,
    keytype="GENEID", column="SEQNAME")
```

## 12.3 Quality control

```
unfiltered <- sce.mam
```

```
is.mito <- rowData(sce.mam)$SEQNAME == "MT"
stats <- perCellQCMetrics(sce.mam, subsets=list(Mito=which(is.mito)))
qc <- quickPerCellQC(stats, percent_subsets="subsets_Mito_percent")
sce.mam <- sce.mam[,!qc$discard]
```

```
colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$discard <- qc$discard

gridExtra::grid.arrange(
    plotColData(unfiltered, y="sum", colour_by="discard") + 
        scale_y_log10() + ggtitle("Total count"),
    plotColData(unfiltered, y="detected", colour_by="discard") + 
        scale_y_log10() + ggtitle("Detected features"),
    plotColData(unfiltered, y="subsets_Mito_percent", 
        colour_by="discard") + ggtitle("Mito percent"),
    ncol=2
)
```

![Distribution of each QC metric across cells in the Bach mammary gland dataset. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-bach-mouse-mammary-gland-10x-genomics/unref-bach-qc-dist-1.png)

Figure 12.1: Distribution of each QC metric across cells in the Bach mammary gland dataset. Each point represents a cell and is colored according to whether that cell was discarded.

```
plotColData(unfiltered, x="sum", y="subsets_Mito_percent", 
    colour_by="discard") + scale_x_log10()
```

![Percentage of mitochondrial reads in each cell in the Bach mammary gland dataset compared to its total count. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-bach-mouse-mammary-gland-10x-genomics/unref-bach-qc-comp-1.png)

Figure 12.2: Percentage of mitochondrial reads in each cell in the Bach mammary gland dataset compared to its total count. Each point represents a cell and is colored according to whether that cell was discarded.

```
colSums(as.matrix(qc))
```

```
##              low_lib_size            low_n_features high_subsets_Mito_percent 
##                         0                         0                       143 
##                   discard 
##                       143
```

## 12.4 Normalization

```
library(scran)
set.seed(101000110)
clusters <- quickCluster(sce.mam)
sce.mam <- computeSumFactors(sce.mam, clusters=clusters)
sce.mam <- logNormCounts(sce.mam)
```

```
summary(sizeFactors(sce.mam))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.264   0.520   0.752   1.000   1.207  10.790
```

```
plot(librarySizeFactors(sce.mam), sizeFactors(sce.mam), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the Bach mammary gland dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-bach-mouse-mammary-gland-10x-genomics/unref-bach-norm-1.png)

Figure 12.3: Relationship between the library size factors and the deconvolution size factors in the Bach mammary gland dataset.

## 12.5 Variance modelling

We use a Poisson-based technical trend to capture more genuine biological variation in the biological component.

```
set.seed(00010101)
dec.mam <- modelGeneVarByPoisson(sce.mam)
top.mam <- getTopHVGs(dec.mam, prop=0.1)
```

```
plot(dec.mam$mean, dec.mam$total, pch=16, cex=0.5,
    xlab="Mean of log-expression", ylab="Variance of log-expression")
curfit <- metadata(dec.mam)
curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
```

![Per-gene variance as a function of the mean for the log-expression values in the Bach mammary gland dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to simulated Poisson counts.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-bach-mouse-mammary-gland-10x-genomics/unref-bach-var-1.png)

Figure 12.4: Per-gene variance as a function of the mean for the log-expression values in the Bach mammary gland dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to simulated Poisson counts.

## 12.6 Dimensionality reduction

```
library(BiocSingular)
set.seed(101010011)
sce.mam <- denoisePCA(sce.mam, technical=dec.mam, subset.row=top.mam)
sce.mam <- runTSNE(sce.mam, dimred="PCA")
```

```
ncol(reducedDim(sce.mam, "PCA"))
```

```
## [1] 15
```

## 12.7 Clustering

We use a higher `k` to obtain coarser clusters (for use in `doubletCluster()` later).

```
snn.gr <- buildSNNGraph(sce.mam, use.dimred="PCA", k=25)
colLabels(sce.mam) <- factor(igraph::cluster_walktrap(snn.gr)$membership)
```

```
table(colLabels(sce.mam))
```

```
## 
##   1   2   3   4   5   6   7   8   9  10 
## 550 847 639 477  54  88  39  22  32  24
```

```
plotTSNE(sce.mam, colour_by="label")
```

![Obligatory $t$-SNE plot of the Bach mammary gland dataset, where each point represents a cell and is colored according to the assigned cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-bach-mouse-mammary-gland-10x-genomics/unref-bach-tsne-1.png)

Figure 12.5: Obligatory \(t\)-SNE plot of the Bach mammary gland dataset, where each point represents a cell and is colored according to the assigned cluster.

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
 [1] BiocSingular_1.28.0         scran_1.40.0               
 [3] AnnotationHub_4.2.0         BiocFileCache_3.2.0        
 [5] dbplyr_2.5.2                scater_1.40.0              
 [7] ggplot2_4.0.3               scuttle_1.22.0             
 [9] ensembldb_2.36.0            AnnotationFilter_1.36.0    
[11] GenomicFeatures_1.64.0      AnnotationDbi_1.74.0       
[13] scRNAseq_2.25.0             SingleCellExperiment_1.34.0
[15] SummarizedExperiment_1.42.0 Biobase_2.72.0             
[17] GenomicRanges_1.64.0        Seqinfo_1.2.0              
[19] IRanges_2.46.0              S4Vectors_0.50.0           
[21] BiocGenerics_0.58.0         generics_0.1.4             
[23] MatrixGenerics_1.24.0       matrixStats_1.5.0          
[25] BiocStyle_2.40.0            rebook_1.22.0              

loaded via a namespace (and not attached):
  [1] RColorBrewer_1.1-3       jsonlite_2.0.0           CodeDepends_0.6.7       
  [4] magrittr_2.0.5           ggbeeswarm_0.7.3         gypsum_1.8.0            
  [7] farver_2.1.2             rmarkdown_2.31           BiocIO_1.22.0           
 [10] vctrs_0.7.3              memoise_2.0.1            Rsamtools_2.28.0        
 [13] RCurl_1.98-1.18          htmltools_0.5.9          S4Arrays_1.12.0         
 [16] curl_7.1.0               BiocNeighbors_2.6.0      Rhdf5lib_2.0.0          
 [19] SparseArray_1.12.0       rhdf5_2.56.0             sass_0.4.10             
 [22] alabaster.base_1.12.0    bslib_0.10.0             alabaster.sce_1.12.0    
 [25] httr2_1.2.2              cachem_1.1.0             GenomicAlignments_1.48.0
 [28] igraph_2.3.0             lifecycle_1.0.5          pkgconfig_2.0.3         
 [31] rsvd_1.0.5               Matrix_1.7-5             R6_2.6.1                
 [34] fastmap_1.2.0            digest_0.6.39            dqrng_0.4.1             
 [37] irlba_2.3.7              ExperimentHub_3.2.0      RSQLite_2.4.6           
 [40] beachmat_2.28.0          labeling_0.4.3           filelock_1.0.3          
 [43] httr_1.4.8               abind_1.4-8              compiler_4.6.0          
 [46] bit64_4.8.0              withr_3.0.2              S7_0.2.2                
 [49] BiocParallel_1.46.0      viridis_0.6.5            DBI_1.3.0               
 [52] HDF5Array_1.40.0         alabaster.ranges_1.12.0  alabaster.schemas_1.12.0
 [55] rappdirs_0.3.4           DelayedArray_0.38.0      bluster_1.22.0          
 [58] rjson_0.2.23             tools_4.6.0              vipor_0.4.7             
 [61] otel_0.2.0               beeswarm_0.4.0           glue_1.8.1              
 [64] h5mread_1.4.0            restfulr_0.0.16          rhdf5filters_1.24.0     
 [67] grid_4.6.0               Rtsne_0.17               cluster_2.1.8.2         
 [70] gtable_0.3.6             metapod_1.20.0           ScaledMatrix_1.20.0     
 [73] XVector_0.52.0           ggrepel_0.9.8            BiocVersion_3.23.1      
 [76] pillar_1.11.1            limma_3.68.0             dplyr_1.2.1             
 [79] lattice_0.22-9           rtracklayer_1.72.0       bit_4.6.0               
 [82] tidyselect_1.2.1         locfit_1.5-9.12          Biostrings_2.80.0       
 [85] knitr_1.51               gridExtra_2.3            bookdown_0.46           
 [88] ProtGenerics_1.44.0      edgeR_4.10.0             xfun_0.57               
 [91] statmod_1.5.1            UCSC.utils_1.8.0         lazyeval_0.2.3          
 [94] yaml_2.3.12              evaluate_1.0.5           codetools_0.2-20        
 [97] cigarillo_1.2.0          tibble_3.3.1             alabaster.matrix_1.12.0 
[100] BiocManager_1.30.27      graph_1.90.0             cli_3.6.6               
[103] jquerylib_0.1.4          dichromat_2.0-0.1        Rcpp_1.1.1-1.1          
[106] GenomeInfoDb_1.48.0      dir.expiry_1.20.0        png_0.1-9               
[109] XML_3.99-0.23            parallel_4.6.0           blob_1.3.0              
[112] bitops_1.0-9             viridisLite_0.4.3        alabaster.se_1.12.0     
[115] scales_1.4.0             purrr_1.2.2              crayon_1.5.3            
[118] rlang_1.2.0              cowplot_1.2.0            KEGGREST_1.52.0
```

### References

Bach, K., S. Pensa, M. Grzelak, J. Hadfield, D. J. Adams, J. C. Marioni, and W. T. Khaled. 2017. “Differentiation dynamics of mammary epithelial cells revealed by single-cell RNA sequencing.” *Nat Commun* 8 (1): 2128.
