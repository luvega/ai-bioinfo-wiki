---
type: scbp-chapter-source
title: "Differential gene expression analysis"
upstream_path: jupyter-book/conditions/differential_gene_expression.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Differential gene expression analysis

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
(differential-analysis)=
# Differential gene expression analysis

<!-- markdown cell 2 -->
(conditions-differential-gene-expression-key-takeaway-1)=
## Motivation

<!-- markdown cell 3 -->
This chapter is a more detailed continuation of the {term}`annotation` [subchapter](https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/conditions/cellular-structure-annotation-DGE) which already introduced {term}`differential gene expression (DGE)` as a tool to annotate {term}`clusters <cluster>` with {term}`cell types <cell type>`.
Here, we focus on more advanced use-cases of differential gene expression testing in complex experimental designs, which involve one or more conditions such as diseases, genetic knockouts or drugs.
In such cases we are commonly interested in the magnitude and significance of differences in gene expression patterns between the condition of interest and a reference.
This reference can be everything but is commonly a healthy sample.
This statistical test can be applied to arbitrary groups, but in the case of single-cell {term}`RNA`-Seq is commonly applied on the cell type level.

:::{figure-md} Differential gene expression overview
<img src="../_static/images/conditions/differential_gene_expression.jpg" alt="DGE analysis overview" class="bg-primary mb-1" width="800px">

DGE analysis attempts to infer genes that are statistically significantly over- or underexpressed between any compared groups (commonly between healthy and condition per cell type).
:::

The outcome of such an analysis could be genesets which effect and potentially explain any observed phenotypes.
These genesets can then be examined more closely with respect to, for example, affected pathways or induced cell-cell communication changes.

<!-- markdown cell 4 -->
A differential gene expression test usually returns the log2 fold-change and the adjusted p-value per compared genes per compared conditions. This list can then be sorted by p-value and investigated in more detail.

<!-- markdown cell 5 -->
The popular student's t-test is one way of conducting such a test.
However, it fails to take several single-cell RNA-seq peculiarities into account such as the excess number of zeros originating from {term}`dropouts <Dropout>` or the need for complex experimental designs.
More specifically, very rarely does one have sufficient sample numbers to accurately estimate the variance without pooling information across genes.
Moreover, raw counts are never an absolute measurement of expression for a specific gene within a given sample.
The actual read number per gene depends on the efficiency of the {term}`library` preparation, the amount of contamination from non-coding transcripts and the {term}`sequencing` depth.
It does therefore lack in both, sensitivity and specificity for single-cell RNA-seq, let alone experimental design flexibility.

As a result, DGE testing is a classic bioinformatics problem which has been tackled by many tools already.
Generally, the problem is currently being approached from two views, the sample-level view where expression is aggregated to create “{term}`pseudobulks <Pseudobulk>`" and then analysed with methods originally designed for {term}`bulk expression <Bulk RNA sequencing>` samples such as edgeR {cite}`de:Robinson2010` or DEseq2 {cite}`Love2014` and the cell-level view where {term}`cells <cell>` are modeled individually using generalized mixed effect models such as MAST {cite}`Finak2015` or glmmTMB {cite}`Brooks2017`. 
The consensus and robustness across datasets for DGE tools is low {cite}`de:Wang2019, Das2021`. As previously described, although single-cell data contains technical noise artifacts such as dropout, zero-inflation and high cell-to-cell variability {cite}`Hicks2017, Vallejos2017, de:Lücken2019`, methods designed for bulk RNA-seq data performed favorably compared to methods explicitly designed for scRNA-seq data {cite}`Das2021, Soneson2018, Jaakkola2016, de:Squair2021`.
Single-cell specific methods were found to be especially prone to wrongly labeling highly expressed genes as differentially expressed.

