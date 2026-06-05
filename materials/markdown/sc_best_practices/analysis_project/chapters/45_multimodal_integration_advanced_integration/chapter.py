# Auto-generated from single-cell-best-practices.
# Title: Advanced integration
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/multimodal_integration/advanced_integration.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (multimodal-integration:advanced-integration)=
# # Advanced integration

# %% [markdown]
# (multimodal-integration-advanced-integration-key-takeaway-1)=
# ## Motivation
# 
# In this notebook, we showcase more advanced methods and techniques for multimodal integration. Examples of such advanced techniques are unpaired integration, integration of partially overlapping data or multimodal query-to-reference mapping. These are especially useful when the measurements of various modalities were not done jointly per cell, but originate from different experiments. 
# 
# We discuss each of these cases in more detail in the corresponding sections below.

# %% [markdown]
# ## Environment setup

# %%
# Upstream code cell: 4
import logging

import anndata
import anndata2ri
import multigrate as mtg
import networkx as nx
import numpy as np
import pandas as pd
import rpy2.rinterface_lib.callbacks
import scanpy as sc
import scglue
from rpy2.robjects import pandas2ri, r
from scvi.model import TOTALVI

rpy2.rinterface_lib.callbacks.logger.setLevel(logging.ERROR)

pandas2ri.activate()
anndata2ri.activate()

%load_ext rpy2.ipython

import warnings

warnings.filterwarnings("ignore")

# %% [markdown]
# If you want to run Seurat bridge integration, please additionally install the developmental version of Seurat package with separately using `remotes::install_github("satijalab/seurat", "feat/dictionary", quiet = TRUE)` or `devtools::install_github("https://github.com/satijalab/seurat/tree/feat/dictionary")` command.

# %%
# Upstream code cell: 6
%%R
suppressPackageStartupMessages({
    library(SingleCellExperiment)
    library(Seurat)
})
set.seed(123)

# %% [markdown]
# ## Prepare data
# We continue using Multiome and CITE-seq data from the NeurIPS 2021 single cell competition {cite}`ai:luecken2021sandbox`. 
# 
# We will need:
# - RNA-seq part of the multiome and ADT from the CITE-seq data for unpaired integration with [GLUE](#glue)
# - paired gene expression and protein from the CITE-seq data for query-to-reference mapping with [totalVI](#totalvi)
# - RNA-seq query from the CITE-seq data for query mapping with [Seurat v4](#seurat)
# - CITE-seq data for [bridge](#bridge) mapping
# - NeurIPS multiome and NeurIPS CITE-seq for trimodal integration and query-to-reference mapping with [multigrate](#multigrate)
# 
# Since we showcase query-to-reference mapping functionality of some methods, we split the data into a reference and a query. For the methods that we only use for integration, we also use the reference batches. 
# 
# We note that the batch names for Multiome and CITE-seq data are the same, but they are actually not the same cells.

# %%
# Upstream code cell: 8
cite_reference_batches = [
    "s1d1",
    "s1d2",
    "s1d3",
]  # need for totalVI, multigrate and bridge (RNA part)
multiome_reference_batches = ["s1d1", "s1d2", "s1d3"]  # need for GLUE and multigrate
cite_query_batches = ["s2d1", "s2d4"]  # need for totalVI, multigrate and bridge
multiome_query_batches = ["s2d1", "s2d4"]  # need for multigrate

# %%
# Upstream code cell: 9
rna_multiome = sc.read(
    "/lustre/groups/ml01/workspace/anastasia.litinetskaya/data/neurips-multiome/rna_hvg.h5ad"
)
rna_multiome

# %%
# Upstream code cell: 10
atac_multiome = sc.read(
    "/lustre/groups/ml01/workspace/anastasia.litinetskaya/data/trimodal_neurips/atac_hvf_muon.h5ad"
)
atac_multiome

# %%
# Upstream code cell: 11
rna_cite = sc.read(
    "/lustre/groups/ml01/workspace/anastasia.litinetskaya/data/neurips-cite/rna_hvg.h5ad"
)
rna_cite

# %%
# Upstream code cell: 12
adt_cite = sc.read("/lustre/groups/ml01/workspace/daniel.strobl/neurips_cite_pp.h5ad")
adt_cite

# %% [markdown]
# There are some differences in `.obs_names` of RNA and ADT of CITE-seq data, so we update them to make sure they align between modalities.

# %%
# Upstream code cell: 14
rna_cite.obs_names

# %%
# Upstream code cell: 15
adt_cite.obs_names

# %%
# Upstream code cell: 16
adt_cite.obs_names = [
    name.split("-")[0] + "-" + name.split("-")[1] + "-" + batch
    for batch, name in zip(adt_cite.obs["donor"], adt_cite.obs_names, strict=False)
]

# %% [markdown]
# We subset to the cells that are present in both modalities.

# %%
# Upstream code cell: 18
common_idx = list(set(rna_cite.obs_names).intersection(set(adt_cite.obs_names)))
rna_cite = rna_cite[common_idx].copy()
adt_cite = adt_cite[common_idx].copy()

