---
type: scbp-chapter-source
title: "Compositional analysis"
upstream_path: jupyter-book/conditions/compositional.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Compositional analysis

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
# Compositional analysis

<!-- markdown cell 2 -->
## Motivation

<!-- markdown cell 3 -->
Beyond changes in gene expression patterns, cell compositions, such as the proportions of cell-types, can change between conditions. A specific drug may, for example, induce a transdifferentiation of a cell type which will be reflected in the cell identity composition. Sufficient cell and sample numbers are required to accurately determine cell-identity cluster proportions and background variation. Compositional analysis can be done on the level of cell identity clusters in the form of known cell types or cell states corresponding to, for example, cells recently affected by perturbations.

<!-- markdown cell 4 -->
:::{figure-md} Compositional analysis overview
<img src="../_static/images/conditions/compositional.jpg" alt="Compositional analysis overview" class="bg-primary mb-1" width="800px">

Differential abundance analysis compares the composition of cell types between two conditions. The samples from both modalities contain different proportions of cell types, which can be tested for significant shifts in abundance.
:::

<!-- markdown cell 5 -->

This chapter will introduce both approaches and apply them to the Haber dataset{cite}`comp:Haber2017`. This dataset contains 53,193 individual epithelial cells from the small intestine and organoids of mice. Some of the cells were also subject to bacterial or helminth infection such as through Salmonella and Heligmosomoides polygyrus respectively.
Throughout this tutorial we are using a subset of the complete Haber dataset which only includes control and infected cells that were collected specifically for this purpose. Notably, we are excluding an additional dataset which collected only large cells for faster computation and reduced complexity.

As a first step, we load the dataset.

<!-- markdown cell 6 -->
## Data loading

## Code cell 7

```python
import warnings

import pandas as pd

warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pertpy as pt
import scanpy as sc
import seaborn as sns
```

## Code cell 8

```python
adata = pt.dt.haber_2017_regions()
adata
```

## Code cell 9

```python
adata.obs
```

<!-- markdown cell 10 -->
The data was collected in 10 batches. Unique conditions are Control, Salmonella, Hpoly.Day3 and Hpoly.Day10 which correspond to the healthy control state, Salmonella infection, Heligmosomoides polygyrus infected cells after 3 days and Heligmosomoides polygyrus infected cells after 10 days. The `cell_label` corresponds to the cell types.

<!-- markdown cell 11 -->
## Why cell-type count data is compositional

<!-- markdown cell 12 -->
When analyzing the compositional shifts in cell count data, multiple technical and methodological limitations need to be accounted for. One challenge is the characteristically low number of experimental replicates, which leads to large confidence intervals when conducting differential abundance analysis with frequentist statistical tests.
Even more important, single-cell sequencing is naturally limited in the number of cells per sample - we can't sequence every cell in a tissue or organ, but use a small, representative snapshot instead. This, however, forces us to view the cell type counts as purely proportional, i.e. the total number of cells in a sample is only a scaling factor. In the statistical literature, such data is known as compositional data{cite}`Aitchison1982`, and characterized by the relative abundances of all features (cell types in our case) in one sample always adding up to one.

Because of this sum-to-one constraint, a negative correlation between the cell type abundances is induced. To illustrate this, let's consider the following example:

In a case-control study, we want to compare the cell type composition of a healthy and a diseased organ. In both cases, we have three cell types (A, B and C), but their abundances differ:
- The healthy organ consists of 2,000 cells of each type (6,000 cells total).
- The disease leads to a doubling of cell type A, while cell types B and C are not affected, so that the diseased organ has 8,000 cells.

## Code cell 13

```python
healthy_tissue = [2000, 2000, 2000]
diseased_tissue = [4000, 2000, 2000]
example_data_global = pd.DataFrame(
    data=np.array([healthy_tissue, diseased_tissue]),
    index=[1, 2],
    columns=["A", "B", "C"],
)
example_data_global["Disease status"] = ["Healthy", "Diseased"]
example_data_global
```

## Code cell 14

```python
plot_data_global = example_data_global.melt(
    "Disease status", ["A", "B", "C"], "Cell type", "count"
)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.barplot(
    data=plot_data_global, x="Disease status", y="count", hue="Cell type", ax=ax[0]
)
ax[0].set_title("Global abundances, by status")

sns.barplot(
    data=plot_data_global, x="Cell type", y="count", hue="Disease status", ax=ax[1]
)
ax[1].set_title("Global abundances, by cell type")

plt.show()
```

<!-- markdown cell 15 -->

We want to find out which cell types increase or decrease in abundance in the diseased organ. If we are able to determine the type of every cell in both organs, the case would be clear, as we can see in the right plot above. Unfortunately, this is not possible. Since our sequencing process has a limited capacity, we can only take a representative sample of 600 cells from both populations. To simulate this step, we can use numpy's `random.multinomial` function to sample 600 cells from the populations without replacement:

## Code cell 16

```python
rng = np.random.Generator(1234)
healthy_sample = rng.multinomial(pvals=healthy_tissue / np.sum(healthy_tissue), n=600)
diseased_sample = rng.multinomial(
    pvals=diseased_tissue / np.sum(diseased_tissue), n=600
)
example_data_sample = pd.DataFrame(
    data=np.array([healthy_sample, diseased_sample]),
    index=[1, 2],
    columns=["A", "B", "C"],
)
example_data_sample["Disease status"] = ["Healthy", "Diseased"]
example_data_sample
```

## Code cell 17

```python
plot_data_sample = example_data_sample.melt(
    "Disease status", ["A", "B", "C"], "Cell type", "count"
)

fig, ax = plt.subplots(1, 2, figsize=(12, 6))
sns.barplot(
    data=plot_data_sample, x="Disease status", y="count", hue="Cell type", ax=ax[0]
)
ax[0].set_title("Sampled abundances, by status")

sns.barplot(
    data=plot_data_sample, x="Cell type", y="count", hue="Disease status", ax=ax[1]
)
ax[1].set_title("Sampled abundances, by cell type")
plt.show()
```

