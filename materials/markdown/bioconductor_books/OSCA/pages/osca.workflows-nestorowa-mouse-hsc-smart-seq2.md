---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/nestorowa-mouse-hsc-smart-seq2.html
ingested_at: 2026-06-04T01:52:11+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 10 Nestorowa mouse HSC (Smart-seq2)

## 10.1 Introduction

This performs an analysis of the mouse haematopoietic stem cell (HSC) dataset generated with Smart-seq2 (Nestorowa et al. [2016](https://bioconductor.org/books/3.23/OSCA.workflows/nestorowa-mouse-hsc-smart-seq2.html#ref-nestorowa2016singlecell)).

## 10.2 Data loading

```
library(scRNAseq)
sce.nest <- NestorowaHSCData()
```

```
library(AnnotationHub)
ens.mm.v97 <- AnnotationHub()[["AH73905"]]
anno <- select(ens.mm.v97, keys=rownames(sce.nest), 
    keytype="GENEID", columns=c("SYMBOL", "SEQNAME"))
rowData(sce.nest) <- anno[match(rownames(sce.nest), anno$GENEID),]
```

After loading and annotation, we inspect the resulting `SingleCellExperiment` object:

```
sce.nest
```

```
## class: SingleCellExperiment 
## dim: 46078 1920 
## metadata(0):
## assays(1): counts
## rownames(46078): ENSMUSG00000000001 ENSMUSG00000000003 ...
##   ENSMUSG00000107391 ENSMUSG00000107392
## rowData names(3): GENEID SYMBOL SEQNAME
## colnames(1920): HSPC_007 HSPC_013 ... Prog_852 Prog_810
## colData names(9): gate broad ... projected metrics
## reducedDimNames(1): diffusion
## mainExpName: endogenous
## altExpNames(2): ERCC FACS
```

## 10.3 Quality control

```
unfiltered <- sce.nest
```

For some reason, no mitochondrial transcripts are available, so we will perform quality control using the spike-in proportions only.

```
library(scater)
stats <- perCellQCMetrics(sce.nest)
qc <- quickPerCellQC(stats, percent_subsets="altexps_ERCC_percent")
sce.nest <- sce.nest[,!qc$discard]
```

We examine the number of cells discarded for each reason.

```
colSums(as.matrix(qc))
```

```
##              low_lib_size            low_n_features high_altexps_ERCC_percent 
##                       146                        28                       241 
##                   discard 
##                       264
```

We create some diagnostic plots for each metric (Figure [10.1](https://bioconductor.org/books/3.23/OSCA.workflows/nestorowa-mouse-hsc-smart-seq2.html#fig:unref-nest-qc-dist)).

```
colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$discard <- qc$discard

gridExtra::grid.arrange(
    plotColData(unfiltered, y="sum", colour_by="discard") +
        scale_y_log10() + ggtitle("Total count"),
    plotColData(unfiltered, y="detected", colour_by="discard") +
        scale_y_log10() + ggtitle("Detected features"),
    plotColData(unfiltered, y="altexps_ERCC_percent",
        colour_by="discard") + ggtitle("ERCC percent"),
    ncol=2
)
```

![Distribution of each QC metric across cells in the Nestorowa HSC dataset. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-nestorowa-mouse-hsc-smart-seq2/unref-nest-qc-dist-1.png)

Figure 10.1: Distribution of each QC metric across cells in the Nestorowa HSC dataset. Each point represents a cell and is colored according to whether that cell was discarded.

## 10.4 Normalization

```
library(scran)
set.seed(101000110)
clusters <- quickCluster(sce.nest)
sce.nest <- computeSumFactors(sce.nest, clusters=clusters)
sce.nest <- logNormCounts(sce.nest)
```

We examine some key metrics for the distribution of size factors, and compare it to the library sizes as a sanity check (Figure [10.2](https://bioconductor.org/books/3.23/OSCA.workflows/nestorowa-mouse-hsc-smart-seq2.html#fig:unref-nest-norm)).

```
summary(sizeFactors(sce.nest))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.0388  0.4202  0.7430  1.0000  1.2490 16.7890
```

```
plot(librarySizeFactors(sce.nest), sizeFactors(sce.nest), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the Nestorowa HSC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-nestorowa-mouse-hsc-smart-seq2/unref-nest-norm-1.png)

Figure 10.2: Relationship between the library size factors and the deconvolution size factors in the Nestorowa HSC dataset.

## 10.5 Variance modelling

We use the spike-in transcripts to model the technical noise as a function of the mean (Figure [10.3](https://bioconductor.org/books/3.23/OSCA.workflows/nestorowa-mouse-hsc-smart-seq2.html#fig:unref-nest-var)).

```
set.seed(00010101)
dec.nest <- modelGeneVarWithSpikes(sce.nest, "ERCC")
top.nest <- getTopHVGs(dec.nest, prop=0.1)
```

```
plot(dec.nest$mean, dec.nest$total, pch=16, cex=0.5,
    xlab="Mean of log-expression", ylab="Variance of log-expression")
curfit <- metadata(dec.nest)
curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
points(curfit$mean, curfit$var, col="red")
```

![Per-gene variance as a function of the mean for the log-expression values in the Nestorowa HSC dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-ins (red).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-nestorowa-mouse-hsc-smart-seq2/unref-nest-var-1.png)

Figure 10.3: Per-gene variance as a function of the mean for the log-expression values in the Nestorowa HSC dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-ins (red).

## 10.6 Dimensionality reduction

```
set.seed(101010011)
sce.nest <- denoisePCA(sce.nest, technical=dec.nest, subset.row=top.nest)
sce.nest <- runTSNE(sce.nest, dimred="PCA")
```

We check that the number of retained PCs is sensible.

```
ncol(reducedDim(sce.nest, "PCA"))
```

```
## [1] 9
```

## 10.7 Clustering

```
snn.gr <- buildSNNGraph(sce.nest, use.dimred="PCA")
colLabels(sce.nest) <- factor(igraph::cluster_walktrap(snn.gr)$membership)
```

```
table(colLabels(sce.nest))
```

```
## 
##   1   2   3   4   5   6   7   8   9  10 
## 198 319 208 147 221 182  21 209  74  77
```

```
plotTSNE(sce.nest, colour_by="label")
```

![Obligatory $t$-SNE plot of the Nestorowa HSC dataset, where each point represents a cell and is colored according to the assigned cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-nestorowa-mouse-hsc-smart-seq2/unref-nest-tsne-1.png)

Figure 10.4: Obligatory \(t\)-SNE plot of the Nestorowa HSC dataset, where each point represents a cell and is colored according to the assigned cluster.

## 10.8 Marker gene detection

```
markers <- findMarkers(sce.nest, colLabels(sce.nest), 
    test.type="wilcox", direction="up", lfc=0.5,
    row.data=rowData(sce.nest)[,"SYMBOL",drop=FALSE])
```

To illustrate the manual annotation process, we examine the marker genes for one of the clusters.
Upregulation of *Car2*, *Hebp1* amd hemoglobins indicates that cluster 10 contains erythroid precursors.

```
chosen <- markers[['10']]
best <- chosen[chosen$Top <= 10,]
aucs <- getMarkerEffects(best, prefix="AUC")
rownames(aucs) <- best$SYMBOL

library(pheatmap)
pheatmap(aucs, color=viridis::plasma(100))
```

![Heatmap of the AUCs for the top marker genes in cluster 10 compared to all other clusters.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-nestorowa-mouse-hsc-smart-seq2/unref-heat-nest-markers-1.png)

Figure 10.5: Heatmap of the AUCs for the top marker genes in cluster 10 compared to all other clusters.

## 10.9 Cell type annotation

```
library(SingleR)
mm.ref <- MouseRNAseqData()

# Renaming to symbols to match with reference row names.
renamed <- sce.nest
rownames(renamed) <- uniquifyFeatureNames(rownames(renamed),
    rowData(sce.nest)$SYMBOL)
labels <- SingleR(renamed, mm.ref, labels=mm.ref$label.fine)
```

Most clusters are not assigned to any single lineage (Figure [10.6](https://bioconductor.org/books/3.23/OSCA.workflows/nestorowa-mouse-hsc-smart-seq2.html#fig:unref-assignments-nest)), which is perhaps unsurprising given that HSCs are quite different from their terminal fates.
Cluster 10 is considered to contain erythrocytes, which is roughly consistent with our conclusions from the marker gene analysis above.

```
tab <- table(labels$labels, colLabels(sce.nest))
pheatmap(log10(tab+10), color=viridis::viridis(100))
```

![Heatmap of the distribution of cells for each cluster in the Nestorowa HSC dataset, based on their assignment to each label in the mouse RNA-seq references from the _SingleR_ package.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-nestorowa-mouse-hsc-smart-seq2/unref-assignments-nest-1.png)

Figure 10.6: Heatmap of the distribution of cells for each cluster in the Nestorowa HSC dataset, based on their assignment to each label in the mouse RNA-seq references from the *SingleR* package.

## 10.10 Miscellaneous analyses

This dataset also contains information about the protein abundances in each cell from FACS.
There is barely any heterogeneity in the chosen markers across the clusters (Figure [10.7](https://bioconductor.org/books/3.23/OSCA.workflows/nestorowa-mouse-hsc-smart-seq2.html#fig:unref-nest-facs));
this is perhaps unsurprising given that all cells should be HSCs of some sort.

```
Y <- assay(altExp(sce.nest, "FACS"))
keep <- colSums(is.na(Y))==0 # Removing NA intensities.

se.averaged <- sumCountsAcrossCells(Y[,keep], 
    colLabels(sce.nest)[keep], average=TRUE)
averaged <- assay(se.averaged)

log.intensities <- log2(averaged+1)
centered <- log.intensities - rowMeans(log.intensities)
pheatmap(centered, breaks=seq(-1, 1, length.out=101))
```

![Heatmap of the centered log-average intensity for each target protein quantified by FACS in the Nestorowa HSC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-nestorowa-mouse-hsc-smart-seq2/unref-nest-facs-1.png)

Figure 10.7: Heatmap of the centered log-average intensity for each target protein quantified by FACS in the Nestorowa HSC dataset.

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
 [1] SingleR_2.14.0              pheatmap_1.0.13            
 [3] scran_1.40.0                scater_1.40.0              
 [5] ggplot2_4.0.3               scuttle_1.22.0             
 [7] AnnotationHub_4.2.0         BiocFileCache_3.2.0        
 [9] dbplyr_2.5.2                ensembldb_2.36.0           
[11] AnnotationFilter_1.36.0     GenomicFeatures_1.64.0     
[13] AnnotationDbi_1.74.0        scRNAseq_2.25.0            
[15] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
[17] Biobase_2.72.0              GenomicRanges_1.64.0       
[19] Seqinfo_1.2.0               IRanges_2.46.0             
[21] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[23] generics_0.1.4              MatrixGenerics_1.24.0      
[25] matrixStats_1.5.0           BiocStyle_2.40.0           
[27] rebook_1.22.0              

loaded via a namespace (and not attached):
  [1] RColorBrewer_1.1-3        jsonlite_2.0.0           
  [3] CodeDepends_0.6.7         magrittr_2.0.5           
  [5] ggbeeswarm_0.7.3          gypsum_1.8.0             
  [7] farver_2.1.2              rmarkdown_2.31           
  [9] BiocIO_1.22.0             vctrs_0.7.3              
 [11] DelayedMatrixStats_1.34.0 memoise_2.0.1            
 [13] Rsamtools_2.28.0          RCurl_1.98-1.18          
 [15] htmltools_0.5.9           S4Arrays_1.12.0          
 [17] curl_7.1.0                BiocNeighbors_2.6.0      
 [19] Rhdf5lib_2.0.0            SparseArray_1.12.0       
 [21] rhdf5_2.56.0              sass_0.4.10              
 [23] alabaster.base_1.12.0     bslib_0.10.0             
 [25] alabaster.sce_1.12.0      httr2_1.2.2              
 [27] cachem_1.1.0              GenomicAlignments_1.48.0 
 [29] igraph_2.3.0              lifecycle_1.0.5          
 [31] pkgconfig_2.0.3           rsvd_1.0.5               
 [33] Matrix_1.7-5              R6_2.6.1                 
 [35] fastmap_1.2.0             digest_0.6.39            
 [37] dqrng_0.4.1               irlba_2.3.7              
 [39] ExperimentHub_3.2.0       RSQLite_2.4.6            
 [41] beachmat_2.28.0           labeling_0.4.3           
 [43] filelock_1.0.3            httr_1.4.8               
 [45] abind_1.4-8               compiler_4.6.0           
 [47] bit64_4.8.0               withr_3.0.2              
 [49] S7_0.2.2                  BiocParallel_1.46.0      
 [51] viridis_0.6.5             DBI_1.3.0                
 [53] HDF5Array_1.40.0          alabaster.ranges_1.12.0  
 [55] alabaster.schemas_1.12.0  rappdirs_0.3.4           
 [57] DelayedArray_0.38.0       bluster_1.22.0           
 [59] rjson_0.2.23              tools_4.6.0              
 [61] vipor_0.4.7               otel_0.2.0               
 [63] beeswarm_0.4.0            glue_1.8.1               
 [65] h5mread_1.4.0             restfulr_0.0.16          
 [67] rhdf5filters_1.24.0       grid_4.6.0               
 [69] Rtsne_0.17                cluster_2.1.8.2          
 [71] gtable_0.3.6              metapod_1.20.0           
 [73] BiocSingular_1.28.0       ScaledMatrix_1.20.0      
 [75] XVector_0.52.0            ggrepel_0.9.8            
 [77] BiocVersion_3.23.1        pillar_1.11.1            
 [79] limma_3.68.0              dplyr_1.2.1              
 [81] lattice_0.22-9            rtracklayer_1.72.0       
 [83] bit_4.6.0                 tidyselect_1.2.1         
 [85] locfit_1.5-9.12           Biostrings_2.80.0        
 [87] knitr_1.51                gridExtra_2.3            
 [89] bookdown_0.46             ProtGenerics_1.44.0      
 [91] edgeR_4.10.0              xfun_0.57                
 [93] statmod_1.5.1             UCSC.utils_1.8.0         
 [95] lazyeval_0.2.3            yaml_2.3.12              
 [97] evaluate_1.0.5            codetools_0.2-20         
 [99] cigarillo_1.2.0           tibble_3.3.1             
[101] alabaster.matrix_1.12.0   BiocManager_1.30.27      
[103] graph_1.90.0              cli_3.6.6                
[105] jquerylib_0.1.4           dichromat_2.0-0.1        
[107] Rcpp_1.1.1-1.1            GenomeInfoDb_1.48.0      
[109] dir.expiry_1.20.0         png_0.1-9                
[111] XML_3.99-0.23             parallel_4.6.0           
[113] blob_1.3.0                sparseMatrixStats_1.24.0 
[115] bitops_1.0-9              viridisLite_0.4.3        
[117] alabaster.se_1.12.0       scales_1.4.0             
[119] purrr_1.2.2               crayon_1.5.3             
[121] rlang_1.2.0               celldex_1.21.0           
[123] cowplot_1.2.0             KEGGREST_1.52.0
```

### References

Nestorowa, S., F. K. Hamey, B. Pijuan Sala, E. Diamanti, M. Shepherd, E. Laurenti, N. K. Wilson, D. G. Kent, and B. Gottgens. 2016. “A single-cell resolution map of mouse hematopoietic stem and progenitor cell differentiation.” *Blood* 128 (8): 20–31.
