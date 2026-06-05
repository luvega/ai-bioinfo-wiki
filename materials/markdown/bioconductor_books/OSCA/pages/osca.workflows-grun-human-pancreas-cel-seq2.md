---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/grun-human-pancreas-cel-seq2.html
ingested_at: 2026-06-04T01:52:06+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 5 Grun human pancreas (CEL-seq2)

## 5.1 Introduction

This workflow performs an analysis of the Grun et al. ([2016](https://bioconductor.org/books/3.23/OSCA.workflows/grun-human-pancreas-cel-seq2.html#ref-grun2016denovo)) CEL-seq2 dataset consisting of human pancreas cells from various donors.

## 5.2 Data loading

```
library(scRNAseq)
sce.grun <- GrunPancreasData()
```

We convert to Ensembl identifiers, and we remove duplicated genes or genes without Ensembl IDs.

```
library(org.Hs.eg.db)
gene.ids <- mapIds(org.Hs.eg.db, keys=rowData(sce.grun)$symbol,
    keytype="SYMBOL", column="ENSEMBL")

keep <- !is.na(gene.ids) & !duplicated(gene.ids)
sce.grun <- sce.grun[keep,]
rownames(sce.grun) <- gene.ids[keep]
```

## 5.3 Quality control

```
unfiltered <- sce.grun
```

This dataset lacks mitochondrial genes so we will do without them for quality control.
We compute the median and MAD while blocking on the donor;
for donors where the assumption of a majority of high-quality cells seems to be violated (Figure [5.1](https://bioconductor.org/books/3.23/OSCA.workflows/grun-human-pancreas-cel-seq2.html#fig:unref-grun-qc-dist)),
we compute an appropriate threshold using the other donors as specified in the `subset=` argument.

```
library(scater)
stats <- perCellQCMetrics(sce.grun)

qc <- quickPerCellQC(stats, percent_subsets="altexps_ERCC_percent",
    batch=sce.grun$donor,
    subset=sce.grun$donor %in% c("D17", "D7", "D2"))

sce.grun <- sce.grun[,!qc$discard]
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

![Distribution of each QC metric across cells from each donor of the Grun pancreas dataset. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-grun-human-pancreas-cel-seq2/unref-grun-qc-dist-1.png)

Figure 5.1: Distribution of each QC metric across cells from each donor of the Grun pancreas dataset. Each point represents a cell and is colored according to whether that cell was discarded.

```
colSums(as.matrix(qc), na.rm=TRUE)
```

```
##              low_lib_size            low_n_features high_altexps_ERCC_percent 
##                       450                       510                       606 
##                   discard 
##                       664
```

## 5.4 Normalization

```
library(scran)
set.seed(1000) # for irlba. 
clusters <- quickCluster(sce.grun)
sce.grun <- computeSumFactors(sce.grun, clusters=clusters)
sce.grun <- logNormCounts(sce.grun)
```

```
summary(sizeFactors(sce.grun))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.0933  0.5044  0.7894  1.0000  1.2307 10.8933
```

```
plot(librarySizeFactors(sce.grun), sizeFactors(sce.grun), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the Grun pancreas dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-grun-human-pancreas-cel-seq2/unref-grun-norm-1.png)

Figure 5.2: Relationship between the library size factors and the deconvolution size factors in the Grun pancreas dataset.

## 5.5 Variance modelling

We block on a combined plate and donor factor.

```
block <- paste0(sce.grun$sample, "_", sce.grun$donor)
dec.grun <- modelGeneVarWithSpikes(sce.grun, spikes="ERCC", block=block)
top.grun <- getTopHVGs(dec.grun, prop=0.1)
```

We examine the number of cells in each level of the blocking factor.

```
table(block)
```

```
## block
##                  CD13+ sorted cells_D17       CD24+ CD44+ live sorted cells_D17 
##                                      87                                      87 
##                  CD63+ sorted cells_D10                TGFBR3+ sorted cells_D17 
##                                      40                                      90 
## exocrine fraction, live sorted cells_D2 exocrine fraction, live sorted cells_D3 
##                                      82                                       7 
##        live sorted cells, library 1_D10        live sorted cells, library 1_D17 
##                                      33                                      88 
##         live sorted cells, library 1_D3         live sorted cells, library 1_D7 
##                                      25                                      85 
##        live sorted cells, library 2_D10        live sorted cells, library 2_D17 
##                                      35                                      83 
##         live sorted cells, library 2_D3         live sorted cells, library 2_D7 
##                                      27                                      84 
##         live sorted cells, library 3_D3         live sorted cells, library 3_D7 
##                                      16                                      83 
##         live sorted cells, library 4_D3         live sorted cells, library 4_D7 
##                                      29                                      83
```

```
par(mfrow=c(6,3))
blocked.stats <- dec.grun$per.block
for (i in colnames(blocked.stats)) {
    current <- blocked.stats[[i]]
    plot(current$mean, current$total, main=i, pch=16, cex=0.5,
        xlab="Mean of log-expression", ylab="Variance of log-expression")
    curfit <- metadata(current)
    points(curfit$mean, curfit$var, col="red", pch=16)
    curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
}
```

![Per-gene variance as a function of the mean for the log-expression values in the Grun pancreas dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red) separately for each donor.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-grun-human-pancreas-cel-seq2/unref-416b-variance-1.png)

Figure 1.4: Per-gene variance as a function of the mean for the log-expression values in the Grun pancreas dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red) separately for each donor.

## 5.6 Data integration

```
library(batchelor)
set.seed(1001010)
merged.grun <- fastMNN(sce.grun, subset.row=top.grun, batch=sce.grun$donor)
```

```
metadata(merged.grun)$merge.info$lost.var
```

```
##           D10      D17       D2      D3      D7
## [1,] 0.030387 0.032160 0.000000 0.00000 0.00000
## [2,] 0.007869 0.013013 0.038314 0.00000 0.00000
## [3,] 0.004285 0.005418 0.008295 0.05409 0.00000
## [4,] 0.013813 0.016670 0.016313 0.01528 0.05643
```

## 5.7 Dimensionality reduction

```
set.seed(100111)
merged.grun <- runTSNE(merged.grun, dimred="corrected")
```

## 5.8 Clustering

```
snn.gr <- buildSNNGraph(merged.grun, use.dimred="corrected")
colLabels(merged.grun) <- factor(igraph::cluster_walktrap(snn.gr)$membership)
```

```
table(Cluster=colLabels(merged.grun), Donor=merged.grun$batch)
```

```
##        Donor
## Cluster D10 D17  D2  D3  D7
##      1   32  71  31  80  29
##      2    3  10   3   3   7
##      3    1  10   0   0   8
##      4   11  70  28   2  69
##      5   11 119   0   0  55
##      6    3  42   0   0   9
##      7   16  37  15  11  45
##      8   14  30   3   2  66
##      9    5  18   0   2  34
##      10   5  13   0   0  10
##      11   3   2   2   4   2
##      12   4  13   0   0   1
```

```
gridExtra::grid.arrange(
    plotTSNE(merged.grun, colour_by="label"),
    plotTSNE(merged.grun, colour_by="batch"),
    ncol=2
)
```

![Obligatory $t$-SNE plots of the Grun pancreas dataset. Each point represents a cell that is colored by cluster (left) or batch (right).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-grun-human-pancreas-cel-seq2/unref-grun-tsne-1.png)

Figure 5.3: Obligatory \(t\)-SNE plots of the Grun pancreas dataset. Each point represents a cell that is colored by cluster (left) or batch (right).

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
 [1] batchelor_1.28.0            scran_1.40.0               
 [3] scater_1.40.0               ggplot2_4.0.3              
 [5] scuttle_1.22.0              org.Hs.eg.db_3.23.1        
 [7] AnnotationDbi_1.74.0        scRNAseq_2.25.0            
 [9] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
[11] Biobase_2.72.0              GenomicRanges_1.64.0       
[13] Seqinfo_1.2.0               IRanges_2.46.0             
[15] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[17] generics_0.1.4              MatrixGenerics_1.24.0      
[19] matrixStats_1.5.0           BiocStyle_2.40.0           
[21] rebook_1.22.0              

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
 [39] digest_0.6.39             dqrng_0.4.1              
 [41] irlba_2.3.7               ExperimentHub_3.2.0      
 [43] RSQLite_2.4.6             beachmat_2.28.0          
 [45] labeling_0.4.3            filelock_1.0.3           
 [47] httr_1.4.8                abind_1.4-8              
 [49] compiler_4.6.0            bit64_4.8.0              
 [51] withr_3.0.2               S7_0.2.2                 
 [53] BiocParallel_1.46.0       viridis_0.6.5            
 [55] DBI_1.3.0                 HDF5Array_1.40.0         
 [57] alabaster.ranges_1.12.0   alabaster.schemas_1.12.0 
 [59] rappdirs_0.3.4            DelayedArray_0.38.0      
 [61] bluster_1.22.0            rjson_0.2.23             
 [63] tools_4.6.0               vipor_0.4.7              
 [65] otel_0.2.0                beeswarm_0.4.0           
 [67] glue_1.8.1                h5mread_1.4.0            
 [69] restfulr_0.0.16           rhdf5filters_1.24.0      
 [71] grid_4.6.0                Rtsne_0.17               
 [73] cluster_2.1.8.2           gtable_0.3.6             
 [75] ensembldb_2.36.0          metapod_1.20.0           
 [77] BiocSingular_1.28.0       ScaledMatrix_1.20.0      
 [79] XVector_0.52.0            ggrepel_0.9.8            
 [81] BiocVersion_3.23.1        pillar_1.11.1            
 [83] limma_3.68.0              dplyr_1.2.1              
 [85] BiocFileCache_3.2.0       lattice_0.22-9           
 [87] rtracklayer_1.72.0        bit_4.6.0                
 [89] tidyselect_1.2.1          locfit_1.5-9.12          
 [91] Biostrings_2.80.0         knitr_1.51               
 [93] gridExtra_2.3             bookdown_0.46            
 [95] ProtGenerics_1.44.0       edgeR_4.10.0             
 [97] xfun_0.57                 statmod_1.5.1            
 [99] UCSC.utils_1.8.0          lazyeval_0.2.3           
[101] yaml_2.3.12               evaluate_1.0.5           
[103] codetools_0.2-20          cigarillo_1.2.0          
[105] tibble_3.3.1              alabaster.matrix_1.12.0  
[107] BiocManager_1.30.27       graph_1.90.0             
[109] cli_3.6.6                 jquerylib_0.1.4          
[111] dichromat_2.0-0.1         Rcpp_1.1.1-1.1           
[113] GenomeInfoDb_1.48.0       dir.expiry_1.20.0        
[115] dbplyr_2.5.2              png_0.1-9                
[117] XML_3.99-0.23             parallel_4.6.0           
[119] blob_1.3.0                AnnotationFilter_1.36.0  
[121] sparseMatrixStats_1.24.0  bitops_1.0-9             
[123] viridisLite_0.4.3         alabaster.se_1.12.0      
[125] scales_1.4.0              crayon_1.5.3             
[127] rlang_1.2.0               cowplot_1.2.0            
[129] KEGGREST_1.52.0
```

### References

Grun, D., M. J. Muraro, J. C. Boisset, K. Wiebrands, A. Lyubimova, G. Dharmadhikari, M. van den Born, et al. 2016. “De Novo Prediction of Stem Cell Identity using Single-Cell Transcriptome Data.” *Cell Stem Cell* 19 (2): 266–77.
