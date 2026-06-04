---
type: scbp-chapter-source
title: "Spatially variable genes"
upstream_path: jupyter-book/spatial/spatially_variable_genes.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Spatially variable genes

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
# Spatially variable genes

(spatial-spatially-variable-genes-key-takeaway-1)=
(spatial-spatially-variable-genes-key-takeaway-2)=
(spatial-spatially-variable-genes-key-takeaway-3)=
## Motivation

One main analysis step for single-cell data is to identify highly-variable genes (HVGs) and perform feature selection to reduce the dimensionality of the dataset. HVGs are genes which show significantly different expression profiles between cells or distinct groups. Methods designed for this task, however, neglect the spatial context of cells and can therefore not identify spatial variation. A gene might for example be highly variable, but not show a distinct spatial pattern and is therefore not spatially variable. 

:::{figure-md} svg

<img src="../_static/images/spatial/svg.jpeg" alt="Difference highly variable gene versus spatially variable gene" class="bg-primary mb-1" width="800px">

Spatially variable genes are genes that show a distinct spatial pattern, whereas highly variable genes reflect genes that differ significantly between cells or groups of cells. 
:::

<!-- markdown cell 2 -->
Spatial variation can be caused by differences in cell-type composition, overall functional dependencies or cell-cell communication events and help to understand the underlying tissue biology. Methods designed to identify spatially variable genes (SVGs) are designed to quantify whether a gene shows a significant spatial pattern by typically decomposing spatial and non-spatial variation in the dataset {cite}`walker_deciphering_2022`. 

Several methods have been proposed for this task with varying complexity and different assumptions. Currently there is no consensus on which method works best and how to define spatial variability in general. SpatialDE {cite}`svensson_spatialde_2018`, SpatialDE2 {cite}`kats_spatialde2_2021` and SPARK{cite}`zhu_spark-x_2021` {cite}`sun_statistical_2020` use spatial correlation testing, Sepal{cite}`andersson_sepal_2021` leverages a Gaussian diffusion on spatial expression, scGCO{cite}`zhang_identification_2022` utilizes a graph cut method and SpaGCN {cite}`Hu2021-SpaGCN` identifies SVGs based on spatial domains identified through a graph convolutional neural network.

In this notebook we provide a pedagogical example using Squidpy {cite}`Palla2022` and its implementation of Moran's I to find SVGs and subsequently an example workflow for SpatialDE.

<!-- markdown cell 3 -->
## Environment setup and data

We first load the respective packages needed in this tutorial and the dataset.

## Code cell 4

```python
import NaiveDE
import scanpy as sc
import SpatialDE
import squidpy as sq

sc.settings.verbosity = 3
sc.settings.set_figure_params(dpi=80, facecolor="white")
```

