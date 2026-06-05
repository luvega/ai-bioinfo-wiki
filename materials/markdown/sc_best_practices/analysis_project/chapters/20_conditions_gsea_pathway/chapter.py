# Auto-generated from single-cell-best-practices.
# Title: Gene set enrichment and pathway analysis
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/conditions/gsea_pathway.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (enrichment-analysis)=
# 
# # Gene set enrichment and pathway analysis

# %% [markdown]
# (conditions-gsea-pathway-key-takeaway-3)=
# ## Motivation

# %% [markdown]
# Single-cell RNA-seq provides unprecedented insights into variations in cell types between conditions, tissue types, species and individuals. {term}`Differential gene expression analysis <Differential gene expression (DGE)>` of the single-cell data is almost always followed by *gene set enrichment analysis*, where the aim is to identify gene programs, such as biological processes, gene ontologies or regulatory pathways that are over-represented in an experimental condition compared to control or other conditions, on the basis of differentially expressed (DE) genes. 
# 
# To determine the pathways enriched in a cell type-specific manner between two conditions, first a relevant collection of gene set signatures is selected, where each gene set defines a biological process (e.g. epithelial to mesenchymal transition, metabolism etc) or pathway (e.g. MAPK signalling). For each gene set in the collection, DE genes present in the gene set are used to obtain a test statistic that is then used to assess the enrichment of the gene set. Depending on the type of the enrichment test chosen, gene expression measurements may or may not be used for the computation of the test statistic. 
# 
# In this chapter, we first provide an overview of different types of gene set enrichment tests, introduce some commonly used gene signature collections and discuss best practices for pathway enrichment and functional enrichment analysis in general.  We conclude the chapter by demonstrating three analytical approaches for gene set enrichment analysis. Note that we use the terms pathway analysis, pathway enrichment analysis, gene set enrichment analysis and functional analysis interchangeably in this chapter.

# %% [markdown]
# ## Pathway and gene set collections

# %% [markdown]
# Gene sets are a curated list of gene names (or gene ids) that are known to be involved in a biological process through previous studies and/or experiments. The Molecular Signatures Database (MSigDB) {cite}`subramanian2005gene,liberzon2011molecular` is the most comprehensive database consisting of 9 collections of gene sets. Some commonly used collections are C5, which is the gene ontology (GO) collection, C2 collection of curated gene signatures from published studies that are typically context (e.g. tissue, condition) specific, but also include KEGG and REACTOME gene signatures. For cancer studies, the Hallmark collection is commonly used, and for immunologic studies the C7 collection is a common choice. Note that these signatures are mainly derived from Bulk-seq measurements and measure continuous phenotypes. Recently and with the wide-spread availability of scRNA-seq datasets, databases have evolved that provide curated marker lists derived from published single cell studies that define cell types in various tissues and species. These include CellMarker {cite}`zhang2019cellmarker` and PanglaoDB {cite}`franzen2019panglaodb`. Curated marker lists are not limited to those made available in databases, and can be curated by oneself.

# %% [markdown]
# (conditions-gsea-pathway-key-takeaway-2)=
# ## Null hypotheses in gene set enrichment analysis

# %% [markdown]
# Gene set tests can be *competitive* or *self-contained* as defined by Goeman and Buhlmann (2007) {cite}`goeman2007analyzing`. Competitive gene set testing tests whether the genes in the set are highly ranked in terms of differential expression relative to the genes not in the set. The sampling unit here is genes, so the test can be done with a single sample (i.e. single-sample GSEA). The test requires genes that are not in the set (i.e background genes). In self-contained gene set testing, the sampling unit is the subject, so multiple samples per group are required, but it is not required to have genes that are not present in the set. A self-contained gene set test tests whether genes in the test set are differentially expressed without regard to any other gene measured in the dataset. These distinctions between the two null hypotheses make differences to the interpretation of gene set enrichment results. Note that in biological data there exist inter-gene correlations, that is the expression of genes in the same pathways are correlated. There are only a few tests that accommodate inter-gene correlations. We will discuss these methods later. Detailed explanations on various gene set tests can be found in [*limma* user manual](https://bioconductor.org/packages/release/bioc/manuals/limma/man/limma.pdf).

# %% [markdown]
# ## Gene set tests and pathway analysis

