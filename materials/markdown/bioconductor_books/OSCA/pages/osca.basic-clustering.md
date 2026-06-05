---
source: OSCA
title: "Basics of Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.basic/clustering.html
ingested_at: 2026-06-04T01:52:34+00:00
status: source_ingested
---

# [Basics of Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/3.23/OSCA.basic/)

# Chapter 5 Clustering

## 5.1 Overview

Clustering is an unsupervised learning procedure that is used to empirically define groups of cells with similar expression profiles.
Its primary purpose is to summarize complex scRNA-seq data into a digestible format for human interpretation.
This allows us to describe population heterogeneity in terms of discrete labels that are easily understood, rather than attempting to comprehend the high-dimensional manifold on which the cells truly reside.
After annotation based on marker genes, the clusters can be treated as proxies for more abstract biological concepts such as cell types or states.

At this point, it is helpful to realize that clustering, like a microscope, is simply a tool to explore the data.
We can zoom in and out by changing the resolution of the clustering parameters, and we can experiment with different clustering algorithms to obtain alternative perspectives of the data.
This iterative approach is entirely permissible given that data exploration constitutes the majority of the scRNA-seq data analysis workflow.
As such, questions about the “correctness” of the clusters or the “true” number of clusters are usually meaningless.
We can define as many clusters as we like, with whatever algorithm we like - each clustering will represent its own partitioning of the high-dimensional expression space, and is as “real” as any other clustering.

A more relevant question is “how well do the clusters approximate the cell types or states of interest?”
Unfortunately, this is difficult to answer given the context-dependent interpretation of the underlying biology.
Some analysts will be satisfied with resolution of the major cell types; other analysts may want resolution of subtypes; and others still may require resolution of different states (e.g., metabolic activity, stress) within those subtypes.
Moreover, two clusterings can be highly inconsistent yet both valid, simply partitioning the cells based on different aspects of biology.
Indeed, asking for an unqualified “best” clustering is akin to asking for the best magnification on a microscope without any context.

Regardless of the exact method used, clustering is a critical step for extracting biological insights from scRNA-seq data.
Here, we demonstrate the application of several commonly used methods with the 10X PBMC dataset.

