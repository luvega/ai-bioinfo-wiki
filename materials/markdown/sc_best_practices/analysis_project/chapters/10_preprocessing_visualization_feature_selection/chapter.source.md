---
type: scbp-chapter-source
title: "Feature selection"
upstream_path: jupyter-book/preprocessing_visualization/feature_selection.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Feature selection

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
(pre-processing:feature-selection)=
# Feature selection

<!-- markdown cell 2 -->
(preprocessing-visualization-feature-selection-key-takeaway-1)=
## Motivation

<!-- markdown cell 3 -->
We now have a normalized data representation that still preserves biological heterogeneity but with reduced technical sampling effects in gene expression.
ScRNA-seq datasets usually contain up to 30,000 genes (depending on the organism) and so far we only removed genes that are not detected in at least 20 cells.
However, many of the remaining genes are not informative and contain mostly zero counts.
Therefore, a standard preprocessing pipeline involves the step of feature selection which aims to exclude uninformative genes which might not represent meaningful biological variation across samples. 

:::{figure-md} Feature selection

<img src="../_static/images/preprocessing_visualization/feature_selection.jpeg" alt="Feature selection" class="bg-primary mb-1" width="800px">

Feature selection generally describes the process of only selecting a subset of relevant features which can be the most informative, most variable or most deviant ones. 

:::

Often, the scRNA-{term}`seq <sequencing>` experiment focuses on one specific tissue and hence, only a small fraction of genes is informative and biologically variable.
Traditional approaches and pipelines either compute the coefficient of variation (highly variable genes) or the average expression level (highly expressed genes) of all genes to obtain 500-2000 selected genes and use these features for their downstream analysis steps.
However, these methods are highly sensitive to the normalization technique used before.
As mentioned earlier, a former preprocessing workflow included normalization with CPM and subsequent log transformation.
But as log-transformation is not possible for exact zeros, analysts often add a small *pseudo count*, e.g., 1 (log1p), to all normalized counts before log transforming the data.
Choosing the pseudo count, however, is arbitrary and can introduce biases to the transformed data.
This arbitrariness has then also an effect on the feature selection as the observed variability depends on the chosen pseudo count.
A small pseudo count value close to zero is increasing the variance of genes with zero counts {cite}`Townes2019`.

<!-- markdown cell 4 -->
Germain et al. instead propose to use *deviance* for feature selection which works on raw counts {cite}`fs:germain_pipecomp_2020`.
Deviance can be computed in closed form and quantifies whether genes show constant expression profile across cells as these are not informative.
Genes with constant expression are described by a multinomial null model, they are approximated by the binomial deviance.
Highly informative genes across cells will have a high deviance value which indicates a poor fit by the null model (i.e., they don't show constant expression across cells).
According to the deviance values, the method then ranks all genes and obtains only highly deviant genes. 

As mentioned before, deviance can be computed in closed form and is provided within the R package scry.

We start by setting up our environment.

## Code cell 5

```python
import logging

import lamindb as ln
import matplotlib.pyplot as plt
import numpy as np
import rpy2.rinterface_lib.callbacks as rcb
import rpy2.robjects as ro
import rpy2.robjects.packages as rpackages
import scanpy as sc
import seaborn as sns
from rpy2.robjects import default_converter, numpy2ri, pandas2ri, r
from rpy2.robjects.conversion import localconverter

# Suppress verbose logging from Scanpy
sc.settings.verbosity = 0

# Set figure parameters for clean, minimal plots
sc.settings.set_figure_params(dpi=80, facecolor="white", frameon=False)

assert ln.setup.settings.instance.slug == "theislab/sc-best-practices"

ln.track()

rcb.logger.setLevel(logging.ERROR)


%load_ext rpy2.ipython
```

## Code cell 6

```r
%%R
library(scry)
library(SingleCellExperiment)
```

<!-- markdown cell 7 -->
Next, we load the already normalized dataset from the [previous chapter](https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/preprocessing_visualization/normalization.ipynb).
Deviance works on raw counts so there is no need to replace `adata.X` with one of the normalized layers, but we can directly use the object as it was stored in the normalization notebook.

## Code cell 8

```python
af = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="preprocessing_visualization/s4d8_normalization.h5ad", is_latest=True
)
adata = af.load()
adata
```

<!-- markdown cell 9 -->
Similar to before, we save the AnnData object in our R environment.

## Code cell 10

```python
X_sparse = adata.X.T.tocoo()

Matrix = rpackages.importr("Matrix")

with localconverter(ro.default_converter + pandas2ri.converter + numpy2ri.converter):
    ro.globalenv["obs"] = adata.obs
    ro.globalenv["var"] = adata.var

i, j = X_sparse.row, X_sparse.col
x = X_sparse.data

ro.globalenv["i"] = ro.IntVector((i + 1).tolist())  # R is 1-indexed
ro.globalenv["j"] = ro.IntVector((j + 1).tolist())
ro.globalenv["x"] = ro.FloatVector(x.tolist())

r("X <- sparseMatrix(i = i, j = j, x = x, dims = c({}, {}))".format(*X_sparse.shape))
```

<!-- markdown cell 11 -->
We can now directly call feature selection with deviance on the non-normalized counts matrix and export the binomial deviance values as a vector.

## Code cell 12

```r
%%R
sce <- SingleCellExperiment(
  assays = list(X = X),
  colData = obs,
  rowData = var
)

sce <- devianceFeatureSelection(sce, assay = "X")
```

## Code cell 13

```python
with localconverter(default_converter + pandas2ri.converter + numpy2ri.converter):
    binomial_deviance = ro.r("rowData(sce)$binomial_deviance")
```

<!-- markdown cell 14 -->
As a next step, we now sort the vector and select the top 4,000 highly deviant genes and save them as an additional column in `.var` as 'highly_deviant'.
We additionally save the computed binomial deviance in case we want to sub-select a different number of highly variable genes afterwards.

## Code cell 15

```python
idx = binomial_deviance.argsort()[-4000:]
mask = np.zeros(adata.var_names.shape, dtype=bool)
mask[idx] = True

adata.var["highly_deviant"] = mask
adata.var["binomial_deviance"] = binomial_deviance
```

<!-- markdown cell 16 -->
Last, we visualise the feature selection results.
We use a scanpy function to compute the mean and dispersion for each gene across all cells.

## Code cell 17

```python
sc.pp.highly_variable_genes(adata, layer="scran_normalization")
```

<!-- markdown cell 18 -->
We inspect our results by plotting dispersion versus mean for the genes and color by 'highly_deviant'.

## Code cell 19

```python
ax = sns.scatterplot(
    data=adata.var, x="means", y="dispersions", hue="highly_deviant", s=5
)
ax.set_xlim(None, 1.5)
ax.set_ylim(None, 3)
plt.show()
```

<!-- markdown cell 20 -->
We observe that genes with a high mean expression are selected as highly deviant.
This is in agreement with empirical observations by {cite}`Townes2019`.

## Code cell 21

```python
af = ln.Artifact.from_anndata(
    adata,
    key="preprocessing_visualization/s4d8_feature_selection.h5ad",
    description="anndata after feature selection",
).save()
af
```

<!-- markdown cell 22 -->
## References

```{bibliography}
:filter: docname in docnames
:labelprefix: fs
```

<!-- markdown cell 23 -->
## Contributors

We gratefully acknowledge the contributions of:

### Authors

* Anna Schaar
* Seo H. Kim

### Reviewers

* Lukas Heumos
