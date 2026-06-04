# Auto-generated from single-cell-best-practices.
# Title: Perturbation modeling
# Upstream: https://github.com/theislab/single-cell-best-practices/blob/735f26fd270b3beceb4ba79f4a556c912192fe83/jupyter-book/conditions/perturbation_modeling.ipynb
# Run with IPython/Jupyter when cells contain magics or shell commands.

# %% [markdown]
# # Perturbation modeling

# %% [markdown]
# ## Motivation

# %% [markdown]
# Advances in single-cell experimental protocols allow for massively multiplexed experiments to measure hundreds of thousands of cells under thousands of unique conditions.
# These are commonly termed "perturbations", which are temporary or permanent changes caused by an external influence {cite}`srivatsan2020`. Recently, such technologies have been adapted to profile CRISPR-Cas9 with multimodal readouts {cite}`Papalexi2021,frangieh2021`, genome-wide perturbations {cite}`replogle2021`, and combinatorial perturbations {cite}`wessels2022`. Despite experimental advances, exploring the massive perturbation space of combinatorial gene knock-outs or drug combinations remains challenging. The vast exploration space motivated the development of computational approaches for modeling single-cell perturbation responses {cite}`ji2021`.
# 
# Perturbation modeling entails areas{cite}`ji2021`:
# 
# 1. **Perturbation responses**: Predicting omics signatures after a perturbation given information about the control and treatment conditions. Predictions can be evaluated by the correlation of predicted features with respect to the true values. It is further possible to predict phenotypic measurements such as IC50 values, area under the dose response curve, toxicity and viability.
# 2. **Targets and mechanisms**: Predicting targets and mechanisms of perturbation using omics measurements. Drug mode of actions can be identified with perturbation modeling even for uncharacterized compounds.
# 3. **Perturbation interactions**: Predicting combinatorial effects of perturbations to gain an understanding of interlinked effects between genetics and drugs or combinations of drugs.
# 4. **Chemical properties**: Predicting chemical properties of perturbations using omics measurements such as molecular fingerprints, R groups, pharmacophores or even complete compounds.
# 
# Robust and accessible tooling for all of these steps is still under development. Hence, we will solely introduce three approaches for a subset of these tasks that can be tackled with single-cell perturbation data in the following sections:
# 
# 1. Finding the cell types that were most affected by perturbations using [Augur](https://github.com/neurorestore/Augur) applied to Kang 2018 {cite}`pemo:kang2018`.
# 2. Predicting the transcriptional response of single cells to perturbations using [scGen](https://github.com/theislab/scgen) applied to Kang 2018 {cite}`pemo:kang2018`.
# 3. Quantifying the sensitivity of genetic CRISPR perturbations using [Mixscape](https://github.com/satijalab/seurat/blob/master/R/mixscape.R) applied to Papalexi 2021 {cite}`Papalexi2021`.

# %% [markdown]
# (conditions-perturbation-modeling-key-takeaway-1)=
# ## Identifying the cell types most affected by perturbations

# %% [markdown]
# ### Motivation

# %% [markdown]
# Perturbations rarely have the same effect on all cells. In particular, different cell types or cells in different states in their cell cycle can be affected to varying degrees. Here we will leverage [Augur](https://github.com/neurorestore/Augur) by Skinnider et al. {cite}`Skinnider2021,Squair2021Augur`, which provides one way of quantifying the degree of response, for this purpose.

# %% [markdown]
# ```{admonition} Augur model
# 
# Augur aims to rank or prioritize cell types according to their response to experimental perturbations given single-cell gene expression data. The basic idea is that in the space of molecular measurements, cells reacting heavily to induced perturbations are more easily separated into perturbed and unperturbed groups than cell types with little or no response. This separability is quantified by measuring how well experimental labels (for example, treatment and control) can be predicted within each cell type. Augur trains a machine learning model predicting experimental labels for each cell type in multiple cross-validation runs and then prioritizes cell type response according to metric scores measuring the accuracy of the model. For categorical data the area under the curve is the default metric and for numerical data the concordance correlation coefficient is used as a proxy for model accuracy, which in turn approximates perturbation response.
# ```

# %% [markdown]
# ### Limitations of Augur

# %% [markdown]
# Since Augur determines the degree of perturbation responses, it requires distinct cell types. If cell type labeling is challenging due to ongoing continuous, smooth processes or trajectories of gene expression such as cell differentiation, Augur might not allow for fine-grained enough rankings. Constructing a clustering tree describing the relationships of different clusters, which were used for cell type annotation, and applying Augur to all possible clustering resolutions, could determine the most suitable resolution and therefore annotation for the perturbation of interest {cite}`Squair2021Augur`.

# %% [markdown]
# Further, cell types mediating tissue- or organism-level responses to specific perturbations might themselves comprise subpopulations of responder and non-responder cells. The assignment of cells into responder and non-responder cells itself can be inaccurate because cells of a given cell type could fall along a continuous trajectory of perturbation response intensity. However, Augur does not decipher the individual cells' perturbation responses and simply aggregates them as averages for the cell types {cite}`pemo:Squair2021`.

