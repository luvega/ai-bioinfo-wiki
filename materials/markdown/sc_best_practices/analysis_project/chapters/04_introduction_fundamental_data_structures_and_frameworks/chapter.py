# Auto-generated from single-cell-best-practices.
# Title: Fundamental data structures and frameworks
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/introduction/fundamental_data_structures_and_frameworks.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (introduction:analysis-frameworks)=
# 
# # Fundamental data structures and frameworks

# %% [markdown]
# (introduction-fundamental-data-structures-and-frameworks-key-takeaway-1)=
# (introduction-fundamental-data-structures-and-frameworks-key-takeaway-2)=
# ## Single-cell analysis frameworks and consortia

# %% [markdown]
# After obtaining the count matrices, as described earlier, the exploratory data analysis phase begins.
# While in the early days, people used to analyze their data with custom scripts, frameworks for precisely this purpose now exist.
# The three most popular options are the R-based Bioconductor {cite}`at:Huber2015` and Seurat {cite}`at:Hao2021` ecosystems and the Python-based scverse {cite}`scverse2022` ecosystem.
# These differ not only in the used programming languages but also in the underlying data structures and available specialized analysis tools.

# %% [markdown]
# Bioconductor is an open-source project for rigorous and reproducible biological data analysis, including single-cell.
# Its greatest strengths are a homogeneous developer and user experience and extensive, user-friendly documentation.
# Seurat is a well-regarded R package for single-cell analysis, covering all analysis steps including multimodal and spatial data.
# It is known for its well-written vignettes and large user base.
# Both R options can struggle with very large datasets (500k+ cells), which motivated the Python community to develop the scverse ecosystem.
# Scverse is an organization dedicated to foundational life science tools, with an initial focus on single-cell.
# Key advantages include scalability, extendability, and strong interoperability with Python's data and machine learning ecosystem.

# %% [markdown]
# All three ecosystems are involved in many efforts to allow for interoperability of the involved frameworks.
# This will be discussed in the ["Interoperability" chapter](../introduction/interoperability.ipynb).
# This book always focuses on the best tools for the corresponding question and will, therefore, use a mix of the above-mentioned ecosystems.
# However, the basis of all analyses will be the scverse ecosystem for two reasons:
# 
# 1. While we will regularly switch ecosystems and even programming languages throughout this book, consistent use of data structures and tooling helps readers focus on the concepts rather than implementation details.
# 2. [A great book on exclusively the Bioconductor ecosystem](https://bioconductor.org/books/release/OSCA/) already exists.
# We encourage users who only want to learn about single-cell analysis with Bioconductor to read it.
# 
# In the following sections, the scverse ecosystem will be introduced in more detail, and the key concepts will be explained with a focus on the most important data structures.
# This chapter introduces the fundamental data structure AnnData and the scanpy framework (See {numref}`scverse-overview-fundamental`).
# In the [following chapter](../introduction/advanced_data_structures_and_frameworks.ipynb), we will explore more advanced libraries.
# This introduction cannot cover all aspects of the data structures and frameworks.
# We refer to the respective frameworks' tutorials and documentation where required.

# %% [markdown]
# :::{figure-md} scverse-overview-fundamental
# <img src="../_static/images/fundamental_data_structures_and_frameworks/fundamental_data_structures_and_frameworks.png" alt="Scverse ecosystem overview" class="bg-primary mb-1" width="100%">
# 
# Scverse ecosystem overview highlighting the libraries of this chapter.
# The publication date by a scientific journal is shown in brackets. We have obtained the symbols of the libraries from the corresponding Github pages {cite}`Virshup2021,Wolf2018,Bredikhin2022,Palla2022,Marconato2025`.
# :::

# %% [markdown]
# (introduction-fundamental-data-structures-and-frameworks-key-takeaway-3)=
# ## Storing unimodal data with AnnData