<!-- markdown cell 18 -->
Now the picture is not clear anymore. While the counts of cell type A still increase (approx. from 200 to 300), the other two cell types seem to decrease from about 200 to 150. This apparent decrease is caused by our constraint to 600 cells - If a larger fraction of the sample is taken up by cell type A, the share of cell types B and C must be lower. Therefore, determining the change in abundance of one cell type is impossible without taking the other cell types into account.

If we ignore the compositionality of the data, and use univariate methods like Wilcoxon rank-sum tests or scDC, a method which performs differential cell-type composition analysis by bootstrap resampling{cite}`comp:Cao2019`, we may falsely perceive cell-type population shifts as statistically sound effects, although they were induced by inherent negative correlations of the cell-type proportions.

Furthermore, the subsampled data does not only give us one valid solution to our question. If both cell types B and C decreased by 1,000 cells in the diseased case, we would obtain the same representative samples of 600 cells as above. To get a unique result, we can fix a reference point for the data, which is assumed to be unchanged throughout all samples{cite}`Brill2019`. This can be a single cell type, an aggregation over multiple cell types such as the geometric mean, or a set of orthogonal bases {cite}`Egozcue2003`.

While single-cell datasets of sufficient size and replicate number have only been around for a few years, the same statistical property has also been discussed in the context of microbial analysis{cite}`Gloor2017`. There, some popular approaches include ANCOM-BC {cite}`Lin2020` and ALDEx2 {cite}`Fernandes2014`. However, these approaches often struggle with single-cell datasets due to the small number of experimental replicates.

<!-- markdown cell 19 -->
This issue has been tackled by scCODA{cite}`Büttner2021`, which we are going to introduce and apply to our dataset in the following section.

<!-- markdown cell 20 -->
(conditions-compositional-key-takeaway-1)=
## With labeled clusters

