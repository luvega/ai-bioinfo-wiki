---
type: scbp-chapter-source
title: "Multimodal and spatial data structures"
upstream_path: jupyter-book/introduction/advanced_data_structures_and_frameworks.ipynb
upstream_ref: 735f26fd270b3beceb4ba79f4a556c912192fe83
status: generated
tags: [single-cell, scbp, notebook, course-material]
---

# Multimodal and spatial data structures

> Generated from the upstream notebook. Markdown and code cells are preserved; outputs are extracted separately.

<!-- markdown cell 1 -->
# Multimodal and spatial data structures

<!-- markdown cell 2 -->
:::{figure-md} scverse-overview-advanced
<img src="../_static/images/advanced_data_structures_and_frameworks/advanced_data_structures_and_frameworks.png" alt="Scverse ecosystem overview" class="bg-primary mb-1" width="100%">

Scverse ecosystem overview highlighting the libraries of this chapter. The publication date by a scientific journal is shown in brackets. We have obtained the symbols of the libraries from the corresponding Github pages {cite}`Virshup2021,Wolf2018,Bredikhin2022,Palla2022,Marconato2025`.
:::

<!-- markdown cell 3 -->
This chapter assumes familiarity with AnnData and scanpy from the [previous chapter](https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/introduction/fundamental_data_structures_and_frameworks.ipynb).
It introduces two further data structures — MuData for multimodal assays and SpatialData for spatially resolved data — and the analysis frameworks built on top of each.

<!-- markdown cell 4 -->
(at:mudata)=
(introduction-advanced-data-structures-and-frameworks-key-takeaway-1)=
(introduction-advanced-data-structures-and-frameworks-key-takeaway-2)=
## Using MuData to store multimodal data