# %% [markdown]
# As previously discussed, genomics data is typically summarized into a feature matrix after alignment and gene {term}`annotation`.
# This matrix will be of the shape `number_observations x number_variables`.
# In scRNA-seq, observations are cellular barcodes, and the variables are annotated genes.
# Throughout the analysis, the observations and variables of this matrix are annotated with computationally derived measurements (e.g., quality control metrics or latent space embeddings) and prior knowledge (e.g., source donor or alternative gene identifier).
# In the scverse ecosystem, {term}`AnnData` {cite}`Virshup2021` is used to associate the data matrix with these annotations.
# To allow for fast and memory-efficient transformations, AnnData also supports {term}`sparse matrices <sparse matrix>` and partial reading.
# 
# While AnnData is broadly similar to data structures from the R ecosystems (e.g., [Bioconductor's SummarizedExperiment](https://bioconductor.org/packages/release/bioc/html/SummarizedExperiment.html) or [Seurat's object](https://rdrr.io/github/mojaveazure/seurat-object/)), R packages use a transposed feature matrix.

# %% [markdown]
# At its core, an AnnData object stores a sparse or dense matrix (the count matrix in the case of scRNA-Seq) in `X`.
# This matrix has the dimensions of `obs_names x var_names` where the obs (=observations) correspond to the cells' barcodes and the var (=variables) correspond to the gene identifiers.
# This matrix `X` is surrounded by Pandas DataFrames `obs` and `var`, which save annotations of cells and genes, respectively.
# Further, AnnData saves whole matrices of calculations for the observations (`obsm`) or variables (`varm`) with the corresponding dimensions.
# Graph-like structures that associate cells with cells or genes with genes are usually saved in `obsp` and `varp`.
# Any other unstructured data which does not fit any other slot is saved as unstructured data in `uns`.
# It is further possible to store more values of `X` in `layers`.
# Use cases for this are, for example, the storage of raw, unnormalized count data in a `counts` layer and the normalized data in the unnamed default layer.
# AnnData is primarily designed for unimodal (for example, just scRNA-Seq) data.
# However, extensions of AnnData, such as {term}`MuData`, which is covered in the [next chapter](../introduction/advanced_data_structures_and_frameworks.ipynb), allow for the efficient storage and access of multimodal data.

# %% [markdown]
# :::{figure-md} anndata-fig
# <img src="../_static/images/fundamental_data_structures_and_frameworks/anndata.jpg" alt="AnnData Overview" class="bg-primary mb-1" width="800px">
# 
# AnnData overview. Image obtained from {cite}`Virshup2021`.
# :::

# %% [markdown]
# ### Installation

# %% [markdown]
# AnnData is available on PyPI and Conda.
# It can be installed using either of the following commands.
# ```bash
# pip install anndata
# conda install -c conda-forge anndata
# ```

# %% [markdown]
# ### Initializing an AnnData object

# %% [markdown]
# This section is inspired by [AnnData's "getting started" tutorial](https://anndata.readthedocs.io/en/latest/tutorials/notebooks/getting-started.html).
# Let us create a simple AnnData object with {term}`sparse <sparse data>` count information, which may, for example, represent gene expression counts.
# First, we import the required packages.

# %%
# Upstream code cell: 15
import warnings

warnings.filterwarnings("ignore")

# %%
# Upstream code cell: 16
import anndata as ad
import lamindb as ln
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix

ln.track()

# %% [markdown]
# As a next step, we initialize an AnnData object with random {term}`Poisson distributed <Poisson distribution>` data.
# It is an unwritten rule to name the primary AnnData object of the analysis `adata`.

# %%
# Upstream code cell: 18
counts = csr_matrix(
    np.random.default_rng().poisson(1, size=(100, 2000)), dtype=np.float32
)
adata = ad.AnnData(counts)
adata

# %% [markdown]
# The obtained AnnData object has 100 observations and 2000 variables.
# This would correspond to 100 cells with 2000 genes.
# The initial data we passed are accessible as a sparse matrix using `adata.X`.

# %%
# Upstream code cell: 20
adata.X