<!-- markdown cell 21 -->
[scCODA](https://sccoda.readthedocs.io/en/latest) belongs to the family of tools that require pre-defined clusters, most common cell types, to statistically derive changes in composition. Inspired by methods for compositional analysis of microbiome data, scCODA proposes a Bayesian approach to address the low replicate issue as commonly encountered in single-cell analysis{cite}`Büttner2021`. It models cell-type counts using a hierarchical Dirichlet-Multinomial model, which accounts for uncertainty in cell-type proportions and the negative correlative bias via joint modeling of all measured cell-type proportions. To ensure a uniquely identifiable solution and easy interpretability, the reference in scCODA is chosen to be a specific cell type. Hence, any detected compositional changes by scCODA always have to be viewed in relation to the selected reference.

<!-- markdown cell 22 -->
However, scCODA assumes a log-linear relationship between covariates and cell abundance, which may not always reflect the underlying biological processes when using continuous covariates. A further limitation of scCODA is the inability to infer correlation structures among cell compositions beyond compositional effects. Furthermore, scCODA only models shifts in mean abundance, but does not detect changes in response variability{cite}`Büttner2021`.

<!-- markdown cell 23 -->
As a first step, we instantiate a scCODA model. 

Then, we use load function to prepare a MuData object for subsequent processing, and it creates a compositional analysis dataset from the input adata. And we specify the cell_type_identifier as `cell_label`, sample_identifier as `batch`, and covariate_obs as `condition` in our case.

## Code cell 24

```python
sccoda_model = pt.tl.Sccoda()
sccoda_data = sccoda_model.load(
    adata,
    type="cell_level",
    generate_sample_level=True,
    cell_type_identifier="cell_label",
    sample_identifier="batch",
    covariate_obs=["condition"],
)
sccoda_data
```

<!-- markdown cell 25 -->
To get an overview of the cell type distributions across conditions we can use scCODA's `boxplots`. To get an even better understanding of how the data is distributed, the red dots show the actual data points.

## Code cell 26

```python
sccoda_model.plot_boxplots(
    sccoda_data,
    modality_key="coda",
    feature_name="condition",
    figsize=(12, 5),
    add_dots=True,
    args_swarmplot={"palette": ["red"]},
)
plt.show()
```

<!-- markdown cell 27 -->
The boxplots highlight some differences in the distributions of the cell types. Clearly noticeable is the high proportion of enterocytes for the Salmonella condition. But other cell types such as transit-amplifying (TA) cells also show stark differences in abundance for the Salmonella condition compared to control. Whether any of these differences are statistically significant has to be properly evaluated.

An alternative visualization is a stacked barplot as provided by scCODA. This visualization nicely displays the characteristics of compositional data: If we compare the Control and Salmonella groups, we can see that the proportion of Enterocytes greatly increases in the infected mice. Since the data is proportional, this leads to a decreased share of all other cell types to fulfill the sum-to-one constraint.

## Code cell 28

```python
sccoda_model.plot_stacked_barplot(
    sccoda_data, modality_key="coda", feature_name="condition", figsize=(4, 2)
)
plt.show()
```

<!-- markdown cell 29 -->
scCODA requires two major parameters beyond the cell count AnnData object: A formula and a reference cell type. The formula describes the covariates, which are specified using the [R-style](https://www.statsmodels.org/stable/example_formulas.html). In our case we specify the condition as the only covariate. Since it is a discrete covariate with four levels (control and three disease states), this models a comparison of each state with the other samples.
If we wanted to model multiple covariates at once, simply adding them in the formula (i.e. `formula = "covariate_1 + covariate_2"`) is enough.
As mentioned above, scCODA requires a reference cell type to compare against, which is believed to be unchanged by the covariates. scCODA can either automatically select an appropriate cell type as reference, which is a cell type that has nearly constant relative abundance over all samples, or be run with a user specified reference cell type. Here we set Endocrine cells as the reference since visually their abundance seems to be rather constant. An alternative to setting a reference cell type manually is to set the `reference_cell_type` to `"automatic"` which will force scCODA to select a suitable reference cell type itself. If the choice of reference cell type is unclear, we recommend to use this option to get an indicator or even a final selection.

## Code cell 30

```python
sccoda_data = sccoda_model.prepare(
    sccoda_data,
    modality_key="coda",
    formula="condition",
    reference_cell_type="Endocrine",
)
sccoda_model.run_nuts(sccoda_data, modality_key="coda", rng_key=1234)
```

## Code cell 31

```python
sccoda_data["coda"].varm["effect_df_condition[T.Salmonella]"]
```

<!-- markdown cell 32 -->
The acceptance rate describes the fraction of proposed samples that are accepted after the initial burn-in phase, and can be an ad-hoc indicator for a bad optimization run. In the case of scCODA, the desired acceptance rate is between 0.4 and 0.9. Acceptance rates that are way higher or too low indicate issues with the sampling process.

## Code cell 33

```python
sccoda_data
```

<!-- markdown cell 34 -->
scCODA selects credible effects based on their inclusion probability. The cutoff between credible and non-credible effects depends on the desired false discovery rate (FDR). A smaller FDR value will produce more conservative results, but might miss some effects, while a larger FDR value selects more effects at the cost of a larger number of false discoveries.
The desired FDR level can be easily set after inference via sim_results.set_fdr(). Per default, the value is 0.05. Since, depending on the dataset, the FDR can have a major influence on the result, we recommend to try out different FDRs up to 0.2 to get the most prominent effects.

In our case, we use less strict FDR of 0.2.

## Code cell 35

```python
sccoda_model.set_fdr(sccoda_data, 0.2)
```

<!-- markdown cell 36 -->
To get the binary classification of compositional changes per cell type we use the `credible_effects` function of scCODA on the result object. Every cell type labeled as "True" is significantly more or less present. The fold-changes describe whether the cell type is more or less present. Hence, we will plot them alongside the binary classification below.

## Code cell 37

```python
sccoda_model.credible_effects(sccoda_data, modality_key="coda")
```

<!-- markdown cell 38 -->
To plot the fold changes together with the binary classification, we can easily use effects_bar_plot function.

## Code cell 39

```python
sccoda_model.plot_effects_barplot(sccoda_data, "coda", "condition")
plt.show()
```

<!-- markdown cell 40 -->
The plots nicely show the significant and credible effects of conditions on the cell types. These effects largely agree with the findings in the Haber paper, who used a non-compositional Poisson regression model their findings:

1. "After Salmonella infection, the frequency of mature enterocytes increased substantially."{cite}`comp:Haber2017`
2. "Heligmosomoides polygyrus caused an increase in the abundance of goblet and tuft cells."{cite}`comp:Haber2017`

Readers familiar with the original publication may wonder why the model used by Haber et al. found more significant effects than scCODA, for example a decrease in Stem and Transit-Amplifying cells in the case of Salmonella infection{cite}`comp:Haber2017`. To explain this discrepancy, remember that cell count data is compositional and therefore an increase in the relative abundance of one cell type will lead to a decrease in the relative abundance of all other cell types.
Due to the stark increase of Enterocytes in the small intestinal epithelium of Salmonella-infected mice, all other cell types appear to decrease, even though this shift is only caused by the compositional properties of the data. While the original (univariate) Poisson regression model will pick up these likely false positive effects, scCODA is able to account for the compositionality of the data and therefore does not fall into this trap.

<!-- markdown cell 41 -->
## With labeled clusters and hierarchical structure

<!-- markdown cell 42 -->
In addition to the abundance of each cell type, a typical single-cell dataset also contains information about the similarity of the different cells in the form of a tree-based hierarchical ordering. These hierarchies can either be determined automatically via clustering of the gene expression (which is usually done to discover the clusters of cells that belong to the same cell type), or through biologically informed hierarchies like cell lineages.
[tascCODA](https://tasccoda.readthedocs.io/en/latest/) is an extension of scCODA that integrates hierarchical information and experimental covariate data into the generative modeling of compositional count data{cite}`Ostner2021`. This is especially beneficial for cell atlassing efforts with increased resolution.

At its core, it uses almost the same Dirichlet-Multinomial setup as scCODA, but extends the model, such that effects on sets of cell types, which are defined as internal nodes in the tree structure.

## Code cell 43

```python
import schist

warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")
```

<!-- markdown cell 44 -->
To use tascCODA, we first have to define a hierarchical ordering of the cell types. One possible hierarchical clustering uses the eight cell types and orders them by their similarity (pearson correlation) in the PCA representation with `sc.tl.dendrogram`.
Since this structure is very simple in our data and will therefore not give us many new insights, we want to have a more complex clustering. One recent method to get such clusters, is the [schist](https://github.com/dawe/schist) package {cite}`Morelli2021`, which uses a nested stochastic block model that clusters the cell population at different resolution levels. Running the method with standard settings takes some time (~15 minutes on our data), and gives us an assignment of each cell to a hierarchical clustering in `adata.obs`.
First, we need to define a distance measure between the cells through a PCA embedding:

## Code cell 45

```python
# use logcounts to calculate PCA and neighbors
adata.layers["counts"] = adata.X.copy()
adata.layers["logcounts"] = sc.pp.log1p(adata.layers["counts"]).copy()
adata.X = adata.layers["logcounts"].copy()
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=30, random_state=1234)
sc.tl.umap(adata)
```

<!-- markdown cell 46 -->
Then, we can run schist on the AnnData object, which results in a clustering that is defined through a set of columns "nsbm_level_{i}" in `adata.obs`:

## Code cell 47

```python
schist.inference.nested_model(adata, samples=100, random_seed=5678)
adata.obs
```

<!-- markdown cell 48 -->
A UMAP plot nicely shows how the clustering from schist (here on levels 1 and 2) is connected to the cell type assignments. The representation on level 1 of the hierarchy is hereby a strict refinement of the level above, i.e. each cluster from level 2 is split into multiple smaller clusters:

## Code cell 49

```python
sc.pl.umap(
    adata, color=["nsbm_level_1", "nsbm_level_2", "cell_label"], ncols=3, wspace=0.5
)
```

<!-- markdown cell 50 -->
Now, we convert our cell-level data to sample-level data and create the tree. We create a tasccoda_model object in the same way as for scCODA, but with the clustering defined by schist and tree levels.

The load function of Tasccoda will prepare a MuData object and it converts our tree representation into a [ete](http://etetoolkit.org/) tree structure and save it as `tasccoda_data['coda'].uns["tree"]`. To get some clusters that are not too small, we cut the tree before the last level by leaving out `"nsbm_level_0"`.

## Code cell 51

```python
tasccoda_model = pt.tl.Tasccoda()
tasccoda_data = tasccoda_model.load(
    adata,
    type="cell_level",
    cell_type_identifier="nsbm_level_1",
    sample_identifier="batch",
    covariate_obs=["condition"],
    levels_orig=["nsbm_level_4", "nsbm_level_3", "nsbm_level_2", "nsbm_level_1"],
    add_level_name=True,
)
tasccoda_data
```

## Code cell 52

```python
tasccoda_model.plot_draw_tree(tasccoda_data)
```

<!-- markdown cell 53 -->
The model setup and execution in tascCODA works analogous to scCODA, and also the free parameters for the reference and the formula are the same. Additionally, we can adjust the tree aggregation and model selection via the parameters `phi` and `lambda_1` in the `pen_args` argument (see {cite}`Ostner2021` for more information). Here, we use an unbiased setting `phi=0` and a model selection that is slightly less strict than the default with `lambda_1=1.7`. We use cluster 18 as our reference, since it is almost identical to the set of Endocrine cells.

## Code cell 54

```python
tasccoda_model.prepare(
    tasccoda_data,
    modality_key="coda",
    reference_cell_type="18",
    formula="condition",
    pen_args={"phi": 0, "lambda_1": 3.5},
    tree_key="tree",
)
```

## Code cell 55

```python
tasccoda_model.run_nuts(
    tasccoda_data, modality_key="coda", rng_key=1234, num_samples=10000, num_warmup=1000
)
```

## Code cell 56

```python
tasccoda_model.summary(tasccoda_data, modality_key="coda")
```

<!-- markdown cell 57 -->
Again, the acceptance probability is right around the desired value of 0.85 for tascCODA, indicating no apparent problems with the optimization.

The result from tascCODA should first and foremost be interpreted as effects on the nodes of the tree. A nonzero parameter on a node means that the aggregated count of all cell types under that node changes significantly.
We can easily visualize this in a tree plot for each of the three disease states. Blue circles indicate an increase, red circles a decrease:

## Code cell 58

```python
tasccoda_model.plot_draw_effects(
    tasccoda_data,
    modality_key="coda",
    tree="tree",
    covariate="condition[T.Salmonella]",
    show_leaf_effects=False,
    show_legend=False,
)
```

## Code cell 59

```python
tasccoda_model.plot_draw_effects(
    tasccoda_data,
    modality_key="coda",
    tree="tree",
    covariate="condition[T.Hpoly.Day3]",
    show_leaf_effects=False,
    show_legend=False,
)
```

## Code cell 60

```python
tasccoda_model.plot_draw_effects(
    tasccoda_data,
    modality_key="coda",
    tree="tree",
    covariate="condition[T.Hpoly.Day10]",
    show_leaf_effects=False,
    show_legend=False,
)
```

<!-- markdown cell 61 -->
Alternatively, effects on internal nodes can also be translated through the tree onto the cell type level, allowing for a calculation of log-fold changes like in scCODA.
To visualize the log-fold changes of the cell types, we do the same plots as for scCODA, inspired by "High-resolution single-cell atlas reveals diversity and plasticity of tissue-resident neutrophils in non-small cell lung cancer"{cite}`Salcher2022`.

## Code cell 62

```python
tasccoda_model.plot_effects_barplot(
    tasccoda_data, modality_key="coda", covariates="condition"
)
```

<!-- markdown cell 63 -->
Another insightful representation can be gained by plotting the effect sizes for each condition on the UMAP embedding, and comparing it to the cell type assignments:

## Code cell 64

```python
kwargs = {"ncols": 3, "wspace": 0.25, "vcenter": 0, "vmax": 1.5, "vmin": -1.5}
tasccoda_model.plot_effects_umap(
    tasccoda_data,
    effect_name=[
        "effect_df_condition[T.Salmonella]",
        "effect_df_condition[T.Hpoly.Day3]",
        "effect_df_condition[T.Hpoly.Day10]",
    ],
    cluster_key="nsbm_level_1",
    **kwargs,
)
sc.pl.umap(
    tasccoda_data["rna"], color=["cell_label", "nsbm_level_1"], ncols=2, wspace=0.5
)
```

<!-- markdown cell 65 -->
The results are very similar to scCODA's findings:
- For the Salmonella infection, we get an aggregated increase in clusters that approximately represent Enterocytes in the cell type clustering. This increase is even stronger for cluster 12, as indicated by the additional positive effect on the leaf level
- For the Heligmosomoides polygyrus infection, we get no credible changes after 3 days. After 10 days, we pick up decreases in clusters that contain Stem- and transit-amplifying cells, as well as a less strong decrease of Enterocytes and Enterocyte progenitors, which was also picked up by scCODA.

<!-- markdown cell 66 -->
(conditions-compositional-key-takeaway-2)=
## Without labeled clusters

<!-- markdown cell 67 -->
It is not always possible or practical to use precisely labeled clusters such as cell-type definitions, especially when we are interested in studying transitional states between cell type clusters, such as during developmental processes, or when we expect only a subpopulation of a cell type to be affected by the condition of interest. In such cases, determining compositional changes based on known annotations may not be appropriate. 

A set of methods exist to detect compositional changes occurring in subpopulations of cells smaller than the cell type clusters, usually defined starting from a k-nearest neighbor (KNN) graph computed from similarities in the same low dimensional space used for clustering. 

- DA-seq computes, for each cell, a score based on the relative prevalence of cells from both biological states in the cell’s neighborhood, using a range of k values{cite}`Zhao2021`. The scores are used as input for a logistic classifier to predict the biological condition of each cell. 
- Milo assigns cells to partially overlapping neighborhoods on the KNN graph, then differential abundance (DA) testing is performed modelling cell counts with a generalized linear model (GLM) {cite}`Dann2022`. 
- MELD calculates a relative likelihood estimate of observing each cell in every condition using graph-based density estimate{cite}`Burkhardt2021`. 

These methods have unique strengths and weaknesses. Because it relies on logistic classification, DA-seq is designed for pairwise comparisons between two biological conditions, but can't be applied to test for differences associated with a continuous covariate (such as age or timepoints). DA-seq and Milo use the variance in the abundance statistic between replicate samples of the same condition to estimate the significance of the differential abundance, while MELD doesn't use this information. While considering consistency across replicates reduces the number of false positives driven by one or a few samples, all KNN-based methods are sensitive to a loss of information if the conditions of interest and confounders, defined by technical or experimental sources of variation, are strongly correlated. The impact of confounders can be mitigated using batch integration methods before KNN graph construction and/or incorporating the confounding covariates in the model for DA testing, as we discuss further in the example below. Another limitation of KNN-based methods to bear in mind is that cells in a neighborhood may not necessarily represent a specific, unique biological subpopulation, because a cellular state may span over multiple neighborhoods. Reducing k for the KNN graph or constructing a graph on cells from a particular lineage of interest can help mitigate this issue and ensure the predicted effects are robust to the choice of parameters and to the data subset used{cite}`Dann2022`. 

Generally, if large differences are apparent in large clusters by visualization or the imbalances between cell types are of interest, direct analysis with cell-type aware methods, such as scCODA, might be more suitable. KNN-based methods are more powerful when we are interested in differences in cell abundances that might appear in transitional states between cell types or in a specific subset of cells of a given cell type.

<!-- markdown cell 68 -->
We will now apply Milo to the Haber dataset to try to find over- or underrepresented neighborhoods of cells upon infection.

Milo is available as [miloR](https://github.com/MarioniLab/miloR) for R users and in [Pertpy](https://github.com/theislab/pertpy) for Python users in the scverse ecosystem. In the following demonstration, we will use milo which is easiest to use with our AnnData object due to its scverse compatibility. Be aware that milo in its current state also requires a working [edgeR](https://bioconductor.org/packages/release/bioc/html/edgeR.html) installation.

<!-- markdown cell 69 -->
To perform DA analysis with Milo, we need to construct a KNN graph that is representative of the biological similarities between cells, as we do when performing clustering or UMAP visualization of a single-cell dataset. This means (A) building a common low-dimensional space for all samples and (B) minimizing cell-cell similarities driven by technical factors (i.e. batch effects).

We first use the standard scanpy workflow for dimensionality reduction to qualitatively assess whether we see a batch effect in this dataset.

## Code cell 70

```python
milo = pt.tl.Milo()
adata = pt.dt.haber_2017_regions()
mdata = milo.load(adata)
mdata
```

## Code cell 71

```python
# use logcounts to calculate PCA and neighbors
adata.layers["counts"] = adata.X.copy()
adata.layers["logcounts"] = sc.pp.log1p(adata.layers["counts"]).copy()
adata.X = adata.layers["logcounts"].copy()

sc.pp.highly_variable_genes(
    adata, n_top_genes=3000, subset=False
)  # 3k genes as used by authors for clustering

sc.pp.pca(adata)
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=30)
sc.tl.umap(adata)
```

## Code cell 72

```python
sc.pl.umap(adata, color=["condition", "batch", "cell_label"], ncols=3, wspace=0.25)
```

<!-- markdown cell 73 -->
While cell type clusters are broadly captured, we can see residual separation between batches, also for replicates of the same treatment. If we define neighbourhoods on this KNN graph we might have a large fraction of neighbourhoods containing cells from just one or a few batches. This could introduce false negatives, if the variance in number of cells between replicates is too low (e.g. 0 cells for all replicates) or too high (e.g. all zero cells except for one replicate with a large number of cells), but also false positives, especially when, like in this case, the number of replicates per condition is low. 

To minimize these errors, we apply the scVI method to learn a batch-corrected latent space, as introduced in the [integration chapter]().

## Code cell 74

```python
import scvi

adata_scvi = adata[:, adata.var["highly_variable"]].copy()
scvi.model.SCVI.setup_anndata(adata_scvi, layer="counts", batch_key="batch")
model_scvi = scvi.model.SCVI(adata_scvi)
max_epochs_scvi = int(np.min([round((20000 / adata.n_obs) * 400), 400]))
model_scvi.train(max_epochs=max_epochs_scvi)
adata.obsm["X_scVI"] = model_scvi.get_latent_representation()
```

## Code cell 75

```python
sc.pp.neighbors(adata, use_rep="X_scVI")
sc.tl.umap(adata)
```

## Code cell 76

```python
sc.pl.umap(adata, color=["condition", "batch", "cell_label"], ncols=3, wspace=0.25)
```

<!-- markdown cell 77 -->
Here we can see much better mixing between batches and cell labels form much more uniform clusters.

```{admonition} Will batch correction remove biological differences between conditions?

This really boils down to good experimental design. In an ideal set-up replicates from the same condition will be processed in different batches. This allows to estimate technical differences more accurately and possibly also incorporate the batch as a confounder in the linear model for differential abundance analysis (see below), to further minimize false positives. When, like in this example, batches are confounded with the biological condition of interest, we have to recognize that while we might be minimizing false positives, the rate of false negatives might also increase. The analyst can decide which type of error is more detrimental depending on the dataset and purpose of the differential abundance analysis.
```

<!-- markdown cell 78 -->
### Define neighbourhoods

<!-- markdown cell 79 -->
Milo is a KNN-based model, where cell abundance is quantified on neighbourhoods of cells. In Milo, a neighbourhood is defined as the group of cells connected by an edge to the same cell (_index cell_) in an undirected KNN graph. While we could in principle have one neighbourhood for each cell in the graph, this would be inefficient and significantly increase the multiple testing burden. Therefore Milo samples a refined set of cells as index cells for neighbourhoods, starting from a random sample of a fraction of cells. The initial proportion can be specified using the `prop` argument in the `milo.make_nhoods` function. As by default, we recommend using `prop=0.1` (10% of cells) and to reduce to 5% or 2% to increase scalability on large datasets (> 100k cells).

If no `neighbors_key` parameter is specified, Milo uses the neighbours from `.obsp`. Therefore, ensure that `sc.pp.neighbors` was run on the correct representation, i.e. an integrated latent space if batch correction was required.

## Code cell 80

```python
milo.make_nhoods(mdata, prop=0.1)
```

<!-- markdown cell 81 -->
Now the binary assignment of cells to neighbourhood is stored in `adata.obsm['nhoods']`. Here we can see that, as expected, the number of neighbourhoods should be less or equal to the number of cells in the graph times the `prop` parameter. In this case, less or equal than 984 neighbourhoods.

## Code cell 82

```python
adata.obsm["nhoods"]
```

<!-- markdown cell 83 -->
At this point we need to check the median number of cells in each neighbourhood, to make sure the neighbourhoods contain enough cells to detect differences between samples.

## Code cell 84

```python
nhood_size = adata.obsm["nhoods"].toarray().sum(0)
plt.hist(nhood_size, bins=20)
plt.xlabel("# cells in neighbourhood")
plt.ylabel("# neighbouthoods")
```

## Code cell 85

```python
np.median(nhood_size)
```

<!-- markdown cell 86 -->
We expect the minimum number of cells to be equal to the k parameter used during graph construction (k=10 in this case). To increase the statistical power for DA testing, we need a sufficient number of cells from all samples in the majority of the neighbourhoods. We can use the following rule of thumb: to have a median of 3 cells from each sample in a neighbourhood, the number of cells in a neighbourhood should be at least 3 times the number of samples. In this case, we have data from 10 samples. If we want to have on average 3 cells from each sample in a neighbourhood, the minimum number of cells should be 30. 

Based on the plot above, we have a large number of neighbourhoods with less than 30 cells, which could lead to an underpowered test. To solve this, we just need to recompute the KNN graph using `n_neighbors=30`. To distinguish this KNN graph used for neighbourhood-level DA analysis from the graph used for UMAP building, we will store this as a distinct graph in `adata.obsp`.

## Code cell 87

```python
sc.pp.neighbors(adata, n_neighbors=30, use_rep="X_scVI", key_added="milo")
milo.make_nhoods(mdata, neighbors_key="milo", prop=0.1)
```

<!-- markdown cell 88 -->
Let's check that the distribution of neighbourhood sizes has shifted.

## Code cell 89

```python
nhood_size = adata.obsm["nhoods"].toarray().sum(0)
plt.hist(nhood_size, bins=20)
plt.xlabel("# cells in neighbourhood")
plt.ylabel("# neighbouthoods")
```

<!-- markdown cell 90 -->
### Count cells in neighbourhoods

<!-- markdown cell 91 -->
In the next step, Milo counts cells belonging to each of the samples (here identified by the `batch` column in `adata.obs`).

## Code cell 92

```python
milo.count_nhoods(mdata, sample_col="batch")
```

<!-- markdown cell 93 -->
This stores a neighbourhood-level AnnData object, where `nhood_adata.X` stores the number of cells from each sample in each neighbourhood.

## Code cell 94

```python
mdata["milo"]
```

<!-- markdown cell 95 -->
We can verify that the average number of cells per sample times the number of samples roughly corresponds to the number of cells in a neighbourhood.

## Code cell 96

```python
mean_n_cells = mdata["milo"].X.toarray().mean(0)
plt.plot(nhood_size, mean_n_cells, ".")
plt.xlabel("# cells in nhood")
plt.ylabel("Mean # cells per sample in nhood")
```

<!-- markdown cell 97 -->
### Run differential abundance test on neighbourhoods

<!-- markdown cell 98 -->
Milo uses edgeR's QLF test to test if there are statistically significant differences between the number of cells from a condition of interest in each neighborhood. 

Here we are interested in detecting in which neighbourhoods there is a significant increase or decrease of cells in response to infection. Since the `condition` covariate stores many different types of infection, we need to specify which conditions we need to contrast in our differential abundance test (following a convention used in R, by default the last level of the covariate against the rest will be used, in this case Salmonella vs rest). To specify the comparison, we use [the syntax used for GLMs in R](https://genomicsclass.github.io/book/pages/expressing_design_formula.html).

Let's first test for differences associated with Salmonella infection.

## Code cell 99

```python
milo.da_nhoods(
    mdata, design="~condition", model_contrasts="conditionSalmonella-conditionControl"
)
milo_results_salmonella = mdata["milo"].obs.copy()
milo_results_salmonella
```

<!-- markdown cell 100 -->
For each neighbourhood, we calculate a set of statistics. The most important ones to understand are:
- **log-Fold Change (logFC):** this represents the effect size of the difference in cell abundance and corresponds to the coefficient associated with the condition of interest in the GLM. If logFC > 0 the neighbourhood is enriched in cells from the condition of interest, if logFC < 0 the neighbourhood is depleted in cells from the condition of interest. 
- **Uncorrected p-value (PValue):** this is the p-value for the QLF test before multiple testing correction.
- **SpatialFDR:** this is the p-value adjusted for multiple testing to limit the false discovery rate. This is calculated adapting the weighted Benjamini-Hochberg (BH) correction introduced by Lun et al {cite}`lun2017`, which accounts for the fact that because neighbourhoods are partially overlapping (i.e. one cell can belong to multiple neighbourhoods) the DA tests on different neighbourhoods are not completely independent. In practice, the BH correction is weighted by the reciprocal of the distance to the k-th nearest neighbor to the index cell (stored in `kth_distance`), which is used as a proxy for the amount of overlap with other neighbourhoods. You might notice that the SpatialFDR values are always lower or equal to the FDR values, calculated with a conventional BH correction.

<!-- markdown cell 101 -->
Before any exploration and interpretation of the results, we can visualize these statistics with a set of diagnostics plots to sanity check our statistical test:

## Code cell 102

```python
def plot_milo_diagnostics(mdata):
    alpha = 0.1  ## significance threshold

    with matplotlib.rc_context({"figure.figsize": [12, 12]}):
        ## Check P-value histogram
        plt.subplot(2, 2, 1)
        plt.hist(mdata["milo"].var["PValue"], bins=20)
        plt.xlabel("Uncorrected P-value")

        ## Visualize extent of multiple-testing correction
        plt.subplot(2, 2, 2)
        plt.scatter(
            mdata["milo"].var["PValue"],
            mdata["milo"].var["SpatialFDR"],
            s=3,
        )
        plt.xlabel("Uncorrected P-value")
        plt.ylabel("SpatialFDR")

        ## Visualize volcano plot
        plt.subplot(2, 2, 3)
        plt.scatter(
            mdata["milo"].var["logFC"],
            -np.log10(mdata["milo"].var["SpatialFDR"]),
            s=3,
        )
        plt.axhline(
            y=-np.log10(alpha),
            color="red",
            linewidth=1,
            label=f"{int(alpha * 100)} % SpatialFDR",
        )
        plt.legend()
        plt.xlabel("log-Fold Change")
        plt.ylabel("- log10(SpatialFDR)")
        plt.tight_layout()

        ## Visualize MA plot
        df = mdata["milo"].var
        emp_null = df[df["SpatialFDR"] >= alpha]["logFC"].mean()
        df["Sig"] = df["SpatialFDR"] < alpha

        plt.subplot(2, 2, 4)
        sns.scatterplot(data=df, x="logCPM", y="logFC", hue="Sig")
        plt.axhline(y=0, color="grey", linewidth=1)
        plt.axhline(y=emp_null, color="purple", linewidth=1)
        plt.legend(title=f"< {int(alpha * 100)} % SpatialFDR")
        plt.xlabel("Mean log-counts")
        plt.ylabel("log-Fold Change")
        plt.show()


plot_milo_diagnostics(mdata)
```

<!-- markdown cell 103 -->
1. The **P-value histogram** shows the distribution of P-values before multiple testing correction. By definition, we expect the p-values under the null hypothesis (> significance level) to be uniformly distributed, while the peak of p-values close to zero represents the significant results. This gives you an idea of how conservative your test is, and it might help to spot early some pathological cases. For example, if the distribution of P-values looks bimodal, with a second peak close to 1, this might indicate that you have a large number of neighbourhoods with no variance between replicates of one condition (e.g. all replicates from one condition have 0 cells) which might indicate a residual batch effect or that you need to increase the size of neighbourhoods; if the p-value histogram is left-skewed this might indicate a [confounding covariate](https://github.com/MarioniLab/miloR/issues/220#issuecomment-1140812805) has not been accounted for in the model. For other pathological cases and possible interpretations see [this blogpost](http://varianceexplained.org/statistics/interpreting-pvalue-histogram/).
2. For each neighbourhood we plot the uncorrected P-Value VS the p-value controlling for the Spatial FDR. Here we expect the adjusted p-values to be larger (so points above the diagonal). If the FDR correction is especially severe (i.e. many values close to 1) this might indicate a pathological case. You might be testing on too many neighbourhoods (you can reduce `prop` in `milo.make_nhoods`) or there might be too much overlap between neighbourhoods (you might need to decrease _k_ when constructing the KNN graph).
3. The **volcano plot** gives us an idea of how many neighbourhoods show significant DA after multiple testing correction ( - log(SpatialFDR) > 1) and shows how many neighbourhoods are enriched or depleted of cells from the condition of interest.  
4. The **MA plot** shows the dependency between average number of cells per sample and the log-Fold Change of the test. In a balanced scenario, we expect points to be concentrated around logFC = 0, otherwise the shift might indicate a strong imbalance in average number of cells between samples from different conditions. For more tips on how to interpret the MA plot see https://github.com/MarioniLab/miloR/issues/208.

<!-- markdown cell 104 -->
After sanity check, we can visualize the DA results for each neighbourhood by the position of the index cell on the UMAP embedding, to qualitatively assess which cell types may be most affected by the infection.

## Code cell 105

```python
milo.build_nhood_graph(mdata)
with matplotlib.rc_context({"figure.figsize": [10, 10]}):
    milo.plot_nhood_graph(mdata, alpha=0.1, min_size=5, plot_edges=False)
    sc.pl.umap(mdata["rna"], color="cell_label", legend_loc="on data")
```

<!-- markdown cell 106 -->
This shows a set of neighbourhoods enriched upon Salmonella infection corresponding to mature enterocytes, and a depletion in a subset of stem cell neighbourhoods. For interpretation of results, it's often useful to annotate neighbourhoods by the cell type cluster that they overlap with.

## Code cell 107

```python
milo.annotate_nhoods(mdata, anno_col="cell_label")
# Define as mixed if fraction of cells in nhood with same label is lower than 0.75

mdata["milo"].var.loc[
    mdata["milo"].var["nhood_annotation_frac"] < 0.75, "nhood_annotation"
] = "Mixed"
```

## Code cell 108

```python
milo.plot_da_beeswarm(mdata)
plt.show()
```

<!-- markdown cell 109 -->
```{admonition} What about the compositional effect?

Comparing the Milo results to the scCODA results, here we identify a strong enrichment upon _Salmonella_ infection in the Enterocytes, but also a depletion in a subset of Stem cells, similarly to what the original authors reported{cite}`comp:Haber2017`. Although we don't have a ground truth to verify whether the decrease in abundance of stem cells is real, it's important to note that the GLM in Milo doesn't explicitly model the compositional nature of cell abundances in neighborhoods, so in theory the results could be affected by compositional biases. In practice, performing a test on a large number of neighbourhoods alleviates this issue, since the effect in the opposite direction is distributed across thousands of neighborhoods rather than tens of cell types. Additionally, the test used in Milo uses the trimmed mean of M values normalization method (TMM normalization {cite}`comp:Robinson2010`) to estimate normalization factors robust to compositional differences across samples. In this particular example, residual compositional effects might be explained by (A) the relatively small number of neighborhoods (< 1000), (B) the very large effect size in Enterocyte neighbourhoods or (C) the very small number of replicates per condition.   
```

<!-- markdown cell 110 -->
Of note, the GLM framework used by Milo allows to test for cell enrichment/depletion also for continuous covariates. We demonstrate this by testing for differential abundance along the _Heligmosomoides polygyrus_ infection time course.

## Code cell 111

```python
## Turn into continuous variable
mdata["rna"].obs["Hpoly_timecourse"] = (
    mdata["rna"]
    .obs["condition"]
    .cat.reorder_categories(["Salmonella", "Control", "Hpoly.Day3", "Hpoly.Day10"])
)
mdata["rna"].obs["Hpoly_timecourse"] = mdata["rna"].obs["Hpoly_timecourse"].cat.codes

## Here we exclude salmonella samples
test_samples = (
    mdata["rna"]
    .obs.batch[mdata["rna"].obs.condition != "Salmonella"]
    .astype("str")
    .unique()
)
milo.da_nhoods(mdata, design="~ Hpoly_timecourse", subset_samples=test_samples)
```

## Code cell 112

```python
plot_milo_diagnostics(mdata)
```

## Code cell 113

```python
with matplotlib.rc_context({"figure.figsize": [10, 10]}):
    milo.plot_nhood_graph(mdata, alpha=0.1, min_size=5, plot_edges=False)
```

## Code cell 114

```python
milo.plot_da_beeswarm(mdata)
plt.show()
```

<!-- markdown cell 115 -->
We can verify that the test captures a linear increase in cell numbers across the time course by plotting the number of cells per sample by condition in neighborhoods where significant enrichment or depletion was detected.

## Code cell 116

```python
entero_ixs = mdata["milo"].var_names[
    (mdata["milo"].var["SpatialFDR"] < 0.1)
    & (mdata["milo"].var["logFC"] < 0)
    & (mdata["milo"].var["nhood_annotation"] == "Enterocyte")
]

plt.title("Enterocyte")
milo.plot_nhood_counts_by_cond(
    mdata, test_var="Hpoly_timecourse", subset_nhoods=entero_ixs
)
plt.show()


tuft_ixs = mdata["milo"].var_names[
    (mdata["milo"].var["SpatialFDR"] < 0.1)
    & (mdata["milo"].var["logFC"] > 0)
    & (mdata["milo"].var["nhood_annotation"] == "Tuft")
]
plt.title("Tuft cells")
milo.plot_nhood_counts_by_cond(
    mdata, test_var="Hpoly_timecourse", subset_nhoods=tuft_ixs
)
plt.show()
```

<!-- markdown cell 117 -->
Interestingly the DA test on the neighbourhoods detects an enrichment upon infection in Tuft cells and in a subset of goblet cells. We can characterize the difference between cell type subpopulations enriched upon infection by examining the mean gene expression profiles of cells in neighbourhoods. For example, if we take the neighbourhoods of Goblet cells, we can see that neighbourhoods enriched upon infection display a higher expression of Retnlb, which is a gene implicated in anti-parasitic immunity {cite}`comp:Haber2017`.

## Code cell 118

```python
## Compute average Retnlb expression per neighbourhood
# (you can add mean expression for all genes using milo.utils.add_nhood_expression)
mdata["rna"].obs["Retnlb_expression"] = (
    mdata["rna"][:, "Retnlb"].layers["logcounts"].toarray().ravel()
)
milo.annotate_nhoods_continuous(mdata, "Retnlb_expression")
# milo.annotate_nhoods(mdata, "Retnlb_expression")

## Subset to Goblet cell neighbourhoods
nhood_df = mdata["milo"].var.copy()
nhood_df = nhood_df[nhood_df["nhood_annotation"] == "Goblet"]

sns.scatterplot(data=nhood_df, x="logFC", y="nhood_Retnlb_expression")
plt.show()
```

<!-- markdown cell 119 -->
> **Accounting for confounding covariates:** several confounding factors might affect cell abundances and proportions other than our condition of interest. For example, different set of samples might have been processed or sequenced in the same batch, or a set of samples could contain cells FAC-sorted using different markers to enrich a subset of populations of interest. As long as these factors are not completely correlated with the condition of interest, we can include these covariates in the model used for differential abundance testing, to estimate differential abundance associated with the condition of interest, while minimizing differences explained by the confounding factors. In Milo, we can express this type of test design using the syntax `~ confounder + condition`.

## Code cell 120

```python
## Make dummy confounder for the sake of this example
nhood_adata = mdata["milo"].copy()
conf_dict = dict(
    zip(
        nhood_adata.obs_names,
        rng.choice(["group1", "group2"], nhood_adata.n_obs),
        strict=False,
    )
)
mdata["rna"].obs["dummy_confounder"] = [conf_dict[x] for x in mdata["rna"].obs["batch"]]

milo.da_nhoods(mdata, design="~ dummy_confounder+condition")
```

## Code cell 121

```python
mdata["milo"].var
```

<!-- markdown cell 122 -->
## Quiz

## Code cell 123

```python
%run ../src/lib.py

flip_card(
    "q1",
    "It is tricky to deduce compositional changes visually. Why?",
    "Interpreting compositional changes visually is challenging because shifts in cell type proportions may be subtle or confounded by the high dimensionality and variability inherent in single-cell data, making it difficult to discern significant differences without statistical analysis.",
    back_font_size=15,
)
flip_card(
    "q2",
    "Why is it necessary to interpret cell type ubundances as proportions instead of absolute counts? What are the dangers of not doing so?",
    "Interpreting cell type abundances as proportions rather than absolute counts is essential because the total number of cells can vary between samples; failing to account for this can lead to misleading conclusions, as apparent changes in cell counts might simply reflect differences in sample sizes rather than true biological variations.",
    back_font_size=13,
)
flip_card(
    "q3",
    "In which cases should tools that use cluster information, such as cell types be used, and in which cases tools that do not use cluster information?",
    "Tools that utilize cluster information, such as cell types, are appropriate when distinct clusters are identifiable, allowing for targeted analysis of known populations. Conversely, methods that do not rely on clustering are beneficial when data lacks clear separations, such as during continuous developmental processes, enabling the detection of subtle changes across a spectrum of cell states.",
    back_font_size=12,
)
```

<!-- markdown cell 124 -->
## References

<!-- markdown cell 125 -->
```{bibliography}
:filter: docname in docnames
:labelprefix: comp
```

<!-- markdown cell 126 -->
## Contributors

We gratefully acknowledge the contributions of:

### Authors

* Johannes Ostner
* Emma Dann
* Lukas Heumos
* Anastasia Litinetskaya

### Reviewers
