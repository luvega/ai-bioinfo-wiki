# Auto-generated from single-cell-best-practices.
# Title: Cell-cell communication
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/mechanisms/cell_cell_communication.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (cell-cell)=
# # Cell-cell communication

# %% [markdown]
# *TL;DR This chapter serves as a brief overview of basic concepts and assumptions of cell-cell communication inference from single-cell transcriptomics data. We provide examples of the two most common approaches for CCC inference: those that focus on ligand-receptor interactions and those that include downstream response.*

# %% [markdown]
# ## Motivation

# %% [markdown]
# Cell communication is a process by which cells react to stimuli from their environment and also from themselves. In multicellular organisms, the dynamic coordination of cells, also called cell-cell communication (CCC), is involved in many biological processes, such as apoptosis and cell migration, and is consequently essential in homeostasis and disease. CCC commonly focuses on protein-mediated interactions, most typically perceived as a secreted ligand binding to its corresponding plasma membrane receptor. However, this picture can be broadened to include secreted enzymes, extra-cellular matrix proteins, transporters, and interactions that require the physical contact between cells, such as cell-cell adhesion proteins and gap junctions {cite}`armingol_2021`. Cell communication is further not independent of other processes, but the contrary, as external stimuli commonly elicit a downstream response. In the case of CCC, this is typically perceived as the induction of canonical pathways and downstream transcription factors in the cells receiving the signal, or receiver cells. Ultimately these external stimuli alter the function of receiver cells, and this alteration is further propagated via the subsequent interaction of these cells with their microenvironment. 
# Traditionally, the study of CCC required specialized in-situ biochemical assays, such as proximity labelling proteomics, co-immunoprecipitation, and yeast two-hybrid screening {cite}`armingol_2021`. Yet, the rapid developments and dropping costs of transcriptomics data generation has enabled a paradigm shift away from focusing on which types of cells are present, but rather on the relationships between them {cite}`almet_2021`. As a consequence, CCC inference from single-cell data is now becoming a routine approach, capable of providing a system-level hypotheses of intercellular crosstalk in vivo.

# %% [markdown]
# (mechanisms-cell-cell-communication-key-takeaway-1)=
# ## Approaches

# %% [markdown]
# As a result of this increased interest, a number of computational tools for CCC inference from single-cell transcriptomics have emerged that can be classified as those that predict CCC interactions alone, commonly referred to as ligand-receptor inference methods (e.g. {cite}`efremova_2020,jin_2021,raredon_2022,hou2020predicting`), and those that additionally estimate intracellular activities induced by CCC (e.g. {cite}`wang_2019,browaeys_2020,hu_2021`). Both categories of tools use gene expression information as a proxy of protein abundance, and typically require the clustering of cells into biologically-meaningful groups (See Annotation tutorial). These CCC tools infer intercellular crosstalk between pairs of cell groups, one group being the source and the other the receiver of a CCC event. CCC events are thus commonly represented as interactions between proteins, expressed by the source and receiver cell clusters.
# 
# The information about the interacting proteins is commonly extracted from prior knowledge resources. In the case of ligand-receptor methods, the interactions can also be represented by heteromeric protein complexes, as different subunit combinations can induce distinct responses and the inclusion of protein complex information has been shown to reduce false positive rates {cite}`efremova_2020,jin_2021,liu_2022`. On the other hand, the approaches that model intracellular signalling also leverage the functional information in receiver cell types, and thus require additional information such as intracellular protein-protein interaction network and/or gene regulatory interactions.
# 
# Recent work has highlighted that the choice of method and/or resource leads to limited consensus in inferred predictions when using different tools {cite}`dimitrov_2022,wang_2022,liu_2022`, thus prompting caution when interpreting their output. The CCC field is further plagued by the lack of ground truth {cite}`armingol_2021,almet_2021`, capable of capturing the complex and dynamic interplay between large numbers of cells and molecules. Nevertheless, independent evaluations have shown that CCC methods are fairly robust to the introduction of noise {cite}`dimitrov_2022,wang_2022,liu_2022`, and are largely concordant with alternative data modalities such as intracellular signalling and spatial information {cite}`dimitrov_2022,liu_2022`.
# 
# In this chapter, we first provide an introduction and example to perhaps the most common and simplest CCC approaches, i.e. ligand-receptor inference with CellPhoneDB {cite}`efremova_2020` and LIANA {cite}`dimitrov_2022`. Then we showcase NicheNet as an example of a CCC inference method with a focus on intracellular activities downstream of CCC events {cite}`browaeys_2020`. Finally, we highlight the common assumptions and limitations of CCC inference from single-cell transcriptomics data as well as suggestions how to improve confidence in intercellular communication predictions. Note that here we generalize for the sake of simplicity, however, there are a plethora of different and newly emerging CCC approaches. We highlight some of those in the **Outlook** section.

# %% [markdown]
# <img src="../_static/images/mechanisms/cell_cell_communication.png" alt="CCC Overview" class="bg-primary mb-1" width="800px">
# 
# **FIGURE 22.1**. Cell-Cell Communication Overview