# %% [markdown]
# Now, we provide the index to both the `obs` and `var` axes using `.obs_names` and `.var_names`, respectively.

# %%
# Upstream code cell: 22
adata.obs_names = [f"Cell_{i:d}" for i in range(adata.n_obs)]
adata.var_names = [f"Gene_{i:d}" for i in range(adata.n_vars)]
print(adata.obs_names[:10])

# %% [markdown]
# ### Adding aligned metadata

# %% [markdown]
# #### Observational or variable level

# %% [markdown]
# The core of our AnnData object is now in place.
# As a next step, we add metadata at both the observational and variable levels.
# Remember, we store such annotations in the `.obs` and `.var` slots of the AnnData object for cell and gene annotations, respectively.

# %%
# Upstream code cell: 26
ct = np.random.default_rng().choice(["B", "T", "Monocyte"], size=(adata.n_obs,))
adata.obs["cell_type"] = pd.Categorical(ct)  # Categoricals are preferred for efficiency
adata.obs

# %% [markdown]
# If we examine the representation of the AnnData object again now, we will notice that it was updated with the `cell_type` information in `obs` as well.

# %%
# Upstream code cell: 28
adata

# %% [markdown]
# #### Subsetting using metadata

# %% [markdown]
# We can also subset the AnnData object with the randomly generated cell types.
# The slicing and masking of the AnnData object behaves similarly to the data access in Pandas DataFrames or R matrices.
# More details on this can be found [below](#subset-adata).

# %%
# Upstream code cell: 31
bdata = adata[adata.obs.cell_type == "B"]
bdata

# %% [markdown]
# ### Observation/variable-level matrices

# %% [markdown]
# We might also have metadata at either level with many dimensions, such as a UMAP embedding of the data.
# AnnData has the `.obsm/.varm` attributes for this type of metadata.
# We use keys to identify the different matrices we insert.
# The restriction of `.obsm/.varm` is that `.obsm` matrices must have a length equal to the number of observations as `.n_obs` and `.varm` matrices must have a length equal to `.n_vars`.
# They can each independently have a different number of dimensions.

# %% [markdown]
# Let us start with a randomly generated matrix that we can interpret as a UMAP embedding of the data we would like to store, as well as some random gene-level metadata.

# %%
# Upstream code cell: 35
adata.obsm["X_umap"] = np.random.default_rng().normal(0, 1, size=(adata.n_obs, 2))
adata.varm["gene_stuff"] = np.random.default_rng().normal(0, 1, size=(adata.n_vars, 5))
adata.obsm

# %% [markdown]
# Again, the AnnData representation is updated.

# %%
# Upstream code cell: 37
adata

# %% [markdown]
# A few more notes about `.obsm/.varm`:
# 
# 1. The “array-like” metadata can originate from a Pandas DataFrame, scipy sparse matrix, or numpy dense array.
# 2. When using scanpy, their values (columns) are not easily plotted, whereas items from `.obs` are easily plotted on, e.g., UMAP plots.

# %% [markdown]
# ### Unstructured metadata

# %% [markdown]
# As mentioned above, AnnData has `.uns`, which allows for any unstructured metadata.
# This can be anything, like a list or a dictionary, with some general information that was useful in the analysis of our data.
# Try only using this slot for data that cannot be efficiently stored in the other slots.

# %%
# Upstream code cell: 41
adata.uns["random"] = [1, 2, 3]
adata.uns

# %% [markdown]
# ### Layers

# %% [markdown]
# Finally, we may have different forms of our original core data, perhaps one that is normalized and one that is not.
# These can be stored in different layers in AnnData.
# For example, let us log transform the original data and store it in a layer.

# %%
# Upstream code cell: 44
adata.layers["log_transformed"] = np.log1p(adata.X)
adata

# %% [markdown]
# Our original matrix `X` was not modified and is still accessible.
# We can verify this by comparing the original `X` to the new layer (`.nnz` returns number of non-zero elements in the boolean matrix).

# %%
# Upstream code cell: 46
(adata.X != adata.layers["log_transformed"]).nnz == 0

