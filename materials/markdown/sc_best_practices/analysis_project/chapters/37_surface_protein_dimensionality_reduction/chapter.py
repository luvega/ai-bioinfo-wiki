# Auto-generated from single-cell-best-practices.
# Title: Dimensionality Reduction
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/surface_protein/dimensionality_reduction.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (surface-protein-dimensionality-reduction)=
# # Dimensionality Reduction

# %% [markdown]
# (surface-protein-dimensionality-reduction-key-takeaway-1)=
# ## Motivation

# %% [markdown]
# Feature matrices of surface protein markers are hard to grasp for humans as raw tables.
# Therefore, we resort to low dimensional embeddings that allow us to visualize the ADTs in commonly two dimensions.
# The approaches that we use and recommend for ADT data do not differ from the ones for transcriptomics data.
# All aforementioned limitations of visualizations obtained through methods like t-SNE and UMAP also apply to ADT data.
# 
# ADT data generally does not require any sophisticated feature selection, because features have already been selected a *priori* during experimental design.
# All selected ADTs should correspond to biologically relevant features.
# Nevertheless, large datasets may benefit from PCA to reduce the dataset from several hundred features to a few principal components.
# This is especially advisable if computational resources are limited.
# 
# In this and the following two chapters, we decided to focus on the ADT data and do not use the RNA data of the study. 
# In the {ref}`multimodal-integration-paired-integration` chapter, we will explore how we can make use of both modalities jointly, which allows for a more detailed cell type annotation.

# %% [markdown]
# ## Environment setup

# %%
# Upstream code cell: 5
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

# %% [markdown]
# ## Loading the data

# %% [markdown]
# We load the MuData object we saved at the end of the previous chapter {ref}`surface-protein-doublet-detection`:

# %%
# Upstream code cell: 8
af = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="surface-protein/cite_doublet_detection.h5mu", is_latest=True
)
mdata = af.load()
mdata

# %% [markdown]
# We remove the counts layer containing the raw data since we do not need it anymore.

# %%
# Upstream code cell: 10
del mdata["prot"].layers["counts"]

# %% [markdown]
# Isotype controls do not contain any biological information since their only purpose is to use them for dsb normalization, see the {ref}`surface-protein-normalization` section. 
# We can therefore remove them from our data.

# %%
# Upstream code cell: 12
mdata["prot"].var.index[:50]

# %%
# Upstream code cell: 13
isotype_controls = ["Mouse-IgG1", "Mouse-IgG2a", "Mouse-IgG2b", "Rat-IgG2b"]
temp = (
    mdata["prot"].var.loc[~mdata["prot"].var.index.isin(isotype_controls), :].index
)  # Select all proteins except isotype controls.

# %% [markdown]
# Now we actually remove isotype controls from the data.

# %%
# Upstream code cell: 15
mu.pp.filter_var(data=mdata["prot"], var=temp.tolist())

# %% [markdown]
# The data does not contain the isotype controls anymore.

# %%
# Upstream code cell: 17
mdata["prot"].var.index[:50]

# %%
# Upstream code cell: 18
mdata["prot"]

# %% [markdown]
# ## PCA and UMAP

# %% [markdown]
# We can now reduce the dimensionality of the data with PCA since our dataset is quite big (136 surface proteins).

# %%
# Upstream code cell: 21
sc.pp.pca(mdata["prot"], svd_solver="arpack", random_state=0)

# %% [markdown]
# We create an elbow plot in order to decide how many PCs we use:

# %%
# Upstream code cell: 23
sc.pl.pca_variance_ratio(mdata["prot"], n_pcs=50)

# %% [markdown]
# We use 20 PCs because PCs 1-20 capture much of the variance in the data and PCs 20-50 capture little variance of the data and can thus be discarded. 
# We now compute a neighborhood graph and a UMAP embedding to visualize the study's variables.

# %%
# Upstream code cell: 25
sc.pp.neighbors(mdata["prot"], n_pcs=20, random_state=0)

# %%
# Upstream code cell: 26
sc.tl.umap(mdata["prot"], random_state=0)

# %% [markdown]
# Now we have our data compressed into 2 dimensions, which we can use to visualize the data.
# Let's first visualize and evaluate if there are batch effects, that is, if different donors and different batches form separate clusters.

# %%
# Upstream code cell: 28
sc.pl.umap(mdata["prot"], color=["donor", "batch"])

# %% [markdown]
# We indeed see that some donors form separate clusters. 
# Also batches form separate clusters. 
# Thus, it seems that batch correction is necessary. 
# To confirm, we plot markers of CD4 and CD8 T cells:

# %%
# Upstream code cell: 30
sc.pl.umap(mdata["prot"], color=["CD4-1", "CD8", "CD3"])

# %% [markdown]
# CD4 T cells fragment into donor-specific mini-clusters, meaning cells are grouping by donor identity rather than cell type. 
# Ideally, CD4 T cells from all donors should cluster together regardless of their donor of origin. 
# This donor-driven separation is a batch effect, and must be corrected before downstream analysis.

# %%
# Upstream code cell: 32
af_dimensionality_reduction = ln.Artifact.from_mudata(
    mdata,
    key="surface-protein/cite_dimensionality_reduction.h5mu",
    description="CITE-seq data after dimensionality reduction",
)
af_dimensionality_reduction.save()

# %%
# Upstream code cell: 33
ln.finish()

# %% [markdown]
# ## References

# %% [markdown]
# ```{bibliography}
# :filter: docname in docnames
# ```

# %% [markdown]
# ## Contributors
# 
# We gratefully acknowledge the contributions of:
# 
# ### Authors
# 
# * Javier Marchena-Hurtado
# * Daniel Strobl
# * Ciro Ramírez-Suástegui
# 
# ### Reviewers
# 
# * Lukas Heumos
# * Anna Schaar
