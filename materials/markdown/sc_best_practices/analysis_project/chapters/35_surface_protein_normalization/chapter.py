# Auto-generated from single-cell-best-practices.
# Title: Normalization
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/surface_protein/normalization.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (surface-protein-normalization)=
# # Normalization

# %% [markdown]
# (surface-protein-normalization-key-takeaway-1)=
# ## Motivation

# %% [markdown]
# Similarly to scRNA-seq data, ADT data also contains noise that needs to be removed. 
# The main sources of noise are 1) sequencing depth differences between cells, 2) unspecific binding of antibodies, 3) ambient noise. 
# We aim to remove these sources of noise with normalization techniques.
# 
# Contrary to the negative binomial distribution of UMI counts, ADT data is less sparse with a negative peak for non-specific antibody binding and a positive peak resembling enrichment of specific cell surface proteins{cite}`Zheng2022`.
# The capture efficiency varies from cell to cell due to differences in biophysical properties. 
# Since CITE-seq experiments enrich for a priori selected features, compositional biases are more severe.
# 
# Analogously to scRNA-seq data, many approaches to normalization exist. 
# We cover the two most widely used methods.
# 
# The traditional way to normalize ADT data, which we cover at the end of this normalization notebook, is using Centered Log-Ratio (CLR) transformation {cite}`Stoeckius2017`. 
# Nevertheless, a new low-level normalization method specifically tailored to dealing with the challenges this modality poses now exists: dsb (denoised and scaled by background) {cite}`Mulè2022`. 
# dsb normalization removes two kinds of noise:
# 
# - First, dsb normalization uses empty droplets to estimate and to remove ambient noise. 
# This ambient noise arises from free-floating proteins in the solution that are not actually part of a cell. 
# These proteins are most often the result of cell debris from broken cells and are said to be part of the "ambient". 
# By measuring ADT counts in empty droplets, dsb models the ambient protein levels for each antibody and subtracts this background from droplets containing cells.
# - Secondly, dsb normalization uses isotype controls to remove noise from unspecific binding. 
# Isotype controls are antibodies that unspecifically bind to many proteins. 
# This information is then used to correct noise arising from unspecific interactions.

# %% [markdown]
# ## Environment setup

# %%
# Upstream code cell: 5
import warnings

import matplotlib.pyplot as plt
import muon as mu
import pandas as pd
import scanpy as sc
import seaborn as sns

warnings.filterwarnings("ignore")
mu.set_options(pull_on_update=False)
sc.settings.verbosity = 0
sc.set_figure_params(dpi=80, facecolor="white", frameon=False)

import lamindb as ln

ln.track()

# %% [markdown]
# ## Loading the data

# %% [markdown]
# We load the MuData object we saved at the end of the previous chapter {ref}`surface-protein-quality-control`:

# %%
# Upstream code cell: 8
af = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="surface-protein/cite_quality_control.h5mu",
    is_latest=True,
)
mdata = af.load()
mdata

# %% [markdown]
# Next, we also load the unfiltered data containing empty droplets for dsb normalization. 
# `mdata_raw` contains the unfiltered MuData object with all droplets and `mdata` contains barcodes that passed the cellranger filtering and our quality control. 
# While the raw object contains over 24 million droplets, the filtered object only contains 118,563.

# %%
# Upstream code cell: 10
af_raw = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="surface-protein/cite_raw.h5mu",
    is_latest=True,
)
mdata_raw = af_raw.load()
mdata_raw

# %% [markdown]
# ## dsb normalization

# %% [markdown]
# dsb normalization {cite}`Mulè2022` is quite effective in removing noise from ADT data. 
# However, dsb normalization requires two additional sources of data: 1) empty droplets (in this tutorial they are part of the "cite_raw.h5mu" dataset) and 2) isotype controls. 
# If you have neither of these two additional sources of data, you cannot use dsb normalization; in this case we recommend using CLR normalization, which we outline at the end of this normalization section. 
# If you have only one of these additional sources of data, you can use only one of the steps of dsb normalization (not described in this tutorial). 
# If you have both additional sources of data, you can use dsb normalization as outlined in this tutorial.
# 
# Isotype controls are antibodies that bind to the cells present in this study non-specifically, meaning you would not expect a significant abundance difference between the cells. 
# Thus, we can use the values of the isotype controls to normalize technical differences.
# 
# Let's first take a look at the raw RNA count distribution in order to tell what droplets are empty droplets and what droplets do contain cells:

# %%
# Upstream code cell: 13
sc.pp.calculate_qc_metrics(mdata_raw["rna"], inplace=True, percent_top=None)
sns.displot(
    mdata_raw["rna"]
    .obs.sample(frac=0.01)
    .query("total_counts<100000 and total_counts>10"),
    x="total_counts",
    log_scale=True,
    hue="donor",
    multiple="stack",
)