# %% [markdown]
# ### Conversion to DataFrames

# %% [markdown]
# It is possible to obtain a Pandas DataFrame from one of the layers.

# %%
# Upstream code cell: 49
adata.to_df(layer="log_transformed")

# %% [markdown]
# ### Reading and writing of AnnData objects

# %% [markdown]
# AnnData objects can be saved on disk to hierarchical array stores like [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) or [Zarr](https://zarr.readthedocs.io/en/stable/index.html) to enable similar structures in disk and on memory.
# AnnData comes with its own persistent HDF5-based file format: `h5ad`.
# If string columns with a few categories are not yet categorical, AnnData will auto-transform them to categorical. We will now save our AnnData object in `h5ad` format.

# %%
# Upstream code cell: 52
adata.write("my_results.h5ad", compression="gzip")

# %% [markdown]
# ... and read it back in.

# %%
# Upstream code cell: 54
adata_new = ad.read_h5ad("my_results.h5ad")
adata_new

# %% [markdown]
# (introduction-fundamental-data-structures-and-frameworks-key-takeaway-4)=
# ### Efficient data access

# %% [markdown]
# #### View and copies

# %% [markdown]
# For the fun of it, let us look at another metadata use case.
# Imagine that the observations come from instruments characterizing 10 readouts in a multi-year study with samples taken from different subjects at different sites.
# We would typically get that information in some format and then store it in a DataFrame:

# %%
# Upstream code cell: 58
obs_meta = pd.DataFrame(
    {
        "time_yr": np.random.default_rng().choice([0, 2, 4, 8], adata.n_obs),
        "subject_id": np.random.default_rng().choice(
            ["subject 1", "subject 2", "subject 4", "subject 8"], adata.n_obs
        ),
        "instrument_type": np.random.default_rng().choice(
            ["type a", "type b"], adata.n_obs
        ),
        "site": np.random.default_rng().choice(["site x", "site y"], adata.n_obs),
    },
    index=adata.obs.index,  # these are the same IDs of observations as above!
)

# %% [markdown]
# This is how we join the readout data with the metadata.
# Of course, the first argument of the following call for `X` could also just be a DataFrame.
# This will result in a single data container that tracks everything.

# %%
# Upstream code cell: 60
adata = ad.AnnData(adata.X, obs=obs_meta, var=adata.var)
adata

# %% [markdown]
# <a id="subset-adata"></a>
# Subsetting the joint data matrix can be important to focus on subsets of variables or observations, or to define train-test splits for a machine learning model.

# %% [markdown]
# Similar to numpy arrays, AnnData objects can either hold actual data or reference another `AnnData` object.
# In the latter case, they are referred to as "view".
# Subsetting AnnData objects always returns views, which has two advantages:
# 
# - No new memory is allocated.
# - It is possible to modify the underlying AnnData object.
#  
# You can get an actual AnnData object from a view by calling `.copy()` on the view.
# Usually, this is not necessary, as any modification of elements of a view (calling `.[]` on an attribute of the view) internally calls `.copy()` and makes the view an AnnData object that holds actual data.
# See the example below.

# %%
# Upstream code cell: 63
adata

# %% [markdown]
# Indexing into AnnData will assume that integer arguments to `[]` behave like `.iloc` in pandas, whereas string arguments behave like `.loc`.
# `AnnData` always assumes string indices.

# %%
# Upstream code cell: 65
adata_view = adata[:5, ["Gene_1", "Gene_3"]]
adata_view

# %% [markdown]
# This is a view! This can be verified by examining the AnnData object again.

# %%
# Upstream code cell: 67
adata

# %% [markdown]
# The dimensions of the AnnData object have not changed. It still contains the same data.
# If we want an AnnData that holds the data in memory, we must call it `.copy()`.

# %%
# Upstream code cell: 69
adata_subset = adata[:5, ["Gene_1", "Gene_3"]].copy()
adata_subset

# %% [markdown]
# For a view, we can also set the first three elements of a column.

