---
type: scbp-chapter-source
title: "Doublet detection"
upstream_path: jupyter-book/surface_protein/doublet_detection.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Doublet detection

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
(surface-protein-doublet-detection)=
# Doublet detection

<!-- markdown cell 2 -->
(surface-protein-doublet-detection-key-takeaway-1)=
## Motivation

<!-- markdown cell 3 -->
In the {ref}`surface-protein-quality-control` chapter, we removed cells that potentially reflect doublets based only on their high count content. 
We also filtered cells based on sample-wise distribution. 
Now, we will focus on heterotypic doublets, that is, doublets that contain cells from different cell types. 
With ADT data, we can detect them using cell type specific surface markers{cite}`Sun2021`.

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
We load the MuData object we saved at the end of the previous chapter {ref}`surface-protein-normalization`:

## Code cell 8

```python
af = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="surface-protein/cite_normalization.h5mu", is_latest=True
)
mdata = af.load()
mdata
```

<!-- markdown cell 9 -->
## Doublets detected with cell type markers

<!-- markdown cell 10 -->
We are now going to look at cell type markers that are mutually exclusive. 
Some examples are CD3 (T cell marker) vs CD19 (B cell marker) to identify T/B cells doublets.
As cells expressing both specific B and T cell markers do not exist under physiological conditions, those droplets contain T/B cell doublets.

The same is true for cells expressing both T cell (CD3) and monocyte (CD14) markers.

## Code cell 11

```python
sc.pl.scatter(mdata["prot"], x="CD3", y="CD19-1", color="log1p_total_counts")
```

<!-- markdown cell 12 -->
In this plot, we can see a large number of cells not expressing T or B cell markers in the lower left, cells expressing only one marker in the upper left and lower right as well as some cells expressing both markers (upper right).

The cells expressing both markers are doublets and can be removed.

<!-- markdown cell 13 -->
We can also use CD3 and CD14 to detect T/monocyte doublets.

## Code cell 14

```python
sc.pl.scatter(mdata["prot"], x="CD3", y="CD14-1", color="log1p_total_counts")
```

<!-- markdown cell 15 -->
It looks like cells that have an expression level above 2.5 in both markers are doublets. 
We use an expression level above 2.5 in both markers to flag doublets.

## Code cell 16

```python
genes2filter = ["CD3", "CD19-1", "CD14-1"]
temp = mdata["prot"][:, genes2filter].X.T.tolist()
```

## Code cell 17

```python
mdata["prot"].obs["doublets_markers"] = [
    (temp[0][i] > 2.5 and temp[1][i] > 2.5) or (temp[0][i] > 2.5 and temp[2][i] > 2.5)
    for i in range(mdata.shape[0])
]
mdata["prot"].obs["doublets_markers"] = (
    mdata["prot"].obs["doublets_markers"].astype(str)
)
```

<!-- markdown cell 18 -->
Doublets usually have a higher count due to the presence of increased counts from more than one cell. 
We can see this effect in the cells classified as doublets using our markers:

## Code cell 19

```python
sc.pl.violin(mdata["prot"], keys="log1p_total_counts", groupby="doublets_markers")
```

<!-- markdown cell 20 -->
We leave out cells expressing both markers.

## Code cell 21

```python
mdata = mdata[mdata["prot"].obs["doublets_markers"] == "False"].copy()
mdata
```

<!-- markdown cell 22 -->
We removed 612 doublets from the data.

In this chapter, we removed doublets using the ADT data by removing cells that highly expressed two mutually exclusive markers. 
Another option to remove doublets would be utilizing methods that detect doublets based on the scRNA-seq data. 
For those methods, we refer to the {ref}`rna:doublet-detection` chapter of scRNA-seq preprocessing and visualization.

## Code cell 23

```python
af_doublet_detection = ln.Artifact.from_mudata(
    mdata,
    key="surface-protein/cite_doublet_detection.h5mu",
    description="CITE-seq data after doublet detection",
)
af_doublet_detection.save()
```

## Code cell 24

```python
ln.finish()
```

<!-- markdown cell 25 -->
## References

<!-- markdown cell 26 -->
```{bibliography}
:filter: docname in docnames
```

<!-- markdown cell 27 -->
## Contributors

We gratefully acknowledge the contributions of:

### Authors

* Javier Marchena-Hurtado
* Daniel Strobl
* Ciro Ramírez-Suástegui

### Reviewers

* Lukas Heumos
* Anna Schaar
