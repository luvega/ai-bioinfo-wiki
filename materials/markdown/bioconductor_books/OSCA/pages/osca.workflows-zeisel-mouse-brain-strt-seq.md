---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/zeisel-mouse-brain-strt-seq.html
ingested_at: 2026-06-04T01:52:24+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 2 Zeisel mouse brain (STRT-Seq)

## 2.1 Introduction

Here, we examine a heterogeneous dataset from a study of cell types in the mouse brain (Zeisel et al. [2015](https://bioconductor.org/books/3.23/OSCA.workflows/zeisel-mouse-brain-strt-seq.html#ref-zeisel2015brain)).
This contains approximately 3000 cells of varying types such as oligodendrocytes, microglia and neurons.
Individual cells were isolated using the Fluidigm C1 microfluidics system (Pollen et al. [2014](https://bioconductor.org/books/3.23/OSCA.workflows/zeisel-mouse-brain-strt-seq.html#ref-pollen2014lowcoverage)) and library preparation was performed on each cell using a UMI-based protocol.
After sequencing, expression was quantified by counting the number of unique molecular identifiers (UMIs) mapped to each gene.

## 2.2 Data loading

We obtain a `SingleCellExperiment` object for this dataset using the relevant function from the *[scRNAseq](https://bioconductor.org/packages/3.23/scRNAseq)* package.
The idiosyncrasies of the published dataset means that we need to do some extra work to merge together redundant rows corresponding to alternative genomic locations for the same gene.

```
library(scRNAseq)
sce.zeisel <- ZeiselBrainData()

library(scater)
sce.zeisel <- aggregateAcrossFeatures(sce.zeisel, 
    id=sub("_loc[0-9]+$", "", rownames(sce.zeisel)))
```

We also fetch the Ensembl gene IDs, just in case we need them later.

```
library(org.Mm.eg.db)
rowData(sce.zeisel)$Ensembl <- mapIds(org.Mm.eg.db, 
    keys=rownames(sce.zeisel), keytype="SYMBOL", column="ENSEMBL")
```

## 2.3 Quality control

```
unfiltered <- sce.zeisel
```

The original authors of the study have already removed low-quality cells prior to data publication.
Nonetheless, we compute some quality control metrics to check whether the remaining cells are satisfactory.

```
stats <- perCellQCMetrics(sce.zeisel, subsets=list(
    Mt=rowData(sce.zeisel)$featureType=="mito"))
qc <- quickPerCellQC(stats, percent_subsets=c("altexps_ERCC_percent", 
    "subsets_Mt_percent"))
sce.zeisel <- sce.zeisel[,!qc$discard]
```

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
    plotColData(unfiltered, y="subsets_Mt_percent",
        colour_by="discard") + ggtitle("Mito percent"),
    ncol=2
)
```

![Distribution of each QC metric across cells in the Zeisel brain dataset. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-zeisel-mouse-brain-strt-seq/unref-zeisel-qc-dist-1.png)

Figure 2.1: Distribution of each QC metric across cells in the Zeisel brain dataset. Each point represents a cell and is colored according to whether that cell was discarded.

```
gridExtra::grid.arrange(
    plotColData(unfiltered, x="sum", y="subsets_Mt_percent",
        colour_by="discard") + scale_x_log10(),
    plotColData(unfiltered, x="altexps_ERCC_percent", y="subsets_Mt_percent",
        colour_by="discard"),
    ncol=2
)
```

![Percentage of mitochondrial reads in each cell in the Zeisel brain dataset, compared to the total count (left) or the percentage of spike-in reads (right). Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-zeisel-mouse-brain-strt-seq/unref-zeisel-qc-comp-1.png)

Figure 2.2: Percentage of mitochondrial reads in each cell in the Zeisel brain dataset, compared to the total count (left) or the percentage of spike-in reads (right). Each point represents a cell and is colored according to whether that cell was discarded.

We also examine the number of cells removed for each reason.

```
colSums(as.matrix(qc))
```

```
##              low_lib_size            low_n_features high_altexps_ERCC_percent 
##                         0                         3                        65 
##   high_subsets_Mt_percent                   discard 
##                       128                       189
```

## 2.4 Normalization

```
library(scran)
set.seed(1000)
clusters <- quickCluster(sce.zeisel)
sce.zeisel <- computeSumFactors(sce.zeisel, cluster=clusters) 
sce.zeisel <- logNormCounts(sce.zeisel)
```

```
summary(sizeFactors(sce.zeisel))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.119   0.486   0.831   1.000   1.321   4.509
```

```
plot(librarySizeFactors(sce.zeisel), sizeFactors(sce.zeisel), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the Zeisel brain dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-zeisel-mouse-brain-strt-seq/unref-zeisel-norm-1.png)

Figure 2.3: Relationship between the library size factors and the deconvolution size factors in the Zeisel brain dataset.

## 2.5 Variance modelling

In theory, we should block on the plate of origin for each cell.
However, only 20-40 cells are available on each plate, and the population is also highly heterogeneous.
This means that we cannot assume that the distribution of sampled cell types on each plate is the same.
Thus, to avoid regressing out potential biology, we will not block on any factors in this analysis.

```
dec.zeisel <- modelGeneVarWithSpikes(sce.zeisel, "ERCC")
top.hvgs <- getTopHVGs(dec.zeisel, prop=0.1)
```

We see from Figure [2.4](https://bioconductor.org/books/3.23/OSCA.workflows/zeisel-mouse-brain-strt-seq.html#fig:unref-zeisel-var) that the technical and total variances are much smaller than those in the read-based datasets.
This is due to the use of UMIs, which reduces the noise caused by variable PCR amplification.
Furthermore, the spike-in trend is consistently lower than the variances of the endogenous gene, which reflects the heterogeneity in gene expression across cells of different types.

```
plot(dec.zeisel$mean, dec.zeisel$total, pch=16, cex=0.5,
    xlab="Mean of log-expression", ylab="Variance of log-expression")
curfit <- metadata(dec.zeisel)
points(curfit$mean, curfit$var, col="red", pch=16)
curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
```

![Per-gene variance as a function of the mean for the log-expression values in the Zeisel brain dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-zeisel-mouse-brain-strt-seq/unref-zeisel-var-1.png)

Figure 2.4: Per-gene variance as a function of the mean for the log-expression values in the Zeisel brain dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red).

## 2.6 Dimensionality reduction

```
library(BiocSingular)
set.seed(101011001)
sce.zeisel <- denoisePCA(sce.zeisel, technical=dec.zeisel, subset.row=top.hvgs)
sce.zeisel <- runTSNE(sce.zeisel, dimred="PCA")
```

We have a look at the number of PCs retained by `denoisePCA()`.

```
ncol(reducedDim(sce.zeisel, "PCA"))
```

```
## [1] 50
```

## 2.7 Clustering

```
snn.gr <- buildSNNGraph(sce.zeisel, use.dimred="PCA")
colLabels(sce.zeisel) <- factor(igraph::cluster_walktrap(snn.gr)$membership)
```

```
table(colLabels(sce.zeisel))
```

```
## 
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14 
## 283 451 114 143 599 167 191 128 350  70 199  58  39  24
```

```
plotTSNE(sce.zeisel, colour_by="label")
```

![Obligatory $t$-SNE plot of the Zeisel brain dataset, where each point represents a cell and is colored according to the assigned cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-zeisel-mouse-brain-strt-seq/unref-zeisel-tsne-1.png)

Figure 2.5: Obligatory \(t\)-SNE plot of the Zeisel brain dataset, where each point represents a cell and is colored according to the assigned cluster.

## 2.8 Interpretation

We focus on upregulated marker genes as these can quickly provide positive identification of cell type in a heterogeneous population.
We examine the table for cluster 1, in which log-fold changes are reported between cluster 1 and every other cluster.
The same output is provided for each cluster in order to identify genes that discriminate between clusters.

```
markers <- findMarkers(sce.zeisel, direction="up")
marker.set <- markers[["1"]]
head(marker.set[,1:8], 10) # only first 8 columns, for brevity
```

```
## DataFrame with 10 rows and 8 columns
##                Top      p.value          FDR summary.logFC   logFC.2   logFC.3
##          <integer>    <numeric>    <numeric>     <numeric> <numeric> <numeric>
## Atp1a3           1 1.45982e-282 7.24035e-279       3.45669 0.0398568 0.0893943
## Celf4            1 2.27030e-246 4.50404e-243       3.10465 0.3886716 0.6145023
## Gad1             1 7.44925e-232 1.34351e-228       4.57719 4.5392751 4.3003280
## Gad2             1 2.88086e-207 3.57208e-204       4.25393 4.2322487 3.8884654
## Mllt11           1 1.72982e-249 3.81309e-246       2.88363 0.5782719 1.4933128
## Ndrg4            1  0.00000e+00  0.00000e+00       3.84337 0.8887239 1.0183408
## Slc32a1          1 2.38276e-110 4.04030e-108       1.92859 1.9196173 1.8252062
## Syngr3           1 3.68257e-143 1.30462e-140       2.55531 1.0981258 1.1994793
## Atp6v1g2         2 3.04451e-204 3.55295e-201       2.50875 0.0981706 0.5203760
## Napb             2 1.10402e-231 1.82522e-228       2.81533 0.1774508 0.3046901
##            logFC.4   logFC.5
##          <numeric> <numeric>
## Atp1a3    1.241388   3.45669
## Celf4     0.869334   3.10465
## Gad1      4.050305   4.47236
## Gad2      3.769556   4.16902
## Mllt11    0.951649   2.88363
## Ndrg4     1.140041   3.84337
## Slc32a1   1.804311   1.92426
## Syngr3    1.188856   2.47696
## Atp6v1g2  0.616391   2.50875
## Napb      0.673772   2.81533
```

Figure [2.6](https://bioconductor.org/books/3.23/OSCA.workflows/zeisel-mouse-brain-strt-seq.html#fig:unref-zeisel-heat-cell) indicates that most of the top markers are strongly DE in cells of cluster 1 compared to some or all of the other clusters.
We can use these markers to identify cells from cluster 1 in validation studies with an independent population of cells.
A quick look at the markers suggest that cluster 1 represents interneurons based on expression of *Gad1* and *Slc6a1* (Zeng et al. [2012](https://bioconductor.org/books/3.23/OSCA.workflows/zeisel-mouse-brain-strt-seq.html#ref-zeng2012largescale)).

```
top.markers <- rownames(marker.set)[marker.set$Top <= 10]
plotHeatmap(sce.zeisel, features=top.markers, order_columns_by="label")
```

![Heatmap of the log-expression of the top markers for cluster 1 compared to each other cluster. Cells are ordered by cluster and the color is scaled to the log-expression of each gene in each cell.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-zeisel-mouse-brain-strt-seq/unref-zeisel-heat-cell-1.png)

Figure 2.6: Heatmap of the log-expression of the top markers for cluster 1 compared to each other cluster. Cells are ordered by cluster and the color is scaled to the log-expression of each gene in each cell.

An alternative visualization approach is to plot the log-fold changes to all other clusters directly (Figure [2.7](https://bioconductor.org/books/3.23/OSCA.workflows/zeisel-mouse-brain-strt-seq.html#fig:unref-zeisel-heat-lfc)).
This is more concise and is useful in situations involving many clusters that contain different numbers of cells.

```
library(pheatmap)
logFCs <- getMarkerEffects(marker.set[1:50,])
pheatmap(logFCs, breaks=seq(-5, 5, length.out=101))
```

![Heatmap of the log-fold changes of the top markers for cluster 1 compared to each other cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-zeisel-mouse-brain-strt-seq/unref-zeisel-heat-lfc-1.png)

Figure 2.7: Heatmap of the log-fold changes of the top markers for cluster 1 compared to each other cluster.

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
 [1] pheatmap_1.0.13             BiocSingular_1.28.0        
 [3] scran_1.40.0                org.Mm.eg.db_3.23.0        
 [5] AnnotationDbi_1.74.0        scater_1.40.0              
 [7] ggplot2_4.0.3               scuttle_1.22.0             
 [9] scRNAseq_2.25.0             SingleCellExperiment_1.34.0
[11] SummarizedExperiment_1.42.0 Biobase_2.72.0             
[13] GenomicRanges_1.64.0        Seqinfo_1.2.0              
[15] IRanges_2.46.0              S4Vectors_0.50.0           
[17] BiocGenerics_0.58.0         generics_0.1.4             
[19] MatrixGenerics_1.24.0       matrixStats_1.5.0          
[21] BiocStyle_2.40.0            rebook_1.22.0              

loaded via a namespace (and not attached):
  [1] RColorBrewer_1.1-3       jsonlite_2.0.0           CodeDepends_0.6.7       
  [4] magrittr_2.0.5           ggbeeswarm_0.7.3         GenomicFeatures_1.64.0  
  [7] gypsum_1.8.0             farver_2.1.2             rmarkdown_2.31          
 [10] BiocIO_1.22.0            vctrs_0.7.3              memoise_2.0.1           
 [13] Rsamtools_2.28.0         RCurl_1.98-1.18          htmltools_0.5.9         
 [16] S4Arrays_1.12.0          AnnotationHub_4.2.0      curl_7.1.0              
 [19] BiocNeighbors_2.6.0      Rhdf5lib_2.0.0           SparseArray_1.12.0      
 [22] rhdf5_2.56.0             sass_0.4.10              alabaster.base_1.12.0   
 [25] bslib_0.10.0             alabaster.sce_1.12.0     httr2_1.2.2             
 [28] cachem_1.1.0             GenomicAlignments_1.48.0 igraph_2.3.0            
 [31] lifecycle_1.0.5          pkgconfig_2.0.3          rsvd_1.0.5              
 [34] Matrix_1.7-5             R6_2.6.1                 fastmap_1.2.0           
 [37] digest_0.6.39            dqrng_0.4.1              irlba_2.3.7             
 [40] ExperimentHub_3.2.0      RSQLite_2.4.6            beachmat_2.28.0         
 [43] labeling_0.4.3           filelock_1.0.3           httr_1.4.8              
 [46] abind_1.4-8              compiler_4.6.0           bit64_4.8.0             
 [49] withr_3.0.2              S7_0.2.2                 BiocParallel_1.46.0     
 [52] viridis_0.6.5            DBI_1.3.0                HDF5Array_1.40.0        
 [55] alabaster.ranges_1.12.0  alabaster.schemas_1.12.0 rappdirs_0.3.4          
 [58] DelayedArray_0.38.0      bluster_1.22.0           rjson_0.2.23            
 [61] tools_4.6.0              vipor_0.4.7              otel_0.2.0              
 [64] beeswarm_0.4.0           glue_1.8.1               h5mread_1.4.0           
 [67] restfulr_0.0.16          rhdf5filters_1.24.0      grid_4.6.0              
 [70] Rtsne_0.17               cluster_2.1.8.2          gtable_0.3.6            
 [73] ensembldb_2.36.0         metapod_1.20.0           ScaledMatrix_1.20.0     
 [76] XVector_0.52.0           ggrepel_0.9.8            BiocVersion_3.23.1      
 [79] pillar_1.11.1            limma_3.68.0             dplyr_1.2.1             
 [82] BiocFileCache_3.2.0      lattice_0.22-9           rtracklayer_1.72.0      
 [85] bit_4.6.0                tidyselect_1.2.1         locfit_1.5-9.12         
 [88] Biostrings_2.80.0        knitr_1.51               gridExtra_2.3           
 [91] bookdown_0.46            ProtGenerics_1.44.0      edgeR_4.10.0            
 [94] xfun_0.57                statmod_1.5.1            UCSC.utils_1.8.0        
 [97] lazyeval_0.2.3           yaml_2.3.12              evaluate_1.0.5          
[100] codetools_0.2-20         cigarillo_1.2.0          tibble_3.3.1            
[103] alabaster.matrix_1.12.0  BiocManager_1.30.27      graph_1.90.0            
[106] cli_3.6.6                jquerylib_0.1.4          dichromat_2.0-0.1       
[109] Rcpp_1.1.1-1.1           GenomeInfoDb_1.48.0      dir.expiry_1.20.0       
[112] dbplyr_2.5.2             png_0.1-9                XML_3.99-0.23           
[115] parallel_4.6.0           blob_1.3.0               AnnotationFilter_1.36.0 
[118] bitops_1.0-9             viridisLite_0.4.3        alabaster.se_1.12.0     
[121] scales_1.4.0             crayon_1.5.3             rlang_1.2.0             
[124] cowplot_1.2.0            KEGGREST_1.52.0
```

### References

Pollen, A. A., T. J. Nowakowski, J. Shuga, X. Wang, A. A. Leyrat, J. H. Lui, N. Li, et al. 2014. “Low-coverage single-cell mRNA sequencing reveals cellular heterogeneity and activated signaling pathways in developing cerebral cortex.” *Nat. Biotechnol.* 32 (10): 1053–8.

Zeisel, A., A. B. Munoz-Manchado, S. Codeluppi, P. Lonnerberg, G. La Manno, A. Jureus, S. Marques, et al. 2015. “Brain structure. Cell types in the mouse cortex and hippocampus revealed by single-cell RNA-seq.” *Science* 347 (6226): 1138–42.

Zeng, H., E. H. Shen, J. G. Hohmann, S. W. Oh, A. Bernard, J. J. Royall, K. J. Glattfelder, et al. 2012. “Large-scale cellular-resolution gene profiling in human neocortex reveals species-specific molecular signatures.” *Cell* 149 (2): 483–96.