# %% [markdown]
# We also copy some of the metadata from RNA to ADT.

# %%
# Upstream code cell: 20
adt_cite.obs = adt_cite.obs.join(rna_cite.obs[["Samplename", "cell_type"]])

# %% [markdown]
# Also we make sure that cells are the same in multiome data.

# %%
# Upstream code cell: 22
assert np.sum(rna_multiome.obs_names != atac_multiome.obs_names) == 0

# %% [markdown]
# Because batch names are the same for different modalities and datasets, we will need to update a bunch of batch columns in `.obs` so we create a helper function for this.

# %%
# Upstream code cell: 24
def update_obs_column(
    adata, obs_column_name, suffix, how="right", new_obs_column_name=None
):
    if new_obs_column_name is None:
        new_obs_column_name = f"new_{obs_column_name}"
    # otherwise can't use + operator with categorical columns
    adata.obs[obs_column_name] = adata.obs[obs_column_name].astype("str").copy()
    # create new column in .obs
    if how == "right":
        adata.obs[new_obs_column_name] = f"_{suffix}"
        adata.obs[new_obs_column_name] = (
            adata.obs[obs_column_name] + adata.obs[new_obs_column_name]
        )
    else:
        adata.obs[new_obs_column_name] = f"{suffix}_"
        adata.obs[new_obs_column_name] = (
            adata.obs[new_obs_column_name] + adata.obs[obs_column_name]
        )
    return adata

# %%
# Upstream code cell: 25
rna_multiome = update_obs_column(rna_multiome, "batch", "_rna_multiome")
atac_multiome = update_obs_column(atac_multiome, "batch", "_atac_multiome")
rna_cite = update_obs_column(rna_cite, "batch", "_rna_cite")
adt_cite = update_obs_column(adt_cite, "donor", "_adt_cite", "batch")

# %% [markdown]
# Finally we subset to the correct batches the reference datasets and the query.

# %%
# Upstream code cell: 27
# query
rna_multiome_query = rna_multiome[
    rna_multiome.obs["batch"].isin(multiome_query_batches)
].copy()
atac_multiome_query = atac_multiome[
    atac_multiome.obs["batch"].isin(multiome_query_batches)
].copy()
rna_cite_query = rna_cite[rna_cite.obs["batch"].isin(cite_query_batches)].copy()
adt_cite_query = adt_cite[adt_cite.obs["donor"].isin(cite_query_batches)].copy()
# reference
rna_multiome = rna_multiome[
    rna_multiome.obs["batch"].isin(multiome_reference_batches)
].copy()
atac_multiome = atac_multiome[
    atac_multiome.obs["batch"].isin(multiome_reference_batches)
].copy()
rna_cite = rna_cite[rna_cite.obs["batch"].isin(cite_reference_batches)].copy()
adt_cite = adt_cite[adt_cite.obs["donor"].isin(cite_reference_batches)].copy()

# %% [markdown]
# <a id='glue'></a>
# ## Unpaired integration with Graph Linked Unified Embedding (GLUE)

# %% [markdown]
# Opposed to paired integration that we demonstrated before, it is also possible to perform completely unpaired integration. In this case, there is no intersection of cell barcodes or features. Hence, we need some prior knowledge to connect different modalities.
# 
# GLUE {cite}`cao2022` is a deep learning model for unpaired integration which makes use of a regulatory graph helping connect features from different modalities. The model is based on conditional variational autoencoders, where the model learns to reconstruct while simultaneously allowing for batch correction. To guide the integration, GLUE learns an embedding for each modality for each feature by utilizing a prior knowledge graph. We demonstrate how to use GLUE to integrate unpaired RNA and ADT data using RNA part of Multiome data and ADT part of CITE-seq data from the NeurIPS competition (https://openproblems.bio/neurips_2021/). To construct the graph, we connect nodes from RNA modality to nodes from ADT modality if and only if the RNA node is a protein encoding gene of a given protein from ADT modality. The output of the GLUE model is a representation of each cell in a shared latent space. 
# 
# We refer the reader to GLUE tutorial to see how one can integrate unpaired RNA and ATAC with GLUE and for more details about the model https://scglue.readthedocs.io/en/latest/tutorials.html.

# %% [markdown]
# We follow the GLUE tutorial on how to preprocess RNA-seq. We log-normalize the raw counts, scale and calculate PCA.

# %%
# Upstream code cell: 31
rna_multiome.X = rna_multiome.layers["counts"].copy()
sc.pp.normalize_total(rna_multiome)
sc.pp.log1p(rna_multiome)
sc.pp.scale(rna_multiome)
sc.tl.pca(rna_multiome, n_comps=100, svd_solver="auto")

# %% [markdown]
# For ADT counts, we use CLR-normalized counts from `.X` and PCA calculated on the normalized values.

# %%
# Upstream code cell: 33
np.max(adt_cite.X)