# %% [markdown]
# In scRNA-seq data analysis, gene set enrichment is generally carried out on clusters of cells or cell types, one-at-a-time. Genes differentially expressed in a cluster or cell type are used to identify over-represented gene sets from the selected collection, using simple hypergeometric tests or Fisher's exact test (as in *Enrichr* {cite}`chen2013enrichr`), for example. Such tests do not require the actual gene expression measurements and read counts to compute enrichment statistics, as they rely on testing how significant it is that an $X$ number of genes in a gene set are differentially expressed in the experiment compared to the number of non-DE genes in the set.
# 
# *fgsea* {cite}`korotkevich2021fast` is a more common tool for gene set enrichment test. *fgsea* is a computationally faster implementation of the well established *Gene Set Enrichment Analysis (GSEA)* algorithm {cite}`subramanian2005gene`, which computes enrichment statistics on the basis of some preranked gene-level test statistics. *fgsea* computes an enrichment score using some signed statistics of the genes in the gene set, such as  the t-statistics, log fold-changes (logFC) or p-values from the differential expression test. An empirical (estimated from the data) null distribution is computed for the enrichment score using some random gene sets of the same size, and a p-value is computed to determine the significance of the enrichment score. The p-values are then adjusted for multiple hypothesis testing. GSVA {cite}`hanzelmann2013gsva` is another example of preranked gene set enrichment approaches. We should note that the pre-ranked gene set tests are not specific to single cell datasets and apply to Bulk-seq assays as well.
# 
# An alternative approach to test for gene set enrichment in a group of cells, that is clusters or cells of identical types, is to create pseudo-bulk samples from single cells and use gene set enrichment methods developed for Bulk RNA-seq. Several self-contained and competitive gene set enrichment tests, namely *fry* and *camera* are implemented in *limma* {cite}`ritchie2015limma`, which are compatible with the differential gene expression analysis framework through linear models and Empirical Bayes moderation of test statistics {cite}`smyth2005limma`. Linear models can accommodate complex experimental designs (e.g. subjects, perturbations, batches, nested contrasts, interactions etc) through the design matrix. In addition, the `camera` and `roast` gene set tests implemented in limma account for inter-gene correlations. Gene set tests in *limma* can also be applied to (properly transformed and normalised) single cell measurements without pseudo-bulk generation. However, there are currently no benchmarks that had assessed the accuracy of gene set test results when these methods are applied directly to single cells.  
# 
# 
# 
# 
# | Test | Bulk or SC  | Type of Null Hypothesis | Input |
# | :------------ |:---------------:|:----------:| :-------
# | Hypergeometric  | both | competitive  | gene counts |
# | Fisher's Exact  | both | competitive |  gene counts | 
# | GSEA$^*$          | bulk | competitive| gene ranks |
# | GSVA$^*$          | bulk | competitive | gene ranks|
# | fgsea           | both | competitive | gene ranks |
# | fry$^*$             | bulk | self-contained | expression matrix |
# | camera$^*$          | bulk | competitive | expression matrix |
# | roast$^*$           | bulk | self-contained | expression matrix|
# 
# Table: Gene set tests, type of the applicable assays and Null Hypothesis they test
# 
# $^*$ These tests are practically applicable to single cell datasets, although their application to single cell may not be a common practice.

# %% [markdown]
# ### Gene set test vs. pathway activity inference

# %% [markdown]
# Gene set tests test whether a pathway is enriched, in other words over-represented, in one condition compared to others, say, in healthy donors compared to severe COVID-19 patients in the monocyte population. An alternative approach is to simply score the activity of a pathway or gene signature, in absolute sense, in individual cells, rather than testing for a differential activity between conditions. Some of the widely used tools for inference of gene set activity in general (including pathway activity) in individual cells include *VISION* {cite}`detomaso2019functional`, *AUCell* {cite}`aibar2017scenic`, pathway overdispersion analysis using *Pagoda2* {cite}`fan2016characterizing, lake2018integrative` and simple combined z-score {cite}`lee2008inferring`. 
# 
# *DoRothEA* {cite}`garcia2019benchmark` and *PROGENy* {cite}`schubert2018perturbation` are among functional analysis tools developed to infer transcription factor (TF) - target activities originally in Bulk RNA data. Holland et al. {cite}`holland2020robustness` found that Bulk RNA-seq methods *DoRothEA* and *PROGENy* have optimal performance in simulated scRNA-seq data, and even partially outperform tools specifically designed for scRNA-seq analysis despite the drop-out events and low library sizes in single cell data. Holland et al. also concluded that pathway and TF activity inference is more sensitive to the choice of gene sets rather than the statistical methods. This observation though can be specific to functional enrichment analyses and be explained by the fact that TF-target relations are context-specific; that is TF-target associations in one cell type may actually differ from another cell type or tissue.  
# 
# In contrast to Holland et al., Zhang et al. {cite}`zhang2020benchmarking` found that single-cell-based tools, specifically Pagoda2, outperform bulk-based methods from three different aspects of accuracy, stability and scalability. It should be noted that pathway and gene set activity inference tools inherently do not account for batch effects or biological variations other than the biological variation of interest. Therefore, it is up to the data analyst to ensure that the differential gene expression analysis step has worked properly.
# 
# Furthermore, while the tools mentioned here score every gene set in individual cells, they are not able to select for the most biologically relevant gene sets among all scored gene sets. scDECAF (https://github.com/DavisLaboratory/scDECAF) is a gene set activity inference tool that allows data-driven selection of the most informative gene sets, thereby aids in dissecting meaningful cellular heterogeneity.

