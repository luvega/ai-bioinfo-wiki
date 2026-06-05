---
source: OSTA
title: "28 Clustering"
original_url: https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html
ingested_at: 2026-06-04T01:51:16+00:00
status: source_ingested
---

# 28  Clustering

## 28.1 Preamble

### 28.1.1 Introduction

In spatial transcriptomics data, we can apply clustering algorithms to identify spatial domains, which represent spatially defined regions consisting of relatively consistent gene expression profiles. For example, spatial domains may consist of regions containing cells from a single cell type or a consistent mixture of cell types.

Several alternative approaches exist for identifying spatial domains. One strategy involves applying standard clustering algorithms from single-cell workflows without incorporating spatial information. Alternatively, spatial information can be integrated at various stages of the workflow. For example, spatial data can inform preprocessing steps, such as selecting spatially variable genes (SVGs), followed by the application of either non-spatial or spatial clustering algorithms. Another widely used strategy involves generating a latent space that incorporates spatial coordinates, often leveraging Bayesian framework or neural networks.

As advancements in spatial transcriptomics techniques enhance tissue resolution, computational tradeoffs between various approaches and parameters become increasingly relevant.

It is also important to keep in mind that when we use clustering to define cell types and/or states, these can be defined at various resolutions (or even on a continuum). The optimal number of clusters depends on the biological context – in particular, there is no “true” number of clusters, since this depends on the biological context (e.g. if we are comparing major cell populations vs. comparing rare subtypes), so the choice of the optimal number of clusters or resolutions requires some judgment and biological interpretation.

Once we have identified spatial domains, these can then be further investigated in additional downstream analyses.

### 28.1.2 Dependencies

Code

```
library(scran)
library(scater)
library(igraph)
library(Banksy)
library(ggspavis)
library(pheatmap)
library(basilisk)
library(patchwork)
library(OSTA.data)
library(BayesSpace)
library(reticulate)
library(SpatialExperiment)
# set seed for random number generation
# in order to make results reproducible
set.seed(2025)
# load processed Xenium datasets
spe <- readRDS("img-spe_cl.rds")
```

## 28.2 Clustering

### 28.2.1 Non-spatial

As a baseline, we will perform a standard graph-based clustering approach developed for scRNA-seq data, using molecular features (gene expression) only. Specifically, we construct a shared nearest neighbor (SNN) graph based on non-spatial PCs (`reducedDim` slot `"PCA_tx"`), and use the Leiden algorithm for community detection ([Traag, Waltman, and Eck 2019](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Traag2019-Louvain-to-Leiden)). [The `resolution` parameter used here was selected in order to obtain a similar number of clusters annotated by the authors.]

Code

```
# build cellular shared nearest-neighbor (SNN) graph
g <- buildSNNGraph(spe, use.dimred="PCA_tx", type="jaccard", k=20)
```

```
##  Warning in .buildSNNGraph(reducedDim(x, use.dimred), d = NA, transposed = TRUE, : 'buildSNNGraph' is deprecated.
##  Use 'bluster::makeSNNGraph' instead.
##  See help("Deprecated")
```

Code

```
# cluster using Leiden community detection algorithm
k <- cluster_leiden(g, objective_function="modularity", resolution=1.2)
table(spe$Leiden <- factor(k$membership))
```

```
##  
##      1     2     3     4     5     6     7     8     9    10    11    12 
##  11568  3492 13007  5460 11417 25518 13042  5402 14789 14433 11607  4028 
##     13    14 
##   3891  2614
```

### 28.2.2 Spatially-aware

