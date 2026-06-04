---
type: scbp-chapter-source
title: "Gene regulatory networks"
upstream_path: jupyter-book/mechanisms/gene_regulatory_networks.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Gene regulatory networks

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
# Gene regulatory networks

<!-- markdown cell 2 -->
## Motivation

Once single-cell genomics data has been processed, one can dissect important relationships between observed features in their genome context. In our genome, the activation of genes is controlled in the nucleus by the RNA transcriptional machinery, which activates local (promoters) or distal cis-regulatory elements (enhancers), to control the amount of RNA produced by every gene.

Conceptually, a Gene Regulatory Network (GRN) refers to a graph representation of how certain genes that control transcription i.e. "**Transcription Factors**" (TF) are in charge of directly controlling the transcription rates of their target genes (cis-regulation). At the same time, such target genes once activated, can be in charge of controlling other downstream target genes (trans-regulation). Computationally, methods that infer GRNs consider the co-variation of gene and chromatin accessibility features to identify modules that could be grouped and associated simultaneously with a few TFs. A group of genes controlled by the activity of the same TF is defined as a **regulon**.

In addition to co-variation, several methods have recognized the gathering and injection of prior knowledge data, such as the locations where a TF bind in the genome, or previously reported TF-target gene associations, to pre-define gene-gene edges that guide the inference of GRNs that are most-supported by that type of evidence. To date, benchmarking of GRNs differs from other machine learning tasks such as image inference, in such a way that labeled data is sparse and hard to validate. For this reason, several methods have developed their own benchmark that compares new methods against others, using majorly real data. The generalization of GRN inference methods is an active discussion topic in regulatory genomics, and differently from previous chapters, requires a gold standard that is at the moment difficult to agree on and be reused consistently by the community.

The purpose of this chapter is to showcase the general pipeline of how a GRN can be generated, using methods that have been to our knowledge presented in a way that allows a validation with a low amount of software dependencies. Due to the benchmarking limitations of GRN tools in general, we recommend these tools but we cannot say that they will perform best in all possible scenarios. We would rather recommend those as a starting point, given available data, to then explore their generated GRN representations with the lowest computational effort.

(mechanisms-gene-regulatory-networks-key-takeaway-2)=
### Gathering TF regulons from public data

