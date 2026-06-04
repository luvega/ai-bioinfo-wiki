---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/grun-mouse-hsc-cel-seq.html
ingested_at: 2026-06-04T01:51:49+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 9 Grun mouse HSC (CEL-seq)

## 9.1 Introduction

This performs an analysis of the mouse haematopoietic stem cell (HSC) dataset generated with CEL-seq (Grun et al. [2016](https://bioconductor.org/books/3.23/OSCA.workflows/grun-mouse-hsc-cel-seq.html#ref-grun2016denovo)).
Despite its name, this dataset actually contains both sorted HSCs and a population of micro-dissected bone marrow cells.

## 9.2 Data loading

```
library(scRNAseq)
sce.grun.hsc <- GrunHSCData(ensembl=TRUE)
```

```
library(AnnotationHub)
ens.mm.v97 <- AnnotationHub()[["AH73905"]]
anno <- select(ens.mm.v97, keys=rownames(sce.grun.hsc), 
    keytype="GENEID", columns=c("SYMBOL", "SEQNAME"))
rowData(sce.grun.hsc) <- anno[match(rownames(sce.grun.hsc), anno$GENEID),]
```

After loading and annotation, we inspect the resulting `SingleCellExperiment` object:

```
sce.grun.hsc
```

```
## class: SingleCellExperiment 
## dim: 21817 1915 
## metadata(0):
## assays(1): counts
## rownames(21817): ENSMUSG00000109644 ENSMUSG00000007777 ...
##   ENSMUSG00000055670 ENSMUSG00000039068
## rowData names(3): GENEID SYMBOL SEQNAME
## colnames(1915): JC4_349_HSC_FE_S13_ JC4_350_HSC_FE_S13_ ...
##   JC48P6_1203_HSC_FE_S8_ JC48P6_1204_HSC_FE_S8_
## colData names(2): sample protocol
## reducedDimNames(0):
## mainExpName: NULL
## altExpNames(0):
```

## 9.3 Quality control

```
unfiltered <- sce.grun.hsc
```

For some reason, no mitochondrial transcripts are available, and we have no spike-in transcripts, so we only use the number of detected genes and the library size for quality control.
We block on the protocol used for cell extraction, ignoring the micro-dissected cells when computing this threshold.
This is based on our judgement that a majority of micro-dissected plates consist of a majority of low-quality cells, compromising the assumptions of outlier detection.

```
library(scuttle)
stats <- perCellQCMetrics(sce.grun.hsc)
qc <- quickPerCellQC(stats, batch=sce.grun.hsc$protocol,
    subset=grepl("sorted", sce.grun.hsc$protocol))
sce.grun.hsc <- sce.grun.hsc[,!qc$discard]
```

We examine the number of cells discarded for each reason.

```
colSums(as.matrix(qc))
```

```
##   low_lib_size low_n_features        discard 
##            465            482            488
```

We create some diagnostic plots for each metric (Figure [9.1](https://bioconductor.org/books/3.23/OSCA.workflows/grun-mouse-hsc-cel-seq.html#fig:unref-hgrun-qc-dist)).
The library sizes are unusually low for many plates of micro-dissected cells; this may be attributable to damage induced by the extraction protocol compared to cell sorting.

```
colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$discard <- qc$discard

library(scater)
gridExtra::grid.arrange(
    plotColData(unfiltered, y="sum", x="sample", colour_by="discard", 
        other_fields="protocol") + scale_y_log10() + ggtitle("Total count") +
        facet_wrap(~protocol),
    plotColData(unfiltered, y="detected", x="sample", colour_by="discard",
        other_fields="protocol") + scale_y_log10() + 
        ggtitle("Detected features") + facet_wrap(~protocol),
    ncol=1
)
```

![Distribution of each QC metric across cells in the Grun HSC dataset. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-grun-mouse-hsc-cel-seq/unref-hgrun-qc-dist-1.png)

Figure 9.1: Distribution of each QC metric across cells in the Grun HSC dataset. Each point represents a cell and is colored according to whether that cell was discarded.

## 9.4 Normalization

```
library(scran)
set.seed(101000110)
clusters <- quickCluster(sce.grun.hsc)
sce.grun.hsc <- computeSumFactors(sce.grun.hsc, clusters=clusters)
sce.grun.hsc <- logNormCounts(sce.grun.hsc)
```

We examine some key metrics for the distribution of size factors, and compare it to the library sizes as a sanity check (Figure [9.2](https://bioconductor.org/books/3.23/OSCA.workflows/grun-mouse-hsc-cel-seq.html#fig:unref-hgrun-norm)).

```
summary(sizeFactors(sce.grun.hsc))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.0275  0.2897  0.6032  1.0000  1.2011 16.4333
```

```
plot(librarySizeFactors(sce.grun.hsc), sizeFactors(sce.grun.hsc), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the Grun HSC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-grun-mouse-hsc-cel-seq/unref-hgrun-norm-1.png)

Figure 9.2: Relationship between the library size factors and the deconvolution size factors in the Grun HSC dataset.

## 9.5 Variance modelling

We create a mean-variance trend based on the expectation that UMI counts have Poisson technical noise.
We do not block on sample here as we want to preserve any difference between the micro-dissected cells and the sorted HSCs.

```
set.seed(00010101)
dec.grun.hsc <- modelGeneVarByPoisson(sce.grun.hsc) 
top.grun.hsc <- getTopHVGs(dec.grun.hsc, prop=0.1)
```

The lack of a typical “bump” shape in Figure [9.3](https://bioconductor.org/books/3.23/OSCA.workflows/grun-mouse-hsc-cel-seq.html#fig:unref-hgrun-var) is caused by the low counts.

```
plot(dec.grun.hsc$mean, dec.grun.hsc$total, pch=16, cex=0.5,
    xlab="Mean of log-expression", ylab="Variance of log-expression")
curfit <- metadata(dec.grun.hsc)
curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
```

![Per-gene variance as a function of the mean for the log-expression values in the Grun HSC dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the simulated Poisson-distributed noise.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-grun-mouse-hsc-cel-seq/unref-hgrun-var-1.png)

Figure 9.3: Per-gene variance as a function of the mean for the log-expression values in the Grun HSC dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the simulated Poisson-distributed noise.

## 9.6 Dimensionality reduction

```
set.seed(101010011)
sce.grun.hsc <- denoisePCA(sce.grun.hsc, technical=dec.grun.hsc, subset.row=top.grun.hsc)
sce.grun.hsc <- runTSNE(sce.grun.hsc, dimred="PCA")
```

We check that the number of retained PCs is sensible.

```
ncol(reducedDim(sce.grun.hsc, "PCA"))
```

```
## [1] 9
```

## 9.7 Clustering

```
snn.gr <- buildSNNGraph(sce.grun.hsc, use.dimred="PCA")
colLabels(sce.grun.hsc) <- factor(igraph::cluster_walktrap(snn.gr)$membership)
```

```
table(colLabels(sce.grun.hsc))
```

```
## 
##   1   2   3   4   5   6   7   8   9  10  11  12 
## 259 148 221 103 177 108  48 122  98  63  62  18
```

```
short <- ifelse(grepl("micro", sce.grun.hsc$protocol), "micro", "sorted")
gridExtra:::grid.arrange(
    plotTSNE(sce.grun.hsc, colour_by="label"),
    plotTSNE(sce.grun.hsc, colour_by=I(short)),
    ncol=2
)
```

![Obligatory $t$-SNE plot of the Grun HSC dataset, where each point represents a cell and is colored according to the assigned cluster (left) or extraction protocol (right).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-grun-mouse-hsc-cel-seq/unref-hgrun-tsne-1.png)

Figure 9.4: Obligatory \(t\)-SNE plot of the Grun HSC dataset, where each point represents a cell and is colored according to the assigned cluster (left) or extraction protocol (right).

## 9.8 Marker gene detection

```
markers <- findMarkers(sce.grun.hsc, test.type="wilcox", direction="up",
    row.data=rowData(sce.grun.hsc)[,"SYMBOL",drop=FALSE])
```

To illustrate the manual annotation process, we examine the marker genes for one of the clusters.
Upregulation of *Camp*, *Lcn2*, *Ltf* and lysozyme genes indicates that this cluster contains cells of neuronal origin.

```
chosen <- markers[['6']]
best <- chosen[chosen$Top <= 10,]
aucs <- getMarkerEffects(best, prefix="AUC")
rownames(aucs) <- best$SYMBOL

library(pheatmap)
pheatmap(aucs, color=viridis::plasma(100))
```

![Heatmap of the AUCs for the top marker genes in cluster 6 compared to all other clusters in the Grun HSC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-grun-mouse-hsc-cel-seq/unref-heat-hgrun-markers-1.png)

Figure 9.5: Heatmap of the AUCs for the top marker genes in cluster 6 compared to all other clusters in the Grun HSC dataset.

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
 [1] pheatmap_1.0.13             scran_1.40.0               
 [3] scater_1.40.0               ggplot2_4.0.3              
 [5] scuttle_1.22.0              AnnotationHub_4.2.0        
 [7] BiocFileCache_3.2.0         dbplyr_2.5.2               
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
 [70] gtable_0.3.6             metapod_1.20.0           BiocSingular_1.28.0     
 [73] ScaledMatrix_1.20.0      XVector_0.52.0           ggrepel_0.9.8           
 [76] BiocVersion_3.23.1       pillar_1.11.1            limma_3.68.0            
 [79] dplyr_1.2.1              lattice_0.22-9           rtracklayer_1.72.0      
 [82] bit_4.6.0                tidyselect_1.2.1         locfit_1.5-9.12         
 [85] Biostrings_2.80.0        knitr_1.51               gridExtra_2.3           
 [88] bookdown_0.46            ProtGenerics_1.44.0      edgeR_4.10.0            
 [91] xfun_0.57                statmod_1.5.1            UCSC.utils_1.8.0        
 [94] lazyeval_0.2.3           yaml_2.3.12              evaluate_1.0.5          
 [97] codetools_0.2-20         cigarillo_1.2.0          tibble_3.3.1            
[100] alabaster.matrix_1.12.0  BiocManager_1.30.27      graph_1.90.0            
[103] cli_3.6.6                jquerylib_0.1.4          dichromat_2.0-0.1       
[106] Rcpp_1.1.1-1.1           GenomeInfoDb_1.48.0      dir.expiry_1.20.0       
[109] png_0.1-9                XML_3.99-0.23            parallel_4.6.0          
[112] blob_1.3.0               bitops_1.0-9             viridisLite_0.4.3       
[115] alabaster.se_1.12.0      scales_1.4.0             purrr_1.2.2             
[118] crayon_1.5.3             rlang_1.2.0              cowplot_1.2.0           
[121] KEGGREST_1.52.0
```

### References

Grun, D., M. J. Muraro, J. C. Boisset, K. Wiebrands, A. Lyubimova, G. Dharmadhikari, M. van den Born, et al. 2016. “De Novo Prediction of Stem Cell Identity using Single-Cell Transcriptome Data.” *Cell Stem Cell* 19 (2): 266–77.