# %% [markdown]
# Some perturbation effects might originate primarily from a change in relative abundance of a particular cell type. The subsampling procedure in Augur, however, discards any information about the relative abundances. In fact, Augur samples equal numbers of cells from each condition prior to cross-validation. Any change in the abundance of a particular cell type could be accompanied by changes in the intrinsic transcriptional profile of that cell type. Strong perturbations could even lead to scenarios where specific cell types are depleted completely or suddenly arise only when perturbed. Hence, it is advisable to perform differential abundance tests for every cell type to help contextualize the Augur analysis results {cite}`Squair2021Augur`.

# %% [markdown]
# Here, we will use a fast reimplementation of the original R implementation of [Augur](https://github.com/neurorestore/Augur) using the perturbation analysis toolbox [pertpy](https://github.com/theislab/pertpy/). pertpy leverages the scverse ecosystem and is therefore fully compatible with `AnnData` in the Python ecosystem.

# %% [markdown]
# ### Predicting cell type prioritization for IFN-β stimulation

# %% [markdown]
# To demonstrate Augur, we will use the Kang dataset, which is a 10x droplet-based scRNA-seq peripheral blood mononuclear cell (PBMC) dataset from 8 Lupus patients before and after 6h-treatment with INF-β (16 samples in total){cite}`pemo:kang2018`. 
# 
# Our goal here is to decipher which cell types were most affected by INF-β treatment.

# %% [markdown]
# First, we import pertpy and scanpy.

# %%
# Upstream code cell: 16
import warnings

warnings.filterwarnings("ignore")
warnings.simplefilter("ignore")

# This is required to catch warnings when the multiprocessing module is used
import os

os.environ["PYTHONWARNINGS"] = "ignore"

# %%
# Upstream code cell: 17
import pertpy as pt
import scanpy as sc

# %% [markdown]
# pertpy provides a convenient data loader to access the Kang dataset.

# %%
# Upstream code cell: 19
adata = pt.dt.kang_2018()

# %% [markdown]
# We rename `label` to `condition` and the conditions themselves for improved readability.

# %%
# Upstream code cell: 21
adata.obs.rename({"label": "condition"}, axis=1, inplace=True)
adata.obs["condition"].replace({"ctrl": "control", "stim": "stimulated"}, inplace=True)

# %% [markdown]
# This dataset contains PBMCs {cite}`pemo:kang2018` across seven different cell-types.

# %%
# Upstream code cell: 23
adata.obs.cell_type.value_counts()

# %% [markdown]
# We now create an Augur object using pertpy based on our estimator of interest to measure how predictable the perturbation labels for each cell type in the dataset are. The options for the estimator are `random_forest_classifier` or `logistic_regression_classifier` for categorical data and `random_forest_regressor` for numerical data. All estimators make use of a `Params` class to define further parameters. Here, we will use a `random_forest_classifier` which is generally a solid and fast choice and suits our categorical data.

# %%
# Upstream code cell: 25
ag_rfc = pt.tl.Augur("random_forest_classifier")

# %% [markdown]
# Next, we need to load the AnnData object into a format that Augur is comfortable with. This can be easily done with the [load](https://pertpy.readthedocs.io/en/development/usage/tools/pertpy.tools.Augur.html#load) function of our Augur object.

# %%
# Upstream code cell: 27
loaded_data = ag_rfc.load(adata, label_col="condition", cell_type_col="cell_type")
loaded_data

# %% [markdown]
# This allows us to run Augur with the `predict` function. Generally, Augur can be run in two modes: 
# 
# 1. A feature selection based on the original Augur implementation (`select_variance_feature=True`) that is also the default. This approach removes features with little cell-to-cell variation within that cell type. We refer to the Augur Nature Protocols paper for more details{cite}`Squair2021Augur`. When this feature selection is chosen the results are very similar to the Augur implementation in R.
# 2. A feature selection based on `scanpy.pp.highly_variable_genes`. This feature selection reduces the number of genes that are taken into account for model training and might result in inflated Augur scores, because the highly variable genes are very useful to separate cell types. However, this mode is faster and recovers effects of perturbations on cell types very well. We recommend it for very large datasets with perturbations that are expected to have a strong effect on specific cell types.

# %% [markdown]
# Since we do not expect INF-β to have an exceptional effect on specific cell types, we run Augur with the original Augur feature selection. To further increase the resolution, we set the `subsample_size` to 20 (default: 50) which corresponds to the number of cells to randomly draw per cell type.

# %%
# Upstream code cell: 30
v_adata, v_results = ag_rfc.predict(
    loaded_data, subsample_size=20, n_threads=4, select_variance_features=True, span=1
)

v_results["summary_metrics"]

# %% [markdown]
# The result table contains several evaluation metrics for the fitted model. For the interpretation of the cell type prioritization of the IFN-β response, only the `mean_augur_score` is relevant, which corresponds to the `mean_auc`. The higher the value, the easier it is for the fitted model to discern between control and perturbed cell states. Hence, the perturbation effect was stronger for this cell type. Let's visualize this effect.

# %%
# Upstream code cell: 32
lollipop = ag_rfc.plot_lollipop(v_results)

# %% [markdown]
# As observed, CD14+ Monocytes were the most affected by IFN-β whereas Megakaryocytes were the least affected. This corresponds roughly to the number of {term}`differentially expressed genes <Differential gene expression (DGE)>` in the original publication for the respective cell types {cite}`pemo:kang2018`.

