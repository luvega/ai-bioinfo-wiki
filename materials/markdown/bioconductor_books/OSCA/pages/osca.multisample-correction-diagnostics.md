---
source: OSCA
title: "Multi-Sample Single-Cell Analyses with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.multisample/correction-diagnostics.html
ingested_at: 2026-06-04T01:51:51+00:00
status: source_ingested
---

# [Multi-Sample Single-Cell Analyses with Bioconductor](https://bioconductor.org/books/3.23/OSCA.multisample/)

# Chapter 2 Correction diagnostics

## 2.1 Motivation

Ideally, batch correction would remove the differences between batches while preserving the heterogeneity within batches.
In the corrected data, cells of the same type should be intermingled and indistinguishable even if they come from different batches, while cells of different types should remain well-separated.
Unfortunately, we rarely have prior knowledge of the underlying types of the cells,
making it difficult to unambiguously determine whether differences between batches represent geniune biology or incomplete correction.
Indeed, it could be said that all correction methods are at least somewhat incorrect (Section [6.4.2](https://bioconductor.org/books/3.23/OSCA.multisample/differential-abundance.html#sacrificing-differences)), though that not preclude them from being useful.

In this chapter, we will describe a few diagnostics that, when combined with biological context, can be used to identify potential problems with the correction.
We will recycle the `mnn.out`, `tab.mnn` and `clusters.mnn` objects that were produced in Section [1.6](https://bioconductor.org/books/3.23/OSCA.multisample/integrating-datasets.html#mnn-correction).
For the sake of brevity, we will not reproduce the relevant code - see Chapter [1](https://bioconductor.org/books/3.23/OSCA.multisample/integrating-datasets.html#integrating-datasets) for more details.

```
mnn.out
```

```
## class: SingleCellExperiment 
## dim: 13429 6791 
## metadata(2): merge.info pca.info
## assays(1): reconstructed
## rownames(13429): ENSG00000239945 ENSG00000228463 ... ENSG00000198695
##   ENSG00000198727
## rowData names(1): rotation
## colnames: NULL
## colData names(1): batch
```

```
## reducedDimNames(1): corrected
## mainExpName: NULL
## altExpNames(0):
```

```
tab.mnn
```

```
##        Batch
## Cluster   1   2
##      1  337 606
##      2  152 181
##      3  261 505
##      4   12   4
##      5  655 589
##      6   13  10
##      7  303 655
##      8  169 115
##      9   11  55
##      10  17  66
##      11  19  62
##      12  92 219
##      13 144  92
##      14 416 979
##      15   4  36
##      16   4   8
```

## 2.2 Mixing between batches

The simplest way to quantify the degree of mixing across batches is to test each cluster for imbalances in the contribution from each batch (Büttner et al. [2019](https://bioconductor.org/books/3.23/OSCA.multisample/correction-diagnostics.html#ref-buttner2019test)).
This is done by applying Pearson’s chi-squared test to each row of `tab.mnn` where the expected proportions under the null hypothesis proportional to the total number of cells per batch.
Low \(p\)-values indicate that there are significant imbalances
In practice, this strategy is most suited to experiments where the batches are technical replicates with identical population composition;
it is usually too stringent for batches with more biological variation, where proportions can genuinely vary even in the absence of any batch effect.

```
library(batchelor)
p.values <- clusterAbundanceTest(tab.mnn)
p.values
```

```
##         1         2         3         4         5         6         7         8 
## 9.047e-02 6.700e-03 1.341e-02 2.627e-03 5.625e-25 7.427e-02 1.555e-05 2.742e-13 
##         9        10        11        12        13        14        15        16 
## 2.801e-04 7.807e-04 5.633e-03 1.356e-03 9.512e-13 4.057e-11 2.197e-04 7.172e-01
```

We favor a more qualitative approach where we compute the variance in the log-normalized abundances across batches for each cluster.
A highly variable cluster has large relative differences in cell abundance across batches;
this may be an indicator for incomplete batch correction, e.g., if the same cell type in two batches was not combined into a single cluster in the corrected data.
We can then focus our attention on these clusters to determine whether they might pose a problem for downstream interpretation.
Of course, a large variance can also be caused by genuinely batch-specific populations,
so some prior knowledge about the biological context is necessary to distinguish between these two possibilities.
For the PBMC dataset, none of the most variable clusters are overtly batch-specific, consistent with the fact that our batches are effectively replicates.

```
rv <- clusterAbundanceVar(tab.mnn)

# Also printing the percentage of cells in each cluster in each batch:
percent <- t(t(tab.mnn)/colSums(tab.mnn)) * 100 
df <- DataFrame(Batch=unclass(percent), var=rv)
df[order(df$var, decreasing=TRUE),]
```

```
## DataFrame with 16 rows and 3 columns
##       Batch.1   Batch.2        var
##     <numeric> <numeric>  <numeric>
## 15   0.153315  0.860832   0.934778
## 13   5.519356  2.199904   0.745173
## 9    0.421617  1.315160   0.682672
## 8    6.477578  2.749880   0.665221
## 10   0.651591  1.578192   0.485170
## ...       ...       ...        ...
## 7   11.613645 15.662363 0.08913828
## 2    5.825987  4.328073 0.08199220
## 3   10.003833 12.075562 0.03496472
## 1   12.916826 14.490674 0.01318296
## 16   0.153315  0.191296 0.00689661
```

## 2.3 Preserving biological heterogeneity

Another useful diagnostic check is to compare the pre-correction clustering of each batch to the clustering of the same cells in the corrected data.
Accurate data integration should preserve population structure within each batch as there is no batch effect to remove between cells in the same batch.
This check complements the previously mentioned diagnostics that only focus on the removal of differences between batches.
Specifically, it protects us against scenarios where the correction method simply aggregates all cells together, which would achieve perfect mixing but also discard the biological heterogeneity of interest.
To illustrate, we will use clustering results from the analysis of each batch of the PBMC dataset:

View set-up code (Chapter [7](https://bioconductor.org/books/3.23/OSCA.multisample/human-pbmcs-10x-genomics.html#human-pbmcs-10x-genomics))

```
#--- loading ---#
library(TENxPBMCData)
all.sce <- list(
    pbmc3k=TENxPBMCData('pbmc3k'),
    pbmc4k=TENxPBMCData('pbmc4k'),
    pbmc8k=TENxPBMCData('pbmc8k')
)

#--- quality-control ---#
library(scater)
stats <- high.mito <- list()
for (n in names(all.sce)) {
    current <- all.sce[[n]]
    is.mito <- grep("MT", rowData(current)$Symbol_TENx)
    stats[[n]] <- perCellQCMetrics(current, subsets=list(Mito=is.mito))
    high.mito[[n]] <- isOutlier(stats[[n]]$subsets_Mito_percent, type="higher")
    all.sce[[n]] <- current[,!high.mito[[n]]]
}

#--- normalization ---#
all.sce <- lapply(all.sce, logNormCounts)

#--- variance-modelling ---#
library(scran)
all.dec <- lapply(all.sce, modelGeneVar)
all.hvgs <- lapply(all.dec, getTopHVGs, prop=0.1)

#--- dimensionality-reduction ---#
library(BiocSingular)
set.seed(10000)
all.sce <- mapply(FUN=runPCA, x=all.sce, subset_row=all.hvgs, 
    MoreArgs=list(ncomponents=25, BSPARAM=RandomParam()), 
    SIMPLIFY=FALSE)

set.seed(100000)
all.sce <- lapply(all.sce, runTSNE, dimred="PCA")

set.seed(1000000)
all.sce <- lapply(all.sce, runUMAP, dimred="PCA")

#--- clustering ---#
for (n in names(all.sce)) {
    g <- buildSNNGraph(all.sce[[n]], k=10, use.dimred='PCA')
    clust <- igraph::cluster_walktrap(g)$membership
    colLabels(all.sce[[n]])  <- factor(clust)
}
```

```
pbmc3k <- all.sce$pbmc3k
table(colLabels(pbmc3k))
```

```
## 
##   1   2   3   4   5   6   7   8   9  10 
## 475 636 153 476 164  31 159 164 340  11
```

```
pbmc4k <- all.sce$pbmc4k
table(colLabels(pbmc4k))
```

```
## 
##   1   2   3   4   5   6   7   8   9  10  11  12 
## 127 594 518 775 211 394 187 993  55 201  91  36
```

Ideally, we should see a many-to-1 mapping where the post-correction clustering is nested inside the pre-correction clustering.
This indicates that any within-batch structure was preserved after correction while acknowledging that greater resolution is possible with more cells.
We quantify this mapping using the `nestedClusters()` function from the *[bluster](https://bioconductor.org/packages/3.23/bluster)* package,
which identifies the nesting of post-correction clusters within the pre-correction clusters.
Well-nested clusters have high `max` values, indicating that most of their cells are derived from a single pre-correction cluster.

```
library(bluster)
tab3k <- nestedClusters(ref=paste("before", colLabels(pbmc3k)),
    alt=paste("after", clusters.mnn[mnn.out$batch==1]))
tab3k$alt.mapping
```

```
## DataFrame with 16 rows and 2 columns
##                max       which
##          <numeric> <character>
## after 1   0.994065    before 9
## after 10  0.647059    before 6
## after 11  1.000000    before 6
## after 12  0.945652    before 2
## after 13  1.000000    before 7
## ...            ...         ...
## after 5   0.697710    before 4
## after 6   0.692308    before 4
## after 7   0.996700    before 1
## after 8   0.923077    before 1
## after 9   1.000000    before 1
```

We can visualize this mapping for the PBMC dataset in Figure [2.1](https://bioconductor.org/books/3.23/OSCA.multisample/correction-diagnostics.html#fig:heat-after-mnn).
Ideally, each row should have a single dominant entry close to unity.
Horizontal stripes are more concerning as these indicate that multiple pre-correction clusters were merged together,
though the exact level of concern will depend on whether specific clusters of interest are gained or lost.
In practice, more discrepancies can be expected even when the correction is perfect, due to the existence of closely related clusters that were arbitrarily separated in the within-batch clustering.

```
library(pheatmap)

# For the first batch:
heat3k <- pheatmap(tab3k$proportions, cluster_row=FALSE, cluster_col=FALSE,
                   main="PBMC 3K comparison", silent=TRUE)

# For the second batch:
tab4k <- nestedClusters(ref=paste("before", colLabels(pbmc4k)),
                        alt=paste("after", clusters.mnn[mnn.out$batch==2]))
heat4k <- pheatmap(tab4k$proportions, cluster_row=FALSE, cluster_col=FALSE,
                   main="PBMC 4K comparison", silent=TRUE)

gridExtra::grid.arrange(heat3k[[4]], heat4k[[4]])
```

![Comparison between the clusterings obtained before (columns) and after MNN correction (rows). One heatmap is generated for each of the PBMC 3K and 4K datasets, where each entry is colored according to the proportion of cells distributed along each row (i.e., the row sums equal unity).](../../../../raw/bioconductor_books/assets/OSCA/osca.multisample-correction-diagnostics/heat-after-mnn-1.png)

Figure 2.1: Comparison between the clusterings obtained before (columns) and after MNN correction (rows). One heatmap is generated for each of the PBMC 3K and 4K datasets, where each entry is colored according to the proportion of cells distributed along each row (i.e., the row sums equal unity).

We use the adjusted Rand index ([Advanced Section 5.3](http://bioconductor.org/books/3.23/OSCA.advanced/clustering-redux.html#comparing-different-clusterings))
to quantify the agreement between the clusterings before and after batch correction.
Recall that larger indices are more desirable as this indicates that within-batch heterogeneity is preserved,
though this must be balanced against the ability of each method to actually perform batch correction.

```
library(bluster)
ri3k <- pairwiseRand(clusters.mnn[mnn.out$batch==1], colLabels(pbmc3k), mode="index")
ri3k
```

```
## [1] 0.6482
```

```
ri4k <- pairwiseRand(clusters.mnn[mnn.out$batch==2], colLabels(pbmc4k), mode="index")
ri4k
```

```
## [1] 0.8335
```

We can also break down the ARI into per-cluster ratios for more detailed diagnostics (Figure [2.2](https://bioconductor.org/books/3.23/OSCA.multisample/correction-diagnostics.html#fig:rand-after-mnn)).
For example, we could see low ratios off the diagonal if distinct clusters in the within-batch clustering were incorrectly aggregated in the merged clustering.
Conversely, we might see low ratios on the diagonal if the correction inflated or introduced spurious heterogeneity inside a within-batch cluster.

```
# For the first batch.
tab <- pairwiseRand(colLabels(pbmc3k), clusters.mnn[mnn.out$batch==1])
heat3k <- pheatmap(tab, cluster_row=FALSE, cluster_col=FALSE,
    col=rev(viridis::magma(100)), main="PBMC 3K probabilities", silent=TRUE)

# For the second batch.
tab <- pairwiseRand(colLabels(pbmc4k), clusters.mnn[mnn.out$batch==2])
heat4k <- pheatmap(tab, cluster_row=FALSE, cluster_col=FALSE,
    col=rev(viridis::magma(100)), main="PBMC 4K probabilities", silent=TRUE)

gridExtra::grid.arrange(heat3k[[4]], heat4k[[4]])
```

![ARI-derived ratios for the within-batch clusters after comparison to the merged clusters obtained after MNN correction. One heatmap is generated for each of the PBMC 3K and 4K datasets.](../../../../raw/bioconductor_books/assets/OSCA/osca.multisample-correction-diagnostics/rand-after-mnn-1.png)

Figure 2.2: ARI-derived ratios for the within-batch clusters after comparison to the merged clusters obtained after MNN correction. One heatmap is generated for each of the PBMC 3K and 4K datasets.

## 2.4 MNN-specific diagnostics

For `fastMNN()`, one useful diagnostic is the proportion of variance within each batch that is lost during MNN correction.
Specifically, this refers to the within-batch variance that is removed during orthogonalization with respect to the average correction vector at each merge step.
This is returned via the `lost.var` field in the metadata of `mnn.out`, which contains a matrix of the variance lost in each batch (column) at each merge step (row).

```
metadata(mnn.out)$merge.info$lost.var
```

```
##          [,1]     [,2]
## [1,] 0.006529 0.003314
```

Large proportions of lost variance (>10%) suggest that correction is removing genuine biological heterogeneity.
This would occur due to violations of the assumption of orthogonality between the batch effect and the biological subspace (Haghverdi et al. [2018](https://bioconductor.org/books/3.23/OSCA.multisample/correction-diagnostics.html#ref-haghverdi2018batch)).
In this case, the proportion of lost variance is small, indicating that non-orthogonality is not a major concern.

Another MNN-related diagnostic involves examining the variance in the differences in expression between MNN pairs.
A small variance indicates that the correction had little effect - either there was no batch effect, or any batch effect was simply a constant shift across all cells.
On the other hand, a large variance indicates that the correction was highly non-linear, most likely involving subpopulation-specific batch effects.
This computation is achieved using the `mnnDeltaVariance()` function on the MNN pairings produced by `fastMNN()`.

```
library(batchelor)
common <- rownames(mnn.out)
vars <- mnnDeltaVariance(pbmc3k[common,], pbmc4k[common,], 
   pairs=metadata(mnn.out)$merge.info$pairs)
vars[order(vars$adjusted, decreasing=TRUE),]
```

```
## DataFrame with 13429 rows and 4 columns
##                      mean     total     trend  adjusted
##                 <numeric> <numeric> <numeric> <numeric>
## ENSG00000111796  0.405882  1.493872  0.659707  0.834166
## ENSG00000257764  0.320745  1.046425  0.548442  0.497983
## ENSG00000170345  2.542949  1.341653  0.950599  0.391054
## ENSG00000187118  0.313330  0.917087  0.538035  0.379052
## ENSG00000177606  1.801539  1.404074  1.035127  0.368946
## ...                   ...       ...       ...       ...
## ENSG00000204472  0.794696  0.538555  0.982401 -0.443846
## ENSG00000011600  1.174530  0.629559  1.074839 -0.445280
## ENSG00000101439  1.133495  0.628259  1.073971 -0.445712
## ENSG00000158869  0.926005  0.577047  1.038913 -0.461866
## ENSG00000105374  1.220880  0.535073  1.074666 -0.539593
```

Such genes with large variances are particularly interesting as they exhibit complex differences between batches that may reflect real biology.
For example, in Figure [2.3](https://bioconductor.org/books/3.23/OSCA.multisample/correction-diagnostics.html#fig:mnn-delta-var-pbmc), the *KLRB1*-positive clusters in the second batch lack any counterpart in the first batch, despite the two batches being replicates.
This may represent some kind of batch-specific state in two otherwise identical populations, though whether this is biological or technical in nature is open for interpretation.

```
library(scater)
top <- rownames(vars)[order(vars$adjusted, decreasing=TRUE)[1]]
gridExtra::grid.arrange(
    plotExpression(pbmc3k, x="label", features=top) + ggtitle("3k"),
    plotExpression(pbmc4k, x="label", features=top) + ggtitle("4k"),
    ncol=2
)
```

![Distribution of the expression of the gene with the largest variance of MNN pair differences in each batch of the the PBMC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.multisample-correction-diagnostics/mnn-delta-var-pbmc-1.png)

Figure 2.3: Distribution of the expression of the gene with the largest variance of MNN pair differences in each batch of the the PBMC dataset.

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
 [1] scater_1.40.0               ggplot2_4.0.3              
 [3] scuttle_1.22.0              pheatmap_1.0.13            
 [5] bluster_1.22.0              batchelor_1.28.0           
 [7] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
 [9] Biobase_2.72.0              GenomicRanges_1.64.0       
[11] Seqinfo_1.2.0               IRanges_2.46.0             
[13] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[15] generics_0.1.4              MatrixGenerics_1.24.0      
[17] matrixStats_1.5.0           BiocStyle_2.40.0           
[19] rebook_1.22.0              

loaded via a namespace (and not attached):
 [1] gridExtra_2.3             CodeDepends_0.6.7        
 [3] rlang_1.2.0               magrittr_2.0.5           
 [5] otel_0.2.0                compiler_4.6.0           
 [7] dir.expiry_1.20.0         DelayedMatrixStats_1.34.0
 [9] vctrs_0.7.3               pkgconfig_2.0.3          
[11] fastmap_1.2.0             XVector_0.52.0           
[13] labeling_0.4.3            rmarkdown_2.31           
[15] graph_1.90.0              ggbeeswarm_0.7.3         
[17] xfun_0.57                 cachem_1.1.0             
[19] beachmat_2.28.0           jsonlite_2.0.0           
[21] rhdf5filters_1.24.0       DelayedArray_0.38.0      
[23] Rhdf5lib_2.0.0            BiocParallel_1.46.0      
[25] irlba_2.3.7               parallel_4.6.0           
[27] cluster_2.1.8.2           R6_2.6.1                 
[29] bslib_0.10.0              RColorBrewer_1.1-3       
[31] limma_3.68.0              jquerylib_0.1.4          
[33] Rcpp_1.1.1-1.1            bookdown_0.46            
[35] knitr_1.51                Matrix_1.7-5             
[37] igraph_2.3.0              tidyselect_1.2.1         
[39] dichromat_2.0-0.1         abind_1.4-8              
[41] yaml_2.3.12               viridis_0.6.5            
[43] codetools_0.2-20          lattice_0.22-9           
[45] tibble_3.3.1              withr_3.0.2              
[47] S7_0.2.2                  evaluate_1.0.5           
[49] pillar_1.11.1             BiocManager_1.30.27      
[51] filelock_1.0.3            sparseMatrixStats_1.24.0 
[53] scales_1.4.0              glue_1.8.1               
[55] metapod_1.20.0            tools_4.6.0              
[57] BiocNeighbors_2.6.0       ScaledMatrix_1.20.0      
[59] locfit_1.5-9.12           scran_1.40.0             
[61] XML_3.99-0.23             cowplot_1.2.0            
[63] rhdf5_2.56.0              grid_4.6.0               
[65] edgeR_4.10.0              beeswarm_0.4.0           
[67] BiocSingular_1.28.0       HDF5Array_1.40.0         
[69] vipor_0.4.7               cli_3.6.6                
[71] rsvd_1.0.5                S4Arrays_1.12.0          
[73] viridisLite_0.4.3         dplyr_1.2.1              
[75] ResidualMatrix_1.22.0     gtable_0.3.6             
[77] sass_0.4.10               digest_0.6.39            
[79] ggrepel_0.9.8             SparseArray_1.12.0       
[81] dqrng_0.4.1               farver_2.1.2             
[83] htmltools_0.5.9           lifecycle_1.0.5          
[85] h5mread_1.4.0             statmod_1.5.1
```

### References

Büttner, Maren, Zhichao Miao, F Alexander Wolf, Sarah A Teichmann, and Fabian J Theis. 2019. “A Test Metric for Assessing Single-Cell Rna-Seq Batch Correction.” *Nature Methods* 16 (1): 43–49.

Haghverdi, L., A. T. L. Lun, M. D. Morgan, and J. C. Marioni. 2018. “Batch effects in single-cell RNA-sequencing data are corrected by matching mutual nearest neighbors.” *Nat. Biotechnol.* 36 (5): 421–27.