TF- Regulons have been annotated in academic studies, databases that compiled those, and also consortia efforts such as ENCODE. As general recommendations, one can inspect [TTRUST](https://www.grnpedia.org/trrust/) {cite}`grn:Han2015-yb`, [DoRothEA](https://saezlab.github.io/dorothea/) {cite}`grn:Garcia-Alonso2019-ly`, [KnockTF](http://www.licpathway.net/KnockTFv2/index.php) {cite}`grn:Feng2020-nl`, among others, for eukaryotic TF-regulons. For prokaryotes [RegulonDB](https://regulondb.ccg.unam.mx/) {cite}`grn:Santos-Zavaleta2018-be` is a known and recognized database.

### Limitations of TF regulons

The source and confidence of a TF-regulon have some limitations, such as data source and experimental readout. If the data source for a regulon is not matched to the cell type of interest, then results can not be put into the context of the particular biological system. Alternatively, if the experimental readout is not measuring *cis* regulation events, directly provoked by the TF of interest, our TF-regulon might contain *trans* regulation events. The usage of a TF regulon gathered in an equivalent biological system is strongly recommended. However, if those are not available the interpretation of results might be biased due to the forcing of priors.

(mechanisms-gene-regulatory-networks-key-takeaway-1)=
### Generation of GRNs using RNA data

We will explore scRNA-seq data and predicted TF-regulons, using the tool SCENIC. Specifically, we will execute SCENIC {cite}`grn:Aibar2017-tp` on a donor of the NeurIPS 2021 dataset, and we will interpret the results. The main processing steps described in this notebook are adapted based on SCENIC's core tutorials [Tutorial](https://github.com/aertslab/SCENICprotocol/blob/master/notebooks/PBMC10k_SCENIC-protocol-CLI.ipynb)

### Outcome of the analysis

This notebook allows interpreting single-cell RNA-seq data through the inference of a gene regulatory network, to get potential associations between Transcription Factors and target genes that explain gene expression, in contexts such as cell differentiation, transitions, and perturbations.

<!-- markdown cell 3 -->
## Dataset description
 Cell-type clusters of 100,000 human PBMCs and the NeurIPS dataset, which contain healthy donors as well as COVID-19 patients{cite}`grn:Schulte-Schrepping2020`.

<!-- markdown cell 4 -->
## Environment setup

## Code cell 5

```python
import warnings

warnings.filterwarnings("ignore")


from pathlib import Path

import loompy as lp
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scanpy as sc
import seaborn as sns
```

<!-- markdown cell 6 -->
## Preparation of the NeurIPS dataset
The current dataset we will be looking at here is already pre-processed (previous chapters) and it contains 69,249 cells, annotated into 22 cell types. Due to batch integration considerations, we will demonstrate the usage of GRN methods for only one, labeled as s1d1 (n=6,224 cells).

<!-- markdown cell 7 -->
Load the full dataset

## Code cell 8

```python
adata = sc.read_h5ad("../../data/openproblems_bmmc_multiome_genes_filtered.h5ad")
adata.shape
```

<!-- markdown cell 9 -->
Subset RNA only features using the label GEX

## Code cell 10

```python
rna = adata[:, adata.var.feature_types == "GEX"]
del adata
sc.pp.log1p(rna)
rna.obs.batch.value_counts()
```

## Code cell 11

```python
rna.shape
```

<!-- markdown cell 12 -->
Here we select highly-variable genes, to minimize the computing requirements for steps down-stream. An execution without defining HVGs is also possible, but will need additional computing memory and time.

## Code cell 13

```python
sc.pp.highly_variable_genes(rna, batch_key="batch", flavor="seurat")
```

## Code cell 14

```python
sc.set_figure_params(facecolor="white")
```

<!-- markdown cell 15 -->
This is the embedding of all gene expression data cells of all donors. One can see that donor is dominant over cell types in terms of groups, and batch-correction methods have not been executed.

## Code cell 16

```python
sc.pl.embedding(rna, "GEX_X_umap", color=["cell_type", "batch"])
```

<!-- markdown cell 17 -->
Here we observe the cells of only donor s1d1. When observing cells for only one donor, cells clusters can be identified based on their provided annotations.

## Code cell 18

```python
adata_batch = rna[rna.obs.batch == "s1d1", :]
sc.pl.embedding(adata_batch, "GEX_X_umap", color=["cell_type", "batch"])
```

<!-- markdown cell 19 -->
## Preparation of SCENIC

<!-- markdown cell 20 -->
Using loompy, we will convert the gene expression values into loom files. This file format is required by pyscenic as input. In addition to this, the file `allTFs_hg38.txt` defines a list of gene symbols related to transcription factors, to be considered when weighting associations between those and other genes.

## Code cell 21

```python
## this file has to be downloaded if not found
!wget -nc https://raw.githubusercontent.com/aertslab/SCENICprotocol/master/example/allTFs_hg38.txt
```

## Code cell 22

```python
tfs_path = "allTFs_hg38.txt"
```

## Code cell 23

```python
loom_path = "data/neurips_processed_input.loom"
loom_path_output = "data/neurips_processed_output.loom"
tfs = [tf.strip() for tf in open(tfs_path)]
```

<!-- markdown cell 24 -->
As a verification, it is recommended to check that genes annotated as TFs are part of the provided input data. If not a high coverage of gene symbols is observed e.g. 50% or more, there could be an issue with the feature names declared in the `.var`, such as Ensembl IDs instead of gene_symbols, or lower/uppercase difference if the genome assembly is mouse or another species that uses a different capitalization style than human.

## Code cell 25

```python
# as a general QC. We inspect that our object has transcription factors listed in our main annotations.
print(
    f"%{np.sum(adata_batch.var.index.isin(tfs))} out of {len(tfs)} TFs are found in the object"
)
```

<!-- markdown cell 26 -->
Usage of HVG or all features can be defined here, by changing the flag `use_hvg` to `False`.

## Code cell 27

```python
use_hvg = True
if use_hvg:
    mask = (adata_batch.var["highly_variable"] is True) | adata_batch.var.index.isin(
        tfs
    )
    adata_batch = adata_batch[:, mask]
```

<!-- markdown cell 28 -->
Create a loom file for NeurIPS donor. If you get an error in this step, verify that the labels for Gene/CellID/etc. are properly defined.

## Code cell 29

```python
row_attributes = {
    "Gene": np.array(adata_batch.var.index),
}
col_attributes = {
    "CellID": np.array(adata_batch.obs.index),
    "nGene": np.array(np.sum(adata_batch.X.transpose() > 0, axis=0)).flatten(),
    "nUMI": np.array(np.sum(adata_batch.X.transpose(), axis=0)).flatten(),
}

lp.create(loom_path, adata_batch.X.transpose(), row_attributes, col_attributes)
```

<!-- markdown cell 30 -->
Once the loom file has been generated, we execute `pyscenic` to generate associations between TFs and genes. TF-gene associations are inferred by GRNBoost, and summarized by a directional weight between TFs and target genes. The output of this analysis is a table summarizing all reported associations with their importance weight.

<!-- markdown cell 31 -->
Some steps below require indicating a number of cores (`num_workers`). Increase according to computing resources available

## Code cell 32

```python
num_workers = 3
```

## Code cell 33

```python
outpath_adj = "adj.csv"
if not Path(outpath_adj).exists():
    !pyscenic grn {loom_path} {tfs_path} -o $outpath_adj --num_workers {num_workers}
```

<!-- markdown cell 34 -->
Show the top of TF-target associations

## Code cell 35

```python
results_adjacencies = pd.read_csv("adj.csv", index_col=False, sep=",")
print(f"Number of associations: {results_adjacencies.shape[0]}")
results_adjacencies.head()
```

<!-- markdown cell 36 -->
Visualize the distribution of weights for general inspection of the quantiles and thresholds obtained from pyscenic. As provided by the pyscenic grn step, the importance scores follow a unimodal distribution, with negative/positive values indicating TF-gene associations with less/more importance, respectively. From the right-tail of this distribution, we can recover the most relevant interactions between TFs and potential target genes, supported by gene expression values and the analysis done by pyscenic.

## Code cell 37

```python
plt.hist(np.log10(results_adjacencies["importance"]), bins=50)
plt.xlim([-10, 10])
```

<!-- markdown cell 38 -->
As targets genes have DNA motifs at promoters (sequence specific DNA motifs), those can be used to link TFs to target genes. Next, we use an annotation of TF associations to Transcription Start Sites (TSSs) to refine this annotation.

<!-- markdown cell 39 -->
Download TSS annotations precalculated by Aerts's lab

## Code cell 40

```bash
!wget -nc https://resources.aertslab.org/cistarget/databases/homo_sapiens/hg38/refseq_r80/mc9nr/gene_based/hg38__refseq-r80__10kb_up_and_down_tss.mc9nr.genes_vs_motifs.rankings.feather
```

## Code cell 41

```python
# ranking databases
db_glob = "*feather"
db_names = " ".join(map(str, Path().glob(db_glob)))
```

<!-- markdown cell 42 -->
Download a catalog of motif-to-TF associations

## Code cell 43

```bash
!wget -nc https://resources.aertslab.org/cistarget/motif2tf/motifs-v9-nr.hgnc-m0.001-o0.0.tbl
```

## Code cell 44

```python
# motif databases
motif_path = "motifs-v9-nr.hgnc-m0.001-o0.0.tbl"
```

<!-- markdown cell 45 -->
Using the catalog of motif and their gene associations at promoters, retrieved a subset adjacencies by pruning of the previous adjacencies.
This step can take several minutes on consumer grade hardware.

## Code cell 46

```python
if not Path("reg.csv").exists():
    !pyscenic ctx adj.csv \
        {db_names} \
        --annotations_fname {motif_path} \
        --expression_mtx_fname {loom_path} \
        --output reg.csv \
        --mask_dropouts \
        --num_workers {num_workers} > pyscenic_ctx_stdout.txt
```

<!-- markdown cell 47 -->
To explore the candidates reported, it is recommended as a rule of thumb to explore the output by the ranking of relative contribution, or by top-quantile thresholds defined visually to obtain a high signal-to-noise ratio.

<!-- markdown cell 48 -->
Define custom quantiles for further exploration

## Code cell 49

```python
import numpy as np

n_genes_detected_per_cell = np.sum(adata_batch.X > 0, axis=1)
percentiles = pd.Series(n_genes_detected_per_cell.flatten().A.flatten()).quantile(
    [0.01, 0.05, 0.10, 0.50, 1]
)
print(percentiles)
```

<!-- markdown cell 50 -->
The histogram below indicates the distribution of genes detected per cell. This visualization is convenient to define the parameter `--auc_threshold` in the next step. Specifically, the default parameter of `--auc_threshold` is 0.05, which in this plot would result in the selection of `144` genes, to be used as a reference per cell for AUCell calculations. The modification of this parameter affects the estimation of AUC values calculated by AUCell.

## Code cell 51

```python
fig, ax = plt.subplots(1, 1, figsize=(8, 5), dpi=100)
sns.distplot(n_genes_detected_per_cell, norm_hist=False, kde=False, bins="fd")
for i, x in enumerate(percentiles):
    fig.gca().axvline(x=x, ymin=0, ymax=1, color="red")
    ax.text(
        x=x,
        y=ax.get_ylim()[1],
        s=f"{int(x)} ({percentiles.index.values[i] * 100}%)",
        color="red",
        rotation=30,
        size="x-small",
        rotation_mode="anchor",
    )
ax.set_xlabel("# of genes")
ax.set_ylabel("# of cells")
fig.tight_layout()
```

<!-- markdown cell 52 -->
This step will use TFs to calculate Area Under the Curve scores, that summarize how well the gene expression observed in each cell can be associated by the regulation of target genes regulated by the mentioned TFs.

<!-- markdown cell 53 -->
Using the above-generated matrix of cell x TFs and those scores, we can calculate a new embedding using only those.

## Code cell 54

```python
if not Path(loom_path_output).exists():
    !pyscenic aucell $loom_path \
        reg.csv \
        --output {loom_path_output} \
        --num_workers {num_workers} > pyscenic_aucell_stdout.txt
```

## Code cell 55

```python
# collect SCENIC AUCell output
lf = lp.connect(loom_path_output, mode="r+", validate=False)
auc_mtx = pd.DataFrame(lf.ca.RegulonsAUC, index=lf.ca.CellID)
lf.close()
```

## Code cell 56

```python
import anndata as ad

ad_auc_mtx = ad.AnnData(auc_mtx)
sc.pp.neighbors(ad_auc_mtx, n_neighbors=10, metric="correlation")
sc.tl.umap(ad_auc_mtx)
sc.tl.tsne(ad_auc_mtx)
```

<!-- markdown cell 57 -->
Visualize the data base on the TF-regulons and auc_mtx generated.

## Code cell 58

```python
adata_batch.obsm["X_umap_aucell"] = ad_auc_mtx.obsm["X_umap"]
adata_batch.obsm["X_tsne_aucell"] = ad_auc_mtx.obsm["X_tsne"]
```

<!-- markdown cell 59 -->
This UMAP visualization confirms that the signal from SCENIC is capable of capturing regulons that keep dividing most cell populations into sub-groups. Hence, there is information TF-regulons that enables cell-type identification.

## Code cell 60

```python
sc.pl.embedding(adata_batch, basis="X_umap_aucell", color="cell_type")
```

<!-- markdown cell 61 -->
A visualization of the tSNE values generated by SCENIC also confirms this cell-type separation, for the majority of cell-types

## Code cell 62

```python
sc.pl.embedding(adata_batch, basis="X_tsne_aucell", color="cell_type")
```

<!-- markdown cell 63 -->
### **Interpretation of results**

## Code cell 64

```python
import seaborn as sns
```

## Code cell 65

```python
auc_mtx["cell_type"] = adata_batch.obs["cell_type"]
mean_auc_by_cell_type = auc_mtx.groupby("cell_type").mean()
```

<!-- markdown cell 66 -->
show the top N TF regulons by a color

## Code cell 67

```python
top_n = 50
top_tfs = mean_auc_by_cell_type.max(axis=0).sort_values(ascending=False).head(top_n)
mean_auc_by_cell_type_top_n = mean_auc_by_cell_type[
    [c for c in mean_auc_by_cell_type.columns if c in top_tfs]
]
```

<!-- markdown cell 68 -->
Once we know the top TF-regulons involved in the biological system we are studying, we can inspect the activities estimated by each TF, based on the scores per cell, or the overall AUCs per cell-type explained by those TF (blue heatmap below).

## Code cell 69

```python
sns.clustermap(
    mean_auc_by_cell_type_top_n,
    figsize=[15, 6.5],
    cmap="Blues",
    xticklabels=True,
    yticklabels=True,
)
```

<!-- markdown cell 70 -->
As the red heatmap is suggesting that some TFs are strongly associated to particular cell types, we can verify their expression levels as an additional validation. This is done by matching the TF names we want to highlight, and visualize those using Scanpy's (red heatmap).

## Code cell 71

```python
tf_names = top_tfs.index.str.replace(r"\(\+\)", "")
adata_batch_top_tfs = adata_batch[:, adata_batch.var_names.isin(tf_names)]
```

## Code cell 72

```python
sc.pl.matrixplot(
    adata_batch,
    tf_names,
    groupby="cell_type",
    cmap="Reds",
    dendrogram=True,
    figsize=[15, 5.5],
    standard_scale="group",
)
```

<!-- markdown cell 73 -->
Through visual inspection and comparison of the TF-regulon AUC scores and TF gene expression by cell type, we can verify that in several cases the cell-type specific expression of a TF is linked to a particular cell type, where the respective TF-regulon is also active e.g. RUNX2 in pDCs, TCF7L2 in CD16+ Mono, LEF1 in CD4+ T activated. Additional inspection can serve to validate previous insights and/or additional associations.

<!-- markdown cell 74 -->
## Quiz

<!-- markdown cell 75 -->
### Theory

## Code cell 76

```python
%run ../src/lib.py

flip_card(
    "q1",
    "How many genes in the human/mouse genome are considered TFs?",
    "Approximately 1,600 genes in the human genome and 1,500 in the mouse genome encode transcription factors (TFs).",
)
flip_card(
    "q2",
    "What is a TF-regulon?",
    "A TF-regulon is a collection of target genes regulated by a specific transcription factor, forming a network that controls gene expression patterns.",
)
flip_card(
    "q3",
    "How many DNA-binding motifs are there to each TFs? Currently, are there more known DNA-binding motifs or TFs that bind those? How can one reconcile the redundancy of these during the analysis?",
    "Each TF can recognize multiple DNA-binding motifs, leading to redundancy where different TFs share motifs. Since there are more known motifs than TFs, integrating gene expression, chromatin accessibility, and TF co-binding data helps accurately map TF-target interactions.",
    front_font_size=15,
    back_font_size=15,
)
flip_card(
    "q4",
    "Additional reading: Describe the futility theorem.",
    "The futility theorem suggests that unbound instances of a TF's binding motif often outnumber those occupied by the TF, indicating that motif presence alone doesn't guarantee TF binding.",
    back_font_size=15,
)
```

<!-- markdown cell 77 -->
### SCENIC

## Code cell 78

```python
%run ../src/lib.py

flip_card(
    "q1",
    "Describe the major steps in the SCENIC pipeline (three or more).",
    "Co-expression Network Inference: Identify modules of co-expressed genes from single-cell RNA-seq data. Regulon Prediction: Map these modules to candidate TFs using motif enrichment analysis to predict regulons. Cellular Activity Scoring: Assess the activity of each regulon in individual cells to determine their influence on cell states.",
    back_font_size=13,
)
flip_card(
    "q2",
    "What could happen if the number of TFs reported in your own data has a low overlap to the one externally retrieved?",
    "If the TFs identified in your data have low overlap with external datasets, it may indicate technical issues, such as batch effects or incomplete annotation, potentially leading to inaccurate network inference.",
)
flip_card(
    "q3",
    "What is the AUC score from pyscenic and how it can be helpful for interpretation of results per cell cluster?",
    "The Area Under the Curve (AUC) score from pySCENIC quantifies the activity of each regulon within a cell or cluster, aiding in identifying key TFs driving specific cellular states or transitions.",
    back_font_size=15,
)
```

<!-- markdown cell 79 -->
## References

<!-- markdown cell 80 -->
```{bibliography}
:filter: docname in docnames
:labelprefix: grn
```

<!-- markdown cell 81 -->
## Contributors
We gratefully acknowledge the contributions of:
### Authors
* Ignacio Ibarra
### Reviewers
* Lukas Heumos
* Anna Schaar
