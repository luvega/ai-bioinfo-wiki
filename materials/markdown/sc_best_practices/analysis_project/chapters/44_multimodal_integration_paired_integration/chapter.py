# Auto-generated from single-cell-best-practices.
# Title: Paired integration
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/multimodal_integration/paired_integration.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (multimodal-integration-paired-integration)=
# # Paired integration

# %% [markdown]
# (multimodal-integration-paired-integration-key-takeaway-1)=
# ## Motivation

# %% [markdown]
# In the recent years several technologies appeared that allow us to measure several modalities in a single-cell. Modalities in this context refer to different type of information that we can capture in each cell. For instance, CITE-seq allows measuring gene expression and surface protein abundance in the same cell. Alternatively, paired RNA-seq/ATAC-seq experiments using, for example, the Multiome assay, capture gene expression and chromatin accessibility simultaneously. 
# 
# We are interested in the most holistic representation of single cells that incorporate information from all the available modalities, but several challenges might arise when integrating these different modalities. Data stemming from different sequencing technologies can vary in dimensions: RNA-seq experiments usually capture 20-30 thousand genes, but the protein panel can be as small just a few proteins up to 200. ATAC-seq experiments on the other hand can have more than 200000 peaks. On top of having different dimensionality, the data can follow different distributions. RNA-seq counts are often modelled with negative binomial distribution, while chromatin accessibility can be binarized and modelled as either open or closed and therefore with a Bernoulli distribution {cite}`pi:ashuach2021`. Alternatively raw ATAC-seq counts can be modelled following Poisson distribution {cite}`pi:martens2022`.
# 
# Here, we showcase several tools for paired integration including MOFA+ {cite}`pi:argelaguet2020`, WNN {cite}`pi:hao2021`, totalVI {cite}`pi:gayoso2021` and multiVI {cite}`pi:ashuach2021`. We use 10x Multiome and CITE-seq data generated for the single cell data integration challenge at the NeurIPS conference 2021 {cite}`pi:luecken2021sandbox`. This dataset captures single-cell data from bone marrow mononuclear cells of 12 healthy human donors measured at four different sites to obtain nested batch effects. In this tutorial, we will use 3 batches from one site to showcase the integration tools. 
# 
# Since there are multiple integration tools available, it can be quite challenging to assess which tool to use for a particular task at hand. We therefore use the scIB {cite}`pi:luecken2022` package that allows to make such a decision by quantitatively assessing the quality of the integration. It is important to note though that scIB was designed for unimodal integration of batches and not for multimodal integration. We expect more metrics to appear in the near future that are specifically designed for multimodal data, but for now we show how to use scIB metrics to compare the integration results.

# %% [markdown]
# ## Environment setup

# %%
# Upstream code cell: 5
import logging

import anndata as ad
import anndata2ri
import matplotlib.pyplot as plt
import muon as mu
import pandas as pd
import rpy2.rinterface_lib.callbacks
import scanpy as sc
import scib
import scipy
import scipy.io
import scvi
import seaborn as sns
from rpy2.robjects import pandas2ri

rpy2.rinterface_lib.callbacks.logger.setLevel(logging.ERROR)

pandas2ri.activate()
anndata2ri.activate()

%load_ext rpy2.ipython

import warnings

warnings.filterwarnings("ignore")

# %%
# Upstream code cell: 6
%%R
suppressPackageStartupMessages({
    library(Seurat)
})
set.seed(123)

# %% [markdown]
# ## CITE-seq data
# 
# We first show how to integrate a CITE-seq dataset using WNN, MOFA+ and totalVI. CITE-seq data contains raw gene expression counts and counts for surface proteins. The surface protein data is represented as antibody-derived tags (adt) here. We refer to the {ref}`surface-protein:motivation` section of the Surface Proteins chapter for more details.

# %% [markdown]
# ### Prepare data

# %%
# Upstream code cell: 9
adt = sc.read(
    "/lustre/groups/ml01/workspace/anastasia.litinetskaya/data/neurips-cite/adt_pp.h5ad"
)
adt

# %%
# Upstream code cell: 10
rna = sc.read(
    "/lustre/groups/ml01/workspace/anastasia.litinetskaya/data/neurips-cite/rna_hvg.h5ad"
)
rna

