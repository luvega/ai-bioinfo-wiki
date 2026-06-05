---
source: OSCA
title: "Multi-Sample Single-Cell Analyses with Bioconductor"
original_url: https://bioconductor.org/books/3.23/OSCA.multisample/ambient-problems.html
ingested_at: 2026-06-04T01:52:27+00:00
status: source_ingested
---

# [Multi-Sample Single-Cell Analyses with Bioconductor](https://bioconductor.org/books/3.23/OSCA.multisample/)

# Chapter 5 Problems with ambient RNA

## 5.1 Background

Ambient contamination is a phenomenon that is generally most pronounced in massively multiplexed scRNA-seq protocols.
Briefly, extracellular RNA (most commonly released upon cell lysis) is captured along with each cell in its reaction chamber, contributing counts to genes that are not otherwise expressed in that cell (see [Advanced Section 7.2](http://bioconductor.org/books/3.23/OSCA.advanced/droplet-processing.html#qc-droplets)).
Differences in the ambient profile across samples are not uncommon when dealing with strong experimental perturbations where strong expression of a gene in a condition-specific cell type can “bleed over” into all other cell types in the same sample.
This is problematic for DE analyses between conditions, as DEGs detected for a particular cell type may be driven by differences in the ambient profiles rather than any intrinsic change in gene regulation.

To illustrate, we consider the *Tal1*-knockout (KO) chimera data from Pijuan-Sala et al. ([2019](https://bioconductor.org/books/3.23/OSCA.multisample/ambient-problems.html#ref-pijuansala2019single)).
This is very similar to the WT chimera dataset we previously examined, only differing in that the *Tal1* gene was knocked out in the injected cells.
*Tal1* is a transcription factor that has known roles in erythroid differentiation; the aim of the experiment was to determine if blocking of the erythroid lineage diverted cells to other developmental fates.
(To cut a long story short: yes, it did.)

```
library(MouseGastrulationData)
sce.tal1 <- Tal1ChimeraData()
counts(sce.tal1) <- as(counts(sce.tal1), "CsparseMatrix") 

library(scuttle)
rownames(sce.tal1) <- uniquifyFeatureNames(
    rowData(sce.tal1)$ENSEMBL, 
    rowData(sce.tal1)$SYMBOL
)
sce.tal1
```

```
## class: SingleCellExperiment 
## dim: 29453 56122 
## metadata(0):
## assays(1): counts
## rownames(29453): Xkr4 Gm1992 ... CAAA01147332.1 tomato-td
## rowData names(2): ENSEMBL SYMBOL
## colnames(56122): cell_1 cell_2 ... cell_56121 cell_56122
## colData names(9): cell barcode ... pool sizeFactor
## reducedDimNames(1): pca.corrected
## mainExpName: NULL
## altExpNames(0):
```

We will perform a DE analysis between WT and KO cells labelled as “neural crest”.
We observe that the strongest DEGs are the hemoglobins, which are downregulated in the injected cells.
This is rather surprising as these cells are distinct from the erythroid lineage and should not express hemoglobins at all.
The most sober explanation is that the background samples contain more hemoglobin transcripts in the ambient solution due to leakage from erythrocytes (or their precursors) during sorting and dissociation.

```
library(scran)
summed.tal1 <- aggregateAcrossCells(sce.tal1, 
    ids=DataFrame(sample=sce.tal1$sample,
        label=sce.tal1$celltype.mapped)
)
summed.tal1$block <- summed.tal1$sample %% 2 == 0 # Add blocking factor.

# Subset to our neural crest cells.
summed.neural <- summed.tal1[,summed.tal1$label=="Neural crest"]
summed.neural
```

```
## class: SingleCellExperiment 
## dim: 29453 4 
## metadata(0):
## assays(1): counts
## rownames(29453): Xkr4 Gm1992 ... CAAA01147332.1 tomato-td
## rowData names(2): ENSEMBL SYMBOL
## colnames: NULL
## colData names(13): cell barcode ... ncells block
## reducedDimNames(1): pca.corrected
## mainExpName: NULL
## altExpNames(0):
```

```
# Standard edgeR analysis, as described in previous chapters.
res.neural <- pseudoBulkDGE(summed.neural, 
    label=summed.neural$label,
    design=~factor(block) + tomato,
    coef="tomatoTRUE",
    condition=summed.neural$tomato)
summarizeTestsPerLabel(decideTestsPerLabel(res.neural))
```

```
##               -1     0   1    NA
## Neural crest 262 10009 379 18803
```

```
# Summary of the direction of log-fold changes.
tab.neural <- res.neural[[1]]
tab.neural <- tab.neural[order(tab.neural$PValue),]
head(tab.neural, 10)
```

```
## DataFrame with 10 rows and 5 columns
##                   logFC    logCPM         F      PValue         FDR
##               <numeric> <numeric> <numeric>   <numeric>   <numeric>
## Hbb-bh1       -8.091019   9.15972 11529.611 1.73303e-32 1.84568e-28
## Hba-x         -7.724798   8.53284  8688.919 4.41154e-31 2.34914e-27
## Hbb-y         -8.415628   8.35705  8090.618 1.01174e-30 3.59168e-27
## Xist          -7.555732   8.21232  5312.985 1.21874e-28 3.24490e-25
## Hba-a1        -8.596678   6.74429  2957.243 8.54543e-26 1.82018e-22
## Hba-a2        -8.866236   5.81300  1378.635 1.24100e-22 2.20277e-19
## Cdkn1c        -8.864542   4.96097   774.121 3.70061e-20 5.63021e-17
## Uba52         -0.879664   8.38618   463.092 1.05184e-16 1.40026e-13
## Fdps           0.981409   7.21805   377.486 9.74340e-16 1.15297e-12
## Gt(ROSA)26Sor  1.481295   5.71617   369.240 1.23759e-15 1.31803e-12
```

As an aside, it is worth mentioning that the “replicates” in this study are more technical than biological,
so some exaggeration of the significance of the effects is to be expected.
Nonetheless, it is a useful dataset to demonstrate some strategies for mitigating issues caused by ambient contamination.

## 5.2 Filtering out affected DEGs

### 5.2.1 By estimating ambient contamination

As shown above, the presence of ambient contamination makes it difficult to interpret multi-condition DE analyses.
To mitigate its effects, we need to obtain an estimate of the ambient “expression” profile from the raw count matrix for each sample.
We follow the approach used in `emptyDrops()` (Lun et al. [2019](https://bioconductor.org/books/3.23/OSCA.multisample/ambient-problems.html#ref-lun2018distinguishing)) and consider all barcodes with total counts below 100 to represent empty droplets.
We then sum the counts for each gene across these barcodes to obtain an expression vector representing the ambient profile for each sample.

```
library(DropletUtils)
ambient <- vector("list", ncol(summed.neural))

# Looping over all raw (unfiltered) count matrices and
# computing the ambient profile based on its low-count barcodes.
# Turning off rounding, as we know this is count data.
for (s in seq_along(ambient)) {
    raw.tal1 <- Tal1ChimeraData(type="raw", samples=s)[[1]]
    counts(raw.tal1) <- as(counts(raw.tal1), "CsparseMatrix")
    ambient[[s]] <- ambientProfileEmpty(counts(raw.tal1), 
        good.turing=FALSE, round=FALSE)
}

# Cleaning up the output for pretty printing.
ambient <- do.call(cbind, ambient)
colnames(ambient) <- seq_len(ncol(ambient))
rownames(ambient) <- uniquifyFeatureNames(
    rowData(raw.tal1)$ENSEMBL, 
    rowData(raw.tal1)$SYMBOL
)
head(ambient)
```

```
##          1  2  3  4
## Xkr4     1  0  0  0
## Gm1992   0  0  0  0
## Gm37381  1  0  1  0
## Rp1      0  1  0  1
## Sox17   76 76 31 53
## Gm37323  0  0  0  0
```

For each sample, we determine the maximum proportion of the count for each gene that could be attributed to ambient contamination.
This is done by scaling the ambient profile in `ambient` to obtain a per-gene expected count from ambient contamination, with which we compute the \(p\)-value for observing a count equal to or lower than that in `summed.neural`.
We perform this for a range of scaling factors and identify the largest factor that yields a \(p\)-value above a given threshold.
The scaled ambient profile represents the upper bound of the contribution to each sample from ambient contamination.
We deliberately use an upper bound so that our next step will aggressively remove any gene that is potentially problematic.

```
max.ambient <- ambientContribMaximum(counts(summed.neural), 
    ambient, mode="proportion")
head(max.ambient)
```

```
##           [,1]   [,2]  [,3] [,4]
## Xkr4       NaN    NaN   NaN  NaN
## Gm1992     NaN    NaN   NaN  NaN
## Gm37381    NaN    NaN   NaN  NaN
## Rp1        NaN    NaN   NaN  NaN
## Sox17   0.1775 0.1833 0.468    1
## Gm37323    NaN    NaN   NaN  NaN
```

Genes in which over 10% of the counts are ambient-derived are subsequently discarded from our analysis.
For balanced designs, this threshold prevents ambient contribution from biasing the true fold-change by more than 10%, which is a tolerable margin of error for most applications.
(Unbalanced designs may warrant the use of a weighted average to account for sample size differences between groups.)
This approach yields a slightly smaller list of DEGs without the hemoglobins, which is encouraging as it suggests that any other, less obvious effects of ambient contamination have also been removed.

```
# Averaging the ambient contribution across samples.
contamination <- rowMeans(max.ambient, na.rm=TRUE)
non.ambient <- contamination <= 0.1
summary(non.ambient)
```

```
##    Mode   FALSE    TRUE     NAs 
## logical    1475   15306   12672
```

```
okay.genes <- names(non.ambient)[which(non.ambient)]
tab.neural2 <- tab.neural[rownames(tab.neural) %in% okay.genes,]

table(Direction=tab.neural2$logFC > 0, Significant=tab.neural2$FDR <= 0.05)
```

```
##          Significant
## Direction FALSE TRUE
##     FALSE  4907  229
##     TRUE   4882  352
```

```
head(tab.neural2, 10)
```

```
## DataFrame with 10 rows and 5 columns
##                   logFC    logCPM         F      PValue         FDR
##               <numeric> <numeric> <numeric>   <numeric>   <numeric>
## Xist          -7.555732   8.21232  5312.985 1.21874e-28 3.24490e-25
## Uba52         -0.879664   8.38618   463.092 1.05184e-16 1.40026e-13
## Fdps           0.981409   7.21805   377.486 9.74340e-16 1.15297e-12
## Gt(ROSA)26Sor  1.481295   5.71617   369.240 1.23759e-15 1.31803e-12
## Grb10         -1.403198   6.58314   357.614 1.74898e-15 1.69333e-12
## Mcts2          1.137663   6.42689   346.570 2.45351e-15 2.17749e-12
## H13           -1.481660   5.90902   326.596 4.64769e-15 3.80753e-12
## Msmo1          1.493798   5.43923   310.155 8.08738e-15 5.99299e-12
## Snrpb          0.564204  10.18934   308.918 8.44083e-15 5.99299e-12
## Mest           0.549344  10.98269   305.397 9.54229e-15 6.35158e-12
```

A softer approach is to simply report the average contaminating percentage for each gene in the table of DE statistics.
Readers can then make up their own minds as to whether a particular DEG’s effect is driven by ambient contamination.
Indeed, it is worth remembering that `maximumAmbience()` will report the maximum possible contamination rather than attempting to estimate the actual level of contamination, and filtering on the former may be too conservative.
This is especially true for cell populations that are contributing to the differences in the ambient pool; in the most extreme case, the reported maximum contamination would be 100% for cell types with an expression profile that is identical to the ambient pool.

```
tab.neural3 <- tab.neural
tab.neural3$contamination <- contamination[rownames(tab.neural3)]
head(tab.neural3)
```

```
## DataFrame with 6 rows and 6 columns
##             logFC    logCPM         F      PValue         FDR contamination
##         <numeric> <numeric> <numeric>   <numeric>   <numeric>     <numeric>
## Hbb-bh1  -8.09102   9.15972  11529.61 1.73303e-32 1.84568e-28     0.9900717
## Hba-x    -7.72480   8.53284   8688.92 4.41154e-31 2.34914e-27     0.9945348
## Hbb-y    -8.41563   8.35705   8090.62 1.01174e-30 3.59168e-27     0.9674483
## Xist     -7.55573   8.21232   5312.99 1.21874e-28 3.24490e-25     0.0605735
## Hba-a1   -8.59668   6.74429   2957.24 8.54543e-26 1.82018e-22     0.8626846
## Hba-a2   -8.86624   5.81300   1378.63 1.24100e-22 2.20277e-19     0.7351403
```

### 5.2.2 With prior knowledge

Another strategy to estimating the ambient proportions involves the use of prior knowledge of mutually exclusive gene expression profiles (Young and Behjati [2018](https://bioconductor.org/books/3.23/OSCA.multisample/ambient-problems.html#ref-young2018soupx)).
In this case, we assume (reasonably) that hemoglobins should not be expressed in neural crest cells and use this to estimate the contamination in each sample.
This is achieved with the `controlAmbience()` function, which scales the ambient profile so that the hemoglobin coverage is the same as the corresponding sample of `summed.neural`.
From these profiles, we compute proportions of ambient contamination that are used to mark or filter out affected genes in the same manner as described above.

```
is.hbb <- grep("^Hb[ab]-", rownames(summed.neural))
ctrl.ambient <- ambientContribNegative(counts(summed.neural), ambient,
    features=is.hbb,  mode="proportion")
head(ctrl.ambient)
```

```
##            [,1]    [,2]   [,3] [,4]
## Xkr4        NaN     NaN    NaN  NaN
## Gm1992      NaN     NaN    NaN  NaN
## Gm37381     NaN     NaN    NaN  NaN
## Rp1         NaN     NaN    NaN  NaN
## Sox17   0.06774 0.08798 0.4796    1
## Gm37323     NaN     NaN    NaN  NaN
```

```
ctrl.non.ambient <- rowMeans(ctrl.ambient, na.rm=TRUE) <= 0.1
summary(ctrl.non.ambient)
```

```
##    Mode   FALSE    TRUE     NAs 
## logical    1388   15393   12672
```

```
okay.genes <- names(ctrl.non.ambient)[which(ctrl.non.ambient)]
tab.neural4 <- tab.neural[rownames(tab.neural) %in% okay.genes,]
head(tab.neural4)
```

```
## DataFrame with 6 rows and 5 columns
##                   logFC    logCPM         F      PValue         FDR
##               <numeric> <numeric> <numeric>   <numeric>   <numeric>
## Xist          -7.555732   8.21232  5312.985 1.21874e-28 3.24490e-25
## Uba52         -0.879664   8.38618   463.092 1.05184e-16 1.40026e-13
## Fdps           0.981409   7.21805   377.486 9.74340e-16 1.15297e-12
## Gt(ROSA)26Sor  1.481295   5.71617   369.240 1.23759e-15 1.31803e-12
## Grb10         -1.403198   6.58314   357.614 1.74898e-15 1.69333e-12
## Mcts2          1.137663   6.42689   346.570 2.45351e-15 2.17749e-12
```

Any highly expressed cell type-specific gene is a candidate for this procedure,
most typically in cell types that are highly specialized towards manufacturing a protein product.
Aside from hemoglobin, we could use immunoglobulins in populations containing B cells,
or insulin and glucagon in pancreas datasets ([Advanced Figure 6.3](http://bioconductor.org/books/3.23/OSCA.advanced/marker-detection-redux.html#fig:viol-gcg-lawlor)).
The experimental setting may also provide some genes that must only be present in the ambient solution;
for example, the mitochondrial transcripts can be used to estimate ambient contamination in single-nucleus RNA-seq,
while *Xist* can be used for datasets involving mixtures of male and female cells
(where the contaminating percentages are estimated from the profiles of male cells only).

If appropriate control features are available, this approach allows us to obtain a more accurate estimate of the contamination in each pseudo-bulk sample compared to the upper bound provided by `maximumAmbience()`.
This avoids the removal of genuine DEGs due to overestimation fo the ambient contamination from the latter.
However, the performance of this approach is fully dependent on the suitability of the control features - if a “control” feature is actually genuinely expressed in a cell type, the ambient contribution will be overestimated.
A simple mitigating strategy is to simply take the lower of the proportions from `controlAmbience()` and `maximumAmbience()`, with the idea being that the latter will avoid egregious overestimation when the control set is misspecified.

### 5.2.3 Without an ambient profile

An estimate of the ambient profile is rarely available for public datasets where only the per-cell count matrices are provided.
In such cases, we must instead use the rest of the dataset to infer something about the effects of ambient contamination.
The most obvious approach is construct a proxy ambient profile by summing the counts for all cells from each sample, which can be used in place of the actual profile in the previous calculations.

```
proxy.ambient <- aggregateAcrossCells(summed.tal1,
    ids=summed.tal1$sample)

# Using 'proxy.ambient' instead of the estimaed 'ambient'.
max.ambient.proxy <- ambientContribMaximum(counts(summed.neural), 
    counts(proxy.ambient), mode="proportion")
head(max.ambient.proxy)
```

```
##           [,1]   [,2]   [,3]   [,4]
## Xkr4       NaN    NaN    NaN    NaN
## Gm1992     NaN    NaN    NaN    NaN
## Gm37381    NaN    NaN    NaN    NaN
## Rp1        NaN    NaN    NaN    NaN
## Sox17   0.7427 0.9891 0.5283 0.9067
## Gm37323    NaN    NaN    NaN    NaN
```

```
con.ambient.proxy <- ambientContribNegative(counts(summed.neural), 
    counts(proxy.ambient), features=is.hbb,  mode="proportion")
head(con.ambient.proxy)
```

```
##         [,1] [,2]   [,3] [,4]
## Xkr4     NaN  NaN    NaN  NaN
## Gm1992   NaN  NaN    NaN  NaN
## Gm37381  NaN  NaN    NaN  NaN
## Rp1      NaN  NaN    NaN  NaN
## Sox17      1    1 0.6032    1
## Gm37323  NaN  NaN    NaN  NaN
```

This assumes equal contributions from all labels to the ambient pool, which is not entirely unrealistic (Figure [5.1](https://bioconductor.org/books/3.23/OSCA.multisample/ambient-problems.html#fig:proxy-ambience)) though some discrepancies can be expected due to the presence of particularly fragile cell types or extracellular RNA.

```
par(mfrow=c(2,2))
for (i in seq_len(ncol(proxy.ambient))) {
    true <- ambient[,i]
    proxy <- assay(proxy.ambient)[,i]
    logged <- edgeR::cpm(cbind(proxy, true), log=TRUE, prior.count=2)
    logFC <- logged[,1] - logged[,2]
    abundance <- rowMeans(logged)
    plot(abundance, logFC, main=paste("Sample", i))
}
```

![MA plots of the log-fold change of the proxy ambient profile over the real profile for each sample in the _Tal1_ chimera dataset.](../../../../raw/bioconductor_books/assets/OSCA/osca.multisample-ambient-problems/proxy-ambience-1.png)

Figure 5.1: MA plots of the log-fold change of the proxy ambient profile over the real profile for each sample in the *Tal1* chimera dataset.

Alternatively, we may choose to mitigate the effect of ambient contamination by focusing on label-specific DEGs.
Contamination-driven DEGs should be systematically present in comparisons for all labels, and thus can be eliminated by simply ignoring all genes that are significant in a majority of these comparisons (Section [4.5.2](https://bioconductor.org/books/3.23/OSCA.multisample/multi-sample-comparisons.html#cross-label-meta-analyses)).
The obvious drawback of this approach is that it discounts genuine DEGs that have a consistent effect in most/all labels, though one could perhaps argue that such “global” DEGs are not particularly interesting anyway.
It is also complicated by fluctuations in detection power across comparisons involving different numbers of cells - or replicates, after filtering pseudo-bulk profiles by the number of cells.

```
res.tal1 <- pseudoBulkSpecific(summed.tal1, 
    label=summed.tal1$label,
    design=~factor(block) + tomato,
    coef="tomatoTRUE",
    condition=summed.tal1$tomato)

# Inspecting our neural crest results again.
tab.neural.again <- res.tal1[["Neural crest"]]
head(tab.neural.again[order(tab.neural.again$PValue),], 10)
```

```
## DataFrame with 10 rows and 6 columns
##                   logFC    logCPM         F      PValue         FDR
##               <numeric> <numeric> <numeric>   <numeric>   <numeric>
## Fdps           0.981409   7.21805  377.4863 9.74340e-16 1.03767e-11
## Msmo1          1.493798   5.43923  310.1551 1.19552e-14 6.36612e-11
## Hmgcs1         1.249745   5.70837  180.2450 2.39115e-12 8.48858e-09
## Idi1           1.173617   5.37688  164.6100 6.01728e-12 1.60210e-08
## Gt(ROSA)26Sor  1.481295   5.71617  369.2397 1.73967e-11 3.70549e-08
## Sox9           0.537525   7.17373  106.9626 4.17496e-10 7.41055e-07
## Insig1         1.257331   4.06887   90.9307 1.91672e-09 2.91615e-06
## Nkd1           0.719050   5.92690   98.3129 2.22975e-09 2.96836e-06
## Acat2          0.508866   6.80012   86.0873 3.17098e-09 3.75232e-06
## Fdft1          0.841062   5.32293   90.4939 4.21256e-09 4.48638e-06
##               OtherAverage
##                  <numeric>
## Fdps            -0.0912367
## Msmo1            0.0269770
## Hmgcs1          -0.0618528
## Idi1            -0.0820179
## Gt(ROSA)26Sor    0.5408775
## Sox9            -0.0426333
## Insig1          -0.2879496
## Nkd1             0.0333592
## Acat2           -0.0521009
## Fdft1            0.0336437
```

```
# By comparison, the hemoglobins are all the way at the bottom.
head(tab.neural.again[is.hbb,], 10)
```

```
## DataFrame with 8 rows and 6 columns
##             logFC    logCPM          F    PValue       FDR OtherAverage
##         <numeric> <numeric>  <numeric> <numeric> <numeric>    <numeric>
## Hbb-bt   -7.76723   1.33059    61.0416 1.0000000   1.00000     -7.86818
## Hbb-bs   -5.84810   3.42835   269.9573 1.0000000   1.00000     -8.15477
## Hbb-bh2        NA        NA         NA        NA        NA     -8.98450
## Hbb-bh1  -8.09102   9.15972 11529.6114 0.9251591   1.00000     -8.08037
## Hbb-y    -8.41563   8.35705  8090.6176 0.4168648   1.00000     -8.21261
## Hba-x    -7.72480   8.53284  8688.9188 0.0808742   0.82501     -7.38501
## Hba-a1   -8.59668   6.74429  2957.2428 0.2809662   1.00000     -8.05722
## Hba-a2   -8.86624   5.81300  1378.6346 0.2596559   1.00000     -7.96514
```

The common theme here is that, in the absence of an ambient profile, we are using all labels as a proxy for the ambient effect.
This can have unpredictable consequences as the results for each label are now dependent on the behavior of the entire dataset.
For example, the metrics are susceptible to the idiosyncrasies of clustering where one cell type may be represented in multple related clusters that distort the percentages in `up.de` and `down.de` or the average log-fold change.
The metrics may also be invalidated in analyses of a subset of the data - for example, a subclustering analysis focusing on a particular cell type may mark all relevant DEGs as problematic because they are consistently DE in all subtypes.

## 5.3 Subtracting ambient counts

It is worth commenting on the seductive idea of subtracting the ambient counts from the pseudo-bulk samples.
This may seem like the most obvious approach for removing ambient contamination, but unfortunately, subtracted counts have unpredictable statistical properties due the distortion of the mean-variance relationship.
Minor relative fluctuations at very large counts become large fold-changes after subtraction, manifesting as spurious DE in genes where a substantial proportion of counts is derived from the ambient solution.
For example, several hemoglobin genes retain strong DE even after subtraction of the scaled ambient profile.

```
scaled.ambient <- controlAmbience(counts(summed.neural), ambient,
    features=is.hbb,  mode="profile")
subtracted <- counts(summed.neural) - scaled.ambient
subtracted <- round(subtracted)
subtracted[subtracted < 0] <- 0
subtracted[is.hbb,]
```

```
##         [,1] [,2] [,3] [,4]
## Hbb-bt     0    0    7   18
## Hbb-bs     1    2   31   42
## Hbb-bh2    0    0    0    0
## Hbb-bh1    2    0    0    0
## Hbb-y      0    0   39  107
## Hba-x      1    1    0    0
## Hba-a1     0    0  365  452
## Hba-a2     0    0  314  329
```

Another tempting approach is to use interaction models to implicitly subtract the ambient effect during GLM fitting.
The assumption is that, for a genuine DEG, the log-fold change within cells is larger in magnitude than that in the ambient solution.
This is based on the expectation that any DE in the latter is “diluted” by contributions from cell types where that gene is not DE.
Unfortunately, this is not always the case; a DE analysis of the ambient counts indicates that the hemoglobin log-fold change is actually stronger in the neural crest cells compared to the ambient solution, which leads to the rather awkward conclusion that the WT neural crest cells are expressing hemoglobin beyond that explained by ambient contamination.
(This is probably an artifact of how cell calling is performed.)

```
library(edgeR)
y.ambient <- DGEList(ambient, samples=colData(summed.neural))
y.ambient <- y.ambient[filterByExpr(y.ambient, group=y.ambient$samples$tomato),]
y.ambient <- calcNormFactors(y.ambient)

design <- model.matrix(~factor(block) + tomato, y.ambient$samples)
y.ambient <- estimateDisp(y.ambient, design)
fit.ambient <- glmQLFit(y.ambient, design, robust=TRUE)
res.ambient <- glmQLFTest(fit.ambient, coef=ncol(design))

summary(decideTests(res.ambient))
```

```
##        tomatoTRUE
## Down         1856
## NotSig       7783
## Up           1599
```

```
topTags(res.ambient, n=10)
```

```
## Coefficient:  tomatoTRUE 
##          logFC logCPM     F    PValue       FDR
## Hbb-y   -5.267 12.803 14999 9.908e-45 1.113e-40
## Hbb-bh1 -5.075 13.725 13232 7.494e-44 3.666e-40
## Hba-x   -4.827 13.122 13015 9.787e-44 3.666e-40
## Hba-a1  -4.662 10.734 10549 2.900e-42 8.148e-39
## Hba-a2  -4.521  9.480  7874 3.236e-40 7.274e-37
## Blvrb   -4.319  7.649  3975 1.928e-35 3.612e-32
## Car2    -3.499  8.534  3894 2.688e-35 4.316e-32
## Xist    -4.376  7.484  3843 3.323e-35 4.668e-32
## Gypa    -5.138  7.213  3779 4.352e-35 5.434e-32
## Hbb-bs  -4.941  7.209  3487 1.579e-34 1.775e-31
```

In addition, there are other issues with implicit subtraction in the fitted GLM that warrant caution with its use.
This strategy precludes detection of DEGs that are common to all cell types as there is no longer a dilution effect being applied to the log-fold change in the ambient solution.
It requires inclusion of the ambient profiles in the model, which is cause for at least some concern as they are unlikely to have the same degree of variability as the cell-derived pseudo-bulk profiles.
Interpretation is also complicated by the fact that we are only interested in log-fold changes that are more extreme in the cells compared to the ambient solution; a non-zero interaction term is not sufficient for removing spurious DE.

See also comments in [Advanced Section 7.3](http://bioconductor.org/books/3.23/OSCA.advanced/droplet-processing.html#removing-ambient-contamination) for more comments on the removal of ambient contamination, mostly for visualization purposes.

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
 [1] edgeR_4.10.0                 limma_3.68.0                
 [3] DropletUtils_1.32.0          scran_1.40.0                
 [5] scuttle_1.22.0               MouseGastrulationData_1.25.0
 [7] SpatialExperiment_1.22.0     SingleCellExperiment_1.34.0 
 [9] SummarizedExperiment_1.42.0  Biobase_2.72.0              
[11] GenomicRanges_1.64.0         Seqinfo_1.2.0               
[13] IRanges_2.46.0               S4Vectors_0.50.0            
[15] BiocGenerics_0.58.0          generics_0.1.4              
[17] MatrixGenerics_1.24.0        matrixStats_1.5.0           
[19] BiocStyle_2.40.0             rebook_1.22.0               

loaded via a namespace (and not attached):
 [1] DBI_1.3.0                 httr2_1.2.2              
 [3] CodeDepends_0.6.7         rlang_1.2.0              
 [5] magrittr_2.0.5            otel_0.2.0               
 [7] compiler_4.6.0            RSQLite_2.4.6            
 [9] DelayedMatrixStats_1.34.0 dir.expiry_1.20.0        
[11] png_0.1-9                 vctrs_0.7.3              
[13] pkgconfig_2.0.3           crayon_1.5.3             
[15] fastmap_1.2.0             dbplyr_2.5.2             
[17] magick_2.9.1              XVector_0.52.0           
[19] rmarkdown_2.31            graph_1.90.0             
[21] purrr_1.2.2               bit_4.6.0                
[23] xfun_0.57                 bluster_1.22.0           
[25] cachem_1.1.0              beachmat_2.28.0          
[27] jsonlite_2.0.0            blob_1.3.0               
[29] rhdf5filters_1.24.0       DelayedArray_0.38.0      
[31] Rhdf5lib_2.0.0            BiocParallel_1.46.0      
[33] irlba_2.3.7               parallel_4.6.0           
[35] cluster_2.1.8.2           R6_2.6.1                 
[37] bslib_0.10.0              jquerylib_0.1.4          
[39] Rcpp_1.1.1-1.1            bookdown_0.46            
[41] knitr_1.51                R.utils_2.13.0           
[43] splines_4.6.0             Matrix_1.7-5             
[45] igraph_2.3.0              tidyselect_1.2.1         
[47] abind_1.4-8               yaml_2.3.12              
[49] codetools_0.2-20          curl_7.1.0               
[51] lattice_0.22-9            tibble_3.3.1             
[53] withr_3.0.2               KEGGREST_1.52.0          
[55] BumpyMatrix_1.20.0        evaluate_1.0.5           
[57] BiocFileCache_3.2.0       ExperimentHub_3.2.0      
[59] Biostrings_2.80.0         pillar_1.11.1            
[61] BiocManager_1.30.27       filelock_1.0.3           
[63] BiocVersion_3.23.1        sparseMatrixStats_1.24.0 
[65] glue_1.8.1                metapod_1.20.0           
[67] tools_4.6.0               AnnotationHub_4.2.0      
[69] BiocNeighbors_2.6.0       ScaledMatrix_1.20.0      
[71] locfit_1.5-9.12           XML_3.99-0.23            
[73] rhdf5_2.56.0              grid_4.6.0               
[75] AnnotationDbi_1.74.0      HDF5Array_1.40.0         
[77] BiocSingular_1.28.0       cli_3.6.6                
[79] rsvd_1.0.5                rappdirs_0.3.4           
[81] S4Arrays_1.12.0           dplyr_1.2.1              
[83] R.methodsS3_1.8.2         sass_0.4.10              
[85] digest_0.6.39             SparseArray_1.12.0       
[87] dqrng_0.4.1               rjson_0.2.23             
[89] R.oo_1.27.1               memoise_2.0.1            
[91] htmltools_0.5.9           lifecycle_1.0.5          
[93] h5mread_1.4.0             httr_1.4.8               
[95] statmod_1.5.1             bit64_4.8.0
```

### References

Lun, A., S. Riesenfeld, T. Andrews, T. P. Dao, T. Gomes, participants in the 1st Human Cell Atlas Jamboree, and J. Marioni. 2019. “EmptyDrops: distinguishing cells from empty droplets in droplet-based single-cell RNA sequencing data.” *Genome Biol.* 20 (1): 63.

Pijuan-Sala, B., J. A. Griffiths, C. Guibentif, T. W. Hiscock, W. Jawaid, F. J. Calero-Nieto, C. Mulas, et al. 2019. “A Single-Cell Molecular Map of Mouse Gastrulation and Early Organogenesis.” *Nature* 566 (7745): 490–95.

Young, M. D., and S. Behjati. 2018. “SoupX Removes Ambient RNA Contamination from Droplet Based Single Cell RNA Sequencing Data.” *bioRxiv*.