# %% [markdown]
# The corresponding `mean_augur_score` is also saved in `v_adata.obs` and can be plotted in a UMAP.

# %%
# Upstream code cell: 35
sc.pp.neighbors(v_adata)
sc.tl.umap(v_adata)

# %%
# Upstream code cell: 36
sc.pl.umap(adata=v_adata, color=["augur_score", "cell_type", "label"])

# %% [markdown]
# ### Determining the most important genes for the prioritization

# %% [markdown]
# The genes that contribute the most to the prioritization, as reflected by the augur score, correspond to the feature importances of our model. These feature importances are saved in the results object and can be easily plotted.

# %%
# Upstream code cell: 39
important_features = ag_rfc.plot_important_features(v_results)

# %% [markdown]
# These genes could now be further explored concerning, for example, their role in pathways or other gene sets. However, since Augur performs inference on the cell type level, it does not directly determine the individual genes that are involved in the perturbation response. The authors of Augur themselves suggest using differential gene expression tests to be both conceptually and pragmatically a more appropriate approach to the inference at the level of individual genes {cite}`Squair2021Augur`.

# %% [markdown]
# ### Differential prioritization

# %% [markdown]
# Augur is also able to perform differential prioritization by executing a permutation test to identify cell types with statistically significant differences in area under the curve (AUC) between two different rounds of cell type prioritization (for example a response to drugs A and B compared to untreated control).
# 
# Bhattacherjee et al. offered mice cocaine, and took samples of the prefrontal cortex for scRNA-seq at 48 hours and 15 days post withdrawal{cite}`Bhattacherjee2019`.
# 
# We will now evaluate the effect of the `withdraw_15d_Cocaine` and `withdraw_48h_Cocaine` conditions compared to `Maintenance_Cocaine`. Basically, differential prioritization is obtained through a [permutation test](https://en.wikipedia.org/wiki/Permutation_test) of the difference in AUC between two sets of cell-type prioritizations, compared with the expected AUC difference between the same two prioritizations after random permutation of sample labels{cite}`Squair2021Augur`. In this procedure, the user first performs cell-type prioritization on drug A (`withdraw_15d_Cocaine`) and drug B (`withdraw_48h_Cocaine`) separately, then calculates the AUC difference between drug A and drug B. To compute the statistical significance of the AUC difference , an empirical null distribution of AUC differences is then calculated for each cell type by permuting the sample labels, then repeating cell-type prioritization in the permuted data. Permutation P-values are then calculated. This procedure thus enables the identification of statistically significant differences in cell-type prioritization between conditions, as well as the condition in which the cell type is more transcriptionally separable.

# %% [markdown]
# Each variation is run once in `default` mode and once in `permute` mode to allow us to perform the [permutation test](https://en.wikipedia.org/wiki/Permutation_test). As a first step, we fetch the `bhattacherjee` dataset using pertpy and create an Augur object that again uses a random forest classifier.

# %%
# Upstream code cell: 44
bhattacherjee_adata = pt.dt.bhattacherjee()
ag_rfc = pt.tl.Augur("random_forest_classifier")

# %% [markdown]
# Next, we run Augur on `Maintenance_Cocaine` and `withdraw_15d_Cocaine` using both `augur_mode=default` and `augur_mode=permute` as previously described. Note that we log normalize the dataset for a simple normalization.

# %%
# Upstream code cell: 46
sc.pp.log1p(bhattacherjee_adata)

# %%
# Upstream code cell: 47
# Default mode
bhattacherjee_15 = ag_rfc.load(
    bhattacherjee_adata,
    condition_label="Maintenance_Cocaine",
    treatment_label="withdraw_15d_Cocaine",
)

bhattacherjee_adata_15, bhattacherjee_results_15 = ag_rfc.predict(
    bhattacherjee_15, random_state=None, n_threads=4
)
bhattacherjee_results_15["summary_metrics"].loc["mean_augur_score"].sort_values(
    ascending=False
)

# %%
# Upstream code cell: 48
# Permute mode
bhattacherjee_adata_15_permute, bhattacherjee_results_15_permute = ag_rfc.predict(
    bhattacherjee_15,
    augur_mode="permute",
    n_subsamples=100,
    random_state=None,
    n_threads=4,
)

# %% [markdown]
# Now let's do the same for `Maintenance_Cocaine` and `withdraw_48h_Cocaine`.

# %%
# Upstream code cell: 50
# Default mode
bhattacherjee_48 = ag_rfc.load(
    bhattacherjee_adata,
    condition_label="Maintenance_Cocaine",
    treatment_label="withdraw_48h_Cocaine",
)

bhattacherjee_adata_48, bhattacherjee_results_48 = ag_rfc.predict(
    bhattacherjee_48, random_state=None, n_threads=4
)

bhattacherjee_results_48["summary_metrics"].loc["mean_augur_score"].sort_values(
    ascending=False
)

# %%
# Upstream code cell: 51
# Permute mode
bhattacherjee_adata_48_permute, bhattacherjee_results_48_permute = ag_rfc.predict(
    bhattacherjee_48,
    augur_mode="permute",
    n_subsamples=100,
    random_state=None,
    n_threads=4,
)

# %% [markdown]
# This allows us to take a look at the augur scores of the two runs in a scatterplot. The diagonal line is the identity function. If the values were the same they would be on the line.

