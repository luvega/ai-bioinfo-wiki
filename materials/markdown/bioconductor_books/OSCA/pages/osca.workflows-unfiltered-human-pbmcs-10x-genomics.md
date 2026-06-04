---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/unfiltered-human-pbmcs-10x-genomics.html
ingested_at: 2026-06-04T01:52:18+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 3 Unfiltered human PBMCs (10X Genomics)

## 3.1 Introduction

Here, we describe a brief analysis of the peripheral blood mononuclear cell (PBMC) dataset from 10X Genomics (Zheng et al. [2017](https://bioconductor.org/books/3.23/OSCA.workflows/unfiltered-human-pbmcs-10x-genomics.html#ref-zheng2017massively)).
The data are publicly available from the [10X Genomics website](https://support.10xgenomics.com/single-cell-gene-expression/datasets/2.1.0/pbmc4k),
from which we download the raw gene/barcode count matrices, i.e., before cell calling from the *CellRanger* pipeline.

## 3.2 Data loading

```
library(DropletTestFiles)
raw.path <- getTestFile("tenx-2.1.0-pbmc4k/1.0.0/raw.tar.gz")
out.path <- file.path(tempdir(), "pbmc4k")
untar(raw.path, exdir=out.path)

library(DropletUtils)
fname <- file.path(out.path, "raw_gene_bc_matrices/GRCh38")
sce.pbmc <- read10xCounts(fname, col.names=TRUE)
```

```
library(scater)
rownames(sce.pbmc) <- uniquifyFeatureNames(
    rowData(sce.pbmc)$ID, rowData(sce.pbmc)$Symbol)

library(EnsDb.Hsapiens.v86)
location <- mapIds(EnsDb.Hsapiens.v86, keys=rowData(sce.pbmc)$ID, 
    column="SEQNAME", keytype="GENEID")
```

## 3.3 Quality control

We perform cell detection using the `emptyDrops()` algorithm, as discussed in [Advanced Section 7.2](http://bioconductor.org/books/3.23/OSCA.advanced/droplet-processing.html#qc-droplets).

```
set.seed(100)
e.out <- emptyDrops(counts(sce.pbmc))
sce.pbmc <- sce.pbmc[,which(e.out$FDR <= 0.001)]
```

```
unfiltered <- sce.pbmc
```

We use a relaxed QC strategy and only remove cells with large mitochondrial proportions, using it as a proxy for cell damage.
This reduces the risk of removing cell types with low RNA content, especially in a heterogeneous PBMC population with many different cell types.

```
stats <- perCellQCMetrics(sce.pbmc, subsets=list(Mito=which(location=="MT")))
high.mito <- isOutlier(stats$subsets_Mito_percent, type="higher")
sce.pbmc <- sce.pbmc[,!high.mito]
```

```
summary(high.mito)
```

```
##    Mode   FALSE    TRUE 
## logical    4080     322
```

```
colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$discard <- high.mito

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

![Distribution of various QC metrics in the PBMC dataset after cell calling. Each point is a cell and is colored according to whether it was discarded by the mitochondrial filter.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-unfiltered-human-pbmcs-10x-genomics/unref-unfiltered-pbmc-qc-1.png)

Figure 3.1: Distribution of various QC metrics in the PBMC dataset after cell calling. Each point is a cell and is colored according to whether it was discarded by the mitochondrial filter.

```
plotColData(unfiltered, x="sum", y="subsets_Mito_percent",
    colour_by="discard") + scale_x_log10()
```

![Proportion of mitochondrial reads in each cell of the PBMC dataset compared to its total count.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-unfiltered-human-pbmcs-10x-genomics/unref-unfiltered-pbmc-mito-1.png)

Figure 3.2: Proportion of mitochondrial reads in each cell of the PBMC dataset compared to its total count.

## 3.4 Normalization

```
library(scran)
set.seed(1000)
clusters <- quickCluster(sce.pbmc)
sce.pbmc <- computeSumFactors(sce.pbmc, cluster=clusters)
sce.pbmc <- logNormCounts(sce.pbmc)
```

```
summary(sizeFactors(sce.pbmc))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.0034  0.7107  0.8792  1.0000  1.1036 11.8046
```

```
plot(librarySizeFactors(sce.pbmc), sizeFactors(sce.pbmc), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the PBMC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-unfiltered-human-pbmcs-10x-genomics/unref-unfiltered-pbmc-norm-1.png)

Figure 3.3: Relationship between the library size factors and the deconvolution size factors in the PBMC dataset.

## 3.5 Variance modelling

```
set.seed(1001)
dec.pbmc <- modelGeneVarByPoisson(sce.pbmc)
top.pbmc <- getTopHVGs(dec.pbmc, prop=0.1)
```

```
plot(dec.pbmc$mean, dec.pbmc$total, pch=16, cex=0.5,
    xlab="Mean of log-expression", ylab="Variance of log-expression")
curfit <- metadata(dec.pbmc)
curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
```

![Per-gene variance as a function of the mean for the log-expression values in the PBMC dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to simulated Poisson counts.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-unfiltered-human-pbmcs-10x-genomics/unref-unfiltered-pbmc-var-1.png)

Figure 3.4: Per-gene variance as a function of the mean for the log-expression values in the PBMC dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to simulated Poisson counts.

## 3.6 Dimensionality reduction

```
set.seed(10000)
sce.pbmc <- denoisePCA(sce.pbmc, subset.row=top.pbmc, technical=dec.pbmc)

set.seed(100000)
sce.pbmc <- runTSNE(sce.pbmc, dimred="PCA")

set.seed(1000000)
sce.pbmc <- runUMAP(sce.pbmc, dimred="PCA")
```

We verify that a reasonable number of PCs is retained.

```
ncol(reducedDim(sce.pbmc, "PCA"))
```

```
## [1] 8
```

## 3.7 Clustering

```
g <- buildSNNGraph(sce.pbmc, k=10, use.dimred = 'PCA')
clust <- igraph::cluster_walktrap(g)$membership
colLabels(sce.pbmc) <- factor(clust)
```

```
table(colLabels(sce.pbmc))
```

```
## 
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19 
## 249 559 367  46 173 914 450 285 266 111 157 130 137  46  41  85  19  16  29
```

```
plotTSNE(sce.pbmc, colour_by="label")
```

![Obligatory $t$-SNE plot of the PBMC dataset, where each point represents a cell and is colored according to the assigned cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-unfiltered-human-pbmcs-10x-genomics/unref-unfiltered-pbmc-tsne-1.png)

Figure 3.5: Obligatory \(t\)-SNE plot of the PBMC dataset, where each point represents a cell and is colored according to the assigned cluster.

## 3.8 Interpretation

```
markers <- findMarkers(sce.pbmc, pval.type="some", direction="up")
```

We examine the markers for cluster 7 in more detail.
High expression of *CD14*, *CD68* and *MNDA* combined with low expression of *FCGR3A* (*CD16*) suggests that this cluster contains monocytes,
compared to macrophages in cluster 16 (Figure [3.6](https://bioconductor.org/books/3.23/OSCA.workflows/unfiltered-human-pbmcs-10x-genomics.html#fig:unref-mono-pbmc-markers)).

```
marker.set <- markers[["7"]]
as.data.frame(marker.set[1:30,1:3])
```

```
##                  p.value        FDR summary.logFC
## CSTA          1.119e-228 3.769e-224        2.3449
## S100A12       4.309e-219 7.259e-215        2.9671
## VCAN          3.002e-196 3.371e-192        2.2075
## MNDA          2.592e-190 2.183e-186        2.4570
## FCN1          1.091e-189 7.349e-186        2.6310
## TYMP          5.656e-149 3.176e-145        2.0055
## LGALS2        2.886e-145 1.389e-141        1.9130
## AIF1          8.929e-138 3.761e-134        2.4806
## MS4A6A        1.733e-135 6.486e-132        1.4980
## RP11-1143G9.4 1.269e-132 4.276e-129        2.8184
## FGL2          5.369e-132 1.644e-128        1.3690
## CD14          7.158e-121 2.010e-117        1.4279
## CFD           1.961e-114 5.082e-111        1.3114
## AP1S2         4.262e-107 1.026e-103        1.7835
## SERPINA1      3.393e-105 7.621e-102        1.3844
## CYBB          6.123e-104 1.290e-100        1.2483
## CLEC7A         7.224e-97  1.432e-93        1.0774
## KLF4           9.440e-95  1.767e-91        1.1718
## TNFSF13B       6.880e-92  1.220e-88        1.0524
## S100A8         1.526e-89  2.571e-86        4.7220
## NAMPT          3.679e-88  5.903e-85        1.0970
## CD36           3.426e-86  5.246e-83        1.0487
## MPEG1          2.504e-84  3.668e-81        0.9781
## CD68           1.330e-82  1.867e-79        0.9343
## CD302          1.506e-80  2.030e-77        0.8891
## CSF3R          6.392e-73  8.283e-70        0.8596
## RBP7           1.216e-72  1.517e-69        0.9072
## BLVRB          1.804e-72  2.171e-69        0.9711
## S100A11        1.824e-71  2.119e-68        1.8392
## CFP            3.688e-71  4.142e-68        1.0117
```

```
plotExpression(sce.pbmc, features=c("CD14", "CD68",
    "MNDA", "FCGR3A"), x="label", colour_by="label")
```

![Distribution of expression values for monocyte and macrophage markers across clusters in the PBMC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-unfiltered-human-pbmcs-10x-genomics/unref-mono-pbmc-markers-1.png)

Figure 3.6: Distribution of expression values for monocyte and macrophage markers across clusters in the PBMC dataset.

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
 [1] scran_1.40.0                EnsDb.Hsapiens.v86_2.99.0  
 [3] ensembldb_2.36.0            AnnotationFilter_1.36.0    
 [5] GenomicFeatures_1.64.0      AnnotationDbi_1.74.0       
 [7] scater_1.40.0               ggplot2_4.0.3              
 [9] scuttle_1.22.0              DropletUtils_1.32.0        
[11] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
[13] Biobase_2.72.0              GenomicRanges_1.64.0       
[15] Seqinfo_1.2.0               IRanges_2.46.0             
[17] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[19] generics_0.1.4              MatrixGenerics_1.24.0      
[21] matrixStats_1.5.0           DropletTestFiles_1.21.0    
[23] BiocStyle_2.40.0            rebook_1.22.0              

loaded via a namespace (and not attached):
  [1] RColorBrewer_1.1-3        jsonlite_2.0.0           
  [3] CodeDepends_0.6.7         magrittr_2.0.5           
  [5] ggbeeswarm_0.7.3          farver_2.1.2             
  [7] rmarkdown_2.31            BiocIO_1.22.0            
  [9] vctrs_0.7.3               memoise_2.0.1            
 [11] Rsamtools_2.28.0          DelayedMatrixStats_1.34.0
 [13] RCurl_1.98-1.18           htmltools_0.5.9          
 [15] S4Arrays_1.12.0           AnnotationHub_4.2.0      
 [17] curl_7.1.0                BiocNeighbors_2.6.0      
 [19] Rhdf5lib_2.0.0            SparseArray_1.12.0       
 [21] rhdf5_2.56.0              sass_0.4.10              
 [23] bslib_0.10.0              httr2_1.2.2              
 [25] cachem_1.1.0              GenomicAlignments_1.48.0 
 [27] igraph_2.3.0              lifecycle_1.0.5          
 [29] pkgconfig_2.0.3           rsvd_1.0.5               
 [31] Matrix_1.7-5              R6_2.6.1                 
 [33] fastmap_1.2.0             digest_0.6.39            
 [35] RSpectra_0.16-2           dqrng_0.4.1              
 [37] irlba_2.3.7               ExperimentHub_3.2.0      
 [39] RSQLite_2.4.6             beachmat_2.28.0          
 [41] labeling_0.4.3            filelock_1.0.3           
 [43] httr_1.4.8                abind_1.4-8              
 [45] compiler_4.6.0            bit64_4.8.0              
 [47] withr_3.0.2               S7_0.2.2                 
 [49] BiocParallel_1.46.0       viridis_0.6.5            
 [51] DBI_1.3.0                 HDF5Array_1.40.0         
 [53] R.utils_2.13.0            rappdirs_0.3.4           
 [55] DelayedArray_0.38.0       bluster_1.22.0           
 [57] rjson_0.2.23              tools_4.6.0              
 [59] vipor_0.4.7               otel_0.2.0               
 [61] beeswarm_0.4.0            R.oo_1.27.1              
 [63] glue_1.8.1                h5mread_1.4.0            
 [65] restfulr_0.0.16           rhdf5filters_1.24.0      
 [67] grid_4.6.0                Rtsne_0.17               
 [69] cluster_2.1.8.2           gtable_0.3.6             
 [71] R.methodsS3_1.8.2         metapod_1.20.0           
 [73] BiocSingular_1.28.0       ScaledMatrix_1.20.0      
 [75] XVector_0.52.0            ggrepel_0.9.8            
 [77] BiocVersion_3.23.1        pillar_1.11.1            
 [79] limma_3.68.0              dplyr_1.2.1              
 [81] BiocFileCache_3.2.0       lattice_0.22-9           
 [83] FNN_1.1.4.1               rtracklayer_1.72.0       
 [85] bit_4.6.0                 tidyselect_1.2.1         
 [87] locfit_1.5-9.12           Biostrings_2.80.0        
 [89] knitr_1.51                gridExtra_2.3            
 [91] bookdown_0.46             ProtGenerics_1.44.0      
 [93] edgeR_4.10.0              xfun_0.57                
 [95] statmod_1.5.1             UCSC.utils_1.8.0         
 [97] lazyeval_0.2.3            yaml_2.3.12              
 [99] cigarillo_1.2.0           evaluate_1.0.5           
[101] codetools_0.2-20          tibble_3.3.1             
[103] BiocManager_1.30.27       graph_1.90.0             
[105] cli_3.6.6                 uwot_0.2.4               
[107] jquerylib_0.1.4           GenomeInfoDb_1.48.0      
[109] dichromat_2.0-0.1         Rcpp_1.1.1-1.1           
[111] dir.expiry_1.20.0         dbplyr_2.5.2             
[113] png_0.1-9                 XML_3.99-0.23            
[115] parallel_4.6.0            blob_1.3.0               
[117] sparseMatrixStats_1.24.0  bitops_1.0-9             
[119] viridisLite_0.4.3         scales_1.4.0             
[121] purrr_1.2.2               crayon_1.5.3             
[123] rlang_1.2.0               cowplot_1.2.0            
[125] KEGGREST_1.52.0
```

### References

Zheng, G. X., J. M. Terry, P. Belgrader, P. Ryvkin, Z. W. Bent, R. Wilson, S. B. Ziraldo, et al. 2017. “Massively parallel digital transcriptional profiling of single cells.” *Nat Commun* 8 (January): 14049.