# %%
# Upstream code cell: 71
print(adata[:3, "Gene_1"].X.toarray().tolist())
adata[:3, "Gene_1"].X = [0, 0, 0]
print(adata[:3, "Gene_1"].X.toarray().tolist())

# %% [markdown]
# If you try to access parts of a view of an AnnData, the content will be auto-copied and a data-storing object will be generated.

# %%
# Upstream code cell: 73
adata_subset = adata[:3, ["Gene_1", "Gene_2"]]
adata_subset

# %%
# Upstream code cell: 74
adata_subset.obs["foo"] = range(3)

# %% [markdown]
# Now `adata_subset` stores the actual data and is no longer just a reference to adata.

# %%
# Upstream code cell: 76
adata_subset

# %% [markdown]
# Evidently, you can use all of pandas to slice with sequences or boolean indices.

# %%
# Upstream code cell: 78
adata[adata.obs.time_yr.isin([2, 4])].obs.head()

# %% [markdown]
# #### Partial reading of large data

# %% [markdown]
# If a single `h5ad` file is very large, you can partially read it into memory by using backed mode.

# %%
# Upstream code cell: 81
adata = ad.read_h5ad("my_results.h5ad", backed="r")

# %%
# Upstream code cell: 82
adata.isbacked

# %% [markdown]
# If you do this, you will need to remember that the AnnData object has an open connection to the file used for reading.

# %%
# Upstream code cell: 84
adata.filename

# %% [markdown]
# As we are using it in read-only mode, we cannot damage anything.
# To proceed with this tutorial, we still need to explicitly close it.

# %%
# Upstream code cell: 86
adata.file.close()

# %% [markdown]
# (introduction-fundamental-data-structures-and-frameworks-key-takeaway-5)=
# ## Unimodal data analysis with scanpy

# %% [markdown]
# Now that we understand the fundamental data structure of unimodal single-cell analysis, the question remains: How can we actually analyze the stored data?
# In the scverse ecosystem, several tools exist for analyzing specific omics data.
# For example, scanpy {cite}`Wolf2018` provides tooling for general RNA-Seq-focused analysis, squidpy {cite}`Palla2022` focuses on spatial transcriptomics, and scirpy {cite}`Sturm2020` provides tooling for the analysis of T-cell receptor (TCR) and B-cell receptor (BCR) data.
# Even though many scverse extensions for various data modalities exist, they usually use some of scanpy's preprocessing and visualization capabilities to some extent.

# %% [markdown]
# More specifically, scanpy is a Python package that builds on top of AnnData to facilitate the analysis of single-cell gene expression data.
# Several methods for preprocessing, embedding, visualization, clustering, {term}`differential gene expression <Differential gene expression (DGE)>` testing, pseudotime and trajectory inference, and simulation of gene regulatory networks are accessible through scanpy.
# The efficient implementation based on the Python data science and machine learning libraries allows scanpy to scale to millions of cells.
# Generally, best-practice single-cell data analysis is an interactive process.
# Many of the decisions and analysis steps depend on the results of previous steps and the potential input of experimental partners.
# Pipelines such as scflow {cite}`at:Khozoie2021` entirely automate some downstream analysis steps.
# These pipelines have to make assumptions and simplifications, which may not result in the most robust analysis.
# Scanpy is therefore designed for interactive analyses with, for example, Jupyter Notebooks {cite}`jupyter`.

# %% [markdown]
# :::{figure-md} scanpy-fig
# <img src="../_static/images/fundamental_data_structures_and_frameworks/scanpy.jpg" alt="scanpy Overview" class="bg-primary mb-1" width="800px">
# 
# Scanpy overview. Image obtained from {cite}`Wolf2018`.
# :::

# %% [markdown]
# ### Installation

# %% [markdown]
# Scanpy is available on PyPI and Conda.
# It can be installed using either of the following commands.
# ```bash
# pip install scanpy
# conda install -c conda-forge scanpy
# ```

# %% [markdown]
# ### Scanpy API design