# %%
# Upstream code cell: 53
scatter = ag_rfc.plot_scatterplot(bhattacherjee_results_15, bhattacherjee_results_48)

# %% [markdown]
# To figure out which cell type was most affected when comparing `withdraw_48h_Cocaine` and `withdraw_15d_Cocaine` we can run differential prioritization.

# %%
# Upstream code cell: 55
pvals = ag_rfc.predict_differential_prioritization(
    augur_results1=bhattacherjee_results_15,
    augur_results2=bhattacherjee_results_48,
    permuted_results1=bhattacherjee_results_15_permute,
    permuted_results2=bhattacherjee_results_48_permute,
)
pvals

# %% [markdown]
# The p-value, following the R Augur implementation is calculated using `b`, the number of times permuted values are larger than original values and `m`, the number of permutations run. Since `b` is the same for all cells but Microglia, the p-value is the same for these as well.

# %%
# Upstream code cell: 57
diff = ag_rfc.plot_dp_scatter(pvals)

# %% [markdown]
# In this case the cell type "Inhibitory" is not very different between the two compared cell types which may indicate that permanent damage was inflicted.

# %% [markdown]
# (conditions-perturbation-modeling-key-takeaway-2)=
# ## Predicting IFN-β response for CD4-T cells

# %% [markdown]
# Many perturbation response modeling methods aim to forecast transcriptomic responses to stimuli, be it drugs, genetic knock-outs, or disease, for unseen populations where the perturbation response has not been measured, to help facilitate experimental design and hypothesis generation. The failure to capture cells treated with a perturbation could happen when a specific population could not be measured due to experimental or sample failure (e.g., failed cell sorting), high experimental costs prohibiting exploring all possibilities, and rare frequency of discovery for some cell types. In all scenarios above, an in-silico prediction of the missing population can lead to an informed decision about conducting new experiments or not.

# %% [markdown]
# Multiple methods for perturbation response modeling have been developed based on autoencoders (AE){cite}`lotfollahi2019,lotfollahi2020,lotfollahi2021,russkikh2020,yuan2021,amodio2018,wei2022`, a deep learning architecture to learn a low-dimensional representation of the data.

# %% [markdown]
# ```{admonition} Variational autoencoders
# 
# The fundamental principle of autoencoders is that they are composed of two parts, an encoder and a decoder. The encoder tries to learn a latent space of the input data (usually gene expression) which can be decoded with minimal reconstruction error by the decoder. The latent space is usually of a lower dimension than the input space.
# An extension of AEs are variational autoencoders (VAE) that address the issue of non-regularized latent spaces of AEs by providing generative capability to the entire space. A non-regularized latent space only really provides strong sampling capability for the distinct classes that formed clusters. The famous MNIST dataset of handwritten digits would only allow the sampling of the digits 0-9 in any of the determined 10 clusters. However, it would result in garbage input if sampling were attempted outside the clusters. Whereas, the encoder in AEs outputs latent vectors, the encoder in VAEs outputs parameters of a pre-defined distribution in the latent space for every input. The latent space gets regularized by the VAE enforcing a normally distributed latent distribution.
# ```

# %% [markdown]
# 
# Here, we demonstrate the application of scGen {cite}`lotfollahi2019`, a variational autoencoder combined with vector arithmetics. The model learns a latent representation of the data in which it estimates a difference vector between control (untreated) and perturbed (treated) cells. The estimated difference vector is then added to control cells for the cell type or population of interest to predict the gene expression response for each single cell. Here, we apply scGen to predict the response to IFN-β for a population of CD4-T cells that are artificially held out (unseen) during training to simulate one of the aforementioned real-world scenarios. We again leverage a dataset that contains peripheral blood mononuclear cells (PBMCs) from eight patients with Lupus treated with IFN-β or left untreated from {cite}`pemo:kang2018` across seven different cell-types.
# 
# As a first step, we import `scanpy` and `scgen` to allow us to work with AnnData objects and employ scGen.

# %%
# Upstream code cell: 64
import pertpy as pt
import scanpy as sc

# %% [markdown]
# ### Setting up the Kang dataset for scGen

# %% [markdown]
# We will again use [pertpy](https://github.com/theislab/pertpy/) to get the Kang dataset.

# %%
# Upstream code cell: 67
adata = pt.dt.kang_2018()

# %% [markdown]
# scGen works best with log transformed data. Highly variable gene selection can speed up computations due to the reduced feature space.

# %%
# Upstream code cell: 69
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata)

# %% [markdown]
# We rename `label` to `condition` and the conditions themselves for improved readability.

# %%
# Upstream code cell: 71
adata.obs.rename({"label": "condition"}, axis=1, inplace=True)
adata.obs["condition"].replace({"ctrl": "control", "stim": "stimulated"}, inplace=True)

# %% [markdown]
# This dataset contains PBMCs {cite}`pemo:kang2018` across seven different cell-types.

# %%
# Upstream code cell: 73
adata.obs.cell_type.value_counts()

# %% [markdown]
# We remove all CD4T cells from the training data (`adata_t`) to simulate a real-world scenario of not capturing a specific population during an experiment.

# %%
# Upstream code cell: 75
adata_t = adata[
    ~(
        (adata.obs["cell_type"] == "CD4 T cells")
        & (adata.obs["condition"] == "stimulated")
    )
].copy()

