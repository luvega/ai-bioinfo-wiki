---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/muraro-human-pancreas-cel-seq.html
ingested_at: 2026-06-04T01:52:14+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 6 Muraro human pancreas (CEL-seq)

## 6.1 Introduction

This performs an analysis of the Muraro et al. ([2016](https://bioconductor.org/books/3.23/OSCA.workflows/muraro-human-pancreas-cel-seq.html#ref-muraro2016singlecell)) CEL-seq dataset,
consisting of human pancreas cells from various donors.

## 6.2 Data loading

```
library(scRNAseq)
sce.muraro <- MuraroPancreasData()
```

Converting back to Ensembl identifiers.

```
library(AnnotationHub)
edb <- AnnotationHub()[["AH73881"]]
gene.symb <- sub("__chr.*$", "", rownames(sce.muraro))
gene.ids <- mapIds(edb, keys=gene.symb, 
    keytype="SYMBOL", column="GENEID")

# Removing duplicated genes or genes without Ensembl IDs.
keep <- !is.na(gene.ids) & !duplicated(gene.ids)
sce.muraro <- sce.muraro[keep,]
rownames(sce.muraro) <- gene.ids[keep]
```

## 6.3 Quality control

```
unfiltered <- sce.muraro
```

This dataset lacks mitochondrial genes so we will do without.
For the one batch that seems to have a high proportion of low-quality cells, we compute an appropriate filter threshold using a shared median and MAD from the other batches (Figure [6.1](https://bioconductor.org/books/3.23/OSCA.workflows/muraro-human-pancreas-cel-seq.html#fig:unref-muraro-qc-dist)).

```
library(scater)
stats <- perCellQCMetrics(sce.muraro)
qc <- quickPerCellQC(stats, percent_subsets="altexps_ERCC_percent",
    batch=sce.muraro$donor, subset=sce.muraro$donor!="D28")
sce.muraro <- sce.muraro[,!qc$discard]
```

```
colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$discard <- qc$discard

gridExtra::grid.arrange(
    plotColData(unfiltered, x="donor", y="sum", colour_by="discard") +
        scale_y_log10() + ggtitle("Total count"),
    plotColData(unfiltered, x="donor", y="detected", colour_by="discard") +
        scale_y_log10() + ggtitle("Detected features"),
    plotColData(unfiltered, x="donor", y="altexps_ERCC_percent",
        colour_by="discard") + ggtitle("ERCC percent"),
    ncol=2
)
```

![Distribution of each QC metric across cells from each donor in the Muraro pancreas dataset. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-muraro-human-pancreas-cel-seq/unref-muraro-qc-dist-1.png)

Figure 6.1: Distribution of each QC metric across cells from each donor in the Muraro pancreas dataset. Each point represents a cell and is colored according to whether that cell was discarded.

We have a look at the causes of removal:

```
colSums(as.matrix(qc))
```

```
##              low_lib_size            low_n_features high_altexps_ERCC_percent 
##                       663                       700                       738 
##                   discard 
##                       773
```

## 6.4 Normalization

```
library(scran)
set.seed(1000)
clusters <- quickCluster(sce.muraro)
sce.muraro <- computeSumFactors(sce.muraro, clusters=clusters)
sce.muraro <- logNormCounts(sce.muraro)
```

```
summary(sizeFactors(sce.muraro))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.0878  0.5411  0.8208  1.0000  1.2108 13.9869
```

```
plot(librarySizeFactors(sce.muraro), sizeFactors(sce.muraro), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the Muraro pancreas dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-muraro-human-pancreas-cel-seq/unref-muraro-norm-1.png)

Figure 6.2: Relationship between the library size factors and the deconvolution size factors in the Muraro pancreas dataset.

## 6.5 Variance modelling

We block on a combined plate and donor factor.

```
block <- paste0(sce.muraro$plate, "_", sce.muraro$donor)
dec.muraro <- modelGeneVarWithSpikes(sce.muraro, "ERCC", block=block)
top.muraro <- getTopHVGs(dec.muraro, prop=0.1)
```

```
par(mfrow=c(8,4))
blocked.stats <- dec.muraro$per.block
for (i in colnames(blocked.stats)) {
    current <- blocked.stats[[i]]
    plot(current$mean, current$total, main=i, pch=16, cex=0.5,
        xlab="Mean of log-expression", ylab="Variance of log-expression")
    curfit <- metadata(current)
    points(curfit$mean, curfit$var, col="red", pch=16)
    curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
}
```

![Per-gene variance as a function of the mean for the log-expression values in the Muraro pancreas dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red) separately for each donor.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-muraro-human-pancreas-cel-seq/unref-muraro-variance-1.png)

Figure 6.3: Per-gene variance as a function of the mean for the log-expression values in the Muraro pancreas dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red) separately for each donor.

## 6.6 Data integration

```
library(batchelor)
set.seed(1001010)
merged.muraro <- fastMNN(sce.muraro, subset.row=top.muraro, 
    batch=sce.muraro$donor)
```

We use the proportion of variance lost as a diagnostic measure:

```
metadata(merged.muraro)$merge.info$lost.var
```

```
##           D28      D29      D30     D31
## [1,] 0.060847 0.024121 0.000000 0.00000
## [2,] 0.002646 0.003018 0.062421 0.00000
## [3,] 0.003449 0.002641 0.002598 0.08162
```

## 6.7 Dimensionality reduction

```
set.seed(100111)
merged.muraro <- runTSNE(merged.muraro, dimred="corrected")
```

## 6.8 Clustering

```
snn.gr <- buildSNNGraph(merged.muraro, use.dimred="corrected")
colLabels(merged.muraro) <- factor(igraph::cluster_walktrap(snn.gr)$membership)
```

```
tab <- table(Cluster=colLabels(merged.muraro), CellType=sce.muraro$label)
library(pheatmap)
pheatmap(log10(tab+10), color=viridis::viridis(100))
```

![Heatmap of the frequency of cells from each cell type label in each cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-muraro-human-pancreas-cel-seq/unref-seger-heat-1.png)

Figure 6.4: Heatmap of the frequency of cells from each cell type label in each cluster.

```
table(Cluster=colLabels(merged.muraro), Donor=merged.muraro$batch)
```

```
##        Donor
## Cluster D28 D29 D30 D31
##      1  104   6  57 112
##      2   59  21  77  97
##      3   12  75  64  43
##      4   28 149 126 120
##      5   87 261 277 214
##      6   21   7  54  26
##      7    1   6   6  37
##      8    6   6   5   2
##      9   11  68   5  30
##      10   4   2   5   8
```

```
gridExtra::grid.arrange(
    plotTSNE(merged.muraro, colour_by="label"),
    plotTSNE(merged.muraro, colour_by="batch"),
    ncol=2
)
```

![Obligatory $t$-SNE plots of the Muraro pancreas dataset. Each point represents a cell that is colored by cluster (left) or batch (right).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-muraro-human-pancreas-cel-seq/unref-muraro-tsne-1.png)

Figure 6.5: Obligatory \(t\)-SNE plots of the Muraro pancreas dataset. Each point represents a cell that is colored by cluster (left) or batch (right).

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
 [1] pheatmap_1.0.13             batchelor_1.28.0           
 [3] scran_1.40.0                scater_1.40.0              
 [5] ggplot2_4.0.3               scuttle_1.22.0             
 [7] ensembldb_2.36.0            AnnotationFilter_1.36.0    
 [9] GenomicFeatures_1.64.0      AnnotationDbi_1.74.0       
[11] AnnotationHub_4.2.0         BiocFileCache_3.2.0        
[13] dbplyr_2.5.2                scRNAseq_2.25.0            
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
 [27] cachem_1.1.0              ResidualMatrix_1.22.0    
 [29] GenomicAlignments_1.48.0  igraph_2.3.0             
 [31] lifecycle_1.0.5           pkgconfig_2.0.3          
 [33] rsvd_1.0.5                Matrix_1.7-5             
 [35] R6_2.6.1                  fastmap_1.2.0            
 [37] digest_0.6.39             dqrng_0.4.1              
 [39] irlba_2.3.7               ExperimentHub_3.2.0      
 [41] RSQLite_2.4.6             beachmat_2.28.0          
 [43] labeling_0.4.3            filelock_1.0.3           
 [45] httr_1.4.8                abind_1.4-8              
 [47] compiler_4.6.0            bit64_4.8.0              
 [49] withr_3.0.2               S7_0.2.2                 
 [51] BiocParallel_1.46.0       viridis_0.6.5            
 [53] DBI_1.3.0                 HDF5Array_1.40.0         
 [55] alabaster.ranges_1.12.0   alabaster.schemas_1.12.0 
 [57] rappdirs_0.3.4            DelayedArray_0.38.0      
 [59] bluster_1.22.0            rjson_0.2.23             
 [61] tools_4.6.0               vipor_0.4.7              
 [63] otel_0.2.0                beeswarm_0.4.0           
 [65] glue_1.8.1                h5mread_1.4.0            
 [67] restfulr_0.0.16           rhdf5filters_1.24.0      
 [69] grid_4.6.0                Rtsne_0.17               
 [71] cluster_2.1.8.2           gtable_0.3.6             
 [73] metapod_1.20.0            BiocSingular_1.28.0      
 [75] ScaledMatrix_1.20.0       XVector_0.52.0           
 [77] ggrepel_0.9.8             BiocVersion_3.23.1       
 [79] pillar_1.11.1             limma_3.68.0             
 [81] dplyr_1.2.1               lattice_0.22-9           
 [83] rtracklayer_1.72.0        bit_4.6.0                
 [85] tidyselect_1.2.1          locfit_1.5-9.12          
 [87] Biostrings_2.80.0         knitr_1.51               
 [89] gridExtra_2.3             bookdown_0.46            
 [91] ProtGenerics_1.44.0       edgeR_4.10.0             
 [93] xfun_0.57                 statmod_1.5.1            
 [95] UCSC.utils_1.8.0          lazyeval_0.2.3           
 [97] yaml_2.3.12               evaluate_1.0.5           
 [99] codetools_0.2-20          cigarillo_1.2.0          
[101] tibble_3.3.1              alabaster.matrix_1.12.0  
[103] BiocManager_1.30.27       graph_1.90.0             
[105] cli_3.6.6                 jquerylib_0.1.4          
[107] dichromat_2.0-0.1         Rcpp_1.1.1-1.1           
[109] GenomeInfoDb_1.48.0       dir.expiry_1.20.0        
[111] png_0.1-9                 XML_3.99-0.23            
[113] parallel_4.6.0            blob_1.3.0               
[115] sparseMatrixStats_1.24.0  bitops_1.0-9             
[117] viridisLite_0.4.3         alabaster.se_1.12.0      
[119] scales_1.4.0              purrr_1.2.2              
[121] crayon_1.5.3              rlang_1.2.0              
[123] cowplot_1.2.0             KEGGREST_1.52.0
```

### References

Muraro, M. J., G. Dharmadhikari, D. Grun, N. Groen, T. Dielen, E. Jansen, L. van Gurp, et al. 2016. “A Single-Cell Transcriptome Atlas of the Human Pancreas.” *Cell Syst* 3 (4): 385–94.