# %% [markdown]
# ## Environment setup

# %%
# Upstream code cell: 9
# python libs
import decoupler as dc
import liana as li
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import seaborn as sns
import session_info

# %%
# Upstream code cell: 10
# Setting up R dependencies
import anndata2ri

anndata2ri.activate()

%load_ext rpy2.ipython

# %%
# Upstream code cell: 11
%%R
suppressPackageStartupMessages({
    library(reticulate)
    library(ggplot2)
    library(tidyr)
    library(dplyr)
    library(purrr)
    library(tibble)
})

# %%
# Upstream code cell: 12
# figure settings
sc.settings.set_figure_params(dpi=200, frameon=False)
sc.set_figure_params(dpi=200, facecolor="white")
sc.set_figure_params(figsize=(5, 5))

# %% [markdown]
# ## Case Study

# %% [markdown]
# As a simple example, we will look at ~25k PBMCs from 8 lupus patients, each before and after IFN-β stimulation {cite}`kang2018multiplexed`. Note that by focusing on PBMCs, for the purpose of this tutorial, we assume that coordinated events occur among them.
# 
# So, let's first download the pre-processed data.

# %%
# Upstream code cell: 15
# Read in
adata = sc.read(
    "kang_counts_25k.h5ad", backup_url="https://figshare.com/ndownloader/files/34464122"
)

# Store the counts for later use
adata.layers["counts"] = adata.X.copy()

# %% [markdown]
# Apply basic quality control steps to remove any low quality cells and lowly expressed genes. We refer the user to the {ref}`quality-control` chapter for more extensive QC steps.

# %%
# Upstream code cell: 17
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

# %%
# Upstream code cell: 18
# Store the counts for later use
adata.layers["counts"] = adata.X.copy()
# Rename label to condition, replicate to patient
adata.obs = adata.obs.rename({"label": "condition", "replicate": "patient"}, axis=1)
# assign sample
adata.obs["sample"] = (
    adata.obs["condition"].astype("str") + "&" + adata.obs["patient"].astype("str")
)

# %% [markdown]
# We will also normalize the data to ensure that the count depth is equalized for all cells, given that we need the gene expression values to be comparable across the cell types. We refer the user to the {ref}`normalization` chapter for more information and alternative normalization approaches that might fit their data better.

# %%
# Upstream code cell: 20
# log1p normalize the data
sc.pp.normalize_total(adata)
sc.pp.log1p(adata)

# %% [markdown]
# In this case study, we will assume that cell types such as B cells and CD4 T cells carry out a signal mediator role, while others, such as CD8 T cells and Natural Killer cells, are composed of the cells that carry out the response. In other words, we will treat B and CD4 T cells as the sources of CCC signalling, while the latter are the receivers of CCC stimuli. This is of course an oversimplification as signalling sources and receivers are expected to be dynamic and multi-directional, thus the cell types that we treat as which category depends on the hypothesis in mind.

# %%
# Upstream code cell: 22
adata.obs["cell_type"].cat.categories

# %% [markdown]
# Show pre-computed UMAP, just to showcase the data

# %%
# Upstream code cell: 24
sc.pl.umap(adata, color=["condition", "cell_type"], frameon=False)

# %% [markdown]
# ### Ligand-receptor inference

# %% [markdown]
# First, let's use the CellPhoneDB (v2) ligand-receptor method {cite}`efremova_2020`.
# 
# We will run CellPhoneDB on the data post IFN-beta stimulation alone, as such methods were initially designed for the inference of CCC events in "steady-state" data, or in other words, they are meant to be used not across samples or conditions, but rather on a single condition or sample at a time. Note that, nevertheless, certain approaches exist to apply ligand-receptor methods across conditions but these are out of scope for this tutorial, and instead we refer to them in the **Outlook** section.

# %%
# Upstream code cell: 27
adata_stim = adata[adata.obs["condition"] == "stim"].copy()
adata_stim

# %%
# Upstream code cell: 28
# import cellphonedb method via liana
from liana.method import cellphonedb

# %% [markdown]
# CellPhoneDB is one of the most commonly-used CCC tools, it represents intercellular communication events as the average gene expression of the proteins involved in the interaction. The proteins involved can also be can also take the form of heteromeric complexes, and in that case the minimum gene expression of the subunits is considered. In addition to the expression average, interaction significance is determined against a null distribution, generated by shuffling the cell group labels.

# %% [markdown]
# Note that we are grouping by cell type and that the CCC statistics that we get will reflect the cell types that were previously pre-defined.

# %%
# Upstream code cell: 31
cellphonedb(
    adata_stim, groupby="cell_type", use_raw=False, return_all_lrs=True, verbose=True
)

# %% [markdown]
# By default, the results are written in place within the anndata object, more specifically in `.uns['liana_res']`.
# 
# Let's examine the output from the CellPhoneDB method:

# %%
# Upstream code cell: 33
adata_stim.uns["liana_res"].head()