# %% [markdown]
# The scanpy framework is designed in a way that functions belonging to the same step are grouped into corresponding modules.
# For example, all preprocessing functions are available in the `scanpy.preprocessing` module, all transformations of a data matrix that are not preprocessing are available in `scanpy.tools`, and all visualizations are available in `scanpy.plot`.
# These modules are commonly accessed after having imported scanpy like `import scanpy as sc` with the corresponding abbreviations `sc.pp` for preprocessing, `sc.tl` for tools, and `sc.pl` for plots.
# All modules which read or write data are directly accessed.
# Further, a module for various datasets is available as `sc.datasets`.
# All functions with corresponding parameters and potential example plots are documented in the scanpy API documentation {cite}`scanpy_api`.
# 
# Note that this tutorial only covers a tiny subset of scanpy's features and options.
# Readers are strongly encouraged to examine [scanpy's documentation](https://scanpy.readthedocs.io/) for more details.

# %% [markdown]
# :::{figure-md} scanpy-api
# <img src="../_static/images/fundamental_data_structures_and_frameworks/scanpy_api.png" alt="scanpy API" class="bg-primary mb-1" width="800px">
# 
# Scanpy API overview. The API is divided into datasets, preprocessing (pp), tools (tl) and corresponding plotting (pl) functions.
# :::

# %% [markdown]
# ### Scanpy example

# %% [markdown]
# In the following cells we will shortly demonstrate the workflow of an analysis with scanpy.
# We explicitly do not conduct a full analysis because the specific analysis steps are covered in the corresponding chapters.

# %% [markdown]
# As a first step we import scanpy and define defaults for our following quick scanpy demo.
# We use scanpy's setting object to  set the Matplotlib plotting defaults for all of scanpy's plots and finally print scanpy's header.
# This header contains the versions of all relevant Python packages in the current environment including scanpy and AnnData.
# This output is especially useful when reporting bugs to the scverse team and for reproducibility reasons.

# %%
# Upstream code cell: 99
import scanpy as sc

sc.settings.set_figure_params(dpi=80, facecolor="white")
sc.logging.print_header()

# %% [markdown]
# The dataset of choice is a dataset of 2700 peripheral blood mononuclear cells of a healthy donor which were sequenced on the Illumina NextSeq 500. 
# We can load the dataset from `lamindb`, although it is also available via `sc.datasets.pbmc3k()`.

# %%
# Upstream code cell: 101
adata = ln.Artifact.get(
    key="introduction/fundamental_data_structures_and_frameworks.h5ad", is_latest=True
).load()
adata

# %% [markdown]
# The returned AnnData object has 2700 cells with 32738 genes. 
# The `var` slot further contains the gene IDs.

# %%
# Upstream code cell: 103
adata.var

# %% [markdown]
# As mentioned above, all of scanpy's analysis functions are accessible via `sc.[pp, tl, pl]`. 
# As a first step to get an overview over our data, we use scanpy to show those genes that yield the highest fraction of counts in each single cell, across all cells. 
# We simply call the `sc.pl.highest_expr_genes` function, pass the AnnData object which is in pretty much all cases the first parameter of any scanpy function, and specify that we want the top 20 expressed genes to be shown.

# %%
# Upstream code cell: 105
sc.pl.highest_expr_genes(adata, n_top=20)

# %% [markdown]
# Apparently, _MALAT1_ is the most expressed gene which is frequently detected in poly-A captured scRNA-Seq data, independent of protocol. 
# This gene has been shown to have an inverse correlation with cell health. 
# Especially dead/dying cells have a higher expression of _MALAT1_.
# 
# We now filter cells with less than 200 detected genes and genes which were found in less than 3 cells for a rough quality threshold with scanpy's preprocessing module.

# %%
# Upstream code cell: 107
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)

# %% [markdown]
# A common step in single-cell RNA-Seq analysis is dimensionality reduction with for example PCA to unveil the main axes of variation. 
# This also denoises the data. 
# Scanpy offers PCA as a `preprocessing` or `tools` function. 
# These are equivalent. 
# Here, we use the version in `tools` for no particular reason.

