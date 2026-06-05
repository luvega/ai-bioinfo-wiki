---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/segerstolpe-human-pancreas-smart-seq2.html
ingested_at: 2026-06-04T01:52:29+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 8 Segerstolpe human pancreas (Smart-seq2)

## 8.1 Introduction

This performs an analysis of the Segerstolpe et al. ([2016](https://bioconductor.org/books/3.23/OSCA.workflows/segerstolpe-human-pancreas-smart-seq2.html#ref-segerstolpe2016singlecell)) dataset,
consisting of human pancreas cells from various donors.

## 8.2 Data loading

```
library(scRNAseq)
sce.seger <- SegerstolpePancreasData()
```

```
library(AnnotationHub)
edb <- AnnotationHub()[["AH73881"]]
symbols <- rowData(sce.seger)$symbol
ens.id <- mapIds(edb, keys=symbols, keytype="SYMBOL", column="GENEID")
ens.id <- ifelse(is.na(ens.id), symbols, ens.id)

# Removing duplicated rows.
keep <- !duplicated(ens.id)
sce.seger <- sce.seger[keep,]
rownames(sce.seger) <- ens.id[keep]
```

We simplify the names of some of the relevant column metadata fields for ease of access.
Some editing of the cell type labels is necessary for consistency with other data sets.

```
emtab.meta <- colData(sce.seger)[,c("cell type", "disease",
    "individual", "single cell well quality")]
colnames(emtab.meta) <- c("CellType", "Disease", "Donor", "Quality")
colData(sce.seger) <- emtab.meta

sce.seger$CellType <- gsub(" cell", "", sce.seger$CellType)
sce.seger$CellType <- paste0(
    toupper(substr(sce.seger$CellType, 1, 1)),
    substring(sce.seger$CellType, 2))
```

## 8.3 Quality control

```
unfiltered <- sce.seger
```

We remove low quality cells that were marked by the authors.
We then perform additional quality control as some of the remaining cells still have very low counts and numbers of detected features.
For some batches that seem to have a majority of low-quality cells (Figure [8.1](https://bioconductor.org/books/3.23/OSCA.workflows/segerstolpe-human-pancreas-smart-seq2.html#fig:unref-seger-qc-dist)), we use the other batches to define an appropriate threshold via `subset=`.

```
low.qual <- sce.seger$Quality == "OK, filtered"

library(scater)
stats <- perCellQCMetrics(sce.seger)
qc <- quickPerCellQC(stats, percent_subsets="altexps_ERCC_percent",
    batch=sce.seger$Donor,
    subset=!sce.seger$Donor %in% c("H6", "H5"))

sce.seger <- sce.seger[,!(qc$discard | low.qual)]
```

```
colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$discard <- qc$discard

gridExtra::grid.arrange(
    plotColData(unfiltered, x="Donor", y="sum", colour_by="discard") +
        scale_y_log10() + ggtitle("Total count") +
        theme(axis.text.x = element_text(angle = 90)),
    plotColData(unfiltered, x="Donor", y="detected", colour_by="discard") +
        scale_y_log10() + ggtitle("Detected features") +
        theme(axis.text.x = element_text(angle = 90)),
    plotColData(unfiltered, x="Donor", y="altexps_ERCC_percent",
        colour_by="discard") + ggtitle("ERCC percent") +
        theme(axis.text.x = element_text(angle = 90)),
    ncol=2
)
```

![Distribution of each QC metric across cells from each donor of the Segerstolpe pancreas dataset. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-segerstolpe-human-pancreas-smart-seq2/unref-seger-qc-dist-1.png)

Figure 8.1: Distribution of each QC metric across cells from each donor of the Segerstolpe pancreas dataset. Each point represents a cell and is colored according to whether that cell was discarded.

```
colSums(as.matrix(qc))
```

```
##              low_lib_size            low_n_features high_altexps_ERCC_percent 
##                       788                      1056                      1031 
##                   discard 
##                      1246
```

## 8.4 Normalization

We don’t normalize the spike-ins at this point as there are some cells with no spike-in counts.

```
library(scran)
clusters <- quickCluster(sce.seger)
sce.seger <- computeSumFactors(sce.seger, clusters=clusters)
sce.seger <- logNormCounts(sce.seger)
```

```
summary(sizeFactors(sce.seger))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.0141  0.3904  0.7082  1.0000  1.3318 11.1815
```

```
plot(librarySizeFactors(sce.seger), sizeFactors(sce.seger), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the Segerstolpe pancreas dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-segerstolpe-human-pancreas-smart-seq2/unref-seger-norm-1.png)

Figure 8.2: Relationship between the library size factors and the deconvolution size factors in the Segerstolpe pancreas dataset.

## 8.5 Variance modelling

We do not use cells with no spike-ins for variance modelling.
Donor H1 also has very low spike-in counts and is subsequently ignored.

```
for.hvg <- sce.seger[,librarySizeFactors(altExp(sce.seger)) > 0 & sce.seger$Donor!="H1"]
dec.seger <- modelGeneVarWithSpikes(for.hvg, "ERCC", block=for.hvg$Donor)
chosen.hvgs <- getTopHVGs(dec.seger, n=2000)
```

```
par(mfrow=c(3,3))
blocked.stats <- dec.seger$per.block
for (i in colnames(blocked.stats)) {
    current <- blocked.stats[[i]]
    plot(current$mean, current$total, main=i, pch=16, cex=0.5,
        xlab="Mean of log-expression", ylab="Variance of log-expression")
    curfit <- metadata(current)
    points(curfit$mean, curfit$var, col="red", pch=16)
    curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
}
```

![Per-gene variance as a function of the mean for the log-expression values in the Grun pancreas dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red) separately for each donor.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-segerstolpe-human-pancreas-smart-seq2/unref-seger-variance-1.png)

Figure 8.3: Per-gene variance as a function of the mean for the log-expression values in the Grun pancreas dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red) separately for each donor.

## 8.6 Dimensionality reduction

We pick the first 25 PCs for downstream analyses, as it’s a nice square number.

```
library(BiocSingular)
set.seed(101011001)
sce.seger <- runPCA(sce.seger, subset_row=chosen.hvgs, ncomponents=25)
sce.seger <- runTSNE(sce.seger, dimred="PCA")
```

## 8.7 Clustering

```
library(bluster)
clust.out <- clusterRows(reducedDim(sce.seger, "PCA"), NNGraphParam(), full=TRUE)
snn.gr <- clust.out$objects$graph
colLabels(sce.seger) <- clust.out$clusters
```

We see a strong donor effect in Figures [8.4](https://bioconductor.org/books/3.23/OSCA.workflows/segerstolpe-human-pancreas-smart-seq2.html#fig:unref-seger-heat-1) and [5.3](https://bioconductor.org/books/3.23/OSCA.workflows/grun-human-pancreas-cel-seq2.html#fig:unref-grun-tsne).
This might be due to differences in cell type composition between donors,
but the more likely explanation is that of a technical difference in plate processing or uninteresting genotypic differences.
The implication is that we should have called `fastMNN()` at some point.

```
tab <- table(Cluster=colLabels(sce.seger), Donor=sce.seger$Donor)
library(pheatmap)
pheatmap(log10(tab+10), color=viridis::viridis(100))
```

![Heatmap of the frequency of cells from each donor in each cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-segerstolpe-human-pancreas-smart-seq2/unref-seger-heat-1-1.png)

Figure 8.4: Heatmap of the frequency of cells from each donor in each cluster.

```
gridExtra::grid.arrange(
    plotTSNE(sce.seger, colour_by="label"),
    plotTSNE(sce.seger, colour_by="Donor"),
    ncol=2
)
```

![Obligatory $t$-SNE plots of the Segerstolpe pancreas dataset. Each point represents a cell that is colored by cluster (left) or batch (right).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-segerstolpe-human-pancreas-smart-seq2/unref-seger-tsne-1.png)

Figure 8.5: Obligatory \(t\)-SNE plots of the Segerstolpe pancreas dataset. Each point represents a cell that is colored by cluster (left) or batch (right).

## 8.8 Data integration

We repeat the clustering after running `fastMNN()` on the donors.
This yields a more coherent set of clusters in Figure [8.6](https://bioconductor.org/books/3.23/OSCA.workflows/segerstolpe-human-pancreas-smart-seq2.html#fig:unref-seger-tsne-correct) where each cluster contains contributions from all donors.

```
library(batchelor)

set.seed(10001010)
corrected <- fastMNN(sce.seger, batch=sce.seger$Donor, subset.row=chosen.hvgs)

set.seed(10000001)
corrected <- runTSNE(corrected, dimred="corrected")

colLabels(corrected) <- clusterRows(reducedDim(corrected, "corrected"), NNGraphParam())

tab <- table(Cluster=colLabels(corrected), Donor=corrected$batch)
tab
```

```
##        Donor
## Cluster  H1  H2  H3  H4  H5  H6 T2D1 T2D2 T2D3 T2D4
##       1   4  20  80   3   2   4    8   29   24   13
##       2  14  53  37  41  14  19   13   20   11   70
##       3   3  19  67   8  27  11    3   78  124   46
##       4   8  21   2   6  11   6    9    6    5   34
##       5   2   1   0   1   2   9    1    2    2    1
##       6  29 114  26 136  49  72  140  121   85   96
##       7   1   1   2   6   3  10    3   12   13    4
##       8   4  20  16   2   1   8   70    8   10   34
```

```
gridExtra::grid.arrange(
    plotTSNE(corrected, colour_by="label"),
    plotTSNE(corrected, colour_by="batch"),
    ncol=2
)
```

![Yet another $t$-SNE plot of the Segerstolpe dataset, this time after batch correction across donors. Each point represents a cell and is colored by the assigned cluster identity.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-segerstolpe-human-pancreas-smart-seq2/unref-seger-tsne-correct-1.png)

Figure 8.6: Yet another \(t\)-SNE plot of the Segerstolpe dataset, this time after batch correction across donors. Each point represents a cell and is colored by the assigned cluster identity.

## 8.9 Multi-sample comparisons

This particular dataset contains both healthy donors and those with type II diabetes.
It is thus of some interest to identify genes that are differentially expressed upon disease in each cell type.
To keep things simple, we use the author-provided annotation rather than determining the cell type for each of our clusters.

```
summed <- aggregateAcrossCells(sce.seger, 
    ids=colData(sce.seger)[,c("Donor", "CellType")])
summed
```

```
## class: SingleCellExperiment 
## dim: 25454 105 
## metadata(0):
## assays(1): counts
## rownames(25454): ENSG00000118473 ENSG00000142920 ... ENSG00000278306
##   eGFP
## rowData names(2): refseq symbol
## colnames: NULL
## colData names(9): CellType Disease ... CellType ncells
## reducedDimNames(2): PCA TSNE
## mainExpName: endogenous
## altExpNames(0):
```

Here, we will use the `voom` pipeline from the *[limma](https://bioconductor.org/packages/3.23/limma)* package instead of the QL approach with *[edgeR](https://bioconductor.org/packages/3.23/edgeR)*.
This allows us to use sample weights to better account for the variation in the precision of each pseudo-bulk profile.
We see that insulin is downregulated in beta cells in the disease state, which is sensible enough.

```
summed.beta <- summed[,summed$CellType=="Beta"]

library(edgeR)
y.beta <- DGEList(counts(summed.beta), samples=colData(summed.beta),
    genes=rowData(summed.beta)[,"symbol",drop=FALSE])
y.beta <- y.beta[filterByExpr(y.beta, group=y.beta$samples$Disease),]
y.beta <- calcNormFactors(y.beta)

design <- model.matrix(~Disease, y.beta$samples)
v.beta <- voomWithQualityWeights(y.beta, design)
fit.beta <- lmFit(v.beta)
fit.beta <- eBayes(fit.beta, robust=TRUE)

res.beta <- topTable(fit.beta, sort.by="p", n=Inf,
    coef="Diseasetype II diabetes mellitus")
head(res.beta)
```

```
##                    symbol  logFC AveExpr      t   P.Value adj.P.Val     B
## ENSG00000254647       INS -2.780  16.680 -7.679 3.122e-06   0.03819 4.924
## ENSG00000137731     FXYD2 -2.606   7.265 -6.751 1.242e-05   0.07593 3.427
## ENSG00000169297     NR0B1 -2.094   6.790 -5.810 5.586e-05   0.09302 2.028
## ENSG00000181029   TRAPPC5 -2.141   7.046 -5.727 6.422e-05   0.09302 1.959
## ENSG00000105707       HPN -1.805   6.118 -5.672 7.051e-05   0.09302 1.783
## LOC284889       LOC284889 -2.119   6.652 -5.541 8.820e-05   0.09302 1.622
```

We also create some diagnostic plots to check for potential problems in the analysis.
The MA plots exhibit the expected shape (Figure [8.7](https://bioconductor.org/books/3.23/OSCA.workflows/segerstolpe-human-pancreas-smart-seq2.html#fig:unref-ma-plots))
while the differences in the sample weights in Figure [8.8](https://bioconductor.org/books/3.23/OSCA.workflows/segerstolpe-human-pancreas-smart-seq2.html#fig:unref-voom-plots) justify the use of `voom()` in this context.

```
par(mfrow=c(5, 2))
for (i in colnames(y.beta)) {
    plotMD(y.beta, column=i)
}
```

![MA plots for the beta cell pseudo-bulk profiles. Each MA plot is generated by comparing the corresponding pseudo-bulk profile against the average of all other profiles](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-segerstolpe-human-pancreas-smart-seq2/unref-ma-plots-1.png)

Figure 8.7: MA plots for the beta cell pseudo-bulk profiles. Each MA plot is generated by comparing the corresponding pseudo-bulk profile against the average of all other profiles

```
# Easier to just re-run it with plot=TRUE than
# to try to make the plot from 'v.beta'.
voomWithQualityWeights(y.beta, design, plot=TRUE)
```

![Diagnostic plots for `voom` after estimating observation and quality weights from the beta cell pseudo-bulk profiles. The left plot shows the mean-variance trend used to estimate the observation weights, while the right plot shows the per-sample quality weights.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-segerstolpe-human-pancreas-smart-seq2/unref-voom-plots-1.png)

Figure 8.8: Diagnostic plots for `voom` after estimating observation and quality weights from the beta cell pseudo-bulk profiles. The left plot shows the mean-variance trend used to estimate the observation weights, while the right plot shows the per-sample quality weights.

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
 [1] edgeR_4.10.0                limma_3.68.0               
 [3] batchelor_1.28.0            pheatmap_1.0.13            
 [5] bluster_1.22.0              BiocSingular_1.28.0        
 [7] scran_1.40.0                scater_1.40.0              
 [9] ggplot2_4.0.3               scuttle_1.22.0             
[11] ensembldb_2.36.0            AnnotationFilter_1.36.0    
[13] GenomicFeatures_1.64.0      AnnotationDbi_1.74.0       
[15] AnnotationHub_4.2.0         BiocFileCache_3.2.0        
[17] dbplyr_2.5.2                scRNAseq_2.25.0            
[19] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
[21] Biobase_2.72.0              GenomicRanges_1.64.0       
[23] Seqinfo_1.2.0               IRanges_2.46.0             
[25] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[27] generics_0.1.4              MatrixGenerics_1.24.0      
[29] matrixStats_1.5.0           BiocStyle_2.40.0           
[31] rebook_1.22.0              

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
 [59] rjson_0.2.23              tools_4.6.0              
 [61] vipor_0.4.7               otel_0.2.0               
 [63] beeswarm_0.4.0            glue_1.8.1               
 [65] h5mread_1.4.0             restfulr_0.0.16          
 [67] rhdf5filters_1.24.0       grid_4.6.0               
 [69] Rtsne_0.17                cluster_2.1.8.2          
 [71] gtable_0.3.6              metapod_1.20.0           
 [73] ScaledMatrix_1.20.0       XVector_0.52.0           
 [75] ggrepel_0.9.8             BiocVersion_3.23.1       
 [77] pillar_1.11.1             dplyr_1.2.1              
 [79] lattice_0.22-9            rtracklayer_1.72.0       
 [81] bit_4.6.0                 tidyselect_1.2.1         
 [83] locfit_1.5-9.12           Biostrings_2.80.0        
 [85] knitr_1.51                gridExtra_2.3            
 [87] bookdown_0.46             ProtGenerics_1.44.0      
 [89] xfun_0.57                 statmod_1.5.1            
 [91] UCSC.utils_1.8.0          lazyeval_0.2.3           
 [93] yaml_2.3.12               evaluate_1.0.5           
 [95] codetools_0.2-20          cigarillo_1.2.0          
 [97] tibble_3.3.1              alabaster.matrix_1.12.0  
 [99] BiocManager_1.30.27       graph_1.90.0             
[101] cli_3.6.6                 jquerylib_0.1.4          
[103] dichromat_2.0-0.1         Rcpp_1.1.1-1.1           
[105] GenomeInfoDb_1.48.0       dir.expiry_1.20.0        
[107] png_0.1-9                 XML_3.99-0.23            
[109] parallel_4.6.0            blob_1.3.0               
[111] sparseMatrixStats_1.24.0  bitops_1.0-9             
[113] viridisLite_0.4.3         alabaster.se_1.12.0      
[115] scales_1.4.0              purrr_1.2.2              
[117] crayon_1.5.3              rlang_1.2.0              
[119] cowplot_1.2.0             KEGGREST_1.52.0
```

### References

Segerstolpe, A., A. Palasantza, P. Eliasson, E. M. Andersson, A. C. Andreasson, X. Sun, S. Picelli, et al. 2016. “Single-Cell Transcriptome Profiling of Human Pancreatic Islets in Health and Type 2 Diabetes.” *Cell Metab.* 24 (4): 593–607.