cd4t_stim = adata[
    (
        (adata.obs["cell_type"] == "CD4 T cells")
        & (adata.obs["condition"] == "stimulated")
    )
].copy()

# %% [markdown]
# scGen requires the data to be in a particular format which is facilitated through `AnnData` and the `setup_anndata` function. It requires the key of the sample, the `batch_key` (in our case, `"condition"`) and the cell type label key, the `labels_key` (`"cell_type"`).

# %%
# Upstream code cell: 77
pt.tl.SCGEN.setup_anndata(adata_t, batch_key="condition", labels_key="cell_type")

# %% [markdown]
# ### Model construction and training

# %% [markdown]
# scGen requires the modified `AnnData` object (`adata_t`) to construct the model object, which can be used to train the model. This function receives multiple user inputs, including the number of nodes in each hidden layer (`n_hidden`) of the model before the bottleneck layer (the middle layer of the network) and also the number of such layers (`n_layers`). Additionally, the user can adapt the dimension of the bottleneck layer, which is used to calculate the difference vector between perturbed cells and control cells. The default parameters used here are taken from the original publication. In practice, wider hidden layers lead to better reconstruction accuracy, which is essential for our aim to predict the perturbation response across many genes.

# %%
# Upstream code cell: 80
model = pt.tl.SCGEN(adata_t, n_hidden=800, n_latent=100, n_layers=2)

# %% [markdown]
# scGen is a neural network with thousands of parameters to learn a low-dimensional data representation. Here, we use `train` method to estimate these parameters using the training data. There are multiple parameters here, `max_epochs` is the maximum number of iterations the model is allowed to update its parameters which are set to 100 here. The higher values training epochs will take more computation time but might help better results. The `batch_size` is the number of samples (individual cells) the model sees to update its parameters. Lower numbers usually lead to better results in the case of scGen. Finally, there is `early_stopping`, which enables the model to stop the training if its results are not improved after `early_stopping_patience` training epochs. The early stopping mechanism prevents potential overfitting of the training data, which can lead to poor generalization to unseen populations.

# %%
# Upstream code cell: 82
model.train(
    max_epochs=100, batch_size=32, early_stopping=True, early_stopping_patience=25
)

# %% [markdown]
# To visualize the learned representation of data by the model, we plot the latent representation of the model using the UMAP algorithm. The `get_latent_representation()`  returns a 100-dimensional vector for each cell. We store the latent representations in the `.obsm` slot of the AnnData object.

# %%
# Upstream code cell: 84
adata_t.obsm["scgen"] = model.get_latent_representation()

# %% [markdown]
# Next, we recalculate the neighbors graph and the UMAP embedding using the calculated latent representation to finally visualize the new embedding in a UMAP plot.

# %%
# Upstream code cell: 86
sc.pp.neighbors(adata_t, use_rep="scgen")
sc.tl.umap(adata_t)

# %%
# Upstream code cell: 87
sc.pl.umap(adata_t, color=["condition", "cell_type"], wspace=0.4, frameon=False)

# %% [markdown]
# As observed above, the IFN-β stimulation induced strong transcriptional changes across all cell-types

# %% [markdown]
# ### Predicting CD4T responses to IFN-β stimulation

# %% [markdown]
# After the model is trained, we can ask the model to simulate the effect of IFN-β response for each control CD4T cell present in the training data. The prediction is made possible via the `predict` method, which receives the corresponding labels (`ctrl_key` and `stim_key` below) in the `condition` (as provided earlier by the user) column of the `AnnData` object to estimate a global difference vector in the latent space between 'control' and 'stimulated' cells. This vector is then added to each single-cell present specified in `celltype_to_predict` (here CD4T).

# %%
# Upstream code cell: 91
pred, delta = model.predict(
    ctrl_key="control", stim_key="stimulated", celltype_to_predict="CD4 T cells"
)

# we annotate the predicted cells to distinguish them later from ground truth cells.
pred.obs["condition"] = "predicted stimulated"

# %% [markdown]
# ### Evaluating the predicted IFN-β response

# %% [markdown]
# In previous sections, we predicted the response to IFN-β for each CD4T cell present among the control population. Since single-cell sequencing is destructive, meaning that cells can not be measured before and after a particular perturbation, it is impossible to directly evaluate the prediction for the same cell after IFN-β stimulation. However, we have a group of cells in the data treated with IFN-β, which we can use to measure how well the predicted cell population aligns with ground truth cells. To pursue this, we evaluate predictions qualitatively by looking at the embedding of control, predicted, and actual CD4T IFN-β cells in principal component analysis (PCA) space. Additionally, we also quantitatively measure the correlation between mean gene expression of predicted cells and IFN-β across all genes and differentially expressed genes after IFN-β stimulation.

# %% [markdown]
# First, we construct an `AnnData` object containing control, predicted stimulated, and actual stimulated cells.

# %%
# Upstream code cell: 95
ctrl_adata = adata[
    ((adata.obs["cell_type"] == "CD4 T cells") & (adata.obs["condition"] == "control"))
]
# concatenate pred, control and real CD4 T cells in to one object
eval_adata = ctrl_adata.concatenate(cd4t_stim, pred)