# %% [markdown]
# ## Technical considerations

# %% [markdown]
# ### Filtering out the gene sets with low number of genes

# %% [markdown]
# A common practice is to exclude any gene sets with a few genes overlapping the data or Highly Variable Genes (HVG) in the pre-processing step. Zhang et al. {cite}`zhang2020benchmarking` found that the performance of both single-cell-based and bulk-based methods drops as gene coverage, that is the number of genes in pathways/gene sets, decreases. Holland et al {cite}`holland2020robustness` also found that gene sets of smaller size adversely impacts the performance of Bulk-seq *DoRothEA* and *PROGENy* on single cell data. These report collectively support that filtering gene sets with low gene counts, say less than 10 or 15 genes in the set, is beneficial in pathway analysis. Damian & Gorfine (2004) {cite}`damian2004statistical` attributed this to the fact gene variances in gene sets with a smaller number of genes are more likely to be large, whereas gene variances in larger gene sets tend to be smaller. This impacts the accuracy of the test statistics computed to test for enrichment. Zhang et al. additionally found that pathway analysis was susceptible to normalization procedures applied to gene expression measurements.

# %% [markdown]
# (conditions-gsea-pathway-key-takeaway-1)=
# ### Data normalization

# %% [markdown]
# Read counts in single cell experiments are typically normalised early on in the pre-processing pipeline to ensure that measurements are comparable across cells of various library sizes. Zhang et al. {cite}`zhang2020benchmarking` found that normalisation by *SCTransform* {cite}`hafemeister2019normalization` and *scran* {cite}`lun2016step` generally improves the performance of both single-cell- and bulk-based pathway scoring tools. They found that the performance of *AUCell* (a rank-based method) and *z-score* (transformation to zero mean, unit standard deviation) is particularly affected by normalization with distinct methods.

# %% [markdown]
# ## Case study: Pathway enrichment analysis and activity level scoring in human PBMC single cells

# %% [markdown]
# ### Prepare and explore the data

# %% [markdown]
# We first download the 25K PBMC data and follow the standard `scanpy` workflow for normalisation of read counts and subsetting on the highly variable genes. The dataset contains untreated and IFN-$\beta$ stimulated human PBMC cells {cite}`gspa:kang2018`. We explore patterns of variation in the data with UMAP representation of 4000 highly variable genes.

# %%
# Upstream code cell: 20
from __future__ import annotations

import anndata as ad
import decoupler
import numpy as np
import pandas as pd
import scanpy as sc
import seaborn.objects as so
import session_info

# %%
# Upstream code cell: 21
sc.settings.set_figure_params(dpi=200, frameon=False)
sc.set_figure_params(dpi=200)
sc.set_figure_params(figsize=(4, 4))

# %%
# Upstream code cell: 22
# Filtering warnings from current version of matplotlib
import warnings

warnings.filterwarnings(
    "ignore", message=".*Parameters 'cmap' will be ignored.*", category=UserWarning
)
warnings.filterwarnings(
    "ignore", message="Tight layout not applied.*", category=UserWarning
)

# %%
# Upstream code cell: 23
# Setting up R dependencies
import anndata2ri

%load_ext rpy2.ipython

anndata2ri.activate()

# %%
# Upstream code cell: 24
%%R
suppressPackageStartupMessages({
    library(SingleCellExperiment)
})

# %%
# Upstream code cell: 25
adata = sc.read(
    "kang_counts_25k.h5ad", backup_url="https://figshare.com/ndownloader/files/34464122"
)
adata

# %%
# Upstream code cell: 26
# Storing the counts for later use
adata.layers["counts"] = adata.X.copy()
# Renaming label to condition
adata.obs = adata.obs.rename({"label": "condition"}, axis=1)

# Normalizing
sc.pp.normalize_total(adata)
sc.pp.log1p(adata)

# %%
# Upstream code cell: 27
# Finding highly variable genes using count data
sc.pp.highly_variable_genes(
    adata, n_top_genes=4000, flavor="seurat_v3", subset=False, layer="counts"
)

# %%
# Upstream code cell: 28
adata

# %% [markdown]
# While the current object comes with UMAP and PCA embeddings, these have been corrected for stimulation condition, which we don't want for this analysis. Instead we will recompute these.

# %%
# Upstream code cell: 30
sc.pp.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)

# %%
# Upstream code cell: 31
sc.pl.umap(
    adata,
    color=["condition", "cell_type"],
    frameon=False,
    ncols=2,
)

# %% [markdown]
# We generally recommend determining the differentially expressed genes as outlined in the `Differential gene expression` chapter. For simplicity, here we run a t-test using `rank_genes_groups` in `scanpy` to rank genes according to their test statistics for differential expression:

