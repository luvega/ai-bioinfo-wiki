---
source: OSCA
title: "Single-Cell Analysis Workflows with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.workflows/messmer-hesc.html
ingested_at: 2026-06-04T01:52:44+00:00
status: source_ingested
---

# [Single-Cell Analysis Workflows with Bioconductor](https://bioconductor.org/books/3.23/OSCA.workflows/)

# Chapter 13 Messmer human ESC (Smart-seq2)

## 13.1 Introduction

This performs an analysis of the human embryonic stem cell (hESC) dataset generated with Smart-seq2 (Messmer et al. [2019](https://bioconductor.org/books/3.23/OSCA.workflows/messmer-hesc.html#ref-messmer2019transcriptional)), which contains several plates of naive and primed hESCs.
The chapter’s code is based on the steps in the paper’s [GitHub repository](https://github.com/MarioniLab/NaiveHESC2016/blob/master/analysis/preprocess.Rmd), with some additional steps for cell cycle effect removal contributed by Philippe Boileau.

## 13.2 Data loading

Converting the batch to a factor, to make life easier later on.

```
library(scRNAseq)
sce.mess <- MessmerESCData()
sce.mess$`experiment batch` <- factor(sce.mess$`experiment batch`)
```

```
library(AnnotationHub)
ens.hs.v97 <- AnnotationHub()[["AH73881"]]
anno <- select(ens.hs.v97, keys=rownames(sce.mess), 
    keytype="GENEID", columns=c("SYMBOL"))
rowData(sce.mess) <- anno[match(rownames(sce.mess), anno$GENEID),]
```

## 13.3 Quality control

Let’s have a look at the QC statistics.

```
colSums(as.matrix(filtered))
```

```
##              low_lib_size            low_n_features high_subsets_Mito_percent 
##                       107                        99                        22 
## high_altexps_ERCC_percent                   discard 
##                       117                       156
```

```
gridExtra::grid.arrange(
    plotColData(original, x="experiment batch", y="sum",
        colour_by=I(filtered$discard), other_field="phenotype") +
        facet_wrap(~phenotype) + scale_y_log10(),
    plotColData(original, x="experiment batch", y="detected",
        colour_by=I(filtered$discard), other_field="phenotype") +
        facet_wrap(~phenotype) + scale_y_log10(),
    plotColData(original, x="experiment batch", y="subsets_Mito_percent",
        colour_by=I(filtered$discard), other_field="phenotype") +
        facet_wrap(~phenotype),
    plotColData(original, x="experiment batch", y="altexps_ERCC_percent",
        colour_by=I(filtered$discard), other_field="phenotype") +
        facet_wrap(~phenotype),
    ncol=1
)
```

![Distribution of QC metrics across batches (x-axis) and phenotypes (facets) for cells in the Messmer hESC dataset. Each point is a cell and is colored by whether it was discarded.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-messmer-hesc/unref-messmer-hesc-qc-1.png)

Figure 13.1: Distribution of QC metrics across batches (x-axis) and phenotypes (facets) for cells in the Messmer hESC dataset. Each point is a cell and is colored by whether it was discarded.

## 13.4 Normalization

```
library(scran)

set.seed(10000)
clusters <- quickCluster(sce.mess)
sce.mess <- computeSumFactors(sce.mess, cluster=clusters)
sce.mess <- logNormCounts(sce.mess)
```

```
par(mfrow=c(1,2))
plot(sce.mess$sum, sizeFactors(sce.mess), log = "xy", pch=16,
     xlab = "Library size (millions)", ylab = "Size factor",
     col = ifelse(sce.mess$phenotype == "naive", "black", "grey"))

spike.sf <- librarySizeFactors(altExp(sce.mess, "ERCC"))
plot(sizeFactors(sce.mess), spike.sf, log = "xy", pch=16,
     ylab = "Spike-in size factor", xlab = "Deconvolution size factor",
     col = ifelse(sce.mess$phenotype == "naive", "black", "grey"))
```

![Deconvolution size factors plotted against the library size (left) and spike-in size factors plotted against the deconvolution size factors (right). Each point is a cell and is colored by its phenotype.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-messmer-hesc/unref-messmer-hesc-norm-1.png)

Figure 13.2: Deconvolution size factors plotted against the library size (left) and spike-in size factors plotted against the deconvolution size factors (right). Each point is a cell and is colored by its phenotype.

## 13.5 Cell cycle phase assignment

Here, we use multiple cores to speed up the processing.

```
set.seed(10001)
hs_pairs <- readRDS(system.file("exdata", "human_cycle_markers.rds", package="scran"))
assigned <- cyclone(sce.mess, pairs=hs_pairs, 
    gene.names=rownames(sce.mess),
    BPPARAM=BiocParallel::MulticoreParam(10))
sce.mess$phase <- assigned$phases
```

```
table(sce.mess$phase)
```

```
## 
##  G1 G2M   S 
## 460 406 322
```

```
smoothScatter(assigned$scores$G1, assigned$scores$G2M, xlab="G1 score",
     ylab="G2/M score", pch=16)
```

![G1 `cyclone()` phase scores against the G2/M phase scores for each cell in the Messmer hESC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-messmer-hesc/unref-messmer-hesc-cyclone-1.png)

Figure 13.3: G1 `cyclone()` phase scores against the G2/M phase scores for each cell in the Messmer hESC dataset.

## 13.6 Feature selection

```
dec <- modelGeneVarWithSpikes(sce.mess, "ERCC", block = sce.mess$`experiment batch`)
top.hvgs <- getTopHVGs(dec, prop = 0.1)
```

```
par(mfrow=c(1,3))
for (i in seq_along(dec$per.block)) {
    current <- dec$per.block[[i]]
    plot(current$mean, current$total, xlab="Mean log-expression", 
        ylab="Variance", pch=16, cex=0.5, main=paste("Batch", i))

    fit <- metadata(current)
    points(fit$mean, fit$var, col="red", pch=16)
    curve(fit$trend(x), col='dodgerblue', add=TRUE, lwd=2)
}
```

![Per-gene variance of the log-normalized expression values in the Messmer hESC dataset, plotted against the mean for each batch. Each point represents a gene with spike-ins shown in red and the fitted trend shown in blue.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-messmer-hesc/unref-messmer-hesc-var-1.png)

Figure 13.4: Per-gene variance of the log-normalized expression values in the Messmer hESC dataset, plotted against the mean for each batch. Each point represents a gene with spike-ins shown in red and the fitted trend shown in blue.

## 13.7 Batch correction

We eliminate the obvious batch effect between batches with linear regression, which is possible due to the replicated nature of the experimental design.
We set `keep=1:2` to retain the effect of the first two coefficients in `design` corresponding to our phenotype of interest.

```
library(batchelor)
sce.mess <- correctExperiments(sce.mess, 
    PARAM = RegressParam(
        design = model.matrix(~sce.mess$phenotype + sce.mess$`experiment batch`),
        keep = 1:2 
    )
)
```

## 13.8 Dimensionality Reduction

We could have set `d=` and `subset.row=` in `correctExperiments()` to automatically perform a PCA on the the residual matrix with the subset of HVGs,
but we’ll just explicitly call `runPCA()` here to keep things simple.

```
set.seed(1101001)
sce.mess <- runPCA(sce.mess, subset_row = top.hvgs, exprs_values = "corrected")
sce.mess <- runTSNE(sce.mess, dimred = "PCA", perplexity = 40)
```

From a naive PCA, the cell cycle appears to be a major source of biological variation within each phenotype.

```
gridExtra::grid.arrange(
    plotTSNE(sce.mess, colour_by = "phenotype") + ggtitle("By phenotype"),
    plotTSNE(sce.mess, colour_by = "experiment batch") + ggtitle("By batch "),
    plotTSNE(sce.mess, colour_by = "CDK1", swap_rownames="SYMBOL") + ggtitle("By CDK1"),
    plotTSNE(sce.mess, colour_by = "phase") + ggtitle("By phase"),
    ncol = 2
)
```

![Obligatory $t$-SNE plots of the Messmer hESC dataset, where each point is a cell and is colored by various attributes.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-messmer-hesc/unref-messmer-hesc-tsne-1.png)

Figure 13.5: Obligatory \(t\)-SNE plots of the Messmer hESC dataset, where each point is a cell and is colored by various attributes.

We perform contrastive PCA (cPCA) and sparse cPCA (scPCA) on the corrected log-expression data to obtain the same number of PCs.
Given that the naive hESCs are actually reprogrammed primed hESCs, we will use the single batch of primed-only hESCs as the “background” dataset to remove the cell cycle effect.

```
library(scPCA)
is.bg <- sce.mess$`experiment batch`=="3"
target <- sce.mess[,!is.bg]
background <- sce.mess[,is.bg]

mat.target <- t(assay(target, "corrected")[top.hvgs,])
mat.background <- t(assay(background, "corrected")[top.hvgs,])

set.seed(1010101001)
con_out <- scPCA(
    target = mat.target,
    background = mat.background,
    penalties = 0, # no penalties = non-sparse cPCA.
    n_eigen = 50,
    contrasts = 100
)
reducedDim(target, "cPCA") <- con_out$x
```

```
set.seed(101010101)
sparse_con_out <- scPCA(
    target = mat.target,
    background = mat.background,
    penalties = 1e-4,
    n_eigen = 50,
    contrasts = 100,
    alg = "rand_var_proj" # for speed.
)
reducedDim(target, "scPCA") <- sparse_con_out$x
```

We see greater intermingling between phases within both the naive and primed cells after cPCA and scPCA.

```
set.seed(1101001)
target <- runTSNE(target, dimred = "cPCA", perplexity = 40, name="cPCA+TSNE")
target <- runTSNE(target, dimred = "scPCA", perplexity = 40, name="scPCA+TSNE")
```

```
gridExtra::grid.arrange(
    plotReducedDim(target, "cPCA+TSNE", colour_by = "phase") + ggtitle("After cPCA"),
    plotReducedDim(target, "scPCA+TSNE", colour_by = "phase") + ggtitle("After scPCA"),
    ncol=2
)
```

![More $t$-SNE plots of the Messmer hESC dataset after cPCA and scPCA, where each point is a cell and is colored by its assigned cell cycle phase.](../../../../raw/bioconductor_books/assets/OSCA/osca.workflows-messmer-hesc/unref-messmer-hesc-cpca-tsne-1.png)

Figure 13.6: More \(t\)-SNE plots of the Messmer hESC dataset after cPCA and scPCA, where each point is a cell and is colored by its assigned cell cycle phase.

We can quantify the change in the separation between phases within each phenotype using the silhouette coefficient.

```
library(bluster)
naive <- target[,target$phenotype=="naive"]
primed <- target[,target$phenotype=="primed"]

N <- approxSilhouette(reducedDim(naive, "PCA"), naive$phase)
P <- approxSilhouette(reducedDim(primed, "PCA"), primed$phase)
c(naive=mean(N$width), primed=mean(P$width))
```

```
##   naive  primed 
## 0.02032 0.03025
```

```
cN <- approxSilhouette(reducedDim(naive, "cPCA"), naive$phase)
cP <- approxSilhouette(reducedDim(primed, "cPCA"), primed$phase)
c(naive=mean(cN$width), primed=mean(cP$width))
```

```
##    naive   primed 
## 0.007696 0.011941
```

```
scN <- approxSilhouette(reducedDim(naive, "scPCA"), naive$phase)
scP <- approxSilhouette(reducedDim(primed, "scPCA"), primed$phase)
c(naive=mean(scN$width), primed=mean(scP$width))
```

```
##    naive   primed 
## 0.006614 0.014601
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
 [1] bluster_1.22.0              scPCA_1.26.0               
 [3] batchelor_1.28.0            scran_1.40.0               
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
  [1] BiocIO_1.22.0             bitops_1.0-9             
  [3] filelock_1.0.3            tibble_3.3.1             
  [5] CodeDepends_0.6.7         graph_1.90.0             
  [7] XML_3.99-0.23             lifecycle_1.0.5          
  [9] httr2_1.2.2               Rdpack_2.6.6             
 [11] edgeR_4.10.0              globals_0.19.1           
 [13] lattice_0.22-9            alabaster.base_1.12.0    
 [15] magrittr_2.0.5            limma_3.68.0             
 [17] sass_0.4.10               rmarkdown_2.31           
 [19] jquerylib_0.1.4           yaml_2.3.12              
 [21] metapod_1.20.0            otel_0.2.0               
 [23] cowplot_1.2.0             DBI_1.3.0                
 [25] RColorBrewer_1.1-3        ResidualMatrix_1.22.0    
 [27] abind_1.4-8               Rtsne_0.17               
 [29] purrr_1.2.2               RCurl_1.98-1.18          
 [31] rappdirs_0.3.4            ggrepel_0.9.8            
 [33] irlba_2.3.7               listenv_0.10.1           
 [35] alabaster.sce_1.12.0      RSpectra_0.16-2          
 [37] parallelly_1.47.0         dqrng_0.4.1              
 [39] DelayedMatrixStats_1.34.0 codetools_0.2-20         
 [41] DelayedArray_0.38.0       tidyselect_1.2.1         
 [43] UCSC.utils_1.8.0          farver_2.1.2             
 [45] ScaledMatrix_1.20.0       viridis_0.6.5            
 [47] GenomicAlignments_1.48.0  jsonlite_2.0.0           
 [49] BiocNeighbors_2.6.0       tools_4.6.0              
 [51] Rcpp_1.1.1-1.1            glue_1.8.1               
 [53] gridExtra_2.3             SparseArray_1.12.0       
 [55] xfun_0.57                 GenomeInfoDb_1.48.0      
 [57] dplyr_1.2.1               HDF5Array_1.40.0         
 [59] gypsum_1.8.0              withr_3.0.2              
 [61] BiocManager_1.30.27       fastmap_1.2.0            
 [63] sparsepca_0.1.2           rhdf5filters_1.24.0      
 [65] digest_0.6.39             rsvd_1.0.5               
 [67] R6_2.6.1                  dichromat_2.0-0.1        
 [69] RSQLite_2.4.6             cigarillo_1.2.0          
 [71] h5mread_1.4.0             data.table_1.18.2.1      
 [73] rtracklayer_1.72.0        httr_1.4.8               
 [75] S4Arrays_1.12.0           pkgconfig_2.0.3          
 [77] gtable_0.3.6              blob_1.3.0               
 [79] S7_0.2.2                  XVector_0.52.0           
 [81] htmltools_0.5.9           bookdown_0.46            
 [83] ProtGenerics_1.44.0       scales_1.4.0             
 [85] alabaster.matrix_1.12.0   png_0.1-9                
 [87] knitr_1.51                rjson_0.2.23             
 [89] curl_7.1.0                cachem_1.1.0             
 [91] rhdf5_2.56.0              stringr_1.6.0            
 [93] BiocVersion_3.23.1        KernSmooth_2.23-26       
 [95] parallel_4.6.0            vipor_0.4.7              
 [97] restfulr_0.0.16           pillar_1.11.1            
 [99] grid_4.6.0                alabaster.schemas_1.12.0 
[101] vctrs_0.7.3               origami_1.0.7            
[103] BiocSingular_1.28.0       beachmat_2.28.0          
[105] cluster_2.1.8.2           beeswarm_0.4.0           
[107] evaluate_1.0.5            cli_3.6.6                
[109] locfit_1.5-9.12           compiler_4.6.0           
[111] Rsamtools_2.28.0          rlang_1.2.0              
[113] crayon_1.5.3              future.apply_1.20.2      
[115] labeling_0.4.3            ggbeeswarm_0.7.3         
[117] stringi_1.8.7             alabaster.se_1.12.0      
[119] viridisLite_0.4.3         BiocParallel_1.46.0      
[121] assertthat_0.2.1          Biostrings_2.80.0        
[123] coop_0.6-3                lazyeval_0.2.3           
[125] Matrix_1.7-5              dir.expiry_1.20.0        
[127] ExperimentHub_3.2.0       future_1.70.0            
[129] sparseMatrixStats_1.24.0  bit64_4.8.0              
[131] Rhdf5lib_2.0.0            KEGGREST_1.52.0          
[133] statmod_1.5.1             alabaster.ranges_1.12.0  
[135] kernlab_0.9-33            rbibutils_2.4.1          
[137] igraph_2.3.0              memoise_2.0.1            
[139] bslib_0.10.0              bit_4.6.0
```

### References

Messmer, T., F. von Meyenn, A. Savino, F. Santos, H. Mohammed, A. T. L. Lun, J. C. Marioni, and W. Reik. 2019. “Transcriptional heterogeneity in naive and primed human pluripotent stem cells at single-cell resolution.” *Cell Rep* 26 (4): 815–24.