# %%
# Upstream code cell: 96
eval_adata.obs.condition.value_counts()

# %% [markdown]
# We first look at the PCA co-embedding of control, IFN-β stimulated and predicted CD4T cells.

# %%
# Upstream code cell: 98
sc.tl.pca(eval_adata)
sc.pl.pca(eval_adata, color="condition", frameon=False)

# %% [markdown]
# As observed above, the predicted stimulated cells were moved towards the CD4T stimulated cells with IFN-β. Yet we should also look at differentially expressed genes (DEGs) to verify whether the most striking DE genes are also present in the predicted stimulated cells. Below, we look at the overall mean correlation between predicted and real cells. Before that, we extract DEGs between control and stimulated cells:

# %%
# Upstream code cell: 100
cd4t_adata = adata[adata.obs["cell_type"] == "CD4 T cells"]

# %% [markdown]
# We estimate DEGs using scanpy's implementation of the Wilcoxon test.

# %%
# Upstream code cell: 102
sc.tl.rank_genes_groups(cd4t_adata, groupby="condition", method="wilcoxon")
diff_genes = cd4t_adata.uns["rank_genes_groups"]["names"]["stimulated"]
diff_genes

# %% [markdown]
# scGen features a `reg_mean_plot` that calculates the R² correlation between mean gene expression of predicted and existing IFN-β cells. The higher the R² (max is 1), the more faithful is the prediction compared to the ground truths. The highlighted genes in red are the top 10 upregulated DEGs after IFN-β stimulation, which are essential for a successful prediction. As observed, the model did a good job for genes with higher mean values, while it failed for some genes with a mean expression between 0-1. We also measure accuracy across non-DEGs because the model should not change genes not affected by the perturbation while changing the expression of DEGs.

# %%
# Upstream code cell: 104
r2_value = model.plot_reg_mean_plot(
    eval_adata,
    condition_key="condition",
    axis_keys={"x": "predicted stimulated", "y": "stimulated"},
    gene_list=diff_genes[:10],
    top_100_genes=diff_genes,
    labels={"x": "predicted", "y": "ground truth"},
    show=True,
    legend=False,
)

# %% [markdown]
# We can additionally look at the distribution of the top upregulated genes by IFN-β. For example, we plotted the distribution of expression in `ISG15`, a well-known gene induced after IFN stimulation. As observed, the model identified that this gene should be upregulated after stimulation with IFN-β, and it indeed shifted values to a similar range in ground-truth (stimulated) cells.

# %%
# Upstream code cell: 106
sc.pl.violin(eval_adata, keys="ISG15", groupby="condition")

# %% [markdown]
# Overall, we demonstrated the application of scGen as an example of perturbation response models in predicting gene expression of the unseen population under desired perturbations. While perturbation response models provide in silico predictions, they cannot replace performing actual experiments. It is also unclear how much of the predicted response is attributed to cell type specific responses or across cell types. However, as observed in the case of scGen, it can predict the overall response for highly expressed genes yet provide poorer predictions for lowly expressed genes, which requires further optimization and motivation for developing more sophisticated and robust approaches.

# %% [markdown]
# ## Analysing single-pooled CRISPR screens

# %% [markdown]
# Expanded CRISPR-compatible CITE-seq (ECCITE-seq) enables the capture of single guide RNA (sgRNA) sequences together with transcriptome and surface protein measurements in the form of antibody-derived tags (ADTs). This allows for the application of many genetic perturbations together with transcriptomics readouts for effect exploration and validation of the perturbations through protein expression, making this assay very powerful. However, this power comes not only with great responsibility, but also with complexity.

# %% [markdown]
# :::{figure-md} eccite-seq
# 
# <img src="../_static/images/conditions/eccite.png" alt="ECCITE-seq Overview" class="bg-primary mb-1" width="800px">
# 
# ECCITE-seq overview. {term}`mRNA <Messenger RNA (mRNA)>` is measured together with surface protein expression using antibody derived tags. Biological replicates are resolved through hashtag-derived oligonucleotides. The assignment of the guide RNAs is done using guide-derived oligonucleotides. Image obtained from (https://cite-seq.com/eccite-seq).
# 
# :::

# %% [markdown]
# For the purpose of this analysis we will be using the Papalexi 2021 dataset {cite}`Papalexi2021`. This dataset contains about 20000 stimulated THP-1 cells that used 111 gRNAs. THP-1 cells stimulated with a combination of IFN-y, decitabine (DAC) and transforming growth factor (TGF)-β1 results in an induction of three immune checkpoints: programmed death-ligand 1 (PD-L1), PD-L2 and CD86. The goal of the ECCITE-seq experiment was to investigate molecular networks that regulate PD-L1 expression, because it is frequently observed in human cancers and can suppress T-cell-mediated immune responses {cite}`Papalexi2021`.

# %% [markdown]
# For this specific analysis, we want to:
# 
# 1. Remove confounding sources of variation such as cell cycle effects or batch effects.
# 2. Determine which cells were affected by the desired perturbations and which cells escaped.
# 3. Visualize perturbation responses.

# %% [markdown]
# To conduct this analysis we will again use pertpy which implements the Mixscape pipeline for the scverse ecosystem about 5-10x faster. This pipeline was originally developed for the Seurat ecosystem, and we largely follow the accompanying Seurat Vignette (https://satijalab.org/seurat/articles/mixscape_vignette.html).
# 
# We start by importing pertpy, scanpy and muon, which we will require for the preprocessing of the protein data.

