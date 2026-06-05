---
type: scbp-chapter-source
title: "Immune Receptor Profiling"
upstream_path: jupyter-book/air_repertoire/ir_profiling.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Immune Receptor Profiling

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
# Immune Receptor Profiling

<!-- markdown cell 2 -->
## Role IR in cells

Immune Receptors (IR) are the key for the recognition of potential hazardous antigens and toxins invading the body. Those receptors are usually located in the membrane of specialized cells, which recognize harmful content and initiate protective mechanisms. There are different kinds of IRs specialized in the recognition of specific structures of foreign agents:

- **Pattern recognition receptors (PRRs)**: Pathogen-associated molecular patterns (PAMPS)
- **Killer activator/inhibitor receptors (KARs/KIRs)**: Host cells abnormalities
- **Complement receptors**: Complement proteins
- **Fc receptors**: Epitope-antibody complex
- **Cytokine receptors**: Cytokines
- **B-cell receptor (BCRs)**: Epitopes
- **T-cell receptors (TCRs)**: Linear epitopes bound to the Major Histocompatibility Complex (MHC)

<!-- markdown cell 3 -->
## IRs of the adaptive immune system

In the adaptive immune system, there are two major lineages of lymphocytes with IRs, which are produced in the Thymus and Bone-marrow called T- and B-cells {cite}`cooper2006evolution`. These adaptive immune receptors (AIRs) of both cell lines detect antigens derived from different pathogens and tumor cells. However, they interact with the antigens in different ways: While the B-cell receptor (BCR) directly recognizes soluble or membrane-bound epitopes, the T-cell receptor interacts with linear peptides bound to the surface protein MHC (pMHC), which enables to view inside cells by presenting its content on the cell's surface. After activation by antigens, B- and T-cells perform various functions such as fighting the pathogen, regulation of the immune response, or forming memory by proliferation.

:::{figure-md} AIR types
<img src="../_static/images/air_repertoire/AIR_types.png" alt="AIR types" class="bg-primary mb-1" width="800px">

Schematic drawing of the two AIR types. Created with BioRender.com.
:::

<!-- markdown cell 4 -->
## Formation of adaptive immune receptors by V(D)J recombination

The AIR is a protein complex consisting of two chains. Depending on the T cell type, these chains are either called α- and β- or γ- and δ-chain. Similarly, the BCR chains are called heavy and light chain (subtypes: κ and λ). While the α-, γ-, κ-, and λ-chains are formed by their respective V- and J-genes, the remaining chains additionally include their D-gene. For simplicity, we will therefore refer to VJ and VDJ chains throughout this book.

Adaptive IRs lines are highly polymorphic in order to capture the immense space of antigens, i.e., there exists an immense variety of different TCR and BCR sequences. The amount of different TCRs have been estimated at 10<sup>20</sup> in total, while a human individual harbors 10<sup>7</sup> different sequences {cite}`zarnitsyna2013estimating`. Similarly, there naturally occur up to 10<sup>18</sup> different BCRs {cite}`briney2019commonality`. The collection of all receptors forms the AIR repertoire of an individual. 

The sequence diversity is introduced by the V(D)J recombination mechanism:

- **Combinatorial diversity** is introduced by the combination of different V-, (D-,) and J-genes in addition to the combination of different VJ and VDJ chains.
- **Junctional diversity** is achieved by insertion of nucleotides at the gene interfaces.

:::{figure-md} VDJ recombination
<img src="../_static/images/air_repertoire/VDJ_recombination.png" alt="VDJ recombination" class="bg-primary mb-1" width="800px">

VDJ recombination at the example of an αβ-TCR. Created with BioRender.com.
:::

Additionally, mutations occur at the BCR binding sites in a process called Somatic Hypermutation for affinity maturation during rapid cell proliferation.

In the resulting AIRs, three regions of high variability - the Complementary Determining Regions (CDRs) 1-3 - were detected per chain, where the AIR interacts with its target. The CDR1 and CDR2 are encoded by the V-gene. However, the CDR3 spans over the intersection of V-, (D-,) and J-genes and is therefore the most diverse element of the AIR. Therefore, it is often assumed that the specificity of an AIR is determined mainly by its CDR3 region of the more diverse VDJ chain.

<!-- markdown cell 5 -->
(air-repertoire-ir-profiling-key-takeaway-1)=
## VDJ-sequencing

### Cell isolation