# %%
# Upstream code cell: 34
sc.tl.pca(adt_cite, n_comps=100, svd_solver="auto")

# %% [markdown]
# We need to make sure that protein encoding gene names and the corresponding protein names align in both data objects. We will need this later for the graph construction.

# %%
# Upstream code cell: 36
rename_proteins = {
    "CD103": "ITGAE",
    "CD11b": "ITGAM",
    "CD11c": "ITGAX",
    "CD122": "IL2RB",
    "CD124": "IL4R",
    "CD127": "IL7R",
    "CD13": "ANPEP",
    "CD137": "TNFRSF9",
    "CD152": "CTLA4",
    "CD154": "CD40LG",
    "CD16": "FCGR3A",
    "CD161": "KLRB1",
    "CD185": "CXCR5",
    "CD194": "CCR4",
    "CD196": "CCR6",
    "CD20": "MS4A1",
    "CD21": "CR2",
    "CD23": "FCER2",
    "CD25": "IL2RA",
    "CD26": "DPP4",
    "CD268": "TNFRSF13C",
    "CD272": "BTLA",
    "CD278": "ICOS",
    "CD29": "ITGB1",
    "CD3": "CD3G",
    "CD303": "CLEC4C",
    "CD304": "NRP1",
    "CD314": "KLRK1",
    "CD319": "SLAMF7",
    "CD335": "NCR1",
    "CD35": "CR1",
    "CD352": "SLAMF6",
    "CD39": "ENTPD1",
    "CD49a": "ITGA1",
    "CD49f": "ITGA6",
    "CD54": "ICAM1",
    "CD56": "NCAM1",
    "CD62L": "SELL",
    "CD71": "TFRC",
    "CD73": "NT5E",
    "CD79b": "CD79B",
    "CD8": "CD8A",
    "CD85j": "LILRB1",
    "CD88": "C5AR1",
    "CD94": "KLRD1",
    "CD95": "FAS",
    "HLA-DR": "HLA-DRA",
    "IgD": "IGHD",
    "IgM": "IGHM",
    "TCR": "TRAC",
}

# %%
# Upstream code cell: 37
adt_cite.var_names = [
    rename_proteins[name] if name in rename_proteins else name
    for name in adt_cite.var_names
]

# %% [markdown]
# ### Graph construction
# 
# Before we can run GLUE integration, we need to construct a graph with prior knowledge on how feature from the two modalities are connected. The node set has to be the union of the features from all the modalities, and the edge weights have to between 0 and 1. To integrate ADT with RNA, we construct the graph the following way: we set the edge weight to 1 if the protein name is the same as the gene name and 0 for all the other edges.

# %%
# Upstream code cell: 39
p = np.array(adt_cite.var_names)
r = np.array(rna_multiome.var_names)  # noqa F811
# mask entries are set to 1 where protein name is the same as gene name
mask = np.repeat(p.reshape(-1, 1), r.shape[0], axis=1) == r
mask = np.array(mask)

# %% [markdown]
# We rename the features so they differ for ADT and RNA modalities.

# %%
# Upstream code cell: 41
rna_vars = [v + "_rna" for v in rna_multiome.var_names]
prot_vars = [v + "_prot" for v in adt_cite.var_names]
rna_multiome.var_names = rna_vars
adt_cite.var_names = prot_vars

# %% [markdown]
# GLUE also requires each node to have a self-loop with weight 1, so we add these here too.

# %%
# Upstream code cell: 43
adj = pd.DataFrame(mask, index=prot_vars, columns=rna_vars)
diag_edges = adj[adj > 0].stack().index.tolist()
diag_edges = [(n1, n2, {"weight": 1.0, "sign": 1}) for n1, n2 in diag_edges]
self_loop_rna = [(g, g, {"weight": 1.0, "sign": 1}) for g in rna_vars]
self_loop_prot = [(g, g, {"weight": 1.0, "sign": 1}) for g in prot_vars]

# %% [markdown]
# Next we construct the actual graph object.

# %%
# Upstream code cell: 45
graph = nx.Graph()
graph.add_nodes_from(rna_vars)
graph.add_nodes_from(prot_vars)
graph.add_edges_from(diag_edges)
graph.add_edges_from(self_loop_prot)
graph.add_edges_from(self_loop_rna)

# %% [markdown]
# We have a graph with 4136 nodes which corresponds to 4000 genes and 136 proteins. We also have 4186 edges with non-zero weights: 4136 self-loops and 50 connections between genes and proteins with the same name.

# %%
# Upstream code cell: 47
graph.number_of_nodes(), graph.number_of_edges()

# %% [markdown]
# ### Configure data
# 
# In this section we again follow the GLUE tutorial to configure the model. First, we set up the RNA encoder-decoder pair to learn to reconstruct raw counts that we assume follow NB distribution. We specify PCA embedding to be used within the encoder.

# %%
# Upstream code cell: 49
scglue.models.configure_dataset(
    rna_multiome,
    "NB",
    use_highly_variable=False,
    use_batch="Samplename",
    use_layer="counts",
    use_rep="X_pca",
)