# %% [markdown]
# We subset the data to Site 1 and the 3 corresponding donors to reduce the run time.

# %%
# Upstream code cell: 12
batches_to_keep = ["s1d1", "s1d2", "s1d3"]
rna = rna[rna.obs["batch"].isin(batches_to_keep)]
adt = adt[adt.obs["donor"].isin(batches_to_keep)]

# %% [markdown]
# We only keep the cells that are present in both modality objects. First we need to make sure that `.obs_names` of both objects have similar structure and if not clean up a bit.

# %%
# Upstream code cell: 14
adt.obs_names

# %%
# Upstream code cell: 15
rna.obs_names

# %%
# Upstream code cell: 16
adt.obs_names = [
    name.split("-")[0] + "-" + name.split("-")[1] + "-" + batch
    for batch, name in zip(adt.obs["donor"], adt.obs_names, strict=False)
]

# %%
# Upstream code cell: 17
common_idx = list(set(rna.obs_names).intersection(set(adt.obs_names)))
rna = rna[common_idx].copy()
adt = adt[common_idx].copy()

# %% [markdown]
# We need to rename the proteins in the `adt` object so that the gene names and protein names do not intersect.

# %%
# Upstream code cell: 19
adt.var_names = ["PROT_" + name for name in adt.var_names]

# %% [markdown]
# Next we create a MuData object where we store data for both modalities.

# %%
# Upstream code cell: 21
mdata = mu.MuData({"rna": rna, "adt": adt})
mdata

# %% [markdown]
# We copy `batch` and `cell_type` column from one of the modality adatas to `.obs` of the mdata object to later use for visualizations.

# %%
# Upstream code cell: 23
mdata.obs["batch"] = rna.obs["batch"].copy()
mdata.obs["cell_type"] = rna.obs["cell_type"].copy()

# %% [markdown]
# ### Weighted Nearest Neighbor (WNN)

# %% [markdown]
# WNN is a graph-based method that takes neighbor graphs for each modality and constructs a common graph which is a weighted combination of the modality graphs. This constructed WNN graph can later be used together with gene expression matrix to obtain a supervised PCA (sPCA) representation guided by a WNN graph. The sPCA representation can be viewed as an embedding in a latent space.
# 
# First, we use the `anndata2ri` package (https://github.com/theislab/anndata2ri) to move Python AnnData object to SingleCellExperiment and Seurat R objects. We create slimmer versions of AnnData objects that only contain the information that we need for the analysis.

# %%
# Upstream code cell: 26
adata_ = ad.AnnData(adt.X.copy())
adata_.obs_names = adt.obs_names.copy()
adata_.var_names = adt.var_names.copy()
adata_.obs["batch"] = adt.obs["donor"].copy()
adata_.obsm["harmony_pca"] = adt.obsm["X_pcahm"].copy()

# %%
# Upstream code cell: 27
%%R -i adata_
# indicate that data is stored in .X of AnnData object
adt = as.Seurat(adata_, data='X', counts=NULL)
# the assay is called "originalexp" by default, we rename it to "ADT"
adt <- RenameAssays(object = adt, originalexp = "ADT", verbose=FALSE) 
adt

# %% [markdown]
# We repeat the same for RNA data.

# %%
# Upstream code cell: 29
adata_ = ad.AnnData(rna.X.copy())
adata_.obs_names = rna.obs_names.copy()
adata_.var_names = rna.var_names.copy()
adata_.obs["cell_type"] = rna.obs["cell_type"].copy()
adata_.obs["batch"] = rna.obs["batch"].copy()

# %%
# Upstream code cell: 30
%%R -i adata_
rna = as.Seurat(adata_, data='X', counts=NULL)
rna

# %% [markdown]
# Next we create a Seurat object with both assays.

# %%
# Upstream code cell: 32
%%R
cite <- rna
cite[["ADT"]] <- CreateAssayObject(data = adt@assays$ADT@data)

# %%
# Upstream code cell: 33
%%R
cite <- RenameAssays(object = cite, originalexp = "RNA", verbose=FALSE)