Before quantifying the single-cell data, the cells of interest should be targeted and isolated. Common options include:

- **Fluorescence Activated Cell Sorting (FACS)** is a method based on flow cytometry with the power to label the cells of interest based on fluorescent probes over the raw cell suspension. A cell suspension is carried by a rapidly flowing stream of liquid. This stream of cells is broken up into individual droplets through a vibrating mechanism. Just before the stream breaks into droplets, the flow passes through a fluorescence measuring station where the fluorescence signal of every cell is measured. The droplets can be further charged for further separations.

- **Magnetic-Activated Cell Sorting (MACS)** can use antibodies, enzymes, lectins, or streptavidins attached to a magnetic bead to label the target cells. Once the cells are labeled from the raw suspension, a magnetic field is applied to attract the magnetic beads and discard the remaining cells from the suspensions. The targeted cells are collected once the magnetic field is turned off. One advantage of this method is the capacity to collect targeted cells with no specific markers to be labeled, in that case, a cocktail of markers is used to label the untargeted cells, and the cells of interests are collected by washing them out once the magnetic field captures the untargeted cells conjugated to a magnetic bead.

- **Laser Capture Microdissection (LCM)** has the power to extract cell populations or single cells from microscope preparations without detriment of the surrounding tissue. The components to perform LCM includes a reverse microscope, a laser control unit, a microscope joy stick to plate stabilization, a CCD camera, and a color monitor. The idea behind LCM consists on labelling cells by visual detection of morphological characteristics of target cells, the plate is immobilized and the laser pulse melts the thin thermoplastic film removing the cells or cells of interest without any damage to the surrounding tissue.

- **Microfluidics** is a versatile method able to work with small quantities of raw suspension even at the order of nanoliters. There are different kinds of microfluidic approaches including cell-affinity chromatography based microfluidics, physical characteristics of cell based microfluidics, immunomagnetics beads based microfluidics, and separation by dielectric properties of some cell-types based microfluidics. The most used microfluidics based method is the chromatographic separation using a chip assay as stationary phase which is modified to include the necessary antibodies to capture the target cells in the mobile phase. After the buffer flows off from the chip, a solution is used to separate the cells attached to the antibodies to collect them for further analysis {cite}`hu2016single`.

### Immune receptor sequencing

A common approach to discern V(D)J chains from single-cell isolations consists of computational reconstructions of different chains' sequences based on full-length single-cell RNA sequencing, with Smart-seq2, a 5'-end RNA template based protocol, being one of the most widely implemented. Regarding computational methods, TRAPeS, TraCer, and VDJPuzzle are usually used to reconstruct TCR sequences based on scRNA-seq data, whereas BALDR {cite}`Upadhyay2018`, BASIC {cite}`canzar2016` and BraCer {cite}`Lindeman2018` were shown to robustly recover BCR sequences. However, they are prone to ignore the whole landscape of recombinatorial products and alternative splicing products in V(D)J region. Some alternatives have arisen to deal with this problem, RAGE-seq for example was developed to capture specific TCR and BCR fragments based on PCR templates designed for immune receptor sequencing and use long-read Oxford Nanopore to capture the whole sequence, whereas the rest of the cDNA is processed based on short-reads protocols provided by, for example, Illumina {cite}`singh2019high`.

<!-- markdown cell 6 -->
## AIR repertoire analysis

VDJ-sequencing provides us with the nucleotide and thereby also the protein sequence of the AIR paired for both chains, from which the V-, (D-,) J-, and C-gene is determined in addition to the CDR3 sequence. Overall, the AIR sequence determines the specificity of the individual B- and T-cell. Therefore, the information obtained by VDJ-sequencing provides us with an indicator of the cells' functionality, which is directly coupled to the AIRs target antigen. This enables us to use the AIR information in three major ways:
- **Phenotyping**: We can group immune cells by identifying cells with the same or similar AIR, which share the same specificity. Having these groups, we can now observe, how disease-specific cells react under different conditions (e.g. transcriptomic change upon stimulation), whether immune cells have proliferated, or how the diversity of an immune repertoire changes after an immune response.
- **Sequence Analysis**: Having identified groups of AIRs (e.g. a reactive cluster detected in other modalities), we can extract properties of their sequence, such as V-, D-, and J-, gene usage or enriched sequence motifs, that are related to specific diseases or therapies.
- **Specificity-Inference**: Last, we can use the sequence to match AIRs to their target antigen via database queries, sequence distances, or predictors. This directly identifies cells reactive to specific infectious diseases, tumors, or self-antigens.