# %% [markdown]
# Next, we set up the ADT encoder and decoder to reconstruct normalized counts following the normal distribution and  to use PCA embeddings.

# %%
# Upstream code cell: 51
scglue.models.configure_dataset(
    adt_cite,
    "Normal",
    use_highly_variable=False,
    use_batch="Samplename",
    use_rep="X_pca",
)

# %% [markdown]
# We initialize and train the final model.

# %%
# Upstream code cell: 53
glue = scglue.models.fit_SCGLUE(
    {"rna": rna_multiome, "adt": adt_cite},
    graph,
)

# %% [markdown]
# Now we can obtain the latent representation for both modalities and concatenate them into one AnnData object for later visualization.

# %%
# Upstream code cell: 55
rna_multiome.obsm["X_glue"] = glue.encode_data("rna", rna_multiome)
adt_cite.obsm["X_glue"] = glue.encode_data("adt", adt_cite)

# %%
# Upstream code cell: 56
adt_cite.obs["modality"] = "ADT"
rna_multiome.obs["modality"] = "RNA"

combined = anndata.concat([rna_multiome, adt_cite])

# %% [markdown]
# Finally, we visualize the integrated latent space.

# %%
# Upstream code cell: 58
sc.pp.neighbors(combined, use_rep="X_glue", metric="cosine")
sc.tl.umap(combined)

# %%
# Upstream code cell: 59
sc.pl.umap(
    combined, color=["cell_type", "modality", "Samplename"], ncols=1, frameon=False
)

# %% [markdown]
# We see that the batches were well integrated as well as the two modalities. Yet again, scIB could be used to evaluate the integration.

# %% [markdown]
# <a id='totalvi'></a>
# (multimodal-integration-advanced-integration-key-takeaway-2)=
# ## Integration with partially overlapping data and query-to-reference mapping with totalVI
# 
# Another multimodal data integration scenario is when we have paired and unpaired data available at the same time, for instance, a CITE-seq and an RNA-seq datasets. This scenario is also known as mosaic integration. We might be interested in mapping the datasets into a shared latent space to make use of all the data available to us. Another use case would be to impute missing modalities (i.e. proteins abundance for RNA-seq dataset). We show how to perform these two tasks, partially overlapping integration and imputation, using totalVI {cite}`pi:gayoso2021`.
# 
# We set the protein counts of one of the batches to zeros to model the missing proteins. This helps later with mapping of the new RNA-only queries.

# %%
# Upstream code cell: 62
adata = rna_cite.copy()
adata.obsm["protein_counts"] = adt_cite.layers["counts"].A.copy()
adata.obsm["protein_counts"][adata.obs["batch"] == "s1d3"] = 0.0
adata

# %% [markdown]
# Next, we setup the AnnData, specify the model parameters and train the model.

# %%
# Upstream code cell: 64
TOTALVI.setup_anndata(
    adata,
    layer="counts",
    batch_key="batch",
    protein_expression_obsm_key="protein_counts",
)

# %%
# Upstream code cell: 65
arches_params = {
    "use_layer_norm": "both",
    "use_batch_norm": "none",
    "n_layers_decoder": 2,
    "n_layers_encoder": 2,
}

vae = TOTALVI(adata, **arches_params)
vae.train()

# %% [markdown]
# Now we obtain the latent representation and visualize it.

# %%
# Upstream code cell: 67
adata.obsm["X_totalvi"] = vae.get_latent_representation()

# %%
# Upstream code cell: 68
sc.pp.neighbors(adata, use_rep="X_totalvi")
sc.tl.umap(adata)

# %%
# Upstream code cell: 69
sc.pl.umap(adata, color=["cell_type", "batch"], ncols=1, frameon=False)

# %% [markdown]
# We see that batches as well as paired/RNA-only data are well integrated.

# %% [markdown]
# ### Query-to-reference mapping
# 
# Now we demonstrate how to map new unimodal (RNA-only) and multimodal query (CITE-seq) onto the above reference.
# 
# We mimic RNA-only query by setting the protein counts of one of the two batches to zero.

# %%
# Upstream code cell: 72
query = rna_cite_query.copy()
query.obsm["protein_counts"] = adt_cite_query.layers["counts"].A.copy()
query.obsm["protein_counts"][query.obs["batch"] == "s2d4"] = 0.0

# %% [markdown]
# We create some additional columns in `.obs` to help with the visualization later.

# %%
# Upstream code cell: 74
adata.obs["dataset_name"] = "Reference"
query.obs["dataset_name"] = "Query"

# %%
# Upstream code cell: 75
adata.obs["dataset_name_fine"] = "CITE reference"
adata.obs["dataset_name_fine"][adata.obs["batch"] == "s1d3"] = "RNA reference"
query.obs["dataset_name_fine"] = "CITE query"
query.obs["dataset_name_fine"][query.obs["batch"] == "s2d4"] = "RNA query"

