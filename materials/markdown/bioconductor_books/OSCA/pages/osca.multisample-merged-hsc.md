---
source: OSCA
title: "Multi-Sample Single-Cell Analyses with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.multisample/merged-hsc.html
ingested_at: 2026-06-04T01:52:51+00:00
status: source_ingested
---

# [Multi-Sample Single-Cell Analyses with Bioconductor](https://bioconductor.org/books/3.23/OSCA.multisample/)

# Chapter 9 Mouse HSC (multiple technologies)

## 9.1 Introduction

The blood is probably the most well-studied tissue in the single-cell field, mostly because everything is already dissociated “for free”.
Of particular interest has been the use of single-cell genomics to study cell fate decisions in haematopoeisis.
Indeed, it was not long ago that dueling interpretations of haematopoeitic stem cell (HSC) datasets were a mainstay of single-cell conferences.
Sadly, these times have mostly passed so we will instead entertain ourselves by combining a small number of these datasets into a single analysis.

## 9.2 Data loading

View set-up code ([Workflow Chapter 10](http://bioconductor.org/books/3.23/OSCA.workflows/nestorowa-mouse-hsc-smart-seq2.html#nestorowa-mouse-hsc-smart-seq2))

```
#--- data-loading ---#
library(scRNAseq)
sce.nest <- NestorowaHSCData()

#--- gene-annotation ---#
library(AnnotationHub)
ens.mm.v97 <- AnnotationHub()[["AH73905"]]
anno <- select(ens.mm.v97, keys=rownames(sce.nest), 
    keytype="GENEID", columns=c("SYMBOL", "SEQNAME"))
rowData(sce.nest) <- anno[match(rownames(sce.nest), anno$GENEID),]

#--- quality-control ---#
library(scater)
stats <- perCellQCMetrics(sce.nest)
qc <- quickPerCellQC(stats, percent_subsets="altexps_ERCC_percent")
sce.nest <- sce.nest[,!qc$discard]

#--- normalization ---#
library(scran)
set.seed(101000110)
clusters <- quickCluster(sce.nest)
sce.nest <- computeSumFactors(sce.nest, clusters=clusters)
sce.nest <- logNormCounts(sce.nest)

#--- variance-modelling ---#
set.seed(00010101)
dec.nest <- modelGeneVarWithSpikes(sce.nest, "ERCC")
top.nest <- getTopHVGs(dec.nest, prop=0.1)
```

```
sce.nest
```

```
## class: SingleCellExperiment 
## dim: 46078 1656 
## metadata(0):
## assays(2): counts logcounts
## rownames(46078): ENSMUSG00000000001 ENSMUSG00000000003 ...
##   ENSMUSG00000107391 ENSMUSG00000107392
## rowData names(3): GENEID SYMBOL SEQNAME
## colnames(1656): HSPC_025 HSPC_031 ... Prog_852 Prog_810
## colData names(10): gate broad ... metrics sizeFactor
## reducedDimNames(1): diffusion
## mainExpName: endogenous
## altExpNames(2): ERCC FACS
```

The Grun dataset requires a little bit of subsetting and re-analysis to only consider the sorted HSCs.

View set-up code ([Workflow Chapter 9](http://bioconductor.org/books/3.23/OSCA.workflows/grun-mouse-hsc-cel-seq.html#grun-mouse-hsc-cel-seq))

```
#--- data-loading ---#
library(scRNAseq)
sce.grun.hsc <- GrunHSCData(ensembl=TRUE)

#--- gene-annotation ---#
library(AnnotationHub)
ens.mm.v97 <- AnnotationHub()[["AH73905"]]
anno <- select(ens.mm.v97, keys=rownames(sce.grun.hsc), 
    keytype="GENEID", columns=c("SYMBOL", "SEQNAME"))
rowData(sce.grun.hsc) <- anno[match(rownames(sce.grun.hsc), anno$GENEID),]

#--- quality-control ---#
library(scuttle)
stats <- perCellQCMetrics(sce.grun.hsc)
qc <- quickPerCellQC(stats, batch=sce.grun.hsc$protocol,
    subset=grepl("sorted", sce.grun.hsc$protocol))
sce.grun.hsc <- sce.grun.hsc[,!qc$discard]
```

```
library(scuttle)
sce.grun.hsc <- sce.grun.hsc[,sce.grun.hsc$protocol=="sorted hematopoietic stem cells"]
sce.grun.hsc <- logNormCounts(sce.grun.hsc)

set.seed(11001)
library(scran)
dec.grun.hsc <- modelGeneVarByPoisson(sce.grun.hsc)
```

Finally, we will grab the Paul dataset, which we will also subset to only consider the unsorted myeloid population.
This removes the various knockout conditions that just complicates matters.

View set-up code ([Workflow Chapter 11](http://bioconductor.org/books/3.23/OSCA.workflows/paul-mouse-hsc-mars-seq.html#paul-mouse-hsc-mars-seq))

```
#--- data-loading ---#
library(scRNAseq)
sce.paul <- PaulHSCData(ensembl=TRUE)

#--- gene-annotation ---#
library(AnnotationHub)
ens.mm.v97 <- AnnotationHub()[["AH73905"]]
anno <- select(ens.mm.v97, keys=rownames(sce.paul), 
    keytype="GENEID", columns=c("SYMBOL", "SEQNAME"))
rowData(sce.paul) <- anno[match(rownames(sce.paul), anno$GENEID),]

#--- quality-control ---#
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

```
sce.paul <- sce.paul[,sce.paul$Batch_desc=="Unsorted myeloid"]
sce.paul <- logNormCounts(sce.paul)

set.seed(00010010)
dec.paul <- modelGeneVarByPoisson(sce.paul)
```

## 9.3 Setting up the merge

```
common <- Reduce(intersect, list(rownames(sce.nest),
    rownames(sce.grun.hsc), rownames(sce.paul)))
length(common)
```

```
## [1] 17147
```

Combining variances to obtain a single set of HVGs.

```
combined.dec <- combineVar(
    dec.nest[common,], 
    dec.grun.hsc[common,], 
    dec.paul[common,]
)
hvgs <- getTopHVGs(combined.dec, n=5000)
```

Adjusting for gross differences in sequencing depth.

```
library(batchelor)
normed.sce <- multiBatchNorm(
    Nestorowa=sce.nest[common,],
    Grun=sce.grun.hsc[common,],
    Paul=sce.paul[common,]
)
```

## 9.4 Merging the datasets

We turn on `auto.merge=TRUE` to instruct `fastMNN()` to merge the batch that offers the largest number of MNNs.
This aims to perform the “easiest” merges first, i.e., between the most replicate-like batches,
before tackling merges between batches that have greater differences in their population composition.

```
set.seed(1000010)
merged <- fastMNN(normed.sce, subset.row=hvgs, auto.merge=TRUE)
```

Not too much variance lost inside each batch, hopefully.
We also observe that the algorithm chose to merge the more diverse Nestorowa and Paul datasets before dealing with the HSC-only Grun dataset.

```
metadata(merged)$merge.info[,c("left", "right", "lost.var")]
```

```
## DataFrame with 2 rows and 3 columns
##             left     right                        lost.var
##           <List>    <List>                        <matrix>
## 1           Paul Nestorowa 0.01082734:0.0000000:0.00745166
## 2 Paul,Nestorowa      Grun 0.00570326:0.0178387:0.00708292
```

## 9.5 Combined analyses

The Grun dataset does not contribute to many clusters, consistent with a pure undifferentiated HSC population.
Most of the other clusters contain contributions from the Nestorowa and Paul datasets, though some are unique to the Paul dataset.
This may be due to incomplete correction though we tend to think that this are Paul-specific subpopulations,
given that the Nestorowa dataset does not have similarly sized unique clusters that might represent their uncorrected counterparts.

```
library(bluster)
colLabels(merged) <- clusterRows(reducedDim(merged), 
    NNGraphParam(cluster.fun="louvain"))
table(Cluster=colLabels(merged), Batch=merged$batch)
```

```
##        Batch
## Cluster Grun Nestorowa Paul
##      1    32       433   94
##      2    90       226   11
##      3    41       337  125
##      4     0        39  194
##      5     0       161  520
##      6     0       214  448
##      7   128        86  391
##      8     0         6   29
##      9     0       135  214
##      10    0        19    0
##      11    0         0  400
##      12    0         0  379
```

While I prefer \(t\)-SNE plots,
we’ll switch to a UMAP plot to highlight some of the trajectory-like structure across clusters (Figure [9.1](https://bioconductor.org/books/3.23/OSCA.multisample/merged-hsc.html#fig:unref-umap-merged-hsc)).

```
library(scater)
set.seed(101010101)
merged <- runUMAP(merged, dimred="corrected")
gridExtra::grid.arrange(
    plotUMAP(merged, colour_by="label"),
    plotUMAP(merged, colour_by="batch"),
    ncol=2
)
```

![Obligatory UMAP plot of the merged HSC datasets, where each point represents a cell and is colored by the batch of origin (left) or its assigned cluster (right).](../../../../raw/bioconductor_books/assets/OSCA/osca.multisample-merged-hsc/unref-umap-merged-hsc-1.png)

Figure 9.1: Obligatory UMAP plot of the merged HSC datasets, where each point represents a cell and is colored by the batch of origin (left) or its assigned cluster (right).

In fact, we might as well compute a trajectory right now.
*[TSCAN](https://bioconductor.org/packages/3.23/TSCAN)* constructs a reasonable minimum spanning tree but the path choices are somewhat incongruent with the UMAP coordinates (Figure [9.2](https://bioconductor.org/books/3.23/OSCA.multisample/merged-hsc.html#fig:unref-umap-traj-hsc)).
This is most likely due to the fact that *[TSCAN](https://bioconductor.org/packages/3.23/TSCAN)* operates on cluster centroids,
which is simple and efficient but does not consider the variance of cells within each cluster.
It is entirely possible for two well-separated clusters to be closer than two adjacent clusters if the latter span a wider region of the coordinate space.

```
library(TSCAN)
pseudo.out <- quickPseudotime(merged, use.dimred="corrected", outgroup=TRUE)
```

```
common.pseudo <- averagePseudotime(pseudo.out$ordering)
plotUMAP(merged, colour_by=I(common.pseudo), 
        text_by="label", text_colour="red") +
    geom_line(data=pseudo.out$connected$UMAP, 
        mapping=aes(x=UMAP1, y=UMAP2, group=edge))
```

![Another UMAP plot of the merged HSC datasets, where each point represents a cell and is colored by its _TSCAN_ pseudotime. The lines correspond to the edges of the MST across cluster centers.](../../../../raw/bioconductor_books/assets/OSCA/osca.multisample-merged-hsc/unref-umap-traj-hsc-1.png)

Figure 9.2: Another UMAP plot of the merged HSC datasets, where each point represents a cell and is colored by its *TSCAN* pseudotime. The lines correspond to the edges of the MST across cluster centers.

To fix this, we construct the minimum spanning tree using distances based on pairs of mutual nearest neighbors between clusters.
This focuses on the closeness of the boundaries of each pair of clusters rather than their centroids,
ensuring that adjacent clusters are connected even if their centroids are far apart.
Doing so yields a trajectory that is more consistent with the visual connections on the UMAP plot (Figure [9.3](https://bioconductor.org/books/3.23/OSCA.multisample/merged-hsc.html#fig:unref-umap-traj-hsc2)).

```
pseudo.out2 <- quickPseudotime(merged, use.dimred="corrected", 
    dist.method="mnn", outgroup=TRUE)

common.pseudo2 <- averagePseudotime(pseudo.out2$ordering)
plotUMAP(merged, colour_by=I(common.pseudo2), 
        text_by="label", text_colour="red") +
    geom_line(data=pseudo.out2$connected$UMAP, 
        mapping=aes(x=UMAP1, y=UMAP2, group=edge))
```

![Yet another UMAP plot of the merged HSC datasets, where each point represents a cell and is colored by its _TSCAN_ pseudotime. The lines correspond to the edges of the MST across cluster centers.](../../../../raw/bioconductor_books/assets/OSCA/osca.multisample-merged-hsc/unref-umap-traj-hsc2-1.png)

Figure 9.3: Yet another UMAP plot of the merged HSC datasets, where each point represents a cell and is colored by its *TSCAN* pseudotime. The lines correspond to the edges of the MST across cluster centers.

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
 [1] TSCAN_1.50.0                TrajectoryUtils_1.20.0     
 [3] scater_1.40.0               ggplot2_4.0.3              
 [5] bluster_1.22.0              batchelor_1.28.0           
 [7] scran_1.40.0                scuttle_1.22.0             
 [9] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
[11] Biobase_2.72.0              GenomicRanges_1.64.0       
[13] Seqinfo_1.2.0               IRanges_2.46.0             
[15] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[17] generics_0.1.4              MatrixGenerics_1.24.0      
[19] matrixStats_1.5.0           BiocStyle_2.40.0           
[21] rebook_1.22.0              

loaded via a namespace (and not attached):
  [1] bitops_1.0-9              gridExtra_2.3            
  [3] CodeDepends_0.6.7         rlang_1.2.0              
  [5] magrittr_2.0.5            RcppAnnoy_0.0.23         
  [7] otel_0.2.0                compiler_4.6.0           
  [9] mgcv_1.9-4                dir.expiry_1.20.0        
 [11] DelayedMatrixStats_1.34.0 vctrs_0.7.3              
 [13] combinat_0.0-8            pkgconfig_2.0.3          
 [15] fastmap_1.2.0             XVector_0.52.0           
 [17] labeling_0.4.3            caTools_1.18.3           
 [19] promises_1.5.0            rmarkdown_2.31           
 [21] graph_1.90.0              ggbeeswarm_0.7.3         
 [23] xfun_0.57                 cachem_1.1.0             
 [25] beachmat_2.28.0           jsonlite_2.0.0           
 [27] later_1.4.8               DelayedArray_0.38.0      
 [29] BiocParallel_1.46.0       irlba_2.3.7              
 [31] parallel_4.6.0            cluster_2.1.8.2          
 [33] R6_2.6.1                  bslib_0.10.0             
 [35] RColorBrewer_1.1-3        limma_3.68.0             
 [37] jquerylib_0.1.4           Rcpp_1.1.1-1.1           
 [39] bookdown_0.46             knitr_1.51               
 [41] httpuv_1.6.17             splines_4.6.0            
 [43] Matrix_1.7-5              igraph_2.3.0             
 [45] tidyselect_1.2.1          dichromat_2.0-0.1        
 [47] abind_1.4-8               yaml_2.3.12              
 [49] viridis_0.6.5             gplots_3.3.0             
 [51] codetools_0.2-20          plyr_1.8.9               
 [53] lattice_0.22-9            tibble_3.3.1             
 [55] shiny_1.13.0              withr_3.0.2              
 [57] S7_0.2.2                  evaluate_1.0.5           
 [59] mclust_6.1.2              pillar_1.11.1            
 [61] BiocManager_1.30.27       filelock_1.0.3           
 [63] KernSmooth_2.23-26        fastICA_1.2-7            
 [65] sparseMatrixStats_1.24.0  scales_1.4.0             
 [67] xtable_1.8-8              gtools_3.9.5             
 [69] glue_1.8.1                metapod_1.20.0           
 [71] tools_4.6.0               BiocNeighbors_2.6.0      
 [73] ScaledMatrix_1.20.0       locfit_1.5-9.12          
 [75] XML_3.99-0.23             cowplot_1.2.0            
 [77] grid_4.6.0                edgeR_4.10.0             
 [79] nlme_3.1-169              beeswarm_0.4.0           
 [81] BiocSingular_1.28.0       vipor_0.4.7              
 [83] cli_3.6.6                 rsvd_1.0.5               
 [85] rappdirs_0.3.4            S4Arrays_1.12.0          
 [87] viridisLite_0.4.3         dplyr_1.2.1              
 [89] uwot_0.2.4                ResidualMatrix_1.22.0    
 [91] gtable_0.3.6              sass_0.4.10              
 [93] digest_0.6.39             SparseArray_1.12.0       
 [95] ggrepel_0.9.8             dqrng_0.4.1              
 [97] farver_2.1.2              htmltools_0.5.9          
 [99] lifecycle_1.0.5           mime_0.13                
[101] statmod_1.5.1
```
