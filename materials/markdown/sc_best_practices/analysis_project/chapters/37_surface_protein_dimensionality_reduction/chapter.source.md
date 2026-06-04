---
type: scbp-chapter-source
title: "Dimensionality Reduction"
upstream_path: jupyter-book/surface_protein/dimensionality_reduction.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Dimensionality Reduction

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
(surface-protein-dimensionality-reduction)=
# Dimensionality Reduction

<!-- markdown cell 2 -->
(surface-protein-dimensionality-reduction-key-takeaway-1)=
## Motivation

<!-- markdown cell 3 -->
Feature matrices of surface protein markers are hard to grasp for humans as raw tables.
Therefore, we resort to low dimensional embeddings that allow us to visualize the ADTs in commonly two dimensions.
The approaches that we use and recommend for ADT data do not differ from the ones for transcriptomics data.
All aforementioned limitations of visualizations obtained through methods like t-SNE and UMAP also apply to ADT data.

ADT data generally does not require any sophisticated feature selection, because features have already been selected a *priori* during experimental design.
All selected ADTs should correspond to biologically relevant features.
Nevertheless, large datasets may benefit from PCA to reduce the dataset from several hundred features to a few principal components.
This is especially advisable if computational resources are limited.

In this and the following two chapters, we decided to focus on the ADT data and do not use the RNA data of the study. 
In the {ref}`multimodal-integration-paired-integration` chapter, we will explore how we can make use of both modalities jointly, which allows for a more detailed cell type annotation.

<!-- markdown cell 4 -->
## Environment setup

## Code cell 5

```python
import warnings

import muon as mu
import scanpy as sc

warnings.filterwarnings("ignore")
mu.set_options(pull_on_update=False)
sc.settings.verbosity = 0
sc.set_figure_params(
    dpi=80,
    facecolor="white",
    frameon=False,
)

import lamindb as ln

ln.track()
```

<!-- markdown cell 6 -->
## Loading the data

<!-- markdown cell 7 -->
We load the MuData object we saved at the end of the previous chapter {ref}`surface-protein-doublet-detection`:

## Code cell 8

```python
af = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="surface-protein/cite_doublet_detection.h5mu", is_latest=True
)
mdata = af.load()
mdata
```

<!-- markdown cell 9 -->
We remove the counts layer containing the raw data since we do not need it anymore.

## Code cell 10

```python
del mdata["prot"].layers["counts"]
```

<!-- markdown cell 11 -->
Isotype controls do not contain any biological information since their only purpose is to use them for dsb normalization, see the {ref}`surface-protein-normalization` section. 
We can therefore remove them from our data.

## Code cell 12

```python
mdata["prot"].var.index[:50]
```

## Code cell 13

```python
isotype_controls = ["Mouse-IgG1", "Mouse-IgG2a", "Mouse-IgG2b", "Rat-IgG2b"]
temp = (
    mdata["prot"].var.loc[~mdata["prot"].var.index.isin(isotype_controls), :].index
)  # Select all proteins except isotype controls.
```

<!-- markdown cell 14 -->
Now we actually remove isotype controls from the data.

## Code cell 15

```python
mu.pp.filter_var(data=mdata["prot"], var=temp.tolist())
```

<!-- markdown cell 16 -->
The data does not contain the isotype controls anymore.

## Code cell 17

```python
mdata["prot"].var.index[:50]
```

## Code cell 18

```python
mdata["prot"]
```

<!-- markdown cell 19 -->
## PCA and UMAP

<!-- markdown cell 20 -->
We can now reduce the dimensionality of the data with PCA since our dataset is quite big (136 surface proteins).

## Code cell 21

```python
sc.pp.pca(mdata["prot"], svd_solver="arpack", random_state=0)
```

<!-- markdown cell 22 -->
We create an elbow plot in order to decide how many PCs we use:

## Code cell 23

```python
sc.pl.pca_variance_ratio(mdata["prot"], n_pcs=50)
```

<!-- markdown cell 24 -->
We use 20 PCs because PCs 1-20 capture much of the variance in the data and PCs 20-50 capture little variance of the data and can thus be discarded. 
We now compute a neighborhood graph and a UMAP embedding to visualize the study's variables.

## Code cell 25

```python
sc.pp.neighbors(mdata["prot"], n_pcs=20, random_state=0)
```

## Code cell 26

```python
sc.tl.umap(mdata["prot"], random_state=0)
```

<!-- markdown cell 27 -->
Now we have our data compressed into 2 dimensions, which we can use to visualize the data.
Let's first visualize and evaluate if there are batch effects, that is, if different donors and different batches form separate clusters.

## Code cell 28

```python
sc.pl.umap(mdata["prot"], color=["donor", "batch"])
```

<!-- markdown cell 29 -->
We indeed see that some donors form separate clusters. 
Also batches form separate clusters. 
Thus, it seems that batch correction is necessary. 
To confirm, we plot markers of CD4 and CD8 T cells:

## Code cell 30

```python
sc.pl.umap(mdata["prot"], color=["CD4-1", "CD8", "CD3"])
```

<!-- markdown cell 31 -->
CD4 T cells fragment into donor-specific mini-clusters, meaning cells are grouping by donor identity rather than cell type. 
Ideally, CD4 T cells from all donors should cluster together regardless of their donor of origin. 
This donor-driven separation is a batch effect, and must be corrected before downstream analysis.

## Code cell 32

```python
af_dimensionality_reduction = ln.Artifact.from_mudata(
    mdata,
    key="surface-protein/cite_dimensionality_reduction.h5mu",
    description="CITE-seq data after dimensionality reduction",
)
af_dimensionality_reduction.save()
```

## Code cell 33

```python
ln.finish()
```

<!-- markdown cell 34 -->
## References

<!-- markdown cell 35 -->
```{bibliography}
:filter: docname in docnames
```

<!-- markdown cell 36 -->
## Contributors

We gratefully acknowledge the contributions of:

### Authors

* Javier Marchena-Hurtado
* Daniel Strobl
* Ciro Ramírez-Suástegui

### Reviewers

* Lukas Heumos
* Anna Schaar
