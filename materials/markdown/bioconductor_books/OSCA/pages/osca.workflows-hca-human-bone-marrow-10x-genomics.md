---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/hca-human-bone-marrow-10x-genomics.html
ingested_at: 2026-06-04T01:52:15+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 14 HCA human bone marrow (10X Genomics)

## 14.1 Introduction

Here, we use an example dataset from the [Human Cell Atlas immune cell profiling project on bone marrow](https://preview.data.humancellatlas.org), which contains scRNA-seq data for 380,000 cells generated using the 10X Genomics technology.
This is a fairly big dataset that represents a good use case for the techniques in [Advanced Chapter 14](http://bioconductor.org/books/3.23/OSCA.advanced/dealing-with-big-data.html#dealing-with-big-data).

## 14.2 Data loading

This dataset is loaded via the *[HCAData](https://bioconductor.org/packages/3.23/HCAData)* package, which provides a ready-to-use `SingleCellExperiment` object.

```
library(HCAData)
sce.bone <- HCAData('ica_bone_marrow', as.sparse=TRUE)
sce.bone$Donor <- sub("_.*", "", sce.bone$Barcode)
```

We use symbols in place of IDs for easier interpretation later.

```
library(EnsDb.Hsapiens.v86)
rowData(sce.bone)$Chr <- mapIds(EnsDb.Hsapiens.v86, keys=rownames(sce.bone),
    column="SEQNAME", keytype="GENEID")

library(scater)
rownames(sce.bone) <- uniquifyFeatureNames(rowData(sce.bone)$ID,
    names = rowData(sce.bone)$Symbol)
```

## 14.3 Quality control

Cell calling was not performed (see [here](https://s3.amazonaws.com/preview-ica-expression-data/Brief+ICA+Read+Me.pdf)) so we will perform QC using all metrics and block on the donor of origin during outlier detection.
We perform the calculation across multiple cores to speed things up.

```
library(BiocParallel)
bpp <- MulticoreParam(8)
sce.bone <- unfiltered <- addPerCellQC(sce.bone, BPPARAM=bpp,
    subsets=list(Mito=which(rowData(sce.bone)$Chr=="MT")))

qc <- quickPerCellQC(colData(sce.bone), batch=sce.bone$Donor,
    sub.fields="subsets_Mito_percent")
sce.bone <- sce.bone[,!qc$discard]
```

```
unfiltered$discard <- qc$discard

gridExtra::grid.arrange(
    plotColData(unfiltered, x="Donor", y="sum", colour_by="discard") +
        scale_y_log10() + ggtitle("Total count"),
    plotColData(unfiltered, x="Donor", y="detected", colour_by="discard") +
        scale_y_log10() + ggtitle("Detected features"),
    plotColData(unfiltered, x="Donor", y="subsets_Mito_percent",
        colour_by="discard") + ggtitle("Mito percent"),
    ncol=2
)
```

![Distribution of QC metrics in the HCA bone marrow dataset. Each point represents a cell and is colored according to whether it was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-hca-human-bone-marrow-10x-genomics/unref-hca-bone-qc-1.png)

Figure 14.1: Distribution of QC metrics in the HCA bone marrow dataset. Each point represents a cell and is colored according to whether it was discarded.

```
plotColData(unfiltered, x="sum", y="subsets_Mito_percent", 
    colour_by="discard") + scale_x_log10()
```

![Percentage of mitochondrial reads in each cell in the HCA bone marrow dataset compared to its total count. Each point represents a cell and is colored according to whether that cell was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-hca-human-bone-marrow-10x-genomics/unref-hca-bone-mito-1.png)

Figure 14.2: Percentage of mitochondrial reads in each cell in the HCA bone marrow dataset compared to its total count. Each point represents a cell and is colored according to whether that cell was discarded.

## 14.4 Normalization

For a minor speed-up, we use already-computed library sizes rather than re-computing them from the column sums.

```
sce.bone <- logNormCounts(sce.bone, size_factors = sce.bone$sum)
```

```
summary(sizeFactors(sce.bone))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##  0.0489  0.4699  0.6479  1.0000  0.8893 42.3813
```

## 14.5 Variance modeling

We block on the donor of origin to mitigate batch effects during HVG selection.
We select a larger number of HVGs to capture any batch-specific variation that might be present.

```
library(scran)
set.seed(1010010101)
dec.bone <- modelGeneVarByPoisson(sce.bone, 
    block=sce.bone$Donor, BPPARAM=bpp)
top.bone <- getTopHVGs(dec.bone, n=5000)
```

```
par(mfrow=c(4,2))
blocked.stats <- dec.bone$per.block
for (i in colnames(blocked.stats)) {
    current <- blocked.stats[[i]]
    plot(current$mean, current$total, main=i, pch=16, cex=0.5,
        xlab="Mean of log-expression", ylab="Variance of log-expression")
    curfit <- metadata(current)
    curve(curfit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
}
```

![Per-gene variance as a function of the mean for the log-expression values in the HCA bone marrow dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the variances.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-hca-human-bone-marrow-10x-genomics/unref-hca-bone-var-1.png)

Figure 14.3: Per-gene variance as a function of the mean for the log-expression values in the HCA bone marrow dataset. Each point represents a gene (black) with the mean-variance trend (blue) fitted to the variances.

## 14.6 Data integration

Here we use multiple cores, randomized SVD[1](https://bioconductor.org/books/3.23/OSCA.workflows/hca-human-bone-marrow-10x-genomics.html#fn1) and approximate nearest-neighbor detection to speed up this step.

```
library(batchelor)
library(BiocNeighbors)

set.seed(1010001)
merged.bone <- fastMNN(sce.bone, batch = sce.bone$Donor, subset.row = top.bone,
     BSPARAM=BiocSingular::RandomParam(deferred = TRUE), 
     BNPARAM=AnnoyParam(),
     BPPARAM=bpp)

reducedDim(sce.bone, 'MNN') <- reducedDim(merged.bone, 'corrected')
```

We use the percentage of variance lost as a diagnostic measure:

```
metadata(merged.bone)$merge.info$lost.var
```

```
##      MantonBM1 MantonBM2 MantonBM3 MantonBM4 MantonBM5 MantonBM6 MantonBM7
## [1,]  0.007133  0.006508  0.000000  0.000000  0.000000  0.000000  0.000000
## [2,]  0.006314  0.006883  0.023528  0.000000  0.000000  0.000000  0.000000
## [3,]  0.005117  0.003096  0.005115  0.019703  0.000000  0.000000  0.000000
## [4,]  0.001991  0.001888  0.001890  0.001766  0.023451  0.000000  0.000000
## [5,]  0.002391  0.001914  0.001735  0.002805  0.002563  0.023692  0.000000
## [6,]  0.003053  0.003180  0.002958  0.002522  0.003211  0.003342  0.024807
## [7,]  0.001826  0.001591  0.002290  0.001881  0.001473  0.002174  0.001908
##      MantonBM8
## [1,]   0.00000
## [2,]   0.00000
## [3,]   0.00000
## [4,]   0.00000
## [5,]   0.00000
## [6,]   0.00000
## [7,]   0.03235
```

## 14.7 Dimensionality reduction

We set `external_neighbors=TRUE` to replace the internal nearest neighbor search in the UMAP implementation with our parallelized approximate search.
We also set the number of threads to be used in the UMAP iterations.

```
set.seed(01010100)
sce.bone <- runUMAP(sce.bone, dimred="MNN",
    external_neighbors=TRUE, 
    BNPARAM=AnnoyParam(),
    BPPARAM=bpp,
    n_threads=bpnworkers(bpp))
```

## 14.8 Clustering

Graph-based clustering generates an excessively large intermediate graph so we will instead use a two-step approach with \(k\)-means.
We generate 1000 small clusters that are subsequently aggregated into more interpretable groups with a graph-based method.
If more resolution is required, we can increase `centers` in addition to using a lower `k` during graph construction.

```
library(bluster)

set.seed(1000)
colLabels(sce.bone) <- clusterRows(reducedDim(sce.bone, "MNN"),
    TwoStepParam(KmeansParam(centers=1000), NNGraphParam(k=5)))

table(colLabels(sce.bone))
```

```
## 
##     1     2     3     4     5     6     7     8     9    10    11    12    13 
## 18859 15812 36360 47699 26528 10869 65650 18584 35321  8009 14930  3601  4206 
##    14    15    16 
##  3155  4824  2318
```

We observe mostly balanced contributions from different samples to each cluster (Figure [14.4](https://bioconductor.org/books/3.23/OSCA.workflows/hca-human-bone-marrow-10x-genomics.html#fig:unref-hca-bone-ab)), consistent with the expectation that all samples are replicates from different donors.

```
tab <- table(Cluster=colLabels(sce.bone), Donor=sce.bone$Donor)
library(pheatmap)
pheatmap(log10(tab+10), color=viridis::viridis(100))
```

![Heatmap of log~10~-number of cells in each cluster (row) from each sample (column).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-hca-human-bone-marrow-10x-genomics/unref-hca-bone-ab-1.png)

Figure 14.4: Heatmap of log10-number of cells in each cluster (row) from each sample (column).

```
# TODO: add scrambling option in scater's plotting functions.
scrambled <- sample(ncol(sce.bone))

gridExtra::grid.arrange(
    plotUMAP(sce.bone, colour_by="label", text_by="label"),
    plotUMAP(sce.bone[,scrambled], colour_by="Donor")
)
```

![UMAP plots of the HCA bone marrow dataset after merging. Each point represents a cell and is colored according to the assigned cluster (top) or the donor of origin (bottom).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-hca-human-bone-marrow-10x-genomics/unref-hca-bone-umap-1.png)

Figure 14.5: UMAP plots of the HCA bone marrow dataset after merging. Each point represents a cell and is colored according to the assigned cluster (top) or the donor of origin (bottom).

## 14.9 Differential expression

We identify marker genes for each cluster while blocking on the donor.

```
markers.bone <- findMarkers(sce.bone, block = sce.bone$Donor, 
    direction = 'up', lfc = 1, BPPARAM=bpp)
```

We visualize the top markers for a randomly chosen cluster[2](https://bioconductor.org/books/3.23/OSCA.workflows/hca-human-bone-marrow-10x-genomics.html#fn2) using a heatmap in Figure [14.6](https://bioconductor.org/books/3.23/OSCA.workflows/hca-human-bone-marrow-10x-genomics.html#fig:unref-hca-bone-heatmap).
The presence of upregulated genes like *LYZ*, *S100A8* and *VCAN* is consistent with a monocyte identity for this cluster.

```
top.markers <- markers.bone[[cluster.choice]]
best <- top.markers[top.markers$Top <= 10,]
lfcs <- getMarkerEffects(best)

library(pheatmap)
pheatmap(lfcs, breaks=seq(-5, 5, length.out=101))
```

![Heatmap of log~2~-fold changes for the top marker genes (rows) of cluster 4 compared to all other clusters (columns).](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-hca-human-bone-marrow-10x-genomics/unref-hca-bone-heatmap-1.png)

Figure 14.6: Heatmap of log2-fold changes for the top marker genes (rows) of cluster 4 compared to all other clusters (columns).

## 14.10 Cell type classification

We perform automated cell type classification using a reference dataset to annotate each cluster based on its pseudo-bulk profile.
This is faster than the per-cell approaches described in Chapter [10.9](https://bioconductor.org/books/3.23/OSCA.workflows/nestorowa-mouse-hsc-smart-seq2.html#cell-type-annotation) at the cost of the resolution required to detect heterogeneity inside a cluster.
Nonetheless, it is often sufficient for a quick assignment of cluster identity, and indeed, cluster 4 is also identified as consisting of monocytes from this analysis.

```
se.aggregated <- sumCountsAcrossCells(sce.bone, id=colLabels(sce.bone), BPPARAM=bpp)

library(celldex)
hpc <- HumanPrimaryCellAtlasData()

library(SingleR)
anno.single <- SingleR(se.aggregated, ref = hpc, labels = hpc$label.main,
    assay.type.test="sum")
anno.single
```

```
## DataFrame with 16 rows and 4 columns
##                             scores      labels delta.next pruned.labels
##                           <matrix> <character>  <numeric>   <character>
## 1   0.384401:0.751148:0.651234:...         GMP  0.0913786           GMP
## 2   0.343557:0.567261:0.479100:...     T_cells  0.4298632       T_cells
## 3   0.323043:0.647364:0.558334:...     T_cells  0.0959201       T_cells
## 4   0.299294:0.745584:0.535751:...    Monocyte  0.2935059      Monocyte
## 5   0.310761:0.672644:0.540285:...      B_cell  0.6024293        B_cell
## ...                            ...         ...        ...           ...
## 12  0.294203:0.707235:0.528198:...    Monocyte  0.3586359      Monocyte
## 13  0.343741:0.731258:0.600058:...    Monocyte  0.1019188            NA
## 14  0.369798:0.652467:0.582201:...      B_cell  0.1976631            NA
## 15  0.378580:0.690882:0.781190:...         MEP  0.0614135           MEP
## 16  0.333963:0.679341:0.559147:...         GMP  0.1114087           GMP
```

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
 [1] SingleR_2.14.0              celldex_1.21.0             
 [3] pheatmap_1.0.13             bluster_1.22.0             
 [5] BiocNeighbors_2.6.0         batchelor_1.28.0           
 [7] scran_1.40.0                BiocParallel_1.46.0        
 [9] scater_1.40.0               ggplot2_4.0.3              
[11] scuttle_1.22.0              EnsDb.Hsapiens.v86_2.99.0  
[13] ensembldb_2.36.0            AnnotationFilter_1.36.0    
[15] GenomicFeatures_1.64.0      AnnotationDbi_1.74.0       
[17] rhdf5_2.56.0                HCAData_1.27.0             
[19] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
[21] Biobase_2.72.0              GenomicRanges_1.64.0       
[23] Seqinfo_1.2.0               IRanges_2.46.0             
[25] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[27] generics_0.1.4              MatrixGenerics_1.24.0      
[29] matrixStats_1.5.0           BiocStyle_2.40.0           
[31] rebook_1.22.0              

loaded via a namespace (and not attached):
  [1] BiocIO_1.22.0             bitops_1.0-9             
  [3] filelock_1.0.3            tibble_3.3.1             
  [5] CodeDepends_0.6.7         graph_1.90.0             
  [7] XML_3.99-0.23             lifecycle_1.0.5          
  [9] httr2_1.2.2               edgeR_4.10.0             
 [11] lattice_0.22-9            alabaster.base_1.12.0    
 [13] magrittr_2.0.5            limma_3.68.0             
 [15] sass_0.4.10               rmarkdown_2.31           
 [17] jquerylib_0.1.4           yaml_2.3.12              
 [19] metapod_1.20.0            otel_0.2.0               
 [21] cowplot_1.2.0             DBI_1.3.0                
 [23] RColorBrewer_1.1-3        ResidualMatrix_1.22.0    
 [25] abind_1.4-8               purrr_1.2.2              
 [27] RCurl_1.98-1.18           rappdirs_0.3.4           
 [29] ggrepel_0.9.8             irlba_2.3.7              
 [31] RSpectra_0.16-2           dqrng_0.4.1              
 [33] DelayedMatrixStats_1.34.0 codetools_0.2-20         
 [35] DelayedArray_0.38.0       tidyselect_1.2.1         
 [37] UCSC.utils_1.8.0          farver_2.1.2             
 [39] ScaledMatrix_1.20.0       viridis_0.6.5            
 [41] BiocFileCache_3.2.0       GenomicAlignments_1.48.0 
 [43] jsonlite_2.0.0            tools_4.6.0              
 [45] Rcpp_1.1.1-1.1            glue_1.8.1               
 [47] gridExtra_2.3             SparseArray_1.12.0       
 [49] xfun_0.57                 GenomeInfoDb_1.48.0      
 [51] dplyr_1.2.1               HDF5Array_1.40.0         
 [53] gypsum_1.8.0              withr_3.0.2              
 [55] BiocManager_1.30.27       fastmap_1.2.0            
 [57] rhdf5filters_1.24.0       digest_0.6.39            
 [59] rsvd_1.0.5                R6_2.6.1                 
 [61] dichromat_2.0-0.1         RSQLite_2.4.6            
 [63] cigarillo_1.2.0           h5mread_1.4.0            
 [65] rtracklayer_1.72.0        httr_1.4.8               
 [67] S4Arrays_1.12.0           uwot_0.2.4               
 [69] pkgconfig_2.0.3           gtable_0.3.6             
 [71] blob_1.3.0                S7_0.2.2                 
 [73] XVector_0.52.0            htmltools_0.5.9          
 [75] bookdown_0.46             ProtGenerics_1.44.0      
 [77] scales_1.4.0              alabaster.matrix_1.12.0  
 [79] png_0.1-9                 knitr_1.51               
 [81] rjson_0.2.23              curl_7.1.0               
 [83] cachem_1.1.0              BiocVersion_3.23.1       
 [85] parallel_4.6.0            vipor_0.4.7              
 [87] restfulr_0.0.16           pillar_1.11.1            
 [89] grid_4.6.0                alabaster.schemas_1.12.0 
 [91] vctrs_0.7.3               BiocSingular_1.28.0      
 [93] dbplyr_2.5.2              beachmat_2.28.0          
 [95] cluster_2.1.8.2           beeswarm_0.4.0           
 [97] evaluate_1.0.5            cli_3.6.6                
 [99] locfit_1.5-9.12           compiler_4.6.0           
[101] Rsamtools_2.28.0          rlang_1.2.0              
[103] crayon_1.5.3              labeling_0.4.3           
[105] ggbeeswarm_0.7.3          viridisLite_0.4.3        
[107] alabaster.se_1.12.0       Biostrings_2.80.0        
[109] lazyeval_0.2.3            Matrix_1.7-5             
[111] dir.expiry_1.20.0         ExperimentHub_3.2.0      
[113] sparseMatrixStats_1.24.0  bit64_4.8.0              
[115] Rhdf5lib_2.0.0            KEGGREST_1.52.0          
[117] statmod_1.5.1             alabaster.ranges_1.12.0  
[119] AnnotationHub_4.2.0       beachmat.hdf5_1.10.0     
[121] igraph_2.3.0              memoise_2.0.1            
[123] bslib_0.10.0              bit_4.6.0
```

Bach, K., S. Pensa, M. Grzelak, J. Hadfield, D. J. Adams, J. C. Marioni, and W. T. Khaled. 2017. “Differentiation dynamics of mammary epithelial cells revealed by single-cell RNA sequencing.” *Nat Commun* 8 (1): 2128.

Grun, D., M. J. Muraro, J. C. Boisset, K. Wiebrands, A. Lyubimova, G. Dharmadhikari, M. van den Born, et al. 2016. “De Novo Prediction of Stem Cell Identity using Single-Cell Transcriptome Data.” *Cell Stem Cell* 19 (2): 266–77.

Lawlor, N., J. George, M. Bolisetty, R. Kursawe, L. Sun, V. Sivakamasundari, I. Kycia, P. Robson, and M. L. Stitzel. 2017. “Single-cell transcriptomes identify human islet cell signatures and reveal cell-type-specific expression changes in type 2 diabetes.” *Genome Res.* 27 (2): 208–22.

Lun, A. T. L., F. J. Calero-Nieto, L. Haim-Vilmovsky, B. Gottgens, and J. C. Marioni. 2017. “Assessing the reliability of spike-in normalization for analyses of single-cell RNA sequencing data.” *Genome Res.* 27 (11): 1795–1806.

Messmer, T., F. von Meyenn, A. Savino, F. Santos, H. Mohammed, A. T. L. Lun, J. C. Marioni, and W. Reik. 2019. “Transcriptional heterogeneity in naive and primed human pluripotent stem cells at single-cell resolution.” *Cell Rep* 26 (4): 815–24.

Muraro, M. J., G. Dharmadhikari, D. Grun, N. Groen, T. Dielen, E. Jansen, L. van Gurp, et al. 2016. “A Single-Cell Transcriptome Atlas of the Human Pancreas.” *Cell Syst* 3 (4): 385–94.

Nestorowa, S., F. K. Hamey, B. Pijuan Sala, E. Diamanti, M. Shepherd, E. Laurenti, N. K. Wilson, D. G. Kent, and B. Gottgens. 2016. “A single-cell resolution map of mouse hematopoietic stem and progenitor cell differentiation.” *Blood* 128 (8): 20–31.

Paul, F., Y. Arkin, A. Giladi, D. A. Jaitin, E. Kenigsberg, H. Keren-Shaul, D. Winter, et al. 2015. “Transcriptional Heterogeneity and Lineage Commitment in Myeloid Progenitors.” *Cell* 163 (7): 1663–77.

Picelli, S., O. R. Faridani, A. K. Bjorklund, G. Winberg, S. Sagasser, and R. Sandberg. 2014. “Full-length RNA-seq from single cells using Smart-seq2.” *Nat Protoc* 9 (1): 171–81.

Pollen, A. A., T. J. Nowakowski, J. Shuga, X. Wang, A. A. Leyrat, J. H. Lui, N. Li, et al. 2014. “Low-coverage single-cell mRNA sequencing reveals cellular heterogeneity and activated signaling pathways in developing cerebral cortex.” *Nat. Biotechnol.* 32 (10): 1053–8.

Segerstolpe, A., A. Palasantza, P. Eliasson, E. M. Andersson, A. C. Andreasson, X. Sun, S. Picelli, et al. 2016. “Single-Cell Transcriptome Profiling of Human Pancreatic Islets in Health and Type 2 Diabetes.” *Cell Metab.* 24 (4): 593–607.

Wajapeyee, N., S. Z. Wang, R. W. Serra, P. D. Solomon, A. Nagarajan, X. Zhu, and M. R. Green. 2010. “Senescence induction in human fibroblasts and hematopoietic progenitors by leukemogenic fusion proteins.” *Blood* 115 (24): 5057–60.

Zeisel, A., A. B. Munoz-Manchado, S. Codeluppi, P. Lonnerberg, G. La Manno, A. Jureus, S. Marques, et al. 2015. “Brain structure. Cell types in the mouse cortex and hippocampus revealed by single-cell RNA-seq.” *Science* 347 (6226): 1138–42.

Zeng, H., E. H. Shen, J. G. Hohmann, S. W. Oh, A. Bernard, J. J. Royall, K. J. Glattfelder, et al. 2012. “Large-scale cellular-resolution gene profiling in human neocortex reveals species-specific molecular signatures.” *Cell* 149 (2): 483–96.

Zheng, G. X., J. M. Terry, P. Belgrader, P. Ryvkin, Z. W. Bent, R. Wilson, S. B. Ziraldo, et al. 2017. “Massively parallel digital transcriptional profiling of single cells.” *Nat Commun* 8 (January): 14049.

---

1. The randomized SVD may give slightly different results on different systems, so the MNN-corrected values may themselves vary across systems.[↩︎](https://bioconductor.org/books/3.23/OSCA.workflows/hca-human-bone-marrow-10x-genomics.html#fnref1)
2. The exact cluster chosen varies across systems due to the MNN-corrected values themselves varying across systems.[↩︎](https://bioconductor.org/books/3.23/OSCA.workflows/hca-human-bone-marrow-10x-genomics.html#fnref2)