# %% [markdown]
# Here, we see that stats are provided for both ligand and receptor entities, more specifically: - `ligand` and `receptor` are typically the two entities that interact. As a reminder, CCC events are not limited to secreted signalling, but we refer to them as `ligand` and `receptor` for simplicity. 
# 
# Also, in the case of heteromeric complexes, the `ligand` and `receptor` columns represent the subunit with minimum expression, while `*_complex` corresponds to the actual complex, with subunits being separated by `_`.
# 
# - `source` and `target` columns represent the source/sender and target/receiver cell identity for each interaction, respectively
# 
# - `*_props`: represents the proportion of cells that express the entity. 
# 
#   By default, in CellPhoneDB and LIANA, any interactions in which either entity is not expressed in above 10% of cells per cell type is considered as a false positive,
#   under the assumption that since CCC occurs between cell types, a sufficient proportion of cells within should express the genes.
# 
# - `*_means`: entity expression mean per cell type
# 
# - `lr_means`: mean ligand-receptor expression, as a measure of ligand-receptor interaction **magnitude**
# 
# - `cellphone_pvals`: permutation-based p-values, as a measure of interaction **specificity**
# 
# Note that `ligand`, `receptor`, `source`, and `target` columns are returned by every ligand-receptor method, while the rest of the columns can vary across the ligand-receptor methods, as each method relies on different assumptions and scoring functions, and hence each returns different ligand-receptor scores.
# Nevertheless, typically most methods use a pair of scoring functions - where one often corresponds to the **magnitude** (strength) of interaction and the other reflects the **specificity** of a given interaction to a pair of cell identities.

# %% [markdown]
# #### Visual exploration

# %% [markdown]
# We can now visualize the results that we just obtained as a dotplot, in which rows represent the prioritized interactions between source/sender (top) and target/receiver (bottom) cell types.

# %%
# Upstream code cell: 37
li.pl.dotplot(
    adata=adata_stim,
    colour="lr_means",
    size="cellphone_pvals",
    inverse_size=True,  # we inverse sign since we want small p-values to have large sizes
    # We choose only the cell types which we wish to plot
    source_labels=["CD4 T cells", "B cells", "FCGR3A+ Monocytes"],
    target_labels=["CD8 T cells", "CD14+ Monocytes", "NK cells"],
    # since cpdbv2 suggests using a filter to FPs
    # we can filter the interactions according to p-values <= 0.01
    filter_fun=lambda x: x["cellphone_pvals"] <= 0.01,
    # as this type of methods tends to result in large numbers
    # of predictions, we can also further order according to expression magnitude
    orderby="lr_means",
    orderby_ascending=False,  # we want to prioritize those with highest expression
    top_n=20,  # and we want to keep only the top 20 interactions
    figure_size=(9, 5),
    size_range=(1, 6),
)

# %% [markdown]
# Great, we get a number of interactions potentially linked to IFN-beta stimulation. 
# 
# We can also see that both the magnitude (expression strength) and specificity of the interactions are cell-type dependent.
# For example, the potential binding of HLA-B binding to CD8A/B logically occurs only when the receiver cells are CD8 T cells.

# %% [markdown]
# #### Generating a Ligand-Receptor consensus with LIANA

# %% [markdown]
# Given the reported limited agreement between the interactions inferred by different ligand-receptor methods, as a way to further increase the confidence in a potential interaction of interest, one could check if this interaction is predicted as relevant by more than a single method. In the same manner, one could also use multiple methods and focus on their consensus, or in other words focus on interactions consistently predicted as relevant. To this end, we will run the `rank_aggregate` method of liana {cite}`dimitrov_2022`, which generates a probability distribution of highly ranked interactions across the methods.

# %% [markdown]
# Let's first examine the ligand-receptor methods in LIANA:

# %%
# Upstream code cell: 42
li.method.show_methods()

# %% [markdown]
# Let's now run the Rank_Aggregate method, which will essentially run the other methods in the background and then generate a consensus.

# %%
# Upstream code cell: 44
from liana.method import rank_aggregate

# %%
# Upstream code cell: 45
rank_aggregate(
    adata_stim, groupby="cell_type", return_all_lrs=True, use_raw=False, verbose=True
)

# %% [markdown]
# Let's now check how the output of liana's rank_aggregate:

# %%
# Upstream code cell: 47
adata_stim.uns["liana_res"].drop_duplicates(
    ["ligand_complex", "receptor_complex"]
).head()

# %% [markdown]
# Here, we can see the output of the scoring functions of all methods (refer to the table above, if interested to map which score belong to which method). More importantly, we also get the `magnitude_rank` and `specificity_rank` for each interaction, which represent the consensus interaction **magnitude** (strength of expression) and **specificity** (across all cell type pairs), respectively. For example, going back to CellPhoneDB, `lr_mean` and `cellphone_pvals` will be correspondingly aggregated into those.

# %% [markdown]
# Let's generate the same plot, but now using the aggregate of the methods:

