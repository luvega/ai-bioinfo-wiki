---
type: scbp-chapter-source
title: "Quality control"
upstream_path: jupyter-book/surface_protein/quality_control.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Quality control

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
(surface-protein:motivation)=
# Quality control

<!-- markdown cell 2 -->
(surface-protein-quality-control-key-takeaway-1)=
## Motivation

<!-- markdown cell 3 -->
In addition to capturing only transcriptomic data with single cell analyses, we are now able to also capture the abundance of surface protein expression. 
The protocol used for this is usually referred to as CITE-seq{cite}`sp:Stoeckius2017`. 
This modality requires different preprocessing compared to what we described earlier for gene expression data since the data distributions are different. 
In the following, we will guide you through the process of dealing with CITE-seq data. 
As CITE-seq data provides you with two different modalities, you can either analyze them separately or jointly. 
Here, we will focus on the ADT part of the data and analyze it unimodally. For a joint analysis of ADT and RNA data, we refer to the multimodal integration chapter {ref}`multimodal-integration-paired-integration`.

<!-- markdown cell 4 -->
Single-cell RNA-seq data acts as a proxy for protein level with a partial correlation at various transcription states of a cell{cite}`Liu2016`. 
Therefore, it is in our interest to measure the protein levels in single-cells if we are to capture a better picture of cellular processes. 
Quantifying these aspects of a cell is essential to understand cell differentiation and fate, cell signal transduction pathways, disease progression, perturbations, and clinical diagnostics{cite}`Xie2022`.

We can already detect relevant populations with single-cell transcriptomics. 
This is a valuable piece of information, but incomplete if we want to better understand the cellular identities and dynamics happening in the biological processes we study. 
Having surface protein measurements allows us to close the gap between identity by transcription and identity by protein where there might be a delay in synthesis that could be important in our experiment. 
For example, it has been noted that ICOS, an immune checkpoint protein, was increased on the surface of treated cells, regardless of the fact that this protein’s {term}`mRNA <Messenger RNA (mRNA)>` does not differ in abundance between the treatment groups{cite}`Peterson2017`. 
Another advantage is that surface protein levels help us detect doublets that might not be reflected at the transcript level in our data. 
This is possible by looking at the co-occurrence of cell-type-specific markers{cite}`sp:Sun2021`, {ref}`surface-protein-doublet-detection`.

By using antibodies tagged with a nucleotide barcode, it is possible to first bind the antibodies to the cells and later sequence the barcodes together with the RNA. 
There are two main protocols: CITE-seq (Cellular Indexing of Transcriptomes and Epitopes by Sequencing) and REAP-seq (RNA expression and protein sequencing assay). 
The main difference resides in their antibody-oligo conjugates also known as Antibody-Derived Tags (ADT). 
CITE-seq uses streptavidin that is noncovalently bound to biotinylated DNA barcodes. REAP-seq implements covalent bonds between the antibody and a DNA barcode{cite}`Peterson2017`. 
Furthermore, there have been advances integrating the CITE-seq protocol in a multimodal assay. 
One is DOGMA-seq{cite}`Mimitou2021`, an adaptation of CITE-seq that allows the measurement of chromatin accessibility, gene expression, and protein from the same cell. 
This method includes ASAP-seq, which combines scATAC-seq and ADT by adding a bridge oligo specific to the CITE-seq reagents{cite}`Mimitou2021`. 
The advantage of ASAP-seq is that it can measure surface and intracellular proteins. 
We will refer to the surface protein measurements as ADT data.