# %%
# Upstream code cell: 33
adata.obs["group"] = adata.obs.condition.astype("string") + "_" + adata.obs.cell_type

# %%
# Upstream code cell: 34
# find DE genes by t-test
sc.tl.rank_genes_groups(adata, "group", method="t-test", key_added="t-test")

# %% [markdown]
# Let's extract the ranks for genes differentially expressed in response to IFN stimulation in the CD16 Monocyte (FCGR3A+ Monocytes) cluster. We use these ranks and the gene sets from REACTOME to find gene sets enriched in this cell population compared to all other populations using `GSEA` as implemented in decoupler.

# %%
# Upstream code cell: 36
celltype_condition = "stim_FCGR3A+ Monocytes"  # 'stimulated_B',  'stimulated_CD8 T', 'stimulated_CD14 Mono'

# %%
# Upstream code cell: 37
# extract scores
t_stats = (
    # Get dataframe of DE results for condition vs. rest
    sc.get.rank_genes_groups_df(adata, celltype_condition, key="t-test")
    # Subset to highly variable genes
    .set_index("names")
    .loc[adata.var["highly_variable"]]
    # Sort by absolute score
    .sort_values("scores", key=np.abs, ascending=False)[
        # Format for decoupler
        ["scores"]
    ]
    .rename_axis(["stim_FCGR3A+ Monocytes"], axis=1)
)
t_stats

# %% [markdown]
# ### Cluster-level gene set enrichment analysis with `decoupler`

# %% [markdown]
# Now we will use the python package [`decoupler`](https://decoupler-py.readthedocs.io/en/latest/) {cite}`badia2022decoupler` to perform GSEA enrichment tests on our data.

# %% [markdown]
# #### Retrieving gene sets

# %% [markdown]
# Download and read the `gmt` file for the REACTOME pathways annotated in the C2 collection of MSigDB.

# %%
# Upstream code cell: 42
# Downloading reactome pathways
from pathlib import Path

if not Path("c2.cp.reactome.v7.5.1.symbols.gmt").is_file():
    !wget -O 'c2.cp.reactome.v7.5.1.symbols.gmt' https://figshare.com/ndownloader/files/35233771

# %%
# Upstream code cell: 43
def gmt_to_decoupler(pth: Path) -> pd.DataFrame:
    """Parse a gmt file to a decoupler pathway dataframe."""
    from itertools import chain, repeat

    pathways = {}

    with Path(pth).open("r") as f:
        for line in f:
            name, _, *genes = line.strip().split("\t")
            pathways[name] = genes

    return pd.DataFrame.from_records(
        chain.from_iterable(zip(repeat(k), v) for k, v in pathways.items()),
        columns=["geneset", "genesymbol"],
    )

# %%
# Upstream code cell: 44
reactome = gmt_to_decoupler("c2.cp.reactome.v7.5.1.symbols.gmt")

# %% [markdown]
# Alternatively, we could just query for these resources from omnipath.
# 
# However, for stability of this tutorial we are using a fixed version of the gene set collection.
# 
# ```python
# # Retrieving via python
# msigdb = decoupler.get_resource("MSigDB")
# 
# # Get reactome pathways
# reactome = msigdb.query("collection == 'reactome_pathways'")
# # Filter duplicates
# reactome = reactome[~reactome.duplicated(("geneset", "genesymbol"))]
# ```

# %%
# Upstream code cell: 46
reactome

# %% [markdown]
# #### Running GSEA

# %% [markdown]
# First we'll prepare our gene sets. By default `decoupler` will not filter gene sets by maximum size, which packages like `fgsea` do. Instead we will simply manually filter gene sets to have a minimum of 15 genes and a maximum of 500 genes.

# %%
# Upstream code cell: 49
# Filtering genesets to match behaviour of fgsea
geneset_size = reactome.groupby("geneset").size()
gsea_genesets = geneset_size.index[(geneset_size > 15) & (geneset_size < 500)]

# %% [markdown]
# We'll use the t-statistics from the t-test to rank the genes for the CD16 Monocyte phenotype upon IFN stimulation and computes p-values for each of the pathways.

# %%
# Upstream code cell: 51
scores, norm, pvals = decoupler.run_gsea(
    t_stats.T,
    reactome[reactome["geneset"].isin(gsea_genesets)],
    source="geneset",
    target="genesymbol",
)

gsea_results = (
    pd.concat({"score": scores.T, "norm": norm.T, "pval": pvals.T}, axis=1)
    .droplevel(level=1, axis=1)
    .sort_values("pval")
)

# %% [markdown]
# We make a bar plot of top 20 pathways significantly enriched in stimulated CD16 Monocytes compared to all other cell types.

