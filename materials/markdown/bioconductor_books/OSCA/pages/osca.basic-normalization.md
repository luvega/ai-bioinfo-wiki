---
source: OSCA
title: "Basics of Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.basic/normalization.html
ingested_at: 2026-06-04T01:52:37+00:00
status: source_ingested
---

# [Basics of Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/3.23/OSCA.basic/)

# Chapter 2 Normalization

## 2.1 Motivation

Systematic differences in sequencing coverage between libraries are often observed in single-cell RNA sequencing data (Stegle, Teichmann, and Marioni [2015](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-stegle2015computational)).
They typically arise from technical differences in cDNA capture or PCR amplification efficiency across cells, attributable to the difficulty of achieving consistent library preparation with minimal starting material.
Normalization aims to remove these differences such that they do not interfere with comparisons of the expression profiles between cells.
This ensures that any observed heterogeneity or differential expression within the cell population are driven by biology and not technical biases.

We will mostly focus our attention on scaling normalization, which is the simplest and most commonly used class of normalization strategies.
This involves dividing all counts for each cell by a cell-specific scaling factor, often called a “size factor” (Anders and Huber [2010](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-anders2010differential)).
The assumption here is that any cell-specific bias (e.g., in capture or amplification efficiency) affects all genes equally via scaling of the expected mean count for that cell.
The size factor for each cell represents the estimate of the relative bias in that cell, so division of its counts by its size factor should remove that bias.
The resulting “normalized expression values” can then be used for downstream analyses such as clustering and dimensionality reduction.
To demonstrate, we will use the Zeisel et al. ([2015](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-zeisel2015brain)) dataset from the *[scRNAseq](https://bioconductor.org/packages/3.23/scRNAseq)* package.

View set-up code ([Workflow Chapter 2](http://bioconductor.org/books/3.23/OSCA.workflows/zeisel-mouse-brain-strt-seq.html#zeisel-mouse-brain-strt-seq))

```
#--- loading ---#
library(scRNAseq)
sce.zeisel <- ZeiselBrainData()

library(scater)
sce.zeisel <- aggregateAcrossFeatures(sce.zeisel, 
    id=sub("_loc[0-9]+$", "", rownames(sce.zeisel)))

#--- gene-annotation ---#
library(org.Mm.eg.db)
rowData(sce.zeisel)$Ensembl <- mapIds(org.Mm.eg.db, 
    keys=rownames(sce.zeisel), keytype="SYMBOL", column="ENSEMBL")

#--- quality-control ---#
stats <- perCellQCMetrics(sce.zeisel, subsets=list(
    Mt=rowData(sce.zeisel)$featureType=="mito"))
qc <- quickPerCellQC(stats, percent_subsets=c("altexps_ERCC_percent", 
    "subsets_Mt_percent"))
sce.zeisel <- sce.zeisel[,!qc$discard]
```

```
sce.zeisel
```

```
## class: SingleCellExperiment 
## dim: 19839 2816 
## metadata(0):
## assays(1): counts
## rownames(19839): 0610005C13Rik 0610007N19Rik ... mt-Tw mt-Ty
## rowData names(2): featureType Ensembl
## colnames(2816): 1772071015_C02 1772071017_G12 ... 1772063068_D01
##   1772066098_A12
## colData names(9): tissue group # ... level1class level2class
## reducedDimNames(0):
## mainExpName: gene
## altExpNames(2): repeat ERCC
```

## 2.2 Library size normalization

Library size normalization is the simplest strategy for performing scaling normalization.
We define the library size as the total sum of counts across all genes for each cell, the expected value of which is assumed to scale with any cell-specific biases.
The “library size factor” for each cell is then directly proportional to its library size where the proportionality constant is defined such that the mean size factor across all cells is equal to 1.
This definition ensures that the normalized expression values are on the same scale as the original counts, which is useful for interpretation - especially when dealing with transformed data (see Section [2.5](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#normalization-transformation)).

```
library(scater)
lib.sf.zeisel <- librarySizeFactors(sce.zeisel)
summary(lib.sf.zeisel)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.176   0.568   0.868   1.000   1.278   4.084
```

In the Zeisel brain data, the library size factors differ by up to 10-fold across cells (Figure [2.1](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#fig:histlib)).
This is typical of the variability in coverage in scRNA-seq data.

```
hist(log10(lib.sf.zeisel), xlab="Log10[Size factor]", col='grey80')
```

![Distribution of size factors derived from the library size in the Zeisel brain dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-normalization/histlib-1.png)

Figure 2.1: Distribution of size factors derived from the library size in the Zeisel brain dataset.

Strictly speaking, the use of library size factors assumes that there is no “imbalance” in the differentially expressed (DE) genes between any pair of cells.
That is, any upregulation for a subset of genes is cancelled out by the same magnitude of downregulation in a different subset of genes.
This ensures that the library size is an unbiased estimate of the relative cell-specific bias by avoiding composition effects (Robinson and Oshlack [2010](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-robinson2010scaling)).
However, balanced DE is not generally present in scRNA-seq applications, which means that library size normalization may not yield accurate normalized expression values for downstream analyses.

In practice, normalization accuracy is not a major consideration for exploratory scRNA-seq data analyses.
Composition biases do not usually affect the separation of clusters, only the magnitude - and to a lesser extent, direction - of the log-fold changes between clusters or cell types.
As such, library size normalization is usually sufficient in many applications where the aim is to identify clusters and the top markers that define each cluster.

## 2.3 Normalization by deconvolution

As previously mentioned, composition biases will be present when any unbalanced differential expression exists between samples.
Consider the simple example of two cells where a single gene \(X\) is upregulated in one cell \(A\) compared to the other cell \(B\).
This upregulation means that either (i) more sequencing resources are devoted to \(X\) in \(A\), thus decreasing coverage of all other non-DE genes when the total library size of each cell is experimentally fixed (e.g., due to library quantification);
or (ii) the library size of \(A\) increases when \(X\) is assigned more reads or UMIs, increasing the library size factor and yielding smaller normalized expression values for all non-DE genes.
In both cases, the net effect is that non-DE genes in \(A\) will incorrectly appear to be downregulated compared to \(B\).

The removal of composition biases is a well-studied problem for bulk RNA sequencing data analysis.
Normalization can be performed with the `estimateSizeFactorsFromMatrix()` function in the *[DESeq2](https://bioconductor.org/packages/3.23/DESeq2)* package (Anders and Huber [2010](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-anders2010differential); Love, Huber, and Anders [2014](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-love2014moderated)) or with the `calcNormFactors()` function (Robinson and Oshlack [2010](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-robinson2010scaling)) in the *[edgeR](https://bioconductor.org/packages/3.23/edgeR)* package.
These assume that most genes are not DE between cells.
Any systematic difference in count size across the non-DE majority of genes between two cells is assumed to represent bias that is used to compute an appropriate size factor for its removal.

However, single-cell data can be problematic for these bulk normalization methods due to the dominance of low and zero counts.
To overcome this, we pool counts from many cells to increase the size of the counts for accurate size factor estimation (Lun, Bach, and Marioni [2016](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-lun2016pooling)).
Pool-based size factors are then “deconvolved” into cell-based factors for normalization of each cell’s expression profile.
This is performed using the `calculateSumFactors()` function from *[scran](https://bioconductor.org/packages/3.23/scran)*, as shown below.

```
library(scran)
set.seed(100)
clust.zeisel <- quickCluster(sce.zeisel) 
table(clust.zeisel)
```

```
## clust.zeisel
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14 
## 170 254 441 178 393 148 219 240 189 123 112 103 135 111
```

```
deconv.sf.zeisel <- calculateSumFactors(sce.zeisel, cluster=clust.zeisel)
summary(deconv.sf.zeisel)
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.119   0.486   0.831   1.000   1.321   4.509
```

We use a pre-clustering step with `quickCluster()` where cells in each cluster are normalized separately and the size factors are rescaled to be comparable across clusters.
This avoids the assumption that most genes are non-DE across the entire population - only a non-DE majority is required between pairs of clusters, which is a weaker assumption for highly heterogeneous populations.
By default, `quickCluster()` will use an approximate algorithm for PCA based on methods from the *[irlba](https://CRAN.R-project.org/package=irlba)* package.
The approximation relies on stochastic initialization so we need to set the random seed (via `set.seed()`) for reproducibility.

We see that the deconvolution size factors exhibit cell type-specific deviations from the library size factors in Figure [2.2](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#fig:deconv-zeisel).
This is consistent with the presence of composition biases that are introduced by strong differential expression between cell types.
Use of the deconvolution size factors adjusts for these biases to improve normalization accuracy for downstream applications.

```
plot(lib.sf.zeisel, deconv.sf.zeisel, xlab="Library size factor",
    ylab="Deconvolution size factor", log='xy', pch=16,
    col=as.integer(factor(sce.zeisel$level1class)))
abline(a=0, b=1, col="red")
```

![Deconvolution size factor for each cell in the Zeisel brain dataset, compared to the equivalent size factor derived from the library size. The red line corresponds to identity between the two size factors.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-normalization/deconv-zeisel-1.png)

Figure 2.2: Deconvolution size factor for each cell in the Zeisel brain dataset, compared to the equivalent size factor derived from the library size. The red line corresponds to identity between the two size factors.

Accurate normalization is most important for procedures that involve estimation and interpretation of per-gene statistics.
For example, composition biases can compromise DE analyses by systematically shifting the log-fold changes in one direction or another.
However, it tends to provide less benefit over simple library size normalization for cell-based analyses such as clustering.
The presence of composition biases already implies strong differences in expression profiles, so changing the normalization strategy is unlikely to affect the outcome of a clustering procedure.

## 2.4 Normalization by spike-ins

Spike-in normalization is based on the assumption that the same amount of spike-in RNA was added to each cell (Lun et al. [2017](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-lun2017assessing)).
Systematic differences in the coverage of the spike-in transcripts can only be due to cell-specific biases, e.g., in capture efficiency or sequencing depth.
To remove these biases, we equalize spike-in coverage across cells by scaling with “spike-in size factors”.
Compared to the previous methods, spike-in normalization requires no assumption about the biology of the system (i.e., the absence of many DE genes).
Instead, it assumes that the spike-in transcripts were (i) added at a constant level to each cell, and (ii) respond to biases in the same relative manner as endogenous genes.

Practically, spike-in normalization should be used if differences in the total RNA content of individual cells are of interest and must be preserved in downstream analyses.
For a given cell, an increase in its overall amount of endogenous RNA will not increase its spike-in size factor.
This ensures that the effects of total RNA content on expression across the population will not be removed upon scaling.
By comparison, the other normalization methods described above will simply interpret any change in total RNA content as part of the bias and remove it.

We demonstrate the use of spike-in normalization on a different dataset involving T cell activation after stimulation with T cell recepter ligands of varying affinity (Richard et al. [2018](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#ref-richard2018tcell)).

```
library(scRNAseq)
sce.richard <- RichardTCellData()
sce.richard <- sce.richard[,sce.richard$`single cell quality`=="OK"]
sce.richard
```

```
## class: SingleCellExperiment 
## dim: 46603 528 
## metadata(0):
## assays(1): counts
## rownames(46603): ENSMUSG00000102693 ENSMUSG00000064842 ...
##   ENSMUSG00000096730 ENSMUSG00000095742
## rowData names(0):
## colnames(528): SLX-12611.N701_S502. SLX-12611.N702_S502. ...
##   SLX-12612.i712_i522. SLX-12612.i714_i522.
## colData names(13): age individual ... stimulus time
## reducedDimNames(0):
## mainExpName: endogenous
## altExpNames(1): ERCC
```

We apply the `computeSpikeFactors()` method to estimate spike-in size factors for all cells.
This is defined by converting the total spike-in count per cell into a size factor, using the same reasoning as in `librarySizeFactors()`.
Scaling will subsequently remove any differences in spike-in coverage across cells.

```
sce.richard <- computeSpikeFactors(sce.richard, "ERCC")
summary(sizeFactors(sce.richard))
```

```
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   0.125   0.428   0.627   1.000   1.070  23.316
```

We observe a positive correlation between the spike-in size factors and deconvolution size factors within each treatment condition (Figure [2.3](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#fig:norm-spike-t)), indicating that they are capturing similar technical biases in sequencing depth and capture efficiency.
However, we also observe that increasing stimulation of the T cell receptor - in terms of increasing affinity or time - results in a decrease in the spike-in factors relative to the library size factors.
This is consistent with an increase in biosynthetic activity and total RNA content during stimulation, which reduces the relative spike-in coverage in each library (thereby decreasing the spike-in size factors) but increases the coverage of endogenous genes (thus increasing the library size factors).

```
to.plot <- data.frame(
    DeconvFactor=calculateSumFactors(sce.richard),
    SpikeFactor=sizeFactors(sce.richard),
    Stimulus=sce.richard$stimulus, 
    Time=sce.richard$time
)

ggplot(to.plot, aes(x=DeconvFactor, y=SpikeFactor, color=Time)) +
    geom_point() + facet_wrap(~Stimulus) + scale_x_log10() + 
    scale_y_log10() + geom_abline(intercept=0, slope=1, color="red")
```

![Size factors from spike-in normalization, plotted against the library size factors for all cells in the T cell dataset. Each plot represents a different ligand treatment and each point is a cell coloured according by time from stimulation.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-normalization/norm-spike-t-1.png)

Figure 2.3: Size factors from spike-in normalization, plotted against the library size factors for all cells in the T cell dataset. Each plot represents a different ligand treatment and each point is a cell coloured according by time from stimulation.

The differences between these two sets of size factors have real consequences for downstream interpretation.
If the spike-in size factors were applied to the counts, the expression values in unstimulated cells would be scaled up while expression in stimulated cells would be scaled down.
However, the opposite would occur if the deconvolution size factors were used.
This can manifest as shifts in the magnitude and direction of DE between conditions when we switch between normalization strategies, as shown below for *Malat1* (Figure [2.4](https://bioconductor.org/books/3.23/OSCA.basic/normalization.html#fig:norm-effect-malat)).

```
# See below for explanation of logNormCounts().
sce.richard.deconv <- logNormCounts(sce.richard, size_factors=to.plot$DeconvFactor)
sce.richard.spike <- logNormCounts(sce.richard, size_factors=to.plot$SpikeFactor)

gridExtra::grid.arrange(
    plotExpression(sce.richard.deconv, x="stimulus", 
        colour_by="time", features="ENSMUSG00000092341") + 
        theme(axis.text.x = element_text(angle = 90)) + 
        ggtitle("After deconvolution"),
    plotExpression(sce.richard.spike, x="stimulus", 
        colour_by="time", features="ENSMUSG00000092341") + 
        theme(axis.text.x = element_text(angle = 90)) +
        ggtitle("After spike-in normalization"),
    ncol=2
)
```

![Distribution of log-normalized expression values for _Malat1_ after normalization with the deconvolution size factors (left) or spike-in size factors (right). Cells are stratified by the ligand affinity and colored by the time after stimulation.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-normalization/norm-effect-malat-1.png)

Figure 2.4: Distribution of log-normalized expression values for *Malat1* after normalization with the deconvolution size factors (left) or spike-in size factors (right). Cells are stratified by the ligand affinity and colored by the time after stimulation.

Whether or not total RNA content is relevant – and thus, the choice of normalization strategy – depends on the biological hypothesis.
In most cases, changes in total RNA content are not interesting and can be normalized out by applying the library size or deconvolution factors.
However, this may not always be appropriate if differences in total RNA are associated with a biological process of interest, e.g., cell cycle activity or T cell activation.
Spike-in normalization will preserve these differences such that any changes in expression between biological groups have the correct sign.

**However!**
Regardless of whether we care about total RNA content, it is critical that the spike-in transcripts are normalized using the spike-in size factors.
Size factors computed from the counts for endogenous genes should not be applied to the spike-in transcripts, precisely because the former captures differences in total RNA content that are not experienced by the latter.
Attempting to normalize the spike-in counts with the gene-based size factors will lead to over-normalization and incorrect quantification.
Thus, if normalized spike-in data is required, we must compute a separate set of size factors for the spike-in transcripts; this is automatically performed by functions such as `modelGeneVarWithSpikes()`.

## 2.5 Scaling and log-transforming

Once we have computed the size factors, we use the `logNormCounts()` function from *[scater](https://bioconductor.org/packages/3.23/scater)* to compute normalized expression values for each cell.
This is done by dividing the count for each gene/spike-in transcript with the appropriate size factor for that cell.
The function also log-transforms the normalized values, creating a new assay called `"logcounts"`.
(Technically, these are “log-transformed normalized expression values”, but that’s too much of a mouthful to fit into the assay name.)
These log-values will be the basis of our downstream analyses in the following chapters.

```
set.seed(100)
clust.zeisel <- quickCluster(sce.zeisel) 
sce.zeisel <- computeSumFactors(sce.zeisel, cluster=clust.zeisel, min.mean=0.1)
sce.zeisel <- logNormCounts(sce.zeisel)
assayNames(sce.zeisel)
```

```
## [1] "counts"    "logcounts"
```

The log-transformation is useful as differences in the log-values represent log-fold changes in expression.
This is important in downstream procedures based on Euclidean distances, which includes many forms of clustering and dimensionality reduction.
By operating on log-transformed data, we ensure that these procedures are measuring distances between cells based on log-fold changes in expression.
Or in other words, which is more interesting - a gene that is expressed at an average count of 50 in cell type \(A\) and 10 in cell type \(B\), or a gene that is expressed at an average count of 1100 in \(A\) and 1000 in \(B\)?
Log-transformation focuses on the former by promoting contributions from genes with strong relative differences.

See [Advanced Chapter 2](http://bioconductor.org/books/3.23/OSCA.advanced/more-norm.html#more-norm) for further comments on transformation strategies.

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
 [1] ensembldb_2.36.0            AnnotationFilter_1.36.0    
 [3] GenomicFeatures_1.64.0      AnnotationDbi_1.74.0       
 [5] scRNAseq_2.25.0             scran_1.40.0               
 [7] scater_1.40.0               ggplot2_4.0.3              
 [9] scuttle_1.22.0              SingleCellExperiment_1.34.0
[11] SummarizedExperiment_1.42.0 Biobase_2.72.0             
[13] GenomicRanges_1.64.0        Seqinfo_1.2.0              
[15] IRanges_2.46.0              S4Vectors_0.50.0           
[17] BiocGenerics_0.58.0         generics_0.1.4             
[19] MatrixGenerics_1.24.0       matrixStats_1.5.0          
[21] BiocStyle_2.40.0            rebook_1.22.0              

loaded via a namespace (and not attached):
  [1] RColorBrewer_1.1-3       jsonlite_2.0.0           CodeDepends_0.6.7       
  [4] magrittr_2.0.5           ggbeeswarm_0.7.3         gypsum_1.8.0            
  [7] farver_2.1.2             rmarkdown_2.31           BiocIO_1.22.0           
 [10] vctrs_0.7.3              memoise_2.0.1            Rsamtools_2.28.0        
 [13] RCurl_1.98-1.18          htmltools_0.5.9          S4Arrays_1.12.0         
 [16] AnnotationHub_4.2.0      curl_7.1.0               BiocNeighbors_2.6.0     
 [19] Rhdf5lib_2.0.0           SparseArray_1.12.0       rhdf5_2.56.0            
 [22] sass_0.4.10              alabaster.base_1.12.0    bslib_0.10.0            
 [25] alabaster.sce_1.12.0     httr2_1.2.2              cachem_1.1.0            
 [28] GenomicAlignments_1.48.0 igraph_2.3.0             lifecycle_1.0.5         
 [31] pkgconfig_2.0.3          rsvd_1.0.5               Matrix_1.7-5            
 [34] R6_2.6.1                 fastmap_1.2.0            digest_0.6.39           
 [37] dqrng_0.4.1              irlba_2.3.7              ExperimentHub_3.2.0     
 [40] RSQLite_2.4.6            beachmat_2.28.0          labeling_0.4.3          
 [43] filelock_1.0.3           httr_1.4.8               abind_1.4-8             
 [46] compiler_4.6.0           bit64_4.8.0              withr_3.0.2             
 [49] S7_0.2.2                 BiocParallel_1.46.0      viridis_0.6.5           
 [52] DBI_1.3.0                alabaster.ranges_1.12.0  HDF5Array_1.40.0        
 [55] alabaster.schemas_1.12.0 rappdirs_0.3.4           DelayedArray_0.38.0     
 [58] rjson_0.2.23             bluster_1.22.0           tools_4.6.0             
 [61] vipor_0.4.7              otel_0.2.0               beeswarm_0.4.0          
 [64] glue_1.8.1               h5mread_1.4.0            restfulr_0.0.16         
 [67] rhdf5filters_1.24.0      grid_4.6.0               cluster_2.1.8.2         
 [70] gtable_0.3.6             BiocSingular_1.28.0      ScaledMatrix_1.20.0     
 [73] metapod_1.20.0           XVector_0.52.0           ggrepel_0.9.8           
 [76] BiocVersion_3.23.1       pillar_1.11.1            limma_3.68.0            
 [79] dplyr_1.2.1              BiocFileCache_3.2.0      lattice_0.22-9          
 [82] rtracklayer_1.72.0       bit_4.6.0                tidyselect_1.2.1        
 [85] locfit_1.5-9.12          Biostrings_2.80.0        knitr_1.51              
 [88] gridExtra_2.3            bookdown_0.46            ProtGenerics_1.44.0     
 [91] edgeR_4.10.0             xfun_0.57                statmod_1.5.1           
 [94] UCSC.utils_1.8.0         lazyeval_0.2.3           yaml_2.3.12             
 [97] evaluate_1.0.5           codetools_0.2-20         cigarillo_1.2.0         
[100] tibble_3.3.1             alabaster.matrix_1.12.0  BiocManager_1.30.27     
[103] graph_1.90.0             cli_3.6.6                jquerylib_0.1.4         
[106] GenomeInfoDb_1.48.0      dichromat_2.0-0.1        Rcpp_1.1.1-1.1          
[109] dir.expiry_1.20.0        dbplyr_2.5.2             png_0.1-9               
[112] XML_3.99-0.23            parallel_4.6.0           blob_1.3.0              
[115] bitops_1.0-9             alabaster.se_1.12.0      viridisLite_0.4.3       
[118] scales_1.4.0             purrr_1.2.2              crayon_1.5.3            
[121] rlang_1.2.0              cowplot_1.2.0            KEGGREST_1.52.0
```

### References

Anders, S., and W. Huber. 2010. “Differential expression analysis for sequence count data.” *Genome Biol.* 11 (10): R106.

Love, M. I., W. Huber, and S. Anders. 2014. “Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2.” *Genome Biol.* 15 (12): 550.

Lun, A. T., K. Bach, and J. C. Marioni. 2016. “Pooling across cells to normalize single-cell RNA sequencing data with many zero counts.” *Genome Biol.* 17 (April): 75.

Lun, A. T. L., F. J. Calero-Nieto, L. Haim-Vilmovsky, B. Gottgens, and J. C. Marioni. 2017. “Assessing the reliability of spike-in normalization for analyses of single-cell RNA sequencing data.” *Genome Res.* 27 (11): 1795–1806.

Richard, A. C., A. T. L. Lun, W. W. Y. Lau, B. Gottgens, J. C. Marioni, and G. M. Griffiths. 2018. “T cell cytolytic capacity is independent of initial stimulation strength.” *Nat. Immunol.* 19 (8): 849–58.

Robinson, M. D., and A. Oshlack. 2010. “A scaling normalization method for differential expression analysis of RNA-seq data.” *Genome Biol.* 11 (3): R25.

Stegle, O., S. A. Teichmann, and J. C. Marioni. 2015. “Computational and analytical challenges in single-cell transcriptomics.” *Nat. Rev. Genet.* 16 (3): 133–45.

Zeisel, A., A. B. Munoz-Manchado, S. Codeluppi, P. Lonnerberg, G. La Manno, A. Jureus, S. Marques, et al. 2015. “Brain structure. Cell types in the mouse cortex and hippocampus revealed by single-cell RNA-seq.” *Science* 347 (6226): 1138–42.