![CITE-Seq](https://citeseq.files.wordpress.com/2017/10/antibody_transparent.png)

With ADT data, we can identify cell types based on conventional markers usually utilized in flow cytometry experiments. 
These markers are especially useful for specific immune cell populations. 
The advantage of ADT is that other modalities are measured simultaneously. 
However, the way we process ADT data differs from others. 
Contrary to the negative binomial distribution of UMI counts, ADT data is less sparse with a negative peak for non-specific antibody binding and a positive peak resembling enrichment of specific cell surface proteins{cite}`Zheng2022`. 
Many experiments include only a small number—typically in the tens or hundreds—of antibodies of interest.. 
Moreover, sequencing resources can be concentrated enabling deeper coverage of ADTs since they are separated from transcripts. 
ADT data can also be noisier, as unbound antibodies lead to counts in cells or empty droplets where the protein is not present.

<!-- markdown cell 5 -->
## Environment setup and data

We use a CITE-seq data set generated for a single cell data integration challenge at the NeurIPS conference 2021 {cite}`sp:Luecken_2021`. 
This dataset captures single-cell RNA and Antibody-Derived Tag (ADT) data from bone marrow mononuclear cells of 12 healthy human donors measured at four different sites to obtain nested batch effects. 
In this tutorial, we will use the whole dataset which contains 140 surface proteins.

We will use scanpy and muon{cite}`Bredikhin_2022` to analyze the data. 
We first start by importing all packages that are required for running this notebook.

## Code cell 6

```python
import warnings

import muon as mu
import numpy as np
import pandas as pd
import scanpy as sc
import seaborn as sns
from scipy.stats import median_abs_deviation

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
```

<!-- markdown cell 7 -->
### Loading the CITE-seq data

Next, we now load the CITE-seq dataset from the single cell data integration challenge at the NeurIPS conference 2021 {cite}`sp:Luecken_2021`. 
This CITE-seq dataset is organized into a MuData object. 
A MuData object of a CITE-seq dataset contains two AnnData objects of the two data modalities: an AnnData object of the RNA data and an AnnData object of the ADT (protein) data.

## Code cell 8

```python
af = ln.Artifact.connect("theislab/sc-best-practices").get(
    key="surface-protein/cite_filtered.h5mu", is_latest=True
)
mdata = af.load()
mdata
```

<!-- markdown cell 9 -->
We have 122,016 droplets. 
The RNA data contains 36601 genes (the full transcriptome) and the ADT data contains 140 surface proteins.
Here we use the filtered version of the data, that is, with all barcodes that passed the preprocessing filter with CellRanger.

<!-- markdown cell 10 -->
(surface-protein-quality-control)=
## Quality Control

<!-- markdown cell 11 -->
As in transcriptomics data quality control and filtering, we need to remove cells that failed to capture ADTs. 
Solely reusing the earlier introduced transcriptomics quality control measures is inappropriate due to the above-mentioned fundamentally different count distributions in ADT data.

We recommend to first remove cells that captured few surface proteins.
In practice, this is more robust than filtering based on total ADT counts alone. 
When targeted proteins are successfully captured, total ADT counts can increase disproportionately, driven by the near-binary expression patterns of many surface markers (i.e., largely present or absent rather than continuously varying). 
As a result, when removing cells that failed to capture ADTs, we recommend removing cells that captured few surface proteins rather than removing cells with low total ADT counts.

## Code cell 12

```python
sc.pp.calculate_qc_metrics(mdata["prot"], inplace=True, percent_top=None)
```

<!-- markdown cell 13 -->
We first look at the distribution of captured ADTs per cell over all samples. 
We plot this using the seaborn library. 
We first take a look at the whole range and can see that most cells
express between 70 and 140 proteins.

## Code cell 14

```python
sns.displot(mdata["prot"].obs.n_genes_by_counts)
```

<!-- markdown cell 15 -->
As the cells falling below a certain threshold of present ADT markers and not following the distribution are probably not viable cells, we want to filter out those cells.
Thus, we look at the lower end of the distribution:

## Code cell 16

```python
sns.displot(
    mdata["prot"][mdata["prot"].obs.n_genes_by_counts < 70].obs.n_genes_by_counts
)
```

<!-- markdown cell 17 -->
We can see a 'valley' in the distribution at around 55 ADTs. 
This looks like an appropriate cutoff.

<!-- markdown cell 18 -->
Next, we do the same thing based on total counts per cell. 
Looking at the total range, we can't see any apparent ranges of the distribution of counts.

## Code cell 19

```python
sns.displot(mdata["prot"].obs.total_counts)
```

<!-- markdown cell 20 -->
We zoom in to see the upper end of the distribution for the total counts to decide on a cutoff for the maximum number of counts as droplets exceeding a certain threshold probably either contain multiple cells, so-called doublets, or are the result of an artificial aggregate of antibodies.

## Code cell 21

```python
sns.displot(
    mdata["prot"].obs.query("total_counts>20000 and total_counts<100000").total_counts
)
```

<!-- markdown cell 22 -->
We remove cells with more than 100000 total protein counts, since from the last two plots we can say there are very few such cells and they are definitely either doublets or the result of an artificial aggregate of antibodies.

## Code cell 23

```python
sc.pp.filter_cells(mdata["prot"], max_counts=100000)
mdata.update()
mu.pp.filter_obs(mdata, mdata["prot"].obs_names)
mdata
```

<!-- markdown cell 24 -->
### Sample-wise QC

<!-- markdown cell 25 -->
Now we search for a more stringent, sample-wise cutoff of low quality cells.
We look at the distribution of counts per cell across the samples to see if there are differences. 
As the total amount of reads and droplets can differ between the samples, a stringent, hard cutoff applied to all samples would not be appropriate.

## Code cell 26

```python
sns.boxplot(y=mdata["prot"].obs.total_counts, x=mdata["prot"].obs["donor"])
```

<!-- markdown cell 27 -->
The distributions of counts are different between samples. 
Thus, sample-wise QC is deemed pertinent.
If we compare sample s3d7 versus sample s4d8, we can see that the outliers of one sample would fit the regular distribution of normal counts in the other sample.

Since we have a significant number of samples, we can do sample-wise QC automatically as described in the RNA preprocessing chapter.

## Code cell 28

```python
def is_outlier(adata, metric: str, nmads: int):
    M = adata.obs[metric]
    outlier = (M < np.median(M) - nmads * median_abs_deviation(M)) | (
        np.median(M) + nmads * median_abs_deviation(M) < M
    )
    return outlier
```

## Code cell 29

```python
outliers = []
for sample in np.unique(mdata["prot"].obs["donor"]):
    adata_temp = mdata["prot"][mdata["prot"].obs["donor"] == sample].copy()
    adata_temp.obs["outlier"] = is_outlier(
        adata_temp, "log1p_total_counts", 5
    ) | is_outlier(adata_temp, "log1p_n_genes_by_counts", 5)
    outliers.append(adata_temp.obs["outlier"])
    print(f"{sample}: outliers {adata_temp.obs.outlier.value_counts()[True]}")
```

## Code cell 30

```python
mdata["prot"].obs["outliers"] = pd.concat(outliers)
```

## Code cell 31

```python
mdata["prot"].obs.head()
```

<!-- markdown cell 32 -->
Now we actually filter out the outliers:

## Code cell 33

```python
mdata = mdata[~mdata["prot"].obs["outliers"]].copy()
mdata
```

<!-- markdown cell 34 -->
We removed around 3500 cells during the filtering which is roughly 3% of cells. 
This is a relatively permissive filtering and we might need further filtering of doublets in the following.

## Code cell 35

```python
sns.boxplot(y=mdata["prot"].obs.total_counts, x=mdata["prot"].obs["donor"])
```

<!-- markdown cell 36 -->
As we can see in the above plot, outliers are now filtered out for each sample separately. 
To now bring the values for each sample into a similar range, we need to normalize the data.

## Code cell 37

```python
af_quality_control = ln.Artifact.from_mudata(
    mdata,
    key="surface-protein/cite_quality_control.h5mu",
    description="CITE-seq filtered data after quality control",
)
af_quality_control.save()
```

## Code cell 38

```python
ln.finish()
```

<!-- markdown cell 39 -->
## References

<!-- markdown cell 40 -->
```{bibliography}
:filter: docname in docnames
:labelprefix: sp
```

<!-- markdown cell 41 -->
## Contributors

We gratefully acknowledge the contributions of:

### Authors

* Javier Marchena-Hurtado
* Daniel Strobl
* Ciro Ramírez-Suástegui
* Anna Schaar

### Reviewers

* Lukas Heumos
