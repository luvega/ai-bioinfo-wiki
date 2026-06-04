---
source: OSCA
title: "Basics of Single-Cell Analysis with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.basic/marker-detection.html
ingested_at: 2026-06-04T01:51:46+00:00
status: source_ingested
---

# [Basics of Single-Cell Analysis with Bioconductor](https://bioconductor.org/books/3.23/OSCA.basic/)

# Chapter 6 Marker gene detection

## 6.1 Motivation

To interpret our clustering results from Chapter [5](https://bioconductor.org/books/3.23/OSCA.basic/clustering.html#clustering), we identify the genes that drive separation between clusters.
These marker genes allow us to assign biological meaning to each cluster based on their functional annotation.
In the simplest case, we have *a priori* knowledge of the marker genes associated with particular cell types, allowing us to treat the clustering as a proxy for cell type identity.
The same principle can be applied to discover more subtle differences between clusters (e.g., changes in activation or differentiation state) based on the behavior of genes in the affected pathways.

The most straightforward approach to marker gene detection involves testing for differential expression between clusters.
If a gene is strongly DE between clusters, it is likely to have driven the separation of cells in the clustering algorithm.
Several methods are available to quantify the differences in expression profiles between clusters and obtain a single ranking of genes for each cluster.
We will demonstrate some of these choices in this chapter using the 10X PBMC dataset:

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

#--- clustering ---#
g <- buildSNNGraph(sce.pbmc, k=10, use.dimred = 'PCA')
clust <- igraph::cluster_walktrap(g)$membership
colLabels(sce.pbmc) <- factor(clust)
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
## colData names(4): Sample Barcode sizeFactor label
## reducedDimNames(3): PCA TSNE UMAP
## mainExpName: NULL
## altExpNames(0):
```

## 6.2 Scoring markers by pairwise comparisons

Our general strategy is to compare each pair of clusters and compute scores quantifying the differences in the expression distributions between clusters.
The scores for all pairwise comparisons involving a particular cluster are then consolidated into a single `DataFrame` for that cluster.
The `scoreMarkers()` function from *[scran](https://bioconductor.org/packages/3.23/scran)* returns a list of `DataFrame`s where each `DataFrame` corresponds to a cluster and each row of the `DataFrame` corresponds to a gene.
In the `DataFrame` for cluster \(X\), the columns contain the `self.average`, the mean log-expression in \(X\);
`other.average`, the grand mean across all other clusters;
`self.detected`, the proportion of cells with detected expression in \(X\);
`other.detected`, the mean detected proportion across all other clusters;
and finally, a variety of effect size summaries generated from all pairwise comparisons involving \(X\).

```
library(scran)
marker.info <- scoreMarkers(sce.pbmc, colLabels(sce.pbmc))
marker.info
```

```
## List of length 19
## names(19): 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
```

```
colnames(marker.info[["5"]]) # statistics for cluster 5.
```

```
##  [1] "self.average"          "other.average"         "self.detected"        
##  [4] "other.detected"        "mean.logFC.cohen"      "min.logFC.cohen"      
##  [7] "median.logFC.cohen"    "max.logFC.cohen"       "rank.logFC.cohen"     
## [10] "mean.AUC"              "min.AUC"               "median.AUC"           
## [13] "max.AUC"               "rank.AUC"              "mean.logFC.detected"  
## [16] "min.logFC.detected"    "median.logFC.detected" "max.logFC.detected"   
## [19] "rank.logFC.detected"
```

For each cluster, we can then rank candidate markers based on one of these effect size summaries.
We demonstrate below with the mean AUC for cluster 5, which probably contains NK cells based on the top genes in Figure [6.1](https://bioconductor.org/books/3.23/OSCA.basic/marker-detection.html#fig:pbmc-scored-markers-5) (and no *CD3E* expression).
The next section will go into more detail on the differences between the various columns.

```
chosen <- marker.info[["5"]]
ordered <- chosen[order(chosen$mean.AUC, decreasing=TRUE),]
head(ordered[,1:4]) # showing basic stats only, for brevity.
```

```
## DataFrame with 6 rows and 4 columns
##        self.average other.average self.detected other.detected
##           <numeric>     <numeric>     <numeric>      <numeric>
## NKG7        4.59366      0.859465      1.000000      0.4070466
## PRF1        2.44789      0.217020      0.942197      0.1578987
## GZMA        2.71043      0.431911      0.965318      0.2414811
## GNLY        4.39154      0.571955      0.976879      0.2317908
## CST7        2.28360      0.336373      0.953757      0.2168489
## FGFBP2      2.09686      0.107363      0.872832      0.0722781
```

```
library(scater)
plotExpression(sce.pbmc, features=head(rownames(ordered)), 
    x="label", colour_by="label")
```

![Distribution of expression values across clusters for the top potential marker genes (as determined by the mean AUC) for cluster 5 in the PBMC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-marker-detection/pbmc-scored-markers-5-1.png)

Figure 6.1: Distribution of expression values across clusters for the top potential marker genes (as determined by the mean AUC) for cluster 5 in the PBMC dataset.

We deliberately use pairwise comparisons rather than comparing each cluster to the average of all other cells.
The latter approach is sensitive to the population composition, which introduces an element of unpredictability to the marker sets due to variation in cell type abundances.
(In the worst case, the presence of one subpopulation containing a majority of the cells will drive the selection of top markers for every other cluster, pushing out useful genes that can distinguish between the smaller subpopulations.)
Moreover, pairwise comparisons naturally provide more information to interpret of the utility of a marker, e.g., by providing log-fold changes to indicate which clusters are distinguished by each gene (Section [6.5](https://bioconductor.org/books/3.23/OSCA.basic/marker-detection.html#obtaining-the-full-effects)).

Previous editions of this chapter used \(p\)-values from the tests corresponding to each effect size, e.g., Welch’s \(t\)-test, the Wilcoxon ranked sum test.
While this is fine for ranking genes, the \(p\)-values themselves are statistically flawed and are of little use for inference -
see [Advanced Section 6.4](http://bioconductor.org/books/3.23/OSCA.advanced/marker-detection-redux.html#p-value-invalidity) for more details.
The `scoreMarkers()` function simplifies the marker detection procedure by omitting the \(p\)-values altogether, instead focusing on the underlying effect sizes.

## 6.3 Effect sizes for pairwise comparisons

In the context of marker detection, the area under the curve (AUC) quantifies our ability to distinguish between two distributions in a pairwise comparison.
The AUC represents the probability that a randomly chosen observation from our cluster of interest is greater than a randomly chosen observation from the other cluster.
A value of 1 corresponds to upregulation, where all values of our cluster of interest are greater than any value from the other cluster;
a value of 0.5 means that there is no net difference in the location of the distributions;
and a value of 0 corresponds to downregulation.
The AUC is closely related to the \(U\) statistic in the Wilcoxon ranked sum test (a.k.a., Mann-Whitney U-test).

```
auc.only <- chosen[,grepl("AUC", colnames(chosen))]
auc.only[order(auc.only$mean.AUC,decreasing=TRUE),]
```

```
## DataFrame with 33694 rows and 5 columns
##         mean.AUC     min.AUC median.AUC   max.AUC  rank.AUC
##        <numeric>   <numeric>  <numeric> <numeric> <integer>
## NKG7    0.979648    0.872869   0.999920  1.000000         1
## PRF1    0.952006    0.859677   0.967670  0.971098         2
## GZMA    0.937148    0.709620   0.978629  0.982659         1
## GNLY    0.936754    0.339047   0.985835  0.988439         2
## CST7    0.929354    0.662126   0.971301  0.976879         3
## ...          ...         ...        ...       ...       ...
## RPL18A 0.1157787 1.64550e-03  0.0329598  0.781352       196
## RPS2   0.1130700 1.63798e-03  0.0333445  0.727193       354
## RPL13  0.1102644 3.79454e-05  0.0265711  0.741644       308
## RPL34  0.1099831 1.26485e-05  0.0292802  0.753267       273
## RPL39  0.0940905 0.00000e+00  0.0106034  0.736617       324
```

Cohen’s \(d\) is a standardized log-fold change where the difference in the mean log-expression between groups is scaled by the average standard deviation across groups.
In other words, it is the number of standard deviations that separate the means of the two groups.
The interpretation is similar to the log-fold change; positive values indicate that the gene is upregulated in our cluster of interest,
negative values indicate downregulation and values close to zero indicate that there is little difference.
Cohen’s \(d\) is roughly analogous to the \(t\)-statistic in various two-sample \(t\)-tests.

```
cohen.only <- chosen[,grepl("logFC.cohen", colnames(chosen))]
cohen.only[order(cohen.only$mean.logFC.cohen,decreasing=TRUE),]
```

```
## DataFrame with 33694 rows and 5 columns
##         mean.logFC.cohen min.logFC.cohen median.logFC.cohen max.logFC.cohen
##                <numeric>       <numeric>          <numeric>       <numeric>
## NKG7             6.87259        1.469909            8.06827        10.01512
## GNLY             4.01156       -0.433635            4.62249         5.17942
## GZMA             3.44448        0.711910            4.11734         4.57485
## PRF1             3.22726        1.477353            3.51292         3.78740
## CTSW             3.05931       -0.134521            3.36589         4.33025
## ...                  ...             ...                ...             ...
## FTL             -2.34664        -5.97894          -1.175343       0.4045696
## HLA-DRA         -2.52222        -7.23626          -1.630425      -0.0731346
## CST3            -2.60740        -8.03982          -0.619617      -0.0446498
## RPL39           -2.64944        -4.38372          -2.772156       0.8637039
## LYZ             -2.75457        -8.95842          -0.313933       0.0527782
##         rank.logFC.cohen
##                <integer>
## NKG7                   1
## GNLY                   2
## GZMA                   2
## PRF1                   3
## CTSW                   3
## ...                  ...
## FTL                 2709
## HLA-DRA            28715
## CST3               28187
## RPL39                470
## LYZ                 5788
```

Finally, we also compute the log-fold change in the proportion of cells with detected expression between clusters.
This ignores any information about the magnitude of expression, only considering whether any expression is detected at all.
Again, positive values indicate that a greater proportion of cells express the gene in our cluster of interest compared to the other cluster.
Note that a pseudo-count is added to avoid undefined log-fold changes when no cells express the gene in either group.

```
detect.only <- chosen[,grepl("logFC.detected", colnames(chosen))]
detect.only[order(detect.only$mean.logFC.detected,decreasing=TRUE),]
```

```
## DataFrame with 33694 rows and 5 columns
##        mean.logFC.detected min.logFC.detected median.logFC.detected
##                  <numeric>          <numeric>             <numeric>
## KLRF1              4.57037         -0.0464514               5.16896
## PRSS23             4.31866          1.4045756               4.64665
## S1PR5              4.26667          0.8262053               4.72494
## XCL2               4.15288         -0.3938819               4.82717
## CD160              4.00963          0.7448285               4.67004
## ...                    ...                ...                   ...
## RAB32             -3.10193           -6.53387              -2.47745
## NCF2              -3.38216           -6.81623              -2.96725
## YBX3              -3.38964           -5.78481              -3.12673
## DAPP1             -3.57309           -6.06609              -3.50599
## LY96              -3.59748           -6.65178              -3.47917
##        max.logFC.detected rank.logFC.detected
##                 <numeric>           <integer>
## KLRF1             6.82930                   1
## PRSS23            5.87797                   2
## S1PR5             5.91562                   1
## XCL2              6.29276                   1
## CD160             6.08169                   1
## ...                   ...                 ...
## RAB32            0.000000                5916
## NCF2             0.000000                5916
## YBX3             0.150334                9174
## DAPP1            0.000000               11221
## LY96             0.000000               11221
```

The AUC or Cohen’s \(d\) is usually the best choice for general purpose marker detection, as they are effective regardless of the magnitude of the expression values.
The log-fold change in the detected proportion is specifically useful for identifying binary changes in expression.
See [Advanced Section 6.2](http://bioconductor.org/books/3.23/OSCA.advanced/marker-detection-redux.html#properties-of-each-effect-size) for more information about the practical differences between the effect sizes.

## 6.4 Summarizing pairwise effects

In a dataset with \(N\) clusters, each cluster is associated with \(N-1\) values for each type of effect size described in the previous section.
To simplify interpretation, we summarize the effects for each cluster into some key statistics such as the mean and median.
Each summary statistic has a different interpretation when used for ranking:

* The most obvious summary statistic is the mean.
  For cluster \(X\), a large mean effect size (>0 for the log-fold changes, >0.5 for the AUCs) indicates that the gene is upregulated in \(X\) compared to the average of the other groups.
* Another summary statistic is the median, where a large value indicates that the gene is upregulated in \(X\) compared to most (>50%) other clusters.
  The median provides greater robustness to outliers than the mean, which may or may not be desirable.
  On one hand, the median avoids an inflated effect size if only a minority of comparisons have large effects;
  on the other hand, it will also overstate the effect size by ignoring a minority of comparisons that have opposing effects.
* The minimum value (`min.*`) is the most stringent summary for identifying upregulated genes, as a large value indicates that the gene is upregulated in \(X\) compared to *all* other clusters.
  Conversely, if the minimum is small (<0 for the log-fold changes, <0.5 for the AUCs), we can conclude that the gene is downregulated in \(X\) compared to at least one other cluster.
* The maximum value (`max.*`) is the least stringent summary for identifying upregulated genes, as a large value can be obtained if there is strong upregulation in \(X\) compared to *any* other cluster.
  Conversely, if the maximum is small, we can conclude that the gene is downregulated in \(X\) compared to all other clusters.
* The minimum rank, a.k.a., “min-rank” (`rank.*`) is the smallest rank of each gene across all pairwise comparisons.
  Specifically, genes are ranked *within* each pairwise comparison based on decreasing effect size, and then the smallest rank *across* all comparisons is reported for each gene.
  If a gene has a small min-rank, we can conclude that it is one of the top upregulated genes in at least one comparison of \(X\) to another cluster.

Each of these summaries is computed for each effect size, for each gene, and for each cluster.
Our next step is to choose one of these summary statistics for one of the effect sizes and to use it to rank the rows of the `DataFrame`.
The choice of summary determines the stringency of the marker selection strategy, i.e., how many other clusters must we differ from?
For identifying upregulated genes, ranking by the minimum is the most stringent and the maximum is the least stringent;
the mean and median fall somewhere in between and are reasonable defaults for most applications.
The example below uses the median Cohen’s \(d\) to obtain a ranking of upregulated markers for cluster 12 (Figure [6.2](https://bioconductor.org/books/3.23/OSCA.basic/marker-detection.html#fig:pbmc-scored-markers-again)), which probably contains monocytes.

```
chosen <- marker.info[["12"]] # using another cluster, for some variety.
ordered <- chosen[order(chosen$median.logFC.cohen,decreasing=TRUE),]
head(ordered[,1:4]) # showing basic stats only, for brevity.
```

```
## DataFrame with 6 rows and 4 columns
##        self.average other.average self.detected other.detected
##           <numeric>     <numeric>     <numeric>      <numeric>
## LYZ         5.83418       2.09901      1.000000       0.652553
## S100A9      5.94112       1.96045      1.000000       0.698117
## S100A8      6.12531       1.70540      0.992308       0.632079
## FTL         6.32822       4.00709      1.000000       0.967855
## CTSS        3.84124       1.49877      0.976923       0.637764
## CST3        3.64555       1.80749      0.984615       0.618048
```

```
plotExpression(sce.pbmc, features=head(rownames(ordered)), 
    x="label", colour_by="label")
```

![Distribution of expression values across clusters for the top potential marker genes (as determined by the median Cohen's $d$) for cluster 12 in the PBMC dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-marker-detection/pbmc-scored-markers-again-1.png)

Figure 6.2: Distribution of expression values across clusters for the top potential marker genes (as determined by the median Cohen’s \(d\)) for cluster 12 in the PBMC dataset.

On some occasions, ranking by the minimum can be highly effective as it yields a concise set of highly cluster-specific markers.
However, any gene that is expressed at the same level in two or more clusters will simply not be detected.
This is likely to discard many interesting genes, especially if the clusters are finely resolved with weak separation.
To give a concrete example, consider a mixed population of CD4+-only, CD8+-only, double-positive and double-negative T cells.
Neither *Cd4* or *Cd8* would be detected as subpopulation-specific markers because each gene is expressed in two subpopulations such that the minimum effect would be small.
In practice, the minimum and maximum are most helpful for diagnosing discrepancies between the mean and median, rather than being used directly for ranking.

Ranking genes by the min-rank is similiar in stringency to ranking by the maximum effect size, in that both will respond to strong DE in a single comparison.
However, the min-rank is more useful as it ensures that a single comparison to another cluster with consistently large effects does not dominate the ranking.
If we select all genes with min-ranks less than or equal to \(T\), the resulting set is the union of the top \(T\) genes from all pairwise comparisons.
This guarantees that our set contains at least \(T\) genes that can distinguish our cluster of interest from any other cluster,
which permits a comprehensive determination of a cluster’s identity.
We demonstrate below for cluster 12, taking the top \(T=5\) genes with the largest Cohen’s \(d\) from each comparison to display in Figure [6.3](https://bioconductor.org/books/3.23/OSCA.basic/marker-detection.html#fig:pbmc-grouped-ranked-heat).

```
ordered <- chosen[order(chosen$rank.logFC.cohen),]
top.ranked <- ordered[ordered$rank.logFC.cohen <= 5,]
rownames(top.ranked)
```

```
##  [1] "S100A9"        "S100A8"        "S100A4"        "DUSP1"        
##  [5] "LYZ"           "FTL"           "CTSS"          "S100A6"       
##  [9] "FTH1"          "H3F3B"         "S100A12"       "FOS"          
## [13] "RP11-1143G9.4" "TYROBP"        "MNDA"          "TMSB4X"       
## [17] "CST3"
```

```
plotGroupedHeatmap(sce.pbmc, features=rownames(top.ranked), group="label", 
    center=TRUE, zlim=c(-3, 3))
```

![Heatmap of the centered average log-expression values for the top potential marker genes for cluster 12 in the PBMC dataset. The set of markers was selected as those genes with Cohen's $d$-derived min-ranks less than or equal to 5.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-marker-detection/pbmc-grouped-ranked-heat-1.png)

Figure 6.3: Heatmap of the centered average log-expression values for the top potential marker genes for cluster 12 in the PBMC dataset. The set of markers was selected as those genes with Cohen’s \(d\)-derived min-ranks less than or equal to 5.

Our discussion above has focused mainly on potential markers that are upregulated in our cluster of interest, as these are the easiest to interpret and experimentally validate.
However, it also means that any cluster defined by downregulation of a marker will not contain that gene among the top features.
This is occasionally relevant for subtypes or other states that are defined by low expression of particular genes.
In such cases, focusing on upregulation may yield a disappointing set of markers,
and it may be worth examining some of the lowest-ranked genes to see if there is any consistent downregulation compared to other clusters.

```
# Omitting the decreasing=TRUE to focus on negative effects.
ordered <- chosen[order(chosen$median.logFC.cohen),1:4]
head(ordered)
```

```
## DataFrame with 6 rows and 4 columns
##        self.average other.average self.detected other.detected
##           <numeric>     <numeric>     <numeric>      <numeric>
## RPSA        1.04854       2.74065      0.507692       0.890276
## RPL13A      3.99036       4.75633      0.992308       0.952263
## EEF1A1      4.20631       5.11958      0.992308       0.953528
## RPS18       3.75229       4.64261      0.984615       0.945780
## RPS27       4.71792       5.35539      0.992308       0.962433
## RPL3        3.01064       4.16446      0.930769       0.946790
```

## 6.5 Obtaining the full effects

For more complex questions, we may need to interrogate effect sizes from specific comparisons of interest.
To do so, we set `full.stats=TRUE` to obtain the effect sizes for all pairwise comparisons involving a particular cluster.
This is returned in the form of a nested `DataFrame` for each effect size type -
in the example below, `full.AUC` contains the AUCs for the comparisons between cluster 12 and every other cluster.

```
marker.info <- scoreMarkers(sce.pbmc, colLabels(sce.pbmc), full.stats=TRUE)
chosen <- marker.info[["12"]]
chosen$full.AUC
```

```
## DataFrame with 33694 rows and 18 columns
##                      1         2         3         4         5         6
##              <numeric> <numeric> <numeric> <numeric> <numeric> <numeric>
## RP11-34P13.3  0.500000  0.500000  0.500000       0.5       0.5       0.5
## FAM138A       0.500000  0.500000  0.500000       0.5       0.5       0.5
## OR4F5         0.500000  0.500000  0.500000       0.5       0.5       0.5
## RP11-34P13.7  0.497992  0.499106  0.498638       0.5       0.5       0.5
## RP11-34P13.8  0.500000  0.500000  0.500000       0.5       0.5       0.5
## ...                ...       ...       ...       ...       ...       ...
## AC233755.2    0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
## AC233755.1    0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
## AC240274.1    0.501668  0.502394  0.503668  0.507692  0.502001  0.501767
## AC213203.1    0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
## FAM231B       0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
##                      7         8         9        10        11        13
##              <numeric> <numeric> <numeric> <numeric> <numeric> <numeric>
## RP11-34P13.3  0.500000  0.500000   0.50000       0.5       0.5       0.5
## FAM138A       0.500000  0.500000   0.50000       0.5       0.5       0.5
## OR4F5         0.500000  0.500000   0.50000       0.5       0.5       0.5
## RP11-34P13.7  0.498889  0.494737   0.49812       0.5       0.5       0.5
## RP11-34P13.8  0.498889  0.498246   0.50000       0.5       0.5       0.5
## ...                ...       ...       ...       ...       ...       ...
## AC233755.2    0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
## AC233755.1    0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
## AC240274.1    0.504376  0.505965  0.503991  0.503257  0.504557  0.507692
## AC213203.1    0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
## FAM231B       0.500000  0.500000  0.500000  0.500000  0.500000  0.500000
##                     14        15        16        17        18        19
##              <numeric> <numeric> <numeric> <numeric> <numeric> <numeric>
## RP11-34P13.3   0.50000       0.5       0.5       0.5       0.5       0.5
## FAM138A        0.50000       0.5       0.5       0.5       0.5       0.5
## OR4F5          0.50000       0.5       0.5       0.5       0.5       0.5
## RP11-34P13.7   0.48913       0.5       0.5       0.5       0.5       0.5
## RP11-34P13.8   0.50000       0.5       0.5       0.5       0.5       0.5
## ...                ...       ...       ...       ...       ...       ...
## AC233755.2     0.50000  0.500000  0.500000  0.500000  0.500000  0.500000
## AC233755.1     0.50000  0.500000  0.500000  0.500000  0.500000  0.500000
## AC240274.1     0.49699  0.507692  0.490317  0.507692  0.507692  0.490716
## AC213203.1     0.50000  0.500000  0.500000  0.500000  0.500000  0.500000
## FAM231B        0.50000  0.500000  0.500000  0.500000  0.500000  0.500000
```

Say we want to identify the genes that distinguish cluster 12 from other clusters with high *LYZ* expression.
We subset `full.AUC` to the relevant comparisons and sort on our summary statistic of choice to obtain a ranking of markers within this subset.
This allows us to easily characterize subtle differences between closely related clusters.
To illustrate, we use the smallest rank from `computeMinRank()` to identify the top DE genes in cluster 12 compared to the other *LYZ*-high clusters (Figure [6.4](https://bioconductor.org/books/3.23/OSCA.basic/marker-detection.html#fig:pbmc-grouped-ranked-heat2)).

```
lyz.high <- c("7", "8", "10", "12", "15", "18") # based on inspection of the previous Figure.
subset <- chosen$full.AUC[,colnames(chosen$full.AUC) %in% lyz.high]
to.show <- subset[computeMinRank(subset) <= 10,]
to.show
```

```
## DataFrame with 21 rows and 5 columns
##                 7         8        10        15        18
##         <numeric> <numeric> <numeric> <numeric> <numeric>
## CTSS     0.558085  0.579001  0.956445  0.817448  0.791346
## S100A9   0.452085  0.857949  0.987110  0.845403  0.700962
## S100A12  0.478538  0.815196  0.916875  0.768199  0.669712
## S100A8   0.613966  0.924953  0.989016  0.898874  0.809135
## S100A6   0.470479  0.603509  0.880665  0.806379  0.799519
## ...           ...       ...       ...       ...       ...
## B2M      0.624051  0.447827  0.837838  0.409381  0.575481
## CYBA     0.622137  0.595547  0.745738  0.764728  0.694231
## H3F3B    0.676726  0.713374  0.722869  0.694559  0.593269
## TYROBP   0.498154  0.503914  0.914068  0.796060  0.820192
## FTL      0.595932  0.582564  0.968815  0.926642  0.867788
```

```
plotGroupedHeatmap(sce.pbmc[,colLabels(sce.pbmc) %in% lyz.high],
    features=rownames(to.show), group="label", center=TRUE, zlim=c(-3, 3))
```

![Heatmap of the centered average log-expression values for the top potential marker genes for cluster 12 relative to other _LYZ_-high clusters in the PBMC dataset. The set of markers was selected as those genes with AUC-derived min-ranks less than or equal to 10.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-marker-detection/pbmc-grouped-ranked-heat2-1.png)

Figure 6.4: Heatmap of the centered average log-expression values for the top potential marker genes for cluster 12 relative to other *LYZ*-high clusters in the PBMC dataset. The set of markers was selected as those genes with AUC-derived min-ranks less than or equal to 10.

Similarly, we can use the full set of effect sizes to define our own summary statistic if the precomputed measures are too coarse.
For example, we may be interested in markers that are upregulated against some percentage - say, 80% - of other clusters.
This improves the cluster specificity of the ranking by being more stringent than the median yet not as stringent as the minimum.
We achieve this by computing and sorting on the 20th percentile of effect sizes, as shown below.

```
stat <- rowQuantiles(as.matrix(chosen$full.AUC), p=0.2)
chosen[order(stat, decreasing=TRUE), 1:4] # just showing the basic stats for brevity.
```

```
## DataFrame with 33694 rows and 4 columns
##        self.average other.average self.detected other.detected
##           <numeric>     <numeric>     <numeric>      <numeric>
## S100A8      6.12531      1.705398      0.992308       0.632079
## S100A9      5.94112      1.960447      1.000000       0.698117
## LYZ         5.83418      2.099010      1.000000       0.652553
## MNDA        2.99279      0.711229      0.938462       0.359890
## FOS         4.61740      2.689020      0.992308       0.848361
## ...             ...           ...           ...            ...
## EEF1A1      4.20631       5.11958      0.992308       0.953528
## RPL13A      3.99036       4.75633      0.992308       0.952263
## RPS27       4.71792       5.35539      0.992308       0.962433
## RPL3        3.01064       4.16446      0.930769       0.946790
## RPS29       3.40484       4.45358      0.969231       0.941641
```

## 6.6 Using a log-fold change threshold

The Cohen’s \(d\) and AUC calculations consider both the magnitude of the difference between clusters as well as the variability within each cluster.
If the variability is lower, it is possible for a gene to have a large effect size even if the magnitude of the difference is small.
These genes tend to be somewhat uninformative for cell type identification despite their strong differential expression (e.g., ribosomal protein genes).
We would prefer genes with larger log-fold changes between clusters, even if they have higher variability.

To favor the detection of such genes, we can compute the effect sizes relative to a log-fold change threshold by setting `lfc=` in `scoreMarkers()`.
The definition of Cohen’s \(d\) is generalized to the standardized difference between the observed log-fold change and the specified `lfc` threshold.
Similarly, the AUC is redefined as the probability of randomly picking an expression value from one cluster that is greater than a random value from the other cluster plus `lfc`.
A large positive Cohen’s \(d\) and an AUC above 0.5 can only be obtained if the observed log-fold change between clusters is significantly greater than `lfc`.
We demonstrate below by obtaining the top markers for cluster 4 in the PBMC dataset with `lfc=2` (Figure [6.5](https://bioconductor.org/books/3.23/OSCA.basic/marker-detection.html#fig:pbmc-markers-4-lfc)).

```
marker.info.lfc <- scoreMarkers(sce.pbmc, colLabels(sce.pbmc), lfc=2)
chosen2 <- marker.info.lfc[["4"]] # another cluster for some variety.
chosen2 <- chosen2[order(chosen2$mean.AUC, decreasing=TRUE),]
chosen2[,c("self.average", "other.average", "mean.AUC")]
```

```
## DataFrame with 33694 rows and 3 columns
##            self.average other.average  mean.AUC
##               <numeric>     <numeric> <numeric>
## PF4             6.59491     0.0443057  0.954053
## TAGLN2          5.61751     1.0214803  0.942738
## SDPR            5.42625     0.0204998  0.912550
## NRGN            4.79064     0.0868449  0.910566
## PPBP            6.33330     0.0388266  0.869268
## ...                 ...           ...       ...
## AC233755.2            0     0.0000000         0
## AC233755.1            0     0.0000000         0
## AC240274.1            0     0.0101298         0
## AC213203.1            0     0.0000000         0
## FAM231B               0     0.0000000         0
```

```
plotDots(sce.pbmc, rownames(chosen2)[1:10], group="label")
```

![Dot plot of the top potential marker genes (as determined by the mean AUC) for cluster 4 in the PBMC dataset. Each row corrresponds to a marker gene and each column corresponds to a cluster. The size of each dot represents the proportion of cells with detected expression of the gene in the cluster, while the color is proportional to the average expression across all cells in that cluster.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-marker-detection/pbmc-markers-4-lfc-1.png)

Figure 6.5: Dot plot of the top potential marker genes (as determined by the mean AUC) for cluster 4 in the PBMC dataset. Each row corrresponds to a marker gene and each column corresponds to a cluster. The size of each dot represents the proportion of cells with detected expression of the gene in the cluster, while the color is proportional to the average expression across all cells in that cluster.

Note that the interpretation of the AUC and Cohen’s \(d\) becomes slightly more complicated when `lfc` is non-zero.
If `lfc` is positive, a positive Cohen’s \(d\) and an AUC above 0.5 represents upregulation.
However, a negative Cohen’s \(d\) or AUC below 0.5 may not represent downregulation; it may just indicate that the observed log-fold change is less than the specified `lfc`.
The converse applies when `lfc` is negative, where the only conclusive interpretation occurs for downregulated genes.
For the most part, this complication is not too problematic for routine marker detection, as we are mostly interested in upregulated genes with large positive Cohen’s \(d\) and AUCs above 0.5.

## 6.7 Handling blocking factors

Large studies may contain factors of variation that are known and not interesting (e.g., batch effects, sex differences).
If these are not modelled, they can interfere with marker gene detection - most obviously by inflating the variance within each cluster, but also by distorting the log-fold changes if the cluster composition varies across levels of the blocking factor.
To avoid these issues, we specify the blocking factor via the `block=` argument, as demonstrated below for the 416B data set.

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

#--- clustering ---#
my.dist <- dist(reducedDim(sce.416b, "PCA"))
my.tree <- hclust(my.dist, method="ward.D2")

library(dynamicTreeCut)
my.clusters <- unname(cutreeDynamic(my.tree, distM=as.matrix(my.dist),
    minClusterSize=10, verbose=0))
colLabels(sce.416b) <- factor(my.clusters)
```

```
m.out <- scoreMarkers(sce.416b, colLabels(sce.416b), block=sce.416b$block)
```

For each gene, each pairwise comparison between clusters is performed separately in each level of the blocking factor - in this case, the plate of origin.
By comparing within each batch, we cancel out any batch effects so that they are not conflated with the biological differences between subpopulations.
The effect sizes are then averaged across batches to obtain a single value per comparison, using a weighted mean that accounts for the number of cells involved in the comparison in each batch.
A similar correction is applied to the mean log-expression and proportion of detected cells inside and outside each cluster.

```
demo <- m.out[["1"]] 
ordered <- demo[order(demo$median.logFC.cohen, decreasing=TRUE),]
ordered[,1:4]
```

```
## DataFrame with 46604 rows and 4 columns
##         self.average other.average self.detected other.detected
##            <numeric>     <numeric>     <numeric>      <numeric>
## Myh11        4.03436      0.861019      0.988132       0.303097
## Cd200r3      7.97667      3.524762      0.977675       0.624507
## Pi16         6.27654      2.644421      0.957126       0.530395
## Actb        15.48533     14.808584      1.000000       1.000000
## Ctsd        11.61247      9.130141      1.000000       1.000000
## ...              ...           ...           ...            ...
## Spc24      0.4772577       5.03548      0.222281       0.862153
## Ska1       0.0787421       4.43426      0.118743       0.773950
## Pimreg     0.5263611       5.35494      0.258150       0.910706
## Birc5      1.5580536       7.07230      0.698746       0.976929
## Ccna2      0.9664521       6.55243      0.554104       0.948520
```

```
plotExpression(sce.416b, features=rownames(ordered)[1:6],
    x="label", colour_by="block")
```

![Distribution of expression values across clusters for the top potential marker genes from cluster 1 in the 416B dataset. Each point represents a cell and is colored by the batch of origin.](../../../../raw/bioconductor_books/assets/OSCA/osca.basic-marker-detection/blocked-markers-416b-1.png)

Figure 6.6: Distribution of expression values across clusters for the top potential marker genes from cluster 1 in the 416B dataset. Each point represents a cell and is colored by the batch of origin.

The `block=` argument works for all effect sizes shown above and is robust to differences in the log-fold changes or variance between batches.
However, it assumes that each pair of clusters is present in at least one batch.
In scenarios where cells from two clusters never co-occur in the same batch, the associated pairwise comparison will be impossible and is ignored during calculation of summary statistics.

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
 [3] scran_1.40.0                scuttle_1.22.0             
 [5] SingleCellExperiment_1.34.0 SummarizedExperiment_1.42.0
 [7] Biobase_2.72.0              GenomicRanges_1.64.0       
 [9] Seqinfo_1.2.0               IRanges_2.46.0             
[11] S4Vectors_0.50.0            BiocGenerics_0.58.0        
[13] generics_0.1.4              MatrixGenerics_1.24.0      
[15] matrixStats_1.5.0           BiocStyle_2.40.0           
[17] rebook_1.22.0              

loaded via a namespace (and not attached):
 [1] tidyselect_1.2.1    viridisLite_0.4.3   vipor_0.4.7        
 [4] dplyr_1.2.1         farver_2.1.2        viridis_0.6.5      
 [7] filelock_1.0.3      S7_0.2.2            fastmap_1.2.0      
[10] bluster_1.22.0      XML_3.99-0.23       digest_0.6.39      
[13] rsvd_1.0.5          lifecycle_1.0.5     cluster_2.1.8.2    
[16] statmod_1.5.1       magrittr_2.0.5      compiler_4.6.0     
[19] rlang_1.2.0         sass_0.4.10         tools_4.6.0        
[22] igraph_2.3.0        yaml_2.3.12         knitr_1.51         
[25] labeling_0.4.3      S4Arrays_1.12.0     dqrng_0.4.1        
[28] DelayedArray_0.38.0 RColorBrewer_1.1-3  abind_1.4-8        
[31] BiocParallel_1.46.0 withr_3.0.2         CodeDepends_0.6.7  
[34] grid_4.6.0          beachmat_2.28.0     edgeR_4.10.0       
[37] scales_1.4.0        dichromat_2.0-0.1   cli_3.6.6          
[40] rmarkdown_2.31      otel_0.2.0          metapod_1.20.0     
[43] ggbeeswarm_0.7.3    cachem_1.1.0        parallel_4.6.0     
[46] BiocManager_1.30.27 XVector_0.52.0      vctrs_0.7.3        
[49] Matrix_1.7-5        jsonlite_2.0.0      dir.expiry_1.20.0  
[52] bookdown_0.46       BiocSingular_1.28.0 BiocNeighbors_2.6.0
[55] ggrepel_0.9.8       beeswarm_0.4.0      irlba_2.3.7        
[58] locfit_1.5-9.12     limma_3.68.0        jquerylib_0.1.4    
[61] glue_1.8.1          codetools_0.2-20    cowplot_1.2.0      
[64] gtable_0.3.6        ScaledMatrix_1.20.0 tibble_3.3.1       
[67] pillar_1.11.1       rappdirs_0.3.4      htmltools_0.5.9    
[70] graph_1.90.0        R6_2.6.1            evaluate_1.0.5     
[73] lattice_0.22-9      pheatmap_1.0.13     bslib_0.10.0       
[76] Rcpp_1.1.1-1.1      gridExtra_2.3       SparseArray_1.12.0 
[79] xfun_0.57           pkgconfig_2.0.3
```