# %%
# Upstream code cell: 50
li.pl.dotplot(
    adata=adata_stim,
    colour="magnitude_rank",
    size="specificity_rank",
    inverse_colour=True,  # we inverse sign since we want small p-values to have large sizes
    inverse_size=True,
    # We choose only the cell types which we wish to plot
    source_labels=["CD4 T cells", "B cells", "FCGR3A+ Monocytes"],
    target_labels=["CD8 T cells", "CD14+ Monocytes", "NK cells"],
    # since the rank_aggregate can also be interpreted as a probability distribution
    # we can again filter them according to their specificity significance
    # yet here the interactions are filtered according to
    # how consistently highly-ranked is their specificity across the methods
    # filterby="specificity_rank",
    # filter_lambda=lambda x: x <= 0.05,
    filter_fun=lambda x: x["specificity_rank"] <= 0.05,
    # again, we can also further order according to magnitude
    orderby="magnitude_rank",
    orderby_ascending=True,  # prioritize those with lowest values
    top_n=20,  # and we want to keep only the top 20 interactions
    figure_size=(9, 5),
    size_range=(1, 6),
)

# %% [markdown]
# Although, the prioritized interactions by both CellPhoneDB and LIANA seem biologically-plausible and potentially relevant to the treatment, it is challenging to ascertain their relevance. In particular, the advantage of these methods to generate systems-level insights in a hypothesis-free manner happens to also be one of their major disadvantages. Specifically because ligand-receptor tools return all plausible ligand-receptor interactions for every pair of cell types, thus we end up with huge lists of interactions, and choosing targets for subsequent experimental validation can be challenging.
# 
# Thus, prior to experimental validation, we suggest that any potential interaction hypotheses should be supported with additional prior knowledge. This may include domain knowledge for the specific condition (e.g. cell types or receptors of interest), as well as orthogonal modalities, such as protein abundance, spatial co-localization, or downstream signalling. To this end, we also further refer the reader to the {ref}`enrichment-analysis` and **spatial CCC** (to be added) chapters.

# %% [markdown]
# (mechanisms-cell-cell-communication-key-takeaway-2)=
# ### Modelling differential intercellular signalling with NicheNet

# %% [markdown]
# NicheNet is another type of CCC method that considers the **intra**cellular signaling effects triggered by **inter**cellular interactions {cite}`browaeys_2020`. 
# 
# In short, NicheNet infers associations between ligands and the downstream targets that they potentially modulate {cite}`browaeys_2020`. Or in other words, NicheNet assumes that a certain sender/source cell type produces a ligand, and the binding of that ligand to a specific receiver/target cell type(s) leads to a signal propagation that affects master gene regulators, or transcription factors, and subsequently their targets. Therefore, predictions on which target genes are modulated by which ligand-receptor pairs may provide interesting hypotheses concerning the ongoing CCC events. Furthermore, enrichment of target genes of a specific ligand-receptor pair in a receiver cell type can also indicate that this ligand-receptor pair is functionally active. In summary, a NicheNet analysis can thus be performed to 1) infer potential target genes of expressed ligand-receptor interactions and 2) prioritize ligand-receptor interactions based on their target gene enrichment in the receiver. This enrichment is called “ligand activity”, in analogy to transcription factor activity {ref}`enrichment-analysis`. 
# 
# To perform these tasks, NicheNet makes use of prior knowledge about ligand-target associations. However, contrary to ligand-receptor databases, comprehensive ligand-target databases do not exist. Therefore, NicheNet predicts ligand-target associations by integrating  three layers of prior knowledge covering ligand-receptor, intracellular signaling, and gene regulatory interactions. Using these three layers of information, NicheNet calculates a regulatory potential score for each ligand-target link. This regulatory potential denotes how well prior knowledge supports that a ligand may regulate the expression of a target gene. To calculate regulatory potential, NicheNet first employs a network diffusion algorithm, known as Personalized PageRank (PPR), on the integrated signaling network to estimate the probability that a given ligand may signal to a particular regulator.  Specifically, the PPR implementation in NicheNet considers a given ligand as the seed node of interest. Hereby, nodes that are closer to the ligand in the signaling network get higher scores than more distant nodes under the assumption that regulators in the network vicinity of the ligand are more likely modulated by the ligand than more distant nodes. The application of PPR for all ligands in the database thus results in a ligand-regulator matrix of signalling probabilities that are then multiplied with a weight matrix of regulators to target genes in order to obtain ligand-target regulatory potential scores {cite}browaeys_2020. Conceptually, this implies that a ligand–target pair receives a high regulatory potential score if the ligand can signal to regulators of that target gene. These prior knowledge-derived scores are then used in conjunction with the expression data of interacting cells to prioritize ligand-receptor interactions and predict their target genes. 
# 
# Because NicheNet focuses on how ligands affect gene expression in potentially interacting cells, one needs to be able to define which gene expression changes may (partially) be caused by CCC processes.  To rank the ligands according to their potential ligand activity in a receiver cell type, it requires a set of genes assumed to be affected by CCC events in the receiver cell types. The authors of NicheNet recommend ideally defining those sets of genes when working with conditions, e.g. treatment  vs control. To this end, we will apply NicheNet in exactly that manner and compare the expression of the patients in our data before and after stimulation with IFN-beta.
# 
# For a more detailed description of the NicheNet method, we specifically refer the reader to the footprint part of the {ref}`enrichment-analysis` chapter as well as NicheNet's [tutorials](https://github.com/saeyslab/nichenetr) and manuscript {cite}`browaeys_2020`.

