# Auto-generated from single-cell-best-practices.
# Title: Annotation
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/surface_protein/annotation.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (surface-protein-annotation)=
# # Annotation

# %% [markdown]
# (surface-protein-annotation-key-takeaway-1)=
# ## Motivation
# 
# Similar to scRNA-seq data, it is possible to annotate the ADT data based on surface protein markers. 
# This can be very beneficial for the annotation of immune cells, since they are difficult to annotate in the RNA space and they are well described by their surface proteins. 
# scRNA-seq data can suffer from dropouts, that is, although a gene is expressed in a cell population, the gene is not detected in some cells due to limitations of the sequencing procedure. 
# Instead, ADT data does not suffer so much from dropouts due to using antibodies to quantify surface proteins. 
# Therefore individual surface proteins show a stronger signal in the ADT data than in the RNA data.
# 
# For example, although sequenced immune cells usually include CD45 cells, the CD45 gene is not always highly expressed in the RNA data. 
# This can be mitigated by annotating (additionally) on the ADT level.
# 
# The general annotation workflow makes use of the same functions as for RNA data and no ADT-specific functions are required.

# %% [markdown]
# ## Environment setup

# %%
# Upstream code cell: 4
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
# We load the MuData object we saved at the end of the previous chapter {ref}`surface-protein-batch-correction`:

# %%
# Upstream code cell: 7
af = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="surface-protein/cite_batch_correction.h5mu", is_latest=True
)
mdata = af.load()
mdata

# %% [markdown]
# ## Manual annotation

# %% [markdown]
# First, we check the expression of CD45. 
# CD45 is one of the most abundant proteins in the T-cell plasma membrane and required for TCR signaling. 
# It activates Lck, which in turn is required to phosphorylate the TCR complex {cite}`Courtney2019`. 
# Therefore, CD45 should be broadly expressed in our dataset, and even more highly expressed in T cells.

# %%
# Upstream code cell: 10
sc.pl.umap(mdata["prot"], frameon=False, color="CD45")

# %% [markdown]
# The measured ADTs use a slightly different nomenclature due to name clashes with RNA genes. 
# The `var_names_make_unique` function was used to separate gene names from protein names and the proteins might have `-1` suffixes.
# We look up an example gene name (CD38) to exemplarily find the exact nomenclature in our variable names:

# %%
# Upstream code cell: 12
mdata["prot"].var[mdata["prot"].var.gene_ids.str.contains("CD38")]

# %% [markdown]
# We cluster the cells with a relatively low resolution. 
# Similarly to scRNA-seq data annotation, it is possible to increase the resolution for more fine-grained annotations.

# %%
# Upstream code cell: 14
sc.tl.leiden(
    mdata["prot"],
    resolution=0.1,
    flavor="igraph",
    n_iterations=2,
    directed=False,
    random_state=0,
)

# %% [markdown]
# To check which surface markers are present in which cell type, we use the scanpy rank_genes_groups() function and then we create a dotplot. 
# The dotplot will indicate the 3 most differentially expressed genes in each cluster.

# %%
# Upstream code cell: 16
sc.tl.rank_genes_groups(mdata["prot"], groupby="leiden")
sc.tl.dendrogram(mdata["prot"], groupby="leiden")
sc.pl.rank_genes_groups_dotplot(
    mdata["prot"], n_genes=3, values_to_plot="logfoldchanges"
)

# %% [markdown]
# We can already identify clusters 0 and 2 as T cell populations by CD3 expression, and cluster 7 as B cells by CD19 expression.
# We next plot the UMAP that we calculated in our previous chapters and color it by cluster.

# %%
# Upstream code cell: 18
sc.pl.umap(mdata["prot"], color="leiden")

# %% [markdown]
# We'll check a few known markers of major immune cell types in order to identify which cell type is each cluster.

# %%
# Upstream code cell: 20
# B cells
sc.pl.umap(mdata["prot"], frameon=False, color=["CD19-1"])

# %% [markdown]
# As could be seen in the dotplot, cluster 7 expresses CD19 which is a B cell marker.

# %% [markdown]
# Let's look into the T cells in more detail and separate them into CD4 and CD8 cells.

# %%
# Upstream code cell: 23
# T cells
sc.pl.umap(mdata["prot"], color=["CD3", "CD4-1", "CD8"])

# %% [markdown]
# In the following few plots, we continue looking for known markers of other cell types: NK cells, monocytes and dendritic cells.

# %%
# Upstream code cell: 25
# NKT cells are CD3+ and CD56+
# NK cells are CD3- and CD56+
sc.pl.umap(mdata["prot"], color=["CD56"], frameon=False)

# %%
# Upstream code cell: 26
# Monocytes
sc.pl.umap(mdata["prot"], color=["CD11b", "CD14-1"], frameon=False)

# %%
# Upstream code cell: 27
# Dendritic
sc.pl.umap(mdata["prot"], color=["CD123", "CD11c", "CD303"], frameon=False)

# %%
# Upstream code cell: 28
# CD16 is expressed in NK cells and in CD16 monocytes, which are CD14-, CD16+ and CD11c+
sc.pl.umap(mdata["prot"], color="CD16", frameon=False)

# %% [markdown]
# Now that we know what cell type each cluster is, let's replace the 0-8 cluster numbers with the actual cell type names:

# %%
# Upstream code cell: 30
mdata["prot"].obs["celltype"] = mdata["prot"].obs.leiden.copy()
mdata["prot"].obs.celltype.replace(
    {
        "0": "CD4 T",
        "1": "Cytotoxic T",
        "2": "CD8 T",
        "3": "CD14 Mono",
        "4": "Proliferating cells",
        "5": "DC",
        "6": "CD16 Mono",
        "7": "B",
        "8": "NK",
    },
    inplace=True,
)

# %%
# Upstream code cell: 31
sc.pl.umap(
    mdata["prot"],
    color="celltype",
    legend_loc="on data",
    legend_fontsize=11,
    legend_fontoutline=2,
)

# %% [markdown]
# We have uncovered and annotated the main cell types in the data. 
# Now we could perform a more fine-grained annotation by increasing the resolution of clustering and annotating the resulting fine-grained clusters.
# 
# In this chapter we describe how to annotate cell types based on the ADT data of CITE-seq. 
# Another interesting way forward is to annotate cell types based on combined information from ADT and from RNA data. 
# We refer to the {ref}`multimodal-integration-paired-integration` chapter for that.

# %%
# Upstream code cell: 33
af_annotation = ln.Artifact.from_mudata(
    mdata,
    key="surface-protein/cite_annotation.h5mu",
    description="CITE-seq data after annotation",
)
af_annotation.save()

# %%
# Upstream code cell: 34
ln.finish()

# %% [markdown]
# ## Automated annotation

# %% [markdown]
# It is technically possible to use cell type classifiers trained on ADT data and to map against ADT reference datasets. 
# However, ADT-specific methods are sparse if not non-existent, and we refer to the RNA annotation chapter for methodological details {ref}`cellular-structure-annotation`.

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