# %%
# Upstream code cell: 114
import muon as mu
import pertpy as pt
import scanpy as sc

# %% [markdown]
# As a first step we fetch the dataset using pertpy. The return type of the dataloader is a MuData object containing the transcriptomics measurements, the ADT measurements and guide RNA counts.

# %%
# Upstream code cell: 116
mdata = pt.dt.papalexi_2021()
mdata

# %% [markdown]
# The original Seurat object contained four assays which were transformed into individual AnnData objects to then create the here downloaded MuData object. The individual modalities are:
# 
# 1. `adt`: A count matrix of the four captured antibody-derived tags (CD86, PDL1, PDL2, CD366) which are also commonly simply referred to as "proteins" in this setting.
# 2. `gdo`: The 111 used guide RNAs (gRNA). To assign a gRNA identity to each cell, guide-derived oligonucleotide (GDO) counts were examined. If a cell had less than five counts for all gRNA sequences, it was classified as negative. For all other cells, the gRNA with the highest number of counts was assigned to that cell. Cells that had high counts for more than one gRNA were classified as doublets.
# 3. `hto`: To keep track of the identity of each biological replicate, the samples were hashed using hashtag-derived oligonucleotides (HTO) following the cell hashing protocol {cite}`Stoeckius2018`.
# 4. `rna`: This corresponds to the transcriptome measurements for all cells and is the usual cells by genes count matrix.

# %% [markdown]
# ### Preprocessing

# %% [markdown]
# We keep the preprocessing of the RNA and ADTs simple. First, we normalize the RNA using scanpy's `normalize_total` followed by log transformation and highly variable gene selection. To normalize the ADTs we apply centered log ration transformation {cite}`Stoeckius2017`.

# %%
# Upstream code cell: 120
sc.pp.normalize_total(mdata["rna"])
sc.pp.log1p(mdata["rna"])
sc.pp.highly_variable_genes(mdata["rna"], subset=True)

# %%
# Upstream code cell: 121
mu.prot.pp.clr(mdata["adt"])

# %% [markdown]
# ### Data exploration

# %% [markdown]
# To get a feeling for our dataset we visualize the replicates, cell-cycle phases and perturbations in a UMAP embedding.

# %%
# Upstream code cell: 124
sc.pp.pca(mdata["rna"])

# %%
# Upstream code cell: 125
# We calculate neighbors with the cosine distance similarly to the original Seurat implementation
sc.pp.neighbors(mdata["rna"], metric="cosine")

# %%
# Upstream code cell: 126
sc.tl.umap(mdata["rna"])

# %%
# Upstream code cell: 127
sc.pl.umap(mdata["rna"], color=["replicate", "Phase", "perturbation"])

# %% [markdown]
# When glancing at the UMAPs we identify two clearly visible issues:
# 
# 1. Many cells are separated by replicate ID. This is a common sign of a batch effect.
# 2. The cell cycle phase is a confounder in the embedding.
# 
# Hence, we now try to project our cells into a perturbation space by calculating local perturbation signatures to mitigate these identified issues.

# %% [markdown]
# ### Calculating local perturbation signatures

# %% [markdown]
# To alleviate the aforementioned issues, we will calculate local perturbation signatures. The core idea is that by subtracting the averaged expression of the `k` nearest cells from the control pool (=NT) from every cell, we retrieve the component of every cell that solely reflects the genetic perturbation. The `k` nearest neighbors must be in a biological state matching the target cell, but are not allowed to have been targeted by any gRNA. The obtained component is denoted as the local perturbation signature. By default, the number of neighbors `k` is set to 20. Following the recommendations of Papalexi et al., we recommend setting from the range of 20 < `k` 30. A `k` that is too small or too large is unlikely to remove any technical variation from the dataset {cite}`Papalexi2021`.
# 
# We now create a Mixscape object using pertpy and calculate the perturbation signature.

# %%
# Upstream code cell: 131
ms = pt.tl.Mixscape()

ms.perturbation_signature(
    mdata["rna"],
    pert_key="perturbation",
    control="NT",
    split_by="replicate",
    n_neighbors=20,
)

# %%
# Upstream code cell: 132
# We create a copy of the object to recalculate the PCA.
# Alternatively we could replace the X of the RNA part of our MuData object with the `X_pert` layer.
adata_pert = mdata["rna"].copy()
adata_pert.X = adata_pert.layers["X_pert"]
sc.pp.pca(adata_pert)
sc.pp.neighbors(adata_pert, metric="cosine")
sc.tl.umap(adata_pert)
sc.pl.umap(adata_pert, color=["replicate", "Phase", "perturbation"])

# %% [markdown]
# Using the perturbation signature to calculate the neighbors graph and the eventual embedding removes technical variation and reveals one additional perturbation-specific cluster. Now that our data is mostly free of confounding effects, we need to determine for which targeted cells (=perturbed) the perturbation was successful (=KO) or not (=NP).

# %% [markdown]
# ### Identifying cells with no detectable perturbation