# %% [markdown]
# #### Load NicheNet Prior-Knowledge

# %% [markdown]
# As mentioned above, NicheNet requires  prior knowledge about ligand-receptor interactions and ligand-target links:
# - a ligand_target_matrix - denotes the potential that a ligand might regulate the expression of a target genes. The weights in this matrix are based on prior knowledge and are required to prioritize possible ligand-receptor interactions and affected target genes.
# 
# - lr_network - the database of ligand-receptor interactions needed to define expressed ligands, receptors and their interactions.
# 
# We will load each of those from Zenodo [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7074291.svg)](https://doi.org/10.5281/zenodo.7074291) (this might take a couple of minutes).

# %%
# Upstream code cell: 56
%%R
# load NicheNet (NicheNet is only available on GitHub)
suppressPackageStartupMessages({
    if(!require(nichenetr)) remotes::install_github("saeyslab/nichenetr", upgrade = "never")
})

# %%
# Upstream code cell: 57
%%R
# Increase timeout threshold
options(timeout=600)

# Load PK
ligand_target_matrix <- readRDS(url("https://zenodo.org/record/7074291/files/ligand_target_matrix_nsga2r_final.rds"))
lr_network <- readRDS(url("https://zenodo.org/record/7074291/files/lr_network_human_21122021.rds"))

# %% [markdown]
# Moreover, one may also tailor the NicheNet prior knowledge and contextualize the networks according to the data at hand using the [OmnipathR](https://github.com/saezlab/OmnipathR) package.

# %% [markdown]
# ##### Step 1. Define cell types of interest to be considered as senders/sources and receiver/targets of CCC interactions
# Here, we will assume that multiple cell types are able to affect the receiver cell type

# %%
# Upstream code cell: 60
sender_celltypes = ["CD4 T cells", "B cells", "FCGR3A+ Monocytes"]
receiver_celltypes = ["CD8 T cells"]

# %% [markdown]
# ##### Step 2. Define a set of ligands that can **potentially** affect receiver cell types
# 
# Similarly to the ligand-receptor methods above, here we are only interested in the potential interactions that involve sufficiently expressed genes in each cell type. So, we will assume that e.g. 10% of the cells is a good threshold to reflect genes as expressed within a cell type.

# %%
# Upstream code cell: 62
# Helper function to obtain sufficiently expressed genes
from functools import reduce


def get_expressed_genes(adata, cell_type, expr_prop):
    # calculate proportions
    temp = adata[adata.obs["cell_type"] == cell_type, :]
    a = temp.X.getnnz(axis=0) / temp.X.shape[0]
    stats = (
        pd.DataFrame({"genes": temp.var_names, "props": a})
        .assign(cell_type=cell_type)
        .sort_values("genes")
    )

    # obtain expressed genes
    stats = stats[stats["props"] >= expr_prop]
    expressed_genes = stats["genes"].values

    return expressed_genes

# %%
# Upstream code cell: 63
sender_expressed = reduce(
    np.union1d,
    [
        get_expressed_genes(adata, cell_type=cell_type, expr_prop=0.1)
        for cell_type in sender_celltypes
    ],
)
receiver_expressed = reduce(
    np.union1d,
    [
        get_expressed_genes(adata, cell_type=cell_type, expr_prop=0.1)
        for cell_type in receiver_celltypes
    ],
)

# %% [markdown]
# Then use this information to keep only ligand-receptor pairs in the NicheNet network that are expressed.

# %%
# Upstream code cell: 65
%%R -i sender_expressed -i receiver_expressed
# get ligands and receptors in the resource
ligands <- lr_network %>% pull(from) %>% unique()
receptors <- lr_network %>% pull(to) %>% unique()

# only keep the intersect between the resource and the data
expressed_ligands <- intersect(ligands, sender_expressed)
expressed_receptors <- intersect(receptors, receiver_expressed)

# filter the network to only include ligands for which both the ligand and receptor are expressed
potential_ligands <- lr_network %>% 
  filter(from %in% expressed_ligands & to %in% expressed_receptors) %>%
  pull(from) %>% unique()

# %% [markdown]
# ##### Step 3. Define a gene set of interest in receiver cell type(s)
# 
# This step is the most critical one in a NicheNet analysis. Here, one defines which genes are potentially modulated by cell-cell communication, i.e. the genes thought to be affected by ligand signalling. For example, one can assume that {term}`differentially expressed genes <Differential gene expression (DGE)>` between conditions in receiver cell type(s) are driven by ligands from one of more interacting sender cell populations. Another example would be differentially expressed genes between a differentiated cell population and a progenitor population in case the differentiation is likely induced through interactions with other cell types.