# %%
# Upstream code cell: 53
(
    so.Plot(
        data=(
            gsea_results.head(20).assign(
                **{"-log10(pval)": lambda x: -np.log10(x["pval"])}
            )
        ),
        x="-log10(pval)",
        y="source",
    ).add(so.Bar())
)

# %% [markdown]
# In the plot above, pathway names are given in the y-axis. The x-axis describes the $-\log_{10}$adjusted p-values. Therefore, the longer the height of the bar, the more significant the pathway is. Pathways are ordered by significance. The majority of interferon-related pathways are indeed ranked among the top 20 most significantly enriched pathways. Some IFN-related pathways include, REACTOME_INTERFERON_SIGNALING (ranked 2nd), REACTOME_INTERFERON_GAMMA_SIGNALING (ranked 3rd), and REACTOME_INTERFERON_ALPHA_BETA_SIGNALING (ranked 4th). Overall, `GSEA` did a decent job in identifying the pathways known to be associated with interferon signalling, given that we know a priori that IFN-related pathways should be the top-ranked terms.

# %% [markdown]
# Let's look at the raw output of `decoupler.run_gsea`:

# %%
# Upstream code cell: 56
gsea_results.head(10)

# %% [markdown]
# In above, `pval` is the p-value for the enrichment test, while `score` and `norm` are enrichment scores and normalized enrichment scores respectively. Note that enrichment scores are signed. Therefore, a negative score suggests the pathway is down-regulated and a positive score is indicative of up-regulation of genes in the pathway or gene set.

# %% [markdown]
# ### Cell-level pathway activity scoring using AUCell

# %% [markdown]
# Unlike the previous approach where we assessed gene set *enrichment* per *cluster* (or rather cell type), one can *score* the activity level of pathways and gene sets in each individual cell, that is based on absolute gene expression in the cell, regardless of expression of genes in the other cells. This we can achieve by activity scoring tools such as `AUCell`.
# 
# Similar to `GSEA`, we will be using the `decoupler` implementation of `AUCell`.

# %%
# Upstream code cell: 60
%%time
decoupler.run_aucell(
    adata,
    reactome,
    source="geneset",
    target="genesymbol",
    use_raw=False,
)

# %%
# Upstream code cell: 61
adata

# %% [markdown]
# We now add the scores for the interferon-related REACTOME pathways to the `obs` field of the `AnnData` object and annotate the activity level of these pathways in each of the cells on the UMAP:

# %%
# Upstream code cell: 63
ifn_pathways = [
    "REACTOME_INTERFERON_SIGNALING",
    "REACTOME_INTERFERON_ALPHA_BETA_SIGNALING",
    "REACTOME_INTERFERON_GAMMA_SIGNALING",
]

adata.obs[ifn_pathways] = adata.obsm["aucell_estimate"][ifn_pathways]

# %% [markdown]
# Plot the scores on the umap

# %%
# Upstream code cell: 65
sc.pl.umap(
    adata,
    color=["condition", "cell_type"] + ifn_pathways,
    frameon=False,
    ncols=2,
    wspace=0.3,
)

# %% [markdown]
# `AUCell` scores the pathways well-known to be implicated in interferon signalling high in IFN-stimulated cells, while cells in the control condition generally have low scores for these pathways, demonstrating that gene set scoring with `AUCell` has been successful. Also note that the scores are generally larger for terms that are ranked higher in the gene set enrichment test results by `GSEA`. The concordance between pathway activity scores by `AUCell` and gene set enrichment test by `GSEA` is promising, given that we know a priori that IFN-related pathways should be the top-ranked terms. In addition, the effect of IFN stimulation is very large in this dataset and this contributes to the performance of the methods here.

# %% [markdown]
# ### Gene set enrichment for complex experimental designs using limma-fry and pseudo-bulks

# %% [markdown]
# In cluster-level t-test approach, differentially expressed genes are found by comparing a cluster to all other clusters, which in this case includes both control and stimulated cells. Linear models allow us to compare cells in the stimulated condition only to those in the control group, resulting in more accurate identification of genes responding to the stimulus. Indeed, linear models can accommodate for complex experimental designs, for example, identification of gene sets enriched in `Cell type A in treatment 1` compared to `Cell type A in treatment 2`; that is, across perturbation and across cell types effects, while adjusting for batch effects, between-individual variations, gender and strain differences in mouse models etc.

# %% [markdown]
# In the next section, we demonstrate a limma-fry workflow that generalize to realistic data analysis routines, say, for single-cell case control studies. We first create pseudo-bulk replicates per cell type and condition (3 replicates per condition - cell type combination). We then find gene sets enriched in stimulated compared to control cells in a cell type. We also assess gene set enrichment between two stimulated cell type populations to find differences in signalling pathways.

# %% [markdown]
# #### Create pseudo-bulk samples and explore the data