Several methods to identify spatial domains in ST data have recently been developed, which each have various methodological and computational tradeoffs. A few example include *[BayesSpace](https://bioconductor.org/packages/3.23/BayesSpace)* ([Zhao et al. 2021](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Zhao2021-BayesSpace)), *[Banksy](https://bioconductor.org/packages/3.23/Banksy)* ([Singhal et al. 2024](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Singhal2024-BANKSY)) and *[PRECAST](https://CRAN.R-project.org/package=PRECAST)* ([W. Liu et al. 2023](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Liu2023-PRECAST)) in R, as well as *[CellCharter](https://github.com/CellCharter)* ([Varrone et al. 2024](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Varrone2024-CellCharter)) and *[SpaceFlow](https://github.com/SpaceFlow)* ([Ren et al. 2022](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Ren2022-SpaceFlow)) in Python.

Here, we demonstrate tools representative of different methodologies, namely, (probabilistic) `BayesSpace` for seq-based Visium, as well as (neighborhood-based) `Banksy` and (encoder-based) `CellCharter` for img-based Xenium data.

#### 28.2.2.1 Probabilistic

Underlying *[BayesSpace](https://bioconductor.org/packages/3.23/BayesSpace)* ([Zhao et al. 2021](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Zhao2021-BayesSpace)) is a Bayesian model that encourages neighboring spots to belong to the same cluster, and utilizes Markov Chain Monte Carlo (MCMC) for estimating model parameters.

Default parameters are `nrep=50,000` MCMC iterations and a burn-in period of `burn.in=1,000`; the authors recommend running with at least 10,000 iterations. Here, we use fewer iterations for the sake of runtime, which will arguably compromise performance. Note that, since MCMC is stochastic, a seed for random number generation should be set in order to make results reproducible.

Code

```
# load processed Visium dataset
vis <- readRDS("seq-spe_cl.rds")
# prepare data for 'BayesSpace'
# skipping PCA (already computed)
.vis <- spatialPreprocess(vis, skip.PCA=TRUE)
# perform spatial clustering with 'BayesSpace'
# using 'd=20' PCs and targeting 'q=10' clusters
.vis <- spatialCluster(.vis, q=10, d=20, nrep=1e3, burn.in=100) 
table(vis$BayesSpace <- factor(.vis$spatial.cluster))
```

```
##  
##    1   2   3   4   5   6   7   8   9  10 
##  560 279 400 545 367 478 313  74 252 371
```

#### 28.2.2.2 Neighborhood-based

*[BANKSY](https://bioconductor.org/packages/3.23/BANKSY)* ([Singhal et al. 2024](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Singhal2024-BANKSY)) embeds cells in a product space of their own and their local neighborhood’s (average) transcriptome, representing cell state and microenvironment. We have already computed `Banksy` PCs in [Chapter 27](https://bioconductor.org/books/release/OSTA/pages/ind-dimensionality-reduction.html) (`reducedDim` slot `PCA_sp`) so that here, we perform SNN graph-based Leiden clustering on said PCs in order to obtain spatially-aware cluster assignments:

Note that we are using a lower `resolution` here, as `Banksy` PCs tend to yield more clusters on the data at hand.

Code

```
# perform SNN graph-based clustering on 'Banksy' PCs using
# same parameters as for 'non-spatial' clustering above
g <- buildSNNGraph(spe, use.dimred="PCA_sp", type="jaccard", k=20)
```

```
##  Warning in .buildSNNGraph(reducedDim(x, use.dimred), d = NA, transposed = TRUE, : 'buildSNNGraph' is deprecated.
##  Use 'bluster::makeSNNGraph' instead.
##  See help("Deprecated")
```

Code

```
k <- cluster_leiden(g, objective_function="modularity", resolution=0.8)
table(spe$Banksy <- factor(k$membership))
```

```
##  
##      1     2     3     4     5     6     7     8     9    10    11    12 
##  11177  3804  5402 11168 14096 21268  9535  9164 12564 16500  4154   570 
##     13    14    15    16    17 
##   3474 12925   632  3166   669
```

#### 28.2.2.3 Encoder-based

Another category of spatially-aware clustering method uses encoder architectures to generate a latent embedding incorporating both spatial and transcriptomics information, which is then clustered using standard algorithms. One typical example is *[cellcharter](https://github.com/CSOgroup/cellcharter)* ([Varrone et al. 2024](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Varrone2024-CellCharter)), which uses a variational auto-encoder to generate a latental feature space and aggregate the features of each spot across its neighbors to preserve their spatial context.

NoteOther methods

Several other published methods have also adopted encoder architectures in different ways to perform spatially-aware clustering. *[STAGATE](https://github.com/zhanglabtools/STAGATE)* ([Dong and Zhang 2022](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Dong2022-STAGATE)) uses a graph attention autoencoder to integrate spatial and transcriptional data by modeling spatial neighborhoods as graphs, whereas *[PROST](https://github.com/Tang-Lab-super/PROST)* ([Liang et al. 2024](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Liang2024-PROST)) employs a self-attention transformer-based encoder to learn spatial patterns by jointly modeling gene expression and spatial coordinates. Graph-based encoder methods, such as `STAGATE`, may be particularly well-suited for imaging-based ST data, as their ability to model spatial neighborhoods as graphs aligns naturally with the continuous and fine-grained spatial organization of tissues captured through imaging.

Code

```
# initialize 'basilisk' environment
env <- BasiliskEnvironment(
  envname="CellCharter", pkgname="OSTA",
  channels=c("conda-forge", "pytorch"),
  packages=c(
    "python=3.10.15",
    "pytorch=1.12.1",
    "torchvision=0.13.1",
    "torchaudio=0.12.1"),
  pip=c(
    "scvi-tools==0.20.3",
    "cellcharter==0.2.0",
    "anndata==0.10.9",
    "scanpy==1.10.4"))
# activate underlying conda environment
use_condaenv(obtainEnvironmentPath(env))
counts <- r_to_py(t(counts(spe)))
coords <- r_to_py(spatialCoords(spe))
```

Code

```
import cellcharter as cc
import anndata as ad
import squidpy as sq
import pandas as pd
import numpy as np
import random
import scvi

adata = ad.AnnData(X = r.counts,
                   obsm = {"spatial":r.coords},
                   layers = {"counts": r.counts})

seed = 2025
random.seed(seed)
scvi.settings.seed = seed

# variational autoencoder for feature extraction
scvi.model.SCVI.setup_anndata(adata, layer="counts")
model = scvi.model.SCVI(adata, n_hidden=64)
model.train(early_stopping=True,
    # the parameters below aim to reduce runtime; 
    # in reality, it'd be better to use defaults
    max_epochs=70, batch_size=512, train_size=0.5, validation_size=0.2)

adata.obsm["X_scVI"] = model.get_latent_representation(adata).astype(np.float32)

# Getting neighborhood aggregation
sq.gr.spatial_neighbors(adata, coord_type="generic", delaunay=True, spatial_key="spatial", percentile=99)
cc.gr.aggregate_neighbors(adata, n_layers=3, use_rep="X_scVI", out_key="X_cellcharter")

# clustering by scanning a range of data number
mod = cc.tl.Cluster(n_clusters=14, random_state=seed)
mod.fit(adata, use_rep="X_cellcharter")

label_df = pd.DataFrame({"label": mod.predict(adata, use_rep="X_cellcharter")}) 
label_df[["label"]].value_counts()
```

Code

```
# pull 'CellCharter' assignments from Python into R
spe$CellCharter <- unlist(py$label_df)
```

## 28.3 Downstream

### 28.3.1 Visualization

Let’s visualize the assignment obtains from non-spatial and spatially-aware clustering:

Code

```
ks <- c("Label", "Leiden", "Banksy")#, "CellCharter")
lapply(ks, \(.) {
    plt <- plotCoords(spe, annotate=.)
    plt$layers[[1]]$aes_params$stroke <- 0
    plt$layers[[1]]$aes_params$size <- 0.2
    plt
}) |>
    wrap_plots(nrow=2) &
    scale_color_manual(values=unname(pals::trubetskoy())) &
    theme(legend.key.size=unit(0, "lines"), legend.justification="left")
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-clustering/plot-xy-k-joint-1.png)

Especially in large tissues, and when there are many subpopulations, the above type of plot makes it difficult to spot rare subpopulations, and might cause cells to overlap in regions with high cellular density. This can be misleading, as we will tend to see only highly abundant subpopulations, or the cells plotted last and on top (i.e., later columns in the object).

To better distinguish between different subpopulations, we can instead generate separate spatial plots with one subpopulation highlighted at a time:

Code

```
# plot selected clusters in order of frequency,
# highlighting cells assigned to cluster 'k'
lapply(tail(names(sort(table(spe$Banksy))), 12), \(k) {
    spe$foo <- spe$Banksy == k
    spe <- spe[, order(spe$foo)]
    plt <- plotCoords(spe, annotate="foo")
    plt$layers[[1]]$aes_params$stroke <- 0
    plt$layers[[1]]$aes_params$size <- 0.2
    plt + ggtitle(k)
}) |>
    wrap_plots(nrow=3) &
    scale_color_manual(values=c("lavender", "purple")) &
    theme(plot.title=element_text(hjust=0.5), legend.position="none")
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-clustering/plot-xy-k-split-1.png)

NotePC regression

### 28.3.2 PC regression

For any single-cell analysis where downstream tasks rely on PCs, it is useful to perform linear regression of (continuous or categorical) covariates of interest onto PCs. This quantifies the variance explained by the covariate and can help assess the extend of unwanted variation (due to, e.g., cell area) as opposed to subpopulations driving transcriptional differences. Here, we regress total counts, cell area, and cluster assignments from different methods against PCs:

Code

```
pcs <- reducedDim(spe, "PCA_tx")
ids <- c("total_counts", "cell_area", ks)
pcr <- lapply(ids, \(id) {
    fit <- summary(lm(pcs ~ spe[[id]]))
    r2 <- sapply(fit, \(.) .$adj.r.squared)
    data.frame(id, pc=seq_along(r2), r2)
}) |> do.call(what=rbind)
```

Here, `Leiden` (transcription-only) and `Banksy` (spatially-aware) clusterings perform similar in terms of capturing (spatially unaware) PCs; as to be expected, `Leiden` clusters do slightly better. Had we set a higher value for \(\lambda\) when running `Banksy`, results would diverge more; vice versa, using spatial PCs for regression would have `Leiden` clusters perform worse. Also, note that we would expect results to converge for \(\lambda=0\).

Code

```
pcr$id <- factor(pcr$id, ids)
pal <- c("red", "magenta", "gold", "cyan", "blue", "black")
ggplot(pcr, aes(pc, r2, col=id)) +
    geom_line(show.legend=FALSE) + geom_point() +
    scale_color_manual("predictor", values=pal) +
    scale_x_continuous(breaks=c(1, seq(5, 20, 5))) +
    scale_y_continuous(limits=c(0, 1), breaks=seq(0, 1, 0.2)) +
    labs(x="principal component", y="coeff. of determination") +
    guides(col=guide_legend(override.aes=list(size=2))) +
    coord_cartesian(xlim=c(1, 20)) +
    theme_minimal() + theme(
        panel.grid.minor=element_blank(),
        legend.key.size=unit(0, "lines"))
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-clustering/plt-pcr-1.png)

### 28.3.3 DGE analysis

To help characterize (unsupervised) clusters, we want to identify ‘markers’ for each subpopulation, i.e., features whose expression is positively or negatively restricted to (a) specific subpopulation(s). For details on identifying genes that are differentially expressed (DE) between groups of cells, we refer readers to [OSCA](https://bioconductor.org/books/3.19/OSCA.basic/marker-detection.html); a standard approach is given below, visualizing the average expression of exemplary markers across clusters:

Code

```
# differential gene expression analysis
mgs <- findMarkers(spe, groups=spe$Leiden, direction="up")
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
top <- lapply(mgs, \(df) rownames(df)[df$Top <= 3])
length(top <- unique(unlist(top)))
```

```
##  [1] 69
```

Code

```
# average expression by clusters
pbs <- aggregateAcrossCells(spe, 
    ids=spe$Leiden, subset.row=top, 
    use.assay.type="logcounts", statistics="mean")
```

```
##  Warning in .local(x, ...): 'aggregateAcrossCells' is deprecated.
##  Use 'scrapper::aggregateAcrossCells.se' instead.
##  See help("Deprecated")
```

Code

```
# visualize averages z-scaled across clusters
pheatmap(mat=t(assay(pbs)), scale="column", breaks=seq(-2, 2, length=101))
```

![](../../../../raw/bioconductor_books/assets/OSTA/ind-clustering/plt-mgs-hm-1.png)

## 28.4 Appendix

### Reviews

* Wang et al. ([2024](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Wang2024-review-spatial-domain)) categorize ST clustering approaches into probability statistics-, graph neural network- and contrastive learning-based approaches, and review their advantages and limitations for clustering of data from seq- and img-based assays.

### Benchmarks

* Hu et al. ([2024](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Hu2024-benchmark-clustering)) compare 16 graph- and statistic-based approaches, including `BayesSpace` and `BANKSY`, across 10 (mostly seq-based) datasets.
* T. Liu et al. ([2024](https://bioconductor.org/books/release/OSTA/pages/ind-clustering.html#ref-Liu2024-network-clustering)) compare eight GNN-based approaches, including `SpaceFlow`, across four seq- and one img-based dataset.

### References

Dong, Kangning, and Shihua Zhang. 2022. “Deciphering Spatial Domains from Spatially Resolved Transcriptomics with an Adaptive Graph Attention Auto-Encoder.” *Nature Communications* 13 (1739). <https://doi.org/10.1038/s41467-022-29439-6>.

Hu, Yunfei, Manfei Xie, Yikang Li, Mingxing Rao, Wenjun Shen, Can Luo, Haoran Qin, Jihoon Baek, and Xin Maizie Zhou. 2024. “Benchmarking Clustering, Alignment, and Integration Methods for Spatial Transcriptomics.” *Genome Biology* 25 (212). <https://doi.org/10.1186/s13059-024-03361-0>.

Liang, Yuchen, Guowei Shi, Runlin Cai, Yuchen Yuan, Ziying Xie, Long Yu, Yingjian Huang, et al. 2024. “PROST: Quantitative Identification of Spatially Variable Genes and Domain Detection in Spatial Transcriptomics.” *Nature Communications* 15 (600). <https://doi.org/10.1038/s41467-024-44835-w>.

Liu, Teng, Zhao-Yu Fang, Zongbo Zhang, Yongxiang Yu, Min Li, and Ming-Zhu Yin. 2024. “A Comprehensive Overview of Graph Neural Network-Based Approaches to Clustering for Spatial Transcriptomics.” *Computational and Structural Biotechnology Journal* 23: 106–28. <https://doi.org/10.1016/j.csbj.2023.11.055>.

Liu, Wei, Xu Liao, Ziye Luo, Yi Yang, Mai Chan Lau, Yuling Jiao, Xingjie Shi, et al. 2023. “Probabilistic Embedding, Clustering, and Alignment for Integrating Spatial Transcriptomics Data with PRECAST.” *Nature Communications* 14 (296). <https://doi.org/10.1038/s41467-023-35947-w>.

Ren, Honglei, Benjamin L. Walker, Zixuan Cang, and Qing Nie. 2022. “Identifying Multicellular Spatiotemporal Organization of Cells with SpaceFlow.” *Nature Communications* 13 (4076). <https://doi.org/10.1038/s41467-022-31739-w>.

Singhal, Vipul, Nigel Chou, Joseph Lee, Yifei Yue, Jinyue Liu, Wan Kee Chock, Li Lin, et al. 2024. “BANKSY Unifies Cell Typing and Tissue Domain Segmentation for Scalable Spatial Omics Data Analysis.” *Nature Genetics* 56: 431–41. <https://doi.org/10.1038/s41588-024-01664-3>.

Traag, V. A., L. Waltman, and N. J. van Eck. 2019. “From Louvain to Leiden: Guaranteeing Well-Connected Communities.” *Scientific Reports* 9 (5233). <https://doi.org/10.1038/s41598-019-41695-z>.

Varrone, Marco, Daniele Tavernari, Albert Santamaria-Martínez, Logan A. Walsh, and Giovanni Ciriello. 2024. “CellCharter Reveals Spatial Cell Niches Associated with Tissue Remodeling and Cell Plasticity.” *Nature Genetics* 56: 74–84. <https://doi.org/10.1038/s41588-023-01588-4>.

Wang, Ziyi, Aoyun Geng, Hao Duan, Feifei Cui, Quan Zou, and Zilong Zhang. 2024. “A Comprehensive Review of Approaches for Spatial Domain Recognition of Spatial Transcriptomes.” *Briefings in Functional Genomics* 23: 702–12. <https://doi.org/10.1093/bfgp/elae040>.

Zhao, Edward, Matthew R. Stone, Xing Ren, Jamie Guenthoer, Kimberly S. Smythe, Thomas Pulliam, Stephen R. Williams, et al. 2021. “Spatial Transcriptomics at Subspot Resolution with BayesSpace.” *Nature Biotechnology* 39: 1375–84. <https://doi.org/10.1038/s41587-021-00935-2>.

Back to top