# %% [markdown]
# So, we will now use `decoupler` to generate {term}`pseudobulk` profiles per cell type and sample, and then perform a differential expression analysis on those. A crucial step of pseudo-bulking is filtering out genes that are not expressed across most cells and samples, since they are very noisy and can result in unstable log-fold changes. To get robust profiles, genes are thus filtered out if again they are not expressed sufficiently per sample (min_prop) and in not enough samples. We refer the reader to the {ref}normalization and {ref}differential-analysis chapters for more info on differential expression analysis and pseudobulk profiles.

# %%
# Upstream code cell: 68
# Get pseudo-bulk profile
pdata = dc.get_pseudobulk(
    adata,
    sample_col="sample",
    groups_col="cell_type",
    min_prop=0.1,
    min_smpls=3,
    layer="counts",
)

# %% [markdown]
# Normalize the pseudobulk counts

# %%
# Upstream code cell: 70
# Storing the raw counts
pdata.layers["counts"] = pdata.X.copy()

# Does PC1 captures a meaningful biological or technical fact?
pdata.obs["lib_size"] = pdata.X.sum(1)

# Normalize
sc.pp.normalize_total(pdata, target_sum=1e4)
sc.pp.log1p(pdata)
# check how this looks like
pdata

# %% [markdown]
# Then we perform a very simple differential analysis contrast. For this example we will use t-test as is implemented in `scanpy` but we could use any other.

# %%
# Upstream code cell: 72
logFCs, pvals = dc.get_contrast(
    pdata,
    group_col="cell_type",
    condition_col="condition",
    condition="stim",
    reference="ctrl",
    method="t-test",
)

# %% [markdown]
# Then keep only the positive significant differentially expressed genes in the receiver cell type(s)

# %%
# Upstream code cell: 74
# Visualize those for e.g. CD14+ Monocytes
dc.plot_volcano(logFCs, pvals, "CD14+ Monocytes", top=15, sign_thr=0.05, lFCs_thr=1)

# %%
# Upstream code cell: 75
# format results
deg = dc.format_contrast_results(logFCs, pvals)
# only keep the receiver cell type(s)
deg = deg[np.isin(deg["contrast"], receiver_celltypes)]
deg.head()

# %% [markdown]
# Now that we have the DE stats for the receiver cell type, we can use those to define the background and geneset of interest for ligand activity analysis with NicheNet.

# %%
# Upstream code cell: 77
# define background of sufficiently expressed genes
background_genes = deg["name"].values

# only keep significant and positive DE genes
deg = deg[(deg["pvals"] <= 0.05) & (deg["logFCs"] > 1)]
# get geneset of interest
geneset_oi = deg["name"].values

# %% [markdown]
# ##### Step 4. NicheNet ligand activity estimation
# 
# To estimate ligand activity, NicheNet uses the regulatory potential of genes (based on prior knowledge) to predict which ligand best predicts the gene set of interest.
# Or in other words, it assesses whether the genes with high regulatory potential in regards to a specific ligand, are more likely to belong to the geneset of interest that we derive for the receiver cell type(s).
# Conceptually, this is not too dissimilar from standard {ref}`enrichment-analysis` and NicheNet proposes different ways to estimate ligand activity, such as the area under the receiver operating characteristic curve, or Pearson correlation {cite}`browaeys_2020`.

# %%
# Upstream code cell: 79
%%R -i geneset_oi -i background_genes -o ligand_activities

ligand_activities <- predict_ligand_activities(geneset = geneset_oi, 
                                               background_expressed_genes = background_genes,
                                               ligand_target_matrix = ligand_target_matrix,
                                               potential_ligands = potential_ligands)

ligand_activities <- ligand_activities %>% 
  arrange(-aupr) %>% 
  mutate(rank = rank(desc(aupr)))

# show top10 ligand activities
head(ligand_activities, n=10)

# %% [markdown]
# ##### Step 5. Infer & Visualize top-predicted target genes for top ligands

# %%
# Upstream code cell: 81
%%R -o vis_ligand_target
top_ligands <- ligand_activities %>%
  top_n(15, aupr) %>% 
  arrange(-aupr) %>%
  pull(test_ligand) %>%
  unique()

# get regulatory potentials
ligand_target_potential <- map(top_ligands,
                               ~get_weighted_ligand_target_links(.x,
                                                                 geneset = geneset_oi,
                                                                 ligand_target_matrix = ligand_target_matrix,
                                                                 n = 500)
                              ) %>%
    bind_rows() %>% 
    drop_na()
    
# prep for visualization
active_ligand_target_links <- 
  prepare_ligand_target_visualization(ligand_target_df = ligand_target_potential, 
                                      ligand_target_matrix = ligand_target_matrix)

# order ligands & targets
order_ligands <- intersect(top_ligands,
                           colnames(active_ligand_target_links)) %>% rev() %>% make.names()
order_targets <- ligand_target_potential$target %>%
  unique() %>% 
  intersect(rownames(active_ligand_target_links)) %>%
  make.names()