<!-- markdown cell 7 -->
## Dataset
To showcase different approaches for preprocessing and analysis of IRs, we will use the dataset published by the Haniffa Lab {cite}`stephenson2021single`, which contains transcriptome sequencing for over 750,000 Peripheral Blood Mononuclear Cells (PBMC) from 130 patients in the context of Severe Acute Respiratory Syndrome Coronavirus 2 (SARS-CoV-2).

It consists of patients from three sources (Newcastle, Cambridge, and London) with different degrees of severity (asymptomatic, mild, moderate, severe, and critical) as well as negative controls (healthy, other severe respiratory illnesses, and healthy with Intravenous Liposaccharide to mimic systemic inflammatory response). Additional, patient-level information such as age, gender, and smoker status are provided. 

The dataset was chosen as an example of a large-scale single cell dataset including VDJ-Sequencing, that is well known to the community. It contains over 150,000 B-Cells and 200,000 T-Cells with IR annotation, that we will regard in this analysis tutorial.

<!-- markdown cell 8 -->
To download the data please run the following commands:

## Code cell 9

```python
path_data = "data/"
path_bcr_input = f"{path_data}/BCR_00_read_aligned.csv"
path_tcr_input = f"{path_data}/TCR_00_read_aligned.tsv"
```

## Code cell 10

```bash
! wget -O $path_bcr_input -nc https://figshare.com/ndownloader/files/35574338
! wget -O $path_tcr_input -nc https://figshare.com/ndownloader/files/35574539
```

