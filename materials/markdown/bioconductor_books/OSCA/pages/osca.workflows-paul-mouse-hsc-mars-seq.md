---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/paul-mouse-hsc-mars-seq.html
ingested_at: 2026-06-04T01:52:50+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 11 Paul mouse HSC (MARS-seq)

## 11.1 Introduction

This performs an analysis of the mouse haematopoietic stem cell (HSC) dataset generated with MARS-seq (Paul et al. [2015](https://bioconductor.org/books/3.23/OSCA.workflows/paul-mouse-hsc-mars-seq.html#ref-paul2015transcriptional)).
Cells were extracted from multiple mice under different experimental conditions (i.e., sorting protocols) and libraries were prepared using a series of 384-well plates.

## 11.2 Data loading

```
library(scRNAseq)
sce.paul <- PaulHSCData(ensembl=TRUE)
```

```
library(AnnotationHub)
ens.mm.v97 <- AnnotationHub()[["AH73905"]]
anno <- select(ens.mm.v97, keys=rownames(sce.paul), 
    keytype="GENEID", columns=c("SYMBOL", "SEQNAME"))
rowData(sce.paul) <- anno[match(rownames(sce.paul), anno$GENEID),]
```

After loading and annotation, we inspect the resulting `SingleCellExperiment` object:

```
sce.paul
```

```
## class: SingleCellExperiment 
## dim: 17483 10368 
## metadata(0):
## assays(1): counts
## rownames(17483): ENSMUSG00000007777 ENSMUSG00000107002 ...
##   ENSMUSG00000039068 ENSMUSG00000064363
## rowData names(3): GENEID SYMBOL SEQNAME
## colnames(10368): W29953 W29954 ... W76335 W76336
## colData names(12): Seq_batch_ID Amp_batch_ID ... CD34_measurement
##   FcgR3_measurement
## reducedDimNames(0):
## mainExpName: NULL
## altExpNames(0):
```

## 11.3 Quality control

```
unfiltered <- sce.paul
```

For some reason, only one mitochondrial transcripts are available, so we will perform quality control using only the library size and number of detected features.
Ideally, we would simply block on the plate of origin to account for differences in processing, but unfortunately, it seems that many plates have a large proportion (if not outright majority) of cells with poor values for both metrics.
We identify such plates based on the presence of very low outlier thresholds, for some arbitrary definition of “low”; we then redefine thresholds using information from the other (presumably high-quality) plates.

```
library(scater)
stats <- perCellQCMetrics(sce.paul) 
qc <- quickPerCellQC(stats, batch=sce.paul$Plate_ID)

# Detecting batches with unusually low threshold values.
lib.thresholds <- attr(qc$low_lib_size, "thresholds")["lower",]
nfeat.thresholds <- attr(qc$low_n_features, "thresholds")["lower",]
ignore <- union(names(lib.thresholds)[lib.thresholds < 100],
    names(nfeat.thresholds)[nfeat.thresholds < 100])

# Repeating the QC using only the "high-quality" batches.
qc2 <- quickPerCellQC(stats, batch=sce.paul$Plate_ID,
    subset=!sce.paul$Plate_ID %in% ignore)
sce.paul <- sce.paul[,!qc2$discard]
```

We examine the number of cells discarded for each reason.

```
colSums(as.matrix(qc2))
```

```
##   low_lib_size low_n_features        discard 
##           1695           1781           1783
```

We create some diagnostic plots for each metric (Figure [11.1](https://bioconductor.org/books/3.23/OSCA.workflows/paul-mouse-hsc-mars-seq.html#fig:unref-paul-qc-dist)).

```
colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$discard <- qc2$discard
unfiltered$Plate_ID <- factor(unfiltered$Plate_ID)

gridExtra::grid.arrange(
    plotColData(unfiltered, y="sum", x="Plate_ID", colour_by="discard") +
        scale_y_log10() + ggtitle("Total count"),
    plotColData(unfiltered, y="detected", x="Plate_ID", colour_by="discard") +
        scale_y_log10() + ggtitle("Detected features"),
    ncol=1
)
```

![Distribution of each QC metric across cells in the Paul HSC dataset. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-paul-mouse-hsc-mars-seq/unref-paul-qc-dist-1.png)

Figure 11.1: Distribution of each QC metric across cells in the Paul HSC dataset. Each point represents a cell and is colored according to whether that cell was discarded.

## 11.4 Normalization

```
library(scran)
set.seed(101000110)
clusters <- quickCluster(sce.paul)
sce.paul <- computeSumFactors(sce.paul, clusters=clusters)
sce.paul <- logNormCounts(sce.paul)
```

We examine some key metrics for the distribution of size factors, and compare it to the library sizes as a sanity check (Figure [11.2](https://bioconductor.org/books/3.23/OSCA.workflows/paul-mouse-hsc-mars-seq.html#fig:unref-paul-norm)).

```
summary(sizeFactors(sce.paul))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.0568  0.4225  0.7755  1.0000  1.3351  9.6539
```

```
plot(librarySizeFactors(sce.paul), sizeFactors(sce.paul), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the Paul HSC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-paul-mouse-hsc-mars-seq/unref-paul-norm-1.png)

Figure 11.2: Relationship between the library size factors and the deconvolution size factors in the Paul HSC dataset.

## 11.5 Variance modelling

We fit a mean-variance trend to the endogenous genes to detect highly variable genes.
Unfortunately, the plates are confounded with an experimental treatment (`Batch_desc`) so we cannot block on the plate of origin.

```
set.seed(00010101)
dec.paul <- modelGeneVarByPoisson(sce.paul)
top.paul <- getTopHVGs(dec.paul, prop=0.1)
```

```
plot(dec.paul$mean, dec.paul$total, pch=16, cex=0.5, 
    xlab="Mean of log-expression", ylab="Variance of log-expression")
curve(metadata(dec.paul)$trend(x), col="blue", add=TRUE)
```

![Per-gene variance as a function of the mean for the log-expression values in the Paul HSC dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to simulated Poisson noise.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-paul-mouse-hsc-mars-seq/unref-paul-var-1.png)

Figure 11.3: Per-gene variance as a function of the mean for the log-expression values in the Paul HSC dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to simulated Poisson noise.

## 11.6 Dimensionality reduction

```
set.seed(101010011)
sce.paul <- denoisePCA(sce.paul, technical=dec.paul, subset.row=top.paul)
sce.paul <- runTSNE(sce.paul, dimred="PCA")
```

We check that the number of retained PCs is sensible.

```
ncol(reducedDim(sce.paul, "PCA"))
```

```
## [1] 13
```

## 11.7 Clustering

```
snn.gr <- buildSNNGraph(sce.paul, use.dimred="PCA", type="jaccard")
colLabels(sce.paul) <- factor(igraph::cluster_louvain(snn.gr)$membership)
```

These is a strong relationship between the cluster and the experimental treatment (Figure [11.4](https://bioconductor.org/books/3.23/OSCA.workflows/paul-mouse-hsc-mars-seq.html#fig:unref-paul-heat)), which is to be expected.
Of course, this may also be attributable to some batch effect; the confounded nature of the experimental design makes it difficult to make any confident statements either way.

```
tab <- table(colLabels(sce.paul), sce.paul$Batch_desc)
rownames(tab) <- paste("Cluster", rownames(tab))
pheatmap::pheatmap(log10(tab+10), color=viridis::viridis(100))
```

![Heatmap of the distribution of cells across clusters (rows) for each experimental treatment (column).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-paul-mouse-hsc-mars-seq/unref-paul-heat-1.png)

Figure 11.4: Heatmap of the distribution of cells across clusters (rows) for each experimental treatment (column).

```
plotTSNE(sce.paul, colour_by="label")
```

![Obligatory $t$-SNE plot of the Paul HSC dataset, where each point represents a cell and is colored according to the assigned cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-paul-mouse-hsc-mars-seq/unref-paul-tsne-1.png)

Figure 11.5: Obligatory \(t\)-SNE plot of the Paul HSC dataset, where each point represents a cell and is colored according to the assigned cluster.

```
plotTSNE(sce.paul, colour_by="label", other_fields="Batch_desc") + 
    facet_wrap(~Batch_desc)
```

![Obligatory $t$-SNE plot of the Paul HSC dataset faceted by the treatment condition, where each point represents a cell and is colored according to the assigned cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-paul-mouse-hsc-mars-seq/unref-paul-tsne2-1.png)

Figure 11.6: Obligatory \(t\)-SNE plot of the Paul HSC dataset faceted by the treatment condition, where each point represents a cell and is colored according to the assigned cluster.

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
 [1] scran_1.40.0                scater_1.40.0              
 [3] ggplot2_4.0.3               scuttle_1.22.0             
 [5] AnnotationHub_4.2.0         BiocFileCache_3.2.0        
 [7] dbplyr_2.5.2                ensembldb_2.36.0           
 [9] AnnotationFilter_1.36.0     GenomicFeatures_1.64.0     
[11] AnnotationDbi_1.74.0        scRNAseq_2.25.0            
[13] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
[15] Biobase_2.72.0              GenomicRanges_1.64.0       
[17] Seqinfo_1.2.0               IRanges_2.46.0             
[19] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[21] generics_0.1.4              MatrixGenerics_1.24.0      
[23] matrixStats_1.5.0           BiocStyle_2.40.0           
[25] rebook_1.22.0              

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
 [91] xfun_0.57                statmod_1.5.1            pheatmap_1.0.13         
 [94] UCSC.utils_1.8.0         lazyeval_0.2.3           yaml_2.3.12             
 [97] evaluate_1.0.5           codetools_0.2-20         cigarillo_1.2.0         
[100] tibble_3.3.1             alabaster.matrix_1.12.0  BiocManager_1.30.27     
[103] graph_1.90.0             cli_3.6.6                jquerylib_0.1.4         
[106] dichromat_2.0-0.1        Rcpp_1.1.1-1.1           GenomeInfoDb_1.48.0     
[109] dir.expiry_1.20.0        png_0.1-9                XML_3.99-0.23           
[112] parallel_4.6.0           blob_1.3.0               bitops_1.0-9            
[115] viridisLite_0.4.3        alabaster.se_1.12.0      scales_1.4.0            
[118] purrr_1.2.2              crayon_1.5.3             rlang_1.2.0             
[121] cowplot_1.2.0            KEGGREST_1.52.0
```

### References

Paul, F., Y. Arkin, A. Giladi, D. A. Jaitin, E. Kenigsberg, H. Keren-Shaul, D. Winter, et al. 2015. “Transcriptional Heterogeneity and Lineage Commitment in Myeloid Progenitors.” *Cell* 163 (7): 1663–77.