# %% [markdown]
# Since we have several batches in the dataset, we would need to perform batch correction before integrating the modalities. One option would be to batch correct using Seurat's `FindIntegrationAnchors()` and `IntegrateData()` (see https://satijalab.org/seurat/articles/integration_introduction.html) functions separately for each modality. We will use batch corrected embedding from previous analysis done separately for ADT and RNA data, namely Harmony corrected PCA embedding for ADT and scVI batch-corrected latent embedding for RNA.

# %%
# Upstream code cell: 35
%%R
# TODO need to change after we have the preprocessed data, for now RNA is not batch-corrected
DefaultAssay(cite) <- "RNA"
VariableFeatures(cite) <- rownames(cite)
cite <- ScaleData(cite, verbose=FALSE)
cite <- RunPCA(cite, verbose=FALSE)

# %%
# Upstream code cell: 36
%%R
cite@reductions$harmony_pca <- adt@reductions$harmony_pca
cite

# %% [markdown]
# Now we follow the WNN vignette to perform the analysis. First, we need to find multimodal neighbors using the specified dimensionality reductions for each of the modalities. This function adds a WNN graph to the Seurat object.

# %%
# Upstream code cell: 38
%%R
cite <- FindMultiModalNeighbors(
    cite, 
    reduction.list = list("pca", "harmony_pca"), 
    dims.list = list(1:50, 1:30), 
    modality.weight.name = "RNA.weight",
    verbose = FALSE
)

# %% [markdown]
# Since we are also interested in finding an embedding for our multimodal data, we additionally run the `RunSPCA()` function that uses RNA gene expression data and the WNN graph for supervised PCA. Supervised PCA is a "guided" version of standard PCA run on gene expression data guided by the WNN graph to better preserve relationships between cells learned in WNN graph. We also will need a reference UMAP later for mapping an RNA query onto this multimodal reference as discussed in {ref}`multimodal-integration:advanced-integration`.

# %%
# Upstream code cell: 40
%%R
cite <- RunSPCA(cite, assay = "RNA", graph = "wsnn", npcs = 20)
cite <- RunUMAP(cite, nn.name = "weighted.nn", reduction.name = "wnn.umap", reduction.key = "wnnUMAP_", return.model=TRUE)

# %%
# Upstream code cell: 41
%%R
cite

# %% [markdown]
# We save the Seurat object as an `.rds` file for the {ref}`multimodal-integration:advanced-integration` section.

# %%
# Upstream code cell: 43
%%R
saveRDS(cite, file = "wnn_ref.rds")

# %% [markdown]
# We move the sPCA embedding to Python and store them in `.obsm` of the MuData object.

# %%
# Upstream code cell: 45
%%R -o spca
spca = Embeddings(object = cite[["spca"]])

# %%
# Upstream code cell: 46
mdata.obsm["X_spca"] = spca

# %% [markdown]
# We also need to extract the calculated WNN graph.

# %%
# Upstream code cell: 48
%%R -o wnn
wnn <- as.data.frame(summary(cite@graphs$wknn))

# %% [markdown]
# The table indicates indices with connections between cells in the WNN graph. Since R starts indexing at 1 but Python at 0, we modify the indices to start with 0.

# %%
# Upstream code cell: 50
wnn[:5]

# %%
# Upstream code cell: 51
wnn["i"] = wnn["i"] - 1
wnn["j"] = wnn["j"] - 1
wnn[:5]

# %% [markdown]
# We store the graph in `.obsp` of the MuData object.

# %%
# Upstream code cell: 53
mdata.obsp["wnn_connectivities"] = scipy.sparse.coo_matrix(
    (wnn["x"], (wnn["i"], wnn["j"]))
)

# %% [markdown]
# Next we use the WNN graph to calculate the UMAP coordinates and save them in `.obsm['X_umap_wnn']`. We could alternatively also just use sPCA coordinates for visualization.

# %%
# Upstream code cell: 55
# we won't actually need the neighbors
# but need to run this anyway as a little trick to make scanpy work with externally-computed neighbors
sc.pp.neighbors(mdata, use_rep="X_spca")
mdata.obsp["connectivities"] = mdata.obsp["wnn_connectivities"].copy()
# delete distances to make sure we are not using anything calculated with sc.pp.neighbors()
del mdata.obsp["distances"]
sc.tl.umap(mdata)