# %%
# Upstream code cell: 71
def subsampled_summation(
    adata: ad.AnnData,
    groupby: str | list[str],
    *,
    n_samples_per_group: int,
    n_cells: int,
    random_state: None | int | np.random.RandomState = None,
    layer: str = None,
) -> ad.AnnData:
    """Sum sample of X per condition.

    Drops conditions which don't have enough samples.

    Parameters
    ----------
    adata
        AnnData to sum expression of
    groupby
        Keys in obs to groupby
    n_samples_per_group
        Number of samples to take per group
    n_cells
        Number of cells to take per sample
    random_state
        Random state to use when sampling cells
    layer
        Which layer of adata to use

    Returns:
    -------
    AnnData with same var as original, obs with columns from groupby, and X.
    """
    from scipy import sparse
    from sklearn.utils import check_random_state

    # Checks
    if isinstance(groupby, str):
        groupby = [groupby]
    random_state = check_random_state(random_state)

    indices = []
    labels = []

    grouped = adata.obs.groupby(groupby)
    for k, inds in grouped.indices.items():
        # Check size of group
        if len(inds) < (n_cells * n_samples_per_group):
            continue

        # Sample from group
        condition_inds = random_state.choice(
            inds, n_cells * n_samples_per_group, replace=False
        )
        for i, sample_condition_inds in enumerate(np.split(condition_inds, 3)):
            if isinstance(k, tuple):
                labels.append((*k, i))
            else:  # only grouping by one variable
                labels.append((k, i))
            indices.append(sample_condition_inds)

    # obs of output AnnData
    new_obs = pd.DataFrame.from_records(
        labels,
        columns=[*groupby, "sample"],
        index=["-".join(map(str, l)) for l in labels],
    )
    n_out = len(labels)

    # Make indicator matrix
    indptr = np.arange(0, (n_out + 1) * n_cells, n_cells)
    indicator = sparse.csr_matrix(
        (
            np.ones(n_out * n_cells, dtype=bool),
            np.concatenate(indices),
            indptr,
        ),
        shape=(len(labels), adata.n_obs),
    )

    return ad.AnnData(
        X=indicator @ sc.get._get_obs_rep(adata, layer=layer),
        obs=new_obs,
        var=adata.var.copy(),
    )

# %%
# Upstream code cell: 72
pb_data = subsampled_summation(
    adata, ["cell_type", "condition"], n_cells=75, n_samples_per_group=3, layer="counts"
)
pb_data

# %%
# Upstream code cell: 73
# Does PC1 captures a meaningful biological or technical fact?
pb_data.obs["lib_size"] = pb_data.X.sum(1)

# %% [markdown]
# Let's normalize this data and take a quick look at it. We won't use a neighbor embedding here since the sample size is significantly reduced.

# %%
# Upstream code cell: 75
pb_data.layers["counts"] = pb_data.X.copy()

# %%
# Upstream code cell: 76
sc.pp.normalize_total(pb_data)
sc.pp.log1p(pb_data)
sc.pp.pca(pb_data)

# %%
# Upstream code cell: 77
sc.pl.pca(pb_data, color=["cell_type", "condition", "lib_size"], ncols=1, size=250)

# %% [markdown]
# PC1 now captures difference between lymphoid (T, NK, B) and myeloid (Mono, DC) populations, while the second PC captures variation due to administration of stimulus (i.e. difference between control and stimulated pseudo-replicates). Ideally, the variation of interest has to be detectable in top few PCs of the pseudo-bulk data. 
# 
# In this case, since we are indeed interested in stimulation effect per cell type, we proceed to gene set testing. We re-iterate that the purpose of plotting PCs is to explore various axes of variability in the data and to spot unwanted variabilities that can substantially influence the test results. Users may proceed with the rest of the analyses should they be satisfied with the variations in their data.

# %% [markdown]
# #### Setup for `limma` and `fry`
# 
# For this next part of the analysis we will be using Bioconductor packages `limma` and it's method `fry`.
# 
# We first set up the design and contrast matrices. Let's remind ourselves that a design matrix is a mathematical representation of group membership (i.e. the group or condition to which a sample belongs), and contrast matrices are mathematical representations of comparisons of interest for the differential test.

# %%
# Upstream code cell: 80
groups = pb_data.obs.condition.astype("string") + "_" + pb_data.obs.cell_type

# %%
# Upstream code cell: 81
%%R -i groups
group <-  as.factor(gsub(" |\\+","_", groups))
design <- model.matrix(~ 0 + group)
head(design)

# %%
# Upstream code cell: 82
%%R
colnames(design)

# %%
# Upstream code cell: 83
%%R 
kang_pbmc_con <- limma::makeContrasts(
    
    # the effect if stimulus in CD16 Monocyte cells
    groupstim_FCGR3A__Monocytes - groupctrl_FCGR3A__Monocytes,
    
    # the effect of stimulus in CD16 Monocytes compared to CD8 T Cells
    (groupstim_FCGR3A__Monocytes - groupctrl_FCGR3A__Monocytes) - (groupstim_CD8_T_cells - groupctrl_CD8_T_cells), 
    levels = design
)