# %% [markdown]
# Next, we update and fine-tune the model.

# %%
# Upstream code cell: 77
vae_q = TOTALVI.load_query_data(
    query,
    vae,
)
vae_q.train(
    plan_kwargs={"weight_decay": 0.0, "scale_adversarial_loss": 0.0},
)

# %% [markdown]
# Finally, we obtain the latent representation for the query and visualize it together with the reference. For this we concatenate reference and the query and recalculate the neighbors and the UMAP.

# %%
# Upstream code cell: 79
query.obsm["X_totalvi_scarches"] = vae_q.get_latent_representation(query)

# %%
# Upstream code cell: 80
adata.obsm["X_totalvi_scarches"] = adata.obsm["X_totalvi"]

# %%
# Upstream code cell: 81
full_data = adata.concatenate(query, batch_key="concat_batch")
full_data

# %%
# Upstream code cell: 82
sc.pp.neighbors(full_data, use_rep="X_totalvi_scarches")
sc.tl.umap(full_data)

# %%
# Upstream code cell: 83
sc.pl.umap(
    full_data,
    color=["cell_type", "batch", "dataset_name", "dataset_name_fine"],
    ncols=1,
    frameon=False,
)

# %% [markdown]
# <a id='seurat'></a>
# ## Query mapping and imputation with Seurat's WNN
# 
# Seurat v4 allows mapping of new RNA-seq queries onto a multimodal reference integrated with weighted-nearest-neighbor (WNN) {cite}`pi:hao2021`. We use the reference we built in the paired integration notebook.
# 
# The mapping is based on finding anchors between the query and the reference. This approach also allows for missing information transfer from the reference to the query. Here we show how to predict cell types and how to impute missing modalities (protein abundance in this case).
# 
# We note that since Seurat v4 is an R library we will need to work with `anndata2ri` package (https://github.com/theislab/anndata2ri) to move all of our data from Python to R.
# 
# First, let's take a look at our reference and the query.

# %%
# Upstream code cell: 85
%%R
ref <- readRDS(cite, file = "wnn_ref.rds")
ref

# %%
# Upstream code cell: 86
rna_cite_query

# %% [markdown]
# We need to preprocess the query first, so we use CLR-normalized counts to calculate PCA.

# %%
# Upstream code cell: 88
sc.pp.pca(rna_cite_query)
rna_cite_query

# %%
# Upstream code cell: 89
np.max(rna_cite_query.X)

# %% [markdown]
# Next, we move the query from Python to R.

# %%
# Upstream code cell: 91
adata_ = sc.AnnData(rna_cite_query.X.copy())
adata_.obs_names = rna_cite_query.obs_names.copy()
adata_.var_names = rna_cite_query.var_names.copy()
adata_.obs["cell_type"] = rna_cite_query.obs["cell_type"].copy()
adata_.obs["batch"] = rna_cite_query.obs["batch"].copy()
adata_.obsm["X_pca"] = rna_cite_query.obsm["X_pca"].copy()

# %%
# Upstream code cell: 92
%%R -i adata_
query = as.Seurat(adata_, data='X', counts=NULL)
query

# %% [markdown]
# Now we need to find anchors between the reference and the query. We specify that we want to use SPCA dimensionality reduction from the reference.

# %%
# Upstream code cell: 94
%%R
anchors <- FindTransferAnchors(
  reference = ref,
  query = query,
  reference.reduction = "spca",
  dims = 1:20
)

# %% [markdown]
# Next, we map query onto the reference using the saved UMAP model to make sure that the UMAP projections stay the same for the reference and the query is mapped onto it. We additionally specify what information we want to transfer from the reference to the query with `refdata` parameter: in our case we want to predict the cell type and the protein counts.

# %%
# Upstream code cell: 96
%%R
query <- MapQuery(
  anchorset = anchors,
  query = query,
  reference = ref,
  refdata = list(
    cell_type = "cell_type",
    predicted_ADT = "ADT"
  ),
  reference.reduction = "spca",
  reduction.model = "wnn.umap",
  verbose=FALSE
)

# %% [markdown]
# Let's visualize the reference and the query together and take a look at predicted vs true cell labels.

# %%
# Upstream code cell: 98
%%R
ref$id <- 'reference'
query$id <- 'query'
refquery <-  merge(ref, query)
refquery[["umap"]] <- merge(ref[["wnn.umap"]], query[["ref.umap"]])

# %%
# Upstream code cell: 99
%%R
p1 <- DimPlot(refquery, reduction = "umap", group.by = "cell_type", label = TRUE, label.size = 3, repel = TRUE) + NoLegend()
p2 <- DimPlot(refquery, reduction = "umap", group.by = "predicted.cell_type", label = TRUE, label.size = 3, repel = TRUE) + NoLegend()
p1 + p2

# %%
# Upstream code cell: 100
%%R
DimPlot(refquery, reduction = "umap", group.by = "id", label = TRUE, label.size = 3, repel = TRUE) + NoLegend()