<!-- markdown cell 5 -->
The dataset used in this tutorial consists of 1 tissue slides from 1 mouse and is provided by [10x Genomics Space Ranger 1.1.0](https://support.10xgenomics.com/spatial-gene-expression/datasets/1.1.0/V1_Adult_Mouse_Brain). The dataset was pre-processed in Squidpy, which provides a loading function for this dataset.

## Code cell 6

```python
adata = sq.datasets.visium_hne_adata()
```

<!-- markdown cell 7 -->
## Moran's I score in Squidpy

One approach for the identification of spatially variable genes is the Moran's I score, a measure of spatial autocorrelation (correlation of signal, such as gene expression, in observations close in space).

It is defined as:
$I = \frac{n}{W}\frac{{\mathop {\sum }\nolimits_{i = 1}^n \mathop {\sum }\nolimits_{j = 1}^n w_{i,j}z_iz_j}}{{\mathop {\sum }\nolimits_{i = 1}^n z_i^2}}$
where 
- $z_{i}$ is the deviation of the feature from the mean $\left( {x_i - \bar X} \right)$
- $w_{i,j}$ is the spatial weight between observations
- $n$ is the number of spatial units
- $W$ is the sum of all $w_{i,j}$

It can be computed with Squidpy with 1 line. For the purpose of the example, we will compute it only for a few genes.

## Code cell 8

```python
sq.gr.spatial_neighbors(adata)
sq.gr.spatial_autocorr(adata, mode="moran", genes=adata.var_names)
```

<!-- markdown cell 9 -->
The method adds a dataframe to `adata.uns` under the key `moranI`. We can inspect the result now:

## Code cell 10

```python
adata.uns["moranI"].head()
```

<!-- markdown cell 11 -->
The Squidpy implementation of Moran's I computed for every gene 

* `I` so the Moran’s I,

* `pval_norm` a p-value under normality assumption.

* `var_norm` the variance of the Moran's I under normality assumption.

* `{p_val}_{corr_method}` the corrected p-values.

<!-- markdown cell 12 -->
Let us look at two of the identified and significant genes, for example *Nrgn* and *Ttr* with corrected p-values of 0.0.

## Code cell 13

```python
sq.pl.spatial_scatter(adata, color=["Nrgn", "Ttr"])
```

<!-- markdown cell 14 -->
We can see that the expression of both of these genes seems to show a distinct localization in the tissue. It should be noted that they might (or might not) be also marker genes for specific cell clusters. One interpretation of spatially variable genes identification is that it is an orthogonal way to perform feature selection, by selecting genes that show a variability in space (instead of, for instance, across observations, as it is usually done).

<!-- markdown cell 15 -->

## SpatialDE

SpatialDE identifies spatially variable genes through Gaussian process regression. The spatial method decomposes each gene's expression variability into a spatial and nonspatial component. It then computes the ratio between the spatial and nonspatial variance term to quantify the overall spatial variance present in the dataset. In order to identify significant spatially variable genes, SpatialDE compares the full model that has access to the spatial component to a model without this term.

We are using the same dataset as we did for computing Moran's I. As SpatialDE requires the counts table saved as a DataFrame with unique variable names, we first make all variable names unique with the help of the respective Scanpy function.

## Code cell 16

```python
adata.var_names_make_unique()
```

<!-- markdown cell 17 -->
Next, we collect the raw count table with all barcode names and variable names saved as dataframe indexes and columns. Scanpy provides an efficient function for this, `get.obs_df` which collects the respective keys stored in `adata`.

## Code cell 18

```python
counts = sc.get.obs_df(adata, keys=list(adata.var_names), use_raw=True)
```

<!-- markdown cell 19 -->
SpatialDE additionally requires the total counts and the spatial coordinates in the form of a DataFrame. We can use the same Scanpy function of collecting these items as before.

## Code cell 20

```python
total_counts = sc.get.obs_df(adata, keys=["total_counts"])
```

<!-- markdown cell 21 -->
SpatialDE assumes a normally distributed noise. Since we just extracted raw counts, which empirically follow a negative binomial distribution, the counts data first needs to be transformed to a normal distributed noise. For this purpose SpatialDE uses a technique based on Anscombe:

## Code cell 22

```python
norm_expr = NaiveDE.stabilize(counts.T).T
```

<!-- markdown cell 23 -->
The transformed data still might include a varying library size across the spatial samples which can introduce a bias in the gene expression. SpatialDE recommends to account for this before actually performing the spatial test and regressing it out with the provided function:

## Code cell 24

```python
resid_expr = NaiveDE.regress_out(total_counts, norm_expr.T, "np.log(total_counts)").T
```

<!-- markdown cell 25 -->
We can now run the actual spatial test by passing the spatial coordinates and the normalized counts to SpatialDE. On the dataset, we are using here SpatialDE takes roughly 15 minutes when running it on all genes.

## Code cell 26

```python
results = SpatialDE.run(adata.obsm["spatial"], resid_expr)
```

<!-- markdown cell 27 -->
We can now inspect the result:

## Code cell 28

```python
results.head()
```

<!-- markdown cell 29 -->
The resulting DataFrame contains the following important columns:

* `g`, the gene name
* `l`, a parameter indicating the genes distance scale a gene changes expression over
* `pval`, the p-value for spatial {term}`differential expression <Differential gene expression (DGE)>`
* `qval`, the corrected p-value after correcting for multiple testing

We can now sort the result based on the corrected p-values (`qval`) and to better read the DataFrame, subset the table to only show `g`, `l` and `qval`. We will additionally save the object as `top10` to conveniently use it for downstream plotting.

## Code cell 30

```python
top10 = results.sort_values("qval").head(10)[["g", "l", "qval"]]
top10
```

<!-- markdown cell 31 -->
We can now plot the top-three significant genes and inspect their spatial pattern. We additionally plot the clusters of the dataset to analyze whether the detected genes might be linked to specific clusters.

## Code cell 32

```python
sq.pl.spatial_scatter(adata, color=list(top10["g"][:3]) + ["cluster"])
```

<!-- markdown cell 33 -->
As we can observe, all three genes show spatial patterns. *Esrra* does not seem to be associated with a specific cluster, but shows a spatial pattern in primarily the cortex layers, the thalamus and hypothalamus. *Fbxo31* and *Jph3* are primarily expressed in the pyramidal layer.

<!-- markdown cell 34 -->
## References

```{bibliography}
:filter: docname in docnames
:labelprefix: spatial
```

## Contributors
### Authors
* Giovanni Palla
* Anna Schaar

### Reviewers
* Lukas Heumos