rownames(active_ligand_target_links) <- rownames(active_ligand_target_links) %>%
  make.names() # make.names() for heatmap visualization of genes like H2-T23
colnames(active_ligand_target_links) <- colnames(active_ligand_target_links) %>%
  make.names() # make.names() for heatmap visualization of genes like H2-T23

vis_ligand_target <- active_ligand_target_links[order_targets, order_ligands] %>%
  t()
    
# convert to dataframe, and then it's returned to py
vis_ligand_target <- vis_ligand_target %>%
    as.data.frame() %>%
    rownames_to_column("ligand") %>%
    as_tibble()

# %%
# Upstream code cell: 82
# convert dot to underscore and set ligand as index
vis_ligand_target["ligand"] = vis_ligand_target["ligand"].replace(
    r"\.", "_", regex=True
)
vis_ligand_target.set_index("ligand", inplace=True)
# keep only columns where at least one gene has a regulatory potential >= 0.05
vis_ligand_target = vis_ligand_target.loc[
    :, vis_ligand_target[vis_ligand_target >= 0.05].any()
]
vis_ligand_target.head()

# %% [markdown]
# ##### Visualize top ligands & regulatory targets

# %%
# Upstream code cell: 84
fig, ax = plt.subplots(1, 1, figsize=(15, 5))
sns.heatmap(vis_ligand_target, xticklabels=True, ax=ax)
plt.show()

# %% [markdown]
# Perfect, we end up with ligands that are most probable to affect downstream signalling in the receiver cell type(s), as well as their most likely targets.

# %% [markdown]
# ### Combining NicheNet output with ligand-receptor inference

# %% [markdown]
# NicheNet and ligand-receptor methods are not exclusive, but rather complementary, as they address different questions and in different ways. Ligand-receptor methods, such as the ones that we show above, infer ligand-receptor interactions using the expression of interacting ligands and receptors, and typically work on "steady-state" data. On the contrary, NicheNet predicts which of these inferred ligand-receptor links are possibly the most functional based on gene expression changes that are induced in the target cell type(s), in a process largely dependent on prior knowledge alone. Thus, while the choice of tool depends on the research question, one could also see ligand-receptor (e.g. CellPhoneDB or LIANA) methods and intracellular signalling CCC methods (e.g. NicheNet) as complementary.

# %% [markdown]
# For example, given the top 3 prioritized ligands, we can focus on ligand-receptor pairs that include those and the receiver cell type that we used to infer the active ligands.
# 
# So, let's see which ligand-receptor interactions that involve the top 5 potentially active ligands from NicheNet were prioritized as consistently relevant by the different methods in LIANA:

# %%
# Upstream code cell: 89
ligand_oi = ligand_activities.head(3)["test_ligand"].values

# %%
# Upstream code cell: 90
ligand_oi

# %%
# Upstream code cell: 91
li.pl.dotplot(
    adata=adata_stim,
    colour="lr_means",
    size="cellphone_pvals",
    inverse_size=True,  # we inverse sign since we want small p-values to have large sizes
    # We choose only the cell types which we wish to plot
    source_labels=sender_celltypes,
    target_labels=receiver_celltypes,
    # keep only those ligands
    # filterby="ligand_complex",
    # filter_lambda=lambda x: np.isin(x, ligand_oi),
    filter_fun=lambda x: x["ligand_complex"] <= 0.01,
    # as this type of methods tends to result in large numbers
    # of predictions, we can also further order according to
    # expression magnitude
    orderby="magnitude_rank",
    orderby_ascending=False,  # we want to prioritize those with highest expression
    top_n=25,  # and we want to keep only the top 25 interactions
    figure_size=(9, 9),
    size_range=(1, 6),
)

# %% [markdown]
# From the results, above we can now see the specific ligand-receptor interactions potentially associated with the inferred ligand activities by NicheNet. Moreover, we can hypothesize that the ligand activities inferred by NicheNet, are perhaps affecting the cell types via ligand-receptor interactions specific to some cell type pairs (e.g. *HLA-A -> CD3G*). Or in other words, while the same ligands may be active as a consequence of IFN-β stimulation, they potentially induce cell-type specific signal transduction changes.

# %% [markdown]
# While we use NicheNet and LIANA in this case, some recent CCC tool developments provide various combinations of the ideas and assumptions in these two categories of CCC inference methods (e.g. {cite}`zhang2021cellcall,zhang2021cellinker,baruzzo2022identify`).

# %% [markdown]
# ## Key takeaways