<!-- markdown cell 6 -->
A recent study highlighted the issue of pseudoreplication where inferential statistics is applied to biological replicates which are not statistically independent.
Failing to account for the inherent correlation of replicates (cells from the same individual) inflates the false discovery rate (FDR) {cite}`de:Squair2021, Zimmerman2021, Junttila2022`.
Therefore, {term}`batch effect` correction or the aggregation of cell-type-specific expression values within an individual through either a sum, mean or random effect per individual, that is pseudobulk generation, should be applied prior to DGE analysis to account for within-sample correlations {cite}`Zimmerman2021`.
Generally, both, pseudobulk methods with sum aggregation such as edgeR, DESeq2, or Limma {cite}`Ritchie2015` and mixed models such as MAST with random effect setting were found to be superior compared to naive methods, such as the popular Wilcoxon rank-sum test or Seurat’s {cite}`de:Hao2021` latent models, which do not account for them {cite}`Junttila2022`.

In matters arising from the Zimmerman paper, Murphy et al. critically examined the Zimmerman {term}`benchmarking <Benchmark>` strategy and improved it {cite}`Murphy_2022`.
They came to the conclusion that pseudobulk methods perform best but whether sum or mean aggregation works better requires further investigation.

<!-- markdown cell 7 -->
Hence, in this notebook, we demonstrate how to perform DGE analysis using the pseudobulk approach.
We choose DESeq2 due to its Python implementation, PyDESeq2.
However, the code can be easily adapted for use with edgeR by following the [pertpy tutorial on differential gene expression](https://pertpy.readthedocs.io/en/stable/tutorials/notebooks/differential_gene_expression.html#differential-expression-testing-with-edger).
For this chapter, we combined parts of the tutorials from [decoupler](https://decoupler.readthedocs.io/en/latest/notebooks/scell/rna_psbk.html) and [pertpy](https://pertpy.readthedocs.io/en/stable/tutorials/notebooks/differential_gene_expression.html).
Please refer to their documentation for more details.

<!-- markdown cell 8 -->
## Environment setup

## Code cell 9

```python
import warnings

warnings.filterwarnings("ignore")
```

## Code cell 10

```python
import decoupler as dc
import lamindb as ln
import numpy as np
import pandas as pd
import pertpy as pt
import scanpy as sc

ln.track()
```

<!-- markdown cell 11 -->
## Preparing the dataset

<!-- markdown cell 12 -->
We will use the Kang dataset, which is a 10x droplet-based scRNA-seq peripheral blood mononuclear cell (PBMC) data from 8 Lupus patients before and after 6h-treatment with INF-β (16 samples in total) {cite}`de:kang2018`.
Interferon beta is used in the form of natural fibroblast or recombinant preparations (interferon beta-1a and interferon beta-1b) and exerts antiviral and antiproliferative properties similar to those of interferon alpha.
Interferon beta has been approved for the treatment of relapsing–remitting multiple sclerosis and secondary progressive multiple sclerosis.

<!-- markdown cell 13 -->
First, we load the full dataset.

## Code cell 14

```python
adata = ln.Artifact.get(
    key="conditions/differential_gene_expression.h5ad",
).load()
adata
```

<!-- markdown cell 15 -->
We will need `label` (which contains the condition label), `replicate` (patient id) and `cell_type` columns of the `.obs`.

## Code cell 16

```python
adata.obs[:5]
```

<!-- markdown cell 17 -->
We will need to work with raw counts so we check that `.X` indeed contains raw counts and put them into the `counts` layer of our {term}`AnnData` object.

## Code cell 18

```python
X = adata.X.data
np.array_equal(X, np.round(X))
```

## Code cell 19

```python
adata.layers["counts"] = adata.X.copy()
```

<!-- markdown cell 20 -->
We have 8 control and 8 disease patients.

## Code cell 21

```python
print(len(adata[adata.obs["label"] == "ctrl"].obs["replicate"].cat.categories))
print(len(adata[adata.obs["label"] == "stim"].obs["replicate"].cat.categories))
```

<!-- markdown cell 22 -->
We filter cells which have less than 200 genes and genes which were found in less than 3 cells for a rudimentary quality control.

## Code cell 23

```python
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
adata.shape
```

<!-- markdown cell 24 -->
(conditions-differential-gene-expression-key-takeaway-2)=
## Pseudobulking

<!-- markdown cell 25 -->
Since PyDESeq2 was introduced as a method for DGE analysis for bulk data, we first need to create pseudobulk samples from our single-cell dataset.
For each patient we create one pseudobulk sample per cell type by aggregating the cells from each subpopulation and taking the sum of gene expression counts.
Regardless of whether we want to run the analysis only on a few cell subpopulations and fit a model for each one of them separately or fit one model for all of them, we first need to prepare the data.

Since we need to create pseudobulks for each patient-condition combination, we first need to create such a column by concatenating `replicate` and `label`.

## Code cell 26

```python
adata.obs["sample"] = pd.Categorical(
    f"{rep}_{l}" for rep, l in zip(
        adata.obs["replicate"],
        adata.obs["label"],
        strict=False
    )
)
```

<!-- markdown cell 27 -->
Next, we generate pseudobulk samples using decoupler. With 8 patients, 8 cell types, and 2 conditions (`ctrl` and `stim`), this yields a total of 128 pseudobulks (8 x 8 x 2).

## Code cell 28

```python
adata_pb = dc.pp.pseudobulk(
    adata, sample_col="sample",
    groups_col="cell_type",
    layer="counts",
    mode="sum"
)
adata_pb
```

<!-- markdown cell 29 -->
Low-quality samples can be filtered using two criteria: the number of cells (`psbulk_cells`) and the total count sum (`psbulk_counts`). 
These metrics can be visualized in the following plot to guide filtering decisions.

## Code cell 30

```python
dc.pl.filter_samples(
    adata=adata_pb,
    groupby=["label", "cell_type", "replicate"],
    min_cells=10,
    min_counts=1000,
    figsize=(5, 8),
)
```

<!-- markdown cell 31 -->
While thresholds are dataset-specific and arbitrary, a commonly used guideline is to retain samples with a minimum of 10 cells and 1,000 total counts. 
Applying these thresholds (indicated by dashed lines) restricts the dataset to pseudobulks in the upper-right quadrant. 
The filtering step can be carried out with `decoupler.pp.filter_samples()`.

## Code cell 32

```python
dc.pp.filter_samples(adata_pb, min_cells=10,min_counts=1000)
```

<!-- markdown cell 33 -->
After filtering out low-quality samples, we can visualize the remaining profiles. 
All megakaryocyte pseudobulk samples failed quality control, and two CD8 T cell samples were removed.

## Code cell 34

```python
dc.pl.obsbar(adata=adata_pb, y="cell_type", hue="label", figsize=(6, 3))
```

<!-- markdown cell 35 -->
(conditions-differential-gene-expression-key-takeaway-3)=
## Variability Exploration

<!-- markdown cell 36 -->
The validity of DGE results highly depends on the capture of the major axis of variations in the statistical model.
Intermediate data exploration steps such as {term}`principal component analysis (PCA)` or multidimensional scaling (MDS) on pseudobulk samples allow for the identification of the sources of variation and thus can guide the construction of corresponding design and contrast matrices that model the data {cite}`Law2020`. 

Failing to account for multiple sources of biological variability for experiments which include biological replicates will inflate the FDR {cite}`Thurman2021, Lähnemann2020`.
While increasing the number of cells per individual increases the precision, it has a limited effect on the power for the detection of differences across individuals.
Therefore, the best way to increase statistical power is to increase the number of independent experimental samples {cite}`Zimmerman2021`.

Since our data has already been generated, we cannot further increase the number of independent experimental samples.
Nevertheless, we will now explore our data to determine the major axes of variation to properly generate our design matrices.

<!-- markdown cell 37 -->
We perform very basic exploratory data analysis on the generated pseudo-replicates to identify potential outliers among patients or pseudobulks.
These outliers can then be excluded to avoid biasing the differential expression results.
We store the raw counts in the `'counts'` layer, then normalize and scale them before computing PCA. 
Afterwards, we revert to the raw counts for {term}`downstream analysis`.

## Code cell 38

```python
adata_pb.layers['counts'] = adata_pb.X.copy()

sc.pp.normalize_total(adata_pb, target_sum=1e6)
sc.pp.log1p(adata_pb)
sc.pp.scale(adata_pb, max_value=10)
sc.tl.pca(adata_pb)

dc.pp.swap_layer(adata=adata_pb, key="counts", inplace=True)
```

<!-- markdown cell 39 -->
We also include `psbulk_counts_log` and `psbulk_cells_log` because taking the log makes library sizes (`psbulk_counts` and `psbulk_cells`) less skewed and allows more reliable detection of correlations with principal components.

## Code cell 40

```python
adata_pb.obs["psbulk_counts_log"] = np.log(adata_pb.obs["psbulk_counts"])
adata_pb.obs["psbulk_cells_log"] = np.log(adata_pb.obs["psbulk_cells"])
```

## Code cell 41

```python
dc.tl.rankby_obsm(adata_pb, key="X_pca")
sc.pl.pca_variance_ratio(adata_pb)
dc.pl.obsm(
    adata=adata_pb,
    return_fig=True,
    nvar=5,
    titles=["PC scores", "Adjusted p-values"],
    figsize=(10, 5)
)
```

<!-- markdown cell 42 -->
In this dataset, PC1 appears to explain the largest proportion of variance because it shows the highest variance ratio of around 0.13.
It is associated with the metadata variables cell type and pseudobulk cells.
Metadata variables associated with PCs that capture a substantial amount of variance are important and should be accounted for as relevant covariates (e.g., include in the design matrix) in downstream differential expression analysis when possible.
The principal components can also be directly visualized, colored by these metadata variables.

## Code cell 43

```python
adata_pb.obs = adata_pb.obs.sort_index(axis=1)
sc.pl.pca(adata_pb, color=adata_pb.obs, ncols=2, size=300)
```

<!-- markdown cell 44 -->
We observe separation of cell types on the PCA plots as well as the separation into stimulated and unstimulated cells.
For pseudobulk cells and counts, we can also observe some clustering, with high values appearing in the top left and top right regions.
Looking more closely, we see that these clusters of high values partially overlap with specific cell type clusters: the top right cluster overlaps with CD4 T cells, while the top left cluster overlaps with CD14+ monocytes.
This suggests that the number of cells and counts assigned to a pseudospot may depend on the pseudospot's cell type.
The covariates replicate and sample do not seem to be clearly correlated with the PCA components so we do not include any of them in our design matrix.

<!-- markdown cell 45 -->
## One cell type or group
If you already know which cell types to focus on, subset them at this step to reduce confounding factors.
Otherwise, you can first [analyze the full dataset](#multiple-cell-types-or-groups) to identify the most affected cell types, then return to this step.

If variability exploration showed that cell types are associated with PCs, it may help to rerun it on your cell type subsets to see if covariate effects disappear.
In our case, the association with pseudobulk cells disappears in CD14+ monocytes.
That's why we won't include it into our first design matrix.

<!-- markdown cell 46 -->
(conditions-differential-gene-expression-key-takeaway-4)=
### Feature selection

In addition to filtering low-quality samples, lowly or noisily expressed genes can also be filtered prior to DGE analysis.
This step should be performed at the cell type level, as different cell types may express distinct sets of genes.
We run the {term}`pipeline` on CD14+ monocytes subset of the data, as it was shown in the paper that the highest number of differentially expressed genes was identified in this subpopulation.

## Code cell 47

```python
adata_mono = adata_pb[adata_pb.obs["cell_type"] == "CD14+ Monocytes"].copy()
adata_mono.shape
```

<!-- markdown cell 48 -->
Two strategies are used to filter genes:

1. `decoupler.pp.filter_by_expr`: Retains genes with a minimum total number of reads across all samples (`min_total_count`) and a minimum number of counts in a given number of samples (`min_count`). 
This approach was introduced in [edgeR](https://rdrr.io/bioc/edgeR/man/filterByExpr.html) {cite}`de:Robinson2010`.
2. `decoupler.pp.filter_by_prop`: Retains genes that are expressed in at least a specified proportion of cells (`min_prop`) across a minimum number of samples (`min_smpls`).
The number of retained genes can be visualized, and the filtering parameters can be adjusted interactively.

## Code cell 49

```python
dc.pl.filter_by_expr(
    adata=adata_mono,
    group="label",
    min_count=10,
    min_total_count=15,
    large_n=10,
    min_prop=0.7,
)
dc.pl.filter_by_prop(
    adata=adata_mono,
    min_prop=0.1,
    min_smpls=2,
)
```

<!-- markdown cell 50 -->
The top plot displays gene frequencies based on the `filter_by_expr` metrics, while the bottom plot corresponds to `filter_by_prop`.
Dashed lines indicate the current threshold values.
In the top plot, only genes in the upper-right quadrant are retained, in the bottom plot, only those to the right of the vertical line are kept.

Although filtering thresholds are arbitrary, a common heuristic is to look for bimodal distributions and set thresholds that separate low-quality genes from the rest.
In this example, the default parameters retain a substantial number of genes while removing potentially noisy ones.

Once the threshold parameters are set, the actual gene filtering can be performed by simply changing `pl` to `pp`.

## Code cell 51

```python
dc.pp.filter_by_expr(
    adata=adata_mono,
    group="label",
    min_count=10,
    min_total_count=15,
    large_n=10,
    min_prop=0.7,
)
dc.pp.filter_by_prop(
    adata=adata_mono,
    min_prop=0.1,
    min_smpls=2,
)
adata_mono.shape
```

<!-- markdown cell 52 -->
### Differential expression testing with PyDESeq2
We now switch to the pertpy package, as it makes it easier to use its built-in plotting functions.
However, DGE analysis can also be performed manually using PyDESeq2.
The interface of PyDESeq2 in pertpy is very similar.

At the next step, it is important to define an appropriate design matrix for the model.
For this purpose, we strongly recommend reading [this guide](https://f1000research.com/articles/9-1444), which provides a helpful introduction to design matrices.

(design-syntax)=
```{admonition} Understand the design syntax
:class: tip, dropdown
We combine all the variables we would like to include in our model with a `+`. 
The variable names correspond to the column names ins `.obs`.
Interactions between variables can be added to the model with `:`.
For example, the model `y ~ a + b + a:b` includes the effect of `a` and `b` on `y` as well as how the effect of `a` on `y` changes depending on `b` and vice versa.
In our context, `y` is the observed gene expression and `a` and `b` could be `label` and `cell_type`.
Now it also becomes clear where the `~` comes from: It separates the two sides of a formula.
So just add `~` at the beginning of your design.
Besides that, it might be useful to know that `a * b` is shorthand for `a + b + a:b`.
In most cases, this is all you need.
For a deeper dive, we recommend reading the [formulaic](https://matthew.wardrop.casa/formulaic/latest/formulas/) and [patsy](https://patsy.readthedocs.io/en/latest/formulas.html) documentation.
```

## Code cell 53

```python
pds2 = pt.tl.PyDESeq2(adata=adata_mono,design='~ label')
```

## Code cell 54

```python
pds2.fit()
```

## Code cell 55

```python
res_df = pds2.test_contrasts(pds2.contrast(
    column="label",
    baseline="ctrl",
    group_to_compare="stim")
)
```

## Code cell 56

```python
res_df.head(10)
```

<!-- markdown cell 57 -->
Let’s take a look at the columns in the [results table](https://hbctraining.github.io/DGE_workshop_salmon/lessons/05_DGE_DESeq2_analysis2.html#:~:text=Results%20exploration):
- `variable`. gene name
- `baseMean`: mean of normalized counts for all samples
- `log_fc`: log2 fold change
- `lfcSE`: standard error
- `stat`: Wald statistic
- `p_value`: Wald test p-value
- `adj_p_value`: Benjamini-Hochberg adjusted p-values

The rows are sorted by `adj_p_value`.
The `log_fc` always depends on the defined baseline. A positive `log_fc` means gene expression is higher in the group of interest compared to the baseline group, while negative values indicate lower expression.
In this case, _IFITM2_ increased by around 4.7 in stimulated compared to control CD14+ monocytes.
In contrast, _VCAN_ decreased by around 4.4 (see the plot below).

Next, we visualize the results.

## Code cell 58

```python
pds2.plot_volcano(res_df, log2fc_thresh=0)
```

<!-- markdown cell 59 -->
The higher a point is on the y-axis, the smaller the `adj_p_value`.
The further a point is from 0 on the x-axis, the larger the change in expression.
Overall, this means that genes in the upper left and upper right regions of the plot show the strongest changes in gene expression and, at the same time, are also the least likely to have changes that occurred by chance.

We can also visualize our results for different subgroups.
In this case, we plot the results for individual patients.

## Code cell 60

```python
pds2.plot_paired(
    adata_mono,
    results_df=res_df,
    n_top_vars=4,
    groupby="label",
    pairedby="replicate"
)
```

<!-- markdown cell 61 -->
We can see that the CD14+ monocytes from patient 1015 appear to be highly responsive to the treatment.

<!-- markdown cell 62 -->
(conditions-differential-gene-expression-key-takeaway-5)=
## Multiple cell types or groups

<!-- markdown cell 63 -->
If you’re unsure which cell type will be most affected by a treatment, a good starting point is to fit a model to the entire dataset.
Afterwards, you can return to the analysis steps from the [first part of this chapter](#one-cell-type-or-group) and focus on the cell type of interest.

In addition, the following steps demonstrate how to handle analyses involving multiple groups within the data.
You may already know which cell type you want to examine more closely, but your dataset might include multiple groups (e.g., sex, responder vs. non-responder status or age groups).
Then, this section provides an initial glimpse of the types of questions you can explore for a single cell type across multiple groups.

Since we do not have particularly interesting subgroups within our CD14+ monocyte subset (`adata_mono`), we will instead analyze multiple cell types together.
Because this analysis includes several cell types simultaneously, we will skip the feature selection step at this stage.
Feature selection is better performed at the level of individual cell types, as different cell types can express distinct gene sets.

We will begin by constructing a simple [design matrix](https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/conditions/design-syntax).

## Code cell 64

```python
pds2 = pt.tl.PyDESeq2(adata=adata_pb, design="~ label")
```

## Code cell 65

```python
pds2.fit()
```

## Code cell 66

```python
res_df = pds2.compare_groups(
    adata_pb,
    column="label",
    baseline="ctrl",
    groups_to_compare=["stim"]
)
```

## Code cell 67

```python
pds2.plot_paired(
    adata_pb,
    results_df=res_df,
    n_top_vars=4,
    groupby="label",
    pairedby="cell_type"
)
```

<!-- markdown cell 68 -->
We can see that the top four differentially expressed genes show their strongest expression changes not only in CD14+ monocytes but also in CD4 T cells.

Now we could ask: Is the gene expression difference between `ctrl` and `stim` different between CD14+ Monocytes and CD4 T cells?
In other words, could the gene expression changes depend on the cell type?

To do so, we create a more complex [desgin matrix](https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/conditions/design-syntax) and then use contrasts to specify the conditions of interest.

## Code cell 69

```python
pds2 = pt.tl.PyDESeq2(adata=adata_pb, design="~ cell_type * label")
```

## Code cell 70

```python
pds2.fit()
```

## Code cell 71

```python
interaction_contrast = (
    pds2.cond(cell_type="CD14+ Monocytes", label="stim") -
    pds2.cond(cell_type="CD14+ Monocytes", label="ctrl")
) - (
    pds2.cond(cell_type="CD4 T cells", label="stim") -
    pds2.cond(cell_type="CD4 T cells", label="ctrl")
)

res_df = pds2.test_contrasts(interaction_contrast)
```

## Code cell 72

```python
pds2.plot_volcano(res_df, log2fc_thresh=0)
```

<!-- markdown cell 73 -->
As we can see, there are some genes that stand out in their differences in gene expression changes.
For example, the change in expression of _RABGAP1L_ is higher in CD14+ monocytes compared to CD4 T cells, while _ENO1_ shows a lower change.

We can also plot the fold changes of the top differentially expressed genes.
However, we only include results that pass a certain alpha threshold, for example 0.01.

## Code cell 74

```python
pds2.plot_fold_change(res_df[res_df["adj_p_value"] < 0.01].copy(), n_top_vars=15)
```

<!-- markdown cell 75 -->
Finally, we can also plot multiple comparisons.
In this case, we are comparing the gene expression of CD14+ monocytes to all other cell types.
Comparing cell types with each other should roughly reflect the marker genes used during annotation.
This therefore mainly shows what is possible and should ideally be replaced by your groups of interest (e.g., sex, responder vs. non-responder status or age groups).

## Code cell 76

```python
res_df = pds2.compare_groups(adata_pb,
    column="cell_type",
    baseline="CD14+ Monocytes",
    groups_to_compare=list(set(adata_pb.obs["cell_type"].unique()) - {"CD14+ Monocytes"})
)
```

## Code cell 77

```python
pds2.plot_multicomparison_fc(res_df, n_top_vars=5, figsize=(12, 1.5))
```

<!-- markdown cell 78 -->
The plot shows genes that are differentially expressed in all other cell types compared to CD14+ monocytes.
For example, _CLL2_ and _CCL7_ are significantly less expressed in all other cell types compared to CD14+ monocytes.

<!-- markdown cell 79 -->
## Questions

<!-- markdown cell 80 -->
### Flipcards

## Code cell 81

```python
%run ../src/lib.py

flip_card("q1", "What is differential gene expression and in which cases are we interested in testing for it?", "DGE analysis identifies genes with significant expression differences between conditions, such as healthy versus diseased states, to elucidate underlying biological mechanisms.", back_font_size=13)
flip_card("q2", "What is the 'pseudoreplication' problem and how can it be circumvented?", "In single-cell RNA sequencing, treating individual cells from the same subject as independent samples can inflate false discovery rates. This issue can be mitigated by aggregating data into 'pseudobulks' per subject or modeling subjects as random effects.", back_font_size=13)
flip_card("q3", "What is the 'multiple testing' problem and how can it be eluded?", "Testing thousands of genes simultaneously increases the likelihood of false positives. To address this, corrections like the Benjamini-Hochberg procedure are applied to control the false discovery rate.", back_font_size=15)
```

<!-- markdown cell 82 -->
### Multiple choice questions

## Code cell 83

```python
%run ../src/lib.py

multiple_choice_question(
    "q4",
    "What does a positive log2 fold change indicate in DESeq2 results?",
    [
        "The gene is expressed equally in both groups",
        "The gene is more expressed in the baseline group",
        "The gene is more expressed in the group of interest compared to baseline",
        "The gene was filtered out during preprocessing",
    ],
    "The gene is more expressed in the group of interest compared to baseline",
    {},
)

multiple_choice_question(
    "q6",
    "What is the purpose of PCA on pseudobulk samples before DGE testing?",
    [
        "To normalize gene expression counts",
        "To identify sources of variation that should be captured in the design matrix",
        "To cluster cells into subtypes",
        "To remove batch effects automatically",
    ],
    "To identify sources of variation that should be captured in the design matrix",
    {},
)

multiple_choice_question(
    "q8",
    "What does an interaction term like `cell_type:label` in a design matrix allow you to test?",
    [
        "Whether cell types differ in total read counts",
        "Whether the effect of treatment differs across cell types",
        "Whether replicates are correlated within patients",
        "Whether batch effects are present in the data",
    ],
    "Whether the effect of treatment differs across cell types",
    {},
)
```

<!-- markdown cell 84 -->
## References

<!-- markdown cell 85 -->
```{bibliography}
:filter: docname in docnames
:labelprefix: de
```

<!-- markdown cell 86 -->
## Contributors

We gratefully acknowledge the contributions of:

### Authors

* Lukas Heumos
* Anastasia Litinetskaya
* Soroor Hediyeh-Zadeh
* Luis Heinzlmeier

### Reviewers