# %% [markdown]
# The first large peak between 10\*\*1 and 10\*\*2.1 is composed of droplets that don't contain cells. 
# We can use these cells for dsb normalization. 
# In this case, the pre-processing software (often CellRanger) already differentiated droplets that contain cells and sorted them into the filtered data, here represented by the "mdata" object. 
# Instead, the unfiltered data, here represented by the "mdata_raw" object, contains all droplets, both with and without cells. 
# dsb normalization will use droplets without cells in order to estimate ambient noise and then remove it.
# 
# Additionally, we also now explicitly list the isotype controls that dsb normalization will use to remove noise from unspecific binding.

# %%
# Upstream code cell: 15
isotype_controls = ["Mouse-IgG1", "Mouse-IgG2a", "Mouse-IgG2b", "Rat-IgG2b"]

# %%
# Upstream code cell: 16
mdata["prot"].layers["counts"] = mdata[
    "prot"
].X.copy()  # saving the raw data in a layer.

# %% [markdown]
# We now call the normalization function `mu.prot.pp.dsb` with the filtered and raw mudata object as well as the names of the isotype controls.

# %%
# Upstream code cell: 18
mu.prot.pp.dsb(mdata, mdata_raw, isotype_controls=isotype_controls, random_state=0)

# %% [markdown]
# Let's have a look at counts before denoising and normalization.

# %%
# Upstream code cell: 20
pd.Series(mdata["prot"].layers["counts"][:100, :100].toarray().flatten()).value_counts()

# %% [markdown]
# See how after denoising and normalization the range changed.

# %%
# Upstream code cell: 22
pd.Series(mdata["prot"].X[:100, :100].flatten()).value_counts()

# %% [markdown]
# Now let's take a look at how total protein counts of each cell changed before and after dsb normalization:

# %%
# Upstream code cell: 24
sns.histplot(mdata["prot"].layers["counts"].sum(axis=1), bins=50)
plt.title("Total counts per cell (raw)")
plt.xlim(0, 20000)

# %% [markdown]
# Before normalization, many cells have quite low total protein counts, while some cells have very high total protein counts. 
# These very large differences in total protein counts are largely driven by ambient noise and unspecific binding.

# %%
# Upstream code cell: 26
sns.histplot(mdata["prot"].X.sum(axis=1), bins=50)
plt.title("Total counts per cell (dsb normalized)")
plt.xlim(-200, 300)

# %% [markdown]
# After normalization, the differences in total protein counts are much smaller and (probably) biology-driven rather than noise-driven.

# %% [markdown]
# ## Centered Log-Ratio normalization

# %% [markdown]
# If you don't have the unfiltered data and/or the isotype controls available, you can also normalize the ADT data with `mu.prot.pp.clr`, implementing **C**entered **L**og-**R**atio normalization. 
# CLR normalization is the traditional way of normalizing ADT data, suggested in the original CITE-seq publication {cite}`Stoeckius2017`. 
# 
# CLR normalization accounts for differences in sequencing depth across cells, which can otherwise dominate downstream analyses. Cells with higher total ADT counts may appear artificially distinct, causing biologically similar cells to separate during clustering.
# CLR normalization rescales protein expression within each cell, making total protein counts more similar in all cells. 
# Specifically, it divides each protein count by the geometric mean of all protein counts in that cell and applies a log transformation.

# %%
# Upstream code cell: 30
mdata_clr_normalize = mdata.copy()
mdata_clr_normalize["prot"].X = mdata_clr_normalize["prot"].layers["counts"].copy()

# %% [markdown]
# Now we apply CLR normalization by using the function `mu.prot.pp.clr`:

# %%
# Upstream code cell: 32
mu.prot.pp.clr(mdata_clr_normalize["prot"])

# %% [markdown]
# We compare the counts before and after normalization:

# %%
# Upstream code cell: 34
pd.Series(mdata["prot"].layers["counts"][:100, :100].toarray().flatten()).value_counts()

# %%
# Upstream code cell: 35
pd.Series(mdata_clr_normalize["prot"].X[:100, :100].toarray().flatten()).value_counts()

# %% [markdown]
# And we plot the distribution of total protein counts per cell:

# %%
# Upstream code cell: 37
sns.histplot(mdata_clr_normalize["prot"].X.sum(axis=1), bins=50)
plt.title("Total counts per cell (CLR normalized)")
plt.xlim(0, 400)

# %% [markdown]
# CLR normalization successfully reduced the difference in total protein counts. 
# The range of total protein counts goes from 0 to 350, which is reasonable. 
# If we compare this range with the range of differences in total protein counts in the raw data, which went from 0 to 20000, CLR normalization alleviated some of those differences, which were largely driven by experimental noise.

# %% [markdown]
# We save our dsb-normalized CITE-seq data, since dsb normalization is our method of choice when isotype controls and empty droplet data is available.

# %%
# Upstream code cell: 40
af_normalization = ln.Artifact.from_mudata(
    mdata,
    key="surface-protein/cite_normalization.h5mu",
    description="CITE-seq data after normalization",
)
af_normalization.save()

# %%
# Upstream code cell: 41
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