View set-up code ([Workflow Chapter 3](http://bioconductor.org/books/3.23/OSCA.workflows/unfiltered-human-pbmcs-10x-genomics.html#unfiltered-human-pbmcs-10x-genomics))

```
#--- loading ---#
library(DropletTestFiles)
raw.path <- getTestFile("tenx-2.1.0-pbmc4k/1.0.0/raw.tar.gz")
out.path <- file.path(tempdir(), "pbmc4k")
untar(raw.path, exdir=out.path)

library(DropletUtils)
fname <- file.path(out.path, "raw_gene_bc_matrices/GRCh38")
sce.pbmc <- read10xCounts(fname, col.names=TRUE)

#--- gene-annotation ---#
library(scater)
rownames(sce.pbmc) <- uniquifyFeatureNames(
    rowData(sce.pbmc)$ID, rowData(sce.pbmc)$Symbol)

library(EnsDb.Hsapiens.v86)
location <- mapIds(EnsDb.Hsapiens.v86, keys=rowData(sce.pbmc)$ID, 
    column="SEQNAME", keytype="GENEID")

#--- cell-detection ---#
set.seed(100)
e.out <- emptyDrops(counts(sce.pbmc))
sce.pbmc <- sce.pbmc[,which(e.out$FDR <= 0.001)]

#--- quality-control ---#
stats <- perCellQCMetrics(sce.pbmc, subsets=list(Mito=which(location=="MT")))
high.mito <- isOutlier(stats$subsets_Mito_percent, type="higher")
sce.pbmc <- sce.pbmc[,!high.mito]

#--- normalization ---#
library(scran)
set.seed(1000)
clusters <- quickCluster(sce.pbmc)
sce.pbmc <- computeSumFactors(sce.pbmc, cluster=clusters)
sce.pbmc <- logNormCounts(sce.pbmc)

#--- variance-modelling ---#
set.seed(1001)
dec.pbmc <- modelGeneVarByPoisson(sce.pbmc)
top.pbmc <- getTopHVGs(dec.pbmc, prop=0.1)

#--- dimensionality-reduction ---#
set.seed(10000)
sce.pbmc <- denoisePCA(sce.pbmc, subset.row=top.pbmc, technical=dec.pbmc)

set.seed(100000)
sce.pbmc <- runTSNE(sce.pbmc, dimred="PCA")

set.seed(1000000)
sce.pbmc <- runUMAP(sce.pbmc, dimred="PCA")
```

```
sce.pbmc
```

```
## class: SingleCellExperiment 
## dim: 33694 4080 
## metadata(1): Samples
## assays(2): counts logcounts
## rownames(33694): RP11-34P13.3 FAM138A ... AC213203.1 FAM231B
## rowData names(2): ID Symbol
## colnames(4080): AAACCTGAGAAGGCCT-1 AAACCTGAGACAGACC-1 ...
##   TTTGTCAGTTAAGACA-1 TTTGTCATCCCAAGAT-1
## colData names(3): Sample Barcode sizeFactor
## reducedDimNames(3): PCA TSNE UMAP
## mainExpName: NULL
## altExpNames(0):
```

## 5.2 Graph-based clustering

### 5.2.1 Background

Popularized by its use in *[Seurat](https://CRAN.R-project.org/package=Seurat)*, graph-based clustering is a flexible and scalable technique for clustering large scRNA-seq datasets.
We first build a graph where each node is a cell that is connected to its nearest neighbors in the high-dimensional space.
Edges are weighted based on the similarity between the cells involved, with higher weight given to cells that are more closely related.
We then apply algorithms to identify “communities” of cells that are more connected to cells in the same community than they are to cells of different communities.
Each community represents a cluster that we can use for downstream interpretation.

The major advantage of graph-based clustering lies in its scalability.
It only requires a \(k\)-nearest neighbor search that can be done in log-linear time on average, in contrast to hierachical clustering methods with runtimes that are quadratic with respect to the number of cells.
Graph construction avoids making strong assumptions about the shape of the clusters or the distribution of cells within each cluster, compared to other methods like \(k\)-means (that favor spherical clusters) or Gaussian mixture models (that require normality).
From a practical perspective, each cell is forcibly connected to a minimum number of neighboring cells, which reduces the risk of generating many uninformative clusters consisting of one or two outlier cells.

The main drawback of graph-based methods is that, after graph construction, no information is retained about relationships beyond the neighboring cells[1](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fn1).
This has some practical consequences in datasets that exhibit differences in cell density, as more steps through the graph are required to move the same distance through a region of higher cell density.
From the perspective of community detection algorithms, this effect “inflates” the high-density regions such that any internal substructure or noise is more likely to cause formation of subclusters.
The resolution of clustering thus becomes dependent on the density of cells, which can occasionally be misleading if it overstates the heterogeneity in the data.

### 5.2.2 Implementation

To demonstrate, we use the `clusterCells()` function in *[scran](https://bioconductor.org/packages/3.23/scran)* on PBMC dataset.
All calculations are performed using the top PCs to take advantage of data compression and denoising.
This function returns a vector containing cluster assignments for each cell in our `SingleCellExperiment` object.

```
library(scran)
nn.clusters <- clusterCells(sce.pbmc, use.dimred="PCA")
table(nn.clusters)
```

```
## nn.clusters
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19 
## 249 559 367  46 173 914 450 285 266 111 157 130 137  46  41  85  19  16  29
```

We assign the cluster assignments back into our `SingleCellExperiment` object as a factor in the column metadata.
This allows us to conveniently visualize the distribution of clusters in a \(t\)-SNE plot (Figure [5.1](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:tsne-clust-graph)).

```
library(scater)
colLabels(sce.pbmc) <- nn.clusters
plotReducedDim(sce.pbmc, "TSNE", colour_by="label")
```

![$t$-SNE plot of the 10X PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from graph-based clustering.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/tsne-clust-graph-1.png)

Figure 5.1: \(t\)-SNE plot of the 10X PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from graph-based clustering.

By default, `clusterCells()` uses the 10 nearest neighbors of each cell to construct a shared nearest neighbor graph.
Two cells are connected by an edge if any of their nearest neighbors are shared,
with the edge weight defined from the highest average rank of the shared neighbors (Xu and Su [2015](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#ref-xu2015identification)).
The Walktrap method from the *[igraph](https://CRAN.R-project.org/package=igraph)* package is then used to identify communities.

If we wanted to explicitly specify all of these parameters, we would use the more verbose call below.
This uses a `SNNGraphParam` object from the *[bluster](https://bioconductor.org/packages/3.23/bluster)* package to instruct `clusterCells()` to detect communities from a shared nearest-neighbor graph with the specified parameters.
The appeal of this interface is that it allows us to easily switch to a different clustering algorithm by simply changing the `BLUSPARAM=` argument,
as we will demonstrate later in the chapter.

```
library(bluster)
nn.clusters2 <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=SNNGraphParam(k=10, type="rank", cluster.fun="walktrap"))
table(nn.clusters2)
```

```
## nn.clusters2
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19 
## 249 559 367  46 173 914 450 285 266 111 157 130 137  46  41  85  19  16  29
```

We can also obtain the graph itself by specifying `full=TRUE` in the `clusterCells()` call.
Doing so will return all intermediate structures that are used during clustering, including a graph object from the *[igraph](https://CRAN.R-project.org/package=igraph)* package.
This graph can be visualized using a force-directed layout (Figure [5.2](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:pbmc-force)), closely related to \(t\)-SNE and UMAP,
though which of these is the most aesthetically pleasing is left to the eye of the beholder.

```
nn.clust.info <- clusterCells(sce.pbmc, use.dimred="PCA", full=TRUE)
nn.clust.info$objects$graph
```

```
## IGRAPH 26ae05b U-W- 4080 128969 -- 
## + attr: weight (e/n)
## + edges from 26ae05b:
##  [1]  4--12 11--15  4--17 12--18 17--18  8--20  8--23  2--25 18--27 17--27
## [11] 24--29 11--30 15--30 10--31 25--33 19--37  9--38 23--41 12--43  4--43
## [21] 21--45 33--47 22--48 18--49 12--49 43--49 48--51 22--51 23--52 11--54
## [31] 15--54 30--54 47--58 21--58 50--59 41--60 52--60 23--60 22--61 48--61
## [41] 51--61 26--62 22--64 61--64 48--64 51--64  1--65 14--66 16--68 55--69
## [51] 59--70 50--70  9--70 40--71  2--71 55--72 63--73 63--76 11--77 15--77
## [61] 30--77 23--79 41--79  8--79 28--81  6--83 67--85 11--86 30--86 15--86
## [71] 77--86 54--86 14--88 51--90 61--90 48--90 22--90 64--90 44--92 38--92
## + ... omitted several edges
```

```
set.seed(11000)
reducedDim(sce.pbmc, "force") <- igraph::layout_with_fr(nn.clust.info$objects$graph)
plotReducedDim(sce.pbmc, colour_by="label", dimred="force")
```

![Force-directed layout for the shared nearest-neighbor graph of the PBMC dataset. Each point represents a cell and is coloured according to its assigned cluster identity.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/pbmc-force-1.png)

Figure 5.2: Force-directed layout for the shared nearest-neighbor graph of the PBMC dataset. Each point represents a cell and is coloured according to its assigned cluster identity.

In addition, the graph can be used to generate detailed diagnostics on the behavior of the graph-based clustering ([Advanced Section 5.2.5](http://bioconductor.org/books/3.23/OSCA.advanced/clustering-redux.html#using-graph-modularity)).

### 5.2.3 Adjusting the parameters

A graph-based clustering method has several key parameters:

* How many neighbors are considered when constructing the graph.
* What scheme is used to weight the edges.
* Which community detection algorithm is used to define the clusters.

One of the most important parameters is `k`, the number of nearest neighbors used to construct the graph.
This controls the resolution of the clustering where higher `k` yields a more inter-connected graph and broader clusters.
Users can exploit this by experimenting with different values of `k` to obtain a satisfactory resolution.

```
# More resolved.
clust.5 <- clusterCells(sce.pbmc, use.dimred="PCA", BLUSPARAM=NNGraphParam(k=5))
table(clust.5)
```

```
## clust.5
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20 
## 540 290 173  80  89 307 846 408 541 273 183  19  20  69  26  64  29  38  18  16 
##  21  22  23 
##  28  15   8
```

```
# Less resolved.
clust.50 <- clusterCells(sce.pbmc, use.dimred="PCA", BLUSPARAM=NNGraphParam(k=50))
table(clust.50)
```

```
## clust.50
##   1   2   3   4   5   6   7   8   9 
## 831 323 186 557 536 494 958 149  46
```

Further tweaking can be performed by changing the edge weighting scheme during graph construction.
Setting `type="number"` will weight edges based on the number of nearest neighbors that are shared between two cells.
Similarly, `type="jaccard"` will weight edges according to the Jaccard index of the two sets of neighbors.
We can also disable weighting altogether by using a simple \(k\)-nearest neighbor graph, which is occasionally useful for downstream graph operations that do not support weights.

```
clust.num <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=NNGraphParam(type="number"))
table(clust.num)
```

```
## clust.num
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20 
## 559 354 843 484  46  85 173 354 312 155  37  46 113 153  83 146  73  19  29  16
```

```
clust.jaccard <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=NNGraphParam(type="jaccard"))
table(clust.jaccard)
```

```
## clust.jaccard
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20 
## 559 837  81  46 354 173 452 356 325  46  31 176 112 157  83  99 129  19  29  16
```

```
clust.none <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=KNNGraphParam())
table(clust.none)
```

```
## clust.none
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20 
## 372 408  46 173 472 283 124 727 152 148 152 279  37 150 106  84  46 207  20  50 
##  21  22 
##  28  16
```

The community detection can be performed by using any of the algorithms provided by *[igraph](https://CRAN.R-project.org/package=igraph)*.
We have already mentioned the Walktrap approach, but many others are available to choose from:

```
clust.walktrap <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=NNGraphParam(cluster.fun="walktrap"))

clust.louvain <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=NNGraphParam(cluster.fun="louvain"))

clust.infomap <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=NNGraphParam(cluster.fun="infomap"))

clust.fast <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=NNGraphParam(cluster.fun="fast_greedy"))

clust.labprop <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=NNGraphParam(cluster.fun="label_prop"))

clust.eigen <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=NNGraphParam(cluster.fun="leading_eigen"))
```

It is straightforward to compare two clustering strategies to see how they differ ([Advanced Section 5.3](http://bioconductor.org/books/3.23/OSCA.advanced/clustering-redux.html#comparing-different-clusterings)).
For example, Figure [5.3](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:walktrap-v-others) suggests that Infomap yields finer clusters than Walktrap while fast-greedy yields coarser clusters.

```
library(pheatmap)

# Using a large pseudo-count for a smoother color transition
# between 0 and 1 cell in each 'tab'.
tab <- table(paste("Infomap", clust.infomap), 
    paste("Walktrap", clust.walktrap))
ivw <- pheatmap(log10(tab+10), main="Infomap vs Walktrap",
    color=viridis::viridis(100), silent=TRUE)

tab <- table(paste("Fast", clust.fast), 
    paste("Walktrap", clust.walktrap))
fvw <- pheatmap(log10(tab+10), main="Fast-greedy vs Walktrap",
    color=viridis::viridis(100), silent=TRUE)

gridExtra::grid.arrange(ivw[[4]], fvw[[4]])
```

![Number of cells assigned to combinations of cluster labels with different community detection algorithms in the PBMC dataset. Each entry of each heatmap represents a pair of labels, coloured proportionally to the log-number of cells with those labels.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/walktrap-v-others-1.png)

Figure 5.3: Number of cells assigned to combinations of cluster labels with different community detection algorithms in the PBMC dataset. Each entry of each heatmap represents a pair of labels, coloured proportionally to the log-number of cells with those labels.

Pipelines involving *[scran](https://bioconductor.org/packages/3.23/scran)* default to rank-based weights followed by Walktrap clustering.
In contrast, *[Seurat](https://CRAN.R-project.org/package=Seurat)* uses Jaccard-based weights followed by Louvain clustering.
Both of these strategies work well, and it is likely that the same could be said for many other combinations of weighting schemes and community detection algorithms.

## 5.3 Vector quantization with \(k\)-means

### 5.3.1 Background

Vector quantization partitions observations into groups where each group is associated with a representative point, i.e., vector in the coordinate space.
This is a type of clustering that primarily aims to compress data by replacing many points with a single representative.
The representatives can then be treated as “samples” for further analysis, reducing the number of samples and computational work in later steps like, e.g., trajectory reconstruction (Ji and Ji [2016](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#ref-ji2016tscan)).
This approach will also eliminate differences in cell density across the expression space, ensuring that the most abundant cell type does not dominate downstream results.

\(k\)-means clustering is a classic vector quantization technique that divides cells into \(k\) clusters.
Each cell is assigned to the cluster with the closest centroid, which is done by minimizing the within-cluster sum of squares using a random starting configuration for the \(k\) centroids.
We usually set \(k\) to a large value such as the square root of the number of cells to obtain fine-grained clusters.
These are not meant to be interpreted directly, but rather, the centroids are used in downstream steps for faster computation.
The main advantage of this approach lies in its speed, given the simplicity and ease of implementation of the algorithm.

### 5.3.2 Implementation

We supply a `KmeansParam` object in `clusterCells()` to perform \(k\)-means clustering with the specified number of clusters in `centers=`.
We again use our top PCs after setting the random seed to ensure that the results are reproducible.
In general, the \(k\)-means clusters correspond to the visual clusters on the \(t\)-SNE plot in Figure [5.4](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:tsne-clust-kmeans), though there are some divergences that are not observed in, say, Figure [5.1](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:tsne-clust-graph).
(This is at least partially due to the fact that \(t\)-SNE is itself graph-based and so will naturally agree more with a graph-based clustering strategy.)

```
set.seed(100)
clust.kmeans <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=KmeansParam(centers=10))
table(clust.kmeans)
```

```
## clust.kmeans
##   1   2   3   4   5   6   7   8   9  10 
## 257  47 453 773  51 499 909 339 200 552
```

```
colLabels(sce.pbmc) <- clust.kmeans
plotReducedDim(sce.pbmc, "TSNE", colour_by="label")
```

![$t$-SNE plot of the 10X PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from $k$-means clustering.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/tsne-clust-kmeans-1.png)

Figure 5.4: \(t\)-SNE plot of the 10X PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from \(k\)-means clustering.

If we were so inclined, we could obtain a “reasonable” choice of \(k\) by computing the gap statistic using methods from the *[cluster](https://CRAN.R-project.org/package=cluster)* package.
A more practical use of \(k\)-means is to deliberately set \(k\) to a large value to achieve overclustering.
This will forcibly partition cells inside broad clusters that do not have well-defined internal structure.
For example, we might be interested in the change in expression from one “side” of a cluster to the other, but the lack of any clear separation within the cluster makes it difficult to separate with graph-based methods, even at the highest resolution.
\(k\)-means has no such problems and will readily split these broad clusters for greater resolution.

```
set.seed(100)
clust.kmeans2 <- clusterCells(sce.pbmc, use.dimred="PCA", 
    BLUSPARAM=KmeansParam(centers=20))
table(clust.kmeans2)
```

```
## clust.kmeans2
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20 
## 180  91  65 436 303 161 434 137 220  48 252 305 145 212 178 139 416  47 140 171
```

```
colLabels(sce.pbmc) <- clust.kmeans2
plotTSNE(sce.pbmc, colour_by="label", text_by="label")
```

![$t$-SNE plot of the 10X PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from $k$-means clustering with $k=20$.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/tsne-clust-kmeans-best-1.png)

Figure 5.5: \(t\)-SNE plot of the 10X PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from \(k\)-means clustering with \(k=20\).

For larger datasets, we can use a variant of this approach named mini-batch \(k\)-means from the *[mbkmeans](https://bioconductor.org/packages/3.23/mbkmeans)* package.
At each iteration, we only update the cluster assignments and centroid positions for a small subset of the observations.
This reduces memory usage and computational time - especially when not all of the observations are informative for convergence - and supports parallelization via *[BiocParallel](https://bioconductor.org/packages/3.23/BiocParallel)*.
Using this variant is as simple as switching to a `MbkmeansParam()` object in our `clusterCells()` call:

```
set.seed(100)
clust.mbkmeans <- clusterCells(sce.pbmc, use.dimred="PCA",
    BLUSPARAM=MbkmeansParam(centers=10))
table(clust.mbkmeans)
```

```
## clust.mbkmeans
##    1    2    3    4    5    6    7    8    9   10 
##  552  264  202   47  281 1057   51  530  569  527
```

### 5.3.3 In two-step procedures

By itself, \(k\)-means suffers from several shortcomings that reduce its appeal for obtaining interpretable clusters:

* It implicitly favors spherical clusters of equal radius.
  This can lead to unintuitive partitionings on real datasets that contain groupings with irregular sizes and shapes.
* The number of clusters \(k\) must be specified beforehand and represents a hard cap on the resolution of the clustering..
  For example, setting \(k\) to be below the number of cell types will always lead to co-clustering of two cell types, regardless of how well separated they are.
  In contrast, other methods like graph-based clustering will respect strong separation even if the relevant resolution parameter is set to a low value.
* It is dependent on the randomly chosen initial coordinates.
  This requires multiple runs to verify that the clustering is stable.

However, these concerns are less relevant when \(k\)-means is being used for vector quantization.
In this application, \(k\)-means is used as a prelude to more sophisticated and interpretable - but computationally expensive - clustering algorithms.
The `clusterCells()` function supports a “two-step” mode where \(k\)-means is initially used to obtain representative centroids that are subjected to graph-based clustering.
Each cell is then placed in the same graph-based cluster that its \(k\)-means centroid was assigned to (Figure [5.6](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:tsne-kmeans-graph-pbmc)).

```
# Setting the seed due to the randomness of k-means.
set.seed(0101010)
kgraph.clusters <- clusterCells(sce.pbmc, use.dimred="PCA",
    BLUSPARAM=TwoStepParam(
        first=KmeansParam(centers=1000),
        second=NNGraphParam(k=5)
    )
)
table(kgraph.clusters)
```

```
## kgraph.clusters
##   1   2   3   4   5   6   7   8   9  10  11  12 
## 552 195 587 764 202 559 815 162  64  88  46  46
```

```
plotTSNE(sce.pbmc, colour_by=I(kgraph.clusters))
```

![$t$-SNE plot of the PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from combined $k$-means/graph-based clustering.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/tsne-kmeans-graph-pbmc-1.png)

Figure 5.6: \(t\)-SNE plot of the PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from combined \(k\)-means/graph-based clustering.

The obvious benefit of this approach over direct graph-based clustering is the speed improvement.
We avoid the need to identifying nearest neighbors for each cell and the construction of a large intermediate graph,
while benefiting from the relative interpretability of graph-based clusters compared to those from \(k\)-means.
This approach also mitigates the “inflation” effect discussed in Section [5.2](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#clustering-graph).
Each centroid serves as a representative of a region of space that is roughly similar in volume,
ameliorating differences in cell density that can cause (potentially undesirable) differences in resolution.

The choice of the number of \(k\)-means clusters determines the trade-off between speed and fidelity.
Larger values provide a more faithful representation of the underlying distribution of cells,
at the cost of requiring more computational work by the second-step clustering procedure.
Note that the second step operates on the centroids, so increasing `clusters=` may have further implications if the second-stage procedure is sensitive to the total number of input observations.
For example, increasing the number of centroids would require an concomitant increase in `k=` (the number of neighbors in graph construction) to maintain the same level of resolution in the final output.

## 5.4 Hierarchical clustering

### 5.4.1 Background

Hierarchical clustering is an old technique that arranges samples into a hierarchy based on their relative similarity to each other.
Most implementations do so by joining the most similar samples into a new cluster, then joining similar clusters into larger clusters, and so on, until all samples belong to a single cluster.
This process yields obtain a dendrogram that defines clusters with progressively increasing granularity.
Variants of hierarchical clustering methods primarily differ in how they choose to perform the agglomerations.
For example, complete linkage aims to merge clusters with the smallest maximum distance between their elements, while Ward’s method aims to minimize the increase in within-cluster variance.

In the context of scRNA-seq, the main advantage of hierarchical clustering lies in the production of the dendrogram.
This is a rich summary that quantitatively captures the relationships between subpopulations at various resolutions.
Cutting the dendrogram at high resolution is also guaranteed to yield clusters that are nested within those obtained at a low-resolution cut;
this can be helpful for interpretation, as discussed in Section [5.5](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#subclustering).
The dendrogram is also a natural representation of the data in situations where cells have descended from a relatively recent common ancestor.

In practice, hierarchical clustering is too slow to be used for anything but the smallest scRNA-seq datasets.
Most implementations require a cell-cell distance matrix that is prohibitively expensive to compute for a large number of cells.
Greedy agglomeration is also likely to result in a quantitatively suboptimal partitioning (as defined by the agglomeration measure) at higher levels of the dendrogram when the number of cells and merge steps is high.
Nonetheless, we will still demonstrate the application of hierarchical clustering here as it can be useful when combined with vector quantization techniques like \(k\)-means.

### 5.4.2 Implementation

The PBMC dataset is too large to use directly in hierarchical clustering, requiring a two-step approach to compress the observations instead (Section [5.3.3](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#in-two-step-procedures)).
For the sake of simplicity, we will demonstrate on the smaller 416B dataset instead.

View set-up code ([Workflow Chapter 1](http://bioconductor.org/books/3.23/OSCA.workflows/lun-416b-cell-line-smart-seq2.html#lun-416b-cell-line-smart-seq2))

```
#--- loading ---#
library(scRNAseq)
sce.416b <- LunSpikeInData(which="416b") 
sce.416b$block <- factor(sce.416b$block)

#--- gene-annotation ---#
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

#--- quality-control ---#
mito <- which(rowData(sce.416b)$SEQNAME=="MT")
stats <- perCellQCMetrics(sce.416b, subsets=list(Mt=mito))
qc <- quickPerCellQC(stats, percent_subsets=c("subsets_Mt_percent",
    "altexps_ERCC_percent"), batch=sce.416b$block)
sce.416b <- sce.416b[,!qc$discard]

#--- normalization ---#
library(scran)
sce.416b <- computeSumFactors(sce.416b)
sce.416b <- logNormCounts(sce.416b)

#--- variance-modelling ---#
dec.416b <- modelGeneVarWithSpikes(sce.416b, "ERCC", block=sce.416b$block)
chosen.hvgs <- getTopHVGs(dec.416b, prop=0.1)

#--- batch-correction ---#
library(limma)
assay(sce.416b, "corrected") <- removeBatchEffect(logcounts(sce.416b), 
    design=model.matrix(~sce.416b$phenotype), batch=sce.416b$block)

#--- dimensionality-reduction ---#
sce.416b <- runPCA(sce.416b, ncomponents=10, subset_row=chosen.hvgs,
    exprs_values="corrected", BSPARAM=BiocSingular::ExactParam())

set.seed(1010)
sce.416b <- runTSNE(sce.416b, dimred="PCA", perplexity=10)
```

```
sce.416b
```

```
## class: SingleCellExperiment 
## dim: 46604 185 
## metadata(0):
## assays(3): counts logcounts corrected
## rownames(46604): 4933401J01Rik Gm26206 ... CAAA01147332.1
##   CBFB-MYH11-mcherry
## rowData names(4): Length ENSEMBL SYMBOL SEQNAME
## colnames(185): SLX-9555.N701_S502.C89V9ANXX.s_1.r_1
##   SLX-9555.N701_S503.C89V9ANXX.s_1.r_1 ...
##   SLX-11312.N712_S507.H5H5YBBXX.s_8.r_1
##   SLX-11312.N712_S517.H5H5YBBXX.s_8.r_1
## colData names(9): cell line cell type ... block sizeFactor
## reducedDimNames(2): PCA TSNE
## mainExpName: endogenous
## altExpNames(2): ERCC SIRV
```

We use a `HclustParam` object to instruct `clusterCells()` to perform hierarchical clustering on the top PCs.
Specifically, it computes a cell-cell distance matrix using the top PCs and then applies Ward’s minimum variance method to obtain a dendrogram.
When visualized in Figure [5.7](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:dend-416b), we see a clear split in the population caused by oncogene induction.
While both Ward’s method and the default complete linkage yield compact clusters, we prefer the former it is less affected by differences in variance between clusters.

```
hclust.416b <- clusterCells(sce.416b, use.dimred="PCA",
    BLUSPARAM=HclustParam(method="ward.D2"), full=TRUE)
tree.416b <- hclust.416b$objects$hclust

# Making a prettier dendrogram.
library(dendextend)
tree.416b$labels <- seq_along(tree.416b$labels)
dend <- as.dendrogram(tree.416b, hang=0.1)

combined.fac <- paste0(sce.416b$block, ".", 
    sub(" .*", "", sce.416b$phenotype))
labels_colors(dend) <- c(
    "20160113.wild"="blue",
    "20160113.induced"="red",
    "20160325.wild"="dodgerblue",
    "20160325.induced"="salmon"
)[combined.fac][order.dendrogram(dend)]

plot(dend)
```

![Hierarchy of cells in the 416B data set after hierarchical clustering, where each leaf node is a cell that is coloured according to its oncogene induction status (red is induced, blue is control) and plate of origin (light or dark).](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/dend-416b-1.png)

Figure 5.7: Hierarchy of cells in the 416B data set after hierarchical clustering, where each leaf node is a cell that is coloured according to its oncogene induction status (red is induced, blue is control) and plate of origin (light or dark).

To obtain explicit clusters, we “cut” the tree by removing internal branches such that every subtree represents a distinct cluster.
This is most simply done by removing internal branches above a certain height of the tree, as performed by the `cutree()` function.
A more sophisticated variant of this approach is implemented in the *[dynamicTreeCut](https://CRAN.R-project.org/package=dynamicTreeCut)* package,
which uses the shape of the branches to obtain a better partitioning for complex dendrograms (Figure [5.8](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:dend-cluster)).
We enable this option by setting `cut.dynamic=TRUE`, with additional tweaking of the `deepSplit=` parameter to control the resolution of the resulting clusters.

```
hclust.dyn <- clusterCells(sce.416b, use.dimred="PCA",
    BLUSPARAM=HclustParam(method="ward.D2", cut.dynamic=TRUE,
        cut.params=list(minClusterSize=10, deepSplit=1)))
table(hclust.dyn)
```

```
## hclust.dyn
##  1  2  3  4 
## 78 69 24 14
```

```
labels_colors(dend) <- as.integer(hclust.dyn)[order.dendrogram(dend)]
plot(dend)
```

![Hierarchy of cells in the 416B data set after hierarchical clustering, where each leaf node is a cell that is coloured according to its assigned cluster identity from a dynamic tree cut.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/dend-cluster-1.png)

Figure 5.8: Hierarchy of cells in the 416B data set after hierarchical clustering, where each leaf node is a cell that is coloured according to its assigned cluster identity from a dynamic tree cut.

This generally corresponds well to the grouping of cells on a \(t\)-SNE plot (Figure [5.9](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:tsne-416b)).
Cluster 2 is split across two visual clusters in the plot but we attribute this to a distortion introduced by \(t\)-SNE,
given that this cluster actually has the highest average silhouette width ([Advanced Section 5.2.2](http://bioconductor.org/books/3.23/OSCA.advanced/clustering-redux.html#silhouette-width)).

```
colLabels(sce.416b) <- factor(hclust.dyn)
plotReducedDim(sce.416b, "TSNE", colour_by="label")
```

![$t$-SNE plot of the 416B dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from hierarchical clustering.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/tsne-416b-1.png)

Figure 5.9: \(t\)-SNE plot of the 416B dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from hierarchical clustering.

### 5.4.3 In two-step procedures, again

Returning to our PBMC example, we can use a two-step approach to perform hierarchical clustering on the representative centroids (Figure [5.10](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:tsne-kmeans-hclust-pbmc)).
This avoids the construction of a distance matrix across all cells for faster computation.

```
# Setting the seed due to the randomness of k-means.
set.seed(1111)
khclust.info <- clusterCells(sce.pbmc, use.dimred="PCA",
    BLUSPARAM=TwoStepParam(
        first=KmeansParam(centers=1000),
        second=HclustParam(method="ward.D2", cut.dynamic=TRUE,
            cut.param=list(deepSplit=3)) # for higher resolution.
    ),
    full=TRUE
)
table(khclust.info$clusters)
```

```
## 
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17 
## 492 431 336 361 317 299 245 246 215 183 170 159 153 112 121 150  90
```

```
plotTSNE(sce.pbmc, colour_by=I(khclust.info$clusters), 
    text_by=I(khclust.info$clusters))
```

![$t$-SNE plot of the PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from combined $k$-means/hierarchical clustering.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/tsne-kmeans-hclust-pbmc-1.png)

Figure 5.10: \(t\)-SNE plot of the PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from combined \(k\)-means/hierarchical clustering.

With a little bit of work, we can also examine the dendrogram constructed on the centroids (Figure [5.11](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:dendroid-pbmc)).
This provides a more quantitative visualization of the relative similarities between the different subpopulations.

```
k.stats <- khclust.info$objects$first
tree.pbmc <- khclust.info$objects$second$hclust

m <- match(as.integer(tree.pbmc$labels), k.stats$cluster)
final.clusters <- khclust.info$clusters[m]

# TODO: expose scater color palette for easier re-use,
# given that the default colors start getting recycled.
dend <- as.dendrogram(tree.pbmc, hang=0.1)
labels_colors(dend) <- as.integer(final.clusters)[order.dendrogram(dend)]

plot(dend)
```

![Dendrogram of the $k$-mean centroids after hierarchical clustering in the PBMC dataset. Each leaf node represents a representative cluster of cells generated by $k$-mean clustering.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/dendroid-pbmc-1.png)

Figure 5.11: Dendrogram of the \(k\)-mean centroids after hierarchical clustering in the PBMC dataset. Each leaf node represents a representative cluster of cells generated by \(k\)-mean clustering.

As an aside, the same approach can be used to speed up any clustering method based on a distance matrix.
For example, we could subject our \(k\)-means centroids to clustering by affinity propagation (Frey and Dueck [2007](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#ref-frey2007clustering)).
In this procedure, each sample (i.e., centroid) chooses itself or another sample as its “exemplar”,
with the suitability of the choice dependent on the distance between the samples, other potential exemplars for each sample, and the other samples with the same chosen exemplar.
Iterative updates of these choices yields a set of clusters where each cluster is defined from the samples assigned to the same exemplar (Figure [5.12](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:tsne-kmeans-affinity-pbmc))
Unlike hierarchical clustering, this does not provide a dendrogram, but it also avoids the extra complication of a tree cut -
resolution is primarily controlled via the `q=` parameter, which defines the strength with which a sample considers itself as an exemplar and thus forms its own cluster.

```
# Setting the seed due to the randomness of k-means.
set.seed(1111)
kaclust.info <- clusterCells(sce.pbmc, use.dimred="PCA",
    BLUSPARAM=TwoStepParam(
        first=KmeansParam(centers=1000),
        second=AffinityParam(q=0.1) # larger q => more clusters
    ),
    full=TRUE
)
table(kaclust.info$clusters)
```

```
## 
##   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17 
## 100 117 239 376 128  15 315 852 188 550  31  30 177  42 185 395 340
```

```
plotTSNE(sce.pbmc, colour_by=I(kaclust.info$clusters), 
    text_by=I(kaclust.info$clusters))
```

![$t$-SNE plot of the PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from combined $k$-means/affinity propagation clustering.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/tsne-kmeans-affinity-pbmc-1.png)

Figure 5.12: \(t\)-SNE plot of the PBMC dataset, where each point represents a cell and is coloured according to the identity of the assigned cluster from combined \(k\)-means/affinity propagation clustering.

## 5.5 Subclustering

Another simple approach to improving resolution is to repeat the feature selection and clustering *within* a single cluster.
This aims to select HVGs and PCs that are more relevant to internal structure, improving resolution by avoiding noise from unnecessary features.
Subsetting also encourages clustering methods to separate cells according to more modest heterogeneity in the absence of distinct subpopulations.
We demonstrate with a cluster of putative memory T cells from the PBMC dataset, identified according to several markers (Figure [5.13](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:ccr7-dist-memory)).

```
clust.full <- clusterCells(sce.pbmc, use.dimred="PCA")
plotExpression(sce.pbmc, features=c("CD3E", "CCR7", "CD69", "CD44"),
    x=I(clust.full), colour_by=I(clust.full))
```

![Distribution of log-normalized expression values for several T cell markers within each cluster in the 10X PBMC dataset. Each cluster is color-coded for convenience.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/ccr7-dist-memory-1.png)

Figure 5.13: Distribution of log-normalized expression values for several T cell markers within each cluster in the 10X PBMC dataset. Each cluster is color-coded for convenience.

```
# Repeating modelling and PCA on the subset.
memory <- 6L
sce.memory <- sce.pbmc[,clust.full==memory]
dec.memory <- modelGeneVar(sce.memory)
sce.memory <- denoisePCA(sce.memory, technical=dec.memory,
    subset.row=getTopHVGs(dec.memory, n=5000))
```

We apply graph-based clustering within this memory subset to obtain *CD4*+ and *CD8*+ subclusters (Figure [5.14](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fig:cd48-memory-expression)).
Admittedly, the expression of *CD4* is so low that the change is rather modest, but the interpretation is clear enough.

```
g.memory <- buildSNNGraph(sce.memory, use.dimred="PCA")
clust.memory <- igraph::cluster_walktrap(g.memory)$membership
plotExpression(sce.memory, features=c("CD8A", "CD4"),
    x=I(factor(clust.memory)))
```

![Distribution of _CD4_ and _CD8A_ log-normalized expression values within each cluster in the memory T cell subset of the 10X PBMC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-clustering/cd48-memory-expression-1.png)

Figure 5.14: Distribution of *CD4* and *CD8A* log-normalized expression values within each cluster in the memory T cell subset of the 10X PBMC dataset.

For subclustering analyses, it is helpful to define a customized function that calls our desired algorithms to obtain a clustering from a given `SingleCellExperiment`.
This function can then be applied multiple times on different subsets without having to repeatedly copy and modify the code for each subset.
For example, `quickSubCluster()` loops over all subsets and executes this user-specified function to generate a list of `SingleCellExperiment` objects containing the subclustering results.
(Of course, the downside is that this assumes that a similar analysis is appropriate for each subset.
If different subsets require extensive reparametrization, copying the code may actually be more straightforward.)

```
set.seed(1000010)
subcluster.out <- quickSubCluster(sce.pbmc, groups=clust.full,
    prepFUN=function(x) { # Preparing the subsetted SCE for clustering.
        dec <- modelGeneVar(x)
        input <- denoisePCA(x, technical=dec,
            subset.row=getTopHVGs(dec, prop=0.1),
            BSPARAM=BiocSingular::IrlbaParam())
    },
    clusterFUN=function(x) { # Performing the subclustering in the subset.
        g <- buildSNNGraph(x, use.dimred="PCA", k=20)
        igraph::cluster_walktrap(g)$membership
    }
)

# One SingleCellExperiment object per parent cluster:
names(subcluster.out)
```

```
##  [1] "1"  "2"  "3"  "4"  "5"  "6"  "7"  "8"  "9"  "10" "11" "12" "13" "14" "15"
## [16] "16" "17" "18" "19"
```

```
# Looking at the subclustering for one example:
table(subcluster.out[[1]]$subcluster)
```

```
## 
## 1.1 1.2 1.3 1.4 
## 106  61  35  47
```

Subclustering is a general and conceptually straightforward procedure for increasing resolution.
It can also simplify the interpretation of the subclusters, which only need to be considered in the context of the parent cluster’s identity - for example, we did not have to re-identify the cells in cluster 6 as T cells.
However, this is a double-edged sword as it is difficult for practitioners to consider the uncertainty of identification for parent clusters when working with deep nesting.
If cell types or states span cluster boundaries, conditioning on the putative cell type identity of the parent cluster can encourage the construction of a “house of cards” of cell type assignments, e.g., where a subcluster of one parent cluster is actually contamination from a cell type in a separate parent cluster.

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
 [1] apcluster_1.4.14            dendextend_1.19.1          
 [3] pheatmap_1.0.13             bluster_1.22.0             
 [5] scater_1.40.0               ggplot2_4.0.3              
 [7] scran_1.40.0                scuttle_1.22.0             
 [9] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
[11] Biobase_2.72.0              GenomicRanges_1.64.0       
[13] Seqinfo_1.2.0               IRanges_2.46.0             
[15] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[17] generics_0.1.4              MatrixGenerics_1.24.0      
[19] matrixStats_1.5.0           BiocStyle_2.40.0           
[21] rebook_1.22.0              

loaded via a namespace (and not attached):
 [1] gridExtra_2.3         CodeDepends_0.6.7     rlang_1.2.0          
 [4] magrittr_2.0.5        otel_0.2.0            compiler_4.6.0       
 [7] dir.expiry_1.20.0     vctrs_0.7.3           pkgconfig_2.0.3      
[10] fastmap_1.2.0         XVector_0.52.0        labeling_0.4.3       
[13] rmarkdown_2.31        graph_1.90.0          ggbeeswarm_0.7.3     
[16] xfun_0.57             cachem_1.1.0          beachmat_2.28.0      
[19] jsonlite_2.0.0        gmp_0.7-5.1           DelayedArray_0.38.0  
[22] BiocParallel_1.46.0   irlba_2.3.7           parallel_4.6.0       
[25] cluster_2.1.8.2       R6_2.6.1              bslib_0.10.0         
[28] RColorBrewer_1.1-3    limma_3.68.0          benchmarkme_1.0.8    
[31] ClusterR_1.3.6        jquerylib_0.1.4       iterators_1.0.14     
[34] Rcpp_1.1.1-1.1        bookdown_0.46         knitr_1.51           
[37] Matrix_1.7-5          igraph_2.3.0          tidyselect_1.2.1     
[40] dichromat_2.0-0.1     abind_1.4-8           yaml_2.3.12          
[43] viridis_0.6.5         doParallel_1.0.17     codetools_0.2-20     
[46] mbkmeans_1.28.0       lattice_0.22-9        tibble_3.3.1         
[49] withr_3.0.2           S7_0.2.2              benchmarkmeData_2.0.0
[52] evaluate_1.0.5        pillar_1.11.1         BiocManager_1.30.27  
[55] filelock_1.0.3        foreach_1.5.2         scales_1.4.0         
[58] glue_1.8.1            metapod_1.20.0        tools_4.6.0          
[61] BiocNeighbors_2.6.0   ScaledMatrix_1.20.0   locfit_1.5-9.12      
[64] XML_3.99-0.23         cowplot_1.2.0         grid_4.6.0           
[67] edgeR_4.10.0          beeswarm_0.4.0        BiocSingular_1.28.0  
[70] vipor_0.4.7           cli_3.6.6             rsvd_1.0.5           
[73] rappdirs_0.3.4        S4Arrays_1.12.0       viridisLite_0.4.3    
[76] dplyr_1.2.1           gtable_0.3.6          dynamicTreeCut_1.63-1
[79] sass_0.4.10           digest_0.6.39         SparseArray_1.12.0   
[82] ggrepel_0.9.8         dqrng_0.4.1           farver_2.1.2         
[85] htmltools_0.5.9       lifecycle_1.0.5       httr_1.4.8           
[88] statmod_1.5.1
```

### References

Frey, B. J., and D. Dueck. 2007. “Clustering by passing messages between data points.” *Science* 315 (5814): 972–76.

Ji, Z., and H. Ji. 2016. “TSCAN: Pseudo-time reconstruction and evaluation in single-cell RNA-seq analysis.” *Nucleic Acids Res.* 44 (13): e117.

Xu, C., and Z. Su. 2015. “Identification of cell types from single-cell transcriptomes using a novel clustering method.” *Bioinformatics* 31 (12): 1974–80.

---

1. Sten Linarrsson talked about this in SCG2018, but I don’t know where that work ended up. So this is what passes as a reference for the time being.[↩︎](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#fnref1)