# %%
# Upstream code cell: 109
sc.tl.pca(adata, svd_solver="arpack")

# %% [markdown]
# The corresponding plotting function allows us to pass genes to the color argument. 
# The corresponding values are automatically extracted from the AnnData object.

# %%
# Upstream code cell: 111
sc.pl.pca(adata, color="CST3")

# %% [markdown]
# A fundamental step for any advanced embedding and downstream calculations is the calculating of the neighborhood graph using the PCA representation of the data matrix.
# It is automatically used for other tools that require it such as the calculation of a UMAP.

# %%
# Upstream code cell: 113
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)

# %% [markdown]
# We now use the calculating neighborhood graph to embed the cells with a UMAP, one of many advanced dimension reduction {term}`algorithms <algorithm>` implemented in scanpy.

# %%
# Upstream code cell: 115
sc.tl.umap(adata)

# %%
# Upstream code cell: 116
sc.pl.umap(adata, color=["CST3", "NKG7", "PPBP"])

# %% [markdown]
# Scanpy's documentation also provides [tutorials](https://scanpy.readthedocs.io/en/stable/tutorials.html) which we recommend to all readers who need a refresher of scanpy or are new to scanpy. 
# Video tutorials are available on the [scverse youtube channel](https://www.youtube.com/channel/UCpsvsIAW3R5OdftJKKuLNMA).

# %% [markdown]
# ## Questions
# ### Flipcards

# %%
# Upstream code cell: 119
%run ../src/lib.py

flip_card(
    "q1",
    "What is the fundamental data structure for single-cell analysis in the scverse?",
    "AnnData",
)

flip_card(
    "q2",
    "What is the fundamental framework for single-cell analysis in the scverse?",
    "Scanpy",
)

flip_card(
    "q3",
    "In single-cell RNA-seq data, which dimensions correspond to genes and cells?",
    "Genes are stored in `.var` (columns), and cells are stored in `.obs` (rows) of the matrix.",
)

# %% [markdown]
# ### Multiple-choice questions

# %%
# Upstream code cell: 121
%run ../src/lib.py

multiple_choice_question(
    question_id="q4",
    question="What is a common limitation of the R-based frameworks Bioconductor and Seurat?",
    options=[
        "Inability to store gene annotations",
        "Lack of preprocessing functions",
        "Scalability issues with more than ~500,000 cells",
        "Lack of comprehensive documentation",
    ],
    correct_answer="Scalability issues with more than ~500,000 cells",
    explanations={},
)

multiple_choice_question(
    question_id="q3a",
    question="In an AnnData object, which slot stores the main count matrix for scRNA-seq data?",
    options=["X", "obs", "var", "uns"],
    correct_answer="X",
    explanations={
        "obs": "`.obs` stores cell-level metadata (observations), not the main count matrix.",
        "var": "`.var` stores gene-level metadata (variables), not the expression matrix itself.",
        "uns": "`.uns` stores unstructured metadata.",
    },
)

multiple_choice_question(
    question_id="q3b",
    question="Where would you store additional matrices derived from the main data, such as normalized counts or log-transformed values, in an AnnData object?",
    options=["layers", "obsm", "varp", "uns"],
    correct_answer="layers",
    explanations={
        "obsm": "`.obsm` stores matrices of calculations for the observations, such as PCA or UMAP embeddings.",
        "varp": "`.varp` stores graph-like structures that associate genes with genes.",
        "uns": "`.uns` stores unstructured metadata.",
    },
)

# %% [markdown]
# ## References

# %% [markdown]
# ```{bibliography}
# :filter: docname in docnames
# :labelprefix: at
# ```

# %% [markdown]
# ## Contributors
# 
# We gratefully acknowledge the contributions of:
# 
# ### Authors
# 
# * Lukas Heumos
# * Luis Heinzlmeier
# 
# ### Reviewers
# 
# * Isaac Virshup