# %% [markdown]
# Index the genes annotated in each pathway in our data as follows:

# %%
# Upstream code cell: 85
log_norm_X = pb_data.to_df().T

# %%
# Upstream code cell: 86
%%R -i log_norm_X -i reactome
# Move pathway info from python to R
pathways = split(reactome$genesymbol, reactome$geneset)
# Map gene names to indices
idx = limma::ids2indices(pathways, rownames(log_norm_X))

# %% [markdown]
# As done in the `gsea` method, let's remove gene sets with less than 15 genes

# %%
# Upstream code cell: 88
%%R
keep_gs <- lapply(idx, FUN=function(x) length(x) >= 15)
idx <- idx[unlist(keep_gs)]

# %% [markdown]
# Now that we have set up the design and contrast matrices, and have indexed the genes in each pathway in our data, we can call `fry()` to test for enriched pathways in each of the contrasts we set above:

# %% [markdown]
# #### fry test for Stimulated vs Control

# %%
# Upstream code cell: 91
%%R -o fry_results
fry_results <- limma::fry(log_norm_X, index = idx, design = design, contrast = kang_pbmc_con[,1])

# %% [markdown]
# Taking a look at the top ranked pathways we'll see some familiar names:

# %%
# Upstream code cell: 93
fry_results.head()

# %%
# Upstream code cell: 94
(
    so.Plot(
        data=(
            fry_results.head(20)
            .assign(**{"-log10(FDR)": lambda x: -np.log10(x["FDR"])})
            .rename_axis(index="Pathway")
        ),
        x="-log10(FDR)",
        y="Pathway",
    ).add(so.Bar())
)

# %% [markdown]
# #### fry test for the comparison between two stimulated cell types

# %%
# Upstream code cell: 96
%%R -o fry_results_negative_ctrl
fry_results_negative_ctrl <- limma::fry(log_norm_X, index = idx, design = design, contrast = kang_pbmc_con[,2])

# %%
# Upstream code cell: 97
(
    so.Plot(
        data=(
            fry_results_negative_ctrl.head(20)
            .assign(**{"-log10(FDR)": lambda x: -np.log10(x["FDR"])})
            .rename_axis(index="Pathway")
        ),
        x="-log10(FDR)",
        y="Pathway",
    ).add(so.Bar())
)

# %% [markdown]
# As demonstrated above, limma-fry can accommodate gene set enrichment tests for datasets and research problems with complex experimental designs. Both `gsea` and `fry` provide insights into the direction of enrichment (positive or negative score in `gsea` and Direction field in `fry`). They both can be applied to clusters of cells or pseudo-bulk samples. However,  Unlike `gsea`, more flexible tests can be carried out with `fry`. In addition, `fry` can reveal if genes in a pathway are changing between the experimental conditions but in consistent or inconsistent directions. Pathways in which the genes change in consistent direction are identified with `FDR` < 0.05. Pathways in which the genes are DE between the conditions but they change in different, inconsistent directions can be identified where `FDR` > 0.05, but `FDR.Mixed` < 0.05 (assuming 0.05 is the desired significance level). `fry` is bidirectional, applicable to arbitrary designs and works well with small number of samples (although this may not be an issue in single cell). Therefore, the results by `fry` might be of more interest biologically.

# %% [markdown]
# ##### On the effect of  filtering low-expression genes
# 
# As mentioned before, Ideally, the variation of interest has to be detectable in top few PCs of the pseudo-bulk data. 
# Let's remove genes with low expression in the data, apply $\log_2$CPM transformation and repeat the PCA plots:

# %%
# Upstream code cell: 100
counts_df = pb_data.to_df(layer="counts").T

# %%
# Upstream code cell: 101
%%R -i counts_df
keep <- edgeR::filterByExpr(counts_df) # in real analysis, supply the desig matrix to the function to retain as more genes as possible
counts_df <- counts_df[keep,]
logCPM <- edgeR::cpm(counts_df, log=TRUE, prior.count = 2)

# %%
# Upstream code cell: 102
%%R -o logCPM
logCPM = data.frame(logCPM)

# %%
# Upstream code cell: 103
pb_data.uns["logCPM_FLE"] = logCPM.T  # FLE for filter low exprs

# %%
# Upstream code cell: 104
pb_data.obsm["logCPM_FLE_pca"] = sc.pp.pca(logCPM.T.to_numpy(), return_info=False)

# %%
# Upstream code cell: 105
sc.pl.embedding(pb_data, "logCPM_FLE_pca", color=pb_data.obs, ncols=1, size=250)

