# Auto-generated from single-cell-best-practices.
# Title: Clustering
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/cellular_structure/clustering.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# (cellular-structure:clustering)=
# # Clustering

# %% [markdown]
# (cellular-structure-clustering-key-takeaway-1)=
# (cellular-structure-clustering-key-takeaway-2)=
# ## Motivation

# %% [markdown]
# Preprocessing and visualization enabled us to describe our scRNA-seq dataset and reduce its dimensionality.
# Up to this point, we embedded and visualized cells to understand the underlying properties of our dataset.
# However, they are still rather abstractly defined.
# The next natural step in single-cell analysis is the identification of cellular structure in the dataset. 
# 
# In scRNA-seq data analysis, we describe cellular structure in our dataset by finding cell identities that relate to known cell states or cell cycle stages.
# This process is usually called cell identity annotation.
# For this purpose, we structure cells into clusters to infer the identity of similar cells. Clustering itself is a common unsupervised machine learning problem. 
# We can derive clusters by minimizing the intra-cluster distance in the reduced expression space.
# In this case, the expression space determines the gene expression similarity of cells with respect to a dimensionality-reduced representation.
# This lower-dimensional representation is, for example, determined with a principal-component analysis, and the similarity scoring is then based on Euclidean distances. 
# 
# The KNN(K-Nearest-Neighbor) graph consists of nodes reflecting the cells in the dataset.
# We first calculate a Euclidean distance matrix on the PC-reduced expression space for all cells and then connect each cell to its K most similar cells.
# Usually, `K` is set to values between 5 and 100, depending on the size of the dataset.
# The KNN graph reflects the underlying topology of the expression data by representing dense regions with respect to expression space, as well as as densely connected regions in the graph {cite}`wolf_paga_2019`.
# Dense regions in the KNN-graph are detected by community detection methods like Leiden and Louvain{cite}`blondel_fast_2008`. 
# 
# ```{admonition} PC-reduced expression space
# :class: dropdown
# PC-reduced expression space refers to the lower-dimensional space obtained after using Principal Component Analysis (PCA) to high-dimensional gene expression data. After PCA, for example, we are working with the top 10-50 principal components instead of 20,000 genes.
# ```
# 
# The Leiden algorithm is an improved version of the Louvain algorithm, which outperformed other clustering methods for single-cell RNA-seq data analysis ({cite}`du_systematic_2018, freytag_comparison_2018, weber_comparison_2016`).
# Since the Louvain algorithm is no longer maintained, using Leiden instead is preferred. 
# 
# We, therefore, propose to use the Leiden algorithm{cite}`traag_louvain_2019` on single-cell k-nearest-neighbour (KNN) graphs to cluster single-cell datasets. 
# 
# Leiden creates clusters by taking into account the number of links between cells in a cluster versus the overall expected number of links in the dataset. 
# 
# :::{figure-md} clustering
# 
# <img src="../_static/images/clustering/clustering.jpeg" alt="Clustering Overview" class="bg-primary mb-1" width="800px">
# 
# The Leiden algorithm computes a clustering on a KNN graph obtained from the PC reduced expression space.
# The starting point is a singleton partition in which each node functions as its own community.
# As a next step, the algorithm creates partitions by moving individual nodes from one community to another, which is refined afterwards to enhance the partitioning.
# The refined partition is then aggregated to a network.
# Subsequently, the algorithm moves again individual nodes in the aggregate network, until refinement no longer changes the partition.
# All steps are repeated until the final clustering is created and partitions no longer change.
# 
# :::
# 
# 
# The Leiden module has a resolution parameter that allows for determining the scale of the partition cluster and therefore the coarseness of the clustering.
# A higher resolution parameter leads to more clusters.
# The algorithm additionally allows efficient sub-clustering of particular clusters in the dataset by sub-setting the KNN graph.
# Sub-clustering enables the user to identify cell-type specific states within clusters or a finer cell type labeling{cite}`wagner_revealing_2016`, but can also lead to patterns that are only due to noise present in the data.
# 
# As mentioned before, the Leiden algorithm is implemented in scanpy.

# %% [markdown]
# ```{admonition} Running this on a GPU
# :class: tip, dropdown
# Leiden clustering on a million-cell graph is one of the worst CPU bottlenecks in a typical pipeline and one of the best GPU wins.
# [rapids-singlecell](../introduction/rapids_singlecell.ipynb) provides `rsc.tl.leiden` with the same signature and routinely runs 50–100× faster than the CPU implementation.
# ```

# %%
# Upstream code cell: 5
import lamindb as ln
import scanpy as sc

assert ln.setup.settings.instance.slug == "theislab/sc-best-practices"

ln.track("rJhR7SskiROg")

