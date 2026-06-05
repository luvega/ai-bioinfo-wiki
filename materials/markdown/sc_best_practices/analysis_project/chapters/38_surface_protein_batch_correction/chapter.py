# Auto-generated from single-cell-best-practices.
# Title: Batch correction
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/surface_protein/batch_correction.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (surface-protein-batch-correction)=
# # Batch correction

# %% [markdown]
# (surface-protein-batch-correction-key-takeaway-1)=
# ## Motivation

# %% [markdown]
# As could be seen for our earlier visualized ADT data, batch effects between donors are very pronounced (see {ref}`surface-protein-dimensionality-reduction`). 
# Hence, batch correction to mitigate this effect is required.
# 
# We use Harmony here. 
# There is no benchmarking of different batch correction methods for ADT data. 
# We therefore use Harmony, a method that has been benchmarked for scRNA-seq data with good results.
# 
# Recently two batch correction methods for ADT data have been published in reputable journals and/or by reputable authors: ADTnorm {cite}`zheng2025adtnorm` and CytoVI {cite}`ingelfinger2025cytovi`. 
# These two methods might be appropriate for ADT data. 
# However, as mentioned, here we stick to Harmony, which is more proven and independently benchmarked (although for transcriptomics and not for ADT data).

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
# We load the MuData object we saved at the end of the previous chapter {ref}`surface-protein-dimensionality-reduction`:

# %%
# Upstream code cell: 8
af = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="surface-protein/cite_dimensionality_reduction.h5mu", is_latest=True
)
mdata = af.load()
mdata

# %% [markdown]
# ## Harmony

# %% [markdown]
# It is not yet clear which batch effect correction works best for ADT data. 
# For general purposes we recommend Harmony {cite}`Korsunsky2019` to perform batch correction of the data due to its robust performance on scRNA-seq data.

# %%
# Upstream code cell: 11
sc.external.pp.harmony_integrate(adata=mdata["prot"], key="donor", random_state=0)

# %% [markdown]
# We now compute a neighborhood graph from the Harmony-corrected PCA and a UMAP embedding to visualize the study's variables.

# %%
# Upstream code cell: 13
sc.pp.neighbors(mdata["prot"], n_pcs=20, use_rep="X_pca_harmony", random_state=0)
sc.tl.umap(mdata["prot"], random_state=0)

# %%
# Upstream code cell: 14
sc.pl.umap(mdata["prot"], color=["donor", "batch"])

# %% [markdown]
# As we can see here, the cells of different donors are much more intermixed in the embedding than before (see plots from the {ref}`surface-protein-dimensionality-reduction` chapter).

# %%
# Upstream code cell: 16
sc.pl.umap(mdata["prot"], color=["CD4-1", "CD8", "CD3"])
sc.pl.umap(mdata["prot"], color=["CD14-1", "CD16"])

# %% [markdown]
# We check the expression of a few marker genes to confirm that separate cell types are still separate from each other. 
# We can see that T cells still form a separate population that is further split into CD4 and CD8 T cells. 
# Additionally, unlike before dimensionality reduction, now CD4 T cells form a discrete cluster where the donors are intermingled. 
# Batch correction was therefore successful.

# %%
# Upstream code cell: 18
af_batch_correction = ln.Artifact.from_mudata(
    mdata,
    key="surface-protein/cite_batch_correction.h5mu",
    description="CITE-seq data after batch correction",
)
af_batch_correction.save()

# %%
# Upstream code cell: 19
ln.finish()

# %% [markdown]
# ## References

# %% [markdown]
# ```{bibliography}
# :filter: docname in docnames
# :labelprefix: sp
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