# %% [markdown]
# <a id='bridge'></a>
# ## Mapping ADT onto an RNA atlas with bridge integration
# 
# Bridge {cite}`ai:hao2022` is a method for mapping new modalities onto an RNA-seq reference. To do so we need a so-called "bridge" dataset that contains paired data (RNA-seq and the new modality we want to map).
# 
# Since we want to showcase the bridging functionality, we assume that our reference consist of only one batch. We refer the reader to the integration vignette if there is a need to integrate batches in the reference (https://satijalab.org/seurat/articles/integration_introduction.html). As the bridge dataset we use one batch of the CITE-seq query, and as the actual ADT query we use ADT modality of the second batch in the CITE-seq query.
# 
# First, we subset the datasets to reference, bridge and query as described above.

# %%
# Upstream code cell: 102
rna_cite_ref = rna_cite[rna_cite.obs["batch"] == "s1d1"].copy()
rna_cite_bridge = rna_cite_query[rna_cite_query.obs["batch"] == "s2d1"].copy()

# %%
# Upstream code cell: 103
adt_cite_bridge = adt_cite_query[adt_cite_query.obs["donor"] == "s2d1"].copy()
adt_cite_query_bridge = adt_cite_query[adt_cite_query.obs["donor"] == "s2d4"].copy()

# %% [markdown]
# Next, we prepare the reference. We move the object from Python to R, normalize the data with SCTransform and calculate PCA. We also calculate the UMAP (and keep the model) that we will later use to map query onto.

# %%
# Upstream code cell: 105
adata_ = sc.AnnData(rna_cite_ref.layers["counts"].A.copy())
adata_.obs_names = rna_cite_ref.obs_names.copy()
adata_.var_names = rna_cite_ref.var_names.copy()
adata_.obs["cell_type"] = rna_cite_ref.obs["cell_type"].copy()

# %%
# Upstream code cell: 106
%%R -i adata_
ref = as.Seurat(adata_, data=NULL, counts='X')
ref

# %%
# Upstream code cell: 107
%%R
ref <- RenameAssays(object = ref, originalexp = "RNA", verbose=FALSE) 
ref <- SCTransform(ref, verbose=FALSE)
ref <- RunPCA(ref, verbose=FALSE)
ref <- RunUMAP(ref, dims = 1:50, return.model=TRUE, verbose=FALSE)

# %% [markdown]
# Next, we prepare the bridge dataset. We move both RNA and ADT objects to R, follow the same normalization procedure as above for RNA, perform CLR-normalization and calculate PCA for ADT counts.

# %%
# Upstream code cell: 109
adata_ = sc.AnnData(adt_cite_bridge.layers["counts"].A.copy())
adata_.obs_names = adt_cite_bridge.obs_names.copy()
adata_.var_names = adt_cite_bridge.var_names.copy()
adata_.obs["cell_type"] = adt_cite_bridge.obs["cell_type"].copy()

# %%
# Upstream code cell: 110
adata_

# %%
# Upstream code cell: 111
%%R -i adata_
adt <- as.Seurat(adata_, data=NULL, counts='X')

# %%
# Upstream code cell: 112
adata_ = sc.AnnData(rna_cite_bridge.layers["counts"].A.copy())
adata_.obs_names = rna_cite_bridge.obs_names.copy()
adata_.var_names = rna_cite_bridge.var_names.copy()
adata_.obs["cell_type"] = rna_cite_bridge.obs["cell_type"].copy()

# %%
# Upstream code cell: 113
%%R -i adata_
rna = as.Seurat(adata_, data=NULL, counts='X')
cite <- rna
cite <- RenameAssays(object = cite, originalexp = "RNA") 
cite[["ADT"]] <- CreateAssayObject(counts = adt@assays$originalexp@data)

# %%
# Upstream code cell: 114
%%R
DefaultAssay(cite) <- "RNA"
VariableFeatures(cite) <- rownames(cite)
cite <- SCTransform(cite, verbose = FALSE)

# %%
# Upstream code cell: 115
%%R
DefaultAssay(cite) <- "ADT"
VariableFeatures(cite) <- rownames(cite)
cite <- NormalizeData(cite, normalization.method = 'CLR', margin = 2, verbose=FALSE)
cite <- ScaleData(cite, verbose=FALSE)

# %% [markdown]
# Finally, we prepare the ADT query the same way as the bridge ADT above.

# %%
# Upstream code cell: 117
adata_ = sc.AnnData(adt_cite_query_bridge.layers["counts"].A.copy())
adata_.obs_names = adt_cite_query_bridge.obs_names.copy()
adata_.var_names = adt_cite_query_bridge.var_names.copy()
adata_.obs["cell_type"] = adt_cite_query_bridge.obs["cell_type"].copy()