# %% [markdown]
# The primary assumption that we make is that every target gene class is a mixture of two Gaussian distributions. One of these represents the successful knockouts (KO) and the other the non-perturbed (NP) cells. The distribution of the NP cells should then be identical to the cells expressing non-targeting gRNAs (NT). After having estimated the distribution of the KO cells, Mixscape calculates the posterior probability that a cell belongs to the KO distribution and classifies cells with a probability of more than 0.5 as KOs. Applying this to all 11 target gene classes allows us to identify all KO cells while evaluating the targeting efficacy of the different gRNAs.

# %%
# Upstream code cell: 136
ms.mixscape(adata=mdata["rna"], control="NT", labels="gene_target", layer="X_pert")

# %% [markdown]
# We can now plot the class distributions for all 111 gRNAs.

# %%
# Upstream code cell: 138
ms.plot_barplot(mdata["rna"], guide_rna_column="guide_ID")

# %% [markdown]
# We detect variation in gRNA targeting efficiency within each class. For example gRNA 4 for STAT1 did not seem to be very effective, but gRNA 1-3 were.

# %% [markdown]
# Let's inspect the perturbation scores of an example target gene (IFNGR2).

# %%
# Upstream code cell: 141
ms.plot_perturbscore(
    adata=mdata["rna"], labels="gene_target", target_gene="IFNGR2", color="orange"
)

# %% [markdown]
# As expected, the distributions of the NT and IFNGR2 NP classes match rather well, whereas the IFGNR2 KO distribution is clearly shifted. This should also be reflected in the posterior probabilities.

# %%
# Upstream code cell: 143
sc.settings.set_figure_params(figsize=(10, 10))
ms.plot_violin(
    adata=mdata["rna"],
    target_gene_idents=["NT", "IFNGR2 NP", "IFNGR2 KO"],
    groupby="mixscape_class",
)

# %% [markdown]
# The posterior probabilities clearly separate the two classes highlighting very few unclear cases. This can be further highlighted by running a simple DE test between the mixscape classes and visualizing the results on a heatmap by ordering the posterior probabilities.

# %%
# Upstream code cell: 145
ms.plot_heatmap(
    adata=mdata["rna"],
    labels="gene_target",
    target_gene="IFNGR2",
    layer="X_pert",
    control="NT",
)

# %% [markdown]
# Up to this point we have only been working with the transcriptomics data, but we can now leverage the measured proteins to demonstrate that only IFGN pathway KO cells have a reduction in PDL1 expression.

# %%
# Upstream code cell: 147
mdata["adt"].obs["mixscape_class_global"] = mdata["rna"].obs["mixscape_class_global"]
ms.plot_violin(
    adata=mdata["adt"],
    target_gene_idents=["NT", "JAK2", "STAT1", "IFNGR1", "IFNGR2", "IRF1"],
    keys="PDL1",
    groupby="gene_target",
    hue="mixscape_class_global",
)

# %% [markdown]
# (conditions-perturbation-modeling-key-takeaway-3)=
# ### Visualizing perturbation responses with Linear Discriminant Analysis

# %% [markdown]
# The final step in the Mixscape pipeline is to calculate and visualize perturbation-specific clusters. This is done by applying linear discriminant analysis (LDA) and recalculating the UMAP using the determined results. LDA attempts to maximize the separability of known labels, which are the mixscape classes in our case, using both gene expression and the labels.

# %%
# Upstream code cell: 150
ms.lda(adata=mdata["rna"], control="NT", labels="gene_target", layer="X_pert")

# %%
# Upstream code cell: 151
ms.plot_lda(adata=mdata["rna"], control="NT")

# %% [markdown]
# The LDA highlights at least two major types of perturbations as evident by the two islands. However, we want to emphasize that only more stringent analyses, such as pathway analysis followed by biological validation, could determine that several knockouts have similar effects.

# %% [markdown]
# ## Quiz

# %%
# Upstream code cell: 154
%run ../src/lib.py

flip_card(
    "q1",
    "Why is it required to have confident cell type labels when applying Augur?",
    "Confident cell type labels are essential when applying Augur because it prioritizes cell types based on their molecular response to perturbations; inaccurate labels can mislead the analysis.",
    back_font_size=15,
)
flip_card(
    "q2",
    "Why should scGen primarily only be applied to highly expressed genes?",
    "scGen should primarily be applied to highly expressed genes, as predicting perturbation responses for lowly expressed genes is challenging due to increased noise and variability.",
    back_font_size=15,
)
flip_card(
    "q3",
    "The mixscape pipeline results in clusters of genetic perturbations. Why must the distances in the UMAPs be interpreted with caution? What does it mean when ome genetic perturbations are close or distant in the UMAP embedding?",
    "In the Mixscape pipeline, distances in UMAP embeddings should be interpreted with caution because they primarily aid visualization; proximity or distance between genetic perturbations in UMAP space doesn't necessarily reflect true biological similarities or differences.",
    front_font_size=15,
    back_font_size=13,
)

# %% [markdown]
# ## References

# %% [markdown]
# ```{bibliography}
# :filter: docname in docnames
# :labelprefix: pemo
# ```

# %% [markdown]
# ## Contributors
# 
# We gratefully acknowledge the contributions of:
# 
# ### Authors
# 
# * Lukas Heumos
# * Mohammad Lotfollahi
# 
# ### Reviewers
# 
# * Yuge Ji
