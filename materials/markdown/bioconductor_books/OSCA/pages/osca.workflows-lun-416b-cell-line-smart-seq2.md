---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/lun-416b-cell-line-smart-seq2.html
ingested_at: 2026-06-04T01:52:20+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 1 Lun 416B cell line (Smart-seq2)

## 1.1 Introduction

The Lun et al. ([2017](https://bioconductor.org/books/3.23/OSCA.workflows/lun-416b-cell-line-smart-seq2.html#ref-lun2017assessing)) dataset contains two 96-well plates of 416B cells (an immortalized mouse myeloid progenitor cell line), processed using the Smart-seq2 protocol (Picelli et al. [2014](https://bioconductor.org/books/3.23/OSCA.workflows/lun-416b-cell-line-smart-seq2.html#ref-picelli2014fulllength)).
A constant amount of spike-in RNA from the External RNA Controls Consortium (ERCC) was also added to each cell’s lysate prior to library preparation.
High-throughput sequencing was performed and the expression of each gene was quantified by counting the total number of reads mapped to its exonic regions.
Similarly, the quantity of each spike-in transcript was measured by counting the number of reads mapped to the spike-in reference sequences.

## 1.2 Data loading

We convert the blocking factor to a `factor` so that downstream steps do not treat it as an integer.

```
library(scRNAseq)
sce.416b <- LunSpikeInData(which="416b") 
sce.416b$block <- factor(sce.416b$block)
```

We rename the rows of our `SingleCellExperiment` with the symbols, reverting to Ensembl identifiers for missing or duplicate symbols.

```
library(AnnotationHub)
ens.mm.v97 <- AnnotationHub()[["AH73905"]]
rowData(sce.416b)$ENSEMBL <- rownames(sce.416b)
rowData(sce.416b)$SYMBOL <- mapIds(ens.mm.v97, keys=rownames(sce.416b),
    keytype="GENEID", column="SYMBOL")
rowData(sce.416b)$SEQNAME <- mapIds(ens.mm.v97, keys=rownames(sce.416b),
    keytype="GENEID", column="SEQNAME")

library(scater)
rownames(sce.416b) <- uniquifyFeatureNames(rowData(sce.416b)$ENSEMBL, 
    rowData(sce.416b)$SYMBOL)
```

## 1.3 Quality control

We save an unfiltered copy of the `SingleCellExperiment` for later use.

```
unfiltered <- sce.416b
```

Technically, we do not need to use the mitochondrial proportions as we already have the spike-in proportions (which serve a similar purpose) for this dataset.
However, it probably doesn’t do any harm to include it anyway.

```
mito <- which(rowData(sce.416b)$SEQNAME=="MT")
stats <- perCellQCMetrics(sce.416b, subsets=list(Mt=mito))
qc <- quickPerCellQC(stats, percent_subsets=c("subsets_Mt_percent",
    "altexps_ERCC_percent"), batch=sce.416b$block)
sce.416b <- sce.416b[,!qc$discard]
```

```
colData(unfiltered) <- cbind(colData(unfiltered), stats)
unfiltered$block <- factor(unfiltered$block)
unfiltered$discard <- qc$discard

gridExtra::grid.arrange(
    plotColData(unfiltered, x="block", y="sum", 
        colour_by="discard") + scale_y_log10() + ggtitle("Total count"),
    plotColData(unfiltered, x="block", y="detected", 
        colour_by="discard") + scale_y_log10() + ggtitle("Detected features"),
    plotColData(unfiltered, x="block", y="subsets_Mt_percent", 
        colour_by="discard") + ggtitle("Mito percent"),
    plotColData(unfiltered, x="block", y="altexps_ERCC_percent", 
        colour_by="discard") + ggtitle("ERCC percent"),
    nrow=2,
    ncol=2
)
```

![Distribution of each QC metric across cells in the 416B dataset, stratified by the plate of origin. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-lun-416b-cell-line-smart-seq2/unref-416b-qc-dist-1.png)

Figure 1.1: Distribution of each QC metric across cells in the 416B dataset, stratified by the plate of origin. Each point represents a cell and is colored according to whether that cell was discarded.

```
gridExtra::grid.arrange(
    plotColData(unfiltered, x="sum", y="subsets_Mt_percent", 
        colour_by="discard") + scale_x_log10(),
    plotColData(unfiltered, x="altexps_ERCC_percent", y="subsets_Mt_percent",
        colour_by="discard"),
    ncol=2
)
```

![Percentage of mitochondrial reads in each cell in the 416B dataset, compared to the total count (left) or the percentage of spike-in reads (right). Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-lun-416b-cell-line-smart-seq2/unref-416b-qc-comp-1.png)

Figure 1.2: Percentage of mitochondrial reads in each cell in the 416B dataset, compared to the total count (left) or the percentage of spike-in reads (right). Each point represents a cell and is colored according to whether that cell was discarded.

We also examine the number of cells removed for each reason.

```
colSums(as.matrix(qc))
```

```
##              low_lib_size            low_n_features   high_subsets_Mt_percent 
##                         5                         0                         2 
## high_altexps_ERCC_percent                   discard 
##                         2                         7
```

## 1.4 Normalization

No pre-clustering is performed here, as the dataset is small and all cells are derived from the same cell line anyway.

```
library(scran)
sce.416b <- computeSumFactors(sce.416b)
sce.416b <- logNormCounts(sce.416b)
```

```
summary(sizeFactors(sce.416b))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.347   0.711   0.921   1.000   1.152   3.604
```

We see that the induced cells have size factors that are systematically shifted from the uninduced cells,
consistent with the presence of a composition bias (Figure [1.3](https://bioconductor.org/books/3.23/OSCA.workflows/lun-416b-cell-line-smart-seq2.html#fig:unref-416b-norm)).

```
plot(librarySizeFactors(sce.416b), sizeFactors(sce.416b), pch=16,
    xlab="Library size factors", ylab="Deconvolution factors", 
    col=c("black", "red")[grepl("induced", sce.416b$phenotype)+1],
    log="xy")
```

![Relationship between the library size factors and the deconvolution size factors in the 416B dataset. Each cell is colored according to its oncogene induction status.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-lun-416b-cell-line-smart-seq2/unref-416b-norm-1.png)

Figure 1.3: Relationship between the library size factors and the deconvolution size factors in the 416B dataset. Each cell is colored according to its oncogene induction status.

## 1.5 Variance modelling

We block on the plate of origin to minimize plate effects,
and then we take the top 10% of genes with the largest biological components.

```
dec.416b <- modelGeneVarWithSpikes(sce.416b, "ERCC", block=sce.416b$block)
chosen.hvgs <- getTopHVGs(dec.416b, prop=0.1)
```

```
par(mfrow=c(1,2))
blocked.stats <- dec.416b$per.block
for (i in colnames(blocked.stats)) {
    current <- blocked.stats[[i]]
    plot(current$mean, current$total, main=i, pch=16, cex=0.5,
        xlab="Mean of log-expression", ylab="Variance of log-expression")
    curfit <- metadata(current)
    points(curfit$mean, curfit$var, col="red", pch=16)
    curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
}
```

![Per-gene variance as a function of the mean for the log-expression values in the 416B dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red). This was performed separately for each plate.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-lun-416b-cell-line-smart-seq2/unref-416b-variance-1.png)

Figure 1.4: Per-gene variance as a function of the mean for the log-expression values in the 416B dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the spike-in transcripts (red). This was performed separately for each plate.

## 1.6 Batch correction

The composition of cells is expected to be the same across the two plates,
hence the use of `removeBatchEffect()` rather than more complex methods.
For larger datasets, consider using `regressBatches()` from the *[batchelor](https://bioconductor.org/packages/3.23/batchelor)* package.

```
library(limma)
assay(sce.416b, "corrected") <- removeBatchEffect(logcounts(sce.416b), 
    design=model.matrix(~sce.416b$phenotype), batch=sce.416b$block)
```

## 1.7 Dimensionality reduction

We do not expect a great deal of heterogeneity in this dataset, so we only request 10 PCs.
We use an exact SVD to avoid warnings from *[irlba](https://CRAN.R-project.org/package=irlba)* about handling small datasets.

```
sce.416b <- runPCA(sce.416b, ncomponents=10, subset_row=chosen.hvgs,
    exprs_values="corrected", BSPARAM=BiocSingular::ExactParam())

set.seed(1010)
sce.416b <- runTSNE(sce.416b, dimred="PCA", perplexity=10)
```

## 1.8 Clustering

```
my.dist <- dist(reducedDim(sce.416b, "PCA"))
my.tree <- hclust(my.dist, method="ward.D2")

library(dynamicTreeCut)
my.clusters <- unname(cutreeDynamic(my.tree, distM=as.matrix(my.dist),
    minClusterSize=10, verbose=0))
colLabels(sce.416b) <- factor(my.clusters)
```

We compare the clusters to the plate of origin.
Each cluster is comprised of cells from both batches, indicating that the clustering is not driven by a batch effect.

```
table(Cluster=colLabels(sce.416b), Plate=sce.416b$block)
```

```
##        Plate
## Cluster 20160113 20160325
##       1       40       38
##       2       37       32
##       3       10       14
##       4        6        8
```

We compare the clusters to the oncogene induction status.
We observe differences in in the composition of each cluster, consistent with a biological effect of oncogene induction.

```
table(Cluster=colLabels(sce.416b), Oncogene=sce.416b$phenotype)
```

```
##        Oncogene
## Cluster induced CBFB-MYH11 oncogene expression wild type phenotype
##       1                                     78                   0
##       2                                      0                  69
##       3                                      1                  23
##       4                                     14                   0
```

```
plotTSNE(sce.416b, colour_by="label")
```

![Obligatory $t$-SNE plot of the 416B dataset, where each point represents a cell and is colored according to the assigned cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-lun-416b-cell-line-smart-seq2/unref-416b-tsne-1.png)

Figure 1.5: Obligatory \(t\)-SNE plot of the 416B dataset, where each point represents a cell and is colored according to the assigned cluster.

Most cells have relatively small positive widths in Figure [1.6](https://bioconductor.org/books/3.23/OSCA.workflows/lun-416b-cell-line-smart-seq2.html#fig:unref-416b-silhouette), indicating that the separation between clusters is weak.
This may be symptomatic of over-clustering where clusters that are clearly defined on oncogene induction status are further split into subsets that are less well separated.
Nonetheless, we will proceed with the current clustering scheme as it provides reasonable partitions for further characterization of heterogeneity.

```
library(cluster)
clust.col <- scater:::.get_palette("tableau10medium") # hidden scater colours
sil <- silhouette(my.clusters, dist = my.dist)
sil.cols <- clust.col[ifelse(sil[,3] > 0, sil[,1], sil[,2])]
sil.cols <- sil.cols[order(-sil[,1], sil[,3])]
plot(sil, main = paste(length(unique(my.clusters)), "clusters"),
    border=sil.cols, col=sil.cols, do.col.sort=FALSE)
```

![Silhouette plot for the hierarchical clustering of the 416B dataset. Each bar represents the silhouette width for a cell and is colored according to the assigned cluster (if positive) or the closest cluster (if negative).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-lun-416b-cell-line-smart-seq2/unref-416b-silhouette-1.png)

Figure 1.6: Silhouette plot for the hierarchical clustering of the 416B dataset. Each bar represents the silhouette width for a cell and is colored according to the assigned cluster (if positive) or the closest cluster (if negative).

## 1.9 Interpretation

```
markers <- findMarkers(sce.416b, my.clusters, block=sce.416b$block)
marker.set <- markers[["1"]]
head(marker.set, 10)
```

```
## DataFrame with 10 rows and 7 columns
##             Top     p.value         FDR summary.logFC   logFC.2   logFC.3
##       <integer>   <numeric>   <numeric>     <numeric> <numeric> <numeric>
## Ccna2         1 9.85422e-67 4.59246e-62      -7.13310  -7.13310  -2.20632
## Cdca8         1 1.01449e-41 1.52514e-38      -7.26175  -6.00378  -2.03841
## Pirb          1 4.16555e-33 1.95516e-30       5.87820   5.28149   5.87820
## Cks1b         2 2.98233e-40 3.23229e-37      -6.43381  -6.43381  -4.15385
## Aurkb         2 2.41436e-64 5.62593e-60      -6.94063  -6.94063  -1.65534
## Myh11         2 1.28865e-46 3.75353e-43       4.38182   4.38182   4.29290
## Mcm6          3 1.15877e-28 3.69887e-26      -5.44558  -5.44558  -5.82130
## Cdca3         3 5.02047e-45 1.23144e-41      -6.22179  -6.22179  -2.10502
## Top2a         3 7.25965e-61 1.12776e-56      -7.07811  -7.07811  -2.39123
## Mcm2          4 1.50854e-33 7.98908e-31      -5.54197  -5.54197  -6.09178
##          logFC.4
##        <numeric>
## Ccna2 -7.3451052
## Cdca8 -7.2617478
## Pirb   0.0352849
## Cks1b -6.4385323
## Aurkb -6.4162126
## Myh11  0.9410499
## Mcm6  -3.5804973
## Cdca3 -7.0539510
## Top2a -6.8297343
## Mcm2  -3.8238103
```

We visualize the expression profiles of the top candidates in Figure [1.7](https://bioconductor.org/books/3.23/OSCA.workflows/lun-416b-cell-line-smart-seq2.html#fig:unref-416b-markers) to verify that the DE signature is robust.
Most of the top markers have strong and consistent up- or downregulation in cells of cluster 1 compared to some or all of the other clusters.
A cursory examination of the heatmap indicates that cluster 1 contains oncogene-induced cells with strong downregulation of DNA replication and cell cycle genes.
This is consistent with the potential induction of senescence as an anti-tumorigenic response (Wajapeyee et al. [2010](https://bioconductor.org/books/3.23/OSCA.workflows/lun-416b-cell-line-smart-seq2.html#ref-wajapeyee2010senescence)).

```
top.markers <- rownames(marker.set)[marker.set$Top <= 10]
plotHeatmap(sce.416b, features=top.markers, order_columns_by="label",
    colour_columns_by=c("label", "block", "phenotype"),
    center=TRUE, symmetric=TRUE, zlim=c(-5, 5))
```

![Heatmap of the top marker genes for cluster 1 in the 416B dataset, stratified by cluster. The plate of origin and oncogene induction status are also shown for each cell.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-lun-416b-cell-line-smart-seq2/unref-416b-markers-1.png)

Figure 1.7: Heatmap of the top marker genes for cluster 1 in the 416B dataset, stratified by cluster. The plate of origin and oncogene induction status are also shown for each cell.

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
 [1] cluster_2.1.8.2             dynamicTreeCut_1.63-1      
 [3] limma_3.68.0                scran_1.40.0               
 [5] scater_1.40.0               ggplot2_4.0.3              
 [7] scuttle_1.22.0              AnnotationHub_4.2.0        
 [9] BiocFileCache_3.2.0         dbplyr_2.5.2               
[11] ensembldb_2.36.0            AnnotationFilter_1.36.0    
[13] GenomicFeatures_1.64.0      AnnotationDbi_1.74.0       
[15] scRNAseq_2.25.0             SingleCellExperiment_1.34.0
[17] SummarizedExperiment_1.42.0 Biobase_2.72.0             
[19] GenomicRanges_1.64.0        Seqinfo_1.2.0              
[21] IRanges_2.46.0              S4Vectors_0.50.0           
[23] BiocGenerics_0.58.0         generics_0.1.4             
[25] MatrixGenerics_1.24.0       matrixStats_1.5.0          
[27] BiocStyle_2.40.0            rebook_1.22.0              

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
 [67] grid_4.6.0               Rtsne_0.17               gtable_0.3.6            
 [70] metapod_1.20.0           BiocSingular_1.28.0      ScaledMatrix_1.20.0     
 [73] XVector_0.52.0           ggrepel_0.9.8            BiocVersion_3.23.1      
 [76] pillar_1.11.1            dplyr_1.2.1              lattice_0.22-9          
 [79] rtracklayer_1.72.0       bit_4.6.0                tidyselect_1.2.1        
 [82] locfit_1.5-9.12          Biostrings_2.80.0        knitr_1.51              
 [85] gridExtra_2.3            bookdown_0.46            ProtGenerics_1.44.0     
 [88] edgeR_4.10.0             xfun_0.57                statmod_1.5.1           
 [91] pheatmap_1.0.13          UCSC.utils_1.8.0         lazyeval_0.2.3          
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

Lun, A. T. L., F. J. Calero-Nieto, L. Haim-Vilmovsky, B. Gottgens, and J. C. Marioni. 2017. “Assessing the reliability of spike-in normalization for analyses of single-cell RNA sequencing data.” *Genome Res.* 27 (11): 1795–1806.

Picelli, S., O. R. Faridani, A. K. Bjorklund, G. Winberg, S. Sagasser, and R. Sandberg. 2014. “Full-length RNA-seq from single cells using Smart-seq2.” *Nat Protoc* 9 (1): 171–81.

Wajapeyee, N., S. Z. Wang, R. W. Serra, P. D. Solomon, A. Nagarajan, X. Zhu, and M. R. Green. 2010. “Senescence induction in human fibroblasts and hematopoietic progenitors by leukemogenic fusion proteins.” *Blood* 115 (24): 5057–60.