# %%
# Upstream code cell: 56
mdata.obsm["X_umap_wnn"] = mdata.obsm["X_umap"].copy()

# %% [markdown]
# Finally we visualize the cell types and batches on a UMAP.

# %%
# Upstream code cell: 58
mu.pl.embedding(
    mdata, color=["cell_type", "batch"], ncols=1, basis="umap_wnn", frameon=False
)

# %% [markdown]
# To be able to quantitatively assess the result of the integration and compare to other methods we compute some of the scIB metrics using the sPCA embedding and WNN graph. More specifically, we calculate the following metrics:
# - bio conservation: `NMI_cluster/label`, `ARI_cluster/label`, `ASW_label` and `isolated_label_silhouette`;
# - batch correction: `ASW_label/batch`, `graph_conn`.

# %%
# Upstream code cell: 60
scib_anndata = sc.AnnData(mdata.obsm["X_spca"]).copy()
scib_anndata.obs = mdata.obs.copy()
scib_anndata.obsp["connectivities"] = mdata.obsp["connectivities"].copy()
scib_anndata.obsm["X_spca"] = mdata.obsm["X_spca"].copy()

# %%
# Upstream code cell: 61
metrics_wnn = scib.metrics.metrics(
    scib_anndata,
    scib_anndata,
    batch_key="batch",
    label_key="cell_type",
    embed="X_spca",
    ari_=True,
    nmi_=True,
    silhouette_=True,
    graph_conn_=True,
    isolated_labels_asw_=True,
)
metrics_wnn

# %% [markdown]
# We note that even though batch correction was performed using Harmony for ADT and scVI for RNA, we still include metrics that assess batch correction here too.

# %% [markdown]
# ### Multi-Omics Factor Analysis (MOFA+)

# %% [markdown]
# MOFA+ is a linear factor model that decomposes the input matrices into the product of low-rank matrices. The low-rank representation can be used as an embedding in a low-dimensional space for visualization and other downstream tasks. The latent dimensions are interpretable with respect to the original input features and represent the leading sources of variation in the data.
# 
# By default, we are using data from `.X` and the data should be normalized. Since there are some batch effects in the data that MOFA+ can correct for, we also pass the `groups_label` parameter to specify the batch covariate.
# 
# If you want to run MOFA+ on a GPU, you need to additionally install a version of cuPY (https://cupy.dev) which is compatible with your CUDA.

# %%
# Upstream code cell: 65
mu.tl.mofa(mdata, groups_label="batch", gpu_mode=True)

# %% [markdown]
# We use the `X_mofa` representation to calculate the neighbors and the UMAP coordinates, and store them in `.obsm['X_umap_mofa']`.

# %%
# Upstream code cell: 67
sc.pp.neighbors(mdata, use_rep="X_mofa")
sc.tl.umap(mdata)
mdata.obsm["X_umap_mofa"] = mdata.obsm["X_umap"].copy()

# %% [markdown]
# We plot the cell types and batches again on the resulting UMAP.

# %%
# Upstream code cell: 69
mu.pl.embedding(
    mdata, color=["cell_type", "batch"], ncols=1, basis="umap_mofa", frameon=False
)

# %% [markdown]
# Finally, we calculate the same scIB metrics as before.

# %%
# Upstream code cell: 71
scib_anndata = sc.AnnData(mdata.obsm["X_mofa"]).copy()
scib_anndata.obs = mdata.obs.copy()
scib_anndata.obsp["connectivities"] = mdata.obsp["connectivities"].copy()
scib_anndata.obsm["X_mofa"] = mdata.obsm["X_mofa"].copy()

# %%
# Upstream code cell: 72
metrics_mofa = scib.metrics.metrics(
    scib_anndata,
    scib_anndata,
    batch_key="batch",
    label_key="cell_type",
    embed="X_mofa",
    ari_=True,
    nmi_=True,
    silhouette_=True,
    graph_conn_=True,
    isolated_labels_asw_=True,
)
metrics_mofa

# %% [markdown]
# ### Total Variational Inference (totalVI)

