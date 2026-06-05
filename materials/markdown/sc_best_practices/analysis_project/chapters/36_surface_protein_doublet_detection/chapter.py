# Auto-generated from single-cell-best-practices.
# Title: Doublet detection
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/surface_protein/doublet_detection.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (surface-protein-doublet-detection)=
# # Doublet detection

# %% [markdown]
# (surface-protein-doublet-detection-key-takeaway-1)=
# ## Motivation

# %% [markdown]
# In the {ref}`surface-protein-quality-control` chapter, we removed cells that potentially reflect doublets based only on their high count content. 
# We also filtered cells based on sample-wise distribution. 
# Now, we will focus on heterotypic doublets, that is, doublets that contain cells from different cell types. 
# With ADT data, we can detect them using cell type specific surface markers{cite}`Sun2021`.

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
# We load the MuData object we saved at the end of the previous chapter {ref}`surface-protein-normalization`:

# %%
# Upstream code cell: 8
af = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="surface-protein/cite_normalization.h5mu", is_latest=True
)
mdata = af.load()
mdata

# %% [markdown]
# ## Doublets detected with cell type markers

# %% [markdown]
# We are now going to look at cell type markers that are mutually exclusive. 
# Some examples are CD3 (T cell marker) vs CD19 (B cell marker) to identify T/B cells doublets.
# As cells expressing both specific B and T cell markers do not exist under physiological conditions, those droplets contain T/B cell doublets.
# 
# The same is true for cells expressing both T cell (CD3) and monocyte (CD14) markers.

# %%
# Upstream code cell: 11
sc.pl.scatter(mdata["prot"], x="CD3", y="CD19-1", color="log1p_total_counts")

# %% [markdown]
# In this plot, we can see a large number of cells not expressing T or B cell markers in the lower left, cells expressing only one marker in the upper left and lower right as well as some cells expressing both markers (upper right).
# 
# The cells expressing both markers are doublets and can be removed.

# %% [markdown]
# We can also use CD3 and CD14 to detect T/monocyte doublets.

# %%
# Upstream code cell: 14
sc.pl.scatter(mdata["prot"], x="CD3", y="CD14-1", color="log1p_total_counts")

# %% [markdown]
# It looks like cells that have an expression level above 2.5 in both markers are doublets. 
# We use an expression level above 2.5 in both markers to flag doublets.

# %%
# Upstream code cell: 16
genes2filter = ["CD3", "CD19-1", "CD14-1"]
temp = mdata["prot"][:, genes2filter].X.T.tolist()

# %%
# Upstream code cell: 17
mdata["prot"].obs["doublets_markers"] = [
    (temp[0][i] > 2.5 and temp[1][i] > 2.5) or (temp[0][i] > 2.5 and temp[2][i] > 2.5)
    for i in range(mdata.shape[0])
]
mdata["prot"].obs["doublets_markers"] = (
    mdata["prot"].obs["doublets_markers"].astype(str)
)

# %% [markdown]
# Doublets usually have a higher count due to the presence of increased counts from more than one cell. 
# We can see this effect in the cells classified as doublets using our markers:

# %%
# Upstream code cell: 19
sc.pl.violin(mdata["prot"], keys="log1p_total_counts", groupby="doublets_markers")

# %% [markdown]
# We leave out cells expressing both markers.

# %%
# Upstream code cell: 21
mdata = mdata[mdata["prot"].obs["doublets_markers"] == "False"].copy()
mdata

# %% [markdown]
# We removed 612 doublets from the data.
# 
# In this chapter, we removed doublets using the ADT data by removing cells that highly expressed two mutually exclusive markers. 
# Another option to remove doublets would be utilizing methods that detect doublets based on the scRNA-seq data. 
# For those methods, we refer to the {ref}`rna:doublet-detection` chapter of scRNA-seq preprocessing and visualization.

# %%
# Upstream code cell: 23
af_doublet_detection = ln.Artifact.from_mudata(
    mdata,
    key="surface-protein/cite_doublet_detection.h5mu",
    description="CITE-seq data after doublet detection",
)
af_doublet_detection.save()

# %%
# Upstream code cell: 24
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