# %% [markdown]
# ### Assumptions & Limitations
# 
# The shared purpose of the methods considered in this work is to predict the most relevant intercellular interactions between different cell types using single-cell transcriptomics data. Thus, all methods assume that the gene expression of different cell types is an informative proxy of the CCC events that occur within the sampled tissue. While single-cell transcriptomics enables the inference of CCC events at a previously unprecedented scale, some assumptions and limitations should be kept in mind. 
# Starting with the assumption that protein co-expressions reflect intercellular interactions, and consequently they are also reflective of any events preceding the interaction, including protein translation and processing, secretion, and diffusion {cite}`armingol_2021,dimitrov_2022` (**Figure 22.2**). Furthermore, if cell communication within an organism is conceptualized as the combination of CCC events that occur at different 'length scales' or ranges {cite}`palla2022spatial`, then the CCC events that can be inferred from single-cell transcriptomics are potentially limited to only the protein-mediated events that occur at 'local' ranges, i.e. between the cell types were sampled. As a result, long-range signalling and CCC driven by other molecules, such as endocrine signalling and system gradients like Calcium and Oxygen concentrations, are likely not captured {cite}`dimitrov_2022`.
# 
# In addition, while the grouping of cell types according to their lineage is common practice to structure our data, when considering the tissue as the place where communication takes place, interactions do not necessarily occur between cell types but rather individual cells {cite}`wilk_2022`. Also, the intercellular interactions are typically presented as one-to-one events between cell types and/or proteins. Therefore, the assumption that the potential co-expression events across cell types might not necessarily reflect true signalling as in order to fundamentally capture the events within a local community, one must identify the magnitude, directionality and biological relevance of the messages passed between the cells within that community {cite}`armingol_2021`.

# %% [markdown]
# ### Summary & Outlook:
# 
# In this chapter we presented two applications of CCC inference methods, namely we used CellPhoneDB and LIANA to predict relevant ligand-receptor interactions from single-context (or steady-state) data and NicheNet to infer potentially active ligands and their targets in a differential-expression context. 
# As the focus of the single-cell field moves further away from the definition of lineages, and into characterizing changes within cell types between conditions, approaches to disentangle CCC insights across contexts are becoming essential. Thus, in addition to NicheNet, we refer the user to other approaches that enable cross-condition comparisons, such as NATMI's differential cell-connectivity analysis {cite}`hou2020predicting`, Crosstalker's network topological measures {cite}`nagai2021crosstalker`, CellChat's pathway-focused manifold learning {cite}`jin_2021`, as well as Tensor-cell2cell's untargeted factorization approach to infer CCC patterns across contexts {cite}`armingol_2022`. 
# 
# As a consequence of the ongoing developments within the single-cell and the cell-cell communication field specifically, there is an ever-growing number of methods, some of which propose alternative ways to predict CCC events, such as those that work at the single-cell resolution {cite}`raredon_2023,wang_2019,wilk_2022`. While others attempt to address some of the limitations above, e.g. by including the inference of interactions mediated by metabolites or small molecules {cite}`zheng_2022,garciaalonso_2022,zhang_2021`.
# 
# Albeit, this chapter does not capture the diversity and all current developments of the CCC field in dissociated single-cell data, it serves to highlight some of the general ideas and limitations. Thus, we intend it as a starting point upon which the reader can expand on by combining their knowledge from other chapters, and further reading within the CCC field itself.

# %% [markdown]
# <img src="../_static/images/mechanisms/ccc_limitations.png" alt="CCC Overview" class="bg-primary mb-1" width="800px">
# 
# **FIGURE 22.2**. Assumptions and Limitations of Cell-Cell Communication from single-cell transcriptomics data

# %% [markdown]
# ## Quiz

# %%
# Upstream code cell: 99
%run ../src/lib.py

flip_card(
    "q1",
    "What are the first three limitations that come to mind when inferring CCC from single-cell transcriptomics data?",
    "Spatial context absence, post-transcriptional modifications, temporal dynamics",
)
flip_card(
    "q2",
    "What is the role of heteromeric complexes in ligand-receptor inference?",
    "Heteromeric complexes, composed of multiple protein subunits, function collectively as a single receptor or ligand.",
)
flip_card(
    "q3",
    "Can you think of an advantage and a disadvantage of inference based on prior-knowledge?",
    "Advantage: Utilizing established databases of ligand-receptor pairs can enhance the accuracy of inferred interactions by providing a validated framework. Disadvantage: Reliance on prior knowledge may bias analyses toward well-characterized interactions, potentially overlooking novel or context-specific communications not documented in existing databases.",
    back_font_size=13,
)
flip_card(
    "q4",
    "Can you think of an important limitation we should consider here regarding the definition of the geneset of interest for the NicheNet analysis on the IFN-beta stimulated PBMC dataset?",
    "An important limitation is ensuring that the gene set of interest accurately reflects the biological response to IFN-beta stimulation. If the selected genes are not truly responsive to IFN-beta, the analysis may yield misleading insights into the signaling pathways and interactions involved.",
    front_font_size=15,
    back_font_size=13,
)

# %% [markdown]
# ## Contributions
# 
# ### Authors:
#  - Daniel Dimitrov
# 
# ### Reviewers:
#  - Lukas Heumos
#  - Gregor Sturm
#  - Robin Browaeys

# %% [markdown]
# ## Session Info

# %%
# Upstream code cell: 102
%%R
sessionInfo()

# %%
# Upstream code cell: 103
session_info.show()

# %% [markdown]
# ## References

# %% [markdown]
# ```{bibliography}
# :filter: docname in docnames
# ```