# Configuring scanpy's settings for outfits and visualization
sc.settings.verbosity = 0
sc.settings.set_figure_params(dpi=80, facecolor="white", frameon=False)

# %% [markdown]
# ## Clustering human bone marrow cells

# %% [markdown]
# Firstly, we load our dataset.
# We perform clustering on the preprocessed sample `site4-donor8` from the NeurIPS human bone marrow dataset, which we already preprocessed and uploaded to our `LaminDB`.  
# 
# This dataset was normalized with scran.

# %%
# Upstream code cell: 8
af = ln.Artifact.get(key="cellular_structure/s4d8_subset.h5ad", is_latest=True)
adata = af.load()

# %% [markdown]
# The Leiden algorithm leverages a KNN graph on the reduced expression space.
# We can calculate the KNN graph on a lower-dimensional gene expression representation with the scanpy function `sc.pp.neighbors`.
# We call this function on the top 30 principal-components as these capture most of the variance in the dataset.
# Visualizing the clustering can help us to understand the results, we therefore embed our cells into a UMAP embedding.
# More details can be found in the [dimensionality reduction chapter](../preprocessing_visualization/dimensionality_reduction.ipynb).

# %%
# Upstream code cell: 10
sc.pp.neighbors(adata, n_pcs=30)
sc.tl.umap(adata)

# %% [markdown]
# We can now call the Leiden algorithm.

# %%
# Upstream code cell: 12
sc.tl.leiden(adata, flavor="igraph", n_iterations=2)

# %% [markdown]
# ```{admonition} Optimizing Leiden Iterations
# :class: dropdown
# The `n_iterations` parameter in `sc.tl.leiden()` determines how many refinement passes the algorithm performs to optimize its community detection.
# 
# * **`n_iterations = 2` (Recommended):** The standard choice for most analyses.
# It offers a significant boost in cluster quality over the Louvain algorithm while remaining computationally efficient.
# * **`n_iterations = -1` (Optimal):** Forces the algorithm to run until it reaches full convergence.
# While this produces the "perfect" mathematical clustering, it can be significantly slower on large datasets.
# * **`n_iterations > 2`:** Allows you to specify a fixed number of passes to balance precision and speed.
# 
# **Tip:** Even at 2 iterations, Leiden effectively prevents the "disconnected clusters" issue often found in older methods.
# ```

# %% [markdown]
# In scanpy, the resolution parameter is used in clustering methods, such as the Louvain or Leiden methods.
# It controls the granularity or coarseness of the resulting clusters.
# The default resolution parameter in scanpy is 1.0.
# However, in many cases the analyst may want to try different resolution parameters to control the coarseness of the clustering.
# Hence, we recommend to save the clustering result under a specified key which indicates the selected resolution.

# %%
# Upstream code cell: 15
sc.tl.leiden(
    adata, key_added="leiden_res0_25", resolution=0.25, flavor="igraph", n_iterations=2
)
sc.tl.leiden(
    adata, key_added="leiden_res0_5", resolution=0.5, flavor="igraph", n_iterations=2
)
sc.tl.leiden(
    adata, key_added="leiden_res1", resolution=1.0, flavor="igraph", n_iterations=2
)

# %% [markdown]
# We now visualize the different clustering results obtained with the Leiden algorithm at different resolutions.
# As we can see, the resolution heavily influences how coarse our clustering is.
# Higher resolution parameters lead to more communities, i.e., more identified clusters, while lower resolution parameters lead to fewer communities.
# You can think of it like zooming, where we take a closer look at the clusters with higher resolution.
# The resolution parameter, therefore, controls how densely clustered regions in the KNN-embedding are grouped together by the algorithm.
# This will become especially important for annotating the clusters.

# %%
# Upstream code cell: 17
sc.pl.umap(
    adata,
    color=["leiden_res0_25", "leiden_res0_5", "leiden_res1"],
    legend_loc="on data",
)

# %% [markdown]
# We now clearly inspect the impact of different resolutions on the clustering result.
# For a resolution of 0.25, the clustering is much coarser, and the algorithm detected fewer communities.
# Additionally, clustered regions are less dense compared to the clustering obtained at a resolution of 1.0. 
# 
# We would like to highlight again that distances between the displayed clusters must be interpreted with caution.
# As the UMAP embedding is in 2D, distances are not necessarily captured well between all points.
# We recommend not interpreting distances between clusters visualized on UMAP embeddings.

# %% [markdown]
# As usual, we will upload the processed anndata to `lamindb`.
# You can skip this part.

# %%
# Upstream code cell: 20
af = ln.Artifact.from_anndata(
    adata,
    key="cellular_structure/s4d8_clustered.h5ad",
    description="anndata after clustering",
).save()
af

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
# * Anna Schaar
# * Seo H. Kim
# 
# ### Reviewers
# 
# * Lukas Heumos