# %% [markdown]
# Here, "logCPM_FLE" denotes filtering for low expressed genes followed by $\log_2$CPM transformation. We can now clearly observe that PC1 captures cell type effect and PC2 captures the treatment effect, when low-expressed genes are removed and differences between library sizes are adjusted by $\log_2$CPM transformation.

# %% [markdown]
# Since in this case study we are indeed interested in stimulation effect per cell type, and this variation is better preserved before gene filtering, we presented the enrichment test results on unfiltered data. 
# In practice, filtering low abundance genes and computation of normalisation factors by `edgeR::calcNormFactors` are standard part of bulk RNA-seq analysis workflow. Should we have been interested in global effects of IFN stimulation, we should have used the filtered data. Additionally, one can note that `design <- model.matrix(~ 0 + lineage + group)` would take into account differences (that is baseline expression differences) between myeloid and lymphoid lineages, improving the separation of pseudo-bulk samples by IFN stimulation, possibly along PC1.  In this case study, we were interested in cell type-specific effects, hence we stayed with a model of data whereby the variability along PC1 is by cell type. The choice of design matrix has to be carefully considered to align with the biological question of interest.

# %% [markdown]
# ##### A note on the redundancy between gene sets and the performance of preranked and fry gene set tests

# %% [markdown]
# Generally, there can be a large overlap between closely related gene sets. This overlap impacts the rank of the gene sets in the enrichment results and can compromise the final interpretation. For example, the cells in Kang et al. are treated with IFN-$\beta$. Therefore, one would expect to see the term REACTOME_INTERFERON_ALPHA_BETA_SIGNALING as the top ranked term. While this term is indeed the top rank term in the output of `fry`, in the output of `GSEA`  REACTOME_INTERFERON_SIGNALING is the top rank term. This term has a larger number of genes (52) compared to REACTOME_INTERFERON_ALPHA_BETA_SIGNALING (24 genes), and most of those genes are shared between the two terms. This illustrates another difference between preranked gene set tests such as `GSEA` and `fry`, in preventing the larger gene sets from dominating the enrichment results. The better performance of `fry` is due to more accurate estimation of gene expression variances, hence more sensitive DE gene results.

# %% [markdown]
# ## Quiz

# %%
# Upstream code cell: 111
%run ../src/lib.py

flip_card(
    "q1",
    "What is the difference between gene set enrichment tests and activity scoring?",
    "Gene set enrichment tests focus on identifying gene sets that are overrepresented among differentially expressed genes. Activity scoring assesses the activity level of a pathway within individual samples by summarizing the expression of genes in a set, providing a continuous score that reflects pathway activity.",
    back_font_size=12,
)
flip_card(
    "q2",
    "Describe examples of settings where gene set tests should be used. Can you outline examples of settings where pathway activity scoring methods are applicable?",
    "Gene Set Tests are aplicable when comparing groups of samples to identify pathways differentially expressed between conditions, such as treated versus untreated groups. Pathway Activity Scoring Methods are useful for single-sample analyses to determine pathway activity levels within individual samples, aiding in personalized medicine or when sample sizes are limited.",
    back_font_size=10,
)
flip_card(
    "q3",
    "What are the two types of Null Hypothesis in gene set enrichment tests? Explain the difference between the two types.",
    "Competitive Null Hypothesis: Posits that genes within the set are not more associated with the phenotype than those outside the set. The test compares the association of genes inside the set to those outside. Self-contained Null Hypothesis: Asserts that no genes in the set are associated with the phenotype. The test evaluates the gene set independently, without considering genes outside the set.",
    back_font_size=10,
)
flip_card(
    "q4",
    "What is the most important preprocessing step in pathway analysis? What are the consequences if it is not conducted properly?",
    "Proper normalization of gene expression data is crucial. Inadequate normalization can lead to misleading results, as technical variations may be mistaken for biological differences, affecting the accuracy of pathway analysis.",
    back_font_size=12,
)
flip_card(
    "q5",
    "Name one gene set testing and one gene set activity scoring algorithm and explain it briefly.",
    "Gene Set Enrichment Analysis (GSEA) evaluates whether predefined gene sets show statistically significant, concordant differences between two biological states. Single-sample GSEA (ssGSEA) computes separate enrichment scores for each pairing of a sample and gene set, transforming gene expression data into pathway activity profiles for individual samples.",
    back_font_size=12,
)

# %% [markdown]
# ## Session info

# %%
# Upstream code cell: 113
%%R
sessionInfo()

# %%
# Upstream code cell: 114
session_info.show()

# %% [markdown]
# ## References

# %% [markdown]
# ```{bibliography}
# :filter: docname in docnames
# :labelprefix: gspa
# ```

# %% [markdown]
# ## Contributors
# 
# We gratefully acknowledge the contributions of:
# 
# ### Authors
# 
# * Lukas Heumos
# * Anastasia Litinetskaya
# * Soroor Hediyeh-Zadeh
# 
# ### Reviewers