# %%
# Upstream code cell: 118
%%R -i adata_
query <- as.Seurat(adata_, data=NULL, counts='X')
query <- RenameAssays(object = query, originalexp = "ADT", verbose=FALSE) 
VariableFeatures(query) <- rownames(query)
query <- NormalizeData(query, normalization.method = 'CLR', margin = 2, verbose=FALSE)
query <- ScaleData(query, verbose=FALSE)
query <- RunPCA(query, verbose=FALSE, reduction.name = 'apca')

# %% [markdown]
# Now we can perform the bridge integration. The final step of query mapping is the same as with Seurat v4 query mapping so we can also predict cell types for the query data.

# %%
# Upstream code cell: 120
%%R
dims.adt <- 1:50
dims.rna <- 1:50

DefaultAssay(cite) <-  "RNA"
DefaultAssay(ref) <- "SCT"
obj.rna.ext <- PrepareBridgeReference(
    reference = ref,
    bridge = cite,
    bridge.query.assay = "ADT",
    reference.reduction = "pca",
    reference.dims = dims.rna,
    normalization.method = "SCT",
    verbose = FALSE
)

# %%
# Upstream code cell: 121
%%R
bridge.anchor <- FindBridgeTransferAnchors(
    extended.reference = obj.rna.ext, 
    query = query,
    reduction = "pcaproject",
    dims = dims.adt,
    verbose = FALSE
)

# %%
# Upstream code cell: 122
%%R
query <- MapQuery(
    anchorset = bridge.anchor, 
    reference = ref, 
    query = query, 
    refdata = list(
        cell_type = "cell_type"
    ),
    reduction.model = "umap",
    verbose = FALSE
)

# %% [markdown]
# Let's visualize the result.

# %%
# Upstream code cell: 124
%%R
p1 <- DimPlot(query, group.by = "predicted.cell_type", reduction = "ref.umap", label = TRUE) + NoLegend()
p2 <- DimPlot(query, group.by = "cell_type", reduction = "ref.umap", label = TRUE) + NoLegend()
p1 + p2

# %%
# Upstream code cell: 125
%%R
ref$id <- 'reference'
query$id <- 'query'
refquery <-  merge(ref, query)
refquery[["umap"]] <- merge(ref[["umap"]], query[["ref.umap"]])
DimPlot(refquery, group.by = 'id', shuffle = TRUE)

# %% [markdown]
# <a id='multigrate'></a>
# ## Trimodal integration and query-to-reference mapping with multigrate
# 
# In our final example, we will build a trimodal reference atlas using RNA, ATAC and ADT as three modalities. Multigrate {cite}`ai:lotfollahi2022` is a deep-learning method based on conditional autoencoders. Data from each modality is fed into a separate encoder which outputs the parameters of the marginal distribution, then the parameters of the joint distribution are calculated with product of experts (PoE) {cite}`ai:lee2021`. The conditional decoders then learn to reconstruct the original input data while simultaneously correction for batch effects. PoE allows the integration of data with missing measurements for some modalities by setting the corresponding marginals to a non-informative distribution. Multigrate also follows scArches {cite}`ai:lotfollahi2022_arches` framework to allow query-to-reference mapping of unimodal as well as multimodal queries.

# %% [markdown]
# ### Building the reference
# 
# First, we load data that has 4000 highly variable genes that are common for the scRNA-seq and scRNA-seq from the CITE-seq and the multiome experiment respectively.

# %%
# Upstream code cell: 128
rna1 = sc.read(
    "/lustre/groups/ml01/workspace/anastasia.litinetskaya/data/trimodal_neurips/rna_hvg_cite.h5ad"
)
rna1_ref = rna1[adt_cite.obs_names].copy()
rna1_query = rna1[adt_cite_query.obs_names].copy()
rna1_ref.shape, rna1_query.shape

# %%
# Upstream code cell: 129
rna2 = sc.read(
    "/lustre/groups/ml01/workspace/anastasia.litinetskaya/data/trimodal_neurips/rna_hvg_multiome.h5ad"
)
rna2_ref = rna2[atac_multiome.obs_names].copy()
rna2_query = rna2[atac_multiome_query.obs_names].copy()
rna2_ref.shape, rna2_query.shape

# %% [markdown]
# Next, we concatenate all the data into one AnnData object specifying how the data is paired and which layers to use.

# %%
# Upstream code cell: 131
adata = mtg.data.organize_multiome_anndatas(
    adatas=[[rna1_ref, rna2_ref], [None, atac_multiome], [adt_cite, None]],
    layers=[["counts", "counts"], [None, "cpm"], [None, None]],
)
adata

# %% [markdown]
# Next, we register covariates that the model will correct for in the latent space.

# %%
# Upstream code cell: 133
mtg.model.MultiVAE.setup_anndata(
    adata,
    categorical_covariate_keys=["Modality", "Samplename"],
    rna_indices_end=4000,
)

# %% [markdown]
# Next, we initialize the model and train it.

# %%
# Upstream code cell: 135
model = mtg.model.MultiVAE(
    adata,
    losses=["nb", "mse", "mse"],
    loss_coefs={
        "kl": 1e-3,
        "integ": 10000,
    },
    integrate_on="Modality",
    mmd="marginal",
)