# %% [markdown]
# TotalVI is a variational-inference-based method for joint analysis of paired gene expression and protein abundance measurements. It takes into account batch effects, protein background noise, which allows the model to learn a joint latent representation disentangled from technical factors. TotalVI models transcriptome counts with negative-binomial (NB) distribution and the protein counts as NB mixture of foreground and background signal. Hence, the model takes raw gene expression and raw protein counts as input.

# %%
# Upstream code cell: 75
adata = mdata["rna"].copy()
adata.obsm["protein_expression"] = mdata["adt"].layers["counts"].A.copy()

# %% [markdown]
# We need to specify that raw counts for RNA are stored in `counts` layer of our adata and that we want to correct for batch effect with `batch_key="batch"` parameter.

# %%
# Upstream code cell: 77
scvi.model.TOTALVI.setup_anndata(
    adata,
    protein_expression_obsm_key="protein_expression",
    layer="counts",
    batch_key="batch",
)

# %% [markdown]
# We initialize the totalVI model.

# %%
# Upstream code cell: 79
vae = scvi.model.TOTALVI(adata)

# %% [markdown]
# Next, we train the model with default parameters.

# %%
# Upstream code cell: 81
vae.train()

# %% [markdown]
# Next, we obtain the latent representation and store it in `.obsm['X_totalVI']` and then use it to calculate the UMAP coordinates.

# %%
# Upstream code cell: 83
mdata.obsm["X_totalVI"] = vae.get_latent_representation()

# %%
# Upstream code cell: 84
sc.pp.neighbors(mdata, use_rep="X_totalVI")
sc.tl.umap(mdata)

# %%
# Upstream code cell: 85
mdata.obsm["X_umap_totalVI"] = mdata.obsm["X_umap"].copy()

# %% [markdown]
# As above, we plot cell types and batches on a UMAP.

# %%
# Upstream code cell: 87
mu.pl.embedding(
    mdata, color=["cell_type", "batch"], ncols=1, basis="umap_totalVI", frameon=False
)

# %% [markdown]
# And finally, we calculate scIB metrics.

# %%
# Upstream code cell: 89
scib_anndata = sc.AnnData(mdata.obsm["X_totalVI"]).copy()
scib_anndata.obs = mdata.obs.copy()
scib_anndata.obsp["connectivities"] = mdata.obsp["connectivities"].copy()
scib_anndata.obsm["X_totalVI"] = mdata.obsm["X_totalVI"].copy()

# %%
# Upstream code cell: 90
metrics_totalvi = scib.metrics.metrics(
    scib_anndata,
    scib_anndata,
    batch_key="batch",
    label_key="cell_type",
    embed="X_totalVI",
    ari_=True,
    nmi_=True,
    silhouette_=True,
    graph_conn_=True,
    isolated_labels_asw_=True,
)
metrics_totalvi

# %% [markdown]
# (multimodal-integration-paired-integration-key-takeaway-2)=
# ### scIB metrics evaluation

# %% [markdown]
# To better see the differences in models' performances, we visualize the scIB output for each of the methods. We need to merge the output DataFrames into one and additionally calculate the overall score for each method. We follow the scIB publication and calculate the overall score as `0.4 * batch_correction_metrics + 0.6 * bio_conservation_metrics`.

# %%
# Upstream code cell: 93
metrics = pd.DataFrame([metrics_wnn[0], metrics_mofa[0], metrics_totalvi[0]])
metrics = metrics.set_index(pd.Index(["WNN", "MOFA+", "totalVI"]))
metrics = metrics.dropna(axis=1)
metrics

# %%
# Upstream code cell: 94
metrics["overall"] = (
    0.4 * (metrics["ASW_label/batch"] + metrics["graph_conn"]) / 2
    + 0.6
    * (
        metrics["NMI_cluster/label"]
        + metrics["ARI_cluster/label"]
        + metrics["ASW_label"]
        + metrics["isolated_label_silhouette"]
    )
    / 4
)
metrics

# %%
# Upstream code cell: 95
sns.scatterplot(data=metrics)
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", borderaxespad=0)

# %% [markdown]
# We observe that totalVI obtained the highest overall score, and therefore we will use totalVI embedding later in the notebook to show how one can annotate the cluster in the latent space using both ADT and RNA markers. Depending on the downstream task and the experimental design, selecting the best performing based on a specific metric is advisable.

