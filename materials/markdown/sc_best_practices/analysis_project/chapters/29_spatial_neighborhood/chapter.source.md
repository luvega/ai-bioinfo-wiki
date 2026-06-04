---
type: scbp-chapter-source
title: "Neighborhood analysis"
upstream_path: jupyter-book/spatial/neighborhood.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Neighborhood analysis

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
# Neighborhood analysis

(spatial-neighborhood-key-takeaway-1)=
(spatial-neighborhood-key-takeaway-2)=
## Motivation
After annotating cell types or cell states in the dataset (or spots, according to the technology at end), we can quantify whether such annotations are spatially enriched and analyze cellular neighborhoods across the tissue.

Cellular neighborhood analysis is a good starting point for various downstream tasks as it can help to understand the cellular composition of the tissue and identify candidates for more in-depth analysis. For example, it can help to find candidates for cell-cell communication based on spatial proximity, or spatial regions and clusters for identification of spatially variable genes. 

Neighborhood analysis is often performed through **spatial statistics** {cite}`gelfand2010handbook`, which are quantitative scores that can be used to identify spatial neighborhoods in the tissue. Here, we'll take a look at various spatial statistics implemented in Squidpy {cite}`Palla2022`.

<!-- markdown cell 2 -->
## Environment setup and data

We first load the respective packages needed in this tutorial and the dataset.

## Code cell 3

```python
import scanpy as sc
import squidpy as sq

sc.settings.verbosity = 3
sc.settings.set_figure_params(dpi=80, facecolor="white")
```

<!-- markdown cell 4 -->
The dataset used in this tutorial consists of 1 tissue slides from 1 mouse and is provided by [10x Genomics Space Ranger 1.1.0](https://support.10xgenomics.com/spatial-gene-expression/datasets/1.1.0/V1_Adult_Mouse_Brain). The dataset was pre-processed in Squidpy, which provides a loading function for this dataset.

## Code cell 5

```python
adata = sq.datasets.visium_hne_adata()
```

<!-- markdown cell 6 -->
## Identifying interactions between spatial communities
After annotating cell types or cell states in the dataset (or spots, according to the technology at end), we can quantify whether such annotations are spatially enriched. To this end, computing a neighborhood enrichment can help us identify clusters that are neighbors in the tissue of interest. In short, it’s an enrichment score on spatial proximity of clusters: if observations (cells or spots) belonging to a cluster are often close to observations belonging to another cluster, then they will have a high score and will appear to be enriched. On the other hand, if they are far apart, and therefore are seldom neighbors, the score will be low and they can be defined as depleted. This score is based on a permutation-based test, and you can set the number of permutations with the n_perms argument (default is 1000).

Since the function works on a spatial connectivity matrix (spatial graph), we need to compute that as well. This can be done with `squidpy.gr.spatial_neighbors()`.

## Code cell 7

```python
sq.gr.spatial_neighbors(adata)
```

<!-- markdown cell 8 -->
We can now run the neighborhood enrichment test by providing the annotation key in `adata.obs`.

## Code cell 9

```python
sq.gr.nhood_enrichment(adata, cluster_key="cluster")
```

<!-- markdown cell 10 -->
The method added `adata.uns['cluster_nhood_enrichment']` to our AnnData object.

## Code cell 11

```python
adata.uns["cluster_nhood_enrichment"]
```

<!-- markdown cell 12 -->
The added object contains two arrays. The first stored under `zscore` contains the enrichment z-score for each cell-cell interaction. The second is stored under `count` and represents the enrichment count.

<!-- markdown cell 13 -->
Finally, we’ll directly visualize the results with `squidpy.pl.nhood_enrichment()`.

## Code cell 14

```python
sq.pl.nhood_enrichment(adata, cluster_key="cluster", method="average", figsize=(5, 5))
```

<!-- markdown cell 15 -->
From the above plot, we can see that there seems to be an enrichment for clusters of the `Pyramidal_layer` and `Dentate_gyrus`. By looking at the spatial scatterplot above, we can confirm that these clusters are indeed "neighbors" as their members are often close.

<!-- markdown cell 16 -->

A similar approach to such problem is computing what we call an *interaction matrix*, that is, the sum of all connecting observations between clusters in tissue. The approach is related to the neighborhood enrichment analysis yet it is not a test, but should be viewed as a simple summary statistics of the spatial graph.
Let's take a look at how the interaction matrix looks like for the dataset.

## Code cell 17

```python
sq.gr.interaction_matrix(adata, cluster_key="cluster")
```

<!-- markdown cell 18 -->
The function added `adata.uns['cluster_interactions']` to our AnnData object, which contains the number of interactions between two clusters with respect to the provided spatial connectivities graph.

## Code cell 19

```python
adata.uns["cluster_interactions"]
```

<!-- markdown cell 20 -->
We can visualize the results with `squidpy.pl.interaction_matrix()`.

## Code cell 21

```python
sq.pl.interaction_matrix(adata, cluster_key="cluster", method="average", figsize=(5, 5))
```

<!-- markdown cell 22 -->
For the dataset, we roughly recapitulate the neighborhood enrichment test, yet we seem to not observe a particularly strong interaction between the `Pyramidal_layer` and `Dentate_gyrus` clusters. 
One explanation for such a result is that the number of observations of such clusters is low, hence the low number of interactions.

<!-- markdown cell 23 -->
## Co-occurrence across spatial dimensions

Another spatial statistic that can be computed on cell type annotations in spatial coordinates is what we call the co-occurrence score {cite}`Tosti2021,Palla2022`. The co-occurrence score gives us an indication on whether clusters co-occur with each other at increasing distances across the tissue.
The co-occurrence score is defined as:

$\frac{p(exp|cond)}{p(exp)}$

where $p(exp|cond)$ is the conditional probability of observing a cluster $exp$ conditioned
on the presence of a cluster $cond$ whereas $exp$ is the probability of observing $exp$
in the radius size of interest. The score is computed across increasing radii size around each observation (i.e. spots here) in the tissue.

## Code cell 24

```python
sq.gr.co_occurrence(adata, cluster_key="cluster")
sq.pl.co_occurrence(adata, cluster_key="cluster", clusters="Cortex_1", figsize=(8, 5))
```

<!-- markdown cell 25 -->
Here, we selected to visualize the cluster `Cortex_1` to visualize how at close distances, the cluster co-occur with the other `Cortex` clusters, as expected.

<!-- markdown cell 26 -->
## References

```{bibliography}
:filter: docname in docnames
:labelprefix: spatial
```

## Contributors
### Authors
* Giovanni Palla

### Reviewers
* Anna Schaar
* Lukas Heumos