<!-- markdown cell 5 -->
AnnData is primarily designed for storing and manipulating unimodal data.
However, multimodal assays such as CITE-Seq generate multimodal data by simultaneously measuring RNA and surface proteins.
This data requires more advanced ways of storing, which is where MuData comes into play.
MuData builds on top of AnnData to store and manipulate multimodal data. Muon {cite}`Bredikhin2022`, a "Scanpy equivalent" and core package of scverse, can then be used to analyze the multimodal omics data. 
The following section is based on the [MuData Quickstart](https://mudata.readthedocs.io/stable/notebooks/quickstart_mudata.html) and the [Multimodal data objects](https://mudata.readthedocs.io/stable/io/mudata.html#) tutorial.

<!-- markdown cell 6 -->
:::{figure-md} mudata-fig
<img src="../_static/images/advanced_data_structures_and_frameworks/mudata.png" alt="MuData Overview" class="bg-primary mb-1" width="800px">

MuData overview. Image obtained from {cite}`Bredikhin2022`.
:::

<!-- markdown cell 7 -->
### Installation

<!-- markdown cell 8 -->
MuData is available on PyPI and Conda. It can be installed using either of the following commands.
```bash
pip install mudata
conda install -c conda-forge mudata
```

<!-- markdown cell 9 -->
The main idea behind MuData is that the MuData object contains references to single AnnData objects of the unimodal data, but the MuData object itself also stores multimodal annotations.
It is therefore possible to directly access the AnnData objects to perform unimodal data transformations which store their results in the corresponding AnnData annotations, but also to aggregate the modalities for joint calculations whose results can be stored in the global MuData object.
Technically, this is realized by MuData objects comprising a dictionary with AnnData objects, one per modality, in their `.mod` (=modality) attribute.
Just as AnnData objects themselves, MuData objects also contain attributes like `.obs` with annotation of observations (samples or cells), `.obsm` with their multidimensional annotations such as embeddings.

## Code cell 10

```python
import os
import warnings

warnings.filterwarnings("ignore")
os.environ["PYTHONWARNINGS"] = "ignore"
```

<!-- markdown cell 11 -->
### Initializing a MuData object

<!-- markdown cell 12 -->
Let's import MuData from the mudata package.

## Code cell 13

```python
import lamindb as ln
import mudata as md
import numpy as np

ln.track()
```

<!-- markdown cell 14 -->
To create an example MuData object we require simulated data.
Therefore, we created two AnnData objects with *data for the same observations*, but for *different variables*.

## Code cell 15

```python
adata = ln.Artifact.get(
    key="introduction/advanced_data_structures_and_frameworks_mudata_1.h5ad",
).load()
adata
```

## Code cell 16

```python
adata2 = ln.Artifact.get(
    key="introduction/advanced_data_structures_and_frameworks_mudata_2.h5ad",
).load()
adata2
```

<!-- markdown cell 17 -->
These two AnnData objects (two "modalities") can then be wrapped into a single MuData object.
Here, we name modality one `A` and modality two `B`.

## Code cell 18

```python
mdata = md.MuData({"A": adata, "B": adata2})
mdata
```

<!-- markdown cell 19 -->
Observations and variables of the `MuData` object are global, which means that observations with the identical name (`.obs_names`) in different modalities are considered to be the same observation (e.g. `obs_1` in `adata` and `obs_1` in `adata2`).
This also means variable names (`.var_names`) should be unique (e.g. `var_1` in `adata` and `var2_1` in `adata2`).
This is reflected in the object description above: `mdata` has 1000 observations and 150 = 100+50 variables.

<!-- markdown cell 20 -->
### MuData attributes

<!-- markdown cell 21 -->
#### `.mod`
MuData objects consist of annotations as earlier described for AnnData objects like `.obs` or `.var`, but extend this behavior with `.mod` which serves as an accessor to the individual modalities.
Modalities are stored in a collection accessible via the `.mod` attribute of the MuData object with names of modalities as keys and AnnData objects as values.

## Code cell 22

```python
list(mdata.mod.keys())
```

<!-- markdown cell 23 -->
Individual modalities can be accessed with their names via the `.mod` attribute or via the MuData object itself as a shorthand.

## Code cell 24

```python
print(mdata.mod["A"])
print(mdata["A"])
```

<!-- markdown cell 25 -->
#### `.obs` and `.var`
Samples (cells) annotation is accessible via the `.obs` attribute and by default includes copies of columns from `.obs` data frames of individual modalities.
The same goes for `.var`, which contains annotation of variables (features).
Observations columns copied from individual modalities contain modality name as their prefix, e.g. rna:n_genes.
This is also true for variables columns.
However if there are columns with identical names in `.var` of multiple modalities (e.g., n_cells), these columns are merged across modalities and no prefix is added.
When those slots are changed in AnnData objects of modalities, e.g. new columns are added or samples (cells) are filtered out, the changes have to be fetched with the `.update()` method (see below).

## Code cell 26

```python
mdata.var_names
```

<!-- markdown cell 27 -->
Multidimensional annotations of samples (cells) are accessible in the `.obsm` attribute.
For instance, that can be UMAP coordinates that were learnt jointly on all modalities.

<!-- markdown cell 28 -->
If the shape of a modality is changed (e.g. change `var_names`), `MuData.update()` has to be run to bring the respective updates to the MuData object.

## Code cell 29

```python
adata2.var_names = ["var_ad2_" + e.split("_")[1] for e in adata2.var_names]
print("Outdated variables names: ...,", ", ".join(mdata.var_names[-3:]))
mdata.update()
print("Updated variables names: ...,", ", ".join(mdata.var_names[-3:]))
```

<!-- markdown cell 30 -->
Importantly, individual modalities are stored as references to the original objects. 
Hence, if the original AnnData is changed the change will also be reflected in the MuData object.

## Code cell 31

```python
# Add some unstructured data to the original object
adata.uns["misc"] = {"adata": True}
```

## Code cell 32

```python
# Access modality A via the .mod attribute
mdata.mod["A"].uns["misc"]
```

<!-- markdown cell 33 -->
### Variable mappings

<!-- markdown cell 34 -->
Upon construction of a MuData object, a global binary mapping between observations and individual modalities is created as well as between variables and modalities.
Since all the observations are the same across modalities in `mdata`, all the values in the observations mappings are set to `True`.

## Code cell 35

```python
mdata.obsm["A"]
```

## Code cell 36

```python
np.sum(mdata.obsm["A"]) == np.sum(mdata.obsm["B"]) == 1000
```

<!-- markdown cell 37 -->
For variables however, those are 150-long vectors.
The `A` modality has 100 `True` values followed by 50 `False` values.

## Code cell 38

```python
mdata.varm["A"]
```

<!-- markdown cell 39 -->
### MuData views

<!-- markdown cell 40 -->
Analogous to the behavior of AnnData objects, slicing MuData objects returns views of the original data.

## Code cell 41

```python
view = mdata[:100, :1000]
print(view.is_view)
print(view["A"].is_view)
```

<!-- markdown cell 42 -->
Subsetting MuData objects is special since it slices them across modalities. 
For example, the slicing operation for a set of `obs_names` and/or `var_names` will be performed for each modality and not only for the global multimodal annotation.
This behavior makes workflows memory-efficient, which is especially important when working with large datasets.
If the object is to be modified however, a copy of it should be created, which is not a view anymore and has no dependence on the original object.

## Code cell 43

```python
mdata_sub = view.copy()
mdata_sub.is_view
```

<!-- markdown cell 44 -->
### Common observations

<!-- markdown cell 45 -->
While a MuData object is comprised of the same observations for both modalities, it is not always the case in the real world where some data might be missing.
By design, MuData accounts for these scenarios since there’s no guarantee observations are the same (or even intersecting) for a MuData instance.
It’s worth noting that other tools might provide convenience functions for some common scenarios of dealing with missing data, such as `intersect_obs()` implemented in muon.

<!-- markdown cell 46 -->
### Reading and Writing of MuData objects

<!-- markdown cell 47 -->

Similarly to AnnData objects, MuData objects were designed to be serialized into HDF5 based `.h5mu` files.
All modalities are stored under their respective names in the `/mod` HDF5 group of the `.h5mu` file. Each individual modality, e.g. `/mod/A`, is stored in the same way as it would be stored in the `.h5ad` file.
MuData objects can be read and written as follows:

## Code cell 48

```python
mdata.write("my_mudata.h5mu")
mdata_r = md.read("my_mudata.h5mu", backed=True)
mdata_r
```

<!-- markdown cell 49 -->
Individual modalities are backed as well inside the `.h5mu` file.

## Code cell 50

```python
mdata_r["A"].isbacked
```

<!-- markdown cell 51 -->
If the original object is backed, provide a new filename to the `.copy()` call, and the resulting object will be backed at a new location.

## Code cell 52

```python
mdata_sub = mdata_r.copy("mdata_sub.h5mu")
print(mdata_sub.is_view)
print(mdata_sub.isbacked)
```

<!-- markdown cell 53 -->
### Multimodal methods

<!-- markdown cell 54 -->
When the MuData object is prepared, it is up to multimodal methods to be used to make sense of the data. 
The most simple and naive approach is to concatenate matrices from multiple modalities to perform for example dimensionality reduction.

## Code cell 55

```python
x = np.hstack([mdata.mod["A"].X, mdata.mod["B"].X])
x.shape
```

<!-- markdown cell 56 -->
We can write a simple function to run a {term}`principal component analysis (PCA)` on such a concatenated matrix.
MuData object provides a place to store multimodal {term}`embeddings <embedding>`: MuData `.obsm`.
It is similar to how the embeddings generated on individual modalities are stored, only this time it is saved inside the MuData object rather than in AnnData `.obsm`.

To calculate for example a PCA for the joint values of the modalities, we horizontally stack the values stored in the individual modalities and then perform the PCA on the stacked matrix.
This is possible because the number of observations matches across modalities (remember, the number of features per modality does not have to match).

## Code cell 57

```python
def simple_pca(mdata):
    from sklearn import decomposition

    x = np.hstack([m.X for m in mdata.mod.values()])

    pca = decomposition.PCA(n_components=2)
    components = pca.fit_transform(x)

    # By default, methods operate in-place and embeddings are stored in the .obsm slot
    mdata.obsm["X_pca"] = components
```

## Code cell 58

```python
simple_pca(mdata)
print(mdata)
```

<!-- markdown cell 59 -->
Our calculated principal components are now stored in the MuData object itself and accessible for further multimodal transformations.

<!-- markdown cell 60 -->
In reality, however, having different modalities often means that the features between them come from different generative processes and are not comparable.
This is where special multimodal integration methods come into play.
For omics technologies, these methods are frequently addressed as multi-omics integration methods.
In the following section we will introduce muon which provides many tools to preprocess unimodal data beyond RNA-Seq and multi-omics integration methods.

<!-- markdown cell 61 -->
(introduction-advanced-data-structures-and-frameworks-key-takeaway-3)=
## Multimodal data analysis with muon

<!-- markdown cell 62 -->
Although Scanpy provides generally applicable tools such as PCA, UMAP, and various visualizations, it is primarily designed to analyze RNA-Seq data.
Muon fills this gap by providing preprocessing functions for other omics, such as chromatin accessibility (ATAC) or protein (CITE) data.
As mentioned above, muon further provides algorithms to run multi-omics algorithms that infer knowledge from the joint modalities.
For example, users may run a PCA on a single modality, but muon further provides multi-omics factor analysis algorithms that take several modalities as input. 
The following sections was adopted from the muon tutorial ["Processing chromatin accessibility of 10k PBMCs"](https://muon-tutorials.readthedocs.io/en/latest/single-cell-rna-atac/pbmc10k/2-Chromatin-Accessibility-Processing.html#Processing-chromatin-accessibility-of-10k-PBMCs).

<!-- markdown cell 63 -->
:::{figure-md} muon-fig
<img src="../_static/images/advanced_data_structures_and_frameworks/muon.png" alt="muon Overview" class="bg-primary mb-1" width="800px">

muon overview. Image obtained from {cite}`Bredikhin2022`.
:::

<!-- markdown cell 64 -->
### Installation

<!-- markdown cell 65 -->
Muon is available on PyPI and can be installed using:
```bash
pip install muon
```

<!-- markdown cell 66 -->
### API overview

<!-- markdown cell 67 -->
To introduce muon, we will examine the ATAC data from a multimodal dataset.
Analogously to the Scanpy chapter, this chapter solely serves as a quick demo and overview of muon and does not analyze a dataset thoroughly, let alone provide best-practice multi-omics analysis.
Please read the corresponding chapters to learn how to properly conduct such analyses.

Muon separates its modules in two ways. First, analogously to Scanpy, general and multimodal functions are grouped in preprocessing (`muon.pp`), tools (`muon.tl`) and plots (`muon.pl`).
Second, unimodal tools are available from the corresponding muon, which are again separated into preprocessing, tools and plots.
For example, all ATAC preprocessing functions are grouped into `muon.atac.pp`.
This also applies to CITE-Seq preprocessing functions (`muon.prot.pp`).

<!-- markdown cell 68 -->
:::{figure-md} muon-api
<img src="../_static/images/advanced_data_structures_and_frameworks/muon_api.png" alt="muon API Overview" class="bg-primary mb-1" width="800px">

Muon API overview. Modality specific functions are provided in correspondingly named modules. Functions for the joint analysis of modalities are available via the muon module directly.
:::

<!-- markdown cell 69 -->
### Muon API demo

<!-- markdown cell 70 -->
The dataset for our demo is a publicly available 10x Genomics Multiome dataset for human peripheral blood mononuclear cells (PBMCs).

## Code cell 71

```python
import muon as mu

mdata = ln.Artifact.get(
    key="introduction/advanced_data_structures_and_frameworks_muon.h5mu", is_latest=True
).load()

fragments = ln.Artifact.get(
    key="introduction/advanced_data_structures_and_frameworks_atac_fragments.tsv.gz",
    is_latest=True,
).cache()

fragments_tbi = ln.Artifact.get(
    key="introduction/advanced_data_structures_and_frameworks_atac_fragments.tsv.gz.tbi",
    is_latest=True,
).cache()

mdata
```

<!-- markdown cell 72 -->
As a first step we subset to the ATAC modality.

## Code cell 73

```python
atac = mdata.mod["atac"]
```

<!-- markdown cell 74 -->
Although, we are now not working with RNA-Seq, it is possible to use some of Scanpy's preprocessing functions which can also be used on ATAC data.
This is possible due to similar distribution and quality issues of both modalities.
The only thing to bear in mind here that a gene would mean a peak in the context of the AnnData object with ATAC-seq data.
Afterwards, ATAC specific preprocessing can be conducted with the ATAC module of muon.

Let us start with some quality control by filtering out cells with too few peaks and peaks detected in too few cells.
For now, we will filter out cells that do not pass QC.

## Code cell 75

```python
import scanpy as sc

sc.pp.calculate_qc_metrics(atac, percent_top=None, log1p=False, inplace=True)
```

## Code cell 76

```python
sc.pl.violin(atac, ["total_counts", "n_genes_by_counts"], jitter=0.4, multi_panel=True)
```

<!-- markdown cell 77 -->
Filter peaks whose expression is not detected.

## Code cell 78

```python
mu.pp.filter_var(atac, "n_cells_by_counts", lambda x: x >= 10)
# This is analogous to
#   sc.pp.filter_genes(rna, min_cells=10)
# but does in-place filtering and avoids copying the object
```

<!-- markdown cell 79 -->
We also filter the cells.

## Code cell 80

```python
mu.pp.filter_obs(atac, "n_genes_by_counts", lambda x: (x >= 2000) & (x <= 15000))
# This is analogous to
#   sc.pp.filter_cells(atac, max_genes=15000)
#   sc.pp.filter_cells(atac, min_genes=2000)
# but does in-place filtering avoiding copying the object

mu.pp.filter_obs(atac, "total_counts", lambda x: (x >= 4000) & (x <= 40000))
```

## Code cell 81

```python
sc.pl.violin(atac, ["n_genes_by_counts", "total_counts"], jitter=0.4, multi_panel=True)
```

<!-- markdown cell 82 -->
Muon also provides histograms which allows for a different view on the metrics.

## Code cell 83

```python
mu.pl.histogram(atac, ["n_genes_by_counts", "total_counts"])
```

<!-- markdown cell 84 -->
Now that we rudimentary filtered out cells with too few peaks and peaks detected in too few cells, we can start with ATAC specific quality control with muon.
Muon has modality specific preprocessing functions in corresponding modules.
We import the ATAC module to access the ATAC specific preprocessing functions.

## Code cell 85

```python
from muon import atac as ac
```

## Code cell 86

```python
# Perform rudimentary quality control with muon's ATAC module
atac.obs["NS"] = 1
ac.tl.locate_fragments(mdata, fragments=str(fragments))
ac.tl.locate_fragments(atac, fragments=str(fragments))
ac.tl.nucleosome_signal(atac, n=1e6)
ac.tl.get_gene_annotation_from_rna(mdata["rna"]).head(3)
tss = ac.tl.tss_enrichment(mdata, n_tss=1000)
ac.pl.tss_enrichment(tss)
```

## Code cell 87

```python
# Save original counts, normalize data and select highly variable genes with scanpy
atac.layers["counts"] = atac.X
sc.pp.normalize_per_cell(atac, counts_per_cell_after=1e4)
sc.pp.log1p(atac)
sc.pp.highly_variable_genes(atac, min_mean=0.05, max_mean=1.5, min_disp=0.5)
atac.raw = atac
```

<!-- markdown cell 88 -->
Although PCA is also commonly used for ATAC data, latent semantic indexing (LSI) is another popular option. It is implemented in muon's ATAC module.

## Code cell 89

```python
ac.tl.lsi(atac)
sc.pp.neighbors(atac, use_rep="X_lsi", n_neighbors=10, n_pcs=30)
sc.tl.leiden(atac, resolution=0.5)
sc.tl.umap(atac, spread=1.5, min_dist=0.5, random_state=20)
sc.pl.umap(atac, color=["leiden", "n_genes_by_counts"], legend_loc="on data")
```

<!-- markdown cell 90 -->
We can use the functionality of the ATAC module in muon to color plots by cut values in peaks corresponding to a certain gene.

## Code cell 91

```python
ac.pl.umap(atac, color=["KLF4"], average="peak_type")
```

<!-- markdown cell 92 -->
For more details on all available functions of muon, please read the [muon API reference](https://muon.readthedocs.io/en/latest/api/index.html) and the [muon tutorials](https://muon-tutorials.readthedocs.io/en/latest/).

<!-- markdown cell 93 -->
(introduction-advanced-data-structures-and-frameworks-key-takeaway-4)=
## Using SpatialData to store multimodal and spatial data

Spatial omics refers to technologies that measure molecular information (gene expression, chromatin accessibility, proteins) while preserving their physical location inside a tissue.
Traditional single-cell methods lose spatial context during tissue dissociation, whereas spatial omics retains both molecular profiles and spatial positions of individual cells.
Because these datasets combine images, coordinates, and multiple molecular measurements, they are large, complex, and require specialized spatially aware data structures.
SpatialData unifies raw and processed data from multiple spatial omics technologies {cite}`Marconato2025`.
Its five primitive elements (SpatialElements) are saved in a Zarr store following the OME–NGFF standard, a standardized format for bioimaging data.

<!-- markdown cell 94 -->
### Installation and importing
Again, either use PyPI or Conda to install SpatialData.
```bash
pip install spatialdata
conda install -c conda-forge spatialdata
```

<!-- markdown cell 95 -->
### Key terms and data model
We can think of a `SpatialData` object as a container for various `Elements`. An `Element` is either a `SpatialElement` (`Images`, `Labels`, `Points`, `Shapes`) or a `Table`. Here is a brief description:
- `Images`: H&E, staining images
- `Labels`: pixel-level segmentation
- `Points`: transcripts locations with gene information, landmarks points
- `Shapes`: cell/nucleus boundaries, subcellular structures, anatomical annotations, regions of interest (ROIs)
- `Tables`: sparse/dense matrices annotating the `SpatialElements` or storing arbitrary (non-spatial) metadata. They do not contain spatial coordinates.

We can categorize the `SpatialElements` into two broad types:
- `Rasters`: Data made up of pixels: including `Images` and `Labels`
- `Vectors`: Data made up of points and lines. Polygons are also vectors, since they are simply a list of connected points. `Points` and `Shapes` are elements of this type.

:::{figure-md} spacialdata-fig
<img src="../_static/images/advanced_data_structures_and_frameworks/SpacialData_elements.png" alt="Overview of SpacialData's elements" max-width = 800px>

The elements of a SpatialData object. Obtained from .
:::

## Code cell 96

```python
import spatialdata as sd
import spatialdata_plot  # noqa: F401
```

<!-- markdown cell 97 -->
Let’s load a mouse liver dataset using `lamindb`. The original dataset is available [here](https://s3.embl.de/spatialdata/spatialdata-sandbox/mouse_liver.zip).

## Code cell 98

```python
# Suppress ome-zarr's "no parent found" log message which indicates a minor structural inconsistency in the Zarr store that does not affect data loading.
import logging

logging.getLogger("ome_zarr").setLevel(logging.ERROR)
```

## Code cell 99

```python
sdata = ln.Artifact.get(
    key="introduction/advanced_data_structures_and_frameworks_spatialdata.zarr"
).load()
sdata
```

## Code cell 100

```python
# Reset ome-zarr logging level back to default
logging.getLogger("ome_zarr").setLevel(logging.WARNING)
```

<!-- markdown cell 101 -->
### Explore the `Elements` of the `SpatialData` object

Let's explore each element type and how they are represented:
- Images: [`xarray.DataArray`](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html) or [`xarray.DataTree`](https://docs.xarray.dev/en/stable/generated/xarray.DataTree.html) objects respectively for single-scale or multi-scale images
- Labels: [`xarray.DataArray`](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html) or [`xarray.DataTree`](https://docs.xarray.dev/en/stable/generated/xarray.DataTree.html) objects containing integer codes for different labels
- Points: [`dask.DataFrame`](https://docs.dask.org/en/stable/dataframe.html) objects containing point coordinates, (lazy version of [`pandas.DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) objects)
- Shapes: [`geopandas.GeoDataFrame`](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.html) objects containing geometric objects like polygons
- Tables: [`anndata.AnnData`](https://anndata.readthedocs.io/en/stable/generated/anndata.AnnData.html) objects for tabular data with annotations

<!-- markdown cell 102 -->
<a id = code-cell></a>

## Code cell 103

```python
sdata["raw_image"]
```

<!-- markdown cell 104 -->
Images can have multiple scales, which are stored in a pyramid for downsampled representations useful for more efficient visualization and analysis. 
We can access a single scale using the `get_pyramid_levels` function, where `0` is the highest resolution, `1` is downsampled by a factor of (usually 2), `2` is downsampled by another factor (usually 2, with respect to the previous scale), etc.

In this case, our image has 2 scales (check out groups of the output from the code cell [above](https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/introduction/code-cell)). Let's access the highest resolution image.

## Code cell 105

```python
sd.get_pyramid_levels(sdata["raw_image"], n=1)
```

<!-- markdown cell 106 -->
To view image properties such as axes and channel names, `SpatialData` provides some helper functions.
More helper functions can be found in the [API](https://spatialdata.scverse.org/en/stable/api.html) page.
The axes `x` and `y` represent the two-dimensional plane of the image, while `c` corresponds to the different channels (e.g., wavelength) within the image.

## Code cell 107

```python
sd.models.get_axes_names(sdata["raw_image"])
```

<!-- markdown cell 108 -->
Here we see that our image only has one channel for DAPI staining (highlights nucleus).

## Code cell 109

```python
sd.models.get_channel_names(sdata["raw_image"])
```

<!-- markdown cell 110 -->
Let's use `spatialdata-plot` to show the image (DAPI staining for nuclei).

## Code cell 111

```python
sdata.pl.render_images("raw_image", cmap="gray").pl.show()
```

<!-- markdown cell 112 -->
### Points

Points are represented as `dask.DataFrame` objects containing point coordinates (lazy version of `pandas.DataFrame` objects).
Lazy-loading the `DataFrame` reduces memory usage, as the information is only retrieved from the data file when it is needed and not all at once.
For spatial transcriptomics datasets measuring single-molecules, coordinates are stored in columns `x` and `y` (optionally `z` for 3D) and have an additional column annotating gene identity.

## Code cell 113

```python
sdata["transcripts"]
```

<!-- markdown cell 114 -->
We can easily convert the `dask.DataFrame` to a `pandas.DataFrame` using `.compute()` so it is easier to work with.
Note that this will load the entire object into memory.
If the data is large you can use directly the `dask` APIs for the manipulation of the dataframe.

## Code cell 115

```python
sdata["transcripts"].compute()
```

<!-- markdown cell 116 -->
When visualizing the points, note that plotting backend automatically switches from `matplotlib` to `datashader`.
This ensures performant rendering when the number of points is large.
As you can see below, it will be more useful to plot subsets of transcripts, such as specific genes.

We further plot the transcripts colored by gene.
The `groups` argument can be used to plot transcripts for a subset of genes.

## Code cell 117

```python
sdata.pl.render_points("transcripts").pl.show()
sdata.pl.render_points(
    "transcripts", color="gene", groups="Vwf", palette="red", table_name="table"
).pl.show()
```

<!-- markdown cell 118 -->
### Shapes

Shapes are represented as `geopandas.GeoDataFrame` objects containing geometric objects like polygons.
For a comprehensive guide on working with `geopandas.GeoDataFrame` objects, please refer to the [`geopandas` documentation](https://geopandas.org/en/stable/docs.html).

## Code cell 119

```python
sdata["nucleus_boundaries"]
```

## Code cell 120

```python
sdata.pl.render_shapes("nucleus_boundaries").pl.show()
```

<!-- markdown cell 121 -->
### Tables

Annotated matrices are represented as `anndata.AnnData` objects.
Ingested datasets will usually have a table located at `sdata['table']` for a count/abundance matrix.
This enables downstream analysis with tools like Scanpy, scVI, etc.

For different spatial technologies this quantifies:
- transcriptomics: transcript counts;
- spatial proteomics: marker abundances;
- slide-based assays: spot/grid abundances ([see spatial chapter](https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/spatial/introduction.ipynb)).

## Code cell 122

```python
sdata["table"]
```

<!-- markdown cell 123 -->
Here is an example of plotting numerical information on the cells (_HAL_ gene expression) and of plotting categorical information (cell types).

## Code cell 124

```python
sdata.pl.render_shapes("nucleus_boundaries", color="Hal").pl.show()
sdata.pl.render_shapes("nucleus_boundaries", color="annotation").pl.show()
```

<!-- markdown cell 125 -->
(introduction-advanced-data-structures-and-frameworks-key-takeaway-5)=
## Spatial omics data analysis with Squidpy

<!-- markdown cell 126 -->
Squidpy is a framework to analyze and visualize spatial omics data.
It was published around two years before SpatialData {cite}`Marconato2025, Palla2022`.
This is also why Squidpy was originally built on top of Scanpy and AnnData.
As the scverse ecosystem will gradually transition Squidpy to use SpatialData internally, this only gives a short introduction on how Squidpy uses spatial data.
Check out future changes and tutorials on the documentation of [SpatialData](https://spatialdata.scverse.org/en/stable/index.html) and [Squidpy](https://spatialdata.scverse.org/en/stable/index.html).

<!-- markdown cell 127 -->
### API overview
Squidpy’s API lets you analyze and visualize spatial molecular data. 
Graph (`gr`) handles spatial relationships and interactions, image (`im`) processes and segments tissue images, tools (`tl`) provides spatial analysis, and plotting (`pl`) visualizes data and results. 
Reading (`read`) and datasets (`datasets`) support importing data and example datasets across technologies.

<!-- markdown cell 128 -->
### Installation and importing packages
Squidpy is available on PyPI and Conda. 
It can be installed using either of the following commands.
```bash
pip install squidpy
conda install -c conda-forge squidpy
```

<!-- markdown cell 129 -->
### SpatialData integration
Let`s start by importing Squidpy.

## Code cell 130

```python
import squidpy as sq
```

<!-- markdown cell 131 -->
We can load a Xenium dataset with `lamindb`.

## Code cell 132

```python
sdata = ln.Artifact.get(
    key="introduction/advanced_data_structures_and_frameworks_squidpy.zarr"
).load()
sdata
```

<!-- markdown cell 133 -->
### Squidpy demo

<!-- markdown cell 134 -->
Let's compute a nearest neighbor graph of the spatial coordinates of the xenium dataset.

## Code cell 135

```python
sq.gr.spatial_neighbors(sdata["table"])
```

<!-- markdown cell 136 -->
After that, we can cluster the cells based on gene expression profiles and compute clustering.

## Code cell 137

```python
%%time
sc.pp.pca(sdata["table"])
sc.pp.neighbors(sdata["table"])
sc.tl.leiden(sdata["table"])
```

<!-- markdown cell 138 -->
And run the neighbor enrichment analysis in Squidpy.

## Code cell 139

```python
sq.gr.nhood_enrichment(sdata["table"], cluster_key="leiden")
sq.pl.nhood_enrichment(sdata["table"], cluster_key="leiden", figsize=(5, 5))
```

<!-- markdown cell 140 -->
We can finally visualize the results in spatial coordinates both with Squidpy as well as with the novel plotting function in SpatialData.

## Code cell 141

```python
%%time
sq.pl.spatial_scatter(sdata["table"], shape=None, color="leiden")
```

<!-- markdown cell 142 -->
## Questions
### Flipcards

## Code cell 143

```python
%run ../src/lib.py

flip_card(
    "q1",
    "What problem does MuData solve?",
    "MuData stores and organizes multimodal single-cell data in a single container, enabling joint analysis of multiple modalities (e.g., RNA + ATAC) while keeping them linked.",
)

flip_card(
    "q2",
    "How does Muon relate to MuData?",
    "Muon is the analysis framework built on top of MuData, providing methods for multimodal integration, processing, and visualization.",
)

flip_card(
    "q3",
    "What is the main purpose of Squidpy?",
    "Squidpy is a tool to analyze and visualize spatial omics data.",
)
```

<!-- markdown cell 144 -->
### Multiple-choice questions

## Code cell 145

```python
%run ../src/lib.py

multiple_choice_question(
    question_id="q4",
    question="How would you access RNA data in a MuData object `mdata`?",
    options=[
        "mdata.rna",
        "mdata.obs['rna']",
        "mdata.mod['rna']",
        "mdata.uns['rna']",
    ],
    correct_answer="mdata.mod['rna']",
    explanations={
        "mdata.rna": "MuData does not provide direct attributes for modalities. They are stored in `mod`.",
        "mdata.obs['rna']": "`obs` stores cell-level metadata, not modality data.",
        "mdata.uns['rna']": "`uns` stores unstructured metadata, not the modality matrix.",
    },
)

multiple_choice_question(
    question_id="q5",
    question="In a SpatialData object, where are the X/Y coordinates of a table (AnnData object) stored?",
    options=[
        ".var",
        ".obs",
        ".obsm['spatial']",
        ".layers['spatial']",
    ],
    correct_answer=".obsm['spatial']",
    explanations={
        ".var": "`.var` contains gene-level metadata, not spatial coordinates.",
        ".obs": "`.obs` contains cell-level metadata but not coordinate arrays.",
        ".layers['spatial']": "`.layers` can store alternate matrices, but spatial coordinates are in `.obsm`.",
    },
)

multiple_choice_question(
    question_id="q6",
    question="SpatialData differs from AnnData because it:",
    options=[
        "Replaces gene expression matrices",
        "Stores only image data",
        "Integrates spatial elements like images and geometries",
        "Works only with multimodal sequencing",
    ],
    correct_answer="Integrates spatial elements like images and geometries",
    explanations={
        "Replaces gene expression matrices": "SpatialData still supports expression matrices. It does not replace them.",
        "Stores only image data": "SpatialData can store images, but also tables and coordinates.",
        "Works only with multimodal sequencing": "SpatialData is not restricted to multimodal sequencing. It adds spatial context.",
    },
)
```

<!-- markdown cell 146 -->
## References

<!-- markdown cell 147 -->
```{bibliography}
:filter: docname in docnames
:labelprefix: at
```

<!-- markdown cell 148 -->
## Contributors

We gratefully acknowledge the contributions of:

### Authors

* Lukas Heumos
* Luis Heinzlmeier

### Reviewers

* Isaac Virshup