# %% [markdown]
# ## Multiome data
# To show that integration methods can also work with multiome (i.e. paired RNA-seq and ATAC-seq) data, we demonstrate how multiVI can be used for this task. We note that WNN and MOFA+ can also be run on multiome data with almost exactly the same code as above, so here we only present multiVI where the underlying model differs from totalVI.

# %% [markdown]
# ### Prepare data

# %%
# Upstream code cell: 99
atac = sc.read(
    "/lustre/groups/ml01/workspace/anastasia.litinetskaya/data/neurips-multiome/atac_hvf.h5ad"
)
atac

# %%
# Upstream code cell: 100
rna = sc.read(
    "/lustre/groups/ml01/workspace/anastasia.litinetskaya/data/neurips-multiome/rna_hvg.h5ad"
)
rna

# %% [markdown]
# We again subset the data to one site and 3 batches.

# %%
# Upstream code cell: 102
batches_to_keep = ["s1d1", "s1d2", "s1d3"]
rna = rna[rna.obs["batch"].isin(batches_to_keep)]
atac = atac[atac.obs["batch"].isin(batches_to_keep)]

# %%
# Upstream code cell: 103
mdata_multiome = mu.MuData({"rna": rna, "atac": atac})
mdata_multiome

# %%
# Upstream code cell: 104
mdata_multiome.obs["batch"] = mdata_multiome["rna"].obs["batch"].copy()
mdata_multiome.obs["cell_type"] = mdata_multiome["rna"].obs["cell_type"].copy()

# %% [markdown]
# ### MultiVI

# %% [markdown]
# MultiVI is also based on variational inference and conditional variational autoencoders. The gene expression counts are modeled exactly the same way as in totalVI, i.e. using raw counts and NB distribution. Chromatin accessibility on the other hand is modeled using Bernoulli distribution modeling how likely a particular region is to be open. Hence, the input data for ATAC assay has to be binary where 0 means a closed region and 1 means an open region.

# %%
# Upstream code cell: 107
n_genes = len(rna.var_names)
n_regions = len(atac.var_names)

# %% [markdown]
# MultiVI requires one AnnData object with concatenated genes and peaks as features. Since we start off with two different objects for each modality but have paired measurements, we can use the following trick to concatenate the AnnData objects along the feature axis.

# %%
# Upstream code cell: 109
adata_paired = ad.concat([rna.copy().T, atac.copy().T]).T
adata_paired.obs = adata_paired.obs.join(rna.obs[["cell_type", "batch"]])
adata_paired.obs["modality"] = "paired"
adata_paired

# %%
# Upstream code cell: 110
adata_mvi = scvi.data.organize_multiome_anndatas(adata_paired)

# %% [markdown]
# We also make sure that we pass raw counts as input to the model by specifying `layer='counts'` in the `setup_anndata` function.

# %%
# Upstream code cell: 112
scvi.model.MULTIVI.setup_anndata(
    adata_mvi,
    batch_key="modality",
    categorical_covariate_keys=["batch"],
    layer="counts",
)

# %% [markdown]
# We initialize the MultiVI model.

# %%
# Upstream code cell: 114
mvi = scvi.model.MULTIVI(
    adata_mvi,
    n_genes=n_genes,
    n_regions=n_regions,
)

# %% [markdown]
# Next, we train the model with the default parameters.

# %%
# Upstream code cell: 116
mvi.train()

# %% [markdown]
# Finally, we visualize the latent embedding on the UMAP.

# %%
# Upstream code cell: 118
mdata_multiome.obsm["X_multiVI"] = mvi.get_latent_representation()

# %%
# Upstream code cell: 119
sc.pp.neighbors(mdata_multiome, use_rep="X_multiVI")
sc.tl.umap(mdata_multiome)

# %%
# Upstream code cell: 120
mdata_multiome.obsm["X_umap_multiVI"] = mdata_multiome.obsm["X_umap"].copy()

# %%
# Upstream code cell: 121
mu.pl.embedding(
    mdata_multiome,
    color=["cell_type", "batch"],
    ncols=1,
    basis="umap_multiVI",
    frameon=False,
)

# %% [markdown]
# Session info.

# %%
# Upstream code cell: 123
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