<!-- markdown cell 11 -->
## Load data
In this tutorial we will mainly use two python packages for loading, cell-level ordering, and visualization:
- **Scanpy**: general package for single cell analysis (https://github.com/theislab/scanpy, {cite}`wolf2018scanpy`)
- **Scirpy**: scanpy extension for immune receptor analysis (https://github.com/scverse/scirpy, {cite}`sturm2020scirpy`)

Here, we only showcase IR analysis with Scirpy. However, there exist several tools with similar functionality such as immunarch(R, {cite}`immunomind2019`), scRepertoire (R, {cite}`borcherding2020screpertoire`), and dandelion (R, {cite}`stephenson2021single`), and Platypus (R, {cite}`yermanos2021platypus`) reviewed in {cite}`valkiers2022recent`. 

:::{warning}
Scirpy changed the format of [its datastructure](https://scirpy.scverse.org/en/latest/data-structure.html#storing-airr-rearrangement-data-in-anndata)
with v0.13. While the overall analysis workflow has not changed, some outputs shown in this chapter might not be accurate anymore. 

See [the scirpy release notes](https://scirpy.scverse.org/en/latest/changelog.html#v0-13-0-new-data-structure-based-on-awkward-arrays) for more details about this change. 
Until we update this chapter, please also refer to the [official scirpy documentation](https://scirpy.scverse.org).
:::

## Code cell 12

```python
import warnings

warnings.filterwarnings(
    "ignore",
    ".*IProgress not found*",
)
warnings.simplefilter(action="ignore", category=FutureWarning)

import pandas as pd
import scanpy as sc
import scirpy as ir

warnings.simplefilter(action="ignore", category=pd.errors.DtypeWarning)
```

<!-- markdown cell 13 -->
Let's set the input and output paths of our data.

## Code cell 14

```python
path_bcr_out = f"{path_data}/BCR_01_preprocessed.h5ad"

path_tcr_csv = f"{path_data}/TCR_00_read_aligned.csv"
path_tcr_out = f"{path_data}/TCR_01_preprocessed.h5ad"
```

<!-- markdown cell 15 -->
### Raw data
We begin by viewing the raw output of the cell ranger pipeline for a better understanding of the data we are working with.
We will load the `filtered_contig_annotations.csv"` file to view its content. Each row will represent one measurement of a sequence.

## Code cell 16

```python
df_bcr_raw = pd.read_csv(path_bcr_input, index_col=0)

# The column 'productive' contains mixed data types which are not compatible with downstream tools.
# We correct them by casting them to strings.
df_bcr_raw["productive"] = df_bcr_raw["productive"].astype(str)
print(f"Total measurements: {len(df_bcr_raw)}")
df_bcr_raw.head(5)
```

<!-- markdown cell 17 -->
The Table contains the following entries, that will be relevant for our preprocessing or analysis. A more detailed explanation of Cell Ranger specific entries can be found here (https://www.10xgenomics.com/support/software/cell-ranger/8.0/analysis/outputs/cr-5p-outputs-annotations-vdj). In other data formats entries (e.g. AIRR) will have similar, deviating names, however the underlying information remains similar.

- **barcode**: tag of the cell the contig was measured from
- **is_cell**: indicates whether the barcode is associated with a cell
- **high_confidence**: confidence of the measurement being a IR
- **chain**: chain of the IR (e.g. TRA: T Cell Receptor α-chain, IGH: Immunoglobulin Heavy chain)
- **{v,d,j,c}_gene**: gene used to form the specific segment of the IR
- **full_length**: whether the full IR was captured (see below)
- **productive**: whether the IR is productive (see below)
- **cdr3{_nt}**: {Nucleotide} sequence of the CDR3 of the IR chain
- **patient_id**: ID indicating the different patients

<!-- markdown cell 18 -->
### Productive AIRs
Even though we can detect the AIR sequence, it might not be productive, i.e., it might not form a valid AIR. Sequences, which do not result in functional AIRs, are therefore flagged as non-productive. These are usually ignored, when loading data by tools such as Scirpy, and not used for any downstream analysis.
Productive Immune receptors are defined by 10x Genomics [here](https://kb.10xgenomics.com/hc/en-us/articles/115003248383-What-are-productive-contigs-) as:
- Sequences spanning over from a V gene to a J-gene
- Having a start {term}`codon` in the leading region
- Containing a CDR3 in the frame of the start codon.
- Do not contain a stop codon within the V-J span

<!-- markdown cell 19 -->
Example 1: Sequences not spanning over a full IR (V to J gene) as indicated by the `full_length` column. You can find missing gene annotation here especially for V and J genes.

## Code cell 20

```python
columns = [
    "barcode",
    "v_gene",
    "d_gene",
    "c_gene",
    "j_gene",
    "productive",
    "full_length",
]
df_bcr_raw[~df_bcr_raw["full_length"]][columns].head()
```

<!-- markdown cell 21 -->
Example 2: Contigs express full length but there is not identifiable CDR3.

## Code cell 22

```python
columns += ["cdr3", "cdr3_nt"]
df_bcr_raw[(df_bcr_raw["productive"] == "False") & (df_bcr_raw["full_length"])][
    columns
].head(5)
```

<!-- markdown cell 23 -->
We will now load the TCR data and convert it from tab-separated format to comma-separated format for later use. Since barcodes overlap between multiple samples within the dataset, we further copy the unique `CellID` as `barcode` annotation. This data also contains annotation on patient-level (e.g. age, outcome, ...) and cell-level annotation (cell type) in addition to the contig annotations previously discussed.

## Code cell 24

```python
df_tcr_raw = pd.read_csv(path_tcr_input, sep="\t")
df_tcr_raw["barcode"] = df_tcr_raw.pop("CellID")
df_tcr_raw.to_csv(path_tcr_csv)
print(f"Total measurements: {len(df_tcr_raw)}")
df_tcr_raw.head()
```

<!-- markdown cell 25 -->
We will find that this data already has been processed: All contigs are of full length and represent a productive IR.

## Code cell 26

```python
df_tcr_raw["full_length"].value_counts()
```

## Code cell 27

```python
df_tcr_raw["productive"].value_counts()
```

<!-- markdown cell 28 -->
## Cell-Aligned Data
In order to perform analysis on cell level, we next need to align IR information previously sorted by contig to a cell based format via the cell barcode. Note that usually many contigs map to the same cell, since every IR consists of VJ and VDJ chain. Also, it has been shown, that a cell can express multiple IRs {cite}`schuldt2019dual`.

We will utilize the Python package Scirpy, that performs the cell-alignment automatically, when reading various TCR information from various formats:

## Code cell 29

```python
adata_tcr = ir.io.read_10x_vdj(path_tcr_csv)
print(f"Amount cells: {len(adata_tcr)}")
```

<!-- markdown cell 30 -->
The IR information will be stored sorted in `adata_tcr.obs` as a Pandas DataFrame with the index representing an individual cell. The DataFrame contains the following columns:
- **has_ir**: indicates whether an IR was detected
- **multi_chain**: indicates whether more than 2 IRs were detected
- **extra_chains**: list of additional chains if multi_chain is true

The contig data we observed in the raw data is stored as well. It is stored as separate columns for the two chains (VJ and VDJ) with up to 2 contigs per chain for each cell:
- IR_V{D}J_{1,2}_locus
- IR_V{D}J_{1,2}_productive
- IR_V{D}J_{1,2}_{v,d,j,c}_call
- IR_V{D}J_{1,2}_junction{_aa}

## Code cell 31

```python
adata_tcr.obs.head(5)
```

<!-- markdown cell 32 -->
Notice, that the patient-level information is not automatically added here. Let's add them by loading the raw data, aligning them on a cell level and indexing them by their barcode.

## Code cell 33

```python
patient_information = [
    "barcode",
    "Centre",
    "Sample",
    "patient_id",
    "Collection_Day",
    "Sex",
    "Swab_result",
    "Status",
    "Smoker",
    "Status_on_day_collection",
    "Status_on_day_collection_summary",
    "Days_from_onset",
    "time_after_LPS",
    "Worst_Clinical_Status",
    "Outcome",
    "initial_clustering",
    "study_id",
    "AgeRange",
    "Age",
]
df_patient = df_tcr_raw[patient_information].copy()
df_patient["Days_from_onset"] = df_patient["Days_from_onset"].astype(
    str
)  # mixed type (str, int)
df_patient = df_patient.drop_duplicates().reset_index(drop=True)

# Assigning barcode as index
df_patient.index = df_patient.pop("barcode")
df_patient.index.name = None
df_patient.head()
```

<!-- markdown cell 34 -->
We can now add this information to the adata object and check, whether the annotation is added as observation.

## Code cell 35

```python
adata_tcr.obs[df_patient.columns] = df_patient
adata_tcr.obs.head()
```

<!-- markdown cell 36 -->
In the same manner we can load the BCR data and check the IR annotation.

## Code cell 37

```python
adata_bcr = ir.io.read_10x_vdj(path_bcr_input)
adata_bcr.obs.head(5)
```

<!-- markdown cell 38 -->
As before, we can add extract additional information annotated for each contig.

## Code cell 39

```python
patient_information = ["barcode", "patient_id"]
df_patient = df_bcr_raw[patient_information].copy()
df_patient = df_patient.drop_duplicates().reset_index(drop=True)

# Assigning barcode as index
df_patient.index = df_patient.pop("barcode")
df_patient.index.name = None
df_patient.head()
```

<!-- markdown cell 40 -->
And add them to the cell annotations:

## Code cell 41

```python
adata_bcr.obs[df_patient.columns] = df_patient
adata_bcr.obs.head()
```

<!-- markdown cell 42 -->
(air-repertoire-ir-profiling-key-takeaway-2)=
## Quality Control
For analysis, we rely on high quality input data. It is therefore of great importance, to identify cells with incorrect or incomplete AIR information:
- **Incomplete AIRs**: A cell is assigned only either a VJ and or a VDJ chain, because the other chain is missed during sequencing. While these are still valid cells, we cannot utilize them for downstream analysis, when full AIR sequence information is required.
- **Multiple AIRs**: It is also possible that a cell gets assigned multiple AIRs. While it has been observed that T- / B-cells can express dual AIR {cite}`schuldt2019dual`, cells with more than two IRs are indicative as doublets, which should not be used for downstream analysis.

We can easily assign this state of the AIR by accumulating the data of the AIR chains. This will enable us later to filter cells, where the AIR cannot be used for our analysis. Here, it heavily depends on your downstream analysis which AIR information is required.

<!-- markdown cell 43 -->
### Assigning AIR State

## Code cell 44

```python
ir.tl.chain_qc(adata_tcr)
```

## Code cell 45

```python
ir.tl.chain_qc(adata_bcr)
```

<!-- markdown cell 46 -->
The following provides the resulting column with an explanation of its possible options:

- chain_pairing
    - **orphan {VJ}/{VDJ}**: cells with only one of VJ or VDJ chain
    - **single pair**: cells with a full paired (VJ and VDJ) AIR
    - **extra {VJ}/{VDJ}**: cells with full paired AIR and an additional VJ or VDJ chain
    - **two full chains**: cells with two paired AIRs
    - **multichain**: cells with more than two VJ or VDJ chains (likely doublets)

- receptor_type: BCR, TCR, no IR, or ambiguous (mixed chains of TCR and BCR)
- receptor_subtype: α/β, ɣ/δ, IG-λ, and IG-κ chain configurations

<!-- markdown cell 47 -->
### Visualization

<!-- markdown cell 48 -->
Depending on the data, the quality of the chain pairing might be different. You should visualize the results over different conditions (e.g. samples, data sources, ...), that could introduce varying quality within your dataset. Let's visualize the data quality collected over the different centers of data collection.

## Code cell 49

```python
_ = ir.pl.group_abundance(adata_tcr, groupby="Centre", target_col="chain_pairing")
```

<!-- markdown cell 50 -->
The data from all three centers contains mainly cells with a single pair of TCRs, which is a sign of good data quality. Often, we can compare different conditions better, when we view the fractions of cells in each condition instead of the absolute amount of cells:

## Code cell 51

```python
_ = ir.pl.group_abundance(
    adata_tcr, groupby="Centre", target_col="chain_pairing", normalize=True
)
```

<!-- markdown cell 52 -->
Here, we can see that all centers offer data of overall comparable data quality. The majority of T cells express a single TCR, followed by orphan VDJ, and VJ chains, which is typical when sequencing TCRs. 
Typical values of a good quality sample may be greater 60% single AIRs, 10-20% orphan chains, and ~10% extra chains.
Note, that the percentage of cells without AIRs is naturally depending on the amount of non-AIR cells in the study, when sequencing multiple-modalities jointly.

## Code cell 53

```python
_ = ir.pl.group_abundance(
    adata_tcr, groupby="Centre", target_col="receptor_type", normalize=True
)
_ = ir.pl.group_abundance(
    adata_tcr, groupby="Centre", target_col="receptor_subtype", normalize=True
)
```

<!-- markdown cell 54 -->
We can see, that the dataset consists only of TCRs (first plot), which is not surprising, since we have separated DataFrames of T - and B-cells. Additionally, the dataset only contains α/β-T cells. Since the amount of cells without IR cannot be recognized in the plot, we will look at the absolute numbers, and observe that only 22 cells have no AIR information. This fraction will be larger in most datasets, when sequencing multiple modalities depending on the amount of AIR cells.

## Code cell 55

```python
adata_tcr.obs["chain_pairing"].value_counts()
```

<!-- markdown cell 56 -->
For the BCR, we will have a look at the patient-level.
For visualization, we downsample to two patients:

## Code cell 57

```python
adata_bcr_tmp = adata_bcr[
    adata_bcr.obs["patient_id"].isin(["COVID-003", "AP11"])
].copy()
_ = ir.pl.group_abundance(
    adata_bcr_tmp, groupby="patient_id", target_col="chain_pairing"
)
_ = ir.pl.group_abundance(
    adata_bcr_tmp, groupby="patient_id", target_col="chain_pairing", normalize=True
)
```

<!-- markdown cell 58 -->
While we observe an considerable difference in the amount of B Cells between the patients, the quality of the chain pairings is comparable.

## Code cell 59

```python
_ = ir.pl.group_abundance(
    adata_bcr_tmp, groupby="patient_id", target_col="receptor_type", normalize=True
)
_ = ir.pl.group_abundance(
    adata_bcr_tmp, groupby="patient_id", target_col="receptor_subtype", normalize=True
)
```

<!-- markdown cell 60 -->
Again, we have only one type of AIR in the dataset (BCRs), but this time a mixture of κ- and λ-chains for the light chain.

<!-- markdown cell 61 -->
(air-repertoire-ir-profiling-key-takeaway-3)=
### Filtering

<!-- markdown cell 62 -->
You might want to filter cells with different AIR states. Depending on your study, you have to decide the trade-off between the amount of data available and the quality of the data, when deciding for filtering. Often, all cells are kept within the dataset with their AIR state flagged. For different downstream analysis, only cells with correct information are then used. E.g. if you perform a database query based on CDR3-VDJ chain (see chapter X), it is possible to use orphan VDJ chains, while this is not possible when searching for the full AIR. In the following, we will show how the filtering is performed. It is up to the reader to decide, whether they want to perform the filtering at this point, or before the different analysis parts.

<!-- markdown cell 63 -->
The filtering can be performed with various degrees of strictness and different combinations such as:
- **has IR**: keep only cells with expressed IRs, since we cannot perform sequence level analysis on them
- **no multi chains**: filter out cells with >2 AIRs to avoid doublets
- **only one AIR**: filter out cells with two AIRs or additional chains since specificity can not be attributed to a certain sequence
- **no single chains**: filter out cells with only VJ or VDJ chains, which cannot be used for all downstream analysis due to missing information

Since we will use the full data throughout this book, we will filter the data to a temporary AnnData object for each step described above. From the absolute cell numbers, you can see how many cells will be lost in each step.

## Code cell 64

```python
adata_bcr_tmp.obs["chain_pairing"].value_counts()
```

## Code cell 65

```python
print(f"Amount of all B cells:\t\t\t\t{len(adata_bcr)}")
adata_bcr_tmp = adata_bcr[adata_bcr.obs["chain_pairing"] != "no IR"]
print(f"Amount of B cells with AIR:\t\t\t{len(adata_bcr_tmp)}")

adata_bcr_tmp = adata_bcr_tmp[adata_bcr_tmp.obs["chain_pairing"] != "multi_chain"]
print(f"Amount of B cells without doublets:\t\t{len(adata_bcr_tmp)}")

adata_bcr_tmp = adata_bcr_tmp[
    ~adata_bcr_tmp.obs["chain_pairing"].isin(
        ["two full chains", "extra VJ", "extra VDJ"]
    )
]
print(f"Amount of B cells with unique AIR per cell:\t{len(adata_bcr_tmp)}")

adata_bcr_tmp = adata_bcr_tmp[adata_bcr_tmp.obs["chain_pairing"] == "single pair"]
print(f"Amount of B cells with sinlge complete AIR:\t{len(adata_bcr_tmp)}")
```

<!-- markdown cell 66 -->
Eventually, we obtain an AnnData object with only single paired BCRs. However, the amount of data can be considerably smaller limiting downstream analysis.

## Code cell 67

```python
adata_bcr_tmp.obs["chain_pairing"].value_counts()
```

<!-- markdown cell 68 -->
Similarly, we can perform this filtering for the TCR data.

## Code cell 69

```python
adata_tcr.obs["chain_pairing"].value_counts()
```

## Code cell 70

```python
print(f"Amount of all T cells:\t\t\t\t{len(adata_tcr)}")
adata_tcr_tmp = adata_tcr[adata_tcr.obs["chain_pairing"] != "no IR"]
print(f"Amount of T cells with AIR:\t\t\t{len(adata_tcr_tmp)}")

adata_tcr_tmp = adata_tcr_tmp[adata_tcr_tmp.obs["chain_pairing"] != "multi_chain"]
print(f"Amount of T cells without doublets:\t\t{len(adata_tcr_tmp)}")

adata_tcr_tmp = adata_tcr_tmp[
    ~adata_tcr_tmp.obs["chain_pairing"].isin(
        ["two full chains", "extra VJ", "extra VDJ"]
    )
]
print(f"Amount of T cells with unique AIR per cell:\t{len(adata_tcr_tmp)}")

adata_tcr_tmp = adata_tcr_tmp[adata_tcr_tmp.obs["chain_pairing"] == "single pair"]
print(f"Amount of T cells with sinlge complete AIR:\t{len(adata_tcr_tmp)}")
```

## Code cell 71

```python
adata_tcr_tmp.obs["chain_pairing"].value_counts()
```

<!-- markdown cell 72 -->
Finally, we save the annotated data for later analysis.

## Code cell 73

```python
sc.write(adata=adata_tcr, filename=path_tcr_out)
sc.write(adata=adata_bcr, filename=path_bcr_out)
```

<!-- markdown cell 74 -->
## Quiz

## Code cell 75

```python
%run ../src/lib.py

flip_card(
    "q1",
    "Where does the high variability of AIRs stem from?",
    "Junctional diversity adds random nucleotides. Peripheral diversity motivates rapid amino acid switches specific to the host organ. Combinatorial diversity of different gene segments. Inherited diversity genetically encodes multiple AIRs.",
    back_font_size=13,
)
flip_card(
    "q2",
    "What properties does a productive AIR have?",
    "It spans over the V- to the J-gene with a CDR3 regions contained. It contains a start codon in the leading region.",
)
flip_card(
    "q3",
    "What cells should be identified for potential filtering?",
    "Cells with high count of AIR sequence reads, cells with incomplete AIR information, etc.",
)
```

<!-- markdown cell 76 -->
## References

<!-- markdown cell 77 -->
```{bibliography}
:filter: docname in docnames
```
