---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/human-pbmc-with-surface-proteins-10x-genomics.html
ingested_at: 2026-06-04T01:52:53+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 4 Human PBMC with surface proteins (10X Genomics)

## 4.1 Introduction

Here, we describe a brief analysis of *yet another* peripheral blood mononuclear cell (PBMC) dataset from 10X Genomics (Zheng et al. [2017](https://bioconductor.org/books/3.23/OSCA.workflows/human-pbmc-with-surface-proteins-10x-genomics.html#ref-zheng2017massively)).
Data are publicly available from the [10X Genomics website](https://support.10xgenomics.com/single-cell-vdj/datasets/3.0.0/vdj_v1_mm_c57bl6_pbmc_5gex), from which we download the filtered gene/barcode count matrices for gene expression and cell surface proteins.

## 4.2 Data loading

```
library(BiocFileCache)
bfc <- BiocFileCache(ask=FALSE)
exprs.data <- bfcrpath(bfc, file.path(
    "http://cf.10xgenomics.com/samples/cell-vdj/3.1.0",
    "vdj_v1_hs_pbmc3",
    "vdj_v1_hs_pbmc3_filtered_feature_bc_matrix.tar.gz"))
untar(exprs.data, exdir=tempdir())

library(DropletUtils)
sce.pbmc <- read10xCounts(file.path(tempdir(), "filtered_feature_bc_matrix"))
sce.pbmc <- splitAltExps(sce.pbmc, rowData(sce.pbmc)$Type)
```

## 4.3 Quality control

```
unfiltered <- sce.pbmc
```

We discard cells with high mitochondrial proportions and few detectable ADT counts.

```
library(scater)
is.mito <- grep("^MT-", rowData(sce.pbmc)$Symbol)
stats <- perCellQCMetrics(sce.pbmc, subsets=list(Mito=is.mito))

high.mito <- isOutlier(stats$subsets_Mito_percent, type="higher")
low.adt <- stats$`altexps_Antibody Capture_detected` < nrow(altExp(sce.pbmc))/2

discard <- high.mito | low.adt
sce.pbmc <- sce.pbmc[,!discard]
```

We examine some of the statistics:

```
summary(high.mito)
```

```
##    Mode   FALSE    TRUE 
## logical    6660     571
```

```
summary(low.adt)
```

```
##    Mode   FALSE 
## logical    7231
```

```
summary(discard)
```

```
##    Mode   FALSE    TRUE 
## logical    6660     571
```

We examine the distribution of each QC metric (Figure [4.1](https://bioconductor.org/books/3.23/OSCA.workflows/human-pbmc-with-surface-proteins-10x-genomics.html#fig:unref-pbmc-adt-qc)).

```
colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$discard <- discard

gridExtra::grid.arrange(
    plotColData(unfiltered, y="sum", colour_by="discard") +
        scale_y_log10() + ggtitle("Total count"),
    plotColData(unfiltered, y="detected", colour_by="discard") +
        scale_y_log10() + ggtitle("Detected features"),
    plotColData(unfiltered, y="subsets_Mito_percent",
        colour_by="discard") + ggtitle("Mito percent"),
    plotColData(unfiltered, y="altexps_Antibody Capture_detected",
        colour_by="discard") + ggtitle("ADT detected"),
    ncol=2
)
```

![Distribution of each QC metric in the PBMC dataset, where each point is a cell and is colored by whether or not it was discarded by the outlier-based QC approach.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-human-pbmc-with-surface-proteins-10x-genomics/unref-pbmc-adt-qc-1.png)

Figure 4.1: Distribution of each QC metric in the PBMC dataset, where each point is a cell and is colored by whether or not it was discarded by the outlier-based QC approach.

We also plot the mitochondrial proportion against the total count for each cell, as one does (Figure [4.2](https://bioconductor.org/books/3.23/OSCA.workflows/human-pbmc-with-surface-proteins-10x-genomics.html#fig:unref-pbmc-adt-qc-mito)).

```
plotColData(unfiltered, x="sum", y="subsets_Mito_percent",
    colour_by="discard") + scale_x_log10()
```

![Percentage of UMIs mapped to mitochondrial genes against the totalcount for each cell.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-human-pbmc-with-surface-proteins-10x-genomics/unref-pbmc-adt-qc-mito-1.png)

Figure 4.2: Percentage of UMIs mapped to mitochondrial genes against the totalcount for each cell.

## 4.4 Normalization

Computing size factors for the gene expression and ADT counts.

```
library(scran)

set.seed(1000)
clusters <- quickCluster(sce.pbmc)
sce.pbmc <- computeSumFactors(sce.pbmc, cluster=clusters)
altExp(sce.pbmc) <- computeMedianFactors(altExp(sce.pbmc))
sce.pbmc <- applySCE(sce.pbmc, logNormCounts)
```

We generate some summary statistics for both sets of size factors:

```
summary(sizeFactors(sce.pbmc))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.074   0.717   0.909   1.000   1.128   9.100
```

```
summary(sizeFactors(altExp(sce.pbmc)))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.101   0.698   0.828   1.000   1.028 227.356
```

We also look at the distribution of size factors compared to the library size for each set of features (Figure [4.3](https://bioconductor.org/books/3.23/OSCA.workflows/human-pbmc-with-surface-proteins-10x-genomics.html#fig:unref-norm-pbmc-adt)).

```
par(mfrow=c(1,2))
plot(librarySizeFactors(sce.pbmc), sizeFactors(sce.pbmc), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", 
    main="Gene expression", log="xy")
plot(librarySizeFactors(altExp(sce.pbmc)), sizeFactors(altExp(sce.pbmc)), pch=16,
    xlab="Library size factors", ylab="Median-based factors", 
    main="Antibody capture", log="xy")
```

![Plot of the deconvolution size factors for the gene expression values (left) or the median-based size factors for the ADT expression values (right) compared to the library size-derived factors for the corresponding set of features. Each point represents a cell.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-human-pbmc-with-surface-proteins-10x-genomics/unref-norm-pbmc-adt-1.png)

Figure 4.3: Plot of the deconvolution size factors for the gene expression values (left) or the median-based size factors for the ADT expression values (right) compared to the library size-derived factors for the corresponding set of features. Each point represents a cell.

## 4.5 Dimensionality reduction

We omit the PCA step for the ADT expression matrix, given that it is already so low-dimensional,
and progress directly to \(t\)-SNE and UMAP visualizations.

```
set.seed(100000)
altExp(sce.pbmc) <- runTSNE(altExp(sce.pbmc))

set.seed(1000000)
altExp(sce.pbmc) <- runUMAP(altExp(sce.pbmc))
```

## 4.6 Clustering

We perform graph-based clustering on the ADT data and use the assignments as the column labels of the alternative Experiment.

```
g.adt <- buildSNNGraph(altExp(sce.pbmc), k=10, d=NA)
clust.adt <- igraph::cluster_walktrap(g.adt)$membership
colLabels(altExp(sce.pbmc)) <- factor(clust.adt)
```

We examine some basic statistics about the size of each cluster,
their separation (Figure [4.4](https://bioconductor.org/books/3.23/OSCA.workflows/human-pbmc-with-surface-proteins-10x-genomics.html#fig:unref-clustmod-pbmc-adt))
and their distribution in our \(t\)-SNE plot (Figure [4.5](https://bioconductor.org/books/3.23/OSCA.workflows/human-pbmc-with-surface-proteins-10x-genomics.html#fig:unref-tsne-pbmc-adt)).

```
table(colLabels(altExp(sce.pbmc)))
```

```
## 
##    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16 
##  160  507  662   39  691 1415   32  650   76 1037  121   47   68   25   15  562 
##   17   18   19   20   21   22   23   24 
##  139   32   44  120   84   65   52   17
```

```
library(bluster)
mod <- pairwiseModularity(g.adt, clust.adt, as.ratio=TRUE)

library(pheatmap)
pheatmap::pheatmap(log10(mod + 10), cluster_row=FALSE, cluster_col=FALSE,
    color=colorRampPalette(c("white", "blue"))(101))
```

![Heatmap of the pairwise cluster modularity scores in the PBMC dataset, computed based on the shared nearest neighbor graph derived from the ADT expression values.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-human-pbmc-with-surface-proteins-10x-genomics/unref-clustmod-pbmc-adt-1.png)

Figure 4.4: Heatmap of the pairwise cluster modularity scores in the PBMC dataset, computed based on the shared nearest neighbor graph derived from the ADT expression values.

```
plotTSNE(altExp(sce.pbmc), colour_by="label", text_by="label", text_colour="red")
```

![Obligatory $t$-SNE plot of PBMC dataset based on its ADT expression values, where each point is a cell and is colored by the cluster of origin. Cluster labels are also overlaid at the median coordinates across all cells in the cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-human-pbmc-with-surface-proteins-10x-genomics/unref-tsne-pbmc-adt-1.png)

Figure 4.5: Obligatory \(t\)-SNE plot of PBMC dataset based on its ADT expression values, where each point is a cell and is colored by the cluster of origin. Cluster labels are also overlaid at the median coordinates across all cells in the cluster.

We perform some additional subclustering using the expression data to mimic an *in silico* FACS experiment.

```
set.seed(1010010)
subclusters <- quickSubCluster(sce.pbmc, clust.adt,
    prepFUN=function(x) {
        dec <- modelGeneVarByPoisson(x)
        top <- getTopHVGs(dec, prop=0.1)
        denoisePCA(x, dec, subset.row=top)
    }, 
    clusterFUN=function(x) {
        g.gene <- buildSNNGraph(x, k=10, use.dimred = 'PCA')
        igraph::cluster_walktrap(g.gene)$membership
    }
)
```

We counting the number of gene expression-derived subclusters in each ADT-derived parent cluster.

```
data.frame(
    Cluster=names(subclusters),
    Ncells=vapply(subclusters, ncol, 0L),
    Nsub=vapply(subclusters, function(x) length(unique(x$subcluster)), 0L)
)
```

```
##    Cluster Ncells Nsub
## 1        1    160    3
## 2        2    507    4
## 3        3    662    5
## 4        4     39    1
## 5        5    691    5
## 6        6   1415    8
## 7        7     32    1
## 8        8    650    8
## 9        9     76    2
## 10      10   1037    9
## 11      11    121    3
## 12      12     47    1
## 13      13     68    3
## 14      14     25    1
## 15      15     15    1
## 16      16    562    6
## 17      17    139    3
## 18      18     32    1
## 19      19     44    1
## 20      20    120    4
## 21      21     84    2
## 22      22     65    2
## 23      23     52    2
## 24      24     17    1
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
 [1] pheatmap_1.0.13             bluster_1.22.0             
 [3] scran_1.40.0                scater_1.40.0              
 [5] ggplot2_4.0.3               scuttle_1.22.0             
 [7] DropletUtils_1.32.0         SingleCellExperiment_1.34.0
 [9] SummarizedExperiment_1.42.0 Biobase_2.72.0             
[11] GenomicRanges_1.64.0        Seqinfo_1.2.0              
[13] IRanges_2.46.0              S4Vectors_0.50.0           
[15] BiocGenerics_0.58.0         generics_0.1.4             
[17] MatrixGenerics_1.24.0       matrixStats_1.5.0          
[19] BiocFileCache_3.2.0         dbplyr_2.5.2               
[21] BiocStyle_2.40.0            rebook_1.22.0              

loaded via a namespace (and not attached):
  [1] DBI_1.3.0                 gridExtra_2.3            
  [3] httr2_1.2.2               CodeDepends_0.6.7        
  [5] rlang_1.2.0               magrittr_2.0.5           
  [7] RcppAnnoy_0.0.23          otel_0.2.0               
  [9] compiler_4.6.0            RSQLite_2.4.6            
 [11] dir.expiry_1.20.0         DelayedMatrixStats_1.34.0
 [13] vctrs_0.7.3               pkgconfig_2.0.3          
 [15] fastmap_1.2.0             XVector_0.52.0           
 [17] labeling_0.4.3            rmarkdown_2.31           
 [19] graph_1.90.0              ggbeeswarm_0.7.3         
 [21] purrr_1.2.2               bit_4.6.0                
 [23] xfun_0.57                 cachem_1.1.0             
 [25] beachmat_2.28.0           jsonlite_2.0.0           
 [27] blob_1.3.0                rhdf5filters_1.24.0      
 [29] DelayedArray_0.38.0       Rhdf5lib_2.0.0           
 [31] BiocParallel_1.46.0       cluster_2.1.8.2          
 [33] irlba_2.3.7               parallel_4.6.0           
 [35] R6_2.6.1                  bslib_0.10.0             
 [37] RColorBrewer_1.1-3        limma_3.68.0             
 [39] jquerylib_0.1.4           Rcpp_1.1.1-1.1           
 [41] bookdown_0.46             knitr_1.51               
 [43] R.utils_2.13.0            igraph_2.3.0             
 [45] Matrix_1.7-5              tidyselect_1.2.1         
 [47] viridis_0.6.5             dichromat_2.0-0.1        
 [49] abind_1.4-8               yaml_2.3.12              
 [51] codetools_0.2-20          curl_7.1.0               
 [53] lattice_0.22-9            tibble_3.3.1             
 [55] withr_3.0.2               S7_0.2.2                 
 [57] Rtsne_0.17                evaluate_1.0.5           
 [59] pillar_1.11.1             BiocManager_1.30.27      
 [61] filelock_1.0.3            sparseMatrixStats_1.24.0 
 [63] scales_1.4.0              glue_1.8.1               
 [65] metapod_1.20.0            tools_4.6.0              
 [67] BiocNeighbors_2.6.0       RSpectra_0.16-2          
 [69] ScaledMatrix_1.20.0       locfit_1.5-9.12          
 [71] XML_3.99-0.23             cowplot_1.2.0            
 [73] rhdf5_2.56.0              grid_4.6.0               
 [75] edgeR_4.10.0              beeswarm_0.4.0           
 [77] BiocSingular_1.28.0       HDF5Array_1.40.0         
 [79] vipor_0.4.7               cli_3.6.6                
 [81] rsvd_1.0.5                rappdirs_0.3.4           
 [83] viridisLite_0.4.3         S4Arrays_1.12.0          
 [85] dplyr_1.2.1               uwot_0.2.4               
 [87] gtable_0.3.6              R.methodsS3_1.8.2        
 [89] sass_0.4.10               digest_0.6.39            
 [91] ggrepel_0.9.8             SparseArray_1.12.0       
 [93] dqrng_0.4.1               farver_2.1.2             
 [95] memoise_2.0.1             htmltools_0.5.9          
 [97] R.oo_1.27.1               lifecycle_1.0.5          
 [99] h5mread_1.4.0             statmod_1.5.1            
[101] bit64_4.8.0
```

### References

Zheng, G. X., J. M. Terry, P. Belgrader, P. Ryvkin, Z. W. Bent, R. Wilson, S. B. Ziraldo, et al. 2017. “Massively parallel digital transcriptional profiling of single cells.” *Nat Commun* 8 (January): 14049.
