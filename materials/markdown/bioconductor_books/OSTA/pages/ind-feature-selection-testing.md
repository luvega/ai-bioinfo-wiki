---
source: OSTA
title: "29 Feature selection & testing"
original_url: https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html
ingested_at: 2026-06-04T01:51:31+00:00
status: source_ingested
---

# 29  Feature selection & testing

## 29.1 Preamble

### 29.1.1 Introduction

Unsupervised clustering and label-transfer approaches yield (discrete, non-overlapping) grouping of cells by transcriptional – and presumably functional – similarity. Identifying **differentially expressed genes (DEGs)**, i.e., genes that are up-/down-regulated in one or few subpopulation(s), helps characterize clusters (and, in an unsupervised setting, find biologically meaningful cluster labels).

By contrast, methods to identify **spatially variable genes (SVGs)** aim to find genes with spatially correlated patterns of expression. Feature selection in terms of SVGs can be used as a spatially-aware alternative to mean-variance relationship-based HVGs (see [Chapter 11](https://bioconductor.org/books/release/OSTA/pages/seq-intermediate-processing.html)), or to identify biologically informative genes as candidates for experimental follow-up.

Here, we demonstrate selected methods to identify SVGs *de novo* (using `nnSVG`), and based on pre-computed spatial clusters (using `DESpace`). We further compare these to DEGs as well as HVGs, and discuss the conceptual similarities and differences between genes identified through these different approaches.

### 29.1.2 Dependencies

Code

```
library(DESpace)
library(dplyr)
library(ggspavis)
library(ggrepel)
library(nnSVG)
library(patchwork)
library(pheatmap)
library(scater)
library(scran)
library(SpatialExperiment)
library(tidyr)
```

Code

```
# set seed for random number generation
# in order to make results reproducible
set.seed(123)
# load data from previous chapters
# (post quality control & clustering)
spe <- readRDS("seq-spe_cl.rds")
```

## 29.2 Non-spatial

We can also use methods originally developed for bulk and single-cell transcriptomics, such as those for detecting highly variable genes (HVGs) and differentially expressed genes (DEGs), on spatial omics data. Note that HVGs are defined only based on molecular features (i.e., gene expression), and do not incorporate spatial information. In the context of single-cell and ST, differentially expressed (DE) may refer to differences between groups of samples, or to differences between clusters (e.g., cell types, or spatial domains); below, we consider changes across spatial structures.

### 29.2.1 Highly variable genes (HVGs)

Feature selection is used as a preprocessing step to identify a subset of biologically informative features (e.g. genes), in order to reduce noise (due to both technical and biological factors) and improve computational performance.

Note that HVGs are defined based only on molecular features (i.e. gene expression), and do not take any spatial information into account. If the spatial patterns in gene expression in a dataset mainly reflect spatial distributions of cell types (defined by gene expression), then relying on HVGs for downstream analyses may be sufficient. However, if there is further biologically meaningful spatial structure that is not captured in this way, spatially-aware methods may be needed instead.

Identifying a set of top “highly variable genes” (HVGs) is a standard step for feature selection in many scRNA-seq workflows, which can also be used as a simple and fast baseline approach in spot-based ST data, or high-plex imaging based ST data; for the former, this makes the simplified assumption that spots can be treated as equivalent to cells.

The set of top HVGs can then be used as the input for subsequent steps, such as dimensionality reduction and clustering. For a comprehensive discussion on HVG selection, we refer readers to [OSCA](https://bioconductor.org/books/release/OSCA.basic/feature-selection.html#hvg-selection).

In this example, we use the *[scran](https://bioconductor.org/packages/3.23/scran)* package ([Lun, McCarthy, and Marioni 2016](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Lun2016-scran)) to identify HVGs in a two-step procedure. We first model the mean-variance relationship, which decomposes variance into a technical component (smooth fit) and biological component (deviation thereof). Secondly, HVGs may be selected based on their rank, using a fixed number `n` or proportion `p` of genes:

A more stringent selection may be obtained by also adding an `FDR.threshold` on the significance of large variances *relative* to other genes.

Code

```
# fit mean-variance relationship, decomposing 
# variance into technical & biological components
dec <- modelGeneVar(spe)
```

```
##  Warning in fitTrendVar(fm, fv, ...): 'fitTrendVar' is deprecated.
##  Use 'scrapper::fitVarianceTrend' instead.
##  See help("Deprecated")
```

```
##  Warning in combineBlocks(collected, method = method, equiweight = equiweight, : 'combineBlocks' is deprecated.
##  See help("Deprecated")
```

Code

```
# select top 2,000 ranked genes (in terms
# of their biological variance component)
hvg <- getTopHVGs(dec, n=2e3)
```

```
##  Warning in getTopHVGs(dec, n = 2000): 'getTopHVGs' is deprecated.
##  Use 'scrapper::chooseHighlyVariableGenes' instead.
##  See help("Deprecated")
```

Code

```
# visualize mean-variance relationship
par(mar = c(4, 4, 0, 0))
fit <- metadata(dec)
plot(fit$mean, fit$var, cex = 0.5, xlab = "mean expression", ylab = "variance")
points(dec[hvg, "mean"], dec[hvg, "total"], cex = 0.5, col = "dodgerblue")
curve(fit$trend(x), add = TRUE, lwd = 2, col = "tomato")
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-feature-selection-testing/plt-hvgs-1.png)

### 29.2.2 Differentially expressed genes (DEGs)

Having clustered our spots (or cells), we can test for differentially expressed genes (DEGs) between clusters. These can be interpreted as marker genes and used to interpret clusters in terms of their function, and to help annotate them (i.e. assign biologically meaningful labels).

For details on identifying DE genes between groups of cells from scRNA-seq data, we refer readers to [OSCA](https://bioconductor.org/books/release/OSCA.basic/marker-detection.html).

Here, we will use pairwise t-tests and specifically test for upregulation (as opposed to downregulation), i.e. expression should be higher in the cluster for which a gene is reported to be a marker; see [Chapter 28](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html) for details.

Code

```
# differential gene expression analysis
mgs <- findMarkers(spe, groups=spe$BayesSpace, direction="up")
```

```
##  Warning in .findMarkers(assay(x, i = assay.type), ...): 'findMarkers' is deprecated.
##  Use 'scrapper::scoreMarkers.se' instead.
##  See help("Deprecated")
```

```
##  Warning in .local(x, ...): 'pairwiseTTests' is deprecated.
##  See help("Deprecated")
```

```
##  Warning in combineMarkers(fit$statistics, fit$pairs, pval.type = pval.type, : 'combineMarkers' is deprecated.
##  Use 'scrapper::summarizeEffects' instead.
##  See help("Deprecated")
```

Code

```
# select for a few markers per cluster
deg <- lapply(mgs, \(df) rownames(df)[df$Top <= 3])
length(deg <- unique(unlist(deg)))
```

```
##  [1] 59
```

We can visualize selected marker genes as a heatmap where bins represent the average expression (here, log-transformed library size-normalized counts) of a given gene (= columns) in a given cluster (= rows).

To visually amplify differences, we use `scale = "column"`. This will, for every gene, subtract the mean and divide by the standard deviation across per-cluster means, bringing genes of potentially very different expression levels to a comparable scale.

Code

```
# compute cluster-wise averages
pbs <- aggregateAcrossCells(spe, 
    ids = spe$BayesSpace, subset.row = deg, 
    use.assay.type = "logcounts", statistics = "mean")
```

```
##  Warning in .local(x, ...): 'aggregateAcrossCells' is deprecated.
##  Use 'scrapper::aggregateAcrossCells.se' instead.
##  See help("Deprecated")
```

```
##  using unknown matrix fallback for 'dgTMatrix'
```

Code

```
# use gene symbols as feature names
mtx <- t(assay(pbs))
colnames(mtx) <- rowData(pbs)$gene_name
# using pheatmap package
pheatmap(mat = mtx, scale = "column")
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-feature-selection-testing/plt-deg-hm-1.png)

In addition, we can plot in x-y space, i.e. coloring spots by their expression of a given marker gene:

Code

```
# select top-3 markers for each cluster & get gene symbols
gs <- unique(unlist(lapply(mgs, \(df) head(rownames(df), 3))))
gs <- rowData(spe)$gene_name[match(gs, rownames(spe))]
# gene-wise spatial plots
ps <- lapply(gs, \(.) {
    plotCoords(spe, 
        annotate = ., 
        feature_names = "gene_name", 
        assay_name = "logcounts") })
# figure arrangement
wrap_plots(ps, nrow = 4) & 
  theme(legend.key.width = unit(0.4, "lines"), 
        legend.key.height = unit(0.8, "lines")) & 
  scale_color_gradientn(colors = rev(hcl.colors(9, "Rocket")))
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-feature-selection-testing/plt-deg-xy-1.png)

## 29.3 Spatially-aware

Here, we demonstrate brief examples of how to identify a set of top SVGs using (*[nnSVG](https://bioconductor.org/packages/3.23/nnSVG)* ([Weber et al. 2023](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Weber2023-nnSVG)) and *[DESpace](https://bioconductor.org/packages/3.23/DESpace)* ([Cai, Robinson, and Tiberi 2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Cai2024-DESpace))). These methods are available through Bioconductor and can be easily integrated into Bioconductor-based workflows.

### 29.3.1 Spatially-variable genes (SVGs)

SVGs are usually identified integrating gene expression measurements with spatial coordinates, either with or without predefined spatial domains. SVGs approaches can be broadly categorized into three types: overall SVGs, spatial domain-specific SVGs, and cell type-specific SVGs ([Yan, Hua, and Li 2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Yan2024-categorization-SVGs)).

The detection of **overall SVGs** is sometimes used as a feature selection step for further downstream analyses such as spatially-aware clustering (see [Chapter 28](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html)). Several methods have been proposed for detecting overall SVGs; below, we report some few notable examples:

* *[spatialDE](https://bioconductor.org/packages/3.23/spatialDE)* ([Svensson, Teichmann, and Stegle 2018](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Svensson2018-SpatialDE)) and *[nnSVG](https://bioconductor.org/packages/3.23/nnSVG)* ([Weber et al. 2023](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Weber2023-nnSVG)), which are based on a Gaussian process model;
* [Moran’s I](https://en.wikipedia.org/wiki/Moran%27s_I) and [Geary’s C](https://en.wikipedia.org/wiki/Geary%27s_C), which ranks genes according to their observed spatial autocorrelation (see [Chapter 31](https://bioconductor.org/books/release/OSTA/pages/ind-spatial-statistics.html)); and,
* *[SPARK](https://github.com/xzhoulab/SPARK)* ([Sun, Zhu, and Zhou 2020](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Sun2020-SPARK); [Zhu, Sun, and Zhou 2021](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Zhu2021-SPARK-X)), which uses a non-parametric test of the covariance matrices of the spatial expression data.

**Spatial domain-specific** SVGs target changes in gene expression between spatial domains, which are used to summarize the whole spatial information. Genes displaying expression changes across spatial clusters indicate SVGs. Spatial domains can be predefined based on morphology knowledge, or identified through spatially-aware clustering approaches such as *[BayesSpace](https://bioconductor.org/packages/3.23/BayesSpace)* ([Zhao et al. 2021](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Zhao2021-BayesSpace)) and *[Banksy](https://bioconductor.org/packages/3.23/Banksy)* ([Singhal et al. 2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Singhal2024-BANKSY)). Methods that belong to this category include *[DESpace](https://bioconductor.org/packages/3.23/DESpace)* ([Cai, Robinson, and Tiberi 2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Cai2024-DESpace)) in R, and *[SpaGCN](https://github.com/jianhuupenn/SpaGCN)* ([Hu et al. 2021](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Hu2021-SpaGCN)) in Python.

**Cell type-specific** SVG methods leverage external cell type annotations to identify SVGs within cell types. They analyze interaction effects between cell types and spatial coordinates ([Yan, Hua, and Li 2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Yan2024-categorization-SVGs)). Examplary methods in R include *[CTSV](https://bioconductor.org/packages/3.23/CTSV)* ([J. Yu and Luo 2022](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Yu2022-CTSV)), *C-SIDE* (implemented in *[spacexr](https://bioconductor.org/packages/3.23/spacexr)*; ([Cable et al. 2022](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Cable2022-C-SIDE))), and *[spVC](https://github.com/shanyu-stat/spVC)* ([S. Yu and Li 2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Yu2024-spVC)).

### 29.3.2 nnSVG

In this example, we use a small subset of the dataset for faster runtime. We select a subset of the data, by subsampling the set of spots and including stringent filtering for lowly expressed genes.

A full analysis with `nnSVG` using all spots for this dataset and default filtering parameters for an individual Visium sample from human brain tissue (available from *[spatialLIBD](https://bioconductor.org/packages/3.23/spatialLIBD)*) takes around 45 minutes on a standard laptop.

Code

```
# set random seed for number generation
# in order to make results reproducible
set.seed(123)
# sample 100 spots to decrease runtime in this demo
# (note: skip this step in full analysis)
n <- 100
sub <- spe[, sample(ncol(spe), 100)]
# filter lowly expressed genes using stringent
# criteria to decrease runtime in this demo
# (note: use default criteria in full analysis)
sub <- filter_genes(sub,     # filter for genes with...
    filter_genes_ncounts=10, # at least 10 counts in
    filter_genes_pcspots=3)  # at least 3% of spots
# re-normalize counts post-filtering
sub <- logNormCounts(sub)
```

```
##  Warning in .local(x, ...): 'normalizeCounts' is deprecated.
##  Use 'scrapper::normalizeCounts' instead.
##  See help("Deprecated")
```

Code

```
# run nnSVG
set.seed(123)
sub <- nnSVG(sub)

# extract gene-level results
res_nnSVG <- rowData(sub)
# show results
head(res_nnSVG, 3)
```

```
##  DataFrame with 3 rows and 18 columns
##                          gene_id   gene_name    feature_type subsets_mito
##                      <character> <character>     <character>    <logical>
##  ENSG00000171603 ENSG00000171603      CLSTN1 Gene Expression        FALSE
##  ENSG00000162545 ENSG00000162545     CAMK2N1 Gene Expression        FALSE
##  ENSG00000117632 ENSG00000117632       STMN1 Gene Expression        FALSE
##                   sigma.sq    tau.sq       phi    loglik   runtime      mean
##                  <numeric> <numeric> <numeric> <numeric> <numeric> <numeric>
##  ENSG00000171603  0.174761  0.539773   5.41081  -121.843     0.019   2.03224
##  ENSG00000162545  0.269047  0.372045   3.08577  -108.057     0.018   2.71693
##  ENSG00000117632  0.239898  0.514311   6.13963  -123.305     0.019   2.64106
##                        var     spcov   prop_sv loglik_lm   LR_stat      rank
##                  <numeric> <numeric> <numeric> <numeric> <numeric> <numeric>
##  ENSG00000171603  0.709124  0.205706  0.244580  -124.205   4.72492        68
##  ENSG00000162545  0.573078  0.190913  0.419670  -113.555  10.99542        40
##  ENSG00000117632  0.742838  0.185453  0.318079  -126.527   6.44437        56
##                        pval      padj
##                   <numeric> <numeric>
##  ENSG00000171603 0.09418802 0.2186956
##  ENSG00000162545 0.00409613 0.0163845
##  ENSG00000117632 0.03986790 0.1139083
```

Code

```
# count significant SVGs (at 5% FDR significance level)
table(res_nnSVG$padj <= 0.05)
```

```
##  
##  FALSE  TRUE 
##    111    49
```

Code

```
# identify the top-ranked SVGs
res_nnSVG$gene_name[res_nnSVG$rank == 1]
```

```
##  [1] "MBP"
```

Code

```
# store the top 7 SVGs
top_nnSVG <- res_nnSVG$gene_name[res_nnSVG$rank < 7.5]
```

### 29.3.3 `DESpace`

`DESpace` relies on pre-computed spatial domains to summarize the primary spatial structures of the data; see [Chapter 28](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html) on clustering.

Code

```
plotCoords(spe, 
    annotate="BayesSpace") +
    theme(legend.key.size=unit(0, "lines")) +
    scale_color_manual(values=unname(pals::trubetskoy()))
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-feature-selection-testing/plt-clu-xy-1.png)

Code

```
# run DESpace
res <- svg_test(spe, cluster_col="BayesSpace")
head(res_DESpace <- res$gene_results)
```

```
##                          gene_id       LR    logCPM PValue FDR
##  ENSG00000101210 ENSG00000101210 1714.407 10.641755      0   0
##  ENSG00000074317 ENSG00000074317 1851.823 10.585181      0   0
##  ENSG00000104435 ENSG00000104435 1907.921 10.555517      0   0
##  ENSG00000183036 ENSG00000183036 1580.067  9.797765      0   0
##  ENSG00000173267 ENSG00000173267 1559.682 10.050258      0   0
##  ENSG00000170027 ENSG00000170027 1755.490 10.864269      0   0
```

Code

```
# count significant SVGs (at 5% FDR significance level)
table(res_DESpace$FDR <= 0.05)
```

```
##  
##  FALSE  TRUE 
##   5302  9837
```

NoteDownstream analyses

## 29.4 Downstream analyses

The set of top SVGs may be further investigated, e.g. by plotting the spatial expression of several top genes and via gene pathway analyses (i.e., comparing significant SVGs with known gene sets associated with specific biological functions).

Code

```
top_HVGs <- getTopHVGs(dec, n=(n <- 6))
```

```
##  Warning in getTopHVGs(dec, n = (n <- 6)): 'getTopHVGs' is deprecated.
##  Use 'scrapper::chooseHighlyVariableGenes' instead.
##  See help("Deprecated")
```

Code

```
top_DEGs <- lapply(mgs, \(df) rownames(df)[df$Top == 1])
top_DEGs <- unique(unlist(top_DEGs))[seq_len(6)]
top_DESpace <- res_DESpace$gene_id[seq_len(6)]
```

### 29.4.1 Visualization

To visualize the expression levels of selected genes in spatial coordinates on the tissue slide, we can use plotting functions from the *[ggspavis](https://bioconductor.org/packages/3.23/ggspavis)* package.

Code

```
# get top SVGs from each method
gs <- list(
    HVGs=top_HVGs, 
    DEGs=top_DEGs, 
    DESpace=top_DESpace)
# get gene symbols from ensembl identifiers
idx <- match(unlist(gs), rowData(spe)$gene_id)
.gs <- rowData(spe)$gene_name[idx]
# expression plots for each top gene
ps <- lapply(seq_along(.gs), \(.) {
    plotCoords(spe, 
        point_size=0,
        annotate=.gs[.], 
        assay_name="logcounts", 
        feature_names="gene_name") + 
        if (. %% 6 == 1) list(
            ylab(names(gs)[ceiling(./6)]), 
            theme(axis.title.y=element_text()))
}) 
wrap_plots(ps, nrow=3) & theme(
    legend.key.width=unit(0.4, "lines"),
    legend.key.height=unit(0.8, "lines")) &
    scale_color_gradientn(colors = pals::parula())
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-feature-selection-testing/plt-xy-1.png)

### 29.4.2 Comparison

We can compare the ranks of the genes detected by each method and compute pairwise correlations, highlighting two known cortical layer-associated SVGs: *MOBP* and *SNAP25*. While all four methods - HVGs, DEGs, SVGs identified through `nnSVG` and `DESpace` - yield similar gene ranks, each method captures distinct aspects of gene expression, with varying pairwise correlations between them.

Code

```
# subset data for the 113 genes nnSVG is based on
sub_gene <- rowData(sub)$gene_id
sub_DESpace <- res_DESpace[sub_gene, ] 
sub_HVG <- as.data.frame(dec[sub_gene, ])

# aggregate DEGs for each spatial domain
subset_mgs <- lapply(mgs, \(x) x[sub_gene, 1:3] |> as.data.frame())
sub_DEG <- do.call(cbind, subset_mgs) 
top_cols <- sub_DEG |> select(ends_with(".Top"))
sub_DEG$Top <- do.call(pmin, c(top_cols, na.rm = TRUE))

# compute ranks 
sub_DESpace$rank <- rank(sub_DESpace$FDR, ties.method = "first")
sub_HVG$rank <- rank(-1 * sub_HVG$bio, ties.method = "first")
sub_DEG$rank <- rank(sub_DEG$Top, ties.method = "first")

# combine 'rank' column for each method
res_all <- list(
    nnSVG = as.data.frame(res_nnSVG),
    DESpace = sub_DESpace, HVGs = sub_HVG, DEGs = sub_DEG
)
rank_all <- do.call(cbind, lapply(res_all, `[[`, "rank"))
rank_all <- data.frame(gene_id = sub_gene, rank_all)
```

Code

```
# known SVGs for this data
known_genes <- c("MOBP", "SNAP25")
# method names
method_names <- c("nnSVG", "DESpace", "HVGs", "DEGs")
# convert data structure
rank_long <- rank_all |>
    left_join(data.frame(rowData(sub)[, c("gene_id", "gene_name")]), by = "gene_id") |>
    select(all_of(c("gene_name", method_names))) |>
    pivot_longer(cols = c(nnSVG, DESpace, HVGs, DEGs), 
                 names_to = "method", 
                 values_to = "rank")
# all pairwise comparisons
df_pairs <- t(combn(method_names, 2)) |> as.data.frame()
# function to plot each pairwise comparison
plot_pairwise_comparison <- function(m1, m2, df) {
  # filter the data for the two methods being compared
  df <- df |>
      filter(method %in% c(m1, m2)) |>
      pivot_wider(names_from = method, values_from = rank)
  # compute pearson correlation between methods
  cor_val <- cor(df[[m1]], df[[m2]], method = "spearman")
  # plot
  ggplot(df, aes(x = .data[[m1]], y = .data[[m2]])) +
      geom_point() + 
      geom_text_repel(data = df %>% filter(gene_name %in% known_genes), 
                      aes(label = gene_name), color = "red", size = 3.25, 
                      nudge_x = 50, nudge_y = 10, box.padding = 0.5) +
      labs(x = paste(m1, "rank"), y = paste(m2, "rank"),
           title = paste(m2, "vs.", m1, ": Cor = ", round(cor_val, 2))) +
      #scale_color_manual(values = c("darkorange", "firebrick3", "deepskyblue2")) +
      theme_bw() + coord_fixed() + 
      xlim(c(0, 120)) + ylim(c(0, 120))
}

# generate and display all pairwise comparison plots
plots <- lapply(seq_len(nrow(df_pairs)), \(i) {
    plot_pairwise_comparison(df_pairs[i, 2], df_pairs[i, 1],rank_long)
})

wrap_plots(plots, ncol = 3)
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-feature-selection-testing/plt-scatter-nnsvg-1.png)

## 29.5 Appendix

### Reviews

* Adhikari et al. ([2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Adhikari2024-advances-SVGs))
* Yan, Hua, and Li ([2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Yan2024-categorization-SVGs))

### Benchmarks

* Li et al. ([2023](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Li2023-benchmarking-SVGs)) compares 14 methods using 60 simulated datasets, generated using four different strategies, 12 experimental ST datasets, and 3 spatial ATAC-seq datasets.
* Chen, Kim, and Yang ([2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Chen2024-evaluating-SVGs)) compares 8 methods based on 22 experimental datasets (8 technologies, 6 tissue types) and 9 datasets simulated using *[scDesign3](https://bioconductor.org/packages/3.23/scDesign3)* ([Song et al. 2024](https://bioconductor.org/books/release/OSTA/pages/ind-feature-selection-testing.html#ref-Song2024-scDesign3)).

### References

Adhikari, Sikta Das, Jiaxin Yang, Jianrong Wang, and Yuehua Cui. 2024. “Recent Advances in Spatially Variable Gene Detection in Spatial Transcriptomics.” *Computational and Structural Biotechnology Journal* 23: 883–91. <https://doi.org/10.1016/j.csbj.2024.01.016>.

Cable, Dylan M., Evan Murray, Vignesh Shanmugam, Simon Zhang, Luli S. Zou, Michael Diao, Haiqi Chen, Evan Z. Macosko, Rafael A. Irizarry, and Fei Chen. 2022. “Cell Type-Specific Inference of Differential Expression in Spatial Transcriptomics.” *Nature Methods* 19: 1076–87. <https://doi.org/10.1038/s41592-022-01575-3>.

Cai, Peiying, Mark D Robinson, and Simone Tiberi. 2024. “DESpace: Spatially Variable Gene Detection via Differential Expression Testing of Spatial Clusters.” *Bioinformatics* 40 (btae027, 2). <https://doi.org/10.1093/bioinformatics/btae027>.

Chen, Carissa, Hani Jieun Kim, and Pengyi Yang. 2024. “Evaluating Spatially Variable Gene Detection Methods for Spatial Transcriptomics Data.” *Genome Biology* 25 (18). <https://doi.org/10.1186/s13059-023-03145-y>.

Hu, Jian, Xiangjie Li, Kyle Coleman, Amelia Schroeder, Nan Ma, David J. Irwin, Edward B. Lee, Russell T. Shinohara, and Mingyao Li. 2021. “SpaGCN: Integrating Gene Expression, Spatial Location and Histology to Identify Spatial Domains and Spatially Variable Genes by Graph Convolutional Network.” *Nature Methods* 18: 1342–51. <https://doi.org/10.1038/s41592-021-01255-8>.

Li, Zhijian, Zain M. Patel, Dongyuan Song, Guanao Yan, Jingyi Jessica Li, and Luca Pinello. 2023. “Benchmarking Computational Methods to Identify Spatially Variable Genes and Peaks.” *bioRxiv*. <https://doi.org/10.1101/2023.12.02.569717>.

Lun, Aaron T. L., Davis J. McCarthy, and John C. Marioni. 2016. “A Step-by-Step Workflow for Low-Level Analysis of Single-Cell RNA-Seq Data with Bioconductor.” *F1000Research* 5 (2122). <https://doi.org/10.12688/f1000research.9501.2>.

Singhal, Vipul, Nigel Chou, Joseph Lee, Yifei Yue, Jinyue Liu, Wan Kee Chock, Li Lin, et al. 2024. “BANKSY Unifies Cell Typing and Tissue Domain Segmentation for Scalable Spatial Omics Data Analysis.” *Nature Genetics* 56: 431–41. <https://doi.org/10.1038/s41588-024-01664-3>.

Song, Dongyuan, Qingyang Wang, Guanao Yan, Tianyang Liu, Tianyi Sun, and Jingyi Jessica Li. 2024. “scDesign3 Generates Realistic in Silico Data for Multimodal Single-Cell and Spatial Omics.” *Nature Biotechnology* 42: 247–52. <https://doi.org/10.1038/s41587-023-01772-1>.

Sun, Shiquan, Jiaqiang Zhu, and Xiang Zhou. 2020. “Statistical Analysis of Spatial Expression Patterns for Spatially Resolved Transcriptomic Studies.” *Nature Methods* 17: 193–200. <https://doi.org/10.1038/s41592-019-0701-7>.

Svensson, Valentine, Sarah A Teichmann, and Oliver Stegle. 2018. “SpatialDE: Identification of Spatially Variable Genes.” *Nature Methods* 15: 343–46. <https://doi.org/10.1038/nmeth.4636>.

Weber, Lukas M., Arkajyoti Saha, Abhirup Datta, Kasper D. Hansen, and Stephanie C. Hicks. 2023. “nnSVG for the Scalable Identification of Spatially Variable Genes Using Nearest-Neighbor Gaussian Processes.” *Nature Communications* 14 (4059). <https://doi.org/10.1038/s41467-023-39748-z>.

Yan, Guanao, Shuo Harper Hua, and Jingyi Jessica Li. 2024. “Categorization of 33 Computational Methods to Detect Spatially Variable Genes from Spatially Resolved Transcriptomics Data.” *arXiv*. <https://doi.org/10.48550/arXiv.2405.18779>.

Yu, Jinge, and Xiangyu Luo. 2022. “Identification of Cell-Type-Specific Spatially Variable Genes Accounting for Excess Zeros.” *Bioinformatics* 38: 4135–44. <https://doi.org/10.1093/bioinformatics/btac457>.

Yu, Shan, and Wei Vivian Li. 2024. “spVC for the Detection and Interpretation of Spatial Gene Expression Variation.” *Genome Biology* 25 (103). <https://doi.org/10.1186/s13059-024-03245-3>.

Zhao, Edward, Matthew R. Stone, Xing Ren, Jamie Guenthoer, Kimberly S. Smythe, Thomas Pulliam, Stephen R. Williams, et al. 2021. “Spatial Transcriptomics at Subspot Resolution with BayesSpace.” *Nature Biotechnology* 39: 1375–84. <https://doi.org/10.1038/s41587-021-00935-2>.

Zhu, Jiaqiang, Shiquan Sun, and Xiang Zhou. 2021. “SPARK-x: Non-Parametric Modeling Enables Scalable and Robust Detection of Spatial Expression Patterns for Large Spatial Transcriptomic Studies.” *Genome Biology* 22 (184). <https://doi.org/10.1186/s13059-021-02404-0>.

Back to top