# %%
# Upstream code cell: 136
model.train()

# %% [markdown]
# Finally, we obtain the latent representation, save it explicitly in `.obsm['latent_ref']` as we will overwrite `.obsm['latent']` later when we work with fine-tuned model after query mapping and visualize the result.

# %%
# Upstream code cell: 138
model.get_latent_representation()
adata.obsm["latent_ref"] = adata.obsm["latent"].copy()
adata

# %%
# Upstream code cell: 139
sc.pp.neighbors(adata, use_rep="latent")
sc.tl.umap(adata)

# %%
# Upstream code cell: 140
sc.pl.umap(adata, color=["cell_type", "Modality", "Samplename"], ncols=1, frameon=False)

# %% [markdown]
# ### Querying the trimodal reference
# 
# We repeat the same steps for the setting up the query as for the reference before.

# %%
# Upstream code cell: 142
query = mtg.data.organize_multiome_anndatas(
    adatas=[
        [rna1_query, rna2_query],
        [None, atac_multiome_query],
        [adt_cite_query, None],
    ],
    layers=[["counts", "counts"], [None, "cpm"], [None, None]],
)

# %%
# Upstream code cell: 143
mtg.model.MultiVAE.setup_anndata(
    query,
    categorical_covariate_keys=["Modality", "Samplename"],
    rna_indices_end=4000,
)

# %% [markdown]
# Let's imitate unimodal queries by masking with zeros the snRNA part of one multiome batch and ADT part of one CITE-seq batch in the query. We get one ATAC-only query batch and one scRNA-only query batch respectively.

# %%
# Upstream code cell: 145
idx_atac_query = query.obs["Samplename"] == "site2_donor4_multiome"
idx_scrna_query = query.obs["Samplename"] == "site2_donor1_cite"

idx_mutiome_query = query.obs["Samplename"] == "site2_donor1_multiome"
idx_cite_query = query.obs["Samplename"] == "site2_donor4_cite"

(
    np.sum(idx_atac_query),
    np.sum(idx_scrna_query),
    np.sum(idx_mutiome_query),
    np.sum(idx_cite_query),
)

# %%
# Upstream code cell: 146
query[idx_atac_query, :4000].X = 0
query[idx_scrna_query, 4000:].X = 0

# %% [markdown]
# We update the model by adding new weights to the new batches in the query and fine-tune those weights.

# %%
# Upstream code cell: 148
q_model = mtg.model.MultiVAE.load_query_data(query, model)

# %%
# Upstream code cell: 149
q_model.train(weight_decay=0)

# %% [markdown]
# We obtain the latent representation for query and the reference from the updated model. Note that the representation of the reference is the same as before up to some sampling noise.

# %%
# Upstream code cell: 151
q_model.get_latent_representation(adata=query)
q_model.get_latent_representation(adata=adata)

# %% [markdown]
# Finally, we concatenate the reference and the query, and visualize both on a UMAP.

# %%
# Upstream code cell: 153
adata.obs["reference"] = "reference"
query.obs["reference"] = "query"

adata.obs["type_of_query"] = "reference"
query.obs.loc[idx_atac_query, "type_of_query"] = "ATAC query"
query.obs.loc[idx_scrna_query, "type_of_query"] = "scRNA query"
query.obs.loc[idx_mutiome_query, "type_of_query"] = "multiome query"
query.obs.loc[idx_cite_query, "type_of_query"] = "CITE-seq query"

# %%
# Upstream code cell: 154
adata_both = anndata.concat([adata, query])

# %%
# Upstream code cell: 155
sc.pp.neighbors(adata_both, use_rep="latent")
sc.tl.umap(adata_both)

# %%
# Upstream code cell: 156
sc.pl.umap(
    adata_both,
    color=["cell_type", "Modality", "Samplename", "reference"],
    ncols=1,
    frameon=False,
)

# %%
# Upstream code cell: 157
sc.pl.umap(
    adata_both, color="type_of_query", ncols=1, frameon=False, groups=["ATAC query"]
)

# %%
# Upstream code cell: 158
sc.pl.umap(
    adata_both, color="type_of_query", ncols=1, frameon=False, groups=["CITE-seq query"]
)

# %%
# Upstream code cell: 159
sc.pl.umap(
    adata_both, color="type_of_query", ncols=1, frameon=False, groups=["multiome query"]
)

# %%
# Upstream code cell: 160
sc.pl.umap(
    adata_both, color="type_of_query", ncols=1, frameon=False, groups=["scRNA query"]
)

# %% [markdown]
# We observe that the query cell types are mapped to the corresponding cell types in the reference. We also note that unimodal query mapping is possible with Multigrate even though there was no unimodal data in the reference.

# %% [markdown]
# ## Session info

# %%
# Upstream code cell: 163
%%R
sessionInfo()

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
# * Anastasia Litinetskaya
# 
# ### Reviewers
# 
# * Lukas Heumos
